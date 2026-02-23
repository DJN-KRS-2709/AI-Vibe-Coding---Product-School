# Module 3: The Pitch to Carlos

**TL;DR:** M3 is the moment students stop prompting and start directing.

---

## The Progression (Why Each Module Feels Like a Step Change)

| | M1 | M2 | M3 |
|---|---|---|---|
| **What students build** | A single page from a vague prompt | A data-driven page with real user quotes, metrics, design reference, and a hypothesis | A multi-screen interactive product with states, expanded from their M2 build via a documented 3-prompt chain |
| **The wow** | "I just made an app" | "My prototype has real data and tests something" | "My M2 build is now a complete product — and my partner reproduced it from just my prompts" |
| **Build method** | One prompt, see what happens | Assemble context in prompt builder, paste into Lovable | 3-prompt chain — expand screens, add states, refine without rebuilding |
| **VP reaction** | "Cool demo" | "What did you learn?" | "Wait, when did engineering build this?" | 

---

## The M3 WOW Moment

**"Students stop prompting and start directing."**

In M1, they asked the AI to build something. In M2, they assembled context and pasted one big prompt. In M3, they **direct** the AI — expand here, add states there, refine this one screen, don't touch anything else. Like giving sprint tickets to an engineer.

Students take their M2 prototype and expand it with a 3-prompt chain. They don't rebuild; they grow what they have. The result:

1. **Multiple connected screens** — from 3 screens to 5+. A complete user journey with secondary views (dashboards, detail pages, admin screens).
2. **Interactive states** — loading skeletons, empty states, error handling. It behaves like a real product.
3. **Iterative refinement** — the third prompt steers one screen without rebuilding. That's the paradigm shift: steering, not restarting.
4. **Documented chain** — every prompt written down. Their partner follows the chain and gets a comparable result. It's portable.

**The wow has two beats:**
- **Beat 1 (after Prompt 2):** Loading skeletons appear. Error messages appear. The same screens they had before suddenly *behave* like software. Before: a mockup. After: a product.
- **Beat 2 (after Prompt 3):** They change ONE thing on ONE screen and nothing else breaks. That's when the instinct to "start over" dies. They're not prompting anymore — they're directing.

**The culmination:** Students click through their full 5-screen prototype for the first time. Multi-screen flow, real data, real states. 22 minutes. 3 prompts.

**Then the triple reveal:** Three browser tabs. M1 on the left. M2 in the middle. M3 on the right. Same student. Same tool. The visual progression is undeniable.

---

## Concrete Example: The Instructor Demo (Retention Engine)

The instructor built this live in M2 — a 3-screen onboarding flow for a B2B PM SaaS:

- **3 screens** — onboarding flow surfacing team invites within the first 3 steps
- **Real data embedded** — Day-3 invite rate 12%, retention with invite 68% vs 22% without, 30% 90-day churn
- **Real user quotes** — "When I invited my co-founder on Day 2, that's when it clicked"
- **Named hypothesis** — "If we surface team invites during first-run onboarding, Day-3 invite rate increases from 12% to 25%"
- **Design-matched to Asana** — already uses a screenshot reference from M2
- **No states** — no loading, no empty, no error
- **No secondary views** — no team workspace after invite, no PM dashboard to track if it's working
- **Built with one big prompt** — not reproducible

In the M3 demo, the instructor takes this same prototype and runs 3 sequential prompts live:

- **Prompt 1 — Expand:** Adds a team workspace screen (post-invite) and an internal PM dashboard showing invite rate, retention, and churn trends. Now 5 connected screens with navigation.
- **Prompt 2 — States:** Adds loading skeletons, failed-invite error state, empty team workspace state. The prototype now behaves like a real product.
- **Prompt 3 — Refine:** Makes the PM dashboard more actionable — adds a nudge button, makes the chart interactive. Doesn't touch anything else. Steering, not restarting.

**Result in ~3 minutes of generation:** 5 connected screens. Complete user journey from onboarding through team setup. Internal PM dashboard for tracking. Loading, error, and empty states. And an iteration that refined without rebuilding. Same data, same hypothesis — dramatically different execution.

**Then students do it to their own M2 builds with 3 prompts in 22 minutes.**

---

## Concrete Example: Student Lab (Marketplace Trust)

A student working on the marketplace trust scenario built this in M2:

- **2 screens** — provider listing + provider profile
- **Real data embedded** — "I'm not going to be the guinea pig," 71% bounce rate, 64% zero-review providers
- **Design reference applied** — uses an Airbnb-style layout from their M2 screenshot
- **No post-booking flow** — story ends at the profile page
- **No states** — no loading, error, or empty handling

In M3, the same student expands their M2 build with a 3-prompt chain:

- **Prompt 1 — Expand:** Adds a booking confirmation screen, a post-booking review prompt, and a provider dashboard. 5 connected screens with navigation.
- **Prompt 2 — States:** Loading skeletons for provider search, empty state for "no providers match your filters," error state for failed booking attempts. Same design language throughout.
- **Prompt 3 — Refine:** The provider profile needs a clearer trust hierarchy — move the guarantee badge above the fold, add response time. Don't change anything else.

**Result:** 5-6 connected screens. Complete user journey from browse through review. Loading states. Error handling. An iterative refinement. And a documented chain their partner can reproduce.

---

## What Makes M3 Different (Not Just "Better Prompting")

**M1 → M2 shift was about SUBSTANCE.** Adding real data and a hypothesis turned a demo into a validation tool.

**M2 → M3 shift is about EXECUTION.** Adding screens, interactive states, iterative refinement, and a documented chain turns a validation prototype into something that looks like it ships tomorrow.

The key insight: In M1 and M2, when something was wrong, the instinct was to start over with a better prompt. M3 kills that instinct. Students learn to direct — expand, add states, refine — with each prompt targeting one thing. They stop being someone who asks the AI to build things and start being someone who directs the AI like giving sprint tickets.

---

## How It Addresses Carlos's Feedback

| Carlos said | M3 delivers |
|---|---|
| "Every module should come with a wow moment" | The triple reveal: M1 vs M2 vs M3 side by side. Visual progression that makes jaws drop. |
| "How are you making sure the look and feel is as similar as possible to your current product?" | M2 already established design matching. M3 builds on it — expanding screens and adding states while preserving the design language. |
| "Advanced prompt chains producing polished output" (M3 column) | 3-step documented chain. Each step targets one aspect. Reproducible by a partner. |
| "Fireworks all the time" | The wow is in the students' hands — they build the product flow themselves, not watch the instructor. |
| "I'm leaving not excited" (M2 original feedback) | M3 surfaces the M2 gap ("would your VP ship this?"), then closes it dramatically in the lab. |

---

## Module Flow (20 slides, ~100 min)

1. **Opening (5 min)** — "Your M2 prototype proves something. Would your VP ship it?"
2. **Instructor Demo (10 min)** — Pulls up the M2 Retention Engine prototype. Runs 3 prompts sequentially in Lovable: expand (team workspace + PM dashboard), states (loading, error, empty), refine (iterate on PM dashboard without rebuilding). Each prompt builds on the last.
3. **Mini Activity (5 min)** — Students diagnose their own M2 prototype. "How many screens? Any loading states? Could someone else reproduce this?" Posts in Slack. Surfaces the gap.
4. **Teaching (12 min)** — Prompting maturity curve, anatomy of a prompt chain (Expand / Behavior / Refine), multi-step prompting, living prompt packs. Light and fast.
5. **Hands-On Lab (30 min)** — THE FIREWORKS. 3-prompt chain starting from their M2 build. Each prompt adds a visible layer. Students expand their M2 into a multi-screen interactive product.
6. **Peer Review (12 min)** — Partner follows the prompt chain. Can they reproduce it? Portability test.
7. **Break It (10 min)** — Live prompt debugging. Diagnose a failing chain.
8. **Wrap (7 min)** — Triple reveal (M1/M2/M3 tabs), three takeaways, accountability, M4 preview.

**Hands-on ratio:** ~55% (vs. 29% in the old M3 outline)

---

## One Sentence

M3 is the moment students stop prompting and start directing — and they prove it with a 3-prompt chain that expands their M2 build into something the VP thinks engineering built.
