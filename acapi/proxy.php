<?php
/**
 * AllCoaching checkout proxy — /acapi/proxy.php?p=<endpoint>
 *
 * Why it exists: the educator API (allcoaching-admin.b-cdn.net) only allows
 * browser calls from studio.allcoaching.in (CORS). The checkout on our landing
 * pages runs on allcoaching.in, so it calls this same-origin file and the
 * request is forwarded server-to-server, where CORS does not apply.
 *
 * Safety rules:
 *  - Only the endpoints the signup/checkout flow needs are forwarded (ALLOW).
 *  - Only requests coming from our own pages are accepted (origin check).
 *  - OTP sends and verifies are rate-limited per visitor IP here, because
 *    upstream now sees every visitor as this server's IP.
 *  - The visitor's IP is passed on in X-Forwarded-For / X-Real-IP.
 *  - The auth token arrives in X-AC-Token (some Hostinger PHP setups strip
 *    the Authorization header) and is sent upstream as "Token <key>".
 *  - Nothing is logged or stored except the rate-limit counters.
 *
 * When the API allows https://allcoaching.in in CORS, set API_DIRECT in
 * /assets/checkout.js and this file is no longer used.
 */

const UPSTREAM = 'https://allcoaching-admin.b-cdn.net/v1/educator/';

// endpoint => [upstream method, body type]
const ALLOW = [
    'login/onboarding/pricing'      => ['GET',   'none'],
    'login/'                        => ['POST',  'json'],
    'login/verify'                  => ['POST',  'json'],
    'login/update'                  => ['PATCH', 'multipart'],
    'login/onboarding/claim'        => ['POST',  'json'],
    'login/onboarding/trial'        => ['POST',  'json'],
    'login/onboarding/coupon/check' => ['POST',  'json'],
    'login/onboarding/pay/checkout' => ['POST',  'json'],
    'login/onboarding/pay/verify'   => ['POST',  'json'],
    // An existing studio (trial running, or upgrading) buys through studio's own
    // Settings ▸ Plan endpoints. All three need the educator's token.
    'institute/usage/'              => ['GET',   'none'],
    'institute/plan/checkout/'      => ['POST',  'json'],
    'institute/plan/verify/'        => ['POST',  'json'],
];

// Profile fields the landing checkout may write (sent upstream as multipart,
// the same wire format studio uses for /login/update).
const PROFILE_FIELDS = ['director_name', 'name', 'vertical', 'referral_code', 'attribution'];

// Per-IP limits: endpoint => [max requests, window seconds]. Generous on purpose: Jio and
// Airtel put many phones behind one IP (CGNAT), and the API keeps its own per-number limits.
// These only stop one source from burning the limits every real educator shares.
const LIMITS = [
    'login/'       => [20, 900],
    'login/verify' => [40, 900],
];

const ALLOWED_HOSTS = ['allcoaching.in', 'www.allcoaching.in', 'localhost', '127.0.0.1'];

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store, private');
header('X-Robots-Tag: noindex');
header('X-Content-Type-Options: nosniff');

function out(int $code, string $message): void {
    http_response_code($code);
    echo json_encode(['status' => 'false', 'message' => $message]);
    exit;
}

function client_ip(): string {
    foreach (['HTTP_CF_CONNECTING_IP', 'HTTP_X_REAL_IP', 'HTTP_X_FORWARDED_FOR'] as $h) {
        if (!empty($_SERVER[$h])) {
            $ip = trim(explode(',', $_SERVER[$h])[0]);
            if (filter_var($ip, FILTER_VALIDATE_IP)) return $ip;
        }
    }
    return $_SERVER['REMOTE_ADDR'] ?? '0.0.0.0';
}

function host_of(?string $url): string {
    if (!$url) return '';
    $h = parse_url($url, PHP_URL_HOST);
    return is_string($h) ? strtolower($h) : '';
}

function rate_limited(string $endpoint, string $ip): bool {
    if (!isset(LIMITS[$endpoint])) return false;
    [$max, $win] = LIMITS[$endpoint];
    $file = sys_get_temp_dir() . '/acapi_' . md5($endpoint . '|' . $ip);
    $now = time();
    $hits = [];
    $fh = @fopen($file, 'c+');
    if (!$fh) return false; // fail open: never block a real educator on a disk error
    flock($fh, LOCK_EX);
    $raw = stream_get_contents($fh);
    if ($raw) {
        foreach (explode(',', $raw) as $t) {
            if ((int)$t > $now - $win) $hits[] = (int)$t;
        }
    }
    $blocked = count($hits) >= $max;
    if (!$blocked) $hits[] = $now;
    ftruncate($fh, 0);
    rewind($fh);
    fwrite($fh, implode(',', $hits));
    flock($fh, LOCK_UN);
    fclose($fh);
    return $blocked;
}

// ── request checks ─────────────────────────────────────────────────────────
$endpoint = isset($_GET['p']) ? (string)$_GET['p'] : '';
if (!isset(ALLOW[$endpoint])) out(404, 'Not found.');
[$method, $bodyType] = ALLOW[$endpoint];

$incoming = $_SERVER['REQUEST_METHOD'] ?? 'GET';
if ($incoming === 'OPTIONS') { http_response_code(204); exit; }
if ($method === 'GET' && $incoming !== 'GET') out(405, 'Method not allowed.');
if ($method !== 'GET' && $incoming !== 'POST') out(405, 'Method not allowed.');

// Only our own pages may use this. Browsers always send Origin on POST;
// a GET from our page carries Referer.
$origin = host_of($_SERVER['HTTP_ORIGIN'] ?? null) ?: host_of($_SERVER['HTTP_REFERER'] ?? null);
if (!in_array($origin, ALLOWED_HOSTS, true)) out(403, 'Forbidden.');

$ip = client_ip();
if (rate_limited($endpoint, $ip)) {
    out(429, $endpoint === 'login/'
        ? 'Too many codes requested. Please wait a few minutes and try again.'
        : 'Too many attempts. Please wait a few minutes and try again.');
}

// ── build the upstream request ─────────────────────────────────────────────
$headers = [
    'Accept: application/json',
    'X-Forwarded-For: ' . $ip,
    'X-Real-IP: ' . $ip,
    'X-AC-Proxy: landing',
];
$token = $_SERVER['HTTP_X_AC_TOKEN'] ?? '';
if ($token !== '') {
    // Session keys are base64url (letters, digits, - and _), 43 characters today.
    if (!preg_match('/^[A-Za-z0-9_.\-]{20,256}$/', $token)) out(400, 'Bad session. Please start again.');
    $headers[] = 'Authorization: Token ' . $token;
}

$ch = curl_init(UPSTREAM . $endpoint);
$opts = [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HEADER         => false,
    CURLOPT_CONNECTTIMEOUT => 8,
    CURLOPT_TIMEOUT        => 25,
    CURLOPT_USERAGENT      => substr($_SERVER['HTTP_USER_AGENT'] ?? 'AllCoaching-Landing', 0, 300),
    CURLOPT_CUSTOMREQUEST  => $method,
];

if ($method !== 'GET') {
    $raw = file_get_contents('php://input', false, null, 0, 20000);
    $data = $raw === '' || $raw === false ? [] : json_decode($raw, true);
    if (!is_array($data)) out(400, 'Bad request.');

    if ($bodyType === 'multipart') {
        $form = [];
        foreach (PROFILE_FIELDS as $k) {
            if (!array_key_exists($k, $data) || $data[$k] === null || $data[$k] === '') continue;
            $v = $data[$k];
            $form[$k] = is_array($v) ? json_encode($v) : substr((string)$v, 0, 2000);
        }
        if (!$form) out(400, 'Nothing to save.');
        $opts[CURLOPT_POSTFIELDS] = $form; // array → multipart/form-data
    } else {
        $headers[] = 'Content-Type: application/json';
        $opts[CURLOPT_POSTFIELDS] = json_encode((object)$data);
    }
}
$opts[CURLOPT_HTTPHEADER] = $headers;
curl_setopt_array($ch, $opts);

$body = curl_exec($ch);
$code = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err  = curl_error($ch);
curl_close($ch);

if ($body === false || $code === 0) {
    error_log('acapi upstream error on ' . $endpoint . ': ' . $err);
    out(502, 'Could not reach AllCoaching right now. Please try again.');
}

http_response_code($code);
// Upstream always answers JSON for these endpoints; anything else (an HTML
// error page) is wrapped so the browser never has to parse HTML.
$trim = ltrim($body);
if ($trim === '' || ($trim[0] !== '{' && $trim[0] !== '[')) {
    echo json_encode(['status' => 'false', 'message' => 'Something went wrong. Please try again.']);
    exit;
}
echo $body;
