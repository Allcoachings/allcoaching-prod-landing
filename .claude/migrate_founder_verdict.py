"""
Migration: apply uniform 'golden circle' founder photo + pixel-perfect verdict
CTA buttons + trust bar across all blogs.

Targets:
  blog/*.html  (skip seo-strategies-for-online-course-creators.html — already done)

Two passes:
  1. Founder photo  — wrap .photo-wrap with circle + gold ring inline style
  2. Verdict CTA    — only verdict blocks containing two <a> tags get their
                      button-wrapper div replaced with pixel-perfect buttons + trust bar
"""
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
BLOG = REPO / "blog"
SKIP = {"seo-strategies-for-online-course-creators.html"}

# ─────────────────────────────────────────────────────────────────────
# Pass 1 — founder photo: circle + gold ring
# ─────────────────────────────────────────────────────────────────────

GOLD_RING_STYLE = (
    'width:180px; height:180px; border-radius:50%; '
    'box-shadow:'
    '0 0 0 4px #FAF8F4,'
    '0 0 0 7px #E0A95C,'
    '0 0 0 8px rgba(197,139,67,.35),'
    '0 0 0 14px rgba(224,169,92,.16),'
    '0 22px 50px -10px rgba(197,139,67,.45);'
)

# Match the existing .photo-wrap (no inline style yet) wrapping a single <img>
FOUNDER_RE = re.compile(
    r'<div class="photo-wrap">\s*'
    r'<img\s+([^>]+?)\s*/?>\s*'
    r'</div>',
    re.DOTALL
)


def patch_founder(text: str):
    def repl(m):
        attrs = m.group(1)
        attrs = re.sub(r'\bwidth="\d+"', 'width="180"', attrs)
        attrs = re.sub(r'\bheight="\d+"', 'height="180"', attrs)
        if 'style=' not in attrs:
            attrs = attrs.rstrip() + ' style="object-position:center 20%;"'
        return (
            f'<div class="photo-wrap" style="{GOLD_RING_STYLE}">'
            f'<img {attrs} />'
            f'</div>'
        )
    return FOUNDER_RE.subn(repl, text)


# ─────────────────────────────────────────────────────────────────────
# Pass 2 — verdict CTA button block: replace with pixel-perfect buttons + trust bar
# ─────────────────────────────────────────────────────────────────────

# Match: the button-wrapper div inside a verdict block.
# Pattern: <div class="...flex...">  ... two <a> tags ...  </div>
# It MUST contain 'studio.allcoaching.in' to be sure we're hitting the CTA buttons.

BTN_BLOCK_RE = re.compile(
    r'<div class="mt-6 flex flex-wrap gap-3">\s*'
    r'<a href="(https://educator\.allcoaching\.in/?)"[^>]*>\s*'
    r'([^<\n]+?)\s*'
    r'<svg[^>]*>.*?</svg>\s*'
    r'</a>\s*'
    r'<a href="(https://allcoaching\.in/contact)"[^>]*>\s*'
    r'([^<\n]+?)\s*'
    r'</a>\s*'
    r'</div>',
    re.DOTALL
)


def make_buttons(primary_href: str, primary_label: str,
                 secondary_href: str, secondary_label: str) -> str:
    return f'''<div class="mt-7 flex flex-col sm:flex-row gap-4 justify-center items-center">
      <a href="{primary_href}" target="_blank" rel="noopener"
         class="group relative inline-flex items-center justify-center gap-2.5 overflow-hidden no-underline"
         style="height:54px; padding:0 28px; border-radius:14px; background:linear-gradient(180deg,#F5C887 0%,#E0A95C 35%,#C58B43 70%,#B07A36 100%); color:#1A100A; font-family:'Inter Tight',sans-serif; font-weight:700; font-size:14.5px; letter-spacing:.01em; text-decoration:none; box-shadow:0 1px 0 rgba(255,255,255,.55) inset,0 -1px 0 rgba(0,0,0,.10) inset,0 0 0 1px rgba(95,55,15,.18),0 12px 28px -8px rgba(197,139,67,.55),0 24px 60px -16px rgba(197,139,67,.45); transition:transform .18s ease, box-shadow .18s ease;"
         onmouseover="this.style.transform='translateY(-2px)';"
         onmouseout="this.style.transform='translateY(0)';">
        <span aria-hidden="true" style="position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.32),rgba(255,255,255,0));pointer-events:none;border-radius:14px 14px 0 0;"></span>
        <span class="relative">{primary_label}</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" class="relative transition-transform group-hover:translate-x-1"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
      </a>
      <a href="{secondary_href}" target="_blank" rel="noopener"
         class="group relative inline-flex items-center justify-center gap-2 no-underline"
         style="height:54px; padding:0 24px; border-radius:14px; color:#F5D8AE; font-family:'Inter Tight',sans-serif; font-weight:600; font-size:14.5px; letter-spacing:.005em; text-decoration:none; background:rgba(245,216,174,.04); border:1px solid rgba(245,216,174,.22); box-shadow:0 1px 0 rgba(255,255,255,.05) inset; transition:all .18s ease;"
         onmouseover="this.style.background='rgba(245,216,174,.10)';this.style.borderColor='rgba(224,169,92,.65)';this.style.color='#FBE2B8';this.style.transform='translateY(-2px)';"
         onmouseout="this.style.background='rgba(245,216,174,.04)';this.style.borderColor='rgba(245,216,174,.22)';this.style.color='#F5D8AE';this.style.transform='translateY(0)';">
        {secondary_label}
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" class="transition-transform group-hover:translate-x-1"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
      </a>
    </div>
    <div class="mt-7 inline-flex flex-wrap items-center justify-center gap-x-5 gap-y-2" style="font-family:'JetBrains Mono',monospace; font-size:10px; letter-spacing:.18em; color:rgba(245,216,174,.5); font-weight:700; text-transform:uppercase;">
      <span>Free to start</span>
      <span style="opacity:.4;">·</span>
      <span>90% revenue</span>
      <span style="opacity:.4;">·</span>
      <span>No lock-in</span>
      <span style="opacity:.4;">·</span>
      <span>Daily payouts</span>
    </div>'''


def patch_verdict(text: str):
    count = 0
    def repl(m):
        nonlocal count
        count += 1
        return make_buttons(m.group(1), m.group(2), m.group(3), m.group(4))
    new = BTN_BLOCK_RE.sub(repl, text)
    return new, count


# ─────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────

def main():
    files = sorted(BLOG.glob("*.html"))
    grand_f = grand_v = 0
    for p in files:
        if p.name in SKIP:
            print(f"  [SKIP] {p.name}")
            continue
        text = p.read_text(encoding="utf-8")
        original = text
        text, fcount = patch_founder(text)
        text, vcount = patch_verdict(text)
        if text != original:
            p.write_text(text, encoding="utf-8")
            print(f"  [OK]   {p.name:<60} founder:{fcount} verdict:{vcount}")
            grand_f += fcount
            grand_v += vcount
        else:
            print(f"  [--]   {p.name}")
    print(f"\nTotal: founder photos updated = {grand_f}, verdict CTAs updated = {grand_v}")


if __name__ == "__main__":
    main()
