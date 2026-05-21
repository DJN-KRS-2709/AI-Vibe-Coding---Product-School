# Module 5 — Speaker Notes

> **Module 5 · Ship Live Products with Full-Stack Logic.** Speaker notes extracted from the instructor deck. Source of truth = `Modules/Module 5 - Slides.html`; this file mirrors those notes for read-only reference and async cohort use.

## 1. Hero — Ship Live Products with Full-Stack Logic

Welcome to Module 5 — the production transition. The last two modules built infrastructure; today we make that infrastructure carry weight. By the end of this session every learner has a live, public URL with signed-in users, partitioned data, and graceful failure handling.

Frame the arc: M4 handed an engineer the spec; M5 hands an engineer (and customers) a running system. Stress: you will deploy *even if* the stress test reveals gaps — you'll document them in `HANDOFF.md` and ship anyway. That's the PM move.

## 2. Class Expectations

Run this quickly — the cohort has seen it four times. Use it as a reset for energy: cameras on, Slack questions only, no group breakouts. Day 5 is high-intensity (two labs, a live deploy) so the momentum norm matters most today.

## 3. Course Arc (M5 active)

Anchor the arc once more before we go in. The bridge from M4 to M5 is the move from "engineering-ready spec" to "engineering-shipped product." After today, the M6 bridge will be from "live product" to "live product that learns from its users."

## 4. Presentation Reminder

Push hard for volunteers for the final showcase. Frame it as the highest-bandwidth feedback in the cohort: live demo, live feedback, in front of peers. Drop the sign-up link in `#cohort-channel` right after this slide; pin the message. Aim for 5–6 names by end of class.

## 5. Today's Agenda

Two labs today — Lab 1 (Schema/RLS/Edge Cases) is the heavier one, the actual production work. Lab 2 (Stress Test + Deploy) is short but the payoff: every learner walks out with a public URL. Watch the clock; if you slip on Lab 1, cut the optional API integration step (Step 7) and protect the deploy.

## 6. Section 01 · From Connected Infrastructure to a Secured Product

Section divider. Brief — the next slide does the framing.

## 7. Instructor-Led Demo — From Connected Infrastructure to Secured Product

Cue the demo (~8 min). Students do not build along — eyes on the screen. Call out the three prompts as they fire and the result after each: schema → real metrics; auth/RLS → users only see their own rows; edge cases → loading skeletons and retry buttons replace dead screens.

End the demo on the DevTools offline toggle — that's the chaos test they'll repeat themselves in Lab 2.

## 8. Section 02 · How to Secure & Extend Your Integration

Brief section divider. The two lecture slides that follow are the conceptual backbone for Lab 1.

## 9. How to Prompt for Integration

The lesson here is a vocabulary shift — from *visual* prompts ("make the button blue") to *transactional* prompts ("when a user clicks this, fetch this row owned by this session"). The three pillars of any integration are: schema (source of truth), ownership (who can see what), and external orchestration (what other systems plug in).

Stress that Lovable's Integration Plan tool generates all three customized to *their* codebase — they don't have to write these prompts from scratch in Lab 1.

## 10. Resistance Engineering — Four Product States

Make the point concrete: every learner's prototype right now passes the "happy path" — a logged-in user with data clicking through the main flow. Every prototype *fails* at least one of these four states. Lab 2's stress test is literally a guided tour of these failures.

Empty & loading are the cheap wins. Error & load-bearing are where most production bugs hide. The Edge Case prompt in Lab 1 (Prompt 3) addresses all four in one shot — that's why we centralise it.

## 11. Section 03 · Hands-On Lab — Add Data Schemas + RLS

Brief section divider. The lab slide follows.

## 12. Lab — Add Data Schemas + RLS (45 min)

This is the heaviest lab in the cohort — 45 minutes, three sequential prompts, two verification gates. Pre-work audit takes 5 min; Plan generation takes ~3 min; each prompt takes ~10 min including verification. If a learner stalls on Prompt 1, get them on Lovable's *Settings → Integrations* tab to confirm Supabase is still linked from M4.

Push the verification language hard:
- **data survives refresh** (Prompt 1)
- **two accounts can't see each other's data** (Prompt 2)
- **offline DevTools toggle shows an error message, not a hung screen** (Prompt 3)

These are the only three signals that matter.

## 13. Break

5-minute timer in `#cohort-channel`. Use the buffer to spot-check the room — anyone whose Prompt 3 failed should ping you in Slack so you can debug before Lab 2.

## 14. Cameras On

Standard reminder slide. Brief.

## 15. Section 04 · Hands-On Lab — Stress Test & Deploy

Section divider before the second lab.

## 16. Lab — Rapid-Fire Stress Test & Deploy (30 min)

Run the first 10 minutes *together*. Ask one volunteer to screen-share their prototype while you walk the room through the Kill Switch. After that, learners go solo on Ghost User / Spam Click for ~10 min, then HANDOFF + Publish for the final ~10.

The PM mindset to repeat 3×: **you never ship perfect code, you ship code with known risks.** A documented Known Gap in `HANDOFF.md` is a professional ship. A silent broken feature is not.

Safari users — they can't toggle offline in DevTools. Give them the simulate-prompt in the Lab Guide.

## 17. Your Evolved Engineering Handoff

This is the slide that connects today's lab back to the M4 narrative. The handoff isn't a one-shot artefact — it evolves with the build. By M6 it'll evolve again to include eval results and iteration evidence.

Stress the "source of truth" framing: the GitHub repo is where engineers go. The `HANDOFF.md` in their repo is the most senior artefact they ship in this cohort.

## 18. Future-Proofing with APIs

This is the optional / advanced section — directly tied to Step 7 of Lab 1 (API integration). Most learners won't get there in class, but flag it as the most leverage in the M6 + final-project window.

The shift is from "my database is my product" to "my product is a switchboard." Personalisation, Real-Time, Continuity — three different verbs. Any one of them in your final demo makes the product feel meaningfully more alive.

## 19. Module 5 · Complete (Dashboard)

Land the plane: this is the identity shift from *someone with an idea* to *a Technical PM who has successfully launched a live production system*. Push hard on the "you have a URL" line — it's the most concrete artefact any learner has shipped in their entire PM career so far.

Use this slide to set up M6: the product is live; now we measure it. Tease the evals + analytics + redeploy loop.

## 20. Key Takeaways

Recap pace — 60 seconds per takeaway. The throughline: *resilience*. M5 is where prototypes either grow up or quietly fail in the wild. Every one of these four takeaways is a guard rail against quiet failure.

## 21. Extra Practice + Next Session

Frame the optional exercises as the gap between "you shipped" and "you shipped something interesting." Most learners stop at the live URL; the ones who do API Value Expansion come back to M6 with a product that's genuinely worth measuring.

Tease M6 as the closer: "today you have a URL — next class we make that URL *learn*."

## 22. Day 5 Survey

Drop the link in `#cohort-channel` as you say this. Two minutes max. Mention that Day 5's feedback most heavily shapes the Day 6 evals walkthrough.

## 23. Resources & Templates

Drop this card list in `#cohort-channel` right after class — pin it. The Lab Guide is the walkthrough; the Integration Plan Template is the reference for "what good looks like"; the Frameworks Reference Card is the cheat sheet for today's four mental models.

**GitHub-first rule:** reinforce one last time — the canonical artefacts live in their GitHub repo at `05-integration/Integration-Plan.md` and the updated `HANDOFF.md`. M6 pulls from `05-integration/` on GitHub. No tools, no browser cache, no exceptions.

## 24. Q&A

Open the floor for 3–4 minutes. If nobody has a live question, pick the highest-energy post from `#cohort-channel` and read it back: *"someone wrote — [paste line] — what's the engineering move on that?"*

## 25. End · See You in Module 6

The session's identity-shift moment lands here. Don't oversell — just acknowledge it: today they moved from "PM with a prototype" to "PM with a live URL." Drop the M6 hook in `#cohort-channel`: pre-read goes out tonight.
