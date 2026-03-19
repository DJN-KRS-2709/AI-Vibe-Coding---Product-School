# Module 3: Ensure Complex System Stability with Prompt Chaining — Speaker Notes

Casual talking points for each slide. Not a script — just the key things to say, what to do on screen, and the energy to bring. Module 3 is the precision shift — students stop prompting and start directing. The vibe moves from "build me something" to "build me exactly this." Real examples woven in. Company stories where relevant.

**Tools referenced in this module:**
- Lovable (building)
- Prompt Chain Planner (planning the 3-step chain before building)
- Prompt Techniques Template (reference sheet for prompting strategies)
- Living Prompt Pack Builder (long-term reusable asset — started in M3, grows through M4–M6)

**What to prepare before class:**
- [ ] Open the M2 Customer Vibe — Retention Engine prototype in Lovable (the context-injected version with 3 screens, real data, real user quotes, but no states, no secondary views)
- [ ] Have 3 demo prompts pre-typed in a text file, ready to paste (see Slide 6 demo script below)
- [ ] Have a pre-built M3 version as backup (same prototype with 5+ screens, states, and refinement already applied)
- [ ] Prompt Chain Planner link ready to drop in Slack
- [ ] Prompt Techniques Template link ready
- [ ] Living Prompt Pack Builder link ready
- [ ] Screen share on
- [ ] Have M1 and M2 prototypes accessible in separate browser tabs (for the triple reveal later)

---

## Slide 1 — Title

Welcome to Module 3 — Ensure Complex System Stability with Prompt Chaining.

Module 1 was speed — you proved you can build. Module 2 was aim — you proved you can build the right thing. Module 3 is precision. You're going to learn to direct the AI like you'd direct an engineer — expand here, add states there, refine this one screen, don't touch anything else.

By the end of today, your M2 prototype won't just test a hypothesis — it'll look like something your VP thinks engineering built.


## Slide 2 — Class Expectations

Same ground rules. Cameras on, be present, arrive on time, participate actively. Use Slack for communication. Any tools and accounts should be active before class — we won't stop to troubleshoot setup today.

One new thing for M3: tool readiness matters more today than any previous session. You'll be executing prompts in a specific sequence — if your Lovable account isn't working or your M2 prototype isn't accessible, you'll fall behind. Check now.


## Slide 3 — Syllabus

Quick refresher on where we are. Six modules, three weeks.

Module 1 was velocity — you built at lightspeed. Module 2 was validation — you injected real data and a hypothesis. Module 3 — today — is stability. You'll master prompt chaining to build multi-screen architectures that don't break when you add complexity.

Module 4 transitions your prototype to production specs — GitHub, Living PRDs, engineering handoff.

Module 5 ships it live — databases, auth, edge cases, and you deploy to a real URL.

And Module 6 closes the loop — you measure real-world performance, use AI-driven analytics, and iterate based on evidence.

Every module builds on the last. What you build today becomes what you structure in M4, integrate in M5, and measure in M6.


## Slide 4 — Agenda

Three things today.

First — how to prove your prototype is resilient. I'll show you what happens when you chain prompts instead of throwing one big mega-prompt at the AI.

Second — a PM's precision prompting toolkit. The techniques that separate exploration prompts from execution prompts.

Third — hands-on lab. You'll execute your own 3-step prompt chain against your M2 build. By the end, you'll have a multi-screen, multi-state product — not a mockup.


## Slide 5 — Chapter Break: How to Prove Your Prototype is Resilient

Let's start with what's missing from your M2 build — and how we fix it.


## Slide 6 — Instructor-Led Demo: The Precision Prompt Chain

> Instructor demo: **The Customer Vibe — Retention Engine** (B2B PM SaaS — 30% churn, team invites — carried from M2 demo)
> Total demo time: ~8 minutes. Pre-type all 3 prompts before class.

### SETUP

- [ ] Open the M2 Retention Engine prototype in Lovable (3-screen onboarding flow with real data, real user quotes, hypothesis embedded — but no states, no secondary views)
- [ ] Have all 3 prompts pre-typed in a text file, ready to paste
- [ ] Have a pre-built M3 version as backup in a separate Lovable project
- [ ] Screen share on

### Show the Gap (~1 min)

**What you do:** Pull up the M2 Retention Engine prototype on screen share. Click through the 3-screen onboarding flow — team value, invite action, collaboration payoff.

**What you say:** "This is our M2 build. Real data — 12% Day-3 invite rate, 68% vs 22% retention split. Real user quotes. A named hypothesis. Design-matched to Asana. Your VP looks at this and says 'Great. Where's the full flow? What happens when something goes wrong? What does the PM dashboard look like?' And you have nothing to show."

**Then point out what's missing:** "Three screens. No loading states — what does the user see while data loads? No error handling — what if the invite fails? No secondary views — where does the user go after inviting? Where does the PM track if this is working? And if I asked your teammate to reproduce this, they couldn't — because it was built with one big prompt."

**What you say:** "Three prompts. Watch what happens."

### Prompt 1 — Expand (~90 sec)

**Paste this prompt:**

> "Build the next phase of this app in a strict sequence: 1. Add a 4th screen: 'Team Workspace' — the screen users see after completing the invite flow. Show invited teammates, their status (pending/accepted), and a quick-start project template. Match the layout and spacing of the existing screens. 2. Add a 5th screen: 'PM Dashboard' — an internal analytics view showing Day-3 invite rate, retention comparison (with invite vs without), onboarding completion rate, and a list of users who haven't invited yet. Match the data-heavy density of the attached reference. 3. Navigation: Write the logic so the onboarding flow leads to Team Workspace, and the PM Dashboard is accessible from a nav menu. Build these in order so the Team Workspace serves as the mandatory anchor for the PM Dashboard."

**While it generates:** "Watch — I'm not rebuilding the 3 screens I already have. I'm expanding from them. The AI builds Screen 4 first, then Screen 5, in sequence. Each one depends on the last."

**When it's done:** Click through all 5 screens. Show the navigation working.

**What you say:** "3 screens became 5. Complete user journey — from onboarding through team setup to PM tracking. Navigation works. And I didn't touch the original 3 screens."

### Prompt 2 — Behavior (~90 sec)

**Paste this prompt:**

> "Apply the following logic constraints to the entire app: 1. Loading states: Add skeleton screens to the Team Workspace and PM Dashboard while data loads. 2. Empty state: If no teammates have been invited yet, the Team Workspace shows 'Your team is waiting — invite your first teammate to get started' with the invite button prominent. 3. Error state: If the invite fails, show 'Invite couldn't be sent — check the email and try again' with a retry button. If the PM Dashboard can't fetch data, show 'Connection lost. Please refresh the dashboard.' 4. Maintain the same design language throughout and tether all behavior strictly to these rules."

**While it generates:** "This is Beat 1 — the moment the prototype starts behaving like real software."

**When it's done:** Show the loading skeleton appearing. Navigate to Team Workspace with no data — show the empty state. Show the error message.

**What you say:** "Same screens. But now they have loading states, empty states, and error handling. Before this prompt, it was a mockup. Now it behaves like a shipped product. Your VP doesn't know the difference."

### Prompt 3 — Refine (~60 sec)

**Paste this prompt:**

> "The PM Dashboard needs a more actionable layout. Start by listing the 3 biggest gaps in the current PM Dashboard compared to a professional analytics tool. Then: add a 'Nudge' button next to each user who hasn't invited — clicking it simulates sending a reminder. Make the retention comparison chart interactive — hover shows exact numbers. Add a 'This Week' / 'This Month' / 'All Time' toggle for the invite rate metric. Don't change anything else in the project or touch the underlying logic of the other screens."

**While it generates:** "This is Beat 2 — I'm refining ONE screen without rebuilding anything else. Surgical steering."

**When it's done:** Show the PM Dashboard improvements. Then click back to the other screens — nothing changed.

**What you say:** "I changed one screen. The other four are untouched. That's the paradigm shift. You're not starting over. You're directing — expand here, add states there, refine this. Like giving sprint tickets to an engineer."

### Debrief (~1 min)

**What you say:** "3 prompts. 5 connected screens. Loading states, error handling, empty states. An interactive PM dashboard with a nudge button. And I didn't rebuild anything — I expanded what I had. You'll do this to your own build in 30 minutes."

**Transition to Slide 7.**

### THE PROMPTS (copy-paste version for your text file)

**Prompt 1 — Expand:**
```
Build the next phase of this app in a strict sequence: 1. Add a 4th screen: 'Team Workspace' — the screen users see after completing the invite flow. Show invited teammates, their status (pending/accepted), and a quick-start project template. Match the layout and spacing of the existing screens. 2. Add a 5th screen: 'PM Dashboard' — an internal analytics view showing Day-3 invite rate, retention comparison (with invite vs without), onboarding completion rate, and a list of users who haven't invited yet. Match the data-heavy density of the attached reference. 3. Navigation: Write the logic so the onboarding flow leads to Team Workspace, and the PM Dashboard is accessible from a nav menu. Build these in order so the Team Workspace serves as the mandatory anchor for the PM Dashboard.
```

**Prompt 2 — Behavior:**
```
Apply the following logic constraints to the entire app: 1. Loading states: Add skeleton screens to the Team Workspace and PM Dashboard while data loads. 2. Empty state: If no teammates have been invited yet, the Team Workspace shows 'Your team is waiting — invite your first teammate to get started' with the invite button prominent. 3. Error state: If the invite fails, show 'Invite couldn't be sent — check the email and try again' with a retry button. If the PM Dashboard can't fetch data, show 'Connection lost. Please refresh the dashboard.' 4. Maintain the same design language throughout and tether all behavior strictly to these rules.
```

**Prompt 3 — Refine:**
```
The PM Dashboard needs a more actionable layout. Start by listing the 3 biggest gaps in the current PM Dashboard compared to a professional analytics tool. Then: add a 'Nudge' button next to each user who hasn't invited — clicking it simulates sending a reminder. Make the retention comparison chart interactive — hover shows exact numbers. Add a 'This Week' / 'This Month' / 'All Time' toggle for the invite rate metric. Don't change anything else in the project or touch the underlying logic of the other screens.
```

### WHAT TO PRE-BUILD (the night before)

1. **The M2 version (the starting point):** Your M2 Retention Engine prototype — 3 screens, real data, no states. This should already exist from the M2 demo.

2. **The M3 version (the payoff):** Run all 3 prompts above sequentially in Lovable. Make sure it generates:
   - 5 connected screens with working navigation
   - Loading skeletons on Team Workspace and PM Dashboard
   - Empty state on Team Workspace
   - Error state on invite failure
   - Interactive PM Dashboard with nudge button and time toggle
   - Original 3 onboarding screens untouched

3. **Have both open in separate browser tabs** so you can switch if the live build fails.


## Slide 7 — Reflection Moment: What's Missing From Your M2?

**ACTION: This is interactive. Give students 3-4 minutes.**

Open up your prototype from Module 2. Take a real look. I want you to answer three questions:

One — how many screens does it have? Can you navigate between them? Most of you have 2-3 screens. A real product has a complete journey.

Two — what happens while data is loading? What if there's an error or no data? If the answer is "nothing" — that's a static mockup, not a product.

Three — if you had to pass this to a teammate today, could they reproduce this exact result using your current prompt? If the answer is no, your process isn't portable.

Post your answers in Slack or unmute and share.

**What you say after the discussion:** "Those three gaps — limited screens, no states, and non-reproducible prompts — are exactly what we close today. By the end of this session, you'll have 5+ screens, loading and error states, and a documented prompt chain someone else can follow."


## Slide 8 — Chapter Break: A PM's Precision Prompting Toolkit

Now let's give you the system that makes this work every time.


## Slide 9 — The Prompting Maturity Curve

This is the key mental model for M3. Your prompt style should match your confidence level.

**Exploration prompts** are open-ended and flexible. "Build me a dashboard for tracking retention." You're defining the *what* — letting the AI suggest the interaction pattern. That was M1 and early M2. You had uncertainty, so your prompts were loose.

**Execution prompts** are rigid and constrained. "Add a loading skeleton to the Team Workspace. If no teammates exist, show this exact empty state message. Don't change anything else." You're defining the *how* — dictating exact business rules and edge cases.

As you learn more about what you're building, your prompts must get more specific. You earned that specificity through M1 and M2. Now you cash it in.

Think of it like this: Spotify's Discover Weekly started as an exploration — "Can we recommend music based on listening habits?" That was the M1 prompt. But by the time it shipped, every rule was precise — what counts as a listen, how to weigh recency vs. frequency, what to exclude. That's M3-level prompting.


## Slide 10 — Three Common Prompting Traps

Three traps to avoid now that you're doing execution prompting.

**The Mega Prompt** — don't try to build a database, API, and UI in one massive prompt. That's like giving an engineer a 47-page spec and saying "build all of it by Friday." Use prompt chaining — build logic first, then apply the design, so if something fails, you know exactly where.

**The Vague Request** — asking for a feature without defining the user state creates hollow shells. "Add a team page" gives you a page. "Add a team page that shows pending invites, accepted members, and an empty state when nobody's been invited yet" gives you a product. Define the functionality AND the specific user path.

**The Micromanager** — wasting credits on text-based pixel tweaks is inefficient. "Make the button 2 pixels bigger and change the hex to #3b82f6" — the AI will do it, but you'll burn 5 credits on what should be 1. Instead, upload a screenshot of the exact style you want and let the AI match it in one shot. Multimodal prompting beats micromanagement every time.


## Slide 11 — The Execution Toolkit

This is the core framework for M3. Three stages, three different prompting techniques layered in sequence.

**Step 1 — Expand: Build the Logic.** Use Chain-of-Thought (COT) prompting. Force the AI to build in a strict, dependent order — Screen A, then Screen B, then Screen C. Attach visual references for every new screen. The prompt anchors the logic, the screenshot anchors the layout.

**Step 2 — Behavior: Define the Flow.** Use Constraint Grounding. Hard-code if/then triggers for the unhappy path — loading, empty, and error states. Ground the AI in specific rules so it behaves like real software, not a static mockup.

**Step 3 — Refine: Polish the Design.** Use Reflection Prompting. Isolate a specific screen, force the AI to audit the UI and list gaps before editing. This ensures precision and prevents the AI from restarting or changing your core logic.

The takeaway: you aren't just splitting one big prompt into three parts. You're layering different cognitive strategies in sequence so precision accumulates without breaking the foundation. That's why it's called chaining — each link depends on the one before it.

**ACTION: Drop the Prompt Techniques Template link in Slack.** Students can reference the full list of techniques during the lab.


## Slide 12 — Prompt Chaining in Action

Here's what the three prompts actually look like — concrete examples for each stage.

**Expand (COT):** "Build the next phase of this app in a strict sequence: 1. Add a 2nd screen: 'User Settings'. Match the layout of the attached Asana reference. 2. Add a 3rd screen: 'Account Activity'. Match the data-heavy density of the attached Intercom reference. 3. Navigation: Write the logic so Settings links to Activity. Build in order."

**Behavior (Constraint Grounding):** "Apply these logic constraints to 'Account Activity': Skeleton screens for loading. Empty state: 'No activity yet. Start your first project to see data here.' Error state: 'Connection lost. Please refresh.' Maintain the same design language."

**Refine (Reflection):** "The User Settings screen needs professional polish. Start by listing the 3 biggest gaps in typography and spacing compared to Asana. Then fix those gaps. Don't change anything else."

Notice the pattern: Expand builds structure, Behavior adds resilience, Refine adds polish. Each one is targeted. Each one is safe — it doesn't undo the previous work.


## Slide 13 — Individual Exercise: Plan Your Prompt Chain

**ACTION: This is individual work. Give students the full time. Do NOT let them open Lovable yet.**

Before you build, you plan. This is the same discipline from M2 — preparation is what makes the build dramatically better.

Four steps:

**Step 1 — Audit your M2 prototype.** Open it and identify 3-5 flow gaps (missing screens, dead ends), 3 specific friction points (no loading states, no error handling), and 1 targeted UI element you want to refine.

**Step 2 — Draft your 3-step chain.** Write your Expand, Behavior, and Refine prompts. If you get stuck, use the Prompt Chain Planner — the link is in Slack. It helps you structure each prompt.

**Step 3 — Gather your references.** For the COT expansion, get screenshots of the layouts you want to match for your new screens. Same Mobbin workflow from M2.

**Step 4 — Copy your finalized prompts into your exercise document.** You'll need them for peer review and the lab. This documentation becomes part of your Living Prompt Pack — a final project deliverable.

**ACTION: Walk the room. Watch for:**
1. **Students who jump to Lovable** — "Close it. Plan first. Your chain isn't ready until it's written down."
2. **Students writing one mega-prompt instead of three** — "Split it. One prompt per stage. Expand, Behavior, Refine."
3. **Students with vague Behavior prompts** — "What exact message appears when data is empty? What exact error text shows? Be specific."


## Slide 14 — Breakout: Show and Swap Your Prompt Chain

**ACTION: Create breakout pairs — random assignment.**

Swap your Prompt Chain Plan — your three drafted prompts — in the chat. Read your partner's prompts silently for 3 minutes. No verbal context, no explanations.

This mirrors a professional handoff. If your partner can't understand the chain without you explaining it, it's not portable. That's the test.

After 3 minutes, discuss:

Did you notice any confusion or sudden jumps in the screen sequence? Is there a specific piece of logic for error handling or loading states that might have been missed? What's the strongest part of this chain — the part that makes it reusable for other projects?

The question isn't "is this clever?" It's "could I run this chain on my own project and get a predictable result?"


## Slide 15 — Quick Debrief: Key Learning Statement

Post on Slack in one sentence: what was the biggest logic gap your partner found in your prompt chain that you completely took for granted?

This is the value of the peer audit. You're too close to your own build — your partner's fresh eyes catch the assumptions you baked in without realizing it.


## Slide 16 — Timer: 5 Minutes

**ACTION: Let the timer run. Quick break.**


## Slide 17 — Cameras On

Welcome back! Cameras on for the main event.


## Slide 18 — Chapter Break: Execute Your Prompt Chain and Extend Your Build

This is the main event. Everything before this was setup. Now you execute.


## Slide 19 — Hands-On Lab: Execute Your Prompt Chain

**ACTION: This is the core lab. Give students 25-30 minutes. Walk the room continuously.**

You have your 3-step chain planned. Now execute it against your M2 prototype. Here's the workflow:

**Step 1 — Open your M2 prototype in Lovable.**

**Step 2 — Execute Prompt 1: Expand.** Copy your Expand prompt from the Planner, attach your visual references, and build your new screens. Fix any layout issues that appear, then document what was produced in your Planner.

**Step 3 — Execute Prompt 2: Behavior.** Paste your logic for loading, error, and empty states. Verify at least one "unhappy path" works in the prototype — test the loading skeleton, trigger the empty state, check the error message. Record the result.

**Step 4 — Execute Prompt 3: Refine.** Use surgical steering to polish one specific element. Check that the change is localized — the other screens should be untouched. Document the final output.

**Step 5 — Finalize your Prompt Chain Planner.** Make sure all "What did this produce?" sections are filled. This becomes the raw data for your Living Prompt Pack — a final project deliverable.

**ACTION: Watch for three key moments as you walk the room:**
1. **The loading skeleton reaction** — when a student's screens suddenly have loading states, their face changes. That's Beat 1. Let it land.
2. **The "I didn't start over" moment** — when a student refines one screen and checks that everything else is intact. That's Beat 2. Name it: "You're steering, not restarting."
3. **Students stuck in a prompt loop** — "If you're 5 prompts deep on the same issue, stop. Read the chain. Find the divergence. Fix ONE prompt."

**At 15 min:** "You should have your Expand done and be working on Behavior. If your Expand broke, don't rebuild — diagnose which part of the sequence failed."

**At 22 min:** "Wrap up Refine. Fill in your Planner. Make sure your shareable link works."

**Credit reminder:** Three prompts, not fifteen. The chain is efficient by design. If you're burning credits, your prompts are too vague.


## Slide 20 — Quick Debrief: Prompt Functionality Statement

Post on Slack in one sentence: what made your prompt work? Or, what didn't work and what did you change?

Then reply to 2 other learning sentences from your peers. The best insights often come from what went wrong — "My Behavior prompt broke the navigation because I forgot to say 'don't change anything else.'" That's a lesson everyone can use.


## Slide 21 — Prompt Chain Debugging

When a chain goes off-rails, diagnose before re-prompting. Throwing more prompts at a broken chain just compounds the error.

Four steps — work them in order:

**Step 1 — Read the Chain.** Go back to your Planner. Read each prompt in sequence. Does the logic flow?

**Step 2 — Compare the Output.** Look at what the AI actually built vs. what you asked for. Where did it diverge?

**Step 3 — Diagnose.** Find the specific prompt where the break happened. Was it ambiguous? Did it conflict with a previous instruction?

**Step 4 — Fix It.** Fix ONE prompt. Not three. Not the whole chain. The smallest possible intervention.

If you're 5+ prompts deep on the same issue, the problem isn't the tool — it's your framing. Step back. Re-read your chain. The fix is almost always in the prompt, not in adding more prompts.


## Slide 22 — Living Prompt Packs

This is where your work today becomes a permanent asset. A Living Prompt Pack is a markdown file that encodes your product's DNA into four reusable blocks:

**Product Context** — your source of truth for every new session. Company, users, hypothesis, constraints.

**Design Reference** — your visual DNA. The screenshots and design system tokens that keep every screen consistent.

**Constraint Templates** — your "always/never" logic. Loading states always show skeletons. Error states always show retry. Empty states always show a clear next action.

**Output Templates** — blueprints for components and navigation flows. The structural patterns that repeat across screens.

The ROI is threefold. **Cross-tool portability** — move between Lovable, Bolt, Cursor without losing your core logic. **Guaranteed reproducibility** — anyone can run your pack and get the same result. **Cumulative precision** — every constraint you refine becomes permanent.

In Module 1, you learned that AI Skills exist. Now you're architecting them yourself. You're not shopping for solutions — you're building the execution framework from scratch. This pack grows through M4, M5, and M6 and becomes a final project deliverable.

**ACTION: Drop the Living Prompt Pack Builder link in Slack.** Students should start populating their pack after class.


## Slide 23 — Module 3 Complete: What You Accomplished Today

Look at what happened. You replaced AI guessing with a 3-step sequence: Expand, Behavior, Refine. You scaled your build without starting over.

**The Fragility Gap: Hardened.** You eliminated happy-path traps. Loading skeletons, error handling, empty states. Your mockup became a resilient machine that anticipates failure.

**Peer Audit: Passed.** You proved your intent was sharp enough for a partner to read and understand your logic without a walkthrough.

**Living Library: Started.** You've started a collection of high-performance prompt structures that port into any future project.

**3 Chained Prompts.** That's all it took to go from a 3-screen mockup to a multi-screen product with interactive states.

Project deliverable reminder: copy your successful "gold standard" prompts from today into the Prompt Library section of your final project deck. Do this today while it's fresh.

Next up — Module 4. Make the jump from prototype to production.


## Slide 24 — Key Takeaways

Let me bring this home with a story about building with precision.

In 2009, Kevin Systrom was working on an app called Burbn — check-ins, photo sharing, gaming mechanics, meetup planning. A dozen features competing for attention. But when he looked at the data, one behavior towered above everything else: people loved sharing photos. So Systrom killed every feature except photos. He went from "build me everything" to "build me exactly this." That's takeaway one — **prompts must evolve as your confidence grows.** Now you have a working prototype with real data and a validated hypothesis. Your prompts need to match that certainty. The maturity curve isn't optional — it's how you prevent the AI from hallucinating as complexity scales.

Once Systrom had that clarity, he and Mike Krieger built Instagram in strict sequence. First: the camera and filters. Then: the social feed. Then: cross-platform sharing. Each layer depended on the one before it. They didn't build sharing before the feed existed. They didn't build the feed before the camera worked. That's takeaway two — **prompt chaining is how PMs master multi-screen builds.** Expand, Behavior, Refine — three stages that layer layout, logic, and polish in sequence. Each uses a different cognitive strategy, and because each prompt is isolated, when something breaks, you know exactly where.

Then came launch day. Twenty-five thousand signups in hours. The servers buckled. Systrom and Krieger didn't panic and rebuild. They traced the problem to one bottleneck — the database wasn't configured for that volume of concurrent writes. They fixed that one thing. By the end of the day, the system stabilized. That's takeaway three — **when a chain fails, diagnose before re-prompting.** If you're 5 prompts deep on the same issue, the problem isn't the tool — it's your framing. Read the chain, find the divergence, fix one prompt. Discipline over volume.

That's the arc. Get precise when you've earned certainty. Layer complexity in sequence. And when something breaks, find the one link that failed.


## Slide 25 — Extra Practice and Next Session

Two optional exercises:

**First — Execute a Partner's Chain.** Swap finalized prompt chains with a peer and try to build their project from scratch in a new Lovable tab. Does their logic hold up without extra prompts? Or does the chain break when they aren't there to steer it? This is the ultimate portability test.

**Second — The 10-Prompt Stress Test.** Take your finished M3 build and add three more complex features using only surgical refinement. See how many layers of logic you can add before the foundation cracks or the AI loses track of your system rules.

Next session — Module 4: Transition From Prototypes to Production Specs. You'll enforce technical rigor by extracting Living PRDs, connecting GitHub, and generating professional handoff documentation. Same product — now it graduates.


## Slide 26 — Survey

At the end of each session, please scan the QR code or use the link to share your feedback. Your insights help us improve and make each cohort better than the last. We'd love to hear about your experience!


## Slide 27 — Bonus Resources

Here you'll find the Module 3 Lab Guide walkthrough and the Vibe Coding Prompt Techniques Template. The Prompt Techniques Template is a reference you'll keep coming back to — bookmark it. And start populating your Living Prompt Pack after class today.


## Slide 28 — Q&A

Alright, before we close — any final questions? This is your time to ask about prompt chaining, debugging, your Living Prompt Pack, or anything else from today. Feel free to unmute or drop your question in the chat. See you next session!
