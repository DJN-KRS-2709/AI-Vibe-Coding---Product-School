# Integration-Plan.md — Template

> **What this is.** The structure Lovable's Module 5 Integration Plan prompt outputs, so you can verify the AI's plan against the shape of "what good looks like" before you run the three execution prompts.
>
> **Where it lives in your repo.** Push the populated file to `05-integration/Integration-Plan.md` alongside your `04-structure/PRD.md` and `HANDOFF.md`. Module 6 pulls from `05-integration/` on GitHub — not from any tool's browser cache.

---

## Section 1 — M4 Status Check

| Question | Status |
| --- | --- |
| How many screens does this prototype have? | _e.g. 6 screens_ |
| Does a Living PRD exist? | _Yes — `04-structure/PRD.md`_ |
| Does the code use clean, descriptive variable + function names? | _Yes / partial / no_ |
| Is GitHub connected? | _Yes (link)_ |
| Is Supabase / Lovable Cloud connected? | _Yes (project)_ |

---

## Section 2 — Data Audit · What's Still Hardcoded?

| Screen / Component | Hardcoded Value | What It Should Query |
| --- | --- | --- |
| Dashboard top-card | `42 active users` | `count(distinct user_id) from sessions where active_at > now() - interval '7 days'` |
| Profile sidebar | `"Welcome, Jamie"` | `select first_name from profiles where id = auth.uid()` |
| _add a row per finding_ | | |

---

## Section 3 — Schema Design

### Existing tables (carried over from M4)

- `profiles(id uuid, first_name text, …)` — _from M4_
- _list each existing table_

### New tables (proposed)

- `invites(id uuid, sender_email text, recipient_email text, status text, created_at timestamp)` — new, replaces hardcoded dashboard metrics

For each new table, list every field with its type (`uuid`, `text`, `int`, `boolean`, `timestamp`, `jsonb`) and a one-line note on its purpose.

---

## Section 4 — Auth Model & Permissions

### Roles

| Role | Sees / can do |
| --- | --- |
| `user` (default) | Their own profile, their own invites, the dashboard scoped to their data. |
| `admin` (optional) | All profiles, all invites, full dashboard. |

### Row-Level Security rules

| Table | RLS policy |
| --- | --- |
| `invites` | `auth.uid() = sender_id` — each user sees only invites they sent. |
| `profiles` | `auth.uid() = id` — users see only their own profile. |

---

## Section 5 — Prompts

Three ready-to-paste prompts, customised to this project's actual table / screen / field names.

### Prompt 1 — Schema Expansion

```
[Lovable will generate this — paste back into Lovable to run]
```

### Prompt 2 — Auth UI + Row-Level Security

```
[Lovable will generate this — paste back into Lovable to run]
```

### Prompt 3 — Edge Cases

```
[Lovable will generate this — paste back into Lovable to run]
```

---

## Section 6 — Edge Case Checklist

- [ ] **Database connection failure** — visible error + Retry button (never a blank screen).
- [ ] **Empty data states** — helpful message + CTA when a list / search returns zero rows.
- [ ] **Form submission failure** — inline error that preserves the user's input.
- [ ] **Loading states** — skeleton screens on every screen that fetches data.
- [ ] **Session expiry** — redirect to login with a "your session ended" message.
- [ ] _add any product-specific edge cases_

---

## Section 7 — Stress Test Plan

| # | Test | What to do | Expected behaviour |
| --- | --- | --- | --- |
| 1 | **The Kill Switch** | DevTools → Network → Offline. | UI shows clear error + Retry, not a hung screen. |
| 2 | **The Ghost User** | Sign up with a brand-new email. | Active empty state with a "Get Started" CTA, not blank. |
| 3 | **The Spam Click** | Hit Submit 5× rapidly. | One transaction, not five duplicates. |

---

## Section 8 — Handoff Note

### What's Real vs What's Mocked

| Feature | Status | Notes |
| --- | --- | --- |
| Dashboard metrics | ✅ Real | Now live from `invites` + `sessions`. |
| Profile editing | ✅ Real | Persisted via `profiles`. |
| _row per major feature_ | | |

### Database Schema Summary

- `profiles` — one row per authenticated user.
- `invites` — outbound invites, owned by sender.
- _one line per table_

### Auth & RLS Model

Brief description of who can see what. Reference Section 4 RLS rules above.

### Edge Cases Handled

_Filled after Lab 1, Prompt 3 runs cleanly._

### Known Gaps

_Filled after Lab 2 stress tests. Format: `[failure mode] — [observed behaviour] — [planned fix or accept as known]`._

### Live URL

_Filled after Lab 2 Publish step._
