"""Second CTR batch from the GSC export of 2026-11-11: pages with 350+ impressions and CTR under 1.7%.
Query evidence is in the comments; where the top-1000 query list has none, the change only removes filler,
completes a cut-off description or drops an unsourced number."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ctr_optimize_nov2026 as base
base.CHANGES = [
    # 15,525 impr, 1.69%. "new rules for coaching classes" 63, "guidelines for coaching centre" 44, "new guidelines for coaching centre" 44.
    ('blog/new-coaching-center-rules-india-2026.html', 'New Coaching Rules 2026: No Under-16 Enrolment, Guidelines',
     'New rules for coaching centres in India in 2026: the Coaching Centre Guidelines 2024, no under-16 enrolment, CCPA ad limits and DPDP data rules explained.'),
    # 3,405 impr, 1.06%. Title was 62 chars and ended in filler.
    ('blogs/hinglish/teachers-ke-liye-best-coaching-app-2026.html', 'Teachers Ke Liye Best Coaching App 2026: Top 5 Compared',
     'Teachers ke liye best coaching app 2026 kaunsa hai? Classplus, Teachmint, Graphy, Unacademy aur AllCoaching ka seedha comparison: fees, apna brand aur students.'),
    # 3,224 impr, 1.02%. "laws for teachers in india" 34, "law for teachers" 13. Description had no ending.
    ('blog/indian-edtech-laws-and-regulations-for-teachers.html', 'Laws for Online Teachers in India: 2026 Compliance Guide',
     'Laws for online teachers in India in 2026: DPDP Act, GST, refunds, ASCI ad rules, POCSO and IT Rules explained in plain English. Not legal advice.'),
    # 2,414 impr, 1.12%. "teachmint alternative" 32 @5, 0 clicks.
    ('blog/teachmint-paid-features-alternative-free.html', 'Teachmint Alternative (2026): Paid Features, Free Trials',
     'Looking for a Teachmint alternative? Teachmint lists no prices, so we compare free trials, no-upfront-fee plans and free tools for its paid features, with sources.'),
    # 2,129 impr, 0.66%. Description was cut mid-sentence.
    ('blogs/en/using-generative-ai-for-automated-quiz-creation.html', 'Generative AI Quiz Creation for Teachers: 2026 Playbook',
     'Generative AI quiz creation can draft a question bank in an afternoon. The prompts to use, difficulty checks and the review steps before students see a question.'),
    # 2,053 impr, 1.22%. "graphy vs classplus" 142 + 9; "classplus vs graphy" only 6.
    ('blog/classplus-vs-graphy-vs-allcoaching.html', 'Graphy vs Classplus vs AllCoaching (2026): Which to Pick',
     'Graphy vs Classplus vs AllCoaching for Indian educators: how each works, free trials, own app and domain, plus Classplus vs AllCoaching cost from published prices.'),
    # 1,899 impr, 0.37%.
    ('blog/monetize-youtube-teaching-channel-via-personal-app.html', 'How to Monetize a YouTube Teaching Channel in India (2026)',
     'How to monetize a YouTube teaching channel in India: turn subscribers into paying students, what to sell first, the conversion maths, and your own app to sell from.'),
    # 1,542 impr, 0.84%, pos 9.2. Title used only 42 of 60 characters.
    ('blog/best-ai-tools-for-teachers-india.html', 'Best AI Tools for Teachers in India 2026: Sorted by Task',
     'The best AI tools for teachers in India in 2026, sorted by task: lesson plans, notes, slides, quizzes and video. Plus how to turn AI-drafted content into income.'),
    # 1,458 impr, 1.10%. "paid whatsapp group" 132 @8, 0 clicks.
    ('blogs/hinglish/whatsapp-group-se-paid-course-kaise-beche.html', 'Paid WhatsApp Group Se Course Kaise Bechein (2026 Guide)',
     'Paid WhatsApp group se course kaise beche? Manual UPI screenshot aur add-remove band karein, aur payment hote hi access apne branded app par automatic karein.'),
    # 1,154 impr, 0.26%. Description carried a stray "Rs 6,999/yr, keep up to 100%".
    ('blog/railway-rrb-ntpc-group-d-coaching-app-for-educators.html', 'RRB NTPC & Group D Coaching App for Educators (2026)',
     'How a railway RRB NTPC or Group D educator goes independent: sectional tests, full mocks with rank and your own brand. Plans from ₹3,999 a month at 0% commission.'),
    # 1,093 impr, 0.82%. Description was short and vague.
    ('blog/student-progress-tracking-analytics-tools-coaching-india.html', 'Student Progress Tracking Tools for Coaching (2026 Guide)',
     'Student progress tracking tools for coaching institutes: go past attendance to see test scores, batch health and drop-off risk in one place. A 2026 guide.'),
    # 1,022 impr, 0.78%. "skool india" 55 @4, "is skool available in india" 11.
    ('blog/skool-circle-so-alternative-india.html', 'Skool in India (2026): Prices, Fees and Rupee Alternatives',
     'Skool in India bills in US dollars. Skool and Circle.so plans and fees next to rupee options with UPI, live classes and tests, and when to stay put.'),
    # 714 impr, 1.40%. Description was cut off and carried an unsourced "40 hours to 4".
    ('blog/using-chatgpt-for-course-curriculum-design.html', 'ChatGPT for Course Curriculum Design: 2026 Educator Guide',
     'Use ChatGPT for course curriculum design: a 5-step workflow, the prompts to use, and the checks to run before you teach from an AI-drafted syllabus.'),
    # 655 impr, 1.37%.
    ('blog/online-neet-coaching-platform-for-educators.html', 'NEET Coaching Platform for Educators (2026): Your Own App',
     'How a NEET teacher starts their own app in 2026 to sell biology test series and recorded lectures: why biology is the wedge, and a 7-day free trial to begin.'),
    # 477 impr, 0.21%, pos 3.0.
    ('blog/how-to-get-first-500-students-for-coaching-app.html', 'How to Get Your First 500 Students Online (2026 Plan)',
     'How to get your first 500 students for a coaching app without relying on ads: publish 10 posts and 10 classes, share them where students are, and keep going.'),
    # 360 impr, 0.56%.
    ('blog/best-app-for-state-psc-coaching-educators.html', 'Best App for State PSC Coaching (UPPSC, BPSC, RAS) 2026',
     'Best app for state PSC coaching educators (UPPSC, BPSC, RAS) in 2026: choose by aspirant discovery, vernacular support and a PYQ test-series stack, not features.'),
    # 400 impr, 1.00%. Description was cut mid-sentence.
    ('blogs/en/virtual-reality-in-indian-online-coaching.html', 'Virtual Reality in Indian Online Coaching: 2026 Reality',
     'Virtual reality in Indian online coaching helps in a few narrow cases. The honest 2026 scope: where immersion clarifies NEET and JEE concepts, and where it does not.'),
]
if __name__ == '__main__':
    base.run('--dry-run' in sys.argv)
