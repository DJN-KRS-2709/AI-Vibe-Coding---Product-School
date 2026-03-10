# Gamma Prompt: Module 5 Teaching Slide Deck

**Copy everything below the line and paste it into Gamma. Use "Paste an outline" or the prompt field.**

---

## Instructions for Gamma

Create a professional slide deck for teaching a 2-hour workshop called **"Module 5: Make It Real — From Prototype to Product"** in a Vibe Coding certification course. The audience is senior product managers who completed Modules 1–4 — they can build fast (M1), build smart with data (M2), build precise with prompt chains (M3), and structure prototypes with living PRDs, GitHub repos, and Supabase connections (M4); now they're building real backend functionality on top of the infrastructure they connected. Tone: energetic, practical, technical. The deck supports live teaching, demos, and hands-on labs. Avoid corporate jargon. Use clean, modern design with clear typography and minimal text per slide. Match Modules 1–4 visual style. Important: the slides are student-facing — keep the content instructional and practical. Do not telegraph emotional beats or name "wow moments" on slides.

---

## Slide 1 — Module 5 Title + 3 Waypoints
**Make It Real — From Prototype to Product**

MODULE 5 | VIBE CODING CERTIFICATION

Three things today:
1. **Real Database Schemas** — Build real tables, store real data. Your Supabase connection from M4 becomes a working backend.
2. **Authentication** — Real users, real accounts. Different people see different data. Row-level security.
3. **Edge Cases & API Integrations** — What happens when things break? Loading, errors, empty states. Plus: connect external APIs.

Module 1 was speed. Module 2 was aim. Module 3 was precision. Module 4 was structure. Module 5 is where it gets real.

*Speaker Notes: "Welcome back. In M4, you connected GitHub and Supabase — your prototype made the transition with real infrastructure. But that infrastructure is still empty. The database has no tables. There's no authentication. There are no API integrations. Today we build on top of what you connected. Three waypoints: real database schemas, authentication, and edge cases with API integrations. By the end of today, your prototype will have real data that persists, real user accounts, and graceful failure handling. It won't be a prototype anymore. It'll be a working product."*

---

## Slide 2 — Bridge from M4 + Agenda
**Your M4 Prototype Has Infrastructure. But the Database Is Empty.**

Your M4 build has a Living PRD, refactored code in GitHub, a Supabase connection, and an engineering handoff. An engineer could clone the repo. But try this: enter data, close the tab, reopen it. The data is gone. Log in as a different user — you can't. The infrastructure is connected, but nothing is built on top of it yet.

Today you build the backend.

Today's flow:
1. **Demo** — Watch a prototype go from empty infrastructure to functional product
2. **Teaching** — Database schemas, auth patterns, edge case thinking, API integrations
3. **Lab** — Build real tables, add authentication, connect APIs
4. **Chaos Round** — Things break. Handle it.
5. **Break It** — The product with zero error handling

---

## Slide 3 — Instructor Demo: The Setup
**Same Prototype. Infrastructure Connected. Nothing Built On It Yet.**

INSTRUCTOR DEMO

The M4 Retention Engine: 5 screens, interactive states, clean code in GitHub, Supabase connected, Living PRD. Everything from M4.

Watch: I enter an invite. Refresh the page. Gone. I "log in" — no password, no account. The PM dashboard shows hardcoded numbers that never change. The Supabase dashboard shows no tables. The infrastructure is there, but it's empty.

3 prompts. Watch what changes.

*Speaker Notes: Pull up the M4 Retention Engine in Lovable. Click through to show the polished UI. Open the Supabase dashboard in a tab — show that the project exists but has no tables. "In M4, you connected the infrastructure. Today you build on top of it." Then demonstrate: type an invite, refresh — gone. "The database is connected but empty. 3 prompts." Keep this fast — 2 minutes setup.*

---

## Slide 4 — Live Build: 3 Prompts
**The Integration Chain**

**Prompt 1 — Database Schema:** "Create a 'users' table and an 'invites' table in Supabase. When a user sends an invite on Screen 2, store it in the invites table with the sender email, recipient email, and timestamp. When the team workspace (Screen 3) loads, fetch all invites for this user from Supabase and display them. When the PM dashboard (Screen 4) loads, query the invites table to calculate actual invite rate and display the real number."

**Prompt 2 — Auth:** "Add Supabase authentication. Add a login/signup screen before the onboarding flow. Users sign up with email and password. After login, the app fetches only their team's invites. Different users see different data. Show the logged-in user's name in the header. Add a logout button."

**Prompt 3 — Edge Cases:** "Handle these failure modes: If the Supabase connection fails, show 'Connection error — please try again' instead of a blank screen. If the user has no invites yet, show 'No invites sent yet — start by inviting your team' instead of an empty list. If the invite submission fails, show 'Couldn't send invite — check the email and try again' with a retry button. Add a loading skeleton while data is being fetched from Supabase."

3 prompts. Real data. Real users. Real error handling.

*Speaker Notes: Run the 3 prompts sequentially. Prompt 1: paste, wait ~90 sec. Send an invite. Refresh the page. "The invite is still there. It's in a real database." Open the Supabase dashboard — show the data appearing in the table. "Remember — you connected this in M4. Now there's actually data in it." Prompt 2: paste, wait ~90 sec. Log out. Sign up as a new user. "Different user, different invites. Real multi-user behavior." Prompt 3: paste, wait ~60 sec. Open DevTools (F12) → Network → check Offline (this only affects the browser tab, not Zoom). "Connection error. The app tells you what happened instead of showing a blank screen." Uncheck Offline. "And it recovers." Total: ~8 minutes. Let the moments land — the persistence moment and the multi-user moment are the biggest reactions you'll get all course.*

---

## Slide 5 — Demo Debrief
**What Changed**

Same prototype. Same 5 screens. Same design.

- **Data persists** — invites are stored in Supabase tables you built on top of M4's connection. Refresh, close tab, reopen — they're still there.
- **Users are real** — login, signup, personalized data. Different users see different things.
- **Failures are handled** — connection errors, empty states, loading states, retry logic.

Before: connected infrastructure with no tables, no auth, no error handling.
After: a working product with real schemas, real users, and graceful failures.

That's the line between infrastructure and product.

*Speaker Notes: "In M4, you connected the infrastructure. Today you built on top of it. The data persists, users are real, and errors are handled. You crossed from infrastructure to product. And you did it with 3 prompts." Transition to teaching: "Let me show you what's actually happening under the hood."*

---

## Slide 6 — Integration Patterns
**How Lovable Connects to the Real World**

Three integration patterns you'll use today:

**1. Database (Supabase)**
Your data lives in tables. Read, write, update, delete. The AI writes the SQL and the API calls. You describe what data to store and when to fetch it.

**2. Authentication (Supabase Auth)**
Signup, login, logout, sessions. The AI wires it up. You describe who should see what. Row-level security means users only see their own data.

**3. External APIs**
Stripe for payments. SendGrid for email. Any API with documentation. The AI reads the docs and writes the integration. You describe the trigger and the action.

You don't write the code. You describe what should happen. The AI integrates it.

*Speaker Notes: Keep this at 3 minutes. Show the Supabase dashboard — tables, auth users, RLS policies. "You connected Supabase in M4. Now you're building on it — tables, auth, security. Lovable talks to Supabase. You describe what data to store and what happens when — the AI writes the integration code." Don't go deep on SQL or APIs — that's not the point. The point is: PMs can describe backend behavior in plain English and the AI makes it work.*

---

## Slide 7 — Edge Case Thinking
**Real Products Break. Yours Should Break Gracefully.**

Prototypes assume the happy path. Products don't.

**The 5 edge cases every product needs:**
1. **Loading** — What does the user see while data is being fetched? (Skeleton screens, spinners)
2. **Empty** — What if there's no data yet? (Helpful message + CTA, not a blank screen)
3. **Error** — What if the API fails? (Error message + retry, not a crash)
4. **Conflict** — What if two users do the same thing simultaneously? (Last-write wins, or merge)
5. **Boundary** — What if there are 10,000 items instead of 10? (Pagination, not a frozen page)

If you can describe the failure, the AI can handle it. Most prototypes fail because nobody described what should happen when things go wrong.

*Speaker Notes: "Most prototypes only handle the happy path — everything works, data loads instantly, users do what you expect. Real products handle the unhappy paths too. Five edge cases. You don't need to code them — you need to describe them. 'When the API fails, show an error message with a retry button.' That's it. The AI builds it." Quick poll: "How many of you have thought about what happens when your prototype's data source is down?" Most won't have. "That's what M5 fixes."*

---

## Slide 8 — The Engineering Handoff Note
**Deliverable #5: What Engineers Actually Need From You**

The Living PRD (M4) describes the product. The Engineering Handoff Note describes the technical reality.

**What goes in the Handoff Note:**
- What integrations exist and how they work (Supabase tables, auth model, API endpoints)
- What's truly functional vs. what's still mocked
- The data model — real schema, not placeholder
- Edge cases handled vs. known gaps
- "Start here" guide: if an engineer inherits this tomorrow, where do they begin?

This is NOT a technical spec. It's a PM's honest assessment of what's real and what's not — written so engineers don't waste time discovering it themselves.

*Speaker Notes: "This is the bridge document. Your Living PRD says what the product does and why. The Handoff Note says what's technically real and what's still mocked. Together, an engineer can pick this up and start building without reverse-engineering your prototype." Stress: honesty over polish. "If the Stripe integration is faked, say so. Engineers respect PMs who are honest about what's real."*

---

## Slide 9 — Mini Activity: What Would You Integrate?
**Plan Before You Build**

INDIVIDUAL EXERCISE | 5 MINUTES

Look at your M4 prototype (Supabase is already connected from M4). Answer three questions:

**1.** What data is currently hardcoded that should come from a database? (User info, metrics, content, settings)

**2.** Who are the different users? Should they see different things? (Roles, permissions, personalization)

**3.** What breaks if the data source is slow or unavailable? (Which screens would be blank or frozen?)

**Post in Slack:** Your top integration priority — the one thing that would make the biggest difference.

*Speaker Notes: This sets up the lab. Students identify their own integration priorities before you give them the tools. Most will realize: "Everything is hardcoded." After 5 minutes: "Who said database? Who said auth? Who said both?" Most will say both. "Good. That's exactly what you'll build in the next 30 minutes."*

---

## Slide 10 — Security in 60 Seconds
**Security Checklist — The One-Page Version**

You're a PM, not a security engineer. But know the basics:

**Do:**
- Use Supabase Row-Level Security (RLS) — users only see their own data
- Use HTTPS (Lovable does this by default)
- Never expose API keys in frontend code (Supabase handles this with anon keys + RLS)
- Hash passwords (Supabase Auth does this automatically)

**Don't:**
- Store sensitive data in the prototype you don't need (no real SSNs, credit cards, etc.)
- Skip auth because "it's just a prototype" — if it has a database, it needs auth
- Trust user input — validate on the server side

This is a prototype, not production. But good habits start now.

*Speaker Notes: Keep this brief — 60 seconds max. Don't turn it into a security lecture. "You don't need to be a security expert. But if your prototype has a database, it needs auth. If it has auth, it needs RLS. Supabase handles most of this for you. The main rule: don't store data you don't need, and never expose API keys in frontend code." Quick enough that students absorb the habits without slowing the momentum before the lab.*

---

## Slide 11 — Lab Part 1: Build the Database Schema
**Hands-on Lab Part 1: Build Real Tables** | 15 Minutes

Open the **Integration Planner** tool. Select your scenario. Your Supabase is already connected from M4 — now you're building on it.

**Step 1 (3 min):** Review the database schema the Planner suggests. What tables? What fields? Customize for your prototype.

**Step 2 (10 min):** Copy the database prompt from the Planner into Lovable. It will create the tables in your connected Supabase project. Test: enter data, refresh the page. Is it still there?

**Step 3 (2 min):** Document in the Planner: What data persists now? What's still hardcoded?

The moment your data survives a page refresh — that's the line.

*Speaker Notes: Drop the Integration Planner link in Slack. Walk the room. "You connected Supabase in M4. Now you're building real tables on top of it." The database prompt usually takes 60-90 seconds. The KEY MOMENT: when a student enters data, refreshes, and the data is still there. Watch for their reaction. "Your data just survived a page refresh. That database you connected last module? It's working." If anyone's Supabase isn't connected from M4, help them connect it now (one click). After 15 min: "Who has persistent data? Show me a refresh."*

---

## Slide 12 — Lab Part 2: Add Auth + Edge Cases
**Hands-on Lab Part 2: Auth & Edge Cases** | 15 Minutes

**Auth (10 min):** Copy the auth prompt from the Planner into Lovable. Add signup/login. Test: create an account, log in, see your data. Log out. Create a different account — different data.

**Edge Cases (5 min):** Copy the edge case prompt. Handle at least 2: loading state while fetching from Supabase, and an error state if the connection fails.

**Document in the Planner:** What integrations work? What's still mocked? What edge cases are handled?

*Speaker Notes: THIS IS THE WOW MOMENT. Walk the room. At auth: watch for the moment a student logs in as User A, sees their data, logs out, logs in as User B, and sees different data. That's the multi-user moment. "You just built a multi-user product. Different people, different data, same prototype." At edge cases: "Open DevTools → Network → Offline. What happens? Does your app crash or show an error message?" After 15 min: "Stop. You have a real database, real auth, and error handling. That's a working product."*

---

## Slide 13 — Chaos Round
**Chaos Round: Things Break** | 10 Minutes

INSTRUCTOR-LED EXERCISE

The instructor triggers chaos. You handle it.

**Round 1:** "Your Supabase project is paused. What does your user see?" (If you handled it: error message. If not: blank screen or crash.)

**Round 2:** "A user sends 500 invites in 1 second. What happens?" (Rate limiting? Pagination? Frozen UI?)

**Round 3:** "The API returns data in a format you didn't expect. What breaks?" (Validation? Type checking? Graceful fallback?)

Discuss: Which of these would you prioritize fixing first? Why?

*Speaker Notes: Make this dramatic. For Round 1: have students open Chrome DevTools (F12) → Network tab → check the "Offline" checkbox. This simulates a network failure for just that browser tab — their Zoom/video call stays connected. "Look at your app. What does your user see?" Let them scramble. Uncheck "Offline" to reconnect. (Alternative: right-click any Supabase request → "Block request domain" to block only Supabase calls.) For Round 2: ask hypothetically — most won't have rate limiting. "That's a real production concern. How would you describe it to an engineer?" Round 3: "What if the invites table returns a date instead of a string?" Discuss as a group: "Which of these three would you fix first?" The answer is usually Round 1 (connection failure) because it affects 100% of users. 10 minutes total.*

---

## Slide 14 — Quick Share
**What Surprised You About Connecting to a Real Backend?**

One insight: What was easier than expected? What was harder? What would you tell your engineering team about this experience?

If you can describe what your backend does in one sentence, you can write the handoff note.

*Speaker Notes: Quick share — 1 minute. Quick hands up: "What was easier than expected? What was harder?" One or two answers, that's it. Land the takeaway: "If you can describe your backend in one sentence, you can write the handoff note." Transition to Break It.*

---

## Slide 15 — Break It: Zero Error Handling
**"Break It" Exercise** — The Product That Never Handles Errors

CAUTIONARY TALE

A demo showing: a real product with a database, auth, and API integrations — but zero error handling.

**Try breaking it:**
- Slow network → infinite loading, no feedback
- Invalid email format → silent failure, user thinks it worked
- Database unreachable → blank screen, no explanation
- Two users editing the same record → last write wins, data lost
- 10,000 results → page freezes for 30 seconds

**The lesson:** A backend without error handling is worse than no backend at all. Users trust that "real" products work. When yours doesn't tell them what went wrong, they blame the product — not the network.

*Speaker Notes: Use a prepared example. Pick the two most visceral failure modes — slow network (infinite spinner) and database unreachable (blank screen). Show each briefly, then show the graceful version. "Same failure. Completely different user experience." The contrast makes the point: backend without error handling creates a worse experience than a static prototype. Keep this to 5 minutes — the deployment demo is coming.*

---

## Slide 16 — Pull Up All Five
**M1. M2. M3. M4. M5. Side by Side.**

Open five tabs.

**Module 1:** One prompt, one page. Static. No data.

**Module 2:** Real data, hypothesis, design-matched. Still hardcoded.

**Module 3:** 5+ screens, states, documented chain. Still a facade.

**Module 4:** Clean code in GitHub, Supabase connected, Living PRD, engineering handoff. Infrastructure ready.

**Module 5:** Real database, real auth, real error handling. It actually works.

Same tool. Same you. Five modules of progression.

*Speaker Notes: Same pattern as M4's four-tab reveal — now five. Let students open all five. 30 seconds of silence. "In M1, you typed a prompt and got a page. In M4, you connected infrastructure. In M5, you built a multi-user product with real database schemas, authentication, and error handling on top of that infrastructure. That's not a prototype anymore." This is the crescendo of the production half. And you're about to deploy it — right now.*

---

## Slide 17 — Instructor Demo: Deploy
**From Working Product to Live URL in One Click**

INSTRUCTOR DEMO

Your M5 product has real data, real auth, real error handling. It works. But it lives inside Lovable's preview. Share the link — it works. Close Lovable — it might not. Nobody outside this class has seen it.

Watch: I click "Deploy." 30 seconds later, it has a live URL. I open it on my phone. I send the link in chat. You can open it right now.

That's deployment. One click. Your product is in the world.

*Speaker Notes: "Pull up the Retention Engine in Lovable. Show the preview — it works, data persists, auth works. Then: 'Watch.' Click the deploy button in Lovable (top right → Share → Deploy or Publish). Wait for the URL to generate. Open it in a new incognito window. Open it on your phone. Drop the link in the Zoom chat or Slack. 'Click it. You're using my product right now. That URL didn't exist 30 seconds ago.' This is the simplest demo in the course — one click — but the impact is huge. They just watched a PM deploy a real product to a live URL."*

---

## Slide 18 — Lab: Deploy Your Product
**Hands-on Lab: Deploy** | 15 Minutes

Open your M5 prototype in Lovable. You're going live.

**Step 1 (3 min):** Click Deploy. Get your live URL. Open it in a new incognito window. Does it work?

**Step 2 (2 min):** Test authentication. Create a new account on the live URL. Log in. Does your data persist?

**Step 3 (2 min):** Open on your phone. Is it usable? Can you navigate, log in, see your data?

**Step 4 (3 min):** Drop your live URL in Slack. Try 2 other classmates' live URLs. Sign up. Use them.

**Step 5 (5 min):** If something broke during deploy — debug it. Common issues: Supabase auth redirect URL doesn't include the new deployment domain.

The moment someone else signs up on YOUR product, from THEIR device — that's ship.

*Speaker Notes: "This should take 15 minutes. Most deployments take under a minute. The remaining time is for testing. Walk the room. THE KEY MOMENT: when a student opens their product on their phone and it works. Watch for the reaction. 'That's your product. On your phone. With a real URL. Anyone in the world can open that right now.' If someone's deploy fails: most common issue is Supabase auth redirect URL not including the new domain — help them update it in Supabase settings. After deploy: 'Who's live? Drop your URL in Slack.'"*

---

## Slide 19 — Deploy Debrief
**Your Product Is Live. What Changed?**

Quick reactions:

1. **What surprised you** about seeing your product on your phone?
2. **What's the difference** between a Lovable preview and a deployed URL?
3. **Who already got a sign-up from a classmate?**

The difference is mostly psychological — but it matters. A live URL changes how people perceive your work. It's not a prototype anymore. It's a product. Anyone in the world can access it.

*Speaker Notes: "Quick debrief — 3 minutes. 'What surprised you?' Most common answer: 'I can't believe it actually works on my phone.' Then: 'What's the difference between preview and deployed?' The answer is mostly psychological — but it matters. A live URL changes how people perceive your work. It's not a prototype anymore. Transition: 'Your product is live. You built it, made it real, and shipped it. Next module — we learn from it.'"*

---

## Slide 20 — What You Did Today
**What You Did Today**

**1. Real Database Schemas** — You built real tables on top of M4's Supabase connection. Your data persists. Refresh, close, reopen — it's still there.

**2. Authentication** — Real users with real accounts. Different people see different data. Login, logout, sessions. Row-level security.

**3. Edge Cases** — Your product handles failures gracefully: loading states while fetching, error messages when things break, empty states when there's no data yet.

**4. Deployed** — Your product has a live URL. Anyone in the world can access it. It's not a preview anymore.

Your prototype crossed the line from connected infrastructure to deployed product.

*Speaker Notes: Mirror slide 1 but now with four accomplishments instead of three. "Real database — your data persists. Authentication — real users, real accounts. Edge cases — graceful failures. And deployed — live URL, accessible to anyone. You crossed the line from infrastructure to deployed product in one session." Keep it tight — 2 minutes.*

---

## Slide 21 — Accountability
**ACCOUNTABILITY** | Before We Wrap

**1. Post in #builds:** Your live URL. Caption: "It's live. Try it." Include your M1 link for comparison.

**2. Engage:** Try 2 other live products. Sign up. Does the data persist? Try to break it — what happens?

**3. Update your Living Prompt Pack:** Add your integration prompts (database, auth, edge cases) to the Output Templates section.

**4. Finalize your Engineering Handoff Note:** What integrations are real? What's still mocked? What edge cases are handled? Use the Integration Planner's handoff section.

*Speaker Notes: "Four things before next module. One — post your live URL in #builds with your M1 link for comparison. Let people see the full journey. Two — try two other live products. Sign up. Does the data persist? Try to break it. Three — add your integration prompts to your Living Prompt Pack. Four — finalize the Handoff Note. This is Deliverable #5 — what's real, what's mocked, where to start."*

---

## Slide 22 — Module 6 Preview
**Module 6: Measure, Learn, Iterate**

Your product is live. Now what?

Real products never end. The next step is learning from real usage. Module 6 closes the loop: gather quantitative insights from your deployed product, use AI to analyze what's working and what isn't, and build evidence-based improvements.

**Module 6 — The Feedback Loop:**
- Set up analytics on your live product
- Use AI to evaluate your metrics against your problem statement
- Build one data-driven improvement and redeploy
- Gallery walk — the class experiences each other's products
- Optional: 5-minute pitch with live demo

Module 1: Build fast.
Module 2: Build smart.
Module 3: Build precise.
Module 4: Structure it.
Module 5: Make it real. Ship it.
Module 6: Learn from it.

*Speaker Notes: "Your product is live. But shipping isn't the finish line — it's the starting line for learning. M6 is about the feedback loop: set up analytics, use AI to analyze your data against your problem statement, and make evidence-based improvements. Then the gallery walk — the class experiences each other's products — and optional presentations. One module left. See you then."*

---

## Slide 23 — Survey
**Your Opinion Matters To Us**

Scan the QR code or use the link to share your feedback. Your insights help us improve each cohort.

---

## Design Notes for Gamma
- Match Modules 1–4 visual template exactly (same fonts, colors, layout grid)
- Slides are student-facing course material — keep content clean, instructional, and practical. Do NOT put pedagogical commentary, emotional cues, or "wow moment" labels on slides.
- Slide 1 — Bold title, three waypoints as prominent numbered list (same pattern as M1–M4 slide 1)
- Slide 3 — The demo setup: show Supabase dashboard (connected but empty tables) alongside the prototype. Emphasize "refresh and data disappears" moment.
- Slide 4 — Show the 3 prompts cleanly (Database / Auth / Edge Cases). Students should see the progression.
- Slide 6 — Three integration patterns as distinct visual blocks with icons
- Slide 7 — The 5 edge cases as a numbered checklist — memorable and scannable
- Slide 8 — Handoff Note structure as a clean list
- Slide 12 — Lab prompts must be scannable at a glance. Students reference this while building.
- Slide 13 — Chaos Round: make the rounds feel dramatic and urgent. Bold the failure scenarios.
- Slide 15 — Break It: the failure modes should feel visceral (blank screens, frozen UIs)
- Slide 16 — Five-column layout (M1 | M2 | M3 | M4 | M5). Let the visual comparison speak.
- Slide 17 — Deploy Demo: Keep it minimal. The simplicity IS the point. One click, one URL.
- Slide 18 — Lab: Deploy steps must be scannable. Bold the key moments (live URL, phone test, Slack share).
- Slide 20 — Takeaways now mirror slide 1's three waypoints plus deployment (visual callback, four items)
- Keep all lab slides (11, 12, 13, 18) highly scannable — students reference these while building
