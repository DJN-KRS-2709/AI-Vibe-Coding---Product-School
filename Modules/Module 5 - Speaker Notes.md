# Module 5: Ship Live Products with Full-Stack Logic — Speaker Notes

---

## Slide 1 — Title

Welcome to Module 5 — Ship Live Products with Full-Stack Logic.

It's been a journey so far. Module 1 was speed — you proved you can build. Module 2 was validation — you proved you can build the right thing and connected GitHub. Module 3 was precision — you orchestrated complex multi-screen systems. And Module 4 was structure and graduation — you cleaned the code, extracted the spec, and connected your backend.

But here's the truth nobody wants to hear: your infrastructure is connected, but your product isn't secured, and isn't resilient. Your database is live — but most of your UI still shows hardcoded values. Today, we close those gaps — and then we ship it live.


## Slide 2 — Class Expectations

Same ground rules. You know the drill by now.


## Slide 3 — Syllabus

Today is where you secure your build, engineer for failure, and deploy to a live URL.


## Slide 4 — Presentation Reminder

We're almost at the end! Next class is your opportunity to volunteer and present your final presentation. I highly recommend this because you get live, actionable feedback from the group. Please volunteer in Slack today — first come, first serve. Trust me, the people who present always walk away with the sharpest feedback.


## Slide 5 — Agenda

Four things today.

First — Moving from Connected Infrastructure to a Secured Product. We'll look at what your M4 prototype has versus what it still needs to survive real users.

Second — How to Secure and Extend Your Integration. The schema expansion, Row-Level Security, and edge case engineering.

Third — Hands-on lab: Expand Your Schema and Add RLS Authentication. You'll wire all your data to the database, add logins, and handle edge cases.

And finish with the second part of the Hands-on lab: Rapid-Fire Stress Test and Deploy Your Product Live.


## Slide 6 — From Connected Infrastructure to a Secured Product

This kicks off the first major section. Your M4 prototype has structure, documentation, clean code, and live infrastructure — GitHub, Lovable Cloud. But the product isn't fully built on top of it yet. Most data is still hardcoded, there's no user isolation, and nothing handles failure gracefully. Let's fix that.

**Pre-flight — re-run the Inheritance Test on your own repo.** Before you start layering RLS, schema changes, and edge case handling, take 90 seconds and point an agent at your repo (Cursor, Claude, ChatGPT with the markdown files attached — whatever you used in M4). Ask it: *"What's real vs. mocked, and where would you start if you had to ship a fix Friday?"* If the answer is fuzzy today, every change you make in M5 will compound that fog. Schema expansion on top of an unclear repo just creates a bigger unclear repo. Fix the doc gaps from your M4 Inheritance Test debrief before you write a single new prompt today.


## Slide 7 — Instructor-Led Demo: From Connected Infrastructure to Secured Product

Let's take a look at our M4 build. Clean code, Living PRD, GitHub repo since Module 2, Lovable Cloud connected. The infrastructure is real. But look at the product sitting on top of it. The Day-3 invite rate? Hardcoded at 38%. No matter what happens. Login users act the same. We see them in the backend stored. They all have the same experience.

**Prompt 1 — Wire All Data to the Database (~90 sec)**

Paste this prompt:

> "Extend the database schema. Create an 'invites' table to store team invites with the inviter's email, the invitee's email, and a timestamp. When a user completes the onboarding flow and invites a teammate, store the invite in this table. Replace the hardcoded Day-3 invite rate on the retention dashboard with a real calculation — query the invites table and compute the actual percentage. Replace all hardcoded metrics on the dashboard with real aggregations from the database. Track onboarding completion in the users table — store which screen the user reached and whether they completed all 3 steps."

When it's done: Go through the onboarding flow. Invite a teammate. Go to the retention dashboard — the Day-3 invite rate has updated from real data.

"The dashboard is now calculating real numbers from real data — not hardcoded values. That percentage isn't a placeholder anymore. It's a live calculation from the invites table."

Optional power move: Open the Lovable Cloud dashboard in a new tab. Show the data sitting in the invites table. "There's your data. In the database you connected in Module 4. You told the AI what to store and when — it wrote the integration."

**Prompt 2 — Auth UI + Row-Level Security (~90 sec)**

> "Add a login and signup screen before the onboarding flow using Lovable Cloud auth. New users sign up with email and password. After login, the app checks if this user has completed onboarding — if not, show the 3-screen onboarding flow. If yes, go straight to the retention dashboard. Add Row-Level Security so each user can only see and modify their own invites and onboarding data. The retention dashboard should show aggregate data across all users — total invites sent, Day-3 invite rate, retention comparison. Show the logged-in user's name in the header. Add a logout button."

"Auth is enabled from Module 4. But there's no login screen and no data isolation. Watch — this is where users become real."

When it's done: Log out. Sign up as a new user (e.g., "sarah@acme.com"). See the onboarding flow. Complete it, invite a teammate. Log out. Sign up as a different user (e.g., "mike@acme.com"). See a fresh onboarding flow — Mike's own experience, not Sarah's.

"Different user, different experience. I completed onboarding and invited a teammate. Just signed up with my new email — I see the onboarding flow fresh. I can't see previous data. That's Row-Level Security — the database enforces who sees what. The retention dashboard shows aggregate data from both. This isn't a prototype anymore — it's a multi-user product."

**Prompt 3 — Edge Cases (~60 sec)**

> "Handle these failure modes: If the database connection fails, show 'Connection error — please try again' instead of a blank screen. If a user tries to invite someone who's already been invited, show 'This teammate has already been invited — they'll get a notification' instead of creating a duplicate. If the invite submission fails, show 'Couldn't send invite — check your connection and try again' with a retry button. If no invites have been sent yet, the retention dashboard should show 'No invites tracked yet — data will appear as users complete onboarding' instead of empty charts. Add a loading skeleton while data is being fetched from the database."

Now Press ⌘ + Option + I (opens DevTools). Go to the "Network" tab. At the top, find "No throttling" dropdown. Select "Offline."

"I just killed the connection. Instead of silence, your user sees an error message with a retry option. That's the difference between connected infrastructure and a resilient product. Real products break — yours should break gracefully."

**Debrief:**

"Same prototype. Same onboarding flow. Same hypothesis. The infrastructure was already connected from Module 4. But now the product actually uses it:

- All data is real. Users are isolated. The retention dashboard shows real aggregations — computed from actual invite data across all users. And failures are handled — connection errors, empty states, loading skeletons, retry logic.

That's the line between having a backend and having a product. And I crossed it with 3 prompts only. You'll do this to your own build in the labs.


## Slide 8 — How to Secure and Extend Your Integration

Before you start building, let's talk about what's actually happening under the hood.


## Slide 9 — How to Prompt for Integration

You've got the infrastructure from Module 4. Now you're moving from 'database is connected' to 'product is built on the database.' That's a shift in how you communicate with the AI. You're no longer prompting for visual elements or one-off features. You're prompting for complete data flows, ownership rules, and failure handling. Let's walk through the three pillars:

**Define Your Schema Structure** — "Your database is live from Module 4, but most of your data is still hardcoded in the UI. You need to extend the schema to cover all the data your product displays. Be specific. 'Create a table for Invites with fields for sender_email, recipient_email, and a status timestamp. Replace the hardcoded dashboard metrics with real queries.' That precision is what makes the difference between a connected database and a database-driven product."

**Script Ownership Permissions** — "In a live environment, the most critical layer of logic is identity. A prototype is identity-blind — it treats every visitor the same. A real product must be identity-aware. You define the rules of ownership by implementing Row-Level Security. Think of it as the bouncer at the door: 'Ensure users can only see records where the user_id matches their authenticated session ID.' That's the line between a shared demo and a secure, multi-tenant platform."

**Orchestrate External APIs** — "This is how you add superpowers without writing the code. Payments through Stripe, emails through SendGrid, AI through OpenAI. Your job is to provide the API documentation and clearly define the trigger and the action."


## Slide 10 — Resistance Engineering for Errors & Failures

Most prototypes are designed for the happy path — the path where everything works perfectly. Real products handle the unhappy paths too. If you can describe these failure modes to the AI, it can build the safety nets.

**Empty States** — "Every user starts at zero. If that experience is a blank box with no instructions, the system has failed the user on day one. Replace blank screens with active empty states — a 'Get Started' CTA rather than a dead end."

**Loading States** — "In a live environment, data takes time to travel, and silence in the UI leads to churn. Don't just show a spinner — implement skeleton screens that show the structure of the data before it arrives."

**Error States** — "APIs and databases are external dependencies that will eventually fail. Every failed transaction must trigger an inline error with a 'Retry' button to keep the session alive. Shift from crashes to graceful recoveries."

**Load Bearing States** — "This is where vibe coding usually breaks. A prototype works with 5 rows of data, but a real product must remain stable with 50,000. If you don't tell the AI how to handle 50,000 items, it will try to load them all at once and crash the browser. Use pagination for large datasets and 'Last-Write-Wins' logic for simultaneous edits."


## Slide 11 — Add Data Schemas and RLS Authentication to Your Prototype

All right, let's kick off our first hands-on.


## Slide 12 — Individual Exercise: Generate Your Integration Plan and Build

Your infrastructure is live from Module 4. You're going to let the AI audit your prototype, create your game plan, and then execute it — all in one exercise. See the lab guide here: Vibe Coding M5: Lab Guide and Walkthrough.

Open Lovable with your prototype. Paste the prompt. It will scan your entire project and generate a personalized Integration Plan — a markdown file with your actual hardcoded values, your real tables, and three customized prompts. **Reminder: the quality of this plan mirrors the quality of your repo.** Lovable's agent is doing what your partner's agent did in the M4 Inheritance Test — it's reading your repo and inferring intent. A clear repo gets a precise plan. A vague repo gets a vague plan. Before you run those prompts, review the plan through three lenses.

First — audit your Data Status.

Second — define your User Status. Are the roles correct? Do different users need different permissions?

Third — map your Error and Data Handling Status. Which screens would freeze or go blank?

Once you've reviewed the plan, start executing it. Run the three prompts from your plan in order — each one builds on the last.

Prompt 1 — Schema expansion. This extends your database and wires your UI to real queries.

Prompt 2 — Auth and Row-Level Security. This adds a login/signup screen and partitions your data by user.

Prompt 3 — Edge cases. This adds loading skeletons, error messages, empty states, and retry logic.

When you're done, push all your changes and integration plan to GitHub. It lives in your repo alongside your Living PRD and engineering handoff.


## Slide 13 — Break

Quick 5-minute break. You've earned it — that was the hardest lab of the course. Grab some water, stretch, and we'll be right back.


## Slide 14 — Cameras On

Welcome back! Quick reminder — it's always better to see your smiling face. Be present and visible to stay engaged and keep interactions valuable.


## Slide 15 — Rapid-Fire Stress Test and Deploy Your Product Live

All right. We're in the final stage. You've built the backend. Now you stress-test it, and then you ship it live.


## Slide 16 — Chaos Round: Pick Your Stress Test

Who wants to run this with me?

"In a real product cycle, you never ship 'perfect' code — you ship code with known risks. If your stress test reveals a flaw, you have two choices: fix it now with one final prompt, or document it as a 'Known Issue' in your Handoff Note and deploy anyway. Both are valid PM moves. Ignoring the flaw is the only mistake."

So who wants to do this with me? All right, then let's do the following stress test: open your prototype and then do the network kill switch — for Mac it's ⌘ + Option + I (opens DevTools), go to the "Network" tab, at the top find "No throttling" dropdown, select "Offline." For PC it's Ctrl + Shift + I.

**The Kill Switch** — "Open DevTools, go to Network, and set to 'Offline.' Does your UI acknowledge the disconnection, or does it simply hang? If it hangs, that's a P0."

Okay. Successfully stress-tested now. Click 'Publish' in Lovable and generate your live URL.

"That URL is live. Right now. On the internet." Let me pull out my phone. Open the URL. "I just signed up on my phone. Went through onboarding. One click. Thirty seconds. Your onboarding flow is live on the internet. Anyone with this URL can open it, sign up, and use it. That's not a prototype. That's a product."


## Slide 17 — Your Evolved Engineering Handoff

"In Module 4, your engineering handoff was a technical inventory — a catalog of components, notes on what's mocked versus real, and a 'Start Here' guide for an engineer. The infrastructure was connected but the handoff documented what could be built."

"Now, your handoff has evolved into a deployed system blueprint. You've expanded the database schema and added Row-Level Security rules. You've mapped how live data flows from the database to the UI. And most importantly, you have an edge case log — the specific results of your stress test, showing what's handled versus what's a known gap."

"This evolved handoff is arguably the most important artifact for engineering you've produced. It proves you've stress-tested the build and are proactively flagging known gaps so the engineering team isn't surprised by a crash later. High-fidelity UI is great, but high-fidelity logic is what actually ships."

"Your Living PRD from Module 4 says what the product does and why. Your new handoff note says what's technically real. Together, an engineer can inherit your project without reverse-engineering anything."

**Push the evolved handoff back to the repo today, alongside your updated Living PRD and integration plan.** The Inheritance Test from M4 only holds if the repo stays current. If you ship the live URL but don't update `handoff.md` and `living-prd.md` with the new schema, RLS rules, and edge cases — an agent reading your repo next week will give your teammate a stale summary. Treat every M5 change as a repo update, not just a Lovable update. The repo is the spec. Keep it true.


## Slide 18 — Future-Proofing Your Product with APIs

And "A product is only as real as its ability to handle live, dynamic data. Your next level of growth comes from moving beyond your internal database and plugging into the global API economy." And you can do this the following ways.

**Personalization** — "Use the User ID as a parameter in an API GET request to fetch a unique profile rather than a generic one. Think Spotify's 'Discover Weekly' — your ID tells the API to ignore the global top 40 and fetch your unique playlist data."

**Continuity** — "Use PUT/POST requests to sync timestamps or state changes to a cloud API so it's accessible on any device. Think Netflix's 'Continue Watching' — your phone sends a timestamp API update so your TV can later fetch exactly where you left off."

**Real-Time Utility** — "Replace static database rows with live API feeds that refresh dynamic, external data every few seconds. Think Uber's driver tracking — the app doesn't guess where the car is; it constantly calls a GPS API to update the coordinates on your screen."

"You don't need to write the integration — you can ask your AI for that. But you do need to define the data contract. You must know what parameters your app needs to send and what specific fields it needs back. This is what turns your live product into a dynamic one that reacts to the world in real-time."


## Slide 19 — Module 5 Complete: What You Accomplished Today

Let's think back to Module 1, when this was nothing more than a few sentences in a prompt. You have taken that raw strategic intent and transformed it into a 100% live production environment.

You executed a stress test audit. And you have turned your Module 4 infrastructure into a version-controlled, publicly-accessible, and fully-deployed product.

Before you close out — update the 'Integrations & Data Model' and 'Edge Cases & Known Gaps' sections on Slide 9 of your final project deck. And of course, push everything to GitHub. Ensure your Live URL is saved and your Handoff Note is exported. Do it today while it's fresh.


## Slide 20 — Key Takeaways

Quick story. When Jason Citron launched Discord in 2015, it was just a voice channel with a text sidebar for gamers. Nothing fancy. But from day one, they got the data architecture right — servers, channels, users, roles, permissions. Every message tied to a specific user in a specific channel. You can't have User A hearing User B's private conversation. That's the first takeaway — **PMs orchestrate integrations by defining the schema, ownership rules, and data contracts.** You define the blueprint.

Voice chat over the internet is unforgiving. Connections drop. Servers overload during game launches. Discord engineered for all of it — a 'Reconnecting...' indicator instead of dead silence, empty states with invite links instead of blank screens, rate limiting instead of browser crashes. The second takeaway — **PMs must enforce technical resilience by accounting for empty, loading, and error states.** Anyone can build a voice channel. Shipping means it recovers when things break.

As Discord scaled, their docs evolved from 'here's how voice works' to a full system blueprint — every error code, every reconnection sequence stress-tested and documented. The third takeaway — **the Engineering Handoff evolves from a static list to a system blueprint.** Similar to your Living PRD.

And the move that turned it into a billion-dollar platform? They launched a bot API. Developers built entire products inside Discord — Midjourney ran its whole experience through Discord channels. That's the fourth takeaway — **PMs future-proof their products by identifying API connections that scale utility beyond the internal database.**

You did all of this today. That's the shift from prototype to production.


## Slide 21 — Extra Practice and Next Session

Two optional exercises for anyone who wants to push further.

The first one — The API Value Expansion. Select a static data point in your product and identify a public API that could provide it live. Use prompts to integrate the API and replace your stored data with a dynamic feed. The question to answer: does the shift to a live feed fundamentally evolve your product utility, or is the change merely cosmetic?

The second — The Multi-Device Continuity Test. Open your live URL on both your laptop and your phone simultaneously. Perform an action on one device and refresh the other to see if the change is reflected instantly via your database. Does your infrastructure provide a seamless experience across devices, or does your product feel like a disconnected local session?

Module 6 is where we transition from a finished product to a continuous cycle of improvement. You'll analyze live user interactions against your original hypothesis, leverage AI-driven analytics to identify high-impact friction points, and redeploy targeted updates that secure the confidence line of your product. If Module 5 made your product real, Module 6 makes it better.


## Slide 22 — Survey

I really want to pause here and encourage you to use this link or scan this QR to send feedback. It takes you one or two minutes max but helps us tremendously to improve. Thank you.


## Slide 23 — Bonus Resources

You can see the lab guide and all additional resources on this slide.


## Slide 24 — Q&A

Alright, before we close — let's run another demo. Any final questions? Anything about the database integration, authentication, edge cases, the stress test, deployment, or how this feeds into Module 6. Feel free to unmute or drop your question in the chat. And as always, share questions in Slack if something comes up later. See you next session!


## Slide 25 — End

Thank you, everyone. What you accomplished today is genuinely impressive — you went from a facade to a live, deployed product with a real database, real users, and real error handling. That's not a small thing. Go update your deliverables deck, share your live URLs, and try to break each other's products. See you in Module 6!
