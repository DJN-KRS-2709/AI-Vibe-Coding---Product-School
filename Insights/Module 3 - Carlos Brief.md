# Module 3: The Pitch to Carlos

**TL;DR:** M1 built a page. M2 built a page that tests something. M3 builds a product.

---

## The Progression (Why Each Module Feels Like a Step Change)

| | M1 | M2 | M3 |
|---|---|---|---|
| **What students build** | A single page from a vague prompt | A single data-driven page with real user quotes, real metrics, and a hypothesis | A multi-screen interactive product flow, design-matched, with states — from a documented 5-prompt chain |
| **The wow** | "I just made an app" | "My prototype has real user language and real data — it tests something" | "This looks like it ships tomorrow — and my partner reproduced it from just my prompt chain" |
| **Build method** | One prompt, see what happens | Assemble context in prompt builder, paste into Lovable | 5-step prompt chain — each prompt targets one aspect, documented and reproducible |
| **VP reaction** | "Cool demo" | "What did you learn?" | "Wait, when did engineering build this?" | 

---

## The M3 WOW Moment

**"In M2 you built a page. In M3 you built a product."**

Students take their M2 prototype — which has real data and a real hypothesis but is one page with generic styling — and rebuild it with a 5-step precision prompt chain. The result:

1. **Multiple connected screens** — not just a listing page, but listing → detail → booking flow → confirmation → review prompt. A complete user journey.
2. **Design-matched** — fed a Mobbin screenshot of a real product (Airbnb, Linear, Salesforce). The prototype looks like it belongs in the actual product.
3. **Interactive states** — loading skeletons, empty states, error handling. It behaves like a real product.
4. **Documented chain** — every prompt written down. Their partner follows the chain and gets a comparable result. It's portable.

**The single moment:** After executing all 5 prompts, students click through their prototype for the first time — navigating between screens, seeing their M2 data flowing through a design that matches their product, with loading states and error handlers. That's when they realize they didn't build a demo. They built a product. In 22 minutes. With 5 prompts.

**Then the triple reveal:** Three browser tabs. M1 on the left. M2 in the middle. M3 on the right. Same student. Same tool. The visual progression is undeniable.

---

## Concrete Example: The Instructor Demo (Retention Engine)

The instructor built this live in M2 — a 3-screen onboarding flow for a B2B PM SaaS:

- **3 screens** — onboarding flow surfacing team invites within the first 3 steps
- **Real data embedded** — Day-3 invite rate 12%, retention with invite 68% vs 22% without, 30% 90-day churn
- **Real user quotes** — "When I invited my co-founder on Day 2, that's when it clicked"
- **Named hypothesis** — "If we surface team invites during first-run onboarding, Day-3 invite rate increases from 12% to 25%"
- **Generic styling** — Lovable defaults, doesn't look like Linear or Asana
- **No states** — no loading, no empty, no error
- **No internal view** — no way for the PM to track whether the intervention is working

In the M3 demo, the instructor takes this same prototype and runs 3 sequential prompts live:

- **Prompt 1 — Design Match:** Attaches a Mobbin screenshot of Linear's onboarding. "Rebuild to match this design system." Result: same content, looks like Linear.
- **Prompt 2 — New Screens:** Adds a team workspace screen (post-invite) and an internal PM dashboard showing invite rate, retention, and churn trends. Now 5 connected screens — both user-facing AND the internal view for the VP.
- **Prompt 3 — States:** Adds loading skeletons, failed-invite error state, empty team workspace state. The prototype now behaves like a real product.

**Result in ~3 minutes of generation:** 5 connected screens. Matched to Linear's design. Complete user journey from onboarding through team setup. Internal PM dashboard for tracking. Loading, error, and empty states. Same data, same hypothesis — dramatically different execution.

**Then students do it to their own M2 builds with 5 prompts in 22 minutes.**

---

## Concrete Example: Student Lab (Marketplace Trust)

A student working on the marketplace trust scenario built this in M2:

- **2 screens** — provider listing + provider profile
- **Real data embedded** — "I'm not going to be the guinea pig," 71% bounce rate, 64% zero-review providers
- **Generic styling** — doesn't look like any real marketplace
- **No post-booking flow** — story ends at the profile page

In M3, the same student rebuilds with a 5-prompt chain:

- **Prompt 1:** Structure + design system match (attaches Airbnb screenshot from Mobbin)
- **Prompt 2:** Provider profile + booking flow (3 connected screens)
- **Prompt 3:** Data injection (real metrics, real quotes as testimonial cards)
- **Prompt 4:** States (loading skeletons, empty state, error handling)
- **Prompt 5:** Post-booking confirmation + review prompt (the missing feature the platform never built)

**Result:** 5-6 connected screens. Matched to Airbnb's design patterns. Complete user journey from browse to review. Loading states. Error handling. Documented chain their partner can reproduce.

---

## What Makes M3 Different (Not Just "Better Prompting")

**M1 → M2 shift was about SUBSTANCE.** Adding real data and a hypothesis turned a demo into a validation tool.

**M2 → M3 shift is about EXECUTION.** Adding design precision, multi-screen flows, interactive states, and a documented chain turns a validation page into something that looks like it ships tomorrow.

The key insight: M2's context injection was one big prompt. M3's prompt chain is like giving sprint tickets to the AI — structure first, then feature, then data, then states, then the next screen. Each prompt builds on the last. The accumulation produces something no single prompt could.

---

## How It Addresses Carlos's Feedback

| Carlos said | M3 delivers |
|---|---|
| "Every module should come with a wow moment" | The triple reveal: M1 vs M2 vs M3 side by side. Visual progression that makes jaws drop. |
| "How are you making sure the look and feel is as similar as possible to your current product?" | Design system matching via Mobbin/Figma screenshots. The prototype looks like the student's actual product. |
| "Advanced prompt chains producing polished output" (M3 column) | 5-step documented chain. Each step targets one aspect. Reproducible by a partner. |
| "Fireworks all the time" | The wow is in the students' hands — they build the product flow themselves, not watch the instructor. |
| "I'm leaving not excited" (M2 original feedback) | M3 surfaces the M2 gap ("would your VP ship this?"), then closes it dramatically in the lab. |

---

## Module Flow (20 slides, ~100 min)

1. **Opening (5 min)** — "Your M2 prototype proves something. Would your VP ship it?"
2. **Instructor Demo (10 min)** — Pulls up the M2 Retention Engine prototype. Runs 3 prompts sequentially in Lovable: design match (Linear), new screens (team workspace + PM dashboard), states (loading, error, empty). Each prompt builds on the last — students see the transformation happen step by step.
3. **Mini Activity (5 min)** — Students diagnose their own M2 prototype. "Does this look like your product? How many screens? Any loading states?" Posts in Slack. Surfaces the gap.
4. **Teaching (12 min)** — Prompting maturity curve, context layering, multi-step prompting, living prompt packs. Light and fast.
5. **Hands-On Lab (30 min)** — THE FIREWORKS. 5-step prompt chain. Each prompt adds a visible layer. Students build a multi-screen, design-matched, interactive product flow.
6. **Peer Review (12 min)** — Partner follows the prompt chain. Can they reproduce it? Portability test.
7. **Break It (10 min)** — Live prompt debugging. Diagnose a failing chain.
8. **Wrap (7 min)** — Triple reveal (M1/M2/M3 tabs), three takeaways, accountability, M4 preview.

**Hands-on ratio:** ~55% (vs. 29% in the old M3 outline)

---

## One Sentence

M3 is where students go from "I can test something" to "I can show my VP something that looks like engineering built it" — and they do it with a 5-prompt chain they document and their partner can reproduce.
