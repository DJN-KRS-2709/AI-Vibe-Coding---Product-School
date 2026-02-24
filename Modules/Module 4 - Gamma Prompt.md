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
2. **Code Refactoring** — Same product, readable code. Clean architecture an engineer can inherit.
3. **Engineering Handoff** — The document that bridges PM prototype to engineering sprint.

Module 1 was speed. Module 2 was aim. Module 3 was precision. Module 4 is graduation.

*Speaker Notes: "Welcome back. You've built fast, built smart, and built precise. Your M3 prototype has 5+ screens, interactive states, and a documented prompt chain. It looks like a real product. But here's the thing — if you got hit by a bus tomorrow, could anyone pick up where you left off? No spec. No structured code. No handoff document. Today we fix that. Three waypoints: living PRD, code refactoring, engineering handoff. By the end of today, your prototype graduates from exploration to something an engineering team can actually build from."*

---

## Slide 2 — Bridge from M3 + Agenda
**Your M3 Prototype Looks Real. Could Engineering Build From It?**

Your M3 build has multiple screens, interactive states, design-matched UI, and a documented prompt chain. If your VP saw it, they'd think engineering built it. But pull up the code — what would an engineer see?

- Component names like `Component1`, `handleClick2`
- Data logic tangled with display logic
- No documentation, no architecture, no spec

Today's flow:
1. **Demo** — Extract a spec. Refactor the code. Generate a handoff.
2. **Teaching** — Living PRDs, the graduation judgment, comprehension debt
3. **Lab** — Graduate your M3 prototype
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

Names like `div1`, `Section3`, `handleSubmit2`. Data fetching mixed into UI components. No README. No structure. An engineer would need a week just to understand what this does.

*Speaker Notes: Pull up the M3 Retention Engine prototype in Lovable. Click through the screens — remind students how polished it is. Then switch to the code view. Let it sit for 10 seconds. Don't explain the mess — let them see it. "This is what your VP doesn't see. This is what the engineer who inherits it sees. Would you want to build from this?" Pause. "3 prompts. Watch."*

---

## Slide 4 — Live Build: 3 Prompts
**The Graduation Chain**

**Prompt 1 — Extract:** "Look at this entire prototype. Write a product requirements document that covers: what this product does, who it's for, the problem it solves, the 5 screens and their purpose, the user flow from first screen to last, the hypothesis it tests, the key metrics, what's currently mocked vs. what would need real data, and recommended next steps for engineering. Format it as a structured document with clear sections."

**Prompt 2 — Refactor:** "Refactor the codebase. Rename all components to be descriptive (e.g., OnboardingWelcome, TeamInviteForm, PMDashboard). Separate data logic from display components. Group files by feature, not by type. Add a README.md that explains the project structure, what each screen does, and how to run it."

**Prompt 3 — Handoff:** "Generate an engineering handoff document: list every component and what it does, describe the data model (what's real vs. mocked), identify the 3 biggest technical decisions an engineer would need to make, and write a 'start here' guide for a new engineer inheriting this project. Be specific, not generic."

3 prompts. A spec, structured code, and an engineering handoff.

*Speaker Notes: Run the 3 prompts sequentially — pre-type each. Prompt 1: paste, wait ~60 sec. Read the PRD aloud — hit the key sections: "Look — product overview, user flows, metrics, what's mocked vs real, next steps for engineering. I didn't write this. The prototype wrote its own spec." Prompt 2: paste, wait ~60 sec. Switch to code view. "Component1 is now OnboardingWelcome. The data logic is in its own folder. There's a README." Show the before/after side by side if possible. Prompt 3: paste, wait ~40 sec. Read the handoff highlights: "It identified 3 technical decisions and wrote a 'start here' guide. That's a PM who ships, not a PM who prototypes." Total: ~7 minutes.*

---

## Slide 5 — Demo Debrief
**What Changed**

Same prototype. Same 5 screens. Same states.

- **Living PRD extracted** — a complete spec, generated from the build. Not imagined before building — extracted after.
- **Code refactored** — descriptive names, separated concerns, README. An engineer can read it on day one.
- **Engineering handoff** — component map, data model, technical decisions, start-here guide.

Traditional PM workflow: Research → Spec → Build → Test.
Vibe Coding workflow: Build → Test → Extract spec. The spec is the output, not the starting point.

*Speaker Notes: Land the paradigm shift explicitly. "In traditional PM, you write the spec BEFORE you build. You spend 2 weeks on a PRD that describes something that doesn't exist yet. In Vibe Coding, you build first, test the hypothesis, and THEN extract the spec from what actually works. The spec isn't imagined — it's grounded in a working prototype. That's fundamentally different." Pause. "You'll do this yourself in 30 minutes."*

---

## Slide 6 — Mini Activity: Look at Your Code
**Open Your M3 Prototype's Code View**

INDIVIDUAL EXERCISE | 5 MINUTES

Open Lovable. Switch to code view on your M3 prototype. Answer:

**1.** Could an engineer understand what each component does from its name alone?

**2.** Is data logic separated from display logic? Or is everything in one file?

**3.** Is there any documentation — a README, comments, anything?

**Post in Slack:** One thing an engineer would struggle with in your current code.

*Speaker Notes: This mirrors the M3 mini activity where students audited their M2 prototype's screens and states. Same structure — surface the gap before the lab closes it. Most students will realize: terrible component names, no separation, zero docs. That's the motivation. After 5 minutes: "Who has descriptive component names? Who has a README? Who would hand this to an engineer right now?" The honest answers set up the teaching and lab. Transition: "Let me show you why this matters — and what happens when you skip it."*

---

## Slide 7 — The Graduation Judgment
**When Do You Stop Exploring and Start Building For Real?**

Not every prototype should graduate. The graduation judgment is the most important PM skill in Vibe Coding.

**Graduate when:**
- The hypothesis is validated (or clearly invalidated — that's still a graduation)
- Stakeholders have seen it and said "build this"
- You can articulate what's real vs. what's mocked
- The prototype answers a specific question with evidence

**Don't graduate when:**
- You're still exploring which direction to go
- The prototype is testing multiple things at once
- You haven't shown it to anyone outside your team
- You can't explain the hypothesis it tests

The graduation moment isn't about the code being ready. It's about the **question being answered.**

*Speaker Notes: "This is the judgment call that separates PMs who prototype from PMs who ship. Graduation isn't a code quality bar — it's a knowledge bar. Have you answered the question you set out to answer? If yes, graduate. If no, keep exploring. The danger is graduating too early — before you know what you're building — or too late, spending months polishing a prototype nobody asked for." Ask 2-3 students: "Based on your M3 prototype, would you graduate today? Why or why not?" Let them reason through it publicly.*

---

## Slide 8 — Comprehension Debt
**Comprehension Debt — The Silent Killer**

Technical debt has a cousin nobody talks about: **comprehension debt.**

Every prompt you run adds features. Every feature adds complexity. After 50+ prompts, even YOU can't explain what your prototype does without clicking through it.

**Signs of comprehension debt:**
- "Let me show you" (you can't describe it without the demo)
- The prototype does things you didn't ask for and you're not sure why
- You can't explain the data model
- New prompts break things that used to work

**The fix:** Extract the spec. If you can't write down what this does, who it's for, and what it tests — you've lost the thread. The Living PRD is your comprehension debt payoff.

*Speaker Notes: "This is the concept that makes graduation urgent. Every module, your prototype got more capable — more screens, more states, more features. But did your UNDERSTANDING keep pace? Comprehension debt is when the prototype knows more than you do. The Living PRD forces you to articulate what you've built. If you can't write it down, you can't hand it off. And if you can't hand it off, it dies with you."*

---

## Slide 9 — The Living PRD
**The Living PRD — A Spec Extracted, Not Imagined**

Traditional PRDs are written before anything exists. They describe a product that doesn't work yet. Living PRDs are extracted from working prototypes. They describe what actually works.

**What goes in a Living PRD:**

| Section | What It Answers |
|---------|----------------|
| Product Overview | What does this do? Who is it for? Company context, target user, value proposition. |
| Problem & Hypothesis | What's happening today (with data)? If we [intervention], then [outcome], because [evidence]. User quotes and data points that support the bet. |
| User Flows & Screen Map | Screen-by-screen flow: entry point, primary action, where it leads. Navigation model. Edge cases (loading, error, empty). |
| Success Metrics | North star metric with current/target/timeframe. Leading indicators. Guardrail metrics. Measurement plan (A/B, cohort, sample size). |
| Technical Reality | What's real vs. mocked? Existing infrastructure to leverage. New infrastructure required. |
| Assumptions & Risks | Core assumptions with confidence levels. Technical, adoption, and business risks. Kill switch with specific threshold. |
| Scope — In vs. Out | What's in scope and why. What's explicitly out and why not now. Dependencies. Phasing (MVP → fast-follow → future). |
| Engineering Recommendation | Recommended build order with rationale. Effort estimates. Open questions for engineering. Experiment plan before full build. |

This is Deliverable #3. It starts today and evolves through M5 and M6.

---

## Slide 10 — Code Refactoring for PMs
**You Don't Need to Be an Engineer. You Need the AI to Clean Up.**

Refactoring isn't about writing code. It's about asking the AI to organize what it already built.

**What refactoring looks like for a PM:**

"Rename all components to be descriptive." → `Component1` becomes `OnboardingWelcome`

"Separate data logic from display logic." → API calls move to their own files

"Group files by feature, not by type." → Everything about the dashboard lives in `/dashboard`

"Add a README that explains the project structure." → A new engineer can orient in 5 minutes

You're not engineering. You're **directing the AI to make the code handoff-ready** — the same way you directed it to add screens and states in M3.

*Speaker Notes: "I know what you're thinking: 'I'm a PM, not an engineer. Why do I care about code structure?' Because the person who inherits this code is an engineer. And if they open it and see Component1 and handleClick2, they'll spend a week just understanding what you built. 10 minutes of refactoring prompts saves a week of engineering confusion. You already know how to direct the AI — M3 proved that. This is the same skill, applied to code instead of UI."*

---

## Slide 11 — Lab Part 1: Extract
**Hands-on Lab Part 1: Extract the Living PRD** | 10 Minutes

Open the **Living PRD Extractor** tool. Select your scenario.

**Step 1 (3 min):** Review the extraction prompt template. Customize it for your prototype — your screens, your hypothesis, your metrics.

**Step 2 (5 min):** Copy the prompt into Lovable. Paste the generated PRD back into the Extractor.

**Step 3 (2 min):** Read your PRD. Does it accurately describe what you built? Flag anything wrong or missing.

Do NOT refactor yet. First, capture the spec.

*Speaker Notes: Drop the Living PRD Extractor link in Slack. Walk the room as they extract. The common reaction: "It actually described my product correctly." That's the first wow — the AI understood what they built well enough to write the spec. Check that everyone has a PRD pasted back into the tool. "If your PRD doesn't match what you built, fix it now. The spec is only useful if it's accurate." Resist the urge to move to refactoring — the extraction needs to be complete first.*

---

## Slide 12 — Lab Part 2: Refactor + Handoff
**Hands-on Lab Part 2: Refactor & Handoff** | 20 Minutes

Now graduate the code. Use these prompts as starting points — customize for your prototype.

**Prompt 1 — Refactor (10 min):** "Refactor this codebase. Rename all components to be descriptive based on what they do. Separate data logic from display components. Group files by feature. Add a README.md explaining the project structure and what each screen does."

After: switch to code view. Compare before and after. Can you find each screen in the file structure?

**Prompt 2 — Handoff (10 min):** "Write an engineering handoff: list every component and its purpose, describe the data model (what's real vs. mocked), identify the top 3 technical decisions, and write a 'start here' guide for a new engineer."

Paste the handoff into the Living PRD Extractor under "Engineering Handoff."

*Speaker Notes: THIS IS THE WOW MOMENT. Walk the room as students refactor. When they switch to code view after the refactor: "Find your dashboard component. What was it called before? What's it called now?" The naming transformation is the most visible change — it clicks immediately. For the handoff prompt: "Read the 'start here' guide out loud. Does it make sense? Would a new engineer know where to begin?" After 20 min: "Stop. You now have a PRD, structured code, and an engineering handoff. That's what graduation looks like." If students want to keep refactoring: "Resist. The PRD and handoff matter more than perfect code. You're a PM, not a code reviewer."*

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

*Speaker Notes: This is the accountability moment. Enforce the rule strictly: NO showing the prototype. PRD only. "If your partner can describe the product, the user, and the hypothesis from just reading your PRD — you've written a spec that stands on its own. If they can't, your PRD has gaps." Watch for the reaction when it works: the student realizes their prototype can exist independently of them. That's graduation. Then switch roles. After both rounds: "Who had a partner that nailed all 5?" Celebrate those. "Who had gaps?" That's iteration — and that's fine.*

---

## Slide 14 — Quick Share
**What Surprised You About Your Own Spec?**

One insight: What did the extracted PRD get right that you hadn't articulated? Or what did it miss that you thought was obvious?

The gap between what you built and what you can describe — that's comprehension debt in action.

---

## Slide 15 — Break It: The Prototype That Never Graduated
**"Break It" Exercise** — 500 Prompts Deep, No Spec

CAUTIONARY TALE

A PM built a prototype over 6 weeks. 500+ prompts. Features everywhere. No spec. No documentation. The PM got promoted and left the project.

**What the inheriting PM found:**
- 47 components, none with descriptive names
- Data logic scattered across 12 files
- 3 features that contradict each other
- No hypothesis documented — nobody knows what it was testing
- The AI can't explain it either — context window exceeded

**The lesson:** If you can't extract the spec, nobody can. Graduation isn't optional. Every prototype that matters needs a Living PRD, or it dies with you.

*Speaker Notes: Make this visceral. Either use a prepared messy codebase example or ask: "Has anyone inherited a project with no documentation?" Let them share horror stories. Then connect it: "This is what happens when you skip M4. Your beautiful M3 prototype — 5 screens, states, everything — becomes legacy code in 6 months if nobody can explain what it does or why. The Living PRD is insurance. The refactored code is respect for the person who comes after you." 10 minutes. Let the room react.*

---

## Slide 16 — Pull Up All Four
**M1. M2. M3. M4. Side by Side.**

Open four tabs.

**Module 1:** Your first build. One prompt, one page. No data.

**Module 2:** Your validation build. Real data, real hypothesis, design-matched.

**Module 3:** Your precision build. 5+ screens, states, documented chain.

**Module 4:** Your graduated build. Clean code, a Living PRD, and an engineering handoff.

Same tool. Same you. Four modules of progression.

*Speaker Notes: Same pattern as the M3 triple reveal — now with four tabs. Have students open all four prototypes. Give it 30 seconds of silence. Then: "In M1, you built a demo. By M4, you have a spec, structured code, and an engineering handoff. That's not a prototype anymore — that's a product brief an engineering team can sprint on." Let the visual progression land. This is the emotional high point of the first half of the course (M1-M4). After this, M5 starts the second half: making it real.*

---

## Slide 17 — What You Did Today
**What You Did Today**

**1. Living PRD** — You extracted a complete product spec from your working prototype. The spec wasn't imagined — it was grounded in what actually works. That's Deliverable #3.

**2. Code Refactoring** — You directed the AI to clean the code: descriptive names, separated concerns, a README. Same product, now engineer-readable.

**3. Engineering Handoff** — You generated a start-here guide: component map, data model, technical decisions. A new engineer can orient in 5 minutes.

Your prototype graduated. It's no longer just yours — it can survive without you.

---

## Slide 18 — Accountability
**ACCOUNTABILITY** | Before We Wrap

**1. Post in #builds:** Your prototype link + your Living PRD (copy from the Extractor). Caption: What did the AI get right about your product that you hadn't written down?

**2. Engage:** Read 2 other PRDs. Could you understand the product without seeing the prototype?

**3. Optional challenge:** Share your engineering handoff with an actual engineer. What questions do they have? Drop their feedback in Slack.

---

## Slide 19 — Module 5 Preview
**Module 5: Make It Real**

Same product. Real connections.

You've built fast (M1), built smart (M2), built precise (M3), and graduated it (M4). Your prototype looks like a product and has a spec. Next: make it actually work.

**Module 5 — The Backend Moment:**
- Connect to a real database — your data persists
- Add authentication — real users, real accounts
- API integrations — Stripe, email, whatever your product needs

Module 1: Build fast.
Module 2: Build smart.
Module 3: Build precise.
Module 4: Build for real.
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
- Slide 4 — Show the 3 prompts cleanly (Extract / Refactor / Handoff). Students should see the progression.
- Slide 7 — Two-column layout: "Graduate when" vs "Don't graduate when." Clean decision framework.
- Slide 8 — Comprehension debt: make the "signs" list scannable and memorable.
- Slide 9 — Living PRD table is the key reference visual. Students will revisit this during the lab.
- Slide 10 — Before/after code examples should be visually distinct (messy → clean)
- Slide 12 — Lab prompts must be scannable at a glance. Students reference this while building.
- Slide 15 — Break It: make it feel like a cautionary tale, not a lecture. Numbers (500+ prompts, 47 components) create visceral impact.
- Slide 16 — Four-column layout (M1 | M2 | M3 | M4). Let the visual comparison speak — minimal text.
- Slide 17 — Takeaways mirror slide 1's three waypoints (visual callback)
- Keep all lab slides (11, 12, 13) highly scannable — students reference these while building
