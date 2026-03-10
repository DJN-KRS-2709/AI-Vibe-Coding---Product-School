# Gamma Prompt: Module 6 Teaching Slide Deck

**Copy everything below the line and paste it into Gamma. Use "Paste an outline" or the prompt field.**

---

## Instructions for Gamma

Create a professional slide deck for teaching a 2-hour workshop called **"Module 6: Measure, Learn, Iterate"** in a Vibe Coding certification course. The audience is senior product managers who completed Modules 1–5 — they can build fast (M1), build smart with data (M2), build precise with prompt chains (M3), structure prototypes with Living PRDs, GitHub repos, and Supabase connections (M4), and build real backend functionality with databases, auth, error handling, AND deploy to a live URL (M5). Now they're closing the product lifecycle loop: measuring what's working, using AI to analyze data, and iterating based on evidence. Tone: analytical but energetic, culminating. The deck supports live teaching, demos, hands-on labs, gallery walk, and student presentations. Avoid corporate jargon. Use clean, modern design with clear typography and minimal text per slide. Match Modules 1–5 visual style. Important: the slides are student-facing — keep the content instructional and practical. Do not telegraph emotional beats or name "wow moments" on slides.

---

## Slide 1 — Module 6 Title + 3 Waypoints
**Measure, Learn, Iterate**

MODULE 6 | VIBE CODING CERTIFICATION

Three things today:
1. **Measure** — Set up analytics on your deployed product. Know what's happening, not what you think is happening.
2. **Learn** — Use AI to analyze your product data against your problem statement. Is your product solving the problem you defined?
3. **Iterate** — Build one evidence-based improvement and redeploy. Not a guess — an improvement backed by data.

Module 1 was speed. Module 2 was aim. Module 3 was precision. Module 4 was structure. Module 5 was ship. Module 6 is how you learn from it.

*Speaker Notes: "Welcome to the final module. Your product is live. People can use it. But shipping isn't the finish line — it's the starting line for learning. Every real product team does this: ship, measure, learn, iterate. Today you'll set up analytics, use AI to analyze your data against your problem statement, and build one improvement based on what you find. Three waypoints: measure, learn, iterate. This is where PMs separate from builders."*

---

## Slide 2 — Bridge from M5 + Agenda
**Your Product Is Live. But How Do You Know It's Working?**

In M5, your product went from facade to deployed. It has a live URL, real data, real users. Anyone can access it. But here's the PM question: **is it solving the problem you defined in M2?**

You shipped. Now you learn.

Today's flow:
1. **Analytics Demo** — Setting up tracking on your deployed product (8 min)
2. **Lab 1: Connect Analytics** — Instrument your product (15 min)
3. **AI Analysis** — Using AI to evaluate metrics against your problem statement (10 min)
4. **Lab 2: AI Analysis Sprint** — Pull data, analyze with AI (15 min)
5. **Iteration** — Build one data-driven improvement and redeploy (10 min)
6. **Quick Polish** — Final cleanup (5 min)
7. **Gallery Walk** — Experience each other's products (25 min)
8. **Presentations** — 5-minute pitch with live demo (30 min)
9. **Wrap** — The full journey, certification, what's next

*Speaker Notes: "In M5, you deployed. You shared your URL. Classmates signed up. But here's the question every PM must answer after shipping: is it working? Not 'does it load' — you know it loads. Is it solving the problem you defined in M2? That requires data. Today is the most advanced module in the course. You'll set up analytics, use AI to analyze what you find, build one evidence-based improvement, and then present the full journey. This is the complete product lifecycle: understand it, think it, build it, ship it, tweak it."*

---

## Slide 3 — Instructor Demo: Setting Up Analytics
**What's Actually Happening on Your Product?**

INSTRUCTOR DEMO

Two ways to see what's happening on your deployed product:

**1. Lovable Insights** — Built-in analytics dashboard. Shows page views, user sessions, most-used features. Available for any deployed Lovable project.

**2. Google Analytics (GA4)** — Industry-standard tracking. Requires adding a GA4 tag to your project. Shows everything: traffic sources, user flows, bounce rates, conversion funnels.

Watch: I open my deployed Retention Engine. I pull up the Lovable insights panel. Then I show you what GA4 adds on top.

The data is already being collected. You just need to look at it.

*Speaker Notes: "Pull up the deployed Retention Engine. Open Lovable's insights/analytics panel (if available) — show page views, sessions, any built-in metrics. Then switch to GA4: show the real-time view, the user flow, the engagement metrics. 'Your product has been live since M5. People have been using it. But did you know this data existed?' Keep the demo to about 5 minutes. Don't go deep on GA4 configuration — the lab covers that. The point is: data is available, you just need to look. Transition: 'Let's talk about what to measure.'"*

---

## Slide 4 — What to Measure
**Not Everything That Counts Can Be Counted. But Start Here.**

For your deployed product, focus on these metrics:

**Engagement:**
- How many users signed up?
- How many completed the core flow?
- Which features are used most? Which are ignored?

**Retention:**
- Do users come back after their first session?
- Where do users drop off?

**Quality:**
- Page load time — under 3 seconds?
- Error rates — are users hitting dead ends?
- Mobile vs. desktop usage

**Impact:**
- Does the product behavior match your M2 hypothesis?
- If your hypothesis was "PMs will track invite status weekly" — are they?

The metric that matters most: **does user behavior confirm or contradict your original problem statement?**

*Speaker Notes: "You don't need 50 metrics. You need 3–5 that map to your problem statement. If your M2 hypothesis was 'PMs will track invite status weekly' — then your key metric is: do they? How often? Where do they drop off? The engagement and retention numbers tell you if people use it. The impact question tells you if it's solving the problem. That's what a PM measures after launch. Not vanity metrics — evidence." Keep this to 3 minutes. It's a framework, not a lecture."*

---

## Slide 5 — Lab Part 1: Connect Analytics
**Hands-on Lab: Set Up Tracking** | 15 Minutes

Instrument your deployed product with analytics.

**Step 1 (5 min):** Open your deployed product's Lovable insights panel. Review what's already being tracked. Screenshot your current metrics — this is your baseline.

**Step 2 (5 min):** Set up Google Analytics. Create a GA4 property (free). Get the Measurement ID (starts with G-). Prompt Lovable:

> "Add Google Analytics tracking to this project. Use Measurement ID: G-XXXXXXXXXX. Add the gtag script to the head of the main HTML file. Track page views automatically."

Redeploy after adding the tag.

**Step 3 (5 min):** Verify tracking is working. Open your deployed product in a new tab. Check GA4 real-time view — you should see yourself as a live user. Open on your phone — two live users.

If GA4 setup takes too long, Lovable insights alone is enough for today's analysis.

*Speaker Notes: "15 minutes. Most students will get GA4 connected in under 5 minutes — it's one prompt. The hard part is finding the Measurement ID in the GA4 setup flow. Walk them through it: go to analytics.google.com, create a property, choose 'Web', get the Measurement ID. If anyone gets stuck on GA4, they can use Lovable's built-in insights — that's enough for the analysis sprint. After 15 min: 'Who can see themselves in the real-time view? That's your product, being measured, right now.'"*

---

## Slide 6 — Teaching: AI-Powered Product Analysis
**The PM's New Superpower: AI + Data + Problem Statement**

Traditional product analysis: export data to a spreadsheet, build charts, write an analysis doc, present to stakeholders. Takes days.

AI-powered product analysis: feed your metrics + your problem statement to AI. Get an evaluation in minutes.

**The formula:**
1. Pull your product metrics (from Lovable insights or GA4)
2. Pull your problem statement from your Living PRD (M4)
3. Pull your M2 hypothesis
4. Feed all three to ChatGPT or Gemini:

> "Here is my problem statement: [X]. Here is my hypothesis: [Y]. Here are the metrics from my deployed product after [Z] days: [data]. Evaluate whether we are solving the problem. What does the data suggest? What would you recommend changing?"

The AI doesn't replace your judgment. It accelerates your analysis.

*Speaker Notes: "This is the most advanced PM skill in the course. You're not asking AI to build something — you're asking it to think with you. Feed it three things: your problem statement, your hypothesis, and your actual data. The AI will synthesize what would take you hours in a spreadsheet. It'll flag patterns you might miss. It'll ask questions you didn't think of. But YOU make the decision about what to do next. The AI accelerates analysis. You own the judgment." Keep this to 5 minutes. The demo next makes it concrete."*

---

## Slide 7 — Demo: AI Analysis in Action
**Watch: From Metrics to Insight in 2 Minutes**

INSTRUCTOR DEMO

Live demo: I pull my Retention Engine metrics. I copy my problem statement from my Living PRD. I paste both into ChatGPT.

**Input:**
- Problem statement: "PMs lose track of candidate invites and follow-up timing, leading to 30% drop-off in their recruitment pipeline."
- Hypothesis: "If PMs can see invite status in a single dashboard, they'll follow up within 48 hours."
- Metrics: [Lovable insights / GA4 data — sessions, core flow completions, feature usage]

**Output:**
- AI evaluation of whether the hypothesis is confirmed
- Patterns in user behavior
- Suggested improvements ranked by likely impact

That analysis would take a product team a day. You just did it in 2 minutes.

*Speaker Notes: "Live demo. Have your ChatGPT or Gemini window open. Copy the problem statement from your Living PRD. Copy the metrics from your Lovable insights or GA4. Paste them together with the analysis prompt. Let students watch the AI response generate in real-time. Read the key findings out loud. 'Look — it identified that users are signing up but not completing the follow-up flow. That matches what we see in the data. It's recommending we simplify the follow-up action.' The point: the AI connected your data to your problem statement faster than you could in a spreadsheet." Keep this to 5 minutes."*

---

## Slide 8 — Lab Part 2: AI Analysis Sprint
**Hands-on Lab: Analyze Your Product** | 15 Minutes

Pull your data. Ask AI to evaluate it.

**Step 1 (3 min):** Open your Lovable insights or GA4. Screenshot or copy your key metrics: sessions, user counts, feature usage, any engagement data.

**Step 2 (2 min):** Open your Living PRD (from M4). Copy your problem statement and your M2 hypothesis.

**Step 3 (5 min):** Open ChatGPT or Gemini. Use this prompt:

> "I built a product to solve this problem: [problem statement]. My hypothesis was: [hypothesis]. Here are the metrics from my deployed product: [paste metrics]. Evaluate: is this product solving the problem? What does the data suggest? What are the top 3 things I should improve, ranked by likely impact?"

**Step 4 (5 min):** Read the AI's analysis. Highlight the single highest-impact recommendation. That's what you'll build next.

*Speaker Notes: "15 minutes. The hardest part is Step 2 — finding their problem statement. If they can't find their Living PRD, have them write a one-sentence problem statement from memory. That's fine. The AI analysis is most powerful when the problem statement is specific. After 15 min: 'What did AI tell you? Anyone surprised by what it found?' Get 2–3 students to share their top finding. This surfaces the learning moment: the data told them something they didn't expect."*

---

## Slide 9 — Teaching: The Iteration Prompt
**Evidence-Based Improvement vs. Guess-Based Improvement**

Most PMs iterate by instinct: "I think the onboarding is confusing, let me redesign it."

Evidence-based iteration: "Users drop off at step 3 of onboarding. The AI analysis suggests the CTA is unclear. Let me rewrite step 3."

**The Iteration Prompt Pattern:**

> "Based on this analysis: [paste AI findings]. The highest-impact improvement is: [specific finding]. Update the product to address this: [describe the change]. Keep everything else working."

This is different from your M1–M5 prompts. You're not building new features. You're improving existing ones based on evidence.

Spotify calls this "tweak it" — the fifth stage of their product lifecycle: understand it, think it, build it, ship it, tweak it.

*Speaker Notes: "This is the mindset shift. In M1 through M5, you were building. Adding features. Creating things. Now you're improving. The iteration prompt is different: you're not saying 'add X.' You're saying 'the data shows Y is broken, fix it like this.' That's the PM skill. Spotify calls it 'tweak it' — the stage after shipping where you learn and improve based on evidence, not guesses. The best PMs spend more time here than in any other stage." Keep this to 5 minutes."*

---

## Slide 10 — Lab Part 3: Build One Improvement
**Hands-on Lab: One Data-Driven Fix** | 10 Minutes

Pick the single highest-impact finding from your AI analysis. Build it.

**Step 1 (2 min):** Write your iteration prompt. Use the pattern:
> "Based on user data showing [specific finding], update [specific part of the product] to [specific change]. Keep all existing functionality working."

**Step 2 (5 min):** Paste the prompt into Lovable. Review the changes. Test them.

**Step 3 (3 min):** Redeploy. Your live URL now reflects a data-driven improvement.

You just completed the full product lifecycle: understand the problem → hypothesize → build → ship → measure → learn → improve.

*Speaker Notes: "10 minutes. One change. The temptation will be to fix everything — resist it. Pick the single highest-impact finding. Write the iteration prompt. Build it. Redeploy. The point is not to ship a perfect product. The point is to close the loop: data → insight → action. After 10 min: 'Who redeployed? What did you change and why?' Get 2–3 answers. Each answer should reference the data that drove the decision."*

---

## Slide 11 — Quick Polish
**Final Cleanup** | 5 Minutes

Quick checklist before the gallery walk:

- [ ] Page title shows your product name
- [ ] Favicon is set
- [ ] Mobile responsive — check on your phone
- [ ] No placeholder text ("Lorem ipsum", "TODO")
- [ ] Live URL works in incognito

If any of these are broken, one prompt each:

> "Update the page title to '[Your Product Name]' and add a favicon that matches the product's brand."

> "Make this app fully responsive for mobile screens."

Redeploy after fixes. Your classmates are about to use your product.

*Speaker Notes: "5 minutes. Quick polish only. Page title, favicon, mobile check. If any of these are broken, it's one prompt each. Redeploy. Your product is about to have real users — your classmates. Don't start new features. Just clean up what's there." Walk the room. After 5 min: 'Stop. Redeploy one final time. Gallery walk starts now.'"*

---

## Slide 12 — Gallery Walk Setup
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

This is not a demo. You're using real products, built by PMs, deployed to real URLs, improved with real data.

*Speaker Notes: "This is the most unique exercise in the course. Your classmates built real, deployed products — and they just improved them based on data analysis. You're going to use them as a real user. Sign up with your actual email. Try the core flow. Try to break it. Then give honest feedback. 'One thing that impressed me. One thing that confused me.' For online: everyone opens products in their browser. Post URLs in Slack. 20 minutes. Walk the virtual room — check Slack for reactions. 'Who found a product that clearly improved from the data analysis? Who found solid error handling?'"*

---

## Slide 13 — Gallery Walk Debrief
**What Did You Notice?**

Quick reactions:

1. **Which product felt the most "real"?** What made it feel that way?
2. **Could you tell** which products had been improved based on data?
3. **What's the difference** between a product that's shipped and a product that's been iterated on?

The difference between M5 and M6: M5 products work. M6 products learn.

*Speaker Notes: "Quick debrief — 5 minutes. 'Which product felt the most real? What made it feel that way?' Then: 'Could you tell which products had been improved based on data versus just polished?' The answer reveals the M6 lesson: iteration based on evidence produces different results than iteration based on instinct. Transition: 'You've used each other's products. Now let's hear the stories behind them.'"*

---

## Slide 14 — Presentation Format
**Your 5-Minute Pitch**

STUDENT PRESENTATIONS | 5 Minutes Each

Structure:

**1. The Problem (30 sec)** — What user problem are you solving? One sentence.

**2. The Hypothesis (30 sec)** — What did you test? What was your M2 assumption?

**3. Live Demo (2 min)** — Show your deployed product. Walk through the core flow. Show one key integration.

**4. What the Data Told You (1 min)** — What did analytics reveal? What did AI analysis surface? What improvement did you make based on evidence?

**5. The Journey (1 min)** — Show your M1 build vs. your M6 build. Side by side. What changed?

No slides required. Your product IS the presentation.

*Speaker Notes: "5 minutes each. Strict time. No slides — your product is the presentation. Share your screen. Walk us through the live URL. The new element vs. previous modules: 'What the data told you.' This is the M6 differentiator — you're not just showing what you built, you're showing what you learned and how you improved based on evidence. The most powerful moment: M1 vs. M6 side by side." If you have 20 students, select 6–8 to present live, others post video walkthroughs in Slack."*

---

## Slide 15 — Presentations Begin
**Let's See What You Built — and What You Learned**

LIVE PRESENTATIONS

[Instructor manages presentation queue — selected students present their 5-minute pitch with live demo]

Feedback format for audience:
- Drop a fire emoji in chat when something impresses you
- "One thing I'd steal from this product: ___"
- "One question I'd ask as a PM: ___"

*Speaker Notes: "Call presenters by name. After each presentation, invite 1–2 questions. Encourage reactions in chat — this keeps energy high and gives presenters real-time feedback. If you have more students than presentation slots, remaining students post a 2-minute Loom video walkthrough in Slack. Everyone's product gets seen. Keep energy celebratory. This is the culmination of the course."*

---

## Slide 16 — The Full Journey: Six Tabs
**M1. M2. M3. M4. M5. M6. The Complete Arc.**

Open six tabs.

**Module 1:** One prompt, one page. Static. No data. Built in 10 minutes.

**Module 2:** Real data, hypothesis, design-matched. Built with context. Still hardcoded.

**Module 3:** 5+ screens, interactive states, documented prompt chain. A complete facade.

**Module 4:** Clean code in GitHub, Supabase connected, Living PRD, engineering handoff. Structured for real.

**Module 5:** Real database, real auth, real error handling. Deployed to a live URL.

**Module 6:** Measured. Analyzed with AI. Improved based on evidence. A product that learns.

Same tool. Same you. Six modules. The complete product lifecycle.

*Speaker Notes: "This is the final reveal. Have students open all six tabs. 30 seconds of silence. 'In Module 1, you typed one prompt and got a page. In Module 6, you used AI to analyze your deployed product's data against your problem statement and made an evidence-based improvement. That's not prototyping. That's product management. The full cycle: understand it, think it, build it, ship it, tweak it.' Let it land."*

---

## Slide 17 — What You Built (Complete Deliverables)
**Your Complete Product Package**

Over six modules, you built:

**1. A Deployed Product** — Live URL, real database, real auth, error handling. Improved based on data. Works on desktop and mobile.

**2. A Living PRD** — AI-extracted spec that describes what your product does, who it's for, what's tested, and what's next.

**3. A GitHub Repository** — Version-controlled, refactored code with a README. Any engineer can clone and continue.

**4. An Engineering Handoff Note** — What integrations are real, what's mocked, what edge cases are handled, where to start.

**5. A Living Prompt Pack** — Your full prompt chain: build, validate, precision, structure, integration, deployment, analytics, iteration. Portable and reusable.

**6. A Data-Driven Presentation** — You pitched a live product to an audience of PMs, including what the data told you and how you improved based on evidence.

This is not a course artifact. This is a product portfolio.

*Speaker Notes: "Let's name what you actually have. A deployed product. A spec. A codebase. A handoff note. A reusable prompt library. And a presentation backed by real data. If you walked into a stakeholder meeting with this package — deployed product, analytics showing user behavior, and a data-driven improvement you already shipped — that's more convincing than most quarterly reviews."*

---

## Slide 18 — The Confidence Line (Complete)
**The Vibe Coding Confidence Line**

Where you started → Where you are:

**M1:** "I can build something in 10 minutes" → Speed confidence

**M2:** "I can test the right thing" → Validation confidence

**M3:** "I can build exactly what I describe" → Precision confidence

**M4:** "I can structure it for a real team" → Structure confidence

**M5:** "I can make it real and ship it" → Ship confidence

**M6:** "I can learn from it and make it better" → Product confidence

The entire arc: from "I wonder if AI can build things" to "I just shipped, measured, and improved a product."

*Speaker Notes: "This is the full confidence line. M5 was ship confidence. M6 adds the final layer: product confidence. You don't just build. You ship, measure, learn, and iterate. That's the complete PM skill set with AI tools. It doesn't expire when you leave this course."*

---

## Slide 19 — What's Next + Certification + Close
**Vibe Coding Certification — Complete**

You've earned it.

**What it means:**
- You can take a product idea from zero to deployed in hours, not months
- You can validate hypotheses with working prototypes, not slide decks
- You can ship to real users AND measure whether it's working
- You can use AI to analyze, iterate, and improve based on evidence

**Three paths forward:**
1. **Ship to Real Users** — Run a real pilot. Use your analytics setup to measure. Iterate.
2. **Hand Off to Engineering** — Living PRD + GitHub + Handoff Note + analytics data = complete package.
3. **Start Your Next Product** — Your Living Prompt Pack is portable. You'll move 10x faster the second time.

**Your certification package:**
- Certificate of completion
- Your deployed product URL
- Your GitHub repository
- Access to the alumni community and prompt library

Keep building. Keep shipping. Keep learning.

*Speaker Notes: "You've completed the Vibe Coding Certification. You can build, validate, ship, measure, and iterate products using AI tools — and you've proven it by doing it. Your prompt pack is portable. Your methodology is transferable. Most PMs in this course go back and apply this to a real project within two weeks. Stay connected in the alumni community. Keep building. Keep shipping. Keep learning." Celebrate. If you have digital certificates, share them now."*

---

## Slide 20 — Survey
**Your Opinion Matters To Us**

Scan the QR code or use the link to share your feedback. Your insights help us improve each cohort.

---

## Design Notes for Gamma
- Match Modules 1–5 visual template exactly (same fonts, colors, layout grid)
- Slides are student-facing course material — keep content clean, instructional, and practical
- **This is the final module — the visual energy should feel culminating. Consider subtle celebratory elements on the certification slide, bolder typography on the six-tab reveal**
- Slide 1 — Bold title, three waypoints (measure, learn, iterate) as prominent numbered list
- Slide 3 — Analytics demo should feel like opening a window: "look at all this data you didn't know existed"
- Slide 5 — Lab steps must be scannable at a glance. Students reference this while setting up analytics
- Slide 7 — AI analysis demo: show the prompt and the AI response side by side. The speed is the point
- Slide 8 — Lab: Analysis sprint. The prompt template should be copy-pasteable from the slide
- Slide 10 — Lab: One improvement. Keep it focused — one change, one redeploy
- Slide 12 — Gallery walk rules should feel like an event, not an exercise
- Slide 14 — Presentation format needs to be scannable — students reference this while presenting
- Slide 16 — Six-column layout (M1 | M2 | M3 | M4 | M5 | M6). The visual comparison is the emotional peak
- Slide 17 — Complete deliverables as a proud list — these represent the full course output
- Slide 18 — Confidence line as a visual progression/staircase — show the arc
- Slide 19 — Certification slide should feel special. Celebratory design. This is the reward
- Keep lab slides (5, 8, 10) highly scannable — students reference these while working
