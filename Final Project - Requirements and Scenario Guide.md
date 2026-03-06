# Final Project: Requirements & Scenario Guide

---

# ONE-PAGER: Final Project at a Glance

*This page is the complete summary. Everything below it is the detailed reference.*

## What It Is

One product, built individually across six modules, deployed to a live URL on the final day. No group dependencies. Your team is your AI agents.

## Two Tracks

| Track | Who It's For |
| --- | --- |
| **Your Company Problem** | You have a real product challenge at work. You leave with something you can show your VP on Monday. |
| **Course Scenario** | You want a clean sandbox. Pick from 4 provided scenarios designed to carry M1–M6. |

Students choose their track by end of M1. From M2 onward, every module builds on the same product.

## Five Deliverables

| # | Deliverable | What It Is | Starts In |
| --- | --- | --- | --- |
| 1 | **Deployed Product** | Live URL. Real integrations. Handles edge cases. Not localhost. | M1 → M6 |
| 2 | **Validation Evidence Brief** | 1 page: what you assumed, what you tested, what you learned, ship/pivot/kill. | M2 → M6 |
| 3 | **Living PRD** | Product spec extracted FROM building, not written before. Evolves with the product. | M4 → M6 |
| 4 | **Prompt Library** | Reusable prompt templates, context blocks, and constraint patterns. Portable to your next initiative. | M3 → M6 |
| 5 | **Engineering Handoff Note** | What's real, what's hacked, what engineering needs to build it for production. | M5 → M6 |

## How It Builds (One Layer Per Module)

| Module | What Happens to Your Product |
| --- | --- |
| **M1** | Explore. Build 2–3 directions fast. Nothing is permanent. |
| **M2** | Commit. Pick your scenario. Name the riskiest assumption. Build to test it. |
| **M3** | Precision. Same product, better execution. Design system. Documented prompt chain. |
| **M4** | Graduate. Extract the living PRD. Refactor the code. Stop exploring, start structuring. |
| **M5** | Harden. Real database, auth, APIs. Edge cases. Write the engineering handoff note. |
| **M6** | Ship. Deploy to live URL. Gallery walk. Optional 5-minute pitch with live demo. |

## The Presentation (M6)

**Optional but encouraged.** 5 minutes, strictly timed:

| 45 sec | The Problem — what ambiguity you started with |
| --- | --- |
| 30 sec | The Assumption — what you set out to test |
| 60 sec | The Journey — what you learned, key pivots, evidence |
| 90 sec | Live Demo — click through the deployed product |
| 30 sec | The Recommendation — ship, pivot, or kill (with evidence) |
| 30 sec | Break It — audience tries to break your live product |

**Everyone deploys.** Presenting is your choice. Those who don't present still participate in the gallery walk.

## Four Course Scenarios

| Scenario | The Problem | Product Type |
| --- | --- | --- |
| **1. The Retention Engine** | B2B SaaS losing 30% of customers in 90 days. Onboarding? Feature discovery? Team invitation? | 0-to-1 |
| **2. The Internal Tool Nobody Uses** | CRM with 18% adoption. Too many clicks? Wrong motivation? AI fix? | 0-to-1 |
| **3. The Marketplace Trust Problem** | Bookings flat despite signups. Zero-review providers. Trust badges? Guarantees? | 0-to-1 |
| **4. The Dashboard Nobody Reads** | Analytics dashboard, 60% bounce rate. Info overload? Navigation? Irrelevant metrics? | Existing product |

## Key Rules

- **Individual.** No group projects. No shared dependencies. Group activities during class for networking and peer review only.
- **No homework.** Optional between-session building, never required.
- **100% deployment rate.** Everyone ships a live URL in M6. Non-negotiable.
- **Evidence over polish.** A scrappy MVP with a clear recommendation beats a beautiful product with no insight.

---
---

# DETAILED REFERENCE

*Everything below expands on the one-pager above.*

---

## Why This Document Exists

Carlos flagged it: "That was never clear in the first session. And people came back with a lot of questions." The final project is the throughline of the entire course. Every lab, every exercise, every module contributes a piece. If students don't know where they're heading from Day 1, every module feels disconnected. This document defines exactly what students deliver, how they build it across modules, and what they present.

---

## The Final Project in One Paragraph

Every student builds **one product** across all six modules. They start in ambiguity (M1), add validation rigor (M2), precision-prompt it into shape (M3), graduate it from exploration to structure (M4), harden it with real integrations (M5), and deploy it to a live URL (M6). On the final day, they present a 5-minute pitch backed by evidence: what they started with, what they tested, what they learned, and what they recommend. The final project is individual — no group dependencies, no shared builds. Your team is your AI agents.

---

## Two Tracks: Your Company or a Course Scenario

Students choose **one track** by the end of Module 1 and carry it through M2–M6:

### Track A: Your Real Company Problem

Use the product challenge you posted in your Slack intro during pre-work. Build a feature, improvement, or new direction for your actual product at work. Feed in screenshots of your real product. Make the prototype look like it belongs. This is the power track — you leave the course with something you can show your VP on Monday.

**Best for:** Students who have a clear product problem at their company and want to leave with a directly applicable artifact.

**What you need:** A screenshot or Figma export of your current product. A real problem or initiative you're wrestling with. Willingness to share (you can anonymize company details if needed).

### Track B: Course Scenario

Pick one of the provided scenarios below. Each scenario is designed to carry through all 6 modules — it's messy enough for M1 exploration, has testable assumptions for M2, needs precision for M3, has a structure moment in M4, requires real integrations in M5, and is deployable in M6.

**Best for:** Students who want a clean sandbox, don't have a current product problem, or can't share company-specific work.

---

## The Five Deliverables

Students build these **incrementally across modules** — not as a last-minute sprint. By M6, everything exists because they've been building it all along.

### 1. Deployed Product (Live URL)

**What it is:** A working product deployed to a live, shareable URL. Not localhost. Not a screenshot. A real URL that anyone on the internet can visit, click through, and use.

**What "working" means:**
- At least one real integration (database, auth, or external API)
- Handles at least 2 edge cases gracefully (doesn't crash on bad input or empty states)
- Looks like a product, not a prototype — design system applied, consistent UI, professional feel

**When it builds:**
- M1: First raw prototype (exploratory, disposable)
- M2: Prototype rebuilt with validation intent
- M3: Refined with precision prompting and design system
- M4: Restructured and refactored for clarity
- M5: Real integrations added (database, auth, APIs)
- M6: Polished, deployed, live

**This is not optional.** 100% deployment rate is the success metric for M6.

---

### 2. Validation Evidence Brief (1 page)

**What it is:** A single-page document that answers: What did I learn by building this? This is what a PM hands to their VP on Monday morning. Not "look what I built" — "here's what we now know."

**Structure:**

| Section | What to Write |
| --- | --- |
| **Starting Assumption** | The riskiest assumption you identified in M2. One sentence. |
| **What I Built to Test It** | The prototype direction and fidelity level. Why this approach? |
| **What I Learned** | Evidence from peer testing, feedback sessions, and your own iteration. What was validated? What was invalidated? What surprised you? |
| **Recommendation** | Ship, pivot, or kill — with reasoning tied to evidence. Not opinion. Evidence. |
| **Confidence Level** | Where is this initiative on the Confidence Line now? What would move it further right? |

**When it builds:**
- M2: The assumption is named. The "what I'm testing" is framed.
- M3–M4: Evidence accumulates through peer feedback and iteration.
- M5: Real-world complexity either strengthens or weakens the case.
- M6: Finalized and presented.

---

### 3. Living PRD

**What it is:** A product spec extracted FROM building, not written before building. It captures what you've learned, what the product does, who it's for, and what's recommended going forward. It's "living" because it evolved across modules — it's not a static template filled out once.

**Structure:**

| Section | What to Write |
| --- | --- |
| **Product Overview** | What does this do? Who is it for? What problem does it solve? |
| **Validated Assumptions** | What did building prove or disprove? |
| **Architecture** | Component structure, data flow, key technical decisions (extracted from M4 refactor) |
| **Current State** | What works, what's mocked, what's hacked |
| **Recommended Next Steps** | What would engineering need to build this for real? |

**When it builds:**
- M4: Extracted from the working prototype. First draft.
- M5: Updated with integration details and technical reality.
- M6: Finalized. Attached to the deployed product.

**Key principle:** If the Living PRD doesn't reference what you learned from building — if it reads like it was written before you touched a tool — it's not living.

---

### 4. Prompt Library / Living Prompt Pack

**What it is:** A reusable collection of prompt templates, context blocks, and constraint patterns that encode your product context. This is the toolkit you take back to your company and use on your next initiative.

**What goes in:**

| Category | Examples |
| --- | --- |
| **Product context block** | The 2–3 sentence product description you paste at the start of every prompt |
| **Design system reference** | Screenshots, color tokens, component descriptions that make AI output look like your product |
| **Exploration prompts** | Open, divergent prompts for early-stage ideation |
| **Execution prompts** | Precise, constrained prompts for building specific features |
| **Constraint templates** | "Always do X. Never do Y." patterns that prevent common AI drift |
| **Debug patterns** | Prompts that helped you diagnose and fix AI output issues |

**When it builds:**
- M3: First prompt chain documented. Context layering and constraint patterns captured.
- M4: Refactoring prompts added.
- M5: Integration-specific prompts added (API calls, auth, edge case handling).
- M6: Finalized and portable.

**The test:** Could another PM at your company pick up your prompt pack and produce a similar result without you in the room?

---

### 5. Engineering Handoff Note

**What it is:** A short document that tells an engineer exactly what they're looking at: what's real, what's hacked, what needs production work, and where to start. This bridges the gap between "PM prototype" and "engineering ticket."

**Structure:** See `Templates/Engineering Handoff Note.md` for the full template. Key sections:
- The Core Intent (what this prototype proved)
- Implementation Status: Real vs. "Vibed" (honest assessment)
- Known Hacks and Technical Debt
- Integration Requirements (especially for existing product track)
- Success Criteria for Production
- Suggested Architecture

**When it builds:**
- M5: First draft written as part of the Integration Sprint.
- M6: Finalized alongside the deployed product.

---

## Module-by-Module Build Map

This is the critical view. Students need to see how each module contributes a piece to the final project — nothing is wasted, nothing comes out of nowhere.

```
MODULE    PRODUCT              EVIDENCE BRIEF    LIVING PRD       PROMPT PACK         HANDOFF NOTE
──────    ──────────────────   ──────────────    ─────────────    ────────────────    ──────────────
M1        Raw prototype        —                 —                —                   —
          (explore, diverge)

M2        Rebuilt with          Assumption        —                —                   —
          validation intent     named. "What
                                I'm testing"
                                framed.

M3        Precision-built.      Evidence from     —                First prompt         —
          Design system         peer review       				  chain documented.
          applied.              begins.                            Context blocks
                                                                   captured.

M4        Refactored.           Evidence          First draft      Refactoring          —
          Structured.           accumulates.      extracted from   prompts added.
          Code cleaned up.                        working
                                                  prototype.

M5        Real integrations.    Real-world        Updated with     Integration          First draft.
          Edge cases handled.   evidence          technical        prompts added.       Real vs. vibed.
          Production-ready.     strengthens or    details.                              Known hacks.
                                weakens case.

M6        DEPLOYED.             FINALIZED.        FINALIZED.       FINALIZED.           FINALIZED.
          Live URL.             Presented.        Attached to      Portable.            Ready for eng.
                                                  product.
```

**The implication for students:** You're not building 5 separate deliverables. You're building one product and documenting your journey. If you engage with each module's lab, the deliverables assemble themselves.

**The implication for instructors:** Reference the final project in every module. "The prototype you're building right now? This becomes your final project. The assumption you just named? That's the first line of your Evidence Brief. The prompt chain you're documenting? That's your prompt pack."

---

## The Final Presentation (Module 6)

### Format: 5-Minute Structured Pitch

Every student can present. It's optional but strongly encouraged — those who present get direct instructor feedback and class feedback. Those who don't still deploy and participate in the gallery walk.

### Pitch Structure

| Section | Time | What to Cover |
| --- | --- | --- |
| **The Problem** | 45 sec | What ambiguity you started with. The messy, real-world problem. Set the context. |
| **The Assumption** | 30 sec | The riskiest assumption you identified. What you set out to test. |
| **The Validation Journey** | 60 sec | What you learned by building. Key pivots, surprises, and evidence from peer testing. The story of moving right on the Confidence Line. |
| **Live Demo** | 90 sec | Walk through your deployed product. Show the real URL. Click through. Show the integration working. Show an edge case handled. |
| **The Recommendation** | 30 sec | Ship, pivot, or kill. With evidence. Not opinion. |
| **Q&A / "Break It"** | 30 sec | Audience tries to break your live product. You handle it gracefully (or learn what breaks). |

**Total: 5 minutes.** Enforced with a visible timer. When the timer goes, you stop.

### Gallery Walk (All Students)

Before the volunteer presentations, every deployed URL is shared in Slack. Students visit each other's products for 15 minutes:
- Leave feedback as Slack thread replies
- React to products that impress you
- Try to break things (and report what breaks)

This creates the FOMO + community effect Carlos described: "Oh wow, look what they built."

### What the Instructor Evaluates

The instructor provides verbal feedback during presentations, focused on:
1. **Evidence quality:** Did the prototype actually test the stated assumption?
2. **Recommendation clarity:** Is the ship/pivot/kill recommendation backed by evidence?
3. **Product quality:** Does the deployed product handle real-world scenarios?
4. **Narrative arc:** Did the student tell a compelling story of moving from ambiguity to confidence?

---

## Assessment Rubrics

All deliverables are individual.

### Validation Evidence Brief

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Assumption clarity** | Specific, testable assumption clearly stated in one sentence | Assumption stated but vague or untestable | No clear assumption identified |
| **Evidence quality** | Prototype directly tested the assumption. Clear data from peer testing and iteration. | Prototype loosely related to assumption. Some evidence gathered. | Prototype didn't test the stated assumption. No evidence. |
| **Recommendation** | Clear ship/pivot/kill backed by specific evidence | Recommendation given but reasoning is weak or generic | No recommendation, or recommendation not tied to evidence |
| **Learning visible** | Brief shows genuine surprises, pivots, or invalidated assumptions | Some learning noted but surface-level | Reads like a success story with no real learning |

### Living PRD

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Extracted, not planned** | Clearly derived from what was learned through building | Mix of pre-planned and extracted content | Written before building; doesn't reflect the actual prototype |
| **Evolution visible** | Shows how the spec changed from M4 to M6 | Some evolution noted | Static document, no iteration visible |
| **Engineer-readable** | An engineer could pick this up and understand what to build next | Mostly clear with some gaps | Would need significant clarification to act on |
| **Validated assumptions referenced** | Ties back to what was proven/disproven | Some connection to validation | No connection between spec and evidence |

### Prompt Library

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Breadth** | 8+ prompts across exploration, execution, debug, and integration categories | 5–7 prompts, limited categories | Fewer than 5 prompts |
| **Portability** | Another PM could use these prompts on a different product and get useful output | Prompts work but are tightly coupled to one specific project | One-off prompts, not reusable |
| **Documentation** | Each prompt has: purpose, when to use, what context to include, expected output | Some prompts documented | No documentation beyond the prompts themselves |
| **Context blocks** | Includes reusable product context blocks and design system references | Some context included | No reusable context patterns |

### Engineering Handoff Note

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Honesty** | Clear, honest distinction between real and hacked/mocked components | Some distinction but vague on specifics | Claims everything is production-ready (it's not) |
| **Actionability** | Engineer could start working from this document tomorrow | Provides direction but missing specifics | Would require extensive discovery before engineering could act |
| **Technical awareness** | Identifies specific technical debt, edge cases, and architecture recommendations | Some technical awareness | No technical specifics |

### Deployed Product

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Live and functional** | Deployed to live URL. All core flows work. Real data. | Deployed but some features broken or mocked | Not deployed, or deployed but non-functional |
| **Integration depth** | Real database + auth or external API. Data persists. | One real integration, others mocked | No real integrations |
| **Edge case handling** | Gracefully handles invalid input, empty states, errors | Handles some edge cases | Crashes or breaks on non-happy-path usage |
| **Design quality** | Looks like a real product. Design system applied. Consistent. | Functional but rough around the edges | Generic AI output with no design refinement |

---

## The Scenario Library

These scenarios are designed to carry a student from M1 through M6. Each one is:
- **Messy enough** for M1 exploration (multiple possible directions)
- **Assumption-rich** for M2 validation (clear riskiest assumptions to name)
- **Complex enough** for M3 precision (needs design systems, multi-step prompting)
- **Ready to graduate** in M4 (has a natural "stop exploring, start structuring" moment)
- **Integration-ready** for M5 (needs real data, auth, or external services)
- **Deployable** in M6 (scoped enough to ship as a live product)

---

### Scenario 1: "The Retention Engine"

**The setup:**
> A B2B SaaS company (project management tool, 5K paying teams) is losing 30% of customers in the first 90 days. The VP of Customer Success says: "Users sign up, poke around for a week, and ghost." The Head of Product thinks it's a feature discovery problem — users don't find the features that would make them sticky. The CEO thinks it's an onboarding problem — the first-run experience is overwhelming. The data team says the highest-retention users all share one behavior: they invite a second team member within the first 3 days. Nobody agrees on the solution. Everyone wants something built yesterday.

**Why this works across all 6 modules:**

| Module | What students do with this scenario |
| --- | --- |
| M1 | Explore 2–3 divergent directions: onboarding wizard? team invitation flow? feature discovery dashboard? Build fast, test with a partner. |
| M2 | Name the assumption. The data suggests "invite a teammate" is the key behavior. But is the problem that users don't know they can invite? Or that the invite flow is buried? Or that solo users don't see the value of collaboration? Frame it. Pick the riskiest assumption. Build to test it. |
| M3 | Precision-build the winning direction. Clone a real PM tool's design (Linear, Asana, Monday.com via Mobbin). Apply design system. Document the prompt chain. |
| M4 | Graduate. Write the living PRD. Is this a standalone onboarding product or a feature addition? Refactor the prototype into clean components. |
| M5 | Add real integrations: Supabase for user data, auth for team accounts, an email/notification trigger when a teammate is invited. Handle edge cases: what if the invited person already has an account? What if they ignore the invite? |
| M6 | Deploy. Present the evidence: "We validated that the invite flow is the lever. Here's the live product. Here's what engineering needs to build it for real. Our recommendation: ship the simplified invite flow; kill the feature discovery dashboard idea." |

**Provided assets (instructor prepares):**
- Mobbin screenshots of 2–3 PM tool dashboards (Linear, Asana, Monday.com)
- **M2 Context Data Pack** (distributed in Module 2):
  - `feedback.md` — 12 user/stakeholder quotes (exit surveys, support tickets, executive perspectives)
  - `metrics.csv` — 15 data points (retention rates, invite rates, feature discovery, NPS by segment)
  - `scenario-brief.md` — full problem brief with competing hypotheses and constraints

---

### Scenario 2: "The Internal Tool Nobody Uses"

**The setup:**
> Your company's 200-person sales team has an internal CRM note-taking tool that was built last year. Adoption is 18%. Sales reps say it's "too many clicks" and keep using Google Docs or just not documenting calls at all. The VP of Sales wants "some kind of AI thing" to fix this. Engineering says the tool is "fine" and the problem is training. Product thinks it's a UX problem. Meanwhile, the company is losing institutional knowledge every time a rep leaves — their call notes go with them. The CEO casually mentioned "maybe we should just buy Gong" in last week's all-hands, and now everyone is panicking.

**Why this works across all 6 modules:**

| Module | What students do with this scenario |
| --- | --- |
| M1 | Explore directions: AI call summarizer? Simplified CRM input (voice-to-notes)? Slack bot that captures notes from conversation? Chrome extension that auto-fills CRM? Build 2 directions fast. |
| M2 | Name the assumption. Is the problem input friction (too many clicks)? Or is it motivation (reps don't see value in documenting)? Or is it timing (they forget by the time they're at their desk)? The riskiest assumption might be: "Reps will document calls if input takes < 30 seconds." Build to test. |
| M3 | Precision-build. Clone the existing CRM's look and feel (pick a screenshot of Salesforce, HubSpot, or Pipedrive from Mobbin). Add the AI layer on top. Document prompts. |
| M4 | Graduate. This is a feature addition to an existing product, not a standalone app. The living PRD references the existing CRM architecture. Refactor. |
| M5 | Real integrations: connect to a database for storing notes, add auth (the CRM needs login), mock an AI summarization API call. Edge cases: what if the call recording fails? What if the summary is wrong and the rep doesn't correct it? |
| M6 | Deploy. Present: "We tested that reducing input to < 30 seconds increases adoption. The AI summarizer + one-click approve flow validated this. Recommendation: ship as a CRM plugin. Kill the Gong purchase — this solves the problem at 10% of the cost." |

**Provided assets:**
- Mobbin screenshots of CRM interfaces (Salesforce, HubSpot, Pipedrive)
- **M2 Context Data Pack** (distributed in Module 2):
  - `feedback.md` — 12 user/stakeholder quotes (rep complaints, manager perspectives, CEO Gong comment)
  - `metrics.csv` — 14 data points (adoption rate, time-to-log, fields completed, mobile crash rate, knowledge loss cost)
  - `scenario-brief.md` — full problem brief with competing hypotheses and constraints

---

### Scenario 3: "The Marketplace Trust Problem"

**The setup:**
> A peer-to-peer services marketplace (think TaskRabbit/Fiverr for home services, 50K registered users, 8K monthly active) has a trust problem. Bookings are flat despite growing signups. Customer research shows the #1 reason people browse but don't book is: "I don't trust the providers." The product team tried adding reviews (6 months ago) — it barely moved the needle because new providers have zero reviews and nobody wants to be the first customer. The growth team wants to add ID verification. The design team wants to redesign provider profiles. The CEO wants a "guarantee" badge program. You have 6 weeks and one engineer (eventually).

**Why this works across all 6 modules:**

| Module | What students do with this scenario |
| --- | --- |
| M1 | Explore directions: enhanced provider profiles with video intros? Trust badge system? AI-generated "provider highlights" from past work? Booking guarantee landing page? Build fast. |
| M2 | Name the assumption. The data says "zero reviews = no bookings." But is the problem lack of social proof? Or is it risk aversion (what if something goes wrong)? The guarantee approach tests risk aversion. The profile redesign tests social proof. Pick one. Frame it. Build to test. |
| M3 | Precision-build. Clone the marketplace's existing look (use Mobbin for marketplace/Airbnb-style templates). Add the trust layer. Apply the design system. Document prompts. |
| M4 | Graduate. Write the living PRD for the trust feature. Is it a standalone flow or an enhancement to existing provider profiles? Refactor. |
| M5 | Real integrations: database for provider data and verification status, auth for provider/customer accounts, a mock verification API. Edge cases: what if a provider fails verification? What if a customer disputes a "guaranteed" booking? |
| M6 | Deploy. Present: "We tested that a money-back guarantee badge increases booking conversion more than enhanced profiles. Here's the live product. Recommendation: ship the guarantee program for top providers; revisit profile redesign in Q3." |

**Provided assets:**
- Mobbin screenshots of marketplace provider profiles (Airbnb, TaskRabbit, Thumbtack)
- **M2 Context Data Pack** (distributed in Module 2):
  - `feedback.md` — 12 user/stakeholder quotes (customer trust concerns, provider cold-start frustration, growth team data)
  - `metrics.csv` — 15 data points (signup-to-booking conversion, provider churn, review distribution, willingness-to-pay for verified)
  - `scenario-brief.md` — full problem brief with competing hypotheses and constraints

---

### Scenario 4: "The Dashboard Nobody Reads" (Existing Product Focus)

**The setup:**
> Your company's customer-facing analytics dashboard has a 60% bounce rate on first visit. The dashboard shows 12 different charts, 4 filter options, and a data export button. New users land, see a wall of charts, and leave within 30 seconds. Power users love it (they've learned to navigate the complexity). But the product is growing and 80% of new signups are non-technical business users who just want to know: "Is my campaign working?" The PM lead thinks it's information overload. The designer thinks it's a navigation problem. Engineering says "just add a tutorial." Customer Success is drowning in support tickets that all say the same thing: "What am I looking at?"

**Why this works across all 6 modules:**

| Module | What students do with this scenario |
| --- | --- |
| M1 | Explore: simplified one-metric view? Guided first-run wizard? Personalized dashboard based on role? AI-generated summary ("Here's what happened this week")? Build 2 directions. |
| M2 | Name the assumption. Is the problem information overload (too many charts)? Or is it lack of guidance (users don't know where to look first)? Or is it irrelevance (the charts don't show what non-technical users care about)? Frame. Build to test. |
| M3 | Precision-build. Clone the existing dashboard's design (use a Mobbin analytics dashboard or screenshot of Mixpanel/Amplitude/Looker). Build the improvement ON TOP of the existing product's look and feel. Document prompts. |
| M4 | Graduate. This is strictly an existing-product improvement. The living PRD is a feature spec: what changes, what stays the same, what existing components it touches. |
| M5 | Real integrations: Supabase for mock analytics data, auth for user roles (show different views to different user types), API call to generate AI summary. Edge cases: what if there's no data yet? What if the AI summary is misleading? |
| M6 | Deploy. Present: "We tested that a single-metric hero card with an AI summary reduces bounce rate in peer testing. Recommendation: ship the simplified first-run view for non-technical users; preserve the full dashboard for power users behind a toggle." |

**Provided assets:**
- Mobbin screenshots of analytics dashboards (Mixpanel, Amplitude, Looker)
- **M2 Context Data Pack** (distributed in Module 2):
  - `feedback.md` — 12 user/stakeholder quotes (new user overwhelm, power user satisfaction, support ticket themes, designer insight)
  - `metrics.csv` — 16 data points (bounce rate, time-to-insight by segment, filter usage, custom view discovery, NPS split)
  - `scenario-brief.md` — full problem brief with competing hypotheses and constraints

---

## How Scenarios Connect to Modules: The Continuity Rule

**The rule:** Starting in M2, students commit to their track (company problem or course scenario) and carry it through M6. They don't switch. Each module adds a layer to the same product.

**What this means for lab briefs:**

| Module | What the lab brief says |
| --- | --- |
| M1 | "Pick one of the scenarios below, or use your own problem. Build something. This is exploration — you might keep it, you might not." |
| M2 | "Commit to your track. If you're using a course scenario, pick one. If you're using your company problem, commit to it. From now on, every lab builds on this. Name the assumption. Frame the problem." |
| M3 | "Take your M2 prototype. Level it up with precision prompting. Same product, better execution." |
| M4 | "Take your M3 prototype. Graduate it. Extract the living PRD. Refactor." |
| M5 | "Take your M4 prototype. Add real integrations. Handle edge cases. Write the handoff note." |
| M6 | "Deploy what you've been building. Finalize all deliverables. Present." |

**Exception for M1:** Module 1 is deliberately exploratory. Students build from any of the provided scenarios or their own problem without committing. This lets them experience the cycle before choosing their final project direction. Some students may carry their M1 prototype forward. Others will pivot in M2. Both are fine.

---

## Final Project Requirements Slide (for M1 Deck)

*This is the content for the single slide Carlos requested. Play after ground rules in Module 1.*

### Slide Content

**YOUR FINAL PROJECT**

You will build and deploy a real product. Individually. No group dependencies.

**One product, six modules.** Each week adds a layer: exploration → validation → precision → structure → integrations → deployment.

**Five deliverables by Module 6:**
1. Deployed product (live URL — not localhost)
2. Validation Evidence Brief (what you learned, not what you built)
3. Living PRD (extracted from building, not written before)
4. Prompt library (your reusable toolkit)
5. Engineering Handoff Note (what's real, what needs work)

**Optional presentation.** 5-minute pitch on the final day. Those who present get direct instructor feedback. Everyone deploys. Presenting is your choice.

**You start today.** What you build in Module 1 might become your final project. Or you might pivot. Both are fine.

---

## Final Project Video Script (3 minutes)

*This is the script for the 3-minute video Carlos requested. Product School produces this. Play in M1 after the slide.*

---

**[0:00–0:30] The Hook**

"By the end of this course, you're going to have a live product on the internet. Not a mockup. Not a prototype on your laptop. A real URL you can text to your VP tonight and say: 'Click this. This is what I built. Here's what we should do next.' That's the final project."

**[0:30–1:00] What You're Building**

"You'll choose one product problem — either from your actual company or from one of our provided scenarios — and you'll build it across all six modules. Module 1, you explore. Module 2, you validate. Module 3, you get precise. Module 4, you structure it. Module 5, you add real integrations — databases, auth, APIs. Module 6, you deploy and present."

**[1:00–1:30] The Five Deliverables**

"You're not just building a product. You're building the evidence that drives decisions. Five things you'll walk out with:
One — a deployed product. Live URL.
Two — a Validation Evidence Brief. One page: what you tested, what you learned, what you recommend.
Three — a Living PRD. A spec that evolved alongside your product.
Four — a prompt library. Reusable templates you can apply to any future initiative.
Five — an Engineering Handoff Note. What's real, what's hacked, what engineering needs to take it forward."

**[1:30–2:15] How It Works**

"This is individual. No group projects. No shared dependencies. You build your own product, at your own pace, with AI as your team. Group activities during class are great — you'll swap prototypes, give feedback, compare notes. But the final project is yours.

On the last day, you'll deploy to a live URL. Everyone deploys — that's non-negotiable. Then we do a gallery walk where everyone visits each other's products. And if you're brave, you present. Five minutes. The problem, the journey, the demo, the recommendation. I give you direct feedback. The audience tries to break your live product. It's the best part of the course."

**[2:15–2:45] Why It Matters**

"Most PM courses hand you a certificate. You'll leave with a deployed product, a validated recommendation backed by evidence, a prompt toolkit you can reuse, and documentation that an engineer could pick up tomorrow. This isn't homework. This is the thing you show your team on Monday and say: 'I built this. Here's what I learned. Here's what we should do.'"

**[2:45–3:00] Close**

"You start today. Module 1 is exploration — you'll build something in the next hour. By Module 2, you'll commit to a direction. By Module 6, it's live. Let's go."

---

## FAQ (Address in M1 or as Needed)

**"Can I change my scenario after M2?"**
You can pivot your approach (that's the whole point of validation), but stay within the same problem space. Switching from the CRM scenario to the marketplace scenario in M4 means you lose 3 modules of accumulated work.

**"What if I'm not technical — can I still deploy?"**
Yes. That's what Lovable is for. Deployment is built into the tool. The instructor walks through it live in M6. If you got through M1, you can deploy.

**"Do I have to present?"**
Presenting is optional. Deploying is not. Everyone ships a live URL. If you don't present, your product is still part of the gallery walk and your deliverables are still evaluated.

**"What if my company won't let me use real product data?"**
Anonymize it. Change the company name, the product name, the data. Keep the problem real. Or use a course scenario — that's what they're for.

**"Is this graded?"**
The rubrics exist to give you feedback, not to fail you. The goal is that every student leaves with deliverables they're proud of. The instructor uses the rubrics to provide structured feedback during and after the course.

**"Can I work on this between sessions?"**
There's no required homework. But if you want to keep building between modules — go for it. Drop your progress in `#builds` and the cohort will cheer you on.

**"What if my prototype is terrible by M6?"**
Every prototype is different. Some students will ship polished products. Some will ship scrappy MVPs. Both are valid if you can articulate what you learned and what you'd recommend. The Evidence Brief matters more than the product's polish.
