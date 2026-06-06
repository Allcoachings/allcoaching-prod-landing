import re

NEW = {
 'how-to-get-paid-students-for-online-coaching-free':
   'How to get paid students for online coaching free in 2026 — why followers are not buyers, and how to fill paid seats with buying-intent marketplace traffic at ₹0 ad spend.',
 'best-app-for-state-psc-coaching-educators':
   'Best app for state PSC coaching educators (UPPSC, BPSC, RAS) in 2026: choose by aspirant discovery, vernacular support and a PYQ test-series stack, not features, at ₹0 upfront.',
 'online-platform-for-ctet-coaching-teachers':
   'Online platform for CTET coaching teachers in 2026: why recorded batches win — record the evergreen CDP syllabus once and sell it across every exam cycle, at ₹0 upfront.',
 'video-drm-protection-for-indian-course-creators':
   'Video DRM protection for Indian course creators in 2026: what video DRM really is, how course piracy happens in India, and the practical protection most educators actually need.',
 'recorded-lecture-hosting-cheap-india-for-teachers':
   'Recorded lecture hosting cheap in India for teachers: the real cost is bandwidth, not storage — the cheapest answer is ₹0 bundled hosting, unlimited videos, no storage bill.',
}

for slug, desc in NEW.items():
    fp = 'blog/' + slug + '.html'
    s = open(fp, encoding='utf-8').read()
    assert '"' not in desc, slug  # would break the content="" attribute
    s2 = re.sub(r'(<meta name="description" content=")(.*?)(" />)',
                lambda m: m.group(1) + desc + m.group(3), s, count=1)
    assert s2 != s and ('content="' + desc + '"') in s2, 'replace failed: ' + slug
    open(fp, 'w', encoding='utf-8', newline='').write(s2)
    print(f'{slug[:46]:46} new meta desc = {len(desc)} chars')
print('DONE')
