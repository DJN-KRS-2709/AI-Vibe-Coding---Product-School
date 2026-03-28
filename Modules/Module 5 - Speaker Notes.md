# Module 5: Ship Live Products with Full-Stack Logic — Speaker Notes

Casual talking points for each slide. Not a script — just the key things to say and the energy to bring. Module 5 is the emotional peak of the course — this is where connected infrastructure becomes a secured, deployed product. The wow moments are when hardcoded dashboard data updates from real queries and when different users see different data via Row-Level Security.

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

But here's the truth nobody wants to hear: your infrastructure is connected, but your product isn't secured, isn't resilient, and isn't accessible. Your database is live — but most of your UI still shows hardcoded values. Auth is enabled — but there's no login screen and no data isolation. And if the connection drops mid-action? Silence. Today, we close those gaps — and then we ship it live.


## Slide 2 — Class Expectations

Same ground rules. Cameras on — it genuinely makes a difference when we can see each other. Be present, arrive on time, participate actively during exercises. Use Slack for all communication. Individual or deep-dive questions will be moved to after-class support to keep the flow going.

Critical for today: all your tools and accounts must be active *before* class. We will not stop or restart for setup. That means Lovable, Supabase, and GitHub should all be ready. If something's broken, fix it during the break or pair up with someone who has it working.


## Slide 3 — Syllabus

Quick refresher on where we are. Six modules across three weeks.

Module 1 was speed — you built at lightspeed and proved you could go from nothing to a working prototype. Module 2 was validation — you injected data and hypotheses to ensure you're solving the right problem. Module 3 was precision — you used prompt chaining to maintain consistency as complexity scaled. Module 4 was structure — you converted your build into version-controlled code with a Living PRD and engineering handoff.

Module 5 — that's today — is where you secure your build with user isolation, engineer for failure, and deploy to a live URL. You'll expand your database schema, add Row-Level Security so each user only sees their own data, handle edge cases, stress-test the system, and ship it to the internet.

Module 6 closes the loop — you measure product performance, use AI-driven analytics, and iterate based on real-world evidence.


## Slide 4 — Presentation Reminder

We're almost at the end! Next class is your opportunity to volunteer and present your final presentation. We highly recommend this because you get live, actionable feedback from the group. I'll ask for five to six volunteers in Slack today — first come, first serve. Trust me, the people who present always walk away with the sharpest feedback and the most polished final deliverable.


## Slide 5 — Agenda

Four things today.

First — Moving from Connected Infrastructure to a Secured Product. We'll look at what your M4 prototype has versus what it still needs to survive real users.

Second — How to Secure and Extend Your Integration. The schema expansion, Row-Level Security, and edge case engineering that turn connected infrastructure into a resilient product.

Third — Hands-on lab: Expand your schema and add auth with Row-Level Security. You'll wire all your data to the database, add login with per-user isolation, and handle edge cases — the same three steps I'll demo for you first.

Fourth — Hands-on lab: Rapid-fire stress test and deploy your product live. You'll chaos-test your build and then hit the publish button. By the end of today, your product will be live on the internet.


## Slide 6 — Moving from Connected Infrastructure to a Secured Product

This kicks off the first major section. Your M4 prototype has structure, documentation, clean code, and live infrastructure — GitHub, Supabase, Lovable Cloud. But the product isn't fully built on top of it yet. Most data is still hardcoded, there's no user isolation, and nothing handles failure gracefully. Let's fix that.


## Slide 7 — Reflection Moment: What's Still Missing?

Give students 5 minutes. Let them think before discussing.

Open up your prototype from Module 4 and think about this:

"Your database is connected. Your code is clean. Your infrastructure is live. Now imagine I send your prototype's URL to 50 strangers right now. They all open it, sign up, enter their data, and start using it. What would they actually experience? Can User 14 see User 37's private data? What happens when someone's internet drops mid-submit? What happens when a brand new user signs up and has zero data? And — can those 50 people even *reach* your product right now?"

And a harder question: "What would happen if two different people tried to edit the exact same piece of information at the same time?"

Feel free to unmute and share, or post your thoughts in the chat.

Keep this to quick answers from 2-3 volunteers. After they share:

"Your infrastructure is real — you built that in Module 4. But having a database and having a *secure, resilient product* are two different things. Right now, most of the data your UI shows is still hardcoded — the dashboard metrics, the counts. There's no login screen, so there's no way to tell users apart. If data is in the database, everyone sees everything — there's no Row-Level Security separating User 14 from User 37. And when the connection drops or a new user has zero data? Nothing handles that gracefully. Plus, your product only works inside Lovable — nobody outside this room can touch it. Today we close those gaps: data completeness, user isolation, failure handling, and shipping it live."


## Slide 8 — Instructor-Led Demo: From Connected Infrastructure to Secured Product

Demo time — ~10 minutes total. Using the Retention Engine prototype carried from M2/M3/M4 demos.

Here's where we are. Your M4 prototype has a GitHub repo, clean code, a Living PRD, and a live Supabase backend. The infrastructure is real. But watch what happens when I stress it.

**Show the gap first.** Pull up the prototype. Click through all the screens — the 3-screen onboarding flow, the retention dashboard, the experiment summary. Remind them how polished it is from M4.

Then demonstrate the gap. Go to the retention dashboard — the Day-3 invite rate says 12%. Go through the onboarding flow, invite a teammate, go back to the dashboard — it still says 12%. That number is hardcoded. Try to be a different user — there's no login screen. Open Chrome DevTools, go to Network, check Offline. The app freezes — no error message, no recovery.

"This is our M4 build. Clean code, Living PRD, GitHub repo, Lovable Cloud connected. The infrastructure is real. But the Day-3 invite rate? Hardcoded at 12% no matter what happens. There's no login screen — every visitor is the same anonymous person. And when I kill the connection? Silence. The foundation is there. The product isn't fully built on it yet."

"Three prompts. Watch what changes."

**Prompt 1 — Wire all data to the database.** Paste:

> "Extend the database schema. Create an 'invites' table to store team invites with the inviter's email, the invitee's email, and a timestamp. When a user completes the onboarding flow and invites a teammate, store the invite in this table. Replace the hardcoded Day-3 invite rate on the retention dashboard with a real calculation — query the invites table and compute the actual percentage. Replace all hardcoded metrics on the dashboard with real aggregations from the database. Track onboarding completion in the users table — store which screen the user reached and whether they completed all 3 steps."

Let the class watch it generate. When it's done, go through the onboarding flow, invite a teammate, go to the retention dashboard — the rate has updated from real data.

"The dashboard is now calculating real numbers from real data — not hardcoded values. That 12% isn't a placeholder anymore. It's a live calculation from the invites table."

**Prompt 2 — Auth + Row-Level Security.** Paste:

> "Add a login and signup screen before the onboarding flow using Lovable Cloud auth. New users sign up with email and password. After login, the app checks if this user has completed onboarding — if not, show the 3-screen onboarding flow. If yes, go straight to the retention dashboard. Add Row-Level Security so each user can only see and modify their own invites and onboarding data. The retention dashboard should show aggregate data across all users — total invites sent, Day-3 invite rate, retention comparison. Show the logged-in user's name in the header. Add a logout button."

While it generates: "Auth is enabled from Module 4. But there's no login screen and no data isolation. Watch — this is where users become real."

When it's done, log out. Sign up as "sarah@acme.com." Complete onboarding, invite a teammate. Log out. Sign up as "mike@acme.com." See a fresh onboarding flow — Mike's own experience, not Sarah's.

"Different user, different experience. Sarah completed onboarding and invited a teammate. Mike just signed up — he sees the onboarding flow fresh. Sarah can't see Mike's data. Mike can't see Sarah's. That's Row-Level Security — the database enforces who sees what. The retention dashboard shows aggregate data from both. This isn't a prototype anymore — it's a multi-user product."

**Prompt 3 — Edge cases.** Paste:

> "Handle these failure modes: If the database connection fails, show 'Connection error — please try again' instead of a blank screen. If a user tries to invite someone who's already been invited, show 'This teammate has already been invited — they'll get a notification' instead of creating a duplicate. If the invite submission fails, show 'Couldn't send invite — check your connection and try again' with a retry button. If no invites have been sent yet, the retention dashboard should show 'No invites tracked yet — data will appear as users complete onboarding' instead of empty charts. Add a loading skeleton while data is being fetched from the database."

When it's done, open DevTools, go to Network, check Offline. Show the error message instead of a blank screen. Uncheck Offline — it recovers. Try inviting the same email twice — see the duplicate message.

"I just killed the connection. Instead of silence, your user sees an error message with a retry option. I tried inviting the same person twice — it caught the duplicate. That's the difference between connected infrastructure and a resilient product. Real products break — yours should break gracefully."

**Debrief:**

"Same prototype. Same onboarding flow. Same hypothesis — surfacing team invites to reduce churn. The infrastructure was already connected from Module 4. But now the product actually *uses* it:

- All data is real — the dashboard metrics are calculated from the database, not hardcoded.
- Users are isolated — login, signup, Row-Level Security. Sarah's data is Sarah's. Mike's data is Mike's.
- The retention dashboard shows real aggregations — computed from actual invite data.
- Failures are handled — connection errors, duplicate invites, empty states, loading skeletons.

Before: connected infrastructure with hardcoded data on top.
After: a secured, resilient product built on that infrastructure.

That's the line between having a backend and having a product. And you crossed it with 3 prompts.

You'll do this to your own build in the labs. But first — let me show you what's actually happening under the hood so you know exactly what to ask for."


## Slide 9 — How to Secure and Extend Your Integration

"Before you start building, let's talk about what's actually happening under the hood — the three integration patterns, how to engineer for failure, and the security basics that keep your product safe."


## Slide 10 — How to Prompt for Integration

"You've got the infrastructure from Module 4. Now you're moving from 'database is connected' to 'product is built on the database.' That's a shift in how you communicate with the AI. You're no longer prompting for visual elements or one-off features. You're prompting for complete data flows, ownership rules, and failure handling."

Walk through the three pillars:

**Define Your Schema Structure** — "Your database is live from Module 4, but most of your data is still hardcoded in the UI. You need to extend the schema to cover *all* the data your product displays. Be specific. 'Create a table for Invites with fields for sender_email, recipient_email, and a status timestamp. Replace the hardcoded dashboard metrics with real queries.' That precision is what makes the difference between a connected database and a database-driven product."

**Script Ownership Permissions** — "In a live environment, the most critical layer of logic is identity. A prototype is identity-blind — it treats every visitor the same. A real product must be identity-aware. You define the rules of ownership by implementing Row-Level Security. Think of it as the bouncer at the door: 'Ensure users can only see records where the user_id matches their authenticated session ID.' That's the line between a shared demo and a secure, multi-tenant platform."

**Orchestrate External APIs** — "This is how you add superpowers without writing the code. Payments through Stripe, emails through SendGrid, AI through OpenAI. Your job is to provide the API documentation and clearly define the trigger and the action. 'Connect the Stripe API. Trigger a checkout session when Upgrade is clicked and return to the dashboard on success.' You describe the contract — the AI builds the bridge."


## Slide 11 — Resistance Engineering for Errors & Failures

"Most prototypes are designed for the happy path — the path where everything works perfectly. Real products handle the unhappy paths too. If you can describe these failure modes to the AI, it can build the safety nets."

**Empty States** — "Every user starts at zero. If that experience is a blank box with no instructions, the system has failed the user on day one. Replace blank screens with active empty states — a 'Get Started' CTA rather than a dead end."

**Loading States** — "In a live environment, data takes time to travel, and silence in the UI leads to abandonment. Don't just show a spinner — implement skeleton screens that show the structure of the data before it arrives."

**Error States** — "APIs and databases are external dependencies that *will* eventually fail. Every failed transaction must trigger an inline error with a 'Retry' button to keep the session alive. Shift from crashes to graceful recoveries."

**Load Bearing States** — "This is where vibe coding usually breaks. A prototype works with 5 rows of data, but a real product must remain stable with 5,000. If you don't tell the AI how to handle 10,000 items, it will try to load them all at once and crash the browser. Use pagination for large datasets and 'Last-Write-Wins' logic for simultaneous edits."

"Building for the happy path is easy, but it's not shipping. Real products are defined by how they handle the 10% of the time that things go wrong."


## Slide 12 — Security Best Practices

"You're a PM, not a security engineer. But it's good to know the basics. Most tools handle this for you automatically. Your job is to not work against it."

Do column: "Use Row-Level Security — without it, your database is a free-for-all. Use environment variables — keep API keys in 'Secrets' and out of your frontend code. Trust the infrastructure — Supabase handles password hashing and HTTPS for you. And if the UI looks right but the data is missing, check the API connection before re-prompting."

Don't column: "Never leave a database open because 'it's just a prototype.' If it has data, it needs a login. Never paste raw API keys into a prompt or file. Don't collect real SSNs or credit card numbers you don't need to test. And never assume form data is valid — always validate server-side."


## Slide 13 — Individual Exercise: Generate Your Integration Plan and Build

45 minutes. Breakout rooms for co-working. Drop the Integration Plan Prompt in Slack.

"Your infrastructure is live from Module 4. You're going to let the AI audit your prototype, create your game plan, and then execute it — all in one exercise. I just dropped a prompt in Slack."

"Open Lovable with your prototype. Paste the prompt. It will scan your entire project and generate a personalized Integration Plan — a markdown file with your actual hardcoded values, your real tables, and three customized prompts. Before you run those prompts, review the plan through three lenses."

"First — audit your Data Status. Did it catch all the hardcoded elements still in your UI? Dashboard metrics, counts, user info — anything that's a placeholder instead of a real query."

"Second — define your User Status. Are the roles correct? Do different users need different permissions? Make sure the Row-Level Security rules make sense."

"Third — map your Error and Data Handling Status. Which screens would freeze or go blank if the connection dropped?"

"Once you've reviewed the plan, start executing it. Run the three prompts from your plan in order — each one builds on the last."

"Prompt 1 — Schema expansion. This extends your database and wires your UI to real queries. Once it runs, check: are your dashboard metrics now pulling from the database instead of showing hardcoded numbers? Change some data and see the numbers update."

"Prompt 2 — Auth and Row-Level Security. This adds a login/signup screen and partitions your data by user. Test it: create two separate accounts. Log in as User A, do something, log out. Log in as User B. Can User B see User A's data? If yes, your Row-Level Security needs work. If no, you're good."

"Prompt 3 — Edge cases. This adds loading skeletons, error messages, empty states, and retry logic. Pick at least two failure modes to verify after it runs."

"Two checkpoints before you stop: dashboard data is computed from real queries, not hardcoded — and different accounts see different data."

"When you're done, push your Integration Plan to GitHub. It lives in your repo alongside your Living PRD."


## Slide 14 — Break

Quick 5-minute break. You've earned it — that was the hardest lab of the course. Grab some water, stretch, and we'll be right back.


## Slide 15 — Cameras On

Welcome back! Quick reminder — it's always better to see your smiling face. Be present and visible to stay engaged and keep interactions valuable.


## Slide 16 — Reflection Moment: Post-Lab Q&A

Give students 5 minutes. Let 2-3 volunteers share.

"Now that you've connected a live backend, what surprised you most? Was the biggest challenge building the functional logic, or anticipating all the ways it could fail?"

And a follow-up: "What would happen if a user with a slow connection tried to submit a form three times because they didn't see a loading state?"

Most students will find that getting the database to work was fast, but realizing how many ways a user can break it is the real eye-opener. "That's exactly right. The complexity in product management often comes from these invisible edge cases, not the visible features."

"Anyone can prompt a pretty UI. A Product Manager's value lies in orchestrating the logic that makes that UI resilient — and you've successfully done that today."


## Slide 17 — Rapid-Fire Stress Test and Deploy Your Product Live

"We're in the final stretch. You've built the backend. Now you stress-test it, and then you ship it live."


## Slide 18 — Chaos Round: Pick Your Stress Test

Keep everyone in the main room. 15 minutes total. Suggest one volunteer to share their screen.

"In a real product cycle, you never ship 'perfect' code — you ship code with known risks. If your stress test reveals a flaw, you have two choices: fix it now with one final prompt, or document it as a 'Known Issue' in your Handoff Note and deploy anyway. Both are valid PM moves. Ignoring the flaw is the only mistake."

Walk through the three stress tests:

**The Kill Switch** — "Open DevTools, go to Network, and set to 'Offline.' Does your UI acknowledge the disconnection, or does it simply hang? If it hangs, that's a P0."

**The Ghost User** — "Sign up with a brand new email. Does the user see an active empty state with a CTA, or a blank screen? Every real user starts at zero."

**The Spam Click** — "Hit your 'submit' button 5 times rapidly. Does your database create 5 duplicate records, or is the transaction handled correctly?"

"Choose one. You don't need to do all three — but you can if you want. Run the test, observe the result, and make a Go/No-Go decision."

After the stress test: "If it passes, you're ready to deploy. Click 'Publish' in Lovable and generate your live URL. If it fails and it's a P0 blocker, run one final prompt to fix it. If it's a known gap you can live with, document it in your handoff and then publish."

**The deploy moment — this is the climax of the module.**

"Alright. You've all just built real backends — databases, auth, error handling. Your apps work. But right now, they only work inside Lovable. Nobody else on the planet can use what you built. Let's fix that."

In Lovable, click Share → Publish. Takes about 20-30 seconds.

"One button. That's it. No CI/CD pipeline, no server configuration, no DNS records, no Dockerfile. One click."

When the URL appears, copy it, paste it in the browser. The app loads with the login screen.

"That URL is live. Right now. On the internet."

Pull out your phone. Open the URL. Sign up as a brand new user. Complete onboarding. Go back to your laptop — log in as a different account. Show the data from the phone appearing in the dashboard.

"I just signed up on my phone. Went through onboarding. Invited a teammate. And here it is — on a different device, in a different browser, in the retention dashboard. Two real users, one shared database, one live URL. That's not a mockup. That's a product."

Drop the URL in Slack. "That URL is now in Slack. Anyone can open it. Your mom could open it. Your VP could open it. Try it — open it on your phone right now."

Pause. Let the room react.

"One click. Thirty seconds. Your onboarding flow is live on the internet. Anyone with this URL can open it, sign up, and use it. That's not a prototype. That's a product. Now it's your turn."

Have students publish their own builds, test in incognito, open on their phone, post their URL in Slack, and open 2 classmates' URLs to try to break them.


## Slide 19 — Your Evolved Engineering Handoff

"In Module 4, your engineering handoff was a technical inventory — a catalog of components, notes on what's mocked versus real, and a 'Start Here' guide for an engineer. The infrastructure was connected but the handoff documented what *could* be built."

"Now, your handoff has evolved into a deployed system blueprint. You've expanded the database schema and added Row-Level Security rules. You've mapped how live data flows from the database to the UI. And most importantly, you have an edge case log — the specific results of your stress test, showing what's handled versus what's a known gap."

"This evolved handoff is arguably the most important artifact you've produced. It proves you've stress-tested the build and are proactively flagging known gaps so the engineering team isn't surprised by a crash later. High-fidelity UI is great, but high-fidelity *logic* is what actually ships."

"Your Living PRD from Module 4 says *what* the product does and *why*. Your new handoff note says *what's technically real*. Together, an engineer can inherit your project without reverse-engineering anything."


## Slide 20 — Future-Proofing Your Product with APIs

"A product is only as real as its ability to handle live, dynamic data. Your next level of growth comes from moving beyond your internal database and plugging into the global API economy."

**Personalization** — "Use the User ID as a parameter in an API GET request to fetch a unique profile rather than a generic one. Think Spotify's 'Discover Weekly' — your ID tells the API to ignore the global top 40 and fetch *your* unique playlist data."

**Real-Time Utility** — "Replace static database rows with live API feeds that refresh dynamic, external data every few seconds. Think Uber's driver tracking — the app doesn't guess where the car is; it constantly calls a GPS API to update the coordinates on your screen."

**Continuity** — "Use PUT/POST requests to sync timestamps or state changes to a cloud API so it's accessible on any device. Think Netflix's 'Continue Watching' — your phone sends a timestamp API update so your TV can later fetch exactly where you left off."

"You don't need to write the integration — you can ask your AI for that. But you do need to define the data contract. You must know what parameters your app needs to send and what specific fields it needs back. This is what turns your live product into a dynamic one that reacts to the world in real-time."


## Slide 21 — Module 5 Complete: What You Accomplished Today

"Let's take stock. Think back to Module 1, when this was nothing more than a few sentences in a prompt. You have taken that raw strategic intent and transformed it into a 100% live production environment."

"You executed a stress test audit — you identified P0 blockers and documented critical logic gaps to ensure a resilient launch. That's not hope-based shipping. That's evidence-based shipping."

"You secured your backend. Module 4 connected the infrastructure — today you made your product actually use it. Every metric is computed from real data. Every user is isolated with Row-Level Security. The database doesn't just exist — it drives every screen."

"You engineered for failure. Empty states, loading skeletons, connection errors, duplicate prevention — your product breaks gracefully instead of silently."

"And you deployed. You've moved past the limitations of a private environment and into a production-ready ecosystem — a resilient public product that handles real-world traffic and edge cases."

"You have turned your Module 4 infrastructure into a version-controlled, publicly-accessible, and fully-deployed product."

"Before you close out — update the 'Integrations & Data Model' and 'Edge Cases & Known Gaps' sections on Slide 9 of your final project deck. Ensure your Live URL is saved and your Handoff Note is exported. Do it today while it's fresh."


## Slide 22 — Key Takeaways

"Quick story. When Jason Citron launched Discord in 2015, it was just a voice channel with a text sidebar for gamers. Nothing fancy. But from day one, they got the data architecture right — servers, channels, users, roles, permissions. Every message tied to a specific user in a specific channel. You can't have User A hearing User B's private conversation. That's the first takeaway — **PMs orchestrate integrations by defining the schema, ownership rules, and data contracts.** You define the blueprint. That's what you did today."

"Voice chat over the internet is unforgiving. Connections drop. Servers overload during game launches. Discord engineered for all of it — a 'Reconnecting...' indicator instead of dead silence, empty states with invite links instead of blank screens, rate limiting instead of browser crashes. The second takeaway — **PMs must enforce technical resilience by accounting for empty, loading, and error states.** Anyone can build a voice channel. Shipping means it recovers when things break."

"As Discord scaled, their docs evolved from 'here's how voice works' to a full system blueprint — every error code, every reconnection sequence stress-tested and documented. The third takeaway — **the Engineering Handoff evolves from a static list to a system blueprint as real-world cases are stress-tested.**"

"And the move that turned it into a billion-dollar platform? They launched a bot API. Developers built entire products *inside* Discord — Midjourney ran its whole experience through Discord channels. The fourth takeaway — **PMs future-proof their products by identifying API connections that scale utility beyond the internal database.**"

"Four takeaways on screen. You already lived them today. That's the shift from prototype to production."


## Slide 23 — Extra Practice and Next Session

"Two optional exercises for anyone who wants to push further — both are on screen."

"The first one — The API Value Expansion. Select a static data point in your product and identify a public API that could provide it live. Use prompts to integrate the API and replace your stored data with a dynamic feed. The question to answer: does the shift to a live feed fundamentally evolve your product utility, or is the change merely cosmetic?"

"The second one — The Multi-Device Continuity Test. Open your live URL on both your laptop and your phone simultaneously. Perform an action on one device and refresh the other to see if the change is reflected instantly via your database. Does your infrastructure provide a seamless experience across devices, or does your product feel like a disconnected local session?"

"Module 6 is where we transition from a finished product to a continuous cycle of improvement. You'll analyze live user interactions against your original hypothesis, leverage AI-driven analytics to identify high-impact friction points, and redeploy targeted updates that secure the confidence line of your product. If Module 5 made your product real, Module 6 makes it better."


## Slide 24 — Survey

At the end of each session, please scan the QR code or use the link to share your feedback. Your insights help us improve and make each cohort better than the last. We'd love to hear about your experience!


## Slide 25 — Bonus Resources

"All the links for today are on this slide — lab guide walkthrough, Integration Plan Prompt, everything. Bookmark the prompt in particular — if you ever want to regenerate your plan after making changes, just paste it again and Lovable will re-scan your project. The Integration Plan markdown lives in your repo alongside your Living PRD."


## Slide 26 — Q&A

Alright, before we close — any final questions? Anything about the database integration, authentication, edge cases, the stress test, deployment, or how this feeds into Module 6. Feel free to unmute or drop your question in the chat. And as always, share questions in Slack if something comes up later. See you next session!


## Slide 27 — End

Thank you, everyone. What you accomplished today is genuinely impressive — you went from a facade to a live, deployed product with a real database, real users, and real error handling. That's not a small thing. Go update your deliverables deck, share your live URLs, and try to break each other's products. See you in Module 6!
