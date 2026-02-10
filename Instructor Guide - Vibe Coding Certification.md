# Instructor Guide: Vibe Coding Certification

This is the companion document to the **Vibe Coding Certification - Course Strategy and Outline**. That document defines *what* we teach. This one defines *how* to deliver it.

---

## How to Use This Guide

**Philosophy:** Labs first, teaching second. Your job is to get students building as fast as possible, then name what they just experienced. If you're running behind, cut the lecture -- never the lab.

**Structure:** Each module has a minute-by-minute timing plan. Follow the times as closely as possible, but use the buffer flexibly. The buffer is your safety net for Q&A, tool issues, and organic discussion.

**One rule above all:** Every student should be building something in every module. If you look around the room and people are watching instead of building, something has gone wrong.

---

## Pre-Class Checklist

Complete these before the first live session:

### 1 Week Before Course Start

- [ ] **Lovable Pro accounts:** Verify that all enrolled students have received their Pro account activation. Follow up with any who haven't. This is the #1 friction point from past cohorts.
- [ ] **Slack channel:** Cohort Slack channel is created and all students are invited. Post a welcome message linking to the pre-work instructions.
- [ ] **Pre-work instructions:** Distribute the pre-work guide (tool setup, first build, Confidence Line primer, Slack intro). Set a deadline of 24 hours before M1.
- [ ] **Problem briefs:** Prepare all problem briefs for M1-M5 labs. Each should be real, messy, and ambiguous (not sanitized textbook problems). Have both 0-to-1 and existing-product briefs ready for M2.
- [ ] **Demo prototypes:** Pre-build your M1 opening demo prototypes. You will deliver them as if live, but having them pre-built means you can recover gracefully if the tool has issues during class. Have backup screenshots/recordings ready.
- [ ] **Alternative tool familiarity:** Be ready to show at least one alternative tool (Bolt, v0, or Cursor) briefly in each module. You don't need to be an expert -- just enough to show "this works here too."

### Day of Each Session

- [ ] **Check Lovable status:** Is the tool up? Any known outages? Have a backup plan (Bolt, v0) if Lovable is down.
- [ ] **Pre-work completion:** Check the Slack channel -- how many students posted their pre-work intro? If <70% completed, plan 5 extra minutes at the start of M1 for quick setup.
- [ ] **Test your demo:** Run through your opening demo to make sure it still works. AI tools update constantly.
- [ ] **Timer ready:** Use a visible timer (on-screen or physical) for lab segments. Students appreciate knowing how much time they have.

---

## Per-Module Delivery Guide

### Pre-Work (Module 0) -- Async

**Your role:** Monitor, don't teach.

- Post the pre-work instructions in Slack 1 week before M1
- Respond to any setup questions in Slack within 24 hours
- 24 hours before M1: check completion rate. If students haven't posted, send a direct reminder
- Note: some students will not do pre-work. That's okay. M1 has buffer time for this. Don't shame them -- just make sure they get set up in the first 5 minutes of M1.

---

### Module 1: Dive In -- Your First Full Cycle

**Total time:** 2 hours (120 min)

| Time | Duration | Activity | Notes |
| --- | --- | --- | --- |
| 0:00 | 3 min | Welcome + housekeeping | Quick intro. Don't over-explain the course. "You'll learn by doing. Let's start." |
| 0:03 | 12 min | **Opening Demo** | Live-code 3 different prototypes from one ambiguous problem. No slides. No explanation. Just build. Show speed. Show divergence. Aim for gasps. |
| 0:15 | 15 min | **Lab: Individual build** | Hand out the ambiguous problem brief. "Open your tool. Build one direction. Go." Walk the room. Help stragglers with tool setup (pre-work non-completers). |
| 0:30 | 15 min | **Lab: Show and test** | Pair students up. Partner A walks through Partner B's prototype as a "user." Then swap. Observe reactions. |
| 0:45 | 10 min | **Lab: Decide** | Each student writes: what did I learn? Double down, pivot, or kill? Share with class. **Celebrate the best "kill" decision.** |
| 0:55 | 15 min | **Retroactive Framework** | NOW introduce the Confidence Line, "Tool vs Toy," and the tool landscape. "Here's the framework that names what you just experienced." |
| 1:10 | 10 min | **Break It exercise** | Demo what happens with no problem frame. AI builds the wrong thing beautifully. Lesson: speed without direction = waste. |
| 1:20 | 40 min | **Buffer** | Use for: Q&A, extended discussion, second mini-build if energy is high, tool troubleshooting, or early dismissal if the group is sharp. |

**If running behind:** Cut the Retroactive Framework to 8 min (just the Confidence Line, skip tool landscape). Never cut the lab.

**Common failure modes:**
- Students can't log into Lovable -> Have them use Bolt (no account needed for basic use) or pair with a neighbor
- Opening demo falls flat -> Have backup screenshots or a pre-recorded 2-min video of a fast build
- Students finish the build in 5 minutes -> Challenge them: "Now build a completely different direction for the same problem"
- One student dominates the "Decide" discussion -> Ask quieter students directly: "What did you decide to kill, and why?"

---

### Module 2: What Are You Actually Testing? -- Problem Framing and Validation Design

**Total time:** 2 hours (120 min)

| Time | Duration | Activity | Notes |
| --- | --- | --- | --- |
| 0:00 | 5 min | Recap M1 + frame M2 | "M1 proved you can build fast. M2 teaches you to build smart." |
| 0:05 | 15 min | **Teaching: Problem framing** | Reforge's method, assumption mapping, fidelity mapping. Keep it concise -- these are tools they'll use in the lab immediately. |
| 0:20 | 10 min | **Lab: Frame first** | Students choose Brief A (greenfield) or Brief B (existing product). Write the assumption, build plan, fidelity choice, and success criteria BEFORE touching any tool. |
| 0:30 | 15 min | **Lab: Individual build** | Build with intent. They're testing a specific assumption, not "building something cool." |
| 0:45 | 15 min | **Lab: Peer validation** | Swap prototypes. Does this actually test what the builder claimed? Structured debrief. |
| 1:00 | 10 min | **Break It exercise** | Beautiful prototype that validates nothing vs. ugly prototype that answers the question. |
| 1:10 | 50 min | **Buffer** | Use for: deeper assumption mapping exercise, existing-product scenario deep dive, extended peer discussions, or a second rapid build round. |

**If running behind:** Cut the teaching to 10 min (skip fidelity mapping detail -- they'll learn it by doing). Never cut Frame First -- that's the whole point of M2.

**Common failure modes:**
- Students skip the "Frame first" and jump to building -> Stop them. "You have to write the assumption first. If you can't name what you're testing, you're building a toy."
- Brief B (existing product) confuses students -> Walk them through one example: "The dashboard has a 60% bounce rate. What's the riskiest assumption? Maybe it's that users don't understand the first chart they see."
- Peer validation is too nice ("looks great!") -> Give them the specific prompt: "Does this prototype actually test the assumption they named? Yes or no. If no, what does it actually test?"

---

### Module 3: Precision Prompting -- Communicating Product Intent to AI

**Total time:** 2 hours (120 min)

| Time | Duration | Activity | Notes |
| --- | --- | --- | --- |
| 0:00 | 5 min | Recap M2 + frame M3 | "You can build fast and smart. Now let's get precise." |
| 0:05 | 10 min | **Teaching: Precision prompting** | Prompting maturity curve, context layering (including for existing products), living prompt packs. Brief agentic prompting intro. |
| 0:15 | 25 min | **Lab: Individual precision build** | Moderately detailed brief. Build using deliberate multi-step prompting. Document your prompt chain. |
| 0:40 | 15 min | **Lab: Peer review** | Swap prompt chains. Can another person reproduce a similar result? Discussion on portability. |
| 0:55 | 10 min | **Break It exercise** | Live diagnosis of a prompt failure from a student's prototype. |
| 1:05 | 55 min | **Buffer** | Use for: extended prompt debugging, agentic prompting demo, context layering for existing products deep dive, prompt pack workshop. |

**If running behind:** Cut the teaching to 7 min. The lab IS the teaching in this module.

**Common failure modes:**
- Students don't document their prompts -> Remind them at the start: "You'll swap with a partner. If they can't follow your prompt chain, you'll know it wasn't precise enough."
- Prompt chains are too short (1-2 prompts) -> Challenge: "Can you break this into 5+ steps? What context is missing?"
- Agentic prompting confuses less technical students -> Frame it simply: "Instead of telling the AI each step, you describe the goal and let it figure out the steps. Like delegating to a junior dev."
- Peer review is superficial -> Give them the rubric: "Could you reproduce this result in a different tool using only this prompt chain? What's missing?"

---

### Module 4: From Vibe to Structure -- The Graduation Moment

**Total time:** 2 hours (120 min)

| Time | Duration | Activity | Notes |
| --- | --- | --- | --- |
| 0:00 | 5 min | Recap M3 + frame M4 | "You can build fast, smart, and precisely. Now: when do you stop exploring and commit?" |
| 0:05 | 10 min | **Teaching: The Graduation Moment** | Signals to graduate, 73% failure stat, comprehension debt. Living spec concept. Graduating within existing products. |
| 0:15 | 25 min | **Lab: Graduate your prototype** | Take M3 prototype. Write the living PRD (extracted, not planned). Refactor the codebase for structure. |
| 0:40 | 15 min | **Lab: Group share** | Small groups compare living PRDs. What's different between 0-to-1 specs and existing-product feature specs? |
| 0:55 | 10 min | **Break It exercise** | Product that never graduated from vibe coding. 500+ prompts deep, unmaintainable. |
| 1:05 | 55 min | **Buffer** | Use for: extended refactoring time, PRD workshop, discussion on when THEIR real projects should graduate, debugging practice. |

**If running behind:** Cut the teaching to 7 min (just the graduation moment concept + 73% stat). The lab is essential.

**Common failure modes:**
- Students don't know what to put in their living PRD -> Give them the template: "What does this do? Who is it for? What assumptions did it validate? What's the recommended direction? What's hacked vs. real?"
- Refactoring feels too technical -> Frame it as "asking AI to clean up." Show one example: "Rename all the components to make sense. Separate the data logic from the display logic."
- Students who built greenfield and students who built existing-product don't have much to compare -> That's the point. The contrast in the group share is the learning moment.

---

### Module 5: Real-World Complexity -- Integrations, Edge Cases, and the Engineering Handoff

**Total time:** 2 hours (120 min)

| Time | Duration | Activity | Notes |
| --- | --- | --- | --- |
| 0:00 | 5 min | Recap M4 + frame M5 | "Your prototype is structured and spec'd. Now make it real." |
| 0:05 | 10 min | **Teaching: Integration reality** | API patterns, edge case thinking. Brief MCP demo (2 min, show don't teach). Engineering handoff framing. |
| 0:15 | 30 min | **Lab: Integration sprint** | Add API integration + handle 2 edge cases + write engineering handoff note. Individual builds. |
| 0:45 | 10 min | **Lab: Chaos round** | Trigger a chaos event. Students handle failure gracefully. Group discussion. |
| 0:55 | 10 min | **Break It exercise** | Prototype with zero error handling. Class identifies all the ways to break it. |
| 1:05 | 5 min | **Engineering handoff discussion** | "How would you present this to your engineering team? What do they need from you?" |
| 1:10 | 50 min | **Buffer** | Use for: extended integration time (APIs are unpredictable), deeper engineering handoff role-play, edge case brainstorming, M6 prep discussion. |

**If running behind:** Cut the MCP demo. Cut the Break It to 5 min. Protect the integration lab and chaos round.

**Common failure modes:**
- API integration fails for technical reasons -> Have a "mock API" backup (a simple JSON endpoint) that always works. Students can switch to this if real APIs are down.
- Students get stuck on auth -> Pair them with someone who's done it before. Or show the 3-line prompt that sets up Supabase auth.
- Chaos round doesn't create enough chaos -> Make it dramatic: "Your database just returned every user's data to every other user. What do you do?"
- Engineering handoff feels abstract -> If any students are engineers or have worked closely with engineering teams, ask them to role-play the "engineer receiving this prototype."

---

### Module 6: Ship It -- Deployment, Scale, and Stakeholder Buy-In

**Total time:** 2 hours (120 min)

| Time | Duration | Activity | Notes |
| --- | --- | --- | --- |
| 0:00 | 5 min | M6 kickoff + group formation | Form groups of 3-4. Distribute project briefs. "You have 55 minutes. Go." |
| 0:05 | 55 min | **Lab: Group build sprint** | Groups build from zero. Each member works on their own tool instance. They coordinate via shared living PRD. Walk the room -- make sure everyone is building, not watching. |
| 1:00 | 10 min | **Deploy** | Each group deploys to a live URL. Help with deployment issues. This should be fast. |
| 1:10 | 30 min | **Present and compete** | Structured pitch: problem, validation journey, live demo, recommendation. Audience tries to break it during demo. Class votes on best product + best pitch. |
| 1:40 | 10 min | **Wrap-up** | Confidence Line revisited. Individual deliverables reminder. What to do tomorrow at work. |
| 1:50 | 10 min | **Buffer** | Presentation overruns, deployment issues, final Q&A. |

**Large cohort contingency (>30 students):**
- Limit presentations to 4 groups (selected by peer vote: "Which group's product do you most want to see?")
- Remaining groups do a gallery walk: everyone visits each deployed URL, leaves feedback on a shared doc
- Gallery walk takes 15 min, replaces some of the presentation time

**If running behind:** Cut the wrap-up to 5 min. Never cut the presentations -- that's the culmination of the course.

**Common failure modes:**
- One group member dominates the build -> Check in at 15 min and 30 min. Ask each member: "What are YOU building?" If someone isn't building, reassign them a specific component.
- Deployment fails -> Have Vercel/Netlify deploy instructions as a 1-page cheat sheet. If a group truly can't deploy, let them present from localhost with a note that deployment is "in progress."
- Presentations are too long -> Enforce the time strictly. Use a visible timer. "You have 5 minutes. When the timer goes, you stop."
- "Break It" during presentations is too gentle -> Seed the audience with specific attacks: "Try entering a 10,000-character name." "Hit the back button 5 times fast." "Open it on your phone."

---

## Tool Troubleshooting FAQ

| Issue | Quick Fix |
| --- | --- |
| Student can't log into Lovable | Check Slack for account activation link. If not received, switch to Bolt for this session. |
| Lovable is down / slow | Switch to Bolt (bolt.new). Similar UX, no migration needed. |
| Student's build is stuck / spinning | Clear the chat and start a new thread. If persistent, try a different browser. |
| Credit/token limit hit | Pro accounts should prevent this. If it happens, the student is sending very long prompts -- help them break into smaller steps. |
| Student wants to use Cursor instead | That's fine. Acknowledge it, but don't teach Cursor-specific steps. The methodology is the same. |
| AI generates broken code | This is normal. Show the student how to describe the error back to the AI. "I got this error: [paste]. How do I fix it?" |
| A student's prototype looks nothing like what they described | Prompt issue. Help them break the request into smaller, clearer steps. This is actually a great learning moment for M3. |
| Deployment fails in M6 | Have a 1-page Vercel deployment cheat sheet ready. Alternatively, use Lovable's built-in hosting (Publish button). |

---

## Cohort Size Adaptations

### Small cohort (< 20 students)

- Pair work instead of groups for peer review (M1-M5)
- M6 groups can be 2-3 instead of 3-4
- All groups present (no gallery walk needed)
- More time for individual attention during labs
- Instructor can do more live debugging with individual students

### Medium cohort (20-30 students)

- This is the sweet spot. Follow the guide as written.
- M6 groups of 3-4
- All groups present if time allows; use gallery walk for any overflow

### Large cohort (30-50 students)

- Peer review works in pairs, not groups
- M6 groups of 4 (no more) -- this gives you 8-12 groups
- Limit M6 presentations to 4-5 groups (peer-voted), gallery walk for the rest
- Consider a teaching assistant to walk the room during labs
- Labs may need 5 extra minutes -- use buffer
- "Break It" exercises work better as whole-class discussion rather than pair work

---

## Assessment Rubric

### Validation Evidence Brief (Group Deliverable, M6)

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Assumption named** | Specific, testable assumption clearly stated | Assumption stated but vague | No clear assumption |
| **Evidence quality** | Prototype directly tested the assumption; clear data | Prototype loosely related to assumption | Prototype didn't test anything specific |
| **Recommendation** | Clear ship/pivot/kill with reasoning tied to evidence | Recommendation given but reasoning weak | No recommendation or not tied to evidence |
| **Presentation clarity** | Compelling 5-min pitch; audience understood the journey | Adequate presentation; some confusion | Disorganized or unclear |

### Prompt Library (Individual Deliverable)

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Quantity** | 8+ reusable prompts across multiple categories | 5-7 prompts | Fewer than 5 |
| **Reusability** | Prompts are context-rich and could be used by another PM | Prompts work but are specific to one project | Prompts are one-off, not reusable |
| **Documentation** | Each prompt has: purpose, when to use, expected output | Some documentation | No documentation |

### Living PRD (Group Deliverable, M6)

| Criterion | Excellent (5) | Good (3) | Needs Work (1) |
| --- | --- | --- | --- |
| **Extracted, not planned** | Clearly shows what was learned from building | Mix of pre-planned and extracted | Written before building; doesn't reflect learnings |
| **Evolution visible** | Shows how the spec changed across modules | Some evolution noted | Static document |
| **Engineer-readable** | An engineer could pick this up and understand what to build | Mostly clear with some gaps | Would need significant clarification |

---

## Quick Reference: What to Skip if Running Behind

Every module has a priority order. If you're running behind, cut from the bottom:

1. **Never cut:** The lab (individual build + peer interaction)
2. **Cut last:** The "Break It" exercise (shorten to 5 min if needed)
3. **Cut second:** Extended discussion / Q&A
4. **Cut first:** Teaching/lecture segments (students learn more by doing)

The buffer time in each module is designed to absorb 30-50 minutes of overflow. If you're consistently using all the buffer, you're probably lecturing too long. Trust the labs.
