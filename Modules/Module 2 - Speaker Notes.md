# Module 2: Sharpen Intent with Strategic Prototypes — Speaker Notes

Casual talking points for each slide. Not a script — just the key things to say, what to do on screen, and the energy to bring. Module 2 is the bridge from speed to direction. The vibe shifts from "build fast" to "build smart." Real examples from companies like Airbnb, Amazon, Netflix, and Dropbox to ground every concept.

**Tools referenced in this module:**
- Lovable (building)
- Structured Prompt Builder (ChatGPT/Claude — assembling prompts)
- Validation Brief (template — hypothesis, risk type, kill switch)
- Context Data Pack (scenario-specific user quotes, metrics, problem brief)
- Visual Reference Guide / Mobbin (screenshot references)

**What to prepare before class:**
- [ ] Have the polished M1 prototype loaded in Lovable (Mobbin-matched, interactive components, but all placeholder data)
- [ ] Have the context-injected version pre-built in a separate Lovable project (same concept rebuilt with real retention data, real user quotes, hypothesis embedded) — deliver as if live but have it ready as backup
- [ ] The context injection prompt pre-typed in a text file, ready to paste (see Slide 6 demo script below for exact prompt)
- [ ] Both Lovable projects open in separate browser tabs for side-by-side comparison
- [ ] Context Data Packs for all 4 scenarios + Bring Your Own template posted to Slack
- [ ] Validation Brief template ready to drop in Slack
- [ ] Structured Prompt Builder link ready
- [ ] Mobbin tab open with pre-selected examples for each scenario
- [ ] Lab guide and exercise document links ready in Slack
- [ ] Screen share on

---

## Slide 1 — Title

Welcome back to Module 2 — Sharpen Intent with Strategic Prototypes.

Last session was fireworks — you built functional prototypes from scratch, got feedback, refined them, and saw how fast you can go from idea to working software. That was Module 1. Speed.

Today the question changes. You can build fast — but are you building the *right thing*? Speed without direction is a liability. Today we add the direction.


## Slide 2 — Class Expectations

Same ground rules as Module 1. Cameras on — I know, I know, but it genuinely makes a difference. Be present, arrive on time, participate actively during exercises. Use Slack for all communication. And save deeper questions for after class so we keep the flow going.

One thing I'll add for today: you're going to be doing more individual work than M1. When I say "don't open Lovable yet" — trust the process. The preparation is what makes the build dramatically better. You'll see.


## Slide 3 — Syllabus

Quick refresher on where we are in the course. Six modules across three weeks — two sessions per week.

Module 1 was speed — you activated the build cycle and proved you can go from nothing to a working prototype.

Module 2 — that's today — is about sharpening your intent. You're going to learn to build prototypes that prove something, not just look like something. Think about how Airbnb started: their first prototype was literally three air mattresses on a floor and a basic website. The idea wasn't the mattresses — it was testing whether strangers would actually pay to sleep in someone else's home. That's a hypothesis-driven prototype. That's Module 2 thinking.

Module 3 is precision — context engineering, prompt chains, building exactly what you describe.

Module 4 translates your prototype into production specs — Living PRDs, clean code structure, and the engineering handoff.

Module 5 makes it real — databases, auth, edge cases, and you deploy it. Live URL. Real users. Your prototype becomes a working product.

And Module 6 — you measure, learn, and iterate. Analytics, AI-powered analysis, and a data-driven improvement cycle. You close the loop from idea to evidence.


## Slide 4 — Agenda

Three things today.

First — how to build smarter, not just faster. I'll show you what happens when you add real context to your builds.

Second — the Prototype Validation Lens. A simple framework that turns every prototype into a hypothesis test instead of a demo.

Third — hands-on lab. You'll start your final project. Not a throwaway exercise — the prototype you build today is the one you'll carry through Modules 3, 4, 5, and 6 all the way to deployment. Choose wisely.


## Slide 5 — Chapter Break: How to Build Smarter, Not Just Faster

This kicks off the first major block. Let's talk about what separates a demo from a decision tool.


## Slide 6 — Reflection Moment: What Does Your M1 Build Prove?

**ACTION: This is interactive. Give students 3–4 minutes. Q&A comes BEFORE the demo — the discomfort has to land before the answer arrives.**

Open up your prototype from Module 1. Take a real look. I want you to answer three questions — and be honest with yourself:

One — what assumption were you actually testing? Not what you think it was retroactively. What was it *when you built it*?

Two — if your VP asked "what did you learn from this?" — what would you say?

Three — where is the real user data? Where are the metrics? Where's the user language?

Post your answers in Slack or unmute and share. This should be slightly uncomfortable. Most of you will realize your M1 build doesn't test anything specific. That's not a failure — that's M1's job. M1 proved you can build. M2 proves you can build something that matters.

**Spend ~2 minutes discussing responses. Acknowledge the gap. That gap is the lesson — and the demo immediately after closes it.**

That gap — between "looks real" and "proves something" — is exactly what we close today.


## Slide 7 — Instructor-Led Demo: What You Can Prove with Context Injection

> Instructor demo: **The Customer Vibe — Retention Engine** (B2B PM SaaS — 30% churn, team invites — carried through M2/M3/M4/M5 demos)
> Total demo time: ~8 minutes. Pre-build both versions before class.

### SETUP (before students arrive)

- [ ] Open the M1 prototype in Lovable (the polished version from M1 — Mobbin-matched design, interactive components, professional layout, but ALL placeholder data)
- [ ] Have the context-injected version pre-built in a separate Lovable project as backup
- [ ] Have the context injection prompt pre-typed in a text file, ready to paste
- [ ] Have both Lovable projects open in separate browser tabs (so you can show side-by-side at the end)
- [ ] Screen share on — students should see everything

### STEP 1: Show the Facade (~2 min)

**What you do:** Click through the M1 prototype on screen share. Show all the key screens — the onboarding flow, the dashboard, any interactive components. It looks polished — Mobbin-matched, professional layout, clickable buttons.

**What you say:** "This is the prototype from Module 1. Clean design, Mobbin-matched, interactive components — it looks like a real product. Pretty impressive for one session's work."

**Then ask the room:** "What assumption is this testing?"

**Pause. Let the silence land. Wait 5-10 seconds.**

**What you do next:** Demonstrate the facade. Point to the charts — "See these numbers? Where did they come from? Nowhere. They're hardcoded." Point to any copy in the UI — "These labels? Placeholder text. No real user data." Point to the metrics — "And these charts? Generic sample data that means nothing."

**What you say:** "If your VP asked 'what did you learn from this?' — what would you say? 'It looks nice'? That's not a product insight. That's interior design. This prototype looks like a product. But it proves nothing."

### STEP 2: Inject Context (~3 min)

**What you say:** "I'm going to rebuild this with three ingredients: a hypothesis, real data, and real user voice. Watch what changes."

**What you do:** Open Lovable (either in the same project or a new one). Paste this prompt:

> "Build a 3-screen onboarding flow for a B2B project management SaaS that prominently surfaces team invitations within the first 3 steps.
>
> Context: Company is 18 months old, Series A, 5,000 paying teams, 4.2M ARR. 30 percent of new customers churn within 90 days. The board requires measurable improvement this quarter.
>
> Data shows: Users who invite a teammate within the first 3 days retain at 68 percent. Users who do not invite retain at only 22 percent. Only 12 percent of new users send an invite in the first 3 days. The invite button is currently buried in Settings > Team > Members. 60 percent of new users never create their first task.
>
> Constraint: No engineering resources for 6 weeks. Prototype only. Must work within the existing product surface.
>
> Hypothesis: If we surface team invites prominently during first-run onboarding, day-3 invite rate increases from 12 percent to 25 percent.
>
> User insight: Retained user: 'When I invited my co-founder on Day 2, that's when it clicked. It's a team tool.' At-risk user: 'I tried to invite my team but it asked for role and department. I don't know that. I just want to add them.'
>
> Instructions: Design a 3-screen onboarding flow with the goal of increasing early team invites.
>
> Screen 1: Reframe the product as a team tool. Make the value of collaboration explicit.
> Screen 2: Make inviting teammates the primary call to action. Remove friction such as role and department requirements.
> Screen 3: Reinforce activation by showing how collaboration unlocks value — shared tasks, comments, progress visibility.
>
> Design principles: Make the invite action feel lightweight and immediate. Do not add new backend functionality. Assume the invite system already exists. Reduce cognitive load. Make the team invite feel like the default next step.
>
> Include: Clear headline and microcopy. Primary and secondary CTAs. Minimal UI elements. Simple visual hierarchy.
>
> Display these metrics visually within the prototype to anchor urgency: Day-3 invite rate: 12 percent. 90-day retention with invite: 68 percent. 90-day retention without invite: 22 percent. 90-day churn overall: 30 percent. Target: reduce churn to 15 percent.
>
> After the 3 screens, include: The single riskiest assumption behind this intervention. A lightweight experiment plan to validate it within 2 weeks. Success criteria and leading indicator metrics.
>
> Output format: Clickable web onboarding prototype with 3 distinct screens plus experiment summary."

**While it generates:** "Watch the difference. Same tool. Same time. But this prompt has a hypothesis, real retention data, a named constraint, and actual user quotes baked in."

**When it's done:** Click through the three onboarding screens and the experiment summary.

### STEP 3: Name the Difference (~2 min)

**What you do:** Open both versions in separate tabs. Click between them — or put them side-by-side if your screen allows it.

**Point to the M1 version:** "This one — placeholder data, hardcoded charts, generic copy. It looks like a product. But what question does it answer? None."

**Point to the context-injected version:** "This one — 12% Day-3 invite rate displayed on screen, real user quotes from interviews, a named hypothesis about surfacing invites during onboarding. It even has an experiment plan and success criteria built in. It's testing a specific assumption: does making the invite flow prominent in onboarding change retention?"

**What you say:** "Same tool. Same amount of time. The only difference is the inputs. Three ingredients: a hypothesis, real data, and user voice."

**Then the bridge:** "The first one generates applause. The second one generates evidence. That's the shift we're making today. You're going to do exactly this to your own build — with your own scenario, your own data, and your own hypothesis."

### STEP 4: Transition (~1 min)

**What you say:** "But before you build, I want you to feel the gap in your own work. Open your M1 prototype right now. Let's see where it stands."

**Transition to Slide 7.**

### THE PROMPT (copy-paste version for your text file)

```
Build a 3-screen onboarding flow for a B2B project management SaaS that prominently surfaces team invitations within the first 3 steps.

Context: Company is 18 months old, Series A, 5,000 paying teams, 4.2M ARR. 30 percent of new customers churn within 90 days. The board requires measurable improvement this quarter.

Data shows: Users who invite a teammate within the first 3 days retain at 68 percent. Users who do not invite retain at only 22 percent. Only 12 percent of new users send an invite in the first 3 days. The invite button is currently buried in Settings > Team > Members. 60 percent of new users never create their first task.

Constraint: No engineering resources for 6 weeks. Prototype only. Must work within the existing product surface.

Hypothesis: If we surface team invites prominently during first-run onboarding, day-3 invite rate increases from 12 percent to 25 percent.

User insight: Retained user: "When I invited my co-founder on Day 2, that's when it clicked. It's a team tool." At-risk user: "I tried to invite my team but it asked for role and department. I don't know that. I just want to add them."

Instructions: Design a 3-screen onboarding flow with the goal of increasing early team invites.

Screen 1: Reframe the product as a team tool. Make the value of collaboration explicit.
Screen 2: Make inviting teammates the primary call to action. Remove friction such as role and department requirements.
Screen 3: Reinforce activation by showing how collaboration unlocks value — shared tasks, comments, progress visibility.

Design principles: Make the invite action feel lightweight and immediate. Do not add new backend functionality. Assume the invite system already exists. Reduce cognitive load. Make the team invite feel like the default next step.

Include: Clear headline and microcopy. Primary and secondary CTAs. Minimal UI elements. Simple visual hierarchy.

Display these metrics visually within the prototype to anchor urgency: Day-3 invite rate: 12 percent. 90-day retention with invite: 68 percent. 90-day retention without invite: 22 percent. 90-day churn overall: 30 percent. Target: reduce churn to 15 percent.

After the 3 screens, include: The single riskiest assumption behind this intervention. A lightweight experiment plan to validate it within 2 weeks. Success criteria and leading indicator metrics.

Output format: Clickable web onboarding prototype with 3 distinct screens plus experiment summary.
```

### WHAT TO PRE-BUILD (the night before)

1. **The M1 version (the facade):** Your existing M1 prototype — polished UI, Mobbin-matched, but all placeholder data. This should already exist from your M1 demos.

2. **The context-injected version (the payoff):** Run the prompt above in Lovable. Make sure it generates clean output with:
   - The retention data visible on screen (12% invite rate, 68% vs 22% retention split)
   - At least 1-2 user quotes displayed in the UI
   - The 3-screen onboarding flow clearly progressing: team value → invite action → collaboration payoff
   - The experiment summary with the riskiest assumption, validation plan, and success criteria
   - Metrics visually anchored (not buried in small text)

3. **Have both open in separate browser tabs** so you can switch instantly during the demo.

4. **Deliver the context-injected version as if you're building it live** — paste the prompt, let it generate. But if it fails or produces weak output, switch to the pre-built backup. Say: "Let me show you the one I built earlier with this exact prompt" and switch tabs.


## Slide 7 — Three Main Ingredients for Context Injection

Three ingredients that M1 didn't have.

**Hypothesis** — before you touch any tool, you state what you're testing. "I'm testing whether [X]." If you can't finish that sentence, you're not ready to build. Amazon does this with their "Working Backwards" process — they write the press release before building anything. The hypothesis is your press release.

**Real Data** — you replace generic placeholders with actual metrics. Not "users are churning" — "30% churn in 90 days. Users who invite a teammate in the first 3 days retain at 68%. Users who don't retain at only 22%. And only 12% of new users send an invite in the first 3 days." That specificity changes what the AI builds and what stakeholders react to.

**User Voice** — you inject the actual tone and language of your users. Not "users find it confusing" — "I tried to invite my team but it asked for role and department. I don't know that. I just want to add them." When your prototype shows that quote on screen, the conversation shifts from "nice demo" to "we need to fix this."

Same tool as M1. Same visual quality. Completely different purpose. You'll assemble all three into a single prompt today.


## Slide 9 — Chapter Break: The Prototype Validation Lens

Now let's give you the framework that makes this repeatable. The Validation Lens.


## Slide 10 — The Validation Lens Loop

Four steps. This is the cycle you'll run in every lab from now on.

**Step 1 — Identify the Hypothesis.** The "why" behind every prompt you write. Before you build anything, name the test. If you can't complete the sentence "I'm testing whether [X]," you aren't ready to build.

**Step 2 — Define the Constraints.** These are your guardrails. What's the risk type? What fidelity level do you need? What are the technical limits?

**Step 3 — Build and Stress-Test.** This is the key shift from M1. You're not building to see it work. You're building to see where it *breaks*. Netflix tested their DVD-by-mail hypothesis by literally mailing themselves DVDs before building any infrastructure. They were looking for what would fail, not what would succeed.

**Step 4 — Synthesize and Pivot.** What did you learn? Update your hypothesis. Continue or change direction.

Each revolution sharpens your hypothesis and tightens constraints. This compresses weeks of traditional development into a single session.


## Slide 11 — What's Your Kill Switch?

Your hypothesis should identify the riskiest part of the product concept. Your kill switch forces clarity about what to build and test first.

Ask yourself: "Which assumption, if wrong, kills the whole thing?"

For **0-to-1 new products** — your kill switch is usually desirability. Nobody wants it yet, so prove they will. You're testing whether the problem is real. Dropbox did this perfectly — Drew Houston didn't build the product first. He made a 3-minute demo video showing how it would work. The waitlist hit 75,000 overnight. Desirability validated before a single line of code.

For **1-to-N existing products** — your kill switch is usually adoption or flow. People have it; now prove they'll use it. You already have users, data, and a product. Screenshot what exists and build on top.

Think about your own work — are you typically in 0-to-1 or 1-to-N territory? That determines which risk you target first.


## Slide 12 — Choose Your Scenario

This is your commitment moment. The scenario you pick today is the one you'll carry through Modules 2 through 6. This becomes your final project. No switching after today.

**ACTION: Give students 3-4 minutes. Read through the options out loud briefly.**

Four options plus Bring Your Own:

**Scenario 1 — The Retention Engine.** B2B SaaS losing 30% of users in 90 days. Why are they leaving? Build a prototype that surfaces churn drivers and tests whether an intervention can change the curve. Likely risk: value.

**Scenario 2 — The Internal Tool Nobody Uses.** CRM with 18% adoption. Built it, no one came. Figure out why adoption is so low and prototype a version that fits how people actually work. Classic 1-to-N. Likely risk: usability.

**Scenario 3 — The Marketplace Trust Problem.** Bookings flat, zero-review providers. Buyers don't trust new sellers. Prototype a trust mechanism that gets first-time providers their first booking. Likely risk: value/feasibility.

**Scenario 4 — The Dashboard Nobody Reads.** Analytics with 60% bounce rate. Data exists but nobody finds insights. Prototype a version that surfaces the right information for decisions. Likely risk: usability.

**Bring Your Own** — use a real problem from your company. Check with me for approval.

This is a product exercise, not a startup pitch. Pick the one closest to your real work. Post your choice in Slack.


## Slide 13 — Quick Debrief: Final Project Commitment

Post on Slack in one sentence: your chosen scenario and your main reason for selecting it.

**ACTION: Scan Slack for 1-2 minutes. Read out a few choices, especially diverse ones. If most students picked the same scenario, that's fine — different hypotheses will make the builds diverge.**

If you chose Bring Your Own, I'll check in with you during the first exercise to make sure it has a clear user, a measurable outcome, and enough ambiguity to test.


## Slide 14 — The Problem Framework

Before you open any tool, you frame the problem. Six elements — and I'm going to show you a filled-out example rather than lecture the theory.

Here's the Retention Engine scenario — the one we just demoed:

**Goal** — reduce 90-day churn from 30% to 15%. **Problem** — solo users churn at 3x the rate of team users, and only 12% of new users send an invite in the first 3 days. **Context** — B2B PM tool, Series A, 5,000 paying teams, 4.2M ARR. The board requires measurable improvement this quarter. **Constraints** — no engineering resources for 6 weeks, must work within the existing product surface. **Success Criteria** — Day-3 invite rate increases from 12% to 25%. And the last one — **Explore** — is the blocker discoverability (the invite button is buried in Settings > Team > Members) or motivation (users don't understand why inviting teammates matters)?

That last element is the one most people skip. Most frameworks stop at "what are we building." This one asks "what are we *learning* by building this?" That's the difference between a demo and a decision tool.

**ACTION: Drop the Problem Framework template link in Slack.** The link is on the slide — point students to it. They'll use it during the exercise.


## Slide 15 — Individual Exercise: Frame Before You Build

**ACTION: This is an individual exercise. Give students the full time. Do NOT let them open Lovable yet.**

Before you build, you prepare. This exercise is your pre-work — gathering the real-world data, user voice, and visual anchors that will make your build fundamentally different from M1.

Three steps:

**Step 1 — Complete your Validation Brief.** Define your hypothesis, risk type, kill switch, and success criteria. Use the Validation Brief template — the link is on screen and in Slack. Write your hypothesis as one sentence: "I'm testing whether [X]."

**Step 2 — Execute context injection using the Context Data Pack.** Open the Context Data Pack for your scenario — it's in Slack. Each pack has three things: 8-12 user and stakeholder quotes from interviews and support tickets, a CSV with 15-20 rows of realistic quantitative data, and a full problem brief. Highlight 2-3 user quotes that directly relate to your hypothesis. Circle 3-5 metrics you want your prototype to display. Copy and paste these into your exercise document. For Bring Your Own: download the blank template and fill in your own data.

**Step 3 — Secure a visual reference.** Go to Mobbin or take a screenshot of your existing product. Focus on the functional pattern — like "team invite flow" or "analytics dashboard" — not the product name. The Visual Reference Guide has instructions.

**ACTION: Walk the room (or monitor Slack/breakout). Watch for two failure modes:**
1. **Students who skip the data pack** and just write a generic brief — redirect them: "Open the feedback file. Which quotes relate to your hypothesis?"
2. **Students who try to include everything** from the data pack — redirect them: "Pick the 3-5 data points that matter most for your specific hypothesis."

**At the 3-minute mark:** "You should have your Validation Brief done. If you're stuck on the hypothesis, ask: what would kill this idea if we learned it was wrong?"

**At the 4-minute mark:** "Finish selecting your quotes and metrics. 1 minute to grab your screenshot and post everything in Slack."


## Slide 16 — Timer: 5 Minutes

**ACTION: Let the timer run. Continue walking the room. Ensure everyone has posted their hypothesis, selected quotes/metrics, and screenshot in Slack before moving on.**


## Slide 17 — Cameras On

Welcome back! Quick reminder — cameras on for this next section. We're about to connect all the pieces.


## Slide 18 — Chapter Break: Start Your Final Project

This is the main event. Everything before this was setup. Now you build.


## Slide 19 — Hands-On Lab: Start Your Final Project and Build With Confidence

**ACTION: This is the core lab. 40 minutes (per the legacy walkthrough). Walk the room continuously. Final 2 min reminder: you can't review a blank screen — partners are assigned the moment the timer hits zero.**

You have everything you need — Validation Brief, Context Data Pack, Visual Reference, and a structured prompt. Here's the workflow:

**Step 1 — Open the Structured Prompt Builder.** The link is in Slack and on your exercise guide. This is where you assemble your mega-prompt — NOT in Lovable directly. Paste your scenario brief, user quotes, and metrics into Block 1 (Context).

**Step 2 — Drop your screenshot into Block 2** (Visual Reference) and specify whether the AI should match the layout, density, or visual style.

**Step 3 — Translate your Validation Brief into Block 3** (Constraints). Paste your hypothesis and kill switch to set the functional guardrails.

**Step 4 — Define your output screens in Block 4.** Then click "Copy Prompt." Use an LLM — ChatGPT or Claude — to refine your mega-prompt and find any logic holes before you spend Lovable credits.

**Step 5 — When your prompt is tight, take it into Lovable and trigger the build.**

**Step 6 — Connect GitHub.** As soon as your first build lands, connect GitHub. In Lovable, click the GitHub icon in the top right → authorize → done. Your code is now in a real repository. From this point forward, every change you make across Modules 3, 4, 5, and 6 is version-controlled. This is your safety net — if a prompt ever breaks your build, you can roll back to the last working version.

Your goal is NOT to build something pretty. Your goal is to build something that shows real data, tests your specific hypothesis, and looks like it belongs in your product's domain — because of the screenshot reference, the metrics, and the user voice you injected.

**ACTION: Watch for three failure modes as you walk the room:**
1. **Students prompting generically without using the data pack** — "Where are the user quotes in your prompt? Where's the data?"
2. **Students building something pretty that doesn't test their hypothesis** — "What assumption does this test? How would you know if it's validated?"
3. **Students who got a strong first result and are polishing aesthetics** — "Good start. Now stress-test it — go to the edge case. What happens when the data is empty? When the user does something unexpected?"

**At the 15-minute mark:** "You should have at least one working direction in Lovable. If your first prompt didn't land, refine it — don't start over."

**At the 20-minute mark:** "5 minutes. Verify your shareable link works. Copy it to Slack. And if you haven't connected GitHub yet — do it now. One click. Your final project needs version control from day one."

**Credit reminder:** This is exactly why we use the Structured Prompt Builder first. One well-assembled prompt instead of five trial-and-error burns in Lovable.


## Slide 20 — Breakout: Show and Swap Your Prototype

**ACTION: Create breakout pairs — random assignment. Same format as M1.**

Swap prototype links in the chat. Explore your partner's build silently for 3 minutes — no verbal context, no explaining. Like a real user.

When Stripe puts a new feature in front of users, they don't explain how it works. They watch where people click and where they hesitate. That's what you're doing now.

After 3 minutes of silent exploration, discuss:

What do you think the core hypothesis or kill switch was? Could you figure it out from the prototype alone? Where did the experience lose credibility? Did the data make you feel like you were using a real product — or did the placeholder trap show up somewhere?

The question isn't "is this cool?" It's "does this test what they said they were testing?" If you have to explain the UI, the intent isn't sharp enough.

After you've discussed, swap roles and repeat.


## Slide 21 — Quick Debrief: What Your Partner Just Told You

Post on Slack: M1 vs. M2 screenshots side by side, plus the one piece of feedback from your Show-and-Swap partner that landed hardest. The signal you came here for came from your partner, not from a number you give yourself.

The credibility rubric on the slide (1 Sketch · 2 Rough Direction · 3 Getting There · 4 Team-Ready · 5 VP-Ready) is private framing only — use it for your own reflection, not for the Slack post.

**ACTION: Read out 2-3 of the partner-feedback lines from #builds.** Don't read out numbers — they're noise and they invite people to defend their score instead of sitting with what their partner said. Pick the feedback lines that name a specific friction point. Follow up with: "what does this tell you about whether the build actually tests what you said it tests?"

The shift from M1 matters. In M1 the gap was about looks. In M2 it's about whether the build tests what you claimed it tests. Same private read, different reason — that's the move.


## Slide 22 — Module 2 Complete: What You Accomplished Today

Look at what happened in this session. You built a targeted prototype designed to surface evidence, not just look finished.

**Context Injection: Decoded.** You moved past simply asking for screens. You fed the AI business logic through user quotes and metrics, turning a generic vibe into a specialized tool that acts as a strategic product partner.

**Credibility Gap: Closed.** You eliminated the placeholder trap by testing specific hypotheses with real-world data. Your mockup went from hollow to something capable of driving real go/no-go decisions with stakeholders.

**Stress-Test Review.** Peer review proved that if you have to explain the UI, the intent isn't sharp enough. Your partner's fresh eyes caught what you couldn't see.

**4 Validation Pillars.** Every prompt you wrote was anchored by a formal hypothesis, risk type, kill switch, and measurable success criteria.

Next up — Module 3. Same product, better execution.


## Slide 23 — Key Takeaways

Let me bring this home with a story that connects all three lessons.

In 2007, Brian Chesky and Joe Gebbia couldn't make rent. They had air mattresses, a conference was coming to San Francisco, and every hotel was booked. So they threw up a basic website — AirBed & Breakfast — with photos of their apartment and a PayPal button. That first prototype tested one thing: will strangers pay to sleep in someone else's home? Three people booked. Hypothesis validated. That's takeaway one — **every prototype starts with a named assumption.** The problem framework, the kill switch, the "I'm testing whether [X]" sentence. If you can't name it, you're building a demo, not running an experiment.

But here's what most people don't know. After those first three guests, Chesky didn't scale the website. He flew to New York and stayed with early hosts. He photographed their apartments himself. He interviewed guests over breakfast. He injected real user voice — actual quotes, actual complaints, actual metrics — back into the next version of the product. The listings with his professional photos booked 2-3x more than the ones without. That data point didn't come from a survey. It came from a working prototype that real people could use. That's takeaway two — **context injection turns prototypes into decision tools.** Real user quotes, real metrics, real problem briefs fed into the builder. The difference between your M1 and M2 prototypes isn't visual quality — it's what they prove.

And takeaway three — **the validation loop compresses months into minutes.** Chesky ran dozens of small experiments in weeks, not quarters. Each one had a hypothesis, constraints, and evidence. By the time Airbnb raised their seed round, they didn't have a pitch deck full of assumptions — they had a pitch deck full of answers. "We tested X. Here's what happened. Here's what we're testing next." That's the loop you ran today — hypothesis, constraints, build, synthesize. Keep running it.

From this point forward, every prototype gets judged by what it validates — not how it looks.


## Slide 24 — Extra Practice and Next Session

Two optional exercises if you want to dig deeper:

**First — Stress-Test Your Kill Switch.** Pick a second high-priority risk from your Validation Brief and build a completely different prototype to test it. If your first build was a landing page for value risk, try a functional app for feasibility. Which one would you actually move forward with?

**Second — Perform a Data Swap.** Take your existing prompt but replace the Context Data Pack with completely different user quotes or market metrics. Observe how the product changes when you inject different context into the same functional frame. Does the AI adapt the copy and flow to match the new user friction?

Next session — Module 3: Architect Precise Prototypes with Context Engineering. You'll move from mega-prompts to prompt chaining — isolating business logic, user flow, and visual design into distinct stages to prevent AI drift. Same product, sharper execution. You'll go from "build me something" to "build me exactly this."


## Slide 25 — Survey

At the end of each session, please scan the QR code or use the link to share your feedback. Your insights help us improve and make each cohort better than the last. We'd love to hear about your experience!


## Slide 26 — Bonus Resources

Here you'll find all the resources for this module — the Module 2 Lab Guide walkthrough and the Vibe Coding Validation Brief template. Bookmark these. The Validation Brief in particular is something you'll use in every module going forward — it's not a one-time exercise.


## Slide 27 — Q&A

Alright, before we close — any final questions? This is your time to ask anything about what we covered today, the tools, your scenario selection, or the final project. Feel free to unmute or drop your question in the chat. And as always, share questions in Slack if something comes up later. See you next session!
