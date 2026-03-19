# Module 5 — Instructor Demo: Step-by-Step

> For the instructor only. Run this as a live demo on screen share.
> Total time: ~10 minutes. Pre-type all 3 prompts before class.
> Instructor demo: **The Customer Vibe — Retention Engine** (B2B PM SaaS — 30% churn, team invites — carried from M2/M3/M4 demos)

---

## SETUP (before students arrive)

- [ ] Open the M4 prototype in Lovable (same one carried from M2/M3/M4 demos — now with clean code, Living PRD, GitHub connected, Lovable Cloud enabled)
- [ ] Have all 3 prompts pre-typed in a text file, ready to paste
- [ ] Lovable Cloud is already enabled from M4 — verify the project has Cloud connected
- [ ] Screen share on — students should see everything
- [ ] Have your phone ready for the deploy moment later in the session (Slide 17)

---

## STEP 1: Show the Facade (2 min)

**What you do:** Click through the M4 prototype — all screens. Show the 3-screen onboarding flow, the retention dashboard, the experiment summary. Remind students how polished and structured it is. Then demonstrate the facade.

**What you do:** Go through the onboarding flow, "invite" a teammate, refresh the page. The invite is gone. Go to the retention dashboard — the metrics never change. Try to "log in" — there's no real login.

**What you say:** "This is the M4 build. Clean code, Living PRD, GitHub repo, Lovable Cloud connected. An engineer could inherit this. But watch — I go through the onboarding flow, invite a teammate, refresh, and the invite is gone. The retention metrics? Hardcoded. The Day-3 invite rate? Still says 12% no matter what happens. There's no login, no real users. It looks like a product. It's still a facade."

**What you say:** "Three prompts. Watch what changes."

---

## STEP 2: Prompt 1 — Database (~90 sec)

**Paste this prompt:**

> "Add a real database to this project using Lovable Cloud. Create a 'users' table and an 'invites' table. When a user completes the onboarding flow and invites a teammate, store the invite in the invites table with the inviter's email, the invitee's email, and the timestamp. When the retention dashboard loads, query the invites table to calculate the real Day-3 invite rate and display the actual number instead of the hardcoded 12%. Track onboarding completion in the users table — store which screen the user reached and whether they completed all 3 steps."

**While it generates:** Stay quiet. Let the class watch.

**When it's done:** Go through the onboarding flow. Invite a teammate. Refresh the page. The invite is still there. Go to the retention dashboard — the Day-3 invite rate has updated.

**What you say:** "The invite persists. Close the tab. Reopen it. Still there. The retention dashboard is now calculating real numbers from real data — not hardcoded values. That data is sitting in a real PostgreSQL database."

**Optional power move:** Open the Lovable Cloud dashboard in a new tab. Show the data sitting in the invites table. "There's your data. In a real database. You described what to store and when — the AI wrote the integration."

**Let the moment land. This is Beat 1.**

---

## STEP 3: Prompt 2 — Authentication (~90 sec)

**Paste this prompt:**

> "Add authentication to this project using Lovable Cloud auth. Add a login/signup screen before the onboarding flow. New users sign up with email and password. After login, the app checks if this user has completed onboarding — if not, show the 3-screen onboarding flow. If yes, go straight to the retention dashboard. Track invites per user. The retention dashboard should show aggregate data across all users — total invites sent, Day-3 invite rate, retention comparison. Show the logged-in user's name in the header. Add a logout button."

**While it generates:** "Watch — this is where it gets real."

**When it's done:** Log out. Sign up as a new user (e.g., "sarah@acme.com"). See the onboarding flow. Complete it, invite a teammate. Log out. Sign up as a different user (e.g., "mike@acme.com"). See a fresh onboarding flow — Mike's own experience, not Sarah's.

**What you say:** "Different user, different experience. Sarah completed onboarding and invited a teammate. Mike just signed up — he sees the onboarding flow fresh. The retention dashboard shows data from both. This isn't a prototype anymore — it's a multi-user product."

**Let the moment land. This is Beat 2.**

---

## STEP 4: Prompt 3 — Edge Cases (~60 sec)

**Paste this prompt:**

> "Handle these failure modes: If the database connection fails, show 'Connection error — please try again' instead of a blank screen. If a user tries to invite someone who's already been invited, show 'This teammate has already been invited — they'll get a notification' instead of creating a duplicate. If the invite submission fails, show 'Couldn't send invite — check your connection and try again' with a retry button. If no invites have been sent yet, the retention dashboard should show 'No invites tracked yet — data will appear as users complete onboarding' instead of empty charts. Add a loading skeleton while data is being fetched from the database."

**When it's done:** Open Chrome DevTools (F12 → Network → check Offline). Show the error message instead of a blank screen. Uncheck Offline — it recovers. Try inviting the same email twice — see the duplicate message.

**What you say:** "I just killed the connection. Instead of a blank screen, your user sees an error message with a retry option. I tried inviting the same person twice — it caught the duplicate. That's the difference between a prototype and a product. Real products break — yours should break gracefully."

---

## STEP 5: Debrief (2 min)

**What you say:**

"Same prototype. Same onboarding flow. Same hypothesis — surfacing team invites to reduce churn. But now:

- Data persists — invites are stored in a real database. Refresh, close, reopen — still there.
- Users are real — login, signup, personalized onboarding state. New users see the flow, returning users skip to the dashboard.
- The retention dashboard shows real numbers — calculated from actual invite data, not hardcoded.
- Failures are handled — connection errors, duplicate invites, empty states, loading skeletons, retry logic.

Before: a visual facade with hardcoded data.
After: a working product with a real backend.

That's the line between prototype and product. And you crossed it with 3 prompts.

You'll do this to your own build in 30 minutes. But first — let me show you what's actually happening under the hood."

**Transition to Teaching (Slide 6).**

---

## LATER IN SESSION: Deploy Demo (Slide 17, ~3 min)

> This happens AFTER the lab, chaos round, and five-tab reveal — as the session climax.

### STEP 6: Set Up the Moment (~30 sec)

**What you do:** Bring the class back to your screen share. Have the Lovable editor open with the onboarding flow — the same project with database, auth, and edge cases already working from earlier.

**What you say:** "Alright. You've all just built real backends — databases, auth, error handling. Your apps work. But right now, they only work inside Lovable. Nobody else on the planet can use what you built. Let's fix that."

### STEP 7: Click Publish (~60 sec)

**What you do:** In Lovable, click the **Share** button (top-right) → then click **Publish**. Lovable will build and deploy the app. A progress indicator appears briefly — takes about 20-30 seconds.

**While it deploys:** "One button. That's it. No CI/CD pipeline, no server configuration, no DNS records, no Dockerfile. One click."

**When the URL appears:** Copy the live URL. Paste it into the browser address bar on your laptop. The app loads — with the login screen.

**What you say:** "That URL is live. Right now. On the internet."

### STEP 8: Prove It's Real (~60 sec)

**What you do — phone:** Pull out your phone. Open the URL in your phone's browser. Hold the phone up so the class can see. Show the login screen loading on your phone.

**What you do — sign up:** On your phone, sign up as a brand new user (e.g., "demo@live.com"). See the onboarding flow. Complete it. Invite a teammate.

**What you do — laptop:** Go back to your laptop. Log in as a different account. Go to the retention dashboard. Show the invite that was just sent from your phone appearing in the dashboard data.

**What you say:** "I just signed up on my phone. Went through onboarding. Invited a teammate. And here it is — on a different device, in a different browser, in the retention dashboard. Two real users, one shared database, one live URL. That's not a mockup. That's a product."

### STEP 9: Drop the URL (~30 sec)

**What you do:** Paste the live URL into the class Slack channel (#builds or wherever the class communicates).

**What you say:** "That URL is now in Slack. Anyone can open it. Your mom could open it. Your VP could open it. Try it — open it on your phone right now."

**Pause.** Let students click the URL. Let the room react. This is the emotional peak of M5 — possibly the whole course.

**What you say:** "One click. Thirty seconds. Your onboarding flow is live on the internet. Anyone with this URL can open it, sign up, and use it. That's not a prototype. That's a product. Now it's your turn."

**Transition to Deploy Lab (Slide 18).**

---

## DEPLOY LAB (Slide 18, ~15 min)

**Step 1 (2 min):** Click Publish in Lovable. Get the live URL.

**Step 2 (3 min):** Test in an incognito/private browser window — can you sign up fresh? Does data persist?

**Step 3 (2 min):** Open on your phone. Does it work on mobile?

**Step 4 (3 min):** Post your live URL in #builds Slack channel with caption: "It's live. Try it."

**Step 5 (5 min):** Open 2 classmates' URLs. Sign up. Try to break them. Post what you found.

**Common issue:** If auth redirects fail after deploy, the auth redirect URL needs to include the new deployment domain. Help students update this in Lovable Cloud settings.
