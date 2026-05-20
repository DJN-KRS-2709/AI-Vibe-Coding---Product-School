# Module 1 — Execute Vibe Coding Velocity

> Long-form companion to the Module 1 deck. Reads like a chapter. Same throughline as the slides, no speaker notes. Use it as your study guide, your reference between sessions, or the document you paste at the top of an AI when you want it to reason about Module 1 with you.

---

## The setup — three executives, three theories, zero data

Enterprise customers are churning thirty days after onboarding. The VP of Customer Success thinks it's a UX problem. The Head of Product thinks it's a feature-discovery problem. The CEO thinks the answer is a self-serve analytics dashboard. Nobody has data. Everybody has opinions. This is the universal scenario where product work goes to die — two weeks of meetings, whoever speaks loudest wins, and the team ships whichever theory the most senior person was attached to.

Module 1 is the antidote. Instead of debating which theory is correct, you build all three as concrete prototypes in about fifteen minutes each, look at them side by side, and let the evidence — not the seniority — make the call. That move is what *vibe coding* is for.

---

## The provocation — vibe coding isn't about speed

A common mis-frame coming in: "Vibe coding helps me ship faster." That's partially true and mostly the wrong vector. The actual point is **evidence per hour**. Speed is the floor; what you do with the speed is the ceiling. If you build five rough prototypes and can't name what you learned from any of them, you didn't compress the feedback loop — you just decorated it.

Two specific claims worth internalizing before the labs:

- **A prototype is useful when it looks polished.** False. Dropbox's launch demo was a three-minute screencast of a folder syncing. It was ugly. It generated seventy-five thousand signups in one night because it proved the core mechanic worked. Polish without proof is a toy.
- **Every build should answer exactly one product question.** True. Airbnb's first prototype was three air mattresses on a floor in San Francisco. The question wasn't "do we have a website." It was "will strangers pay to sleep in someone's home." One question. One test. One answer.

---

## The High-Velocity Prototyping Cycle

Four moves. You'll loop through them twice today, and roughly fifty times by the end of the certification.

1. **Build** — from instinct, not methodology. The goal is a shareable URL, not a finished product.
2. **Show** — silent walkthrough. No verbal tour, no explanation. You're watching where the eye goes and where the click hesitates.
3. **Learn** — raw signal beats polite feedback. Write down what confused. That confusion is the data.
4. **Decide** — kill it, refine it, or escalate it. No prototype is allowed to live without a verdict attached.

PMs reliably skip step four. They build, show, learn — then go to lunch. The cycle isn't closed until you've named what changes next. Make the decision visible.

---

## The Triple-Threat Build — three theories, one demo

The instructor demo walks through three different prototypes built from the same churn problem, in roughly fifteen minutes total:

- **Prototype 1 — Customer-facing onboarding dashboard.** The VP of CS theory: maybe users don't know what to do next. The build surfaces progress, recommended actions, and a help block.
- **Prototype 2 — Internal churn-ops view.** The Head of Product theory inverted: maybe the answer isn't a customer-facing tool at all. The build surfaces risk scores, last-login dates, feature adoption — a CS rep's pre-emptive view.
- **Prototype 3 — Design-matched analytics dashboard.** The CEO theory, but rendered against a real design system (a Mobbin screenshot) so it looks like it belongs in production. Suddenly the conversation moves from "is this a fake?" to "when can we ship this?"

The point of the demo isn't the prototype quality. It's the **act of swapping**. Three rough builds beats one polished build, every time. You can compare evidence; you cannot compare opinions.

---

## Three multimodal entry points

Modern vibe-coding tools read pixels and code, not just text. That gives you three ways to start every build:

- **Text-to-App.** Natural-language prompt. Best when no design exists yet. Cures blank-page syndrome. The right choice for greenfield ideas where you're still discovering the shape. This is what you'll do in Lab 1.
- **Screenshot-to-App.** Upload a pattern — Mobbin, your competitor's product, a sketch on a whiteboard. The AI clones the layout, palette, navigation. Best when you're refining a vibe sketch against a known-good professional pattern. This is what you'll do in Lab 2 Path A.
- **Design-to-Code.** Paste Figma frames or design-system tokens. Best when you're prototyping inside an existing product and the brand has to be right from minute one. This is Lab 2 Path D — and it's the most underused trick in the room, because it eliminates the "looks like a toy" stakeholder objection before the meeting even starts.

You never start from a blank canvas. You start from something that already exists.

---

## Credit efficiency — the rule that protects your runway

A Pro plan is roughly a hundred credits a month. That's a lot if you treat the tool as an execution engine and very little if you treat it as a scratchpad. Four rules:

1. **Plan in a sandbox.** Do sixty percent of your prompt refinement in ChatGPT, Gemini, or Claude — all free. Only paste into Lovable when the prompt is locked.
2. **Paste, don't draft.** Aim for one-shot generations. Every "trial-and-error" pass is a credit you cannot use for a real architectural shift later.
3. **Edit code directly.** Hex codes, label typos, padding tweaks — fix them in the code panel. Re-prompting for cosmetic changes is the most expensive way to do a five-second job.
4. **The Eject Rule.** If a prompt fails twice, *stop*. Export the code, debug it externally, paste the fix back. The "credit death spiral" is the most common way a beginner runs out of runway by day two.

---

## Lab 1 — Your First Vibe Build

Open `Modules/M1 - Lab 1 Guide.html`. Pick one of four scenarios (Retention Engine, Internal Tool Nobody Uses, Marketplace Trust, Dashboard Nobody Reads). Pick a launch path — either copy-and-customize a starter prompt, or use the First Screen Method (visualize the first thing the user sees and prompt that exactly). Build on instinct for thirteen minutes. At the two-minute mark, freeze and generate your shareable link. Lab 2 is its own focused page (`M1 - Lab 2 Guide.html`) — opens after the break.

Commit the URL plus a screenshot to `01-velocity/prototype-v1.md`. That's the first artifact in your repo.

If a prompt fails twice, pivot. Do not re-prompt the same broken logic — that's how you burn credits.

---

## Show and Swap — peer review

After Lab 1, you pair up for ten minutes. The point is to experience a real user failing on your UI — that moment is the lesson, and you can't generate it for yourself.

Drop your shareable link in the breakout chat. Grab your partner's. **No verbal context** — no setup, no apologies, no "what I was going for was…". The build has to speak for itself, exactly like it would for a real user landing cold.

Click your partner's build silently for three minutes. Don't narrate. Take notes on three things: what you understood immediately about the product's purpose, what confused you, and what assumption you think they were testing. Then discuss those three points with your partner for three minutes. Then swap roles and repeat the whole loop on your build.

The silent rule is the whole point. The comment you most want to make at minute two is the most useful signal of the exercise — write it down instead of saying it.

If no partner is available, fall back to a silent self-walk plus the AI-review prompt below into ChatGPT or Claude. Same three dimensions, different reviewer.

```
You are a senior product reviewer. I built a prototype to explore the following assumption: [paste your one-sentence assumption]. The link is: [paste]. Critique the build on three dimensions: (1) Does the first screen communicate the core value in under 10 seconds? (2) What's the single biggest source of confusion? (3) What's the one change that would most increase my confidence in this direction? End with the question you would ask the user if you could only ask one.
```

After class, post a screenshot plus your one-line learning from your partner's feedback to `#cohort-channel`. The async share captures patterns across the cohort that no individual pair can see.

---

## Skill Markdowns — the superpower most PMs don't know exists

Brief preview, because you'll author your own in Module 3. A skill is a markdown file that tells an AI: "Here's how to build dashboards for B2B SaaS" or "Always use this design system." The AI follows it on every prompt. You don't have to re-explain your context every time.

Where to find them: the Anthropic Skills marketplace, Cursor's skill folder, public GitHub repos. Free. Install in one click. The mental model is "installing an app on your phone" — someone else figured out how to make the AI great at a specific task, and you import their expertise.

By Module 3 you'll build a *Living Prompt Pack*, which is your own skill. Today, just know they exist. AI competence stops being about prompt-engineering tricks and starts being about installing the right expertise.

---

## Lab 2 — Strategically Refine Your Build

Same prototype, two upgrade passes. The point of Lab 2 is to feel the difference between *building* and *iterating*. Same speed; sharper aim.

Pick **two of four** upgrade paths from the lab guide:

- **Path A — Design Match.** Upload a Mobbin screenshot. Prompt the AI to clone the palette, the card layout, the navigation. Same content. Now it looks like Linear.
- **Path B — Add Interactivity.** Filters that filter. Cards that expand on click. A loading skeleton for one-and-a-half seconds of perceived performance. Small details, enormous credibility boost.
- **Path C — Surgical Refinement.** Fix one section without touching the rest. Header gets a notification bell. Help block becomes a real CTA. Two small focused prompts beat one "rebuild the whole page" prompt every time.
- **Path D — Existing Product Track.** Match your real company's brand. Paste your actual hex codes and Figma CSS. Now the prototype belongs in your product, not in a sandbox.

Draft the refinement prompts in ChatGPT first. Credits.

Commit the v2 URL plus before-and-after screenshots to `01-velocity/prototype-v2.md`.

---

## Self-Score — your prototype

Five minutes. Score your v2 from 1 to 5, honestly:

| Score | Meaning |
|---|---|
| 1 | Sketch. Exists. Not ready for eyes. |
| 2 | Rough direction. Good idea, no execution. |
| 3 | Getting there. Recognizable, not functional. |
| 4 | Team-ready. You'd show this to your immediate team. |
| 5 | VP-ready. You'd show this to leadership tomorrow. |

Most learners score themselves a 3. The honest ones score a 2. The proud ones score a 4. Almost nobody scores a 5 today, and that's the right outcome — the entire rest of the course is the gap between where you are and where you want to be.

Post your screenshots, your score, and one sentence each on **why you scored what you did** and **the single change that would bump it +1** in `#cohort-channel`.

---

## The Confidence Line — the framework that runs through every module

You just lived **Phase 1**.

- **M1–M2: High Ambiguity.** Build to think. Explore many directions. Compress feedback to hours. Kill bad ideas fast.
- **M3–M4: Gaining Clarity.** Apply context and intent. Build functional, living specs. Transition from vibe to structure.
- **M5–M6: Production Confidence.** Real APIs, real data, real edge cases. Deploy a live URL. Measure, learn, and iterate against evidence.

Every prompt you write is a choice: *explore* the path, or *refine* it. Today was almost all explore. M2 introduces deliberate refinement. M3 is where precision starts mattering. M5 is where the prototype touches production.

You earned your way into Phase 1 today. The remaining five modules are the path to Phase 3.

---

## Toy vs Tool — the distinction that organizes everything

| The Toy | The Tool |
|---|---|
| Looks impressive. Proves nothing. | Looks real. Proves something works. |
| Generates applause, not insights. | Validates an assumption with clickable evidence. |
| No logic behind the screen. | Handles at least one real user flow end-to-end. |
| Dies after the demo. | Survives when someone else uses it. |
| Can't survive a real user. | Generates a decision, not a reaction. |

Whatever you scored your v2 above is exactly the distance between your build and a tool. The rest of the course closes that distance, deliberately.

---

## Your repo after today

One folder. Three artifacts.

```
01-velocity/
├── prototype-v1.md            # Lab 1 build (URL + screenshot + assumption tested)
├── prototype-v2.md            # Lab 2 refinement (URL + before/after + score)
└── confidence-line-reflection.md   # One-paragraph reflection on Phase 1
```

By the end of the certification this becomes six folders, a deployed URL, a Validation Evidence Brief, a Living PRD, a Prompt Library, and an Engineering Handoff. Today is the first deposit.

---

## Bridge to Module 2

You can build fast. The next question is whether you're building the *right* thing. Module 2 — *Validate Product Hypotheses via Risk-Based Prototyping* — introduces assumption mapping, the validation lens, and fidelity choice. Bring `prototype-v2.md` with you; we'll dissect what assumption it was actually testing, and whether you tested the right one.

---

## Key takeaways

- **Build to think, not to ship.** Today's two prototypes were not products. They were thought experiments rendered in pixels. Slack's entire pivot from gaming to enterprise communication started exactly this way — a tool the team built to talk to each other while making a game.
- **Vibes become tools through intentional, incremental layers.** Design match, interactivity, surgical refinement — three compounding passes, no rebuilds. Starting over is the most expensive mistake in vibe coding.
- **Every build must move the Confidence Line.** A prototype is a tool only when it answers a real question. Slack's "two thousand messages" magic number — the data point that justified the pivot — was generated by a working product, not a meeting.
- **Credits are fuel. Plan in a sandbox.** Sixty percent of your prompt work happens outside the tool. The tool is for committing the plan, not for finding it.
- **The mental barrier is gone.** You shipped functional software twice today without writing a line of code. Every M2–M6 deliverable assumes you can already do this.

---

## Extra practice (optional, async)

- **Pick a different scenario.** Return to the lab guide. Pick one of the four scenarios you did *not* use today. Repeat the 15-minute build. Compare which scenario felt easier and ask yourself why.
- **Swap the tool.** Try the same scenario in Bolt, Cursor, or v0. The methodology doesn't change — but you'll feel where each tool's defaults bias the build. A side-by-side comparison is a LinkedIn post nobody else in your cohort has.
