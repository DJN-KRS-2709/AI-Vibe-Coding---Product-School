# Module 2: What Are You Actually Testing? — Problem Framing and Validation Design

## Detailed Session Plan (2 Hours)

---

## Module Overview

| Field | Value |
| --- | --- |
| **Duration** | 120 minutes |
| **Confidence Line Position** | Still left. High ambiguity, but now with methodology. |
| **Core Principle** | Name the assumption before you open the tool. Build smart, not just fast. |
| **Tool** | Lovable (Pro accounts). Gemini/ChatGPT for prompt planning. Mobbin for templates. |
| **Pre-requisite** | Module 1 complete. Students have built 2 prototypes and experienced the full cycle. |
| **What students walk out with** | A framed problem with a named assumption, 1–3 divergent prototypes built to test it, and the design systems/prompt anatomy that makes prototypes look and feel real |

### The Energy Contract

Module 1 proved they can build fast. Module 2 teaches them to build smart. The core question: *What am I actually testing?* If they can't answer that in one sentence before they start building, they're building a toy, not a tool.

**Carlos feedback (from Feb 17):** Design systems are a meaty topic. People want to decompose what makes an excellent prompt—templates, Figma import, Mobbin patterns. Module 2 goes deeper. This is where we cover that.

**Terminology (consistent across all Product School courses):**
- **Demo** = instructor building live
- **Hands-on lab** = students building in the tool
- **Breakout group activity** = students working in groups (e.g., filling templates, peer validation)

---

## Minute-by-Minute Breakdown

---

### Block 1: The Lens (0:00 - 0:41)

---

#### 0:00 - 0:03 | Slide 1: Recap + The Core Question (3 min)

**What happens:** Quick recap of Module 1. Bridge to the core question of Module 2.

**Instructor script:**

> "Module 1: you built fast. You completed a full cycle — build, show, learn, decide. Today, two things change. First: you commit. You're picking the scenario you'll carry through the rest of this course — your company problem or one of the course scenarios. What you build today is the foundation of your final project. Second: we add the lens. Before you open any tool, you answer one question: What am I actually testing? If you can't answer that in one sentence, you're building a toy, not a tool. That's today."

**Slide content:** "What Are You Actually Testing?" | MODULE 2 | The lens that turns speed into strategy. *Today you commit to your final project scenario.*

---

#### 0:03 - 0:09 | Ice Breaker: True or False — Did AI Really Do This? (6 min)

**What happens:** Instructor runs 5–6 items from "True or False Set A." Poll true/false, reveal. Bridges to "what are we actually testing?"

**Instructor script:**

> "Quick gut check. I'll read a claim about something AI did. True or false? [Poll.] [Reveal.] Half sound fake and are real. Half sound real and are fake. That's why we ask: what are we actually testing?"

**Reference:** See `Module Ice Breakers - Fun Start Activities.md`

---

#### 0:09 - 0:24 | Slides 2–4: Problem Framing & Assumption Mapping (15 min)

**Purpose:** Introduce the scaffolding that turns fast building into smart building. Reforge's 6-element problem frame, adapted for validation.

**Slide 2: The Problem Frame (Reforge-adapted)**

**Six elements** — used to frame *what you're testing*, not just what you're building:
- **Goal** — What are we trying to achieve?
- **Problem** — What's blocking us?
- **Context** — Who, where, when?
- **Constraints** — What can't we change?
- **Success Criteria** — What does "validated" look like?
- **Explore** — What are we trying to learn?

**Instructor script:**

> "You don't need to fill out a 6-page PRD. But you do need to name the thing you're trying to learn. This frame helps. Goal, problem, context, constraints, success criteria, explore. The last one—explore—is the key. What are we trying to learn by building this?"

**Slide 3: Assumption Mapping**

**The discipline:** For any product idea, what are the 3 riskiest assumptions? Which one, if wrong, kills the whole thing? Build to test THAT one first.

**Two tracks:**
- **0-to-1 (greenfield):** Risk is usually desirability—do users want this?
- **1-to-N (existing product):** Risk is adoption ("will users find this?") or integration ("does this break existing workflows?")

**Instructor script:**

> "Most teams build to look smart. You build to learn. Assumption mapping: what are the three riskiest assumptions? Which one kills the whole thing if it's wrong? Build to test that one first. For existing products, the risk shifts—it's adoption, integration, not just desirability."

**Slide 4: Divergent Prototypes & Fidelity Mapping**

**Divergent prototypes:** Build 3–5 fundamentally different solution directions, not variations of the same idea. Prompt for divergence.

**Fidelity mapping:** Match fidelity to the question. Don't build a full app when a landing page answers the question.
- Landing page → "Will they sign up?"
- Clickable mockup → "Does this flow make sense?"
- Functional app → "Can they complete the task?"

**Instructor script:**

> "Most teams ask for 'a few options' and get the same thing with different button placements. You want divergence—fundamentally different directions. And match fidelity to the question. Don't build a full app when a landing page answers 'will they sign up?'"

---

#### 0:24 - 0:41 | Slides 5–7: Design Systems & Prompt Anatomy (17 min)

**Purpose:** Carlos feedback—this is the meaty content. Decompose what makes an excellent prompt. Templates, Figma, Mobbin, credits strategy.

**Slide 5: What Makes an Excellent Prompt**

**The anatomy of a great prompt:**
- **Context** — What's the product? Who's it for?
- **Reference** — Screenshot, design system, or template that shows the look and feel
- **Constraint** — What must be included? What must be avoided?
- **Output** — What should it produce? One screen? Full flow? Specific components?

**Instructor script:**

> "Carlos asked: what makes an excellent prompt? Context—what's the product, who's it for. Reference—a screenshot or template so the AI knows the look and feel. Constraint—what must be there, what must not. Output—one screen or full flow? The more specific, the better the result."

**Slide 6: Templates & Design System Sources**

**Mobbin (free for students):** Real product screens. Pricing pages, checkout flows, dashboards, onboarding. Use for inspiration and as prompt context.

**Figma:** If your design system lives in Figma, you can import it. MCP servers can connect Lovable directly to Figma—we'll demo the possibility. (Brief mention—full setup is Module 3.)

**Your existing product:** Screenshot it. Feed it in. "Match this look and feel, then add [your new feature]."

**Instructor script:**

> "Mobbin is free—check out pricing page examples, checkout flows, dashboards. Use them as context. If your design system is in Figma, you can import it—we'll go deeper in Module 3. For now: screenshot your product, feed it in. Match the look, add your feature."

**Slide 7: Credits Strategy**

**The reality:** Lovable gives ~100 credits/month. You can burn through them fast if you prompt in the tool.

**The strategy:**
- **Plan in Gemini or ChatGPT** — Structure your prompt, iterate on wording, get it right. No credits burned.
- **Paste into Lovable** — When the prompt is ready, paste it in. One generation, one credit.
- **Fix in code when possible** — Sometimes fixing the code directly (edit the generated output) is faster and cheaper than re-prompting.

**Instructor script:**

> "Credits reminder. Plan your prompts in Gemini or ChatGPT—we have a code for free ChatGPT Plus. Get the prompt right there. Paste it into Lovable when you're ready to build. That alone saves credits. And if something's wrong—a typo, a wrong color—sometimes fixing the code directly is faster than re-prompting."

---

### Block 2: Frame First, Then Build (0:41 - 1:26)

---

#### 0:41 - 0:51 | Hands-on Lab Part 1: "Frame Before You Build" (10 min)

**Purpose:** Students write their assumption and success criteria before touching any tool. This is the discipline M1 didn't require.

**Lab Brief (displayed + Slack):**

> **This is your commitment moment.** Starting today, you're building your final project. Pick the scenario you'll carry through M2–M6. Everything you build from now on adds a layer to this product.
>
> **Choose your track:**
>
> **Course Scenario 1 — The Retention Engine:** B2B SaaS losing 30% of customers in 90 days. Is it onboarding? Feature discovery? Team invitation? (Full brief in Final Project guide.)
>
> **Course Scenario 2 — The Internal Tool Nobody Uses:** CRM with 18% adoption. Too many clicks? Wrong motivation? Wrong timing? (Full brief in Final Project guide.)
>
> **Course Scenario 3 — The Marketplace Trust Problem:** Bookings flat despite signups. Zero-review providers. Trust badges? Guarantees? Profile redesign? (Full brief in Final Project guide.)
>
> **Course Scenario 4 — The Dashboard Nobody Reads (Existing Product):** Analytics dashboard with 60% bounce rate. Information overload? Navigation? Irrelevance? (Full brief in Final Project guide.)
>
> **Your Company Problem:** The problem you posted in Slack. This is your actual work challenge.
>
> **Before you open Lovable, write:**
> 1. The riskiest assumption I'm testing
> 2. What I'll build to test it
> 3. What fidelity is needed (landing page? clickable flow? functional app?)
> 4. What "validated" vs. "invalidated" looks like
>
> **Post your frame in Slack** (one short paragraph). Include which scenario you chose. That's your commitment — this is your final project from here on out.

**What the instructor does:**
- Circulates. Checks that students are writing, not building.
- At 5 min: "If you're stuck on the assumption, ask: what would kill this idea if we learned it was wrong?"
- At 8 min: "1 minute to post your frame. Then we build."

---

#### 0:51 - 1:16 | Hands-on Lab Part 2: "Build to Test" (25 min)

**Purpose:** Students build with intent. They're building specifically to test their named assumption, at the fidelity they chose.

**Lab Brief (continued):**

> **Now build.** You have 25 minutes. Remember: this is the start of your final project. What you build today carries forward.
>
> - Use your frame as your North Star. Every prompt should serve the assumption.
> - Apply what we just covered: add context, use a Mobbin template or screenshot as reference, add constraints.
> - Build 1–3 divergent directions — different solutions, not variations.
> - Credits tip: Plan complex prompts in Gemini/ChatGPT first. Paste into Lovable when ready.
>
> **Produce:** 1–3 prototype links. Share in Slack with your assumption: "Scenario: [name]. Testing: [X]. Links: [A], [B], [C]."

**What the instructor does:**
- Circulates. If someone is building without referencing their frame: "What assumption are you testing? Does this prototype test it?"
- Highlights students using Mobbin or design matching. "Who used a Mobbin template? Show us."
- At 12 min: "You should have at least one direction. If you're building a second, make it divergent—different approach, not a tweak."
- At 22 min: "2 minutes. Whatever you have, share the link. It doesn't need to be perfect—it needs to test something."

---

#### 1:16 - 1:26 | Breakout Group Activity: "Does This Actually Test It?" (10 min)

**Purpose:** Peer validation. The validator evaluates: does this prototype actually test the assumption the builder claimed? Or did they build something impressive that proves nothing?

**How it works:**
- Breakout rooms. "How many per room? Press the button." (Carlos: random assignment fine.)
- Person A shares their frame + links. Person B reviews as a user: Does this prototype test the stated assumption? What would validate vs. invalidate it?
- Switch roles. Repeat.

**Feedback questions:**
- Does this prototype actually test the assumption you wrote?
- What would validate it? What would invalidate it?
- If you were the stakeholder, what would you decide?

**Instructor script:**

> "The question isn't 'is this cool?' It's 'does this test what you said you were testing?' Your partner will tell you. Be honest. If they built something impressive that proves nothing, say so. That's the valuable feedback."

---

### Block 3: Full-Class Share (1:26 - 1:36)

---

#### 1:26 - 1:31 | Quick Share: "What Did You Validate?" (5 min)

**Format:** Full-class discussion. Everyone back in main room.

> "Popcorn. One sentence: What assumption did you test, and what did you learn? Validated, invalidated, or still unclear."

Take 4–5 responses. Synthesize: "The best outcomes aren't always 'it worked.' Sometimes the best outcome is 'we learned it doesn't work—and we learned it in 30 minutes, not 3 months.'"

---

#### 1:31 - 1:36 | Pulse Check (5 min)

**Format:** Slack poll or show of hands.

> "Rate your frame. 1 = I built something but didn't really test an assumption. 5 = I built something that definitively tested what I said I was testing."

Preview: "By Module 4, everyone should be at 4–5. That's the skill we're building."

---

### Block 4: Break It + Synthesis (1:36 - 2:01)

---

#### 1:36 - 1:48 | "Break It" Exercise (12 min)

**What we're trying to break:** The illusion that *fidelity = value*. A beautiful prototype that validated nothing is a toy. An ugly one that answered the critical question is a tool.

**How it works:**

Instructor shows two prototypes side by side:

**Prototype A:** High-fidelity, polished, looks production-ready. But it doesn't test any specific assumption. It's impressive. It proves nothing.

**Prototype B:** Low-fidelity, rough, maybe one screen. But it definitively answers: "Will users understand this flow?" or "Do they want this feature?" It's ugly. It's a tool.

**Instructor script:**

> "Fidelity without intent is vanity. This one [A] looks great. Stakeholders will ooh and aah. But what did we learn? Nothing. This one [B] is rough. But we answered the question. Clarity of question beats quality of build. Every time."

**Reflection moment (2 min):**

> "Take 60 seconds. Look at your own prototype. Does it test your assumption? Or did you build something impressive that doesn't quite answer the question? No wrong answers—just honest reflection."

---

#### 1:48 - 1:58 | Retroactive Framework: "The Validation Mindset" (10 min)

**Purpose:** Name what they just did. Connect to the Confidence Line.

**Key talking points:**

**1. The Validation Design Loop**
> "Frame → Build → Test → Decide. You just did it with discipline. You named the assumption first. You built to test it. You got feedback. That's the difference between Module 1 and Module 2."

**2. Confidence Line position**
> "You're still on the left side—high ambiguity. But now you have a methodology. You're not just building fast. You're building to learn. Module 3 adds precision—structured prompts, living prompt packs. Module 4 is the graduation moment. Each module builds."

**3. What's coming (Module 3)**
> "Next: Precision prompting. Context layering, design system imports, agentic workflows. You'll learn to say 'build me exactly this' instead of 'build me something.'"

---

### Block 5: Close (1:58 - 2:06)

---

#### 1:58 - 2:06 | Accountability + Wrap (8 min)

**The ask:**
> "Post your framed prototype(s) in #builds. Caption: What assumption did you test? What did you learn? Not what you built—what you learned. Engage: look at 2 others. Did their prototype actually test what they said?"

**Wrap + Preview:**
> "No homework. But you've committed to your scenario — that's your product from here forward. Next module, you take what you built today and level it up with precision prompting. Same product, better execution. Context layering, design system matching, documented prompt chains. Module 3: build me exactly this. See you then."

---

## Session Summary

| Block | Time | Duration | Activity Type |
| --- | --- | --- | --- |
| Recap + Core Question | 0:00 - 0:03 | 3 min | Instructor talk |
| Ice Breaker: True or False — Did AI Really Do This? | 0:03 - 0:09 | 6 min | Fun start activity |
| Problem Framing + Assumption Mapping | 0:09 - 0:24 | 15 min | Instructor talk |
| Design Systems + Prompt Anatomy | 0:24 - 0:41 | 17 min | Instructor talk |
| Hands-on Lab: Frame First | 0:41 - 0:51 | 10 min | **Hands-on lab** (writing) |
| Hands-on Lab: Build to Test | 0:51 - 1:16 | 25 min | **Hands-on lab** (building) |
| Breakout: Does This Test It? | 1:16 - 1:26 | 10 min | Breakout group activity |
| Quick Share + Pulse Check | 1:26 - 1:36 | 10 min | Class discussion |
| Break It + Reflection | 1:36 - 1:48 | 12 min | Instructor demo + discussion |
| Retroactive Framework | 1:48 - 1:58 | 10 min | Instructor talk |
| Accountability + Wrap | 1:58 - 2:06 | 8 min | Slack + close |

### Time Distribution

| Category | Minutes | Percentage |
| --- | --- | --- |
| **Students building** | 25 min | 21% |
| **Students framing** | 10 min | 8% |
| **Breakout / peer validation** | 10 min | 8% |
| **Instructor teaching** | 47 min | 39% |
| **Class discussion / Break It** | 24 min | 20% |
| **Wrap** | 8 min | 7% |
| **Total hands-on (framing + building + breakout)** | **45 min** | **38%** |

---

## Key Materials Needed

### Prepared Before Class

1. **Problem framing slides** — 6-element frame, assumption mapping, fidelity mapping
2. **Design systems slides** — Prompt anatomy, Mobbin, Figma mention, credits strategy
3. **Two problem briefs** — One 0-to-1, one existing product (see Appendix)
4. **"Break It" prototypes** — Pre-built: (A) beautiful but validates nothing, (B) ugly but answers the question
5. **Mobbin tab open** — Pre-selected examples: pricing page, checkout flow, dashboard
6. **Lab briefs** ready to paste in Slack

### Student Requirements

- Module 1 complete
- Lovable Pro account
- Slack access
- Optional: Screenshot of their real product (for Scenario 4 or Your Company track)

---

## Appendix: Problem Briefs (Aligned to Final Project Scenarios)

*Students commit to one of these scenarios in M2 and carry it through M6. Full scenario details, including module-by-module progression, are in `Final Project - Requirements and Scenario Guide.md`.*

### Scenario 1: The Retention Engine (0-to-1)
> A B2B SaaS company (project management tool, 5K paying teams) is losing 30% of customers in the first 90 days. Users "sign up, poke around, and ghost." The data team says the highest-retention users all invite a second team member within 3 days. **M2 framing:** Is the problem that users don't know they can invite? That the invite flow is buried? Or that solo users don't see the value of collaboration? Name the riskiest assumption. Build 1–3 divergent directions to test it.

### Scenario 2: The Internal Tool Nobody Uses (0-to-1)
> A 200-person sales team has a CRM note-taking tool with 18% adoption. Reps say "too many clicks." The VP wants AI. Engineering says the tool is "fine." **M2 framing:** Is the problem input friction (too many clicks)? Motivation (reps don't see value in documenting)? Timing (they forget by the time they're at their desk)? Name the riskiest assumption. Build to test it.

### Scenario 3: The Marketplace Trust Problem (0-to-1)
> A peer-to-peer services marketplace has bookings flat despite growing signups. The #1 reason people don't book: "I don't trust the providers." New providers have zero reviews. **M2 framing:** Is the problem lack of social proof (no reviews)? Risk aversion (what if something goes wrong)? Information asymmetry (can't evaluate providers)? Name the riskiest assumption. Build to test it.

### Scenario 4: The Dashboard Nobody Reads (Existing Product)
> A customer-facing analytics dashboard has a 60% bounce rate on first visit. 12 charts, 4 filter options. Power users love it. 80% of new signups are non-technical users who just want: "Is my campaign working?" **M2 framing:** Is the problem information overload? Lack of guidance? Irrelevant metrics for non-technical users? Name the riskiest assumption. You can't redesign the whole product — just the first experience.

### Your Company Problem (Your Product Track)
> Use the problem from your Slack intro. Write the assumption frame. Build 1–2 prototypes to test it. Use a screenshot of your existing product as context. **M2 framing:** What's the riskiest assumption about your initiative? If you learned it was wrong, would it kill the project?
