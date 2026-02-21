# Module 2 — Context Data Packs

**Purpose:** Pre-prepared qualitative and quantitative feedback files that students import into their prototypes during the M2 lab. This is the "context injection" that makes the M2 wow moment work — prototypes built with real data look and feel dramatically different from M1's blank-page builds.

**When distributed:** At the start of Lab Part 2 (Build With Context). Students receive the pack for their chosen scenario via Slack or a shared Google Drive folder.

**Core principle:** Students should never prototype in a vacuum. Real products have users, data, and feedback. These packs simulate that reality so even the course scenarios feel grounded.

---

## What's in Each Pack

Every scenario pack contains **three files**:

| File | Format | What It Contains | How Students Use It |
|---|---|---|---|
| `feedback.md` | Markdown | 8–12 qualitative quotes from users, stakeholders, and support tickets | Paste into the prompt as context. "Here's what users are saying." The tool builds with this voice in mind. |
| `metrics.csv` | CSV | 15–20 rows of fictional but realistic quantitative data (usage stats, conversion rates, time-on-task, etc.) | Import as a data source. The prototype can display real-looking charts, tables, or KPI cards — not placeholder "lorem ipsum" data. |
| `scenario-brief.md` | Markdown | A one-page problem brief with stakeholder context, constraints, and competing priorities | Students paste this as the opening context block in their prompt. It replaces the generic "build me an app" with "here's the full situation." |

**Total prep time per scenario:** ~2 hours. Fictional but realistic data. Can be generated with AI assistance and refined for authenticity.

---

## Scenario 1: The Retention Engine

### feedback.md — User & Stakeholder Quotes

```markdown
# The Retention Engine — User & Stakeholder Feedback

## User Quotes (from exit surveys and support tickets)

1. "I signed up because my manager told me to. I opened it once, couldn't figure out where my tasks were, and went back to Notion." — Churned user, Day 3

2. "The onboarding asked me to set up a project, but I don't even know what a 'workspace' is in your tool. I just need a to-do list." — Churned user, Day 1

3. "I actually liked it once I figured out the board view. But it took me two weeks to find it. By then my trial was almost over." — Retained user

4. "I invited my co-founder on Day 2 and we started using it together. That's when it clicked — it's a team tool, not a solo tool." — Retained user, power user

5. "Why can't I just share a link to my board? I had to explain to my teammate how to sign up, create an account, join the workspace... she gave up." — Churned user, Day 7

6. "The weekly summary email is the only reason I come back. Without it I'd forget this tool exists." — At-risk user

7. "I tried to invite my team but the invite flow asked for their 'role' and 'department.' I don't know their department codes. I just want to add them." — At-risk user, Day 4

8. "Your competitor lets me import my existing tasks from Trello. You don't. So I'm running two tools and that's not sustainable." — Churned user, Day 14

## Stakeholder Quotes

9. VP of Customer Success: "The data is clear — users who invite a teammate in the first 3 days retain at 3x the rate. But only 12% of new users send an invite in that window."

10. Head of Product: "We buried the invite button in Settings > Team > Members. I know. It's on the roadmap to move it."

11. CEO: "I don't care if it's onboarding or invites or whatever. I need the 90-day churn number to drop by half or we're not raising our Series B."

12. Data Analyst: "There's a weird correlation — users who create their first task within 10 minutes of signup retain at 2x. But 60% of users never create a task at all. They just look around and leave."
```

### metrics.csv — Quantitative Data

```csv
metric,value,segment,time_period,notes
signup_to_first_task_minutes,8.2,retained_users,first_session,Median time for users who stay past 90 days
signup_to_first_task_minutes,never,churned_users,first_session,60% never create a task
day_3_invite_rate,0.12,all_users,first_3_days,Only 12% invite a teammate
retention_90_day_with_invite,0.68,invited_teammate,90_days,Users who invite retain at 68%
retention_90_day_without_invite,0.22,solo_users,90_days,Solo users retain at 22%
feature_discovery_board_view,0.31,all_users,first_14_days,31% find board view in first 2 weeks
feature_discovery_board_view,0.89,retained_users,first_14_days,89% of retained users found board view
onboarding_completion_rate,0.44,all_users,first_session,44% complete full onboarding
onboarding_drop_off_step,workspace_setup,churned_users,first_session,Highest drop-off at workspace config
weekly_email_open_rate,0.62,all_users,weekly,Summary email drives 35% of return visits
nps_score,24,all_users,quarterly,Below benchmark of 40
nps_score,71,power_users,quarterly,Power users love it
support_tickets_onboarding,342,all_users,monthly,38% of all support tickets
churn_rate_90_day,0.30,all_users,quarterly,Target: reduce to 0.15
mau_to_dau_ratio,0.18,all_users,current,Low daily engagement
```

### scenario-brief.md — Problem Brief

```markdown
# Scenario Brief: The Retention Engine

## The Company
B2B project management SaaS. 5,000 paying teams. $4.2M ARR. Series A. 18 months old.

## The Problem
30% of new customers churn within 90 days. The company cannot raise Series B with this churn rate. The board has given the team one quarter to show measurable improvement.

## What We Know
- Users who invite a teammate in the first 3 days retain at 3x the rate (68% vs 22%)
- Only 12% of new users send an invite in the first 3 days
- The invite button is buried in Settings > Team > Members
- 60% of new users never create their first task
- Users who find the board view retain at higher rates, but only 31% discover it in the first 2 weeks

## Competing Hypotheses
- **VP Customer Success:** "It's a team activation problem. Make inviting effortless."
- **Head of Product:** "It's a feature discovery problem. Users don't find the features that make us sticky."
- **CEO:** "I don't care what it is. Cut 90-day churn in half."

## Constraints
- No engineering resources for 6 weeks (they're finishing a migration)
- Must work within the existing product — no standalone app
- Budget: $0 (prototype only, no paid tools beyond what we have)

## Your Job
Prototype the intervention that has the highest likelihood of reducing 90-day churn. Use the data and feedback to identify the riskiest assumption, then build to test it.
```

---

## Scenario 2: The Internal Tool Nobody Uses

### feedback.md — User & Stakeholder Quotes

```markdown
# The Internal Tool Nobody Uses — User & Stakeholder Feedback

## Sales Rep Quotes (from internal survey and 1:1s)

1. "I know I'm supposed to log my calls. But by the time I open the CRM, find the right contact, click through three screens, and type my notes... I've forgotten half of what was said." — Senior AE

2. "I just text myself after calls and paste it into a Google Doc. I know that's not ideal but at least I can find it later." — SDR

3. "The CRM wants me to fill out 'Next Steps,' 'Decision Maker,' 'Budget Range,' 'Timeline' after every single call. Most of the time I don't have that info yet. So I just skip it." — AE

4. "I used it for a week when I started. Then I realized nobody else on the team uses it either, so why bother?" — New hire, 2 months in

5. "If it could just listen to my calls and fill itself out, I'd use it every day. The problem isn't the tool — it's the data entry." — Senior AE

6. "My manager checks the CRM once a quarter for pipeline reviews. That's literally the only time it matters. So I bulk-update everything the night before." — AE

7. "I actually like the reporting features. But the data in there is garbage because nobody enters it consistently. So the reports are useless." — Sales Manager

8. "The mobile app crashes constantly. I'm usually in my car between meetings. If I can't do it from my phone, it's not happening." — Field Sales Rep

## Stakeholder Quotes

9. VP of Sales: "We spent $180K building this tool. 18% adoption. I need to either fix it or justify buying Gong to the board. Either way, I need a prototype by end of month."

10. Engineering Lead: "The tool works fine. The problem is user behavior, not the software. We've offered training three times — nobody shows up."

11. CEO (from all-hands): "Maybe we should just buy Gong. I've heard good things. Can someone look into this?"

12. Revenue Ops: "We're losing an estimated $2.3M annually in deal intelligence because reps don't document. When a rep leaves, their entire book of business context walks out the door."
```

### metrics.csv

```csv
metric,value,segment,time_period,notes
adoption_rate,0.18,all_reps,current,18% active weekly users
daily_active_users,11,all_reps,current,Out of 200 reps
avg_time_to_log_call,4.5,active_users,per_call,Minutes from call end to note saved
calls_per_rep_per_day,6.2,all_reps,daily,Average across team
calls_logged_per_rep_per_day,0.8,all_reps,daily,Most calls go unlogged
fields_completed_per_entry,3.2,active_users,per_entry,Out of 9 required fields
mobile_crash_rate,0.23,mobile_users,per_session,23% of mobile sessions crash
training_attendance_rate,0.11,all_reps,last_3_sessions,11% attend voluntary training
bulk_update_before_review,0.67,all_reps,quarterly,67% bulk-update night before pipeline review
rep_turnover_annual,0.34,all_reps,annual,34% annual turnover
knowledge_loss_per_departure,estimated_47_deals,departing_reps,per_event,Avg deals with no CRM context
gong_annual_cost,285000,company,annual,Alternative solution estimate
current_tool_build_cost,180000,company,one_time,Sunk cost
nps_internal_tool,-12,all_reps,last_survey,Negative NPS
```

### scenario-brief.md

```markdown
# Scenario Brief: The Internal Tool Nobody Uses

## The Company
Mid-market SaaS. 200-person sales team across 3 offices + remote. $45M ARR. Series C.

## The Problem
Internal CRM note-taking tool built last year has 18% adoption. Sales reps prefer Google Docs, text messages to themselves, or nothing at all. The company is losing institutional knowledge with every rep departure (34% annual turnover). The CEO mentioned buying Gong at the all-hands — the VP of Sales is under pressure to show the internal tool can work.

## What We Know
- Average time to log a call: 4.5 minutes (too long for reps between meetings)
- Reps make ~6 calls/day but log fewer than 1
- The tool requires 9 fields per entry; reps fill out 3.2 on average
- Mobile app crashes 23% of sessions
- 67% of reps bulk-update the CRM the night before quarterly pipeline reviews
- Reps who DO use it consistently report better win rates, but correlation ≠ causation

## Competing Hypotheses
- **VP Sales:** "Make it so easy they can't NOT use it. Under 30 seconds per call."
- **Engineering:** "The tool works. It's a training problem."
- **Revenue Ops:** "The real cost isn't the tool — it's the $2.3M in lost deal intelligence annually."
- **CEO:** "Just buy Gong."

## Constraints
- Cannot replace the existing CRM (political reasons — it was the CTO's initiative)
- Must layer on top of or integrate with the existing tool
- Budget: prototype only (proving the concept before requesting build resources)
- Sales team won't participate in another training session

## Your Job
Prototype an intervention that gets adoption above 50% without requiring training. Use the data and feedback to identify the real blocker, then build to test your hypothesis.
```

---

## Scenario 3: The Marketplace Trust Problem

### feedback.md

```markdown
# The Marketplace Trust Problem — User & Stakeholder Feedback

## Customer Quotes (from user research interviews)

1. "I found three providers who looked good. None had reviews. I'm not going to be the guinea pig who finds out they're terrible." — Browsed, didn't book

2. "I booked once. The provider was 45 minutes late and didn't apologize. There was no way to report it or get a refund. I deleted the app." — One-time booker, churned

3. "On Airbnb I trust the system because of the guarantee. Here, if something goes wrong, I'm on my own." — Browsed, didn't book

4. "I would pay more for a 'verified' provider. I don't care about the cheapest option — I care about not having a stranger in my house who I know nothing about." — Browsed, didn't book

5. "The provider profiles are just a name and a photo. No bio, no work samples, no response time. How am I supposed to decide?" — Browsed, didn't book

6. "I actually had a great experience! But the app never asked me to leave a review. I would have." — Satisfied booker

## Provider Quotes

7. "I signed up a month ago. Zero bookings. No one will take a chance on the new person. It's a chicken-and-egg problem." — New provider

8. "I do great work but I can't get my first review. I offered 50% off for my first 3 customers and the platform doesn't even let me do that." — New provider

9. "The top providers have 50+ reviews and get all the bookings. The rest of us get nothing. There's no way to break in." — Provider, 3 months, 0 reviews

## Stakeholder Quotes

10. Head of Growth: "Signups are up 22% QoQ. Bookings are flat. The funnel breaks at the provider selection page."

11. Head of Product: "We need to solve the cold-start problem for new providers. If we can't get them their first 3 bookings, we lose them."

12. CEO: "I want a guarantee program. Airbnb has one. We need one. But the team keeps telling me it's complicated."
```

### metrics.csv

```csv
metric,value,segment,time_period,notes
registered_users,50000,all,current,Total signups
monthly_active_users,8000,all,monthly,Browsing or booking
signup_to_first_booking_rate,0.14,customers,all_time,Only 14% of signups ever book
browse_to_book_conversion,0.06,customers,monthly,6% of browsing sessions result in booking
provider_page_bounce_rate,0.71,customers,monthly,71% leave the provider page without action
avg_reviews_per_provider,2.1,all_providers,current,Heavily skewed — median is 0
providers_with_zero_reviews,0.64,all_providers,current,64% have zero reviews
new_provider_first_booking_days,47,new_providers,median,Median 47 days to first booking
new_provider_churn_90_day,0.72,new_providers,90_days,72% of new providers leave within 90 days
top_10_providers_booking_share,0.58,top_providers,monthly,Top 10% get 58% of all bookings
customer_willingness_to_pay_premium_verified,0.73,surveyed_customers,survey,73% would pay more for verified
repeat_booking_rate,0.41,booked_customers,6_months,Those who book once often book again
review_request_sent,0,all,current,Platform does not prompt for reviews
support_complaints_trust,156,customers,monthly,Trust-related complaints
nps_score,18,all_users,quarterly,Low trust drags NPS
```

### scenario-brief.md

```markdown
# Scenario Brief: The Marketplace Trust Problem

## The Company
Peer-to-peer home services marketplace. 50K registered users, 8K MAU. Pre-Series A. 2 years old.

## The Problem
Bookings are flat despite 22% QoQ signup growth. The funnel breaks at provider selection — 71% bounce from the provider page. The root cause: customers don't trust providers who have no reviews, and 64% of providers have zero reviews. New providers wait a median of 47 days for their first booking; 72% churn within 90 days.

## What We Know
- The platform never prompts customers to leave reviews (no review request system exists)
- 73% of surveyed customers would pay a premium for "verified" providers
- Provider profiles show only name and photo — no bio, work samples, or response time
- Top 10% of providers (by reviews) capture 58% of all bookings
- Repeat booking rate is 41% — once trust is established, customers come back

## Competing Hypotheses
- **Growth:** "It's a cold-start problem. Get new providers their first 3 reviews and bookings will follow."
- **Product:** "It's a profile problem. Richer profiles = more trust signals = more bookings."
- **CEO:** "It's a guarantee problem. Offer a money-back guarantee like Airbnb."

## Constraints
- Small team (8 people total). No dedicated engineering for new features.
- Must work within the existing marketplace UX — no separate app
- Cannot offer actual financial guarantees yet (no insurance partner)
- Must show traction (bookings increase) within one quarter

## Your Job
Prototype the trust mechanism that has the highest impact on first bookings for new providers. The hypothesis you test should directly address why browsers don't convert to bookers.
```

---

## Scenario 4: The Dashboard Nobody Reads

### feedback.md

```markdown
# The Dashboard Nobody Reads — User & Stakeholder Feedback

## User Quotes (from support tickets and user interviews)

1. "I log in, see 12 charts, and immediately feel overwhelmed. I don't know which one matters. So I close the tab." — New user, marketing manager

2. "I just want to know: is my campaign working? Yes or no. I don't need a scatter plot to tell me that." — New user, small business owner

3. "I love the dashboard. But I've been using it for 2 years and I know exactly where to look. My new team members are completely lost." — Power user, head of analytics

4. "The filters are confusing. I selected 'Last 30 days' but one of the charts is still showing all-time data. I don't trust the numbers anymore." — New user, product manager

5. "Someone showed me the 'custom view' feature and it changed everything. But I never would have found it on my own — it's hidden under a gear icon in the corner." — Retained user

6. "I get the weekly email summary. That's all I need. I never actually open the dashboard." — Casual user

7. "I exported the data to Google Sheets and built my own charts. Your dashboard has the data — it just doesn't present it in a way I can use." — Frustrated user, ops manager

8. "What am I looking at? — Literally what I said when I first opened it. And I have an MBA." — New user, VP of Marketing

## Stakeholder Quotes

9. PM Lead: "We built this for data analysts. Then we 10x'd our user base with non-technical users. The product didn't evolve with the audience."

10. Designer: "The information hierarchy is broken. Everything has equal visual weight. Nothing says 'look here first.'"

11. Head of Customer Success: "38% of our support tickets are some variation of 'I don't understand the dashboard.' That's 400+ tickets a month."

12. CEO: "Bounce rate is embarrassing. If new users can't get value in the first minute, we have a product problem, not a training problem."
```

### metrics.csv

```csv
metric,value,segment,time_period,notes
first_visit_bounce_rate,0.60,new_users,monthly,60% leave within 30 seconds
time_to_first_insight,never,new_users,first_session,Most new users never find actionable data
time_to_first_insight_seconds,45,power_users,per_session,Power users know exactly where to look
charts_on_default_view,12,all,current,Information overload
filters_available,4,all,current,Date range / segment / source / custom
filter_usage_rate,0.22,new_users,first_30_days,Only 22% of new users try filters
filter_usage_rate,0.91,power_users,per_session,Power users filter constantly
custom_view_discovery_rate,0.08,new_users,first_30_days,8% find the custom view feature
custom_view_usage_power_users,0.76,power_users,per_session,76% of power users use custom views
weekly_email_open_rate,0.54,all_users,weekly,Many users rely solely on the email
data_export_rate,0.19,all_users,monthly,19% export to build their own charts
support_tickets_dashboard,412,all_users,monthly,38% of all support volume
user_base_composition_technical,0.20,all_users,current,Only 20% are data-savvy
user_base_composition_non_technical,0.80,all_users,current,80% are business users
nps_new_users,11,new_users,quarterly,Very low
nps_power_users,72,power_users,quarterly,Power users love it
monthly_active_users,14200,all_users,monthly,Growing but retention lagging
```

### scenario-brief.md

```markdown
# Scenario Brief: The Dashboard Nobody Reads

## The Company
Customer-facing analytics platform. 14,200 MAU. $8.5M ARR. Series B. 3 years old.

## The Problem
60% first-visit bounce rate. The dashboard was built for data analysts but the user base is now 80% non-technical business users (marketing managers, small business owners, ops leads). New users see 12 charts on the default view and leave within 30 seconds. Meanwhile, power users (20%) love the product and have NPS of 72.

## What We Know
- 12 charts on the default dashboard with no hierarchy — everything has equal visual weight
- Only 8% of new users discover the "custom view" feature (76% of power users rely on it)
- 54% of users rely on the weekly email summary instead of the dashboard itself
- 19% export data to Google Sheets to build their own charts
- 38% of support tickets (~412/month) are dashboard comprehension questions
- New users who DO find value (via custom views or guided exploration) retain at 3x the rate

## Competing Hypotheses
- **PM Lead:** "Information overload. We need a simplified default view for non-technical users."
- **Designer:** "It's a hierarchy problem. Nothing tells users where to look first."
- **Engineering:** "Just add a tutorial. Problem solved."
- **Customer Success:** "We're drowning in tickets. Whatever you build, make it self-explanatory."

## Constraints
- Cannot remove charts from the power user view (they'll revolt)
- Must serve both audiences (non-technical AND power users) — likely means role-based views
- The data pipeline is solid — the problem is presentation, not data quality
- Budget: prototype only (prove the concept before committing engineering)

## Your Job
Prototype the intervention that gets first-visit bounce rate below 30% for non-technical users while preserving the power user experience. Use the data and feedback to identify whether the core issue is information overload, lack of guidance, or irrelevant defaults.
```

---

## How Students Use the Packs in the Lab

### Step-by-step (instructor guidance):

1. **Download your pack** (Slack or shared folder) — 1 minute
2. **Read the scenario brief** — this replaces the generic scenario card. Now you have the full context. — 2 minutes
3. **Scan the feedback quotes** — highlight 2-3 that directly relate to your hypothesis. These become part of your prompt context. — 2 minutes
4. **Open the metrics CSV** — identify 3-5 data points you want your prototype to display or reference. — 2 minutes
5. **Build your prompt** using the Context/Reference/Constraint/Output framework:
   - **Context:** Paste the scenario brief
   - **Reference:** Your Mobbin screenshot or product screenshot
   - **Constraint:** "Use the following real user quotes in the onboarding flow..." or "Display these actual metrics in the dashboard..."
   - **Output:** Specify the screens and flows you need
6. **Build in Lovable** — the tool now has rich context, visual references, and real data to work with. The output will be dramatically different from M1.

### What the instructor watches for:
- Students who skip the data and just prompt generically (redirect them — "use the pack")
- Students who try to include ALL the data (redirect — "pick the 3-5 most relevant data points")
- Students who don't connect the data to their hypothesis (redirect — "which of these data points would prove or disprove your assumption?")

---

## Scenario 5: Bring Your Own (Company Track)

Students on the company track don't receive a pre-made data pack — they build their own using this template. The template mirrors the same three-file structure so that all students enter Lab 2 with equivalent context, regardless of track.

### Distributed via Slack at the start of Lab 1.

### feedback-template.md — Blank Template

```markdown
# [Your Company / Product] — User & Stakeholder Feedback

## Instructions
Gather 5-8 real quotes from your product's users, stakeholders, or support channels.
Sources: user interviews, NPS comments, support tickets, Slack messages, meeting notes, customer emails.
If you don't have exact quotes, paraphrase from memory — the point is to ground your prototype in real user voice.

## User Quotes

1. "[Quote from a user about the problem you're solving]" — [Role, context]

2. "[Quote]" — [Role, context]

3. "[Quote]" — [Role, context]

4. "[Quote]" — [Role, context]

5. "[Quote]" — [Role, context]

## Stakeholder Quotes

6. [Title/Role]: "[What they think the problem is or what they want built]"

7. [Title/Role]: "[A competing perspective or priority]"

8. [Title/Role]: "[The constraint or pressure they're facing]"
```

### metrics-template.csv — Blank Template

```csv
metric,value,segment,time_period,notes
[key_metric_1],[value],[who],[when],[why this matters]
[key_metric_2],[value],[who],[when],[why this matters]
[key_metric_3],[value],[who],[when],[why this matters]
[key_metric_4],[value],[who],[when],[why this matters]
[key_metric_5],[value],[who],[when],[why this matters]
```

**Guidance for filling this in:**
- Pull 5-10 real metrics from your product's analytics, dashboards, or reports
- Good metrics: conversion rates, adoption rates, retention curves, time-on-task, NPS scores, support ticket volumes, engagement rates
- Include the segment (all users? new users? power users?) and time period
- If you don't have exact numbers, use your best estimate — the point is realistic data in the prototype, not precision

### scenario-brief-template.md — Blank Template

```markdown
# Scenario Brief: [Your Product / Initiative]

## The Company
[One sentence: what the company does, size, stage]

## The Problem
[2-3 sentences: what's broken, what's the impact, why it matters now]

## What We Know
- [Data point or insight 1]
- [Data point or insight 2]
- [Data point or insight 3]
- [Data point or insight 4]

## Competing Hypotheses
- **[Stakeholder 1 title]:** "[What they think the problem is]"
- **[Stakeholder 2 title]:** "[A different perspective]"
- **[Stakeholder 3 title]:** "[The constraint or political pressure]"

## Constraints
- [What you can't change — technical, political, timeline, budget]
- [What must stay the same — existing systems, user base, etc.]

## Your Job
[One sentence: what you're prototyping and what hypothesis you're testing]
```

**Instructor note for Bring Your Own students:**
- Check that they have at least 5 user/stakeholder quotes and 5 metrics before Lab 2
- If they're struggling to fill in the template, suggest they pull from: last team meeting notes, their product's NPS comments, recent support tickets, or a conversation with a colleague
- Anonymization is fine — change company/product names, round numbers. Keep the problem real.

---

## Preparation Checklist

| Task | Owner | Time Estimate | Status |
|---|---|---|---|
| Write feedback.md for each scenario (4 scenarios) | Dejan | 1 hr each (4 hr total) | Drafted |
| Create metrics.csv for each scenario (4 scenarios) | Dejan | 30 min each (2 hr total) | Drafted |
| Write scenario-brief.md for each scenario (4 scenarios) | Dejan | 30 min each (2 hr total) | Drafted |
| Create Bring Your Own blank templates (3 files) | Dejan | 30 min | Done |
| Review all packs for authenticity and consistency | Dana | 2 hr | Pending |
| Package and test distribution (Slack/Drive) | Dana | 1 hr | Pending |
| Write instructor guide for lab integration | Dejan | 1 hr | Pending |
| **Total** | | **~12.5 hr** | |

**Note:** All scenario data packs and the Bring Your Own templates are drafted. Dana to review for authenticity before distribution.
