# Dana / Dejan: AI Prototyping Kick Off

**Date:** February 9, 2025
**Participants:** Dana M., Dejan K.

---

## Key Decisions & Alignments

1. **Course theme: From Uncertainty to Confidence.** The course should follow an arc from high ambiguity (don't know what to build) through validation (using AI to gain confidence) to production readiness (scaling with confidence). This is the unifying narrative.

2. **Rebrand away from "Prototyping."** The term "prototyping" is limiting. "Vibe coding" is the current term but may already be aging. The exact term matters less than the methodology underneath it.

3. **Tool-agnostic approach.** The course should NOT be a Lovable tutorial. It should teach a framework/method that works regardless of which tool students use (Lovable, Bolt, Cursor, v0, etc.). The current course leans too heavily on teaching the tool itself.

4. **Validate early with Carlos.** Target: share draft outline by Wednesday with Dana, validate with Carlos on Friday (Feb 13). Don't wait until Feb 17 -- too late given Dejan starts teaching AI Agents course on Feb 24.

5. **Reuse over recreate.** Aim to reuse 50-60% of existing content where the bones are good. The issue isn't the structure -- it's that the good stuff gets lost in "basically a Lovable demo."

---

## Key Insights from Dana

### On Course History & Politics
- Fernan views the course as "basically a failure" -- but this is based on flawed data. The first cohort had a weak instructor, second cohort had Anamika who didn't follow any of Dana's revamp suggestions. The actual content improvements have never been properly measured.
- Dana has already done two rounds of revamps based on feedback, but neither has been fairly tested due to instructor issues.
- There will be "constant tension" around this perception. Need to manage it.

### On the Lovable/Tool Problem
- Lovable updates every few days (new models, new features). The course will always be outdated if it's tool-specific.
- The feedback loop was: "make it more advanced/deeper" → the only way to go deeper was to explain tool-specific mechanics → course becomes a tool tutorial. This is the trap to avoid.
- Lovable Pro partnership should give 3 months free accounts to all students, reducing credit friction.

### On Hands-On Lab Structure
- **Core problem:** In group prototyping, only one person can actually prototype. Everyone else watches. This kills engagement.
- **Proposed solution (from Agents course model):** Everyone builds individually to practice and learn the cycle, THEN they come together for a group project. This way everyone gets hands-on time.
- Agents course example: individual Langflow builds → group orchestration project
- AIPC course example: individual Juno + Lovable practice → group artifact building
- Could dedicate a whole module to "now build together from zero" after individual practice.

### On Student Deliverables
- Idea: students should leave not just with a certificate but with a **tool/artifact they can apply in their day-to-day work**. Something personalized to their needs.
- They'd have both: (1) their group project, and (2) their individual build they can keep developing.

### On Cohort Size Issues
- Recent cohorts had 40-50 students -- too many. Mixed feedback is partly a function of scale, not content quality.
- Instructor quality remains the #1 variable. Some instructors skip hands-on activities because they think there's "not enough time."

### On Content Reuse
- Dana believes 50-60% of existing content has "really good bones and structure" about prototyping.
- The value gets lost in tool-specific focus. The methodology underneath is sound.

---

## Action Items

| Who | What | When |
|-----|------|------|
| Dejan | Create repo with all materials, insights, competitive analysis | In progress |
| Dejan | Draft skeleton/outline document (strategy, diagnosis, competitive analysis, proposal) | By Wednesday Feb 11 |
| Dana | Review draft outline | Wednesday/Thursday |
| Dana | Schedule validation meeting with Carlos | Friday Feb 13 |
| Dana | Share "AI Prototyping 1st & 2nd Cohort Feedback" doc with Dejan | Done |
| Both | Validate skeleton before going into module details | Friday Feb 13 |

---

## Ideas to Explore

- **Juno integration:** Could students leave with a Juno setup they can use going forward? A persistent tool, not just course knowledge.
- **Lenny podcast reference:** Lazar (first "vibe coder" -- prototypes for Lovable full-time). Listen for insights on professional vibe coding workflows.
- **PRDs as guardrails:** How to use PRDs not as upfront documents but as living guardrails during the build process.
- **Repo as content library:** If this works, could scale the repo approach to all courses -- a living content library that's easy to update, iterate, and maintain.
- **Individual + Group build model:** Borrow from Agents course structure for better hands-on engagement.

---

## Raw Transcript

<details>
<summary>Full meeting transcript (click to expand)</summary>

Me: Happy Monday.
Them: Good morning. Afternoon. Monday post bonito bowl.
Me: How did you like it?
Them: It was so nice. It was good. I feel like. A nice way to show. Some unity in a time of not very happy news, you know, going across. America. So I think that was a very nice message to put out there.
Me: 100%. I really love it. A lot of small things, right? Also with the kids. And the flags.
Them: Of course. Yeah, it was great. It was really cool. I really enjoyed it a lot. And it makes me even more excited because, you know, he's coming to. He's coming to Madrid and he's doing like. He got, like 10 sold out shows, and I fought for, like, two days on Ticketmaster to get tickets and.
Me: You got it.
Them: I have tickets for one of his shows, so I'm super excited to get to see him in, in June when he's going to be here.
Me: Nice. Yeah. I was watching on YouTube. There's from, I think Apple TV, they have. And there was one comment I had to laugh that were, like, so nice of him, letting the guys play during his concert. I was.
Them: Exactly. So nice of them to put on a football game for, you know, as entertainment for us. Exactly. Exactly. Hilarious. Yeah, it was. It was really good. I really enjoyed it.
Me: As a sideshow. Cool. Is it a madrid?
Them: The concert.
Me: Yeah.
Them: Yeah, it's at the new. The new Athletico stadium that they. They built outside of the city, which is huge. I've never been to it, but I know it's. It's really big. You drive by it on the way to, like, the airport and stuff. So, yeah, that's going to be. That's going to be fun.
Me: Nice, nice.
Them: Well, here we are.
Me: Here we are again.
Them: Here. I got. Here we are.
Me: But it's good. I didn't know that AI also. AI prototyping was at the danger zone in regards to the content quality.
Them: Yeah.
Me: But I think. Yeah, I saw the tldr I got from carlos and fernan on Friday. On the one hand, braids. Just restructuring it wouldn't do the thing. As when we build a product managers. Fernando was always talking about how he sees you can go from prototyping to implementation and you build. After we've talked this ambiguity from this ambiguity metrics type of thing. I was thinking to also build the cors around that from uncertainty to confidence. Something around that line and that should be like the theme.
Them: Okay?
Me: In the beginning you are ambiguous, don't really know what to do. And then you start developing and using AI in order to gain confidence. And then the more confidence you get, the more you can then think about production ready things and all of that. So I will start to draft a document around that. But that was the one clear theme.
Them: Y. Ep.
Me: The other was that calling it prototyping, I think, is not the right thing. Carlos was speaking. Yes, exactly.
Them: Y. Eah. They're on the vibe coding train.
Me: And I was reflecting on Friday on that, and I was like, is vibe coding also already the old thing?
Them: Falling over. Yeah, I know.
Me: So we can think about it. What is the term? I couldn't care less what the term is, but it's definitely something we need to think about. I don't know if you've seen also I've heard this morning latest podcast episode with Lenny and there is this dude Lazar, and he is the first.
Them: Yeah.
Me: Vibe coding. That's his job. So he prototypes for lovable.
Them: Oh, I saw.
Me: Check it out. I think it's a nice listen. And I know Rena, when she was talking about this, she mentioned she has a person and his job is just prototyping the whole day. And I think it was really interesting concept. I think there's definitely something also we can take with us about PRDs, how to use them as guardrails or. Really understanding what do I want to do, how to go about it. I was also thinking how much we can use Juno or. I think that would be also something interesting for us to think about. Because. I think, wouldn't it be amazing that people not just go out with a certificate, they go out with the tool they can apply on their day to day. So at the end of the course, give them this tool. They can use going forward. Something to think about as well.
Them: Yeah.
Me: But yeah, that's so far where it with the limited amount of time.
Them: I think from my side what I can share and like. I think this course is going to be a challenge for a couple of different reasons. One, I think. I don't know about Carlos because he doesn't necessarily have the insight. He only gets what gets fed to him from front end, for example. But Fernan has it in his mind that, like this course is basically a failure. So. And. You know, frankly, the problem I have with that is. That was taken off. The fact that, you know, the first cohort didn't necessarily go that great. It was. It wasn't necessarily that the course was bad, but, like, the instructor wasn't great. So it didn't, like, have that impact that we wanted. And then I did a whole revamp of the. Course, based on all of the feedback that we got, I implemented that. And then, you know, Anamika literally hit the bed. And anything that I could have even tried to use as like a benchmark of did this help or not, was totally thrown to the wayside because she didn't follow anything that I suggested. And, like, of course, just bombed. So he's got it in his mind that, like. We need to change everything. When, like, I've changed things twice. But he's never gone back and checked that, like, if any of those things actually had any impact, because we don't have a way to measure that. Very well. So I think that's going to be a constant piece of. Of tension. And I think the other piece is just. Using Lovable or if we decide to try something else, like, I know we're going to try and get three months free for all users so that everyone has levelable Pro, which will be great. Like, that'll. That'll reduce a lot of friction. But, like, I get an update from Lovable every couple days. Being, like, now we're using cloud opus. No. Whatever. And now you can do this. The course is going to be outdated. So fast. So, like, it's always going to be a challenge of how to. Like, fit it in a way that if the tool changes, the core concept is still strong. I think that's going to be our biggest challenge with this course.
Me: Yeah. Y.
Them: Which, you know, is fun, but it's a challenge.
Me: Eah. Yeah, no, I agree. And that's why I also think it should not be focusing on any tool or any. Concept in the tool. It should teach more the approach, right? I think how I see it with prototyping or vibe coding. You are significantly increasing the time to market time to validation time to intend. Whatever we want to call it. How do you validate intent earlier? And I think. That should be the message. The tool does not matter. If it's Claude. 4.5 or 4.6 does not matter. It is. How can we teach you a method? Where you can validate your intents as early as possible.
Them: Yes, I agree. I agree.
Me: And then you can replace. Then you can replace lovable with bold or with whatever it is. I think that shouldn't be the problem.
Them: Yeah, I agree. And I think that at the moment, the course is leaning very heavily on the fact that. It's teaching the tool. Which was a lot of the feedback. It's like, well, you didn't get deep enough into the tool of how to. How do you go in and how do you fix the code rather than reprompting. And so, like, those. That was all the feedback that we kept giving, like, make it more advanced, make it deeper. But the only way for us to go deeper was to explain what to do within the tool. And so we have to find a way to scale that back. And kind of still be able to teach those tricks. Without saying, hey, you need to click in here and then go to do X, Y, Z. That's how I. That's how I see the course at the moment.
Me: Okay? That's good. So what I plan to do is I will download all of the material. I will create a repo for us.
Them: Okay?
Me: And then I think, We should incorporate also the sessions we do, validations. We can use those transcripts. I don't know. You just record or also transcribing. And is this a summary or is it a full transcript?
Them: You know what? I think it's a summary that it provides. Is there a way to change?
Me: Yeah. Yes. Yes, it is. So if you go to the settings,
Them: Gemini is taking notes.
Me: I'll show you. I can show you. And then you can see it and try it. For us. It's now disabled because I have been doing so much of the transcripts lately. So I can show you for here. So you need to go to edit.
Them: Y.
Me: And then you go to the cogwheel.
Them: Es.
Me: And there needs to be a setting with meeting records.
Them: Okay?
Me: And here it says, take notes with Gemini. And below that, in the past. Was transcripts. Do you see that?
Them: Let me go to the actual piece here and see if I can. Edit. I don't know if. It gives me that option. More actions. I don't know. I'll have to play around, but I know it's definitely taking notes. Like, I can see in our call right now, it's got the little Gemini, you know, piece there that it's notetaking, but I'm not sure if it's in transcripts.
Me: Okay? Yeah. Yeah, yeah, yeah. Okay. Otherwise, what I will do. I have Granola. I can. I can take notes. And then I'm going to dump those into the repo as well.
Them: Nice.
Me: So at the end.
Them: Y.
Me: It will be around the course and. I was also thinking about, okay, how to incorporate a competitor analysis, what do we have and all. So we'll. We'll play around that as well.
Them: Es.
Me: Once I have that ready, I will push it and then, you know, I will share the repo with you as well, and then we can take a look. But the idea is, rather than having it isolated and let's put everything in there and then iterate and then I can give you going forward.
Them: Y. Es.
Me: I can just give you, you know, you have the repo, right? And then if you want to do in, let's say, six months, it's. Some content is outdated.
Them: We can swap it.
Me: Yeah, exactly right. And you can. You don't need to start from the scratch. You can always use it going forward.
Them: Nice. Yeah, that's great. I also have. I don't know if you. Saw my tag in the prototyping refinement doc. I have all of the final survey feedback from the students on a separate tab there. And like, again, the feedback isn't necessarily that bad. Like all things considered. But I think there's obviously, you know, lots of room for improvement. And, and obviously the thing that students love most is the hands on activities. We just got to find a way to. Do it.
Me: Yes.
Them: Better because to be fair, when. When I. When we were building these. When I was building them with Divya, who was the person who helped us to create all these, this was the first one we built. So we didn't really have the. The flow of, like, how the hands on labs work. How do we combine the tool activity with, like an artifact that then maps better to the project. Like, we didn't have that. That really defined. So I think that's why this one still feels a little clumsy.
Me: I see. Okay, now, that's good. Let's take it from the one. One other thing I wanted to check with you. There is this feedback doc, AI prototyping, first and second cohort feedback I don't have access to. Is it. Is there useful feedback, do you think?
Them: Yes. Oh, shoot. This one. This document is a bit crazy. I'll share it with you. This is the one that like they were taking notes during the. Class.
Me: Okay?
Them: And so there's some interesting pieces here. But it's a lot of noise.
Me: Yeah, I don't know. How much of that shall we really use or not?
Them: Yeah. I mean, I would suggest maybe looking through it a little bit. The first cohort. I've basically implemented all of that feedback into the second cohort.
Me: Okay?
Them: And the second one, I tried to implement a lot of it. But this is, like the. It's got feedback from, like, Lisa and macz and, like, there's a lot of stuff in there, so it's noisy, that's for sure.
Me: O. Kay. Then. Okay, good, good. Just wanted to check.
Them: Just shared it with you anyway, so you've got it there. I think. I think the main piece, like, I know that, you know, Machek is very technical. He's part of our platform's team. But, like, he had some good suggestions of, like, how we could try to make the course feel more, you know, advanced, which is, like, what? Both Carlos and Fernand want or, like, more hands on. I don't know if a lot of it is feasible, but he definitely had some interesting ideas that we could possibly pursue if, you know,
Me: Okay? Okay?
Them: Let's see.
Me: Yeah, I think let's have a foundation. I think you and I agree on and align, and we think that's the right approach. And once we feel confident, then let's incorporate more feedback, refine it. But I hope the skeleton and the theme.
Them: Y.
Me: And digested what you think about this ambiguity. Because. Yeah. Remember? Right. Fernan is saying, look, you don't need engineering anymore. You could use the tool, ship it and it's live.
Them: Eah.
Me: And I agree to that. Right? But I think you need to do a lot of things before that, right? You need to validate it. You need to be confident that it's true.
Them: Yes.
Me: And I think in the past. You. Had different tools in that process. So in this high ambiguity, Place you. Had documents, you had Figma, you had other visualization things. You had Miro board, right?
Them: Y.
Me: And then the more confidence you get. This is where you then used production ready tools in order to ship things.
Them: Es.
Me: Now. Those disconnected tools. Is 1.
Them: Y.
Me: But the process has not changed. It's just that instead of having these disconnected tools, you have one tool which has everything combined.
Them: Ep.
Me: And you're moving this tool from one place to the other. And it's just showcasing that and using the same tool across the board. By continuously improving it. So that would be, you know, I think the message I would suggest to go with, because then it's not tool specific.
Them: Yeah.
Me: It's not a how to use Lovable, bold, whatever. And by having that framework, you can use whatever. And then we can use these tools, right? And on the hands on lab activities and all, we can use lovable to, to go through those different stages and explain how you can use it. But then, you know, if people in their organization use cursor or use bold or use V0, right. They can still apply it because they know what the framework is.
Them: Sure. Yeah, exactly. And I think one thing we'll also have to kind of figure out is, like, for me, what Fernand kept saying was, like, oh, well, you know, you can build it in, like, 30 minutes. So, like, why are we. Why are we spending so much time, like, teaching content? So I think we need to be able to. Strike the right balance between. How much time we're giving students in this course maybe compared to others, to actually be doing a build project. And what are we teaching them? That. Is unique. I suppose to prototyping that doesn't. That doesn't matter as much for, like. Like the assumption is supposed to be that if they're product managers, then they don't need to know all of the like. High level details like this should be things that are specific for this new. Cycle. So that's where we should be kind of, like, focusing. Our attention on, I guess.
Me: Okay?
Them: But yeah.
Me: So do you think there might be also a chance to slim down from. Three weeks to last or six modules to less or it's more the amount of teaching versus them doing.
Them: It's the amount of teaching versus doing and finding a better. A better way. Like, I think the other issue with this course is, you know, like in the agents course, for example, when we do Langflow, they're build, everyone's building on their own, so they get to kind of like, practice, and then they come together and do the build as a whole.
Me: The orchestration.
Them: You know, and in the new aipc, it's the same thing. Everyone's, like, building Juno on their own and lovable to kind of, like, see how it works. But then they go back together and they build the, like, artifact pieces. That relate to the project together as a group. So I feel like we need to find a better way to do that with this course, too. Because at the moment, we're getting them in the groups to, like, prototype pieces of the. And, like, it's not fun because only one person can technically do the prototyping, so everyone else is kind of like, twiddling their thumbs. So I think we need to strike the balance of, like, everyone is kind of like, maybe it's the same sort of concept like in agents, where everyone's. Kind of building their own thing to, like, practice. So everyone gets familiar with how it works, how the. The cycle is. And then we give them almost, like, a whole module of, like, all right, now here's the project. Like, go do it together, and, like, build from zero. And then they really get to play around for, like, the whole class kind of thing doing that.
Me: Yeah. Y. Es. Y. Eah. Yeah, I like that.
Them: That might be a better, that might be a better approach so that students aren't feeling that, like, they're not active in the, the process of it. And then we can still tie in the other pieces of, like, okay, build your simplified PRD of, like, what you want this to look like, and like, that sort of thing, but that. That's my thought of, like, how we could approach it in a way that gives students more time.
Me: Yeah.
Them: To build.
Me: I like that. Yeah. This ties to. At the end of the course, they have something they can take with them and use it right, and it's personalized to their needs.
Them: Exactly. Exactly. Well, they've got both, right? They've got their little project that they worked on together, and then they've got their own separate little thing that if they want to keep going with that and. Build it out more than they can do that on their own.
Me: Yes. Good. Yeah.
Them: So I think that's a good approach to take for the meeting later with Carlos.
Me: Yeah. I mean, I have seen. I think by mistake, he booked it on the 16th.
Them: On. On the 6th on Monday.
Me: No. On. On the Tuesday. Wait. On the 17th.
Them: On the.
Me: No. Yeah. Revamp Working session. That's too late, right? Was this his intention?
Them: 17th.
Me: Or tomorrow.
Them: I think is an. I have a. I have a meeting with him today to kind of, like, probably talk about next steps, I would assume. So I can check with him on that. But my assumption is he would probably want to see by next week.
Me: Okay?
Them: On that Tuesday, like, how far we've come along to, like, validate it and then again on the Friday sort of thing.
Me: Yeah, I think.
Them: So perhaps he's giving us a week to kind of, like, lay out the new. Vision. We can validate that and then buy the Friday we like. Show him what the new module one looks like, for example.
Me: So what do you think? I think it's too late.
Them: You think it's too late?
Me: I think so. I don't know how much. I think ambitiously we could. We can show him something on Thursday.
Them: This Thursday the 12th.
Me: Oh, wait, but we're not. Friday. Friday. Sorry, Friday.
Them: Friday to the 13th.
Me: The 13th.
Them: Yeah.
Me: Yeah, it's. What? What do you think?
Them: And. And you're talking about, like, a high level outline of the new vision.
Me: Yes.
Them: I think that's pretty reasonable.
Me: The reason why I'm saying that is I spoke with him and I said I'm going to start teaching on. The 20. Second, I think. AI agents. I have a new course.
Them: Oh, you've got a new agents course.
Me: Yeah, 24th.
Them: And. The 24th. So it's another Tuesday. Thursday, of course.
Me: Yes. So with, you know, my day to day work and this, and then it might be.
Them: Okay? Yeah, of course.
Me: My goal is to have a good, let's say, 70%, 80% of the skeleton of the. The themes, the labs and all of that fleshed out. So that, you know, you. You basically have everything you need. And then I think that worked quite well. You know, having together building the skeleton and the foundation of the course. And then, you know, us iterating on it once, you know, you put it into concrete actions and then iterating. Because this is, I think also a lot of things will potentially change because then when, when things get concrete,
Them: Yes.
Me: Oh, you know, this is conceptually, it worked. But then we change things and then the module 2 there's a dependency, and then we had to go back and then we switch and, you know, we need to iterate. So I think that a lot of work will happen at that point of time as well. That's why it would be great to align with car with Carlos already this week.
Them: Yes. Yes.
Me: Is this aligning with your expectation? If not, then we can. We can have till Tuesday for another way. I don't know if you know we will land a home run. Initially, right? Or do we need to consider his feedback? And I think if we wait.
Them: Yes. Definitely.
Me: Till Tuesday, and then we need to iterate, and then.
Them: And it's a whole week later. Yeah, no, I agree. That's a good point. I'll reach out. To him and, and find out about that and see if we can schedule something. And then for this Friday as, like the, the first review of.
Me: Yes.
Them: Of the outline. I think that would be great.
Me: Yeah. And I feel like I might be able to share on Wednesday a draft with you.
Them: Okay? Yeah. Yeah, because, like, for me, I know that. I know that, like, this new vision that they have for product school is, like, they want to move super fast. And, like, I think that's great, and that's ambitious, and I want to be able to help do that. But I also know that at the end of the day like the logistics of moving fast. Always get stuck, like you said, with all these extra dependencies that as soon as you change one thing, you got to go and, like, tweak everything else, and that ends up taking up the extra time. So if we can nail that early on,
Me: Yeah. Y. Eah.
Them: So we don't have to go back and forth. So much that will certainly make things go faster.
Me: Yeah. And then let's. Let's think about. And then let's also experiment with this concept of having the repo with the content. And then, you know, see how easy. Then this is. Think about this as your library, right? Your content library. And then you can. You can select, reiterate, adjust, slim down, whatever. And then if, you know, you could. You could theoretically build this for all the courses, right? And then you could say, hey, take a look. Now I have changed this. Where should it change as well? And. All right, you could play around with this.
Them: Yeah. Yes. Yeah, that's. I would. I mean, I would love to have that. And, like, I. That's, like, my goal. Just, you know, when do I have time to do that? When they keep throwing every. Like, go fix this course and go fix. I have no time.
Me: Exactly. Reactive rather than proactive, right?
Them: Exactly. Totally. I just. I don't have the time to make any of those things when I'm always fighting fires and trying to, you know, have it ready.
Me: I. Don't know.
Them: By the next. Day of the class starts, basically.
Me: By the way, how did it go? Any feedback so far on the course?
Them: So it's. It's a bit weird because Ruhab never gave any feedback. And then Sophia, another instructor, taught the course. And like, both of, like, all of the cohorts basically started one after the another, and they all had like 40 or 50 students in them. And you know firsthand that, like, a cohort with 40 or 50 students is tough and you could have the best content and, like, you're going to get a big mixed bag because. That's just. That's just the way it is. It's. It's very challenging, so. It seems like the content is well received. Like the, the, the feedback that I've read for the content seems to be pretty good. I think there's a mixed reactions of like, oh, we didn't get to do enough hands on because the instructor basically didn't do it with them because she thought they didn't have enough time, which. Kind of defeats the purpose. And then, you know, some students saying that, like, oh, we. We didn't see how, like, some of the modules connected with each other, but again, I'm not sure if that's because.
Me: Yeah.
Them: She just didn't have it. Like, they didn't have enough time to go through the content, so it's a little bit all over the place.
Me: Okay?
Them: And it's hard to kind of parse. What? to like what to take from that and make
Me: A plan of action. I'm going to incorporate all of those learnings, do some sort of competitive analysis, incorporate also all the learnings and everything you said about the course being hands on. That also. Every student needs to participate, create, to incorporate all of that. And then, as previously, we'll create like a document.
Them: Yes.
Me: First with the skeleton with I will like a strategy, document, diagnosis, diagnosis, insights, competitive analysis, assessments, proposal and then on a high level explain how the course should look.
Them: Okay?
Me: And then if I have time, it can go already a bit in detail about. Module one is this. Module two is this. Module three is that. And then explain that also on a high level. I don't want to spend too much time going into the details without validating that the skeleton is the right thing.
Them: Yes. I agree. I think that's definitely a good call. And hopefully from there. I'd also. Understand. If we have to totally swap stuff out, then that's fine, but I would hope that we can reuse. A good 50, 60% of the content to kind of save us a little bit. Because, again, I think there are some really good bones and structure to what we're trying to say about prototyping. But like I said, I think it's getting lost in this, like, focus on, basically a lovable demo.
Me: How to.
Them: Rather than what the outcome can be from that tool. Or, like you said, any other version of the tool.
Me: Yeah, okay. Then I will also try to come up with some principles. We'll see if it's only for us, but yeah, I think one of the principle is let's reuse rather than create.
Them: Yeah. Where we can. Sure.
Me: And then we can take it from there.
Them: Sounds great. Okay. Well, I'll look forward to your little outline. Whatever. Your breakout line. Let's see, whatever comes my way midweek. And then I'll see what I can get together. And I'll also message Carlos to figure out what time. Do you think? Normally he's got it set for like, 5pM. Our time. So if that works, we could try to set it for this Friday at around the same time, if that's okay with you.
Me: Yeah. I told him Tuesday and Friday that time would work for me. And then he said, okay, then let's set it up.
Them: Perfect. Perfect. Sounds good. I'll reach out and see if I can get that set up then for this Friday, too, so that we've got something we can validate going into the weekend anyway, so that we're set ready for the start of the new week.
Me: Let's go. All right.
Them: Great. All right.
Me: Have a great start to your week.
Them: Thank you. You too. Bye.
Me: Bye. Bye.

</details>
