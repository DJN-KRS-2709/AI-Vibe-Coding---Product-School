# Module 5: Make It Real — Carlos Brief

## TL;DR
M5 is where the prototype becomes a product AND goes live. It stops being a facade and becomes a working product with a real database, real authentication, real error handling — and then deploys to a live URL anyone can access. **Your prototype actually works now. And it's in the world.**

Carlos's exact words: *"I can connect to a database. I can connect to Stripe. Oh, shit. I can push something to production. That would be magic."* M5 delivers every part of that quote — including the production push.

---

## The Progression

| Module | What Students Build | The Wow | VP Reaction |
|--------|-------------------|---------|-------------|
| M1 | First app in minutes | "I made an app" | "Cool demo" |
| M2 | Hypothesis-driven prototype | "It has real data" | "What did you learn?" |
| M3 | Multi-screen product with states | "It behaves like software" | "When did engineering build this?" |
| M4 | Living PRD + clean code | "It wrote its own spec" | "Send me the spec" |
| **M5** | **Real database, auth, error handling + deployed** | **"It's live. On my phone."** | **"Wait — this has a real URL?"** |
| M6 | Analytics, AI analysis, iteration | "It's getting better from data" | "How did you measure that?" |

---

## The M5 WOW Moment

**The paradigm shift:** Everything through M4 was visual. Beautiful, polished, but a facade — hardcoded data, no persistence, no real users. M5 is when the facade becomes real — and then goes live.

**Beat 1 — The Persistence Moment (after database):**
Student enters data. Refreshes the page. The data is still there. They close the tab, reopen it — still there. *"It persists. This isn't a mockup anymore."*

The instructor shows the Supabase dashboard — the actual data sitting in a real table. The prototype is talking to a real database.

**Beat 2 — The Multi-User Moment (after auth):**
Student logs in as User A. Sees their data. Logs out. Creates a new account as User B. Different data. Real multi-user behavior. *"This is a real product."*

**The Chaos Round (bonus beat):**
Instructor triggers a "chaos event" — API returns an error, database connection drops. Students who handled edge cases see error messages. Students who didn't see blank screens. *"Real products break. Yours should break gracefully."*

**Beat 3 — The Deploy Moment (after five-tab reveal):**
Instructor clicks Deploy in Lovable. Gets a live URL. Opens it on their phone. Drops it in Slack. Students deploy their own products. They open them on their phones. They share URLs with classmates. Someone signs up on your product from THEIR device. *"That's your product. On your phone. With a real URL. Anyone in the world can open that right now."*

This is the emotional climax of the entire course. Every student will have this moment.

---

## Instructor Demo (Retention Engine)

Starting from the M4 prototype (clean code, Living PRD):

**Prompt 1 — Connect (Database):**
Add Supabase. Create users and invites tables. When a user sends an invite, store it in the database. When the team workspace loads, fetch real invites. When the PM dashboard loads, calculate actual metrics from real data.

*Expected result:* Send an invite, refresh the page — it's still there. Open Supabase dashboard — data in the table.

**Prompt 2 — Auth (Authentication):**
Add Supabase authentication. Login/signup screen. After login, fetch only this user's team invites. Different users see different data. Show username in header. Logout button.

*Expected result:* Log in as User A — see their invites. Log out. Log in as User B — different invites. Real multi-user behavior.

**Prompt 3 — Edge Cases (Failure Handling):**
Handle: Supabase connection failure (error message), no invites yet (empty state + CTA), invite submission failure (error + retry), data loading (skeleton screens).

*Expected result:* Disconnect WiFi — error message instead of blank screen. New user — helpful empty state instead of empty list.

---

## Student Lab (Marketplace Trust)

Students apply the same 3-prompt pattern to their M3/M4 prototypes:

1. **Connect:** Add Supabase. Store provider verification data, booking data, dispute records. Real data that persists.
2. **Auth:** Provider accounts and customer accounts see different views. Providers see their verification status. Customers see provider trust scores.
3. **Edge Cases:** Provider fails verification — what does the customer see? Booking cancelled mid-transaction — where does the money go? API is slow — loading skeletons instead of frozen UI.

**Deliverables:**
- Updated prototype with real integrations
- Engineering Handoff Note (first draft) — what's real, what's mocked, what edge cases are handled
- Integration prompts added to Living Prompt Pack

---

## What Makes M5 Different

### M4 graduated the prototype. M5 makes it functional and ships it.

In M4, the prototype "wrote its own spec" — the Living PRD described the product, the code was clean, an engineer could read it. But the product itself was still a facade. Hardcoded data. No users. No persistence.

M5 is the moment the facade falls away AND the product goes live. Data persists. Users are real. Errors are handled. Then it deploys to a live URL. The prototype stops being a demonstration and becomes a shipped product.

This matters because:
- **Stakeholders can use it** — not just see a demo, but open a URL on their phone. Sign up, enter data, come back tomorrow. Share it with anyone.
- **Engineers can evaluate the backend** — real schema, real auth model, real edge case handling. The technical handoff becomes concrete.
- **The PM can answer "is this real?"** — not "it looks real" but "yes, it's deployed. Here's the URL."

---

## How It Addresses Carlos's Feedback

| Carlos Principle | How M5 Delivers |
|-----------------|----------------|
| **Every module has fireworks** | Three distinct beats: persistence moment (Beat 1), multi-user moment (Beat 2), deploy moment (Beat 3). Plus Chaos Round. |
| **Hands-on over slides** | 30 min lab (database + auth + edge cases) + 10 min chaos round + 5 min Break It + 15 min deploy lab = 60 min hands-on. 58% hands-on ratio. |
| **"I can connect to a database"** | Directly delivers Carlos's vision. Students see Supabase dashboard with their data. It's real. |
| **"I can push something to production"** | Deployment is now the M5 climax. One-click deploy, live URL, product on their phone. Carlos's exact words become reality. |
| **Engineering handoff** | Handoff Note (Deliverable #5) starts here — honest assessment of what's real vs. mocked. Engineers can inherit it. |
| **Not just prototyping** | M5 explicitly crosses the line from prototyping to shipping. Students deploy a live product. |
| **Break It is memorable** | Break It exercise: compressed to 5 min but the visceral contrast still lands. |

---

## Module Flow

| # | Type | Time | What Happens |
|---|------|------|-------------|
| 1-2 | Opening | 8 min | Title, bridge from M4, agenda |
| 3-5 | Demo | 15 min | Instructor demo: 3 prompts (DB → Auth → Edge Cases). Two wow beats. |
| 6-8 | Teaching | 12 min | Integration patterns, edge case thinking, handoff note structure |
| 9 | Activity | 5 min | "What would you integrate?" — plan before building |
| 10 | Teaching | 3 min | Security checklist (60-second version) |
| 11-12 | Lab | 30 min | Part 1: Database (15 min). Part 2: Auth + Edge Cases (15 min). Using Integration Planner. |
| 13 | Chaos | 10 min | Instructor triggers failures. Students handle them. Group discussion. |
| 14 | Share | 1 min | Quick share: what surprised you? |
| 15 | Break It | 5 min | The prototype with zero error handling (compressed) |
| 16 | Wow | 3 min | Five-tab reveal: M1 → M2 → M3 → M4 → M5 side by side |
| 17 | Demo | 3 min | Instructor deploys in Lovable. Live URL. Opens on phone. Drops in Slack. |
| 18 | Lab | 15 min | Students deploy. Test on phone. Share URLs. Try classmates' products. |
| 19 | Debrief | 3 min | Deploy debrief: "What's the difference between preview and deployed?" |
| 20-23 | Wrap | 8 min | Takeaways, accountability, M6 preview, survey |
| | | **~121 min** | **Buffer: ~1 min. If tight, compress Deploy Lab to 10 min.** |

---

## Interactive Tool

### M5 - Integration Planner
The lab companion for M5. Guides students through planning and executing their backend integration:
- **Scenario selector** (Retention Engine, Internal Tool, Marketplace Trust, Dashboard) with auto-populate
- **Database schema section** — what tables, what fields, what relationships
- **Auth flow section** — what type of auth, what user roles, what permissions
- **Edge case checklist** — common edge cases with scenario-specific items
- **3 integration prompt cards** (Connect, Auth, Edge Cases) with template hints
- **Engineering Handoff Note section** — what's real, what's mocked, what edge cases are handled
- **Full preview + copy/export** for documentation
- **localStorage persistence** + import/export for portability

---

## One Sentence

M5 is the moment the prototype stops being a facade and becomes a deployed product — real data, real users, real error handling, live URL — delivering Carlos's entire quote: "I can connect to a database. I can push something to production."
