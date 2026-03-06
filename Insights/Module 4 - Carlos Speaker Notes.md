# Module 4: From Vibe to Structure — Speaker Notes for Carlos

> For Carlos only. High-level bullets explaining what we're doing and why.
> Slide numbers match the Gamma Prompt (slides 1–20). Update if Gamma reorders.

---

## Where M4 Sits

- M1 = speed, M2 = aim, M3 = precision, **M4 = structure**
- The hinge of the entire course: first half ends here (build), second half begins (make it real)
- Students go from owning a personal prototype → owning a **team-ready product with real infrastructure**
- Structure now means more than docs — it means GitHub repo + Supabase database + Living PRD + handoff
- Kills the "it's just a prototype" perception — this has real version control and a real database

---

## The M4 Wow (Three Beats + Crescendo)

- **Beat 1 (extraction):** A complete Living PRD appears from the prototype. "I didn't write this. The prototype wrote its own spec."
- **Beat 2 (refactoring):** Code view before/after. `Component1` → `OnboardingWelcome`. README appears.
- **Beat 3 (infrastructure — THE BIG ONE):** One click → GitHub connected. One click → Supabase connected. Student opens their GitHub repo, sees their code. Opens Supabase dashboard, sees the database. "This isn't a toy anymore. This is real infrastructure."
- **Clincher (partner test):** Partner reads ONLY the PRD — never sees the prototype. Nails all 5 questions. The prototype can survive without its creator.
- **Crescendo:** Four-tab reveal — M1 / M2 / M3 / M4 side by side.

---

## What Changed From the Previous Version (Carlos's Feedback, Mar 3)

- **GitHub + Supabase moved from M5 into M4** — Carlos: "just forcing people to do that... go to that aha moment of like, holy shit, there is not only code, it's actually production code"
- **Teaching compressed** — structure judgment + comprehension debt combined into one slide (was two)
- **Demo now includes infrastructure clicks** — 3 prompts + 2 clicks instead of just 3 prompts
- **New Lab Part 3** — dedicated 10-minute infrastructure connection section (the infrastructure connection)
- **M5 now starts with infrastructure already connected** — goes deeper into schemas, auth, APIs, edge cases
- **Waypoints updated** — "Code Refactoring" replaced by "Real Infrastructure" (GitHub + Supabase)

---

## Slide 1 | Opening (Title + 3 Waypoints)

- Three waypoints: Living PRD, Real Infrastructure, Engineering Handoff
- "If you got hit by a bus tomorrow, could anyone pick up where you left off?"
- Infrastructure is now a first-class waypoint — not just documentation

---

## Slide 2 | Chapter 1: Setup & Agenda

- "Your M3 prototype looks real. Could engineering build from it?"
- Adds two new gaps to the call-out: no version control, no backend
- Creates pull for the demo — they want the full transition, not just the docs

---

## Slides 3–5 | Demo (Setup → Live Build → Debrief)

- **Slide 3:** Pull up M3 Retention Engine — click through polish, then switch to code view. Let the mess sit.
- **Slide 4:** Run 5 steps live:
  - **Prompt 1 — Extract** → complete Living PRD generated from prototype
  - **Prompt 2 — Refactor** → `Component1` becomes `OnboardingWelcome`, README added
  - **Prompt 3 — Handoff** → component map, data model, technical decisions, start-here guide
  - **Click 4 — GitHub** → one click, code in a real repo (open the URL, show it)
  - **Click 5 — Supabase** → one click, real database connected (open dashboard, show it)
- **Slide 5:** Debrief — paradigm shift PLUS infrastructure shift. "The spec is the output, not the starting point. And the infrastructure follows the prototype, not the other way around."
- Total demo: ~8 min. The GitHub/Supabase clicks are the moment the room shifts.

---

## Slide 6 | Mini Activity (Open Your Code View)

- Students diagnose their own M3 code: names, separation, docs, version control
- Same gap-surfacing pattern as M3
- Quick — 5 minutes. Sets up the lab.

---

## Slide 7 | Teaching: Structure Judgment + Comprehension Debt (COMBINED)

- Compressed from 2 slides to 1 (Carlos: "cutting something that's not super intense")
- Two-column: "Structure when" vs. "Don't structure when"
- Comprehension debt as a callout box: after 50+ prompts, the prototype knows more than you
- Ask 2–3 students: "Would you structure your M3 today?"

---

## Slide 8 | Teaching: Living PRD Structure

- The reference table (Product Overview through Engineering Recommendation)
- Key addition: "Technical Reality" now includes infrastructure status (GitHub? Supabase?)
- Students reference this during the lab — make it scannable

---

## Slide 9 | Teaching: Infrastructure for PMs

- Three blocks: Refactoring, GitHub, Supabase
- Refactoring = same skill as M3 but applied to code
- GitHub = one click, real version control, engineers can clone the repo
- Supabase = one click, real database, foundation for M5
- Key message: "You're not engineering. You're connecting the infrastructure."
- Addresses Carlos's point: "structure actually means you have something with a backend logic, a commit button"

---

## Slides 10–11 | Lab Parts 1 & 2: PRD + Refactoring

- **Slide 10 — Part 1: Extract (10 min)** — Open Living PRD Extractor, customize prompt, extract PRD
  - First wow: "It actually described my product correctly"
  - "Do NOT refactor yet. Capture the spec first."
- **Slide 11 — Part 2: Refactor + Handoff (12 min)** — Rename components, separate concerns, generate handoff
  - The naming transformation is the most visible change
  - "The PRD and handoff matter more than perfect code"

---

## Slide 12 | Lab Part 3: Connect GitHub + Supabase — THE INFRASTRUCTURE CONNECTION

- **This is the new wow moment Carlos asked for**
- 5 steps, 10 minutes:
  1. Create accounts (GitHub + Supabase) if needed — 3 min, both free
  2. Click "Connect GitHub" in Lovable — code pushed to real repo
  3. Verify: open GitHub URL, browse refactored code, see README
  4. Click "Add Supabase" in Lovable — database connected
  5. Verify: open Supabase dashboard, see the project
- Walk the room. The GitHub moment: "That's your code in a real repo. An engineer can clone it right now."
- The Supabase moment: "Your prototype has a real PostgreSQL database."
- Combined effect: "10 minutes ago this was code trapped in Lovable. Now it has a spec, clean code in GitHub, and a real database."
- Students who already have accounts finish fast — have them help others

---

## Slide 13 | Peer Review — The Handoff Test

- Same as before: share ONLY the PRD, partner answers 5 questions
- Now enhanced: partner can also check the GitHub repo link in the PRD
- "If your partner can describe the product from just the spec, it's handoff-ready"

---

## Slide 14 | Quick Share

- "What surprised you about your own spec?"
- Surface comprehension debt gaps — fast, 3 minutes

---

## Slide 15 | Break It — The Prototype That Never Made the Transition

- Same cautionary tale but now with added horror: "Not connected to GitHub — no repo, no way to share with engineering"
- 500+ prompts, 47 unnamed components, code trapped in Lovable
- "If the code isn't in GitHub, it doesn't exist outside your browser"
- Compressed to 8 minutes (from 10) to make room for Lab Part 3

---

## Slide 16 | Four-Tab Reveal — M1. M2. M3. M4.

- Four browser tabs. 30 seconds of silence.
- M1: one prompt, one page → M4: spec, GitHub repo, Supabase, engineering handoff
- "That's not a prototype anymore — that's a product brief with real infrastructure"
- Emotional high point of the first half. M5 starts the second half.

---

## Slides 17–20 | Wrap

- **Slide 17 — What You Did Today:** Living PRD, Real Infrastructure, Engineering Handoff (mirrors slide 1)
- **Slide 18 — Accountability:** Post prototype link + GitHub repo link + PRD in #builds. Optional: share repo with an actual engineer.
- **Slide 19 — M5 Preview:** "Your infrastructure is connected. Next: build on top of it." Real schemas, auth, APIs, edge cases.
- **Slide 20 — Survey**

---

## Tools

- **Living PRD Extractor** — used DURING lab Parts 1 & 2. Students extract PRD, add handoff, document infrastructure status.
- **Living Prompt Pack Builder** — continues from M3. Students add structure prompts + infrastructure steps to their pack.
- **Structure Checklist** (NEW — recommended) — simple step-by-step for GitHub + Supabase connection with verification. Could be a section added to the PRD Extractor or a standalone lightweight tool.

---

## Timing (fits in 2 hours)

| Block | Slides | Duration |
|-------|--------|----------|
| Opening + Demo | 1–5 | ~13 min |
| Mini Activity | 6 | ~5 min |
| Teaching | 7–9 | ~10 min |
| Lab Part 1: Extract PRD | 10 | ~10 min |
| Lab Part 2: Refactor + Handoff | 11 | ~12 min |
| **Lab Part 3: GitHub + Supabase** | **12** | **~10 min** |
| Peer Review | 13 | ~10 min |
| Quick Share | 14 | ~3 min |
| Break It | 15 | ~8 min |
| Four-Tab Reveal | 16 | ~3 min |
| Wrap | 17–20 | ~8 min |
| **Total** | | **~92 min** |

Hands-on ratio: ~55% (Lab Parts 1–3 + Mini Activity + Peer Review + Break It)

---

## How It Addresses Carlos's Feedback (Mar 3 Session)

- **"The magical moment... at least one in every class"** → Three beats: extraction, refactoring, infrastructure connection. The GitHub/Supabase clicks are the "holy shit" moment.
- **"Bring some of M5 up... at least a connection to the database"** → Supabase connected in M4. GitHub connected in M4. M5 builds on top of it.
- **"With Lovable it's one click... just forcing people to do that"** → Lab Part 3 is dedicated to exactly this. One click each.
- **"Structure actually means I have something with a backend logic, a commit button"** → GitHub = commit button. Supabase = backend logic. Both connected before leaving M4.
- **"Allocate maybe 5 minutes for account creation"** → 3 min allocated in Lab Part 3, Step 1. Pair faster students with slower ones.
- **"Maybe cutting something that's not super intense"** → Compressed structure judgment + comprehension debt into one slide. Break It shortened to 8 min. Lab Part 2 trimmed from 20 to 12 min.
- **"Skills marketplace"** → Noted for M1 integration (Carlos: "this can be covered in module number one"). Not a major M4 element but can be mentioned when discussing the Living Prompt Pack Builder.
