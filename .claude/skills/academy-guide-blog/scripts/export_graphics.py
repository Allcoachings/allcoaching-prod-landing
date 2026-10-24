"""Render every SVG in a folder to WebP with the real brand fonts.

Usage: python .claude/skills/academy-guide-blog/scripts/export_graphics.py assets/blog/<slug> [name-filter]

- In-article graphics (viewBox 1220 wide) export at 1220 px (2x the 610 px column).
- cover.svg (1600x900) exports at 1600x900 for og:image and the hero.
Needs Node + Playwright (pre-installed here) and Pillow.
"""
import os, subprocess, sys, tempfile, json
from PIL import Image

FONTS = ('https://fonts.googleapis.com/css2?family=Inter:wght@300..800&family=Inter+Tight:wght@400..900'
         '&family=Caveat:wght@500..700&family=Instrument+Serif:ital@1&family=IBM+Plex+Mono:wght@500;600&display=swap')

JS = r"""
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const [dir,outDir,filter,fonts]=process.argv.slice(2);
(async()=>{const b=await chromium.launch();
for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.svg')&&(!filter||f.includes(filter)))){
  const svg=fs.readFileSync(path.join(dir,f),'utf8');const m=svg.match(/viewBox="0 0 (\d+) (\d+)"/);const w=+m[1],h=+m[2];
  const cover=f==='cover.svg';const vw=cover?w:w/2,vh=cover?h:h/2;
  const p=await b.newPage({viewport:{width:Math.round(vw),height:Math.round(vh)},deviceScaleFactor:cover?1:2});
  await p.setContent(`<html><head><link href="${fonts}" rel="stylesheet"><style>body{margin:0}svg{width:${vw}px;height:${vh}px;display:block}</style></head><body>${svg}</body></html>`,{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  await p.screenshot({path:path.join(outDir,f.replace('.svg','.png')),clip:{x:0,y:0,width:vw,height:vh}});
  await p.close();console.log(f);}
await b.close();})();
"""


def main():
    d = os.path.abspath(sys.argv[1])
    flt = sys.argv[2] if len(sys.argv) > 2 else ''
    tmp = tempfile.mkdtemp()
    js = os.path.join(tmp, 'render.js')
    open(js, 'w').write(JS)
    subprocess.run(['node', js, d, tmp, flt, FONTS], check=True)
    for f in sorted(os.listdir(tmp)):
        if f.endswith('.png'):
            out = os.path.join(d, f[:-4] + '.webp')
            Image.open(os.path.join(tmp, f)).convert('RGB').save(out, 'WEBP', quality=84, method=6)
            print(f'{out}  {os.path.getsize(out) // 1024} KB')


if __name__ == '__main__':
    main()
