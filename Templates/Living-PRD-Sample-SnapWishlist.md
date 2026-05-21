# 🔎 Sample Living PRD: Airbnb SnapWishlist

> Extracted, not imagined. This is what a Living PRD looks like after running the extract prompt against a working prototype. Use it as a reference for what "good" looks like when you build your own.

---

## 1. 🔎 Product Overview

> *A high-level description of the validated system, its primary functions, and the specific target persona it serves.*

**System Function:** SnapWishlist analyzes user-uploaded travel inspiration photos using multimodal AI to identify locations and vibes, then surfaces matching Airbnb listings in a personalized wishlist carousel.

**Target Persona:** *"The Visual Planner"* — A Gen-Z/Millennial traveler who plans trips based on aesthetics and Instagram vibes, not just price or dates.

---

## 2. 🎯 Strategic Hypothesis

> *A formal record of the user friction identified and the evidence-backed justification for the chosen intervention.*

**Current User Friction:** Users find travel inspiration on social media but cannot bridge the gap between a saved photo and a bookable Airbnb listing — the discovery flow is manual, slow, and disconnected.

**The Intervention:** *If* we allow users to upload an inspiration photo and let AI surface matching listings, *then* wishlist creation will increase and drop-off in the discovery phase will decrease, *because* prototype testing showed >80% location identification accuracy and positive intent signals from target users.

---

## 3. 🗺️ Functional Architecture & User Flow

> *Record a screen-by-screen map of the navigation paths, interactive logic, and specific edge cases currently handled in the code.*

**Screen Inventory:**

- Homepage (entry CTA: "Create Wishlist from Photo")
- Photo Upload Screen (library / camera roll selector)
- AI Analysis Loading Screen
- "Found it!" Results Screen (location tag + listing carousel)
- Wishlist Save Screen (add to new or existing wishlist)

**Navigation Logic:**

- User taps CTA on homepage → Upload Screen → AI Analysis → Results → Save to Wishlist

**Edge Case Handling:**

- Non-travel photo uploaded → Friendly error: "We can't fly there! Try a travel photo."
- Face detected in photo → Auto-blur applied before analysis (privacy compliance)
- Generic vibe image (no specific landmark) → Tag-based global search (e.g., "Cabin," "Forest," "Cozy")

---

## 4. 📈 Success Metrics & Measurement

> *The North Star metric, leading indicators, and the specific technical plan for tracking performance in production.*

**North Star Metric:** Number of wishlists created per week via photo upload (SnapWishlist sessions → saved wishlists).

**Leading Indicators:**

1. Photo-to-results completion rate (target >75%)
2. "Save to Wishlist" click rate on results screen (target >40%)
3. Repeat usage within 30 days

**Tracking Plan:** Event logging on `photo_upload_initiated`, `analysis_complete`, `listing_card_tapped`, `wishlist_saved`. Dashboard in internal analytics tool; weekly review by PM.

---

## 5. 🛠️ Technical Reality (Truth Report)

> *A transparent audit of what is functionally operational versus what remains a visual mock, including current infrastructure connections.*

**Functional Logic:** Image upload (JPEG/PNG), multimodal AI call (GPT-4o / Gemini Vision), location tag extraction, tag-based listing query, wishlist save flow.

**Simulated Elements:**

- Listing database is a mocked JSON file (not live Airbnb data).
- Visual Similarity Score is hardcoded in prototype — not a real ML model output.

**Infrastructure Stack:**

- Frontend: Lovable (React + Tailwind CSS).
- AI: GPT-4o or Gemini Vision API.
- Data: Mocked Airbnb Listing JSON.
- No backend persistence yet — photos discarded post-analysis.

---

## 6. ⚠️ Risk Assessment & Constraints

> *A report on current confidence levels, technical boundaries, and "Kill Switch" criteria that would justify halting the build.*

**Technical Constraints:**

- Desktop-only prototype (mobile responsiveness not yet validated).
- Depends on third-party AI API availability and rate limits.
- Mocked data limits real-world listing diversity testing.

**Kill Switch Triggers:**

- AI location accuracy falls below 60% in expanded test set.
- Latency exceeds 5 seconds consistently.
- Legal/privacy review flags photo-handling approach.

**Risk Mitigation:**

- Cap image upload size to reduce latency.
- Add fallback tag-based search if landmark detection fails.
- Confirm no photo storage post-analysis (already in spec).

---

## 7. 🧱 Production Scope

> *A definitive boundary of what is included in the current handoff, what is explicitly excluded, and what is deferred for future versions.*

**In-Scope:**

- Photo upload (JPEG/PNG).
- AI-powered location + vibe identification.
- Mocked listing carousel (3–5 results per query).
- Wishlist save (new or existing).
- Face-blur privacy layer.
- Non-travel photo error state.

**Out-of-Scope:**

- Live Airbnb listing API integration.
- User authentication.
- Price/date filtering.
- Mobile app build.
- Multi-photo uploads.

**Future Roadmap:**

- Real-time listing database connection.
- True Visual Similarity Score via embeddings model.
- Social sharing of wishlists.
- Mobile-first responsive design.
- Multi-photo mood board input.

---

## 8. 📋 Engineering Handoff Recommendations

> *A strategic guide for the build order, estimated technical effort, and unresolved architectural questions.*

**Suggested Build Order:**

1. Harden photo upload + AI call pipeline (error handling, retry logic).
2. Replace mocked JSON with live listing API (Airbnb or equivalent).
3. Implement real Visual Similarity scoring.
4. Build mobile-responsive layout.
5. Add auth + persistent wishlist storage.

**Technical Effort Estimates:**

- AI pipeline hardening: **Medium** (2–3 days).
- Live API integration: **High** (1–2 weeks, pending API access).
- Visual similarity model: **High** (requires ML expertise).
- Mobile layout: **Low–Medium** (2–4 days).

**Open Questions:**

- Will Airbnb grant API access for listing data, or is a third-party travel database needed?
- What is the acceptable latency SLA for production?
- Should face-blurring happen client-side or server-side for GDPR compliance?

---

> **How to use this sample:** This is the *shape* of a Living PRD — not the *content* of yours. Don't copy these sections; extract your own by running the prompt from `M4 - Lab Guide.html` against your prototype. Your PRD documents *your* reality, including the parts that are still mocked.
