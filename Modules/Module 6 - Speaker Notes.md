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

Two labs again, but both are lighter than M5: Lab 1 (~10 min Insights + ~10 min peer feedback in Slack) and Lab 2 (~15 min AI sprint). The biggest time investment is the final showcase. Watch the clock — if anything slips, protect the showcase, not the polish-deliverables block.

## 6. Section 01 · Shift From Shipping to Proving With Data

Brief section divider. The demo + the three lecture slides that follow are the conceptual setup for Lab 1.

## 7. Instructor Demo · Making Data-Driven Decisions

Cue the demo (~3 min). Ask for one volunteer to share their Lovable project — open the Insights panel together. Call out each metric: **Visitors** (unique), **Page Views** (total), **Views Per Visit** (depth), **Duration** (engagement), **Bounce Rate** (entry-screen quality).

End with: "in 10 minutes, every one of you will do this on your own product." That's the bridge into the Iteration Mindset framing slides before Lab 1.

## 8. The Iteration Mindset (3 levers)

Make the three levers concrete with a single example: a learner's invite-tracker product. Feature Prioritisation says *"the only screen anyone visits is the dashboard — your settings page is dead weight."* Friction Identification says *"50% of new users bounce on the sign-up screen — your CTA is broken."* Hypothesis Validation says *"users send invites but never check the status tab — your value prop isn't the tracker, it's the send flow."*

The throughline for every M6 lecture slide is the same: prompts now start with **"based on the data..."**, not *"I think it should..."*.

## 9. Metrics That Matter

Stress the discipline: **3–5 signals, not 50.** The four buckets are guard-rails — pick one or two per bucket and run with them. For most learners the M6 set will be: Engagement (sessions / core-flow events), Retention (return visits), Quality (bounce rate), Impact (one event tied to the M2 hypothesis).

The North Star line is the one to land hard: if the data *contradicts* your hypothesis, the right move is a pivot, not a tweak. We'll see this exact split show up in their AI analysis output in Lab 2.

## 10. Three Layers of Analytics

Layer 1 is what we use in class — Lovable Insights is free, instant, and already running. Layer 2 (GA4) is the optional post-class add-on; the Lab Guide has a 10-minute walkthrough. Layer 3 is the most advanced and the most powerful — the Supabase connection from M5 is exactly what enables it.

Tell the cohort: "the most senior PM move you can make on your final project is layering all three. You won't do it today — but the moment you have a paying user, this is the architecture."

## 11. Section 02 · Hands-On Lab — Read Lovable Insights

Brief section divider. The lab slide follows.

## 12. Lab · Read Lovable Insights + Peer Feedback (20 min)

Run the first 10 minutes as a guided exercise — ask one volunteer to screen-share their Insights panel while you walk the room. The other 10 minutes is Slack peer feedback: every learner posts their URL, opens four others, leaves one labelled comment on each.

Watch for two failure modes:
- **(1) A learner who never posted their URL in M5** — they get peer-tested last and won't have feedback for Lab 2. Catch them now.
- **(2) Feedback that's too vague** — "nice app!" doesn't help. Push the four labels: 🐛 / 🤔 / 🤩 / 💡 with one specific sentence each.

## 13. Break

5-minute timer in `#cohort-channel`. While they break, read the room: anyone whose Insights panel was empty (no real users), pair them up with a peer who has data so Lab 2's prompt still runs against real signal.

## 14. Cameras On

Standard reminder slide. Today the cameras matter more than usual — they keep the energy up for the showcase later in the session.

## 15. Section 03 · AI-Driven Product Iteration

Brief section divider. The two lecture slides that follow are the conceptual backbone for Lab 2.

## 16. AI-Powered Analysis · The PM's New Superpower

The reframe: 10x faster decisions, same level of judgement required. Stress that the strategic prompt has four inputs — problem, hypothesis, metrics, feedback — and asks for a **ranked** backlog. Ranking is what makes it actionable.

The discipline line is the one to land: **one finding, not three.** Lab 2 is 15 minutes; they don't have time for a full rebuild. Picking the single highest-impact tweak is the muscle we're building.

## 17. From Data Signal to Technical Fix

The three patterns map to the three types of finding the AI most often returns: voice/copy issues (→ Persona), structural / UX issues (→ Branching), logic / data issues (→ Guardrail). Walk through one example per pattern — keep it concrete.

The pattern line is what learners write down: **"based on the data showing..."** opens every iteration prompt. It enforces the discipline that you're *repairing friction*, not adding features.

## 18. Section 04 · Hands-On Lab — AI Iteration Sprint

Brief section divider. The Lab 2 slide follows.

## 19. Lab · Run an AI-Driven Iteration Sprint (15 min)

15 minutes is tight on purpose. Push the constraint hard: **one finding, one change.** Most learners will want to fix three things — that's how they break their product right before the showcase. Block that instinct.

Spin up Zoom breakout rooms for a "co-working" feel — everyone builds in parallel with cameras on. Stay in the main room for support; learners DM you in Slack if stuck.

The single hardest thing to do well: **test before redeploying.** If Lovable made multiple changes and one broke something, don't ship it — re-prompt to revert that piece first.

## 20. Finalize Your Project Deliverables (15 min)

15 minutes of solo polish. Drop the Vibe Coding Final Project Deliverables template link in `#cohort-channel` — every learner submits a copy. Remind them this is the only deliverable that gates certification.

Walk the slide map: 5 product · 6 validation · 7 PRD · 8 prompt chain · 9 handoff · 10 story. The story slide (10) is where most learners under-invest — push hard: "what was your aha moment? Write the sentence you'd say at a dinner party."

## 21. Learner Journey · M1 → M6

Slow down here. This is the emotional payoff of the whole certification. Read each row out loud — let the cohort feel the arc. "In Module 1, you executed the velocity. In Module 6, you built the iteration engine." Six modules, six shifts, one loop closed.

Land the closer: "you now have a build-measure-iterate toolkit most PMs at unicorn companies don't have. That's the identity you walk out with today."

## 22. Key Takeaways

Recap pace — 60 seconds per takeaway. The throughline: *discipline*. M6 is where the build-measure-iterate loop stops being a buzzword and becomes a muscle.

## 23. Section 05 · Final Project Showcase

Section divider before the showcase. Brief — the kickoff slide follows.

## 24. Showcase Kick-Off — Your Time to Shine

Call on your first volunteer right after this slide. Get them to share their screen. Live feedback uses the same rubric as the cohort feedback (Project Clarity, Credibility & Reasoning, Strategic Thinking, Application of Concepts) — but make it warm. This is the celebration moment, not an exam.

Give a 6–7 minute warning per presenter. If a learner is going long, cut respectfully — protect the rest of the showcase. After all volunteers, return here to remind every learner about the 7-day Docebo deadline.

## 25. Day 6 Survey

Drop the link in `#cohort-channel` as you say this. Two minutes max. The Day 6 survey is the most actionable — it shapes the next cohort's entire structure. Push for honest, specific feedback.

## 26. Resources & Templates

Drop this card list in `#cohort-channel` right after class — pin it. The Lab Guide is the walkthrough; the Iteration Sprint Brief Template is the "what good looks like" reference; the Frameworks Reference Card is the cheat sheet for the M6 mental models.

**GitHub-first rule, one last time:** the canonical artefact lives at `06-iteration/Iteration-Sprint-Brief.md`. The Final Project deck goes to Docebo for cert; the GitHub repo is your portfolio piece for the rest of your career.

## 27. Q&A

Open the floor for 3–4 minutes. Two common Q&A patterns at the end of a cohort:
- **"What do I do after I submit?"** — point them at the Final Project Brief next-steps section and the cohort alumni Slack.
- **"How do I keep building?"** — recommend they iterate on their own product weekly for the next 30 days using the same M6 loop.

## 28. End · Certification Complete

The identity-shift closer. Don't oversell — name it: today they finished as Technical PMs who can ship, measure, and iterate end-to-end. Thank them for the cohort energy. Drop the alumni Slack channel link and the post-cert resource list one last time.
