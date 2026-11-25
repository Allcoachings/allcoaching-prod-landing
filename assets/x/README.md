# X layer: AllCoaching's premium dark design (Nov 2026)

Shopify-style structure in AllCoaching's own brand. Files:

- `x.css`: header, homepage sections, inner-page kit, phone frame.
- `x.js`: mega menus, mobile drawer, reveal on scroll, in-view video, video modal.
- `header.html`: the shared header. Never edit it inside a page; edit this file and run
  `python .claude/scripts/apply_x_header.py` (it also bumps the `?v=` on x.css / x.js: raise `VER` in the script when x.css changes).
- `phone.html`: realistic iPhone frame snippet (replace `IMG` and `ALT`). Scale it with `font-size` on `.xphone`.
- `home-main.html`, `home-final.html`, `overlays.html`: homepage sources (spliced into `index.html` between the `<!-- X HOME -->` markers).

## Inner-page recipe (reference: `pricing.html`)

1. `<body class="… xpage xin">` (add the two classes, keep the existing ones).
2. Replace the page's first (hero) section with a dark hero:

```html
<section class="xphero" id="top">            <!-- add "solo" for text-only (legal pages), "center" to centre -->
  <div class="xw">
    <div class="tx">
      <div class="xh-eye">Eyebrow</div>
      <h1>Light setup line <span class="bd">bold payoff.</span></h1>   <!-- keep the page's existing H1 wording -->
      <p class="sub">…existing lede…</p>
      <div class="xcta"><a class="xbtn xbtn-w" href="https://studio.allcoaching.in/">Start free trial</a><a class="xbtn xbtn-o" href="#…">Second action</a></div>
      <div class="xnote"><span>7 days free, no card needed</span>…</div>
    </div>
    <div class="vis"><div class="xframe"><img src="/assets/x/….webp" …/></div> <!-- optional phone.html snippet after it --></div>
  </div>
  <div class="xw" style="display:block"><div class="xkpis"><div><small>Label</small><b>Big</b><span>caption</span></div>…x3</div></div>  <!-- optional -->
</section>
<div class="xlight">      <!-- white sheet with a 48px rounded top that slides over the hero -->
  …all the existing light sections, unchanged…
</div>
```

3. Replace the page's last CTA band with the dark final (close the `.xlight` div first):

```html
</div>
<section class="xfinal plain"><div class="xw">
  <h2 class="xd" style="font-size:clamp(44px,6vw,96px);max-width:13ch">Setup words <b>payoff.</b></h2>
  <p class="xlead">…</p>
  <div class="xcta"><a class="xbtn xbtn-w" href="https://studio.allcoaching.in/">Start free trial</a><a class="xbtn xbtn-o" href="https://api.whatsapp.com/send/?phone=919889977262" target="_blank" rel="noopener">Ask on WhatsApp</a></div>
</div></section>
```

Other kit pieces (all dark, use inside `.xdark` or a dark section): `.xsec` (120px section), `.xd .xh2` headline with `<span class="xdim">` grey continuation or `<b>` payoff,
`.xlead`, `.xpanel` (two-column gradient panel with `.tx` + `.vis`, `.xshot` absolute screenshot, `.xfloat` floating white card), `.x3` three cards, `.x2` two cards,
`.xnum-grid`/`.xnum` big numbers, `.xchips`, `.xtool-list`, `.xframe` (framed screenshot), `.xsteps` 01/02/03, `.xsheet` / `.xblue` / `.xnums` rounded-top sheets, `.xrv` reveal on scroll.

## Real screenshots available (all real UI, demo data)

Desktop 1600x900 (and `-800` versions): `s-course` (new course form), `s-site` / `a-home` (academy website home), `a-courses` (course list with prices), `a-course` (course page with price + Enroll),
`s-live` (live classes), `s-tests` (test results), `s-getpaid` (Razorpay / bank set-up), `s-int` (integrations), `s-home` (studio home: shows an account name, avoid).
Phone 780x1688: `m-home`, `m-courses`, `m-course`. Poster: `tour-poster.webp`. Video (placeholder for every slot): `https://allcoaching-store.b-cdn.net/blog-images/allcoaching-studio-tour-v4-1080p.mp4`.
More 4K studio shots: `C:\Users\allco\codes\video-studio\public\shots\*.png` (3840x2160; export to webp at 1600x900, quality ~80, into `assets/x/`). Avoid shots showing personal names ("kaya", "AJANTA…").

## QA screenshot helper

`cd C:/Users/allco/codes/video-studio && node capture/pageshot.mjs "http://localhost:8765/<page>.html" <out.png> [desktop|mobile] [scrollY or CSS selector] [full]`
It prints JSON with `overflowX` and page errors. The local server on port 8765 is already running.

## Feature pages (/features/)

14 product feature pages plus the hub `features/index.html`, generated. Never hand-edit `features/*.html`.

- Content: `data/features/<slug>.json`, schema and writing rules in `data/features/_BRIEF.md`. Screenshots: `assets/x/f/<slug>-<n>.webp`. Tutorial thumbnails: `assets/x/tut/<EP>.webp`.
- Build: `python .claude/scripts/build_feature_pages.py` (`--check` validates only; `--register` also refreshes the `<!-- features:start/end -->` block in `sitemap.xml` and the "Features" section in `llms.txt`). Then run `apply_x_header.py`.
- The episode list (YouTube ids, titles, publish dates, durations) is `EPS` at the top of the build script. Each page embeds its tutorial with a lite player (`.xyt` in `x.js`); `courses` has two (EP02, EP03) with a switcher.

## Palette, footer, fonts (2026-11-25, owner)

- **Colours:** studio dashboard charcoal, not navy. Base `#151515`, surfaces `#1b1b1b` / `#1f1f1f` / `#232323`, light ink `#f2f2f2`, accent `#2B44FF`, light accent `#A9B6FF`. `.claude/scripts/x_palette_charcoal.py` maps old navy values.
- **Footer:** shared `assets/x/footer.html` (built by `.claude/scripts/x_footer_build.py`), applied by `apply_x_header.py` to every page. No registered address in any footer (owner, 2026-11-25); `footer-reg.html` is kept but unused.
- **Header:** transparent over a dark hero on every page that starts with `.xhero` / `.xphero` (x.js adds `.over` and `body.xover`); solid on scroll and on light pages.
- **Fonts:** Inter Tight for everything, JetBrains Mono for mono, Instrument Serif italic only for the wordmark. `.claude/scripts/x_fonts_unify.py` rewrites CSS rules and the Google Fonts link (re-run it after adding pages written with older styles).
- **Icons and cards:** studio Home card art in `assets/x/art/<id>.webp` (rendered from `video-studio/src/tour/ArtTile.tsx`); menu icons are coloured chips (`.xi`, hue per feature).
- **Hero story:** `assets/x/story/` holds `story-loop.mp4` (1080p, silent), `story-loop-720.mp4` (mobile), `story-full.mp4` (Hindi voiceover + music, opened by "Watch her story") and `story-poster.webp`. Generated in ElevenLabs (Kling 3 Pro video, eleven_v4 "Amit Ratan" voice, eleven_music), flow "AllCoaching hero story 2027".

## Hero and final-section videos (2026-11-25)
- The mp4 files live on Bunny CDN: `https://allcoaching-store.b-cdn.net/blog-images/allcoaching-cdn-videos/` (india-hero, india-hero-720, india-hero-full, india-footer, india-footer-720). Only the posters stay in the repo. Originals: `Downloads/allcoaching-cdn-videos/`.
- Hero: `story/india-hero.mp4` (1080p, 16 s, silent loop), `india-hero-720.mp4` (mobile), poster `india-hero-poster.webp`; "Watch the film" opens `india-hero-full.mp4` (with music).
- Final CTA section (`home-final.html`): `story/india-footer.mp4` + `india-footer-poster.webp` (8 s).
- Made in Remotion (`video-studio/src/hero/IndiaMontage.tsx`, compositions HeroIndia / FooterIndia) from 12 Google Flow clips (Veo 3.1 Quality + Omni 1.2 Flash, upscaled to 1080p); prompts in `video-studio/story/montage-prompts-v2.md`. Older `montage-*`, `split-*`, `story-*` files are kept, unused.
