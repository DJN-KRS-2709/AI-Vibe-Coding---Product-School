# Module 1 — Frameworks Reference Card

> One-page summary of every framework introduced in Module 1. Use it as the cheat sheet you keep open while you build.

---

## 1. The Confidence Line

The single arc that runs through the entire certification. Every module sits on a phase.

| Phase | Modules | What you do | What you produce |
|---|---|---|---|
| **High Ambiguity** | M1–M2 | Build to think. Explore many directions. Kill bad ideas fast. | Rough prototypes + named assumptions. |
| **Gaining Clarity** | M3–M4 | Apply context and intent. Transition from vibe to structure. | Living PRD + structured prompt pack. |
| **Production Confidence** | M5–M6 | Real APIs, deployment, measurement, iteration. | Live URL + evidence brief + handoff note. |

**Rule:** every prompt is a choice — *explore* the path, or *refine* it.

---

## 2. The High-Velocity Prototyping Cycle

Four moves. Loop through them twice in M1; roughly fifty times across the certification.

| Move | What it means | What to skip if you must |
|---|---|---|
| ① **Build** | From instinct. Goal: shareable URL, not finished product. | Never skip. |
| ② **Show** | Silent walkthrough. No verbal tour. | Never skip — this is where most signal lives. |
| ③ **Learn** | Raw signal beats polite feedback. Write what confused. | Never skip. |
| ④ **Decide** | Kill, refine, or escalate. No prototype lives without a verdict. | **PMs reliably skip this.** Don't. |

---

## 3. The Three Multimodal Entry Points

Three ways to start every build. Pick by job, not by habit.

| Entry point | When | Job |
|---|---|---|
| **Text-to-App** | 0 → 1, no design yet. | Greenfield exploration. Cures blank-page syndrome. |
| **Screenshot-to-App** | 1 → N, refining vibe sketch. | Clone a known-good pattern (Mobbin, competitor). |
| **Design-to-Code** | On-brand from minute one. | Prototyping inside an existing product. Paste Figma + tokens. |

---

## 4. Credit Efficiency — The Four Rules

Credits are fuel. Pro plan ≈ 100 credits/month. Spend them on architecture, not typos.

1. **Plan in a sandbox.** 60% of prompt refinement happens in ChatGPT / Gemini / Claude (free).
2. **Paste, don't draft.** Aim for one-shot generations. Lovable is the execution engine.
3. **Edit code directly.** Hex codes, padding, label typos — fix in the code panel.
4. **The Eject Rule.** If a prompt fails twice, *stop*. Export, debug externally, paste back. Never enter the "credit death spiral."

---

## 5. The Lab 2 Upgrade Paths

Four ways to turn a vibe sketch into a credible tool. Pick **two**, depth over breadth.

| Path | Move | Best when |
|---|---|---|
| **A — Design Match** | Mobbin screenshot → clone palette/layout/nav. | Your v1 looks unbranded. |
| **B — Add Interactivity** | Filters, expandable cards, loading skeleton. | Your v1 is a screenshot in disguise. |
| **C — Surgical Refinement** | One focused prompt, one section. | Your v1 mostly works; one block lets it down. |
| **D — Existing Product Track** | Paste real hex codes + Figma CSS. | You're prototyping for your actual day job. |

---

## 6. Toy vs Tool — The Distinction

| The Toy | The Tool |
|---|---|
| Looks impressive. Proves nothing. | Looks real. Proves something works. |
| Generates applause, not insights. | Validates an assumption with clickable evidence. |
| No logic behind the screen. | Handles at least one real user flow end-to-end. |
| Dies after the demo. | Survives when someone else uses it. |

**Test:** If your prototype helped you *decide* something, it's a tool. If it only looked cool, it's a toy.

---

## 7. The Triple-Threat Build (mental model)

When three executives have three theories and zero data:

1. **Don't pick a side.** Don't escalate. Don't debate.
2. **Build all three** as rough prototypes (15 min each).
3. **Compare evidence** side by side, not opinions.
4. **Kill two**, keep one, name the assumption it tested.

This is the universal Module-1 move. You'll repeat it whenever your team has more opinions than data.

---

## 8. The Review Stack — Show & Swap + Self-Score

Every lab in this module ends with a structured review. The reviewer changes; the structure doesn't:

1. **Time-box** — `⏰ N min`.
2. **Open the artifact in a fresh tab** — no narration, no setup context.
3. **Three questions** — what was immediately clear · what confused the reviewer · what assumption the build is testing.
4. **The reviewer** — a peer (Show & Swap after Lab 1) or yourself against the 1–5 rubric (after Lab 2). Async fallback: the AI-review prompt.
5. **Async share** — commit to your repo, post the one-line learning in `#cohort-channel`.

**One paired touch-point per module, otherwise individual. The build is yours. The signal can come from a peer, the rubric, or the AI — whichever is closest to honest.**

---

## 9. Submission rule (for the final project)

- **What:** the URL of your `vibe-coding-project/` fork.
- **When:** within 7 days post-cohort.
- **Format:** 100% solo. No live demo required.
- **Optional showcase:** 3-min async Loom in `#cohort-channel`. Instructor responds in-thread within ~5 days.
- **Rubric:** Application of Concepts · Credibility & Reasoning · Clarity · Strategic Thinking. Scale 1 (Poor 0–49) / 2 (Sufficient 50–79) / 3 (Excellent 80–100).

---

## Quick reference — what to remember walking out of M1

- Speed is the floor. **Evidence per hour** is the ceiling.
- Three theories beat one opinion. **Build all three.**
- The cycle isn't closed until you've **decided**.
- Plan prompts in a sandbox. **Paste, don't draft.**
- Whatever you scored your v2 is **the gap M2–M6 closes**.
