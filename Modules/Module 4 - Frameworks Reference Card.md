# Module 4 — Frameworks Reference Card

> Every framework from Module 4 in the order you use them. Keep this open while you refactor, extract, and hand off.

---

## 1. The Production Threshold

Not every prototype should move into production. **Threshold judgement** is the most important PM skill in Vibe Coding — move too early and you harden a build that still needs to change; move too late and the AI's complexity outpaces your ability to manage it.

| ✅ Move to Production Spec when | 🚫 Stay in Prototyping mode when |
|---|---|
| Your "kill switch" hypothesis is proven with functional evidence. | Your core value proposition or user flow is still changing. |
| Stakeholders have approved the direction for a real build. | You haven't gathered feedback outside your immediate team. |
| You can explain the logic **without needing a demo**. | You can't yet define the business rules the AI is executing. |
| Your goal has shifted from discovery to durability. | Speed of iteration is still more valuable than system stability. |

**Gut check:** Could you explain what your prototype does, how the data flows, and what it's testing — *without opening Lovable*? If yes, you're ready. If you need the demo to explain your own product, keep iterating.

---

## 2. The Vibe Loop — The New Operating Model

The shift from traditional PM workflow to Vibe Coding isn't just about speed — it's about what you trade.

| Old Way · Dependency Loop | New Way · Vibe Loop |
|---|---|
| Research → Write Spec → Wait for Eng/Design → Review Build → Feedback → Wait for Update | Idea → Build Prototype → Test & Iterate → Extract Spec → Connect Infra → Live |
| Spec is your **starting point** (your best guess at requirements). | Prototype is the **source of truth** (what's already been validated). |
| You are a **requestor**, dependent on others' time. | You are an **author**, handing engineers proven logic. |
| Trade documents-as-guesses for documents-as-guesses. | Trade live links + extracted specs for live links + extracted specs. |

**Rule:** Your spec is no longer the input. It's the **output** of a functional build.

---

## 3. The Eight Building Blocks of a Living PRD

The eight specific blocks that turn a black box of AI code into a professional-grade specification.

| # | Block | What it captures |
|---|---|---|
| 1 | **🔎 Product Overview** | High-level summary of the validated system — what it does and who it's for. |
| 2 | **🎯 Problem & Hypothesis** | Clear definition of user friction and the evidence-backed intervention being tested. |
| 3 | **🗺️ User Flow & Screen Map** | Visual and descriptive map of navigation paths, screen states, and interactive logic. |
| 4 | **📈 Success Metrics** | North Star metric and leading indicators used to measure production performance. |
| 5 | **🛠️ Technical Reality** | Truth vs. Mock report — functional logic vs. mocked elements and current infra connections. |
| 6 | **⚠️ Assumptions & Risks** | Current confidence levels, kill switch triggers, and potential technical failure points. |
| 7 | **🧱 In vs. Out Scope** | Definitive list of included features, excluded items, and proposed roadmap for future phases. |
| 8 | **📋 Engineering Recommendation** | Strategic guide on build order, technical effort estimates, and open architectural questions. |

**Rule:** Document the truth — *including what's mocked*. You're not losing points for missing features. You're gaining points for documenting reality.

---

## 4. From Prompt Pack to Product Spec — Three Pillars of Extraction

You've already done most of the work. A traditional PRD is a *wish list written before a build*. A Living PRD is a *reality report extracted from a build*.

| Module | Pillar | Why this becomes a PRD section |
|---|---|---|
| **M2** | The Intent — Hypothesis & Data Packs | You injected strategic intent from day one — the AI reads the hypothesis you embedded, not a guessed one. |
| **M3** | The Architecture — Prompt Chaining | Your Expansion + Behavior chains hard-coded **states, logic, and if/then rules**. The AI translates those back into a User Flow + Screen Map. |
| **M4** | The Reality — Baseline Code | Your functional prototype is a **measurable asset**. The AI audits actual files to define exactly what's functional vs. mocked. |

---

## 5. The Three Pillars of an Engineering-Ready System

Non-negotiable standards for moving any prototype into a production environment. You don't need to be an engineer — you need the AI to set up the infrastructure.

| Pillar | Role | What "done" looks like |
|---|---|---|
| **📂 GitHub Connection** (Front Door) | Version-controlled repo with permanent history, safe rollbacks, secure front door for collaboration. | Engineer can `git clone` your repo on day one and see commit history. |
| **🧱 Code Refactoring** (Cleanup) | Structurally organised codebase, professional naming, data separated from display, generated README. | Engineer can orient within **5 minutes** of reading the README. |
| **🗄️ Supabase Connection** (Memory) | Persistent PostgreSQL database + Auth layer, managed through a visual table editor. | Real tables visible in dashboard; product remembers things across sessions. |

**Rule:** You direct, the AI executes and connects.

---

## 6. The Four-Prompt Refactor Chain — In Order

Each prompt is small. The order matters. Each subsequent prompt depends on the artifact the previous one produced.

### 1 · Extract the Living PRD

```
Extract a PRD from this prototype covering:
- what it does, who it's for, the problem it solves,
- all screens and their purpose,
- the user flow, the hypothesis, key metrics,
- and what is mocked versus real.
```

> If Lovable seems confused: *"Audit the existing files and our previous conversation to find these details."*
> Save as `04-structure/PRD.md` — push to GitHub.

### 2 · Refactor the Code

```
Refactor this codebase. Rename components: [list your screen names from PRD].
Separate data logic from display components. Group files by feature.
Add a README explaining the flow and project structure.
```

> Copy the screen names from your PRD's User Flow section.
> Verify: open `src/pages` — file names are descriptive; `README.md` exists.

### 3 · Generate the Engineering Handoff

```
Generate an engineering handoff for this prototype.
List every component and its purpose. Describe the data model.
Note what is mocked versus real.
Write a Start Here guide explaining how the project is structured
and where an engineer should begin.
```

> Save as `HANDOFF.md` — push to GitHub.

### 4 · Connect the Backend

```
Set up a Supabase backend for this project.
Create the database tables needed to support the core data in my prototype.
```

> Lovable will prompt to enable — click **Allow**. Verify in Settings: database + auth + storage live.
> *Lovable Cloud vs. Supabase nuance:* either way you end up with a real PostgreSQL database.

---

## 7. The Show-and-Swap Test — Peer Cold-Read

Hand your `PRD.md` + `HANDOFF.md` to a partner. **3 minutes of silent reading. No verbal context.** Confusion is data.

| # | Question | What "pass" looks like |
|---|---|---|
| 1 | **Product Value:** Can you identify the What / Who / Hypothesis in under 60 seconds? | Reader names all three from the Product Overview alone. |
| 2 | **Technical Reality:** Is Real vs. Mocked clear enough that you aren't guessing what works? | Reader can predict whether clicking a button saves data or shows a fake success. |
| 3 | **Engineering Handoff:** Does it tell you exactly which file or feature to open and build first? | Reader points to a specific screen/file as the starting point — without ambiguity. |

**Rule:** If your partner can't follow your handoff in silence, your docs aren't engineer-ready. Capture the feedback in `04-structure/swap-notes.md` — input for tightening before M5.

---

## 8. Voice Calibration — From Vibe to Spec

| You were saying | You should now write |
|---|---|
| "This is what my prototype does." | *"Product Overview: [System function]. Target persona: [The Visual Planner — Gen-Z traveler who plans by aesthetic, not price]."* |
| "Some of it isn't really connected yet." | *"Technical Reality. **Functional:** image upload, multimodal AI call, location tag extraction. **Mocked:** listing DB is a JSON file (not live Airbnb data); Visual Similarity Score is hardcoded."* |
| "Here's what I think we should build next." | *"Engineering Recommendation. Suggested build order: 1) Harden photo upload + AI call pipeline. 2) Replace mocked JSON with live listing API. Effort: medium 2–3 days / high 1–2 weeks."* |

---

## 9. The Identity Move

| You were | You are |
|---|---|
| A prototype-builder with a black box of code only you understood | A system designer with a documented, refactored, version-controlled product |
| Trapped between "demo it" and "explain it" | Equipped to hand over a system an engineer can inherit cold |
| Iterating on vibes | Hardening the build with technical rigor |

Four prompts. Three pillars. One inheritable system.
**The Living PRD is the proof — your refactored repo is the asset.**
