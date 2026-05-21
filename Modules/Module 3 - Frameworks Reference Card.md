# Module 3 — Frameworks Reference Card

> Every framework from Module 3 in the order you use them. Keep this open while you chain.

---

## 1. The Prompting Maturity Curve

Your prompt style should match your **certainty**. As product certainty rises, precision rises with it — exploration prompts give way to execution prompts.

| Stage | When | Style | Example pattern |
|---|---|---|---|
| **Exploration** | M1–M2 (low certainty) | Open-ended, conversational. Define the "what." | *"Build a dashboard for [audience] that helps them [goal]."* |
| **Execution** | M3 onwards (high certainty) | Rigid, system-grade instructions. Dictate the "how." | *"Add a 4th screen. Match the attached Asana layout. Navigation: A → B → C. Build in order — screen 1 is the mandatory anchor."* |

**Rule:** Vagueness is a bug. By end of M3, your prompts should look like technical specifications.

---

## 2. Three Common Prompting Traps

Each is solvable with one prompting strategy. Name the trap when you spot it — then apply the fix.

| Trap | Failure mode | Fix |
|---|---|---|
| **🧱 The Mega Prompt** | Database + flow + button animations in one prompt. If the build fails, you can't tell which part broke. | **Prompt Chaining** — build logic first, then design. |
| **🌫️ The Vague Request** | "Build a Dashboard" without defining user state or business rules → generic rectangle that breaks on click. | **Intentionality** — define functionality + path before you hit enter. |
| **🔬 The Micromanager** | Arguing with the AI about hex codes or padding in text. Burns credits, drifts the core logic. | **Multimodal** — don't describe the blue; *show* the blue (upload a screenshot). |

---

## 3. The Execution Toolkit — Three Steps, Three Strategies

You aren't splitting one big prompt into three parts. You're **layering different cognitive strategies in sequence** so precision accumulates without breaking the foundation.

| # | Step | Strategy | How | What it produces |
|---|---|---|---|---|
| 1 | **Expand — Build the Logic** | Chain-of-Thought (COT) | Force the AI to build in strict, dependent order (Screen A → B → C). Use a visual reference for every new screen. | New screens with hard-wired navigation logic. |
| 2 | **Behavior — Define the Flow** | Constraint Grounding | Hard-code if/then triggers for the unhappy path. Exact strings for loading / empty / error states. | A prototype that behaves like real software, not a static mockup. |
| 3 | **Refine — Polish the Design** | Reflection Prompting | Isolate ONE screen. Force the AI to audit and list gaps before editing. End with *"Don't change anything else."* | Surgical UI polish without regression in the rest of the build. |

**COT vs Prompt Chaining:** COT is *how you reason inside one prompt*. Prompt Chaining is *the sequence of prompts you send in order*. They operate at different levels — which is why they combine.

---

## 4. Prompt Chaining in Action — Three Real Prompts

### 1 · Expand (Sequential Logic — COT)

```
Build the next phase of this app in a strict sequence:
1. Add a 2nd screen: "User Settings". Match the layout and spacing of the attached Asana reference.
2. Add a 3rd screen: "Account Activity". Match the data-heavy density of the attached Intercom reference.
3. Navigation: write the logic so User Settings links to Account Activity.

Build these in order so the Settings screen serves as the mandatory anchor for the Activity view.
```

> Notice: each new screen is tethered to a visual North Star. The prompt handles the "how"; the screenshot handles the "where."

### 2 · Behavior (Constraint Grounding)

```
Apply the following logic constraints to the Account Activity flow:
- Use skeleton screens for the transaction list loading state.
- If no data is present, show the empty state: "No activity yet. Start your first project to see data here."
- On fetch failure, trigger the error state: "Connection lost. Please refresh the dashboard."

Maintain the same design language throughout and tether all behavior strictly to these rules.
```

> Notice: exact strings for each state. Hard-coding the unhappy path is what separates a mockup from a product.

### 3 · Refine (Reflection Prompt)

```
The User Settings screen needs a professional Asana-style polish.
1. Start by listing the 3 biggest gaps in typography and spacing compared to the Asana design system.
2. Once you've identified those, resize the headers and update the primary button hex code to match.

Don't change anything else in the project or touch the underlying logic.
```

> Notice: audit first, then act. The "Don't change anything else" line is your insurance policy.

---

## 5. Prompt Chain Debugging — The "Break It" Mindset

When a chain goes off-rails, **diagnose before re-prompting**. Throwing more prompts at a broken chain just compounds the error.

| Step | Move | What you're looking for |
|---|---|---|
| 01 | **Read the Chain** | Open the actual text of your previous 3 prompts. Did you give a "Never" rule in Prompt 1 that contradicts Prompt 3? |
| 02 | **Compare the Output** | What's the delta between what you asked for and what was produced? Logic miss, or context clutter? |
| 03 | **Diagnose** | Identify the one specific point of failure. Did the AI ignore a constraint? Did it lose the design thread? Isolate **one variable**. |
| 04 | **Fix It** | Revert to the last stable state. Re-prompt with a cleaner, more targeted instruction that addresses the specific framing error. |

**The 5+ prompt rule:** If you're 5 or more prompts deep on the same issue, the problem isn't the tool — it's your framing. Stop, read your own chain, find the contradiction.

---

## 6. The Prompt Chain Workflow — End-to-End

| Step | What you do | Where it lives |
|---|---|---|
| 1 | Generate a README of your M2 build | Lovable → GitHub |
| 2 | Audit your prototype (3–5 flow gaps · 3 friction points · 1 UI target) | Prompt Chain Planner |
| 3 | Draft Expand · Behavior · Refine using the templates | Prompt Chain Planner |
| 4 | Peer cold-read (3 min silent) → capture feedback | `03-prompt-chaining/swap-notes.md` |
| 5 | Execute the chain in order, log each result | Lovable + Planner |
| 6 | Save `PROMPTS.md` to your GitHub repo | Lovable → GitHub |
| 7 | Add this chain to your Living Prompt Pack | Living Prompt Pack Builder |

---

## 7. Voice Calibration — Exploration vs Execution Language

| You want to say | Reframe it as |
|---|---|
| "Build a dashboard for retention." | *"Add a Retention Dashboard (Screen 4). Match the attached Mixpanel layout. Include: Day-3 invite rate, retention comparison, onboarding completion, users-not-yet-invited."* |
| "Make it look professional." | *"Match the attached Asana reference. List the 3 biggest typography gaps before touching code, then resize headers and primary buttons to match."* |
| "Handle errors gracefully." | *"On fetch failure, trigger the error state: 'Connection lost. Please refresh the dashboard.' On no data, show: 'No activity yet. Start your first project to see data here.'"* |

---

## 8. The Identity Move

| You were | You are |
|---|---|
| A prompt-sender expecting the AI to fill in the gaps | An architect dictating system rules the AI must obey |
| Rage-prompting until something works | Diagnosing your own chain before re-prompting |
| A one-shot vibe builder | A reproducible chain author whose prompts a teammate could re-run |

Three prompts. Three strategies. One resilient build.
**The chain is the IP — your build is the receipt.**
