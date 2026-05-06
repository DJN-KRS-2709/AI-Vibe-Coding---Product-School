# Shareable Notes Template

The shareable notes are a **reader-facing companion** to the slide deck — the document a participant takes home after a session, or shares with a colleague who couldn't attend. They walk through the same slide arc as the speaker notes but in a third-person, reader-oriented voice.

**Reference**: `Modules/Module 1 - Notes (Shareable).md` in the AI Product Strategy course.

---

## Template

```markdown
# Module N — Title

*Shareable companion notes. These walk you back through what each slide covered, in case you want to review the arguments, examples, and frameworks at your own pace.*

---

## What this module is about

[1-2 paragraph overview. Third person, reader-facing. Cover:]

- The thesis of the module
- The traditional assumption it challenges
- What students leave with (the artifact, the framework, the reframe)
- How this module fits in the course arc

Bold the key concepts (e.g. **probabilistic thinking**, **living strategy repo**) so a skim-reader catches them.

---

### Slide 1 — Title

[1 short paragraph: the strategic question the module answers, the three waypoints, the deliverable. Reads like the back-cover blurb of the session.]

### Slide 4 — Course Arc

[If the course has an explicit arc slide, summarize the full arc here as a bullet list:]

- **M1 — The Bet:** Where does strategy break?
- **M2 — The Moat:** Can anyone copy you?
- ...

### Slide 6 — {Concept Name}

[For lecture slides: explain the concept in 1-2 short paragraphs. Use:]

- Tables for comparisons (Traditional vs. AI, before vs. after, etc.)
- Bold for the named framework or concept
- Italic for the source attribution ("from Madhavan Ramanujam's Monetizing Innovation")
- Real company names as evidence (Bloomberg, Salesforce, Apple — not "a major SaaS company")

[For case study slides: tell the story in 2-3 paragraphs. Lead with the big number. Name the company, the bet, the crack, the correction or the fall.]

[For exercise slides: describe what the exercise asked the participant to do, what good answers looked like, and what insight the exercise was designed to surface. Do NOT include the speaker's coaching prompts — those live in Speaker Notes.]

[For provocations: state the claim and the answer (True / False) with a one-line proof point.]

### Slide N — {Slide Title}

[Continue for every substantive slide. Skip purely transitional slides like Agenda or Recall when they don't carry standalone meaning.]

---

## What you take home

- [Artifact 1 — the file or scorecard or map they built]
- [Artifact 2 — the framework or mental model they now own]
- [Artifact 3 — the question they can now answer about their product]

---

## Going deeper

- [Source 1 — book, post, or talk referenced in the module]
- [Source 2 — companion tool or template]
- [Source 3 — relevant module to revisit]
```

---

## Tone Rules

| Do | Don't |
|----|-------|
| Third person, reader-facing ("By the end of the session, students have...") | Second person to the instructor ("you should...") |
| Concise paragraphs that summarize the argument | Verbatim transcripts of what was said in the room |
| Bold the named frameworks and concepts | Bullet-list everything |
| Tables for any comparison the slides showed | Long prose where a table would do |
| Real company names | Generic placeholders ("a tech giant") |
| Italicize source attributions | Cite without context |
| Skip purely transitional slides | Force a section per slide |

---

## What's different from Speaker Notes

| Speaker Notes (Module N - Speaker Notes.md) | Shareable Notes (Module N - Notes (Shareable).md) |
|---|---|
| Briefing memo for the instructor | Reader companion for the participant |
| Second person to the instructor | Third person, neutral voice |
| Explains intent: "why this slide exists" | Explains content: "what the slide argued" |
| Conversational, like coffee chat | Edited, like a magazine article |
| Includes coaching prompts | Includes the framework, not the coaching |
| One section per slide, no skipping | Skip transitional slides; merge consecutive ones |
| ~2,000 words per module | ~1,500 words per module |

The two files cover the same arc but serve different readers. Generate them from the same audit row in Step 4.

---

## Content Checklist

- [ ] Opens with `# Module N — Title` and the italicized companion blurb
- [ ] Has `## What this module is about` summary
- [ ] Horizontal rule (`---`) before slide-by-slide notes
- [ ] Substantive slides have an `### Slide N — Title` entry
- [ ] Transitional slides (agenda, recall, breaks) are skipped
- [ ] Tables used for any comparison the slides showed
- [ ] Real company names match the slides
- [ ] Closes with `## What you take home` and `## Going deeper`
