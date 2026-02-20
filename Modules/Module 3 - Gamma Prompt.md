# Gamma Prompt: Module 3 Teaching Slide Deck

**Copy everything below the line and paste it into Gamma. Use "Paste an outline" or the prompt field.**

---

## Instructions for Gamma

Create a professional slide deck for teaching a 2-hour workshop called **"Module 3: Precision Prompting — Communicating Product Intent to AI"** in a Vibe Coding certification course. The audience is senior product managers who completed Modules 1–2 — they can build fast and build smart; now they're learning to build precise. Tone: energetic, practical, technical. The deck supports live teaching, demos, and hands-on labs. Avoid corporate jargon. Use clean, modern design with clear typography and minimal text per slide.

---

## Slide 1 — Module 3 Title + The Precision Shift
**Precision Prompting**

MODULE 3 | VIBE CODING CERTIFICATION

Module 1: build fast. Module 2: build smart and commit to your scenario. Today: build precise.

**The shift:** "Build me something" becomes "build me exactly this." You've got a product. You've got a direction. Now take your M2 prototype and level it up — same product, precision execution.

---

## Slide 2 — The Prompting Maturity Curve
**The Prompting Maturity Curve**

**Exploration prompts (left):** Divergent, open. "Build me something that could help with X." Good for ambiguity.

**Execution prompts (right):** Convergent, precise. "Build me a settings page with these 4 sections, matching this design system." Good when you know what you want.

Your prompt style should match your confidence level. Today we move right.

---

## Slide 3 — Context Layering
**Context Layering** — The Core Technique

**What to feed the AI:**
- **PRD or product brief** — What does this do? Who is it for?
- **Design system** — Colors, typography, components. Screenshot, tokens, or Figma link.
- **User research** — Key quotes, behaviors, pain points.
- **Constraints** — What must be included? What must be avoided?

Generic prompt = generic output. Specific context = specific output.

---

## Slide 4 — Context for Existing Products
**"Clone Your Product"** — Context for Existing Products

**Generic:** "Build me a settings page." → Standalone, could be any product.

**Contextual:** "Build me a settings page that matches our existing design system—here's the component library, color tokens, navigation pattern." → Looks like it *belongs*.

For PMs on shipped products: stakeholders take prototypes seriously when they look like the real product.

---

## Slide 5 — Templates & Design Imports
**Templates & Design Imports**

**Mobbin** — Real product screens. Feed a screenshot as reference. "Build me a pricing page that looks like this."

**Figma** — If your design system lives in Figma, import it. Share the link or export components.

**Screenshot-based cloning** — Screenshot your actual product. "Match this layout, colors, navigation. Add [your new feature] on top."

---

## Slide 6 — MCP for Design Systems
**MCP for Design Systems**

Model Context Protocol connects AI tools directly to Figma files, design systems, APIs.

**Demo:** Lovable (or connected tool) pulling from a Figma file. Real components, real styles.

You don't need to set this up today. But you should know it exists. This is where the industry is heading.

---

## Slide 7 — Living Prompt Packs
**Living Prompt Packs**

A collection of reusable, evolving prompt templates that encode your product context. NOT static—dynamic toolkit.

**What goes in:**
- Product context block (paste at the start of every prompt)
- Design system reference (screenshot or link)
- Constraint templates ("Always X. Never Y.")
- Output templates ("Build me a [component] with [features]")

The pack evolves as you learn. Today you start building yours.

---

## Slide 8 — Advanced Techniques
**Advanced Techniques** (Applied to Product Work)

**Chain-of-Thought** — Break complex flows into steps. "First the header. Then the sidebar. Then the content."

**Constraint Injection** — Add guardrails. "Use only these 5 colors. No modals. Mobile-first."

**Iterative refinement** — Don't rebuild. "The header is good. Change only the sidebar." Steering, not restarting.

---

## Slide 9 — Prompt Debugging
**Prompt Debugging**

When the AI builds the wrong thing, diagnose before re-prompting.

**Three culprits:**
1. **Missing context** — Did you give it the design system? Constraints?
2. **Conflicting constraints** — Did you say "simple" and "feature-rich"?
3. **Wrong tool** — Some things need code editing, not re-prompting.

**The heuristic:** 5+ prompts deep on the same issue? The problem isn't the tool—it's your framing. Step back. Simplify.

---

## Slide 10 — Agentic Prompting (Brief)
**Agentic Prompting** — The Future

**"Prompt and wait"** → You type every step.

**"Delegate and supervise"** → You give direction. The AI decides the steps. Agent mode.

We're moving there. For now, focus on precision in your prompts.

---

## Slide 11 — Hands-on Lab: The Precision Build
**Hands-on Lab: Level Up Your Final Project** | 25 Minutes

Take your M2 prototype — the one you committed to — and rebuild it with precision. Same product. Same scenario. Better execution.

**Requirements:**
- Document your prompt chain. Each prompt, why you wrote it, what it produced. This becomes the foundation of your Prompt Library (Deliverable #4).
- Use context layering: product context, design reference (Mobbin or screenshot), constraints.
- Build with multi-step prompting — no single mega-prompt.
- Apply a design system. Make it look like it belongs in a real product.

**Deliverable:** Prototype link + prompt chain. Your partner will try to reproduce using only your chain.

---

## Slide 12 — Breakout Group Activity: Prompt Chain Peer Review
**Breakout Group Activity: Prompt Chain Peer Review** | 10 Minutes

Person A shares prompt chain + prototype. Person B: Can you reproduce a similar result using only the chain?

**Feedback questions:**
- Was the prompt chain clear? What was missing?
- Could you reproduce? If not, why?
- What would make this reusable across projects?

The test: Can someone else use your prompt chain? If not, it's not portable yet.

**Format:** Breakout rooms. "How many per room? Press the button."

---

## Slide 13 — What Made Your Prompts Work?
**What Made Your Prompts Work?** — Full-class discussion

One insight: What made your prompts work? Or what didn't—and what did you change?

Portability is the test. If your prompt chain only works for you, it's not a pack yet.

---

## Slide 14 — "Break It" Exercise: Live Prompt Debugging
**"Break It" Exercise** — Live Prompt Debugging

**What we're breaking:** The assumption that more prompts = better result.

**Process:** Take a prototype that went off-rails. Diagnose live:
1. Read the prompt chain. What did they ask for?
2. Look at the output. What did they get?
3. Diagnose: Missing context? Conflicting constraints? Wrong tool?
4. Fix it live. Rephrase. Add context. Or edit the code directly.

---

## Slide 15 — Reflection Moment
**Reflection Moment**

Think about your own build. Where did your prompts fail? What would you do differently?

That reflection—that's the start of your living prompt pack.

---

## Slide 16 — The Precision Loop
**The Precision Loop**

**Context → Prompt → Output → Refine**

You're not guessing anymore. You're directing. That's the precision shift.

---

## Slide 17 — Confidence Line + What's Next
**The Confidence Line**

You're moving right. M1–M2: ambiguity. M3: gaining clarity. You know what you want. You can communicate it.

**Next: Module 4** — From Vibe to Structure. The graduation moment. Living specs. Refactoring. When to commit.

---

## Slide 18 — Accountability: Before We Wrap
**ACCOUNTABILITY** | Before We Wrap

**Post your prototype + prompt chain** in #builds. Caption: What made your prompts work? What would you add to your living prompt pack?

**Engage** — Look at 2 others. Could you use their prompt chain?

---

## Slide 19 — Wrap + Preview
**Wrap + Preview**

**No Homework** — Optional: build one more screen of your project using only your prompt chain — test its portability.

**Next: Module 4** — You take the prototype you've been building and graduate it. Extract the living PRD (Deliverable #3). Refactor the code. Get it structured for real. That's the midpoint of your final project.

See you then.

---

## Slide 20 — What You Accomplished Today
**What You Accomplished Today**

- **Leveled up your final project** — Same product from M2, rebuilt with precision
- **Context layering** — PRD, design system, constraints
- **Clone-your-product** — Screenshots, Mobbin, Figma
- **Documented prompt chain** — First artifact of your Prompt Library (Deliverable #4)
- **Prompt debugging** — Diagnose before re-prompting

Your final project is three modules in. M1: explored. M2: committed. M3: precision-built.

---

## Slide 21 — The Journey Continues
**The Journey Continues**

Module 1: Build fast.  
Module 2: Build smart.  
Module 3: Build precise.  
Module 4: Build for real.

From "I don't know what to build" to "I know exactly what to build and how to direct the AI."

Next up: The graduation moment.

---

## Design Notes for Gamma
- Use a consistent, modern template (match Modules 1–2 if part of a series)
- Keep slides readable from the back of a room — large text, high contrast
- Slide 1 — "Precision Prompting" as the hook
- Slides 3–5 — Context layering (core technique; clear, scannable)
- Slide 6 — MCP demo (visual if possible)
- Slide 14 — "Break It" live debugging (interactive concept)
- Slides 20–21 — Celebratory close, bridge to Module 4
