# Module 5: Make It Real — Speaker Notes for Carlos

> For Carlos only. High-level bullets explaining what we're doing and why.
> Slide numbers match the Gamma Prompt (slides 1–23). Update if Gamma reorders.

---

## Where M5 Sits

- M1 = speed, M2 = aim, M3 = precision, M4 = structure, **M5 = integration**
- The hinge between "it looks real" and "it IS real"
- Students go from owning infrastructure (GitHub + Supabase connected) → owning a **working product with real data, real users, and graceful error handling**
- M4 connected the pipes. M5 turns on the water.
- This is Carlos's "oh shit" moment: *"I can connect to a database. I can connect to Stripe. Oh, shit. I can push something to production. That would be magic."*

---

## The M5 Wow (Three Beats + Chaos)

- **Beat 1 — The Persistence Moment (after database):** Student enters data. Refreshes the page. The data is still there. Opens Supabase dashboard — the data is sitting in a real table. "This isn't a mockup anymore." This is the single biggest reaction in the course.
- **Beat 2 — The Multi-User Moment (after auth):** Student logs in as User A. Sees their data. Logs out. Signs up as User B. Completely different data. "This is a real product." The room shifts.
- **Chaos Round (bonus beat):** Instructor triggers failures. Students who handled edge cases see error messages. Students who didn't see blank screens. Visceral contrast. "Real products break. Yours should break gracefully."
- **Beat 3 — The Deploy Moment (after five-tab reveal):** Instructor clicks Deploy in Lovable. Gets a live URL. Opens it on phone. Drops it in Slack. Students deploy their own products. They open them on their phones. They share URLs with classmates. "That's your product. On your phone. With a real URL." This is the emotional climax.
- **Crescendo:** Five-tab reveal → deploy → product on their phone. The progression from single page to live deployed product.

---

## What Changed From M4 (Carlos's Feedback, Mar 3)

- **GitHub + Supabase were moved INTO M4** per Carlos's feedback — so M5 now starts with infrastructure already connected
- **M5 builds ON TOP of M4's infrastructure** — schemas, auth, edge cases, not connection setup
- **Three integration prompts** — Database → Auth → Edge Cases. Same 3-prompt pattern students know from M3, applied to backend
- **Chaos Round is new** — instructor-triggered failures. Makes edge cases visceral, not theoretical
- **Break It focuses on zero error handling** — a product with a backend but no error handling is WORSE than a static prototype
- **Engineering Handoff Note (Deliverable #5)** — the bridge document between Living PRD (what it does) and technical reality (what's connected)

---

## Slide 1 | Opening (Title + 3 Waypoints)

- Three waypoints: Real Database Schemas, Authentication, Edge Cases & API Integrations
- "M4 connected the infrastructure. Today you build on top of it."
- The infrastructure is there from M4 — but the database has no tables, there's no auth, no error handling
- Frame it as: the facade becomes real today

---

## Slide 2 | Bridge from M4 + Agenda

- "Enter data, close the tab, reopen it. The data is gone. Log in as a different user — you can't."
- Names the gap between connected infrastructure and working product
- Creates pull for the demo: they want to see the facade fall away
- Agenda: Demo → Teaching → Lab → Chaos → Break It → Wrap

---

## Slides 3–5 | Demo (Setup → Live Build → Debrief)

- **Slide 3:** Pull up M4 Retention Engine. Show the polished UI. Open Supabase dashboard — project exists, zero tables. Demonstrate: type an invite, refresh — gone. "Connected but empty."
- **Slide 4:** Run 3 prompts live:
  - **Prompt 1 — Database:** Create tables, store invites, fetch real data. ~90 sec.
  - **Prompt 2 — Auth:** Login/signup, different users see different data. ~90 sec.
  - **Prompt 3 — Edge Cases:** Connection errors, empty states, loading skeletons. ~60 sec.
- **Slide 5:** Debrief. "Same prototype. Same 5 screens. Now the data persists, users are real, and errors are handled."
- **Total demo: ~8 minutes.** The persistence moment (Beat 1) and multi-user moment (Beat 2) are the biggest reactions. Let them land. Don't rush past them.
- **KEY DEMO MOMENT:** Open the Supabase dashboard AFTER Prompt 1. Show data appearing in the table. "Remember — you connected this in M4. Now there's actually data in it." This is the Carlos moment.

---

## Slides 6–8 | Teaching (Integration Patterns + Edge Cases + Handoff Note)

- **Slide 6 — Integration Patterns:** Three patterns — Database (Supabase), Auth (Supabase Auth), External APIs (Stripe, SendGrid). Keep at 3 minutes. "You describe what should happen. The AI integrates it."
- **Slide 7 — Edge Case Thinking:** The 5 edge cases every product needs (Loading, Empty, Error, Conflict, Boundary). Key message: "If you can describe the failure, the AI can handle it."
- **Slide 8 — Engineering Handoff Note:** Deliverable #5. The bridge between Living PRD (what it does) and technical reality (what's connected). Five sections: Integrations, Real vs. Mocked, Data Model, Edge Cases, Start Here.
- Combined teaching: ~12 minutes. Don't go deep on SQL or API docs — the point is PMs describe backend behavior in plain English
- Stress on Slide 8: honesty over polish. "If the Stripe integration is faked, say so."

---

## Slide 9 | Mini Activity (What Would You Integrate?)

- Students look at their own M4 prototype: what's hardcoded? who are the users? what breaks?
- Same gap-surfacing pattern as M3 and M4 — feel the problem before the lab
- Most will realize: "Everything is hardcoded"
- After 5 minutes: "Who said database? Who said auth? Who said both?" → sets up the lab

---

## Slide 10 | Security Basics (60 Seconds)

- Not a security lecture — 60 seconds of good habits
- Do: RLS, HTTPS, don't expose API keys, hash passwords (Supabase handles most of this)
- Don't: store sensitive data you don't need, skip auth, trust user input
- Key line: "If it has a database, it needs auth"
- Keep this fast — don't slow momentum before the lab

---

## Slides 11–12 | Lab Parts 1 & 2: Database + Auth + Edge Cases — THE FIREWORKS

- **Slide 11 — Part 1: Database (15 min)** — Open Integration Planner, select scenario, customize schema, copy database prompt into Lovable. Test: enter data, refresh.
  - **THIS IS BEAT 1.** Walk the room. Watch for the moment a student enters data, refreshes, and the data is still there. That's the persistence moment. "Your data just survived a page refresh. That database you connected last module? It's working."
  - If anyone's Supabase isn't connected from M4, help them connect (one click)
  - After 15 min: "Who has persistent data? Show me a refresh."

- **Slide 12 — Part 2: Auth + Edge Cases (15 min)** — Auth prompt (10 min): signup/login, different users see different data. Edge case prompt (5 min): loading states, error handling.
  - **THIS IS BEAT 2.** The multi-user moment. Student logs in as User A, sees data. Logs out. Logs in as User B — different data. "You just built a multi-user product."
  - Edge cases: "Open DevTools (F12) → Network → check Offline. What happens? Does your app crash or show an error message?" (This only affects the browser tab — Zoom stays connected.)
  - After 15 min: "Stop. You have a real database, real auth, and error handling. That's a working product."

- **Tool:** Integration Planner has pre-built prompts for all 4 scenarios. Students customize and copy.
- **Key instructor behavior:** Walk the room for both beats. The reactions happen in students' hands, not on the big screen.

---

## Slide 13 | Chaos Round — Things Break

- **This is the memorable exercise Carlos asked for**
- Instructor triggers chaos — three rounds:
  - **Round 1:** Chrome DevTools → Network → Offline checkbox. Error message vs. blank screen. (Only affects the browser tab — Zoom/video call stays connected.)
  - **Round 2:** 500 invites in 1 second. Rate limiting? Frozen UI?
  - **Round 3:** API returns unexpected data format. Validation? Graceful fallback?
- Make it dramatic. For Round 1, walk students through DevTools (F12 → Network → Offline). Alternative: right-click any Supabase request → "Block request domain" to block only Supabase calls
- Group discussion: "Which would you fix first?" → Usually Round 1 (connection failure, 100% of users)
- 10 minutes total. Prioritization thinking is the real skill here.

---

## Slide 14 | Quick Share

- "What was easier than expected? What was harder?"
- Surface insights — fast, 1 minute
- Transition line: "If you can describe your backend in one sentence, you can write the handoff note"

---

## Slide 15 | Break It — Zero Error Handling

- The cautionary tale: a real product with database, auth, APIs — but zero error handling
- Pick the two most visceral failures: slow network (infinite spinner) and database unreachable (blank screen)
- Show the WITH vs. WITHOUT error handling side by side. Same failure. Completely different user experience.
- Key message: "A backend without error handling is worse than no backend at all. Users trust that 'real' products work."
- 5 minutes. Compressed to make room for deployment. The contrast still makes the point.

---

## Slide 16 | Five-Tab Reveal — M1. M2. M3. M4. M5.

- Same pattern as M4's four-tab reveal — now five
- Let students open all five. 30 seconds of silence.
- "In M1, you typed a prompt and got a page. In M5, you have a multi-user product with a real database, authentication, and error handling. That's not a prototype anymore."
- This is the crescendo — and you're about to deploy it right now.

---

## Slides 17–19 | Deploy — THE CLIMAX

- **Slide 17 — Instructor Demo: Deploy:** Pull up the Retention Engine in Lovable. Click Deploy. Get the live URL. Open on phone. Drop in Slack. "One click. 30 seconds. Live." The simplicity IS the point. Students watch a PM deploy a real product.
- **Slide 18 — Lab: Students Deploy (15 min):** Students deploy their own products. Step by step: click deploy, get URL, test in incognito, test on phone, share in Slack, try classmates' URLs. THE KEY MOMENT: when a student opens their product on their phone and it works. Walk the room. If deploy fails, most common issue is Supabase auth redirect URL not including the new deployment domain.
- **Slide 19 — Deploy Debrief (3 min):** "What surprised you?" "What's the difference between preview and deployed?" Quick reactions. The difference is mostly psychological but it matters. A live URL changes perception. "It's not a prototype anymore. It's a product."

---

## Slides 20–23 | Wrap

- **Slide 20 — What You Did Today:** Real Database, Authentication, Edge Cases, Deployed (mirrors slide 1 but now four accomplishments). "You crossed the line from infrastructure to deployed product in one session."
- **Slide 21 — Accountability:** Post live URL ("It's live. Try it." + M1 link for comparison), try 2 other live products, update Living Prompt Pack, finalize Engineering Handoff Note
- **Slide 22 — M6 Preview:** "Measure, Learn, Iterate. Your product is live. Now what?" Analytics, AI-powered analysis, evidence-based improvements, gallery walk, presentations. One module left.
- **Slide 23 — Survey**

---

## Tools

- **Integration Planner** — used DURING lab (slides 11–12). Scenario auto-populate, database schema planning, auth flow, edge case checklist, 3 prompt cards with templates, Engineering Handoff Note section. Full preview + export.
- **Lovable Deploy** — used DURING deploy lab (slide 18). One-click deploy from Lovable's Share menu. Students get a live URL.
- **Living Prompt Pack Builder** (from M3) — continues growing. Students add integration prompts (database, auth, edge cases) to their pack.
- **Living PRD Extractor** (from M4) — students update their Living PRD to reflect what's now real vs. mocked after integration.
- Together: plan → build → document → deploy → hand off

---

## Timing (fits in 2 hours)

| Block | Slides | Duration |
|-------|--------|----------|
| Opening | 1–2 | ~8 min |
| Demo | 3–5 | ~15 min |
| Teaching | 6–8 | ~12 min |
| Mini Activity | 9 | ~5 min |
| Security Basics | 10 | ~3 min |
| Lab Part 1: Database | 11 | ~15 min |
| Lab Part 2: Auth + Edge Cases | 12 | ~15 min |
| Chaos Round | 13 | ~10 min |
| Quick Share | 14 | ~1 min |
| Break It | 15 | ~5 min |
| Five-Tab Reveal | 16 | ~3 min |
| Deploy Demo | 17 | ~3 min |
| Lab: Deploy | 18 | ~15 min |
| Deploy Debrief | 19 | ~3 min |
| Wrap | 20–23 | ~8 min |
| **Total** | | **~121 min** |

Hands-on ratio: ~58% (Lab Parts 1–2 + Mini Activity + Chaos Round + Break It + Deploy Lab)
Buffer: ~1 min. If tight, compress Deploy Lab to 10 min or trim Chaos Round to 7 min.

---

## How It Addresses Carlos's Feedback

- **"Every module should come with a wow moment"** → Three distinct beats: The Persistence Moment (Beat 1), The Multi-User Moment (Beat 2), and The Deploy Moment (Beat 3). Plus Chaos Round as a bonus beat.
- **"Fireworks all the time"** → 58% hands-on. The wow happens in students' hands, not instructor's. Walk the room for all three beats.
- **"I can connect to a database"** → This IS the module. Students see their data in the Supabase dashboard. Carlos's exact quote is the design principle.
- **"I can connect to Stripe. Oh, shit."** → External APIs covered in teaching (Slide 6). Stripe, SendGrid, any documented API. The pattern is: describe the trigger, describe the action, AI writes the integration.
- **"I can push something to production. That would be magic."** → Deployment is now the M5 climax. One-click deploy, live URL, product on their phone. Carlos's exact words become reality.
- **"Bring some of M5 up... at least a connection to the database"** → Done in M4. M5 now starts with Supabase already connected and builds real schemas, auth, edge cases on top.
- **"Lovable doesn't want to say prototyping anymore"** → M5 explicitly crosses from prototyping to shipping. Students deploy a live product.
- **"Each module significantly better"** → Five-tab reveal makes the progression undeniable. Then deployment makes it permanent — live URL, accessible to anyone.
- **"Break It is memorable"** → Break It with zero error handling: blank screens, crashes, silent failures. Compressed to 5 min but the visceral contrast still lands.
- **"The magical moment... at least one in every class"** → Beat 1 (persistence) is the most universal reaction. Beat 3 (deploy — product on their phone) is the emotional climax of the entire course.
