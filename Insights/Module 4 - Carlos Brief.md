# Module 4: The Pitch to Carlos

**TL;DR:** M4 is the moment the prototype stops being the PM's and starts being the team's. Your prototype writes its own spec.

---

## The Progression (Why Each Module Feels Like a Step Change)

| | M1 | M2 | M3 | M4 |
|---|---|---|---|---|
| **What students build** | A single page from a vague prompt | A data-driven page with real quotes, metrics, design reference, and hypothesis | A multi-screen interactive product with states, expanded via documented 3-prompt chain | A graduated product: Living PRD, refactored code, engineering handoff — all extracted from what they built |
| **The wow** | "I just made an app" | "My prototype has real data and tests something" | "My M2 build is now a complete product — and my partner reproduced it from my prompts" | "My prototype wrote its own spec — and my partner understood the product without ever seeing it" |
| **Build method** | One prompt, see what happens | Assemble context in prompt builder, paste into Lovable | 3-prompt chain: expand, states, refine | 3-prompt graduation chain: extract PRD, refactor code, generate handoff |
| **VP reaction** | "Cool demo" | "What did you learn?" | "Wait, when did engineering build this?" | "Send me the spec and the code" |

---

## The M4 WOW Moment

**"Your prototype writes its own spec."**

In M1, students built a demo. In M2, they added substance. In M3, they directed the AI with precision. In M4, they do something PMs have never been able to do: **extract a complete product spec from a working prototype in 5 minutes.**

Traditional PM workflow: Research → Spec → Build → Test. Two weeks on a PRD describing something that doesn't exist yet.

Vibe Coding workflow: Build → Test → Extract spec. The spec isn't imagined. It's grounded in what actually works.

That's the paradigm shift. The spec is the output, not the starting point.

**The wow has two beats:**
- **Beat 1 (after extraction):** A complete Living PRD appears — product overview, user flows, hypothesis, metrics, what's real vs. mocked, next steps for engineering. Students didn't write it. The AI extracted it from their working prototype. "I would have spent 2 weeks on this. It took 5 minutes — and it's based on something that actually works."
- **Beat 2 (after refactoring):** Students switch to code view. `Component1` is now `OnboardingWelcome`. Data logic has its own folder. There's a README. Same product — now an engineer can read it on day one. The before/after in the code view is the visual payoff.

**The partner test (the clincher):** Partner reads ONLY the Living PRD — not the prototype. Can they describe the product, the user, the hypothesis, what's mocked, and what engineering should build first? When the partner nails all 5 from just the spec, the student realizes: the prototype can survive without them. That's graduation.

**The four-tab reveal:** M1 on the left. M2 next. M3 next. M4 on the right. One prompt, one page → real data and hypothesis → 5 screens with states → clean code, a spec, and an engineering handoff. Same tool. Same student. Four modules of progression.

---

## Concrete Example: The Instructor Demo (Retention Engine)

The instructor's M3 prototype: 5-screen Retention Engine with onboarding flow, team workspace, PM dashboard, loading states, error handling, interactive charts. Design-matched to Asana. Built with a documented 3-prompt chain.

The instructor switches to code view. It's a mess: `Component1`, `handleClick2`, data logic scattered everywhere, no README.

3 prompts:

- **Prompt 1 — Extract:** "Look at this prototype. Write a product requirements document: what it does, who it's for, the problem it solves, the 5 screens and their purpose, the user flow, the hypothesis, the key metrics, what's mocked vs. real, and next steps for engineering."
  - **Result:** A structured Living PRD appears. Product overview, user flows, hypothesis (surface team invites → increase Day-3 invite rate from 12% to 25%), metrics, technical reality (data is mocked, invite API exists), recommended engineering path.

- **Prompt 2 — Refactor:** "Rename all components to be descriptive. Separate data logic from display. Group files by feature. Add a README."
  - **Result:** `Component1` → `OnboardingWelcome`. `Section3` → `PMDashboard`. Data logic in `/services`. README explains the project. Before/after in code view is dramatic.

- **Prompt 3 — Handoff:** "Generate an engineering handoff: component list with purposes, data model, top 3 technical decisions, and a 'start here' guide."
  - **Result:** A handoff document an engineer could actually use. Identifies that the invite API exists but the analytics are mocked, recommends starting with real data integration, flags the nudge email feature as needing backend support.

**The reveal:** "3 prompts. I have a spec, structured code, and an engineering handoff. That used to be 2 weeks of PM work and a sprint of tech debt cleanup. I did it in 10 minutes. You'll do it in 30."

---

## Concrete Example: Student Lab (Marketplace Trust)

A student's M3 marketplace trust prototype: 5 screens (provider listing, enhanced profile, booking confirmation, review prompt, provider dashboard). Loading states, error handling, trust badges. Documented prompt chain from M3.

In M4:

- **Extract:** PRD captures: two-sided marketplace solving cold-start trust problem. Hypothesis: enriched profiles + satisfaction guarantee increase browse-to-book from 6% to 15%. 5 screens with flows. Mocked: review data, booking API, guarantee system. Real: user research quotes, market metrics.

- **Refactor:** Generic component names → `ProviderSearchResults`, `TrustBadgeGroup`, `BookingConfirmation`. Provider-related logic grouped in `/provider`. Customer flow in `/booking`. README explains the trust system architecture.

- **Handoff:** Engineering handoff identifies that the guarantee system needs a new backend service, review data needs a content moderation layer, and recommends starting with the provider profile enrichment (lowest engineering effort, highest impact based on the 71% bounce rate).

**Partner test:** Partner reads only the PRD. Can they explain: what it does (marketplace trust system), who it's for (customers who won't book unreviewed providers), the hypothesis (trust signals increase conversion), what's mocked (booking API, reviews), and what to build first (provider profile enrichment). If yes — it's handoff-ready.

---

## What Makes M4 Different (Not Just "Better Documentation")

**M2 → M3 shift was about EXECUTION.** Adding screens, states, and precision turned a validation prototype into something that looks like a product.

**M3 → M4 shift is about OWNERSHIP.** Extracting the spec, cleaning the code, and generating the handoff turns a PM's personal prototype into something the team can build from.

The key insight: In M1-M3, the prototype lived in the PM's head. They could demo it, but nobody else could pick it up. M4 is the moment the prototype becomes independent of its creator. The Living PRD means anyone can understand it. The refactored code means an engineer can read it. The handoff means someone else can continue it.

**M4 also introduces "comprehension debt"** — the gap between what the prototype does and what the PM can articulate about it. After 50+ prompts across 3 modules, the prototype knows more than the PM. The Living PRD is the comprehension debt payoff.

---

## How It Addresses Carlos's Feedback

| Carlos said | M4 delivers |
|---|---|
| "Every module should come with a wow moment" | The extraction wow: a complete PRD appears from the prototype. The refactoring wow: before/after code view. The partner test: PRD stands alone. |
| "Fireworks all the time" | The wow is in the students' hands — they extract their own spec, refactor their own code, test it with a partner. Not a lecture. |
| "Export/deployment readiness — 'this could ship'" (M4 gap from Carlos session) | Living PRD + refactored code + engineering handoff = a PM who can hand this to engineering and say "build from this." |
| "Each module should be significantly better than the previous" | M3: looks like a product. M4: has a spec, clean code, and a handoff. The gap is "prototype" vs. "shippable brief." |
| "Advanced, not basic" | Comprehension debt, graduation judgment, extracted specs — these are senior PM concepts, not beginner material. |

---

## Module Flow (20 slides, ~100 min)

1. **Opening (5 min)** — "Your M3 prototype looks real. Could engineering build from it?" Show the polished UI, then the messy code.
2. **Instructor Demo (10 min)** — 3 prompts: extract PRD, refactor code, generate handoff. The AI writes the spec. The code transforms.
3. **Mini Activity (5 min)** — Students open their own code view. "Could an engineer understand this?" Surfaces the gap.
4. **Teaching (12 min)** — Graduation judgment, comprehension debt, Living PRD structure, refactoring for PMs. Light and fast.
5. **Hands-On Lab (30 min)** — THE FIREWORKS. Extract the Living PRD (10 min). Refactor + generate handoff (20 min). Use the Living PRD Extractor tool.
6. **Peer Review (10 min)** — Partner reads only the PRD. Can they describe the product? The handoff test.
7. **Break It (10 min)** — The prototype that never graduated: 500+ prompts, no spec, unmaintainable. Horror story.
8. **Wrap (8 min)** — Four-tab reveal (M1/M2/M3/M4), three takeaways, accountability, M5 preview.

**Hands-on ratio:** ~55% (lab + review + mini activity + break it)

---

## One Sentence

M4 is the moment the prototype stops being the PM's and starts being the team's — and they prove it when their partner understands the product from just the extracted spec.
