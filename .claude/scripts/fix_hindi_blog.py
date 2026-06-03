import sys

path = 'blogs/hinglish/hindi-medium-teacher-ke-liye-online-platform.html'
h = open(path, encoding='utf-8').read()

fixes = [
    # (label, old, new, expected_count)
    ('dead-link', 'blogs/en/multi-language-lms-for-regional-indian-languages',
                  'blog/multi-language-lms-for-regional-indian-languages', 4),
    ('mojibake',  'angrezी-medium', 'angrezi-medium', 1),
    ('creators',  'creators', 'educators', 5),
    ('faq-q10',   'website ya app dono chahiye', 'website aur app dono chahiye', 1),
    ('faq-q9',    'usme de sakte hain. <strong>Niche',
                  'usme de sakte hain, jaise Hindi, Bhojpuri-belt Hindi, Maithili, ya Marwari. <strong>Niche', 1),
]

ok = True
for label, old, new, exp in fixes:
    n = h.count(old)
    if n != exp:
        print(f'  !! {label}: found {n}, expected {exp} — NOT applied')
        ok = False
        continue
    h = h.replace(old, new)
    print(f'  ok {label}: replaced {n}')

if not ok:
    print('ABORTED — no file written (count mismatch)')
    sys.exit(1)

open(path, 'w', encoding='utf-8', newline='').write(h)
print('written:', path)
