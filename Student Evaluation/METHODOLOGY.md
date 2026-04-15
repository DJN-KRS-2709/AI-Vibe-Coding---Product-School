# Student Evaluation Methodology

**Course:** AI Prototyping & Vibe Coding — Product School  
**Evaluator:** AI-assisted evaluation (Claude / Cursor Agent)  
**Date:** April 13–14, 2026  
**Cohort Size:** 18 students

---

## 1. Evaluation Framework

Each student submitted a final project deliverable documenting their experience building a live product using AI-assisted development tools (primarily Lovable). Submissions were received as PDFs and PowerPoint decks (`.pptx`).

The evaluation rubric was derived directly from the course modules — specifically **Module 5** (Ship a Live Product) and **Module 6** (Measure & Iterate) — which define the deliverables students were expected to produce.

### Scoring Scale

- **Maximum:** 100 points
- **Floor:** 80 points (no student receives below 80 to reflect that all students completed the course and shipped a working prototype)
- **Score Bands:**
  - 90–100: Exceptional — comprehensive, strategic, production-quality
  - 85–89: Strong — solid across most dimensions with clear strengths
  - 80–84: Good — meets requirements with room for deeper documentation

---

## 2. Evaluation Criteria (7 Dimensions)

| Dimension | Weight | What Was Evaluated |
|-----------|--------|--------------------|
| **Deployed Prototype** | 15 pts | Clarity of hypothesis and bet, problem scenario framing, live Lovable link |
| **Validation Brief** | 15 pts | Risk type identification, kill switch criteria, stress test methodology, findings |
| **Living PRD** | 15 pts | Product overview, user flows, screen maps, success metrics (North Star + leading indicators), scope (In/Out) |
| **Prompt Library & Logic** | 15 pts | Product context block (anchor), behavior/knowledge grounding (RAG rules), design system reference, actual prompt text shown |
| **Engineering Handoff** | 20 pts | Functional truth table (Real vs. Mocked), integrations, data model (tables/schema), edge cases & known gaps, "Start Here" guide |
| **Individual Insights** | 10 pts | Friction points encountered, key learnings, "aha moment" |
| **Overall Quality** | 10 pts | Completeness across all sections, polish, strategic thinking, coherence |

### Why Engineering Handoff is weighted highest (20 pts)

The course emphasizes that prototypes are only valuable if someone else can pick them up. The Engineering Handoff tests whether the student can articulate what's real, what's faked, what breaks, and where to start — the hardest and most practically valuable skill.

---

## 3. Evaluation Process

### Step 1: Establish Context

Read the course materials (Module 5 and Module 6 speaker notes) to understand exactly what students were taught and what was expected in their deliverables. This ensured scoring was aligned with course objectives, not arbitrary standards.

### Step 2: Ingest Submissions

- **PDF files** — read directly using document parsing
- **PPTX files** — binary files cannot be read directly; text was extracted using a Python script that parses the XML structure inside `.pptx` archives:

```python
from zipfile import ZipFile
import xml.etree.ElementTree as ET

with ZipFile(pptx_file) as z:
    slide_files = sorted([f for f in z.namelist()
                          if f.startswith('ppt/slides/slide')
                          and f.endswith('.xml')])
    for sf in slide_files:
        with z.open(sf) as slide:
            tree = ET.parse(slide)
            for t in tree.getroot().iter(
                '{http://schemas.openxmlformats.org/drawingml/2006/main}t'
            ):
                if t.text:
                    texts.append(t.text)
```

- **Web-hosted presentations** (Beautiful.ai) — fetched via screenshots when dynamic rendering prevented direct content extraction
- **Screenshots** — read as images when other formats were unavailable

### Step 3: Score Each Submission

Each submission was scored independently across all 7 dimensions. Scoring was based on:

- **Presence:** Did the student include this section?
- **Depth:** How detailed and specific is the content?
- **Quality:** Does it demonstrate genuine understanding vs. surface-level completion?
- **Originality:** Does it show the student's own thinking, not just template-following?

### Step 4: Rank and Calibrate

After individual scoring, all students were ranked and scores were reviewed for consistency. Calibration checks included:

- Are students with similar depth scoring similarly?
- Do the relative rankings reflect the actual quality differences?
- Is the 80-point floor being respected without inflating genuinely strong work?

### Step 5: Write Personalized Feedback

Each student received 4 paragraphs of personalized feedback:

1. **Lead with celebration** — what makes their submission special and what they should be proud of
2. **Highlight a specific strength** — a concrete example from their work that demonstrates real skill
3. **Acknowledge their journey** — reference their personal insights, learnings, or aha moments
4. **Encourage the next step** — frame growth areas as exciting opportunities, not deficiencies

The tone was calibrated to be warm, empathetic, and genuinely encouraging — recognizing that these are students who shipped real products and deserve to feel proud of their work.

---

## 4. Scoring Rubric Detail

### Deployed Prototype (15 pts)

| Score | Criteria |
|-------|----------|
| 14–15 | Clear, testable hypothesis with quantified bet; specific problem scenario with market context; live link works |
| 12–13 | Hypothesis present but less specific; problem scenario identified; live link provided |
| 10–11 | Basic hypothesis; generic problem framing; link may be present |

### Validation Brief (15 pts)

| Score | Criteria |
|-------|----------|
| 14–15 | Risk type named; kill switch with quantified thresholds; structured stress test with named scenarios; specific findings with data |
| 12–13 | Risk identified; kill switch present; stress test described; some findings |
| 9–11 | Partial coverage; missing kill switch or findings; surface-level validation |

### Living PRD (15 pts)

| Score | Criteria |
|-------|----------|
| 14–15 | Complete with product overview, detailed user flows, success metrics (North Star + leading), and explicit In/Out scope |
| 12–13 | Most sections present; metrics may lack specificity; scope defined |
| 9–11 | Partial PRD; missing flows or metrics; scope unclear |

### Prompt Library & Logic (15 pts)

| Score | Criteria |
|-------|----------|
| 14–15 | All three steps shown (Expand/Behavior/Refine); actual prompt text included; grounding rules with conditional logic |
| 12–13 | Structure present; some prompts shown; design system referenced |
| 8–11 | Categories mentioned but prompts not shown; high-level descriptions only |

### Engineering Handoff (20 pts)

| Score | Criteria |
|-------|----------|
| 17–20 | Functional truth table (Real/Mocked per component); data model with table names and fields; edge cases with severity; "Start Here" guide with file paths |
| 13–16 | Most components covered; data model present; some edge cases identified |
| 8–12 | Partial coverage; missing data model or edge cases; no Start Here guide |
| 0–7 | Section missing or single-line entries |

### Individual Insights (10 pts)

| Score | Criteria |
|-------|----------|
| 9–10 | Genuine friction points with specifics; key learnings that show growth; memorable "aha moment" with real substance |
| 7–8 | Insights present but less specific; learnings are valid but generic |
| 5–6 | Brief reflection; surface-level observations |

### Overall Quality (10 pts)

| Score | Criteria |
|-------|----------|
| 9–10 | All sections complete, polished, internally consistent; demonstrates strategic thinking beyond the template |
| 7–8 | Most sections complete; some areas lighter than others; shows engagement |
| 5–6 | Notable gaps or placeholder content; meets minimum but lacks polish |

---

## 5. Output

The evaluation was delivered as an interactive HTML scorecard (`evaluation-scorecard.html`) featuring:

- **Summary statistics** — total students, average score, highest/lowest
- **Evaluation criteria** — the 7 dimensions with point weights
- **Top 3 podium** — visual highlight of the highest-scoring students
- **Full rankings** — expandable cards for each student with:
  - Overall score and rank
  - Per-dimension score breakdown (7 categories)
  - Personalized feedback (4 paragraphs)
  - Standout callout highlighting each student's unique contribution

The scorecard is published via GitHub Pages for easy sharing.

---

## 6. Final Rankings

| Rank | Student | Product | Score |
|------|---------|---------|-------|
| 1 | Maria A. Ramirez Hidalgo | PULSE — Account Health Dashboard | 96 |
| 2 | Alexandra Darbyshire | Bifocal Dash — Progressive Disclosure Analytics | 95 |
| 3 | David Ninidze | VibePay — Georgian Neobank | 95 |
| 4 | Katie Elliott | HealthBloom — AI Wellness for Women 35+ | 93 |
| 5 | Mahni Shayganfar | Aethon SIM — Drone Flight Simulation | 93 |
| 6 | Effrosyni Theodoratou | SubShield — Fintech Subscription Manager | 92 |
| 7 | Giuliana Sperotto | WaveUp — Peer-to-Peer Instructor Marketplace | 92 |
| 8 | Thomas Zielhorst-Kessels | Conservation Connect — Wildlife Project Health | 91 |
| 9 | Rihab Belhaj | DawnDesk — Async Standup Tool | 89 |
| 10 | Katia De Juan | Voice CRM Companion | 88 |
| 11 | Vikrant Shukla | LocalVouch Hub — Marketplace Trust Solution | 87 |
| 12 | Wendy Voon | V-Pulse — B2B Retention Dashboard | 87 |
| 13 | Hwanchul Seong | Bounce — Insight-First Analytics Dashboard | 86 |
| 14 | Bandar Alassmi | Namaa — AI-Powered Adaptive Learning | 85 |
| 15 | Shifali Gupta | Meal Plan Done — AI Meal Planner | 83 |
| 16 | Omar Bahgat | Pulseboard — Customer Ops Dashboard | 82 |
| 17 | David Mitchell-Dawson | Parametric Business Interruption Insurance | 81 |
| 18 | Rishika Verma | Passport AI — Onboarding Flow | 80 |

**Average Score:** 88.6 / 100

---

## 7. Key Observations

- **Strongest dimension across the cohort:** Individual Insights — nearly every student reflected genuinely on their experience
- **Most variable dimension:** Engineering Handoff — ranged from missing entirely to exhaustive 30-slide documentation
- **Common strength:** Problem framing and hypothesis clarity were consistently strong, reflecting the course emphasis on "bet before build"
- **Common growth area:** Prompt Library sections often described prompts at a high level rather than including actual prompt text
- **Standout trend:** Several students applied the course directly to real jobs (Rishika at Euromonitor, Katie with HealthBloom, David Ninidze with VibePay for the Georgian market), demonstrating immediate professional value from the course

---

*Interactive scorecard: [evaluation-scorecard.html](evaluation-scorecard.html)*
