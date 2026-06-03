import re, sys

FILES = [
    'blogs/hinglish/online-tuition-class-kaise-shuru-kare-aur-paise-kamaye.html',
    'blogs/hinglish/youtube-se-coaching-app-par-kaise-shift-kare.html',
]

# Correct structure (from blog/how-to-start-online-academy-in-5-steps.html):
#   <div class="step-card"><div class="step-num">N</div><div><p class="step-l">..</p><h3>..</h3><p>..</p></div></div>
# Broken structure we wrote:
#   <div class="step-card"><p class="step-l">Step 0N</p><h3>..</h3><p>..</p></div>

open_re = re.compile(r'(<div class="step-card[^"]*">)\s*<p class="step-l">')

for path in FILES:
    src = open(path, encoding='utf-8').read()
    lines = src.split('\n')
    fixed = 0
    out = []
    for line in lines:
        if 'class="step-card' in line and '<p class="step-l">' in line and 'step-num' not in line:
            m = re.search(r'Step\s*0?(\d+)', line)
            num = m.group(1) if m else ''
            # insert the number badge + open the col-2 wrapper right after the step-card div
            new = open_re.sub(r'\g<1><div class="step-num">' + num + r'</div><div><p class="step-l">', line)
            # the line ended with the step-card's closing </div>; append one more to close the wrapper
            if new.rstrip().endswith('</div>'):
                new = new.rstrip() + '</div>'
            else:
                print('  !! unexpected line end, skipped close-div on:', path)
            # sanity: balanced div tags on this line
            if new.count('<div') != new.count('</div>'):
                print('  !! UNBALANCED divs after fix in', path, '->', new.count('<div'), 'open vs', new.count('</div>'), 'close')
            out.append(new)
            fixed += 1
        else:
            out.append(line)
    open(path, 'w', encoding='utf-8', newline='').write('\n'.join(out))
    # verify counts
    res = open(path, encoding='utf-8').read()
    print(f'{path}: step-cards fixed={fixed}, step-num now={res.count("step-num")}, step-card={res.count(chr(34)+"step-card")}')
