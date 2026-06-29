# -*- coding: utf-8 -*-
"""Delay Google Tag Manager until first user interaction OR 3.5s (whichever first),
to cut Total Blocking Time. dataLayer is created immediately so events still queue."""
import glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

DELAYED = ("(function(w,d,s,l,i){w[l]=w[l]||[];"
  "var g=function(){if(w.__gtm)return;w.__gtm=1;"
  "w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
  "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';"
  "j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);};"
  "var e=['scroll','mousemove','touchstart','keydown','click'],"
  "t=function(){e.forEach(function(n){w.removeEventListener(n,t)});g();};"
  "e.forEach(function(n){w.addEventListener(n,t,{passive:true})});"
  "w.setTimeout(g,3500);"
  "})(window,document,'script','dataLayer','GTM-T3KFKD3G');")

OLD_SINGLE = ("(function(w,d,s,l,i){w[l]=w[l]||[];"
  "w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});"
  "var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';"
  "j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
  "})(window,document,'script','dataLayer','GTM-T3KFKD3G');")

OLD_MULTI = (
"  (function(w,d,s,l,i){\n"
"  w[l]=w[l]||[];\n"
"  w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});\n"
"  var f=d.getElementsByTagName(s)[0],\n"
"  j=d.createElement(s),\n"
"  dl=l!='dataLayer'?'&l='+l:'';\n"
"  j.async=true;\n"
"  j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;\n"
"  f.parentNode.insertBefore(j,f);\n"
"  })(window,document,'script','dataLayer','GTM-T3KFKD3G');")

files = glob.glob('**/*.html', recursive=True) + glob.glob('templates/**/*.j2', recursive=True)
files = [f for f in files if os.path.isfile(f) and '.claude' not in f and 'node_modules' not in f]

changed = 0
already = 0
for f in sorted(files):
    s = open(f, encoding='utf-8').read()
    if '__gtm=1' in s:
        already += 1
        continue
    o = s
    if OLD_SINGLE in s:
        s = s.replace(OLD_SINGLE, DELAYED, 1)
    if OLD_MULTI in s:
        s = s.replace(OLD_MULTI, "  " + DELAYED, 1)
    if s != o:
        open(f, 'w', encoding='utf-8', newline='').write(s)
        changed += 1

print(f"  files changed: {changed} | already-delayed (skipped): {already}")

# verify
gtm = [f for f in files if 'GTM-T3KFKD3G' in open(f, encoding='utf-8').read()]
delayed = [f for f in gtm if '__gtm=1' in open(f, encoding='utf-8').read()]
old_left = [f for f in gtm if (OLD_SINGLE in open(f, encoding='utf-8').read()) or (OLD_MULTI in open(f, encoding='utf-8').read())]
print(f"  files with GTM: {len(gtm)} | now delayed: {len(delayed)} | still old (eager): {len(old_left)} {old_left[:3]}")
