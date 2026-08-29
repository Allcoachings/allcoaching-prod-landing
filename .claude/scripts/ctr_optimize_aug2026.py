"""
CTR + relevance optimisation pass, driven by the GSC export (3 months to 2026-08-26).

Principle applied throughout: the title must answer the query, not describe the page.
GSC evidence in this dataset:
  - budget-home-studio-setup has Rs 15,000 IN the title -> 2.45% CTR
  - appx-vs-classplus is an exact query match      -> 6.86% CTR (site's best)
  - pages with vague/brand-first titles            -> 0.17%-1.2% CTR

Also aligns with Google's current guidance: 50-60 char titles, front-loaded
primary keyword, and descriptions in the 105-155 band (longer ones get
truncated in the SERP, which is why several here were shortened).

Each entry records the query evidence that justifies the change.
"""
import re, sys

CHANGES = [
    {
        'file': 'vs/classplus.html',
        # gap 379 clicks/qtr. Queries: "classplus pricing" 1177 impr @4.03,
        # "class plus app charges" 368, "classplus app price" 285.
        # Pricing intent wants the NUMBER in the SERP, not "Is It Free?".
        'title': 'Classplus Pricing 2026: ₹8,000–₹50,000/yr + Commission',
        'desc': 'Classplus pricing is quote-based — reportedly ₹8,000–₹50,000+ a year, plus a setup fee and a cut of your sales. The full 2026 breakdown.',
    },
    {
        'file': 'blog/coaching-centre-library-safety-norms-avoid-sealing-india.html',
        # gap 342. Best-converting queries are NOC ones: "fire safety rules for
        # coaching classes" 9.38% CTR, "fire noc for coaching institute" @4.23,
        # "noc for coaching institute" @3.48. Title said neither "fire NOC" nor "sealing".
        'title': 'Coaching Centre Fire NOC and Sealing Rules in India (2026)',
        'desc': 'Why coaching centres and libraries are being sealed in India — fire NOC, basement bans and capacity limits, and how to stay compliant. Not legal advice.',
    },
    {
        'file': 'blog/new-coaching-center-rules-india-2026.html',
        # gap 250. "What Every Educator Must Know" was 30 chars of filler at the
        # 65-char limit. Queries want "guidelines" + "centre": "new coaching
        # guidelines" @4.68, "guidelines for coaching institutes" @6.82.
        'title': 'New Coaching Centre Rules in India 2026: Full Guidelines',
        'desc': 'New coaching centre rules in India for 2026 — the Coaching Centre Guidelines 2024, no under-16 enrolment, CCPA ad limits and DPDP data rules explained.',
    },
    {
        'file': 'blog/gst-for-coaching-institutes-india.html',
        # gap 161, and the clearest miss in the dataset. The page ranks
        # "sac code 999293" @1.56, "999293 sac code" @3.59, "999293" 122 impr
        # @6.68 - roughly 243 impressions on the SAC code alone, 1 click.
        # The code was nowhere in the title.
        'title': 'GST on Coaching Fees: 18%, SAC 999293, ITC Rules (2026)',
        'desc': 'GST on coaching fees in India is 18% under SAC 999293. Registration at ₹20 lakh turnover, input tax credit, and reverse charge on rent. Not tax advice.',
    },
    {
        'file': 'vs/graphy.html',
        # gap 52 but the title was 74 chars (truncated in SERP) and brand-first.
        # "graphy pricing" 398 impr @6.09 plus ~120 more across pricing variants.
        'title': 'Graphy Pricing 2026: Plans, Fees and a ₹0 Alternative',
        'desc': 'What Graphy actually costs in 2026 — plans, transaction fees and the total you pay per sale, next to a ₹0-to-start alternative for Indian educators.',
    },
    {
        'file': 'vs/teachmint.html',
        # 591 impressions, 1 click, 0.17% - worst CTR on the site. Title was
        # 77 chars and brand-first. Queries: "teachmint" 280 impr @2.4,
        # "teachmint pricing" @5.67, "teachmint app price" @3.73.
        'title': 'Teachmint Pricing 2026: Plans, Fees and a ₹0 Alternative',
        'desc': 'What Teachmint actually costs in 2026 — plans, per-sale fees and what is free, next to a ₹0-to-start alternative for Indian coaching educators.',
    },
    {
        'file': 'blog/classplus-vs-graphy-vs-allcoaching.html',
        # gap 137. "graphy vs classplus" 150 impr @2.79 is the bigger query and
        # was buried third in the title. Front-load it.
        'title': 'Graphy vs Classplus vs AllCoaching: 2026 Pricing Verdict',
        'desc': 'Graphy vs Classplus vs AllCoaching in 2026 — what each really costs per sale, and which one actually brings you students instead of just an app.',
    },
    {
        'file': 'blog/affordable-lms-for-independent-educators.html',
        # gap 122. Queries want India + price: "lms pricing in india" @5.96,
        # "lms cost in india" @4.97, "cheapest lms platform", "affordable lms".
        # "Real-Cost Guide" told the searcher nothing.
        'title': 'Affordable LMS in India 2026: Real Pricing vs ₹0 Options',
        'desc': 'What an LMS really costs in India in 2026 — subscription pricing compared against a ₹0-to-start platform that also sends you students.',
    },
    {
        'file': 'blog/teachmint-paid-features-alternative-free.html',
        # gap 92 @5.07. Title was 66 chars and led with brand-swap framing.
        'title': 'Teachmint Paid Features: Free Alternative for Teachers 2026',
        'desc': 'Which Teachmint paid features matter, and how Indian teachers get the same capability free — branded app, fee collection and student records at ₹0.',
    },
    {
        'file': 'blog/best-upi-payment-gateway-for-online-courses.html',
        # gap 230 but position 9.06 is the real constraint, and most of the
        # 10,843 impressions are generic fintech queries, not educators.
        # Retitled to be educator-specific so the page competes for the subset
        # it can actually win rather than the whole payments market.
        'title': 'UPI Payment Gateway for Course Sellers: Real Charges 2026',
        'desc': 'UPI looks free, but most gateways still take 1.5–2% plus GST on every course sale. What Indian educators actually pay, and the ₹0 options.',
    },
]


def clen(s):
    """Length as the HTML validator sees it (entities expanded)."""
    return len(s.replace('&', '&amp;'))


def apply(path, title, desc, dry=False):
    h = open(path, encoding='utf-8').read()
    orig = h
    t_esc = title.replace('&', '&amp;')
    d_esc = desc.replace('&', '&amp;').replace('"', '&quot;')

    old_t = re.search(r'<title>(.*?)</title>', h, re.DOTALL)
    old_d = re.search(r'<meta name="description" content="([^"]*)"', h)
    if not old_t or not old_d:
        return None, 'SKIP (no title/description)'

    h = re.sub(r'<title>.*?</title>', '<title>%s</title>' % t_esc, h, count=1, flags=re.DOTALL)
    h = re.sub(r'<meta name="description" content="[^"]*"',
               '<meta name="description" content="%s"' % d_esc, h, count=1)
    # keep social cards in sync with the SERP title
    h = re.sub(r'(<meta property="og:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % t_esc, h, count=1)
    h = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', r'\g<1>%s\g<2>' % t_esc, h, count=1)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % d_esc, h, count=1)
    h = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")', r'\g<1>%s\g<2>' % d_esc, h, count=1)

    if not dry:
        open(path, 'w', encoding='utf-8').write(h)
    return (old_t.group(1), old_d.group(1)), ('OK' if h != orig else 'NO-CHANGE')


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    bad = 0
    for c in CHANGES:
        tl, dl = clen(c['title']), clen(c['desc'])
        flag = ''
        if tl > 65:
            flag += ' TITLE-TOO-LONG'; bad += 1
        if not (50 <= dl <= 175):
            flag += ' DESC-OUT-OF-RANGE'; bad += 1
        old, status = apply(c['file'], c['title'], c['desc'], dry)
        print('%-58s T=%-3d D=%-3d %s%s' % (c['file'].split('/')[-1][:56], tl, dl, status, flag))
        if old:
            print('    was: %s' % old[0][:70])
            print('    now: %s' % c['title'][:70])
    print('\n%d files, %d validation problems' % (len(CHANGES), bad))
    print('dry run only' if dry else 'applied')
