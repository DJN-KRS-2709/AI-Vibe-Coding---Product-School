# Module 6: Measure Product Performance for AI-Driven Iteration — Speaker Notes

---

## Slide 1 — Title

Welcome to Module 6. I want to take a second to recognize where you are. You've shipped a live product. It has a real URL. Real people have been clicking around in it. That's not nothing. Most PMs spend months in planning and never get to this point.

Today we close the loop. The question we've been building toward since Module 2 — "is my product actually solving the problem?" — we answer it with data today. Not a gut feeling. Not a stakeholder's opinion. Data from real user behavior on your real deployed product.

Let's go.


## Slide 2 — Class Expectations

You know the drill by now.


## Slide 3 — Syllabus

As mentioned, today we close the loop. You measure what your product is actually doing, use AI to analyze the data against your original problem statement, make one evidence-based improvement, and present the full journey. This is the final stage of the product lifecycle.


## Slide 4 — Agenda

Four things today.

First — Shift From Shipping to Proving With Data. We'll look at why the moment your product goes live, the game changes completely.

Second — Read your Lovable Insights. Your product has been collecting data since you deployed in M5 — you're going to open it and understand what it's telling you.

Third — AI-Driven Product Iteration. You'll use AI to analyze your data against your problem statement and identify the highest-impact improvement. And then in the hands-on lab, action improving your product.

And lastly — the final stretch. Presenting.


## Slide 5 — Shift From Shipping to Proving With Data

In Module 5, shipping was the win. You got the live URL, you tested it on your phone, you posted it in Slack. That felt like the finish line. It wasn't. That was the starting gun for a different race. Today you run that race.


## Slide 6 — Rapid-Fire Feedback Loop

Before we get into the weeds, I want you to collect one more layer of input — human feedback from your peers. Not a survey. Not a form. Real usage.

Go to the cohort Slack channel. Find at least four classmates' deployed product links. Open each one as a real user — sign up with your email, test the core flow, try to break things. Then leave one piece of specific feedback for each product in the same thread as the link, tagged to the builder.

Specific is kind. "I was confused when I clicked Submit and nothing happened on the confirm screen" is useful. "Looks good" is not. You can leave a bug, flag friction, pay a compliment, or pitch a feature idea — but make it specific enough that the person can actually do something with it.


## Slide 7 — The Iteration Mindset

Most PMs are taught to build, launch, and move on to the next thing. There's always another feature waiting. But that instinct — as natural as it feels — means you never actually find out if what you built worked. You just keep stacking new things on top of something that might be broken.

Every V1 has ghost features. Things you were completely convinced were going to be the core of the product — and nobody touches them. The data tells you which 20% is driving 80% of the value so you can stop wasting time on the rest.

And here's the uncomfortable truth: you are the worst person to spot the friction in your own product. You built it, it's your baby. You know exactly how it works. Real users don't have that context — and their confusion is the most valuable signal you have.

But the most important shift is this one. You defined a hypothesis in Module 2. You built something to test it. You shipped it. Now you find out if you were right. Not with a feeling. Not with a stakeholder's opinion. With data. That's the only objective verdict that matters.

From this point forward, your job is to replace "I think" with "the data shows." That's not a small shift. But that's the role of a real product builder.


## Slide 8 — Metrics That Matter

You don't need 50 metrics to evaluate a V1. You need 3–5 specific signals that map directly to your problem statement. Analysis paralysis is the biggest killer of V2. If you track everything, you'll understand nothing.

Engagement isn't just "how many logins." It's the core flow. If you built a task manager, are users actually creating tasks — or are they clicking Settings and leaving? You need to know which features are anchors and which are ghosts.

Retention is your honesty metric. One-time usage is a fluke. A second session is a signal. If users don't come back, your value proposition didn't stick — or the friction of using the app outweighed the benefit. Be honest with yourself about which one it is.

Quality is where technical friction lives. If your page takes 5 seconds to load, the user is gone before they even see your value. Look for dead ends — places where the user expected a result and got nothing.

And impact circles back to your hypothesis. If you predicted users would do X weekly and the data shows they do it once a month, your impact isn't matching your intent. That's the "so what" of your data.

The question that overrides everything else: does user behavior confirm or contradict your original problem statement? If it contradicts, your next move isn't a tweak — it might be a pivot.


## Slide 9 — Three Layers of Analytics

There are three layers of analytics available to you as a PM, and I want you to know all three exist — but today we're working with the one you already have.

The first layer is built right into Lovable. No setup. It's been collecting data since you deployed in M5. Active users, page views, feature clicks, return sessions. For a V1 analysis, it's enough.

The second layer is external tools — things like Mixpanel — that give you deeper funnel signal: where users are dropping off, where they came from, conversion paths. We're not doing this today, but it's a one-prompt add in Lovable when you're ready for it.

The third layer is custom — feedback collection you build directly into your product and pipe into your own Supabase tables. A "Report Issue" button. A star rating. Data you fully own. That's for when you're running a real pilot.

Today is layer one. You already have the data. Let's go look at it.


## Slide 10 — Lab Section Header

Your product has been collecting data since you deployed in Module 5. We're not adding a new tool. We're opening what's already there. Let's go look at your numbers.


## Slide 11 — Lab: Read Your Lovable Insights

I want one volunteer to share their screen and walk through their Insights panel live — and everyone else opens their own at the same time. You're all doing this together. Here is also the walkthrough guide.

Open your Lovable Insights panel on your deployed project and give it a second to load. The first thing we'll do from now on — this is your baseline, the starting point you'll compare any future iteration against.

Then find three specific numbers: your total sessions or unique visitors, your most-clicked feature or screen, and your lowest-engagement screen or feature. Write them down.

These three are what you're feeding into the AI in the next lab.

Now ask yourself the honest question: is that what you expected? Did your users do what you predicted — or did they do something completely different? Hold that thought. It's the most important thing you're bringing into the analysis sprint.


## Slide 12 — Section Header: AI-Driven Product Iteration

You've got data. Now we figure out what it means. And this is where M6 gets really interesting — because the way you analyze data is about to change completely.


## Slide 13 — AI-Powered Analysis: The PM's New Superpower

Think about the old way. You export CSVs. You build a pivot table. You spend half a day writing a "product insights" document with 14 charts and a seven-page executive summary. By the time you're done, the engineering team has already moved on. You spent the whole sprint producing a document that was out of date before anyone read it.

Now you feed your metrics, your problem statement, and your hypothesis directly into an AI. You get a coherent evaluation in two minutes. Not 50 bullet points — a ranked, prioritized analysis of whether your product is working and what to fix first.

Here's the exact prompt you're going to use:

"I built a product to solve this problem: [Problem Statement]. My hypothesis was: [Hypothesis]. Here are the metrics from my live product after 3 days: [Paste Lovable Insights Data]. Evaluate: Is this product solving the problem? What does the data suggest? What are the top 3 things I should improve, ranked by likely impact?"

And here's the thing I need you to remember: the AI doesn't make the decision — you do. The AI provides the synthesis. You provide the conviction. Your job is to read that analysis and choose the one specific improvement that you believe will move the needle most for your users. That's a judgment call. And judgment is a PM skill, not an AI skill.


## Slide 14 — From Data Signal to Technical Fix

Your AI analysis gives you a diagnosis. It doesn't give you a prescription. That's your job. And there are three types of fixes — each one maps to a different kind of signal.

The first is Persona Refinement. When users tell you the AI output feels vague, or unhelpful, you don't just ask it to "write less." You change the brain. The prompt looks like this: "Based on this data, update the System Persona to 'Efficiency Expert.' Enforce a max 3 sentences rule per response and strictly prioritize quantitative data over prose." You're hardcoding a constraint, not tweaking a copy.

The second is Visual Branching. When your Lovable Insights shows users bouncing or stalling on a complex screen, the mental model might be wrong. You're not moving buttons. You're swapping the entire component. "Based on this data, user behavior shows high friction on the Table component. Replace it with a Kanban Board layout to help users visualize workflow status at a glance." The data proved the current pattern failed — so you replace the pattern entirely.

The third is Logic Guardrails. When Lovable Insights shows users are clicking Submit but the database entry is missing a required field, that's a logic failure, not a UI problem. You write a hard rule: "Based on this data, there is a logic failure in the submission flow. Inject a hard logic guardrail: IF field A is empty, THEN prevent submission and trigger an error toast. Do not attempt to guess the value." You're making the failure impossible, not just harder.

Every prompt you write in this phase starts with "Based on the data..." That's what keeps you honest. You're not feature creeping. You're surgically repairing the exact friction points the data identified.


## Slide 15 — AI-Driven Sprint

All right, let's do those surgical repairs in our own products.


## Slide 16 — Lab: AI-Driven Iteration Sprint

Open your Lovable Insights panel. Copy your key numbers: sessions, user counts, which features got clicks, which screens got ignored. A paragraph of plain numbers is enough. You don't need a spreadsheet.

Then find your problem statement and your Module 2 hypothesis. It's in your Living PRD from Module 4. If you can't find it, write a one-sentence problem statement from memory — you know what your product was trying to solve. Open ChatGPT or Gemini. Use the prompt from the previous slide: "I built a product to solve this problem: [Problem Statement]. My hypothesis was: [Hypothesis]. Here are the metrics from my live product after 3 days: [Paste Lovable Insights Data]. Evaluate: Is this product solving the problem? What does the data suggest? What are the top 3 things I should improve, ranked by likely impact?" Paste in your metrics, your problem statement, your hypothesis. Hit send. Read the full response.

Here's the hardest instruction I'm going to give you today: pick one thing. Not three. Not a small refactor plus a design tweak plus a new feature. One. The data told you what's broken. Your AI analysis ranked it. Pick the top one. Build it and ship it.

Use this prompt pattern: "Based on user data showing [specific finding], update [specific part] to [specific change]. Keep all existing functionality working." That last line matters — it's your safety net. You're improving, not rebuilding.

Paste it into Lovable. Review the change. Does it fix what the data flagged? Does anything else break? Test the core flow before you do anything else. Then redeploy. Your live URL now reflects a data-driven decision. That's not a prototype update. That's a V2. Push all the changes to your GitHub repo.


## Slide 17 — Prepare Your Final Project Deliverables

You've got 15 minutes to finalize your final project deliverables deck.

Your deck needs to tell the full story: the problem you set out to solve and the hypothesis you tested, the key elements of your Living PRD, two or three prompts from your prompt library that were pivotal, a snippet from your engineering handoff, your Lovable Insights screenshot and what the AI analysis told you, and your individual reflection on the build — what surprised you, what you'd do differently.

You're not submitting perfection. You're submitting strategic logic and evidence of learning. Those are two very different things and I want you to focus on the last.


## Slide 18 — Learner Journey

Let's look at what you actually built across six modules.

Module 1 — one prompt, a working prototype in minutes. Speed you'd never experienced before.

Module 2 — you added aim. Risk-based prototyping. A real hypothesis you were willing to be wrong about.

Module 3 — precision. Multi-screen systems with prompt chaining. Consistency at scale. Things stopped breaking.

Module 4 — structure. Your build became something someone else could actually work with. And the best part — Living PRD, engineering handoff for free.

Module 5 — we went live. Real database, real auth, real URL. Your prototype became a product.

Module 6 — today. Measure, analyze, improve. Your product became something that learns.

And that, my friends, is the confidence line in action.


## Slide 19 — Break

Five minutes. You've earned it. Grab some water, come back ready — the best part of the whole course is coming up next.


## Slide 20 — Cameras On

Welcome back. Cameras on — I want to see your faces for the final stretch. This is the good part.


## Slide 21 — Final Project Showcase

Presentation time.


## Slide 22 — LMS Submission Reminder

Quick one — to qualify for certification, you need to upload your final project deliverables into the LMS. You have seven days from today. Everything you need is already built. Don't let the deadline sneak up on you.


## Slide 23 — Presentation Kick-Off

You've got roughly 10 minutes per group. I'll give you a heads up at seven minutes. Here's the structure I want to hear: the problem you set out to solve, the hypothesis you tested, a live demo of your deployed product, what the data told you after it was live, and one honest reflection on the journey from Module 1 to now.

That last part — M1 versus M6 — is the most interesting thing you'll say. Don't skip it.


## Slide 24 — Key Takeaways

Quick story. In 2014, Spotify had over 50 million users and the biggest music library on the planet — but they had a discovery problem. Users were drowning in 30 million songs and defaulting to the same playlist on repeat. Spotify had already shipped Browse pages, editorial playlists, and Related Artists — all designed to help users find new music. All shipped. All had middling engagement. Then a small team at a Spotify hack week built a prototype: a single playlist of 30 songs, personalized to each user, refreshed every Monday. They called it Discover Weekly and shipped it in July 2015. Within weeks, users had streamed over a billion tracks through it. But here's what the team didn't expect: users weren't just listening — they were saving songs to their own libraries at a rate no other feature had ever produced. The editorial playlists Spotify had spent years curating couldn't touch it. Shipping wasn't the win. Shipping was the moment they could finally see what users actually wanted — and it wasn't what Spotify had been building for years. That's the first takeaway — **shipping is the start of the feedback loop, not the finish line.** The moment your product went live in M5, the real learning started. Everything you built before that was a hypothesis. The data is the verdict.

The Discover Weekly team wasn't a hundred-person data science initiative. It started as a hack week project — a handful of engineers who had their listening data, their skip rates, and their save rates. They had their problem statement about music discovery. And they had collaborative filtering to connect the dots. They didn't commission a six-month research study. They didn't build a new analytics platform. They used the signals their product was already collecting and let the patterns speak. The insight came in days, not quarters. The hard part wasn't the analysis. It was the conviction to bet on a machine-generated playlist over the hand-curated editorial strategy Spotify had invested years in. That's the second takeaway — **you don't need a data team to analyze your product.** You need your metrics, your problem statement, and an AI. That combination gives you a product evaluation in minutes that used to take weeks. The analysis isn't the hard part anymore. The decision is.

And then came the discipline. After launch, the data surfaced dozens of potential improvements — adjust the playlist length, change the refresh cadence, add social sharing, tweak genre diversity, send push notifications. They didn't chase all of them. They focused on one signal: which songs users saved versus which songs users skipped. A saved song meant the recommendation changed someone's library. A skipped song meant it missed. They tuned the algorithm around that single metric — not total listens, not completion rate, saves. One finding, one change. And every Monday, Discover Weekly got sharper. That's the third takeaway — **data-driven iteration isn't about fixing everything at once. It's one finding, one change, one redeploy.** The discipline of picking the highest-impact improvement — and only that one — is the actual PM skill. Anyone can generate a list of fixes. Knowing which one to do first is judgment. That's yours now.


## Slide 25 — Survey

Two minutes to fill out the Day 6 survey. QR code is on screen, link is in Slack. This isn't a formality — your feedback directly shapes how we run the next cohort. Tell us what landed, what didn't, and what you wish we'd spent more time on.


## Slide 26 — Bonus Resources

Lab guide and all additional resources are on this slide. If you want to go back and run any of the analytics or iteration steps again on your own, it's all there. Bookmark it.


## Slide 27 — Q&A

Open floor. Anything about the data analysis, the iteration process, the presentations, certifications, or anything from the last six modules. Drop it in chat or unmute. And hit me up in Slack anytime after we close.


## Slide 28 — Thank You

Before you leave. Congratulations — you made it.

For me, this has been an incredible ride. You showed up with curiosity, you pushed through the uncomfortable parts, and you kept building when things broke. That takes courage. And now you're walking out with a new superpower: the ability to identify a real problem, prototype at speed, ship it live, measure whether it works, and improve it with evidence. That's how products get built in this new age.

You didn't just finish a course. Now you have a deployed URL, a Living PRD, a prompt library, an engineering handoff, and a data-driven V2. That arc is yours.

Look around — you now have peers across different companies and industries, all thinking about the same challenges. Don't let that go quiet after today. And you can always reach out to me — whether you're stuck on an idea, want feedback on a prototype, or just want to share something you shipped. I'm here. This is just the beginning.

Be bold, stay curious, stay playful. The world needs people who build with intention and aren't afraid to ship something imperfect and make it better with data. That's you now.

Huge congratulations. You earned this. Now go build something that matters.
