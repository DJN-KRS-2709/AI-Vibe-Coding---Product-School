# Module 4: Transition From Prototypes to Production Specs — Speaker Notes

Casual talking points for each slide. Not a script — just the key things to say, what to do on screen, and the energy to bring. Module 4 is the hinge of the course — the first half ends here. The vibe shifts from "build" to "make it durable." Real examples from companies like Instagram, Stripe, GitHub, and WhatsApp to ground every concept.

**Tools referenced in this module:**
- Lovable (building, refactoring, connecting infrastructure)
- Living PRD Extractor (lab tool — extract and document the PRD)
- Living Prompt Pack Builder (continuing from M3 — add structure prompts)
- GitHub (version control — connect from Lovable sidebar)
- Supabase (database — connect from Lovable)

**What to prepare before class:**
- [ ] Open the M3 Retention Engine prototype in Lovable (same one carried from M2/M3 demos — now with prompt chain refinements, design system matching, and Living Prompt Pack applied)
- [ ] Have all prompts pre-typed in a text file, ready to paste (refactor, handoff)
- [ ] Have GitHub account logged in so the connection is instant
- [ ] Have Supabase ready (Lovable auto-generates the connection)
- [ ] Living PRD Extractor link ready to drop in Slack
- [ ] Lab guide and exercise links ready in Slack
- [ ] Screen share on

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

Module 4 — that's today — is where we enforce technical rigor. You'll convert your build into a version-controlled GitHub repository, formalize your logic into a Living PRD, and bridge the gap between your vision and an engineering handoff. This is where you stop being the only person who understands your product.

Module 5 ships it live — real databases, secure APIs, live URL, real users. And Module 6 closes the loop — you measure performance, use AI-driven analytics, and iterate based on evidence.


## Slide 4 — Agenda

Four things today.

First — The Black Box Gap. We'll look at what's actually under the hood of your M3 prototype. Spoiler: it's not pretty.

Second — How to Move From Prototype to Production. The theory behind the transition — when to do it, what the Living PRD is, and how it pays off your comprehension debt.

Third — Hands-on lab: Refactor your prototype code and generate your engineering handoff. You'll clean up the mess and produce a document an engineer can sprint from.

Fourth — Hands-on lab: Connect your infrastructure with GitHub and Supabase. One-click connections that move your prototype from a local preview to version-controlled code with a real database.


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

Here's the problem we're solving. Your prototype looks like a finished product — high-fidelity visuals, solid hypothesis, interactive states, the works. But if an engineer asked "How does the data flow?" or "Where is the logic for this screen?" — you'd be stuck digging through a messy file tree.

Stripe had this exact problem in their early days. Their first payment integration was brilliant from the user's perspective — 7 lines of code to accept payments. But behind the scenes, the early codebase was a tangle that only the Collison brothers could navigate. The moment they needed to scale the team, they had to stop and restructure everything. That's the transition we're making today — except you'll do it in 8 minutes instead of 3 months.

### STEP 1: Show the Facade (~2 min)

**What you do:** Pull up the M3 Retention Engine prototype in Lovable on screen share. Click through the screens — the 3-screen onboarding flow (team value → invite action → collaboration payoff), the retention metrics dashboard, the experiment summary. Remind them how polished it is.

**What you say:** "This is our M3 build. The onboarding flow that surfaces team invites to reduce churn. Three screens, design-system matched, interactive states, real user quotes and retention data embedded throughout. If your VP saw this, they'd think engineering built it."

**Then:** Switch to Lovable's code view. Let the mess sit on screen for 10 seconds. Don't explain it.

**What you say:** "Now look at the code. `Component1`. `handleClick2`. All logic in one file. No README. No documentation. This is what the engineer who inherits your prototype actually sees. This is the black box. Three prompts, two clicks — watch."

### STEP 2: Prompt 1 — Extract the Living PRD (~60 sec)

**Paste this prompt:**

> "Look at this entire prototype. Write a product requirements document that covers: what this product does, who it's for, the problem it solves, the screens and their purpose, the user flow from first screen to last, the hypothesis it tests, the key metrics, what's currently mocked vs. what would need real data, and recommended next steps for engineering."

**While it generates:** Stay quiet. Let the class watch the PRD appear.

**When it's done:** Read 2-3 sections aloud — Product Overview and Technical Reality are the most impactful.

**What you say:** "I didn't write this. The prototype wrote its own spec. The hypothesis — 'surfacing team invites during first-run onboarding increases Day-3 invite rate from 12% to 25%' — extracted from what we built, not imagined before building."

### STEP 3: Prompt 2 — Refactor the Code (~60 sec)

**Paste this prompt:**

> "Refactor the codebase. Rename all components to be descriptive (e.g., TeamValueScreen, InviteFlow, CollaborationPayoff, RetentionDashboard, ExperimentSummary). Separate data logic from display components. Group files by feature, not by type. Add a README.md that explains the project structure."

**While it generates:** "Watch the file tree on the left."

**When it's done:** Switch to code view. Show the before/after.

**What you say:** "`Component1` is now `TeamValueScreen`. `Component3` is now `InviteFlow`. There's a `/services` folder for data logic. There's a README. An engineer can read this on day one. Same product — readable code."

### STEP 4: Prompt 3 — Engineering Handoff (~40 sec)

**Paste this prompt:**

> "Generate an engineering handoff document: list every component and what it does, describe the data model (what's real vs. mocked), identify the 3 biggest technical decisions an engineer would need to make, and write a 'start here' guide."

**When it's done:** Read the "start here" section and one technical decision aloud.

**What you say:** "A new engineer joins the team Monday. They open this document. In 5 minutes, they know what the onboarding flow does, what's real, what's mocked, and where to start. That's the handoff."

### STEP 5: Connect GitHub (~30 sec)

**What you do:** In Lovable, click the GitHub integration button. One click. Code pushes to a real repo.

**What you do next:** Open the GitHub repo URL in a new browser tab. Show the file tree, the README, the refactored components.

**What you say:** "One click. Your code is now in a real GitHub repository. An engineer can clone this right now. It's not trapped in Lovable anymore — it's real version control."

### STEP 6: Connect the Backend (~30 sec)

**What you do:** Trigger the backend by prompting Lovable to add a feature that requires a database (e.g., "Save user onboarding progress to the database so returning users resume where they left off"). Lovable Cloud prompts you to enable — click Allow. Database, auth, storage, and edge functions are now live.

**What you do next:** Open the Lovable Cloud dashboard (Settings → Cloud). Show the database tables, the region, the live backend.

**What you say:** "One click. Your prototype has a real database, real auth, and real storage. This isn't a toy anymore. This is real infrastructure."

**Pause. Let it land.**

### STEP 7: Debrief (~2 min)

**What you say:**

"Same prototype. Same onboarding flow. Same screens testing the team invite hypothesis. But now it has:

- A Living PRD — complete spec, extracted from the build
- Clean code — `TeamValueScreen`, `InviteFlow`, not `Component1`
- An engineering handoff — component map, data model, start-here guide
- A GitHub repo — real version control
- A real backend — database, auth, and storage

Traditional PM workflow: research, spec, build, test. Vibe Coding workflow: build, test, extract the spec. The spec is the output, not the starting point. And the infrastructure follows the prototype — not the other way around.

You'll do all of this to your own build in the labs. But first — let's talk about *when* to make this transition and *how* the Living PRD works."

### THE PROMPTS (copy-paste version for your text file)

```
Prompt 1 — Extract:
Look at this entire prototype. Write a product requirements document that covers: what this product does, who it's for, the problem it solves, the screens and their purpose, the user flow from first screen to last, the hypothesis it tests, the key metrics, what's currently mocked vs. what would need real data, and recommended next steps for engineering.

Prompt 2 — Refactor:
Refactor the codebase. Rename all components to be descriptive (e.g., TeamValueScreen, InviteFlow, CollaborationPayoff, RetentionDashboard, ExperimentSummary). Separate data logic from display components. Group files by feature, not by type. Add a README.md that explains the project structure.

Prompt 3 — Handoff:
Generate an engineering handoff document: list every component and what it does, describe the data model (what's real vs. mocked), identify the 3 biggest technical decisions an engineer would need to make, and write a 'start here' guide.
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

Bring it to life with Instagram: "Kevin Systrom didn't sit in a conference room writing requirements for a photo-sharing app. He built Burbn — a messy, overloaded check-in app with a dozen features. Then he watched what users actually did. One feature kept winning: photos. The product spec wasn't written — it was discovered inside a working build. That's the vibe loop. That's what you're doing today."


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

"You've got three problems right now. First — your code is unreadable. You saw that in the reflection. That's what refactoring solves. Second — your code lives inside Lovable. If Lovable goes down, your work vanishes. That's what GitHub solves. Third — every piece of data in your prototype is fake. Hardcoded names, dummy metrics, simulated flows. That's what Supabase solves."

Make the engineering connection relatable: "None of this requires you to become a developer. You already did the hard part — you built the product. These three steps are about making the build *portable*. Think of refactoring as giving your code a proper filing system. GitHub is like saving your work to the cloud instead of a USB drive. And Supabase swaps out the cardboard props for real furniture."

The key reassurance: "You'll do all three in the labs. Each one is a click or a prompt. Lovable handles the wiring. Your job is to decide *what* gets structured, not *how* — and that's a product decision, not an engineering one."


## Slide 17 — Break

Quick 5-minute break. Grab some water, stretch, and we'll be right back.


## Slide 18 — Cameras On

Welcome back! Quick reminder — it's always better to see your smiling face. Be present and visible to stay engaged and keep interactions valuable.


## Slide 19 — Refactor Your Prototype Code and Generate Your Eng Handoff

Time to get our hands dirty. You're about to clean up the black box and produce a document that makes your code legible to anyone.


## Slide 20 — Hands-On Lab: Refactor & Generate Handoff

**ACTION: Give students 15-20 minutes. Walk the room continuously.**

"Steps are on screen. Before you dive in — two things. First, start by opening Code View and looking at your file tree. Notice how messy it is. That's your before picture. Second, after you paste the refactor prompt, switch back to Code View immediately and watch the file names change in real time. That transformation is the moment it clicks."

Guide the flow without reading the slide: "Refactor first, then handoff. The refactor prompt cleans up names and file structure. The handoff prompt generates your 'Start Here' guide. Both outputs go back into your Living PRD Extractor — that's your single source of truth now."

**Watch for:** After the refactor, walk up to students and ask: "Find your dashboard component. What was it called 5 minutes ago?" That contrast sticks.

If the code view still shows generic names after the prompt, tell them to re-prompt — it means the refactor didn't fully land.

Common trap: students get excited about refactoring and want to keep going. Pull them back. "The clean code is satisfying, I know. But the handoff document matters more. An engineer can rename a file in 10 seconds. They can't guess your data model or your intended build order."


## Slide 21 — Breakout: Show and Swap Your Spec Handoff Package

**ACTION: Create breakout pairs. 10 minutes total — 5 minutes per round.**

Set the stakes before you split them up: "Here's the test. You're going to screen share your Living PRD and Engineering Handoff with a partner. They read it in silence for 3 minutes — no questions, no verbal walkthrough, no 'oh let me explain this part.' Just the document. If they can understand your product from the docs alone, your handoff works. If they can't, you've got more work to do."

"This isn't an academic exercise. This is what happens when an engineer inherits your project on a Monday morning. They don't get a demo. They get a repo and a doc. Can they ship something by Friday?"

After the silent reading, have them discuss three things: Can you identify what the product does and who it's for in under a minute? Is it clear which parts are real and which are mocked? And does the handoff point to a specific starting place — or is it 'good luck, figure it out'?

Stripe runs this exact test with new hires. Day one: here's the docs, here's the codebase, build something. If they ship in the first week, the documentation did its job.

**Watch for:** The moment a partner accurately describes their classmate's product without any verbal help — that's the breakthrough. Point it out when you see it. "Your docs just survived the handoff test."


## Slide 22 — Connect Your Infrastructure with GitHub and Supabase

The final lab. This is where your prototype moves from a local preview to a real engineering environment.


## Slide 23 — Hands-On Lab: Connect GitHub and Supabase

**ACTION: Give students 10-15 minutes. Walk the room. This is the infrastructure moment.**

"Steps are on screen. This is the fastest lab of the day — most of you will finish in under 10 minutes. Start with GitHub: hit the icon in the Lovable sidebar, follow the prompts, and check your GitHub account for the initial commit. Once that's confirmed, prompt Lovable to add a database feature, and watch the backend spin up."

The emotional arc matters more than the mechanics here. This is the wow moment of the module. When they open their GitHub account and see real code in a real repo, let that land. When database tables appear that match their prototype's data model, that's the second hit.

Walk the room and narrate what you see: "Who's got their first commit? Open that repo — look at the README, the refactored components. That's yours. An engineer could clone it right now and start building." And: "Who's got database tables? Go look at them. Those column names match your prototype. That's not a preview anymore — that's infrastructure."

Students who already have GitHub accounts will breeze through — have them pair up with anyone who's creating accounts for the first time. Don't let setup friction kill the energy.

Last step they often forget: updating their Living PRD with the new repo and database URLs. Remind them — the PRD is the single source of truth, and it needs to reflect the infrastructure they just connected.


## Slide 24 — Module 4 Complete: What You Accomplished Today

The slide shows the summary stats. Don't just read them — connect each number to what changed.

"Let's take stock. At the start of this session, you had a polished prototype with unreadable code, no documentation, and no way for anyone else to work on it. Now look at where you are."

Tick through the wins conversationally: "You've got a Living PRD — eight sections that describe exactly what your product does, what's real, what's mocked, and where to go next. You didn't write that from a template. You extracted it from something that already works. That's fundamentally different."

"Your code has real names. An engineer can open your file tree and immediately understand the structure. And you've got a handoff document that tells them where to start — not 'figure it out,' but 'open this file, here's the data model, here are the three biggest decisions you need to make.'"

"And your prototype now lives outside of Lovable. It's in GitHub with version history. It's backed by a real database. If your laptop caught fire right now, your work survives."

Land the project deliverable reminder: "Before you close out — copy your Living PRD into slide 7 and your Engineering Handoff into slide 9 of your final deliverables deck. Do it today while it's fresh."


## Slide 25 — Key Takeaways

The slide shows three formal takeaways. You're going to deliver them through a single story instead of reading bullets.

"Let me close with a story you've been living through all day — you just didn't know it was someone else's story too."

"In 2010, Kevin Systrom had a build that looked like a product but wasn't. Burbn — check-ins, photo sharing, gaming, social features, a dozen things crammed together. Users were on it. Investors had funded it. And nobody — including Systrom — could explain what it actually *was*. Sounds a lot like a Module 3 prototype with no Living PRD, right? Features everywhere, no clarity."

"So he did exactly what you did today. He looked at the evidence — not what he hoped users would do, but what they were already doing. One feature dominated: photos. He didn't write a spec first. He let the build tell him what the product was. That's the shift from guessing to extracting. Your Living PRD does the same thing — it pulls the spec from reality, not from a planning meeting."

"Then Systrom and Krieger refactored. Same codebase, radically restructured. Generic modules became purposeful features. They stripped everything that didn't serve the photo-sharing flow. Renamed, reorganized, documented. That refactoring — from tangled experiment to clean architecture — is why 13 engineers could serve 30 million users. Sound familiar? You just did that to your code 20 minutes ago."

"And when Facebook acquired them for a billion dollars, hundreds of engineers needed to understand what 13 people had built. They could — because the code was readable, the architecture was documented, and the infrastructure was real. GitHub. Real databases. Clean handoffs. That's why we connected your prototype to version control and a live backend today. Your build can now survive without you in the room."

Pause. Then: "Three takeaways on screen. But you already lived them. Extract instead of predict. Document as a byproduct of building. And make the infrastructure real before you hand it off."


## Slide 26 — Extra Practice and Next Session

"Two optional exercises for anyone who wants to push further — both are on screen."

Frame them as challenges, not homework: "The first one is fun and a little scary. You're going to intentionally break your prototype with a reckless prompt — then use your shiny new GitHub history to roll back to the last stable version. It's the best way to prove to yourself that version control actually protects you. If the rollback works, you'll never be afraid of a bold prompt again."

"The second one tests whether your prototype can handle reality. Open your Supabase dashboard, manually insert some garbage data — a negative price, a blank required field — and see what happens. Does your UI handle it gracefully, or does everything fall apart? This is the kind of thing that happens the moment real users touch a live product."

Preview the next session: "Module 5 is where your prototype goes live. Real URL. Real users. Real database with security rules. Everything we set up today — GitHub, Supabase, the Living PRD — becomes the foundation for shipping. If Module 4 was about making your build legible, Module 5 is about making it durable under pressure."


## Slide 27 — Survey

At the end of each session, please scan the QR code or use the link to share your feedback. Your insights help us improve and make each cohort better than the last. We'd love to hear about your experience!


## Slide 28 — Bonus Resources

"All the links for today are on this slide — lab guide, Living PRD template, everything. Bookmark the PRD template in particular. You'll keep updating it through Module 5 and 6 as your prototype evolves. It's a living document, not a one-time assignment."


## Slide 29 — Q&A

Alright, before we close — any final questions? Anything about the Living PRD, the refactoring process, GitHub, Supabase, or how this feeds into Module 5. Feel free to unmute or drop your question in the chat. And as always, share questions in Slack if something comes up later. See you next session!
