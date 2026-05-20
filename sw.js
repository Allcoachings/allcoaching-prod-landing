/* AllCoaching — Service Worker
 * Strategy:
 *   - Static assets (images, css, fonts): cache-first with background revalidation
 *   - HTML navigations: network-first, fall back to cached shell when offline
 *   - Cross-origin (CDNs, fonts): stale-while-revalidate
 * Bump CACHE_VERSION on every deploy to invalidate old caches.
 */

const CACHE_VERSION = 'v2026.05.20.5';
const STATIC_CACHE  = `ac-static-${CACHE_VERSION}`;
const RUNTIME_CACHE = `ac-runtime-${CACHE_VERSION}`;
const HTML_CACHE    = `ac-html-${CACHE_VERSION}`;

const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/manifesto.html',
  '/about.html',
  '/contact.html',
  '/privacy.html',
  '/terms.html',
  '/404.html',
  '/styles.css',
  '/dist/tw.min.css',
  '/manifest.webmanifest',
  '/assets/AllCoaching-logo.webp',
  '/assets/Amit-Ratan.webp',
  '/assets/fevicon.webp'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then((cache) => cache.addAll(PRECACHE_URLS).catch(() => {}))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => ![STATIC_CACHE, RUNTIME_CACHE, HTML_CACHE].includes(k))
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

// Allow page to trigger immediate activation after deploy
self.addEventListener('message', (event) => {
  if (event.data === 'SKIP_WAITING') self.skipWaiting();
});

function isHTMLRequest(req) {
  return req.mode === 'navigate' ||
         (req.method === 'GET' && req.headers.get('accept')?.includes('text/html'));
}

function isStaticAsset(url) {
  return /\.(?:css|js|png|jpg|jpeg|webp|avif|svg|gif|ico|woff2?|ttf|otf)$/i.test(url.pathname);
}

// CSS and JS change frequently — never serve stale.
// Images/fonts are immutable per deploy — cache-first is fine.
function isCodeAsset(url) {
  return /\.(?:css|js)$/i.test(url.pathname);
}

self.addEventListener('fetch', (event) => {
  const { request } = event;

  // Only handle GET; never intercept analytics, GTM, or POSTs
  if (request.method !== 'GET') return;

  const url = new URL(request.url);

  // Bypass cache for analytics / tag managers / API
  if (
    url.hostname.includes('googletagmanager.com') ||
    url.hostname.includes('google-analytics.com') ||
    url.hostname.includes('analytics.google.com') ||
    url.pathname.startsWith('/api/')
  ) return;

  // HTML navigations — network-first
  if (isHTMLRequest(request)) {
    event.respondWith(networkFirst(request, HTML_CACHE));
    return;
  }

  // Same-origin CSS/JS — network-first (so brand.css edits are visible immediately)
  if (url.origin === self.location.origin && isCodeAsset(url)) {
    event.respondWith(networkFirst(request, STATIC_CACHE));
    return;
  }

  // Same-origin images/fonts — cache-first (immutable per deploy)
  if (url.origin === self.location.origin && isStaticAsset(url)) {
    event.respondWith(cacheFirst(request, STATIC_CACHE));
    return;
  }

  // Cross-origin (fonts, CDNs) — stale-while-revalidate
  if (url.origin !== self.location.origin) {
    event.respondWith(staleWhileRevalidate(request, RUNTIME_CACHE));
    return;
  }

  // Default: try network, fall back to cache
  event.respondWith(
    fetch(request).catch(() => caches.match(request))
  );
});

async function networkFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  try {
    const fresh = await fetch(request);
    if (fresh && fresh.ok) cache.put(request, fresh.clone());
    return fresh;
  } catch (_) {
    const cached = await cache.match(request);
    if (cached) return cached;
    // Last resort: cached home shell
    const shell = await caches.match('/index.html') || await caches.match('/');
    return shell || Response.error();
  }
}

async function cacheFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) {
    // Background revalidate
    fetch(request).then((res) => {
      if (res && res.ok) cache.put(request, res.clone());
    }).catch(() => {});
    return cached;
  }
  try {
    const fresh = await fetch(request);
    if (fresh && fresh.ok) cache.put(request, fresh.clone());
    return fresh;
  } catch (_) {
    return cached || Response.error();
  }
}

async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  const network = fetch(request).then((res) => {
    if (res && res.ok) cache.put(request, res.clone());
    return res;
  }).catch(() => null);
  return cached || (await network) || Response.error();
}
