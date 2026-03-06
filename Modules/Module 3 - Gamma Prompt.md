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

Your M2 build has real data, real user quotes, a design reference, and a real hypothesis. That's a huge leap from M1. But if you showed it to your VP right now, they'd say: "This tests the right thing, but it's only 3 screens. Where's the full flow? What happens when things go wrong?"

Today's flow:
1. **Demo** — What precision looks like
2. **Diagnose** — How does your M2 build hold up?
3. **The Precision Toolkit** — Prompt chain anatomy, multi-step prompting, living prompt packs
4. **Lab** — Expand your M2 build with a 3-prompt chain
5. **Peer Review** — Can someone else follow your prompt chain?

---

## Slide 3 — Instructor Demo: The Setup
**Remember This? Would Your VP Present It?**

INSTRUCTOR DEMO

The M2 prototype: Retention Engine onboarding flow.

- Real data, real user quotes, design-matched to Asana
- Named hypothesis: "Surface team invites during first-run onboarding"
- 3-screen onboarding flow

What's still missing?
- Only 3 screens — where's the team workspace after they invite? Where's the PM dashboard to track if it's working?
- No loading states, no error handling — what happens when things go wrong?
- Built with one big prompt — could someone else reproduce this?

*Speaker Notes: Pull up the actual M2 Retention Engine prototype you built live in Module 2. It already has the design match and real data — that's M2's work. Ask: "Would your VP present this to the board?" Pause. The answer is "almost" — it tests the right thing and looks right, but it's incomplete. Name the three gaps: not enough screens, no states, not reproducible. Keep it to 2 minutes.*

---

## Slide 4 — Live Build: 3 Prompts
**The Precision Chain**

**Prompt 1 — Expand:** Attach 2 screenshots: Asana team view + Intercom reporting dashboard. "Add a 4th screen: after the user invites teammates, show a team workspace with shared tasks and a 'Your team is set up' confirmation — match the attached Asana screenshot. Add a 5th screen: an internal PM dashboard showing Day-3 invite rate, retention with vs without invite, and churn trend — match the attached Intercom dashboard screenshot. Navigation between all 5 screens."

**Prompt 2 — States:** "Add loading skeletons for the onboarding flow. Error state for failed invites: 'Couldn't send invite — check the email.' Empty state for the team workspace: 'Waiting for teammates to join.' Same design language throughout."

**Prompt 3 — Refine:** "The PM dashboard needs to be more actionable. Add a 'Send nudge email' button next to at-risk accounts. Make the churn trend chart show weekly breakdown on hover. Don't change anything else."

3 prompts. 5 screens. States. And an iteration without rebuilding.

*Speaker Notes: Run the 3 prompts sequentially — pre-type each one so you paste instantly. Prompt 1: paste with 2 Mobbin screenshots attached (Asana team view for Screen 4, Intercom reporting dashboard for Screen 5), wait ~40 sec, click through the new screens. "We went from 3 to 5 — and there's a PM dashboard the VP can actually use." Prompt 2: paste, wait ~40 sec, show the loading skeleton and error state. "Now it behaves like a real product." Prompt 3: paste, wait ~40 sec. "Notice I didn't rebuild anything. I refined ONE screen. Steering, not restarting. That's precision." Don't linger — 5 minutes total. The students will do it themselves.*

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

## Slide 8 — Anatomy of a Prompt Chain
**Why Chains Beat Mega-Prompts**

In M2, you put everything into one prompt. It worked — but the AI had to solve layout, data, design, and flow all at once. Things get lost.

A prompt chain uses **3 different types of prompts in sequence:**

| Step | Prompt Type | What it does | Example |
|---|---|---|---|
| 1 | **Expand** | Add new screens, extend the flow | "Add a dashboard and a detail view. Navigation between all screens." |
| 2 | **Behavior** | Add states and interactions | "Loading skeletons. Error messages. Empty states." |
| 3 | **Refine** | Steer one thing, don't rebuild | "Make the chart interactive. Don't change anything else." |

Each prompt type does a different job. You're not splitting one big prompt into 3 parts — you're using different **kinds** of prompts in sequence. The AI focuses on one thing at a time. Precision accumulates.

*Speaker Notes: Connect this directly to the demo they just watched. "Remember the 3 prompts I ran? Prompt 1 was an Expand prompt — I added screens. Prompt 2 was a Behavior prompt — I added states. Prompt 3 was a Refine prompt — I changed one screen. Three different kinds of prompts. That's the structure you'll use in the lab."*

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

Your prompt chain from today becomes the first entry in your Prompt Library (Deliverable #4). Build it in the **Living Prompt Pack Builder** — it evolves as you learn.

**Remember skills from M1?** What you're building here IS a skill file. In M1, you learned that AI tools can import pre-made skills from marketplaces. Now you're creating your own. Your Living Prompt Pack is a skill that any AI tool can use — and that anyone on your team can import. By M6, this pack will be a portable, shareable asset you take with you.

*Speaker Notes: Connect back to M1's skills slide: "In Module 1, I showed you that AI tools can import skills — pre-made instruction sets. What you're building right now in the Living Prompt Pack Builder is exactly that. It's YOUR skill file. When you export it as markdown, any AI tool that supports skills can import it. Your teammates can use it. Future you on a different project can use it. The prompt chain you write today is the first entry — it grows through M4, M5, and M6."*

---

## Slide 11 — Lab Part 1: Assess and Plan
**Hands-on Lab Part 1: Prepare** | 8 Minutes

Do NOT open Lovable yet. Open the **Prompt Chain Planner** and plan your chain first.

**Step 1 (3 min):** Fill in the M2 Audit in the Planner. How many screens? Any states? Reproducible?

**Step 2 (3 min):** Write your 3-prompt chain in the Planner's color-coded cards:
- Prompt 1 (Expand) — what 1-2 screens would make this a complete flow?
- Prompt 2 (Behavior) — loading skeletons, error messages, empty states
- Prompt 3 (Refine) — pick one screen that needs iteration, steer it without rebuilding

**Step 3 (2 min):** Read each prompt aloud. If you can't explain what each step does, you're not ready.

*Speaker Notes: Drop the Prompt Chain Planner link in Slack now. Walk the room. Check that everyone has the Planner open with the audit filled in and all 3 prompt cards written — not in their head, in the tool. "If your chain isn't in the Planner, you're not ready for the build yet." Common issue: students want to START OVER instead of expanding their M2. Redirect them: "Your M2 work is your foundation. Don't rebuild — expand." This 8 minutes of planning IS the difference between M2 and M3.*

---

## Slide 12 — Lab Part 2: The Precision Build
**Hands-on Lab Part 2: Build** | 22 Minutes

Start from your M2 prototype. Copy each prompt from the **Prompt Chain Planner** into Lovable, one at a time. Document results back in the Planner.

**Prompt 1 — Expand:** "Add a [detail view / dashboard / secondary screen] to this prototype. When a user clicks [X], show [specific content]. Include navigation back to the main view. Keep the existing design language."

**Prompt 2 — States:** "Add a loading state with skeleton screens for [specific section]. Add an empty state for [scenario]: '[helpful message]'. Add an error state for [failure case]: '[error message]'. Same design language throughout."

**Prompt 3 — Refine:** "The [specific screen] needs [specific change]. [Add/move/resize a component]. Don't change anything else." Steer one thing. Don't rebuild.

**Document each result** in the Planner's "What did this produce?" section. Then **Copy Full Chain** — this is the foundation of your Prompt Library (Deliverable #4).

*Verify your shareable link works — you're swapping prototypes next.*

*Speaker Notes: THIS IS THE WOW MOMENT — it happens in the students' hands, not yours. Walk the room as they execute. At Prompt 1: check they're expanding their M2, not rebuilding from scratch. At Prompt 2: watch for reactions when loading skeletons appear — that's usually when it clicks. "It looks like a real product now." At Prompt 3: "Notice you didn't start over. You steered one thing. That's the difference." After 20 min: "Stop. Click through your prototype from the first screen to the last." Let them navigate. Let them see the multi-screen flow and the states. Don't narrate it — let the experience speak. At 22 min: "Document your last prompt. Make sure your shareable link works." If someone wants to start over: "Resist the urge. Expand what you have. That's precision."*

---

## Slide 13 — Peer Review: Prompt Chain Portability
**Breakout Group Activity: Can You Follow My Chain?** | 10 Minutes

Breakout rooms. Groups of 2.

**The test:** Person A shares their documented prompt chain (from the Prompt Chain Planner) + prototype link. Person B reads the chain. Can you understand each step? Could you reproduce a similar result using only the chain?

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

**1. Prompt Chain** — You documented a 3-step chain in the Prompt Chain Planner. Each prompt targeted one aspect. Your partner followed it. That's the first entry in your Living Prompt Pack (Deliverable #4).

**2. Multi-Screen Flow** — Multiple connected screens with navigation. Not a single page.

**3. Interactive States** — Loading, empty, error. Your prototype behaves like a shipped product.

---

## Slide 18 — Accountability
**ACCOUNTABILITY** | Before We Wrap

**1. Post in #builds:** Your prototype link + your full prompt chain (copy from the Prompt Chain Planner). Caption: What made your prompts work? What would you add to your Living Prompt Pack?

**2. Engage:** Look at 2 others. Could you follow their prompt chain? Would you get a similar result?

**3. Optional challenge:** Add a 4th prompt to your chain — one screen you didn't have time to build today. Drop the before/after in Slack with the prompt that created it.

---

## Slide 19 — Module 4 Preview
**Module 4: From Vibe to Structure**

Same product. Next level.

You've built fast (M1), built smart (M2), and built precise (M3). Your prototype looks like a real product. Next: structure it.

**Module 4 — From Vibe to Structure:**
- Extract the living PRD from what you've built (Deliverable #3)
- Refactor the code — clean architecture, proper naming, separation of concerns
- Connect real infrastructure — GitHub repo and Supabase database
- The judgment call: when to stop exploring and start building for real

Module 1: Build fast.
Module 2: Build smart.
Module 3: Build precise.
Module 4: Structure it.

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
- Slide 8 — Anatomy of a Prompt Chain: the 3-column table (Expand / Behavior / Refine) is the key visual. Students will reference this during the lab.
- Slide 9 — Multi-Step Prompting: three techniques as distinct visual blocks
- Slide 12 — 3-step prompt chain as a clear, numbered workflow. Students will reference this while building. Must be scannable at a glance. This is the most-referenced slide in the module.
- Slide 16 — Three-column layout (M1 | M2 | M3). Let the visual comparison do the talking — minimal text.
- Slide 17 — Takeaways mirror slide 1's three waypoints (visual callback, same pattern as M2)
- Keep all lab slides (11, 12, 13) highly scannable — students reference these while building
