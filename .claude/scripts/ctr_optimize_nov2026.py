"""
CTR pass driven by the GSC export of 2026-11-11 (last 3 months: 3,006 clicks, 193,769 impressions).
Principle (same as ctr_optimize_aug2026.py): the title answers the query the page already ranks for.
Each entry records the query evidence. Also syncs JSON-LD, v3 content JSON, llms.txt, indexes and feed.
"""
import re, sys, os, json, glob, html
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
os.chdir(ROOT)

CHANGES = [
    # 18,854 impr, 0.65% CTR, pos 4.9. "999293" 1,295 impr, "sac 999293" 310, "999293 sac" 251, "hsn 999293" 169: ~2,400 impr, 2 clicks.
    ('blog/gst-for-coaching-institutes-india.html',
     'SAC Code 999293: 18% GST on Coaching Fees Explained (2026)',
     'SAC 999293 is the GST code for commercial training and coaching services. GST rate: 18%. Registration at ₹20 lakh, input tax credit and reverse charge. Not tax advice.'),
    # 10,490 impr, 1.36%, pos 4.4. "classplus pricing" 1,333 @2.3 (1.8% CTR), "class plus app charges" 487, "classplus app price" 320. Searchers want the number.
    ('vs/classplus.html',
     'Classplus Pricing 2026: ₹29,999 a Year, App Charges Checked',
     'Classplus pricing in 2026: its official page lists ₹29,999 for 1 year and ₹39,999 for 2 years. GST and per-sale fees are not stated. Compare AllCoaching from ₹3,999 a month.'),
    # 10,205 impr, 0.82%, pos 9.5. "free upi payment gateway" 610, "upi payment gateway without kyc" 196, "free payment gateway for upi" 121.
    ('blog/best-upi-payment-gateway-for-online-courses.html',
     'Free UPI Payment Gateway in India? Real Charges in 2026',
     'Is there a free UPI payment gateway in India? Not fully: most gateways charge 1.5–2% plus GST on each course sale, and all need KYC. What educators really pay in 2026.'),
    # 3,761 impr, 1.33%. "graphy pricing" 634 @4.2. Graphy's page changed (checked 11 Nov 2026), so the title carries the fee range, not plan prices.
    ('vs/graphy.html',
     'Graphy Pricing 2026: Plans, 5–10% Per-Sale Fee, Real Cost',
     'Graphy pricing in 2026: paid plans plus a 5% to 10% fee on every sale. What you pay in total at your sales level, next to AllCoaching at 0% commission from ₹3,999 a month.'),
    # 1,869 impr in 5 days, 0.05% CTR, pos 4.3. "classplus diy" 1,303 @3.6, "diy classplus" 202: mostly people looking for the DIY page or login.
    ('blog/classplus-diy-alternative.html',
     'Classplus DIY: Login Link, Price and What You Get (2026)',
     'Classplus DIY login is at classplusapp.com/diy/login. It is the self-serve sign-up to make your own app. Listed price ₹29,999 a year, what is not stated, and what to check.'),
    # 5,254 impr, 1.22%, pos 7.1. "home tuition app" 115, "best app for home tutors" 69, "home tuition app for students" 42: 0 clicks.
    ('blog/best-app-for-home-tutors-to-manage-students-and-fees.html',
     'Home Tuition App for Tutors: Manage Students & Fees (2026)',
     'A home tuition app for tutors in India to manage students, attendance and fees. What to track, why a diary breaks past 20 students, and how to run it all from one app.'),
    # 11,804 impr, 0.91%, pos 6.5. "online tuition kaise start kare" 67 @3.8 (0 clicks), "online tuition kaise padhaye" 60.
    ('blogs/hinglish/online-tuition-class-kaise-shuru-kare-aur-paise-kamaye.html',
     'Online Tuition Kaise Start Kare: Ghar Se Kamai Guide (2026)',
     'Online tuition kaise start kare aur ghar se kaise padhaye? 2026 ka step-by-step roadmap: setup, fees, pehle 10 paying students aur pehli kamai.'),
    # 7,426 impr, 0.08%. "hindi lms" 80, "lms hindi" 47, "multilanguage lms" 140 @33.
    ('blog/multi-language-lms-for-regional-indian-languages.html',
     'Hindi LMS & Multi-Language LMS for Indian Educators (2026)',
     'Looking for a Hindi LMS or a multi-language LMS? Translated menus are not enough. Best practices for Hindi, Marathi, Tamil and Bengali academies in 2026.'),
    # 7,558 impr, 1.75%. "how to record video lecture on laptop for free" 91 @7.3, 0 clicks.
    ('blog/best-free-tools-for-teachers-to-record-lectures.html',
     'Record Video Lectures on a Laptop Free: 6 Best Tools (2026)',
     'How to record video lectures on a laptop for free in 2026: OBS Studio, Loom, ScreenPal, DaVinci Resolve, CapCut and Descript, with honest pros and cons for teachers.'),
    # 3,433 impr, 1.78%, pos 7.7. "pw alternatives" 153 (0 clicks), "pw alternative app" 106, "pw alternative" 92.
    ('blog/physics-wallah-alternative-for-educators.html',
     'PW Alternative for Teachers (2026): Start Your Own App',
     'Looking for a PW alternative as a teacher? What Physics Wallah publishes about faculty roles, what it does not, and how JEE and NEET teachers start their own app safely.'),
    # 2,657 impr, 0.53%. Description was cut mid-sentence and carried an unsourced "90%".
    ('blogs/hinglish/online-home-tuition-kaise-shuru-kare.html',
     'Online Home Tuition Kaise Shuru Kare: Ghar Se Guide (2026)',
     'Online home tuition kaise shuru kare? Ghar se live batches, board-pattern practice aur doubt-solving apne branded app par. Setup, fees aur pehle students ka plan.'),
    # 1,954 impr, 0.61%, pos 5.8.
    ('blog/how-much-can-you-earn-teaching-online-india.html',
     'How Much Do Online Teachers Earn in India? Calculator (2026)',
     'How much do online teachers earn in India? Students × price, minus platform fee, plan cost and ads. Free income calculator, 3 worked examples and tax notes.'),
]

def E(s): return s.replace('&', '&amp;')
def run(dry=False):
    reg = [p for p in ['llms.txt', 'feed.xml', 'blog/index.html', 'blogs/index.html', 'blogs/en/index.html', 'blogs/hinglish/index.html', 'sitemap.xml'] if os.path.exists(p)]
    bad = 0
    for path, title, desc in CHANGES:
        h = open(path, encoding='utf-8').read()
        ot = re.search(r'<title>(.*?)</title>', h, re.S).group(1).strip()
        od = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
        tl, dl = len(title), len(desc)
        if tl > 60 or not 120 <= dl <= 175: bad += 1; print('!! length', path, tl, dl)
        te, de = E(title), E(desc).replace('"', '&quot;')
        n = h.replace(ot, te).replace(od, de)
        # JSON-LD and plain-text copies (unescaped variants)
        for a, b in [(html.unescape(ot), title), (html.unescape(od), desc)]:
            n = n.replace(json.dumps(a, ensure_ascii=False)[1:-1], json.dumps(b, ensure_ascii=False)[1:-1])
        if not dry: open(path, 'w', encoding='utf-8').write(n)
        slug = os.path.basename(path)[:-5]
        cj = '.claude/skills/academy-guide-blog/content/%s.json' % slug
        if os.path.exists(cj):
            j = json.load(open(cj, encoding='utf-8')); j['title'] = title; j['description'] = desc
            if 'og_description' in j: j['og_description'] = desc
            if not dry: json.dump(j, open(cj, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        hits = 0
        for r in reg:
            t = open(r, encoding='utf-8').read(); o = t
            for a, b in [(ot, te), (html.unescape(ot), title), (od, de), (html.unescape(od), desc)]:
                t = t.replace(a, b)
            if t != o:
                hits += 1
                if not dry: open(r, 'w', encoding='utf-8').write(t)
        print('%-62s T=%d D=%d registries=%d\n    was: %s\n    now: %s' % (path[-62:], tl, dl, hits, html.unescape(ot), title))
    print('\n%d pages, %d problems, %s' % (len(CHANGES), bad, 'dry run' if dry else 'applied'))

if __name__ == '__main__':
    run('--dry-run' in sys.argv)
