"""Clone vs/classplus.html into vs/<competitor>.html with all references swapped.

Usage:
  python .claude/scripts/clone_vs_page.py graphy "Graphy" "video course platform builder"
  python .claude/scripts/clone_vs_page.py teachmint "Teachmint" "white-label coaching platform"

Replaces:
- "Classplus" -> "<Competitor>" everywhere
- "classplus" -> "<competitor_lower>" in URLs/identifiers
- "/vs/classplus" -> "/vs/<competitor_lower>"
- "https://classplus.co" -> appropriate URL
- "white-label app builder" -> custom positioning per competitor
- Wikipedia anchor URL per competitor

Preserves all structure, schemas, design, math, FAQ — only swaps competitor identity.
"""
import sys, re, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

COMPETITORS = {
    'graphy': {
        'name': 'Graphy',
        'lower': 'graphy',
        'url': 'https://graphy.com',
        'wiki': '',
        'positioning': 'Course platform / LMS for creators',
        'tag': 'Course platform builder',
        'description_short': 'Graphy is a Unacademy-owned LMS-style course platform builder primarily targeting individual content creators selling pre-recorded courses globally.',
        'pricing_per_month_low': '2999',
        'pricing_per_month_high': '34999',
        'commission_low': '0',  # Graphy uses subscription, no commission on most plans
        'commission_high': '5',
        'fits_when': [
            'You sell <strong style="color:#15110D;">pre-recorded video courses globally</strong> (not India-specific exam coaching).',
            'You don\'t need live class infrastructure or test series.',
            'You\'re fine with <strong style="color:#15110D;">no marketplace discovery</strong> — you have an existing audience.',
            'You can afford ₹30K–₹4L/year subscription with no commission flexibility.'
        ]
    },
    'teachmint': {
        'name': 'Teachmint',
        'lower': 'teachmint',
        'url': 'https://teachmint.com',
        'wiki': '',
        'positioning': 'White-label classroom infrastructure for institutes',
        'tag': 'Institute classroom builder',
        'description_short': 'Teachmint is a classroom infrastructure / white-label platform serving K-12 schools and traditional institutes, with strong attendance + administration features.',
        'pricing_per_month_low': '5000',
        'pricing_per_month_high': '50000',
        'commission_low': '2',
        'commission_high': '5',
        'fits_when': [
            'You run a <strong style="color:#15110D;">traditional K-12 school or institute</strong> with admin staff handling enrolment.',
            'You need <strong style="color:#15110D;">deep attendance + report card workflows</strong> for institute administration.',
            'You\'re not selling to individual learners on a marketplace.',
            'Your institute has ₹2 Cr+ revenue and dedicated admin/marketing staff.'
        ]
    }
}

def clone_for(competitor_key):
    if competitor_key not in COMPETITORS:
        print(f"Unknown competitor: {competitor_key}")
        return

    comp = COMPETITORS[competitor_key]
    source_path = os.path.join(ROOT, 'vs', 'classplus.html')
    target_path = os.path.join(ROOT, 'vs', f'{competitor_key}.html')

    with open(source_path, 'r', encoding='utf-8') as fp:
        text = fp.read()

    # Simple identity swaps
    text = text.replace('Classplus', comp['name'])
    text = text.replace('/vs/classplus', f"/vs/{comp['lower']}")
    text = text.replace('classplus-vs-graphy-vs-allcoaching', 'classplus-vs-graphy-vs-allcoaching')  # blog ref unchanged
    text = text.replace('https://classplus.co', comp['url'])
    text = text.replace('https://en.wikipedia.org/wiki/Classplus', comp['wiki'] or 'https://en.wikipedia.org/wiki/Educational_technology')

    # Fix the cross-link in CTA section (currently says vs/graphy + vs/teachmint, exclude self)
    if competitor_key == 'graphy':
        text = text.replace(
            '<a href="/vs/graphy" style="color:#8E5F22; text-decoration:underline;">AllCoaching vs Graphy</a>',
            '<a href="/vs/classplus" style="color:#8E5F22; text-decoration:underline;">AllCoaching vs Classplus</a>'
        )
    elif competitor_key == 'teachmint':
        text = text.replace(
            '<a href="/vs/teachmint" style="color:#8E5F22; text-decoration:underline;">AllCoaching vs Teachmint</a>',
            '<a href="/vs/classplus" style="color:#8E5F22; text-decoration:underline;">AllCoaching vs Classplus</a>'
        )

    # Fix nav footer cross-link (mark self as active)
    text = text.replace(
        f'<li><a href="/vs/{competitor_key}" class="hover:text-[#15110D]">vs {comp["name"]}</a></li>',
        f'<li><a href="/vs/{competitor_key}" class="hover:text-[#15110D] font-semibold">vs {comp["name"]}</a></li>'
    )
    # And remove font-semibold from classplus footer link (since it's no longer the active page)
    text = text.replace(
        '<li><a href="/vs/classplus" class="hover:text-[#15110D] font-semibold">vs Classplus</a></li>',
        '<li><a href="/vs/classplus" class="hover:text-[#15110D]">vs Classplus</a></li>'
    )

    # Adjust description tag
    text = text.replace(
        f'<div class="vs-tag">White-label app builder</div>',
        f'<div class="vs-tag">{comp["tag"]}</div>'
    )

    # Adjust some context-specific phrasings that don't translate well
    if competitor_key == 'graphy':
        text = text.replace(
            'white-label coaching app builder',
            'creator LMS / course platform'
        )
    elif competitor_key == 'teachmint':
        text = text.replace(
            'white-label coaching app builder',
            'classroom infrastructure platform'
        )

    with open(target_path, 'w', encoding='utf-8', newline='\n') as fp:
        fp.write(text)

    print(f"Wrote {target_path} ({len(text)} chars)")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        clone_for(sys.argv[1])
    else:
        for key in COMPETITORS:
            clone_for(key)
