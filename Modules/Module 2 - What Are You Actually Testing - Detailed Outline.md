# Module 2: The Validation Lens — Build Smart, Not Just Fast

## Detailed Session Plan (2 Hours)

---

## Module Overview

| Field | Value |
| --- | --- |
| **Duration** | 120 minutes |
| **Confidence Line Position** | Still left. High ambiguity, but now with methodology + context. |
| **Core Principle** | Speed without direction is a liability. Build with constraints, context, and intent. |
| **Tool** | Lovable (Pro accounts). Gemini/ChatGPT for prompt planning. Mobbin for design references. |
| **Pre-requisite** | Module 1 complete. Students have built 2 prototypes and experienced the full cycle. |
| **What students walk out with** | A committed scenario, a Validation Brief, a Context Data Pack, and a prototype that is *visibly, meaningfully better* than what they built in M1 — because it was built with real user feedback, real data, and a real design reference. |
| **The Wow Moment** | M1 vs M2 side-by-side comparison. Students see the leap from "generic app from a vague prompt" to "contextual prototype that looks like a real product and tests a specific hypothesis." |

### The Energy Contract

Module 1 was fireworks — "I just built an app." Module 2 must maintain that energy while adding discipline. The trap: death by methodology. Carlos's feedback (Feb 20): "The problem framework is slow. It felt like another theory block with a bunch of things I already know. I'm leaving my Module 2 not excited."

**The fix:** Lead with action, not theory. The session opens with a live demo that shows what's possible (screenshot → prototype in one prompt). The methodology is compressed to ~6 minutes and taught through examples, not abstractions. The wow comes from students' OWN work — when they compare what they built in M1 to what they build here, the leap is visceral.

**Core principle (established Feb 20):** Every module must have a wow moment. Not just M1. Every session.

**Three things students walk away with (primed at opening, breadcrumbs throughout, reinforced at close):**
1. **A constraint toolkit** — how to frame what you're testing and why
2. **A context injection skill** — how to go from blank canvas to "this looks like my actual product"
3. **A prototype that's meaningfully better than M1** — higher fidelity, contextually relevant, designed to answer a specific question

### Terminology (consistent across all Product School courses)
- **Demo** = instructor building live
- **Hands-on lab** = students building in the tool
- **Breakout group activity** = students working in groups (e.g., swapping prototypes, peer review)

---

## Minute-by-Minute Breakdown

---

### Block 1: The Hook — You'll Never Start From Scratch Again (0:00 - 0:18)

---

#### 0:00 - 0:03 | Title + 3 Waypoints + Bridge from M1 (3 min)

**What happens:** Quick title, name the three things students will learn, bridge from M1.

**Instructor script:**

> "Module 1: you built fast. You proved you can go from nothing to a working prototype. That was fireworks. Today, three things change.
>
> One — you get a constraint toolkit. Before you touch any tool, you'll name what you're testing and why. Two — you learn context injection. You'll never start from a blank page again. Three — you'll build something that is visibly, meaningfully better than what you built last session. By the end, you'll compare the two side by side and see the difference.
>
> One more thing: this course operates in the solution space. We're not teaching you how to find the right problem — that's product strategy. We're teaching you how to test solutions faster. Everything from here assumes you've got a problem worth solving. We give you the tools to validate your proposed solution."

**Slide content:** "The Validation Lens" | MODULE 2 | Three things today: Constraints. Context. Build.

---

#### 0:03 - 0:11 | Instructor Demo: Never Start From Scratch (8 min)

**What happens:** The first energy peak. Before any methodology, show students what's possible. This is the "wake people up" moment Carlos asked for.

**Demo flow:**

1. **Text-to-App (baseline)** — Instructor shows a simple text prompt: "Build me a dashboard for tracking customer retention." Result: generic, placeholder-heavy, looks like every other AI demo. ~1 min.

2. **Screenshot-to-App (the magic)** — Instructor takes a screenshot of a real SaaS product (e.g., Linear, Mixpanel, or the students' scenario domain). Pastes it into Lovable alongside a structured prompt: "Match this look and feel. Build a retention dashboard that shows these 3 metrics: [specific numbers from the data pack]." Result: a prototype that looks like the real product, with real-looking data. ~3 min.

3. **Side-by-side comparison** — Show both results. "Same tool, same session. The only difference is context. One looks like a demo. The other looks like something you'd present to your VP." ~1 min.

4. **Three entry points (quick overview)** — Text-to-App (new concepts, no existing design). Screenshot-to-App (existing products, competitors, Mobbin inspiration). Design-to-Code (Figma imports — mention that Figma just announced a code-to-design partnership, the boundary is dissolving both ways). ~2 min.

5. **The promise:** "By the end of this session, you'll do exactly this — but with YOUR scenario, YOUR data, and YOUR design context." ~1 min.

**Instructor notes:**
- Pre-build both prototypes before class. Deliver them as if live, but have them ready as backup.
- The screenshot used should match one of the four course scenarios so students see direct relevance.
- This demo replaces the old "Bridging Design and Build" slide (which was buried late in the deck). Same content, moved to where it creates maximum impact.

---

#### 0:11 - 0:18 | Choose Your Scenario — The Commitment Moment (7 min)

**What happens:** Students pick the scenario they'll carry through M2-M6. This is their final project starting point.

**Instructor script:**

> "Time to commit. You're picking the scenario you'll build on for the rest of this course. Everything you do from today forward layers onto this product. No switching after today.
>
> Four options, plus bring your own:
>
> **Scenario 1 — The Retention Engine:** B2B SaaS losing 30% of customers in 90 days. Users sign up, poke around, and ghost. The data says team invites matter. What's the real blocker?
>
> **Scenario 2 — The Internal Tool Nobody Uses:** CRM with 18% adoption. Sales reps hate it. The CEO wants to buy Gong. Can you fix adoption without replacing the tool?
>
> **Scenario 3 — The Marketplace Trust Problem:** Bookings flat. Zero-review providers can't get their first customer. How do you solve cold-start trust?
>
> **Scenario 4 — The Dashboard Nobody Reads:** Analytics dashboard with 60% bounce rate. Power users love it, new users flee. How do you serve both?
>
> **Bring Your Own:** A real problem from your company. Requirements: a clear user, a measurable outcome, and enough ambiguity to test.
>
> Quick note: this is a product exercise, not a startup pitch. You're building to test a hypothesis, not to launch a business. Pick the one closest to your real work. Post your choice in Slack now — you have 2 minutes."

**What the instructor does:**
- Read the room. If most students are undecided after 90 seconds, give a nudge: "If you can't decide, pick Scenario 1 or 4 — they work for almost any PM role."
- Watch for students picking "Bring Your Own" — check in Slack that their problem has a clear user and measurable outcome, not just "make our product better."

---

### Block 2: The Constraint Toolkit — Lean Methodology (0:18 - 0:30)

**Design principle:** Carlos said the problem framework felt like "another theory block." The fix: 12 minutes total for ALL methodology, taught through examples and interaction, not slides of bullet points.

---

#### 0:18 - 0:20 | The Problem Framework — Example-Based (2 min)

**What happens:** 90-second intro to the 6-element frame. Shown as a filled-out example, not in the abstract.

**Instructor script:**

> "Before you build, you frame. Six elements — I'll show you a filled-out example for the Retention Engine scenario.
>
> Goal: reduce 90-day churn from 30% to 15%. Problem: users don't invite teammates, and solo users churn at 3x the rate. Context: B2B PM tool, 5K teams, Series A. Constraints: no engineering for 6 weeks, must work within the existing product. Success criteria: validated if the invite flow increases Day-3 invite rate from 12% to 25%. Explore: we're trying to learn whether the blocker is discoverability (can't find the invite button) or motivation (don't see the value of inviting).
>
> That last element — Explore — is the key. Most PM frameworks stop at 'what are we building.' This one asks 'what are we LEARNING.' You'll fill this out for YOUR scenario in the lab."

**Slide content:** The 6-element Problem Frame with one filled-out example. Clean, one slide.

---

#### 0:20 - 0:22 | Risk Types + Kill Switch — Combined (2 min)

**What happens:** Three risk types, then the kill-switch question. Chat interaction.

**Instructor script:**

> "Your riskiest assumption falls into one of three categories:
>
> Value — will anyone actually want this? Usability — will the experience make sense? Feasibility — will the logic actually work?
>
> Here's why this matters: your risk type determines what you build. Value risk? A landing page tests that faster than a full app. Usability risk? You need a clickable flow. Feasibility risk? You need working logic.
>
> Now the kill switch: which assumption, if wrong, kills the whole thing? For the Retention Engine: if users don't actually want to collaborate — if the tool is fundamentally a solo tool — then nothing we build around invites will matter. That's the kill switch.
>
> Type in chat: what's YOUR risk type? Value, usability, or feasibility?"

**Slide content:** Three risk categories with fidelity mapping. One slide.

---

#### 0:22 - 0:24 | The Validation Loop + Template Handout (2 min)

**What happens:** Introduce the 4-step loop and hand out the Validation Brief.

**Instructor script:**

> "Here's the cycle you'll run in every lab from now on: Identify the hypothesis. Define the constraints. Build and stress-test — meaning intentionally find where it breaks. Synthesize and pivot — use what you learned to update the hypothesis.
>
> Step 3 is the key shift from M1: you're not building to see it work. You're building to see where it BREAKS.
>
> I'm dropping a Validation Brief template in Slack right now. It combines the problem frame, your risk type, your kill switch, and a space for your first prompt. Fill this out in Lab 1."

**Slide content:** The 4-step validation loop. One slide. Validation Brief template linked in Slack.

---

#### 0:24 - 0:27 | Prompt Anatomy — Tool Configuration (3 min)

**What happens:** Four elements of a good prompt. Quick — students will apply this immediately in the lab.

**Instructor script:**

> "Last thing before we build. Four elements that turn a vague prompt into a useful one:
>
> Context — what's the product, who's it for? Don't say 'build me a dashboard.' Say 'Build a customer retention dashboard for a B2B PM tool used by 5K teams.'
>
> Reference — a visual anchor. That screenshot you'll grab from Mobbin or your own product? This is where it goes. Show, don't describe.
>
> Constraint — the guardrails. 'Prioritize the team invite flow. Avoid generic dashboard patterns. Keep it to 3 screens.'
>
> Output — what exactly should the tool produce? 'A 3-screen flow: invite prompt on first login, team setup wizard, and a collaborative task view.'
>
> Think of this as configuring a builder tool, not chatting with an AI. The more specific your configuration, the better the output."

**Slide content:** Prompt Anatomy — Context / Reference / Constraint / Output. One slide.

---

#### 0:27 - 0:30 | Context Data Packs + Lab Instructions (3 min)

**What happens:** This is what makes M2 different from M1. Introduce the data packs, show what's inside, set up the lab.

**Instructor script:**

> "Here's what makes today fundamentally different from Module 1. In M1, you opened Lovable with nothing — a vague prompt, no data, no design reference. Today, you open it with four things:
>
> One — your Validation Brief. The hypothesis, the constraints, what 'validated' looks like. Two — a visual reference. A screenshot from Mobbin, your own product, or a competitor. Three — a Context Data Pack. And four — a structured prompt using the anatomy we just covered.
>
> Let me show you what's in the Context Data Pack. [Shows on screen.] For each scenario, you're getting three files: First, user and stakeholder feedback — 8 to 12 real-sounding quotes from interviews, surveys, and support tickets. Your users are talking. Second, a metrics CSV — 15 to 20 rows of fictional but realistic quantitative data. Retention curves, adoption rates, conversion funnels. Real numbers, not placeholder text. Third, a scenario brief — the full problem context with competing stakeholder hypotheses.
>
> For those on the 'Bring Your Own' track — you have a template in Slack to structure your own context. Gather 5-8 user quotes, pull 5-10 real metrics from your product, and write a one-paragraph problem brief. Same format, your data.
>
> When you build your prompt, you'll paste actual user quotes and reference actual metrics. Your prototype will show real data and real user voice — not lorem ipsum. That's the difference you'll see.
>
> Credits reminder from M1: plan your prompt in Gemini or ChatGPT first, paste into Lovable when ready, fix small things in code. If a prompt fails twice, eject to ChatGPT — don't burn credits debugging.
>
> Ready? Let's go."

---

### Block 3: The Labs — Build With Intent (0:30 - 1:17)

---

#### 0:30 - 0:42 | Hands-on Lab Part 1: Frame + Gather Context (12 min)

**Purpose:** Students prepare EVERYTHING they need before touching Lovable. The discipline M1 didn't require — and the context that makes M2's output dramatically better.

**Lab Brief (displayed + Slack):**

> **Lab Part 1: Frame + Gather Context** | 12 Minutes
>
> Do NOT open Lovable yet. You're preparing the inputs that will make your build dramatically better than M1.
>
> **Step 1 (5 min) — Fill out your Validation Brief:**
> - Which scenario did you choose?
> - What's the riskiest assumption you're testing?
> - What risk type? (Value / Usability / Feasibility)
> - What's the kill switch — what assumption, if wrong, kills the whole thing?
> - What does "validated" vs. "invalidated" look like?
> - What fidelity do you need? (Landing page / Clickable flow / Functional app)
>
> **Step 2 (4 min) — Read your Context Data Pack:**
> - Download your scenario's data pack from the shared folder (link in Slack)
> - *Bring Your Own track:* Download the blank template and fill in your own data
> - Read the user/stakeholder quotes. **Highlight 2-3** that directly relate to your hypothesis.
> - Scan the metrics CSV. **Circle 3-5 data points** you want your prototype to display or reference.
>
> **Step 3 (3 min) — Find your visual reference:**
> - Go to Mobbin (free) and find a screen that looks like what you're building. OR screenshot your own product / a competitor.
> - Drop the screenshot in Slack alongside your Validation Brief.
>
> **Post in Slack when done:** "Scenario: ___. Testing: ___. Risk type: ___. [Screenshot + highlighted quotes/metrics attached]"

**What the instructor does:**
- Circulates. Checks for two failure modes:
  1. Students who skip the data pack and just write a generic brief (redirect: "Open the feedback file. Which quotes relate to your hypothesis?")
  2. Students who try to include ALL the data (redirect: "Pick the 3-5 data points that matter most for your specific hypothesis")
- At 5 min: "You should have your Validation Brief done. If you're stuck on the assumption, ask: what would kill this idea if we learned it was wrong?"
- At 9 min: "You should have a screenshot and highlighted quotes. 3 minutes to post in Slack."
- At 12 min: "Time. Open Lovable. Let's build."

---

#### 0:42 - 1:07 | Hands-on Lab Part 2: Build With Context — THE WOW (25 min)

**Purpose:** THE centerpiece. Students build with all four inputs. The output is dramatically different from M1.

**Lab Brief (continued):**

> **Lab Part 2: Build With Context** | 25 Minutes
>
> Open Lovable. You have everything you need:
>
> 1. Your **Validation Brief** — the hypothesis, constraints, and success criteria
> 2. Your **visual reference** — the screenshot from Mobbin or your own product
> 3. Your **Context Data Pack** — user quotes and metrics
> 4. Your **prompt** — structured using Context / Reference / Constraint / Output
>
> **Build your prompt like this:**
>
> *Context:* Paste your scenario brief. Include 2-3 user quotes: "Here's what users are saying: [quote 1], [quote 2]."
>
> *Reference:* Attach your screenshot. "Match this look and feel."
>
> *Constraint:* "Display these specific metrics: [metric 1], [metric 2], [metric 3]. Use these actual numbers, not placeholder data."
>
> *Output:* "Build a [2-3 screen] flow that tests whether [your hypothesis]. Include: [screen 1], [screen 2], [screen 3]."
>
> **Your goal is NOT to build something pretty.** Your goal is to build something that:
> - Looks like a real product in your domain (because of the screenshot reference)
> - Shows real data (because of the metrics CSV)
> - Tests your specific hypothesis (because of the Validation Brief)
>
> **Produce:** A shareable prototype link. Verify the link works — you're swapping with a partner in 25 minutes.

**What the instructor does:**
- Circulates. Watches for:
  1. Students prompting generically without using the data pack (redirect: "Where are the user quotes in your prompt? Where's the data?")
  2. Students building something pretty that doesn't test their hypothesis (redirect: "What assumption does this test? How would you know if it's validated?")
  3. Students who got a strong first result and are refining aesthetics (redirect: "Good start. Now stress-test it — go to the edge case. What happens when the data is empty? When the user does something unexpected?")
- At 12 min: "You should have at least one working direction. If you're building a second, make it fundamentally different — different architecture, not different colors."
- At 20 min: "5 minutes. Verify your shareable link works. Copy it to Slack."
- At 24 min: "1 minute. Whatever you have is enough. Share the link."

---

#### 1:07 - 1:17 | Breakout Group Activity: Does This Test It? (10 min)

**Purpose:** Peer validation. The critical question isn't "is this cool?" — it's "does this test what you said you were testing?"

**How it works:**
- New breakout rooms, groups of 2. Random assignment. ("Press the button." — Carlos)
- Person A shares their Validation Brief + prototype link in chat.
- 3 minutes of complete silence — Person B explores the prototype cold, no explanation, like a real user.
- Then discuss (4 min per pair):

**Feedback questions:**
- Does this prototype actually test the stated hypothesis? Or is it just a demo?
- Where does the experience break when you go beyond the happy path?
- Can you see the real user data in here? Does it make the prototype feel more credible?
- Tool vs. Toy: would this help the builder make a decision, or does it just look good?

**Instructor script (before breakout):**

> "The question isn't 'is this cool?' It's 'does this test what you said you were testing?' Your partner has fresh eyes — they'll see what you can't. Be honest. If they built something impressive that proves nothing, say so. That's the valuable feedback."

---

### Block 4: The Reveal — M1 vs M2 (1:17 - 1:30)

**Design principle:** This is the wow moment made visible. Students see their own improvement. Not the instructor telling them they improved — them SEEING it.

---

#### 1:17 - 1:25 | Side-by-Side: Your M1 Build vs Your M2 Build (8 min)

**What happens:** 2-3 volunteers show their M1 prototype alongside their M2 prototype. Full class discussion.

**Instructor script:**

> "I need 2-3 volunteers. Pull up what you built in Module 1 and what you built today. We're going to look at them side by side.
>
> [Volunteer shares both screens.]
>
> Look at the difference. Same tool. Same student. Same amount of time. What changed?
>
> [Class discussion. Instructor guides toward the three waypoints:]
>
> The M1 build started from a blank page and a vague prompt. It looks generic — placeholder text, default layout, no real data.
>
> The M2 build started from a hypothesis, a screenshot, user feedback, and real metrics. It looks like a product someone actually works on. The data is real. The design matches the domain. And it was designed to answer a specific question.
>
> That's the validation lens. Constraints plus context plus intent. Three inputs that transform what comes out."

**What the instructor watches for:**
- Volunteers who represent different scenarios (don't pick three Retention Engines)
- The moment when the class visually registers the improvement — that's the energy peak
- Students who built something impressive in M2 but can't articulate what it tests — use that as a teaching moment: "Beautiful build. What question does it answer?"

---

#### 1:25 - 1:28 | Pulse Check: Production-Readiness Score (3 min)

**Format:** Slack poll. 1-5 with one sentence "why."

> "Rate your M2 prototype. 1 = just a sketch. 5 = I'd show this to my VP tomorrow. Post your number and one sentence explaining why in Slack."

Instructor reads 3-4 responses. Follows up on extremes — especially the 4s and 5s ("What specific upgrade made the difference?") and the 1s and 2s ("Was it the prompting? The tool? Or the hypothesis?").

---

#### 1:28 - 1:30 | Quick Share: What Did You Learn? (2 min)

> "Popcorn. One sentence: what assumption did you test, and what did you learn? Validated, invalidated, or still unclear."

Take 3-4 responses. Synthesize: "The best outcomes aren't always 'it worked.' Sometimes the best outcome is 'we learned it doesn't work — in 30 minutes, not 3 months.'"

---

### Block 5: Break + Close (1:30 - 1:50)

---

#### 1:30 - 1:35 | Break (5 min)

Standard break. Teaching and labs are done.

---

#### 1:35 - 1:40 | Key Takeaways — The Three Waypoints (5 min)

**Purpose:** Close the loop. Mirror the three things primed at the opening.

**Instructor script:**

> "Three things you did today — the same three I named at the start:
>
> One — you got a constraint toolkit. You filled out a Validation Brief: hypothesis, risk type, kill switch, success criteria. Every build from now on starts with a brief, not a blank prompt. That's the discipline.
>
> Two — you learned context injection. You took a screenshot, real user feedback, and real metrics, and you fed them into the tool. You will never start from a blank page again. That's the skill.
>
> Three — you built something meaningfully better than Module 1. Pull up both prototypes. Look at them. That leap didn't come from spending more time — it came from starting with better inputs. Constraints plus context plus intent.
>
> That's the validation lens. From this point forward, every prototype you build gets judged not by how it looks, but by what it validates."

---

#### 1:40 - 1:45 | Next Session Preview + Accountability (5 min)

**Instructor script:**

> "Before we go — post your M2 prototype in #builds. Caption: what assumption did you test? What did you learn? Not what you built — what you LEARNED. Then look at 2 others. Did their prototype actually test what they claimed?
>
> No homework. But here's an optional challenge: take your M2 prototype and rebuild it using a screenshot of your actual company's product. See how close you can get. Drop the before/after in Slack.
>
> Next session: Module 3 — Precision Prompting. Same product, better execution. Context layering, design system matching, documented prompt chains. You'll go from 'build me something' to 'build me exactly this.' See you then."

---

#### 1:45 - 1:50 | Q&A + Survey + Close (5 min)

Q&A, then Product School survey (QR code). Close.

---

## Session Summary

| Block | Time | Duration | Activity Type |
| --- | --- | --- | --- |
| Title + 3 Waypoints + M1 Bridge | 0:00 - 0:03 | 3 min | Instructor talk |
| **Instructor Demo: Never Start From Scratch** | **0:03 - 0:11** | **8 min** | **Instructor demo (live build)** |
| Choose Your Scenario | 0:11 - 0:18 | 7 min | Student commitment + Slack |
| Problem Framework (example-based) | 0:18 - 0:20 | 2 min | Instructor talk |
| Risk Types + Kill Switch | 0:20 - 0:22 | 2 min | Instructor talk + chat interaction |
| Validation Loop + Template Handout | 0:22 - 0:24 | 2 min | Instructor talk |
| Prompt Anatomy | 0:24 - 0:27 | 3 min | Instructor talk |
| Context Data Packs + Lab Instructions | 0:27 - 0:30 | 3 min | Instructor talk |
| **Lab 1: Frame + Gather Context** | **0:30 - 0:42** | **12 min** | **Hands-on lab (writing + research)** |
| **Lab 2: Build With Context (THE WOW)** | **0:42 - 1:07** | **25 min** | **Hands-on lab (building)** |
| **Peer Review: Does This Test It?** | **1:07 - 1:17** | **10 min** | **Breakout group activity** |
| **M1 vs M2 Reveal (Side-by-Side)** | **1:17 - 1:25** | **8 min** | **Class discussion + student showcase** |
| Pulse Check | 1:25 - 1:28 | 3 min | Slack + discussion |
| Quick Share | 1:28 - 1:30 | 2 min | Popcorn discussion |
| Break | 1:30 - 1:35 | 5 min | Break |
| Key Takeaways | 1:35 - 1:40 | 5 min | Instructor talk |
| Next Session + Accountability | 1:40 - 1:45 | 5 min | Instructor talk + Slack |
| Q&A + Survey + Close | 1:45 - 1:50 | 5 min | Q&A |

### Time Distribution

| Category | Minutes | Percentage |
| --- | --- | --- |
| **Students building (labs)** | 37 min | 34% |
| **Breakout / peer review** | 10 min | 9% |
| **Student showcase / reveal** | 8 min | 7% |
| **Instructor demo (live build)** | 8 min | 7% |
| **Instructor teaching** | 22 min | 20% |
| **Student commitment (scenario)** | 7 min | 6% |
| **Class discussion / pulse / share** | 5 min | 5% |
| **Wrap / preview / accountability** | 10 min | 9% |
| **Break** | 5 min | 5% |
| **Total hands-on (labs + peer + reveal)** | **55 min** | **50%** |

**Buffer:** 10 minutes remaining from 120. Recommendation: extend Lab 2 from 25 to 30 min if the room is energized and building. That brings hands-on to 55%.

**Compared to the previous version:**
| Metric | Old | New | Change |
|---|---|---|---|
| Teaching time | 47 min (39%) | 22 min (20%) | -25 min |
| Student building time | 25 min (21%) | 37 min (34%) | +12 min |
| Total hands-on | 45 min (38%) | 55 min (50%) | +10 min |
| Wow moment | None identified | M1 vs M2 reveal | NEW |

---

## Key Materials Needed

### Prepared Before Class

1. **"Never Start From Scratch" demo prototypes** — Pre-built: (A) generic text-only prompt result, (B) screenshot-injected result. Both for the same scenario. Have backup screenshots if live demo fails.
2. **Context Data Packs** — One per scenario + the Bring Your Own template. Distributed via Slack or shared folder at the start of Lab 1. (See `Module 2 - Context Data Packs.md` for full contents.)
3. **Validation Brief template** — Distributed via Slack at 0:22. One-page template: scenario, hypothesis, risk type, kill switch, success criteria, first prompt.
4. **Bring Your Own Context Template** — For students on the company track. Blank template mirroring the data pack structure. (See `Module 2 - Context Data Packs.md`.)
5. **Problem Framework slide** — 6 elements with one filled-out example (Retention Engine scenario). One slide, not three.
6. **Risk Types + Fidelity slide** — Three risk types → three fidelity levels. One slide.
7. **Validation Loop slide** — 4-step cycle. One slide.
8. **Prompt Anatomy slide** — Context / Reference / Constraint / Output. One slide.
9. **Scenario cards** — One slide with all 4 scenarios + Bring Your Own, with enough detail for students to choose.
10. **Mobbin tab open** — Pre-selected examples for each scenario: PM dashboards, CRM interfaces, marketplace profiles, analytics dashboards.
11. **Lab briefs** ready to paste in Slack

### Student Requirements

- Module 1 complete
- Lovable Pro account
- Slack access
- M1 prototype still accessible (for the side-by-side reveal)
- Optional: screenshot of their real product (for Bring Your Own track)

---

## Appendix: What Changed and Why

| What Changed | Why (Carlos Feedback, Feb 20) |
|---|---|
| "Never Start From Scratch" demo moved to opening | "Move it up. This will wake people up." — Carlos |
| Problem Framework cut from 15 min to 2 min | "It felt like another theory block with a bunch of things I already know." — Carlos |
| Context Data Packs added to labs | "How can you magically bring context in this session?" — Carlos |
| M1 vs M2 side-by-side reveal added | "If I can leave Module 2 with something that is just meaningfully better than what I built in Module 1 — I can see it." — Carlos |
| Credit strategy moved to M1 | "My suggestion would be to even put that in Module 1, so they don't learn too late." — Carlos |
| 3 waypoints threaded throughout | "If it's three things — boom, boom, boom — clarifying at the beginning and making sure those three points are easy to follow." — Carlos |
| Solution space clarification added | "Ultimately what we're building here is operating mostly on the solution space." — Carlos |
| Ice breaker removed | Replaced by the "Never Start From Scratch" live demo — a stronger energy peak |
| "Break It" exercise removed | The M1 vs M2 reveal achieves the same goal (fidelity ≠ value) through students' own work |
| Scenario selection moved earlier | Students need their scenario before the methodology makes sense |
