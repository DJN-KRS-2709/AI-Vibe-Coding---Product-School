# M4: Transition From Prototypes to Production Specs

> Source: PowerPoint deck `draft_M4_ Transition From Prototypes to Production Specs.pptx`
> Extracted: 2026-03-23

---

## Slide 1 — Title

Transition From Prototypes to Production Specs
Module 4

---

## Slide 2 — Class Expectations

- Cameras On — Be present and visible
- Arrive On Time
- Engage to Network — Participate in labs and discussions
- Tool Readiness — All tools and accounts must be active before class
- Use Slack for all communication
- Class Momentum — Deep-dive questions moved to after-class support

---

## Slide 3 — Vibe Coding Syllabus

| Module | Title | Description |
|---|---|---|
| M1 | Execute Vibe Coding Velocity | Build a functional prototype from an ambiguous problem. Generate immediate evidence. |
| M2 | Validate Product Hypotheses via Risk-Based Prototyping | Inject data, metrics, and hypotheses to ensure you're solving the right problem. |
| M3 | Ensure Complex System Stability with Prompt Chaining | Master context layering and constraint grounding to orchestrate multi-screen architectures. |
| **M4** | **Transition From Prototypes to Production Specs** | **Enforce technical rigor. Convert builds into version-controlled GitHub repos. Formalize logic for engineering handoff.** |
| M5 | Ship Live Products with Full-Stack Logic | Connect live databases and secure APIs. Transform standalone features into production-ready products on a live URL. |
| M6 | Measure Product Performance for AI-Driven Iteration | Analyze real-world interactions. Use AI-driven analytics to identify friction and redeploy improved updates. |

---

## Slide 4 — Agenda

1. The Black Box Gap of AI-Generated Code
2. How to Move From Prototype to Production
3. Hands-On Lab: Refactor Your Prototype Code and Generate Your Eng Handoff
4. Hands-On Lab: Connect Your Infrastructure with GitHub and Supabase

---

## Slide 5 — Section Header: The Black Box Gap of AI-Generated Code

---

## Slide 6 — Reflection Moment: Q&A Discussion

**Instructor-Led Q&A**

Open up your prototype from Module 3 and answer honestly:

- Could an engineer understand what each component does from its name alone?
- Is data logic separated from display logic, or is everything tangled in one file?
- Do you have any additional documentation such as a README, comments, etc.?

Feel free to unmute and share, or post your thoughts in the chat!

---

## Slide 7 — Quick Debrief: Documentation Accountability Statement

**POST ON SLACK IN ONE SENTENCE:**
What is one thing an engineer would struggle with in your current code?

---

## Slide 8 — Instructor-Led Demo: Comparing the Exterior With What's Under the Hood

Your prototype looks like a finished product, but the code is currently a black box.

**THE PROBLEM:** You have high-fidelity visuals and a solid hypothesis, but if an engineer asked, "How does the data flow?" or "Where is the logic for this screen?", you'd be stuck digging through a messy file tree.

---

## Slide 9 — The New Operating Model: Vibe Coding Workflow

**Traditional PM Workflow (Old Way: Dependency Loop):**
Idea → Research → Write Spec → Wait for Eng/Design → Provide Feedback → Review Build → Wait for Update → Test and Iterate

**Vibe Coding Workflow (New Way: Vibe Loop):**
Build Prototype → Test Live → Extract Spec → Connect Infra

Your spec is the output, not the starting point. Your prototype is the source of truth; the spec is the evidence.

---

## Slide 10 — Section Header: How to Move From Prototype to Production

---

## Slide 11 — The Production Threshold

Not every prototype should move into production. Threshold judgment is the most important PM skill in Vibe Coding.

**✅ Move to Production Spec When:**
- Your "kill switch" hypothesis is proven with functional evidence
- Stakeholders have approved the direction for a real build
- You can explain the logic without needing a demo
- Your goal is shifted from discovery to durability

**🚫 Stay in Prototyping Mode When:**
- Your core value proposition or user flow is still changing
- You haven't gathered feedback outside your immediate team
- You can't yet define the business rules the AI is executing
- Speed of iteration is still more valuable than system stability

If you don't transition at the right time, you hit a ceiling where the AI's complexity outpaces your ability to manage it.

---

## Slide 12 — Paying Off Your Comprehension Debt

Comprehension debt — where the AI knows the logic better than you do — can come as a trade-off to vibe coding speed. The Living PRD is your technical translation layer, forcing the AI to explain the logic it manifested during the build.

It extracts the functional reality of your prototype to create a repeatable source of truth.

**Executable Prototype (The Truth) + Living PRD (The Evidence) = Production-Ready Handoff**

---

## Slide 13 — The Eight Building Blocks of a Living PRD

1. **Product Overview** — A high-level summary of the validated system; what it does and who it's for.
2. **Problem & Hypothesis** — A clear definition of the current user friction and the evidence-backed intervention being tested.
3. **User Flow & Screen Map** — A visual and descriptive map of navigation paths, screen states, and interactive logic.
4. **Success Metrics** — The North Star metric and leading indicators used to measure production performance.
5. **Technical Reality** — A detailed report on functional logic versus mocked elements and current infrastructure connections.
6. **Assumptions & Risks** — An assessment of current confidence levels, kill switch triggers, and potential technical failure points.
7. **In vs. Out Scope** — A definitive list of included features, excluded items, and the proposed roadmap for future phases.
8. **Engineering Recommendation** — A strategic guide on build order, technical effort estimates, and open architectural questions.

Create your own Living PRD extractor [link]

---

## Slide 14 — Living PRD Example Snapshot

Example of a completed Living PRD. Build your own Living PRD [link].

---

## Slide 15 — From Prompt Pack to Product Spec

A traditional PRD is a wish list written before a build. A Living PRD is a reality report extracted from a build. You've done most of the work already, so extracting becomes the next logical step before handoff.

---

## Slide 16 — Individual Exercise: Extract Your Living PRD

**INSTRUCTIONS:** Use the Living PRD Extractor tool to interrogate your current build and generate a professional specification. Your goal is to capture an honest report of your prototype's functional logic, screen map, and technical reality before you transition to the engineering-ready pillars.

**Steps:**
1. Open the Living PRD Extractor tool and select your scenario.
2. Review the extraction prompt template and customize the variables (screen count, hypothesis, key metrics).
3. Copy your customized prompt into the Lovable chat interface to trigger the technical audit.
4. Paste the AI's generated output back into the Extractor tool to populate the 8 sections.
5. Read through the generated PRD to verify accuracy and flag misrepresentations.

Note: This is pre-work to document the current state, even if it is not perfect.

---

## Slide 17 — Quick Debrief: Living PRD Key Learning Statement

**POST ON SLACK IN ONE SENTENCE:**
What did the extracted PRD get right that you hadn't articulated, or what did it miss that you thought was obvious?

Then, reply to 2 other learning sentences from your peers.

---

## Slide 18 — The Three Pillars of an Engineering-Ready System

**Code Refactoring** — The codebase must be structurally organized with professional naming conventions and separated logic so an engineer can fully orient within 5 minutes of reading the README.

**GitHub Connection** — The project must live in a version-controlled repository to enable a permanent history of changes and a secure "front door" for technical collaboration and rollbacks.

**Supabase Connection** — The system must move from mocked data to a persistent PostgreSQL database and Auth layer, managed through a visual table editor rather than hard-coded simulations.

You don't need to be an engineer — you need the AI to set up the infrastructure. You direct, the AI executes and connects.

---

## Slide 19 — Break (5 minutes)

---

## Slide 20 — Cameras On

---

## Slide 21 — Section Header: Refactor Your Prototype Code and Generate Your Eng Handoff

---

## Slide 22 — Hands-On Lab: Refactor & Generate Handoff

**LAB EXERCISE:** Use two specific command prompts to re-organize your prototype's file names and generate a technical "Start Here" manual for your code.

**Steps:**
1. Open the Code View tab and navigate to `src/pages` to see your current generic file names.
2. Copy the Refactor Prompt from the tool and paste it into Lovable to rename components and group files by feature.
3. Switch back to the Code View tab to confirm descriptive screen names and no more generic "component" titles.
4. Review the new `README.md` file to ensure it accurately explains your project structure and screen purpose.
5. Copy the Handoff Prompt from the tool and paste it into Lovable to generate your "Start Here" guide and data model summary.
6. Paste the AI's generated handoff response into the Engineering Handoff section of your Living PRD Extractor tool.

Keep in mind: You must check the Code View tab to ensure files have been renamed to descriptive titles.

---

## Slide 23 — Breakout Group Exercise: Show and Swap Your Spec Handoff Package

Screen share your documentation (Living PRD + Engineering Handoff). Read your partner's documentation silently for 3 minutes. No verbal context or explanations.

**After 3 minutes of silent reading, discuss:**
- Can you identify the Product Value (What/Who/Hypothesis) in under 60 seconds?
- Is the Technical Reality (Real vs. Mocked) clear enough that you aren't guessing what works?
- Does the Handoff tell you exactly which file or feature to open and build first?

---

## Slide 24 — Section Header: Connect Your Infrastructure with GitHub and Supabase

---

## Slide 25 — Hands-On Lab: Connect GitHub and Supabase

**LAB EXERCISE:** Connect your Lovable project to GitHub for version control and Supabase to establish a real, persistent database. Your goal is to move into a production-ready environment that can support real users, authentication, and persistent data.

**Steps:**
1. Click the GitHub icon in the Lovable sidebar and follow prompts to create a new repository.
2. Confirm the connection by verifying your "Initial Commit" in your GitHub account.
3. Prompt Lovable to create a backend database system for one of your features.
4. Review the Database tab in Lovable to ensure tables have been automatically generated.
5. Open your Living PRD and update the Infrastructure section with your new GitHub repository and Supabase project URLs.

Keep in mind: This will ensure you're ready for the activities in Module 5!

---

## Slide 26 — Module 4 Complete: What You Accomplished Today

**The Numbers:**
- 8 PRD Blocks — Extracted strategic intent into eight distinct blocks
- 1 Eng Handoff — Refactored files and generated a "Start Here" manual
- 2 Backend Connections — Linked GitHub and Supabase

**The Shifts:**
- **The Black Box Logic: Explained** — Moved from a build only you understand to a documented system any engineer can audit.
- **The Prototype Ceiling: Broken** — Moved from spaghetti logic to clean architecture. Foundation that can scale in production.

📍 **Project Deliverable Check:** Copy your completed Living PRD elements into slide 7 and your Engineering Handoff sections into slide 9 of your final project deliverables deck today.

Next: Module 5 — Move from connected infrastructure to a fully deployed, live product.

---

## Slide 27 — Key Takeaways

- PMs must shift from the dependency loop of hypothetical specs to a vibe loop of functional evidence. The Living PRD becomes a validated output of a working build rather than a document of unproven guesses.
- The Living PRD automates documentation by extracting the hypothesis, data context, and prompt chains used during construction. The eight building blocks ensure the technical handoff is an effortless byproduct of the build process.
- PMs must enforce technical rigor by refactoring AI code into structurally organized, production-ready assets. Connecting to GitHub and Supabase establishes the required durability for live environments.

---

## Slide 28 — Extra Practice + Next Session

**Optional exercises:**
1. **The Repo Rollback Drill** — Intentionally break a feature with a reckless prompt. Use commit history to revert. Does version control act as a safety net?
2. **The Data Integrity Stress Test** — Manually add bad data in Supabase. Does the UI catch errors gracefully or crash?

**Next Session — M5: Ship Live Products with Full-Stack Logic**
Transform standalone prototypes into integrated, production-ready systems. Connect live databases and secure APIs. Enforce data persistence and Row-Level Security on a live URL.

---

## Slide 29 — Survey

Scan the QR code or use the Day 4 Survey Link to share your feedback.

---

## Slide 30 — Bonus Resources

- Module 4 Lab Guide (Hands-On Lab Walkthrough)
- Living PRD Template (Product School Template)

---

## Slide 31 — Q&A

---

## Slide 32 — End
