# Module 1 — Glossary

> Terms used in Module 1, defined the way we use them in this certification. When a term appears in a deck or notes file, it means *this* — not the generic dictionary version.

---

**AI-Review Prompt**
The verbatim text block a learner pastes into ChatGPT, Claude, or Cursor — together with their artifact — to get a structured critique. Every solo lab in this certification ships one. The pattern replaces what would historically have been a peer review.

**Confidence Line**
The single arc that runs through the entire certification. Three phases: High Ambiguity (M1–M2) → Gaining Clarity (M3–M4) → Production Confidence (M5–M6). Every prompt the learner writes is a choice on this line — explore the path, or refine it.

**Credit Death Spiral**
The most common beginner mistake. A learner re-prompts the same broken logic three or four times, hoping the AI will recover. It does not. Credits drain. The Eject Rule exists to prevent this.

**Design-to-Code**
The multimodal entry point where the learner pastes Figma frames or design-system tokens (hex codes, spacing rules, typography) and the AI generates a prototype that matches a real brand from the first generation. Best for prototyping inside an existing product.

**Eject Rule**
If a prompt fails twice, stop. Export the code, debug it externally, paste the fix back. Never enter a credit death spiral.

**Evidence per Hour**
The actual metric vibe coding optimizes. Not speed — speed is the floor. *Evidence per hour* is how much signal a learner generates per unit of build time. Three rough prototypes that each test a different assumption beat one polished prototype that tests nothing.

**Eviction**
*See Eject Rule.* Same thing, different name in older artifacts.

**First Screen Method**
A launch path in Lab 1. The learner visualizes the very first thing the user would see when they open the app and prompts the AI to build exactly that. Defeats blank-page paralysis when no template fits the scenario.

**High-Velocity Prototyping Cycle**
The four-move loop: Build → Show → Learn → Decide. The whole course in four boxes. PMs reliably skip step four ("Decide"), which is what separates a tool from a toy.

**Lab 1 Scenarios**
Four product situations the learner picks from for the first build:
- *Retention Engine* — B2B SaaS losing 30% of customers in 90 days.
- *Internal Tool Nobody Uses* — CRM with 18% adoption.
- *Marketplace Trust Problem* — zero-review providers can't get first customer.
- *Dashboard Nobody Reads* — analytics with 60% bounce rate.

**Living Prompt Pack**
A learner-authored skill markdown that travels with them. Introduced in Module 3. Mentioned in Module 1 only as a forward-reference.

**Lovable**
The primary demo tool for the certification. Visual-first, lowest barrier for non-technical PMs, supports backend (databases, Stripe, auth, deployment). Pro access (3 months free) included via Product School partnership. The methodology is tool-agnostic — Bolt, Cursor, v0, Replit, Claude Code all work the same way conceptually.

**Mobbin**
A library of real-product screenshots used as reference patterns. In Module 1, learners use a Mobbin screenshot as input to the Screenshot-to-App entry point — the AI clones the palette, layout, and navigation from the reference into the learner's prototype.

**Multimodal**
The property of modern vibe-coding tools that lets them ingest text, screenshots, and design files as inputs to a single prompt. Practical consequence: you never start from a blank canvas.

**One-Shot Generation**
The goal mode for credit efficiency — a single prompt that produces a useful result, vs. trial-and-error iteration. Achievable when the prompt has been drafted and refined in a free LLM sandbox before pasting into Lovable.

**Pre-Read**
A short async document the learner reads before the live module session. Module 1's pre-read covers tool setup, the Confidence Line in 60 seconds, and the four scenarios.

**Prototype-Readiness Score**
The 1–5 self-evaluation the learner runs after Lab 2 (see *Toy vs Tool*). 1 = sketch, 5 = VP-ready. Most learners score 2–3 today; the score gap is what M2–M6 closes.

**Refresh Code Directly**
A credit-saving move: for cosmetic fixes (hex codes, label typos, padding), edit the generated code in the code panel rather than re-prompting. Re-prompting cosmetic changes is the most expensive way to do a five-second job.

**Repo / Repo-CTA**
The folder structure (`01-velocity/`, `02-validation/`, etc.) where every learner artifact is committed. Each `applied_work` slide ends with a green Repo-CTA pointing at the exact path the artifact should land at.

**Sandbox (Prompt Sandbox)**
A free LLM (ChatGPT, Gemini, Claude) used to draft and refine a prompt *before* pasting it into Lovable. Where 60% of credit-saving prompt work happens.

**Screenshot-to-App**
The multimodal entry point where the learner uploads a screenshot (Mobbin, competitor, hand-drawing) and the AI clones the layout and design system into a prototype. Best for refining a vibe sketch against a known-good professional pattern.

**Self-Review Checklist**
The 3–5 questions a learner walks through on their own prototype after a lab. Replaces what was historically a peer-review checklist. Every lab in the certification has one.

**Show and Swap** *(deprecated)*
The legacy paired-review exercise. Replaced in the current curriculum by **Solo Review · Walk Your Build** — a silent self-walk plus AI-review prompt. Same intent (raw signal on the prototype); individual format.

**Skill (Skill Markdown)**
A markdown file that gives an AI specialized instructions for a domain (e.g. "build dashboards for B2B SaaS," "always use this design system"). The AI follows the skill on every prompt without the learner re-explaining context. Marketplaces (Anthropic, Cursor) and public GitHub repos host them. Module 3 teaches authoring.

**Solo Review**
The individual-format replacement for paired peer reviews. Three steps: silent walk → written self-review → AI-review prompt. The output (one-line learning + screenshot) is shared async in `#cohort-channel`.

**Text-to-App**
The multimodal entry point where the learner uses a natural-language prompt as the only input. Best for greenfield exploration where no design or competitor reference exists yet.

**Toy**
A prototype that looks impressive but proves nothing. Generates applause, not insights. No logic behind the screen. Dies after the demo. Cannot survive a real user.

**Tool**
A prototype that looks real and proves something works. Validates an assumption with clickable evidence. Handles at least one real user flow end-to-end. Survives when someone else uses it. Generates a decision, not a reaction.

**Triple-Threat Build**
The Module 1 demo and the universal Module 1 move: when three stakeholders have three theories and zero data, build all three as rough prototypes (15 min each), compare evidence side by side, and let evidence — not seniority — decide. The phrase is named after the instructor demo video, but the move generalizes.

**Vibe Coding**
This certification's process-name: the practice of validating product intent as fast as possible using whatever AI building tool is available. The *tool* is replaceable; the *process* is durable. Today's tool is Lovable. Tomorrow's might not be. The methodology stays the same.

**Vibe Sketch**
A first-pass prototype with the vibe right but the polish missing. The output of every Lab 1. The starting point for every Lab 2 strategic refinement.
