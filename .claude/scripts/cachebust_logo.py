"""One-off: cache-bust the new logo by appending ?v=20260629 to fevicon.webp / AllCoaching-logo.webp refs."""
import re, glob, os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VER = "?v=20260629"
pats = [(re.compile(r'fevicon\.webp(?!\?)'), 'fevicon.webp' + VER),
        (re.compile(r'AllCoaching-logo\.webp(?!\?)'), 'AllCoaching-logo.webp' + VER)]

files = set()
files |= set(glob.glob('**/*.html', recursive=True))
files |= {'manifest.webmanifest', 'sw.js', 'feed.xml'}
files |= set(glob.glob('templates/**/*.j2', recursive=True))
files |= set(glob.glob('scripts/**/*.py', recursive=True))

def excluded(f):
    return ('.claude' in f) or ('node_modules' in f) or ('.git' in f)

files = [f for f in files if os.path.isfile(f) and not excluded(f)]

changed = 0
refs = 0
for f in sorted(files):
    s = open(f, encoding='utf-8').read()
    o = s
    for rx, rep in pats:
        s = rx.sub(rep, s)
    if s != o:
        open(f, 'w', encoding='utf-8', newline='').write(s)
        changed += 1
        refs += s.count('?v=20260629') - o.count('?v=20260629')
print(f"  files changed: {changed} | versioned refs added: {refs}")

# guards
unv = 0
for f in glob.glob('**/*.html', recursive=True):
    if os.path.isfile(f) and not excluded(f):
        if re.search(r'fevicon\.webp(?!\?)|AllCoaching-logo\.webp(?!\?)', open(f, encoding='utf-8').read()):
            unv += 1
dbl = sum(1 for f in files if '?v=20260629?v=' in open(f, encoding='utf-8').read())
print(f"  HTML still unversioned: {unv} | double-versioned files: {dbl}")
print("  manifest versioned:", 'fevicon.webp?v=20260629' in open('manifest.webmanifest', encoding='utf-8').read())
print("  sw.js versioned:", 'webp?v=20260629' in open('sw.js', encoding='utf-8').read())
print("  feed.xml versioned:", 'webp?v=20260629' in open('feed.xml', encoding='utf-8').read())
