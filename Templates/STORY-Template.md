# STORY — Friction · Learning · Aha

> Copy this file into your project repo as **`STORY.md`** (root) or **`docs/STORY.md`** and fill in each section. The Showcase Generator scans every markdown file in your repo for these exact headings (`## Friction`, `## Learning`, `## Aha`) and pulls the content into the corresponding slides.

---

## Friction

What broke during the build? Where did you hit a wall?

> Example: *"Lovable kept restyling the PM dashboard every time I touched the onboarding flow. I lost two hours before I realised I was prompting the whole repo instead of the onboarding feature folder."*

One short paragraph is enough. Be honest — the friction slide is what makes the showcase feel real, not curated.

---

## Learning

What did you take away that you'd carry into the next project?

> Example: *"My best prompts started naming the directory: 'in `src/features/onboarding/`, update Screen 2 to…'. The cleverness lived in the architecture (feature-grouped folders) once I made the prompt match it."*

One paragraph. The principle, not the play-by-play.

---

## Aha

The moment it clicked — the thing you can't un-see now.

> Example: *"My aha moment was the iteration sprint. I'd been telling colleagues for years that retention is an onboarding problem — and in fifteen minutes I had real data, an AI-prioritised finding, and a deployed fix that moved the number. The loop I'd been arguing for on whiteboards finally ran end-to-end on something I shipped."*

Make this one count. The aha is the closing slide of the showcase — give it some weight.

---

## How the generator finds these

The `Templates/Showcase-Generator.html` tool crawls every `.md` file in your public GitHub repo, looks for headings that match `## Friction`, `## Learning`, and `## Aha` (case-insensitive), and pulls the content under each heading into the showcase.

You don't have to put them in this file — you can scatter them across your repo if you prefer. But keeping them together in one `STORY.md` is the cleanest pattern.
