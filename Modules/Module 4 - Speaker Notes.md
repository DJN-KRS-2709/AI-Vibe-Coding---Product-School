# Module 4: Transition From Prototypes to Production Specs — Speaker Notes

> Talking points for each slide. Not a verbatim script — the key things to say, what to do on screen, and the energy to bring. **Module 4 is the engineering transition** — the moment students stop being prototype-makers and start being system-designers who can hand a build to an engineer cold.


## Tools referenced in this module

- **Lovable** — building, refactoring, connecting infrastructure (paste prompts directly into chat).
- **GitHub** — version control. Connected from Lovable in M2; today's deliverables push here as `04-structure/PRD.md` and `HANDOFF.md`.
- **Supabase / Lovable Cloud** — real PostgreSQL database, auth, and storage. Provisioned by Lovable.
- **Living PRD Sample (SnapWishlist)** — the reference exemplar in `Templates/`. Use as a "what good looks like" comparison after Lovable extracts the PRD.

## What to prepare before class

- [ ] M3 Retention Engine prototype open in Lovable (same project carried from M2/M3 demos).
- [ ] Pre-typed prompts in a text file, ready to paste: extract PRD, refactor, engineering handoff, Supabase setup.
- [ ] GitHub account logged in (no auth pause mid-demo).
- [ ] Slack channel open with links: Lab Guide, Frameworks Reference Card, Living PRD Sample.
- [ ] Screen share on.

## Before we start

Thank students for the survey feedback so far. Repeat the question protocol: raise hand for live questions; drop in chat; or Slack anytime. Keep momentum.

---

## Slide 1 — Transition From Prototypes to Production Specs

Open hot. Today is the graduation moment — students walked in with a polished M3 prototype, and the job is to make them confront how unreadable that code actually is to an engineer. Then hand them the tools to fix it.
One sentence to set the table: *"Module 3 proved you can build something resilient. Module 4 proves you can hand it to an engineer without losing an hour explaining it."* The shift is identity: from prototype-maker to system-designer.
Three artefacts must exist in their GitHub repo by end of class: `04-structure/PRD.md`, `HANDOFF.md`, and a connected backend (Supabase or Lovable Cloud). The repo is the deliverable — not anything that lives in a tool's browser cache.

---

## Slide 2 — Class Expectations

30 seconds. Same expectations as every module — but call out Tool Readiness specifically today: students need their M3 Lovable project, GitHub account, and (if used in M3) Supabase open **before** the lab starts. The lab is 25 minutes including a Supabase setup. Students hunting for credentials during the lab lose 5 minutes of build time.
Reinforce Slack as the help channel — instructor will be checking it during exercises.

---

## Slide 3 — The Course Arc

15 seconds. Skip if running long. The point is to remind them this is the bridge module — M1-M3 was speed and resilience, M5-M6 is going live and measuring. Today is the transition that makes everything after possible.

---

## Slide 4 — Today's Agenda

30 seconds. The three sections map to a clear arc: *name the gap → close it → harden it*. Tell them the lab at the end is where the actual artefacts get created — everything before it is preparation.

---

## Slide 5 — Section 01 · The Black Box Gap

*(No speaker notes on this slide — silent transition.)*

---

## Slide 6 — Reflection · M3 Code Check

10 minutes total. Keep all students in the main room. Ask for *one* volunteer to screenshare their Lovable project — walk them through clicking the Code tab, expanding `src/pages`. Everyone else does it simultaneously on their own builds. Stress that while you're walking one student through, the rest are following along, not watching.
Once everyone is in code view, open the three questions and give 1 minute to look around before discussing. Prompt: *"Don't overthink it, just tell me what you see."* No wrong answers, but make the technical debt visible — UI looks great, infrastructure is not engineering-ready.
If responses are slow, run a quick show of hands instead: *"Who has files named like Component_1 instead of descriptive names? Who has a README that actually explains the data flow? Who feels confident an engineer could fix a bug here without a 30-minute meeting first?"*
Land it: *"You've built high-fidelity. Today you're building a Product. M3 was about precision and polish. M4 is graduation — you're moving from AI-managed code to engineer-managed code by cleaning up the file tree and generating the documentation that turns a prototype into a real asset."*

---

## Slide 7 — Demo · The Exterior vs. The Hood

**Setup before play (~30 sec):** *"Here's the problem we're solving. Your prototype looks like a finished product — high-fidelity visuals, solid hypothesis, interactive states. But if an engineer asked 'How does the data flow?' or 'Where is the logic for this screen?' — you'd be stuck digging through a messy file tree. Watch what happens when we run four prompts."*
**Step 1 — Show the Black Box.** M3 Retention Engine in Lovable. Click through the polished screens, then switch to code view. The file tree shows generic names — `screen five`, `handleClick2`, everything in one file, no README. Voice over: "This is our M3 build. Five screens, design-system matched, interactive states, real user quotes. If your VP saw this, they'd think engineering built it. Now look at the code. `screen five`. `handleClick2`. All logic in one file. No README. This is what the engineer who inherits your prototype actually sees. This is the black box."
**Prompt 1 — Refactor the Code.** Paste the refactor prompt. The file tree transforms — component names change, a `/services` folder appears, a `README.md` generates. Voice over while generating: *"Watch the file tree on the left."* When done: "`Component1` is now `TeamValueScreen`. `Component3` is now `InviteFlow`. There's a `/services` folder for data logic. There's a README. An engineer can read this on day one. Same product — readable code."
**Prompt 2 — Extract the Living PRD.** Paste the PRD extraction prompt. A `PRD.md` file appears with Product Overview, Problem & Hypothesis, User Flow, Technical Reality, etc. Let it generate in silence. When done: *"I didn't write this. The prototype wrote its own spec. The hypothesis — 'surfacing team invites during first-run onboarding increases Day-3 invite rate from 12% to 25%' — extracted from what we built, not imagined before building."*
**Prompt 3 — Generate the Eng Handoff.** Paste the handoff prompt. `HANDOFF.md` generates with component list, data model, top 3 technical decisions, "start here" guide. When done: *"A new engineer joins the team Monday. They open this document. In 5 minutes, they know what the onboarding flow does, what's real, what's mocked, and where to start. That's the handoff."*
**Prompt 4 — Connect Supabase.** Prompt Lovable to add a database. Lovable Cloud / Supabase asks to enable. Click Allow. Database, auth, storage spin up. Dashboard shows real tables. Voice over: *"Your prototype has a real database, real auth, and real storage. This isn't a toy anymore. This is real infrastructure."*
**Pause and land it:** *"Same prototype. Same onboarding flow. Same hypothesis. But now it has clean code, a Living PRD, an engineering handoff, GitHub from Module 2 with refactored code, and a real backend. Coming up next, you'll do the same for your own project."*
**If short on time:** play the video at 1.5× during the generation phases. The four prompts and what they produce matter more than watching them generate in real-time.

---

## Slide 8 — The New Operating Model

As you just identified in Slack, your M3 code is likely a black box to an engineer. To bridge that gap, you have to shift your fundamental operating model. You are moving away from using documents to describe what *might* happen and toward using functional builds to prove what *does* happen.
**The Old Way was the Dependency Loop.** The Spec was your starting point — your best guess at requirements before any code was written. Because you couldn't build it yourself, you were forced into a cycle of waiting for Design and Engineering just to see a mock-up. Your spec was the Input, and your role was a Requestor dependent on other people's time to validate a hypothesis.
**The New Way is the Vibe Loop.** Your prototype is the source of truth. You start by manifesting the logic and testing the live app yourself. You iterate in real-time until the product works. The Spec is no longer the starting point — it's the Output. You aren't giving an engineer a document of assumptions; you are giving them a functional system as evidence of what is already validated.
The shift here is about what you trade. You stop trading static documents that represent guesses and you start trading live links and extracted specs that represent proven logic. Now that you understand that the spec is the output of your build, you need to know exactly *when* to trigger that output so you don't waste time documenting ideas that are still changing — which is exactly what the next slide covers.

---

## Slide 9 — Section 02 · From Prototype to Production

*(No speaker notes on this slide — silent transition.)*

---

## Slide 10 — The Production Threshold

Moving into production requires a higher level of rigor, so as PMs, you have to decide exactly when to stop iterating on vibes and start hardening your build. Not every prototype is meant to be a product.
**The "Move to Production" checklist is your signal that discovery is over.** You cross this threshold when your core hypothesis — that "Kill Switch" you named back in Module 2 — is no longer an assumption, but proven evidence. At this point, you have stakeholder alignment to move forward, and your focus shifts from *seeing if it works* to *ensuring it is durable*. You're ready when you can articulate the logic clearly enough to guide an engineer, rather than just clicking through a vibe and hoping for the best.
**Stay in the Prototyping loop as long as the cost of change is still high.** If your direction is fluid or your business rules are changing every ten minutes, don't move to production specs yet. Hardening a build by connecting GitHub, cleaning code, and setting up databases adds friction to your speed. Stay here when discovery is still your primary goal and you need the freedom to break and rebuild in seconds.
Here's the gut check to give them: *"Could you explain what your prototype does, how the data flows, and what it's testing — without opening Lovable? If yes, you're probably ready. If you need the demo to explain your own product, that's a signal to keep iterating."*

---

## Slide 11 — Paying Off Your Comprehension Debt

If you've reached the point where your prototype is functional and your direction is clear — and you're ready to pull the trigger on the production transition — you have to address the "black box" of code that has been growing behind the scenes before you can move into a real engineering environment.
In the previous modules, you focused on build speed. But that speed comes at the cost of **Comprehension Debt** — the gap that forms when the AI understands the underlying logic of your app better than you do. To close that gap, you use the Living PRD.
Think of this as your technical translation layer. Instead of you trying to manually decode thousands of lines of AI-generated files, you force the AI to explain the functional rules it manifested during your rapid build. This isn't about writing a document from scratch; it's about extracting the operational reality of your app so you can maintain total ownership of the system.
Make this concrete: *"Imagine your VP pings you on Slack and says 'walk me through the technical architecture of your prototype.' Right now, you'd probably open Lovable and click through screens. That's a demo, not an explanation. The Living PRD is the difference — it forces the AI to articulate the logic that's buried in the code. Think of it as the AI writing the technical memoir of your build."*
Now that they understand *why* the Living PRD matters, the next slide breaks down *what's in it* — the eight specific building blocks.

---

## Slide 12 — The Eight Building Blocks

Here are the eight specific building blocks that turn your prototype into a professional-grade specification:
**1. Product Overview** — high-level summary of the validated system. Defines exactly what the tool does and who it's for so the engineer understands context before looking at code.
**2. Problem & Hypothesis** — clear definition of user friction and the evidence-backed intervention. Explains the *why* so the team stays aligned on the goal.
**3. User Flows & Screen Map** — visual and descriptive map of navigation and interactive logic. Documents the screen-by-screen flow that already exists in your functional prototype.
**4. Success Metrics** — North Star + leading indicators used to measure production performance. Defines exactly how you'll prove the product is working once it's live.
**5. Technical Reality** — your Truth vs. Mock report. Explicitly documents which parts of the logic are fully functional and which are hard-coded or simulated.
**6. Assumptions & Risks** — confidence levels and Kill Switch triggers. Identifies specific technical boundaries or potential failure points the engineer needs to watch for.
**7. Scope — In vs. Out** — definitive list of what's included and what's excluded. Sets clear boundaries to prevent scope creep during the transition.
**8. Engineering Recommendation** — strategic guide for build order. Since you've already manifested the logic, you can provide effort estimates and highlight open architectural questions.
By extracting these eight blocks, you turn a black box of AI code into a professional specification and a documented system for handoff.

---

## Slide 13 — Living PRD · Sample Snapshot

Optional pause: if you have time, walk through this example. Otherwise, briefly point out that the SnapWishlist sample lives in their repo (`Templates/Living-PRD-Sample-SnapWishlist.md`) and they should reference it as a guide.
The key insight to surface: notice the "Technical Reality" row mentions **mocked** elements explicitly. The Living PRD's job is to document the truth — including limitations. Students often want to hide what's mocked. Push back: *"You're not losing points for missing features. You're gaining points for documenting the truth."*
If you have time, also show the remaining four blocks (Success Metrics, Assumptions & Risks, Scope, Engineering Recommendation) by opening the markdown file directly. Otherwise, defer to self-study.

---

## Slide 14 — From Prompt Pack to Product Spec

One of the biggest pain points in a PM's life is the **PRD dread** — that moment you have to sit down at a blank document and try to remember every edge case and logic flow you discussed weeks ago. The beauty of the vibe coding workflow you've been following is that because you've been building with precision, the work is already done. You're simply *extracting* the intelligence you've already embedded in your prototype.
**The Intent (Hypothesis & Data Packs from M2):** Because you didn't just build a generic app — but one grounded in specific user friction and evidence-backed data — the *why* of your product is already baked in. The AI doesn't need to hallucinate a strategy; it's auditing the strategic intent you've been injecting since day one.
**The Architecture (Prompt Chaining from M3):** Your M3 work is the real hero here. Because you moved beyond simple one-off prompts and used structured Expansion and Behavior chains, your code contains deep logic — it knows what happens when a user clicks save, or what the empty state looks like. The AI isn't guessing your navigation; it's translating those functional paths back into a formal User Flow and Screen Map.
**The Reality (Baseline Code):** Finally, because you have a functional prototype sitting in your editor, your codebase has become a measurable asset. Instead of a wish list of what an app should do, the AI performs a literal audit of your actual files. It provides an honest Truth vs. Mock report.
Now they're ready for the exercise — they have everything they need to extract.

---

## Slide 15 — Extract Your Living PRD

15 minutes. Emphasise that this is an **audit, not a creation**. Students often feel the need to polish their code before running this prompt — stop them. The value is capturing reality. If their database isn't connected or their logic is mocked, the PRD should say exactly that.
Hard rule: **do NOT fix the code yet**. The point of this exercise is the honest extraction. If they start refactoring during PRD extract, they'll fall behind for the lab.
Group dynamics: use Zoom breakout pairs ("co-working" environment) so they build in the presence of peers. If they hit a snag, they hop back to the main room.
Critical: at T+12 min remind everyone to commit `PRD.md` to GitHub. If they leave without that file pushed, the next lab (refactor) won't have a screen-name source to reference.
If Lovable seems confused about what the product is, prompt: *"Audit the existing files and our previous conversation to find these details."*

---

## Slide 16 — Break

Literal break. Don't fill it with content. Re-launch with the Cameras On slide.

---

## Slide 17 — Cameras On

Same as every module — cameras on for the lab. Re-energise the room.

---

## Slide 18 — Section 03 · The Engineering Handoff

*(No speaker notes on this slide — silent transition.)*

---

## Slide 19 — Lab · Refactor + Handoff

25 minutes. This is a technical housekeeping session. Students already saw their messy file names during the Reflection Q&A — now they're fixing them. The win here is seeing `Component_1` transform into `TeamValueScreen`. Make this visible — pull up a student volunteer's screen at T+15 to show the file-tree transformation.
While students work independently, create Zoom breakout pairs to simulate a co-working environment. Remind them you're in the main room for support if AI gets stuck.
**Critical:** students must have their `HANDOFF.md` pushed to GitHub before the timer ends. They'll be swapping their handoff with a partner for peer review immediately after this lab. They cannot review a blank file.
Supabase / Lovable Cloud nuance: depending on the student's Lovable setup, the backend may be Lovable Cloud (built-in) or a separate Supabase connection. Either way, they end up with a real PostgreSQL database. If your instructor directs students to connect a separate Supabase account, walk that path instead.
If a student's refactor doesn't pick up their screen names properly, re-prompt: "Rename the files in the `src/pages` directory to match the names in my PRD."

---

## Slide 20 — Show and Swap Your Handoff

10 minutes total — 3 min silent reading + 2 min Q&A per side, then swap. This is a *logic stress test*, not a polite review. If a partner gets confused, that *is* the data.
Pair students randomly — don't let them pick a friend. The point is professional handoff: can a stranger follow your docs? Use Zoom pair rooms of 2.
Three sharing options to call out: **(1) screenshare** (simplest), **(2) add partner as GitHub collaborator** (recommended — mirrors real engineering teams), **(3) make repo public** (Settings → Danger Zone → Change visibility).
Read the three questions cold. After the swap, ask 1–2 volunteers to name *one thing* their partner caught that they hadn't seen. Then transition to the Three Pillars debrief.

---

## Slide 21 — The Three Pillars

Before you hand over your build, you have to ask: is this actually "Engineering-Ready"? These three pillars are the non-negotiable standards. If you skip them, you aren't handing over a product — you're handing over a mess. And you don't need to be an engineer to do this; you just need to direct the AI.
**GitHub Connection — your Front Door.** Permanent home for the code with version history. Safe rollbacks if a future prompt breaks something. The exact place an engineer goes to clone the code.
**Code Refactoring — your Cleanup.** Use Lovable's intelligence to structurally clean up — renaming spaghetti components into professional labels and organising files. When a human engineer looks at your project, they see a system they recognise, not AI-generated noise.
**Supabase Connection — your Memory.** Real PostgreSQL database. Moves you from toy data into a real backend tool where you can manage users and information through a visual editor.
By checking these three boxes, students have effectively paid off their technical debt. The build has moved from a temporary builder link into a structured, version-controlled system.

---

## Slide 22 — Module 4 Complete

Use this slide as a way to not only share today's accomplishments but get students excited about what's to come. This is the **"landing the plane"** moment where you shift their identity from a prototyper to someone who can successfully manage a high-fidelity engineering handoff.
As we wrap up today, look at the math of your new operating model. You've moved from building in a vacuum to building *for production*. In a typical product cycle, how much time is wasted in back-and-forth meetings because the black box of the requirements wasn't clear, or the vibe of the prototype didn't match the technical reality? Usually, that's where projects die. But look at what you did today.
You explained the black box logic by turning your strategic intent into eight distinct, documented building blocks. You moved past "What does this do?" ambiguity and created a system any engineer can audit. By manifesting your prompts into a Living PRD, you ensured your logic isn't trapped in your head — it's a documented reality that stands on its own.
Most importantly, you **broke the prototype ceiling**. You moved from spaghetti logic into clean, refactored architecture that can actually scale. By separating data from display and generating a Start Here manual, you transformed your build into a professional asset ready for a real-world engineering team.
You turned your AI-assisted build into a version-controlled, database-connected, and fully-specified product.
**Project reminder:** take a moment today to copy your Living PRD elements into Slide 7 and your Engineering Handoff sections into Slide 9 of your final project deck. These are the artifacts that prove your build is production-ready.
Coming up in Module 5, we cross the finish line. You've built the logic and the infrastructure; now we go live — fully deployed product with real users, real authentication, and a live URL anyone in the world can access.

---

## Slide 23 — Key Takeaways

At the end of each module, recap key concepts and content covered in today's lesson. Keep this to 30 seconds. The point isn't to re-teach — it's to anchor.

---

## Slide 24 — Extra Practice + Next Session

30 seconds. The Extra Practice is optional but flagged for students who want to push past minimum. The Rollback Drill is particularly useful — it teaches them GitHub isn't just storage, it's a safety net.
Bridge to M5: *"You've connected the infrastructure. Tomorrow we connect the users. Real auth, real APIs, real edge cases, and a live URL that anyone in the world can access."*

---

## Slide 25 — Day 4 Survey

Drop the survey link in chat. *"Two minutes. We read every response. Like real product managers, we iterate based on data."*

---

## Slide 26 — Resources & Templates

Drop this card list once in `#cohort-channel` immediately after class — pin it. The Lab Guide is the walkthrough; the Living PRD sample is the reference for "what good looks like"; the Frameworks Reference Card is the cheat sheet for the four mental models from today.
**GitHub-first rule:** reinforce one last time that the tools above are *aids* — the canonical artefacts live in their GitHub repo. M5 onwards pulls from `04-structure/` on GitHub, not from any tool's browser cache.

---

## Slide 27 — Q&A

Open the floor for 3–4 minutes. If nobody has a live question, pick the highest-energy post from the cohort channel and read it back: *"someone wrote — [paste partner-feedback line] — what's the engineering move on that?"*

---

## Slide 28 — See You in Module 5

Land it hot. 15 seconds. *"You did the work. Your prototype is engineering-ready. Tomorrow we cross the finish line — fully deployed product, real auth, real database, live URL. See you in Module 5."*

---


## Closing checklist for the instructor

After Module 4, students should walk away with:

- `04-structure/PRD.md` — 8-block Living PRD in their GitHub repo.
- `HANDOFF.md` — engineering handoff document in their GitHub repo.
- Refactored `src/pages` with descriptive component names + a generated `README.md`.
- A live Supabase / Lovable Cloud backend connected to their project.
- `04-structure/swap-notes.md` — partner feedback from the Show and Swap.

**If any of these aren't in GitHub, Module 5 starts without a spec to integrate.** Pin the artifacts checklist in the cohort Slack channel before students log off.

**Coming up — Module 5.** From connected infrastructure to a fully deployed, live product. Real database schemas, authentication, API integrations, edge case handling.
