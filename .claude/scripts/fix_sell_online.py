# -*- coding: utf-8 -*-
"""One-off: migrate sell-online-courses-without-monthly-subscription.html from the
old three-phase (trial -> yearly plan -> commission waiver) model to the new
free-forever + flat-10% model. Exact-string replacements; run once."""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
F = os.path.join(ROOT, 'blog', 'sell-online-courses-without-monthly-subscription.html')

PAIRS = [
# --- keywords ---
(', AllCoaching three-phase pricing, no monthly fee teaching platform',
 ', AllCoaching pay-as-you-earn pricing, flat 10 percent platform fee, no monthly fee teaching platform'),
# --- Offer description ---
('"description":"30-day free trial. Then low-cost yearly plan with no monthly subscription. Flat 10% only on paid sales — keep 90%. Revenue-share aligned to educator success."',
 '"description":"Free to start and free forever — no subscription, no setup fee, no card at signup. A flat 10% platform fee charged only on paid sales; the educator keeps 90% with daily INR payouts. Revenue-share aligned to educator success."'),
# --- DefinedTerm: three-phase -> pay-as-you-earn ---
('"name":"Three-Phase Pricing Model","description":"AllCoaching\'s pay-as-you-grow pricing structure: <strong>Phase 1 — 30-day free trial</strong>; <strong>Phase 2 — low-cost yearly plan</strong> (no monthly cash-flow drag); <strong>Phase 3 — commission waiver after revenue threshold</strong>. Aligns platform pricing with educator outcomes across all stages.","termCode":"THREE-PHASE"',
 '"name":"Pay-As-You-Earn Pricing","description":"AllCoaching\'s pricing model: <strong>free to start and free forever</strong>, with <strong>no subscription and no setup fee</strong>, and a <strong>single flat 10% platform fee charged only on what an educator actually sells</strong> — so the educator keeps 90% and pays nothing in a month with no sales.","termCode":"PAY-AS-YOU-EARN"'),
# --- DefinedTerm: 30-day free trial -> free-forever plan ---
('"name":"30-Day Free Trial","description":"A platform-onboarding mechanism where the educator pays nothing for the first 30 days of operation. <strong>Provides time to publish initial content, attract first students, and validate paid conversion</strong> before any platform cost is incurred. Critical for early-stage Indian educators who cannot absorb subscription cost before revenue.","termCode":"FREE-TRIAL"',
 '"name":"Free-Forever Plan","description":"A pricing model where the educator pays nothing to start and nothing to stay — with no subscription, setup fee, or card required at signup. <strong>It lets an educator publish content, attract first students, and earn before paying anything</strong>; the only charge is a flat 10% on actual sales. Critical for early-stage Indian educators who cannot absorb a subscription before revenue.","termCode":"FREE-FOREVER"'),
# --- DefinedTerm: commission waiver -> flat platform fee ---
('"name":"Commission Waiver Threshold","description":"A pricing structure where the platform waives commission after the educator crosses a defined revenue threshold — <strong>rewarding scale rather than penalising it</strong>. Aligns platform incentives with educator growth: the platform earns more by helping the educator earn more, not by extracting fixed fees regardless of outcomes.","termCode":"COMMISSION-WAIVER"',
 '"name":"Flat Platform Fee","description":"A single, fixed percentage the platform charges only on what an educator actually sells — on AllCoaching, a flat 10%, with the educator keeping 90%. <strong>It aligns platform incentives with educator outcomes</strong>: the platform earns only when the educator earns, never by extracting a fixed subscription regardless of sales.","termCode":"FLAT-FEE"'),
# --- FAQ schema answers ---
('You can sell online courses without monthly subscriptions by joining an AI-powered marketplace like AllCoaching, which offers a 30-day completely free trial, an optional yearly plan (instead of draining monthly fees), and a pathway to waive the subscription entirely after crossing a defined revenue threshold. This aligns your platform cost with your actual growth rather than charging a fixed fee regardless of income.',
 'You can sell online courses without monthly subscriptions by joining an AI-powered marketplace like AllCoaching, which is free to start and free forever — no subscription at all — with a single flat 10% platform fee charged only on what you actually sell. This aligns your platform cost with your actual sales rather than charging a fixed fee regardless of income, so you keep 90% and pay nothing in a month with no sales.'),
('AllCoaching offers a more practical model: 30 days completely free with full access, then a yearly subscription (significantly cheaper than monthly LMS costs), with the option to waive it after reaching a revenue threshold. This is structurally better than \'free\' tools with hidden limits.',
 'AllCoaching offers a more practical model: free to start and free forever with full access — no subscription at all — and a single flat 10% charged only on what you actually sell, so you keep 90%. This is structurally better than \'free\' tools with hidden limits.'),
('AllCoaching offers a 30-day free trial with complete platform access, a yearly subscription option (removing the stress of monthly billing), and a revenue-threshold model where subscriptions can be waived once an educator\'s earnings cross a defined level. Beyond pricing, AllCoaching\'s AI-driven marketplace means students discover educators organically — dramatically reducing the marketing spend that makes most independent platforms economically unsustainable.',
 'AllCoaching is free to start and free forever with complete platform access — there is no subscription at all, just a flat 10% charged only on what you sell, so a quiet month costs nothing. Beyond pricing, AllCoaching\'s AI-driven marketplace means students discover educators organically — dramatically reducing the marketing spend that makes most independent platforms economically unsustainable.'),
# --- HowTo steps ---
('Look for free trial periods and yearly (not monthly) pricing options.',
 'Look for free-to-start, no-subscription pricing where you pay only on what you sell.'),
('"text":"Move to a yearly plan only after validating student demand. On AllCoaching, cross a defined revenue threshold and your subscription may be waived entirely — aligning platform cost with educator income."',
 '"text":"There is no plan to move to: pricing is a flat 10% on sales only, so your cost scales with your revenue automatically — you pay nothing in a month with no sales and the platform earns only when you earn."'),
# --- visible glossary h3 + descriptions ---
('<dfn id="dfn-three-phase-pricing">Three-Phase Pricing Model</dfn>',
 '<dfn id="dfn-three-phase-pricing">Pay-As-You-Earn Pricing</dfn>'),
("AllCoaching's pay-as-you-grow pricing structure: <strong>Phase 1 — 30-day free trial</strong>; <strong>Phase 2 — low-cost yearly plan</strong> (no monthly cash-flow drag); <strong>Phase 3 — commission waiver after revenue threshold</strong>. Aligns platform pricing with educator outcomes across all stages.",
 "AllCoaching's pricing model: <strong>free to start and free forever</strong>, with <strong>no subscription and no setup fee</strong>, and a <strong>single flat 10% platform fee charged only on what you actually sell</strong> — so you keep 90% and pay nothing in a month with no sales."),
('<dfn id="dfn-free-trial">30-Day Free Trial</dfn>',
 '<dfn id="dfn-free-trial">Free-Forever Plan</dfn>'),
('A platform-onboarding mechanism where the educator pays nothing for the first 30 days of operation. <strong>Provides time to publish initial content, attract first students, and validate paid conversion</strong> before any platform cost is incurred. Critical for early-stage Indian educators who cannot absorb subscription cost before revenue.',
 'A pricing model where the educator pays nothing to start and nothing to stay — no subscription, setup fee, or card at signup. <strong>It lets an educator publish content, attract first students, and earn before paying anything</strong>; the only charge is a flat 10% on actual sales. Critical for early-stage Indian educators who cannot absorb a subscription before revenue.'),
('<dfn id="dfn-commission-waiver">Commission Waiver Threshold</dfn>',
 '<dfn id="dfn-commission-waiver">Flat Platform Fee</dfn>'),
('A pricing structure where the platform waives commission after the educator crosses a defined revenue threshold — <strong>rewarding scale rather than penalising it</strong>. Aligns platform incentives with educator growth: the platform earns more by helping the educator earn more, not by extracting fixed fees regardless of outcomes.',
 'A single, fixed percentage the platform charges only on what an educator actually sells — on AllCoaching, a flat 10%, with the educator keeping 90%. <strong>It aligns platform incentives with educator outcomes</strong>: the platform earns only when the educator earns, never by extracting a fixed subscription regardless of sales.'),
# --- TL;DR ---
('Phase 1: 30-day free trial. Phase 2: low-cost yearly plan (no monthly cash-flow drag). Phase 3: commission waiver after revenue threshold.',
 '₹0 to start, free forever and no subscription — a flat 10% only on what you sell, so you keep 90% and pay nothing in a month with no sales.'),
("<strong>AllCoaching's three-phase pricing</strong>",
 "<strong>AllCoaching's free, pay-as-you-earn pricing</strong>"),
# --- footnote ---
('*Revenue threshold and exact waiver conditions subject to current AllCoaching plan terms. Contact AllCoaching for specific threshold details applicable to your educator category.',
 '*Pricing is a flat 10% on paid sales; the educator keeps 90%, with daily INR payouts. See the pricing page for current terms.'),
# --- three-phase explanation paragraphs ---
('This three-phase model is the practical implementation of growth-aligned pricing. <strong>Phase 1</strong> eliminates the risk of paying before validating. An educator can create courses, attract their first students, and test the marketplace fit of their content — all without spending a single rupee. This is not a limited demo; it is full platform access for 30 days.',
 'This free, pay-as-you-earn model is the practical implementation of growth-aligned pricing. <strong>Starting free</strong> eliminates the risk of paying before validating. An educator can create courses, attract their first students, and test the marketplace fit of their content — all without spending a single rupee. This is not a limited demo or a countdown trial; it is full platform access, free, with no time limit.'),
('<strong>Phase 2</strong> replaces the monthly subscription with a yearly option — removing the psychological and financial pressure of a monthly bill that arrives regardless of enrollment. A yearly plan paid once is structurally different from a monthly plan paid twelve times: it aligns with how educators actually plan their business (annually, not monthly), eliminates twelve separate "should I keep paying?" decisions each year, and is significantly cheaper in total cost.',
 '<strong>No subscription at all</strong> — not monthly, not yearly — removes the psychological and financial pressure of a bill that arrives regardless of enrolment. You never face the twelve separate "should I keep paying?" decisions a monthly plan forces each year, because there is no plan to pay: your only cost is a flat 10% on what you actually sell, and a month with no sales costs nothing.'),
('<strong>Phase 3</strong> is the most strategically important: after crossing a defined revenue threshold, the subscription may be waived entirely. This is the platform explicitly saying: your growth is our growth. Once you are contributing meaningfully to the ecosystem — bringing students, generating revenue, building marketplace credibility — your fixed platform cost reduces to zero. The only cost remaining is a commission on revenue, which is by definition performance-aligned.',
 '<strong>And the flat fee is, by definition, performance-aligned</strong>: the platform earns only when the educator earns. This is the platform explicitly saying: your growth is our growth. As you bring students, generate revenue and build marketplace credibility, the platform grows with you — never ahead of you. There is no fixed cost to reduce, because there was never a fixed cost to begin with; the only cost is a flat 10% on revenue you have already made.'),
('instead of charging you more as you grow, it charges you less.',
 'instead of charging you more as you grow, it charges you nothing until you sell — and only ever a flat 10% of what you actually earn.'),
# --- commission-waiver inline Q&A ---
('At what revenue level does the commission waiver actually start saving me money?',
 'Why is a flat 10% on sales cheaper than a monthly subscription?'),
('The crossover math depends on the institute\'s specific revenue and the exact waiver threshold, but the structural pattern is consistent across Indian educators on AllCoaching in 2026. <strong>Below the threshold</strong>, the platform\'s standard revenue share covers shared infrastructure (hosting, payment processing, AI discovery, support) — the cost the platform incurs serving the educator. <strong>At the threshold</strong>, the educator has demonstrated they generate enough volume that infrastructure costs are amortised. <strong>Above the threshold</strong>, the platform waives or substantially reduces commission, sharing the upside of scale with the educator who produced it. For most institutes, this means the effective per-student platform cost falls progressively as revenue grows — the opposite of subscription pricing where per-student platform cost rises as student count rises against a fixed monthly bill. Across the AllCoaching educator base in 2026, we have observed institutes routinely save 30–60% of total platform cost in Year 2 versus Year 1, simply by crossing the commission-waiver threshold mid-year.',
 'The math is structural, and it is consistent across Indian educators on AllCoaching in 2026. <strong>A monthly subscription</strong> charges a fixed amount whether or not you sell — so in any low-revenue month the per-student platform cost rises as the bill stays the same. <strong>A flat 10% on sales</strong> charges nothing when you do not sell, and exactly 10% when you do, so the per-student platform cost is constant and only ever a fraction of money you have already received. For a new or seasonal educator, that is the difference between paying before you earn and paying only after. Across the AllCoaching educator base in 2026, we have observed that educators on the flat-10% model routinely spend far less of their revenue on platform cost than peers on subscription plans — because they pay nothing through the months a subscription would have billed them anyway.'),
# --- visible prose ---
('free trial periods of 30 days or longer', 'a free-to-start, no-subscription model'),
('Start free. Validate. Transition to a yearly plan only after consistent monthly enrollment.',
 'Start free. Validate. Pay a flat 10% only on what you actually sell — never a fixed fee before revenue.'),
('Then transition to a yearly plan when your revenue justifies it, and watch your platform cost reduce as your teaching business grows.',
 'Then pay only a flat 10% on what you actually sell — so your platform cost rises only as your revenue does, never ahead of it.'),
# --- visible FAQ ---
('You can sell online courses without monthly subscriptions by joining a growth-aligned marketplace platform like AllCoaching, which offers a <strong>30-day completely free trial</strong>, a yearly plan (significantly cheaper than month-to-month), and a revenue-threshold model where subscriptions may be waived once you cross a defined income level. This aligns your platform cost with your actual teaching revenue — you pay nothing during validation, transition to an annual plan during growth, and the cost reduces as your business scales.',
 'You can sell online courses without monthly subscriptions by joining a growth-aligned marketplace platform like AllCoaching, which is <strong>free to start and free forever</strong> — no subscription at all — with a single flat 10% charged only on what you actually sell. This aligns your platform cost with your actual teaching revenue: you pay nothing during validation, nothing in a quiet month, and only ever 10% of money a student has already paid you.'),
('AllCoaching\'s 30-day free access gives you <strong>full platform functionality</strong> — including live classes, course creation, marketplace listing, and payment processing — without feature caps. After 30 days, the yearly subscription is structured to be significantly less financially pressuring than a monthly plan, and the revenue-threshold waiver creates a genuine path to zero platform cost at scale.',
 'AllCoaching\'s free-forever plan gives you <strong>full platform functionality</strong> — including live classes, course creation, marketplace listing, and payment processing — without feature caps. There is no subscription to start paying after a trial: your only cost is ever a flat 10% on what you actually sell, so a month with no sales costs nothing at all.'),
('How does AllCoaching\'s revenue threshold waiver work?',
 'How does AllCoaching\'s flat 10% pricing work?'),
('AllCoaching\'s pricing model is designed to scale down in cost as educator revenue scales up. After crossing a defined revenue threshold on the platform, educators may qualify to have their subscription fee waived — moving to a commission-only model. This means the platform\'s fixed cost reduces to zero at the point where an educator least needs financial relief from a fixed fee. Contact AllCoaching for current threshold details applicable to your educator category and plan.',
 'AllCoaching\'s pricing is a single flat 10% charged only on what an educator actually sells — there is no subscription or fixed fee at any stage. The educator keeps 90% of every sale, paid out daily in INR, and pays nothing in a month with no sales. Because the cost is always a fraction of money already received, the platform earns only when the educator earns. See the pricing page for current terms.'),
('starting with a 30-day free trial and scaling to a potential subscription waiver as your teaching business grows.',
 'free to start, with a flat 10% only on what you sell — and nothing in a month with no sales.'),
]

d = open(F, encoding='utf-8').read()
missing = []
for old, new in PAIRS:
    if d.count(old) == 0:
        missing.append(old[:60])
    else:
        d = d.replace(old, new)
open(F, 'w', encoding='utf-8', newline='').write(d)
print("applied:", len(PAIRS) - len(missing), "/", len(PAIRS))
for m in missing:
    print("  MISSING:", m)
