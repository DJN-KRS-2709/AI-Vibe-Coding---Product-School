"""Build Module 6 instructor + shareable decks by reusing M5's design-system shell.

Reads `Modules/Module 5 - Slides.html`, swaps the title + slide body for the
M6 content while keeping the <head> CSS and <script> controller verbatim.

Outputs:
  - Modules/Module 6 - Slides.html              (instructor, with .notes blocks)
  - Modules/Module 6 - Slides (Shareable).html  (notes stripped)

Mirrors the canonical class catalog used across M1-M5.
"""
from pathlib import Path
import re

REPO = Path(__file__).resolve().parent.parent
M5 = REPO / 'Modules' / 'Module 5 - Slides.html'
M6 = REPO / 'Modules' / 'Module 6 - Slides.html'
M6_SHARE = REPO / 'Modules' / 'Module 6 - Slides (Shareable).html'

DEMO_ID = '1fMWLvDYJr2kxyKBcFwZt-WGoK4CYNZR1'

# ---------------------------------------------------------------------------
# M6 slide body — every section in source order. Uses canonical classes only.
# ---------------------------------------------------------------------------

BODY = r"""
<!-- 1. HERO -->
<section class="hero" data-title="Measure Product Performance for AI-Driven Iteration">
  <div class="hero-logo"><img src="../Design/Product-School-Logo.png" alt="Product School"/></div>
  <div class="section-label">Module 6 — Vibe Coding Certification</div>
  <h1>Measure Product Performance<br><span>for AI-Driven Iteration</span></h1>
  <p class="subtitle">Replace "I think" with "the data shows." Read the three layers of analytics on your live product, run an AI-powered iteration sprint on one high-impact finding, redeploy, and demo what you shipped — closing the Confidence Line.</p>
  <div class="waypoints">
    <div class="waypoint"><div class="waypoint-num">1</div><div class="waypoint-text"><div class="wt-title">Shift From Shipping to Proving With Data</div><div class="wt-desc">Why a live URL is the start of the feedback loop, not the finish line. The Iteration Mindset, the metrics that matter, and the three layers of analytics.</div></div></div>
    <div class="waypoint"><div class="waypoint-num">2</div><div class="waypoint-text"><div class="wt-title">Lab — Read Your Lovable Insights</div><div class="wt-desc">Open Lovable Insights, baseline your engagement metrics, identify your lowest-engagement screen, and gather peer feedback in Slack.</div></div></div>
    <div class="waypoint"><div class="waypoint-num">3</div><div class="waypoint-text"><div class="wt-title">Lab — Run an AI-Driven Iteration Sprint</div><div class="wt-desc">Feed problem + hypothesis + metrics + peer feedback into an LLM. Get a prioritised backlog. Implement one fix. Redeploy.</div></div></div>
    <div class="waypoint"><div class="waypoint-num">4</div><div class="waypoint-text"><div class="wt-title">Final Project Showcase</div><div class="wt-desc">Demo your live product to the cohort. Get live, actionable feedback. Submit your final deliverables to the LMS to qualify for certification.</div></div></div>
  </div>
  <p class="repo-cta">Today's repo lands in <strong><code>06-iteration/</code></strong> — <code>Iteration-Sprint-Brief.md</code> with the AI analysis + the one change you shipped, plus your redeployed live URL.</p>
  <div class="scroll-hint">Scroll to explore<span>↓</span></div>
  <div class="notes">
    <h4>Speaker Notes</h4>
    <p>Welcome to Module 6 — the final session. Five modules built up to a live URL; today we make that URL <em>learn</em>. By the end of class every learner has read their own analytics, run an AI-powered iteration on real signal, redeployed, and demoed their product to the cohort.</p>
    <p>Frame the arc: M5 was "ship the thing." M6 is "prove the thing." This is the move from PM-as-builder to PM-as-operator. Push hard on the identity shift — they finish today as Technical PMs who can close a build-measure-iterate loop end-to-end.</p>
  </div>
</section>

<!-- 2. CLASS EXPECTATIONS -->
<section class="centered" data-title="Class Expectations">
  <div class="inner">
    <div class="section-label">Cohort Norms</div>
    <h2>Class expectations.</h2>
    <p class="subtitle">Same six norms across the certification. Show up, ship something, share generously — for the last time.</p>
    <div class="expect-grid">
      <div class="expect-card"><div class="expect-icon">📹</div><div class="expect-title">Cameras On</div><div class="expect-desc">Be present and visible — especially today, the showcase runs on energy.</div></div>
      <div class="expect-card"><div class="expect-icon">⏰</div><div class="expect-title">Arrive On Time</div><div class="expect-desc">Respect everyone's time by arriving promptly to sessions.</div></div>
      <div class="expect-card"><div class="expect-icon">🤝</div><div class="expect-title">Engage to Network</div><div class="expect-desc">Participate in the peer feedback loop and the showcase to close the cohort connection.</div></div>
      <div class="expect-card"><div class="expect-icon">🛠️</div><div class="expect-title">Tool Readiness</div><div class="expect-desc">Lovable, GitHub, your LLM of choice, and your live URL — all active before class starts.</div></div>
      <div class="expect-card"><div class="expect-icon">💬</div><div class="expect-title">Use Slack</div><div class="expect-desc">Use Slack for the Rapid-Fire Feedback Loop and for everything else.</div></div>
      <div class="expect-card"><div class="expect-icon">🚀</div><div class="expect-title">Class Momentum</div><div class="expect-desc">Individual or deep-dive questions move to after-class support so the showcase stays on time.</div></div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Run this quickly — the cohort has seen it five times. The momentum norm matters most today because the showcase is on a hard clock: ~10 minutes per presenter, 5–6 presenters.</p>
    </div>
  </div>
</section>

<!-- 3. COURSE ARC — M6 active -->
<section class="centered" data-title="The Course Arc">
  <div class="inner" style="max-width: 1180px;">
    <div class="section-label">Vibe Coding Certification — Syllabus</div>
    <h2>Where M6 closes the arc.</h2>
    <p class="subtitle">You shipped in M5. Today you turn shipping into a measurement loop and demo the result. This is the final lap.</p>
    <div class="arc-flow">
      <div class="arc-node"><div class="ad-num">M1</div>Velocity</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M2</div>Validation</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M3</div>Prompt Chaining</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M4</div>Production Specs</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node"><div class="ad-num">M5</div>Full-Stack Logic</div>
      <div class="arc-arrow">→</div>
      <div class="arc-node active-node"><div class="ad-num">M6</div>Measure &amp; Iterate</div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Anchor the arc one last time. M1–M5 was the build; M6 is the proof. The Confidence Line goes from "I have an idea" all the way to "the data confirms the idea" — that's the journey we close today.</p>
    </div>
  </div>
</section>

<!-- 4. LMS SUBMISSION REMINDER — final project required for cert -->
<section class="centered" data-title="Final Project Submission Reminder">
  <div class="inner" style="max-width: 880px;">
    <div class="demo-tag tag-activity">Required · Certification</div>
    <h2>To certify, you must submit.</h2>
    <p class="subtitle">Today's showcase is the highest-bandwidth feedback moment in the cohort. The LMS submission is what unlocks your certificate. Both matter — for different reasons.</p>
    <div class="artifact-preview" style="max-width: 640px;">
      <div class="ap-title">Required · Final Project Deliverables Deck</div>
      <p style="font-size:14px; color:#cdd5e3; line-height:1.7;">Submit a finalised copy of your <strong>Final Project Deliverables Deck</strong> in Docebo within <strong>7 days</strong> of this class. Live URL, hypothesis, validation brief, Living PRD, prompt chain, engineering handoff, and your individual aha-moment — all in one deck.</p>
    </div>
    <p style="font-size:14px; color:#8899bb; margin-top:18px;">5–6 volunteers will demo live today. Sign up in <code>#cohort-channel</code>. Everyone else — submit by the 7-day deadline.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>This is the only "this is required for certification" moment in the deck — make it stick. Drop the Docebo link in <code>#cohort-channel</code> right after this slide and pin the message. Mention the 7-day window explicitly. Then ask for the 5–6 showcase volunteers right now while attention is high.</p>
    </div>
  </div>
</section>

<!-- 5. TODAY'S AGENDA -->
<section class="centered" data-title="Today's Agenda">
  <div class="inner" style="max-width: 1080px;">
    <div class="section-label">Today's Agenda</div>
    <h2>Five moves, one closing demo.</h2>
    <p class="subtitle">Two short labs, a 15-minute deck polish, then the final showcase.</p>
    <div class="waypoints" style="margin: 24px auto;">
      <div class="waypoint"><div class="waypoint-num">01</div><div class="waypoint-text"><div class="wt-title">Shift From Shipping to Proving With Data</div><div class="wt-desc">Instructor demo + Rapid-Fire Feedback Loop on classmates' products + the Iteration Mindset, metrics, and three layers of analytics.</div></div></div>
      <div class="waypoint"><div class="waypoint-num">02</div><div class="waypoint-text"><div class="wt-title">Hands-On Lab — Read Your Lovable Insights</div><div class="wt-desc">Open Insights, baseline your numbers, identify your lowest-engagement screen, audit honestly against your M2 hypothesis.</div></div></div>
      <div class="waypoint"><div class="waypoint-num">03</div><div class="waypoint-text"><div class="wt-title">AI-Driven Product Iteration</div><div class="wt-desc">The PM's new superpower: feed inputs to an LLM, get a prioritised backlog, translate data signals into surgical prompts.</div></div></div>
      <div class="waypoint"><div class="waypoint-num">04</div><div class="waypoint-text"><div class="wt-title">Hands-On Lab — Run an AI-Driven Iteration Sprint</div><div class="wt-desc">One finding, one prompt, one redeploy. Push the brief to GitHub.</div></div></div>
      <div class="waypoint"><div class="waypoint-num">05</div><div class="waypoint-text"><div class="wt-title">Final Project Showcase</div><div class="wt-desc">5–6 cohort volunteers present live. Everyone submits to Docebo within 7 days.</div></div></div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Three timed activities today: the Rapid-Fire Feedback Loop (10 min on peers' products), Lab 1 (10 min on your own Insights), Lab 2 (15 min AI sprint). Plus a 15-min deliverables-deck polish. The biggest time investment is the final showcase. Watch the clock — if anything slips, protect the showcase, not the polish block.</p>
    </div>
  </div>
</section>

<!-- 6. SECTION 01 — Shift From Shipping to Proving With Data -->
<section class="section-break" data-title="Section 01 · Shift From Shipping to Proving With Data">
  <div class="section-break-inner">
    <div class="section-num">01</div>
    <div class="lab-title">Section 01</div>
    <div class="lab-name">Shift From Shipping to Proving With Data.</div>
    <div class="lab-desc">Your product is live. Your gut is not data. We'll watch what's already there and what to do with it.</div>
  </div>
</section>

<!-- 7. INSTRUCTOR-LED DEMO — Making Data-Driven Decisions -->
<section data-title="Instructor Demo · Making Data-Driven Decisions">
  <div class="inner" style="max-width: 1180px;">
    <div class="demo-tag tag-case">Instructor-Led Demo · 3 minutes</div>
    <h2>From "I think it's working" to "the data says so."</h2>
    <p class="subtitle">Your product has been live for a few days. Real users have clicked around. But how do you actually know if it's solving the problem from M2? Let's open Lovable Insights together — no setup, no extra tool, it's been collecting since M5.</p>
    <div class="demo-split">
      <div class="problem-panel">
        <span class="pp-label">⚠ The Gap</span>
        <div class="pp-headline">A hunch isn't data — it's confirmation bias.</div>
        <div class="pp-execs">
          <div class="pp-exec"><div class="pp-avatar">👁️</div><div class="pp-quote">"I tested it myself and it felt great." — every PM ever, right before launch.</div></div>
          <div class="pp-exec"><div class="pp-avatar">📊</div><div class="pp-quote">"Real sessions, real users, real screens visited. Insights has been on since the moment we deployed."</div></div>
          <div class="pp-exec"><div class="pp-avatar">🎯</div><div class="pp-quote">"In a moment, you'll do the same thing on <em>your</em> product — and on four of your classmates'."</div></div>
        </div>
        <div class="pp-coda">Shipping is 50% of the job. The other 50% is reading what just happened.</div>
      </div>
      <div class="demo-video-col">
        <div class="demo-video-frame">
          <iframe src="https://drive.google.com/file/d/__DEMO_ID__/preview" allow="autoplay" allowfullscreen></iframe>
        </div>
        <div class="demo-video-cta">
          <a class="tool-btn" href="https://drive.google.com/file/d/__DEMO_ID__/view" target="_blank" rel="noopener">▶ Watch the full demo ↗</a>
          <div class="demo-helper">Lovable Insights tour — Visitors · Page Views · Views Per Visit · Duration · Bounce Rate. Right after this, every learner gives that same critical eye to four classmates' products.</div>
        </div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Cue the demo (~3 min). Ask for one volunteer to share their Lovable project — open the Insights panel together. Call out each metric: <strong>Visitors</strong> (unique), <strong>Page Views</strong> (total), <strong>Views Per Visit</strong> (depth), <strong>Duration</strong> (engagement), <strong>Bounce Rate</strong> (entry-screen quality).</p>
      <p>End with: "in 10 minutes, you'll bring that same critical eye to four of your classmates' products." That's the bridge into the Rapid-Fire Feedback Loop.</p>
    </div>
  </div>
</section>

<!-- 8. RAPID-FIRE FEEDBACK LOOP — individual exercise · 10 min -->
<section data-title="Rapid-Fire Feedback Loop">
  <div class="inner" style="max-width: 1240px;">
    <div class="demo-tag tag-exercise">Individual Exercise · 10 minutes</div>
    <h2>Rapid-Fire Feedback Loop.</h2>
    <p class="subtitle">Head to <code>#cohort-channel</code>. Test four classmates' deployed products. Leave one structured comment per product. This is the peer signal that fuels Lab 2's AI analysis later — and it builds the critical eye you'll use on your own product in Lab 1.</p>
    <div class="flow-steps" style="grid-template-columns: repeat(3, 1fr); max-width: 1140px;">
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">1</div><div class="fs-icon">🔗</div></div>
        <div class="fs-title">Pick four classmates' URLs</div>
        <div class="fs-text">From the cohort Slack channel, choose at least <strong>four different deployed Lovable links</strong> classmates have shared.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">2</div><div class="fs-icon">🧪</div></div>
        <div class="fs-title">Test each for ~2 minutes</div>
        <div class="fs-text"><strong>Sign up with your email</strong>, run the core flow, or try to break the product by testing edge cases.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">3</div><div class="fs-icon">💬</div></div>
        <div class="fs-title">Leave specific feedback in-thread</div>
        <div class="fs-text">Reply in the <em>same Slack thread</em> as the URL was posted. <strong>Tag the builder.</strong> Pick one of the four labels below — be specific.</div>
      </div>
    </div>
    <div class="blocks-grid" style="margin-top: 18px;">
      <div class="block-card">
        <div class="bc-icon">🐛</div>
        <div class="bc-title">A Bug</div>
        <div class="bc-desc"><em>"I clicked X and nothing happened — the form just stayed open."</em></div>
      </div>
      <div class="block-card">
        <div class="bc-icon">🤔</div>
        <div class="bc-title">Friction</div>
        <div class="bc-desc"><em>"I was confused by the label on the submit button — I wasn't sure what would happen."</em></div>
      </div>
      <div class="block-card">
        <div class="bc-icon">🤩</div>
        <div class="bc-title">A Compliment</div>
        <div class="bc-desc"><em>"I was so impressed with the empty-state CTA — I knew exactly what to click first."</em></div>
      </div>
      <div class="block-card">
        <div class="bc-icon">💡</div>
        <div class="bc-title">A Feature Idea</div>
        <div class="bc-desc"><em>"It would be cool if this could also import contacts from CSV in bulk."</em></div>
      </div>
    </div>
    <div class="callout-strip">
      <span class="callout-pill">The rule</span>
      <span>One labelled comment per peer product. Specific. Tagged. In-thread. <em>"Nice app!"</em> is noise, not signal.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Activity: Individual Exercise · 10 minutes. Push hard on two things at the top of the activity:</p>
      <p><strong>(1) Everyone needs a URL posted.</strong> If a learner never shared their deployed link in <code>#cohort-channel</code> from M5, they need to post it <em>now</em> — otherwise classmates can't leave feedback for them and they'll arrive at Lab 2 with no peer signal.</p>
      <p><strong>(2) Feedback must be specific.</strong> <em>"Nice app!"</em> doesn't help anyone. The four labels (🐛 / 🤔 / 🤩 / 💡) each force a concrete observation in one sentence. Demo the difference live: vague vs specific.</p>
      <p>The exercise serves two purposes — it gives the cohort the qualitative signal they'll need for the AI analysis in Lab 2, and it develops their critical eye <em>before</em> they read their own Insights data in Lab 1. That's why the order matters: peer review first, self review second.</p>
    </div>
  </div>
</section>

<!-- 9. THE ITERATION MINDSET — 3 levers · loop diagram -->
<section data-title="The Iteration Mindset">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">The Iteration Mindset</div>
    <h2>Shipping a prototype isn't the finish line — it's the start of the feedback loop.</h2>
    <p class="subtitle">Your goal: replace <em>"I think"</em> with <em>"the data shows."</em> From this point forward, your intuition is just a hypothesis the data either proves or kills.</p>

    <!-- Loop diagram: 3 nodes + forward arrows + dashed return curve -->
    <svg viewBox="0 0 1200 230" preserveAspectRatio="xMidYMid meet" role="img" aria-label="The Iteration Mindset loop: Prioritise → Identify → Validate → back to Prioritise" style="width:100%; max-width:1100px; margin:8px auto 22px; display:block;">
      <defs>
        <marker id="m6-arrow-fwd" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#60a5fa"/>
        </marker>
        <marker id="m6-arrow-back" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
          <path d="M 0,0 L 10,5 L 0,10 z" fill="#a78bfa"/>
        </marker>
        <radialGradient id="m6-node-grad" cx="50%" cy="40%" r="60%">
          <stop offset="0%" stop-color="#3b82f6"/>
          <stop offset="100%" stop-color="#0c2f7a"/>
        </radialGradient>
      </defs>

      <!-- Forward arrows: 1 → 2 and 2 → 3 -->
      <line x1="248" y1="78" x2="552" y2="78" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#m6-arrow-fwd)"/>
      <line x1="648" y1="78" x2="952" y2="78" stroke="#60a5fa" stroke-width="2.5" marker-end="url(#m6-arrow-fwd)"/>

      <!-- Dashed return curve from node 3 (right) down and around back to node 1 (left) -->
      <path d="M 1000,118 C 1000,210 200,210 200,118" fill="none" stroke="#a78bfa" stroke-width="2.5" stroke-dasharray="7 7" marker-end="url(#m6-arrow-back)"/>
      <text x="600" y="200" text-anchor="middle" fill="#a78bfa" font-family="Poppins, sans-serif" font-weight="700" font-size="12" letter-spacing="3">REPEAT THE LOOP</text>

      <!-- Node 1 -->
      <circle cx="200" cy="78" r="44" fill="url(#m6-node-grad)" stroke="#60a5fa" stroke-width="2.5"/>
      <text x="200" y="88" text-anchor="middle" fill="#ffffff" font-family="Poppins, sans-serif" font-weight="900" font-size="26">1</text>
      <text x="200" y="148" text-anchor="middle" fill="#cbd5e1" font-family="Poppins, sans-serif" font-weight="700" font-size="13" letter-spacing="2.5">PRIORITISE</text>

      <!-- Node 2 -->
      <circle cx="600" cy="78" r="44" fill="url(#m6-node-grad)" stroke="#60a5fa" stroke-width="2.5"/>
      <text x="600" y="88" text-anchor="middle" fill="#ffffff" font-family="Poppins, sans-serif" font-weight="900" font-size="26">2</text>
      <text x="600" y="148" text-anchor="middle" fill="#cbd5e1" font-family="Poppins, sans-serif" font-weight="700" font-size="13" letter-spacing="2.5">IDENTIFY</text>

      <!-- Node 3 -->
      <circle cx="1000" cy="78" r="44" fill="url(#m6-node-grad)" stroke="#60a5fa" stroke-width="2.5"/>
      <text x="1000" y="88" text-anchor="middle" fill="#ffffff" font-family="Poppins, sans-serif" font-weight="900" font-size="26">3</text>
      <text x="1000" y="148" text-anchor="middle" fill="#cbd5e1" font-family="Poppins, sans-serif" font-weight="700" font-size="13" letter-spacing="2.5">VALIDATE</text>
    </svg>

    <div class="m4-complete-grid">
      <div class="m4c-tile">
        <div class="m4c-num">1</div>
        <div class="m4c-meta">
          <div class="m4c-label">Feature Prioritisation</div>
          <div class="m4c-title">Find the 20% that drives 80% of value</div>
          <div class="m4c-desc">Every V1 has ghost features — things you thought were critical that no one touches. Data identifies the 20% of your product driving 80% of the value so you stop wasting engineering cycles on the other 80%.</div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">2</div>
        <div class="m4c-meta">
          <div class="m4c-label">Friction Identification</div>
          <div class="m4c-title">See the leaks you can't see</div>
          <div class="m4c-desc">You know how the app works because you built it. Real users don't. Data exposes the leaks and dead ends in your UI that your own bias makes you blind to.</div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">3</div>
        <div class="m4c-meta">
          <div class="m4c-label">Hypothesis Validation</div>
          <div class="m4c-title">Audit the workflow you designed</div>
          <div class="m4c-desc">Compare the workflow you designed against how humans actually navigate it. Data is the only objective way to see if your solution is operating the way you engineered it to.</div>
        </div>
      </div>
    </div>
    <div class="callout-strip">
      <span class="callout-pill">The reframe</span>
      <span>Every decision from here is <em>backed by evidence</em>, not instinct. Your intuition gets you to a hypothesis; the data either funds it or kills it.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Make the three levers concrete with a single example: a learner's invite-tracker product. Feature Prioritisation says <em>"the only screen anyone visits is the dashboard — your settings page is dead weight."</em> Friction Identification says <em>"50% of new users bounce on the sign-up screen — your CTA is broken."</em> Hypothesis Validation says <em>"users send invites but never check the status tab — your value prop isn't the tracker, it's the send flow."</em></p>
      <p>The throughline for every M6 lecture slide is the same: prompts now start with <strong>"based on the data..."</strong>, not <em>"I think it should..."</em>.</p>
    </div>
  </div>
</section>

<!-- 10. METRICS THAT MATTER — 4 buckets + North Star -->
<section data-title="Metrics That Matter">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">Metrics That Matter</div>
    <h2>3–5 signals beat 50 — every time.</h2>
    <p class="subtitle">Analysis paralysis is the biggest killer of V2. Narrow the lens to a handful of signals that map directly to your problem statement.</p>
    <div class="blocks-grid">
      <div class="block-card">
        <div class="bc-icon">🚦</div>
        <div class="bc-title">Engagement</div>
        <div class="bc-desc"><strong>The core flow.</strong> How many users signed up? Which features are used most — and which are ignored ghosts?</div>
      </div>
      <div class="block-card">
        <div class="bc-icon">🔁</div>
        <div class="bc-title">Retention</div>
        <div class="bc-desc"><strong>Your honesty metric.</strong> Do users return after their first session? Where exactly do they drop off in the flow?</div>
      </div>
      <div class="block-card">
        <div class="bc-icon">⚙️</div>
        <div class="bc-title">Quality</div>
        <div class="bc-desc"><strong>The "is it broken" check.</strong> Is the page load under 3 seconds? Are users hitting dead ends or high error rates?</div>
      </div>
      <div class="block-card">
        <div class="bc-icon">🎯</div>
        <div class="bc-title">Impact</div>
        <div class="bc-desc"><strong>The hypothesis check.</strong> Does user behaviour match your M2 hypothesis? Is what you predicted actually happening?</div>
      </div>
    </div>
    <div class="callout-strip">
      <span class="callout-pill">North Star</span>
      <span>Does user behaviour <em>confirm</em> or <em>contradict</em> your original problem statement? If the data says no, your V2 isn't an update — it's a pivot.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Stress the discipline: <strong>3–5 signals, not 50.</strong> The four buckets are guard-rails — pick one or two per bucket and run with them. For most learners the M6 set will be: Engagement (sessions / core-flow events), Retention (return visits), Quality (bounce rate), Impact (one event tied to the M2 hypothesis).</p>
      <p>The North Star line is the one to land hard: if the data <em>contradicts</em> your hypothesis, the right move is a pivot, not a tweak. We'll see this exact split show up in their AI analysis output in Lab 2.</p>
    </div>
  </div>
</section>

<!-- 11. THREE LAYERS OF ANALYTICS — Internal · External · Custom (matrix mirrors PPTX) -->
<section data-title="Three Layers of Analytics">
  <div class="inner" style="max-width: 1280px;">
    <div class="section-label">Three Layers of Analytics</div>
    <h2>What users do · what they feel · what they say.</h2>
    <p class="subtitle">To truly iterate, you need a multi-layered approach that captures what users <em>do</em>, what they <em>feel</em>, and what they <em>say</em>.</p>

    <div style="display:grid; grid-template-columns: 56px repeat(3, 1fr); margin: 12px auto 14px; max-width: 1220px; background: rgba(11,25,51,0.55); border: 1px solid rgba(96,165,250,0.22); border-radius: 18px; overflow: hidden; text-align: left;">
      <!-- ROW 1 · LAYER -->
      <div style="background: linear-gradient(180deg, #1241B0, #0c2f7a); display:flex; align-items:center; justify-content:center; border-bottom: 1px solid rgba(96,165,250,0.22);">
        <span style="writing-mode: vertical-rl; transform: rotate(180deg); font-family: Poppins, sans-serif; font-weight: 900; font-size: 11px; letter-spacing: 4px; color: #ffffff;">LAYER</span>
      </div>
      <div style="display:flex; align-items:center; gap:14px; padding: 14px 24px; border-bottom: 1px solid rgba(96,165,250,0.22); border-right: 1px solid rgba(96,165,250,0.12);">
        <span style="display:inline-flex; width:30px; height:30px; border-radius:50%; background:#1241B0; border:2px solid #60a5fa; color:#fff; font-weight:900; font-size:14px; align-items:center; justify-content:center; flex-shrink:0;">1</span>
        <span style="font-family: Poppins, sans-serif; font-weight: 700; font-size: 18px; color:#ffffff;">Internal</span>
      </div>
      <div style="display:flex; align-items:center; gap:14px; padding: 14px 24px; border-bottom: 1px solid rgba(96,165,250,0.22); border-right: 1px solid rgba(96,165,250,0.12);">
        <span style="display:inline-flex; width:30px; height:30px; border-radius:50%; background:#5b21b6; border:2px solid #a78bfa; color:#fff; font-weight:900; font-size:14px; align-items:center; justify-content:center; flex-shrink:0;">2</span>
        <span style="font-family: Poppins, sans-serif; font-weight: 700; font-size: 18px; color:#ffffff;">External</span>
      </div>
      <div style="display:flex; align-items:center; gap:14px; padding: 14px 24px; border-bottom: 1px solid rgba(96,165,250,0.22);">
        <span style="display:inline-flex; width:30px; height:30px; border-radius:50%; background:#065f46; border:2px solid #34d399; color:#fff; font-weight:900; font-size:14px; align-items:center; justify-content:center; flex-shrink:0;">3</span>
        <span style="font-family: Poppins, sans-serif; font-weight: 700; font-size: 18px; color:#ffffff;">Custom</span>
      </div>

      <!-- ROW 2 · TYPE -->
      <div style="background: rgba(96,165,250,0.08); display:flex; align-items:center; justify-content:center; border-bottom: 1px solid rgba(96,165,250,0.18);">
        <span style="writing-mode: vertical-rl; transform: rotate(180deg); font-family: Poppins, sans-serif; font-weight: 900; font-size: 11px; letter-spacing: 4px; color: #94a3b8;">TYPE</span>
      </div>
      <div style="padding: 12px 24px; border-bottom: 1px solid rgba(96,165,250,0.18); border-right: 1px solid rgba(96,165,250,0.12); font-family: Poppins, sans-serif; font-weight: 600; font-size: 14px; color: #e2e8f0;">Passive System Tracking</div>
      <div style="padding: 12px 24px; border-bottom: 1px solid rgba(96,165,250,0.18); border-right: 1px solid rgba(96,165,250,0.12); font-family: Poppins, sans-serif; font-weight: 600; font-size: 14px; color: #e2e8f0;">Passive Behaviour Tracking</div>
      <div style="padding: 12px 24px; border-bottom: 1px solid rgba(96,165,250,0.18); font-family: Poppins, sans-serif; font-weight: 600; font-size: 14px; color: #e2e8f0;">Active Sentiment Tracking</div>

      <!-- ROW 3 · DATA -->
      <div style="background: rgba(96,165,250,0.04); display:flex; align-items:center; justify-content:center; border-bottom: 1px solid rgba(96,165,250,0.18);">
        <span style="writing-mode: vertical-rl; transform: rotate(180deg); font-family: Poppins, sans-serif; font-weight: 900; font-size: 11px; letter-spacing: 4px; color: #94a3b8;">DATA</span>
      </div>
      <div style="padding: 12px 24px; border-bottom: 1px solid rgba(96,165,250,0.18); border-right: 1px solid rgba(96,165,250,0.12); font-size: 13px; color: #94a3b8; line-height: 1.5;">Surface-level engagement: active users, sessions, and page views.</div>
      <div style="padding: 12px 24px; border-bottom: 1px solid rgba(96,165,250,0.18); border-right: 1px solid rgba(96,165,250,0.12); font-size: 13px; color: #94a3b8; line-height: 1.5;">Deep-funnel signal: traffic sources, bounce rates, and conversion paths.</div>
      <div style="padding: 12px 24px; border-bottom: 1px solid rgba(96,165,250,0.18); font-size: 13px; color: #94a3b8; line-height: 1.5;">Direct qualitative data: star ratings, bug reports, and feature requests.</div>

      <!-- ROW 4 · TOOL -->
      <div style="background: linear-gradient(180deg, rgba(96,165,250,0.18), rgba(96,165,250,0.06)); display:flex; align-items:center; justify-content:center;">
        <span style="writing-mode: vertical-rl; transform: rotate(180deg); font-family: Poppins, sans-serif; font-weight: 900; font-size: 11px; letter-spacing: 4px; color: #cbd5e1;">TOOL</span>
      </div>
      <div style="padding: 14px 14px 12px; border-right: 1px solid rgba(96,165,250,0.12); display:flex; flex-direction: column; align-items: center; gap: 8px;">
        <img src="assets/m6/lovable-insights.png" alt="Lovable Insights Analytics dashboard" loading="lazy" style="width:100%; height:130px; object-fit: cover; object-position: top left; border-radius: 10px; border: 1px solid rgba(96,165,250,0.35); box-shadow: 0 6px 22px rgba(0,0,0,0.4);"/>
        <div style="font-family: Poppins, sans-serif; font-weight: 700; font-size: 10px; letter-spacing: 2px; color: #60a5fa;">LOVABLE INSIGHTS · BUILT-IN</div>
      </div>
      <div style="padding: 14px 14px 12px; border-right: 1px solid rgba(96,165,250,0.12); display:flex; flex-direction: column; align-items: center; gap: 8px;">
        <img src="assets/m6/ga4-dashboard.png" alt="Google Analytics 4 conversions dashboard" loading="lazy" style="width:100%; height:130px; object-fit: cover; object-position: top left; border-radius: 10px; border: 1px solid rgba(167,139,250,0.35); box-shadow: 0 6px 22px rgba(0,0,0,0.4);"/>
        <div style="font-family: Poppins, sans-serif; font-weight: 700; font-size: 10px; letter-spacing: 2px; color: #a78bfa;">GOOGLE ANALYTICS 4 · OPTIONAL</div>
      </div>
      <div style="padding: 14px 14px 12px; display:flex; flex-direction: column; align-items: center; gap: 8px;">
        <img src="assets/m6/feedback-modal.png" alt="In-product feedback modal with star rating" loading="lazy" style="width:100%; height:130px; object-fit: contain; background:#0b1220; border-radius: 10px; border: 1px solid rgba(52,211,153,0.35); box-shadow: 0 6px 22px rgba(0,0,0,0.4);"/>
        <div style="font-family: Poppins, sans-serif; font-weight: 700; font-size: 10px; letter-spacing: 2px; color: #34d399;">IN-PRODUCT CAPTURE · SUPABASE</div>
      </div>
    </div>

    <div class="callout-strip">
      <span class="callout-pill">The stack</span>
      <span>Lovable Insights is <em>Lab 1</em> today. GA4 is the optional post-class layer. The custom Supabase feedback loop is the senior-PM finishing move.</span>
    </div>

    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Layer 1 is what we use in class — Lovable Insights is free, instant, and already running. Layer 2 (GA4) is the optional post-class add-on; the Lab Guide has a 10-minute walkthrough. Layer 3 is the most advanced and the most powerful — the Supabase connection from M5 is exactly what enables it.</p>
      <p>Tell the cohort: "the most senior PM move you can make on your final project is layering all three. You won't do it today — but the moment you have a paying user, this is the architecture."</p>
    </div>
  </div>
</section>

<!-- 12. SECTION 02 — Hands-On Lab: Read Lovable Insights -->
<section class="section-break" data-title="Section 02 · Lab — Read Lovable Insights">
  <div class="section-break-inner">
    <div class="section-num">02</div>
    <div class="lab-title">Section 02 · Hands-On Lab</div>
    <div class="lab-name">Read Your Lovable Insights.</div>
    <div class="lab-desc">Open Insights, baseline your numbers, identify your lowest-engagement screen — then gather Slack peer feedback to triangulate.</div>
  </div>
</section>

<!-- 13. LAB 1 — Read Lovable Insights (10 min instructor-led) -->
<section data-title="Lab · Read Your Lovable Insights (10 min)">
  <div class="inner" style="max-width: 1240px;">
    <div class="demo-tag tag-exercise">Instructor-Led Lab · 10 minutes</div>
    <h2>Read your own analytics — the same critical eye, turned inward.</h2>
    <p class="subtitle">You just gave four classmates' products a critical read. Now do the same to your own. Capture your metrics as text — you'll paste them into Lab 2's AI prompt.</p>
    <div class="flow-steps" style="grid-template-columns: repeat(4, 1fr); max-width: 1180px; gap: 14px;">
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">1</div><div class="fs-icon">📊</div></div>
        <div class="fs-title">Open Lovable Insights</div>
        <div class="fs-text">In Lovable, click the chart icon in the top nav. Screenshot the panel to baseline your starting point.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">2</div><div class="fs-icon">📝</div></div>
        <div class="fs-title">Copy your key metrics</div>
        <div class="fs-text">Capture <strong>Visitors · Page Views · Views Per Visit · Duration · Bounce Rate</strong> as text — you'll paste them into Lab 2's prompt.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">3</div><div class="fs-icon">🔍</div></div>
        <div class="fs-title">Identify your weakest screen</div>
        <div class="fs-text">Where are users dropping off or not engaging? The lowest-engagement screen is the one Lab 2 will target.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">4</div><div class="fs-icon">🎯</div></div>
        <div class="fs-title">Audit honestly</div>
        <div class="fs-text">Is this what you expected? Are users behaving the way you predicted in M2 — or is the data telling a different story?</div>
      </div>
    </div>
    <div style="margin-top: 22px; padding: 16px 22px; background: rgba(96,165,250,0.08); border: 1.5px solid rgba(96,165,250,0.35); border-radius: 12px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;">
      <div style="text-align: left;">
        <div style="font-family:'Poppins',sans-serif; font-weight: 700; font-size: 15px; color: #fff; margin-bottom: 4px;">Open the full walkthrough</div>
        <div style="font-size: 13px; color: #b0b4c8;">Step-by-step Insights tour with the metric-capture table and the three audit questions — in the M6 Lab Guide.</div>
      </div>
      <a class="tool-btn" href="M6 - Lab Guide.html#phase-1" target="_blank" rel="noopener" style="white-space: nowrap;">→ Open Lab Guide · Phase 1 ↗</a>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Run this as a guided exercise — ask one volunteer to screen-share their Insights panel while you walk the room. Every learner does the same on their own product in parallel.</p>
      <p>Watch for the <strong>empty-data failure mode</strong>: a learner whose product had no real users yet (Insights panel is blank). Have them open their live URL in two different browsers right now to generate at least some signal before the lab moves on — otherwise the AI prompt in Lab 2 runs against nothing.</p>
      <p>Land the audit question hard: <em>"is the data telling you the M2 hypothesis is confirmed, or is it telling you V2 is a pivot?"</em> That's the question the AI will answer in Lab 2.</p>
    </div>
  </div>
</section>

<!-- 14. SECTION 03 — AI-Driven Product Iteration -->
<section class="section-break" data-title="Section 03 · AI-Driven Product Iteration">
  <div class="section-break-inner">
    <div class="section-num">03</div>
    <div class="lab-title">Section 03</div>
    <div class="lab-name">AI-Driven Product Iteration.</div>
    <div class="lab-desc">Stop crunching CSVs. Feed your signal to an LLM. Get a prioritised backlog in minutes. Translate one finding into one surgical prompt.</div>
  </div>
</section>

<!-- 15. AI-POWERED ANALYSIS — Old way vs New way + the strategic prompt -->
<section data-title="AI-Powered Analysis · The PM's New Superpower">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">AI-Powered Analysis · The PM's New Superpower</div>
    <h2>From data cruncher to decision maker.</h2>
    <p class="subtitle">You've been here before. Days cleaning data, building charts, writing a 10-page findings doc no one reads. In the AI era, you move from analysis to decision in minutes — but you still own the call.</p>
    <div class="two-col">
      <div class="tc tc-old">
        <div class="tc-label">🕰️ Old Way · Manual Analysis</div>
        <div class="tc-title">Days of exports + pivot tables</div>
        <ul>
          <li>Export CSVs from every tool.</li>
          <li>Build pivot tables in spreadsheets.</li>
          <li>Spend 6 hours writing a "findings" doc.</li>
          <li>Hope someone reads it before the product moves on.</li>
        </ul>
      </div>
      <div class="tc tc-new">
        <div class="tc-label">⚡ New Way · AI-Powered Synthesis</div>
        <div class="tc-title">Minutes to a prioritised backlog</div>
        <ul>
          <li>Feed problem statement + hypothesis + metrics + peer feedback to the LLM.</li>
          <li>Ask: "is this solving the problem? What are the top 3 fixes, ranked by impact?"</li>
          <li>Get a synthesised, ranked backlog in seconds.</li>
          <li>You own the final decision — the AI does not.</li>
        </ul>
      </div>
    </div>
    <div class="artifact-preview" style="max-width: 960px; margin-top: 22px; text-align: left;">
      <div class="ap-title">The Strategic Prompt · paste into your LLM of choice</div>
      <p style="font-size:13.5px; color:#cdd5e3; line-height:1.7; font-family:'IBM Plex Mono', monospace;">I built a product to solve this problem: <code>[problem statement]</code>. My hypothesis was: <code>[hypothesis]</code>. Here are the metrics from my live product: <code>[paste Lovable Insights data]</code>. Here is the peer feedback I received: <code>[paste Slack feedback]</code>.<br><br>Evaluate: is this product solving the problem? What does the data suggest? What are the top 3 things I should improve, <strong>ranked by likely impact</strong>?</p>
    </div>
    <div class="callout-strip">
      <span class="callout-pill">The discipline</span>
      <span>The AI provides the synthesis — <em>you</em> provide the conviction. Pick one finding. Not three.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>The reframe: 10x faster decisions, same level of judgement required. Stress that the strategic prompt has four inputs — problem, hypothesis, metrics, feedback — and asks for a <strong>ranked</strong> backlog. Ranking is what makes it actionable.</p>
      <p>The discipline line is the one to land: <strong>one finding, not three.</strong> Lab 2 is 15 minutes; they don't have time for a full rebuild. Picking the single highest-impact tweak is the muscle we're building.</p>
    </div>
  </div>
</section>

<!-- 16. FROM DATA SIGNAL TO TECHNICAL FIX — Persona · Branching · Guardrail -->
<section data-title="From Data Signal to Technical Fix">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">From Data Signal to Technical Fix</div>
    <h2>Every prompt now starts with <em>"based on the data..."</em></h2>
    <p class="subtitle">The AI tells you <strong>what</strong> is wrong — it's a list of problems. It doesn't tell you <strong>how</strong> to fix it. This is where you move from analysis to architecture.</p>
    <div class="m4-complete-grid">
      <div class="m4c-tile">
        <div class="m4c-num">🧠</div>
        <div class="m4c-meta">
          <div class="m4c-label">From "Verbose" to "Persona"</div>
          <div class="m4c-title">Persona Refinement</div>
          <div class="m4c-desc">If users are overwhelmed by text, don't ask for "less copy" — that's a tweak. Hardcode a <em>persona</em> into the system: "act as an efficiency expert" — and the entire app's voice shifts permanently.<br><br><code style="background:rgba(255,255,255,0.08); padding:6px 10px; border-radius:6px; font-size:11.5px; color:#cfd9e8; display:block; line-height:1.5;">"Based on the data showing 70% bounce, refactor all copy to the voice of an efficiency expert — short, declarative, action-first."</code></div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">🔀</div>
        <div class="m4c-meta">
          <div class="m4c-label">From "Bounce" to "Branching"</div>
          <div class="m4c-title">Visual Branching</div>
          <div class="m4c-desc">If GA4 shows a 70% bounce on a screen, the AI might suggest "the UI is too complex." Translate that into a <em>different mental model</em> — swap a list for a board, or a wizard for a single page.<br><br><code style="background:rgba(255,255,255,0.08); padding:6px 10px; border-radius:6px; font-size:11.5px; color:#cfd9e8; display:block; line-height:1.5;">"Based on the 70% bounce on /onboarding, swap the multi-step wizard for a single Kanban board the user can move cards on."</code></div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">🛡️</div>
        <div class="m4c-meta">
          <div class="m4c-label">From "Functional Gap" to "Guardrail"</div>
          <div class="m4c-title">Hard IF/THEN Rules</div>
          <div class="m4c-desc">When Insights show submissions failing in a specific shape, the AI flags a logic error. Translate that into a <em>guardrail</em> — an unbreakable IF/THEN rule the system can never violate.<br><br><code style="background:rgba(255,255,255,0.08); padding:6px 10px; border-radius:6px; font-size:11.5px; color:#cfd9e8; display:block; line-height:1.5;">"Based on the data showing duplicate invites, IF the recipient_email already exists in invites for this sender, THEN block the submit and show an inline warning."</code></div>
        </div>
      </div>
    </div>
    <div class="callout-strip">
      <span class="callout-pill">The pattern</span>
      <span>Every M6 prompt starts with <em>"based on the data showing..."</em> — that's how you stop feature-creeping and start surgically repairing.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>The three patterns map to the three types of finding the AI most often returns: voice/copy issues (→ Persona), structural / UX issues (→ Branching), logic / data issues (→ Guardrail). Walk through one example per pattern — keep it concrete.</p>
      <p>The pattern line is what learners write down: <strong>"based on the data showing..."</strong> opens every iteration prompt. It enforces the discipline that you're <em>repairing friction</em>, not adding features.</p>
    </div>
  </div>
</section>

<!-- 17. SECTION 04 — Hands-On Lab: AI Iteration Sprint -->
<section class="section-break" data-title="Section 04 · Lab — AI Iteration Sprint">
  <div class="section-break-inner">
    <div class="section-num">04</div>
    <div class="lab-title">Section 04 · Hands-On Lab</div>
    <div class="lab-name">Run an AI-Driven Iteration Sprint.</div>
    <div class="lab-desc">One finding, one prompt, one redeploy. Push the brief to GitHub.</div>
  </div>
</section>

<!-- 18. LAB 2 — AI Iteration Sprint (15 min) -->
<section data-title="Lab · Run an AI-Driven Iteration Sprint (15 min)">
  <div class="inner" style="max-width: 1240px;">
    <div class="demo-tag tag-exercise">Individual Lab · 15 minutes</div>
    <h2>Close the loop: data → AI → one fix → redeploy.</h2>
    <p class="subtitle">Pull together everything you gathered, run the strategic prompt, pick the single highest-impact finding, ship the fix, push to GitHub. Resist the temptation to fix everything — one finding, one change.</p>
    <div class="flow-steps" style="grid-template-columns: repeat(3, 1fr); max-width: 1180px; gap: 14px;">
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">1</div><div class="fs-icon">📥</div></div>
        <div class="fs-title">Gather your inputs</div>
        <div class="fs-text">Problem statement + hypothesis from your Living PRD, Lovable Insights metrics from Lab 1, and the peer feedback from your Slack thread.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">2</div><div class="fs-icon">🤖</div></div>
        <div class="fs-title">Run the strategic prompt</div>
        <div class="fs-text">Paste the prompt from slide 16 into ChatGPT / Claude / Gemini. Replace the four placeholders. Read the ranked backlog.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">3</div><div class="fs-icon">🎯</div></div>
        <div class="fs-title">Pick one finding</div>
        <div class="fs-text">The single highest-impact recommendation. Not three. Not the safest. The one that moves the needle.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">4</div><div class="fs-icon">⚡</div></div>
        <div class="fs-title">Write your "based on the data" prompt</div>
        <div class="fs-text">Pattern: <em>"Based on the user data showing [finding], update [specific part] to [specific change]. Keep all existing functionality working."</em> Pick Persona, Branching, or Guardrail.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">5</div><div class="fs-icon">🧪</div></div>
        <div class="fs-title">Test, audit, then redeploy</div>
        <div class="fs-text">Does the change work as expected? Did anything else break? If yes, re-prompt before redeploying. Once clean, click Publish.</div>
      </div>
      <div class="flow-step">
        <div class="fs-head"><div class="fs-num">6</div><div class="fs-icon">📤</div></div>
        <div class="fs-title">Push to GitHub</div>
        <div class="fs-text">Commit <code>Iteration-Sprint-Brief.md</code> to <code>06-iteration/</code> with the AI analysis, the chosen finding, the implementation prompt, and the redeployed URL.</div>
      </div>
    </div>
    <div style="margin-top: 22px; padding: 16px 22px; background: rgba(110,231,183,0.08); border: 1.5px solid rgba(110,231,183,0.35); border-radius: 12px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;">
      <div style="text-align: left;">
        <div style="font-family:'Poppins',sans-serif; font-weight: 700; font-size: 15px; color: #fff; margin-bottom: 4px;">Open the sprint walkthrough</div>
        <div style="font-size: 13px; color: #b0b4c8;">Every step, every verification check, plus the optional GA4 post-class setup — in the M6 Lab Guide.</div>
      </div>
      <a class="tool-btn" href="M6 - Lab Guide.html#phase-2" target="_blank" rel="noopener" style="white-space: nowrap;">→ Open Lab Guide · Phase 2 ↗</a>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>15 minutes is tight on purpose. Push the constraint hard: <strong>one finding, one change.</strong> Most learners will want to fix three things — that's how they break their product right before the showcase. Block that instinct.</p>
      <p>Spin up Zoom breakout rooms for a "co-working" feel — everyone builds in parallel with cameras on. Stay in the main room for support; learners DM you in Slack if stuck.</p>
      <p>The single hardest thing to do well: <strong>test before redeploying.</strong> If Lovable made multiple changes and one broke something, don't ship it — re-prompt to revert that piece first.</p>
    </div>
  </div>
</section>

<!-- 19. FINALIZE PROJECT DELIVERABLES — 15 min individual exercise -->
<section data-title="Finalize Your Project Deliverables">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">Individual Exercise · 15 minutes</div>
    <h2>Build your showcase site — host the whole journey on GitHub.</h2>
    <p class="subtitle">You've got everything you need across six modules in your repo. Fifteen minutes to fork the showcase template, drop in your placeholders, and push to GitHub Pages — that public URL is what you submit to Docebo.</p>
    <div class="m4-complete-grid" style="grid-template-columns: repeat(3, 1fr);">
      <div class="m4c-tile">
        <div class="m4c-num">05</div>
        <div class="m4c-meta">
          <div class="m4c-label">The Product</div>
          <div class="m4c-title">Live URL + Hypothesis + Scenario</div>
          <div class="m4c-desc">The deployed product link, your original M2 hypothesis, and the scenario the product was built to solve.</div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">06</div>
        <div class="m4c-meta">
          <div class="m4c-label">The Validation</div>
          <div class="m4c-title">Validation Brief Highlights</div>
          <div class="m4c-desc">Key sections of your Validation Brief — assumptions tested, data confirmed or challenged.</div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">07</div>
        <div class="m4c-meta">
          <div class="m4c-label">The Blueprint</div>
          <div class="m4c-title">Living PRD Key Elements</div>
          <div class="m4c-desc">The source of truth bridging your prototype and engineering handoff.</div>
        </div>
      </div>
      <div class="m4c-tile">
        <div class="m4c-num">08</div>
        <div class="m4c-meta">
          <div class="m4c-label">The Logic</div>
          <div class="m4c-title">Core Prompt Chain</div>
          <div class="m4c-desc">The prompts that power your multi-screen architecture from M3.</div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">09</div>
        <div class="m4c-meta">
          <div class="m4c-label">The Handoff</div>
          <div class="m4c-title">Finalised Engineering Handoff</div>
          <div class="m4c-desc">Production-ready spec bridging vision and execution — including today's iteration evidence.</div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">10</div>
        <div class="m4c-meta">
          <div class="m4c-label">The Story</div>
          <div class="m4c-title">Friction · Learning · Aha</div>
          <div class="m4c-desc">Your individual insights — what broke, what you learned, the biggest aha moment of the course.</div>
        </div>
      </div>
    </div>
    <div style="margin-top: 18px; padding: 16px 22px; background: linear-gradient(135deg, rgba(59,130,246,0.12), rgba(167,139,250,0.08)); border: 1.5px solid rgba(96,165,250,0.35); border-radius: 12px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap;">
      <div style="text-align: left;">
        <div style="font-family:'Poppins',sans-serif; font-weight: 700; font-size: 15px; color: #fff; margin-bottom: 4px;">Open the Showcase Generator</div>
        <div style="font-size: 13px; color: #b0b4c8;">Paste your <strong>public</strong> GitHub repo URL — the tool crawls every markdown file, finds your Problem · Hypothesis · Validation · PRD · Prompts · Handoff · Friction · Learning · Aha sections, and renders the showcase live. Download <code>index.html</code>, drop it in <code>docs/</code>, push, and turn on GitHub Pages.</div>
      </div>
      <a class="tool-btn" href="../Templates/Showcase-Generator.html" target="_blank" rel="noopener" style="white-space: nowrap;">↗ Open the generator</a>
    </div>
    <div style="margin-top: 12px; padding: 14px 20px; background: rgba(167,139,250,0.08); border-left: 4px solid #a78bfa; border-radius: 8px; font-size: 13.5px; color: #e0e0f0; line-height: 1.55; text-align: left;">
      🎯 <strong>The bar is not perfection.</strong> The bar is your <em>strategic logic</em> and what you learned. If a section is missing from your repo, the generator shows a clear placeholder telling you exactly what heading to add.
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>15 minutes of solo polish — but the deliverable is <strong>a live GitHub Pages site</strong>, not a PowerPoint. Drop the link to <code>Templates/Showcase-Generator.html</code> in <code>#cohort-channel</code>. Every learner opens it, pastes their repo URL, and the tool scans every markdown file in their repo — pattern-matching H2 headers against the 8 showcase slots (Problem · Hypothesis · Validation · PRD elements · Handoff · Friction · Learning · Aha) plus fenced code blocks for the prompt chain. Hit Download HTML, drop the file in <code>docs/index.html</code>, push, Settings → Pages → main / /docs → done. That public URL is what they submit to Docebo.</p>
      <p>Two prereqs to flag: (1) the repo must be <strong>public</strong> (or paste a personal access token in the optional field), and (2) any section the tool can't find shows up as a yellow placeholder card with explicit instructions. Most learners will be missing Friction · Learning · Aha — those usually aren't in <code>livingprd.md</code> or <code>engineeringhandoff.md</code>. Tell them to drop a <code>STORY.md</code> in their repo root with three short sections (<code>## Friction</code>, <code>## Learning</code>, <code>## Aha</code>). Template lives in <code>Templates/STORY-Template.md</code>.</p>
      <p>Walk the slide map: title · product · problem · hypothesis · validation · PRD · prompts · handoff · friction · learning · aha. The story slides (friction/learning/aha) are where most learners under-invest — push hard: <em>"what was your aha moment? Write the sentence you'd say at a dinner party."</em> Same energy as the AI Product Strategy showcases — the URL is the artifact, not a slide deck.</p>
    </div>
  </div>
</section>

<!-- 20. LEARNER JOURNEY · M1 → M6 RECAP -->
<section data-title="Learner Journey · M1 → M6">
  <div class="inner" style="max-width: 1400px;">
    <div class="demo-tag tag-debrief">The Journey · Complete</div>
    <h2>Six modules. Three phases. One closed loop.</h2>
    <p class="subtitle">The Confidence Line climbed module by module — from planning paralysis to a measured iteration.</p>

    <!-- THE CONFIDENCE LINE — 3 PHASE BLOCKS -->
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 26px 0 14px;">

      <!-- ═══ PHASE 1 · HIGH AMBIGUITY ═══ -->
      <div style="background: linear-gradient(180deg, rgba(244,114,182,0.06), rgba(244,114,182,0.02)); border: 1px solid rgba(244,114,182,0.22); border-radius: 16px; padding: 18px; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #f472b6, #ec4899);"></div>
        <div style="text-align: center; padding: 4px 0 14px; border-bottom: 1px solid rgba(244,114,182,0.18); margin-bottom: 14px;">
          <div style="font-family:'Poppins',sans-serif; font-size: 11px; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase; color: #f9a8d4; margin-bottom: 4px;">Phase 1</div>
          <div style="font-family:'Poppins',sans-serif; font-size: 20px; font-weight: 800; color: #fff; letter-spacing: -0.01em;">High Ambiguity</div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <div style="background: rgba(255,255,255,0.035); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.04);">
            <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px;">
              <div style="font-family:'Poppins',sans-serif; font-size: 24px; font-weight: 900; color: #f9a8d4; line-height: 1;">M1</div>
              <div style="font-family:'Poppins',sans-serif; font-size: 15px; font-weight: 700; color: #fff;">Execute Velocity</div>
            </div>
            <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.55;"><strong style="color: #fff;">Shift:</strong> planning paralysis &rarr; building at lightspeed.<br><strong style="color: #fff;">Win:</strong> a functional prototype from an ambiguous problem in one session.</div>
          </div>
          <div style="background: rgba(255,255,255,0.035); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.04);">
            <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px;">
              <div style="font-family:'Poppins',sans-serif; font-size: 24px; font-weight: 900; color: #f9a8d4; line-height: 1;">M2</div>
              <div style="font-family:'Poppins',sans-serif; font-size: 15px; font-weight: 700; color: #fff;">Validation Pivot</div>
            </div>
            <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.55;"><strong style="color: #fff;">Shift:</strong> building by instinct &rarr; prototypes that answer the why.<br><strong style="color: #fff;">Win:</strong> mapping assumptions, injecting data, solving the right problem.</div>
          </div>
        </div>
      </div>

      <!-- ═══ PHASE 2 · GAINING CLARITY ═══ -->
      <div style="background: linear-gradient(180deg, rgba(96,165,250,0.06), rgba(96,165,250,0.02)); border: 1px solid rgba(96,165,250,0.28); border-radius: 16px; padding: 18px; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #60a5fa, #3b82f6);"></div>
        <div style="text-align: center; padding: 4px 0 14px; border-bottom: 1px solid rgba(96,165,250,0.2); margin-bottom: 14px;">
          <div style="font-family:'Poppins',sans-serif; font-size: 11px; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase; color: #93c5fd; margin-bottom: 4px;">Phase 2</div>
          <div style="font-family:'Poppins',sans-serif; font-size: 20px; font-weight: 800; color: #fff; letter-spacing: -0.01em;">Gaining Clarity</div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <div style="background: rgba(255,255,255,0.035); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.04);">
            <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px;">
              <div style="font-family:'Poppins',sans-serif; font-size: 24px; font-weight: 900; color: #93c5fd; line-height: 1;">M3</div>
              <div style="font-family:'Poppins',sans-serif; font-size: 15px; font-weight: 700; color: #fff;">Architecture Leap</div>
            </div>
            <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.55;"><strong style="color: #fff;">Shift:</strong> single screens &rarr; multi-screen systems that hold under complexity.<br><strong style="color: #fff;">Win:</strong> prompt chaining + constraint grounding for consistency at scale.</div>
          </div>
          <div style="background: rgba(255,255,255,0.035); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.04);">
            <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px;">
              <div style="font-family:'Poppins',sans-serif; font-size: 24px; font-weight: 900; color: #93c5fd; line-height: 1;">M4</div>
              <div style="font-family:'Poppins',sans-serif; font-size: 15px; font-weight: 700; color: #fff;">Engineering Bridge</div>
            </div>
            <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.55;"><strong style="color: #fff;">Shift:</strong> informal builds &rarr; handoff-ready production specs.<br><strong style="color: #fff;">Win:</strong> converting a prototype into a spec engineering can execute on.</div>
          </div>
        </div>
      </div>

      <!-- ═══ PHASE 3 · PRODUCTION CONFIDENCE ═══ -->
      <div style="background: linear-gradient(180deg, rgba(52,211,153,0.06), rgba(52,211,153,0.02)); border: 1px solid rgba(52,211,153,0.25); border-radius: 16px; padding: 18px; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #34d399, #10b981);"></div>
        <div style="text-align: center; padding: 4px 0 14px; border-bottom: 1px solid rgba(52,211,153,0.18); margin-bottom: 14px;">
          <div style="font-family:'Poppins',sans-serif; font-size: 11px; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase; color: #6ee7b7; margin-bottom: 4px;">Phase 3</div>
          <div style="font-family:'Poppins',sans-serif; font-size: 20px; font-weight: 800; color: #fff; letter-spacing: -0.01em;">Production Confidence</div>
        </div>
        <div style="display: flex; flex-direction: column; gap: 10px;">
          <div style="background: rgba(255,255,255,0.035); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.04);">
            <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px;">
              <div style="font-family:'Poppins',sans-serif; font-size: 24px; font-weight: 900; color: #6ee7b7; line-height: 1;">M5</div>
              <div style="font-family:'Poppins',sans-serif; font-size: 15px; font-weight: 700; color: #fff;">Production Leap</div>
            </div>
            <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.55;"><strong style="color: #fff;">Shift:</strong> standalone interfaces &rarr; integrated, deployed products.<br><strong style="color: #fff;">Win:</strong> live DBs, secure APIs, a public URL.</div>
          </div>
          <div style="background: rgba(255,255,255,0.035); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255,255,255,0.04);">
            <div style="display: flex; align-items: baseline; gap: 10px; margin-bottom: 7px;">
              <div style="font-family:'Poppins',sans-serif; font-size: 24px; font-weight: 900; color: #6ee7b7; line-height: 1;">M6</div>
              <div style="font-family:'Poppins',sans-serif; font-size: 15px; font-weight: 700; color: #fff;">Iteration Engine</div>
            </div>
            <div style="font-size: 12.5px; color: #cbd5e1; line-height: 1.55;"><strong style="color: #fff;">Shift:</strong> shipping and hoping &rarr; measuring, learning, redeploying.<br><strong style="color: #fff;">Win:</strong> AI-driven analytics + a surgical fix that secures the Confidence Line.</div>
          </div>
        </div>
      </div>
    </div>

    <!-- THE CONFIDENCE LINE TRAJECTORY BAR — gradient flows across all 3 phases -->
    <div style="display: flex; align-items: center; gap: 18px; padding: 16px 22px; background: linear-gradient(90deg, rgba(244,114,182,0.1), rgba(96,165,250,0.12) 50%, rgba(52,211,153,0.1)); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; margin-top: 4px;">
      <span style="background: linear-gradient(135deg, #f472b6, #60a5fa 50%, #34d399); color: #fff; font-family:'Poppins',sans-serif; font-size: 11px; font-weight: 800; letter-spacing: 0.15em; text-transform: uppercase; padding: 6px 14px; border-radius: 6px; white-space: nowrap;">The Confidence Line</span>
      <span style="font-size: 14px; color: #e0e0f0; line-height: 1.55;"><em style="color: #f9a8d4; font-style: normal; font-weight: 600;">vague intuition</em> &rarr; <em style="color: #93c5fd; font-style: normal; font-weight: 600;">clarifying signal</em> &rarr; <em style="color: #6ee7b7; font-style: normal; font-weight: 600;">data-backed conviction</em>. That's not a course &mdash; that's a career shift.</span>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Slow down here. This is the emotional payoff of the whole certification. Walk the three phases of the Confidence Line out loud: <strong>"In Phase 1 — High Ambiguity</strong>, you went from planning paralysis to a clickable prototype (M1) and from instinct to falsifiable validation (M2). <strong>In Phase 2 — Gaining Clarity</strong>, you scaled to multi-screen systems with prompt chains (M3) and turned them into engineering-ready specs (M4). <strong>In Phase 3 — Production Confidence</strong>, you put the product on a live URL (M5) and closed the build-measure-iterate loop with real data (M6)."</p>
      <p>Point at the gradient bar at the bottom: "this is the Confidence Line, end-to-end. Pink to blue to green. Vague intuition to clarifying signal to data-backed conviction." Let the visual carry the closer: "you now have a build-measure-iterate toolkit most PMs at unicorn companies don't have. That's the identity you walk out with today."</p>
    </div>
  </div>
</section>

<!-- 21. BREAK · between Learner Journey and the Final Project Showcase -->
<section class="centered" data-title="Take a Beat">
  <div class="inner">
    <div class="demo-tag tag-break">Break · 5 minutes</div>
    <h2>Take a beat. ☕</h2>
    <p class="subtitle">Six modules sit behind you. Refill, stretch, breathe. When you come back, it's <em>your</em> turn to demo.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>5-minute timer in <code>#cohort-channel</code>. Use the buffer to pre-load the showcase order — pin a quick list of who presents first, second, third. Anyone with audio/video issues, troubleshoot now, not during the demos.</p>
    </div>
  </div>
</section>

<!-- 22. CAMERAS ON · pre-showcase reminder -->
<section class="cameras-section" data-title="Cameras On">
  <div class="cameras-inner">
    <div class="cameras-layout">
      <div class="cameras-left">
        <img class="cameras-logo" src="../Design/Product-School-Logo.png" alt="Product School"/>
        <div class="cameras-card">
          <h2>Reminder! 🚨</h2>
          <div class="cameras-arrow">→ Cameras On</div>
          <p>It's always better to see your smiling face — especially on showcase day! Be present and visible to keep the energy high for every demo.</p>
        </div>
      </div>
      <div class="cameras-photo-strip">
        <img src="../Design/cameras-on.png" alt="Cameras On"/>
      </div>
    </div>
  </div>
</section>

<!-- 23. KEY TAKEAWAYS -->
<section data-title="Key Takeaways">
  <div class="inner" style="max-width: 1180px;">
    <div class="section-label">Key Takeaways</div>
    <h2>Measure product performance for AI-driven iteration.</h2>
    <div class="m4-complete-grid">
      <div class="m4c-tile">
        <div class="m4c-num">01</div>
        <div class="m4c-meta">
          <div class="m4c-label">Shipping ≠ Finishing</div>
          <div class="m4c-title">The live URL is the start of the loop</div>
          <div class="m4c-desc">Shipping a vibe-coded product is the <em>start</em> of the feedback loop, not the finish line. PMs replace "I think" with "the data shows" — tracking metrics that validate or challenge the M2 hypothesis.</div>
        </div>
      </div>
      <div class="m4c-tile b">
        <div class="m4c-num">02</div>
        <div class="m4c-meta">
          <div class="m4c-label">Layered Analytics</div>
          <div class="m4c-title">Internal · External · Custom</div>
          <div class="m4c-desc">A multi-layered analytics approach captures system engagement, behavioural funnel signal, and qualitative sentiment — together they surface the evidence needed to prioritise fixes.</div>
        </div>
      </div>
      <div class="m4c-tile c">
        <div class="m4c-num">03</div>
        <div class="m4c-meta">
          <div class="m4c-label">AI as Decision Engine</div>
          <div class="m4c-title">Minutes, not days</div>
          <div class="m4c-desc">PMs transform live product data into a prioritised backlog in minutes by feeding problem + hypothesis + metrics + feedback into an LLM. Hours of manual analysis become a synthesised, actionable evaluation.</div>
        </div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Recap pace — 60 seconds per takeaway. The throughline: <em>discipline</em>. M6 is where the build-measure-iterate loop stops being a buzzword and becomes a muscle.</p>
    </div>
  </div>
</section>

<!-- 24. SECTION 05 — Final Project Showcase -->
<section class="section-break" data-title="Section 05 · Final Project Showcase">
  <div class="section-break-inner">
    <div class="section-num">05</div>
    <div class="lab-title">Section 05 · Final Project Showcase</div>
    <div class="lab-name">Demo Your Live Product.</div>
    <div class="lab-desc">5–6 volunteers present live. 10 minutes per demo. Everyone submits to Docebo within 7 days.</div>
  </div>
</section>

<!-- 25. SHOWCASE KICKOFF — LMS + presentation flow -->
<section data-title="Your Time to Shine">
  <div class="inner" style="max-width: 1180px;">
    <div class="demo-tag tag-debrief">Showcase Kick-Off</div>
    <h2>Your time to shine. 🌟</h2>
    <p class="subtitle">10 minutes per volunteer. Demo your live product, walk through your strategic logic, share the one finding from today's iteration sprint.</p>
    <div class="ep-grid">
      <div class="ep-card">
        <div class="ep-num">01</div>
        <div class="ep-title">For volunteers · ~10 minutes each</div>
        <div class="ep-desc">Open with the problem (M2). Show the live URL. Walk through one core flow. Land on your aha moment from today's iteration sprint. Stay on time — the instructor will give a 6–7 minute warning.</div>
      </div>
      <div class="ep-card">
        <div class="ep-num">02</div>
        <div class="ep-title">For the audience</div>
        <div class="ep-desc">Cameras on. Energy high. Drop one piece of feedback in <code>#cohort-channel</code> per demo — same labels as Lab 1: 🐛 Bug · 🤔 Friction · 🤩 Compliment · 💡 Feature Idea.</div>
      </div>
    </div>
    <div style="margin-top: 18px; padding: 14px 20px; background: rgba(248,113,113,0.08); border-left: 4px solid #f87171; border-radius: 8px; font-size: 13.5px; color: #e0e0f0; line-height: 1.55; text-align: left;">
      📍 <strong>LMS submission required.</strong> Every learner — volunteer or not — must submit a finalised copy of the Final Project Deliverables Deck to <strong>Docebo</strong> within <strong>7 days</strong> of class to qualify for certification.
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Call on your first volunteer right after this slide. Get them to share their screen. Live feedback uses the same rubric as the cohort feedback (Project Clarity, Credibility &amp; Reasoning, Strategic Thinking, Application of Concepts) — but make it warm. This is the celebration moment, not an exam.</p>
      <p>Give a 6–7 minute warning per presenter. If a learner is going long, cut respectfully — protect the rest of the showcase. After all volunteers, return here to remind every learner about the 7-day Docebo deadline.</p>
    </div>
  </div>
</section>

<!-- 26. DAY 6 SURVEY -->
<section class="centered" data-title="Day 6 Survey">
  <div class="inner">
    <div class="demo-tag tag-debrief">Feedback</div>
    <h2>Your opinion matters.</h2>
    <p class="subtitle">Two minutes. Helps us iterate the cohort — like a real product team.</p>
    <div class="artifact-preview" style="max-width: 560px;">
      <div class="ap-title">End-of-Session Survey · Day 6</div>
      <p style="font-size:14px; color:#cdd5e3; line-height:1.6;">Scan the QR or use the link in <code>#cohort-channel</code>. Your insights shape the next cohort.</p>
    </div>
    <p style="font-size:14px; color:#8899bb; margin-top:18px; text-align:center;">This is your last in-class survey — make it count.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Drop the link in <code>#cohort-channel</code> as you say this. Two minutes max. The Day 6 survey is the most actionable — it shapes the next cohort's entire structure. Push for honest, specific feedback.</p>
    </div>
  </div>
</section>

<!-- 27. RESOURCES & TEMPLATES -->
<section data-title="Resources &amp; Templates">
  <div class="inner" style="max-width: 1240px;">
    <div class="section-label">Resources &amp; Templates</div>
    <h2>Everything Module 6 ships with.</h2>
    <p class="subtitle">Bookmark them — they're referenced across your final-project submission. <strong>Your GitHub repo is the source of truth</strong>; the tools below are aids.</p>

    <div class="resources-hero">
      <div class="rh-logo"><img src="../Design/logos/github.svg" alt="GitHub"/></div>
      <div class="rh-content">
        <div class="rh-eyebrow">Primary artifact · GitHub-first</div>
        <div class="rh-title">Your GitHub repo (source of truth)</div>
        <div class="rh-desc"><strong>This is where your work lives.</strong> Today's deliverable: <code>06-iteration/Iteration-Sprint-Brief.md</code> with the AI analysis, the chosen finding, the implementation prompt, and the redeployed URL. Plus the finalised Final-Project deck submitted to Docebo within 7 days.</div>
      </div>
    </div>

    <div class="resources-tiles">
      <div class="card-item" style="--card-accent:#60a5fa;">
        <div class="card-icon">🧪</div>
        <div class="card-title">Module 6 Lab Guide</div>
        <div class="card-desc"><a href="M6 - Lab Guide.html" target="_blank" rel="noopener" style="color:#60a5fa;">Open the lab guide ↗</a> — full walkthrough: Insights tour, Slack peer feedback, AI analysis, the one fix, redeploy + GitHub push.</div>
      </div>
      <div class="card-item" style="--card-accent:#a78bfa;">
        <div class="card-icon">📋</div>
        <div class="card-title">Iteration Sprint Brief Template</div>
        <div class="card-desc"><a href="../Templates/Iteration-Sprint-Brief.md" target="_blank" rel="noopener" style="color:#a78bfa;">Open the template ↗</a> — the 7-section structure your <code>Iteration-Sprint-Brief.md</code> follows.</div>
      </div>
      <div class="card-item" style="--card-accent:#fb7185;">
        <div class="card-icon">📚</div>
        <div class="card-title">M6 Frameworks Reference Card</div>
        <div class="card-desc"><a href="Module 6 - Frameworks Reference Card.html" target="_blank" rel="noopener" style="color:#fb7185;">Open the card ↗</a> — Iteration Mindset · Metrics That Matter · Three Layers · AI Analysis Prompt · Data Signal → Fix.</div>
      </div>
      <div class="card-item" style="--card-accent:#f9a8d4;">
        <div class="card-icon">📋</div>
        <div class="card-title">Final Project Brief</div>
        <div class="card-desc"><a href="../Final Project - Requirements and Scenario Guide.html" target="_blank" rel="noopener" style="color:#f9a8d4;">Open the brief ↗</a> — scenarios, deliverables, rubric, timeline, and the LMS submission requirements.</div>
      </div>
    </div>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Drop this card list in <code>#cohort-channel</code> right after class — pin it. The Lab Guide is the walkthrough; the Iteration Sprint Brief Template is the "what good looks like" reference; the Frameworks Reference Card is the cheat sheet for the M6 mental models.</p>
      <p><strong>GitHub-first rule, one last time:</strong> the canonical artefact lives at <code>06-iteration/Iteration-Sprint-Brief.md</code>. The Final Project deck goes to Docebo for cert; the GitHub repo is your portfolio piece for the rest of your career.</p>
    </div>
  </div>
</section>

<!-- 28. Q&A -->
<section class="centered" data-title="Q&amp;A">
  <div class="inner">
    <div class="demo-tag tag-debrief">Instructor-Led Q&amp;A</div>
    <h2>Questions?</h2>
    <p class="subtitle">Last chance live. Async: <code>#cohort-channel</code> stays open — instructor responds within ~24h while submissions roll in.</p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>Open the floor for 3–4 minutes. Two common Q&amp;A patterns at the end of a cohort: <strong>"what do I do after I submit?"</strong> — point them at the Final Project Brief next-steps section and the cohort alumni Slack. <strong>"how do I keep building?"</strong> — recommend they iterate on their own product weekly for the next 30 days using the same M6 loop.</p>
    </div>
  </div>
</section>

<!-- 29. END -->
<section class="centered" data-title="Certification Complete">
  <div class="inner">
    <div class="demo-tag tag-debrief">End of Module 6 · End of Certification</div>
    <h2>You closed the loop.</h2>
    <p class="subtitle">A live URL. Real user data. An AI-powered iteration. A redeploy. A finalised deck. You don't just have a product — you have a <em>practice</em>.</p>
    <div class="artifact-preview" style="max-width: 620px;">
      <div class="ap-title">Today's repo state</div>
      <p style="font-size:14px; color:#cdd5e3; line-height:1.7;"><code>06-iteration/Iteration-Sprint-Brief.md</code> · updated <code>HANDOFF.md</code> · redeployed URL in <code>README.md</code>. Final Project deck submitted to Docebo within 7 days.</p>
    </div>
    <p style="font-size:14px; color:#8899bb; margin-top:20px; text-align:center;">Welcome to the Vibe Coding alumni community. <strong style="color:#fff;">Keep shipping. Keep measuring. Keep iterating.</strong></p>
    <div class="notes">
      <h4>Speaker Notes</h4>
      <p>The identity-shift closer. Don't oversell — name it: today they finished as Technical PMs who can ship, measure, and iterate end-to-end. Thank them for the cohort energy. Drop the alumni Slack channel link and the post-cert resource list one last time.</p>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# Assemble
# ---------------------------------------------------------------------------

src = M5.read_text()

# split header / footer at the body markers
m_start = re.search(r'<!--\s*1\.\s*HERO\s*-->', src)
m_end = re.search(r'\n<script>\s*\n\s*const sections', src)
if not m_start or not m_end:
    raise SystemExit('Could not find M5 body markers — abort.')

header = src[:m_start.start()]
footer = src[m_end.start():]

# Update the page title in <head>
header = header.replace(
    '<title>Module 5 — Ship Live Products with Full-Stack Logic · Instructor</title>',
    '<title>Module 6 — Measure Product Performance for AI-Driven Iteration · Instructor</title>',
)

# Substitute demo id placeholders
body = BODY.replace('__DEMO_ID__', DEMO_ID)

# Assemble instructor deck (with notes)
instructor = header + body.lstrip('\n') + '\n\n' + footer
M6.write_text(instructor)
print(f'wrote {M6} ({len(instructor)} bytes)')

# Build shareable deck by stripping <div class="notes">...</div> blocks.
# Pattern matches the entire indented block on its own lines so the parent's
# closing </div> retains its original indentation.
shareable = re.sub(
    r'^[ \t]*<div class="notes">[\s\S]*?</div>[ \t]*\r?\n',
    '',
    instructor,
    flags=re.MULTILINE,
)
M6_SHARE.write_text(shareable)
print(f'wrote {M6_SHARE} ({len(shareable)} bytes)')
