import re, glob, os

# ---------- True counts (verified: blog/ 33 + blogs/en/ 21 + hinglish/ 13 + hi/ 0 = 67) ----------
def posts(d): return len([f for f in glob.glob(d+'/*.html') if not f.replace('\\','/').endswith('/index.html')])
N_BLOG, N_EN, N_HI, N_HING = posts('blog'), posts('blogs/en'), posts('blogs/hi'), posts('blogs/hinglish')
N_ENGLISH = N_BLOG + N_EN
N_ALL = N_ENGLISH + N_HI + N_HING
print(f'counts: blog={N_BLOG} en={N_EN} hi={N_HI} hinglish={N_HING} -> English={N_ENGLISH} All={N_ALL}')
assert N_ALL == 67, N_ALL

# ---------- 1) Backfill blog/index.html blogPost[] to mirror the 33-item ItemList ----------
idx='blog/index.html'; h=open(idx,encoding='utf-8').read()
il_names = re.findall(r'"@type":"ListItem","position":\d+,"url":"([^"]+)","name":"((?:[^"\\]|\\.)*)"', h)
il_urls = [u for u,_ in il_names]
bp_block_start = h.index('"blogPost":[')
bp_close = h.index('\n    ]', bp_block_start)
bp_inner = h[bp_block_start:bp_close]
existing_urls = set(re.findall(r'"BlogPosting","headline":"(?:[^"\\]|\\.)*","url":"([^"]+)"', bp_inner))
missing = [u for u in il_urls if u not in existing_urls]
print('ItemList urls:', len(il_urls), '| existing blogPost:', len(existing_urls), '| missing:', len(missing))
def post_meta(url):
    slug = url.rsplit('/',1)[-1]; fp = 'blog/'+slug+'.html'
    src = open(fp,encoding='utf-8').read()
    head = re.search(r'"headline"\s*:\s*"((?:[^"\\]|\\.)*)"', src).group(1)
    date = re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"', src).group(1)
    return head, date
new_entries=[]
for u in missing:
    head,date = post_meta(u)
    new_entries.append('{"@type":"BlogPosting","headline":"%s","url":"%s","datePublished":"%s"}' % (head,u,date))
if new_entries:
    block = ',\n' + ',\n'.join('      '+e for e in new_entries)
    h = h[:bp_close] + block + h[bp_close:]
    open(idx,'w',encoding='utf-8',newline='').write(h)
total_bp = h.count('"@type":"BlogPosting"')
print('blog/index.html blogPost entries now:', total_bp)
assert total_bp == 33, total_bp

# ---------- 2) Fix navigation chip + guides + published counts across the 4 blogs/* index files ----------
PUBLISHED = {'blogs/index.html': N_ALL, 'blogs/en/index.html': N_ENGLISH, 'blogs/hi/index.html': N_HI, 'blogs/hinglish/index.html': N_HING}
for f, pub in PUBLISHED.items():
    s=open(f,encoding='utf-8').read(); orig=s
    s,n1=re.subn(r'(All <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_ALL, s)
    s,n2=re.subn(r'(English <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_ENGLISH, s)
    s,n3=re.subn(r'(Hinglish <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_HING, s)
    s,n4=re.subn(r'(हिन्दी</span> <span class="filter-chip-count">)\d+', r'\g<1>%d'%N_HI, s)
    s,n5=re.subn(r'\d+( guides · By the founder)', r'%d\1'%N_ALL, s)
    s,n6=re.subn(r'\d+( published · Newest first)', r'%d\1'%pub, s)
    open(f,'w',encoding='utf-8',newline='').write(s)
    print(f'{f}: All={n1} English={n2} Hinglish={n3} Hindi={n4} guides={n5} published={n6}(->{pub})')
print('DONE')
