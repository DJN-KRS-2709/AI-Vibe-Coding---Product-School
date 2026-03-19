# Module 2 — Instructor Demo: Step-by-Step

> For the instructor only. Run this as a live demo on screen share.
> Total time: ~8 minutes. Pre-build both versions before class.
> Instructor demo: **The Customer Vibe — Retention Engine** (B2B PM SaaS — 30% churn, team invites — carried through M2/M3/M4/M5 demos)

---

## SETUP (before students arrive)

- [ ] Open the M1 prototype in Lovable (the polished version from M1 — Mobbin-matched design, interactive components, professional layout, but ALL placeholder data)
- [ ] Have the context-injected version pre-built in a separate Lovable project as backup
- [ ] Have the context injection prompt pre-typed in a text file, ready to paste
- [ ] Have both Lovable projects open in separate browser tabs (so you can show side-by-side at the end)
- [ ] Screen share on — students should see everything

---

## STEP 1: Show the Facade (~2 min)

**What you do:** Click through the M1 prototype on screen share. Show all the key screens — the onboarding flow, the dashboard, any interactive components. It looks polished — Mobbin-matched, professional layout, clickable buttons.

**What you say:** "This is the prototype from Module 1. Clean design, Mobbin-matched, interactive components — it looks like a real product. Pretty impressive for one session's work."

**Then ask the room:** "What assumption is this testing?"

**Pause. Let the silence land. Wait 5-10 seconds.**

**What you do next:** Demonstrate the facade. Point to the charts — "See these numbers? Where did they come from? Nowhere. They're hardcoded." Point to any copy in the UI — "These labels? Placeholder text. No real user data." Point to the metrics — "And these charts? Generic sample data that means nothing."

**What you say:** "If your VP asked 'what did you learn from this?' — what would you say? 'It looks nice'? That's not a product insight. That's interior design. This prototype looks like a product. But it proves nothing."

---

## STEP 2: Inject Context (~3 min)

**What you say:** "I'm going to rebuild this with three ingredients: a hypothesis, real data, and real user voice. Watch what changes."

**What you do:** Open Lovable (either in the same project or a new one). Paste the prompt below.

**While it generates:** "Watch the difference. Same tool. Same time. But this prompt has a hypothesis, real retention data, a named constraint, and actual user quotes baked in."

**When it's done:** Click through the three onboarding screens and the experiment summary.

---

## STEP 3: Name the Difference (~2 min)

**What you do:** Open both versions in separate tabs. Click between them — or put them side-by-side if your screen allows it.

**Point to the M1 version:** "This one — placeholder data, hardcoded charts, generic copy. It looks like a product. But what question does it answer? None."

**Point to the context-injected version:** "This one — 12% Day-3 invite rate displayed on screen, real user quotes from interviews, a named hypothesis about surfacing invites during onboarding. It even has an experiment plan and success criteria built in. It's testing a specific assumption: does making the invite flow prominent in onboarding change retention?"

**What you say:** "Same tool. Same amount of time. The only difference is the inputs. Three ingredients: a hypothesis, real data, and user voice."

**Then the bridge:** "The first one generates applause. The second one generates evidence. That's the shift we're making today. You're going to do exactly this to your own build — with your own scenario, your own data, and your own hypothesis."

---

## STEP 4: Transition (~1 min)

**What you say:** "But before you build, I want you to feel the gap in your own work. Open your M1 prototype right now. Let's see where it stands."

**Transition to Slide 7 — Reflection Moment.**

---

## THE PROMPT (copy-paste version)

For quick reference, here's the prompt ready to paste into a text file before class:

```
Build a 3-screen onboarding flow for a B2B project management SaaS that prominently surfaces team invitations within the first 3 steps.

Context: Company is 18 months old, Series A, 5,000 paying teams, 4.2M ARR. 30 percent of new customers churn within 90 days. The board requires measurable improvement this quarter.

Data shows: Users who invite a teammate within the first 3 days retain at 68 percent. Users who do not invite retain at only 22 percent. Only 12 percent of new users send an invite in the first 3 days. The invite button is currently buried in Settings > Team > Members. 60 percent of new users never create their first task.

Constraint: No engineering resources for 6 weeks. Prototype only. Must work within the existing product surface.

Hypothesis: If we surface team invites prominently during first-run onboarding, day-3 invite rate increases from 12 percent to 25 percent.

User insight: Retained user: "When I invited my co-founder on Day 2, that's when it clicked. It's a team tool." At-risk user: "I tried to invite my team but it asked for role and department. I don't know that. I just want to add them."

Instructions: Design a 3-screen onboarding flow with the goal of increasing early team invites.

Screen 1: Reframe the product as a team tool. Make the value of collaboration explicit.
Screen 2: Make inviting teammates the primary call to action. Remove friction such as role and department requirements.
Screen 3: Reinforce activation by showing how collaboration unlocks value — shared tasks, comments, progress visibility.

Design principles: Make the invite action feel lightweight and immediate. Do not add new backend functionality. Assume the invite system already exists. Reduce cognitive load. Make the team invite feel like the default next step.

Include: Clear headline and microcopy. Primary and secondary CTAs. Minimal UI elements. Simple visual hierarchy.

Display these metrics visually within the prototype to anchor urgency: Day-3 invite rate: 12 percent. 90-day retention with invite: 68 percent. 90-day retention without invite: 22 percent. 90-day churn overall: 30 percent. Target: reduce churn to 15 percent.

After the 3 screens, include: The single riskiest assumption behind this intervention. A lightweight experiment plan to validate it within 2 weeks. Success criteria and leading indicator metrics.

Output format: Clickable web onboarding prototype with 3 distinct screens plus experiment summary.
```

---

## WHAT TO PRE-BUILD (the night before)

1. **The M1 version (the facade):** Your existing M1 prototype — polished UI, Mobbin-matched, but all placeholder data. This should already exist from your M1 demos.

2. **The context-injected version (the payoff):** Run the prompt above in Lovable. Make sure it generates clean output with:
   - The retention data visible on screen (12% invite rate, 68% vs 22% retention split)
   - At least 1-2 user quotes displayed in the UI
   - The 3-screen onboarding flow clearly progressing: team value → invite action → collaboration payoff
   - The experiment summary with the riskiest assumption, validation plan, and success criteria
   - Metrics visually anchored (not buried in small text)

3. **Have both open in separate browser tabs** so you can switch instantly during the demo.

4. **Deliver the context-injected version as if you're building it live** — paste the prompt, let it generate. But if it fails or produces weak output, switch to the pre-built backup. Say: "Let me show you the one I built earlier with this exact prompt" and switch tabs.
