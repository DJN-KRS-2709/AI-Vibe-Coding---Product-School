# Iteration-Sprint-Brief.md — Template

> **What this is.** The structure your M6 lab artefact follows: the inputs you fed into the AI, the analysis it gave you back, the *one* finding you picked, the prompt you ran in Lovable, and the verification + redeploy log.
>
> **Where it lives in your repo.** Push the populated file to `06-iteration/Iteration-Sprint-Brief.md` alongside your `04-structure/PRD.md`, `05-integration/Integration-Plan.md`, and the updated `HANDOFF.md`. This is the canonical record of your first measured iteration.

---

## Section 1 — Sprint Context

| Field | Value |
| --- | --- |
| Sprint date | _e.g. 2026-05-21_ |
| Live URL (pre-sprint) | _https://your-prototype.lovable.app/_ |
| Live URL (post-sprint) | _same URL — your changes redeploy to the same address_ |
| Time invested | _e.g. 15 minutes (one M6 lab)_ |

---

## Section 2 — Inputs

The four things you fed into the AI analysis. Keep this section verbatim — it's the audit trail for the finding you ship.

### 2.1 Problem statement (from M2 Living PRD)

> _One sentence. Copy from `04-structure/PRD.md` — do not paraphrase._

### 2.2 Hypothesis (from M2 Living PRD)

> _Your original M2 prediction about how users would behave._

### 2.3 Lovable Insights metrics — baseline

| Metric | Value | What it told you |
| --- | --- | --- |
| Visitors | _e.g. 27_ | _Unique users who reached the product._ |
| Page Views | _e.g. 84_ | _Total pages viewed across all sessions._ |
| Views Per Visit | _e.g. 3.1_ | _Depth — how many screens an average user explored._ |
| Duration | _e.g. 1m 42s_ | _Average session length._ |
| Bounce Rate | _e.g. 48%_ | _% who left without interacting — entry-screen quality._ |

### 2.4 Peer feedback (from Slack `#cohort-channel`)

Paste every labelled comment you received on your URL thread. Keep the labels — they help the AI weight the signal.

- 🐛 **Bug** — _e.g. "I clicked 'Send Invite' and nothing happened — the form just stayed open."_
- 🤔 **Friction** — _e.g. "I wasn't sure what 'Track Status' meant — it sounded like it would email me."_
- 🤩 **Compliment** — _e.g. "The empty state was so clear — I knew exactly what to click first."_
- 💡 **Feature Idea** — _e.g. "It would be great to bulk-import contacts from CSV."_
- _add a row per comment_

---

## Section 3 — Strategic Analysis Prompt + AI Response

### 3.1 The exact prompt you sent

Paste the final, expanded version of the [Strategic Analysis Prompt](../Modules/Module%206%20-%20Frameworks%20Reference%20Card.html) you sent — with placeholders replaced by your real inputs from Section 2.

```
I built a product to solve this problem: [your problem statement].
My hypothesis was: [your hypothesis].
Here are the metrics from my deployed product (Lovable Insights):
[your five metric values]
Here is the feedback I received from peer users in Slack:
[your peer comments, with labels]
Evaluate: ...
```

### 3.2 The AI's response — ranked backlog (Top 3)

| Rank | Finding | Pattern | Why the AI ranked it here |
| --- | --- | --- | --- |
| **1** | _e.g. "62% bounce rate on the landing screen — the value prop isn't clear in 5 seconds."_ | Persona Refinement | _"Hero copy is verbose; bounce + 'Friction' comments both point at the same friction."_ |
| 2 | _e.g. "Users sign up but don't reach Track Status — the navigation label is unclear."_ | Visual Branching | _"3 of 4 peers flagged the same label confusion."_ |
| 3 | _e.g. "Duplicate submissions allowed when users double-click 'Send'."_ | Guardrail | _"Edge case from peer testing; not a top-impact fix this sprint."_ |

### 3.3 The honesty check

| Question | Answer |
| --- | --- |
| Is this product solving the problem? | _Yes / No / Partially. One sentence on the AI's evidence._ |
| Hypothesis confirmed or contradicted? | _Confirmed / Contradicted / Partial. One sentence._ |
| If contradicted, is V2 a tweak or a pivot? | _Tweak / Pivot. One sentence._ |

---

## Section 4 — The One Finding You Picked

You picked one. Not three. Write the chosen finding in your own words plus why it beat the other two.

### 4.1 The chosen finding

> _e.g. "Bounce rate of 62% on the landing screen is the single largest source of friction. Fixing it should compound — every downstream metric improves with more users staying past 5 seconds."_

### 4.2 The pattern it maps to

- [ ] 🧠 **Persona Refinement** — copy / voice / framing fix
- [ ] 🔀 **Visual Branching** — change the mental model
- [ ] 🛡️ **Guardrail** — enforce an IF/THEN rule

### 4.3 Why this over the other two

> _Two sentences max. e.g. "Finding #2 depends on Finding #1 being solved first (you have to land users before navigation matters). Finding #3 affects ~5% of submissions — a fix worth doing in week 2, not now."_

---

## Section 5 — The Lovable Implementation Prompt

The actual prompt you pasted into Lovable. Starts with **"Based on the user data showing..."** — no exceptions.

```
Based on the user data showing [specific finding from Section 4.1],
update [specific component / screen] to [specific change].
Keep all existing functionality and component structure working.
Change only [the scoped piece this prompt touches].
```

> Tag the pattern used (Persona / Branching / Guardrail) inline so the next sprint can pattern-match against it.

---

## Section 6 — Verification + Redeploy Log

### 6.1 Did the change work?

- [ ] **Yes** — the friction the AI flagged is visibly resolved.
- [ ] **Partially** — re-prompted (see Section 6.2 below).
- [ ] **No** — reverted, did not redeploy. (Recorded as a known gap below.)

### 6.2 Did anything else break?

| Check | Status | Notes |
| --- | --- | --- |
| Core flow still works (sign-up → main action → result) | ✅ / ❌ | _One line._ |
| Pre-existing data still displays | ✅ / ❌ | _One line._ |
| RLS / auth from M5 still enforces user isolation | ✅ / ❌ | _One line._ |
| No new console errors on the changed screen | ✅ / ❌ | _One line._ |

### 6.3 Re-prompts (if any)

If Lovable's first pass broke something, log the recovery prompts you ran here. Future you will thank current you.

```
e.g. "The last change broke the Send Invite button on the dashboard.
Restore the working button behaviour while keeping the new hero copy."
```

### 6.4 Redeploy

| Field | Value |
| --- | --- |
| Redeployed | ✅ Yes / ❌ No (gap documented) |
| Redeployed URL | _same as Section 1 — confirm it resolves_ |
| Tested in incognito | ✅ / ❌ |
| Tested on mobile | ✅ / ❌ |

---

## Section 7 — What You'd Run Next Sprint

The single most senior thing you can write in this brief is what you'd measure or fix *next* week — if anyone (including you) ever runs this loop again.

### Next sprint candidate findings

1. _e.g. Finding #2 from Section 3.2 — now that bounce is below 30%, the Track Status navigation friction becomes the top issue._
2. _e.g. Add Layer 2 (GA4) so we can see traffic sources, not just session counts._
3. _e.g. Add Layer 3 — a "Report Issue" capture wired to Supabase — so we own the sentiment data._

### What you'd measure first

- _e.g. "Bounce rate on landing screen — re-baseline in 7 days. Target: under 35%."_
- _e.g. "Track Status visit rate — currently 12% of sessions. Target: 40%+ if Finding #2 ships."_

---

> **Done.** Commit this file to `06-iteration/`. Your GitHub repo is now the full story of one closed build-measure-iterate loop — from problem statement (M2) to a measured, redeployed product (M6). That repo is your portfolio piece.
