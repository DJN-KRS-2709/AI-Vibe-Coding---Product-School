# Module 6: Ship It — Speaker Notes for Carlos

> For Carlos only. High-level bullets explaining what we're doing and why.
> Slide numbers match the Gamma Prompt (slides 1–20). Update if Gamma reorders.

---

## Where M6 Sits

- M1 = speed, M2 = aim, M3 = precision, M4 = structure, M5 = integration, **M6 = ship**
- The finish line of the entire course: students deploy and present a working product
- Students go from owning a working product → owning a **deployed, public, presentable product**
- The two halves converge: exploration (M1–M3) produced the concept, production (M4–M5) made it real, M6 puts it in front of people
- This is what separates this course from every other AI course: students leave with a shipped product, not a certificate about concepts

---

## The M6 Wow (Three Beats + Crescendo)

- **Beat 1 (deployment):** Student clicks Deploy. Opens their product on their phone. It works. "That's your product. On your phone. With a real URL." First time most PMs have ever deployed anything.
- **Beat 2 (gallery walk):** Students sign up on each other's products. Real sign-ups, real data, real usage. "Someone you've never met just created an account on YOUR product." The social proof moment.
- **Beat 3 (six-tab reveal):** M1 → M6 side by side. One prompt in M1, a deployed multi-user product in M6. The visual arc of the entire course.
- **Crescendo (presentations):** Students pitch their live product. No slides — the product IS the presentation. The M1 vs M6 comparison is the most powerful moment: same scenario, six modules of growth.

---

## What M6 Is NOT

- NOT a lecture module — minimal teaching, maximum doing and showing
- NOT about learning new tools — they know Lovable, Supabase, GitHub
- NOT about building new features — the product is done from M5
- It IS about: deploying, polishing details, experiencing each other's work, and presenting
- Think of it as a launch event, not a class session

---

## Module Flow and Timing

| Time | Duration | Activity |
|------|----------|----------|
| 0:00 | 5 min | **Slide 1–2:** Title + Bridge. Name the gap (works but nobody can access it) |
| 0:05 | 5 min | **Slide 3–5:** Demo: deploy in one click. Show on phone. Custom domains. |
| 0:10 | 15 min | **Slide 6:** Lab Part 1 — Students deploy. Test on phone. Share URLs. |
| 0:25 | 5 min | **Slide 7–8:** Polish checklist + sprint intro |
| 0:30 | 15 min | **Slide 8:** Lab Part 2 — Polish sprint. Favicon, title, mobile, meta tags. |
| 0:45 | 5 min | **Slide 9:** Gallery walk setup |
| 0:50 | 20 min | **Slide 9:** Gallery walk — students use each other's products |
| 1:10 | 5 min | **Slide 10:** Gallery walk debrief |
| 1:15 | 5 min | **Slide 11:** Presentation format |
| 1:20 | 30 min | **Slide 12:** Presentations — 5 min each, 6 presenters |
| 1:50 | 10 min | **Slides 13–19:** Six-tab reveal, deliverables, confidence line, certification, close |

---

## Slide-by-Slide Notes

### Slide 1–2 | Title + Bridge

- Same pattern as M1–M5: three waypoints on slide 1 (deploy, polish, present)
- Bridge: "Your M5 product works. But only you can access it."
- Name the gap: it's inside Lovable's preview, not a real URL
- Energy should be: "We're at the finish line. Let's ship."

---

### Slide 3–5 | Demo: Deploy

- **This is the easiest demo in the course.** One click. 30 seconds. Live URL.
- Show it on your phone. Drop the link in Zoom chat / Slack. Students open it live.
- "Click it. You're using my product right now."
- Don't over-explain infrastructure (CDN, hosting, etc.) — 2 minutes max on Slide 4
- Custom domains (Slide 5) — mention, don't demo. 1 minute.

---

### Slide 6 | Lab Part 1: Deploy (15 min)

- Students deploy their M5 product
- **THE WOW MOMENT:** Student opens their product on their phone and it works
- Common deployment issue: Supabase auth redirect URL doesn't include the new deployment domain — help students update it in Supabase settings
- After deploy: students share URLs in Slack. "Who's live? Drop your URL."
- Walk the room (virtual or physical). Watch for reactions when products go live.

---

### Slides 7–8 | Polish Sprint (15 min)

- Quick checklist: favicon, page title, mobile responsiveness, empty states
- These are fast fixes — 1 prompt each in Lovable
- Students redeploy after each fix (instant update)
- Prioritize: page title/favicon → mobile → empty states
- Don't let polishing eat into gallery walk time. Strict 15 min.

---

### Slides 9–10 | Gallery Walk (20 min)

- **This is the most unique exercise in the course**
- Students open 4–5 classmates' live URLs
- They sign up with real emails, try the core flow, try to break it
- Feedback in Slack: "One thing that impressed me. One thing that confused me."
- For online: everyone opens products in their own browser. Monitor Slack for reactions.
- Debrief: "What surprised you?" → Usually: "I was surprised how real it felt"
- Transition: "You've used each other's products. Now let's hear the stories."

---

### Slides 11–12 | Presentations (30–40 min)

- 5-minute pitch format: Problem → Hypothesis → Live Demo → What I Learned → The Journey (M1 vs M6)
- No slides required — the product IS the presentation
- **The M1 vs M6 side-by-side is the most powerful moment.** Same scenario, six modules of growth.
- If 20+ students: select 6–8 to present live. Others post 2-minute Loom walkthroughs in Slack.
- Audience engagement: fire emoji in chat, "one thing I'd steal," one PM question
- Be strict on time (5 min). It forces clarity.
- Applaud after each one. This is the celebration.

---

### Slide 13 | Six-Tab Reveal

- The final progression reveal: M1 through M6 side by side
- If students saved all versions: have them open all six tabs
- 30 seconds of silence. Let them look.
- "In Module 1, you typed one prompt and got a page. In Module 6, you deployed a multi-user product with a live URL that anyone in the world can access."
- This is the emotional peak. Don't rush.

---

### Slides 14–15 | Deliverables + Confidence Line

- Name the complete package: deployed product, Living PRD, GitHub repo, handoff note, prompt pack, presentation
- "This is a product portfolio, not a course artifact"
- Confidence line: speed → validation → precision → structure → integration → ship
- "From 'I wonder if AI can build things' to 'I just shipped a product.'"

---

### Slides 16–19 | What's Next + Certification + Close

- Three paths: ship to real users, hand off to engineering, start your next product
- Certification: celebrate. If digital certificates exist, share them now.
- Final accountability: verify URL, finalize handoff note, export prompt pack, post final build
- Close: "You came in wondering if AI tools were real. You're leaving with a deployed product."
- If energy allows: invite one student for a final reflection. Keep it short. End high.

---

## Tools

- **No new tools for M6** — students use Lovable (deploy), Supabase (verify), and GitHub (verify)
- The M5 Integration Planner's handoff section is used to finalize the Engineering Handoff Note
- The Living Prompt Pack (from M3 onward) gets its final export
- Lab Guide provides the step-by-step deployment and polish instructions

---

## How This Addresses Carlos's Feedback

| Carlos's Point | How M6 Handles It |
|---|---|
| "Will use some of the time to ship and then some of the time for Demos" | First 45 min = deploy + polish. Remaining 75 min = gallery walk + presentations + wrap |
| "Make sure instructors know they have to demo" | Demo is the simplest in the course: one click deploy. Speaker notes are explicit about live demo. |
| "Students appreciate knowing exactly how to replicate" | Lab guide + polish checklist + presentation format — all step-by-step |
| "Consider fireworks" | Gallery walk (using each other's products), six-tab reveal (visual arc), certification moment, celebratory design notes for Gamma |
| "This is real / deployment into production" | Entire module is about making it publicly accessible. "This is not a prototype anymore." |
| "Consistency for instructors" | Pre-built prototype available as backup. Deployment demo is one click — minimal risk of failure. |
