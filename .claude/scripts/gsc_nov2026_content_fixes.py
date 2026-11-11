"""Follow-up to the GSC export of 2026-11-11: question-style H2s (People Also Ask / AI answers),
internal links to under-linked new posts, and the Classplus DIY login line. Edits v3 content JSON; rebuild after."""
import json, os, sys
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'skills', 'academy-guide-blog', 'content')
def L(slug, text): return '<a href="/blog/%s">%s</a>' % (slug, text)
H2 = {
 'best-platform-to-sell-online-courses-in-india': {'short-answer': 'Which is the best platform to sell online courses in India?', 'who-owns': 'Who owns the student, the brand, the payout and the data?', 'yearly-cost': 'How much does it cost to sell courses online in India in a year?', 'which-fits': 'Which type of platform fits which educator?'},
 'classplus-diy-alternative': {'what-it-offers': "What does Classplus DIY offer, in Classplus's own words?", 'price': 'What is the Classplus DIY price?', 'who-suits': 'Who does Classplus DIY suit?'},
 'how-to-get-paid-students-for-online-coaching-free': {'conversion': 'How do you turn free followers into paid students?', 'measure': 'How do you track which free channel brings paying students?'},
 'online-course-launch-plan': {'honest-urgency': 'How do you create urgency without fake deadlines?', 'mistakes': 'What are the common online course launch mistakes?'},
}
LINKS = {
 'classplus-alternative-for-coaching-institutes': ["If you came here after seeing Classplus's self-serve sign-up, our guide to " + L('classplus-diy-alternative', 'Classplus DIY') + ' covers what that page offers and what it leaves unstated.'],
 'appx-vs-classplus': ['Classplus also has a self-serve route. See ' + L('classplus-diy-alternative', 'what Classplus DIY is and what it costs') + ' before you decide.'],
 'classplus-vs-graphy-vs-allcoaching': ["Considering Classplus's do-it-yourself sign-up? Read " + L('classplus-diy-alternative', 'Classplus DIY: what it is and what to check') + '.'],
 'how-to-get-paid-students-for-online-coaching-free': ['Once the first students arrive, the next stage is covered in ' + L('grow-online-coaching-students', 'how to grow online coaching from 50 to 1,000 students') + '.'],
 'online-course-launch-plan': ['After launch, follow the plan in ' + L('grow-online-coaching-students', 'grow your online coaching from 50 to 1,000 students') + '. For the free class in week 3, compare ' + L('youtube-live-vs-zoom-for-teachers', 'YouTube Live vs Zoom for teachers') + ' before you pick a room.'],
 'how-to-start-online-academy-in-5-steps': ['Still choosing a name? See ' + L('coaching-institute-name-ideas', 'coaching institute name ideas and how to choose one') + '. If you were planning a WordPress site, read ' + L('coaching-institute-website-without-wordpress', 'how to create a coaching institute website without WordPress') + ' first.'],
 'domain-name-for-coaching-institute': ['Not settled on the name yet? Start with ' + L('coaching-institute-name-ideas', 'coaching institute name ideas') + ', then come back for the domain.'],
 'coaching-institute-website-without-wordpress': ['A good site starts with a clear name. See ' + L('coaching-institute-name-ideas', 'how to name your coaching institute') + '.'],
 'best-lms-for-coaching-institutes-india': ['Teaching alone rather than running an institute? See ' + L('best-lms-for-private-tutors', 'the best LMS for private tutors') + '.'],
 'create-your-first-online-course-india': ['Planning live classes with the course? Compare ' + L('youtube-live-vs-zoom-for-teachers', 'YouTube Live vs Zoom for teachers') + '.'],
 'meta-ads-for-coaching-institutes': ['Before paying for ads, set up the free listing: ' + L('google-business-profile-for-coaching-centre', 'Google Business Profile for coaching centres') + '.'],
 'grow-online-coaching-students': ['For students in your own city, a complete ' + L('google-business-profile-for-coaching-centre', 'Google Business Profile for your coaching centre') + ' brings map and local search visits.'],
 'how-to-make-coaching-app-without-coding': ['The same no-code route works for the website. See ' + L('coaching-institute-website-without-wordpress', 'coaching institute website without WordPress') + '.'],
 'youtube-live-vs-zoom-for-teachers': ['Live classes are one part of growth. The full plan is in ' + L('grow-online-coaching-students', 'grow online coaching from 50 to 1,000 students') + '.'],
 'google-business-profile-for-coaching-centre': ['Your profile name must match your real name. If you are still choosing one, see ' + L('coaching-institute-name-ideas', 'coaching institute name ideas') + '.'],
}
BUMP = set(H2) | {'physics-wallah-alternative-for-educators', 'how-much-can-you-earn-teaching-online-india'}
touched = []
for slug in sorted(set(H2) | set(LINKS) | BUMP):
    p = os.path.join(C, slug + '.json'); j = json.load(open(p, encoding='utf-8')); before = json.dumps(j, ensure_ascii=False)
    for s in j['sections']:
        if s['id'] in H2.get(slug, {}): s['h2'] = H2[slug][s['id']]
    for para in LINKS.get(slug, []):
        href = para.split('href="')[1].split('"')[0]
        if href in json.dumps(j['sections'], ensure_ascii=False) and all(h in json.dumps(j['sections']) for h in [x.split('"')[0] for x in para.split('href="')[1:]]): continue
        last = j['sections'][-1]; html = last['html']
        add = '<p>' + para + '</p>'
        if isinstance(html, list): html.append(add)
        else: last['html'] = html.rstrip() + '\n      ' + add
    if slug == 'classplus-diy-alternative':
        line = ' If you only want to log in, the page is classplusapp.com/diy/login.'
        if isinstance(j['intro'], list) and 'diy/login' not in j['intro'][0]: j['intro'][0] += line
    if slug in BUMP: j['date_modified'] = '2026-11-11'
    if json.dumps(j, ensure_ascii=False) != before:
        json.dump(j, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2); touched.append(slug)
print('\n'.join(touched))
