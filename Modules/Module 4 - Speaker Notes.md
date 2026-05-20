# Module 4: Transition From Prototypes to Production Specs — Speaker Notes

Casual talking points for each slide. Not a script — just the key things to say, what to do on screen, and the energy to bring. Module 4 is the hinge of the course — the first half ends here. The vibe shifts from "build" to "make it durable." Real examples from companies like Slack, Stripe, GitHub, and WhatsApp to ground every concept.

**Tools referenced in this module:**
- Lovable (building, refactoring, connecting infrastructure)
- Living PRD Extractor (lab tool — extract and document the PRD)
- Living Prompt Pack Builder (continuing from M3 — add structure prompts)
- GitHub (version control — connect from Lovable sidebar)
- Supabase (database — connect from Lovable)
- Cursor / Claude / any AI-native IDE (for the Inheritance Test — students use whatever AI tool they already have. The course doesn't require a new tool here. Goal is to demonstrate that any agent can read a well-structured repo.)

**What to prepare before class:**
- [ ] Open the M3 Retention Engine prototype in Lovable (same one carried from M2/M3 demos — now with prompt chain refinements, design system matching, and Living Prompt Pack applied)
- [ ] Have all prompts pre-typed in a text file, ready to paste (refactor, handoff)
- [ ] Have GitHub account logged in so the connection is instant
- [ ] Have Supabase ready (Lovable auto-generates the connection)
- [ ] Living PRD Extractor link ready to drop in Slack
- [ ] Lab guide and exercise links ready in Slack
- [ ] Screen share on

---

## Before We Start

Before we jump in — thank you. The feedback you're sharing after each session genuinely helps shape how we run this course, so keep it coming.

One thing that came through clearly: you want to stay in the flow. Questions are always welcome — I never want you to hold back — but here's how we'll handle them so everyone gets the most out of our time together:

1. **Raise your hand** if you want to ask something live. I'll give you your turn — I just might not take it immediately if we're mid-exercise, so bear with me.
2. **Drop it in the chat.** I see everything, and I'll address it when the moment is right. Bonus: other participants often jump in with great answers too.
3. **Slack me anytime.** Before, during, after — I'll get back to you.

This way nothing gets lost, and we keep the momentum going.

---

## Slide 1 — Title

Welcome to Module 4 — Transition From Prototypes to Production Specs.

You've been building for three modules. Module 1 was speed — you proved you can build. Module 2 was validation — you proved you can build the *right thing*. Module 3 was precision — you proved you can orchestrate complex multi-screen systems with prompt chaining.

But here's the question nobody's asked yet: what happens when you hand this to someone else? Today we answer that. By the end of this session, your prototype won't just look like a product — it'll be documented, version-controlled, and engineered for handoff.


## Slide 2 — Class Expectations

Same ground rules. Cameras on — I know, I know, but it genuinely makes a difference. Be present, arrive on time, participate actively during exercises. Use Slack for all communication. Save deeper questions for after class so we keep the flow going.

One addition for today: make sure all your tools and accounts are active *before* class. We will not stop or restart for setup. If you don't have GitHub or Supabase accounts yet, you'll create them during the lab — but everything else needs to be ready to go.


## Slide 3 — Syllabus

Quick refresher on where we are. Six modules across three weeks.

Module 1 was speed — you activated the build cycle and proved you can go from nothing to a working prototype. Module 2 was validation — you learned to build prototypes that prove something, not just look like something. Module 3 was precision — you used prompt chaining to maintain consistency and prevent breakage as complexity scaled.

Module 4 — that's today — is where we enforce technical rigor. You'll formalize your logic into a Living PRD, refactor your code so it's readable, connect your backend, and bridge the gap between your vision and an engineering handoff. Your code has been in GitHub since Module 2 — today we make what's inside that repo worth inheriting.

Module 5 ships it live — real databases, secure APIs, live URL, real users. And Module 6 closes the loop — you measure performance, use AI-driven analytics, and iterate based on evidence.


## Slide 4 — Agenda

Four things today.

First — The Black Box Gap. We'll look at what's actually under the hood of your M3 prototype. Spoiler: it's not pretty.

Second — How to Move From Prototype to Production. The theory behind the transition — when to do it, what the Living PRD is, and how it pays off your comprehension debt.

Third — Hands-on lab: Refactor your prototype code and generate your engineering handoff. You'll clean up the mess and produce a document an engineer can sprint from.

Fourth — Hands-on lab: Connect your backend with Supabase. Your code is already in GitHub from Module 2 — now we give your prototype a real database.


## Slide 5 — The Black Box Gap of AI-Generated Code

This kicks off the first major section. Your M3 prototype looks incredible from the outside. But the code? It's a black box. Let's open it up.


## Slide 6 — Reflection Moment: What's Under the Hood?

**ACTION: This is interactive. Give students 3-5 minutes. Let them explore before discussing.**

Open up your prototype from Module 3. Switch to the code view. Answer honestly:

One — could an engineer understand what each component does from its name alone? Or is it all `Component1` and `handleClick2`?

Two — is data logic separated from display logic? Or is everything tangled in one file?

Three — do you have any documentation? A README? Comments? Anything at all?

Feel free to unmute and share, or post your thoughts in the chat.

**Spend 2-3 minutes on responses.** Most students will discover: terrible names, no separation, zero docs. That's expected. That's the black box gap — your prototype looks like a finished product on the outside, but the code is incomprehensible to anyone who didn't build it.


## Slide 7 — Instructor-Led Demo: Comparing the Exterior With What's Under the Hood

> Instructor demo: **The Customer Vibe — Retention Engine** (B2B PM SaaS — 30% churn, team invites — carried from M2/M3 demos)
> Total demo time: ~8 minutes. Pre-type all 3 prompts before class.

Here's the problem we're solving. Your prototype looks like a finished product — high-fidelity visuals, solid hypothesis, interactive states — but if an engineer asked "How does the data flow?" or "Where is the logic for this screen?" — you'd be stuck digging through a messy file tree.

### STEP 1: Show the Facade (~2 min)

**What you do:** Pull up the M3 Retention Engine prototype in Lovable on screen share. Click through the screens — the 3-screen onboarding flow (team value → invite action → collaboration payoff), the retention metrics dashboard, the experiment summary. Remind them how polished it is.

**What you say:** "This is our M3 build. The onboarding flow that surfaces team invites to reduce churn. Three screens, design-system matched, interactive states, real user quotes and retention data embedded throughout. If your VP saw this, they'd think engineering built it."

**Then:** Switch to Lovable's code view. Let the mess sit on screen for 10 seconds. Don't explain it.

**What you say:** "Now look at the code. `screen five`. `handleClick2`. All logic in one file. No README. No documentation. This is what the engineer who inherits your prototype actually sees. This is the black box. Three prompts, two clicks — watch."

### STEP 2: Prompt 1 — Refactor the Code (~60 sec)

**Paste this prompt:**

> "Refactor the codebase. Rename all components to be descriptive (e.g., TeamValueScreen, InviteFlow, CollaborationPayoff, RetentionDashboard, ExperimentSummary). Separate data logic from display components. Group files by feature, not by type. Add a README.md that explains the project structure."

**While it generates:** "Watch the file tree on the left."

**When it's done:** Switch to code view. Show the before/after.

**What you say:** "`Component1` is now `TeamValueScreen`. `Component3` is now `InviteFlow`. There's a `/services` folder for data logic. There's a README. An engineer can read this on day one. Same product — readable code."

### STEP 3: Prompt 2 — Extract the Living PRD (~60 sec)

**Paste this prompt:**

> "Look at this entire prototype. Write a product requirements document that covers: what this product does, who it's for, the problem it solves, the screens and their purpose, the user flow from first screen to last, the hypothesis it tests, the key metrics, what's currently mocked vs. what would need real data, and recommended next steps for engineering. Create me a livingprd.md that stores this info."

**While it generates:** Stay quiet. Let the class watch the PRD appear.

**When it's done:** Read 2-3 sections aloud — Product Overview and Technical Reality are the most impactful.

**What you say:** "I didn't write this. The prototype wrote its own spec. The hypothesis — 'surfacing team invites during first-run onboarding increases Day-3 invite rate from 12% to 25%' — extracted from what we built, not imagined before building."

### STEP 4: Prompt 3 — Engineering Handoff (~40 sec)

**Paste this prompt:**

> "Generate an engineering handoff document: list every component and what it does, describe the data model (what's real vs. mocked), identify the 3 biggest technical decisions an engineer would need to make, and write a 'start here' guide. Create me a engineeringhandoff.md that stores this info."

**When it's done:** Read the "start here" section and one technical decision aloud.

**What you say:** "A new engineer joins the team Monday. They open this document. In 5 minutes, they know what the onboarding flow does, what's real, what's mocked, and where to start. That's the handoff."

### STEP 5: Connect the Backend (~30 sec)

**What you do:** Trigger the backend by prompting Lovable to add a feature that requires a database (e.g., "Save user onboarding progress to the database so returning users resume where they left off"). Lovable Cloud prompts you to enable — click Allow. Database, auth, storage, and edge functions are now live.

**What you do next:** Open the Lovable Cloud dashboard (Settings → Cloud). Show the database tables, the region, the live backend.

**What you say:** "One click. Your prototype has a real database, real auth, and real storage. This isn't a toy anymore. This is real infrastructure."

**Pause. Let it land.**

### STEP 6: Debrief (~2 min)

**What you say:**

"Same prototype. Same onboarding flow. Same screens testing the team invite hypothesis. But now it has:

- Clean code — `TeamValueScreen`, `InviteFlow`, not `Component1`
- A Living PRD — complete spec, extracted from the build
- An engineering handoff — component map, data model, start-here guide
- GitHub — already connected since Module 2, now with refactored code and a proper README
- A real backend — database, auth, and storage

Traditional PM workflow: research, spec, build, test. Vibe Coding workflow: build, test, extract the spec. The spec is the output, not the starting point. And the infrastructure follows the prototype — not the other way around.

You'll do all of this to your own build in the labs. But first — let's talk about *when* to make this transition and *how* the Living PRD works."

### THE PROMPTS (copy-paste version for your text file)

```
Prompt 1 — Refactor:
Refactor the codebase. Rename all components to be descriptive (e.g., TeamValueScreen, InviteFlow, CollaborationPayoff, RetentionDashboard, ExperimentSummary). Separate data logic from display components. Group files by feature, not by type. Add a README.md that explains the project structure.

Prompt 2 — Extract:
Look at this entire prototype. Write a product requirements document that covers: what this product does, who it's for, the problem it solves, the screens and their purpose, the user flow from first screen to last, the hypothesis it tests, the key metrics, what's currently mocked vs. what would need real data, and recommended next steps for engineering. Create me a livingprd.md that stores this info.

Prompt 3 — Handoff:
Generate an engineering handoff document: list every component and what it does, describe the data model (what's real vs. mocked), identify the 3 biggest technical decisions an engineer would need to make, and write a 'start here' guide. Create me a engineeringhandoff.md that stores this info.
```

### WHAT TO PRE-BUILD (the night before)

1. **The M3 prototype (the facade):** Your existing M3 Retention Engine — polished UI, Mobbin-matched, interactive states, but messy code underneath. This should already exist from your M3 demos.

2. **Have all 3 prompts pre-typed in a text file** so you can paste each one instantly.

3. **Have GitHub logged in** so the connection click is immediate — no auth delays during the demo.

4. **Deliver the prompts as if live** — paste and let them generate. But if any prompt produces weak output, have a pre-built backup version ready in a separate Lovable project you can switch to.


## Slide 8 — The New Operating Model: Vibe Coding Workflow

The slide shows two workflows side by side. Let the visual do the work — your job is to make students *feel* the difference, not describe the diagram.

"Raise your hand if you've ever written a PRD, waited weeks for engineering to build it, reviewed the result, and thought 'that's not what I meant.' Right. That loop — idea, spec, wait, feedback, wait, iterate — it's the PM hamster wheel. You spend more time describing what you want than testing whether it works."

Point to the right side of the slide: "Now look at what you've already been doing for three modules. You built first. You tested live. Today you'll extract the spec and connect the infrastructure. The documentation is the *output*, not the starting point."

Bring it to life with Shopify: "Tobias Lütke didn't write a spec for an e-commerce platform. He needed to sell snowboards online, couldn't find a tool he liked, so he built his own store. The store worked. Then his friends wanted one. Then strangers wanted one. The platform spec was extracted from a store that already had real customers and real transactions. He didn't predict the product — the product revealed itself through the build. That's the vibe loop. That's what you're doing today."


## Slide 9 — How to Move From Prototype to Production

This kicks off the teaching section. We'll cover when to transition, how to pay off comprehension debt, and the building blocks of a Living PRD.


## Slide 10 — The Production Threshold

The slide shows you the checklist — green side and red side. Don't just read them. Instead, make it personal.

"Here's a question I want you to sit with: could you explain what your prototype does, how the data flows, and what it's testing — *without* opening Lovable? If the answer is yes, you're probably ready to transition. If you need the demo to explain your own product, that's a signal to keep iterating."

Walk through the green column by giving examples, not definitions. "Proven hypothesis" means your M2 kill switch has a clear answer. "Stakeholders approved" means someone outside your build team has seen it and said go. "Explain without a demo" is the gut check — if you can whiteboard the logic in 2 minutes, you're there.

The red column is equally important. If you're still debating whether this is a dashboard product or a workflow product, don't lock it down yet. Premature structure is just as dangerous as no structure.

WhatsApp is the perfect cautionary tale in reverse. Jan Koum's first version was a status-update tool — "Jan is at the gym." When users started sending messages through the status feature, that was the signal. He didn't add production infrastructure to the status app. He waited until the product proved what it wanted to be — then he structured *that*. If he'd locked down the status tool with GitHub and docs, he'd have over-invested in the wrong product.

The real danger of waiting too long? Your AI-generated codebase becomes so tangled that even the AI can't maintain it. That's the ceiling. You'll feel it as prompts that break things that used to work.


## Slide 11 — Paying Off Your Comprehension Debt

The slide shows a formula. Don't read it — tell them what it means through an experience they just had.

"Think back to the reflection exercise. Most of you opened your code view and went 'I have no idea what half of this does.' That feeling? That's comprehension debt. You traded understanding for speed — and that was the right trade at the time. Modules 1 through 3 were about momentum, not legibility. But debt has interest. The longer you wait, the harder it is to explain your own product."

Here's how to make this concrete: "Imagine your VP pings you on Slack and says 'walk me through the technical architecture of your prototype.' Right now, you'd probably open Lovable and click through screens. That's a demo, not an explanation. The Living PRD is the difference — it forces the AI to articulate the logic that's buried in the code. Think of it as the AI writing the technical memoir of your build."

The equation on screen is the anchor they'll remember: working prototype plus documented evidence equals something an engineer can actually run with. Without both halves, you've got either a spec nobody believes or a build nobody can maintain.


## Slide 12 — The Eight Building Blocks of a Living PRD

The slide already lists all eight blocks — students can read them. Your job is to tell them which blocks surprise people and which ones catch the most gaps.

"Eight blocks sounds like a lot. It's not. The AI populates most of this from your existing build. But there are three blocks that consistently reveal things students didn't know about their own prototype."

Highlight these three:

**Technical Reality** — "This is where the AI tells you what's real and what's smoke and mirrors. Every one of you has mocked data in your prototype. This block makes you face it. You can't hand off a product to engineering and then say 'oh, that data is fake' after they've built on top of it."

**Assumptions & Risks** — "This one is uncomfortable. The AI will surface assumptions you didn't even know you were making. Kill switch triggers, technical failure points, confidence levels. Most students read this block and go 'huh, I never thought about that.' That's the point."

**Engineering Recommendation** — "This is the 'start here' guide. Build order, open questions, effort levels. An engineer reads this block first. If it's vague, everything else is wasted."

The other five blocks — Product Overview, Problem & Hypothesis, User Flow, Success Metrics, Scope — tend to populate cleanly because they mirror what you've already built and tested. Don't over-explain them now; students will fill them in during the lab.

"I'll drop the Living PRD Extractor link in Slack. You'll use it to generate all eight — the tool walks you through each one."

Think about why GitHub adopted the open-source convention of structured READMEs and contributing guides. The most popular repos aren't the ones with the best code — they're the ones where a stranger can understand the project in 5 minutes and start contributing. That's the bar your Living PRD should clear.


## Slide 13 — Living PRD Example Snapshot

Don't linger here — the example speaks for itself. Just orient them.

"This is a completed Living PRD for a sample product. Scroll through it and notice the difference from a traditional spec — every section is grounded in what the prototype actually does, not what someone hoped it would do. Yours will look like this in about 20 minutes. Link is on screen."


## Slide 14 — From Prompt Pack to Product Spec

The slide shows the distinction between a traditional PRD and a Living PRD. Don't read it — flip it into a question.

"How many of you have written a PRD before starting a project? Okay. And how many of those PRDs actually matched the shipped product? Exactly. Traditional specs are predictions. They're written before you know anything. The Living PRD is different because it's written *after* you know everything — the build already exists."

Connect the dots back to their M3 work: "Look, you're not starting from zero here. Your hypothesis? You defined it in M2. Your screens? You built them across M2 and M3. Your user flows? They're live in Lovable right now. The Living PRD just formalizes what you've already created. It's more like an audit than a writing exercise."

Land this: "Your Prompt Pack from M3 — the one that maintained your design system, your data model, your component names — that's your evidence trail. It feeds directly into the spec. The prompts are the breadcrumbs that explain how you got here."


## Slide 15 — Individual Exercise: Extract Your Living PRD

**ACTION: Give students 10-12 minutes. Walk the room. Drop the Living PRD Extractor link in Slack.**

"The steps are on screen. Here's what matters most — this is an audit, not an aspiration exercise. You're documenting what your prototype *actually* does right now, not what you wish it did. If the AI says a feature is mocked, don't fix it — write it down. Honesty now saves you a painful conversation with engineering later."

The slide walks them through six steps. Give them a quick orientation before they start: "Open the Extractor tool — link's in Slack. Pick your scenario, customize the extraction prompt with your screen count and hypothesis, paste it into Lovable, and let the AI generate your spec. Then move the output back into the Extractor to populate all eight sections."

Set the pace: "You've got about 10 minutes. Don't try to perfect every section. Get the extraction done, read through it, and flag anything that feels wrong. We'll clean it up later."

**Watch for:** The common reaction is surprise — "It actually described my product correctly." That's the first wow. If their PRD has obvious gaps or misrepresentations, tell them to flag it and re-prompt with more specific instructions.


## Slide 16 — The Three Pillars of an Engineering-Ready System

The slide lists the three pillars. Frame them as problems students already feel, not abstract requirements.

"You've got three problems right now. First — your code is unreadable. You saw that in the reflection. That's what refactoring solves. Second — your code is in GitHub from Module 2, but what's in that repo is a mess. Unreadable component names, no README, no structure. Version control doesn't help if what you're versioning is chaos. That's what today's refactor fixes. Third — every piece of data in your prototype is fake. Hardcoded names, dummy metrics, simulated flows. That's what Supabase solves."

Make the engineering connection relatable: "None of this requires you to become a developer. You already did the hard part — you built the product. These steps are about making the build *portable*. Think of refactoring as giving your code a proper filing system. Your GitHub repo is already there — now we make what's inside it worth cloning. And Supabase swaps out the cardboard props for real furniture."

The key reassurance: "You'll do all of this in the labs. Each one is a click or a prompt. Lovable handles the wiring. Your job is to decide *what* gets structured, not *how* — and that's a product decision, not an engineering one."


## Slide 17 — Break

Quick 5-minute break. Grab some water, stretch, and we'll be right back.


## Slide 18 — Cameras On

Welcome back! Quick reminder — it's always better to see your smiling face. Be present and visible to stay engaged and keep interactions valuable.


## Slide 19 — Refactor Your Prototype Code and Generate Your Eng Handoff

Connect this back to the demo: "Remember what I did to the Retention Engine in 8 minutes? You already extracted your Living PRD in the earlier exercise. Now you're going to do the rest: refactor the code, get the README, generate the engineering handoff, connect GitHub, and connect the backend. Same steps. Your build, your hands."


## Slide 20 — Hands-On Lab: Refactor & Generate Handoff

**ACTION: Give students 15-20 minutes. Walk the room continuously.**

Frame this as the next phase of the transformation from the demo: "You've already got your Living PRD from the earlier exercise. Now you're doing what I did first in the demo — refactoring the code and generating the engineering handoff. After this lab, you'll connect GitHub and the backend. By the end of today you'll have the complete package — exactly what I showed you in the demo."

"Before you dive in — start by opening Code View and looking at your file tree. Notice how messy it is. That's your before picture. After you paste the refactor prompt, switch back to Code View immediately and watch the file names change in real time. That transformation is the moment it clicks."

Guide the flow: "Refactor first — that gives you clean component names and a README. Then handoff — that generates the 'Start Here' guide and data model documentation. Both outputs go back into your Living PRD Extractor — that's your single source of truth now."

**Watch for:** After the refactor, walk up to students and ask: "Find your dashboard component. What was it called 5 minutes ago?" That contrast sticks.

If the code view still shows generic names after the prompt, tell them to re-prompt — it means the refactor didn't fully land.

Common trap: students get excited about refactoring and want to keep going. Pull them back. "The clean code is satisfying, I know. But the handoff document matters more. An engineer can rename a file in 10 seconds. They can't guess your data model or your intended build order."


## Slide 21 — Breakout: The Inheritance Test

**ACTION: Create breakout pairs. 15 minutes total — 7 minutes per round + 1 minute buffer.**

Set the stakes before you split them up: "We're going to do the most honest handoff test there is. This isn't 'read my doc and tell me if it makes sense.' This is: *your partner clones your repo, opens it in their AI tool, and asks the agent — not you — to explain your product.* That's how PMs at Indeed, Linear, Vercel, and a growing list of AI-first companies actually collaborate today. The repo is the spec. The agent is the reading interface."

"There's no Confluence in this workflow. No 30-page doc nobody reads. There's a GitHub repo with a Living PRD, a handoff note, the prototype, and enough context for an agent to answer any question a teammate has. Today you're going to find out if your repo passes that test."

**How it runs:**

1. **Swap GitHub repo URLs in the chat.** No verbal explanation. No screen share of Lovable. Just the URL.
2. **Clone or fork your partner's repo into your AI tool of choice.** Cursor, Claude Code, Lovable's agent on the imported project, ChatGPT with the repo attached — whatever you use. The point isn't the tool. The point is that an AI is reading the repo, not you.
3. **Ask the agent these 5 questions** (paste them in one go):
   - What does this product do, and who is it for?
   - What hypothesis is it testing?
   - What's real vs. what's mocked?
   - What are the 3 biggest technical decisions an engineer needs to make next?
   - If you had to ship a fix on Friday, which file would you open first?
4. **Compare the agent's answers to your partner's actual intent.** Where did the repo communicate clearly? Where did the agent guess, hallucinate, or get it wrong? *That's your data.*

"This is the future of PM handoffs. Your engineer doesn't read your PRD on Monday morning — they point their agent at your repo and ask it questions. If the agent can't answer them, neither can the engineer. The gap between what the agent gets right and what your partner *meant* is the gap in your documentation."

**Watch for:** The moment a student says "the agent got everything except [X]" — that [X] is the section they need to rewrite. Point it out: "That's not the agent's failure. That's a gap in your repo. Fix it before Module 5."

Also call out the moment when the agent surfaces something the *partner* didn't realize was unclear. Cursor canvases, Claude artifacts, ChatGPT summaries — they expose the gaps a human reader would politely paper over. That's why this works.

If a student is struggling because their repo doesn't have a PRD + handoff yet — that's data too. Their lab output isn't complete. Send them back to finish.

After the swap, post one sentence in Slack: *"The biggest gap my partner's agent surfaced about my repo was ___."* Reply to 2 others.

**Why this exercise belongs here, not later:** Your Module 5 work assumes a teammate (or future you) can reload context from the repo. If the agent can't reconstruct your build today, M5 will compound the confusion. Catch it now.


## Slide 22 — Connect Your Backend with Supabase

"One step left. You've got the Living PRD, clean code, a README, the engineering handoff, and your code has been in GitHub since Module 2. Now we give your prototype a real backend. This is the last piece from the demo."


## Slide 23 — Hands-On Lab: Connect Supabase

**ACTION: Give students 10-15 minutes. Walk the room. This is the infrastructure moment.**

"Steps are on screen. This is the fastest lab of the day — most of you will finish in under 10 minutes. Prompt Lovable to add a database feature — something like saving user progress or storing form submissions. Lovable Cloud will prompt you to enable — click Allow. Database, auth, storage, and edge functions are now live."

The emotional arc matters here. When database tables appear that match their prototype's data model, that's the wow moment.

Walk the room and narrate what you see: "Who's got database tables? Go look at them. Those column names match your prototype. That's not a preview anymore — that's infrastructure." And: "Open your GitHub repo. Your refactored code is already there from Module 2, but now look at it — clean component names, a README, the engineering handoff. That repo went from messy M2 code to something an engineer could clone and sprint from."

Last step they often forget: updating their Living PRD with the database URL. Remind them — the PRD is the single source of truth, and it needs to reflect the infrastructure they just connected.


## Slide 24 — Module 4 Complete: What You Accomplished Today

The slide shows the summary stats. Don't just read them — connect each number to what changed.

"Let's take stock. At the start of this session, you had a polished prototype with unreadable code, no documentation, and no way for anyone else to work on it. Now look at where you are."

Tick through the wins conversationally: "You've got a Living PRD — eight sections that describe exactly what your product does, what's real, what's mocked, and where to go next. You didn't write that from a template. You extracted it from something that already works. That's fundamentally different."

"Your code has real names. An engineer can open your file tree and immediately understand the structure. And you've got a handoff document that tells them where to start — not 'figure it out,' but 'open this file, here's the data model, here are the three biggest decisions you need to make.'"

"And your prototype lives outside of Lovable. It's been in GitHub since Module 2 — but now what's in that repo is clean, documented, and structured. And it's backed by a real database. If your laptop caught fire right now, your work survives."

Land the new mental model from the Inheritance Test: "Your repo is your spec. Not Confluence. Not a Google Doc. The repo. A teammate clones it, points their agent at it, and gets up to speed in minutes — not days. That's the workflow PMs are running at the most AI-fluent companies right now. You just built one of those repos. The follow-the-Repo-Structure-template document in `Templates/` shows you what the canonical layout looks like — use it as your reference for what goes where."

Land the project deliverable reminder: "Before you close out — copy your `livingprd.md` into slide 7 and your `engineeringhandoff.md` into slide 9 of your final deliverables deck. Make sure both are committed to your repo with descriptive filenames. Do it today while it's fresh."


## Slide 25 — Key Takeaways

The slide shows three formal takeaways. Deliver them through a story they'll remember.

"Quick story. In 2007, Justin Kan strapped a camera to his head and launched Justin.tv — a platform where anyone could livestream anything. General purpose. No focus. Lifecasting, cooking shows, people filming their cats. It had users, it had investors, and it had no identity. The platform was a black box of content with no clear product thesis."

"But the data told a different story. One category kept growing while everything else flatlined: gaming. Gamers were streaming themselves playing, watching each other play, building communities around specific games. The Justin.tv team didn't plan for this. They discovered it by looking at what users were actually doing — not what the team hoped they'd do. So they extracted the spec from the evidence: gaming livestreaming is the product. That's the first takeaway — **extract instead of predict.** Your Living PRD does the same thing. It pulls the product definition from a working build, not from a brainstorm."

"Then came the hard part. Justin.tv's codebase was built for general-purpose streaming. To turn the gaming category into a real product, they had to refactor everything — new component names that reflected gaming, separate data models for channels and viewers, documentation that any new engineer could follow. They didn't rebuild from zero. They restructured what already worked and made it legible. That refactoring is what allowed them to go from a small team to a platform that could onboard hundreds of engineers. That's the second takeaway — **document as a byproduct of building.** When you refactored your code and generated the handoff today, you weren't doing extra work. You were making the build transferable."

"In 2011, they spun the gaming product out as its own thing — Twitch. Its own repo, its own infrastructure, its own database, its own brand. Justin.tv eventually shut down. Twitch didn't just survive — Amazon acquired it for nearly a billion dollars. It outlived the platform it was born inside because it had independent infrastructure. That's the third takeaway — **make the infrastructure real before you hand it off.** Your prototype just got a GitHub repo and a live database. It exists outside of Lovable now. It can survive without the tool that built it — and without you in the room."

Pause. Then: "Three takeaways on screen. You already lived them. You extracted your spec from evidence. You documented your build by restructuring it. And you gave your prototype infrastructure that stands on its own. That's the transition from prototype to production."


## Slide 26 — Extra Practice and Next Session

"Three optional exercises for anyone who wants to push further — all on screen."

Frame them as challenges, not homework: "The first one is fun and a little scary. You're going to intentionally break your prototype with a reckless prompt — then use your shiny new GitHub history to roll back to the last stable version. It's the best way to prove to yourself that version control actually protects you. If the rollback works, you'll never be afraid of a bold prompt again."

"The second one tests whether your prototype can handle reality. Open your Supabase dashboard, manually insert some garbage data — a negative price, a blank required field — and see what happens. Does your UI handle it gracefully, or does everything fall apart? This is the kind of thing that happens the moment real users touch a live product."

"The third is the **Outside Reader Test** — an extension of today's Inheritance Test. Share your repo URL with a non-PM friend (an engineer, a designer, a relative who's never seen the project). They clone it, open it in any AI tool, and ask the agent: *'In one paragraph, what is this product?'* If the agent's summary is something you'd be proud to ship to a stakeholder, your repo is ready for the wild. If it's not — that's your weekend work. The repo only counts as a spec if a stranger can extract the spec from it."

Preview the next session: "Module 5 is where your prototype goes live. Real URL. Real users. Real database with security rules. Everything we've set up — GitHub since Module 2, Supabase, the Living PRD, the engineering handoff, and a repo any agent can read — becomes the foundation for shipping. If Module 4 was about making your build legible to humans *and* agents, Module 5 is about making it durable under pressure."


## Slide 27 — Survey

At the end of each session, please scan the QR code or use the link to share your feedback. Your insights help us improve and make each cohort better than the last. We'd love to hear about your experience!


## Slide 28 — Bonus Resources

"All the links for today are on this slide — lab guide, Living PRD template, everything. Bookmark the PRD template in particular. You'll keep updating it through Module 5 and 6 as your prototype evolves. It's a living document, not a one-time assignment."


## Slide 29 — Q&A

Alright, before we close — any final questions? Anything about the Living PRD, the refactoring process, GitHub, Supabase, or how this feeds into Module 5. Feel free to unmute or drop your question in the chat. And as always, share questions in Slack if something comes up later. See you next session!
