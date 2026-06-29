# -*- coding: utf-8 -*-
"""Reorient vs/classplus.html for the 'classplus pricing' keyword + correct pricing to reported reality."""
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
f = "vs/classplus.html"
h = open(f, encoding="utf-8").read()

ND = "–"  # en dash

pairs = [
# --- HEAD: SEO reorientation to 'classplus pricing' ---
("<title>AllCoaching vs Classplus — Honest 2026 India Comparison · Cost · Features</title>",
 "<title>Classplus Pricing in 2026 — Plans, Real Cost &amp; AllCoaching Comparison</title>"),

('<meta name="description" content="The honest 2026 comparison of AllCoaching vs Classplus for Indian educators. Real Year 1 cost breakdown (Classplus ₹4–11 lakh vs AllCoaching ₹1.32 lakh), feature-by-feature analysis across 12 dimensions, migration playbook with timeline, and the structural difference between a white-label app builder (Classplus) and an educator-first marketplace (AllCoaching)." />',
 '<meta name="description" content="Classplus pricing in 2026, explained honestly: plans are quote-based and not publicly listed, with reported annual fees of roughly ₹8,000–₹50,000+ plus a transaction commission and add-ons. See the real Year-1 cost for a ₹10 lakh educator — and the transparent ₹0 + flat-10% alternative on the AllCoaching marketplace." />'),

('<meta name="keywords" content="AllCoaching vs Classplus, Classplus vs AllCoaching, AllCoaching alternative to Classplus, Classplus cost 2026, AllCoaching pricing comparison, white label vs marketplace coaching India, Classplus review, migrate from Classplus to AllCoaching" />',
 '<meta name="keywords" content="Classplus pricing, Classplus price, Classplus cost 2026, Classplus plans, how much does Classplus cost, is Classplus free, Classplus subscription fee, Classplus commission, is Classplus pricing transparent, AllCoaching vs Classplus, Classplus alternative, migrate from Classplus" />'),

('<meta property="og:title" content="AllCoaching vs Classplus — Honest 2026 Comparison" />',
 '<meta property="og:title" content="Classplus Pricing 2026 — What It Really Costs (Honest Breakdown)" />'),

('<meta property="og:description" content="Real Year 1 cost breakdown: Classplus ₹4–11 lakh vs AllCoaching ₹1.32 lakh. 12-dimension feature comparison, migration playbook, structural difference (white-label vs marketplace). Founder-written." />',
 '<meta property="og:description" content="Classplus pricing is quote-based — reported ₹8,000–₹50,000+/year plus commissions. The honest Year-1 cost breakdown vs a transparent ₹0 + flat-10% alternative on AllCoaching." />'),

('<meta name="twitter:title" content="AllCoaching vs Classplus — Honest 2026 Comparison" />',
 '<meta name="twitter:title" content="Classplus Pricing 2026 — The Honest Cost Breakdown" />'),

('<meta name="twitter:description" content="Classplus ₹4–11 lakh Year 1 vs AllCoaching ₹1.32 lakh. Founder-written honest comparison + migration playbook." />',
 '<meta name="twitter:description" content="Classplus pricing is quote-based (reported ₹8k–₹50k+/yr + commissions). Real Year-1 math vs a transparent ₹0 + flat-10% alternative." />'),

# dateModified bumps
('<meta property="og:updated_time" content="2026-05-16T19:00:00+05:30" />',
 '<meta property="og:updated_time" content="2026-06-29T12:00:00+05:30" />'),
('<meta property="article:modified_time" content="2026-05-16" />',
 '<meta property="article:modified_time" content="2026-06-29" />'),
('<meta name="article:modified_time" content="2026-05-16" />',
 '<meta name="article:modified_time" content="2026-06-29" />'),

# --- JSON-LD ---
('"description":"A founder-written comparison of AllCoaching (India\'s first educator-first marketplace) and Classplus (white-label coaching app builder). Year 1 cost analysis (₹4–11 lakh vs ₹1.32 lakh), 12-row feature matrix, structural architecture difference, migration playbook for educators moving from Classplus to AllCoaching, and the use cases where each platform genuinely fits.",',
 '"description":"A founder-written, honest guide to Classplus pricing in 2026 — reported quote-based annual plans of roughly ₹8,000–₹50,000+ plus transaction commissions and add-ons — compared with AllCoaching (India\'s educator-first marketplace), with a real Year-1 cost analysis for a ₹10 lakh educator, a 12-row feature matrix, a migration playbook, and the use cases where each platform genuinely fits.",'),

# JSON-LD Q1 ending
("Year 1 cost difference for a ₹10 lakh revenue educator: Classplus ₹4–11 lakh, AllCoaching ₹1.32 lakh.\"}},",
 "Year 1 cost for a ₹10 lakh revenue educator: Classplus roughly ₹1.5–4 lakh or more (platform fees plus your own marketing), AllCoaching ₹1 lakh (flat 10%, marketing and discovery included).\"}},"),

# JSON-LD Q2 full text
('{"@type":"Question","name":"What does Classplus actually cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"Classplus headline pricing starts around ₹2,500–₹1,25,000 per month depending on tier, but the true Year 1 cost includes setup ₹25K–₹2L, monthly software 30K–15L, 1.5–4% transaction commission on top of payment gateway 0.3–1%, SMS/WhatsApp credit packs ₹2K–8K/month, branding refresh fees, 15–25% annual escalation, and marketing the educator pays themselves (₹6–18L/year for sustained student flow). Real Year 1 all-in for a typical ₹10 lakh revenue institute: ₹4–11 lakh."}},',
 '{"@type":"Question","name":"What does Classplus actually cost in 2026?","acceptedAnswer":{"@type":"Answer","text":"Classplus does not publish public pricing — it is quote-based and sales-led. Reported annual plans range roughly from ₹8,000 to ₹50,000 or more depending on the features you need, and Classplus also takes a transaction commission on your sales, with SMS/WhatsApp credits and setup often charged separately. Because there is no built-in discovery, you also fund your own marketing. For a ₹10 lakh revenue institute, a realistic Year-1 total — platform fees plus modest self-marketing — works out to roughly ₹1.5–4 lakh or more. Always confirm a current quote and commission rate directly with Classplus."}},'
 # + insert 2 new pricing FAQs after Q2
 '\n      {"@type":"Question","name":"Is Classplus free, or does it have a free plan?","acceptedAnswer":{"@type":"Answer","text":"No — Classplus is not free and does not offer a permanent free plan for educators. It is a paid, subscription-based platform with quote-based annual pricing, and it also takes a transaction commission on your sales. There may be a demo or trial, but running your coaching on Classplus is a paid commitment. If you want a genuinely free way to start — a branded app, courses, payments and discovery at ₹0 upfront, paying only a flat 10% when you actually sell — that is AllCoaching\'s model, not Classplus\'s."}},'
 '\n      {"@type":"Question","name":"Is Classplus pricing transparent?","acceptedAnswer":{"@type":"Answer","text":"Not really — Classplus does not publish its prices publicly, so you have to request a quote from their sales team, and the final figure depends on your plan, negotiation and add-ons. This lack of upfront, listed pricing is a common frustration for educators comparing options. AllCoaching takes the opposite approach: the price is public and simple — ₹0 to start, no subscription, and a flat 10% on paid sales only, with the educator keeping 90%. You can see exactly what you will pay before signing up."}},'),

# --- VISIBLE BODY ---
# hero lede
('Real Year 1 math (Classplus <strong style="color:#15110D;">₹4–11 lakh</strong> vs AllCoaching <strong style="color:#15110D;">₹1.32 lakh</strong>), 12-row feature matrix, and the structural reason marketplaces beat white-label app builders for 90%+ of Indian educators under ₹2 Cr revenue.',
 '<strong>Classplus pricing is quote-based</strong> (reported ₹8,000–₹50,000+ a year plus commissions), so the real Year-1 cost for a ₹10 lakh educator runs to roughly <strong style="color:#15110D;">₹1.5–4 lakh+</strong> once you add your own marketing — vs AllCoaching\'s transparent <strong style="color:#15110D;">₹1 lakh</strong> (flat 10%, discovery included).'),

# TL;DR
('<li><strong>Real Year 1 cost for a ₹10L educator: Classplus ₹4–11 lakh</strong> (setup + monthly + commission stack + escalation + marketing) <strong>vs AllCoaching ₹1.32 lakh</strong> (subscription + 10% all-inclusive).</li>',
 '<li><strong>Classplus pricing is quote-based</strong> — reported ₹8,000–₹50,000+/year plus commission; real Year-1 total for a ₹10L educator ≈ <strong>₹1.5–4 lakh+</strong> with your own marketing, <strong>vs AllCoaching ₹1 lakh</strong> (flat 10%, all-inclusive).</li>'),

# table: setup fee
("<td>₹25,000 – ₹2,00,000</td>",
 "<td>Reported up to ~₹25,000 (varies, quote-based)</td>"),
# table: monthly/annual software
("<td>₹2,500 – ₹1,25,000 / month (₹30K – 15L / year)</td>",
 "<td>₹8,000 – ₹50,000+ / year (reported; quote-based, not publicly listed)</td>"),
# table: marketing row
("<td>Educator pays separately (₹6–18 lakh / year)</td>",
 "<td>You fund your own marketing — no built-in discovery</td>"),
# table: Real Year 1 cost
('<td><span class="cmp-no">₹4–11 lakh</span></td>',
 '<td><span class="cmp-no">₹1.5–4 lakh+</span></td>'),
('<td class="us cmp-yes">₹1.32 lakh (13.2% of revenue)</td>',
 '<td class="us cmp-yes">₹1 lakh (flat 10%, all-inclusive)</td>'),
# source note
("Source for Classplus pricing data: public Classplus listings + industry contracts",
 "Classplus does not publish public pricing; figures are reported ranges from third-party listings (Techjockey, SoftwareSuggest) and vary — confirm a current quote with Classplus"),

# math section heading -> add keyword
('<h2 class="h-chap font-display mt-3 mb-6 text-center">Year 1 actual cost — <span class="grad-text">side by side.</span></h2>',
 '<h2 class="h-chap font-display mt-3 mb-6 text-center">Classplus pricing vs AllCoaching — <span class="grad-text">Year 1, side by side.</span></h2>'),

# math box Classplus rows
('<div class="math-row"><span class="lbl">Setup fee (one-time)</span><span class="val val-bad">₹50,000</span></div>',
 '<div class="math-row"><span class="lbl">Setup fee (varies)</span><span class="val val-bad">₹25,000</span></div>'),
('<div class="math-row"><span class="lbl">Monthly software × 12</span><span class="val val-bad">₹1,80,000</span></div>',
 '<div class="math-row"><span class="lbl">Subscription (annual plan)</span><span class="val val-bad">₹45,000</span></div>'),
('<div class="math-row"><span class="lbl">SMS / WhatsApp credit packs × 12</span><span class="val val-bad">₹48,000</span></div>',
 '<div class="math-row"><span class="lbl">SMS / WhatsApp credits</span><span class="val val-bad">₹24,000</span></div>'),
('<div class="math-row"><span class="lbl">Marketing / Meta+Google Ads (modest)</span><span class="val val-bad">₹3,00,000</span></div>',
 '<div class="math-row"><span class="lbl">Your own marketing (no discovery)</span><span class="val val-bad">₹1,00,000</span></div>'),
('<div class="math-row"><span class="lbl">18% GST on subscription + commission</span><span class="val val-bad">₹37,260</span></div>',
 '<div class="math-row"><span class="lbl">18% GST on platform fees</span><span class="val val-bad">₹18,000</span></div>'),
('<div class="math-total"><span class="lbl">Year 1 all-in</span><span class="val val-bad">₹6.47 L</span></div>',
 '<div class="math-total"><span class="lbl">Year 1 all-in</span><span class="val val-bad">₹2.44 L</span></div>'),

# verdict
('<div class="verdict-num mt-3">₹5.47 L</div>',
 '<div class="verdict-num mt-3">₹1.44 L</div>'),
('For a ₹10 lakh revenue educator, AllCoaching costs <em style="color:#C58B43;">4.9× less</em> than Classplus in Year 1.',
 'For a ₹10 lakh revenue educator, AllCoaching costs <em style="color:#C58B43;">2.4× less</em> than Classplus in Year 1 — and the price is transparent.'),

# visible FAQ Q1 ending
("Year 1 cost difference for a ₹10 lakh revenue educator: Classplus ₹4–11 lakh, AllCoaching ₹1.32 lakh.</p>",
 "Year 1 cost for a ₹10 lakh revenue educator: Classplus roughly ₹1.5–4 lakh or more (platform fees plus your own marketing), AllCoaching ₹1 lakh (flat 10%, marketing and discovery included).</p>"),

# visible FAQ Q2 full
('<p>Classplus headline pricing starts around ₹2,500–₹1,25,000 per month, but the <strong>true Year 1 cost</strong> includes setup ₹25K–₹2L, monthly software 30K–15L, 1.5–4% transaction commission on top of payment gateway 0.3–1%, SMS/WhatsApp credit packs ₹2K–8K/month, branding refresh fees, 15–25% annual escalation, and marketing the educator pays themselves (₹6–18L/year). <strong>Real Year 1 all-in for a ₹10L institute: ₹4–11 lakh.</strong></p>',
 '<p><strong>Classplus does not publish public pricing</strong> — it is quote-based and sales-led. Reported annual plans range roughly from ₹8,000 to ₹50,000 or more depending on features, and Classplus also takes a transaction commission on your sales, with SMS/WhatsApp credits and setup often charged separately. Because there is no built-in discovery, you also fund your own marketing. For a ₹10 lakh revenue institute, a realistic Year-1 total — platform fees plus modest self-marketing — works out to roughly <strong>₹1.5–4 lakh or more</strong>. Always confirm a current quote and commission rate directly with Classplus.</p>'),
]

for old, new in pairs:
    n = h.count(old)
    assert n == 1, f"count {n} for: {old[:70]!r}"
    h = h.replace(old, new, 1)

# insert 2 new visible FAQ <details> after Q2, before Q3 ("Can I migrate")
vis_anchor = '      <details class="faq-item">\n        <summary>Can I migrate from Classplus to AllCoaching?</summary>'
assert h.count(vis_anchor) == 1
new_vis = (
'      <details class="faq-item">\n'
'        <summary>Is Classplus free, or does it have a free plan?</summary>\n'
'        <p>No — <strong>Classplus is not free and does not offer a permanent free plan</strong> for educators. It is a paid, subscription-based platform with quote-based annual pricing, and it also takes a transaction commission on your sales. There may be a demo or trial, but running your coaching on Classplus is a paid commitment. If you want a genuinely free way to start — a branded app, courses, payments and discovery at ₹0 upfront, paying only a flat 10% when you actually sell — that is AllCoaching\'s model, not Classplus\'s.</p>\n'
'      </details>\n\n'
'      <details class="faq-item">\n'
'        <summary>Is Classplus pricing transparent?</summary>\n'
'        <p>Not really — <strong>Classplus does not publish its prices publicly</strong>, so you have to request a quote from their sales team, and the final figure depends on your plan, negotiation and add-ons. This lack of upfront, listed pricing is a common frustration for educators comparing options. AllCoaching takes the opposite approach: the price is public and simple — ₹0 to start, no subscription, and a flat 10% on paid sales only, with the educator keeping 90%. You can see exactly what you will pay before signing up.</p>\n'
'      </details>\n\n'
)
h = h.replace(vis_anchor, new_vis + vis_anchor, 1)

open(f, "w", encoding="utf-8").write(h)
print("OK: all replacements applied")

# quick stats
import re
print("  'classplus pricing' (any case):", len(re.findall(r'classplus pricing', h, re.I)))
print("  stale figures left (1.32 / 4.9x / 4-11 lakh / 6.47):",
      len(re.findall(r'1\.32 lakh|4\.9×|₹4–11 lakh|6\.47 L|5\.47 L', h)))
print("  visible <summary> count:", h.count('<summary>'))
import json
faq = re.search(r'"@type":"FAQPage".*?"mainEntity":\[(.*?)\]\s*\}\s*</script>', h, re.S).group(1)
print("  JSON-LD Question count:", faq.count('"@type":"Question"'))
PY = None
