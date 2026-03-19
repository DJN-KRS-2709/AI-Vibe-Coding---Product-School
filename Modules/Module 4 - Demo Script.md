# Module 4 — Instructor Demo: Step-by-Step

> For the instructor only. Run this as a live demo on screen share.
> Total time: ~8 minutes. Pre-type all 3 prompts before class.
> Instructor demo: **The Customer Vibe — Retention Engine** (B2B PM SaaS — 30% churn, team invites — carried from M2/M3 demos)

---

## SETUP (before students arrive)

- [ ] Open the M3 Retention Engine prototype in Lovable (same one carried from M2/M3 demos — now with prompt chain refinements, design system matching, and Living Prompt Pack applied)
- [ ] Have all 3 prompts pre-typed in a text file, ready to paste
- [ ] Have GitHub account logged in (so the click is instant)
- [ ] Lovable Cloud is enabled in workspace settings (it's on by default — verify at Settings → Connectors → Lovable Cloud)
- [ ] Screen share on — students should see everything

---

## STEP 1: Show the Facade (2 min)

**What you do:** Click through the M3 prototype — all screens. Show the 3-screen onboarding flow (team value → invite action → collaboration payoff), the retention metrics dashboard, the experiment summary. Remind students how polished it is.

**What you say:** "This is our M3 build. The onboarding flow that surfaces team invites to reduce churn. Three screens, design-system matched, interactive states, real user quotes and retention data embedded throughout. If your VP saw this, they'd think engineering built it."

**Then:** Switch to Lovable's code view. Let the mess sit on screen for 10 seconds. Don't explain it.

**What you say:** "Now look at the code. `Component1`. `handleClick2`. All logic in one file. No README. No documentation. This is what the engineer who inherits your prototype actually sees. Three prompts, two clicks. Watch."

---

## STEP 2: Prompt 1 — Extract the Living PRD (~60 sec)

**Paste this prompt:**

> "Look at this entire prototype. Write a product requirements document that covers: what this product does, who it's for, the problem it solves, the screens and their purpose, the user flow from first screen to last, the hypothesis it tests, the key metrics, what's currently mocked vs. what would need real data, and recommended next steps for engineering."

**While it generates:** Stay quiet. Let the class watch the PRD appear.

**When it's done:** Read 2-3 sections aloud — Product Overview and Technical Reality are the most impactful.

**What you say:** "I didn't write this. The prototype wrote its own spec. The hypothesis — 'surfacing team invites during first-run onboarding increases Day-3 invite rate from 12% to 25%' — extracted from what we built, not imagined before building."

---

## STEP 3: Prompt 2 — Refactor the Code (~60 sec)

**Paste this prompt:**

> "Refactor the codebase. Rename all components to be descriptive (e.g., TeamValueScreen, InviteFlow, CollaborationPayoff, RetentionDashboard, ExperimentSummary). Separate data logic from display components. Group files by feature, not by type. Add a README.md that explains the project structure."

**While it generates:** "Watch the file tree on the left."

**When it's done:** Switch to code view. Show the before/after.

**What you say:** "`Component1` is now `TeamValueScreen`. `Component3` is now `InviteFlow`. There's a `/services` folder for data logic. There's a README. An engineer can read this on day one. Same product — readable code."

---

## STEP 4: Prompt 3 — Engineering Handoff (~40 sec)

**Paste this prompt:**

> "Generate an engineering handoff document: list every component and what it does, describe the data model (what's real vs. mocked), identify the 3 biggest technical decisions an engineer would need to make, and write a 'start here' guide."

**When it's done:** Read the "start here" section and one technical decision aloud.

**What you say:** "A new engineer joins the team Monday. They open this document. In 5 minutes, they know what the onboarding flow does, what's real, what's mocked, and where to start. That's the handoff."

---

## STEP 5: Click 4 — Connect GitHub (~30 sec)

**What you do:** In Lovable, click the GitHub integration button. One click. Code pushes to a real repo.

**What you do next:** Open the GitHub repo URL in a new browser tab. Show the file tree, the README, the refactored components.

**What you say:** "One click. Your code is now in a real GitHub repository. An engineer can clone this right now. It's not trapped in Lovable anymore — it's real version control."

---

## STEP 6: Click 5 — Enable Lovable Cloud Backend (~30 sec)

**What you do:** Trigger the backend by prompting Lovable to add a feature that requires a database (e.g., "Save user onboarding progress to the database so returning users resume where they left off"). Lovable Cloud prompts you to enable — click Allow. Database, auth, storage, and edge functions are now live. No external accounts needed.

**What you do next:** Open the Lovable Cloud dashboard (Settings → Cloud). Show the database tables, the region, the live backend.

**What you say:** "One click. Your prototype has a real database, real auth, and real storage — all built into Lovable Cloud. No Supabase account, no AWS, no setup. It's just there. This isn't a toy anymore. This is real infrastructure."

**Pause. Let it land.**

---

## STEP 7: Debrief (2 min)

**What you say:**

"Same prototype. Same onboarding flow. Same screens testing the team invite hypothesis. But now it has:

- A Living PRD — complete spec, extracted from the build
- Clean code — `TeamValueScreen`, `InviteFlow`, not `Component1`
- An engineering handoff — component map, data model, start-here guide
- A GitHub repo — real version control
- A Lovable Cloud backend — real database, auth, and storage

Traditional PM workflow: research, spec, build, test.

Vibe Coding workflow: build, test, extract the spec. The spec is the output, not the starting point. And the infrastructure follows the prototype — not the other way around.

You'll do all of this to your own build in 30 minutes. But first — let's see what your code actually looks like right now."

**Transition to Mini Activity (Slide 6).**
