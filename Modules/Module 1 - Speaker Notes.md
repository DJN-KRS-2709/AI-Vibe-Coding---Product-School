# Module 1: Activate Vibe Coding Speed — Speaker Notes

Casual talking points for each slide. Not a script — just the key things to say and the energy to bring. Real examples from companies like Airbnb, Spotify, Slack, and Instagram to ground every concept.

---

## Slide 1 — Title

Welcome to Module 1 — Activate Vibe Coding Speed. Let's get started.


## Slide 2 — Class Expectations

Before we dive in, let's set our ground rules. Cameras on — it makes a huge difference in how we connect and learn together. Be present, arrive on time, and participate actively during exercises. Use Slack for all communication so nothing gets lost. And save deeper questions for after class so we don't interrupt the flow — but don't worry, there will be plenty of time to ask everything.


## Slide 3 — Introductions

Hey everybody, I'm Dejan. I'm a father of two boys — six and eight — and they definitely keep me busy. I like to say I buy Lego for them… but let's be honest, I'm really buying it for myself.

I've been in product for more than 16 years. Back in the day, product management meant writing huge specification documents and then praying for six months that the features would be delivered as expected. They never were.

Before Spotify, I worked at SoundCloud, where we built an insights and analytics platform from scratch. I also launched Fan-Powered Royalties — a completely new way of paying artists on a streaming service. I've been at Spotify for about 4 years now.

But enough about me — I'd love to get to know you. Drop your name, role, and at least one fun fact in Slack or the chat. The more we know about each other, the better we can learn together.


## Slide 4 — Syllabus

Here's the full outline of the course. Six modules across three weeks — two sessions per week, each one building on the last.

Module 1 is where we are today — speed. You'll build your first functional prototype from scratch.

Module 2 is about sharpening your intent — making sure you're building the right thing, not just building fast. Think of it like this: Airbnb's first prototype was three air mattresses on a floor. The idea wasn't the mattresses — it was testing whether strangers would pay to stay in someone's home. That's Module 2 thinking.

Module 3 is precision — using context engineering to get exactly what you describe. No more "build me something" — it becomes "build me exactly this."

Module 4 translates your prototype into production specs — Living PRDs, GitHub, Supabase. This is where Instagram went from a photo filter app called Burbn to a focused product.

Module 5 makes it real — databases, auth, APIs, and you deploy it. Live URL. Real users. Your prototype becomes a real working product.

And Module 6 — you measure, learn, and iterate. Analytics, AI-powered analysis, and a data-driven improvement cycle. You close the loop from idea to evidence.


## Slide 5 — Final Project Explanation

At the end of our three weeks you will present your final project. Let me play the video for you.


## Slide 6 — Final Project Deliverables

Here are the key deliverables for your final project. You'll submit individually — no group dependencies.

Six things in your deck: your live deployed link, your validation brief, your Living PRD, your prompt library, your engineering handoff, and your personal insights into the build process.

Think of this as your product portfolio — not a homework assignment. When Dropbox launched, Drew Houston didn't have a working product. He had a demo video that proved the concept. Your deliverable is even better — you'll have a live, working product with evidence behind it.


## Slide 7 — Agenda

Here's what we're covering today. We'll start with a live demo — I'll build three completely different prototypes from one messy problem in 15 minutes. Then you'll do the same in your first hands-on lab. After that, we'll level up your prototype with design systems and interactivity. And we'll wrap by naming the framework you just lived through — the Confidence Line.


## Slide 8 — The High-Velocity Prototyping Cycle

This kicks off the first major section — the high-velocity prototyping cycle. This is the core of vibe coding: build fast, show fast, learn fast. Let's dig in.


## Slide 9 — Instructor-Led Demo: The Triple-Threat Build

Here's the scenario. Enterprise customers are churning 30 days after onboarding. The VP of Customer Success thinks it's a UX issue. The Head of Product thinks you need better feature discovery. The CEO thinks we should add a self-serve analytics dashboard. Nobody has data. Everybody has opinions.

Sound familiar? This is the reality of product work. Slack had this exact problem early on — teams would sign up, poke around for a day, and ghost. They discovered the magic number: if a team sent 2,000 messages, they almost never churned. But they had to build and test to find that.

I'm going to build three completely different prototypes from this one problem — live, right now. Watch how fast this goes.


## Slide 10 — Your Vibe Coding Tool Stack

We're using the best tool in the market right now: Lovable. Partnership with Product School means you get Pro access for free throughout this course.

Why Lovable? It's visual-first and has the lowest barrier for non-technical PMs. You don't need to understand code to build functional prototypes. Figma revolutionized design by making it accessible — Lovable does the same for building.

Your Pro package includes about 100 credits per month — not unlimited. Tip: do your prompt planning in Gemini or ChatGPT first. Paste the polished prompt into Lovable when it's time to build. That alone will save you from running out of credits mid-module.


## Slide 11 — Skill Markdowns

This is a superpower most people don't know about yet. AI tools like Cursor, Claude, and Lovable can import skills — pre-made instruction sets that give the AI specialized capabilities.

Think of it like installing an app on your phone. Someone else figured out how to make the AI great at building dashboards, and you can import their skill in one click. Shopify's AI, for example, uses specialized instruction sets for different merchant tasks — inventory management gets different rules than marketing.

By Module 3, you'll build your own skills in your Living Prompt Pack. For now, just know they exist. It's a superpower you can acquire without writing a single line of code.


## Slide 12 — Bridging Design and Build

Modern vibe coding tools are multimodal — they can ingest your existing assets and match your company's design system instantly.

There are three main entry points. Text-to-App — you describe what you want in natural language. Best for completely new concepts where no design exists yet. Screenshot-to-App — you upload a screenshot of an existing product and the AI clones the pattern. This is how teams at companies like Notion rapidly prototype variations — screenshot the current UI, describe what's different. And Design-to-Code — you import Figma files or design system docs. Best for on-brand prototypes when you already have a design system.

The takeaway: you don't start from a blank canvas. You start from what already exists.


## Slide 13 — Vibe Coding Credit Efficiency

Credit efficiency is like fuel management. Tesla doesn't waste battery on unnecessary acceleration — and you shouldn't waste Lovable credits on half-baked prompts.

Three steps. First, plan in a sandbox — do 60% of your refinement work in ChatGPT or Gemini. Get the prompt tight before you touch Lovable. Second, paste into Lovable when it's polished — aim for one generation, not five. Third, for minor fixes like colors or typos, adjust the code directly instead of burning a credit.

And here's the eject rule: if a prompt fails twice, stop. Export the code, debug it externally, and paste the fix back. Never enter a "credit death spiral" by re-prompting the same broken logic.


## Slide 14 — Your First Vibe Build in Lovable

Time to get our hands dirty! We're moving from watching to building. In this lab, you'll build your very first functional prototype from scratch.


## Slide 15 — Lab 1: Your First Vibe Build

Open Lovable and choose one of the four scenarios from the lab guide. You've got two approaches if you're staring at a blank prompt box.

Option 1 — Copy and Customize: grab the starter prompt from the lab guide and replace the brackets with your specifics. Option 2 — First Screen Method: visualize the very first thing your user would see and prompt Lovable to build exactly that.

Build on instinct. No methodology, no framework — just speed and immediate execution. If the output isn't right, prompt again or prompt differently. Aim for "clickable" over "perfect."

Instagram's first version was built in eight weeks by two people. It did one thing: let you take a photo, apply a filter, and share it. That's the energy here — what's the simplest version that proves your idea works?


## Slide 16 — Show and Swap: Breakout Exercise

Pair up with someone. Swap prototype links in the chat. Now here's the key rule — explore your partner's build silently for 3 minutes. No verbal context. No explaining.

This mirrors real user behavior. When Stripe puts a new feature in front of users, they don't explain how it works. They watch where people click, where they hesitate, where they get confused. That's exactly what you're doing now.

After 3 minutes of silent exploration, discuss: what you understood immediately, what confused you, and what assumption you think this prototype was testing.


## Slide 17 — Quick Debrief

In one sentence, share in Slack: what was something surprising you learned from watching someone use your prototype?

This is the power of rapid feedback. You just compressed weeks of assumption-testing into 30 minutes. Most product teams spend months debating features in conference rooms. You just built, tested, and learned in the time it takes to have one meeting.


## Slide 18 — Estimated Time: 5 Minutes

Quick 5-minute break. Grab some water, stretch, and we'll be right back.


## Slide 19 — Cameras On

Welcome back! Quick reminder — it's always better to see your smiling face. Be present and visible to stay engaged and keep interactions valuable.


## Slide 20 — Instructor-Led Demo: Moving From Basic to Pro

You have three working prototypes, but they all look like "vibe" sketches. Your VP of Design won't look at them because they don't match the brand, and your Engineering Lead says they're too generic to be useful.

Speed got you the idea. Now, strategic iteration must get you the buy-in.

This is exactly what happened at Spotify when we prototyped new features — the first version always looks generic. What convinces stakeholders isn't more features, it's making it look and feel like it already belongs in the product. Watch how I transform this in 6 prompts.


## Slide 21 — Strategically Refine Your Build in Lovable

Time for round two. You're heading back into the lab to take your rough prototype and make it look like something you'd proudly show your VP.


## Slide 22 — Lab 2: Strategically Refine Your Build

Return to your Lab 1 prototype and identify the weakest section. Select at least two upgrades:

Design Match — use a Mobbin screenshot to clone professional colors, layouts, and navigation. This is what Airbnb does when they prototype new features — they start from their existing design system, not from scratch.

Add Interactivity — make a filter work, a detail view expand, or a form validate. Static screenshots don't validate anything.

Refine Without Rebuilding — use a focused prompt to surgically fix one specific section. The key skill here is steering, not starting over.

Generate your upgraded link and prepare to share the before-and-after transformation in Slack. Remember: plan your prompts outside of Lovable to save credits.


## Slide 23 — Swap and Review: Breakout Exercise

New pairs this time. Swap prototype links again. Explore silently for 3 minutes, then discuss:

Does this feel like a "real" product or just a visual mockup? Where did the interactivity fail to meet your expectations as a user? And the big question: would you show this to your VP as a credible representation of a solution?

When Notion tests new features internally, the bar isn't "does it work?" — it's "would you use this yourself every day?" That's the standard we're aiming for.


## Slide 24 — Quick Debrief: Prototype-Readiness Score

Share screenshots of your before and after prototypes in Slack. Then score your refined prototype from 1 to 5:

1 means "just a sketch — it exists but it's not ready for eyes." 3 means "getting there — recognizable but not functional." 5 means "VP ready — I'd show this to leadership tomorrow."

Be honest. The gap between where you are and where you want to be — that's exactly what the rest of this course closes.


## Slide 25 — From Prompt to Functional Strategy

Now we're moving from building to naming. Everything you just experienced — the building, the testing, the iteration — follows a pattern. Let's name it.


## Slide 26 — The Confidence Line

This is the framework that runs through the entire course — the Confidence Line.

On the left, you start in ambiguity. You don't know what to build. That's where you were 90 minutes ago. Modules 1 and 2 live here — you build fast, you test assumptions, you figure out what's worth pursuing.

In the middle, you gain clarity. Modules 3 and 4 — you get precise with your prompting and start structuring for real teams. This is where Slack went from "chat tool for a video game company" to "enterprise communication platform." They didn't start with that clarity — they built their way to it.

On the right, you're confident. Module 5 — real integrations, real deployment, real users. You'll have a live URL that anyone on the internet can use. And Module 6 closes the loop — you measure what's happening, use AI to analyze it, and iterate based on evidence. That's the full product lifecycle.

The tool doesn't matter. The progression does. Even if every AI tool changes next month, this framework stays the same.


## Slide 27 — From Toy to Tool

Here's the most important distinction in this course. A toy looks impressive but proves nothing. It generates applause, not insights. No logic behind the screen. Dies after the demo.

A tool looks real and proves something works. It validates an assumption with clickable evidence. Handles at least one real user flow end-to-end. Survives when someone else uses it.

Think about the score you just gave your prototype — was it a toy or a tool? Dropbox's famous demo video wasn't pretty. It was a 3-minute screencast showing a folder syncing. But it proved the core concept worked. That's a tool. That gap is what the rest of this course closes.


## Slide 28 — Accountability Statement

In one sentence, post on Slack: what is one thing you learned about your product idea that you didn't know 60 minutes ago?

Then reply to 2 other learning sentences from your peers. This is your cohort — support each other. The best products are built by people who learn from each other's mistakes, not just their own.


## Slide 29 — Module 1 Complete

Look at what you accomplished today. Two prototypes built — from scratch to shareable in under 60 minutes. Two feedback loops — real users testing your assumptions, not your opinions. And 67% hands-on time — more time building than any PM course on the market.

Here's the shift that happened: the mental barrier is gone. You built functional software without writing a single line of code. The wall between thinking and building is removed. You're no longer waiting on engineering to validate your product instincts — you validated them yourself, today, in real time.

And you learned the tool vs. toy distinction. If your prototype helped you decide something, it's a tool. If it only looked cool, it's a toy. You built tools today.


## Slide 30 — Key Takeaways

Let me bring this home with a story you've already been living today.

Remember when I told you about Slack at the beginning of class? Stewart Butterfield wasn't building a chat product. He was building a game called Glitch — and his team needed an internal tool to talk to each other. So they built one. Fast. No spec, no PRD, no design review. Just "we need a way to communicate" and a rough prototype that worked. That's takeaway one — they built to think. The prototype wasn't a deliverable. It was how they figured out what they actually needed.

The game flopped. But the chat tool? People wouldn't stop using it. So Butterfield's team started layering. First it was just messages. Then they added channels. Then search. Then file sharing. Then integrations. Each layer wasn't a redesign — it was a precise addition that made the tool more functional without breaking what already worked. Sound familiar? That's exactly what you did today. You started with a vibe, layered on a design system, added interactivity, then surgically refined one section. Each pass compounded. That's takeaway two — vibes become tools through intentional, incremental layers, not through starting over.

But here's the part that changed everything. Butterfield's team discovered a number: 2,000. Teams that sent 2,000 messages almost never churned. Teams that didn't, disappeared. That wasn't an opinion. That wasn't a gut feeling. That was evidence — generated by a working product that people could actually use. And that single data point gave them the confidence to pivot an entire company from gaming to enterprise communication. That's takeaway three — every build must move the Confidence Line by answering a real question. A prototype is a tool only when it generates evidence, not applause.

That's the arc of what we covered today. Build fast to think. Layer intentionally to make it real. And always — always — build to answer a question, not to impress a room.


## Slide 31 — Extra Practice and Next Session

If you want to dig deeper, two optional exercises:

First — pick an alternative scenario and try your vibe build again. Pick one you're less familiar with to challenge your newly acquired speed skill.

Second — try another tool like Bolt or Cursor and compare the outputs. Which one was easier? Which gave you the best V1? The methodology works across all of them.

Next session — Module 2: Sharpen Intent with Strategic Prototypes. You can build fast. Now: are you building the right thing? We'll apply the validation framework and make sure you're choosing the right fidelity for your build intent.


## Slide 32 — Survey

At the end of each session, please scan the QR code or use the link to share your feedback. Your insights help us improve and make each cohort better than the last. We'd love to hear about your experience!


## Slide 33 — Resources and Templates

Here you'll find all the resources for this module — the final project brief, the Module 1 Lab Guide, and the final project deliverables template. Make sure to bookmark these for reference as you continue your journey through the course.


## Slide 34 — Q&A

Alright, before we close — any final questions? This is your time to ask anything about what we covered today. Feel free to unmute or drop your question in the chat. Or share questions in Slack if something pops up later. See you next week!
