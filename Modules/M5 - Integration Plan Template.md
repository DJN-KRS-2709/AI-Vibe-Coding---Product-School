# Module 5 — Integration Plan Prompt

Paste this prompt into Lovable (or whatever AI building tool you're using) while your Module 4 prototype is open. It will analyze your project and generate a personalized Integration Plan as a markdown file.

---

## The Prompt

```
Analyze this project and generate a markdown file called "Integration Plan.md" with the following sections. Base everything on what actually exists in this codebase — don't make up features or data that isn't here.

## Section 1: M4 Status Check
Create a table listing:
- How many screens this prototype has (count them)
- Whether a Living PRD or product requirements document exists
- Whether the code uses clean, descriptive variable and function names
- Whether GitHub is connected
- Whether Supabase or a database backend is connected
For each item, fill in the actual status based on what you can see in the project.

## Section 2: Data Audit — What's Still Hardcoded?
Scan every screen and component. Find every value that is hardcoded in the UI instead of coming from a real database query — metrics, counts, user names, dates, status labels, sample data. Create a table with three columns:
- Screen / Component (where you found it)
- Hardcoded Value (the exact value)
- What It Should Query (the database table and calculation that should replace it)

## Section 3: Schema Design
List every database table that currently exists. Then, based on the Data Audit, propose any new tables or fields needed to replace hardcoded values. For each table, list every field with its type (uuid, text, int, boolean, timestamp, jsonb) and a short note on its purpose. Mark which tables are new vs. existing from M4.

## Section 4: Auth Model & Permissions
Based on this product's screens and user flows, define:
- What user roles exist or should exist (e.g., regular user vs. admin, buyer vs. seller)
- What each role can see and do
- Row-Level Security rules — which tables need per-user data isolation, and what the policy should be (e.g., "users can only read/write rows where user_id matches their authenticated ID")

## Section 5: Prompts
Generate three ready-to-use prompts that I can paste back into this tool one at a time. Each prompt should be specific to THIS project — use real table names, real screen names, real field names from this codebase.

### Prompt 1 — Schema Expansion
A prompt to extend the database schema, create any new tables from Section 3, and replace all hardcoded UI values identified in Section 2 with real database queries.

### Prompt 2 — Auth UI + Row-Level Security
A prompt to add a login/signup screen, implement the roles and RLS policies from Section 4, show the logged-in user's name in the header, add a logout button, and ensure different users see different data.

### Prompt 3 — Edge Cases
A prompt to handle these failure modes across the entire app:
- Database connection failure → error message with retry button (not a blank screen)
- Empty data states → helpful message with a call-to-action (not an empty list)
- Form submission failure → inline error that preserves user input
- Loading states → skeleton screens on every screen that fetches data
- Session expiry → redirect to login with a message

Each prompt should be inside a code block so I can copy it easily.

## Section 6: Edge Case Checklist
Generate a checklist (using markdown checkboxes) of every edge case this specific product should handle. Include the five from Prompt 3 plus any product-specific ones (e.g., duplicate submissions, self-referential actions, large datasets, invalid input formats). Each checkbox should have a bold label and a one-line description.

## Section 7: Stress Test Plan
Create three named stress tests tailored to this product:
- One that tests connection failure (e.g., going offline mid-action)
- One that tests empty/new user experience (signing up fresh, zero data)
- One that tests rapid repeated actions (spam-clicking submit, double-booking, etc.)
For each test, describe exactly what to do and what the expected behavior should be. Add a Pass/Fail field and space for notes.

## Section 8: Handoff Note
Create a handoff note template with these sub-sections, pre-filled based on what currently exists:
- What's Real vs. What's Mocked (table with every major feature and whether it uses real data or is still mocked)
- Database Schema Summary (one line per table with its purpose)
- Auth & RLS Model (who can see what)
- Edge Cases Handled (leave blank — to be filled after the lab)
- Known Gaps (leave blank — to be filled after stress testing)
- Live URL (leave blank — to be filled after deployment)

Format the entire output as clean markdown. Use tables, code blocks, and checkboxes where appropriate. This file will be committed to the GitHub repo as a Module 5 deliverable.
```

---

## What Happens Next

After Lovable generates the file:

1. **Review it** — Does the data audit look right? Did it catch all the hardcoded values? Are the tables correct?
2. **Run Prompt 1** (schema expansion) — then document the result in the file
3. **Run Prompt 2** (auth + RLS) — then document the result
4. **Run Prompt 3** (edge cases) — then document the result
5. **Run the stress tests** — fill in pass/fail and notes
6. **Complete the handoff note** — update what's real, known gaps, and your live URL after deployment

When complete, commit `Integration Plan.md` to your GitHub repo alongside your Living PRD and M4 engineering handoff.
