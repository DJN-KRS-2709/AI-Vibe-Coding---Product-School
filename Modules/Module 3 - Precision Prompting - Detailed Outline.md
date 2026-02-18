# Module 3: Precision Prompting — Communicating Product Intent to AI

## Detailed Session Plan (2 Hours)

---

## Module Overview

| Field | Value |
| --- | --- |
| **Duration** | 120 minutes |
| **Confidence Line Position** | Moving right. You know your direction. Now you need precision. |
| **Core Principle** | Shift from "build me something" to "build me exactly this." |
| **Tool** | Lovable. Gemini/ChatGPT for prompt planning. Mobbin. Figma/MCP for design context. |
| **Pre-requisite** | Modules 1–2 complete. Students can build fast and build smart. |
| **What students walk out with** | A documented prompt chain, a precision-built prototype, and the foundation for a living prompt pack |

### The Energy Contract

As confidence grows, prompts must evolve. Module 1: raw speed. Module 2: named assumptions. Module 3: precision. The goal is to direct the AI like a tech lead—giving it enough context, constraints, and reference so it builds what you actually mean.

**Carlos feedback (from Feb 13):** "How are you making sure the look and feel is as similar as possible to your current product?" Context layering for existing products—Figma, Mobbin, screenshot-based cloning—is critical. MCP for design systems: show it's possible.

**Terminology (consistent across all Product School courses):**
- **Demo** = instructor building live
- **Hands-on lab** = students building in the tool
- **Breakout group activity** = students working in groups (e.g., swapping prompt chains, peer review)

---

## Minute-by-Minute Breakdown

---

### Block 1: The Precision Shift (0:00 - 0:37)

---

#### 0:00 - 0:03 | Slide 1: Recap + The Precision Shift (3 min)

**What happens:** Bridge from Module 2. Introduce the core shift.

**Instructor script:**

> "Module 1: build fast. Module 2: build smart—name the assumption first. Today: build precise. You know what you want. Now you need to communicate it so the AI builds exactly that. 'Build me something' becomes 'build me exactly this.'"

**Slide content:** "Precision Prompting" | MODULE 3 | Communicating product intent to AI. The shift from exploration to execution.

---

#### 0:03 - 0:10 | Ice Breaker: Who Said It? — Extended Set (7 min)

**What happens:** Instructor runs 8–10 items from "Who Said It? Set B." Deeper cuts before precision work. Poll, reveal.

**Instructor script:**

> "Same game, deeper cuts. Human or AI? [Run 8–10.] Today we're moving from exploration to precision — so calibrating your radar matters."

**Reference:** See `Module Ice Breakers - Fun Start Activities.md`

---

#### 0:10 - 0:22 | Slides 2–4: Prompting Maturity Curve & Context Layering (12 min)

**Purpose:** Introduce the framework. Exploration prompts (M1–M2) vs. execution prompts (M3+). Context layering as the core technique.

**Slide 2: The Prompting Maturity Curve**

**Exploration prompts (left):** Divergent, open. "Build me something that could help with X." Good for ambiguity.

**Execution prompts (right):** Convergent, precise. "Build me a settings page with these 4 sections, matching this design system, with these constraints." Good when you know what you want.

**Instructor script:**

> "Your prompt style should match your confidence level. When you're exploring, open prompts are fine. When you know your direction, you need precision. That's today."

**Slide 3: Context Layering — The Core Technique**

**What to feed the AI:**
- **PRD or product brief** — What does this product do? Who is it for?
- **Design system** — Colors, typography, components. Screenshot, tokens, or Figma link.
- **User research** — Key quotes, behaviors, pain points.
- **Constraints** — What must be included? What must be avoided?

**The principle:** The more context you give, the more aligned the output. Generic prompts produce generic products.

**Instructor script:**

> "Context layering: feed the AI everything it needs to build what you mean. PRD, design system, user research, constraints. Generic prompt, generic output. Specific context, specific output."

**Slide 4: Context for Existing Products — "Clone Your Product"**

**The difference:**
- **Generic:** "Build me a settings page." → Standalone, could be any product.
- **Contextual:** "Build me a settings page that matches our existing design system—here's the component library, color tokens, navigation pattern." → Looks like it *belongs*.

**For PMs on shipped products:** Stakeholders take prototypes seriously when they look like the real product. Otherwise they dismiss them as "not how our product looks."

**Carlos:** "How are you making sure the look and feel is as similar as possible to your current product?" This is the answer.

**Instructor script:**

> "Existing product: your prompts need to carry that context. Screenshot your product. Feed in design tokens. 'Match this look and feel, then add my new feature.' That's the difference between a prototype stakeholders take seriously and one they dismiss."

---

#### 0:22 - 0:37 | Slides 5–7: Templates, Figma, MCP & Living Prompt Packs (15 min)

**Purpose:** Deep dive on design system sources and the living prompt pack concept.

**Slide 5: Templates & Design Imports**

**Mobbin:** Real product screens. Feed a screenshot as reference. "Build me a pricing page that looks like this." Pricing, checkout, dashboards, onboarding.

**Figma:** If your design system lives in Figma, you can import it. Share the link or export components. The AI uses it as visual context.

**Screenshot-based cloning:** Screenshot your actual product. "Match this layout, colors, and navigation. Add [your new feature] on top."

**Instructor script:**

> "Mobbin for inspiration—pricing page, checkout flow. Figma if your design system is there. Or just screenshot your product. Feed it in. 'Match this, add that.' Carlos flagged this as critical—make it look like it belongs."

**Slide 6: MCP for Design Systems (Brief Demo)**

**What is MCP:** Model Context Protocol. Connects AI tools directly to external sources—Figma files, design systems, APIs.

**Demo (3 min):** Show how Lovable (or a connected tool) can pull from a Figma file. Real components, real styles. Students don't need to set this up—they need to see it's possible. "This is where the industry is heading."

**Instructor script:**

> "MCP: AI tools connecting directly to Figma, design systems, databases. Brief demo—you don't need to set this up today. But you should know it exists. In 12 months, this will be standard."

**Slide 7: Living Prompt Packs**

**Concept:** A collection of reusable, evolving prompt templates that encode your product context. NOT a static document—a dynamic toolkit.

**What goes in:**
- Product context block (paste at the start of every prompt)
- Design system reference (screenshot or link)
- Constraint templates ("Always do X. Never do Y.")
- Output templates ("Build me a [component] with [features]")

**Key:** The pack evolves as you learn. What works gets added. What doesn't gets removed. It's living.

**Instructor script:**

> "Living prompt pack: reusable templates that encode your context. Product block, design reference, constraints. Not static—it evolves. Today you'll start building yours by documenting your prompt chain."

---

### Block 2: Advanced Techniques & Prompt Debugging (0:37 - 0:52)

---

#### 0:37 - 0:47 | Slides 8–9: Advanced Techniques & Prompt Debugging (10 min)

**Purpose:** Chain-of-Thought, Constraint Injection, and how to diagnose when things go wrong.

**Slide 8: Advanced Techniques (Applied to Product Work)**

**Chain-of-Thought:** For complex flows, break the prompt into steps. "First, build the header. Then, add the sidebar. Then, the main content area." The AI reasons through the structure.

**Constraint Injection:** Add guardrails explicitly. "Use only these 5 colors. No modal dialogs. Mobile-first." Prevents the AI from drifting.

**Iterative refinement:** Don't rebuild. "The header is good. Change only the sidebar—simplify to 4 nav items." Steering, not restarting.

**Instructor script:**

> "Chain-of-Thought: break complex flows into steps. Constraint injection: spell out what you don't want. Iterative refinement: fix one section, don't rebuild. These compound."

**Slide 9: Prompt Debugging**

**When the AI builds the wrong thing:** Diagnose before re-prompting.

**Three culprits:**
1. **Missing context** — Did you give it the design system? The constraints?
2. **Conflicting constraints** — Did you say "simple" and "feature-rich" in the same prompt?
3. **Wrong tool for the job** — Some things need code editing, not re-prompting.

**The Reforge heuristic:** If you're 5+ prompts deep on the same issue, the problem isn't the tool—it's your framing. Step back. Simplify. Rephrase.

**Instructor script:**

> "When it goes wrong: missing context? Conflicting constraints? Wrong tool? If you're 5 prompts deep on the same bug, the problem is your framing. Step back. Simplify."

---

#### 0:47 - 0:52 | Slide 10: Agentic Prompting (Brief Intro) (5 min)

**Purpose:** Tease the future. "Prompt and wait" vs. "delegate and supervise."

**Concept:** Agent mode—the AI takes multi-step tasks, makes decisions, reports back. You direct like a tech lead. ZTM's "Creative Director" framing: you're not typing every command; you're giving direction.

**Keep it brief:** 2–3 minutes. Students don't need to use it now. They need to know it's coming. Future-proof for 2026–2027.

**Instructor script:**

> "Agentic prompting: delegate, don't micromanage. 'Build this feature, handle edge cases, report what you did.' The AI decides the steps. You give direction. We're moving there. For now, focus on precision in your prompts."

---

### Block 3: Hands-on Lab (0:52 - 1:32)

---

#### 0:52 - 0:57 | Slide 11: Lab Brief (5 min)

**Purpose:** Set up the lab. Clear brief, clear deliverable.

**Lab Brief (displayed + Slack):**

> **The Precision Build**
>
> You're building for a product you understand. Use a moderately detailed brief (see Appendix—or use your M2 prototype and level it up with precision).
>
> **Requirements:**
> - Document your prompt chain. Each prompt, why you wrote it that way, what it produced.
> - Use context layering: product context, design reference (Mobbin or screenshot), constraints.
> - Build with multi-step prompting. No single mega-prompt—break it into logical steps.
>
> **Deliverable:** Prototype link + prompt chain (paste in Slack or shared doc). Your partner will try to reproduce a similar result using only your prompt chain.
>
> **25 minutes to build. 15 minutes for peer review.**

---

#### 0:57 - 1:22 | Hands-on Lab: "The Precision Build" (25 min)

**Purpose:** Students build with deliberate, documented prompting. The prompt chain becomes the first artifact of their living prompt pack.

**What the instructor does:**
- Circulates. Checks that students are documenting prompts, not just building.
- If someone is stuck: "What context are you giving it? Try adding a screenshot or Mobbin reference."
- If someone is re-prompting the same thing repeatedly: "5 prompts deep? Step back. What's the real constraint you're missing?"
- At 12 min: "You should have 2–3 prompts documented. If you're only on prompt 1, you might be over-specifying. Or under-specifying. Check your context."
- At 22 min: "2 minutes. Paste your prompt chain in Slack or a doc. Share the link. Your partner will try to use it."

**Expected outcomes:**
- Students produce a more refined prototype than M1–M2
- Students have a documented prompt chain (3–6 prompts)
- Some will discover their prompts are ambiguous—partner can't reproduce. That's the learning.

---

#### 1:15 - 1:25 | Breakout Group Activity: "Prompt Chain Peer Review" (10 min)

**Purpose:** Students swap prompt chains. Can another person reproduce a similar result using only the prompt chain? Tests portability and clarity.

**How it works:**
- Breakout rooms. "How many per room? Press the button."
- Person A shares their prompt chain + prototype link. Person B reads the chain, tries to understand it. Can they see how each prompt led to the output?
- Person B attempts to use Person A's first prompt (or a similar one) in their own Lovable project. Do they get something comparable?
- Switch roles. Repeat.

**Feedback questions:**
- Was the prompt chain clear? What was missing?
- Could you reproduce a similar result? If not, why?
- What would make this a "living" prompt pack—reusable across projects?

**Instructor script:**

> "The test: can someone else use your prompt chain and get something similar? If not, your prompts aren't portable yet. That's the bar for a living prompt pack."

---

### Block 4: Full-Class Share + Break It (1:25 - 1:52)

---

#### 1:25 - 1:32 | Quick Share: "What Made Your Prompts Work?" (7 min)

**Format:** Full-class discussion.

> "Popcorn. One insight: What made your prompts work? Or what didn't work—and what did you change?"

Take 4–5 responses. Synthesize: "Portability is the test. If your prompt chain only works for you, it's not a pack yet. Add context. Add constraints. Make it reusable."

---

#### 1:32 - 1:45 | "Break It" Exercise: Live Prompt Debugging (13 min)

**What we're trying to break:** The assumption that "more prompts = better result." Sometimes the problem is the prompt. Sometimes it's the framing. Sometimes it's the tool.

**How it works:**

Instructor takes a student's prototype that went off-rails (ask for a volunteer before class, or use a prepared example). Walk through diagnosis live:

1. **Read the prompt chain.** What did they ask for?
2. **Look at the output.** What did they get?
3. **Diagnose:** Missing context? Conflicting constraints? Wrong tool?
4. **Fix it live.** Rephrase. Add context. Or: edit the code directly.

**Instructor script:**

> "Let's debug this together. [Student] built X but got Y. Where did it go wrong? Was it the prompt? The context? The constraint? Let's fix it."

**Reflection moment (2 min):**

> "Think about your own build. Where did your prompts fail? What would you do differently? That reflection—that's the start of your living prompt pack."

---

#### 1:45 - 1:52 | Retroactive Framework: "The Precision Mindset" (7 min)

**Purpose:** Name what they did. Connect to Confidence Line.

**Key talking points:**

**1. The precision loop**
> "Context → Prompt → Output → Refine. You're not guessing anymore. You're directing. That's the precision shift."

**2. Confidence Line position**
> "You're moving right. M1–M2: ambiguity. M3: gaining clarity. You know what you want. You can communicate it. Module 4 is the graduation moment—when to stop exploring and start structuring. Extract the spec. Refactor the code."

**3. What's coming (Module 4)**
> "Next: From Vibe to Structure. The graduation moment. Living specs. Refactoring. When to commit."

---

### Block 5: Close (1:52 - 2:00)

---

#### 1:52 - 2:00 | Accountability + Wrap (8 min)

**The ask:**
> "Post your prototype + prompt chain in #builds. Caption: What made your prompts work? What would you add to your living prompt pack? Engage: look at 2 others. Could you use their prompt chain?"

**Wrap + Preview:**
> "No homework. Optional: build one more screen using only your prompt chain—test its portability. Next: Module 4. The graduation moment. When to stop exploring and start building for real. See you then."

---

## Session Summary

| Block | Time | Duration | Activity Type |
| --- | --- | --- | --- |
| Recap + Precision Shift | 0:00 - 0:03 | 3 min | Instructor talk |
| Ice Breaker: Who Said It? — Extended | 0:03 - 0:10 | 7 min | Fun start activity |
| Prompting Maturity + Context Layering | 0:10 - 0:22 | 12 min | Instructor talk |
| Templates, Figma, MCP, Living Packs | 0:22 - 0:37 | 15 min | Instructor talk |
| Advanced Techniques + Debugging | 0:37 - 0:52 | 15 min | Instructor talk |
| Lab Brief | 0:52 - 0:57 | 5 min | Instructor talk |
| Hands-on Lab: Precision Build | 0:57 - 1:22 | 25 min | **Hands-on lab** |
| Breakout: Prompt Chain Peer Review | 1:15 - 1:25 | 10 min | Breakout group activity |
| Quick Share | 1:25 - 1:32 | 7 min | Class discussion |
| Break It: Live Debugging | 1:32 - 1:45 | 13 min | Instructor demo |
| Retroactive Framework | 1:45 - 1:52 | 7 min | Instructor talk |
| Accountability + Wrap | 1:52 - 2:00 | 8 min | Slack + close |

### Time Distribution

| Category | Minutes | Percentage |
| --- | --- | --- |
| **Students building** | 25 min | 21% |
| **Breakout / peer review** | 10 min | 8% |
| **Instructor teaching** | 52 min | 43% |
| **Class discussion / Break It** | 20 min | 17% |
| **Wrap** | 8 min | 7% |
| **Total hands-on (building + breakout)** | **35 min** | **29%** |

---

## Key Materials Needed

### Prepared Before Class

1. **Context layering slides** — Maturity curve, clone-your-product, templates
2. **MCP demo** — Figma connection or similar (if available). Have backup slide if demo fails.
3. **Moderately detailed product brief** — See Appendix
4. **Volunteer or prepared "broken" prototype** — For live debugging in Break It
5. **Lab brief** ready to paste in Slack
6. **Mobbin tab open** — Pre-selected templates

### Student Requirements

- Modules 1–2 complete
- Lovable Pro account
- Slack access
- Optional: Figma file or design system link (for students building for real products)

---

## Appendix: Product Briefs for Precision Build

### Brief A: SaaS Settings Page
> Build a settings page for a B2B SaaS product. The product has a dark sidebar navigation (like Linear), a white main content area, and uses a blue accent (#2563eb). The settings page should have 4 sections: Profile, Notifications, Billing, and Security. Each section has a heading and 3–5 configurable items. Use a Mobbin screenshot of a similar settings page as reference, or describe the layout precisely. Document every prompt you use. Build in 3–4 logical steps (e.g., layout first, then sections, then interactions).

### Brief B: Onboarding Flow (3 Screens)
> Build a 3-screen onboarding flow for a fitness app. Screen 1: Welcome + "Get Started" CTA. Screen 2: Select goals (3 options: Lose weight, Build muscle, Stay active). Screen 3: Summary + "Complete" button. Match a Strava or similar fitness app aesthetic (bold typography, green/accent colors). Document your prompt chain. Use context layering—what does the user need to know at each step?

### Brief C: Your M2 Prototype — Level Up with Precision
> Take your best prototype from Module 2. Rebuild it with precision prompting. Document your prompt chain. Use a Mobbin template or screenshot of your real product as reference. Add 2–3 constraints you didn't have before. The goal: same product, but built with a portable prompt chain someone else could use.
