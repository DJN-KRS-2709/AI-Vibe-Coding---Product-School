# Gamma Prompt: Module 2 Teaching Slide Deck

**Copy everything below the line and paste it into Gamma. Use "Paste an outline" or the prompt field.**

---

## Instructions for Gamma

Create a professional slide deck for teaching a 2-hour workshop called **"Module 2: What Are You Actually Testing? — Problem Framing and Validation Design"** in a Vibe Coding certification course. The audience is senior product managers who completed Module 1 — they can build fast; now they're learning to build smart. Tone: energetic, practical, strategic. The deck supports live teaching and hands-on labs. Avoid corporate jargon. Use clean, modern design with clear typography and minimal text per slide.

---

## Slide 1 — Module 2 Title + Core Question
**What Are You Actually Testing?**

MODULE 2 | VIBE CODING CERTIFICATION

Module 1: you built fast. Today we add the lens.

**The core question:** What am I actually testing? If you can't answer that in one sentence before you open the tool, you're building a toy, not a tool.

---

## Slide 2 — The Problem Frame
**The Problem Frame** (Reforge-adapted)

Six elements to frame *what you're testing*, not just what you're building:

- **Goal** — What are we trying to achieve?
- **Problem** — What's blocking us?
- **Context** — Who, where, when?
- **Constraints** — What can't we change?
- **Success Criteria** — What does "validated" look like?
- **Explore** — What are we trying to learn?

The last one—*Explore*—is the key. What are we trying to learn by building this?

---

## Slide 3 — Assumption Mapping
**Assumption Mapping**

For any product idea, what are the 3 riskiest assumptions? Which one, if wrong, kills the whole thing? Build to test THAT one first.

**0-to-1 (greenfield):** Risk is usually desirability—do users want this?

**1-to-N (existing product):** Risk shifts to adoption ("will users find this?") or integration ("does this break existing workflows?")

Most teams build to look smart. You build to learn.

---

## Slide 4 — Divergent Prototypes & Fidelity Mapping
**Divergent Prototypes & Fidelity Mapping**

**Divergent prototypes:** Build 3–5 fundamentally different solution directions, not variations of the same idea. Prompt for divergence.

**Fidelity mapping:** Match fidelity to the question. Don't overbuild.
- Landing page → "Will they sign up?"
- Clickable mockup → "Does this flow make sense?"
- Functional app → "Can they complete the task?"

Most teams ask for "a few options" and get the same thing with different button placements.

---

## Slide 5 — What Makes an Excellent Prompt
**What Makes an Excellent Prompt**

The anatomy of a great prompt:

**Context** — What's the product? Who's it for?

**Reference** — Screenshot, design system, or template that shows the look and feel

**Constraint** — What must be included? What must be avoided?

**Output** — What should it produce? One screen? Full flow? Specific components?

The more specific, the better the result.

---

## Slide 6 — Templates & Design System Sources
**Templates & Design System Sources**

**Mobbin** (free) — Real product screens. Pricing pages, checkout flows, dashboards, onboarding. Use for inspiration and as prompt context.

**Figma** — If your design system lives in Figma, you can import it. MCP can connect Lovable to Figma. (Module 3 goes deeper.)

**Your existing product** — Screenshot it. Feed it in. "Match this look and feel, then add [your new feature]."

---

## Slide 7 — Credits Strategy
**Credits Strategy**

Lovable gives ~100 credits/month. You can burn through them fast.

**The strategy:**
1. **Plan in Gemini or ChatGPT** — Structure your prompt, iterate on wording. No credits burned.
2. **Paste into Lovable** — When the prompt is ready, paste it in. One generation.
3. **Fix in code when possible** — A typo or wrong color? Edit the generated output directly instead of re-prompting.

---

## Slide 8 — Hands-on Lab: Frame Before You Build
**Hands-on Lab Part 1: Frame Before You Build** | 10 Minutes

**Choose one brief:**
- **Brief A (0-to-1):** New product problem
- **Brief B (Existing Product):** Dashboard 60% bounce rate—prototype 3 improvements

**Before you open Lovable, write:**
1. The riskiest assumption I'm testing
2. What I'll build to test it
3. What fidelity is needed
4. What "validated" vs. "invalidated" looks like

**Post your frame in Slack.** That's your commitment.

---

## Slide 9 — Hands-on Lab: Build to Test
**Hands-on Lab Part 2: Build to Test** | 25 Minutes

**Now build.** Use your frame as your North Star.

- Apply prompt anatomy: context, reference, constraints, output
- Use Mobbin or a screenshot as reference
- Build 1–3 divergent directions—different solutions, not variations
- Credits tip: Plan complex prompts in Gemini/ChatGPT first

**Produce:** 1–3 prototype links. Share in Slack with your assumption: "Testing: [X]. Links: [A], [B], [C]."

---

## Slide 10 — Breakout Group Activity: Does This Actually Test It?
**Breakout Group Activity: Does This Actually Test It?** | 10 Minutes

Person A shares their frame + links. Person B reviews: Does this prototype test the stated assumption?

**Feedback questions:**
- Does this prototype actually test the assumption you wrote?
- What would validate it? What would invalidate it?
- If you were the stakeholder, what would you decide?

The question isn't "is this cool?" It's "does this test what you said you were testing?"

**Format:** Breakout rooms. Instructor: "How many per room? Press the button."

---

## Slide 11 — What Did You Validate?
**What Did You Validate?** — Full-class discussion

One sentence: What assumption did you test, and what did you learn?

Validated, invalidated, or still unclear.

The best outcomes aren't always "it worked." Sometimes the best outcome is "we learned it doesn't work—in 30 minutes, not 3 months."

---

## Slide 12 — "Break It" Exercise
**"Break It" Exercise**

**What we're breaking:** The illusion that fidelity = value.

**Prototype A:** High-fidelity, polished, production-ready. Validates nothing. Impressive. A toy.

**Prototype B:** Low-fidelity, rough, one screen. Definitively answers the question. Ugly. A tool.

Fidelity without intent is vanity. Clarity of question beats quality of build. Every time.

---

## Slide 13 — Reflection Moment
**Reflection Moment**

Take 60 seconds. Look at your own prototype.

Does it test your assumption? Or did you build something impressive that doesn't quite answer the question?

No wrong answers—just honest reflection.

---

## Slide 14 — The Validation Design Loop
**The Validation Design Loop**

**Frame → Build → Test → Decide**

You just did it with discipline. You named the assumption first. You built to test it. You got feedback.

That's the difference between Module 1 and Module 2.

---

## Slide 15 — Confidence Line + What's Next
**The Confidence Line**

You're still on the left side—high ambiguity. But now you have a methodology. You're not just building fast. You're building to learn.

**Next: Module 3** — Precision prompting. Context layering, design system imports, agentic workflows. "Build me exactly this" instead of "build me something."

---

## Slide 16 — Accountability: Before We Wrap
**ACCOUNTABILITY** | Before We Wrap

**Post your framed prototype(s)** in #builds. Caption: What assumption did you test? What did you learn?

**Engage** — Look at 2 others. Did their prototype actually test what they said?

---

## Slide 17 — Wrap + Preview
**Wrap + Preview**

**No Homework** — You're done. Optional: take your real product problem, write the assumption frame, build one prototype to test it.

**Next: Module 3** — Precision prompting. Build me exactly this.

See you then.

---

## Slide 18 — What You Accomplished Today
**What You Accomplished Today**

- **Framed before you built** — Named the assumption, chose the fidelity
- **Built with intent** — 1–3 prototypes designed to test, not impress
- **Validated (or invalidated)** — You learned something definitive
- **Design systems foundation** — Prompt anatomy, Mobbin, credits strategy

You didn't just build. You built to learn.

---

## Slide 19 — The Journey Continues
**The Journey Continues**

Module 1: Build fast.  
Module 2: Build smart.  
Module 3: Build precise.

From "I don't know what to build" to "I know exactly what to build and why."

Next up: Precision prompting.

---

## Design Notes for Gamma
- Use a consistent, modern template (match Module 1 if part of a series)
- Keep slides readable from the back of a room — large text, high contrast
- Slide 1 — "What Are You Actually Testing?" as the hook
- Slides 2–4 — Problem framing content (can be dense; use bullets)
- Slides 5–7 — Design systems (Carlos: meaty topic; clear, scannable)
- Slide 12 — "Break It" contrast: A vs B side by side concept
- Slides 18–19 — Celebratory close, bridge to Module 3
