/* AllCoaching demo — handwritten hover hints. One file, shared by the hub, the Studio and the student app. */
(function () {
  'use strict';
  if (window.__acGuide) return;
  window.__acGuide = true;

  var script = document.currentScript || document.querySelector('script[data-product]');
  var product = (script && script.getAttribute('data-product')) || 'hub';
  var KEY = 'ac-demo-hints';
  var enabled = true;
  try { enabled = localStorage.getItem(KEY) !== 'off'; } catch (e) {}
  var SHOT = /[?&]shot=1/.test(location.search);
  if (SHOT) { document.documentElement.classList.add('shot'); enabled = false; }
  var BASE = script && script.src ? new URL('.', script.src).href : '/';

  if (!document.querySelector('link[href*="family=Caveat"]')) {
    var font = document.createElement('link');
    font.rel = 'stylesheet';
    font.href = 'https://fonts.googleapis.com/css2?family=Caveat:wght@600&display=swap';
    document.head.appendChild(font);
  }

  var css = document.createElement('style');
  css.textContent =
    '.acg-tip{position:fixed;left:0;top:0;z-index:2147483600;pointer-events:none;box-sizing:border-box;max-width:min(230px,calc(100vw - 20px));' +
    'font-family:"Caveat","Segoe Print","Bradley Hand","Comic Sans MS",cursive;font-weight:600;font-size:17px;line-height:1.08;letter-spacing:.1px;' +
    'font-style:normal;text-transform:none;text-align:left;white-space:normal;overflow-wrap:break-word;color:#15110D;' +
    'background:#FFFDF6;border:1.25px solid #15110D;border-radius:13px 15px 11px 16px/15px 11px 16px 13px;padding:3px 10px 5px;' +
    'box-shadow:1.5px 1.5px 0 #15110D;opacity:0;transform:translateY(5px) rotate(var(--acg-r,-1deg)) scale(.9);' +
    'transition:opacity .12s ease,transform .24s cubic-bezier(.34,1.56,.64,1)}' +
    '.acg-tip.acg-on{opacity:1;transform:translateY(0) rotate(var(--acg-r,-1deg)) scale(1)}' +
    '.acg-tip::after{content:"";position:absolute;left:var(--acg-ax,50%);width:8px;height:8px;background:#FFFDF6;border:1.25px solid #15110D;transform:translateX(-50%) rotate(45deg)}' +
    '.acg-tip[data-side="top"]::after{bottom:-5.5px;border-top:0;border-left:0}' +
    '.acg-tip[data-side="bottom"]::after{top:-5.5px;border-bottom:0;border-right:0}' +
    '@media (prefers-reduced-motion:reduce){.acg-tip{transition:opacity .01s}}';
  document.head.appendChild(css);

  var tip = document.createElement('div');
  tip.className = 'acg-tip';
  tip.setAttribute('role', 'tooltip');
  tip.setAttribute('aria-hidden', 'true');

  /* ─── what each control does ───────────────────────────────────────────── */
  var NUMERIC = /^[\s₹$\d,.:+%·\-–—/()]*$|^\d+\s?(p|g|m|h|s|min|hrs?)$/i;

  var STUDIO = [
    [/^dashboard$/, 'Your academy at a glance — sales, students, next steps'],
    [/^transactions$|all transactions/, 'Every payment and payout, line by line'],
    [/^content$/, 'All your videos, PDFs and tests in one library'],
    [/^videos$/, 'Recorded lectures — upload once, use in any course'],
    [/^pdfs$/, 'Notes and DPPs students read inside the app'],
    [/^test series$/, 'Tests with timers and instant results'],
    [/^courses$/, 'Package your content into courses and set a price'],
    [/^free content$/, 'Free lessons that bring new students to you'],
    [/^live$/, 'Live classes — every one is recorded for you'],
    [/^community$/, 'Comments, reviews and followers in one place'],
    [/^discounts?$/, 'Coupon codes to fill a batch faster'],
    [/^analytics$/, 'What sells, what gets watched, where students drop'],
    [/^website$/, 'Your academy website — free address included'],
    [/^notifications$/, 'Enrolments, payments and doubts land here'],
    [/^referrals$/, 'Invite other educators and earn rewards'],
    [/^settings$/, 'Profile, payouts, branding and team'],
    [/toggle sidebar|collapse|expand menu/, 'Show or hide the menu'],
    [/upload video/, 'Upload a recorded lecture into a course'],
    [/whatsapp/, 'Talk to a real person at AllCoaching'],
    [/toggle theme|dark mode|light mode/, 'Dark mode for late-night teaching'],
    [/start a live class|^go live$/, 'Start a live class — students get notified'],
    [/educator profile|profile · settings/, 'Your profile and account settings'],
    [/^search/, 'Find any student, course or payment'],
    [/^start a class$|new class/, 'Set up a new live class'],
    [/^plans?$|see plans|compare plans/, 'Live hours and seats in each plan'],
    [/create and go live/, 'Creates the class and opens your studio'],
    [/schedule class/, 'Books the class — students see it in their app'],
    [/^this computer$/, 'Teach from this laptop — camera and screen'],
    [/^my phone$/, 'Use your phone as the camera — just scan a QR'],
    [/obs|encoder/, 'Pro setup — stream from OBS with a stream key'],
    [/^everyone$/, 'Anyone who follows your academy can join'],
    [/^one course$/, 'Only students of one course can join'],
    [/^start now$/, 'Go live right after setup'],
    [/^later$/, 'Pick a date and time for the class'],
    [/^cancel$/, 'Close without saving'],
    [/^restart$/, 'Reconnect your camera and mic'],
    [/full ?screen/, 'Fill the screen with the preview'],
    [/camera only/, 'Students see only you'],
    [/screen only/, 'Students see only your screen'],
    [/screen.*camera/, 'Your screen, with you in the corner'],
    [/refresh devices/, 'New mic or camera plugged in? Refresh'],
    [/try again/, 'Ask the browser for camera access again'],
    [/^show( key)?$|^hide( key)?$/, 'Reveals the stream key — keep it private'],
    [/simulate/, 'Demo only — pretends the stream is connected'],
    [/end class/, 'Ends the class and saves the recording'],
    [/back to classes/, 'Back to all your live classes'],
    [/set up autopay|upgrade/, 'Change plan — demo checkout, nothing is charged'],
    [/switch to free/, 'Move back to the free plan'],
    [/your plan|current plan/, 'The plan you are on right now'],
    [/move to bin|delete/, 'Goes to the bin first — you can restore it'],
    [/^restore$/, 'Bring it back from the bin'],
    [/^pin$|^unpin$/, 'Keep this at the top of the list'],
    [/reset demo/, 'Clears your changes in this demo'],
    [/^grid$|^list$|grid view|list view/, 'Change how the list looks'],
    [/unlock|^pay\b|checkout/, 'Demo checkout — no money moves'],
    [/add a custom domain|add your own domain/, 'Connect a domain you already own — nothing is charged in the demo'],
    [/^connect/, 'Link a domain name you already own'],
    [/check now|verify dns/, 'Checks whether your DNS records are live'],
    [/^remove$/, 'Disconnect this domain'],
    [/^preview$/, 'See your website before students do'],
    [/open my site/, 'Opens your website'],
    [/view as student/, 'Your site exactly as a student sees it'],
    [/^desktop$/, 'Laptop view'],
    [/^mobile$/, 'Phone view'],
    [/^close$|^done$/, 'Close this'],
    [/sign in|send otp|verify|get otp/, 'Student login by OTP — demo code 123456'],
    [/export|download csv/, 'Download as a spreadsheet'],
    [/create code|new code|new coupon/, 'Make a new coupon code'],
    [/create course|new course/, 'Start a new course'],
    [/^duplicate$/, 'Copy this as a starting point'],
    [/save as draft/, 'Saved, but not visible to students yet'],
    [/publish/, 'Make it visible to students'],
    [/view public page/, 'The page students land on'],
    [/^share$/, 'Share a link on WhatsApp or anywhere'],
    [/^reply$/, 'Answer your student right here'],
    [/view all|see all/, 'See the full list'],
    [/mark all( as)? read/, 'Clear all unread dots'],
    [/^copy|copy link/, 'Copies it to your clipboard'],
    [/^edit/, 'Make changes'],
    [/save/, 'Saves your changes — in this demo, only in your browser'],
    [/filter/, 'Narrow the list down'],
    [/invite/, 'Invite someone with a link'],
    [/refund/, 'Refunds go back to the student'],
    [/payout|bank/, 'Your earnings, paid to your bank daily'],
    [/upload|add file/, 'Add files from your device'],
    [/^next$|^previous$|^prev$|›|‹/, 'Next or previous page'],
    [/^(all|paid|pending|refunded|failed|active|scheduled|expired|draft|published|comments|reviews|followers|engagement|funnel|overview)\b/, 'Switch what the list shows'],
    [/^help$/, 'Guides and answers to common questions'],
    [/add content/, 'Upload videos, PDFs or a new test'],
    [/open studio/, 'Opens the live studio for this class'],
    [/manage courses/, 'All your courses in one list'],
    [/^calendar$/, 'Your classes on a calendar'],
    [/schedule new|^schedule$/, 'Publish it later, automatically'],
    [/bulk import/, 'Upload many videos at once'],
    [/build test/, 'Create a test with questions and a timer'],
    [/preview app feed/, 'See free content the way students do'],
    [/import/, 'Reuse something you already uploaded'],
    [/^playlists$/, 'Group free lessons into playlists'],
    [/open inbox/, 'Every unread message in one place'],
    [/new post|^post$/, 'Post an update to your followers'],
    [/^(text|image \/ notes|short|poll|quiz|new lecture)$/, 'Pick what kind of post to make'],
    [/ai · improve|improve/, 'Tidy up your post with AI'],
    [/ai summary/, 'Your numbers, explained in plain words'],
    [/^use$/, 'Turn this idea into a coupon'],
    [/^skip$/, 'Hide this suggestion'],
    [/^preferences$/, 'Choose what you get notified about'],
    [/send notification/, "Send a message to your students' phones"],
    [/star this/, 'Star it to find it later'],
    [/^view |^explore$|^manage/, 'Opens it'],
    [/^(email|x \/ twitter|embed|whatsapp)$/, 'Share your referral link'],
    [/\?$/, 'Tap to see the answer'],
    [/^billing$/, 'Your plan and invoices'],
    [/user & roles|team/, 'Add teachers and staff with their own login'],
    [/^payment$/, 'Where your payouts go'],
    [/^notification$/, 'Which alerts you receive'],
    [/^account$/, 'Login, phone and security'],
    [/change cover/, 'Change your profile banner'],
    [/^discard$/, 'Throw away unsaved changes'],
    [/^(posts|doubts|drafts|pinned|inbox|sent|unread|read|students|payments|system|audience|content)\b/, 'Switch what the list shows']
  ];
  var STUDIO_PRE = [
    [/^(7d|30d|90d|12m|1y|all time)$/i, 'Change the date range'],
    [/^dislike$/i, 'Reactions from your students']
  ];
  var STUDIO_CTX = [
    ['.ck-box,input[type="checkbox"]', 'Select rows for bulk actions'],
    ['.pill', 'Reactions from your students'],
    ['.lecture-embed', 'Opens the attached lecture'],
    ['.muted-card', 'A suggested campaign — tap Use to try it'],
    ['.nx-star', 'Star it to find it later'],
    ['.nx-avatar,.nx-body', 'Opens this notification'],
    ['.tb-avatar,.rail-me', 'Your profile and account settings'],
    ['.tb-search', 'Find any student, course or payment'],
    ['.rail-brand', 'Back to your dashboard'],
    ['tbody tr', 'Opens the full details'],
    ['.kpi,.kpi-card', 'The number behind your growth'],
    ['.lv-card,.lv-class', 'Open this class'],
    ['.sf-app a,.sf-app button', 'Part of your website — try it like a student']
  ];

  var STUDENT = [
    [/^search/, 'Search classes, courses, tests and notes'],
    [/^live( class)?$/, 'Classes happening right now'],
    [/^home$/, 'The home screen your students open'],
    [/^explore$/, 'Everything the academy teaches'],
    [/^courses$|all courses/, 'Every course, with filters and prices'],
    [/^test series$|^tests$|all tests/, 'Timed tests with instant results'],
    [/^notes|all notes|pdfs/, 'Notes and PDFs to read in the app'],
    [/community/, 'Where students ask and discuss'],
    [/my library/, 'Everything the student has bought'],
    [/^saved$|save for later|^save$/, 'Saved to watch or read later'],
    [/my profile|^you$|edit profile/, "The student's profile and progress"],
    [/book a (counselling )?call|contact us|send enquiry/, 'Enquiries reach you in the studio and on WhatsApp'],
    [/whatsapp/, 'Students message the academy on WhatsApp'],
    [/^install/, 'Adds the app to their home screen — no store needed'],
    [/dismiss|got it/, 'Close this note'],
    [/remind me/, 'Get a reminder before the class starts'],
    [/for you/, 'Picked for what the student is preparing for'],
    [/faculty|full profile|view profile/, 'Your teachers and their profiles'],
    [/join live|^join$/, 'Join the live class'],
    [/^see all|see programmes/, 'See the full list'],
    [/^(jee|neet|jee advanced|olympiad|foundation|boards|all|free|paid|popular|rating|price ↑|price ↓|easy|medium|hard)$/, 'Filter the list'],
    [/open community/, 'Go to the discussion board'],
    [/^share$/, 'Share on WhatsApp or anywhere'],
    [/youtube|instagram|linkedin/, "The academy's social profiles"],
    [/programme/, 'Opens this programme'],
    [/^(call|email)$|^\+91|@allcoaching/, 'Reach the academy directly'],
    [/full name|mobile|@example|select a programme|class, target/, 'Type anything — this form is a sandbox'],
    [/say something/, 'Chat with the class while it is live'],
    [/play or pause|^play$|^pause$/, 'Play or pause'],
    [/back 10|forward 10/, 'Skip 10 seconds'],
    [/^mute$|^unmute$/, 'Sound on or off'],
    [/playback speed/, 'Watch at 1.5x or 2x'],
    [/captions/, 'Subtitles on or off'],
    [/quality/, 'Choose the video quality'],
    [/^like$/, 'Like this class'],
    [/add a comment|^post$/, 'Comment under the class'],
    [/watch again/, 'Replay from the start'],
    [/^(overview|modules|reviews|demo|about|videos)$/, 'Jump to this section'],
    [/enrolled|enrol|buy now|^buy/, 'Enrol and pay — demo checkout'],
    [/start test/, 'Start the test — the timer begins'],
    [/attempt later/, 'Keep it for later'],
    [/zoom|fit to page/, 'Zoom the page'],
    [/^download$/, 'Save for offline reading'],
    [/^print$/, 'Print these notes'],
    [/^close$|^back$/, 'Go back'],
    [/progress|my courses|certificates|following/, "The student's own dashboard"],
    [/^(submit|next|previous|mark for review|clear)/, 'Moves through the test'],
    [/^reply$/, 'Reply to this comment'],
    [/theme|dark/, 'Light or dark mode'],
    [/notification|bell/, 'Class reminders and new uploads'],
    [/menu/, 'Open the menu']
  ];
  var STUDENT_CTX = [
    ['[onclick*="go(\'livewatch\'"]', 'Join the live class'],
    ['[onclick*="go(\'course\'"]', 'Opens the course page — syllabus, demo, enrol'],
    ['[onclick*="go(\'watch\'"]', 'Plays a recorded class'],
    ['[onclick*="go(\'test\'"]', 'A timed test with instant results'],
    ['[onclick*="go(\'pdf\'"]', 'Opens these notes in the reader'],
    ['[onclick*="go(\'post\'"]', 'Opens this community post'],
    ['[onclick*="go(\'educator\'"]', 'The faculty profile page'],
    ['.wafab', 'Students message the academy on WhatsApp'],
    ['.scrim,.pctrl', null],
    ['[onclick*="openNotifs"]', 'Class reminders and new uploads'],
    ['[onclick*="doSearch"]', 'Search classes, courses, tests and notes'],
    ['.brand', 'Back to the home screen'],
    ['[onclick*="go(\'profile\'"]', "The student's profile and progress"],
    ['[onclick*="toggleLike"]', 'Like this post'],
    ['[onclick*="toggleSave"]', 'Save this post for later'],
    ['[onclick*="vote("]', 'Vote — the results show instantly'],
    ['.frow', 'Reach the academy directly'],
    ['[onclick*="Settings opened"]', 'App settings'],
    ['[onclick*="Link copied"]', 'Copy the profile link'],
    ['.bigplay', 'Play the class'],
    ['[onclick*="sendChat"]', 'Send your message to the class'],
    ['.pbar,[onclick*="seek("]', 'Jump to any point in the class'],
    ['[onclick*="toggleFS"]', 'Watch full screen'],
    ['[onclick*="jump("]', 'Jump to this chapter of the class'],
    ['.player', 'Tap the video to show the controls'],
    ['[onclick*="pdfNav"]', 'Previous or next page'],
    ['[onclick*="pdfGo"]', 'Go to this chapter of the notes'],
    ['.iconbtn', 'Open the menu'],
    ['.avatar', 'Profile photo and account']
  ];

  var FALLBACK = [
    function (l) { return l + ' — click and see what happens'; },
    function (l) { return 'Try “' + l + '” — it is a safe demo'; },
    function (l) { return l + ' — go ahead, nothing breaks here'; }
  ];

  var isStudent = product === 'website' || product === 'app' || product === 'student';
  var RULES = product === 'studio' ? STUDIO : isStudent ? STUDENT : [];
  var CTX = product === 'studio' ? STUDIO_CTX : isStudent ? STUDENT_CTX : [];
  var PRE = product === 'studio' ? STUDIO_PRE : [];
  var GENERIC = product !== 'hub';

  var INTERACTIVE = 'button,a[href],[role="button"],[role="tab"],[role="menuitem"],[role="switch"],[role="checkbox"],[role="radio"],' +
    'input:not([type="hidden"]),select,textarea,summary,[onclick],[data-tip]';

  var hash = function (s) { var h = 0; for (var i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0; return Math.abs(h); };

  var findTarget = function (node) {
    if (!node || node.nodeType !== 1 || node === tip) return null;
    if (node.closest('[data-tip-off]')) return null;
    var hit = node.closest(INTERACTIVE);
    if (hit) return hit;
    if (!GENERIC) return null;
    var el = node;
    for (var i = 0; el && i < 5 && el !== document.body; i++, el = el.parentElement) {
      if (getComputedStyle(el).cursor === 'pointer') return el;
    }
    return null;
  };

  var labelOf = function (el) {
    var l = el.getAttribute('aria-label') || el.getAttribute('title') || el.getAttribute('data-acg-title') || '';
    var tag = el.tagName;
    if (!l && (tag === 'INPUT' || tag === 'TEXTAREA')) l = el.getAttribute('placeholder') || (el.labels && el.labels[0] && el.labels[0].innerText) || el.value || '';
    if (!l && tag === 'SELECT') l = (el.labels && el.labels[0] && el.labels[0].innerText) || (el.options[0] && el.options[0].text) || '';
    if (!l) l = (el.innerText || '').trim().split('\n')[0];
    if (!l) l = (el.textContent || '').trim();
    return l.replace(/\s+/g, ' ').trim();
  };

  var textFor = function (el) {
    var own = el.getAttribute('data-tip');
    if (own !== null) return own || null;
    if (!GENERIC) return null;
    var label = labelOf(el);
    var low = label.toLowerCase();
    var usable = label && !NUMERIC.test(label);
    for (var p = 0; p < PRE.length; p++) if (PRE[p][0].test(label)) return PRE[p][1];
    if (usable) {
      for (var i = 0; i < RULES.length; i++) if (RULES[i][0].test(low)) return RULES[i][1];
    }
    for (var j = 0; j < CTX.length; j++) {
      try { if (el.matches(CTX[j][0]) || el.closest(CTX[j][0])) return CTX[j][1]; } catch (e) {}
    }
    var tag = el.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA') return 'Type anything — it is a sandbox';
    if (tag === 'SELECT') return 'Pick an option — nothing is saved';
    if (!usable || label.length < 2) return 'Try it — this is a safe demo';
    var short = label.length > 26 ? label.slice(0, 24).trim() + '…' : label;
    return FALLBACK[hash(label) % FALLBACK.length](short);
  };

  window.__acGuideText = function (el) { var t = findTarget(el); return t ? textFor(t) : null; };

  var current = null, timer = null, hideTimer = null, px = 0, py = 0;

  var restoreTitle = function (el) {
    if (el && el.hasAttribute('data-acg-title')) {
      el.setAttribute('title', el.getAttribute('data-acg-title'));
      el.removeAttribute('data-acg-title');
    }
  };

  var place = function (el, usePointer) {
    var r = el.getBoundingClientRect();
    var vw = document.documentElement.clientWidth, vh = window.innerHeight;
    var tw = tip.offsetWidth, th = tip.offsetHeight;
    var anchorX = usePointer ? px : r.left + r.width / 2;
    var topY = usePointer ? py - 14 : r.top;
    var bottomY = usePointer ? py + 18 : r.bottom;
    var side = topY - th - 9 >= 6 ? 'top' : 'bottom';
    var y = side === 'top' ? topY - th - 9 : Math.min(bottomY + 9, vh - th - 6);
    var x = Math.max(8, Math.min(anchorX - tw / 2, vw - tw - 8));
    tip.setAttribute('data-side', side);
    tip.style.setProperty('--acg-ax', Math.max(12, Math.min(anchorX - x, tw - 12)) + 'px');
    tip.style.left = Math.round(x) + 'px';
    tip.style.top = Math.round(y) + 'px';
  };

  var show = function (el, fromTouch) {
    if (!enabled) return;
    var text = textFor(el);
    if (!text) return;
    clearTimeout(hideTimer);
    if (!tip.parentNode) document.body.appendChild(tip);
    if (current && current !== el) restoreTitle(current);
    current = el;
    if (el.hasAttribute('title')) { el.setAttribute('data-acg-title', el.getAttribute('title')); el.removeAttribute('title'); }
    tip.textContent = text;
    tip.style.setProperty('--acg-r', ((hash(text) % 5) * 0.6 - 1.6).toFixed(1) + 'deg');
    tip.classList.remove('acg-on');
    var r = el.getBoundingClientRect();
    place(el, !fromTouch && (r.height > 110 || r.width > 420));
    requestAnimationFrame(function () { tip.classList.add('acg-on'); });
    if (fromTouch) hideTimer = setTimeout(hide, 1900);
  };

  var hide = function () {
    clearTimeout(timer);
    tip.classList.remove('acg-on');
    restoreTitle(current);
    current = null;
  };

  document.addEventListener('pointerover', function (e) {
    if (e.pointerType === 'touch') return;
    var el = findTarget(e.target);
    if (el === current) return;
    clearTimeout(timer);
    if (!el) { hide(); return; }
    px = e.clientX; py = e.clientY;
    timer = setTimeout(function () { show(el, false); }, current ? 60 : 260);
  }, true);

  document.addEventListener('pointermove', function (e) { px = e.clientX; py = e.clientY; }, { passive: true, capture: true });

  document.addEventListener('pointerout', function (e) {
    if (e.pointerType === 'touch' || !current) return;
    var to = e.relatedTarget;
    if (!to || !current.contains(to)) { if (findTarget(to) !== current) hide(); }
  }, true);

  document.addEventListener('pointerdown', function (e) {
    if (e.pointerType !== 'touch') { clearTimeout(timer); return; }
    var el = findTarget(e.target);
    if (el) { px = e.clientX; py = e.clientY; show(el, true); }
  }, true);

  document.addEventListener('focusin', function (e) {
    var el = findTarget(e.target);
    if (!el) return;
    try { if (!el.matches(':focus-visible')) return; } catch (err) { return; }
    show(el, false);
  });
  document.addEventListener('focusout', function () { hide(); });
  window.addEventListener('scroll', function () { if (current) hide(); }, { passive: true, capture: true });
  window.addEventListener('resize', hide);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hide(); });

  var setEnabled = function (on) { enabled = on; if (!on) hide(); };
  window.addEventListener('message', function (e) {
    if (e.origin !== location.origin || !e.data || e.data.type !== 'ac-guide') return;
    setEnabled(!!e.data.enabled);
  });
  window.addEventListener('storage', function (e) { if (e.key === KEY) setEnabled(e.newValue !== 'off'); });

  /* ─── floating "Live demo" bar on the full-screen product pages ───────── */
  var PRODUCTS = {
    studio: ['Studio', 'Your dashboard', 'studio/'],
    website: ['Website', 'Your academy website', 'website/'],
    app: ['Student app', "Your students' phone", 'app/']
  };
  var WA_MSG = {
    studio: 'Hi AllCoaching, I just tried the Studio demo and want to start my academy.',
    website: 'Hi AllCoaching, I just tried the website demo and want a website like this for my academy.',
    app: 'Hi AllCoaching, I just tried the student app demo and want an app like this for my academy.'
  };
  if (!PRODUCTS[product] || window.top !== window.self || SHOT) return;

  if (product === 'app') document.documentElement.classList.add('acd-tabbar');
  var barCss = document.createElement('style');
  barCss.textContent =
    '.acd{font-family:"Inter Tight",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased;letter-spacing:-.005em}' +
    '.acd *{box-sizing:border-box}' +
    '.acd-bar{position:fixed;left:50%;bottom:calc(14px + env(safe-area-inset-bottom));transform:translateX(-50%);z-index:2147483000;width:max-content;max-width:calc(100vw - 24px);display:flex;align-items:center;gap:4px;padding:4px;border-radius:999px;background:#15110D;box-shadow:0 14px 32px -10px rgba(21,17,13,.55),inset 0 0 0 1px rgba(255,255,255,.08)}' +
    '.acd-toggle{display:flex;align-items:center;gap:7px;height:38px;margin:0;padding:0 11px 0 5px;border:0;border-radius:999px;background:transparent;color:#F5F0E8;font-family:inherit;font-size:13.5px;font-weight:600;line-height:1;cursor:pointer;white-space:nowrap}' +
    '.acd-toggle:hover{background:rgba(255,255,255,.09)}' +
    '.acd-toggle img{width:28px;height:28px;border-radius:50%;background:#fff;display:block}' +
    '.acd-toggle svg{transition:transform .2s ease}' +
    '.acd-toggle[aria-expanded="true"] svg{transform:rotate(180deg)}' +
    '.acd-join{display:flex;align-items:center;height:38px;padding:0 16px;border-radius:999px;background:linear-gradient(135deg,#E0A95C 0%,#C58B43 55%,#9C6A2E 100%);color:#2A1B07!important;font-size:13.5px;font-weight:700;line-height:1;text-decoration:none!important;white-space:nowrap}' +
    '.acd-sheet{position:fixed;left:50%;bottom:calc(66px + env(safe-area-inset-bottom));transform:translateX(-50%);z-index:2147483001;width:min(300px,calc(100vw - 24px));max-height:calc(100vh - 100px);overflow:auto;background:#FFFDF8;color:#15110D;border:1px solid rgba(20,17,13,.12);border-radius:18px;padding:8px;box-shadow:0 24px 48px -16px rgba(38,28,14,.38);text-align:left}' +
    '.acd-sheet[hidden]{display:none!important}' +
    '.acd-note{margin:4px 10px 8px;font-family:"Caveat","Segoe Print","Comic Sans MS",cursive;font-weight:600;font-size:17px;line-height:1.1;color:#9C6A2E}' +
    '.acd-item{display:flex;flex-direction:column;gap:2px;padding:9px 12px;border-radius:12px;color:#15110D!important;text-decoration:none!important}' +
    '.acd-item b{font-size:14px;font-weight:700}' +
    '.acd-item small{font-size:12px;color:#8C8378}' +
    '.acd-item:hover{background:#F5F0E8}' +
    '.acd-item.acd-on{background:#F5E8D2;box-shadow:inset 3px 0 0 #C58B43}' +
    '.acd-sep{height:1px;background:rgba(20,17,13,.08);margin:6px 8px}' +
    '.acd-row{display:flex;align-items:center;justify-content:space-between;width:100%;margin:0;padding:10px 12px;border:0;border-radius:10px;background:transparent;color:#15110D!important;font-family:inherit;font-size:13.5px;font-weight:600;line-height:1.2;text-align:left;text-decoration:none!important;cursor:pointer}' +
    '.acd-row:hover{background:#F5F0E8}' +
    '.acd-state{font-size:12px;font-weight:700;color:#2F8F4E}' +
    '.acd-state.acd-off{color:#8C8378}' +
    '@media (max-width:900px){html.acd-tabbar .acd-bar{bottom:calc(68px + env(safe-area-inset-bottom))}html.acd-tabbar .acd-sheet{bottom:calc(120px + env(safe-area-inset-bottom))}}' +
    '@media print{.acd{display:none}}' +
    'body:has(.mobile-nav-open) .acd-bar,body:has(.mobile-nav-open) .acd-sheet{display:none!important}';
  document.head.appendChild(barCss);

  var bar = document.createElement('div');
  bar.className = 'acd';
  bar.setAttribute('data-tip-off', '');
  bar.innerHTML =
    '<div class="acd-sheet" id="acd-sheet" hidden>' +
      '<p class="acd-note">sample data — nothing is saved or charged</p>' +
      Object.keys(PRODUCTS).map(function (k) {
        var p = PRODUCTS[k], on = k === product;
        return '<a class="acd-item' + (on ? ' acd-on' : '') + '" href="' + BASE + p[2] + '"' + (on ? ' aria-current="page"' : '') + '><b>' + p[0] + '</b><small>' + p[1] + '</small></a>';
      }).join('') +
      '<div class="acd-sep"></div>' +
      '<button type="button" class="acd-row" data-act="hints">Handwritten hints <span class="acd-state"></span></button>' +
      '<button type="button" class="acd-row" data-act="reset">Start over</button>' +
      '<a class="acd-row" target="_blank" rel="noopener" href="https://wa.me/919889977262?text=' + encodeURIComponent(WA_MSG[product]) + '">WhatsApp us</a>' +
      '<a class="acd-row" href="' + BASE + '">All demos</a>' +
    '</div>' +
    '<div class="acd-bar">' +
      '<button type="button" class="acd-toggle" aria-expanded="false" aria-controls="acd-sheet"><img src="' + BASE + 'assets/favicon.webp" alt="" width="28" height="28"/><span>Live demo</span>' +
      '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 15l6-6 6 6"/></svg></button>' +
      '<a class="acd-join" href="https://studio.allcoaching.in/">Join now</a>' +
    '</div>';
  document.body.appendChild(bar);

  var sheet = bar.querySelector('.acd-sheet'), toggle = bar.querySelector('.acd-toggle'), state = bar.querySelector('.acd-state');
  var paint = function () { state.textContent = enabled ? 'On' : 'Off'; state.classList.toggle('acd-off', !enabled); };
  var openSheet = function (open) { sheet.hidden = !open; toggle.setAttribute('aria-expanded', String(open)); };
  paint();
  toggle.addEventListener('click', function () { openSheet(sheet.hidden); });
  document.addEventListener('click', function (e) { if (!sheet.hidden && !bar.contains(e.target)) openSheet(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !sheet.hidden) { openSheet(false); toggle.focus(); } });
  bar.querySelector('[data-act="hints"]').addEventListener('click', function () {
    var next = !enabled;
    try { localStorage.setItem(KEY, next ? 'on' : 'off'); } catch (e) {}
    setEnabled(next); paint();
  });
  bar.querySelector('[data-act="reset"]').addEventListener('click', function () {
    try { var keep = localStorage.getItem(KEY); localStorage.clear(); if (keep) localStorage.setItem(KEY, keep); } catch (e) {}
    location.href = BASE + PRODUCTS[product][2];
  });
})();
