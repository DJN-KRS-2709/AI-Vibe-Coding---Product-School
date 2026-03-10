# Module 6: Measure, Learn, Iterate — Speaker Notes for Carlos

> For Carlos only. High-level bullets explaining what we're doing and why.
> Slide numbers match the Gamma Prompt (slides 1–20). Update if Gamma reorders.

---

## Where M6 Sits

- M1 = speed, M2 = aim, M3 = precision, M4 = structure, M5 = ship, **M6 = learn**
- The final stage of the product lifecycle: understand it, think it, build it, ship it, **tweak it**
- Students go from owning a deployed product → owning a **product that learns from data**
- M5 shipped it. M6 closes the loop: measure what's happening, use AI to analyze it, iterate based on evidence
- This is the most advanced PM module — not because it's hard, but because it requires the mindset shift from "building" to "learning"

---

## The M6 Wow (Two Beats)

- **Beat 1 — The Data Reveal:** Students open their analytics and see real usage data from their deployed product. They didn't know this data existed. "People have been using my product and I can see exactly what they did." The moment data becomes real.
- **Beat 2 — AI-Powered Analysis:** Students feed their metrics + problem statement to ChatGPT/Gemini and get back a coherent product analysis in 2 minutes. Something that would take a product team a day to produce. "AI just told me what to fix — and it's right."
- **Crescendo:** Six-tab reveal — M1 through M6 side by side. The progression from one prompt to a deployed, measured, iterated product. The full product lifecycle in six tabs.

---

## What Changed From Previous M6

- **Deployment moved to M5** — Students already deployed in M5. Their products have been live. M6 starts with a live, deployed product.
- **M6 is no longer about shipping** — it's about the feedback loop after shipping. Measure, learn, iterate.
- **Three new labs** — Lab 1: Connect Analytics. Lab 2: AI Analysis Sprint. Lab 3: Build One Improvement.
- **AI as analyst, not builder** — In M1–M5, AI built things. In M6, AI analyzes things. That's the mindset shift.
- **Gallery walk and presentations preserved** — Same format, but now students present what the data told them, not just what they built.
- **Compressed polish** — 5 minutes instead of 15. The polish sprint from old M6 is compressed because students already polished during deploy in M5.

---

## Slide 1 | Opening (Title + 3 Waypoints)

- Three waypoints: Measure, Learn, Iterate
- "Your product is live. But how do you know it's working?"
- Frame the session as the final stage of the product lifecycle
- Module 1 was speed, Module 2 was aim, Module 3 was precision, Module 4 was structure, Module 5 was ship, Module 6 is how you learn from it

---

## Slide 2 | Bridge from M5 + Agenda

- "Your product has a live URL, real data, real users. But is it solving the problem you defined in M2?"
- Names the gap between shipping and learning
- Agenda: Analytics Demo → Lab 1 → AI Analysis → Lab 2 → Iteration → Lab 3 → Polish → Gallery Walk → Presentations → Wrap
- Key line: "You shipped. Now you learn."

---

## Slide 3 | Demo: Setting Up Analytics

- Pull up the deployed Retention Engine
- Show Lovable's built-in insights panel (page views, sessions, feature usage)
- Show GA4 dashboard with richer data (real-time view, user flows, engagement)
- "Your product has been live since M5. People have been using it. Did you know this data existed?"
- ~5 minutes. Don't go deep on GA4 configuration — the lab covers that

---

## Slide 4 | What to Measure

- Four categories: Engagement, Retention, Quality, Impact
- The metric that matters most: does user behavior confirm or contradict the original problem statement?
- "You don't need 50 metrics. You need 3–5 that map to your problem statement."
- ~3 minutes. Framework, not lecture.

---

## Slide 5 | Lab 1: Connect Analytics (15 min)

- Students set up tracking on their deployed products
- Step 1: Review Lovable insights — screenshot baseline metrics
- Step 2: Set up GA4 — create property, get Measurement ID, prompt Lovable to add the tag, redeploy
- Step 3: Verify — see themselves as a live user in real-time view
- **If GA4 setup takes too long:** Lovable insights alone is enough for the analysis sprint
- Walk the room. Most deployments take one prompt. The "aha" is seeing themselves in the real-time view.

---

## Slide 6 | Teaching: AI-Powered Product Analysis

- Traditional analysis: export → spreadsheet → charts → doc → days
- AI-powered analysis: metrics + problem statement + AI → evaluation in minutes
- The formula: pull metrics + pull problem statement + pull hypothesis → feed to ChatGPT/Gemini
- "The AI doesn't replace your judgment. It accelerates your analysis."
- ~5 minutes. The demo next makes it concrete.

---

## Slide 7 | Demo: AI Analysis in Action

- Live demo: pull Retention Engine metrics, copy problem statement from Living PRD, paste both into ChatGPT
- Show the AI evaluating whether the hypothesis is confirmed
- Show patterns it surfaces, improvements it recommends
- "That analysis would take a product team a day. You just did it in 2 minutes."
- **THIS IS BEAT 2.** The speed and quality of the AI analysis is the wow. Let them see it happen in real-time.
- ~5 minutes.

---

## Slide 8 | Lab 2: AI Analysis Sprint (15 min)

- Students pull their metrics, problem statement, and hypothesis
- Feed all three to ChatGPT/Gemini using the provided prompt template
- Read the AI's analysis. Highlight the single highest-impact recommendation.
- **Key instructor behavior:** Walk the room. The "aha" moments happen when AI tells them something they didn't expect about their own product.
- After 15 min: "What did AI tell you? Anyone surprised by what it found?" Get 2–3 students to share.

---

## Slide 9 | Teaching: The Iteration Prompt

- Evidence-based vs. guess-based iteration
- The iteration prompt pattern: "Based on this analysis: [findings]. The highest-impact improvement is: [specific]. Update the product to address this."
- Different from M1–M5 prompts: not building new features, improving existing ones based on evidence
- Spotify's "tweak it" — the fifth stage: understand it, think it, build it, ship it, tweak it
- ~5 minutes.

---

## Slide 10 | Lab 3: Build One Improvement (10 min)

- Pick the single highest-impact finding from AI analysis
- Write the iteration prompt. Paste into Lovable. Review changes. Redeploy.
- "You just completed the full product lifecycle: understand → hypothesize → build → ship → measure → learn → improve."
- **Key guidance:** Resist the temptation to fix everything. ONE change. The discipline of prioritization is the skill.
- After 10 min: "Who redeployed? What did you change and why?" Every answer should reference the data.

---

## Slide 11 | Quick Polish (5 min)

- Compressed checklist: page title, favicon, mobile responsive, no placeholder text, live URL works
- One prompt per fix. Redeploy after.
- "Your classmates are about to use your product."
- Don't let anyone start new features. Just clean up.

---

## Slide 12 | Gallery Walk Setup (20 min)

- Post live URLs in Slack
- Open 4–5 classmates' products as a real user
- Sign up, try the core flow, try to break it
- Feedback: one thing that impressed you, one thing that confused you
- "These products have been measured and improved with real data. Can you tell?"

---

## Slide 13 | Gallery Walk Debrief

- "Which product felt the most real? What made it feel that way?"
- "Could you tell which products had been improved based on data?"
- Key insight: "The difference between M5 and M6 — M5 products work. M6 products learn."
- ~5 minutes. Transition to presentations.

---

## Slide 14 | Presentation Format

- 5 minutes each. Strict time. No slides — product is the presentation.
- Structure: Problem → Hypothesis → Live Demo → What the Data Told You → The Journey (M1 vs M6)
- **New element:** "What the Data Told You" — this is the M6 differentiator. Not just what they built, but what they learned and improved.
- If 20 students, select 6–8 to present live. Others post Loom walkthroughs in Slack.

---

## Slide 15 | Presentations Begin (30 min)

- Call presenters by name
- After each: 1–2 audience questions
- Encourage reactions in chat (fire emoji, "one thing I'd steal")
- Keep energy celebratory — this is the culmination of the course

---

## Slide 16 | Six-Tab Reveal

- Same pattern as M5's five-tab reveal — now six
- M6 tab: "Measured. Analyzed with AI. Improved based on evidence. A product that learns."
- 30 seconds of silence. Let them look.
- "In Module 1, you typed one prompt and got a page. In Module 6, you used AI to analyze your deployed product's data and made an evidence-based improvement. That's product management."

---

## Slide 17 | Complete Deliverables

- Name everything they built across six modules
- New additions: analytics setup, data-driven improvement, presentation backed by real data
- "If you walked into a stakeholder meeting with this package — deployed product, analytics, data-driven improvement — that's more convincing than most quarterly reviews."

---

## Slide 18 | The Confidence Line (Complete)

- M1: Speed → M2: Validation → M3: Precision → M4: Structure → M5: Ship → M6: Product
- "The entire arc: from 'I wonder if AI can build things' to 'I just shipped, measured, and improved a product.'"
- M6 adds the final layer: product confidence. Not just building — learning.

---

## Slide 19 | Certification + What's Next + Close

- Certification is complete. Celebrate.
- Three paths: ship to real users (with analytics), hand off to engineering (with data), start your next product (with your prompt pack)
- "Keep building. Keep shipping. Keep learning."
- Share digital certificates if available. This is the moment.

---

## Slide 20 | Survey

- Standard end-of-module survey
- QR code or link

---

## Tools

- **Lovable Insights** — built-in analytics for deployed Lovable projects. Used DURING Lab 1 (slide 5) for baseline metrics.
- **Google Analytics (GA4)** — industry-standard tracking. Set up DURING Lab 1 (slide 5). Free. One prompt to add the tag.
- **ChatGPT / Gemini** — used DURING Lab 2 (slide 8) for AI-powered product analysis. Students feed metrics + problem statement + hypothesis.
- **Living PRD Extractor** (from M4) — students pull their problem statement and hypothesis for the analysis prompt.
- **Living Prompt Pack Builder** (from M3) — continues growing. Students add analytics and iteration prompts.
- Together: ship → measure → analyze → improve → present

---

## Timing (fits in 2.5 hours)

| Block | Slides | Duration |
|-------|--------|----------|
| Opening | 1–2 | ~5 min |
| Analytics Demo | 3–4 | ~8 min |
| Lab 1: Connect Analytics | 5 | ~15 min |
| AI Analysis Teaching + Demo | 6–7 | ~10 min |
| Lab 2: AI Analysis Sprint | 8 | ~15 min |
| Iteration Prompt Teaching | 9 | ~5 min |
| Lab 3: Build One Improvement | 10 | ~10 min |
| Quick Polish | 11 | ~5 min |
| Gallery Walk | 12–13 | ~25 min |
| Presentations | 14–15 | ~30 min |
| Wrap (Six-Tab, Deliverables, Cert) | 16–20 | ~12 min |
| **Total** | | **~140 min** |

Hands-on ratio: ~56% (three labs + gallery walk + presentations)
If tight: compress Lab 1 to 10 min and polish to 3 min → saves 7 min.

---

## How It Addresses Carlos/Neha Feedback (Mar 10 Meeting)

- **"Move deploy into M5"** → Done. Students already deployed in M5. M6 starts with a live product.
- **"M6 should be the most advanced module"** → It is. AI-powered product analysis is the most sophisticated PM skill in the course. Not building — analyzing and improving.
- **"Close the product lifecycle"** → Spotify's five stages: understand it, think it, build it, ship it, tweak it. M6 is "tweak it."
- **"Keep gallery walk and presentations"** → Preserved. Same format, but now students present what the data told them.
- **"Make the data real"** → Students set up actual analytics on their deployed products. Real data, real analysis, real improvement.
- **"Every module should have a wow moment"** → Beat 1: seeing real usage data. Beat 2: AI analysis in 2 minutes. Both happen in students' hands.
