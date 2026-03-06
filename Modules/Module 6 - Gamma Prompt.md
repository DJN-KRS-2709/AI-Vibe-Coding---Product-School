# Gamma Prompt: Module 6 Teaching Slide Deck

**Copy everything below the line and paste it into Gamma. Use "Paste an outline" or the prompt field.**

---

## Instructions for Gamma

Create a professional slide deck for teaching a 2-hour workshop called **"Module 6: Ship It — Go Live"** in a Vibe Coding certification course. The audience is senior product managers who completed Modules 1–5 — they can build fast (M1), build smart with data (M2), build precise with prompt chains (M3), structure prototypes with Living PRDs, GitHub repos, and Supabase connections (M4), and build real backend functionality with databases, auth, and error handling (M5). Now they're deploying to production and presenting their work. Tone: celebratory but professional, energetic, culminating. The deck supports live teaching, demos, hands-on deployment, and student presentations. Avoid corporate jargon. Use clean, modern design with clear typography and minimal text per slide. Match Modules 1–5 visual style. Important: the slides are student-facing — keep the content instructional and practical. Do not telegraph emotional beats or name "wow moments" on slides.

---

## Slide 1 — Module 6 Title + 3 Waypoints
**Ship It — Go Live**

MODULE 6 | VIBE CODING CERTIFICATION

Three things today:
1. **Deploy** — Your product goes live. A real URL anyone can access. No more localhost, no more preview links.
2. **Polish** — Final QA pass. The details that separate a demo from a product: favicon, meta tags, loading performance, mobile responsiveness.
3. **Present** — Gallery walk + optional pitch. The class experiences each other's products. You show what you built and why it matters.

Module 1 was speed. Module 2 was aim. Module 3 was precision. Module 4 was structure. Module 5 was integration. Module 6 is the finish line.

*Speaker Notes: "Welcome to the last module. Everything you've built over five modules — the prototype, the hypothesis, the precision prompts, the structured code, the real database and auth — it all leads here. Today your product goes live. A real URL. Anyone in the world can access it. We deploy, we polish, and then you present your work to the class. Three waypoints: deploy, polish, present. Let's ship."*

---

## Slide 2 — Bridge from M5 + Agenda
**Your M5 Product Works. But Only You Can Access It.**

Your M5 build has real data persistence, real authentication, real error handling. It's a working product. But it lives inside Lovable's preview. Share the link — it works. Close Lovable — it might not. Nobody outside this class has seen it.

Today it goes live.

Today's flow:
1. **Deploy** — One-click deployment to a live URL (15 min)
2. **Polish** — Final QA checklist: mobile, performance, meta tags (15 min)
3. **Gallery Walk** — Experience each other's products (20 min)
4. **Presentations** — 5-minute pitch with live demo (40 min)
5. **The Full Journey** — M1 through M6, side by side
6. **Wrap** — Certification, what's next

*Speaker Notes: "In M5, your product became real — data persists, users log in, errors are handled. But it still lives inside Lovable's preview environment. Today it gets a real URL. Anyone can access it — your manager, your engineering team, your users. We deploy, we polish the details, and then the gallery walk: you'll experience each other's products as real users. After that, presentations — 5 minutes each. Show what you built, what you learned, and what you'd do next. This is the finish line."*

---

## Slide 3 — Instructor Demo: Deploy
**From Preview to Production in One Click**

INSTRUCTOR DEMO

The M5 Retention Engine is a working product inside Lovable. Watch: I click "Deploy." 30 seconds later, it has a live URL. I open it on my phone. I send the link in chat. You can open it right now.

That's deployment.

*Speaker Notes: "Pull up the M5 Retention Engine in Lovable. Show the preview — it works, data persists, auth works. Then: 'Watch.' Click the deploy button in Lovable (top right → Share → Deploy or Publish). Wait for the URL to generate. Open it in a new incognito window. Open it on your phone. Drop the link in the Zoom chat or Slack. 'Click it. You're using my product right now. That URL didn't exist 30 seconds ago.' Let the moment land. This is the simplest demo in the course — one click — but the impact is huge. They're accessing a real product built by a PM, live, on their own devices."*

---

## Slide 4 — What Deployment Actually Means
**What Just Happened**

When you click Deploy in Lovable:

**1. Your code goes to a CDN** — Content Delivery Network. Your app is served from the closest server to whoever opens it. Fast everywhere.

**2. You get a URL** — A real, permanent web address. Share it with anyone. Works on desktop, mobile, any browser.

**3. It's connected to your backend** — Same Supabase database, same auth. Deploy doesn't break your integrations. Users who signed up in preview? Their accounts still work.

**4. Updates are instant** — Change something in Lovable, redeploy. The live URL updates. No DevOps, no CI/CD pipeline, no server configuration.

You don't need to understand infrastructure. You need to click one button.

*Speaker Notes: "Most PMs think deployment requires engineering. Servers, Docker, CI/CD pipelines — none of that. Lovable deploys to a CDN. Your Supabase backend stays connected. Existing user accounts still work. And if you change something, you redeploy — the URL updates instantly. One button. That's it." Keep this to 2 minutes. Don't go deep on CDNs or infrastructure — the point is: deployment is not a barrier for PMs."*

---

## Slide 5 — Custom Domains (Optional)
**Want Your Own Domain?**

Your Lovable deployment gives you a URL like `yourapp.lovable.app`. That works. But if you want a custom domain:

**1. Buy a domain** — Namecheap, Google Domains, Cloudflare (~$10/year)

**2. Point it** — Add a CNAME record pointing to your Lovable deployment

**3. Done** — `yourproduct.com` now loads your app

This is optional. The `.lovable.app` URL is permanent and shareable. Custom domains are for when you want to show this to stakeholders or users who expect a real brand.

*Speaker Notes: "Quick note — you don't need a custom domain. The Lovable URL works fine for demos, testing, and sharing with your team. Custom domains matter when you're putting this in front of real users or stakeholders who expect a polished URL. It's $10 and 5 minutes of DNS configuration. We won't do this in class, but it's in the lab guide if you want to set it up later." 1 minute max. Don't demo this — just mention it."*

---

## Slide 6 — Lab Part 1: Deploy Your Product
**Hands-on Lab Part 1: Deploy** | 15 Minutes

Open your M5 prototype in Lovable. You're going live.

**Step 1 (3 min):** Click Deploy. Get your live URL. Open it in a new incognito window. Does it work?

**Step 2 (2 min):** Test authentication. Create a new account on the live URL. Log in. Does your data persist?

**Step 3 (2 min):** Open on your phone. Is it usable? Can you navigate, log in, see your data?

**Step 4 (3 min):** Drop your live URL in Slack. Try 2 other classmates' live URLs. Sign up. Use them.

**Step 5 (5 min):** If something broke during deploy — debug it. Common issues: Supabase connection, environment variables, auth redirect URLs.

The moment someone else signs up on YOUR product, from THEIR device — that's ship.

*Speaker Notes: "This should take 15 minutes. Most deployments take under a minute. The remaining time is for testing. Walk the room. THE KEY MOMENT: when a student opens their product on their phone and it works. Watch for the reaction. 'That's your product. On your phone. With a real URL. Anyone in the world can open that right now.' If someone's deploy fails: most common issue is Supabase auth redirect URL not including the new domain — help them update it in Supabase settings. After 15 min: 'Who's live? Drop your URL in Slack. We're about to experience each other's products.'"*

---

## Slide 7 — The Polish Checklist
**The Details That Separate a Demo From a Product**

Before the gallery walk, run through this checklist:

**Visual Polish:**
- [ ] Favicon — does your app have a custom icon in the browser tab?
- [ ] Page title — does the tab show your product name, not "Vite App"?
- [ ] Loading — is there a loading state, or does the page flash blank?
- [ ] Mobile — does it work on a phone screen without horizontal scrolling?

**Functional Polish:**
- [ ] Auth flow — can a new user sign up, log in, and see their data?
- [ ] Error handling — what happens if the network is slow?
- [ ] Empty states — what does a brand-new user see before they have any data?
- [ ] Navigation — can a user get back to where they started?

**Professional Polish:**
- [ ] Meta tags — does the link preview show a title and description when shared?
- [ ] Performance — does the page load in under 3 seconds?
- [ ] Copy — are there any placeholder texts like "Lorem ipsum" or "TODO"?

*Speaker Notes: "This is your pre-launch checklist. You don't need all green — but you should know which ones are red. The gallery walk is in 15 minutes. Your classmates are about to use your product as real users. These details matter." Drop the checklist in Slack or reference the lab guide. 2 minutes to explain, then they work on it."*

---

## Slide 8 — Lab Part 2: Polish Sprint
**Polish Sprint** | 15 Minutes

Work through the checklist. Fix what you can in 15 minutes. Prioritize:

**High impact, fast fixes:**
1. Page title and favicon (1 prompt in Lovable)
2. Mobile responsiveness (1 prompt)
3. Empty states for new users (1 prompt)

**Medium impact:**
4. Meta tags for link previews
5. Loading performance
6. Copy cleanup

**Skip for now:**
- Custom domain (do later)
- Advanced performance optimization
- Additional features

After fixing, **redeploy**. Your live URL updates instantly.

*Speaker Notes: "15 minutes. Prioritize. The three fastest wins: page title and favicon — one prompt. Mobile responsive — one prompt. Empty states — one prompt. That's 3 prompts and your product looks professional. After each fix, redeploy. The URL updates instantly." Walk the room. Help anyone stuck on redeployment. After 15 min: 'Stop polishing. Redeploy one final time. Your product is about to have real users — your classmates.'"*

---

## Slide 9 — Gallery Walk Setup
**Gallery Walk: Experience Each Other's Products**

GALLERY WALK | 20 Minutes

Rules:
1. **Post your live URL** in the Slack channel
2. **Open 4–5 classmates' products** — you're a real user now
3. **For each product, do a real user test:**
   - Sign up with a real email
   - Try the core flow — what's this product trying to do?
   - Try to break it — what happens when you do something unexpected?
   - Note: one thing that impressed you, one thing that confused you
4. **Post feedback in Slack** — tag the builder with your one-line review

This is not a demo. You're not watching a presentation. You're using real products, built by PMs, deployed to real URLs.

*Speaker Notes: "This is the most unique exercise in the course. Your classmates built real, deployed products. You're going to use them — as a real user. Sign up with your actual email. Try the core flow. Try to break it. Then give honest feedback. 'One thing that impressed me. One thing that confused me.' This is the PM skill: evaluating a product as a user, not as a builder." For online teaching: everyone opens products in their own browser. Post URLs in Slack. 20 minutes. Walk the virtual room — check Slack for reactions, highlight interesting moments. 'Who found a product where the error handling actually worked? Who found one where it didn't?'"*

---

## Slide 10 — Gallery Walk Debrief
**What Did You Notice?**

Quick reactions:

1. **What surprised you** about using someone else's product?
2. **What's the difference** between a deployed product and a Lovable preview?
3. **Which product felt the most "real"?** What made it feel that way?

The things that made products feel real: persistent data, personalized content after login, proper error messages, fast loading, mobile-friendly, professional details (favicon, title, meta tags).

*Speaker Notes: "Quick debrief — 5 minutes. 'What surprised you?' Most common answer: 'I was surprised how real it felt' or 'I found a bug the builder didn't know about.' Then: 'What's the difference between preview and deployed?' The answer is mostly psychological — but it matters. A live URL changes how people perceive your work. It's not a prototype anymore. It's a product.' Transition to presentations: 'You've used each other's products. Now let's hear the stories behind them.'"*

---

## Slide 11 — Presentation Format
**Your 5-Minute Pitch**

STUDENT PRESENTATIONS | 5 Minutes Each

Structure:

**1. The Problem (30 sec)** — What user problem are you solving? One sentence.

**2. The Hypothesis (30 sec)** — What did you test? What was your M2 assumption?

**3. Live Demo (2 min)** — Show your deployed product. Walk through the core flow. Show one integration: data persistence, auth, or an API.

**4. What You Learned (1 min)** — What worked? What surprised you? What would you change?

**5. The Journey (1 min)** — Show your M1 build vs. your M6 build. Side by side. What changed?

No slides required. Your product IS the presentation.

*Speaker Notes: "5 minutes each. Strict time. No slides — your product is the presentation. Share your screen. Walk us through the live URL. Show the problem, the hypothesis, the product, what you learned. The most powerful moment: your M1 build vs. M6 build side by side. Same scenario, five modules of growth." If teaching online, students share screen. Have a timer visible. Be strict on 5 minutes — it forces clarity. If you have 20 students, select 6–8 to present live, have others post video walkthroughs in Slack."*

---

## Slide 12 — Presentations Begin
**Let's See What You Built**

LIVE PRESENTATIONS

[Instructor manages presentation queue — selected students present their 5-minute pitch with live demo]

Feedback format for audience:
- 🔥 Drop a fire emoji in chat when something impresses you
- 💡 "One thing I'd steal from this product: ___"
- ❓ "One question I'd ask as a PM: ___"

*Speaker Notes: "Call presenters by name. After each presentation, invite 1–2 questions from the audience. Encourage the fire emoji and 'one thing I'd steal' reactions — this keeps energy high and gives presenters real-time feedback. If you have more students than presentation slots: the remaining students post a 2-minute Loom video walkthrough in Slack before the next session. Everyone's product gets seen." Keep energy celebratory. This is the culmination of the course. Applaud after each one."*

---

## Slide 13 — The Full Journey: Six Tabs
**M1. M2. M3. M4. M5. M6. The Complete Arc.**

Open six tabs.

**Module 1:** One prompt, one page. Static. No data. Built in 10 minutes.

**Module 2:** Real data, hypothesis, design-matched. Built with context. Still hardcoded.

**Module 3:** 5+ screens, interactive states, documented prompt chain. A complete facade.

**Module 4:** Clean code in GitHub, Supabase connected, Living PRD, engineering handoff. Structured for real.

**Module 5:** Real database, real auth, real error handling. A working product.

**Module 6:** Deployed. Live URL. Anyone can access it. Polished. Presented. Shipped.

Same tool. Same you. Six modules.

*Speaker Notes: "This is the final reveal. If students have all six versions saved — have them open all six tabs. 30 seconds of silence. Let them look. 'In Module 1, you typed one prompt and got a page. In Module 6, you deployed a multi-user product with a real database, authentication, error handling, and a live URL that anyone in the world can access. You built this. All of it. In six modules.' This is the emotional crescendo. Don't rush it. Let it land."*

---

## Slide 14 — What You Built (Complete Deliverables)
**Your Complete Product Package**

Over six modules, you built:

**1. A Deployed Product** — Live URL, real database, real auth, error handling. Works on desktop and mobile.

**2. A Living PRD** — AI-extracted spec that describes what your product does, who it's for, what's tested, and what's next.

**3. A GitHub Repository** — Version-controlled, refactored code with a README. Any engineer can clone and continue.

**4. An Engineering Handoff Note** — What integrations are real, what's mocked, what edge cases are handled, where to start.

**5. A Living Prompt Pack** — Your full prompt chain: build, validate, precision, structure, integration, deployment. Portable and reusable.

**6. A Presentation** — You pitched a live product to an audience of PMs. The product spoke for itself.

This is not a course artifact. This is a product portfolio.

*Speaker Notes: "Let's name what you actually have. Not what you learned — what you built. A deployed product. A spec. A codebase. A handoff note. A reusable prompt library. And a presentation where your live product was the demo. That's a portfolio. If you walked into a stakeholder meeting tomorrow with this package — deployed product, spec, GitHub repo, handoff note — you'd be further along than most product teams are after a quarter of work."*

---

## Slide 15 — The Confidence Line (Complete)
**The Vibe Coding Confidence Line**

Where you started → Where you are:

**M1:** "I can build something in 10 minutes" → Speed confidence

**M2:** "I can test the right thing" → Validation confidence

**M3:** "I can build exactly what I describe" → Precision confidence

**M4:** "I can structure it for a real team" → Structure confidence

**M5:** "I can make it actually work" → Integration confidence

**M6:** "I can ship it to real users" → Ship confidence

The entire arc: from "I wonder if AI can build things" to "I just shipped a product."

*Speaker Notes: "This is the full confidence line. In M1, most of you weren't sure AI tools could build anything useful. Now you've shipped a multi-user product with a database, auth, and a live URL. That's not because the tool is magic — it's because you learned how to describe what you want, when to validate, how to be precise, when to structure, how to integrate, and when to ship. That's the Vibe Coding methodology. It doesn't expire when you leave this course."*

---

## Slide 16 — What's Next: Beyond the Course
**This Doesn't End Here**

Three paths forward:

**1. Ship to Real Users**
Your product has a live URL. Show it to real users. Run a pilot. Collect feedback. Iterate with the same methodology: build-show-learn-decide.

**2. Hand Off to Engineering**
Your Living PRD + GitHub repo + Engineering Handoff Note = a complete package. An engineer can clone your repo and start building tomorrow. You've done the hard part: proving the concept works.

**3. Start Your Next Product**
Your Living Prompt Pack is portable. Open a new Lovable project. Import your prompts. You'll move 10x faster the second time because you've already built the muscle memory.

*Speaker Notes: "Three paths. One — ship to real users. Your product is live. Show it to your actual users or stakeholders. Run a real pilot. You have a deployed product with real data — that's enough to validate with real people. Two — hand off to engineering. You have a spec, a codebase, and a handoff note. That's the package engineers need. Three — start something new. Your prompt pack is a reusable skill. You'll move dramatically faster the second time. Most PMs in this course go back and apply this methodology to a real project within two weeks."*

---

## Slide 17 — Certification
**Vibe Coding Certification — Complete**

You've earned it.

**What it means:**
- You can take a product idea from zero to deployed in hours, not months
- You can validate hypotheses with working prototypes, not slide decks
- You can structure prototypes into real products with specs, version control, and integrations
- You can ship — to a live URL, with a real backend, ready for real users

**Your certification package:**
- Certificate of completion
- Your deployed product URL
- Your GitHub repository
- Access to the alumni community and prompt library

*Speaker Notes: "You've completed the Vibe Coding Certification. What does that mean? It means you can build, validate, and ship products using AI tools — and you've proven it by doing it. You have a deployed product, a spec, a codebase, and a reusable prompt library. That's not theoretical. That's tangible. Keep building. Keep shipping. And stay connected — the alumni community is where you'll share what you build next." Celebrate. This is the moment. If you have digital certificates, share them now."*

---

## Slide 18 — Final Accountability
**ACCOUNTABILITY** | Your Ship Checklist

Before you close your laptop:

**1. Verify your live URL works** — Open it in incognito. Send it to someone outside this class. Does it work?

**2. Finalize your Engineering Handoff Note** — What's real, what's mocked, what's next. Use the Integration Planner's handoff section from M5.

**3. Export your Living Prompt Pack** — Your complete prompt chain from M1–M6. Save it as a markdown file. This is your portable skill.

**4. Post your final build in #builds** — Live URL + one-sentence summary: "What problem does this solve?" Include your M1 build link for comparison.

**5. Celebrate** — You just shipped a product. Most product teams take quarters. You did it in six sessions.

*Speaker Notes: "Five things before you leave. One — verify your live URL works right now. Open it in incognito. Send it to someone outside this class. Two — finalize your Engineering Handoff Note. Three — export your Living Prompt Pack — that's your portable skill file. Four — post your final build in #builds with your M1 link for comparison. Let the community see the journey. Five — celebrate. You shipped a product. That's real."*

---

## Slide 19 — Thank You
**Thank You**

You came in wondering if AI tools were real. You're leaving with a deployed product.

That's Vibe Coding.

Keep building. Keep shipping. Stay curious.

*Speaker Notes: "Simple close. 'Thank you for showing up every session and building. You came in wondering if AI tools were real. You're leaving with a deployed product, a spec, a codebase, and a methodology you can apply tomorrow. That's Vibe Coding. Now go ship something.' If energy allows — invite one student to share a final reflection. Keep it short. End on a high."*

---

## Slide 20 — Survey
**Your Opinion Matters To Us**

Scan the QR code or use the link to share your feedback. Your insights help us improve each cohort.

---

## Design Notes for Gamma
- Match Modules 1–5 visual template exactly (same fonts, colors, layout grid)
- Slides are student-facing course material — keep content clean, instructional, and practical
- **This is the final module — the visual energy should feel culminating. Consider subtle celebratory elements: confetti/sparkle accents on the certification slide, bolder typography on the six-tab reveal**
- Slide 1 — Bold title, three waypoints (deploy, polish, present) as prominent numbered list
- Slide 3 — Demo should feel effortless: one click, live URL. Minimal text, maximum impact
- Slide 6 — Lab steps must be scannable at a glance. Students reference this while deploying
- Slide 7 — Polish checklist should use actual checkboxes. Students work through this
- Slide 9 — Gallery walk rules should feel like an event, not an exercise
- Slide 11 — Presentation format needs to be scannable — students reference this while presenting
- Slide 13 — Six-column layout (M1 | M2 | M3 | M4 | M5 | M6). The visual comparison is the emotional peak
- Slide 14 — Complete deliverables as a proud list — these represent the full course output
- Slide 15 — Confidence line as a visual progression/staircase — show the arc
- Slide 17 — Certification slide should feel special. Celebratory design. This is the reward
- Keep lab slides (6, 8) highly scannable — students reference these while working
