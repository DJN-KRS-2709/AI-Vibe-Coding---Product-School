# Module 5 — Slide Changes for Dana

**Why these changes:** Module 4 already connects Supabase (database + auth + storage) and GitHub. Several M5 slides currently say things like "the database is empty," "your data is gone," and "from empty infrastructure" — none of that is true anymore after M4. Below are the exact text changes per slide.

---

## Slide 3 — Syllabus

**Current text (M5 description):**
> Ship Live Products with Full-Stack Logic — Connect your build to live databases and secure APIs to move beyond the interface. Navigate system logic and edge cases to transform standalone features into integrated, production-ready products on a live URL.

**Replace with:**
> Ship Live Products with Full-Stack Logic — Secure your build with user isolation and Row-Level Security, engineer for failure with edge case handling, and deploy to a live URL. Transform your connected infrastructure into a production-ready product.

---

## Slide 5 — Agenda

**Current item 01:**
> Moving from Standalone Logic to Integrated Systems

**Replace with:**
> Moving from Connected Infrastructure to a Secured Product

**Current item 02:**
> How to Implementing Live Database Connectivity

**Replace with:**
> How to Secure and Extend Your Integration

---

## Slide 6 — Section Header

**Current title:**
> Moving from Standalone Logic to Integrated Systems

**Replace with:**
> Moving from Connected Infrastructure to a Secured Product

---

## Slide 7 — Reflection Moment

**Current question:**
> Your prototype has come along way. What do you still think is missing to get it across the finish line as a fully deployed product for multiple users to test?

**Replace with:**
> Your database is connected. Your code is clean. Your infrastructure is live. Now imagine I send your prototype's URL to 50 strangers right now. They all sign up, enter their data, and start using it. Can User 14 see User 37's private data? What happens when someone's internet drops mid-submit? And can those 50 people even reach your product right now?

---

## Slide 8 — Instructor-Led Demo

**Current title:**
> From Empty Infrastructure to Persistent Backend

**Replace with:**
> From Connected Infrastructure to Secured Product

**Current body text:**
> Your prototype now has all the information needed for an eng handoff; with a GitHub repo that can be cloned and connected infrastructure.
> But what happens when you close the app, refresh and enter again?
> Your data is gone.

**Replace with:**
> Your prototype has a GitHub repo, clean code, a Living PRD, and a live Supabase backend — all from Module 4. The infrastructure is real.
> But the dashboard metrics? Still hardcoded. There's no login screen. No way to tell users apart. And when the connection drops? Silence.
> The foundation is there. The product isn't fully built on it yet.

**Replace "THE PROBLEM:" label with:**
> THE GAP:

---

## Slide 9 — Section Header

**Current title:**
> How to Implementing Live Database Connectivity

**Replace with:**
> How to Secure and Extend Your Integration

---

## Slide 10 — How to Prompt for Integration

**Current opening text:**
> You are moving from a linear prototype with one path and one user to a matrixed product that can handle multiple users and states with permanent memory.

**Replace with:**
> You've got the infrastructure from Module 4. Now you're moving from "database is connected" to "product is built on the database." You're prompting for complete data flows, ownership rules, and failure handling.

**Current pillar 1 description:**
> Specify table names, data types (e.g., UUID, Text, Boolean), and the relationships between them to ensure the backend can reliably store and retrieve your product's information,

**Replace with:**
> Your database is live from M4. Extend the schema to cover all the data your product displays. Specify new table names, data types, and relationships — and replace hardcoded UI values with real queries.

**Current pillar 1 example prompt:**
> "Create a table for 'Invites' with fields for sender_email, recipient_email, and a status timestamp."

**Replace with:**
> "Extend the schema. Create an 'Invites' table with fields for sender_email, recipient_email, and a status timestamp. Replace hardcoded dashboard metrics with real queries from this table."

---

## Slide 13 — Individual Exercise: Plan Before You Build

**Current intro text:**
> In this individual exercise, you will audit your existing prototype to identify the technical gaps between your static UI and a live system.

**Replace with:**
> In this individual exercise, you will audit your existing prototype to identify what's still hardcoded despite the database being connected, who needs data isolation, and where failures aren't handled.

**Current goal text:**
> Your goal is to map your data, user roles, and failure points to create a functional execution plan before you start building.

**Replace with:**
> Your goal is to map the gap between "infrastructure connected" and "production-ready" — identifying hardcoded data, missing user isolation, and unhandled failure points.

**Current step 1:**
> Audit your data status by listing key hardcoded elements in your UI, such as user metrics or account names, that must be replaced by a live database.

**Replace with:**
> Audit your data status — your database is connected, but what's actually using it? List key hardcoded elements still in your UI (dashboard metrics, counts, user info) that need to be wired to real queries.

---

## Slide 15 — Lab Section Header

**Current title:**
> Add Data Schemas and RLS Authentication To Your Prototype

**Replace with:**
> Expand Your Schema and Add RLS Authentication

---

## Slide 16 — Lab Exercise

**Current intro text:**
> In this hands-on lab, you'll use the Integration Planner to review your database schema, generate real tables in Supabase, and implement secure authentication and edge case handling.

**Replace with:**
> In this hands-on lab, you'll prompt Lovable to generate a personalized Integration Plan for your project, then use its prompts to extend your M4 database schema, wire all data to real queries, and implement Row-Level Security with edge case handling.

**Current goal text:**
> Your goal is to move to to a functional system where data survives a page refresh and users can securely log in to see their specific information.

**Replace with:**
> Your goal is to replace every hardcoded value with a real database query and add user isolation so different accounts see different data.

**Current step 1:**
> Review your suggested database schema in the 🔗 Integration Planner to customize the specific tables and fields required for your project.

**Replace with:**
> Paste the Integration Plan Prompt into Lovable — it will scan your project and generate a personalized plan with your actual tables, hardcoded values, and customized prompts. Review what it found, then use Prompt 1 to extend your schema.

**Current step 2:**
> Copy the database prompt into Lovable to create live tables in Supabase, then verify your build by entering data and refreshing the page.

**Replace with:**
> Copy the schema expansion prompt into Lovable to extend your database and wire your UI to real queries. Verify: are your dashboard metrics now pulling from the database instead of showing hardcoded numbers?

**Current "Keep in mind" text:**
> Keep in mind: You must verify that your data persists after a refresh and that different logged-in accounts see different data.

**Replace with:**
> Keep in mind: You must verify that dashboard data is computed from real queries (not hardcoded) and that different logged-in accounts see different data.

---

## Slide 22 — Your Evolved Engineering Handoff

**Current opening text:**
> Previously, you documented a plan. Now that your product is live, you are documenting a system. Your Engineering Handoff has evolved from a 'to-do' list into a source of truth for a resilient, data-driven product.

**Replace with:**
> In Module 4, your handoff documented connected infrastructure and what could be built. Now that your product is live, you are documenting a working system. Your Engineering Handoff has evolved from a technical inventory into a source of truth for a secured, deployed product.

**Under "Now: Deployed System Blueprint" — current first bullet:**
> Data Model & Schema: The real database structure and RLS rules protecting the data.

**Replace with:**
> Data Model & Schema: The expanded database structure and RLS rules enforcing per-user data isolation.

**Under "Previously: Static Technical Inventory" — current first bullet:**
> Component List: A catalog of buttons, inputs, and screens.

**Replace with:**
> Component List: A catalog of components, connected infrastructure, and notes on what's mocked vs. real.

---

## Slide 24 — Module 5 Complete

**Current subtitle under "The Static Backend: Connected":**
> You've moved past static placeholders. By finalizing your database schema and Auth rules, you've built a persistent system that secures data across every user session.

**Replace with:**
> Module 4 connected the infrastructure. Today you made your product use it. Every metric is computed from real data. Every user is isolated with Row-Level Security. The database drives every screen.

**Current subtitle under "The Sandbox Prototype: Deployed":**
> You've moved past the limitations of a private environment and into a production-ready ecosystem, transforming your isolated build into a resilient public product that handles real-world traffic and edge cases.

**Replace with:**
> You've moved past a private environment into a production-ready ecosystem. Empty states, loading skeletons, connection errors, and duplicate prevention — your product handles real-world conditions and breaks gracefully.

---

## No Changes Needed

These slides are fine as-is:

- **Slide 1** — Title
- **Slide 2** — Class Expectations
- **Slide 4** — Presentation Reminder
- **Slide 11** — Resistance Engineering for Errors & Failures
- **Slide 12** — Security Best Practices
- **Slide 14** — Quick Debrief
- **Slide 17** — Break
- **Slide 18** — Cameras On
- **Slide 19** — Post-Lab Reflection
- **Slide 20** — Stress Test section header
- **Slide 21** — Chaos Round + Deploy
- **Slide 23** — Future-Proofing with APIs
- **Slide 25** — Key Takeaways
- **Slide 26** — Extra Practice + Next Session
- **Slide 27** — Survey
- **Slide 28** — Bonus Resources
- **Slide 29** — Q&A
- **Slide 30** — End
