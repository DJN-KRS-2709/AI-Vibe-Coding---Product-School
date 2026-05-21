# Module 2 — Frameworks Reference Card

> Every framework from Module 2 in the order you use them. Keep this open while you build.

---

## 1. The Validation Lens Loop

Four moves. Each revolution sharpens your hypothesis and tightens constraints — moving your product from uncertain to evidence-backed.

| Step | Move | What it does |
|---|---|---|
| ① **Identify the Hypothesis** | Name the test. If you can't complete *"I'm testing whether [X]"*, you aren't ready to build. | The "why" that governs every prompt. |
| ② **Define the Constraints** | Set the guardrails — intent, logic, interaction patterns. Inject Data + User Voice as context. | Guardrails for the build. |
| ③ **Build and Stress-Test** | Don't build to look pretty. Build to find where it **breaks**. Finding a break = highest signal. | Find logic and friction gaps now. |
| ④ **Synthesize and Pivot** | Update your hypothesis with what you learned, then continue or pivot. Iterate strategy, not pixels. | Close the loop with learning. |

**Rule:** building in a straight line is M1. Vibe Coding requires a circle.

---

## 2. The Kill Switch + Risk Type Matrix

Ask: *"Which assumption, if wrong, kills the whole thing?"* Then match the build to the risk.

| Risk Type | Question | Build This | Why |
|---|---|---|---|
| **Value** | "Will anyone actually want this?" | Landing page | Tests whether the core premise solves a real problem or is just a novelty. |
| **Usability** | "Will the experience make sense?" | Clickable mockup | Simplifies complex steps and surfaces where the flow breaks down. |
| **Feasibility** | "Will the logic actually work?" | Functional app | Finds edge cases where your logic or data might fail. |

### Kill switch by product stage

| Stage | Default kill switch |
|---|---|
| **0 → 1 (New product)** | **Desirability.** Nobody wants it yet, so prove they will. You're testing whether the problem is real before you invest in building. |
| **1 → N (Existing product)** | **Adoption + flow.** People have the surface area, now prove they'll use it. Screenshot what exists and build on top. |

---

## 3. The Problem Framework — Six-Part Checklist

This six-element framework forces you to articulate **what you're testing**, not just what you're shipping. Fill this out *before* you open any tool — every element sharpens your intent.

| # | Element | The question | What it gives you |
|---|---|---|---|
| 1 | **Goal** | What are we trying to achieve? | The outcome, not the output. |
| 2 | **Problem** | What's blocking us right now? | Names the obstacle precisely. |
| 3 | **Context** | Who, where, when? | The specifics that shape the solution space. |
| 4 | **Constraints** | What can't we change? | Technical limits, timelines, budgets. |
| 5 | **Success Criteria** | What does validation look like? | The pass/fail threshold, upfront. |
| 6 | **Explore** | What are we trying to learn by building this? | The key. This is the learning intent. |

**Prototyping doesn't replace the PM responsibility of identifying the problem; it makes validation faster.**

---

## 4. The Three Ingredients of Context Injection

Design systems and components provide the shell. **Context Injection provides the soul.** Without these three, you're generating high-fidelity Lorem Ipsum.

| # | Ingredient | What it is | Example |
|---|---|---|---|
| 1 | **Hypothesis** | The strategic anchor. Defines the core strategic goal of your build in the opening prompt. | *"I am testing whether a guided walkthrough reduces user friction during initial onboarding."* |
| 2 | **Real Data** | Domain-specific evidence. Replaces generic placeholders with information that stress-tests the logic. | *"Use this CSV of 50 anonymized user logs to populate the retention risk dashboard."* |
| 3 | **User Voice** | Persona terminology. Injects specific tone so the prototype resonates with the target audience. | *"Use the direct, analytical tone of a Customer Success VP — focus on 'NRR' and 'Health Scores'."* |

---

## 5. The Four Final-Project Scenarios

This is your commitment moment. Pick the scenario you'll carry through M2–M6. **No switching after Module 2.**

| # | Scenario | Setup | Likely risk |
|---|---|---|---|
| 1 | **The Retention Engine** | B2B SaaS losing 30% of users in 90 days. Why are they leaving? Build a prototype that helps you understand churn drivers and test whether an intervention can change the curve. | Value |
| 2 | **The Internal Tool Nobody Uses** | CRM with 18% adoption. Built it, no one came. Figure out why adoption is so low and prototype a version that actually fits into how people work. Classic 1→N problem. | Usability |
| 3 | **The Marketplace Trust Problem** | Bookings flat, zero-review providers. Buyers don't trust new providers. Prototype a trust mechanism that gets first-time providers their first booking. | Value / Feasibility |
| 4 | **The Dashboard Nobody Reads** | Analytics with 60% bounce rate. Data exists but nobody finds insights. Prototype a version that surfaces the right information so people use it to make decisions. | Usability |

**Bring your own:** use a real problem from your own company. Check with your instructor for approval.

---

## 6. The Validation Brief — what goes in it

Every M2 build starts with one of these. The brief is the strategic instrument; the build is the test.

**Part 1 · Strategic Intent**
- **Hypothesis** — *"I am testing whether [X] leads to [Y]."*
- **Risk Type** — Value · Usability · Feasibility
- **Kill Switch** — the single assumption that ends the project if wrong

**Part 2 · The Problem Framework** — the six-part checklist above.

**Part 3 · Context Injection** — paste from your Context Data Pack:
- Scenario brief
- User & stakeholder feedback quotes
- Quantitative metrics

**Part 4 · Visual Reference** — Mobbin screenshot OR your M1 prototype screenshot. Search for the *pattern*, not the *product*.

---

## 7. The Review Stack — Show and Swap (one round in M2)

Every lab in this course ends with a paired review. M2 has one round, after the build.

1. **Time-box** — `⏰ 10 min`.
2. **Swap links · open in a fresh tab** — no verbal context.
3. **3 minutes silent** on your partner's build. Let them stay stuck if you're the watcher.
4. **Discuss three questions · then swap roles** for the other 6 minutes.
5. **Async share** — post M1 vs M2 screenshots + the feedback that landed hardest in `#cohort-channel`.

### The three credibility questions (verbatim from the legacy walkthrough)

1. What do you think the core **hypothesis or kill switch** was?
2. Where did the experience **lose credibility**?
3. Did the data make you feel like you were using a **real product**?

**Builds are individual, reviews are paired.** Solo fallback if no partner: the AI-review prompt with the three credibility questions as the dimensions.

---

## 8. The Pre-Lovable Discipline

The most expensive credit you'll burn is the one spent finding the prompt. The cheapest is the one spent committing it.

| Move | Where it happens | Why |
|---|---|---|
| Frame the Validation Brief | Validation Brief template (Module 2) | Locks the test before the tool is open. |
| Gather context | Context Data Pack | Real quotes + metrics replace placeholder hallucinations. |
| Assemble the mega-prompt | Structured Prompt Builder | Granular control prevents AI drift. |
| Smoke-test the prompt | ChatGPT / Gemini / Claude | Find logic holes *before* burning Lovable credits. |
| **Commit the prompt** | **Lovable** | One shot. Targeted edits, not full rebuilds. |

**Rule:** 60% of your prompt work happens outside the tool. The tool is for committing the plan, not finding it.
