# Module 5: Ship Live Products with Full-Stack Logic — Speaker Notes

Casual talking points for each slide. Not a script — just the key things to say, what to do on screen, and the energy to bring. Module 5 is the emotional peak of the course — this is where the facade becomes a functioning product. The wow moments are when data survives a page refresh and when different users see different data. Real examples from companies like Instagram, Slack, Netflix, and Uber to ground every concept.

**Tools referenced in this module:**
- Lovable (building, database integration, auth, edge cases, deployment)
- Integration Planner (lab tool — schema design, prompt generation, handoff documentation)
- Supabase (database, authentication, Row-Level Security)
- GitHub (version control — carried from M4)

**What to prepare before class:**
- [ ] Open the M4 Retention Engine prototype in Lovable (same one carried from M2/M3/M4 demos — now with clean code, Living PRD, GitHub connected, Lovable Cloud enabled)
- [ ] Have all 3 demo prompts pre-typed in a text file, ready to paste (database, auth, edge cases)
- [ ] Lovable Cloud is already enabled from M4 — verify the project has Cloud connected
- [ ] Have your phone ready for the deploy moment later in the session
- [ ] Integration Planner link ready to drop in Slack
- [ ] Lab guide and exercise links ready in Slack
- [ ] Screen share on

---

## Before We Start

Before we jump in — thank you. We're past the halfway mark now, and the energy I'm seeing from this cohort is incredible. The builds are getting sharper, the questions are getting harder, and the work is getting more real. Keep that momentum.

Same approach for questions:

1. **Raise your hand** if you want to ask something live. I'll give you your turn — I just might not take it immediately if we're mid-exercise, so bear with me.
2. **Drop it in the chat.** I see everything, and I'll address it when the moment is right. Bonus: other participants often jump in with great answers too.
3. **Slack me anytime.** Before, during, after — I'll get back to you.

This way nothing gets lost, and we keep the momentum going.

---

## Slide 1 — Title

Welcome to Module 5 — Ship Live Products with Full-Stack Logic.

You've been building for four modules. Module 1 was speed — you proved you can build. Module 2 was validation — you proved you can build the *right thing*. Module 3 was precision — you orchestrated complex multi-screen systems. Module 4 was structure — you cleaned the code, extracted the spec, and connected infrastructure.

But here's the truth nobody wants to hear: everything you've built so far is a facade. It looks real. It isn't. Enter data, close the tab, reopen it — the data is gone. Log in as a different user — you can't. The metrics on your dashboard? Hardcoded. Today, we make it real.


## Slide 2 — Class Expectations

Same ground rules. Cameras on — it genuinely makes a difference when we can see each other. Be present, arrive on time, participate actively during exercises. Use Slack for all communication. Individual or deep-dive questions will be moved to after-class support to keep the flow going.

Critical for today: all your tools and accounts must be active *before* class. We will not stop or restart for setup. That means Lovable, Supabase, and GitHub should all be ready. If something's broken, fix it during the break or pair up with someone who has it working.


## Slide 3 — Syllabus

Quick refresher on where we are. Six modules across three weeks.

Module 1 was speed — you built at lightspeed and proved you could go from nothing to a working prototype. Module 2 was validation — you injected data and hypotheses to ensure you're solving the right problem. Module 3 was precision — you used prompt chaining to maintain consistency as complexity scaled. Module 4 was structure — you converted your build into version-controlled code with a Living PRD and engineering handoff.

Module 5 — that's today — is where you connect your build to live databases and secure APIs to move beyond the interface. You'll navigate system logic and edge cases to transform standalone features into integrated, production-ready products on a live URL.

Module 6 closes the loop — you measure product performance, use AI-driven analytics, and iterate based on real-world evidence.


## Slide 4 — Presentation Reminder

"We're almost at the end! Next class is your opportunity to volunteer and present your final presentation. We highly recommend this because you get live, actionable feedback from the group. I'll ask for five to six volunteers in Slack today — first come, first serve. Trust me, the people who present always walk away with the sharpest feedback and the most polished final deliverable."


## Slide 5 — Agenda

Four things today.

First — Moving from Standalone Logic to Integrated Systems. We'll look at the gap between what your M4 prototype looks like and what it actually does when you stress it.

Second — How to Implement Live Database Connectivity. The integration patterns, security basics, and edge case engineering that turn a facade into a system.

Third — Hands-on lab: Add Data Schemas and RLS Authentication to Your Prototype. You'll connect a real database, add real auth, and handle edge cases — the same three steps I'll demo for you first.

Fourth — Hands-on lab: Rapid-Fire Stress Test and Deploy Your Product Live. You'll chaos-test your build and then hit the publish button. By the end of today, your product will be live on the internet.


## Slide 6 — Moving from Standalone Logic to Integrated Systems

This kicks off the first major section. Your M4 prototype has structure, documentation, and clean code. But it's still operating in a vacuum — one path, one user, no memory. Let's fix that.


## Slide 7 — Reflection Moment: What's Still Missing?

**ACTION: This is interactive. Give students 5 minutes. Let them think before discussing.**

Open up your prototype from Module 4 and answer honestly:

"Your prototype has come a long way. What do you still think is missing to get it across the finish line as a fully deployed product for multiple users to test?"

And a harder question: "What would happen if two different people tried to edit the exact same piece of information at the same time?"

Feel free to unmute and share, or post your thoughts in the chat.

**Keep this to quick answers from 2-3 volunteers.** There are no wrong answers, but highlight the transition from visual success to functional success. A prototype can look perfect but fail the moment the internet drops or a second user logs in. The goal is to shift their mindset from "Does it look right?" to "Is the logic secure and resilient enough for a stranger to use it?"

**What you say after:** "You've mastered the facade. Today you're finalizing the engine. Module 5 is about the data's journey through the infrastructure — making things work for real by securing the backend and planning for failure."


## Slide 8 — Instructor-Led Demo: From Empty Infrastructure to Persistent Backend

> Instructor demo: **The Customer Vibe — Retention Engine** (B2B PM SaaS — 30% churn, team invites — carried from M2/M3/M4 demos)
> Total demo time: ~10 minutes. Pre-type all 3 prompts before class.

Here's the problem. Your prototype has all the information needed for an engineering handoff — a GitHub repo, clean code, a Living PRD. But what happens when you close the app, refresh, and enter again? Your data is gone.

### STEP 1: Show the Facade (~2 min)

**What you do:** Pull up the M4 Retention Engine prototype in Lovable on screen share. Click through all the screens — the 3-screen onboarding flow, the retention dashboard, the experiment summary. Remind them how polished and structured it is from M4.

**Then demonstrate the facade:** Go through the onboarding flow, "invite" a teammate, refresh the page. The invite is gone. Go to the retention dashboard — the metrics never change. Try to "log in" — there's no real login.

**What you say:** "This is our M4 build. Clean code, Living PRD, GitHub repo, Lovable Cloud connected. An engineer could inherit this. But watch — I go through the onboarding flow, invite a teammate, refresh, and the invite is gone. The retention metrics? Hardcoded. The Day-3 invite rate? Still says 12% no matter what happens. There's no login, no real users. It looks like a product. It's still a facade."

**What you say:** "Three prompts. Watch what changes."

### STEP 2: Prompt 1 — Database (~90 sec)

**Paste this prompt:**

> "Add a real database to this project using Lovable Cloud. Create a 'users' table and an 'invites' table. When a user completes the onboarding flow and invites a teammate, store the invite in the invites table with the inviter's email, the invitee's email, and the timestamp. When the retention dashboard loads, query the invites table to calculate the real Day-3 invite rate and display the actual number instead of the hardcoded 12%. Track onboarding completion in the users table — store which screen the user reached and whether they completed all 3 steps."

**While it generates:** Stay quiet. Let the class watch.

**When it's done:** Go through the onboarding flow. Invite a teammate. Refresh the page. The invite is still there. Go to the retention dashboard — the Day-3 invite rate has updated.

**What you say:** "The invite persists. Close the tab. Reopen it. Still there. The retention dashboard is now calculating real numbers from real data — not hardcoded values. That data is sitting in a real PostgreSQL database."

**Optional power move:** Open the Lovable Cloud dashboard in a new tab. Show the data sitting in the invites table. "There's your data. In a real database. You described what to store and when — the AI wrote the integration."

**Let the moment land. This is Beat 1 — the Persistence Moment.**

### STEP 3: Prompt 2 — Authentication (~90 sec)

**Paste this prompt:**

> "Add authentication to this project using Lovable Cloud auth. Add a login/signup screen before the onboarding flow. New users sign up with email and password. After login, the app checks if this user has completed onboarding — if not, show the 3-screen onboarding flow. If yes, go straight to the retention dashboard. Track invites per user. The retention dashboard should show aggregate data across all users — total invites sent, Day-3 invite rate, retention comparison. Show the logged-in user's name in the header. Add a logout button."

**While it generates:** "Watch — this is where it gets real."

**When it's done:** Log out. Sign up as a new user (e.g., "sarah@acme.com"). See the onboarding flow. Complete it, invite a teammate. Log out. Sign up as a different user (e.g., "mike@acme.com"). See a fresh onboarding flow — Mike's own experience, not Sarah's.

**What you say:** "Different user, different experience. Sarah completed onboarding and invited a teammate. Mike just signed up — he sees the onboarding flow fresh. The retention dashboard shows data from both. This isn't a prototype anymore — it's a multi-user product."

**Let the moment land. This is Beat 2 — the Multi-User Moment.**

### STEP 4: Prompt 3 — Edge Cases (~60 sec)

**Paste this prompt:**

> "Handle these failure modes: If the database connection fails, show 'Connection error — please try again' instead of a blank screen. If a user tries to invite someone who's already been invited, show 'This teammate has already been invited — they'll get a notification' instead of creating a duplicate. If the invite submission fails, show 'Couldn't send invite — check your connection and try again' with a retry button. If no invites have been sent yet, the retention dashboard should show 'No invites tracked yet — data will appear as users complete onboarding' instead of empty charts. Add a loading skeleton while data is being fetched from the database."

**When it's done:** Open Chrome DevTools (F12 → Network → check Offline). Show the error message instead of a blank screen. Uncheck Offline — it recovers. Try inviting the same email twice — see the duplicate message.

**What you say:** "I just killed the connection. Instead of a blank screen, your user sees an error message with a retry option. I tried inviting the same person twice — it caught the duplicate. That's the difference between a prototype and a product. Real products break — yours should break gracefully."

### STEP 5: Debrief (~2 min)

**What you say:**

"Same prototype. Same onboarding flow. Same hypothesis — surfacing team invites to reduce churn. But now:

- Data persists — invites are stored in a real database. Refresh, close, reopen — still there.
- Users are real — login, signup, personalized onboarding state. New users see the flow, returning users skip to the dashboard.
- The retention dashboard shows real numbers — calculated from actual invite data, not hardcoded.
- Failures are handled — connection errors, duplicate invites, empty states, loading skeletons, retry logic.

Before: a visual facade with hardcoded data.
After: a working product with a real backend.

That's the line between prototype and product. And you crossed it with 3 prompts.

You'll do this to your own build in the labs. But first — let me show you what's actually happening under the hood so you know exactly what to ask for."

### THE PROMPTS (copy-paste version for your text file)

```
Prompt 1 — Database:
Add a real database to this project using Lovable Cloud. Create a 'users' table and an 'invites' table. When a user completes the onboarding flow and invites a teammate, store the invite in the invites table with the inviter's email, the invitee's email, and the timestamp. When the retention dashboard loads, query the invites table to calculate the real Day-3 invite rate and display the actual number instead of the hardcoded 12%. Track onboarding completion in the users table — store which screen the user reached and whether they completed all 3 steps.

Prompt 2 — Authentication:
Add authentication to this project using Lovable Cloud auth. Add a login/signup screen before the onboarding flow. New users sign up with email and password. After login, the app checks if this user has completed onboarding — if not, show the 3-screen onboarding flow. If yes, go straight to the retention dashboard. Track invites per user. The retention dashboard should show aggregate data across all users — total invites sent, Day-3 invite rate, retention comparison. Show the logged-in user's name in the header. Add a logout button.

Prompt 3 — Edge Cases:
Handle these failure modes: If the database connection fails, show 'Connection error — please try again' instead of a blank screen. If a user tries to invite someone who's already been invited, show 'This teammate has already been invited — they'll get a notification' instead of creating a duplicate. If the invite submission fails, show 'Couldn't send invite — check your connection and try again' with a retry button. If no invites have been sent yet, the retention dashboard should show 'No invites tracked yet — data will appear as users complete onboarding' instead of empty charts. Add a loading skeleton while data is being fetched from the database.
```

### WHAT TO PRE-BUILD (the night before)

1. **The M4 prototype (the facade):** Your existing M4 Retention Engine — polished UI, clean code, Living PRD, GitHub connected, but still hardcoded data underneath. This should already exist from your M4 demos.

2. **Have all 3 prompts pre-typed in a text file** so you can paste each one instantly.

3. **Have Lovable Cloud enabled** so the database and auth connections are immediate — no setup delays during the demo.

4. **Have your phone ready** for the deploy moment later in the session — you'll open the live URL on your phone to prove it works cross-device.

5. **Deliver the prompts as if live** — paste and let them generate. But if any prompt produces weak output, have a pre-built backup version ready in a separate Lovable project you can switch to.


## Slide 9 — How to Implement Live Database Connectivity

This kicks off the teaching section. We'll cover the three integration patterns, resistance engineering for edge cases, and security basics — everything students need to know before they start building.


## Slide 10 — How to Prompt for Integration

The slide shows three columns. Don't just read them — frame the mindset shift.

"You're moving from a linear prototype — one path, one user — to a matrixed product that handles multiple users and states with permanent memory. That's a fundamental shift in how you communicate with the AI. You're no longer prompting for visual elements. You're prompting for technical transactions."

Walk through the three pillars by connecting them to what students already know:

**Define Your Schema Structure** — "Every professional application relies on a source of truth that exists outside the user interface. You need to act as the data architect — specify table names, data types, and relationships. Be specific. 'Create a table for Invites with fields for sender_email, recipient_email, and a status timestamp.' That level of precision is what makes the difference between a database that works and one that corrupts."

**Script Ownership Permissions** — "In a live environment, the most critical layer of logic is identity. A prototype is identity-blind — it treats every visitor the same. A real product must be identity-aware. You define the rules of ownership by implementing Row-Level Security — RLS. Think of it as the bouncer at the door: 'Ensure users can only see records where the user_id matches their authenticated session ID.' That's the line between a shared demo and a secure, multi-tenant platform."

**Orchestrate External APIs** — "This is how you add superpowers without writing the code. Payments through Stripe, emails through SendGrid, AI through OpenAI. Your job is to provide the API documentation and clearly define the trigger and the action. 'Connect the Stripe API. Trigger a checkout session when Upgrade is clicked and return to the dashboard on success.' You describe the contract — the AI builds the bridge."


## Slide 11 — Resistance Engineering for Errors & Failures

The slide shows four product states. This is where most prototypes fail — nobody described what should happen when things go wrong.

"Most prototypes are designed for the happy path — the path where everything works perfectly. Real products handle the unhappy paths too. If you can describe these failure modes to the AI, it can build the safety nets. Let me walk you through the four states you need to engineer for."

**Empty States** — "Every user starts at zero. If that experience is a blank box with no instructions, the system has failed the user on day one. Replace blank screens with active empty states. If a search or a table is empty, the system must provide a 'Get Started' CTA rather than a dead end."

**Loading States** — "In a live environment, data takes time to travel, and silence in the UI often leads to user abandonment. Don't just show a spinner — implement skeleton screens that show the structure of the data before it arrives, keeping the user anchored in the flow."

**Error States** — "APIs and databases are external dependencies that *will* eventually fail or timeout. Don't let that crash your app. Every failed transaction must trigger an inline error with a 'Retry' button to keep the session alive. Shift from crashes to graceful recoveries."

**Load Bearing States** — "This is where vibe coding usually breaks. A prototype works with 5 rows of data, but a real product must remain stable with 5,000. If you don't tell the AI how to handle 10,000 items, it will try to load them all at once and crash the browser. Use pagination for large datasets and 'Last-Write-Wins' logic for simultaneous edits."

Land it: "Building for the happy path is easy, but it's not shipping. Real products are defined by how they handle the 10% of the time that things go wrong. By engineering for these edge cases now, you're building a resilient, market-ready system."


## Slide 12 — Security Best Practices

The slide shows a Do/Don't checklist. Keep this brief — 2-3 minutes. Don't turn it into a security lecture.

"You're a PM, not a security engineer. But it's good to know the basics and build good habits. Most tools handle this for you automatically. Your job is to not work against it."

Walk through the Do column conversationally:

"Use Row-Level Security — without RLS, your database is a free-for-all. Use environment variables — keep API keys in 'Secrets' and out of your frontend code. Trust the infrastructure — Supabase handles password hashing and HTTPS for you. And if the UI looks right but the data is missing, check the API connection before re-prompting — diagnose the symptom."

Then the Don't column: "Never leave a database open because 'it's just a prototype.' If it has data, it needs a login. Never paste raw API keys into a prompt, tool, or file — once a key is in the code, it's no longer a secret. Don't collect real SSNs or credit card numbers you don't need to test. And never assume form data is valid — always validate server-side."

"Keep these in mind as you start to build. Good habits now save painful security conversations later."


## Slide 13 — Individual Exercise: Plan Before You Build

**ACTION: Give students 20 minutes. They should NOT open Lovable yet — this is pre-work to audit their gaps. Create breakout rooms for a "co-working" environment. Remain in the main room to troubleshoot.**

"Before you start building, you need to know exactly what needs to be made real. This exercise is a quick audit of your technical debt — you're mapping your data, user roles, and failure points to create a functional execution plan."

Drop the exercise guide link in Slack and orient them on the three steps:

"Start with the Data Status audit — list the key hardcoded elements in your UI. User metrics, account names, dashboard numbers — anything that's currently a placeholder that must be replaced by a live database. Focus on the source of truth for your most important data."

"Next, the User Status — identify the key roles in your system. Do different users need different permissions or personalized views? This is the logic that will govern your authentication flow."

"Finally, the Error and Data Handling Status — flag key screens or features that would currently freeze or appear blank if the data source was slow or unavailable. These are your targets for resilience logic."

"Do *not* open Lovable yet. This is a planning exercise. You need to identify your targets before you start prompting."

**Watch for:** Students who skip ahead to Lovable. Pull them back — the audit is what makes the build phase efficient.


## Slide 14 — Quick Debrief: Top Integration Priority

**ACTION: 2 minutes. Quick Slack post.**

"Based on your quick audit, what is your top integration priority — the one thing that will make the biggest difference in your prototype? Post one sentence in our Slack channel."

As the responses come in, read them aloud and comment on patterns. Most students will say database or auth — validate that. "Notice how many of you identified the same gap? That's because every prototype hits this wall at the same point. The data is the foundation — without it, nothing else holds up."


## Slide 15 — Hands-On Lab: Add Data Schemas and RLS Authentication To Your Prototype

This is the moment the module pivots from theory to practice. The win here is the page refresh — seeing data stay on the screen when it used to disappear.


## Slide 16 — Individual Exercise: Add Data Schemas and RLS Authentication

**ACTION: Give students 30 minutes. Create breakout rooms for a "co-working" environment. Remain in the main room for support. Drop the exercise guide link in Slack.**

"This is the magic moment. You are about to turn a drawing into a system. If your data survives a refresh, you've officially moved past prototyping."

Walk them through the five steps before they start:

"Step 1 — Review your suggested database schema in the Integration Planner. Customize the specific tables and fields required for your project. Don't skip this — if your schema is wrong, everything built on top of it will be wrong."

"Step 2 — Copy the database prompt into Lovable to create live tables in Supabase. Once it runs, perform the Persistence Test: enter data into your app, refresh the browser, and verify the data is still there. That refresh is the moment of truth."

"Step 3 — Execute the Authentication prompt to add signup and login flows. This isn't just a UI change — it's activating Row-Level Security. Your data is now partitioned by user."

"Step 4 — Run a test sequence. Create two separate accounts. Verify that User A cannot see User B's data. This confirms your RLS is working correctly."

"Step 5 — Implement your Edge Case prompts. Add loading skeletons and error messages that handle slow or failed data connections. Pick at least two."

"Keep in mind: You must verify that your data persists after a refresh and that different logged-in accounts see different data. Those are your two checkpoints."

**Watch for:** The persistence moment — when a student enters data, refreshes, and the data is still there. Watch their face. That reaction is the emotional peak. Walk up and narrate it: "Your data just survived a page refresh. That's not a prototype anymore."

The multi-user moment is the second hit — when they log in as User A, see their data, log out, log in as User B, and see different data. "You just built a multi-user product. Different people, different data, same prototype."

**Common issues:** If students get stuck on the Supabase connection, pair them with someone who has it working. If the auth redirect fails after deploy, the redirect URL needs to include the new deployment domain — help students update this in Lovable Cloud settings.

**After 30 minutes:** "Stop. You have a real database, real auth, and error handling. That's a working product."


## Slide 17 — Break

Quick 5-minute break. You've earned it — that was the hardest lab of the course. Grab some water, stretch, and we'll be right back.


## Slide 18 — Cameras On

Welcome back! Quick reminder — it's always better to see your smiling face. Be present and visible to stay engaged and keep interactions valuable.


## Slide 19 — Reflection Moment: Post-Lab Q&A

**ACTION: This is interactive. Give students 5 minutes. Let 2-3 volunteers share.**

"Now that you've connected a live backend, what surprised you most? Was the biggest challenge building the functional logic, or anticipating all the ways it could fail?"

And a follow-up to push deeper: "What would happen if a user with a slow connection tried to submit a form three times because they didn't see a loading state?"

Feel free to unmute and share, or post your thoughts in the chat.

**What you'll hear:** Most students will find that getting the database to work was fast, but realizing how many ways a user can break it is the real eye-opener. Validate that: "That's exactly right. The complexity in product management often comes from these invisible edge cases, not the visible features."

**Land this:** "Anyone can prompt a pretty UI. A Product Manager's value lies in orchestrating the logic that makes that UI resilient — and you've successfully done that today."


## Slide 20 — Rapid-Fire Stress Test and Deploy Your Product Live

"We're in the final stretch. You've built the backend. Now you stress-test it, and then you ship it live."


## Slide 21 — Chaos Round: Pick Your Stress Test

**ACTION: Keep students all together in the main room. 15 minutes total. Suggest one volunteer to share their screen and run through their chosen stress test — put the student in the driver seat while others follow along.**

Frame this as a professional launch: "In a real product cycle, you never ship 'perfect' code — you ship code with known risks. If your Stress Test reveals a flaw, you have two choices: fix it now with one final prompt, or document it as a 'Known Issue' in your Handoff Note and deploy anyway. Both are valid PM moves. Ignoring the flaw is the only mistake."

Walk through the three stress tests:

**The Kill Switch** — "Open DevTools, go to Network, and set to 'Offline.' Does your UI acknowledge the disconnection, or does it simply hang? If it hangs, that's a P0."

**The Ghost User** — "Sign up with a brand new email. Does the user see an active empty state with a CTA, or a blank screen? Remember — every real user starts at zero."

**The Spam Click** — "Hit your 'submit' button 5 times rapidly. Does your database create 5 duplicate records, or is the transaction handled correctly? This happens more than you'd think."

"Choose one. You don't need to do all three — but you can if you want. Run the test, observe the result, and make a Go/No-Go decision."

**After the stress test:** "If it passes, you're ready to deploy. Click 'Publish' in Lovable and generate your live URL. If it fails and it's a P0 blocker, run one final prompt to fix it. If it's a known gap you can live with, document it in your handoff and then publish."

### DEPLOY MOMENT

**This is the climax of the module — possibly the entire course.**

"Alright. You've all just built real backends — databases, auth, error handling. Your apps work. But right now, they only work inside Lovable. Nobody else on the planet can use what you built. Let's fix that."

**What you do:** In Lovable, click the **Share** button (top-right) → then click **Publish**. Lovable builds and deploys the app. A progress indicator appears — takes about 20-30 seconds.

**While it deploys:** "One button. That's it. No CI/CD pipeline, no server configuration, no DNS records, no Dockerfile. One click."

**When the URL appears:** Copy the live URL. Paste it into the browser address bar. The app loads — with the login screen.

**What you say:** "That URL is live. Right now. On the internet."

**Phone moment:** Pull out your phone. Open the URL in your phone's browser. Hold the phone up so the class can see. Sign up as a brand new user on your phone. Complete onboarding. Go back to your laptop — log in as a different account. Show the data from the phone appearing in the dashboard.

**What you say:** "I just signed up on my phone. Went through onboarding. Invited a teammate. And here it is — on a different device, in a different browser, in the retention dashboard. Two real users, one shared database, one live URL. That's not a mockup. That's a product."

**Drop the URL in Slack:** "That URL is now in Slack. Anyone can open it. Your mom could open it. Your VP could open it. Try it — open it on your phone right now."

**Pause.** Let students click the URL. Let the room react.

**What you say:** "One click. Thirty seconds. Your onboarding flow is live on the internet. Anyone with this URL can open it, sign up, and use it. That's not a prototype. That's a product. Now it's your turn."

**Have students publish and test their own builds:** Click Publish, get the live URL, test in an incognito browser, open on their phone, post the URL in Slack, and open 2 classmates' URLs to try to break them.


## Slide 22 — Your Evolved Engineering Handoff

The slide shows a before/after comparison. Connect it to what they just experienced.

"Previously, in Module 4, your engineering handoff was a static technical inventory — a catalog of buttons and screens, notes on what's mocked versus real, and a 'Start Here' guide for an engineer. That was great. But it was a to-do list."

"Now, your handoff has evolved into a deployed system blueprint. You've finalized the real database structure and RLS rules. You've mapped how live data flows from the database to the UI. And most importantly, you have an edge case log — the specific results of your stress test, showing what's handled versus what's a known gap."

"This evolved handoff is arguably the most important artifact you've produced. It proves you've stress-tested the build and are proactively flagging known gaps so the engineering team isn't surprised by a crash later. High-fidelity UI is great, but high-fidelity *logic* is what actually ships."

"Your Living PRD from Module 4 says *what* the product does and *why*. Your new handoff note says *what's technically real*. Together, an engineer can inherit your project without reverse-engineering anything."


## Slide 23 — Future-Proofing Your Product with APIs

The slide shows three patterns for scaling beyond your database. Keep this forward-looking and aspirational — this is about where they go next, not what they need to build today.

"A product is only as real as its ability to handle live, dynamic data. Your next level of growth comes from moving beyond your internal database and plugging into the global API economy."

**Personalization** — "Use the User ID as a parameter in an API GET request to fetch a unique profile rather than a generic one. Think Spotify's 'Discover Weekly' — your ID tells the API to ignore the global top 40 and fetch *your* unique playlist data."

**Real-Time Utility** — "Replace static database rows with live API feeds that refresh dynamic, external data every few seconds. Think Uber's driver tracking — the app doesn't guess where the car is; it constantly calls a GPS API to update the coordinates on your screen."

**Continuity** — "Use PUT/POST requests to sync timestamps or state changes to a cloud API so it's accessible on any device. Think Netflix's 'Continue Watching' — your phone sends a timestamp API update so your TV can later fetch exactly where you left off."

"You don't need to write the integration — you can ask your AI for that. But you do need to define the data contract. You must know what parameters your app needs to send and what specific fields it needs back to render the experience. This is what turns your live product into a dynamic one that reacts to the world in real-time."


## Slide 24 — Module 5 Complete: What You Accomplished Today

The slide shows the summary stats. Don't just read them — connect each one to the transformation they experienced.

"Let's take stock. Think back to Module 1, when this was nothing more than a few sentences in a prompt. You have taken that raw strategic intent and transformed it into a 100% live production environment."

Tick through the wins conversationally:

"You executed a stress test audit — you identified P0 blockers and documented critical logic gaps to ensure a resilient launch. That's not hope-based shipping. That's evidence-based shipping."

"You finalized your static backend. You've moved past simple UI mockups and, by architecting your own database schema and security rules, you've built a persistent system that actually functions in the wild. Data survives a refresh. Users are real. RLS is active."

"And you deployed. You've moved past the limitations of a private environment and into a production-ready ecosystem — a resilient public product that handles real-world traffic and edge cases."

"You have turned your journey into a version-controlled, publicly-accessible, and fully-deployed product."

Land the project deliverable reminder: "Before you close out — update the 'Integrations & Data Model' and 'Edge Cases & Known Gaps' sections on Slide 9 of your final project deck. Ensure your Live URL is saved and your Handoff Note is exported. Do it today while it's fresh."


## Slide 25 — Key Takeaways

The slide shows four formal takeaways. Deliver them through a story they'll remember.

"Quick story. In 2015, Jason Citron launched Discord as a voice chat tool for gamers. Simple idea — hop into a channel with your squad, talk while you play. The first version was basically a voice channel with a text sidebar. Nothing fancy. But here's what made it work from day one: they got the data architecture right before they got the features right."

"Discord had to define a precise schema — servers, channels, users, roles, permissions. Every message was tied to a specific user in a specific channel on a specific server. The ownership rules were non-negotiable from the start. You can't have User A hearing User B's private conversation. You can't have a moderator's tools leaking to a regular member. Citron's team didn't just build a chat app — they defined the exact data contracts for who owns what, who sees what, and how every record in the database maps to a real human session. That's the first takeaway — **PMs orchestrate integrations by defining the schema, ownership rules, and data contracts.** You don't write the code. You define the blueprint. That's what you did today when you set up your tables and your RLS policies."

"Now here's where it gets interesting. Voice chat over the internet is brutally unforgiving. Connections drop mid-sentence. Latency spikes. Servers overload during a game launch. Discord had to engineer for every single failure mode. What happens when your connection drops mid-call? You see a 'Reconnecting...' indicator and it silently re-establishes the stream — not dead silence. What happens when a channel has zero members? It shows an empty state with an invite link — not a dead screen. What happens when 100,000 people flood a server for a Fortnite tournament? Rate limiting and pagination — not a browser crash. Every one of those is an edge case they anticipated and described. The second takeaway — **PMs must enforce technical resilience by accounting for empty, loading, and error states.** Anyone can build a voice channel. Shipping means the channel recovers when the internet drops, loads gracefully when the server is slammed, and guides new users when the room is empty."

"As Discord grew — from a small gaming tool to a platform used by study groups, crypto communities, art collectives, and corporate teams — their engineering documentation had to evolve with it. The early handoff was 'here's how voice works.' The mature handoff was a complete system blueprint — every WebSocket event, every rate limit, every error code, every reconnection sequence documented and stress-tested. And they stress-tested it with real chaos — game launches where millions of users would surge simultaneously. Each surge updated the blueprint. Each failure they caught became a documented edge case for the next engineer who inherited the system. The third takeaway — **the Engineering Handoff evolves from a static list to a system blueprint as real-world cases are stress-tested.** Your handoff note from today isn't a to-do list. It's a living record of what your system actually does under pressure."

"And here's the move that turned a gaming voice app into a platform valued at billions. Discord didn't stay locked inside its own database. They launched a bot API that let developers build anything on top of Discord — music bots, moderation bots, game integrations, custom commands. The bot ecosystem became so powerful that entire products were built *inside* Discord. Midjourney — the AI image generator — ran its entire user experience through Discord servers. No separate app, no separate website. Just Discord channels and API calls. Discord's utility scaled far beyond what their internal database could support because they opened the door to external integrations. The fourth takeaway — **PMs future-proof their products by identifying API connections that scale utility beyond the internal database.** Your database is the foundation. The API economy is what makes your product dynamic."

Pause. Then: "Four takeaways on screen. You already lived them. You defined the schema and the ownership rules. You engineered for resilience. You stress-tested and documented the system. And you identified where APIs can take your product next. That's the shift from prototype to production."


## Slide 26 — Extra Practice and Next Session

"Two optional exercises for anyone who wants to push further — both are on screen."

Frame them as challenges, not homework:

"The first one — The API Value Expansion. Select a static data point in your product and identify a public API that could provide it live. Use prompts to integrate the API and replace your stored data with a dynamic feed. The question to answer: does the shift to a live feed fundamentally evolve your product utility, or is the change merely cosmetic?"

"The second one — The Multi-Device Continuity Test. Open your live URL on both your laptop and your phone simultaneously. Perform an action on one device and refresh the other to see if the change is reflected instantly via your database. Does your infrastructure provide a seamless experience across devices, or does your product feel like a disconnected local session?"

Preview the next session: "Module 6 is where we transition from a finished product to a continuous cycle of improvement. You'll analyze live user interactions against your original hypothesis, leverage AI-driven analytics to identify high-impact friction points, and redeploy targeted updates that secure the confidence line of your product. If Module 5 made your product real, Module 6 makes it better."


## Slide 27 — Survey

At the end of each session, please scan the QR code or use the link to share your feedback. Your insights help us improve and make each cohort better than the last. We'd love to hear about your experience!


## Slide 28 — Bonus Resources

"All the links for today are on this slide — lab guide walkthrough, Integration Planner, everything. Bookmark the Integration Planner in particular — you'll keep referencing it as you refine your handoff and expand your integrations."


## Slide 29 — Q&A

Alright, before we close — any final questions? Anything about the database integration, authentication, edge cases, the stress test, deployment, or how this feeds into Module 6. Feel free to unmute or drop your question in the chat. And as always, share questions in Slack if something comes up later. See you next session!


## Slide 30 — End

Thank you, everyone. What you accomplished today is genuinely impressive — you went from a facade to a live, deployed product with a real database, real users, and real error handling. That's not a small thing. Go update your deliverables deck, share your live URLs, and try to break each other's products. See you in Module 6!
