"""Build Module 5 instructor deck by reusing M4's design-system foundation.

Reads `Modules/Module 4 - Slides.html`, swaps the title + slide body for the
M5 content while keeping the <head> CSS and <script> controller verbatim.
Mirrors the canonical class catalog (see canonical-classes.md).
"""
from pathlib import Path
import re

REPO = Path(__file__).resolve().parent.parent
M4 = REPO / 'Modules' / 'Module 4 - Slides.html'
M5 = REPO / 'Modules' / 'Module 5 - Slides.html'

DEMO_ID = '1a0Oyh3jWjwgZ96SofDZkcIXCvWiOQb-X'

# ---------------------------------------------------------------------------
# M5 slide body — every section in source order. Uses canonical classes only.
# ---------------------------------------------------------------------------

BODY = r"""
<!-- 1. HERO -->
<section class="hero" data-title="Ship Live Products with Full-Stack Logic">
  <div class="hero-logo"><img src="../Design/Product-School-Logo.png" alt="Product School"/></div>
  <div class="section-label">Module 5 — Vibe Coding Certification</div>
  <h1>Ship Live Products<br><span>with Full-Stack Logic</span></h1>
  <p class="subtitle">Secure your build with user isolation and Row-Level Security, engineer for failure with edge-case handling, and deploy to a live URL. Transform your connected infrastructure into a production-ready product.</p>
  <div class="waypoints">
    <div class="waypoint"><div class="waypoint-num">1</div><div class="waypoint-text"><div class="wt-title">From Connected Infrastructure to a Secured Product</div><div class="wt-desc">The gap between functional plumbing and a real, signed-in, error-resilient product.</div></div></div>
    <div class="waypoint"><div class="waypoint-num">2</div><div class="waypoint-text"><div class="wt-title">How to Secure &amp; Extend Your Integration</div><div class="wt-desc">Prompt for schema, Row-Level Security, and external APIs. Engineer for empty / loading / error / load-bearing states.</div></div></div>
    <div class="waypoint"><div class="waypoint-num">3</div><div class="waypoint-text"><div class="wt-title">Lab — Add Data Schemas + RLS</div><div class="wt-desc">Generate your personalised Integration Plan in Lovable, then run three prompts: schema, auth/RLS, edge cases.</div></div></div>
    <div class="waypoint"><div class="waypoint-num">4</div><div class="waypoint-text"><div class="wt-title">Lab — Rapid-Fire Stress Test &amp; Deploy</div><div class="wt-desc">Kill-Switch + Ghost User / Spam Click stress tests, update HANDOFF.md, then Publish to a live public URL.</div></div></div>
  </div>
  <p class="repo-cta">Today's repo lands in <strong><code>05-integration/</code></strong> — <code>Integration-Plan.md</code> + updated <code>HANDOFF.md</code> + your live URL.</p>
  <div class="scroll-hint">Scroll to explore<span>↓</span></div>
  <div class="notes">
    <h4>Speaker Notes</h4>
    <p>Welcome to Module 5 — the production transition. The last two modules built infrastructure; today we make that infrastructure carry weight. By the end of this session every learner has a live, public URL with signed-in users, partitioned data, and graceful failure handling.</p>
    <p>Frame the arc: M4 handed an engineer the spec; M5 hands an engineer (and customers) a running system. Stress: you will deploy <em>even if</em> the stress test reveals gaps — you'll document them in HANDOFF.md and ship anyway. That's the PM move.</p>
  </div>
</section>

<!-- 2. CLASS EXPECTATIONS -->
<section class="centered" data-title="Class Expectations">
  <div class="inner">
    <div class="section-label">Cohort Norms</div>
    <h2>Class expectations.</h2>
    <p class="subtitle">Same six norms across the certification. Show up, ship something, share generously.</p>
    <div class="expect-grid">
      <div class="expect-card"><div class="expect-icon">📹</div><div class="expect-title">Cameras On</div><div class="expect-desc">Be present and visible to stay engaged in class.</div></div>
      <div class="expect-card"><div class="expect-icon">⏰</div><div class="expect-title">Arrive On Time</div><div class="expect-desc">Respect everyone's time by arriving promptly to sessions.</div></div>
      <div class="expect-card"><div class="expect-icon">🤝</div><div class="expect-title">Engage to Network</div><div class="expect-desc">Participate in labs and discussions to build your professional learning network.</div></div>
      <div class="expect-card"><div class="expect-icon">🛠️</div><div class="expect-title">Tool Readiness</div><div class="expect-desc">Lovable, GitHub, and Supabase must be active before class — we will not stop or restart for setup.</div></div>
      <div class="expect-card"><div class="expect-icon">💬</div><div class="expect-title">Use Slack</div><div class="expect-desc">Use Slack for all communication to keep questions and comments organised.</div></div>
      <div class="expect-card"><div class="expect-icon">🚀</div><div class="expect-title">Class Momentum</div><div class="expect-desc">Individual or deep-dive questions move to after-class support so the cohort keeps pace.</div></div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Run this quickly — the cohort has seen it four times. Use it as a reset for energy: cameras on, Slack questions only, no group breakouts. Day 5 is high-intensity (two labs, a live deploy) so the momentum norm matters most today.</p>
    </div>
  </div>
</section>

<!-- 3. COURSE ARC — M5 active -->
<section class="centered" data-title="The Course Arc">
  <div class="inner" style="max-width: 1180px;">
    <div class="section-label">Vibe Coding Certification — Syllabus</div>
    <h2>Where M5 sits in the arc.</h2>
    <p class="subtitle">You shipped infrastructure in M4. Today you ship a product. Then M6 turns shipping into a measurement loop.</p>
    <div class="arc-flow">
      <div class="arc-node"><div class="ad-num">M1</div>Velocity</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M2</div>Validation</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M3</div>Prompt Chaining</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M4</div>Production Specs</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node active-node"><div class="ad-num">M5</div>Full-Stack Logic</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M6</div>Measure &amp; Iterate</div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Anchor the arc once more before we go in. The bridge from M4 to M5 is the move from "engineering-ready spec" to "engineering-shipped product." After today, the M6 bridge will be from "live product" to "live product that learns from its users."</p>
    </div>
  </div>
</section>

<!-- 4. PRESENTATION REMINDER — optional showcase next class -->
<section class="centered" data-title="Presentation Reminder">
  <div class="inner" style="max-width: 880px;">
    <div class="demo-tag tag-activity">Heads-up · Next Class</div>
    <h2>Volunteer for the final showcase.</h2>
    <p class="subtitle">We're almost at the end — next class is your chance to demo your live product to the cohort and get live, actionable feedback from the instructor.</p>
    <div class="artifact-preview" style="max-width: 640px;">
      <div class="ap-title">Optional · Final Showcase</div>
      <p style="font-size:14px; color:#cdd5e3; line-height:1.7;">Your instructor will ask for 5–6 volunteers in <code>#cohort-channel</code> — first come, first served. Bring your live URL, your <code>Integration-Plan.md</code>, and the one decision you're proudest of.</p>
    </div>
    <p style="font-size:14px; color:#8899bb; margin-top:18px;">If you want feedback before you submit your final repo, this is the highest-leverage slot in the cohort.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Push hard for volunteers. Frame it as the highest-bandwidth feedback in the cohort: live demo, live feedback, in front of peers. Drop the sign-up link in <code>#cohort-channel</code> right after this slide; pin the message. Aim for 5–6 names by end of class.</p>
    </div>
  </div>
</section>

<!-- 5. TODAY'S AGENDA -->
<section class="centered" data-title="Today's Agenda">
  <div class="inner" style="max-width: 1080px;">
    <div class="section-label">Today's Agenda</div>
    <h2>Four moves, one live URL.</h2>
    <p class="subtitle">Two lectures bracketed by two labs. By the end of the second lab you publish.</p>
    <div class="waypoints">
      <div class="waypoint"><div class="waypoint-num">01</div><div class="waypoint-text"><div class="wt-title">From Connected Infrastructure to a Secured Product</div><div class="wt-desc">Instructor demo · the gap between a wired backend and a real product.</div></div></div>
      <div class="waypoint"><div class="waypoint-num">02</div><div class="waypoint-text"><div class="wt-title">How to Secure &amp; Extend Your Integration</div><div class="wt-desc">Prompt patterns for schema, RLS, and external APIs. Engineer for empty / loading / error / load-bearing states.</div></div></div>
      <div class="waypoint"><div class="waypoint-num">03</div><div class="waypoint-text"><div class="wt-title">Hands-On Lab — Add Data Schemas + RLS</div><div class="wt-desc">Generate your Integration Plan, then run three prompts in Lovable: schema · auth/RLS · edge cases.</div></div></div>
      <div class="waypoint"><div class="waypoint-num">04</div><div class="waypoint-text"><div class="wt-title">Hands-On Lab — Rapid-Fire Stress Test &amp; Deploy</div><div class="wt-desc">Kill-Switch + Ghost User / Spam Click, update HANDOFF.md, then click Publish.</div></div></div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Two labs today — Lab 1 (Schema/RLS/Edge Cases) is the heavier one, the actual production work. Lab 2 (Stress Test + Deploy) is short but the payoff: every learner walks out with a public URL. Watch the clock; if you slip on Lab 1, cut the optional API integration step (Step 7) and protect the deploy.</p>
    </div>
  </div>
</section>

<!-- 6. SECTION 01 — From Connected Infrastructure to a Secured Product -->
<section class="section-break" data-title="Section 01 · From Connected Infrastructure to a Secured Product">
  <div class="section-break-inner">
    <div class="section-num">01</div>
    <div class="lab-title">Section 01</div>
    <div class="lab-name">From Connected Infrastructure to a Secured Product.</div>
    <div class="lab-desc">Your prototype has a backend. It does not yet have a product. We'll watch what's missing and what we'll prompt to add.</div>
  </div>
</section>

<!-- 7. INSTRUCTOR-LED DEMO — From Connected Infrastructure to Secured Product -->
<section data-title="Instructor Demo · From Connected Infrastructure to Secured Product">
  <div class="inner" style="max-width: 1180px;">
    <div class="demo-tag tag-case">Instructor-Led Demo · 8 minutes</div>
    <h2>From connected infrastructure to a secured product.</h2>
    <p class="subtitle">The M4 build has a backend wired in — but the dashboard is still hard-coded, there's no login, no user isolation, no error handling. Watch what three prompts add.</p>
    <div class="demo-split">
      <div class="problem-panel">
        <span class="pp-label">⚠ The Gap</span>
        <div class="pp-headline">Functional infrastructure ≠ functional product.</div>
        <div class="pp-execs">
          <div class="pp-exec"><div class="pp-avatar">🗂️</div><div class="pp-quote">"Dashboard metrics are still hard-coded. The numbers don't reflect anything in the database."</div></div>
          <div class="pp-exec"><div class="pp-avatar">🔓</div><div class="pp-quote">"No login. Every visitor sees every record."</div></div>
          <div class="pp-exec"><div class="pp-avatar">📡</div><div class="pp-quote">"Drop the network and the UI just hangs. No error, no retry, no recovery."</div></div>
        </div>
        <div class="pp-coda">The foundation is set — but the product isn't fully powered by it yet.</div>
      </div>
      <div class="demo-video-col">
        <div class="demo-video-frame">
          <iframe src="https://drive.google.com/file/d/__DEMO_ID__/preview" allow="autoplay" allowfullscreen></iframe>
        </div>
        <div class="demo-video-cta">
          <a class="tool-btn" href="https://drive.google.com/file/d/__DEMO_ID__/view" target="_blank" rel="noopener">▶ Watch the full demo ↗</a>
          <div class="demo-helper">Three prompts: wire all data to the database · add auth + RLS · handle edge cases. Then a DevTools chaos test.</div>
        </div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Cue the demo (~8 min). Students do not build along — eyes on the screen. Call out the three prompts as they fire and the result after each: schema → real metrics; auth/RLS → users only see their own rows; edge cases → loading skeletons and retry buttons replace dead screens.</p>
      <p>End the demo on the DevTools offline toggle — that's the chaos test they'll repeat themselves in Lab 2.</p>
    </div>
  </div>
</section>

<!-- 8. SECTION 02 — How to Secure and Extend Your Integration -->
<section class="section-break" data-title="Section 02 · How to Secure &amp; Extend Your Integration">
  <div class="section-break-inner">
    <div class="section-num">02</div>
    <div class="lab-title">Section 02</div>
    <div class="lab-name">How to secure &amp; extend your integration.</div>
    <div class="lab-desc">Prompt patterns for schema, ownership rules, external APIs — and the four product states every live system has to render.</div>
  </div>
</section>

<!-- 9. HOW TO PROMPT FOR INTEGRATION — 3 numbered cards in dashboard tile pattern -->
<section data-title="How to Prompt for Integration">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">How to Prompt for Integration</div>
    <h2>Move from a connected infrastructure to a product fully built on the database.</h2>
    <p class="subtitle">🎯 <strong>The goal:</strong> prompt for complete data flows, ownership rules, and failure handling — not just visual elements. You're no longer prompting for pixels; you're prompting for <em>technical transactions</em>.</p>
    <div class="m4-complete-grid">
      <div class="m4c-tile">
        <div class="m4c-num">1</div>
        <div class="m4c-meta">
          <div class="m4c-label">Schema Expansion</div>
          <div class="m4c-title">Define Your Schema Structure</div>
          <div class="m4c-desc">Extend your live database schema to cover all displayed product data. Specify new table names, data types, and relationships to replace hardcoded UI values with live queries.<br><br><code style="background:rgba(255,255,255,0.08); padding:6px 10px; border-radius:6px; font-size:11.5px; color:#cfd9e8; display:block; line-height:1.5;">"Extend the schema. Create an 'Invites' table with sender_email, recipient_email, status, timestamp. Replace hardcoded dashboard metrics with real queries from this table."</code></div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">2</div>
        <div class="m4c-meta">
          <div class="m4c-label">Ownership Permissions</div>
          <div class="m4c-title">Script Ownership Permissions</div>
          <div class="m4c-desc">Explicitly instruct the AI to implement Row-Level Security (RLS) — partition data so each user can only interact with records tied to their authenticated session.<br><br><code style="background:rgba(255,255,255,0.08); padding:6px 10px; border-radius:6px; font-size:11.5px; color:#cfd9e8; display:block; line-height:1.5;">"Ensure users can only see records where the 'user_id' matches their authenticated session ID."</code></div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">3</div>
        <div class="m4c-meta">
          <div class="m4c-label">External APIs</div>
          <div class="m4c-title">Orchestrate External APIs</div>
          <div class="m4c-desc">Provide the API documentation and describe the trigger and action to integrate third-party services like Stripe, SendGrid, or OpenAI for extended product functionality.<br><br><code style="background:rgba(255,255,255,0.08); padding:6px 10px; border-radius:6px; font-size:11.5px; color:#cfd9e8; display:block; line-height:1.5;">"Connect the Stripe API. Trigger a checkout session when 'Upgrade' is clicked and return to the dashboard on success."</code></div>
        </div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>The lesson here is a vocabulary shift — from <em>visual</em> prompts ("make the button blue") to <em>transactional</em> prompts ("when a user clicks this, fetch this row owned by this session"). The three pillars of any integration are: schema (source of truth), ownership (who can see what), and external orchestration (what other systems plug in).</p>
      <p>Stress that Lovable's Integration Plan tool generates all three customized to <em>their</em> codebase — they don't have to write these prompts from scratch in Lab 1.</p>
    </div>
  </div>
</section>

<!-- 10. RESISTANCE ENGINEERING FOR ERRORS & FAILURES — 4 product states -->
<section data-title="Resistance Engineering for Errors &amp; Failures">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">Resistance Engineering for Errors &amp; Failures</div>
    <h2>Most prototypes fail because nobody described what should happen when things go wrong.</h2>
    <p class="subtitle">A prototype works with 5 rows. A product survives 5,000 — and survives an offline laptop, a spam-clicker, and a brand-new user with zero data. These four states are the safety nets.</p>
    <div class="blocks-grid">
      <div class="block-card">
        <div class="bc-icon">📭</div>
        <div class="bc-title">Empty States</div>
        <div class="bc-desc"><strong>Day-zero experience.</strong> Replace blank screens with active empty states. If a search or a table is empty, the system must provide a "Get Started" CTA rather than a dead end.</div>
      </div>
      <div class="block-card">
        <div class="bc-icon">⏳</div>
        <div class="bc-title">Loading States</div>
        <div class="bc-desc"><strong>Perceived performance.</strong> Use skeleton screens to show the structure of the data <em>before</em> it arrives — silence in the UI leads to abandonment.</div>
      </div>
      <div class="block-card">
        <div class="bc-icon">⚠️</div>
        <div class="bc-title">Error States</div>
        <div class="bc-desc"><strong>Graceful recovery, not crashes.</strong> Every failed transaction triggers an inline error with a "Retry" button. APIs <em>will</em> time out. The session must survive it.</div>
      </div>
      <div class="block-card">
        <div class="bc-icon">📊</div>
        <div class="bc-title">Load-Bearing States</div>
        <div class="bc-desc"><strong>5 rows → 5,000.</strong> Define system limits. Use pagination for large datasets and "last-write-wins" logic for simultaneous edits to prevent browser freezes or data corruption.</div>
      </div>
    </div>
    <div class="callout-strip">
      <span class="callout-pill">The reframe</span>
      <span>If you can <em>describe</em> these failure modes to the AI, it can <em>build</em> you the safety nets. Lab 1's third prompt does exactly this — system-wide.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Make the point concrete: every learner's prototype right now passes the "happy path" — a logged-in user with data clicking through the main flow. Every prototype <em>fails</em> at least one of these four states. Lab 2's stress test is literally a guided tour of these failures.</p>
      <p>Empty &amp; loading are the cheap wins. Error &amp; load-bearing are where most production bugs hide. The Edge Case prompt in Lab 1 (Prompt 3) addresses all four in one shot — that's why we centralise it.</p>
    </div>
  </div>
</section>

<!-- 11. SECTION 03 — Hands-On Lab: Add Data Schemas and RLS Authentication -->
<section class="section-break" data-title="Section 03 · Lab — Add Data Schemas + RLS">
  <div class="section-break-inner">
    <div class="section-num">03</div>
    <div class="lab-title">Section 03 · Hands-On Lab</div>
    <div class="lab-name">Add Data Schemas + RLS Authentication.</div>
    <div class="lab-desc">Generate your personalised Integration Plan in Lovable, then run three prompts: schema · auth + RLS · edge cases.</div>
  </div>
</section>

<!-- 12. LAB 1 — Schema + RLS + Edge Cases (45 min) -->
<section data-title="Lab · Add Data Schemas + RLS (45 min)">
  <div class="inner" style="max-width: 1240px;">
    <div class="demo-tag tag-exercise">Hands-On Lab · 45 minutes</div>
    <h2>Add data schemas and RLS authentication to your prototype.</h2>
    <p class="subtitle">Audit your M4 prototype for hardcoded UI, generate a personalised Integration Plan, then run three prompts. By the end, your data survives a refresh and your RLS protects user privacy.</p>
    <div class="flow-steps">
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">1</div><div class="fs-icon">🔍</div></div>
        <div class="fs-title">Pre-work audit</div>
        <div class="fs-text">Scan your UI for hardcoded metrics, key user roles &amp; permissions, and screens that would freeze if the data source was slow or unavailable.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">2</div><div class="fs-icon">📋</div></div>
        <div class="fs-title">Generate Integration Plan</div>
        <div class="fs-text">Paste the Integration Plan prompt into Lovable. It scans your project and outputs <code>Integration-Plan.md</code> with three customised prompts.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">3</div><div class="fs-icon">🗄️</div></div>
        <div class="fs-title">Prompt 1 — Schema</div>
        <div class="fs-text">Extend your schema, replace every hardcoded UI value with live queries. Verify: enter data, refresh — does it survive?</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">4</div><div class="fs-icon">🔐</div></div>
        <div class="fs-title">Prompt 2 — Auth + RLS</div>
        <div class="fs-text">Add signup/login, activate Row-Level Security. Verify with two accounts that each user only sees their own data.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">5</div><div class="fs-icon">🛡️</div></div>
        <div class="fs-title">Prompt 3 — Edge cases</div>
        <div class="fs-text">Add loading skeletons, error messages, empty states, retry logic. Verify at least two failure modes (Loading Test + Error Test).</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">6</div><div class="fs-icon">📤</div></div>
        <div class="fs-title">Push to GitHub</div>
        <div class="fs-text">Commit <code>Integration-Plan.md</code> to <code>05-integration/</code> alongside your Living PRD and HANDOFF from M4.</div>
      </div>
    </div>
    <div style="margin-top: 22px; padding: 16px 22px; background: rgba(96,165,250,0.08); border: 1.5px solid rgba(96,165,250,0.35); border-radius: 12px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;">
      <div style="text-align: left;">
        <div style="font-family:'Poppins',sans-serif; font-weight: 700; font-size: 15px; color: #fff; margin-bottom: 4px;">Open the full walkthrough</div>
        <div style="font-size: 13px; color: #b0b4c8;">Every step, every verification check, every "if it broke, do this" recovery prompt — in the M5 Lab Guide.</div>
      </div>
      <a class="tool-btn" href="M5 - Lab Guide.html#phase-1" target="_blank" rel="noopener" style="white-space: nowrap;">→ Open Lab Guide · Phase 1 ↗</a>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>This is the heaviest lab in the cohort — 45 minutes, three sequential prompts, two verification gates. Pre-work audit takes 5 min; Plan generation takes ~3 min; each prompt takes ~10 min including verification. If a learner stalls on Prompt 1, get them on Lovable's <em>Settings → Integrations</em> tab to confirm Supabase is still linked from M4.</p>
      <p>Push the verification language hard: <strong>data survives refresh</strong> (Prompt 1), <strong>two accounts can't see each other's data</strong> (Prompt 2), <strong>offline DevTools toggle shows an error message, not a hung screen</strong> (Prompt 3). These are the only three signals that matter.</p>
    </div>
  </div>
</section>

<!-- 13. BREAK -->
<section class="centered" data-title="Take a Beat">
  <div class="inner">
    <div class="demo-tag tag-break">Break · 5 minutes</div>
    <h2>Take a beat. ☕</h2>
    <p class="subtitle">You earned it. Refill, stretch, breathe.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>5-minute timer in <code>#cohort-channel</code>. Use the buffer to spot-check the room — anyone whose Prompt 3 failed should ping you in Slack so you can debug before Lab 2.</p>
    </div>
  </div>
</section>

<!-- 14. CAMERAS ON -->
<section class="cameras-section" data-title="Cameras On">
  <div class="cameras-inner">
    <div class="cameras-layout">
      <div class="cameras-left">
        <img class="cameras-logo" src="../Design/Product-School-Logo.png" alt="Product School"/>
        <div class="cameras-card">
          <h2>Reminder! 🚨</h2>
          <div class="cameras-arrow">→ Cameras On</div>
          <p>It's always better to see your smiling face! Be present and visible to stay engaged and keep interactions valuable.</p>
        </div>
      </div>
      <div class="cameras-photo-strip">
        <img src="../Design/cameras-on.png" alt="Cameras On"/>
      </div>
    </div>
  </div>
</section>

<!-- 15. SECTION 04 — Hands-On Lab: Rapid-Fire Stress Test -->
<section class="section-break" data-title="Section 04 · Lab — Stress Test &amp; Deploy">
  <div class="section-break-inner">
    <div class="section-num">04</div>
    <div class="lab-title">Section 04 · Hands-On Lab</div>
    <div class="lab-name">Rapid-Fire Stress Test &amp; Deploy.</div>
    <div class="lab-desc">Run the Kill Switch, choose your additional stress test, update HANDOFF.md, then click Publish.</div>
  </div>
</section>

<!-- 16. LAB 2 — Stress Test + Deploy (30 min) -->
<section data-title="Lab · Rapid-Fire Stress Test &amp; Deploy (30 min)">
  <div class="inner" style="max-width: 1240px;">
    <div class="demo-tag tag-exercise">Instructor-Led Lab · 30 minutes</div>
    <h2>Rapid-fire stress test &amp; deploy your product live.</h2>
    <p class="subtitle">Audit your system's resilience under real-world stress. Document gaps. Decide if you ship. Then trigger the deploy.</p>
    <div class="flow-steps">
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">1</div><div class="fs-icon">🔌</div></div>
        <div class="fs-title">The Kill Switch</div>
        <div class="fs-text">DevTools → Network → Offline. Does the UI acknowledge the disconnection or hang? If it hangs, your Prompt 3 from Lab 1 didn't take — re-prompt now.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">2</div><div class="fs-icon">👻</div></div>
        <div class="fs-title">Ghost User <em>or</em> Spam Click</div>
        <div class="fs-text"><strong>Ghost User:</strong> sign up with a new email — empty state with CTA, or blank screen? <strong>Spam Click:</strong> click submit 5× rapidly — does it create 5 duplicates?</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">3</div><div class="fs-icon">📝</div></div>
        <div class="fs-title">Update HANDOFF.md</div>
        <div class="fs-text">P0 blocker → re-prompt and fix. Known gap → document in <code>HANDOFF.md</code> "Known Gaps" section. Both are valid. Ignoring it is the only mistake.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">4</div><div class="fs-icon">🚀</div></div>
        <div class="fs-title">Deploy live</div>
        <div class="fs-text">Click <strong>Publish</strong> in Lovable. Customise icon, title, share image. Copy your live URL. Paste it in <code>#cohort-channel</code>.</div>
      </div>
    </div>
    <div style="margin-top: 22px; padding: 16px 22px; background: rgba(110,231,183,0.08); border: 1.5px solid rgba(110,231,183,0.35); border-radius: 12px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;">
      <div style="text-align: left;">
        <div style="font-family:'Poppins',sans-serif; font-weight: 700; font-size: 15px; color: #fff; margin-bottom: 4px;">Open the stress-test walkthrough</div>
        <div style="font-size: 13px; color: #b0b4c8;">Includes the Safari-user fallback prompt and the "what good vs bad looks like" reference clips.</div>
      </div>
      <a class="tool-btn" href="M5 - Lab Guide.html#phase-2" target="_blank" rel="noopener" style="white-space: nowrap;">→ Open Lab Guide · Phase 2 ↗</a>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Run the first 10 minutes <em>together</em>. Ask one volunteer to screen-share their prototype while you walk the room through the Kill Switch. After that, learners go solo on Ghost User / Spam Click for ~10 min, then HANDOFF + Publish for the final ~10.</p>
      <p>The PM mindset to repeat 3×: <strong>you never ship perfect code, you ship code with known risks.</strong> A documented Known Gap in HANDOFF.md is a professional ship. A silent broken feature is not.</p>
      <p>Safari users — they can't toggle offline in DevTools. Give them the simulate-prompt in the Lab Guide.</p>
    </div>
  </div>
</section>

<!-- 17. YOUR EVOLVED ENG HANDOFF — Previously vs Now -->
<section data-title="Your Evolved Eng Handoff">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">Your Evolved Engineering Handoff</div>
    <h2>From technical inventory to deployed-system blueprint.</h2>
    <p class="subtitle">In M4 your <code>HANDOFF.md</code> documented what <em>could</em> be built. Today it documents how the live engine actually <em>operates</em>.</p>
    <div class="two-col">
      <div class="tc tc-old">
        <div class="tc-label">M4 · Previously</div>
        <div class="tc-title">Static Technical Inventory</div>
        <ul>
          <li><strong>Component List</strong> — a catalogue of components, connected infrastructure, and notes on what's mocked vs real.</li>
          <li><strong>Mocked vs Real</strong> — a note on which parts of the app are functional vs static.</li>
          <li><strong>Start-Here Guide</strong> — instructions for an engineer to begin building.</li>
        </ul>
      </div>
      <div class="tc tc-new">
        <div class="tc-label">M5 · Now</div>
        <div class="tc-title">Deployed System Blueprint</div>
        <ul>
          <li><strong>Data Model &amp; Schema</strong> — the expanded database structure plus RLS rules enforcing per-user data isolation.</li>
          <li><strong>Source of Truth</strong> — a map of how live data flows from the database to the UI.</li>
          <li><strong>Edge Case Log</strong> — what the stress test handled, plus the known technical gaps.</li>
        </ul>
      </div>
    </div>
    <div class="callout-strip">
      <span class="callout-pill">Identity shift</span>
      <span>You moved from "the person building the thing" to <em>"the person owning the system."</em> Your documentation has to keep up.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>This is the slide that connects today's lab back to the M4 narrative. The handoff isn't a one-shot artefact — it evolves with the build. By M6 it'll evolve again to include eval results and iteration evidence.</p>
      <p>Stress the "source of truth" framing: the GitHub repo is where engineers go. The HANDOFF.md in their repo is the most senior artefact they ship in this cohort.</p>
    </div>
  </div>
</section>

<!-- 18. FUTURE-PROOFING WITH APIs -->
<section data-title="Future-Proofing Your Product with APIs">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">Future-Proofing Your Product with APIs</div>
    <h2>How to scale beyond your database.</h2>
    <p class="subtitle">Your product is only as real as its ability to handle live, dynamic data. The next level of growth is plugging into the global API economy.</p>
    <div class="m4-complete-grid">
      <div class="m4c-tile">
        <div class="m4c-num">👤</div>
        <div class="m4c-meta">
          <div class="m4c-label">Personalisation · GET</div>
          <div class="m4c-title">User-ID as a query parameter</div>
          <div class="m4c-desc">Use the User ID in an API GET request to fetch a unique profile rather than a generic one.<br><br><strong>Example — Spotify "Discover Weekly":</strong> your ID tells the API to ignore the global top 40 and fetch <em>your</em> weekly mix.</div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">📡</div>
        <div class="m4c-meta">
          <div class="m4c-label">Real-Time Utility · WebSocket</div>
          <div class="m4c-title">Live feeds, not static rows</div>
          <div class="m4c-desc">Replace static database rows with live API feeds or WebSockets that refresh dynamic external data every few seconds.<br><br><strong>Example — Uber "Driver Tracking":</strong> the app doesn't guess; it constantly calls a GPS API to update the coordinates on your screen.</div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">🔁</div>
        <div class="m4c-meta">
          <div class="m4c-label">Continuity · POST/PUT</div>
          <div class="m4c-title">State sync across devices</div>
          <div class="m4c-desc">Use PUT/POST to sync timestamps or state changes to a cloud API so any device can pick them up.<br><br><strong>Example — Netflix "Continue Watching":</strong> your phone sends a timestamp API update so your TV can fetch where you left off.</div>
        </div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>This is the optional / advanced section — directly tied to Step 7 of Lab 1 (API integration). Most learners won't get there in class, but flag it as the most leverage in the M6 + final-project window.</p>
      <p>The shift is from "my database is my product" to "my product is a switchboard." Personalisation, Real-Time, Continuity — three different verbs. Any one of them in your final demo makes the product feel meaningfully more alive.</p>
    </div>
  </div>
</section>

<!-- 19. MODULE 5 COMPLETE — Dashboard -->
<section data-title="Module 5 · Complete">
  <div class="inner" style="max-width: 1280px;">
    <div class="demo-tag tag-debrief">Module 5 · Complete</div>
    <h2>What you accomplished today.</h2>
    <p class="subtitle">The Production Transition — from connected to deployed. By the numbers.</p>
    <div class="dash-divider"></div>
    <div class="m4-complete-grid">
      <div class="m4c-tile">
        <div class="m4c-num">3</div>
        <div class="m4c-meta">
          <div class="m4c-label">Integration Prompts</div>
          <div class="m4c-title">Schema · Auth · Edge Cases</div>
          <div class="m4c-desc">Three sequential prompts turned a connected backend into a secured, resilient product.</div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">2</div>
        <div class="m4c-meta">
          <div class="m4c-label">Stress Tests Passed</div>
          <div class="m4c-title">Kill-Switch · Ghost/Spam</div>
          <div class="m4c-desc">You identified P0 blockers and documented critical logic gaps to ensure a resilient launch.</div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">1</div>
        <div class="m4c-meta">
          <div class="m4c-label">Live Public URL</div>
          <div class="m4c-title">Production Deploy</div>
          <div class="m4c-desc">You triggered a public product deployment with persistent database connectivity and secure user authentication.</div>
        </div>
      </div>
    </div>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 18px;">
      <div class="shift-card">
        <div class="sc-num">THE SHIFTS · 01</div>
        <div class="sc-title">Static Backend → Live Data System</div>
        <div class="sc-text">You moved from a connected infrastructure to a fully functional data-driven system. Every metric is now computed from <em>live</em> records; every interaction is secured by RLS.</div>
      </div>
      <div class="shift-card">
        <div class="sc-num">THE SHIFTS · 02</div>
        <div class="sc-title">Sandbox Prototype → Deployed Product</div>
        <div class="sc-text">You moved past simple deployment into a production-ready ecosystem that handles real-world conditions. Loading + error states keep the product resilient when reality breaks.</div>
      </div>
    </div>
    <div class="next-module-bar">
      <div class="nmb-icon">📊</div>
      <div class="nmb-text"><strong>Next: Module 6</strong> — from finished product to <em>continuous cycle of improvement</em>. Real user interactions, AI-driven analytics, redeploy.</div>
      <div class="nmb-arrow">→</div>
    </div>
    <div style="margin-top: 18px; padding: 12px 18px; background: rgba(248,113,113,0.08); border-left: 4px solid #f87171; border-radius: 8px; font-size: 13.5px; color: #e0e0f0; line-height: 1.55; text-align: left;">
      📍 <strong>Project deliverable check:</strong> update the "Integrations &amp; Data Model" and "Edge Cases &amp; Known Gaps" sections on Slide 9 of your final project deck. Confirm your <strong>Live URL</strong> is saved and your <strong>HANDOFF.md</strong> is exported to <code>05-integration/</code> on GitHub.
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Land the plane: this is the identity shift from <em>someone with an idea</em> to <em>a Technical PM who has successfully launched a live production system</em>. Push hard on the "you have a URL" line — it's the most concrete artefact any learner has shipped in their entire PM career so far.</p>
      <p>Use this slide to set up M6: the product is live; now we measure it. Tease the evals + analytics + redeploy loop.</p>
    </div>
  </div>
</section>

<!-- 20. KEY TAKEAWAYS -->
<section data-title="Key Takeaways">
  <div class="inner" style="max-width: 1180px;">
    <div class="section-label">Key Takeaways</div>
    <h2>Ship live products with full-stack logic.</h2>
    <div class="m4-complete-grid" style="grid-template-columns: repeat(2, 1fr);">
      <div class="m4c-tile">
        <div class="m4c-num">01</div>
        <div class="m4c-meta">
          <div class="m4c-label">Integration is a Data Contract</div>
          <div class="m4c-title">Define the schema, define the rules</div>
          <div class="m4c-desc">PMs orchestrate integrations by defining the schema and ownership logic. Internal databases and external APIs must communicate through a <em>predictable data contract</em>.</div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">02</div>
        <div class="m4c-meta">
          <div class="m4c-label">Resilience is Prompted</div>
          <div class="m4c-title">Empty · Loading · Error · Load-Bearing</div>
          <div class="m4c-desc">PMs enforce technical resilience by accounting for failure states. Standardising prompts for these scenarios keeps the product functional under real-world stress.</div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">03</div>
        <div class="m4c-meta">
          <div class="m4c-label">Handoff is a Living Document</div>
          <div class="m4c-title">Spec → Blueprint</div>
          <div class="m4c-desc">The Engineering Handoff evolves as real-world cases are stress-tested. Hand over a <em>resilient architecture</em>, not a static inventory.</div>
        </div>
      </div>
      <div class="m4c-tile">
        <div class="m4c-num">04</div>
        <div class="m4c-meta">
          <div class="m4c-label">Scale Beyond the Database</div>
          <div class="m4c-title">Personalisation · Real-Time · Continuity</div>
          <div class="m4c-desc">Future-proof products by identifying API connections that scale utility beyond the internal database. Dynamic feeds = real-time updates + cross-platform continuity.</div>
        </div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Recap pace — 60 seconds per takeaway. The throughline: <em>resilience</em>. M5 is where prototypes either grow up or quietly fail in the wild. Every one of these four takeaways is a guard rail against quiet failure.</p>
    </div>
  </div>
</section>

<!-- 21. EXTRA PRACTICE + NEXT SESSION -->
<section data-title="Extra Practice + Next Session">
  <div class="inner" style="max-width: 1180px;">
    <div class="section-label">Extra Practice · Optional</div>
    <h2>Dig deeper.</h2>
    <p class="subtitle">Optional exercises for learners who want to push beyond today's lab. Both build on your live URL.</p>
    <div class="ep-grid">
      <div class="ep-card">
        <div class="ep-num">01</div>
        <div class="ep-title">The API Value Expansion</div>
        <div class="ep-desc">Select a static data point in your product, identify a public API that could provide it live, prompt to integrate the feed. Did the shift to a live feed fundamentally evolve product utility — or is it cosmetic?</div>
      </div>
      <div class="ep-card">
        <div class="ep-num">02</div>
        <div class="ep-title">The Multi-Device Continuity Test</div>
        <div class="ep-desc">Open your live URL on laptop + phone. Act on one, refresh the other. Does the change reflect instantly via your database? Or does the product feel like disconnected local sessions?</div>
      </div>
    </div>
    <div class="next-arrow-bar">
      <div class="nab-meta">Next Session</div>
      <div class="nab-title">M6 · Measure Product Performance for AI-Driven Iteration</div>
      <div class="nab-desc">Transition from gut-based guesses to evidence-based improvements. Analyse live user interactions against your hypothesis. Leverage AI-driven analytics to identify high-impact friction points and redeploy targeted updates that secure the confidence line.</div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Frame the optional exercises as the gap between "you shipped" and "you shipped something interesting." Most learners stop at the live URL; the ones who do API Value Expansion come back to M6 with a product that's genuinely worth measuring.</p>
      <p>Tease M6 as the closer: "today you have a URL — next class we make that URL <em>learn</em>."</p>
    </div>
  </div>
</section>

<!-- 22. DAY 5 SURVEY -->
<section class="centered" data-title="Day 5 Survey">
  <div class="inner">
    <div class="demo-tag tag-debrief">Feedback</div>
    <h2>Your opinion matters.</h2>
    <p class="subtitle">Two minutes. Helps us make the next cohort better than this one.</p>
    <div class="artifact-preview" style="max-width: 560px;">
      <div class="ap-title">End-of-Session Survey · Day 5</div>
      <p style="font-size:14px; color:#cdd5e3; line-height:1.6;">Scan the QR or use the link in <code>#cohort-channel</code>. Your insights help us iterate the cohort.</p>
    </div>
    <p style="font-size:14px; color:#8899bb; margin-top:18px; text-align:center;">See you in Module 6 — <em>Measure Product Performance for AI-Driven Iteration</em>.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Drop the link in <code>#cohort-channel</code> as you say this. Two minutes max. Mention that Day 5's feedback most heavily shapes the Day 6 evals walkthrough.</p>
    </div>
  </div>
</section>

<!-- 23. RESOURCES & TEMPLATES -->
<section data-title="Resources &amp; Templates">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">Resources &amp; Templates</div>
    <h2>Everything Module 5 ships with.</h2>
    <p class="subtitle">Bookmark them — they're referenced across M6. <strong>Your GitHub repo is the source of truth</strong>; the tools below are aids that live in browser memory.</p>

    <div class="resources-hero">
      <div class="rh-logo"><img src="../Design/logos/github.svg" alt="GitHub"/></div>
      <div class="rh-content">
        <div class="rh-eyebrow">Primary artifact · GitHub-first</div>
        <div class="rh-title">Your GitHub repo (source of truth)</div>
        <div class="rh-desc"><strong>This is where your work lives across modules.</strong> Today's deliverables: <code>05-integration/Integration-Plan.md</code>, updated <code>HANDOFF.md</code>, and your <strong>Live URL</strong> in <code>README.md</code>. M6 pulls from here, not from any tool's cache.</div>
      </div>
    </div>

    <div class="resources-tiles">
      <div class="card-item" style="--card-accent:#60a5fa;">
        <div class="card-icon">🧪</div>
        <div class="card-title">Module 5 Lab Guide</div>
        <div class="card-desc"><a href="M5 - Lab Guide.html" target="_blank" rel="noopener" style="color:#60a5fa;">Open the lab guide ↗</a> — full walkthrough: pre-work audit → Integration Plan → 3 prompts → stress test → deploy.</div>
      </div>
      <div class="card-item" style="--card-accent:#a78bfa;">
        <div class="card-icon">📋</div>
        <div class="card-title">Integration Plan Template</div>
        <div class="card-desc"><a href="../Templates/Integration-Plan-Template.md" target="_blank" rel="noopener" style="color:#a78bfa;">Open the template ↗</a> — the 8-section structure Lovable generates: status check, data audit, schema, RLS, prompts, edge cases, stress tests, handoff.</div>
      </div>
      <div class="card-item" style="--card-accent:#fb7185;">
        <div class="card-icon">📚</div>
        <div class="card-title">M5 Frameworks Reference Card</div>
        <div class="card-desc"><a href="Module 5 - Frameworks Reference Card.html" target="_blank" rel="noopener" style="color:#fb7185;">Open the card ↗</a> — Three Integration Pillars · Four Product States · Stress-Test Trio · API Scaling Triangle.</div>
      </div>
      <div class="card-item" style="--card-accent:#f9a8d4;">
        <div class="card-icon">📋</div>
        <div class="card-title">Final Project Brief</div>
        <div class="card-desc"><a href="../Final Project - Requirements and Scenario Guide.html" target="_blank" rel="noopener" style="color:#f9a8d4;">Open the brief ↗</a> — scenarios, deliverables, rubric, timeline.</div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Drop this card list in <code>#cohort-channel</code> right after class — pin it. The Lab Guide is the walkthrough; the Integration Plan Template is the reference for "what good looks like"; the Frameworks Reference Card is the cheat sheet for today's four mental models.</p>
      <p><strong>GitHub-first rule:</strong> reinforce one last time — the canonical artefacts live in their GitHub repo at <code>05-integration/Integration-Plan.md</code> and the updated <code>HANDOFF.md</code>. M6 pulls from <code>05-integration/</code> on GitHub. No tools, no browser cache, no exceptions.</p>
    </div>
  </div>
</section>

<!-- 24. Q&A -->
<section class="centered" data-title="Q&amp;A">
  <div class="inner">
    <div class="demo-tag tag-debrief">Instructor-Led Q&amp;A</div>
    <h2>Questions?</h2>
    <p class="subtitle">Live: unmute or drop in chat. Async: post in <code>#cohort-channel</code> — instructor responds within ~24h.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Open the floor for 3–4 minutes. If nobody has a live question, pick the highest-energy post from <code>#cohort-channel</code> and read it back: <em>"someone wrote — [paste line] — what's the engineering move on that?"</em></p>
    </div>
  </div>
</section>

<!-- 25. END -->
<section class="centered" data-title="See You in Module 6">
  <div class="inner">
    <div class="demo-tag tag-debrief">End of Module 5</div>
    <h2>You shipped.</h2>
    <p class="subtitle">A live URL. A secured database. A documented handoff. You are no longer prototyping — you are operating a product.</p>
    <div class="artifact-preview" style="max-width: 620px;">
      <div class="ap-title">Today's repo state</div>
      <p style="font-size:14px; color:#cdd5e3; line-height:1.7;"><code>05-integration/Integration-Plan.md</code> · updated <code>HANDOFF.md</code> · live URL in <code>README.md</code>. Push before you close the laptop.</p>
    </div>
    <p style="font-size:14px; color:#8899bb; margin-top:20px; text-align:center;">Next session: <strong style="color:#fff;">Module 6 — Measure Product Performance for AI-Driven Iteration</strong> — turn shipping into a learning loop.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>The session's identity-shift moment lands here. Don't oversell — just acknowledge it: today they moved from "PM with a prototype" to "PM with a live URL." Drop the M6 hook in <code>#cohort-channel</code>: pre-read goes out tonight.</p>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# Assemble
# ---------------------------------------------------------------------------

src = M4.read_text()

# split header / footer
m_start = re.search(r'<!--\s*1\.\s*HERO\s*-->', src)
m_end = re.search(r'\n<script>\s*\n\s*const sections', src)

header = src[:m_start.start()]
footer = src[m_end.start():]

# Update the page title in <head>
header = header.replace(
    '<title>Module 4 — Transition From Prototypes to Production Specs · Instructor</title>',
    '<title>Module 5 — Ship Live Products with Full-Stack Logic · Instructor</title>',
)

# Substitute demo id placeholders
body = BODY.replace('__DEMO_ID__', DEMO_ID)

out = header + body.lstrip('\n') + '\n\n' + footer

M5.write_text(out)
print(f'wrote {M5} ({len(out)} bytes)')
