"""
Build the vertical ad landing pages: /onboarding-<slug>  (onboarding-<slug>.html at the repo root).

The /onboarding- prefix is load-bearing: the live GTM container fires the Meta Pixel
InitiateCheckout (and GA4 onboarding_cta_click) on a click on a studio link only when the page
path contains "/onboarding". Keep it for every new campaign page.

    python scripts/build_lp.py

Stdlib only. Copy lives in PAGES below; styles in templates/lp/lp.css (inlined into
each page); the on-page checkout is /assets/checkout.js (shared by every campaign page).

Each page:
  - is an ad destination: noindex, no site nav, one action (open the checkout)
  - sells the studio to one vertical (ids match studio's VerticalId)
  - pushes the same ob_* funnel events as /onboarding, with page='lp_<slug>'
  - opens the checkout on every CTA; the checkout signs up, takes payment and
    hands the educator to studio, firing studio's own conversion events

To add a campaign page: copy one PAGES entry, change slug/copy/offer, rebuild.
An offer is just `coupon` (an activation code made in the admin), applied automatically.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT
CSS = (ROOT / "templates" / "lp" / "lp.css").read_text(encoding="utf-8")
STUDIO = "https://studio.allcoaching.in/"
WA = "https://api.whatsapp.com/send/?phone=919889977262&text="

# ─────────────────────────────────────────────────────────────────────────────
# Page copy. Facts must match the allcoaching skill: 14-day trial, Starter ₹6,999 /
# Growth ₹12,999 / Pro ₹24,999 a year + GST, keep 90/92.5/95%, 500+ educators,
# no payout-speed claims, no DRM claims, no fabricated stats.
# ─────────────────────────────────────────────────────────────────────────────
PAGES = [
    {
        "slug": "competitive-exams",
        "vertical": "competitive",
        "plan": "growth",
        "coupon": "",
        "title": "Your Own Govt Exam Coaching App & Website | AllCoaching",
        "desc": "Build your own UPSC, SSC, Banking and State PSC coaching academy in a few clicks: mock tests with ranks, courses, PDFs and live classes under your brand.",
        "pill": "For UPSC, SSC, Banking &amp; State PSC educators",
        "h1_lt": "Your test series, courses and live classes.",
        "h1_bd": "Your own exam-prep academy.",
        "lede": "Build your own LMS for government exam prep in a few clicks: mock tests with ranks, recorded courses, PDF notes and live classes, <b>on your own website and app, under your name.</b> No developer, no sales call.",
        "chip1": ("i-test", "SSC CGL Mock 07 published", "Timer · negative marking"),
        "chip2": ("i-live", "Daily current affairs · Live", "Recording saved for later"),
        "who": "Built for educators who teach government exams",
        "exams": ["UPSC CSE", "SSC CGL", "SSC CHSL", "IBPS PO", "SBI Clerk", "RRB NTPC", "NDA &amp; CDS", "UPPSC", "BPSC", "RPSC", "CTET", "Judiciary"],
        "pain_h": ("Aspirants want a serious academy.", "Give them one with your name on it."),
        "pains": [
            ("Mock tests on Google Forms and ranks in Excel", "Real mock tests with ranks", "Upload questions from a DOCX, set the timer and negative marking. Every attempt lands on a leaderboard."),
            ("Your PDFs forwarded free on Telegram groups", "Notes behind a login", "PDF notes and videos open only for students who have paid for them."),
            ("Collecting fees on WhatsApp and checking screenshots", "Students pay, access opens", "UPI and card checkout. Access opens the moment an aspirant pays."),
            ("Current affairs scattered across five apps", "One feed for your students", "Post updates, polls and quizzes to your students from the same studio."),
            ("Only your YouTube followers ever find your course", "Found by new aspirants", "Your courses are also listed on the AllCoaching app, where students search by exam."),
            ("A big platform's name sitting on top of yours", "Your brand, your domain", "Your logo and colours on your own domain, like yourias.in."),
        ],
        "bp_h": ("What a government-exam academy", "looks like on AllCoaching."),
        "bp_lede": "Sell a test series, a full course and live revision side by side, and give a free demo so aspirants can judge you before they pay.",
        "bp_points": [
            "<b>Test series</b> with timer, negative marking and ranks",
            "<b>Recorded courses</b> with lectures and PDF notes together",
            "<b>Live classes</b> for daily current affairs and revision",
            "<b>Free demo content</b> so aspirants can try before they buy",
        ],
        "academy": {
            "url": "yourias.in", "mark": "P", "name": "Prayas IAS Academy", "tag": "UPSC · UPPSC · current affairs",
            "items": [
                ("i-test", "Test series", "Prelims GS · 30 full mocks", "With ranks and solutions", "₹1,499"),
                ("i-layout", "Course", "Polity for Prelims", "60 lectures + PDF notes", "₹2,999"),
                ("i-live", "Live", "Daily current affairs", "8 am, Monday to Saturday", "₹499/mo*"),
                ("i-brand", "Free", "Demo: 3 lectures + 1 mock", "No payment needed", "Free"),
            ],
            "foot": "Example academy. Prices are illustrative and set by the educator. *Sold as a course with a validity you choose.",
        },
        "calc": {"students": 120, "price": 1499, "h": "Your test series, your numbers"},
        "faq": [
            ("Can I run a full test series with negative marking?", "<strong>Yes.</strong> Upload questions from a DOCX file, set the timer and negative marking, and publish. Every attempt is ranked on a leaderboard students can see."),
            ("Can I teach and test in Hindi?", "<strong>Yes.</strong> Your lectures, notes and questions can be in Hindi, English or any language you teach in."),
            ("Can I sell a test series separately from my course?", "<strong>Yes.</strong> Each course and test series has its own price, so aspirants can buy only the mocks, only the course, or both."),
        ],
        "wa_text": "Hi AllCoaching, I teach government exams and want to start my own academy.",
    },
    {
        "slug": "jee-neet",
        "vertical": "entrance",
        "plan": "growth",
        "coupon": "",
        "title": "Your Own JEE & NEET Coaching App & Website | AllCoaching",
        "desc": "Build your own JEE and NEET coaching academy in a few clicks: lectures, DPPs, mock tests with ranks and live doubt classes, on your own website and app.",
        "pill": "For JEE, NEET &amp; Foundation educators",
        "h1_lt": "Your JEE and NEET coaching,",
        "h1_bd": "online under your own name.",
        "lede": "Lectures, DPPs, mock tests with ranks and live doubt classes. <b>Your own website and student app, built in a few clicks.</b> No developer, no sales call.",
        "chip1": ("i-test", "NEET Full Mock 12 published", "Timer · negative marking"),
        "chip2": ("i-live", "Live doubt class · Physics", "Recording saved for later"),
        "who": "Built for JEE, NEET and Foundation educators",
        "exams": ["JEE Main", "JEE Advanced", "NEET UG", "BITSAT", "MHT CET", "WBJEE", "KCET", "Foundation 9–10", "NTSE", "Olympiads", "Class 11 Physics", "Class 12 Chemistry"],
        "pain_h": ("Your results are your brand.", "Your academy should carry it."),
        "pains": [
            ("DPPs sent as WhatsApp images with no record of who solved what", "Tests with real results", "Timed tests with negative marking, attempt history and a rank list for every batch."),
            ("A missed live class means a missed chapter", "Live classes, recorded", "Hold live doubt classes and keep the recording for students who missed them."),
            ("Your notes and lectures leaked on Telegram", "Content behind a login", "Videos and PDFs open only for students enrolled in that course."),
            ("Diagrams turning to blur in compressed videos", "1080p, or 4K on Pro", "Ray diagrams, reaction mechanisms and graphs stay readable."),
            ("Fees on WhatsApp and payment screenshots to check", "Students pay, access opens", "UPI and card checkout. Access opens the moment the payment lands."),
            ("Your name hidden behind a big brand's batches", "Your academy, your app", "Your logo and colours on your own domain and in the student app."),
        ],
        "bp_h": ("What a JEE and NEET academy", "looks like on AllCoaching."),
        "bp_lede": "Run separate batches for Class 11, Class 12 and droppers, sell mock series on their own, and let co-teachers handle their subjects.",
        "bp_points": [
            "<b>Batches</b> as separate courses, each with its own price and students",
            "<b>Mock test series</b> with ranks, sold on their own or bundled",
            "<b>Live doubt classes</b> with recordings kept for later",
            "<b>Co-teachers</b> with their own logins for Physics, Chemistry and Biology",
        ],
        "academy": {
            "url": "vectorclasses.in", "mark": "V", "name": "Vector Classes", "tag": "JEE · NEET · Class 11–12",
            "items": [
                ("i-layout", "Course", "JEE 2027 crash course", "120 lectures + DPPs", "₹14,999"),
                ("i-test", "Test series", "NEET full mock series", "25 mocks with ranks", "₹1,999"),
                ("i-live", "Live", "Doubt classes", "Monday to Saturday, 7 pm", "Included"),
                ("i-brand", "Free", "Demo: Physics chapter 1", "No payment needed", "Free"),
            ],
            "foot": "Example academy. Prices are illustrative and set by the educator.",
        },
        "calc": {"students": 40, "price": 14999, "h": "Your batch, your numbers"},
        "faq": [
            ("Can I run separate batches for Class 11, Class 12 and droppers?", "<strong>Yes.</strong> Create each batch as its own course with its own price, content and students."),
            ("Can my co-teachers upload their own subjects?", "<strong>Yes.</strong> Invite teachers with their own logins. Your institute decides how it pays them."),
            ("Do mock tests support negative marking?", "<strong>Yes.</strong> Set the timer and negative marking per test. Students see their score and rank after every attempt."),
        ],
        "wa_text": "Hi AllCoaching, I teach JEE/NEET and want to start my own academy.",
    },
    {
        "slug": "school-tuition",
        "vertical": "school",
        "plan": "starter",
        "coupon": "",
        "title": "Take Your Tuition Classes Online, Your Brand | AllCoaching",
        "desc": "Take your Class 1–12 tuition online in a few clicks: chapter-wise lectures, notes, tests and live classes for CBSE, ICSE and state boards, with fees paid online.",
        "pill": "For CBSE, ICSE &amp; state board teachers",
        "h1_lt": "Your tuition classes,",
        "h1_bd": "now an online academy.",
        "lede": "Chapter-wise lectures, notes, tests and live classes for Class 1 to 12. <b>On your own website and app, with fees paid online.</b> No developer, no sales call.",
        "chip1": ("i-layout", "Class 10 Maths · Chapter 4", "Lecture + notes published"),
        "chip2": ("i-rupee", "Fee paid by UPI", "Access opened instantly"),
        "who": "Built for school teachers and tuition centres",
        "exams": ["CBSE", "ICSE", "UP Board", "Bihar Board", "Maharashtra Board", "RBSE", "MP Board", "Class 10 Maths", "Class 12 Physics", "Class 9 Science", "Class 12 Accountancy", "Spoken English"],
        "pain_h": ("Parents trust teachers they can see.", "Show them your academy."),
        "pains": [
            ("Only students within a few kilometres can join your tuition", "Teach students in any city", "Students learn on your website and app, and new ones find you on the AllCoaching app."),
            ("Chasing fees every month", "Fees paid online first", "UPI and card checkout. Access opens only after the payment."),
            ("Notes photocopied and passed around", "Notes behind a login", "PDF notes and videos open only for students who have paid."),
            ("Teaching the same chapter again for every batch", "Record once, reuse", "Recorded lectures serve every batch, and live classes are for doubts."),
            ("No way to check who understood the chapter", "Tests after every chapter", "Quick timed tests with scores, so you know who needs help."),
            ("New parents have no way to judge you", "Free demo lectures", "Give a free chapter so parents can try your teaching before paying."),
        ],
        "bp_h": ("What a tuition academy", "looks like on AllCoaching."),
        "bp_lede": "Organise by class, subject and chapter. Sell the full year, or one subject, and keep a free demo up for new parents.",
        "bp_points": [
            "<b>Chapter-wise courses</b> by class, board and subject",
            "<b>Chapter tests</b> with scores after every attempt",
            "<b>Live classes</b> for doubts and board revision",
            "<b>Teach in Hindi, English</b> or your state language",
        ],
        "academy": {
            "url": "guptatuitions.in", "mark": "G", "name": "Gupta Tuition Centre", "tag": "CBSE · UP Board · Class 9–12",
            "items": [
                ("i-layout", "Course", "Class 10 Maths · full year", "Chapter-wise lectures + notes", "₹2,999"),
                ("i-layout", "Course", "Class 12 Physics · boards", "Revision + previous papers", "₹3,499"),
                ("i-test", "Tests", "Weekly chapter tests", "Scores after every attempt", "Included"),
                ("i-brand", "Free", "Demo: 2 lectures", "No payment needed", "Free"),
            ],
            "foot": "Example academy. Prices are illustrative and set by the educator.",
        },
        "calc": {"students": 60, "price": 2999, "h": "Your classes, your numbers"},
        "faq": [
            ("Can I teach in Hindi or my state language?", "<strong>Yes.</strong> Lectures, notes and tests can be in any language you teach in."),
            ("I run a small tuition centre with 2–3 teachers. Does that work?", "<strong>Yes.</strong> Each teacher gets their own login. Your centre decides how it pays them."),
            ("Can students study on their phones?", "<strong>Yes.</strong> Students use your website in the browser, or the AllCoaching app on Android and iOS."),
        ],
        "wa_text": "Hi AllCoaching, I run tuition classes and want to take them online.",
    },
    {
        "slug": "skills",
        "vertical": "skills",
        "plan": "starter",
        "coupon": "",
        "title": "Sell Your Skill Courses on Your Own Academy | AllCoaching",
        "desc": "Turn your skill into your own online academy in a few clicks: recorded courses, live sessions and coupons, sold on your own website and app.",
        "pill": "For coaches of coding, English, trading, yoga &amp; more",
        "h1_lt": "Turn your skill into",
        "h1_bd": "your own online academy.",
        "lede": "Recorded courses, live sessions and launch offers. <b>Sold on your own website and app, at your price.</b> No developer, no sales call.",
        "chip1": ("i-globe", "youracademy.in", "Connected · your brand"),
        "chip2": ("i-rupee", "Paid by UPI · ₹1,999", "Course access opened"),
        "who": "Built for people who teach a skill",
        "exams": ["Spoken English", "Python", "Web development", "Excel", "Digital marketing", "Stock market", "Graphic design", "Video editing", "Yoga", "Music", "IELTS", "Drawing"],
        "pain_h": ("Your audience already trusts you.", "Give them somewhere to buy."),
        "pains": [
            ("Selling on big course marketplaces at their price, under their name", "Your price, your brand", "You set the price, the discounts and the look of your academy."),
            ("Course links shared around in DMs", "Content behind a login", "Lessons open only for learners who have paid."),
            ("Launch offers run by hand in chats", "Coupons and offers", "Create coupon codes for launches and festivals in the studio."),
            ("Followers on Instagram but nowhere to sell", "A real academy behind your bio link", "Your own domain with course pages, checkout and a student app."),
            ("Live batches on one app, recordings on another", "Live and recorded together", "Live sessions included every month, alongside your recorded courses."),
            ("Payments, content and students in five different tools", "One studio", "Courses, payments, live sessions and learners in one login."),
        ],
        "bp_h": ("What a skills academy", "looks like on AllCoaching."),
        "bp_lede": "Sell a self-paced course, add live practice, and run a launch offer with a coupon. Your first lesson can be free.",
        "bp_points": [
            "<b>Self-paced courses</b> with video lessons and downloads",
            "<b>Live sessions</b> for practice, Q&amp;A and feedback",
            "<b>Coupons</b> for launches, festivals and early learners",
            "<b>Community posts</b>, polls and quizzes for your learners",
        ],
        "academy": {
            "url": "speakwithneha.in", "mark": "N", "name": "Speak with Neha", "tag": "Spoken English · interview prep",
            "items": [
                ("i-layout", "Course", "Spoken English in 60 days", "40 lessons + worksheets", "₹1,999"),
                ("i-live", "Live", "Weekend speaking practice", "Small groups, every Saturday", "₹999"),
                ("i-layout", "Course", "Interview English", "15 lessons + mock interviews", "₹1,499"),
                ("i-brand", "Free", "First lesson", "No payment needed", "Free"),
            ],
            "foot": "Example academy. Prices are illustrative and set by the educator.",
        },
        "calc": {"students": 150, "price": 1999, "h": "Your course, your numbers"},
        "faq": [
            ("I teach a hobby, not an exam. Is this for me?", "<strong>Yes.</strong> Skills and hobbies are a full category, from coding and trading to yoga and music."),
            ("Can I run a launch offer?", "<strong>Yes.</strong> Create coupon codes in the studio and share them with your audience."),
            ("Do my learners need to download an app?", "<strong>No.</strong> They can learn on your website in the browser, or use the AllCoaching app on Android and iOS."),
        ],
        "wa_text": "Hi AllCoaching, I teach a skill and want to start my own academy.",
    },
]

COMMON_FAQ = [
    ("How does the 14-day free trial work?", "<strong>Pick the free trial in the last step.</strong> You get the Starter plan for 14 days, no card needed. After that, choose a plan to keep your academy live. Or pick a plan and pay now to go live on it straight away."),
    ("What do I pay, and when?", "<strong>One yearly plan:</strong> Starter ₹6,999, Growth ₹12,999 or Pro ₹24,999 a year, plus GST. No setup fee and no monthly bill. You pay once a year, securely through Razorpay by UPI, card or netbanking."),
    ("I'm not technical. Can I really build it myself?", "<strong>Yes.</strong> Everything is drag and drop. If you can use WhatsApp, you can set up your academy. If you get stuck, message us on WhatsApp."),
    ("How much of each sale do I keep?", "<strong>90% on Starter, 92.5% on Growth and 95% on Pro.</strong> Your share is paid out to your bank automatically."),
    ("Do I pay extra for my own domain?", "<strong>No.</strong> Connecting your domain is included on every plan. The only thing you buy separately is the domain name itself, about ₹600–1,200 a year, registered in your own name."),
    ("Can I upgrade later?", "<strong>Yes, any time.</strong> Upgrades take effect when payment clears, and what you already paid this year is credited."),
    ("What happens if I do not renew?", "<strong>Your academy goes offline</strong> at the end of your paid year. Your content and student data stay exportable, and renewing brings it back."),
]

OTHERS = [("competitive-exams", "Government exams"), ("jee-neet", "JEE &amp; NEET"), ("school-tuition", "School &amp; tuition"), ("skills", "Skills &amp; hobbies")]

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></symbol>
  <symbol id="i-x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></symbol>
  <symbol id="i-globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></symbol>
  <symbol id="i-rupee" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4h12M6 9h12M14 4c3 0 3 10-3 10H6l8 6"/></symbol>
  <symbol id="i-layout" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M9 9v11"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M11 18.5h2"/></symbol>
  <symbol id="i-live" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 10l5-3v10l-5-3"/><rect x="3" y="6" width="12" height="12" rx="2"/></symbol>
  <symbol id="i-test" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4h6l1 2h3v14H5V6h3z"/><path d="m9 13 2 2 4-4"/></symbol>
  <symbol id="i-brand" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/></symbol>
  <symbol id="i-export" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 8l5-5 5 5M4 15v4a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-4"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></symbol>
  <symbol id="i-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/></symbol>
  <symbol id="i-lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.09 1.76-.72 2.01-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.05 21.8h-.01a9.73 9.73 0 0 1-4.96-1.36l-.36-.21-3.69.97.98-3.6-.23-.37a9.72 9.72 0 0 1-1.49-5.19c0-5.38 4.38-9.76 9.77-9.76 2.6 0 5.06 1.02 6.9 2.86a9.7 9.7 0 0 1 2.86 6.9c0 5.38-4.38 9.76-9.77 9.76z"/></symbol>
</svg>"""


def cta(where: str, label: str, cls: str = "cta", plan: str = "", arrow: bool = True) -> str:
    """Every CTA is a real studio link (works without JS) that opens the checkout."""
    p = f' data-plan="{plan}"' if plan else ""
    a = ' <svg><use href="#i-arrow"/></svg>' if arrow else ""
    return f'<a class="{cls}" href="{STUDIO}" data-checkout{p} data-ev="ob_cta_click" data-where="{where}">{label}{a}</a>'


def wa_link(where: str, text: str, cls: str, inner: str, label: str = "") -> str:
    aria = f' aria-label="{label}"' if label else ""
    return (f'<a class="{cls}" href="{WA}{html.escape(text).replace(" ", "%20")}" target="_blank" rel="noopener"'
            f'{aria} data-ev="ob_whatsapp_click" data-where="{where}">{inner}</a>')


def render(pg: dict) -> str:
    slug = pg["slug"]
    page_id = "lp_" + slug.replace("-", "_")
    url = f"https://allcoaching.in/onboarding-{slug}"
    ac = pg["academy"]
    c1, c2 = pg["chip1"], pg["chip2"]
    marquee = "".join(f"<span>{e}</span>" for e in pg["exams"])
    pains = "".join(
        f'<div class="pc rv"><div class="p"><svg><use href="#i-x"/></svg>{p}</div>'
        f'<div class="s"><b><svg><use href="#i-check"/></svg>{s}</b><span>{d}</span></div></div>'
        for p, s, d in pg["pains"])
    bp_points = "".join(f'<li><svg><use href="#i-check"/></svg><span>{t}</span></li>' for t in pg["bp_points"])
    items = "".join(
        f'<div class="it{" free" if price == "Free" else ""}"><span class="k"><svg><use href="#{ic}"/></svg>{kind}</span>'
        f'<b>{name}</b><span>{sub}</span><span class="pr">{price}</span></div>'
        for ic, kind, name, sub, price in ac["items"])
    faqs = pg["faq"] + COMMON_FAQ
    faq_html = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(faqs))
    others = "".join(f'<a href="/onboarding-{s}">{n}</a>' for s, n in OTHERS if s != slug)
    cfg = json.dumps({"page": page_id, "variant": "v1", "vertical": pg["vertical"], "plan": pg["plan"],
                      "coupon": pg["coupon"], "trial": True})
    calc = pg["calc"]

    return TEMPLATE.substitute(
        title=pg["title"], desc=html.escape(pg["desc"], quote=True), url=url, css=CSS, icons=ICONS, cfg=cfg,
        page_id=page_id, vertical=pg["vertical"],
        wa_header=wa_link("header", pg["wa_text"], "wa", '<svg><use href="#i-wa"/></svg><span>Talk to us</span>'),
        wa_final=wa_link("final", pg["wa_text"], "cta ghost", "Ask a question on WhatsApp"),
        wa_bar=wa_link("sticky", pg["wa_text"], "w2", '<svg><use href="#i-wa"/></svg>', "WhatsApp"),
        cta_header=cta("header", "Start now", "cta go", arrow=False),
        cta_hero=cta("hero", "Start my academy"),
        cta_pain=cta("pain", "Build my academy"),
        cta_bp=cta("blueprint", "Set up my academy"),
        cta_video=cta("video", "Build mine now"),
        cta_starter=cta("pay-starter", "Get Starter", "cta line", "starter", False),
        cta_growth=cta("pay-growth", "Get Growth", "cta", "growth", False),
        cta_pro=cta("pay-pro", "Get Pro", "cta line", "pro", False),
        cta_final=cta("final", "Start my academy", "cta white"),
        cta_bar=cta("sticky", "Start now", arrow=False),
        pill=pg["pill"], h1_lt=pg["h1_lt"], h1_bd=pg["h1_bd"], lede=pg["lede"],
        c1_ic=c1[0], c1_b=c1[1], c1_s=c1[2], c2_ic=c2[0], c2_b=c2[1], c2_s=c2[2],
        who=pg["who"], marquee=marquee + marquee,
        pain_lt=pg["pain_h"][0], pain_bd=pg["pain_h"][1], pains=pains,
        bp_lt=pg["bp_h"][0], bp_bd=pg["bp_h"][1], bp_lede=pg["bp_lede"], bp_points=bp_points,
        ac_url=ac["url"], ac_mark=ac["mark"], ac_name=ac["name"], ac_tag=ac["tag"], ac_items=items, ac_foot=ac["foot"],
        calc_h=calc["h"], calc_n=calc["students"], calc_p=calc["price"],
        faq=faq_html, others=others,
    )


TEMPLATE = Template("""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"/>
<meta name="theme-color" content="#FFFFFF"/>
<meta name="color-scheme" content="light"/>
<title>${title}</title>
<meta name="description" content="${desc}"/>
<!-- ad destination: generated by scripts/build_lp.py — edit the copy there, not here -->
<meta name="robots" content="noindex, follow"/>
<link rel="canonical" href="${url}"/>
<link rel="icon" type="image/webp" href="/assets/fevicon.webp?v=20260707"/>
<link rel="apple-touch-icon" href="/assets/logo/allcoaching-logo.webp?v=20260707"/>
<meta property="og:title" content="${title}"/>
<meta property="og:description" content="${desc}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="${url}"/>
<meta property="og:image" content="https://allcoaching.in/demo/assets/shots/studio-desktop.webp?v=b2"/>
<meta property="og:locale" content="en_IN"/>
<meta name="twitter:card" content="summary_large_image"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@200;400;500;600;700&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet"/>
<link rel="preconnect" href="https://checkout.razorpay.com"/>
<!-- Google Tag Manager — loads at once on ad pages so the Meta Pixel PageView is never missed -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-T3KFKD3G');</script>
<!--
  TRACKING (all through GTM-T3KFKD3G; no pixels hardcoded here). What the live container does
  with this page's events (checked 2026-10-19):
    page load                 -> Meta PageView, GA4 page_view, Ads remarketing
    click on a CTA (studio link on a path containing /onboarding)
                              -> Meta InitiateCheckout, GA4 onboarding_cta_click
    user_identified           -> Meta advanced matching (fbq init with external_id/ph/fn/ln)
    purchase_complete         -> purchase_verified -> Meta Purchase (eventID = transaction_id =
                                 Razorpay payment id), Google Ads purchase, GA4 purchase, X
    lead_complete             -> GA4 generate_lead, Google Ads lead, X
                                 (Meta Lead only fires on join.allcoaching.in in the container)
  Also pushed for reporting (no tags yet): ob_view, ob_cta_click, ob_whatsapp_click, ob_scroll,
  ob_video_play, ob_calc, lp_checkout (checkout steps), sign_up, studio_signup_complete,
  start_trial, add_payment_info. All carry page='${page_id}', vertical='${vertical}'.
  Click IDs and UTMs: /assets/attribution.js (ac_attr cookie on .allcoaching.in).
-->
<style>
${css}
</style>
<script>window.AC_CHECKOUT=${cfg};</script>
<script src="/assets/attribution.js?v=1" defer></script>
<script src="/assets/checkout.js?v=5" defer></script>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T3KFKD3G" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
${icons}

<header class="hd" id="hd">
  <div class="w">
    <a class="lk" href="#top"><img src="/assets/logo/allcoaching-logo.webp?v=20260707" alt="AllCoaching" width="512" height="512"/><b>AllCoaching</b></a>
    <div class="hd-r">${wa_header}${cta_header}</div>
  </div>
</header>

<main>
<section class="hero" id="top">
  <div class="blob b1" aria-hidden="true"></div><div class="blob b2" aria-hidden="true"></div>
  <div class="w">
    <div>
      <span class="pill"><i></i>${pill}</span>
      <h1><span class="lt">${h1_lt}</span><br/><span class="bd">${h1_bd}</span></h1>
      <p class="lede">${lede}</p>
      <div class="hero-cta">
        ${cta_hero}
        <div class="micro"><span><svg><use href="#i-check"/></svg>14-day free trial, no card</span><span><svg><use href="#i-check"/></svg>Or go live today from ₹6,999/yr</span><span><svg><use href="#i-check"/></svg>Keep 90% to 95% of every sale</span></div>
      </div>
      <div class="proof">
        <div class="avs" aria-hidden="true"><span style="background:#2B44FF"><svg width="16" height="16"><use href="#i-users"/></svg></span><span style="background:#16A34A"><svg width="16" height="16"><use href="#i-check"/></svg></span></div>
        <p><b>500+ educators</b> are already selling their courses on AllCoaching.</p>
      </div>
    </div>
    <div class="vis" aria-hidden="true">
      <div class="dev"><img src="/assets/hero/studio-light-1536.webp?v=b2" srcset="/assets/hero/studio-light-1536.webp?v=b2 1536w, /assets/hero/studio-light-3072.webp?v=b2 3072w" sizes="(max-width:980px) 92vw, 540px" alt="" width="1536" height="960" fetchpriority="high" decoding="async"/></div>
      <div class="ph"><img src="/demo/assets/shots/app-mobile.webp?v=b2" alt="" width="780" height="1688" decoding="async"/></div>
      <div class="chip c1"><span class="ic"><svg><use href="#${c1_ic}"/></svg></span><span><b>${c1_b}</b><small>${c1_s}</small></span></div>
      <div class="chip c2"><span class="ic" style="background:#E7F7EE;color:#16A34A"><svg><use href="#${c2_ic}"/></svg></span><span><b>${c2_b}</b><small>${c2_s}</small></span></div>
    </div>
  </div>
</section>

<div class="who" aria-label="Who it is for">
  <p>${who}</p>
  <div class="mq" aria-hidden="true"><div class="mq-r">${marquee}</div></div>
</div>

<section class="pain">
  <div class="w">
    <div class="center rv">
      <p class="eb">What changes for you</p>
      <h2 class="h2"><span class="lt">${pain_lt}</span><br/><span class="bd">${pain_bd}</span></h2>
    </div>
    <div class="pg">${pains}</div>
    <div class="center sec-cta rv">${cta_pain}</div>
  </div>
</section>

<section id="academy">
  <div class="w bp">
    <div class="bp-l rv">
      <p class="eb">Your academy, laid out</p>
      <h2 class="h2"><span class="lt">${bp_lt}</span><br/><span class="bd">${bp_bd}</span></h2>
      <p class="lede">${bp_lede}</p>
      <ul>${bp_points}</ul>
      <div class="sec-cta">${cta_bp}</div>
    </div>
    <div class="acad rv" aria-label="Example academy">
      <div class="acad-top"><span class="dots"><i></i><i></i><i></i></span><span class="url">${ac_url}</span></div>
      <div class="acad-hd"><span class="mk">${ac_mark}</span><span><b>${ac_name}</b><small>${ac_tag}</small></span></div>
      <div class="acad-list">${ac_items}</div>
      <p class="acad-ft">${ac_foot}</p>
    </div>
  </div>
</section>

<section class="vsec" id="demo" style="padding-top:0">
  <div class="w">
    <div class="center rv">
      <p class="eb">4-minute demo</p>
      <h2 class="h2"><span class="lt">See it built,</span> <span class="bd">start to finish.</span></h2>
      <p class="lede">A coaching app, website, courses and a test series, set up in one sitting.</p>
    </div>
    <div class="vbox rv">
      <button class="vf" type="button" data-yt="Q1OI9SstFkg" data-ev="ob_video_play" data-where="demo" aria-label="Play the demo video: Build Your Own LMS in a Few Clicks">
        <img src="https://i.ytimg.com/vi/Q1OI9SstFkg/maxresdefault.jpg" alt="AllCoaching demo: build your own LMS in a few clicks" width="1280" height="720" loading="lazy" decoding="async"/>
        <span class="vp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span>
        <span class="vt">Watch the demo · 4:36</span>
      </button>
    </div>
    <div class="center rv" style="margin-top:22px">${cta_video}</div>
  </div>
</section>

<section id="calc" style="padding-top:0">
  <div class="w">
    <div class="calc rv" id="calcbox" data-n="${calc_n}" data-p="${calc_p}">
      <div>
        <p class="eb">Which plan pays you most</p>
        <h2>${calc_h}</h2>
        <p class="note" style="margin-top:0">Move the sliders. We work out what you keep on each plan, after the platform fee and the yearly plan price.</p>
        <div class="fld"><label for="cn">Students in a year <output id="cn-o"></output></label><input type="range" id="cn" min="5" max="1000" step="5"/></div>
        <div class="fld"><label for="cp">Your course price <output id="cp-o"></output></label><input type="range" id="cp" min="199" max="30000" step="100"/></div>
        <p class="note">An illustrative example, not a promise. What you earn depends on your students and your price. Plan prices exclude GST.</p>
      </div>
      <div class="res" aria-live="polite">
        <div class="tot"><span>Total sales in a year</span><b id="c-tot"></b></div>
        <div class="rows">
          <div class="rw" data-k="starter"><span class="nm">Starter</span><span class="dt">10% fee + ₹6,999/yr</span><span class="v"></span></div>
          <div class="rw" data-k="growth"><span class="nm">Growth</span><span class="dt">7.5% fee + ₹12,999/yr</span><span class="v"></span></div>
          <div class="rw" data-k="pro"><span class="nm">Pro</span><span class="dt">5% fee + ₹24,999/yr</span><span class="v"></span></div>
        </div>
        <a class="cta" id="c-cta" href="https://studio.allcoaching.in/" data-checkout data-ev="ob_cta_click" data-where="calc">Start with Starter <svg><use href="#i-arrow"/></svg></a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="w inc">
    <div class="rv">
      <p class="eb">Everything included</p>
      <h2 class="h2"><span class="lt">Your whole academy.</span><br/><span class="bd">Your name on it.</span></h2>
      <p class="lede">Students buy and learn on your website and in the app. They see your brand, not ours.</p>
      <ul class="feat">
        <li><span class="ic"><svg><use href="#i-globe"/></svg></span><span><b>Website on your domain</b>Course pages, faculty and enquiry form</span></li>
        <li><span class="ic"><svg><use href="#i-phone"/></svg></span><span><b>Student app</b>Android, iOS and web</span></li>
        <li><span class="ic"><svg><use href="#i-layout"/></svg></span><span><b>Recorded courses</b>Videos, notes and PDFs</span></li>
        <li><span class="ic"><svg><use href="#i-test"/></svg></span><span><b>Test series</b>Mock tests with ranks</span></li>
        <li><span class="ic"><svg><use href="#i-live"/></svg></span><span><b>Live classes</b>5, 10 or 15 hours a month</span></li>
        <li><span class="ic"><svg><use href="#i-rupee"/></svg></span><span><b>UPI and card checkout</b>Automatic payouts to your bank</span></li>
        <li><span class="ic"><svg><use href="#i-users"/></svg></span><span><b>Student CRM</b>Plus logins for your teachers</span></li>
        <li><span class="ic"><svg><use href="#i-search"/></svg></span><span><b>Marketplace listing</b>New students can find you</span></li>
      </ul>
    </div>
    <div class="phones rv" aria-hidden="true">
      <div class="glow"></div>
      <div class="pp a"><img src="/demo/assets/shots/website-mobile.webp?v=b2" alt="" width="780" height="1688" loading="lazy" decoding="async"/></div>
      <div class="pp b"><img src="/assets/hero/studio-mobile-light.webp?v=b2" alt="" width="780" height="1688" loading="lazy" decoding="async"/></div>
      <div class="cap x">Your academy website</div>
      <div class="cap y">Your studio, on your phone</div>
    </div>
  </div>
</section>

<section class="pricing" id="pay">
  <div class="w">
    <div class="center rv">
      <p class="eb">Simple, open pricing</p>
      <h2 class="h2"><span class="lt">Pick a plan and go live today.</span><br/><span class="bd">Or try it free for 14 days.</span></h2>
      <p class="lede">Same academy on every plan. Bigger plans keep more of every sale.</p>
    </div>
    <div class="trial rv"><span><b>Pay now:</b> your plan starts today</span><span class="dot"></span><span><b>Or:</b> 14 days free on Starter, no card</span><span class="dot"></span><span><b>Either way:</b> no setup fee</span></div>
    <div class="plans">
      <div class="pl rv"><span class="nm">Starter</span><p class="for">For a new academy finding its first students.</p><div class="pr"><b>₹6,999</b><span>/year + GST</span></div><div class="keep">You keep <b>90%</b> of every sale</div>
        <ul><li><svg><use href="#i-check"/></svg>512 GB storage · 1080p</li><li><svg><use href="#i-check"/></svg>5 live-class hours a month</li><li><svg><use href="#i-check"/></svg>Your own domain, connected</li><li><svg><use href="#i-check"/></svg>Website, app and marketplace</li></ul>
        ${cta_starter}</div>
      <div class="pl ft rv"><span class="bdg">Most popular</span><span class="nm">Growth</span><p class="for">More room for content and live classes, and a lower cut.</p><div class="pr"><b>₹12,999</b><span>/year + GST</span></div><div class="keep">You keep <b>92.5%</b> of every sale</div>
        <ul><li><svg><use href="#i-check"/></svg>1 TB storage · 1080p</li><li><svg><use href="#i-check"/></svg>10 live-class hours a month</li><li><svg><use href="#i-check"/></svg>Your own domain, connected</li><li><svg><use href="#i-check"/></svg>Website, app and marketplace</li></ul>
        ${cta_growth}</div>
      <div class="pl rv"><span class="nm">Pro</span><p class="for">4K video, the lowest cut and a premium template.</p><div class="pr"><b>₹24,999</b><span>/year + GST</span></div><div class="keep">You keep <b>95%</b> of every sale</div>
        <ul><li><svg><use href="#i-check"/></svg>3 TB storage · 4K</li><li><svg><use href="#i-check"/></svg>15 live-class hours a month</li><li><svg><use href="#i-check"/></svg>Premium website template</li><li><svg><use href="#i-check"/></svg>Website, app and marketplace</li></ul>
        ${cta_pro}</div>
    </div>
    <p class="fine">Prices exclude GST · No setup fee · Secure payment by Razorpay · Upgrade any time and what you paid is credited</p>
  </div>
</section>

<section>
  <div class="w">
    <div class="center rv">
      <p class="eb">No risk in starting</p>
      <h2 class="h2"><span class="lt">Built by you.</span> <span class="bd">Owned by you.</span></h2>
    </div>
    <div class="prom">
      <div class="pm rv"><span class="ic"><svg><use href="#i-lock"/></svg></span><b>Secure payment</b><p>Pay by UPI, card or netbanking through Razorpay.</p></div>
      <div class="pm rv"><span class="ic"><svg><use href="#i-layout"/></svg></span><b>No sales call</b><p>Sign up and launch on your own, at your own pace.</p></div>
      <div class="pm rv"><span class="ic"><svg><use href="#i-export"/></svg></span><b>Your data stays yours</b><p>Courses, students and payments are always exportable.</p></div>
      <div class="pm rv"><span class="ic"><svg><use href="#i-chat"/></svg></span><b>Help on WhatsApp</b><p>Stuck on a step? Message us and we'll walk you through it.</p></div>
    </div>
    <div class="founder rv">
      <img src="/assets/Amit-Ratan.webp" alt="Amit Ratan, founder of AllCoaching" width="128" height="128" loading="lazy"/>
      <div><q>We built AllCoaching so an educator can launch a real academy without asking anyone for help, and keep up to 95% of what they earn.</q><small>Amit Ratan · Founder &amp; CEO</small></div>
    </div>
  </div>
</section>

<section id="faq" style="background:var(--soft)">
  <div class="w">
    <div class="center rv">
      <p class="eb">Before you decide</p>
      <h2 class="h2"><span class="lt">Questions</span> <span class="bd">educators ask us.</span></h2>
    </div>
    <div class="faq">${faq}</div>
  </div>
</section>

<section class="final" id="final">
  <div class="rays" aria-hidden="true"></div>
  <div class="w">
    <h2 class="rv"><span class="lt">Your academy could be</span><br/><span class="bd">live tonight.</span></h2>
    <p class="rv">Verify your number, name your academy and pick a plan. Then add your first course.</p>
    <div class="row rv">${cta_final}${wa_final}</div>
    <div class="micro rv"><span><svg><use href="#i-check"/></svg>14-day free trial available</span><span><svg><use href="#i-check"/></svg>Plans from ₹6,999 a year</span><span><svg><use href="#i-check"/></svg>No sales call</span></div>
  </div>
</section>
</main>

<footer class="foot">
  <div class="w">
    <a class="lk" href="/"><img src="/assets/logo/allcoaching-logo.webp?v=20260707" alt="" width="512" height="512"/><b>AllCoaching</b></a>
    <div><span>© <span id="yr">2026</span> AllCoaching</span><a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="mailto:contact@allcoaching.in">contact@allcoaching.in</a></div>
    <div class="also"><span>Also for:</span>${others}</div>
  </div>
</footer>

<div class="bar" id="bar" role="region" aria-label="Start your academy">
  <div class="px"><b>From ₹6,999/yr</b><i>or 14 days free</i></div>
  ${cta_bar}
  ${wa_bar}
</div>

<script>
(function(){
  document.documentElement.classList.add('js');
  var dl=window.dataLayer=window.dataLayer||[];
  var PAGE='${page_id}',VERTICAL='${vertical}';
  function eid(){return 'ob.'+Date.now().toString(36)+'.'+Math.random().toString(36).slice(2,10)}
  function attr(){try{var m=document.cookie.match(/(?:^|; )ac_attr=([^;]*)/);var l=m?(JSON.parse(decodeURIComponent(m[1])).last||{}):{};var u=new URLSearchParams(location.search);['utm_source','utm_campaign','gclid','fbclid','twclid'].forEach(function(k){if(u.get(k))l[k]=u.get(k)});return{utm_source:l.utm_source||'',utm_campaign:l.utm_campaign||'',click_id:l.gclid?'gclid':l.fbclid?'fbclid':l.twclid?'twclid':''}}catch(e){return{}}}
  function push(ev,extra){var o={event:ev,event_id:eid(),page:PAGE,page_variant:'v1',vertical:VERTICAL,offer_inr:6999,currency:'INR'};var a=attr();for(var k in a)o[k]=a[k];for(var k2 in extra)o[k2]=extra[k2];dl.push(o)}
  push('ob_view',{});
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-ev]');if(!a)return;push(a.getAttribute('data-ev'),{where:a.getAttribute('data-where')||'',plan:a.getAttribute('data-plan')||''})},false);
  var sent={};addEventListener('scroll',function(){var h=document.documentElement,p=(scrollY+innerHeight)/h.scrollHeight*100;[50,90].forEach(function(d){if(p>=d&&!sent[d]){sent[d]=1;push('ob_scroll',{depth:d})}})},{passive:true});
  // demo video: load the YouTube player only when the visitor taps play
  var vf=document.querySelector('.vf');
  if(vf)vf.addEventListener('click',function(){if(vf.classList.contains('on'))return;var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+vf.getAttribute('data-yt')+'?autoplay=1&rel=0&playsinline=1&modestbranding=1';f.title='AllCoaching demo video';f.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';f.allowFullscreen=true;vf.classList.add('on');vf.appendChild(f)});
  // earnings calculator: what the educator keeps on each plan after the fee and the plan price
  var box=document.getElementById('calcbox');
  if(box){
    var cn=document.getElementById('cn'),cp=document.getElementById('cp'),cta=document.getElementById('c-cta');
    var P={starter:[.10,6999,'Starter'],growth:[.075,12999,'Growth'],pro:[.05,24999,'Pro']};
    function inr(x){return '\\u20B9'+Math.round(x).toLocaleString('en-IN')}
    function fill(el){var p=(el.value-el.min)/(el.max-el.min)*100;el.style.setProperty('--p',p+'%')}
    var used=false;
    function calc(){
      var n=+cn.value,pr=+cp.value,s=n*pr,best=null,bv=-Infinity;
      document.getElementById('cn-o').textContent=n.toLocaleString('en-IN');
      document.getElementById('cp-o').textContent=inr(pr);
      document.getElementById('c-tot').textContent=inr(s);
      Object.keys(P).forEach(function(k){var v=s*(1-P[k][0])-P[k][1];box.querySelector('[data-k="'+k+'"] .v').textContent=(v<0?'\\u2212':'')+inr(Math.abs(v));if(v>bv){bv=v;best=k}});
      [].forEach.call(box.querySelectorAll('.rw'),function(r){r.classList.toggle('best',r.getAttribute('data-k')===best)});
      box.querySelectorAll('.rw .tag').forEach(function(t){t.remove()});
      var b=box.querySelector('.rw.best .nm');if(b){var t=document.createElement('span');t.className='tag';t.textContent='Best for you';b.appendChild(t)}
      cta.setAttribute('data-plan',best);cta.firstChild.nodeValue='Start with '+P[best][2]+' ';
      fill(cn);fill(cp);
    }
    cn.value=box.getAttribute('data-n');cp.value=box.getAttribute('data-p');
    function onIn(){calc();if(!used){used=true;push('ob_calc',{})}}
    cn.addEventListener('input',onIn);cp.addEventListener('input',onIn);
    calc();
  }
  // reveal on scroll
  var els=document.querySelectorAll('.rv');
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target)}})},{threshold:.12});els.forEach(function(el){io.observe(el)})}else els.forEach(function(el){el.classList.add('in')});
  // header border + header CTA + mobile sticky bar after the hero CTA leaves view
  var hd=document.getElementById('hd'),bar=document.getElementById('bar'),heroCta=document.querySelector('.hero-cta .cta'),fin=document.getElementById('final');
  function sc(){var y=scrollY;hd.classList.toggle('sc',y>8);var past=heroCta.getBoundingClientRect().bottom<0;var atEnd=fin.getBoundingClientRect().top<innerHeight*.6;bar.classList.toggle('on',past&&!atEnd)}
  sc();addEventListener('scroll',sc,{passive:true});
  var y=document.getElementById('yr');if(y)y.textContent=new Date().getFullYear();
})();
</script>
</body>
</html>
""")


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    for pg in PAGES:
        out = OUT_DIR / f"onboarding-{pg['slug']}.html"
        out.write_text(render(pg), encoding="utf-8", newline="\n")
        print("wrote", out.relative_to(ROOT).as_posix(), f"({len(pg['title'])}-char title, {len(pg['desc'])}-char description)")


if __name__ == "__main__":
    main()
