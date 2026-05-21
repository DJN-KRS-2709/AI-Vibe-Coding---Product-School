# Module 6 — Speaker Notes

> **Module 6 · Measure Product Performance for AI-Driven Iteration.** Speaker notes extracted from the instructor deck. Source of truth = `Modules/Module 6 - Slides.html`; this file mirrors those notes for read-only reference and async cohort use.

## 1. Hero — Measure Product Performance for AI-Driven Iteration

Welcome to Module 6 — the final session. Five modules built up to a live URL; today we make that URL *learn*. By the end of class every learner has read their own analytics, run an AI-powered iteration on real signal, redeployed, and demoed their product to the cohort.

Frame the arc: M5 was "ship the thing." M6 is "prove the thing." This is the move from PM-as-builder to PM-as-operator. Push hard on the identity shift — they finish today as Technical PMs who can close a build-measure-iterate loop end-to-end.

## 2. Class Expectations

Run this quickly — the cohort has seen it five times. The momentum norm matters most today because the showcase is on a hard clock: ~10 minutes per presenter, 5–6 presenters.

## 3. Course Arc (M6 active)

Anchor the arc one last time. M1–M5 was the build; M6 is the proof. The Confidence Line goes from "I have an idea" all the way to "the data confirms the idea" — that's the journey we close today.

## 4. Final Project Submission Reminder

This is the only "this is required for certification" moment in the deck — make it stick. Drop the Docebo link in `#cohort-channel` right after this slide and pin the message. Mention the 7-day window explicitly. Then ask for the 5–6 showcase volunteers right now while attention is high.

## 5. Today's Agenda

Three timed activities today: the Rapid-Fire Feedback Loop (10 min on peers' products), Lab 1 (10 min on your own Insights), Lab 2 (15 min AI sprint). Plus a 15-min deliverables-deck polish. The biggest time investment is the final showcase. Watch the clock — if anything slips, protect the showcase, not the polish block.

## 6. Section 01 · Shift From Shipping to Proving With Data

Brief section divider. The demo + the Rapid-Fire Feedback Loop + the three lecture slides that follow are the conceptual setup for Lab 1.

## 7. Instructor Demo · Making Data-Driven Decisions

Cue the demo (~3 min). Ask for one volunteer to share their Lovable project — open the Insights panel together. Call out each metric: **Visitors** (unique), **Page Views** (total), **Views Per Visit** (depth), **Duration** (engagement), **Bounce Rate** (entry-screen quality).

End with: "in 10 minutes, you'll bring that same critical eye to four of your classmates' products." That's the bridge into the Rapid-Fire Feedback Loop.

## 8. Rapid-Fire Feedback Loop (10 min)

Activity: Individual Exercise · 10 minutes. Push hard on two things at the top of the activity:

- **(1) Everyone needs a URL posted.** If a learner never shared their deployed link in `#cohort-channel` from M5, they need to post it *now* — otherwise classmates can't leave feedback for them and they'll arrive at Lab 2 with no peer signal.
- **(2) Feedback must be specific.** *"Nice app!"* doesn't help anyone. The four labels (🐛 / 🤔 / 🤩 / 💡) each force a concrete observation in one sentence. Demo the difference live: vague vs specific.

The exercise serves two purposes — it gives the cohort the qualitative signal they'll need for the AI analysis in Lab 2, and it develops their critical eye *before* they read their own Insights data in Lab 1. That's why the order matters: peer review first, self review second.

## 9. The Iteration Mindset (3 levers)

Make the three levers concrete with a single example: a learner's invite-tracker product. Feature Prioritisation says *"the only screen anyone visits is the dashboard — your settings page is dead weight."* Friction Identification says *"50% of new users bounce on the sign-up screen — your CTA is broken."* Hypothesis Validation says *"users send invites but never check the status tab — your value prop isn't the tracker, it's the send flow."*

The throughline for every M6 lecture slide is the same: prompts now start with **"based on the data..."**, not *"I think it should..."*.

## 10. Metrics That Matter

Stress the discipline: **3–5 signals, not 50.** The four buckets are guard-rails — pick one or two per bucket and run with them. For most learners the M6 set will be: Engagement (sessions / core-flow events), Retention (return visits), Quality (bounce rate), Impact (one event tied to the M2 hypothesis).

The North Star line is the one to land hard: if the data *contradicts* your hypothesis, the right move is a pivot, not a tweak. We'll see this exact split show up in their AI analysis output in Lab 2.

## 11. Three Layers of Analytics

Layer 1 is what we use in class — Lovable Insights is free, instant, and already running. Layer 2 (GA4) is the optional post-class add-on; the Lab Guide has a 10-minute walkthrough. Layer 3 is the most advanced and the most powerful — the Supabase connection from M5 is exactly what enables it.

Tell the cohort: "the most senior PM move you can make on your final project is layering all three. You won't do it today — but the moment you have a paying user, this is the architecture."

## 12. Section 02 · Hands-On Lab — Read Lovable Insights

Brief section divider. The lab slide follows.

## 13. Lab · Read Your Lovable Insights (10 min)

Run this as a guided exercise — ask one volunteer to screen-share their Insights panel while you walk the room. Every learner does the same on their own product in parallel.

Watch for the **empty-data failure mode**: a learner whose product had no real users yet (Insights panel is blank). Have them open their live URL in two different browsers right now to generate at least some signal before the lab moves on — otherwise the AI prompt in Lab 2 runs against nothing.

Land the audit question hard: *"is the data telling you the M2 hypothesis is confirmed, or is it telling you V2 is a pivot?"* That's the question the AI will answer in Lab 2.

## 14. Section 03 · AI-Driven Product Iteration

Brief section divider. The two lecture slides that follow are the conceptual backbone for Lab 2.

## 15. AI-Powered Analysis · The PM's New Superpower

The reframe: 10x faster decisions, same level of judgement required. Stress that the strategic prompt has four inputs — problem, hypothesis, metrics, feedback — and asks for a **ranked** backlog. Ranking is what makes it actionable.

The discipline line is the one to land: **one finding, not three.** Lab 2 is 15 minutes; they don't have time for a full rebuild. Picking the single highest-impact tweak is the muscle we're building.

## 16. From Data Signal to Technical Fix

The three patterns map to the three types of finding the AI most often returns: voice/copy issues (→ Persona), structural / UX issues (→ Branching), logic / data issues (→ Guardrail). Walk through one example per pattern — keep it concrete.

The pattern line is what learners write down: **"based on the data showing..."** opens every iteration prompt. It enforces the discipline that you're *repairing friction*, not adding features.

## 17. Section 04 · Hands-On Lab — AI Iteration Sprint

Brief section divider. The Lab 2 slide follows.

## 18. Lab · Run an AI-Driven Iteration Sprint (15 min)

15 minutes is tight on purpose. Push the constraint hard: **one finding, one change.** Most learners will want to fix three things — that's how they break their product right before the showcase. Block that instinct.

Spin up Zoom breakout rooms for a "co-working" feel — everyone builds in parallel with cameras on. Stay in the main room for support; learners DM you in Slack if stuck.

The single hardest thing to do well: **test before redeploying.** If Lovable made multiple changes and one broke something, don't ship it — re-prompt to revert that piece first.

## 19. Finalize Your Project Deliverables (15 min)

15 minutes of solo polish — but the deliverable is **a live GitHub Pages site, not a PowerPoint.** Drop the link to `Templates/Showcase-Generator.html` in `#cohort-channel`. Every learner opens it, pastes their repo URL, and the tool scans every markdown file in their repo — pattern-matching H2 headers against the 8 showcase slots (Problem · Hypothesis · Validation · PRD elements · Handoff · Friction · Learning · Aha) plus fenced code blocks for the prompt chain. Hit Download HTML, drop the file in `docs/index.html`, push, `Settings → Pages → main / /docs → Save`. That public URL is what they submit to Docebo.

Two prereqs to flag before they start: (1) the repo must be **public** (or paste a personal access token in the optional field) — public is required for free GitHub Pages anyway; (2) any section the tool can't find shows up as a yellow placeholder card with the exact heading to add. Most learners will be missing Friction · Learning · Aha — those typically aren't in `livingprd.md` or `engineeringhandoff.md`. Tell them to drop a `STORY.md` in their repo root with three short sections (`## Friction`, `## Learning`, `## Aha`). Template lives in `Templates/STORY-Template.md`.

Walk the slide map: title · product · problem · hypothesis · validation · PRD · prompts · handoff · friction · learning · aha. The story slides (friction/learning/aha) are where most learners under-invest — push hard: *"what was your aha moment? Write the sentence you'd say at a dinner party."* Same energy as the AI Product Strategy showcases — the URL is the artifact, not a slide deck.

## 20. Learner Journey · M1 → M6

Slow down here. This is the emotional payoff of the whole certification. Read each row out loud — let the cohort feel the arc. "In Module 1, you executed the velocity. In Module 6, you built the iteration engine." Six modules, six shifts, one loop closed.

Land the closer: "you now have a build-measure-iterate toolkit most PMs at unicorn companies don't have. That's the identity you walk out with today."

## 21. Take a Beat (5-minute break)

5-minute timer in `#cohort-channel`. Use the buffer to pre-load the showcase order — pin a quick list of who presents first, second, third. Anyone with audio/video issues, troubleshoot now, not during the demos.

## 22. Cameras On

Standard reminder slide, placed deliberately right before the showcase. Today the cameras matter more than any other day — they keep the energy up for every demo and make the room feel like a real launch event.

## 23. Key Takeaways

Recap pace — 60 seconds per takeaway. The throughline: *discipline*. M6 is where the build-measure-iterate loop stops being a buzzword and becomes a muscle.

## 24. Section 05 · Final Project Showcase

Section divider before the showcase. Brief — the kickoff slide follows.

## 25. Showcase Kick-Off — Your Time to Shine

Call on your first volunteer right after this slide. Get them to share their screen. Live feedback uses the same rubric as the cohort feedback (Project Clarity, Credibility & Reasoning, Strategic Thinking, Application of Concepts) — but make it warm. This is the celebration moment, not an exam.

Give a 6–7 minute warning per presenter. If a learner is going long, cut respectfully — protect the rest of the showcase. After all volunteers, return here to remind every learner about the 7-day Docebo deadline.

## 26. Day 6 Survey

Drop the link in `#cohort-channel` as you say this. Two minutes max. The Day 6 survey is the most actionable — it shapes the next cohort's entire structure. Push for honest, specific feedback.

## 27. Resources & Templates

Drop this card list in `#cohort-channel` right after class — pin it. The Lab Guide is the walkthrough; the Iteration Sprint Brief Template is the "what good looks like" reference; the Frameworks Reference Card is the cheat sheet for the M6 mental models.

**GitHub-first rule, one last time:** the canonical artefact lives at `06-iteration/Iteration-Sprint-Brief.md`. The Final Project deck goes to Docebo for cert; the GitHub repo is your portfolio piece for the rest of your career.

## 28. Q&A

Open the floor for 3–4 minutes. Two common Q&A patterns at the end of a cohort:
- **"What do I do after I submit?"** — point them at the Final Project Brief next-steps section and the cohort alumni Slack.
- **"How do I keep building?"** — recommend they iterate on their own product weekly for the next 30 days using the same M6 loop.

## 29. End · Certification Complete

The identity-shift closer. Don't oversell — name it: today they finished as Technical PMs who can ship, measure, and iterate end-to-end. Thank them for the cohort energy. Drop the alumni Slack channel link and the post-cert resource list one last time.
