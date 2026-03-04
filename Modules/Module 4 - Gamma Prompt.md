# Gamma Prompt: Module 4 Teaching Slide Deck

**Copy everything below the line and paste it into Gamma. Use "Paste an outline" or the prompt field.**

---

## Instructions for Gamma

Create a professional slide deck for teaching a 2-hour workshop called **"Module 4: From Vibe to Structure — The Graduation Moment"** in a Vibe Coding certification course. The audience is senior product managers who completed Modules 1–3 — they can build fast (M1), build smart with data and hypotheses (M2), and build precise with multi-screen flows, states, and documented prompt chains (M3); now they're learning when to stop exploring and start building for real. Tone: energetic, practical, technical. The deck supports live teaching, demos, and hands-on labs. Avoid corporate jargon. Use clean, modern design with clear typography and minimal text per slide. Match Modules 1–3 visual style. Important: the slides are student-facing — keep the content instructional and practical. Do not telegraph emotional beats or name "wow moments" on slides.

---

## Slide 1 — Module 4 Title + 3 Waypoints
**From Vibe to Structure — The Graduation Moment**

MODULE 4 | VIBE CODING CERTIFICATION

Three things today:
1. **Living PRD** — Extracted from what you built, not written before building. Your prototype becomes the spec.
2. **Real Infrastructure** — GitHub repo and Supabase database. Your code is version-controlled and your data has a real home.
3. **Engineering Handoff** — The document that bridges PM prototype to engineering sprint.

Module 1 was speed. Module 2 was aim. Module 3 was precision. Module 4 is graduation.

*Speaker Notes: "Welcome back. You've built fast, built smart, and built precise. Your M3 prototype has 5+ screens, interactive states, and a documented prompt chain. It looks like a real product. But here's the thing — if you got hit by a bus tomorrow, could anyone pick up where you left off? No spec. No structured code. No version control. No backend. Today we fix all of that. Three waypoints: Living PRD, real infrastructure, engineering handoff. By the end of today, your prototype graduates — it has a spec, clean code in a GitHub repo, a Supabase database, and a handoff document an engineer can sprint from."*

---

## Slide 2 — Bridge from M3 + Agenda
**Your M3 Prototype Looks Real. Could Engineering Build From It?**

Your M3 build has multiple screens, interactive states, design-matched UI, and a documented prompt chain. If your VP saw it, they'd think engineering built it. But pull up the code — what would an engineer see?

- Component names like `Component1`, `handleClick2`
- Data logic tangled with display logic
- No documentation, no architecture, no spec
- No version control — one bad prompt and it's gone
- No backend — every data point is hardcoded

Today's flow:
1. **Demo** — Extract a spec. Refactor the code. Connect real infrastructure.
2. **Teaching** — Living PRDs, the graduation judgment, infrastructure for PMs
3. **Lab** — Graduate your M3 prototype: PRD, refactoring, GitHub, Supabase
4. **Peer Review** — Can your partner understand the product from just the PRD?
5. **Break It** — The prototype that never graduated

---

## Slide 3 — Instructor Demo: The Setup
**Your M3 Prototype. Let's Look Under the Hood.**

INSTRUCTOR DEMO

The M3 Retention Engine prototype:

- 5 screens with navigation — onboarding flow, team workspace, PM dashboard
- Interactive states — loading skeletons, error handling, empty states
- Refined PM dashboard with nudge button and interactive charts
- Design-matched to Asana
- Built with a documented 3-prompt chain

Now open the code view.

Names like `div1`, `Section3`, `handleSubmit2`. Data fetching mixed into UI components. No README. No structure. Not connected to anything. An engineer would need a week just to understand what this does.

*Speaker Notes: Pull up the M3 Retention Engine prototype in Lovable. Click through the screens — remind students how polished it is. Then switch to the code view. Let it sit for 10 seconds. Don't explain the mess — let them see it. "This is what your VP doesn't see. This is what the engineer who inherits it sees. Would you want to build from this?" Pause. "5 steps. Watch."*

---

## Slide 4 — Live Build: The Graduation Chain
**5 Steps to Graduate**

**Prompt 1 — Extract:** "Look at this entire prototype. Write a product requirements document that covers: what this product does, who it's for, the problem it solves, the 5 screens and their purpose, the user flow from first screen to last, the hypothesis it tests, the key metrics, what's currently mocked vs. what would need real data, and recommended next steps for engineering. Format it as a structured document with clear sections."

**Prompt 2 — Refactor:** "Refactor the codebase. Rename all components to be descriptive (e.g., OnboardingWelcome, TeamInviteForm, PMDashboard). Separate data logic from display components. Group files by feature, not by type. Add a README.md that explains the project structure, what each screen does, and how to run it."

**Prompt 3 — Handoff:** "Generate an engineering handoff document: list every component and what it does, describe the data model (what's real vs. mocked), identify the 3 biggest technical decisions an engineer would need to make, and write a 'start here' guide for a new engineer inheriting this project. Be specific, not generic."

**Step 4 — Connect GitHub:** Click "Connect GitHub" in the top right. One click. Your code now lives in a real repository with version history.

**Step 5 — Connect Supabase:** Click "Add Supabase" in the top right. One click. Your prototype now has a real database backend.

3 prompts + 2 clicks. A spec, structured code, version control, a database, and an engineering handoff.

*Speaker Notes: Run the 3 prompts sequentially — pre-type each. Prompt 1: paste, wait ~60 sec. Read the PRD aloud — hit the key sections. "I didn't write this. The prototype wrote its own spec." Prompt 2: paste, wait ~60 sec. Switch to code view. "Component1 is now OnboardingWelcome. There's a README." Prompt 3: paste, wait ~40 sec. Read the handoff highlights. Then the infrastructure — click Connect GitHub. "Open this URL. That's your code in a real repo. Every change, every version, tracked." Click Add Supabase. "Your prototype now has a database. This isn't a toy anymore." Total: ~8 minutes. The GitHub and Supabase clicks are the moment the room shifts — it goes from documentation exercise to "this is real infrastructure."*

---

## Slide 5 — Demo Debrief
**What Changed**

Same prototype. Same 5 screens. Same states.

- **Living PRD extracted** — a complete spec, generated from the build. Not imagined before building — extracted after.
- **Code refactored** — descriptive names, separated concerns, README. An engineer can read it on day one.
- **GitHub connected** — real version control. Every change tracked. Rollback if something breaks.
- **Supabase connected** — real database infrastructure. Your data has a real home.
- **Engineering handoff** — component map, data model, technical decisions, start-here guide.

Traditional PM workflow: Research → Spec → Build → Test.
Vibe Coding workflow: Build → Test → Extract spec → Connect infrastructure. The spec is the output, not the starting point. The infrastructure follows the prototype, not the other way around.

*Speaker Notes: Land the paradigm shift explicitly. "In traditional PM, you write the spec BEFORE you build. You spend 2 weeks on a PRD that describes something that doesn't exist yet. In Vibe Coding, you build first, test the hypothesis, and THEN extract the spec and connect the infrastructure. The spec isn't imagined — it's grounded in a working prototype. And that prototype now has real version control and a real database." Pause. "You'll do this yourself in 30 minutes."*

---

## Slide 6 — Mini Activity: Look at Your Code
**Open Your M3 Prototype's Code View**

INDIVIDUAL EXERCISE | 5 MINUTES

Open Lovable. Switch to code view on your M3 prototype. Answer:

**1.** Could an engineer understand what each component does from its name alone?

**2.** Is data logic separated from display logic? Or is everything in one file?

**3.** Is there any documentation — a README, comments, anything?

**Post in Slack:** One thing an engineer would struggle with in your current code.

*Speaker Notes: Same structure as M3 — surface the gap before the lab closes it. Most students will realize: terrible component names, no separation, zero docs, no version control. That's the motivation. After 5 minutes: "Who has descriptive component names? Who has a README? Who has their code in GitHub?" The honest answers set up the teaching and lab.*

---

## Slide 7 — The Graduation Judgment + Comprehension Debt
**When Do You Stop Exploring and Start Building For Real?**

Not every prototype should graduate. The graduation judgment is the most important PM skill in Vibe Coding.

**Graduate when:**
- The hypothesis is validated (or clearly invalidated)
- Stakeholders have seen it and said "build this"
- You can articulate what's real vs. what's mocked
- The prototype answers a specific question with evidence

**Don't graduate when:**
- You're still exploring which direction to go
- You haven't shown it to anyone outside your team
- You can't explain the hypothesis it tests

**Watch for comprehension debt:** After 50+ prompts, the prototype knows more than you do. Signs: "Let me show you" (you can't describe it without the demo), features you didn't ask for, prompts breaking things that used to work. The Living PRD is your comprehension debt payoff.

*Speaker Notes: "This is the judgment call that separates PMs who prototype from PMs who ship. Graduation isn't a code quality bar — it's a knowledge bar. Have you answered the question you set out to answer?" Ask 2-3 students: "Based on your M3 prototype, would you graduate today?" Then transition to comprehension debt: "Every module, your prototype got more capable. But did your understanding keep pace? If you can't write down what this does and who it's for, you've lost the thread. The Living PRD forces you to articulate it."*

---

## Slide 8 — The Living PRD
**A Spec Extracted, Not Imagined**

Traditional PRDs are written before anything exists. Living PRDs are extracted from working prototypes.

**What goes in a Living PRD:**

| Section | What It Answers |
|---------|----------------|
| Product Overview | What does this do? Who is it for? |
| Problem & Hypothesis | What's happening today? If we [intervention], then [outcome], because [evidence]. |
| User Flows & Screen Map | Screen-by-screen flow. Navigation. Edge cases. |
| Success Metrics | North star. Leading indicators. Measurement plan. |
| Technical Reality | What's real vs. mocked? Infrastructure connected? |
| Assumptions & Risks | Confidence levels. Kill switch. |
| Scope — In vs. Out | What's in, what's out, phasing. |
| Engineering Recommendation | Build order. Effort estimates. Open questions. |

This is Deliverable #3. It starts today and evolves through M5 and M6.

---

## Slide 9 — Infrastructure for PMs: Git + Supabase + Refactoring
**You Don't Need to Be an Engineer. You Need the AI to Set Up the Infrastructure.**

**Code Refactoring:**
"Rename all components to be descriptive." → `Component1` becomes `OnboardingWelcome`
"Separate data logic from display logic." → API calls move to their own files
"Add a README." → A new engineer orients in 5 minutes

**GitHub Connection:**
One click in Lovable. Your code gets a real repository. Version history. Rollback. Collaboration. An engineer clones the repo and starts working — no copy-paste, no screenshots.

**Supabase Connection:**
One click in Lovable. Your prototype gets a real PostgreSQL database. In M5, you'll build real schemas and auth on top of it. Today: connect it and know it's there.

You're not engineering. You're **connecting the infrastructure** — the same way you directed the AI to add screens and states in M3.

**Your Living Prompt Pack grows today.** Add your graduation prompts (extract, refactor, handoff) to the pack you started in M3. Export the pack as markdown — it's a portable skill file any AI tool can import. Your Living PRD + prompt pack together become a reusable product playbook: the next time you tackle a similar problem, you don't start from scratch.

*Speaker Notes: "Connecting GitHub and Supabase is one click each in Lovable. It's the easiest thing you'll do today — and the most impactful. GitHub means your code isn't trapped inside Lovable. It's in a real repo any engineer can clone. Supabase means your prototype has a real database waiting for real data. You'll build on top of it in M5. Today, just connect it and see it. If you don't have accounts yet, you'll create them during the lab — it takes 2 minutes and it's free. And remember — add your graduation prompts to your Living Prompt Pack. That pack is becoming a real skill file. By M6, it's a playbook you can hand to anyone."*

---

## Slide 10 — Lab Part 1: Extract the Living PRD
**Hands-on Lab Part 1: Extract the Living PRD** | 10 Minutes

Open the **Living PRD Extractor** tool. Select your scenario.

**Step 1 (3 min):** Review the extraction prompt template. Customize it for your prototype — your screens, your hypothesis, your metrics.

**Step 2 (5 min):** Copy the prompt into Lovable. Paste the generated PRD back into the Extractor.

**Step 3 (2 min):** Read your PRD. Does it accurately describe what you built? Flag anything wrong or missing.

Do NOT refactor yet. First, capture the spec.

*Speaker Notes: Drop the Living PRD Extractor link in Slack. Walk the room as they extract. The common reaction: "It actually described my product correctly." That's the first wow. Check that everyone has a PRD pasted back into the tool. "If your PRD doesn't match what you built, fix it now."*

---

## Slide 11 — Lab Part 2: Refactor + Handoff
**Hands-on Lab Part 2: Refactor & Handoff** | 12 Minutes

**Prompt 1 — Refactor (7 min):** "Refactor this codebase. Rename all components to be descriptive based on what they do. Separate data logic from display components. Group files by feature. Add a README.md explaining the project structure and what each screen does."

After: switch to code view. Compare before and after. Can you find each screen in the file structure?

**Prompt 2 — Handoff (5 min):** "Write an engineering handoff: list every component and its purpose, describe the data model (what's real vs. mocked), identify the top 3 technical decisions, and write a 'start here' guide for a new engineer."

Paste the handoff into the Living PRD Extractor under "Engineering Handoff."

*Speaker Notes: Walk the room. When they switch to code view after the refactor: "Find your dashboard component. What was it called before?" The naming transformation clicks immediately. For the handoff: "Read the 'start here' guide. Would a new engineer know where to begin?" If students want to keep refactoring: "Resist. The PRD and handoff matter more than perfect code."*

---

## Slide 12 — Lab Part 3: Connect GitHub + Supabase
**Hands-on Lab Part 3: Real Infrastructure** | 10 Minutes

THE GRADUATION CEREMONY

**Step 1 — Accounts (3 min):** Create a GitHub account and a Supabase account if you don't have them. Both are free. Links in Slack.

**Step 2 — Connect GitHub (2 min):** In Lovable, click the GitHub icon (top right) → "Connect GitHub." Authorize. Your code is now in a real repository.

**Step 3 — Verify GitHub (1 min):** Open the GitHub repo URL. Browse the code. Find your refactored component names. See the README.

**Step 4 — Connect Supabase (2 min):** In Lovable, click "Add Supabase" (top right). Connect. Your prototype now has a real PostgreSQL database.

**Step 5 — Verify Supabase (2 min):** Open the Supabase dashboard. See the project. This is the database you'll build on in Module 5.

Your prototype just graduated. It has version control and a database. This isn't a demo anymore.

*Speaker Notes: THIS IS THE WOW MOMENT. It's one click each — but the impact is everything. Walk the room. When students open their GitHub repo and see their refactored code with the README: "That's your code. In a real repo. An engineer can clone it right now." When they connect Supabase: "Your prototype has a real PostgreSQL database. In M5, you'll build real tables and auth on top of it." The combined effect: 10 minutes ago this was code trapped in Lovable with hardcoded data. Now it has a spec, clean code in GitHub, and a real database. Students who already have GitHub/Supabase accounts will finish fast — have them help others. If anyone gets stuck on account creation, pair them up. After 10 min: "Who has their code in GitHub? Who has Supabase connected? Open your GitHub repo. That's graduation."*

---

## Slide 13 — Peer Review: The Handoff Test
**Breakout Group Activity: Can You Build From This?** | 10 Minutes

Breakout rooms. Groups of 2.

**The test:** Person A shares ONLY their Living PRD (not the prototype). Person B reads it.

**Person B answers:**
- What does this product do?
- Who is it for?
- What hypothesis does it test?
- What's real vs. mocked?
- What should engineering build first?

If Person B can answer all 5 from just the PRD, it's handoff-ready. If not, iterate.

*Speaker Notes: Enforce the rule strictly: NO showing the prototype. PRD only. "If your partner can describe the product, the user, and the hypothesis from just reading your PRD — you've written a spec that stands on its own." Watch for the reaction when it works: the student realizes their prototype can exist independently of them. That's graduation. After both rounds: "Who had a partner that nailed all 5?"*

---

## Slide 14 — Quick Share
**What Surprised You About Your Own Spec?**

One insight: What did the extracted PRD get right that you hadn't articulated? Or what did it miss that you thought was obvious?

The gap between what you built and what you can describe — that's comprehension debt in action.

---

## Slide 15 — Break It: The Prototype That Never Graduated
**"Break It" Exercise** — 500 Prompts Deep, No Spec, No Repo

CAUTIONARY TALE

A PM built a prototype over 6 weeks. 500+ prompts. Features everywhere. No spec. No documentation. Not connected to GitHub. No database. The PM got promoted and left the project.

**What the inheriting PM found:**
- 47 components, none with descriptive names
- Data logic scattered across 12 files
- 3 features that contradict each other
- No hypothesis documented — nobody knows what it was testing
- Code trapped in Lovable — no repo, no way to share with engineering
- The AI can't explain it either — context window exceeded

**The lesson:** If you can't extract the spec, nobody can. If the code isn't in GitHub, it doesn't exist outside your browser. Graduation isn't optional.

*Speaker Notes: Make this visceral. Ask: "Has anyone inherited a project with no documentation?" Let them share horror stories. Then connect it: "This is what happens when you skip M4. Your beautiful M3 prototype becomes legacy code if nobody can explain what it does. The Living PRD is insurance. The GitHub repo is permanence. The Supabase connection is foundation. The refactored code is respect for the person who comes after you." Keep to 8 minutes.*

---

## Slide 16 — Pull Up All Four
**M1. M2. M3. M4. Side by Side.**

Open four tabs.

**Module 1:** Your first build. One prompt, one page. No data.

**Module 2:** Your validation build. Real data, real hypothesis, design-matched.

**Module 3:** Your precision build. 5+ screens, states, documented chain.

**Module 4:** Your graduated build. Living PRD, clean code in GitHub, Supabase connected, engineering handoff.

Same tool. Same you. Four modules of progression.

*Speaker Notes: Have students open all four prototypes. Give it 30 seconds of silence. Then: "In M1, you built a demo. By M4, you have a spec, structured code in a real GitHub repo, a real database, and an engineering handoff. That's not a prototype anymore — that's a product brief with real infrastructure an engineering team can sprint on." This is the emotional high point of the first half. After this, M5 starts the second half: building on top of the infrastructure you just connected.*

---

## Slide 17 — What You Did Today
**What You Did Today**

**1. Living PRD** — You extracted a complete product spec from your working prototype. The spec wasn't imagined — it was grounded in what actually works. That's Deliverable #3.

**2. Real Infrastructure** — Your code is in GitHub with version control. Your prototype has a Supabase database. One click each — but the difference is everything. This isn't trapped in a tool anymore.

**3. Engineering Handoff** — You generated a start-here guide: component map, data model, technical decisions. A new engineer can clone the repo and orient in 5 minutes.

Your prototype graduated. It's no longer just yours — it can survive without you.

---

## Slide 18 — Accountability
**ACCOUNTABILITY** | Before We Wrap

**1. Post in #builds:** Your prototype link + GitHub repo link + Living PRD. Caption: What did the AI get right about your product that you hadn't written down?

**2. Engage:** Read 2 other PRDs. Could you understand the product without seeing the prototype?

**3. Optional challenge:** Share your GitHub repo with an actual engineer. What questions do they have?

---

## Slide 19 — Module 5 Preview
**Module 5: Make It Real**

Same product. Real backend. Real users.

You've built fast (M1), built smart (M2), built precise (M3), and graduated it (M4). Your prototype has a spec, clean code in GitHub, and Supabase connected. Next: build on top of that infrastructure.

**Module 5 — The Backend Moment:**
- Build real database schemas — your data persists across sessions
- Add authentication — real users, real accounts, different people see different data
- API integrations — Stripe, email, whatever your product needs
- Edge case handling — what happens when things break

Module 1: Build fast.
Module 2: Build smart.
Module 3: Build precise.
Module 4: Graduate it.
Module 5: Make it real.

---

## Slide 20 — Survey
**Your Opinion Matters To Us**

Scan the QR code or use the link to share your feedback. Your insights help us improve each cohort.

---

## Design Notes for Gamma
- Match Modules 1–3 visual template exactly (same fonts, colors, layout grid)
- Slides are student-facing course material — keep content clean, instructional, and practical. Do NOT put pedagogical commentary, emotional cues, or "wow moment" labels on slides.
- Slide 1 — Bold title, three waypoints as prominent numbered list (same pattern as M1–M3 slide 1)
- Slide 3 — Show the polished prototype vs. the messy code. The contrast is the hook.
- Slide 4 — Show the 5 steps cleanly: 3 prompts + 2 infrastructure clicks. Visual progression from prompts to infrastructure.
- Slide 7 — Two-column layout: "Graduate when" vs "Don't graduate when." Comprehension debt as a callout box below.
- Slide 8 — Living PRD table is the key reference visual. Students will revisit this during the lab.
- Slide 9 — Three distinct blocks: Refactoring, GitHub, Supabase. Before/after code examples for refactoring. Screenshots/icons for GitHub and Supabase.
- Slide 12 — THE KEY SLIDE. Make the 5 steps feel like a ceremony. Large step numbers. Screenshots of GitHub repo and Supabase dashboard. "Your prototype just graduated" should feel like a milestone.
- Slide 15 — Break It: make it feel like a cautionary tale, not a lecture. Numbers (500+ prompts, 47 components) create visceral impact. Add "No repo" to the horror.
- Slide 16 — Four-column layout (M1 | M2 | M3 | M4). Let the visual comparison speak — minimal text.
- Slide 17 — Takeaways mirror slide 1's three waypoints (visual callback)
- Keep all lab slides (10, 11, 12) highly scannable — students reference these while building
