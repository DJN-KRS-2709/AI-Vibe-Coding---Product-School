# Module 3: The Precision Shift — Speaker Notes for Carlos

> These notes are for Carlos only. They explain what we're doing in M3, why we designed it this way, and where the fireworks are. This is NOT student-facing content.

---

## The Big Picture: Where M3 Sits

**M1** taught them they can build. **M2** taught them they should aim before they build. **M3** teaches them to direct the AI like an engineering lead — not one big prompt, but a deliberate sequence where each prompt does one job.

The paradigm shift in one line: **Students stop asking the AI to build things and start directing the AI like they're assigning sprint tickets.**

In M1 and M2, when something looked wrong, the instinct was to throw everything away and start over with a "better prompt." M3 kills that instinct. They learn to expand, add behavior, and refine — without rebuilding. That's the skill that separates someone who uses AI from someone who directs AI.

---

## Why This Matters for the Course Arc

M3 is the hinge. After M3, students have something that looks like a real product — multiple screens, navigation, loading states, error handling. That's what makes M4 (graduation), M5 (backend), and M6 (ship) possible. Without M3's execution quality, the later modules don't land because the prototype still looks like a prototype.

The Confidence Line:
- **M1–M2:** Ambiguity → "Can I even do this?"
- **M3:** Clarity → "I can direct this tool to build exactly what I want"
- **M4–M6:** Production Confidence → "This is a real product"

M3 is where ambiguity turns into clarity. It's the most important inflection point in the course.

---

## The Opening (Slides 1–2) — What We're Doing

**The hook:** "Your M2 prototype proves something. Would your VP ship it?"

We're surfacing the gap between "validates a hypothesis" (M2) and "looks like a real product" (M3). Most M2 builds have 2-3 screens, no loading states, no error handling. They test the right thing but look incomplete. The VP would say: "Good thinking. But where's the rest?"

**Why this framing works:** It respects what they built in M2 (we don't trash it) while creating honest urgency. They already know their M2 build is incomplete — we're just naming it. That creates pull for the teaching and lab ahead.

**For Carlos:** We're NOT saying M2 was bad. We're saying M2 was the foundation, and M3 is the execution layer on top of it. Same data, same hypothesis — dramatically better output.

---

## The Instructor Demo (Slides 3–5) — What We're Doing

**The setup:** Pull up the actual M2 Retention Engine prototype. Click through all 3 screens. Remind the room how good it already is — real data, design-matched to Asana, named hypothesis. Then demonstrate the facade: only 3 screens, no states, built with one mega-prompt nobody else could reproduce.

**The build:** 3 prompts, run live, sequentially:

1. **Expand** — Add a team workspace screen and a PM dashboard. Goes from 3 screens to 5 with navigation.
2. **Behavior** — Add loading skeletons, error handling, empty states. The same screens suddenly behave like real software.
3. **Refine** — Change one thing on one screen (make the PM dashboard more actionable) without touching anything else.

**Why 3 prompts, not 1:** This is the core teaching. In M2, everything went into one big prompt. That works for simple builds. But for anything complex, you lose control — the AI has to solve layout, data, design, states, and flow all at once. Things get lost. The chain approach gives the AI one job at a time. Precision accumulates.

**Where the wow is:** Two beats.
- **Beat 1 (after Prompt 2):** Loading skeletons appear. Error messages appear. The prototype suddenly *behaves* like shipped software. That's the visceral moment — same content, but it feels real now.
- **Beat 2 (after Prompt 3):** They change ONE screen and nothing else breaks. That's when the "start over" instinct dies. They're steering, not restarting.

**For Carlos:** The demo should be fast — 5 minutes total. Pre-type all 3 prompts so you paste instantly. The speed IS the point. "3 prompts, 5 screens, states, and an iteration — in under 5 minutes." Then hand it to the students.

---

## The Mini Activity (Slide 6) — What We're Doing

**The exercise:** Students pull up their own M2 prototype and answer 3 questions:
1. Does it look like it belongs in your product?
2. How many screens?
3. What happens when data is loading / there's an error / there's no data?

**Why we do this BEFORE teaching:** This is a gap-surfacing move. Most students will realize their M2 has 1-2 screens, no states, and generic styling. That's uncomfortable — and that's the point. The gap creates the motivation for the lab. If we taught first and built second, they'd nod along. By surfacing the gap first, they WANT the toolkit.

**For Carlos:** This is the "I'm leaving not excited" fix from your feedback. In the old structure, students sat through teaching without feeling the urgency. Now they feel the gap in their own work before we give them the tools to close it. The teaching lands harder because they're already thinking "how do I fix this?"

---

## The Teaching (Slides 7–10) — What We're Doing

Four concepts, kept light and fast (~12 minutes total):

**1. Prompting Maturity Curve (Slide 7):** In M1-M2, prompts were exploratory — "build me something that could help with X." In M3+, prompts are execution-level — "build me a settings page with these 4 sections, matching this design system, with loading states." We're moving students from the left (exploration) to the right (execution) of the curve.

**2. Anatomy of a Prompt Chain (Slide 8):** The 3-column framework: Expand / Behavior / Refine. This isn't "split one prompt into 3 pieces." It's 3 different TYPES of prompts that do different jobs. Expand adds scope. Behavior adds realism. Refine steers without rebuilding. Students reference this table during the lab — it's the most-used slide in the module.

**3. Multi-Step Prompting (Slide 9):** Three techniques: chain-of-thought (break complex flows into steps), constraint injection (explicit guardrails), iterative refinement (change one thing, don't rebuild). These are the execution patterns they'll use from now on.

**4. Living Prompt Packs (Slide 10):** A reusable toolkit that grows over time — context block, design references, constraint templates, output templates. Their M3 prompt chain becomes the first entry. This introduces Deliverable #4 (the Prompt Library) and connects to the **Living Prompt Pack Builder** tool they'll use after the lab.

**For Carlos:** The teaching is intentionally compressed. We cut it from the old M3's ~40 minutes of slides to ~12 minutes. The ratio flipped: 55% hands-on vs. the old 29%. Your "fireworks all the time" feedback drove this — less lecture, more building. The teaching exists to give them just enough framework to succeed in the lab.

---

## The Hands-On Lab (Slides 11–12) — Where the Fireworks Are

**This is the heart of M3.** 30 minutes, two parts.

**Part 1 — Plan (8 min):** Students open the **Prompt Chain Planner** tool (not Lovable). They fill in their M2 audit, then write all 3 prompts in the color-coded cards BEFORE building. This is critical — the planning is what makes M3 different from "just prompting better." If their chain isn't written down, they're not ready.

**Why plan first:** In M2, students dove straight into Lovable. The results were fine but not reproducible. M3's planning step creates a documented artifact — the prompt chain itself becomes a deliverable. It also forces them to think before they act, which is the precision skill we're teaching.

**Part 2 — Build (22 min):** Copy each prompt from the Planner into Lovable, one at a time. Document what happened after each prompt back in the Planner.

**Where the wow happens:** It happens in the STUDENTS' hands, not the instructor's. Watch for these moments:
- **At Prompt 1:** They go from 2-3 screens to 5. The app suddenly has a complete flow. "I have a dashboard now."
- **At Prompt 2:** Loading skeletons and error states appear. "It looks like a real product." This is usually the biggest reaction in the room.
- **At Prompt 3:** They change one screen without rebuilding everything else. The "start over" instinct dies. "I just steered it."

**For Carlos:** The wow being in students' hands is deliberate. In M1 and M2, the instructor demo carries the excitement. In M3, the students ARE the demo. Walk the room. Watch for the reactions. Call them out: "Show me your loading state. Show me your error message. That's M3." The energy in the room during this lab is the best 22 minutes of the course.

---

## Peer Review (Slide 13) — What We're Doing

**The portability test:** Partner A shares their documented prompt chain + prototype link. Partner B reads ONLY the chain. Can they understand each step? Could they reproduce a similar result?

**Why this matters:** A prompt chain that only works for the person who wrote it isn't portable. If your partner can follow it, the chain itself is the artifact — not just the prototype. This validates that they've learned to document their process, not just their output.

**The second wow beat:** When students see their partner get a similar result from just reading their chain, it clicks — the chain is reusable. It's not magic. It's a repeatable process. That's the foundation for the Living Prompt Pack (Deliverable #4).

**For Carlos:** This peer review step addresses the "advanced prompt chains producing polished output" item from your M3 column. The chain IS the advanced skill — and the peer review proves it's not just good prompting, it's a reproducible system.

---

## Break It (Slide 15) — What We're Doing

**The exercise:** When a prompt chain goes off-rails, diagnose before re-prompting. Read the chain. Compare the output. Find where it diverged. Fix ONE prompt.

**Why:** Students' instinct when something goes wrong is to start over or add more to the prompt. M3 teaches them to diagnose — was it missing context? Conflicting constraints? Wrong prompt type? This is the debugging skill that separates casual AI users from people who can reliably direct AI tools.

**For Carlos:** This directly addresses production readiness. In M5 and M6, when things go wrong with real backends and deployments, they need the debugging instinct — not the "start over" instinct. Break It establishes that skill here.

---

## The Triple Reveal (Slide 16) — The Crescendo

**Three browser tabs. M1 on the left. M2 in the middle. M3 on the right.**

Let students open all three themselves. Don't describe it. Don't narrate. Give it 30 seconds of silence while they look.

- **M1:** One prompt, one page. Static. No data.
- **M2:** Real data, hypothesis, design-matched. 2-3 screens.
- **M3:** 5+ screens, navigation, loading states, error handling, documented chain.

Then: "Same tool. Same you. That's three modules of progression."

**For Carlos:** This is the "fireworks" moment you asked for. It's visual, undeniable, and personal — they built all three. No slides can replicate the impact of a student looking at their own M1 next to their own M3. This is the image they take home. It's also the setup for M4's four-tab reveal, M5's five-tab, and M6's final showcase.

---

## Wrap + Accountability (Slides 17–19) — What We're Doing

**Takeaways** mirror the three waypoints from slide 1 (visual callback):
1. Prompt chain — documented, portable
2. Multi-screen flow — complete user journey
3. Interactive states — behaves like shipped software

**Accountability:**
- Post prototype link + full prompt chain in #builds
- Engage with 2 others — could you follow their chain?
- Optional: add a 4th prompt (creates incentive to keep building)

**M4 Preview:** "You've built fast, built smart, and built precise. Your prototype looks like a real product. Next: graduate it. Extract the spec. Clean the code. Make it handoff-ready."

**For Carlos:** The M4 preview is intentionally tantalizing. Students leave M3 with the best prototype they've ever built — and the preview says "you haven't even graduated it yet." That emotional arc (pride in M3 → curiosity about M4) is what keeps them engaged between sessions.

---

## The Interactive Tools for M3

**1. Prompt Chain Planner** — Used DURING the lab. Students plan their 3-prompt chain here before opening Lovable. Has scenario auto-populate (Retention Engine, Internal Tool, Marketplace Trust, Dashboard) with example prompts. M2 audit section. Color-coded prompt cards. Result documentation. Copy Full Chain button.

**2. Living Prompt Pack Builder** — Used AFTER the lab. Students take their prompt chain and build it into a reusable toolkit: context block, design references, constraint templates, output templates. This is Deliverable #4. Has localStorage auto-save and import/export for portability across sessions.

**For Carlos:** The Planner is the lab companion — it forces planning before building. The Pack Builder is the long-term asset — it grows across M3, M4, M5, and M6. Together they establish the habit: plan → build → document → reuse.

---

## Summary: What M3 Achieves

| What | Why It Matters |
|------|---------------|
| Students expand their M2 build instead of starting over | Kills the "rebuild" instinct. Teaches iterative direction. |
| 3-prompt chain (Expand / Behavior / Refine) | Structured framework they'll use in every module going forward |
| Interactive states (loading, empty, error) | The prototype crosses from "mockup" to "feels like real software" |
| Documented, portable chain | The process becomes the deliverable, not just the output |
| Peer review / portability test | Validates the chain works for someone else — not just the author |
| Triple reveal (M1/M2/M3) | Visual proof of progression. The "fireworks" moment. |
| Living Prompt Pack (Deliverable #4) | Long-term asset that grows through M4, M5, M6. Reusable across projects. |

**One sentence for Carlos:** M3 is where students stop asking the AI to build things and start directing it with precision — and they prove it by expanding their M2 into something the VP thinks engineering built, using a documented 3-prompt chain their partner can reproduce.
