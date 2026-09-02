"""Cluster the GSC query export (3 months to 2026-08-26) into demand themes."""
import re

# (query, clicks, impressions, position) — from Queries.csv
Q = [
 ("classplus pricing",17,1177,4.03),("appx vs classplus",13,187,5.11),("graphy pricing",12,398,6.09),
 ("mock test ai",10,207,6.71),("classplus app price",7,285,5.52),("online teaching studio setup cost",7,140,4.66),
 ("free upi payment gateway",6,400,7.02),("class plus app charges",6,368,5.71),("telegram banned in india",5,4048,12.35),
 ("ai mock test",4,160,7.18),("graphy vs classplus",4,150,2.79),("free upi payment gateway india",4,122,6.87),
 ("online teaching setup",4,110,6.54),("class plus pricing",4,101,5.36),("upi payment gateway free",3,70,5.93),
 ("classplus alternative",3,69,7.86),("classplus vs graphy",3,33,2.7),("fire safety rules for coaching classes",3,32,3.56),
 ("classplus",2,298,3.81),("free payment gateway for upi",2,126,7.25),("upi payment gateway without kyc",2,97,9.04),
 ("lms pricing in india",2,83,5.96),("classplus competitors",2,61,10.18),("testbook alternative",2,48,7.5),
 ("lms cost in india",2,34,4.97),("coaching rules",2,29,5.41),("graphy revenue",2,26,6.65),
 ("pw alternative app",2,24,9.46),("mock test generator",2,24,16.46),("classplus cost",2,22,4.23),
 ("graphy alternative in india",2,13,5.69),("udemy alternatives for instructors",2,9,4.22),
 ("teachmint",1,280,2.4),("when is telegram coming back in india",1,218,10.94),("999293",1,122,6.68),
 ("classplus price",1,108,3.9),("classplus subscription charges",1,74,4.0),("classplus pricing per month",1,71,4.97),
 ("online teaching setup equipment",1,71,7.11),("graphy pricing india",1,50,6.22),("classplus charges",1,46,4.52),
 ("fire noc for coaching institute",1,44,4.23),("classplus subscription",1,43,5.47),("free upi gateway",1,40,6.12),
 ("teaching studio setup cost",1,35,5.31),("new rules for coaching classes",1,34,5.82),("best app for home tutors",1,30,5.07),
 ("skool india",1,27,5.15),("noc for coaching institute",1,23,3.48),("new coaching guidelines",1,22,4.68),
 ("online teaching kit",1,21,4.48),("learnyst alternatives",1,20,5.2),("guidelines for coaching institutes",1,17,6.82),
 ("physics wallah alternative",1,13,4.85),("cheap lms platform",1,13,5.92),("teach mint",1,11,2.18),
 ("studio for online teaching",1,11,5.82),("coaching centre rules and regulations",1,10,9.6),
 ("regional language support in indian edtech saas best practices",0,2595,5.42),
 ("classplus abonnement",0,1468,8.58),("telegram banned in india 2026",0,229,9.19),("class plus pro",0,191,1.24),
 ("multilanguage lms",0,183,47.51),("upi payment gateway",0,178,12.06),("paid whatsapp group",0,141,8.38),
 ("classplus c est quoi",0,110,2.05),("winuall",0,98,13.15),("abonnement classplus",0,96,5.09),
 ("graphy alternatives",0,91,9.88),("multilingual lms",0,91,47.58),("best upi payment gateway",0,85,15.06),
 ("lms platforms with multi-language support",0,73,36.27),("online class setup equipment",0,69,8.36),
 ("graphy alternative",0,61,9.9),("upi gateway free",0,59,6.07),("free payment gateway india",0,59,21.15),
 ("payment gateway with 0 charges on upi",0,58,9.34),("classplus abonnement annuel",0,56,8.96),
 ("telegram ban in india",0,55,11.58),("upi payment gateway for website",0,54,25.96),("gst on coaching fees",0,52,6.15),
 ("lms fees",0,50,7.04),("free coaching application",0,48,2.75),("upi payment gateway in india",0,48,22.52),
 ("classplus plans",0,46,6.35),("payment gateway for collecting course fees online india",0,46,7.5),
 ("apna coaching",0,45,9.22),("graphy alternatives for digital products",0,44,5.66),("kitna paisa lagta hai",0,44,9.3),
 ("aakash franchise cost",0,44,10.36),("free payment gateway",0,44,17.55),("sac 999293",0,43,6.23),
 ("upi payment gateway india",0,43,13.91),("classplus login",0,38,3.32),("class plus",0,37,3.78),
 ("class plus abonnement",0,36,3.56),("telegram ban in india 2026",0,34,8.85),("upi payment gateway charges",0,33,17.0),
 ("online class setup cost",0,32,7.53),("999293 sac code",0,29,3.59),("setup required for online teaching",0,29,6.17),
 ("home tuition app",0,29,7.48),("best payment gateway for edtech platform india",0,29,9.79),
 ("online class studio setup price",0,30,8.43),("graphy app",0,28,10.21),("upi payment gateway list",0,28,13.43),
 ("techmint",0,25,2.24),("online coaching app for teachers",0,25,6.68),("999293 sac",0,24,6.38),
 ("payment gateway free",0,24,15.04),("graphy price",0,23,5.52),("best psc coaching app",0,23,7.43),
 ("best ai for mock test",0,22,7.18),("hindi lms",0,22,7.77),("multi language lms",0,22,36.23),
 ("classplus app charges",0,21,4.48),("new guidelines for coaching centre",0,21,5.0),
 ("coaching classes rules and regulations",0,21,8.19),("testbook alternative free",0,21,8.71),
 ("lms portal fee",0,20,3.4),("online studio setup price",0,20,8.1),("coaching guidelines 2024",0,20,8.5),
 ("free coaching app for students",0,20,10.05),("unacademy competitors",0,20,16.6),("classplus app",0,19,3.42),
 ("gst on coaching institutes",0,19,5.58),("law for teachers",0,19,7.37),("lms charges",0,19,7.47),
 ("lms certificate fees",0,19,7.63),("lms hindi",0,19,8.42),("lms fee",0,18,6.5),("graphy app price",0,18,7.67),
 ("multi-language lms",0,18,35.06),("coaching app kaise banaye",0,17,4.18),("classplus pro",0,17,5.35),
 ("graphy lms pricing",0,17,6.41),("ai for mock test",0,17,6.65),("studio setup for teaching",0,17,6.94),
 ("create and sell mock test",0,17,10.82),("sac code 999293",0,16,1.56),("appx pricing",0,16,5.5),
 ("laws for teachers in india",0,16,6.12),("lms subscription",0,16,8.0),("testbook like apps",0,16,8.88),
 ("ai mock test generator india",0,15,3.8),("cuemath franchise",0,15,5.53),("cost of lms software in india",0,15,13.27),
 ("coaching centre income tax code",0,14,6.07),("cheapest lms platform",0,14,6.29),("affordable lms",0,14,6.57),
 ("rules for coaching classes",0,14,7.21),("coaching guidelines",0,14,8.71),("coaching rules and regulations",0,14,9.43),
 ("gst on coaching",0,13,7.31),("testbook sell",0,13,7.38),("kajabi vs teachable vs graphy for course selling",0,13,8.77),
 ("online class equipment for teachers",0,13,8.92),("best ai tools for teachers in india",0,13,17.23),
 ("appx app price",0,12,5.33),("teachmint pricing",0,12,5.67),("business code for coaching classes",0,12,7.33),
 ("classplus pricing india 2026",0,12,6.75),("free coaching app",0,12,8.83),("classplus profit",0,12,9.0),
 ("unacademy vs udemy",0,12,11.67),("teachmint app price",0,11,3.73),("pw alternative",0,11,5.64),
 ("gst on coaching classes",0,11,8.18),("classplus review",0,11,9.55),("app like testbook",0,11,10.09),
 ("teachmint smart board price",0,10,2.6),("best home tutor app",0,10,6.7),("cheapest lms",0,10,6.7),
 ("online tuition kaise start kare",0,10,7.3),("coaching institute gst rate",0,9,6.22),("999293 gst rate",0,9,6.44),
 ("coaching centre code income tax",0,9,9.0),("neet mock test generator",0,9,13.22),("teachmintx",0,9,2.33),
 ("gst for coaching classes",0,8,6.25),("learnyst alternative",0,8,6.88),("coaching centre opening guidelines",0,8,6.25),
 ("guidelines for regulation of coaching center 2024",0,8,9.25),("gst rate on coaching classes",0,7,5.29),
 ("coaching classes gst rate",0,7,6.29),("teachmint fee management",0,7,8.57),("gst on private coaching classes",0,7,8.71),
 ("teachers protection act",0,7,9.14),("online teaching equipment",0,7,9.14),
 ("gst calculator coaching tuition fees",0,7,10.86),("can we claim gst input on watch in education coaching institite",0,7,11.14),
 ("coaching centre guidelines",0,7,8.43),("teaching app kaise banaye",0,6,7.5),("apna app kaise banaye free me",0,6,7.83),
 ("coaching gst rate",0,6,7.83),("gst on coaching institute",0,6,6.83),("coaching centre gst rate",0,6,5.17),
 ("gst on coaching classes fees",0,6,7.5),("online teaching equipment list",0,6,6.33),
 ("government guidelines for coaching institute",0,6,3.17),("ministry of education guidelines for coaching centres",0,4,6.75),
 ("business code for coaching",0,6,5.33),
]

CLUSTERS = [
 ('Competitor: Classplus',      r'class\s*plus|classplu'),
 ('Competitor: Graphy',         r'\bgraphy\b'),
 ('Competitor: Teachmint',      r'teach\s*mint|techmint'),
 ('Competitor: others',         r'unacademy|udemy|kajabi|testbook|winuall|learnyst|teachable|physics ?wallah|\bpw\b|cuemath|skool|appx|aakash'),
 ('GST / tax / SAC code',       r'\bgst\b|999293|income tax|business code'),
 ('Coaching rules / fire NOC',  r'coaching (rules|guideline|classes rule|centre rule|centre guideline|centre opening)|guidelines for|fire noc|\bnoc\b|fire safety|regulation of coaching|teachers protection|laws? for teachers|new rules|rules for coaching|coaching rules'),
 ('Studio / equipment setup',   r'studio setup|setup (cost|equipment|for teaching|required)|teaching setup|teaching kit|class setup|class equipment|teaching equipment|studio for|studio setup|setup price'),
 ('AI mock test / test series', r'mock test|test series|create and sell'),
 ('LMS pricing',                r'\blms\b'),
 ('Hinglish "kaise banaye"',    r'kaise banaye|kitna paisa|kaise start|kaise shuru'),
 ('Free coaching app',          r'free coaching app|free coaching application|coaching app for teachers|home tutor app|home tuition app|psc coaching app'),
 ('AI tools for teachers',      r'ai tools'),
 ('__SPLIT__',                  None),
 ('JUNK: Telegram news',        r'telegram'),
 ('JUNK: generic payments',     r'payment gateway|upi'),
 ('JUNK: French/foreign',       r'abonnement|c est quoi'),
 ('JUNK: multi-language LMS',   r'multi.?lang|regional language|hindi lms'),
 ('JUNK: brand/navigational',   r'^classplus$|^class plus$|^teachmint$|^apna coaching$|login|^techmint$|^teach mint$'),
]

used = set()
print(f'{"CLUSTER":30s} {"qs":>4s} {"clicks":>7s} {"impr":>8s} {"CTR":>7s} {"avgPos":>7s}')
print('-'*70)
edu_c=edu_i=junk_c=junk_i=0
junk=False
for label,pat in CLUSTERS:
    if pat is None:
        print('-'*70); junk=True; continue
    hits=[(i,q) for i,q in enumerate(Q) if i not in used and re.search(pat,q[0])]
    for i,_ in hits: used.add(i)
    if not hits: continue
    c=sum(q[1] for _,q in hits); im=sum(q[2] for _,q in hits)
    pos=sum(q[3]*q[2] for _,q in hits)/im
    if junk: junk_c+=c; junk_i+=im
    else: edu_c+=c; edu_i+=im
    print(f'{label:30s} {len(hits):4d} {c:7d} {im:8d} {c/im*100:6.2f}% {pos:7.2f}')
rest=[q for i,q in enumerate(Q) if i not in used]
print('-'*70)
print(f'{"(long tail, unclustered)":30s} {len(rest):4d} {sum(q[1] for q in rest):7d} {sum(q[2] for q in rest):8d}')
print()
print(f'EDUCATOR-INTENT : {edu_c:5d} clicks / {edu_i:6d} impr  = {edu_c/edu_i*100:.2f}% CTR')
print(f'JUNK/WRONG-AUD  : {junk_c:5d} clicks / {junk_i:6d} impr  = {junk_c/junk_i*100:.2f}% CTR')
print(f'junk share of impressions: {junk_i/(edu_i+junk_i)*100:.0f}%')
