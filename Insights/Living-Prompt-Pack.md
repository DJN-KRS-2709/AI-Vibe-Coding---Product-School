LIVING PROMPT PACK
━━━━━━━━━━━━━━━━━━━━━━

── CONSTRAINT TEMPLATES ──
ALWAYS: Match existing design language from the attached screenshot
NEVER: Add new backend functionality or API calls
ALWAYS: Include loading, error, and empty states for every screen
NEVER: Use placeholder text like lorem ipsum or "Sample User"
ALWAYS: Keep navigation consistent across all screens
NEVER: Rebuild screens that already exist — only modify what I specify

── OUTPUT TEMPLATES ──
[Expand]: Add a [screen type] screen: [what it shows]. Match the attached [reference] screenshot. Navigation between all [N] screens.
[Behavior]: Add a loading state with skeleton screens for [section]. Add an empty state for [scenario]: "[message]". Add an error state for [failure]: "[message]". Same design language.
[Refine]: The [screen] needs [change]. [Specific instruction]. Don't change anything else.

── CHAIN ENTRIES ──

--- Entry 1 (Mar 26, 2026) ---
CONTEXT:

1. SCENARIO BRIEF
Company: SubShield is a seed-stage consumer fintech startup that helps users find, manage, cancel, or downgrade recurring subscriptions by connecting to their bank account via PSD2/Open Banking. The company has 22 employees, ~€1.1M ARR, and is trying to prove retention before scaling acquisition spend.

Problem: SubShield solves a real pain point, but too many users leave before they experience a credible savings outcome. The business impact is severe because 57% of new users churn within 90 days, which weakens premium conversion, lowers LTV, and makes paid growth harder to justify.

Key Data:

48% of new signups start bank connection, but only 35% complete it

61% of users who begin SCA finish it; the rest abandon during authentication

56% of connected users open the Subscription Hub in their first session

19% of activated users complete a cancel or downgrade action within 14 days

Users shown a clear savings opportunity in-session retain 2.0x better at Day 30 than users who only see detected subscriptions

Constraints: SubShield depends on third-party PSD2/Open Banking providers and bank-specific SCA flows it cannot fully control. It has read-only access, so it cannot guarantee one-tap cancellation for every merchant. It also has to earn trust despite privacy concerns, masked wallet charges, and messy transaction descriptors.

Your Job: Build a prototype that proves whether reducing consent/SCA friction and surfacing immediate savings opportunities can increase activation and first-action rates. The prototype needs to show that users will trade bank access for fast, trustworthy subscription savings.

Competing Hypotheses:

VP of Growth: “This is mainly a trust problem. People won’t connect their bank unless the value is obvious immediately.”

Head of Data Science: “The bigger issue is detection confidence. If the merchant names look fuzzy or wrong, users stop believing the product works.”

Director of Customer Success: “Users get through connect, then stall because taking action feels too manual. The value dies when canceling feels harder than expected.”

2. USER & STAKEHOLDER FEEDBACK
User quotes

Time-poor Maximizer, active user, Week 2: “Once it showed me I could save about €34 a month, I was in. Before that, it just felt like a lot of bank permissions for a maybe.”

Churned user, Day 3: “I got to the bank verification step and just stopped. It felt like way too much friction for something I hadn’t seen value from yet.”

Budget-Conscious Parent, at-risk user, Day 9: “I liked the idea, but I wasn’t fully sure the app had identified everything correctly. I didn’t want to make decisions on half-right data.”

Deal Seeker / Student, churned user, Day 5: “I wanted help catching trials before they renewed, but the app asked me to connect my bank before showing anything useful. That was a hard sell.”

Satisfied user, Month 1: “It found two subscriptions I forgot about and one that had gone up in price. That made it feel instantly worth it.”

At-risk user, Day 14: “I connected fine, but after that I was basically staring at a list. I needed the app to tell me what was worth acting on first.”

Churned user, Day 1: “You kept saying ‘read-only,’ but giving bank access still felt invasive. I wasn’t convinced the payoff would be big enough.”

Budget-Conscious Parent, retained user, Month 2: “The savings tracker is what kept me around. Seeing the yearly number go up made it feel like I was actually getting something back.”

Deal Seeker / Student, active user, Week 3: “The only reason I came back was because it flagged a trial ending soon. That kind of alert is what I wanted from day one.”

Frustrated user, Day 11: “Some of the subscriptions were marked as ‘suspected’ and that just killed my confidence. If you’re not sure, I’m not sure either.”

Stakeholder quotes

CEO: “If users won’t connect their bank for subscription savings, the whole model breaks. That’s the assumption we have to test fastest.”

Engineering Lead: “We can improve the UX, but some of the drop-off is caused by bank-specific SCA flows we don’t control.”

Customer Support Lead: “The pattern I hear is trust first, then confusion, then disappointment. People expect it to feel more automatic than it does.”

Lifecycle Marketing Manager: “The users who stay usually hit one clear savings moment early. The ones who just browse detected subscriptions rarely come back.”

3. QUANTITATIVE METRICS TABLE
| Metric | Value | Segment | Notes |

| --------------------------------------------- | ------- | ------------------------------ | --------------------------------------------------------------------------- |

| 90-day churn rate | 57% | All new signups | Core business problem; most churn happens before users see realized savings |

| Bank connection start rate | 48% | All new signups | Interest is decent, but many users hesitate before starting |

| Bank connection completion rate | 35% | All new signups | Major activation drop between intent and completion |

| SCA completion rate | 61% | Users who start SCA | Strong friction point in onboarding |

| Consent-screen abandonment rate | 27% | Users who view consent | Indicates trust/privacy hesitation |

| Subscription Hub view rate | 56% | Connected users | Many connected users still do not reach clear value |

| Detected subscriptions per connected user | 4.8 | Connected users | Median number of recurring subscriptions surfaced |

| Low-confidence match rate | 23% | Connected users | Includes masked wallet descriptors and noisy merchant names |

| 14-day cancel/downgrade action rate | 19% | Activated users | Below target for habit-forming value |

| Users shown in-session savings estimate | 39% | Connected users | Leading indicator tied directly to the hypothesis |

| Day-30 retention | 31% | All new signups | Retention remains weak without fast value |

| Day-30 retention after savings estimate shown | 46% | Connected users | Roughly 2.0x higher than users who only saw a subscription list |

| 7-day return rate | 28% | All new signups | Suggests weak re-engagement after first session |

| NPS after first successful savings action | +29 | Users who cancelled/downgraded | Satisfaction increases sharply once value is tangible |

| NPS without first savings action | -10 | Connected non-actors | Users perceive setup effort without enough reward |

| Estimated monthly revenue lost to early churn | €44,000 | Business impact | Includes lost premium conversions and weaker referral/LTV economics |

REFERENCE:

Use my Figma as the visual reference, match styles and icons attached

Use my PRD as the source of product logic

CONSTRAINTS:

HYPOTHESIS: If we reduce consent/SCA friction and show immediate savings opportunities after bank connect, then activation and first-action rates will increase, because users stay when SubShield proves value quickly and feels trustworthy.

KILL SWITCH: If users are not willing to trade bank access for clear subscription savings, the core product does not work.

EXPLORING: Is 90-day churn mainly caused by trust/connect friction or by failure to show fast, credible savings value after connection?

FIDELITY: Functional App

VALIDATED IF: At least 60% of new users connect and view subscriptions on Day 1, and at least 30% complete a cancel/downgrade action within 14 days

INVALIDATED IF: Users still fail to reach first value fast enough, and activation or action rates remain below target after fixing trust and SCA friction.

COPY: Use real user quotes in the UI, not placeholder text

CRITICAL: Build a product a user interacts with, NOT a dashboard or analysis

OUTPUT:

Build: A 4-screen clickable mobile flow that a real SubShield user can interact with.

Screens: 1. Consent / Trust screen: explain read-only bank access, privacy, and why connecting helps find subscription savings. 2. Bank connect + SCA screen: show the authentication step clearly with reassuring progress and low-friction UX. 3. First value screen: after connection, show detected subscriptions and an immediate savings opportunity like “You could save €34/month.” 4. Action confirmation screen: let the user choose a subscription to cancel or downgrade and show projected monthly/yearly savings.

This prototype tests: The user should be able to move from trust to connect, see immediate value, and begin an action so I can observe whether reducing consent/SCA friction and surfacing fast savings increases trust and first-action intent.

--- Entry 2 (Mar 26, 2026) ---
# Prompt Chain — Module 3

**Date:** 2026-03-26  
**Scenario:** Build Your Own  
**Starting point:** M2 prototype (5 screens, has states, reproducible)

---

## Prompt 1 — Expand

```
Add bank-specific branching flows and error handling to the current SubShield mobile prototype.

Important:

Do not redesign the whole app

Extend the existing 4-screen prototype

Keep the same design system, trust-first fintech tone, and current visual style

Build different connection and recovery flows depending on which bank the user selects

Bank-specific behavior:

When the user selects a bank, the prototype should show a slightly different connect/SCA experience and different possible failure states.

Create at least 3 example banks with distinct flows, such as:

Barclays
standard login + SMS / app verification

possible errors: timeout, wrong credentials, expired verification code

Credit Agricole
faster OAuth-style connect flow

possible errors: consent expired, redirect failed, provider temporarily unavailable

ING
slower multi-step authentication

possible errors: SCA abandoned, long loading delay, bank unavailable, retry required later

Requirements:

the flow should branch depending on the selected bank

each bank should feel slightly different in UI copy, step order, timing, and recovery pattern

preserve progress where possible

provide clear recovery options such as retry, continue later, get help, or choose another bank

avoid generic “Something went wrong” states

use calm, practical, trustworthy copy

Also add edge cases to the product flow after connect:

no subscriptions detected

only low-confidence / suspected subscriptions found

masked wallet charge or unclear merchant

cancel flow unavailable for this merchant

downgrade not available

manual follow-up needed

Goal:

Make the prototype feel realistic by showing that different banks create different authentication friction, and test whether users still trust the product and continue toward value when those bank-specific issues happen.
```

**Result:** Bank-specific branching flows (BankConnectScreen):

Barclays: SMS + app verification with errors for timeout, wrong credentials, and expired code
Crédit Agricole: Fast OAuth redirect with errors for consent expiry, redirect failure, and provider unavailability
ING: Slower multi-step auth with errors for SCA abandonment, slow connection, and bank downtime
Each bank shows distinct UI copy, step count, timing, and auth method
A "Simulate error" toggle lets you demo error states — retrying always succeeds
Error screens have contextual recovery options (retry, continue later, get help, choose another bank) with reassuring copy
Post-connect edge cases (SubscriptionHub + Detail):

No subscriptions detected: Empty state with option to connect another bank
Low-confidence only: All suspected charges with abbreviated merchant names and a warning banner
Masked wallet charges: Apple Pay/Google Pay charges with explanatory notes about what they might be
Cancel unavailable: Adobe and unclear merchants show "direct cancel not available" with manual follow-up logging
Downgrade unavailable: Shows inline explanation when plan switching isn't possible through SubShield
A demo switcher at the bottom of the hub lets you toggle between edge cases

## Prompt 2 — Behavior

```
Remove all demo mode toggles, testing switches, scenario selectors, and fake control panels from the prototype.

Important:

Do not redesign the whole app

Keep the current visual design system and overall structure

Remove anything that feels like a prototype control layer or internal demo tooling

This should feel like a real user-facing product, not a sandbox

What I want instead:

Build clear, consistent behavior paths for each user flow.

Requirements:

Each bank flow should be triggered naturally by the bank the user selects

Do not expose “demo mode” or manual state toggles to the user

Each path should behave like a real product journey with logical transitions

Keep the flow deterministic and believable

Create clean user-facing paths for:

Successful connect flow

Failed SCA flow

Bank timeout / unavailable flow

No subscriptions detected flow

Low-confidence subscriptions flow

Successful first savings flow

Cancel/downgrade unavailable flow

Behavior rules:

The selected bank should determine which path the user enters

Errors should appear as natural states inside the flow, not as manually triggered demo options

Each path should have a clear start, transition, recovery step, and outcome

Preserve progress where appropriate

Always provide a next best action such as retry, continue later, get help, review subscriptions, or switch bank

Keep copy calm, concise, and trustworthy

Make the experience feel production-like and consistent across all screens

Goal:

Turn the prototype from a clickable demo with toggles into a realistic user flow with clear, consistent behavior paths.
```

**Result:** Removed all demo toggles and replaced them with deterministic, bank-driven behavior paths:

Revolut → smooth connect → no subscriptions detected
UBS → smooth connect → low-confidence/fuzzy merchant names
Barclays → smooth connect → normal subscriptions with savings
Crédit Agricole → consent expired error on first attempt → retry succeeds → masked wallet charges
ING → bank unavailable error on first attempt → retry succeeds → normal subscriptions
Every path now feels like a real product journey with natural error states, clear recovery actions, and logical transitions — no toggles or switchers visible to the user.

## Prompt 3 — Refine

```
Refine only the first screen of the current SubShield prototype to improve trust before bank connection.

Do not redesign the flow.

Do not change the rest of the prototype.

Keep the current premium mobile layout, burgundy branding, CTA placement, and overall structure.

Goal:

Reduce hesitation before tapping “Connect your bank” by adding stronger credibility, familiarity, and reassurance signals without making the screen look like a marketing landing page.

Keep these existing elements:

SubShield logo and brand at the top

main headline

3-bullet value structure

“Celebrate savings” bullet

testimonial block

main CTA

bottom reassurance row

bottom navigation

Make these exact improvements:

Headline area
keep the current headline structure, but add one short trust/social-proof line near the top section

place it directly below the headline or subtitle

this line should communicate one or two of these:

trusted usage

average savings

familiarity with known providers

keep it to one compact line, not a paragraph

Subtitle / trust language
replace generic security wording with more credible fintech wording

include PSD2 / Open Banking language

make it clear access is read-only and revocable

tone should be calm and factual, not hype

Bullet list
keep 3 bullets total

keep the “Celebrate savings” bullet

keep the first bullet about detecting recurring charges

soften the second bullet if it sounds too strong; prefer guided-action language over unrealistic instant-action language

maintain the detect → act → celebrate story

Testimonial block
revise the testimonial so it supports both trust and value

it should sound like a real user who was initially hesitant but felt reassured and then saw savings

keep the testimonial short and believable

do not make it sound like ad copy

Familiarity / provider trust
add a subtle trust cue showing support for familiar providers such as Revolut, UBS, Barclays, ING, N26, and PayPal

do this in a lightweight way, such as a small text row or compact chip row

do not make it visually heavy

CTA area
keep the CTA as “Connect your bank”

strengthen the reassurance around the CTA with clearer trust language

keep the reassurance concise and readable

Footer reassurance row
improve the current trust row so it reads more credibly

include concepts like:

read-only

PSD2/Open Banking

encrypted

revoke anytime

keep it short and scannable

Content rules:

do not remove the emotional savings payoff

do not remove the “Celebrate savings” concept

do not overload the screen with badges, shields, ratings, or long paragraphs

do not use fake awards or fake app-store style proof

avoid exaggerated claims

keep everything specific, believable, and premium

Design rules:

preserve whitespace and current visual hierarchy

keep the screen calm, clean, and trustworthy

this should feel like a real fintech product screen, not a pitch deck or landing page

Output:

Return the improved first screen with stronger trust signals and more credible copy, while keeping the rest of the prototype unchanged. Use realistic prototype copy. If a numeric trust claim like “10,000+ users” is not supported, replace it with a softer but credible line such as “Trusted by thousands of subscription-conscious users” or “Used across major European banks and payment providers.”
```

**Result:** # Prompt Chain — Module 3

**Date:** 2026-03-26  
**Scenario:** Build Your Own  
**Starting point:** M2 prototype (5 screens, has states, reproducible)

---

## Prompt 1 — Expand

```
Add bank-specific branching flows and error handling to the current SubShield mobile prototype.

Important:

Do not redesign the whole app

Extend the existing 4-screen prototype

Keep the same design system, trust-first fintech tone, and current visual style

Build different connection and recovery flows depending on which bank the user selects

Bank-specific behavior:

When the user selects a bank, the prototype should show a slightly different connect/SCA experience and different possible failure states.

Create at least 3 example banks with distinct flows, such as:

Barclays
standard login + SMS / app verification

possible errors: timeout, wrong credentials, expired verification code

Credit Agricole
faster OAuth-style connect flow

possible errors: consent expired, redirect failed, provider temporarily unavailable

ING
slower multi-step authentication

possible errors: SCA abandoned, long loading delay, bank unavailable, retry required later

Requirements:

the flow should branch depending on the selected bank

each bank should feel slightly different in UI copy, step order, timing, and recovery pattern

preserve progress where possible

provide clear recovery options such as retry, continue later, get help, or choose another bank

avoid generic “Something went wrong” states

use calm, practical, trustworthy copy

Also add edge cases to the product flow after connect:

no subscriptions detected

only low-confidence / suspected subscriptions found

masked wallet charge or unclear merchant

cancel flow unavailable for this merchant

downgrade not available

manual follow-up needed

Goal:

Make the prototype feel realistic by showing that different banks create different authentication friction, and test whether users still trust the product and continue toward value when those bank-specific issues happen.
```

**Result:** Bank-specific branching flows (BankConnectScreen):

Barclays: SMS + app verification with errors for timeout, wrong credentials, and expired code
Crédit Agricole: Fast OAuth redirect with errors for consent expiry, redirect failure, and provider unavailability
ING: Slower multi-step auth with errors for SCA abandonment, slow connection, and bank downtime
Each bank shows distinct UI copy, step count, timing, and auth method
A "Simulate error" toggle lets you demo error states — retrying always succeeds
Error screens have contextual recovery options (retry, continue later, get help, choose another bank) with reassuring copy
Post-connect edge cases (SubscriptionHub + Detail):

No subscriptions detected: Empty state with option to connect another bank
Low-confidence only: All suspected charges with abbreviated merchant names and a warning banner
Masked wallet charges: Apple Pay/Google Pay charges with explanatory notes about what they might be
Cancel unavailable: Adobe and unclear merchants show "direct cancel not available" with manual follow-up logging
Downgrade unavailable: Shows inline explanation when plan switching isn't possible through SubShield
A demo switcher at the bottom of the hub lets you toggle between edge cases

## Prompt 2 — Behavior

```
Remove all demo mode toggles, testing switches, scenario selectors, and fake control panels from the prototype.

Important:

Do not redesign the whole app

Keep the current visual design system and overall structure

Remove anything that feels like a prototype control layer or internal demo tooling

This should feel like a real user-facing product, not a sandbox

What I want instead:

Build clear, consistent behavior paths for each user flow.

Requirements:

Each bank flow should be triggered naturally by the bank the user selects

Do not expose “demo mode” or manual state toggles to the user

Each path should behave like a real product journey with logical transitions

Keep the flow deterministic and believable

Create clean user-facing paths for:

Successful connect flow

Failed SCA flow

Bank timeout / unavailable flow

No subscriptions detected flow

Low-confidence subscriptions flow

Successful first savings flow

Cancel/downgrade unavailable flow

Behavior rules:

The selected bank should determine which path the user enters

Errors should appear as natural states inside the flow, not as manually triggered demo options

Each path should have a clear start, transition, recovery step, and outcome

Preserve progress where appropriate

Always provide a next best action such as retry, continue later, get help, review subscriptions, or switch bank

Keep copy calm, concise, and trustworthy

Make the experience feel production-like and consistent across all screens

Goal:

Turn the prototype from a clickable demo with toggles into a realistic user flow with clear, consistent behavior paths.
```

**Result:** Removed all demo toggles and replaced them with deterministic, bank-driven behavior paths:

Revolut → smooth connect → no subscriptions detected
UBS → smooth connect → low-confidence/fuzzy merchant names
Barclays → smooth connect → normal subscriptions with savings
Crédit Agricole → consent expired error on first attempt → retry succeeds → masked wallet charges
ING → bank unavailable error on first attempt → retry succeeds → normal subscriptions
Every path now feels like a real product journey with natural error states, clear recovery actions, and logical transitions — no toggles or switchers visible to the user.

## Prompt 3 — Refine

```
Refine only the first screen of the current SubShield prototype to improve trust before bank connection.

Do not redesign the flow.

Do not change the rest of the prototype.

Keep the current premium mobile layout, burgundy branding, CTA placement, and overall structure.

Goal:

Reduce hesitation before tapping “Connect your bank” by adding stronger credibility, familiarity, and reassurance signals without making the screen look like a marketing landing page.

Keep these existing elements:

SubShield logo and brand at the top

main headline

3-bullet value structure

“Celebrate savings” bullet

testimonial block

main CTA

bottom reassurance row

bottom navigation

Make these exact improvements:

Headline area
keep the current headline structure, but add one short trust/social-proof line near the top section

place it directly below the headline or subtitle

this line should communicate one or two of these:

trusted usage

average savings

familiarity with known providers

keep it to one compact line, not a paragraph

Subtitle / trust language
replace generic security wording with more credible fintech wording

include PSD2 / Open Banking language

make it clear access is read-only and revocable

tone should be calm and factual, not hype

Bullet list
keep 3 bullets total

keep the “Celebrate savings” bullet

keep the first bullet about detecting recurring charges

soften the second bullet if it sounds too strong; prefer guided-action language over unrealistic instant-action language

maintain the detect → act → celebrate story

Testimonial block
revise the testimonial so it supports both trust and value

it should sound like a real user who was initially hesitant but felt reassured and then saw savings

keep the testimonial short and believable

do not make it sound like ad copy

Familiarity / provider trust
add a subtle trust cue showing support for familiar providers such as Revolut, UBS, Barclays, ING, N26, and PayPal

do this in a lightweight way, such as a small text row or compact chip row

do not make it visually heavy

CTA area
keep the CTA as “Connect your bank”

strengthen the reassurance around the CTA with clearer trust language

keep the reassurance concise and readable

Footer reassurance row
improve the current trust row so it reads more credibly

include concepts like:

read-only

PSD2/Open Banking

encrypted

revoke anytime

keep it short and scannable

Content rules:

do not remove the emotional savings payoff

do not remove the “Celebrate savings” concept

do not overload the screen with badges, shields, ratings, or long paragraphs

do not use fake awards or fake app-store style proof

avoid exaggerated claims

keep everything specific, believable, and premium

Design rules:

preserve whitespace and current visual hierarchy

keep the screen calm, clean, and trustworthy

this should feel like a real fintech product screen, not a pitch deck or landing page

Output:

Return the improved first screen with stronger trust signals and more credible copy, while keeping the rest of the prototype unchanged. Use realistic prototype copy. If a numeric trust claim like “10,000+ users” is not supported, replace it with a softer but credible line such as “Trusted by thousands of subscription-conscious users” or “Used across major European banks and payment providers.”
```

**Result:** All six trust refinements applied to the ConsentScreen — credible fintech language, social proof, softened bullets, revised testimonial, provider familiarity row, and updated CTA reassurance.
