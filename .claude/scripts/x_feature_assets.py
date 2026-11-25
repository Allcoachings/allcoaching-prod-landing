#!/usr/bin/env python3
"""One-off, idempotent: add the YouTube lite embed to assets/x/x.js and the feature-page CSS to assets/x/x.css."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)

YT = r'''
  /* ---------- YouTube lite embed: <button class="xyt" data-yt="ID"> -> iframe on click ---------- */
  d.addEventListener('click', function (e) {
    var b = e.target.closest('.xyt'); if (!b || b.classList.contains('on')) return;
    e.preventDefault();
    var f = d.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + b.getAttribute('data-yt') + '?autoplay=1&rel=0&playsinline=1&modestbranding=1';
    f.title = b.getAttribute('aria-label') || 'AllCoaching studio tutorial';
    f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    f.allowFullscreen = true;
    b.classList.add('on'); b.appendChild(f);
  });
  /* tutorial switcher: [data-ytpick="ID"] swaps the main player */
  d.addEventListener('click', function (e) {
    var t = e.target.closest('[data-ytpick]'); if (!t) return;
    var main = d.querySelector('.xyt'); if (!main) return;
    e.preventDefault();
    var fr = main.querySelector('iframe'); if (fr) fr.remove(); main.classList.remove('on');
    main.setAttribute('data-yt', t.getAttribute('data-ytpick'));
    var img = main.querySelector('img'); if (img && t.getAttribute('data-thumb')) img.src = t.getAttribute('data-thumb');
    var cap = d.querySelector('.xf-vcap b'); if (cap && t.getAttribute('data-title')) cap.textContent = t.getAttribute('data-title');
    [].forEach.call(d.querySelectorAll('[data-ytpick]'), function (x) { x.classList.toggle('on', x === t); });
  });
'''

CSS = r'''
/* ---------- feature pages (/features/*) ---------- */
.xyt{position:relative;display:block;width:100%;aspect-ratio:16/9;border:0;padding:0;border-radius:20px;overflow:hidden;background:#0B1033;cursor:pointer;box-shadow:0 50px 100px -30px rgba(0,0,0,.75),0 0 0 1px rgba(255,255,255,.12)}
.xyt img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .6s var(--x-ease),filter .3s}
.xyt:hover img{transform:scale(1.03);filter:brightness(.92)}
.xyt .pl{position:absolute;left:50%;top:50%;width:84px;height:84px;margin:-42px 0 0 -42px;border-radius:50%;background:rgba(255,255,255,.95);display:grid;place-items:center;box-shadow:0 20px 50px -10px rgba(0,0,0,.6);transition:transform .25s var(--x-ease)}
.xyt:hover .pl{transform:scale(1.08)}
.xyt .pl svg{width:30px;height:30px;fill:#2B44FF;margin-left:5px}
.xyt iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.xyt.on img,.xyt.on .pl{visibility:hidden}
.xf-vcap{display:flex;align-items:center;gap:12px;margin-top:16px;color:var(--x-dim);font-size:14px;flex-wrap:wrap}
.xf-vcap b{color:#fff;font-weight:600}
.xf-vcap i{font-style:normal;font-family:var(--mono,'JetBrains Mono',monospace);font-size:11.5px;letter-spacing:.1em;padding:5px 9px;border-radius:8px;background:rgba(43,68,255,.22);color:#C9D1FF}
.xf-picks{display:flex;gap:10px;margin-top:14px;flex-wrap:wrap}
.xf-picks button{font:inherit;font-size:13px;color:var(--x-soft);background:rgba(255,255,255,.06);border:1px solid var(--x-line);border-radius:999px;padding:7px 14px;cursor:pointer}
.xf-picks button.on{background:#fff;color:#050819;border-color:#fff}
.xf-crumb{font-family:var(--mono,'JetBrains Mono',monospace);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--x-dim);margin-bottom:20px}
.xf-crumb a{color:var(--x-dim);text-decoration:none}.xf-crumb a:hover{color:#fff}
.xf-crumb span{margin:0 8px;opacity:.5}
.xf{font-family:var(--ui,'Inter',system-ui,sans-serif);color:#14161F}
.xf .xw{max-width:1280px}
.xf-sec{padding:104px 0;border-top:1px solid #EEF0F5}
.xf-sec:first-child{border-top:0}
.xf-row{display:grid;grid-template-columns:.9fr 1.1fr;gap:72px;align-items:center}
.xf-row.rev .xf-tx{order:2}
.xf-eye{font-family:var(--mono,'JetBrains Mono',monospace);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#2B44FF}
.xf h2{margin:16px 0 0;font-size:clamp(30px,3.4vw,50px);font-weight:300;letter-spacing:-.03em;line-height:1.08;color:#14161F}
.xf h2 b{font-weight:700}
.xf-tx p{margin-top:18px;font-size:18px;line-height:1.6;color:#4A5063;max-width:52ch}
.xf-ul{list-style:none;margin:26px 0 0;padding:0;display:grid;gap:12px}
.xf-ul li{display:flex;gap:12px;font-size:16px;line-height:1.5;color:#2A2E3D}
.xf-ul li:before{content:"";flex:none;width:22px;height:22px;margin-top:1px;border-radius:50%;background:#E8F0FF url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232B44FF' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m6 12 4 4 8-8'/%3E%3C/svg%3E") center/13px no-repeat}
.xf-vis{position:relative}
.xf-shot{border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 1px 2px rgba(20,22,31,.05),0 40px 80px -36px rgba(23,40,160,.4),0 0 0 1px #E6E8F0}
.xf-shot img{display:block;width:100%;height:auto}
.xf-vis .xphone{position:absolute;right:-3%;bottom:-14%;font-size:clamp(5.5px,.55vw,8px)}
.xf-vis.has-phone{padding-bottom:40px}
.xf-steps-h{text-align:center}
.xf-steps-h p{margin:16px auto 0;font-size:18px;color:#4A5063;max-width:56ch}
.xf-steps{list-style:none;margin:56px 0 0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;counter-reset:s}
.xf-steps li{position:relative;background:#F6F8FC;border:1px solid #E6E8F0;border-radius:18px;padding:26px 24px 28px;counter-increment:s}
.xf-steps li:before{content:"0" counter(s);display:block;font-family:var(--mono,'JetBrains Mono',monospace);font-size:13px;color:#2B44FF;margin-bottom:14px}
.xf-steps b{display:block;font-size:18px;font-weight:600;line-height:1.3}
.xf-steps span{display:block;margin-top:8px;font-size:15px;line-height:1.55;color:#4A5063}
.xf-faq{max-width:880px;margin:44px auto 0}
.xf-faq details{border-bottom:1px solid #E6E8F0}
.xf-faq summary{list-style:none;cursor:pointer;padding:24px 44px 24px 0;position:relative;font-size:19px;font-weight:600;line-height:1.4;color:#14161F}
.xf-faq summary::-webkit-details-marker{display:none}
.xf-faq summary:after{content:"";position:absolute;right:6px;top:30px;width:10px;height:10px;border-right:2px solid #14161F;border-bottom:2px solid #14161F;transform:rotate(45deg);transition:transform .25s}
.xf-faq details[open] summary:after{transform:rotate(225deg);top:34px}
.xf-faq p{padding:0 0 24px;font-size:17px;line-height:1.65;color:#4A5063;max-width:72ch}
.xf-rel{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:44px}
.xf-card{display:block;text-decoration:none;color:#14161F;border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px #E6E8F0,0 24px 50px -36px rgba(23,40,160,.35);transition:transform .3s var(--x-ease),box-shadow .3s}
.xf-card:hover{transform:translateY(-4px);box-shadow:0 0 0 1px #D9DCE7,0 30px 60px -30px rgba(23,40,160,.45)}
.xf-card img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover}
.xf-card div{padding:20px 22px 24px}
.xf-card small{font-family:var(--mono,'JetBrains Mono',monospace);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:#2B44FF}
.xf-card b{display:block;margin-top:8px;font-size:19px;font-weight:600}
.xf-card span{display:block;margin-top:6px;font-size:15px;line-height:1.5;color:#4A5063}
.xf-group{margin-top:80px}
.xf-group:first-child{margin-top:0}
.xf-group h2{font-size:clamp(26px,2.6vw,38px)}
.xf-group .xf-rel{grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}
@media (max-width:980px){.xf-sec{padding:72px 0}.xf-row{grid-template-columns:1fr;gap:36px}.xf-row.rev .xf-tx{order:0}.xf-vis .xphone{right:2%;bottom:-10%;font-size:5px}.xf-rel{grid-template-columns:1fr}.xf-faq summary{font-size:17px}}
'''

p = 'assets/x/x.js'
s = open(p, encoding='utf-8').read()
if 'class="xyt"' not in s and "'.xyt'" not in s:
    anchor = '  /* ---------- floating studio-tour pill ---------- */'
    assert anchor in s
    s = s.replace(anchor, YT.strip('\n') + '\n\n' + anchor)
    open(p, 'w', encoding='utf-8').write(s)
    print('js: added')

p = 'assets/x/x.css'
c = open(p, encoding='utf-8').read()
if '/* ---------- feature pages' not in c:
    a = c.index('/* responsive */')
    c = c[:a] + CSS.strip() + '\n\n' + c[a:]
    open(p, 'w', encoding='utf-8').write(c)
    print('css: added')
