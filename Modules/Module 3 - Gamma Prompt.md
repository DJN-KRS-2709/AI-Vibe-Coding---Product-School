# Gamma Prompt: Module 3 Teaching Slide Deck

**Copy everything below the line and paste it into Gamma. Use "Paste an outline" or the prompt field.**

---

## Instructions for Gamma

Create a professional slide deck for teaching a 2-hour workshop called **"Module 3: Precision Prompting — Build Me Exactly This"** in a Vibe Coding certification course. The audience is senior product managers who completed Modules 1–2 — they can build fast (M1) and build smart with data and hypotheses (M2); now they're learning to build precise. Tone: energetic, practical, technical. The deck supports live teaching, demos, and hands-on labs. Avoid corporate jargon. Use clean, modern design with clear typography and minimal text per slide. Match Modules 1–2 visual style. Important: the slides are student-facing — keep the content instructional and practical. Do not telegraph emotional beats or name "wow moments" on slides.

---

## Slide 1 — Module 3 Title + 3 Waypoints
**Precision Prompting — Build Me Exactly This**

MODULE 3 | VIBE CODING CERTIFICATION

Three things today:
1. **Prompt Chain** — Not one big prompt. A documented sequence, step by step, that someone else can follow.
2. **Multi-Screen Flow** — Not a single page. Connected screens with navigation.
3. **Interactive States** — Loading, empty, error. Your prototype behaves like a real product.

Module 1 was speed. Module 2 was aim. Module 3 is precision.

*Speaker Notes: "Welcome back. M1 was speed — you proved you can build. M2 was aim — you proved you can build something that tests a real question. Today is precision. Same product, dramatically better execution. Three waypoints: prompt chain, multi-screen flow, interactive states. By the end of today, your prototype won't just test something — it'll look like your VP could ship it tomorrow."*

---

## Slide 2 — Bridge from M2 + Agenda
**Your M2 Prototype Proves Something. Would Your VP Ship It?**

Your M2 build has real data, real user quotes, a real hypothesis. That's a huge leap from M1. But if you showed it to your VP right now, they'd say: "Cool, but this doesn't look like our product."

Today's flow:
1. **Demo** — What precision looks like
2. **Diagnose** — How does your M2 build hold up?
3. **The Precision Toolkit** — Design systems, prompt chains, context layering
4. **Lab** — Build a multi-screen product flow with a 5-prompt chain
5. **Peer Review** — Can someone else follow your prompt chain?

---

## Slide 3 — Instructor Demo: The Setup
**Remember This? Would Your VP Present It?**

INSTRUCTOR DEMO

The M2 prototype: Retention Engine onboarding flow.

- Day-3 invite rate: 12%
- Retention with invite: 68% vs 22% without
- 3-screen onboarding flow with real user quotes and a named hypothesis

What's missing?
- Doesn't match your product — generic styling
- No loading states, no error handling
- No internal view for the PM team to track results

*Speaker Notes: Pull up the actual M2 Retention Engine prototype you built live in Module 2. Let the room look at it. Ask: "Would your VP present this to the board?" Pause. Let the silence do the work. Then walk through the three gaps. This sets up the demo — students need to feel the gap before you show the fix. Keep it to 2 minutes.*

---

## Slide 4 — Live Build: 3 Prompts
**The Precision Chain**

**Prompt 1 — Design:** "Rebuild this onboarding flow to match this design system [Mobbin screenshot of Linear]. Keep the invite-first flow and all the metrics. Match the card layout, typography, and navigation."

**Prompt 2 — Screens:** "Add a team workspace screen after the user invites teammates. Add an internal PM dashboard showing Day-3 invite rate, retention, and churn trend. Navigation between all screens."

**Prompt 3 — States:** "Add loading skeletons. Error state for failed invites. Empty state for the team workspace. Same design language throughout."

3 prompts. 5 screens. Matched to Linear. With states.

*Speaker Notes: Run the 3 prompts sequentially in Lovable — pre-type each one in a separate tab so you paste instantly. Prompt 1: paste, wait ~40 sec, let the design transform land. "Same content, looks like Linear now." Prompt 2: paste, wait ~40 sec, click through the new screens. "We went from 3 screens to 5 — and there's a PM dashboard now." Prompt 3: paste, wait ~40 sec, show the loading skeleton and error state. "It behaves like a real product." Don't linger — this is a teaser. 5 minutes total. The students will do it themselves and that's where the real moment lives.*

---

## Slide 5 — Demo Debrief
**What Changed**

Same tool. Same data.

- **Prompt chain** — 3 prompts, each targeting one thing. Not one mega-prompt.
- **Multi-screen flow** — from 3 screens to 5, with navigation and an internal dashboard
- **Interactive states** — loading, empty, error

Three prompts. Each one built on the last. That's precision prompting.

*Speaker Notes: Quick debrief — name the three things that changed. Don't oversell it. "You'll do this to your own build in 20 minutes. But first, let's see where your M2 prototype actually stands." Transition to the mini activity.*

---

## Slide 6 — Mini Activity: Assess Your M2 Build
**Pull Up Your M2 Prototype**

INDIVIDUAL EXERCISE | 5 MINUTES

Open your M2 prototype. Answer three questions:

**1.** Does this look like it belongs in your product? Or does it look AI-generated?

**2.** How many screens does it have?

**3.** What happens when the data is loading? When there's an error? When there's no data yet?

**Post in Slack:** Your M2 link + your answers.

*Speaker Notes: This should be slightly uncomfortable. Most students will realize their M2 build is 1-2 screens, generic styling, no states. That's the point — it surfaces the gap the lab will close. After 5 minutes, do a quick hand-check: "Who has more than 2 screens? Who has loading states? Who would show this to their VP right now?" The honest answers create the motivation for the teaching and lab ahead. Transition: "Now I'll give you the toolkit to fix all three."*

---

## Slide 7 — The Prompting Maturity Curve
**The Prompting Maturity Curve**

Your prompt style should match your confidence level.

**Exploration prompts (M1–M2):** Divergent, open. "Build me something that could help with X." Good for ambiguity. Good for discovering what to test.

**Execution prompts (M3+):** Convergent, precise. "Build me a settings page with these 4 sections, matching this design system, with loading states and navigation." Good when you know what you want.

M1–M2 lived on the left. Today you move right.

---

## Slide 8 — Context Layering: The Core Technique
**Context Layering** — Feed the AI Everything It Needs

Generic prompt = generic output. Layered context = your product.

**What to feed:**
- **Product brief** — What does this do? Who is it for?
- **Design system** — Colors, typography, components. Screenshot, tokens, or Figma link.
- **User research** — Key quotes, behaviors, pain points (you already have these from M2).
- **Constraints** — What must be included? What must be avoided?

**The "clone your product" technique:** Screenshot your actual product. "Match this layout, colors, navigation. Add my new feature on top." Stakeholders take prototypes seriously when they look like the real product.

MCP (Model Context Protocol) connects AI tools directly to Figma files and design systems. You don't need to set this up today — but know it exists.

---

## Slide 9 — Multi-Step Prompting
**Multi-Step Prompting** — No More Mega-Prompts

In M2, you assembled one big prompt. Today you build a chain. Each prompt targets ONE aspect.

**Chain-of-Thought:** Break complex flows into steps. "First the layout. Then the feature. Then the states. Then the second screen." The AI reasons through the structure.

**Constraint Injection:** Add guardrails explicitly. "Use only these 5 colors. No modals. Mobile-first. Match the sidebar pattern from the screenshot."

**Iterative Refinement:** Don't rebuild. "The dashboard is good. Change only the detail view — simplify to 3 sections." Steering, not restarting.

The prompt chain becomes an artifact. If someone else can follow your chain and get a similar result, you've built something portable.

---

## Slide 10 — Living Prompt Packs
**Living Prompt Packs** — Your Reusable Toolkit

A collection of evolving prompt templates that encode your product context. NOT static — dynamic and growing.

**What goes in:**
- Product context block (paste at the start of every prompt)
- Design system reference (screenshot or Figma link)
- Constraint templates ("Always do X. Never do Y.")
- Output templates ("Build me a [component] with [features] matching [design system]")

Your prompt chain from today becomes the first entry in your Prompt Library (Deliverable #4). It evolves as you learn.

---

## Slide 11 — Lab Part 1: Prepare Your Precision Inputs
**Hands-on Lab Part 1: Prepare** | 8 Minutes

Do NOT open Lovable yet. Prepare the ammunition.

**Step 1 (3 min):** Capture your design system reference.
- Option A: Screenshot your company's actual product (if working on real problem)
- Option B: Find a Mobbin reference matching your scenario's product type (PM tool, CRM, marketplace, dashboard)
- Option C: Export Figma components if you have them

**Step 2 (3 min):** Plan your 5-step prompt chain on paper or in a doc.
- Prompt 1: Structure + design match
- Prompt 2: Feature from your M2 hypothesis
- Prompt 3: Real data injection (metrics + quotes from M2)
- Prompt 4: Interactive states (loading, empty, error)
- Prompt 5: Second screen + navigation

**Step 3 (2 min):** Gather your M2 materials — pull up your M2 hypothesis, data pack quotes, and metrics.

*Speaker Notes: Walk the room. Check that everyone has a design system reference — if they don't have a Mobbin screenshot yet, help them find one. Check that their 5-step plan is written down, not just in their head. "If you don't have a screenshot and a plan on paper, you're not ready for the build yet." This 8 minutes of prep IS the difference between M2 and M3.*

---

## Slide 12 — Lab Part 2: The Precision Build
**Hands-on Lab Part 2: Build** | 22 Minutes

Execute your chain step by step. Document every prompt.

**Prompt 1 — Structure:** Open Lovable. Attach your design system screenshot. "Build a [dashboard/flow] with this layout: [sidebar/header/main content]. Match this design system."

**Prompt 2 — Feature:** "Add [your M2 hypothesis feature]. Keep the design system. Include these sections: [specific sections from your M2 build]."

**Prompt 3 — Data:** "Display these real metrics: [paste 3-5 numbers from your M2 data pack]. Show these user quotes as feedback cards: [paste 2-3 quotes]."

**Prompt 4 — States:** "Add a loading state with skeleton screens. Add an empty state for new users with an onboarding message. Add an error state. Same design language throughout."

**Prompt 5 — Second Screen:** "Add a detail view when a user clicks [X]. Include navigation back to the main view. Show [specific data] on this screen."

**Document each prompt** — what you wrote, why, and what it produced. This is the foundation of your Prompt Library (Deliverable #4).

*Verify your shareable link works — you're swapping prototypes next.*

*Speaker Notes: THIS IS THE WOW MOMENT — it happens in the students' hands, not yours. Walk the room as they execute. At prompt 1: check the design match landed. At prompt 3: watch for reactions when loading states appear — that's usually when it clicks. At prompt 5: "Stop. Click through your prototype from the first screen to the last." Let them navigate. Let them see the multi-screen flow, the data, the states. Don't narrate it — let the experience speak. At 20 min: "2 minutes. Document your last prompt. Make sure your shareable link works." If someone is stuck on prompt 2: "What context are you giving it? Try adding the screenshot again." If someone's result looks off: "That's prompt debugging — we'll cover it later. For now, steer with your next prompt, don't restart."*

---

## Slide 13 — Peer Review: Prompt Chain Portability
**Breakout Group Activity: Can You Follow My Chain?** | 10 Minutes

Breakout rooms. Groups of 2.

**The test:** Person A shares their documented prompt chain + prototype link. Person B reads the chain. Can you understand each step? Could you reproduce a similar result using only the chain?

**Feedback questions:**
- Was the prompt chain clear? What was missing?
- Could you follow the logic from prompt to prompt?
- What would make this reusable across projects — not just for this scenario?

If your partner can't follow your chain, it's not portable yet.

*Speaker Notes: The portability test is the second wow beat — when students see their partner get a similar result from just reading their chain, it validates that the chain itself is the artifact, not just the prototype. Enforce the structure: Person A shares chain + link, Person B reads the chain and evaluates. Then switch. "If your partner gets lost at step 3, your chain is missing context at step 3."*

---

## Slide 14 — Quick Share
**What Made Your Prompts Work?**

One insight: What made your prompts work? Or what didn't — and what did you change?

If your prompt chain only works for you, it's not a pack yet.

---

## Slide 15 — Break It: Prompt Debugging
**"Break It" Exercise** — Prompt Debugging

When a prompt chain goes off-rails, diagnose before re-prompting:

1. **Read the chain.** What did you ask for at each step?
2. **Compare the output.** What did you get? Where did it diverge?
3. **Diagnose:** Missing context? Conflicting constraints? Wrong tool?
4. **Fix it.** Rephrase one prompt. Add a constraint. Or edit the code directly.

If you're 5+ prompts deep on the same issue, the problem isn't the tool — it's your framing.

*Speaker Notes: Use a volunteer's prototype that went off-rails, or a prepared example. Walk through the diagnosis live with the class. Ask the room: "Where did it diverge? Prompt 2 or prompt 3?" Let students diagnose before you do. Fix ONE prompt live and show the improvement. 10 minutes total.*

---

## Slide 16 — Pull Up All Three
**M1. M2. M3. Side by Side.**

Open three tabs.

**Module 1:** Your first build. One prompt, one page.

**Module 2:** Your validation build. Real data, real hypothesis, real user quotes.

**Module 3:** Your precision build. Design-matched. Multiple screens. States. Documented chain.

Same tool. Same you.

*Speaker Notes: This is the third wow beat — the visual payoff. Have students open all three tabs themselves. Don't describe it. Let the three-tab comparison do the talking. Give it 30 seconds of silence while people look. Then: "Same tool. Same you. That's three modules of progression." This is the image they take home.*

---

## Slide 17 — What You Did Today
**What You Did Today**

**1. Prompt Chain** — You documented a 5-step chain. Each prompt targeted one aspect. Your partner could follow it. That's the first entry in your Prompt Library (Deliverable #4).

**2. Multi-Screen Flow** — Multiple connected screens with navigation. Not a single page.

**3. Interactive States** — Loading, empty, error. Your prototype behaves like a shipped product.

---

## Slide 18 — Accountability
**ACCOUNTABILITY** | Before We Wrap

**1. Post in #builds:** Your prototype link + your full prompt chain. Caption: What made your prompts work? What would you add to your living prompt pack?

**2. Engage:** Look at 2 others. Could you follow their prompt chain? Would you get a similar result?

**3. Optional challenge:** Take your company's real product screenshot and design system. Rebuild your M3 prototype to match. Drop the before/after in Slack.

---

## Slide 19 — Module 4 Preview
**Module 4: From Vibe to Structure**

Same product. Next level.

You've built fast (M1), built smart (M2), and built precise (M3). Your prototype looks like a real product. Next: graduate it.

**Module 4 — The Graduation Moment:**
- Extract the living PRD from what you've built (Deliverable #3)
- Refactor the code — clean architecture, proper naming, separation of concerns
- The judgment call: when to stop exploring and start building for real

Module 1: Build fast.
Module 2: Build smart.
Module 3: Build precise.
Module 4: Build for real.

---

## Slide 20 — Survey
**Your Opinion Matters To Us**

Scan the QR code or use the link to share your feedback. Your insights help us improve each cohort.

---

## Design Notes for Gamma
- Match Modules 1–2 visual template exactly (same fonts, colors, layout grid)
- Slides are student-facing course material — keep content clean, instructional, and practical. Do NOT put pedagogical commentary, emotional cues, or "wow moment" labels on slides. The experience should speak for itself.
- Slide 1 — Bold title, three waypoints as prominent numbered list (same pattern as M2 slide 1)
- Slide 3 — Large question, minimal clutter. This is a conversation starter, not a lecture slide.
- Slide 4 — Show the 3 prompts cleanly. Students should be able to read the prompt text and see the progression.
- Slide 6 — Three numbered questions, prominent and scannable from the back of the room
- Slide 8 — Context Layering: four inputs as a visual stack or card grid
- Slide 9 — Multi-Step Prompting: three techniques as distinct visual blocks
- Slide 12 — 5-step prompt chain as a clear, numbered workflow. Students will reference this while building. Must be scannable at a glance. This is the most-referenced slide in the module.
- Slide 16 — Three-column layout (M1 | M2 | M3). Let the visual comparison do the talking — minimal text.
- Slide 17 — Takeaways mirror slide 1's three waypoints (visual callback, same pattern as M2)
- Keep all lab slides (11, 12, 13) highly scannable — students reference these while building
