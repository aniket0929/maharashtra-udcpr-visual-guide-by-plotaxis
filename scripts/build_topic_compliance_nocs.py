"""
UDCPR FROM SCRATCH - TOPIC 8 WORKBENCH GENERATOR
Builds topics/building-compliance-and-nocs.html with an interactive statutory compliance engine,
trigger-based NOC matrix, chronological 4-stage approval roadmap, and verification quiz.
Strictly anchored to ucpr_real.md (Reg. 2.2.11, 1.3(93)(xiv), 3.1, 9.29, 12.1, 13.2-13.4, 2.7-2.9).
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Building Compliance, Statutory NOCs &amp; Approval Roadmap | UDCPR from Scratch</title>
  <meta name="description" content="Statutory Compliance &amp; NOC Roadmap for Maharashtra UDCPR. Determine required clearances: Fire CFO, Environmental SEIAA, STP Grey Water, RWH, Airport, Railway, and Forest buffers based on exact plot parameters.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/blueprint.css">
  <link rel="stylesheet" href="/css/components.css">
  <style>
    .compliance-card {
      border: 1px solid var(--line-strong);
      background: var(--paper);
      padding: 14px;
      margin-bottom: 12px;
      position: relative;
    }
    .compliance-card.triggered {
      border-left: 4px solid var(--blueprint);
      background: var(--paper-raised);
    }
    .compliance-card.exempt {
      border-left: 4px solid var(--line-strong);
      opacity: 0.65;
    }
    .stage-badge {
      font-family: var(--mono);
      font-size: 10px;
      font-weight: 700;
      padding: 2px 8px;
      text-transform: uppercase;
      display: inline-block;
    }
    .stage-presanction {
      background: #e8f0fe;
      color: #1a73e8;
      border: 1px solid #1a73e8;
    }
    .stage-plinth {
      background: #fef7e0;
      color: #b06000;
      border: 1px solid #b06000;
    }
    .stage-superstructure {
      background: #f3e8fd;
      color: #7b1fa2;
      border: 1px solid #7b1fa2;
    }
    .stage-oc {
      background: #e6f4ea;
      color: #137333;
      border: 1px solid #137333;
    }
    .clause-ref {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--blueprint);
      font-weight: 600;
    }
    .dept-pill {
      font-family: var(--mono);
      font-size: 10px;
      background: var(--paper);
      border: 1px solid var(--ink);
      padding: 1px 6px;
      color: var(--ink);
    }
    .filter-tab-btn {
      background: var(--paper);
      border: 1px solid var(--ink);
      padding: 6px 14px;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      color: var(--ink);
    }
    .filter-tab-btn.active {
      background: var(--blueprint);
      color: #FAF8F2;
      border-color: var(--blueprint);
    }
  </style>
</head>
<body>

  <!-- THE DRAWING SHEET CONTAINER -->
  <div class="sheet">
    <div class="ruler-top"></div>
    <div class="corner-tick tl"></div>
    <div class="corner-tick tr"></div>
    <div class="corner-tick bl"></div>
    <div class="corner-tick br"></div>

    <!-- Statutory Disclaimer Strip -->
    <div class="disclaimer-strip">
      <strong>STATUTORY SPECIFICATION:</strong> Reg. 2.2.11 (Clearance from Other Departments), Reg. 1.3(93)(xiv) (Special Buildings), Reg. 3.1 (Site Ineligibility &amp; Restrictions), Reg. 9.29 (Fire Exits), Reg. 13.2-13.4, and Appendices A to J of UDCPR-2020.
    </div>

    <!-- Sheet Navigation -->
    <nav class="sheet-nav">
      <a href="/" class="brand-block">
        <span class="brand-stamp">UDCPR</span>
        <div class="brand-title-group">
          <h1>UDCPR from Scratch</h1>
          <span>Practice Workbench • Drawing Sheet</span>
        </div>
      </a>

      <ul class="nav-menu">
        <li class="nav-item"><a href="/topics/" class="active">Topics</a></li>
        <li class="nav-item"><a href="/chapters/">Chapters</a></li>
        <li class="nav-item"><a href="/glossary.html">Glossary</a></li>
        <li class="nav-item"><a href="/formulas.html">Formulas</a></li>
        <li class="nav-item"><a href="/amendments.html">Amendments (#)</a></li>
        <li class="nav-item"><a href="/govt-orders.html">Orders</a></li>
      </ul>

      <div class="nav-tools">
        <button class="tool-btn" onclick="openSearchModal()">Search <kbd style="font-family:var(--mono);">Ctrl+K</kbd></button>
      </div>
    </nav>

    <!-- Main Content -->
    <main style="max-width: 980px; margin: 0 auto; padding-top: 10px;">

      <!-- Breadcrumbs & Kicker -->
      <div class="kicker-muted" style="margin-bottom: 10px;">
        <a href="/" style="color:var(--ink-soft); text-decoration:none;">HOME</a> / 
        <a href="/topics/" style="color:var(--ink-soft); text-decoration:none;">TOPICS</a> / 
        <span style="color:var(--blueprint);">COMPLIANCE &amp; STATUTORY NOCS</span>
      </div>

      <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
        <span class="badge badge-clause">Reg. 2.2.11 (NOCs)</span>
        <span class="badge badge-clause">Reg. 3.1 (Restrictions)</span>
        <span class="badge badge-clause">Reg. 13.2 – 13.4</span>
        <span class="badge badge-status-done">Live Compliance Engine</span>
      </div>

      <h1 style="font-size:2.2rem; margin-bottom:12px; line-height:1.2;">
        Building Compliance, Statutory NOCs &amp; Approval Roadmap
      </h1>

      <p style="font-size:1.05rem; color:var(--ink-soft); line-height:1.6; margin-bottom:28px;">
        Determine which external clearances, technical certificates, and environmental NOCs your building legally requires under Maharashtra UDCPR-2020. Understand the exact <strong>statutory conditions that trigger them</strong>, the <strong>issuing departments</strong>, and the <strong>mandatory project lifecycle stage</strong> (Pre-Sanction, Plinth, Superstructure, or Final Occupancy).
      </p>

      <!-- SECTION 1: STATUTORY LIFECYCLE STAGES -->
      <section style="margin-bottom:32px;">
        <span class="kicker">01 // APPROVAL CHRONOLOGY</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">The 4 Chronological Approval Milestones (Reg. 2.6 – 2.9)</h2>
        <div class="panel-info">
          <p style="margin-bottom:14px;">
            Statutory compliance is not a single submission. Under UDCPR Chapter 2, building sanctions unfold across four legally enforceable checkpoints:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:12px;">
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="stage-badge stage-presanction" style="margin-bottom:6px;">Stage 1 • Pre-Sanction</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Commencement (CC)</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Ownership proof (Mojni &lt; 6 mos), site eligibility (Reg. 3.1), Provisional Fire NOC, Environmental Clearance, and Railway/Airport clearances prior to granting CC (Appendix D-1/D-2/D-3).</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="stage-badge stage-plinth" style="margin-bottom:6px;">Stage 2 • Ground Zero</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Plinth Check (App-G)</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Mandatory notice of completion up to plinth level under Reg. 2.8.3. Authority must inspect within 15 days before any vertical superstructure or slab work can commence.</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="stage-badge stage-superstructure" style="margin-bottom:6px;">Stage 3 • Superstructure</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Mid-Construction Audits</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Refuge floor provision at 24m+ (Reg. 9.29.2), 6.0m clear fire tender driveway (Reg. 6.2.3), dual plumbing lines installation, and half-yearly fire safety compliance.</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="stage-badge stage-oc" style="margin-bottom:6px;">Stage 4 • Handover</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Occupancy (OC • App-J)</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Final Fire NOC, Structural Stability (App-C), Rainwater Harvesting execution, STP water testing report, and Lift License. Crucially: occupation without OC is illegal under MRTP Sec 52.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 2: INTERACTIVE COMPLIANCE ROADMAP ENGINE -->
      <section style="margin-bottom:32px;">
        <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--ink); padding-bottom:6px; margin-bottom:14px;">
          <div>
            <span class="kicker">02 // INTERACTIVE WORKBENCH</span>
            <h2 style="font-size:1.35rem; margin:0;">Live Project Compliance &amp; NOC Matrix Engine</h2>
          </div>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REACTIVE STATUTORY SCANNER</span>
        </div>

        <div style="background:var(--paper-raised); border:1px solid var(--ink); padding:20px;">
          <!-- CONTROLS: PROJECT DNA -->
          <div style="margin-bottom:20px;">
            <span class="kicker" style="color:var(--blueprint);">STEP 1 // INPUT PROJECT PARAMETERS (PROJECT DNA)</span>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:16px; margin-top:8px;">
              <div class="calc-field">
                <label for="comp-height" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Building Height (H in meters)</label>
                <input type="number" id="comp-height" class="sheet-input" value="36" min="3" max="150" step="1">
                <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);" id="comp-height-desc">36m (G+11 Floors • High-Rise)</span>
              </div>

              <div class="calc-field">
                <label for="comp-plot-area" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Gross Plot Area (sq.m)</label>
                <input type="number" id="comp-plot-area" class="sheet-input" value="1800" min="50" max="200000" step="100">
                <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);" id="comp-plot-desc">0.18 Ha (Below 0.40 Ha ROS trigger)</span>
              </div>

              <div class="calc-field">
                <label for="comp-total-bua" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Total Built-Up Area BUA (sq.m)</label>
                <input type="number" id="comp-total-bua" class="sheet-input" value="4500" min="50" max="250000" step="250">
                <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);" id="comp-bua-desc">Below 20,000 sqm SEIAA trigger</span>
              </div>

              <div class="calc-field">
                <label for="comp-tenants" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Total Tenements / Units</label>
                <input type="number" id="comp-tenants" class="sheet-input" value="48" min="1" max="2000" step="4">
                <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);" id="comp-tenants-desc">Below 100 flats STP trigger</span>
              </div>

              <div class="calc-field" style="grid-column: 1 / -1;">
                <label for="comp-occupancy" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Occupancy Classification (Reg. 1.3)</label>
                <select id="comp-occupancy" class="sheet-input">
                  <option value="residential" selected>Residential Apartment Building</option>
                  <option value="commercial">Commercial / Retail Mall / Office Complex</option>
                  <option value="assembly">Assembly Building (Cinema, Auditorium, Marriage Hall &gt; 500 sqm)</option>
                  <option value="educational">Educational Building (School / College)</option>
                  <option value="hospital">Hospital / Medical Institution</option>
                  <option value="industrial">Industrial / Warehouse / Hazardous</option>
                </select>
              </div>
            </div>
          </div>

          <!-- SITE CONSTRAINTS & SENSITIVITIES (REG 3.1 & 2.2.11) -->
          <div style="background:var(--paper); border:1px solid var(--line-strong); padding:16px; margin-bottom:20px;">
            <span class="kicker" style="color:var(--amber);">STEP 2 // SITE CONSTRAINTS &amp; PROXIMITIES (REG. 3.1 &amp; 2.2.11)</span>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:10px; margin-top:10px; font-size:0.88rem;">
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-railway" style="accent-color:var(--blueprint);">
                <span>Near Railway Line (within 30m of track)</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-airport" style="accent-color:var(--blueprint);">
                <span>Within Airport Obstacle Funnel / CCZM</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-river" style="accent-color:var(--blueprint);">
                <span>Abutting River / Watercourse (Flood Lines)</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-defense" style="accent-color:var(--blueprint);">
                <span>Near Defence Establishment (Works of Defence Act)</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-ht-line" style="accent-color:var(--blueprint);">
                <span>Overhead High-Tension (HT) Electric Line</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-prison" style="accent-color:var(--blueprint);">
                <span>Near Prison Premises (within 150m)</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-heritage" style="accent-color:var(--blueprint);">
                <span>Listed Ancient Monument / Heritage Structure</span>
              </label>
              <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
                <input type="checkbox" id="check-trees" style="accent-color:var(--blueprint);" checked>
                <span>Existing Mature Trees requiring Felling</span>
              </label>
            </div>
          </div>

          <!-- FILTER BAR -->
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
            <div style="display:flex; gap:6px; flex-wrap:wrap;">
              <button class="filter-tab-btn active" id="flt-all" onclick="filterCompliance('all')">ALL COMPLIANCES (<span id="count-all">0</span>)</button>
              <button class="filter-tab-btn" id="flt-stage1" onclick="filterCompliance('stage1')">STAGE 1: PRE-SANCTION (<span id="count-stage1">0</span>)</button>
              <button class="filter-tab-btn" id="flt-stage2" onclick="filterCompliance('stage2')">STAGE 2: PLINTH (<span id="count-stage2">0</span>)</button>
              <button class="filter-tab-btn" id="flt-stage3" onclick="filterCompliance('stage3')">STAGE 3: SUPERSTRUCTURE (<span id="count-stage3">0</span>)</button>
              <button class="filter-tab-btn" id="flt-stage4" onclick="filterCompliance('stage4')">STAGE 4: OCCUPANCY (OC) (<span id="count-stage4">0</span>)</button>
            </div>
          </div>

          <!-- DYNAMIC COMPLIANCE CARDS CONTAINER -->
          <div id="compliance-cards-container">
            <!-- Populated dynamically via JS -->
          </div>

        </div>
      </section>

      <!-- SECTION 3: SUMMARY OF STATUTORY AUTHORITIES & MANDATORY APPENDICES -->
      <section style="margin-bottom:32px;">
        <span class="kicker">03 // STATUTORY CITATIONS</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Statutory Authorities &amp; Prescribed Appendices</h2>
        
        <div style="overflow-x:auto; margin-bottom:16px;">
          <table class="drawing-table">
            <thead>
              <tr>
                <th>Statutory Department / Officer</th>
                <th>Governing Regulation</th>
                <th>Nature of Clearance / Inspection</th>
                <th>Prescribed Appendix</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Chief Fire Officer (CFO)</strong></td>
                <td><span class="clause-ref">Reg. 2.2.11 &amp; Reg. 9.29</span></td>
                <td>Fire safety clearance for Special Buildings (&gt; 24m or Assembly &gt; 500 sqm)</td>
                <td style="font-family:var(--mono);">Provisional before CC; Final before OC</td>
              </tr>
              <tr>
                <td><strong>SEIAA / MoEFCC Environment Dept</strong></td>
                <td><span class="clause-ref">Reg. 2.2.11 (EIA 2006)</span></td>
                <td>Prior Environmental Clearance (EC) for BUA &ge; 20,000 sq.m</td>
                <td style="font-family:var(--mono);">EC Order before Ground Breaking</td>
              </tr>
              <tr>
                <td><strong>Licensed Structural Engineer</strong></td>
                <td><span class="clause-ref">Reg. 2.2.15 &amp; Reg. 12.1</span></td>
                <td>Design per NBC Part-6 (IS 1893 Seismic &amp; IS 456 Concrete)</td>
                <td style="font-family:var(--mono);">Appendix-C (Certificate of Stability)</td>
              </tr>
              <tr>
                <td><strong>Authority Town Planning Engineer</strong></td>
                <td><span class="clause-ref">Reg. 2.8.3</span></td>
                <td>Plinth level site inspection (15-day deemed sanction period)</td>
                <td style="font-family:var(--mono);">Appendix-G (Plinth Completion Notice)</td>
              </tr>
              <tr>
                <td><strong>Civil Aviation Authority (AAI)</strong></td>
                <td><span class="clause-ref">Reg. 2.2.11 &amp; Reg. 3.1.13</span></td>
                <td>Height clearance if penetrating Colour Coded Zoning Map (CCZM)</td>
                <td style="font-family:var(--mono);">NOCAS Online Certificate</td>
              </tr>
              <tr>
                <td><strong>Irrigation Department (Water Resources)</strong></td>
                <td><span class="clause-ref">Reg. 3.1.3</span></td>
                <td>Demarcation of Blue and Red Flood Lines on natural watercourses</td>
                <td style="font-family:var(--mono);">Certified River Flood Line Map</td>
              </tr>
              <tr>
                <td><strong>Tree Authority</strong></td>
                <td><span class="clause-ref">Reg. 2.2.4 &amp; Tree Act</span></td>
                <td>Permission to fell or transplant trees on building footprint</td>
                <td style="font-family:var(--mono);">Tree Officer Sanction &amp; Replanting Bond</td>
              </tr>
              <tr>
                <td><strong>Public Health / Environmental Officer</strong></td>
                <td><span class="clause-ref">Reg. 13.3 &amp; Reg. 13.4</span></td>
                <td>RWH execution certificate &amp; Grey Water STP testing every 6 months</td>
                <td style="font-family:var(--mono);">Lab Test Certificate &amp; Dual Piping Plan</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- SECTION 4: SCRUTINY WATCHOUTS -->
      <section style="margin-bottom:32px;">
        <span class="kicker">04 // SCRUTINY WATCHOUTS</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Top 5 Compliance Traps that Halt Construction &amp; OC</h2>
        <div class="panel-warning">
          <ul style="padding-left:18px; margin:0; display:flex; flex-direction:column; gap:10px; font-size:0.92rem; line-height:1.55;">
            <li>
              <strong>1. Starting Construction on Sites &ge; 20,000 sqm BUA without SEIAA EC:</strong> Under the Environment Protection Act and Reg. 2.2.11, commencing excavation or plinth work on a plot whose cumulative BUA reaches 20,000 sq.m without Prior Environmental Clearance constitutes a severe violation, leading to work stoppage orders and heavy National Green Tribunal (NGT) penalties.
            </li>
            <li>
              <strong>2. Pouring Slabs above Plinth without Appendix-G Plinth Inspection:</strong> Under Regulation 2.8.3, pouring upper floor columns without submitting the Appendix-G plinth notice (and awaiting the 15-day inspection period) renders the superstructure legally unauthorized.
            </li>
            <li>
              <strong>3. Failure to Color-Code Dual Plumbing Lines for Grey Water:</strong> Under Regulation 13.4.1(ii), building plans for layouts &ge; 10,000 sqm or buildings with &ge; 100 tenements must clearly show separate, distinct color-coded drainage and plumbing pipes for flushing and gardening water. Omitting this triggers plan rejection.
            </li>
            <li>
              <strong>4. Allowing Physical Occupation Before Receiving Appendix-J Occupancy Certificate (OC):</strong> Handing over possession or moving occupants into a building before the Authority issues the final Occupancy Certificate under Reg. 2.9 is a criminal offense under Section 52 of the MRTP Act, resulting in immediate disconnection of municipal water and electricity supplies.
            </li>
            <li>
              <strong>5. Ignoring 100m Prohibited Buffer Around Archaeological Monuments:</strong> Under Reg. 3.1.10 and the Ancient Monuments and Archaeological Sites and Remains Act, no construction of any nature is permissible within <strong>100 meters</strong> of a monument of national importance, and construction between 100m and 300m requires mandatory National Monuments Authority (NMA) clearance.
            </li>
          </ul>
        </div>
      </section>

      <!-- SECTION 5: KNOWLEDGE CHECK QUIZ -->
      <section style="margin-bottom:32px;">
        <span class="kicker">05 // VERIFICATION QUIZ</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Knowledge Check: Building Compliance &amp; Statutory NOCs</h2>
        <div class="quiz-container" id="comp-quiz-box"></div>
      </section>

    </main>

    <!-- Sheet Footer -->
    <footer class="sheet-footer">
      <div>UDCPR FROM SCRATCH • TOPIC 08: BUILDING COMPLIANCE &amp; STATUTORY NOCS</div>
      <div>DRAWING SHEET ARCHITECTURAL SPECIFICATION • MAHARASHTRA STATE</div>
    </footer>
  </div>

  <!-- Universal Search Modal -->
  <div class="search-modal-backdrop" id="search-modal-backdrop" onclick="if(event.target === this) closeSearchModal()">
    <div class="search-modal">
      <div class="search-modal-header">
        <span style="font-family:var(--mono); font-size:13px; font-weight:700;">SEARCH //</span>
        <input type="text" id="search-modal-input" class="search-modal-input" placeholder="Search clauses, compliance, NOCs..." autocomplete="off">
        <button onclick="closeSearchModal()" class="tool-btn" style="padding:2px 8px;">ESC</button>
      </div>
      <ul class="search-results-list" id="search-results-list"></ul>
    </div>
  </div>

  <script src="/js/app.js"></script>
  <script src="/js/search.js"></script>
  <script src="/js/quiz.js"></script>
  <script>
    let activeFilter = 'all';

    function filterCompliance(stage) {
      activeFilter = stage;
      document.querySelectorAll('.filter-tab-btn').forEach(btn => btn.classList.remove('active'));
      document.getElementById('flt-' + stage).classList.add('active');

      const cards = document.querySelectorAll('.compliance-card');
      cards.forEach(card => {
        if (stage === 'all') {
          card.style.display = 'block';
        } else {
          card.style.display = card.getAttribute('data-stage') === stage ? 'block' : 'none';
        }
      });
    }

    document.addEventListener('DOMContentLoaded', function () {
      const hEl = document.getElementById('comp-height');
      const plotEl = document.getElementById('comp-plot-area');
      const buaEl = document.getElementById('comp-total-bua');
      const tenEl = document.getElementById('comp-tenants');
      const occEl = document.getElementById('comp-occupancy');

      const chkRailway = document.getElementById('check-railway');
      const chkAirport = document.getElementById('check-airport');
      const chkRiver = document.getElementById('check-river');
      const chkDefense = document.getElementById('check-defense');
      const chkHtLine = document.getElementById('check-ht-line');
      const chkPrison = document.getElementById('check-prison');
      const chkHeritage = document.getElementById('check-heritage');
      const chkTrees = document.getElementById('check-trees');

      function scanCompliance() {
        const H = parseFloat(hEl.value) || 36;
        const plot = parseFloat(plotEl.value) || 1800;
        const bua = parseFloat(buaEl.value) || 4500;
        const tenements = parseInt(tenEl.value) || 48;
        const occ = occEl.value;

        // Descriptors
        const isSpecial = H > 24.0 || (H > 15.0) || (occ !== 'residential' && bua >= 500);
        document.getElementById('comp-height-desc').textContent = H.toFixed(1) + 'm (' + (H > 24 ? 'High-Rise' : (H > 15 ? 'Special Building' : 'Low-Rise')) + ')';
        document.getElementById('comp-plot-desc').textContent = (plot / 10000).toFixed(2) + ' Ha (' + (plot >= 4000 ? 'ROS Mandatory' : 'Below 0.40 Ha ROS') + ')';
        document.getElementById('comp-bua-desc').textContent = bua >= 20000 ? 'SEIAA Environment Clearance Mandatory' : 'Below 20,000 sqm SEIAA trigger';
        document.getElementById('comp-tenants-desc').textContent = tenements >= 100 ? 'STP Mandatory (≥ 100 tenements)' : 'Below 100 flats STP trigger';

        // COMPLIANCE DATABASE (Anchored strictly to ucpr_real.md)
        const compliances = [
          // STAGE 1: PRE-SANCTION
          {
            id: 'land-demarcation',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Land Ownership Verification & Mojni Demarcation Sheet',
            dept: 'Revenue Dept / City Survey Officer (CTSO)',
            clause: 'Reg. 2.2.1 & 2.2.2',
            triggered: true,
            condition: 'Universal: All proposals require certified 7/12 extract or Property Card issued within 6 months and official measurement (Mojni) map.',
            action: 'Submit certified Mojni map (1:500/1:1000) and title clearance certificate with initial notice (Appendix A-1/A-2).'
          },
          {
            id: 'fire-provisional',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Provisional Fire CFO No Objection Certificate (NOC)',
            dept: 'Chief Fire Officer (CFO) / Director of Fire Services',
            clause: 'Reg. 2.2.11 & Reg. 1.3(93)(xiv)',
            triggered: isSpecial,
            condition: isSpecial ? 'TRIGGERED: Building Height ' + H.toFixed(1) + 'm > 15m or Special Building occupancy under Reg. 1.3(93)(xiv).' : 'EXEMPT: Building height ≤ 15m and residential occupancy under 500 sqm floor plate.',
            action: 'Submit architectural schemes showing fire tender access, hydrant locations, and emergency staircase enclosure to Fire Dept before Commencement Certificate (CC).'
          },
          {
            id: 'env-clearance',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Prior Environmental Clearance (EC) from SEIAA',
            dept: 'State Environment Impact Assessment Authority (SEIAA) / MoEFCC',
            clause: 'Reg. 2.2.11 & EIA Notification 2006 (Item 8a)',
            triggered: bua >= 20000,
            condition: bua >= 20000 ? ('TRIGGERED: Total Built-Up Area BUA (' + bua.toLocaleString() + ' sqm) ≥ 20,000 sq.m threshold.') : 'EXEMPT: Total BUA (' + bua.toLocaleString() + ' sqm) is below the 20,000 sq.m national EIA threshold.',
            action: 'Obtain formal Environmental Clearance from SEIAA before commencing any physical construction, excavation, or tree felling on site.'
          },
          {
            id: 'tree-noc',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Tree Authority Clearance & Felling / Transplantation Permission',
            dept: 'Municipal Tree Authority / Forest Officer',
            clause: 'Reg. 2.2.4 & Maharashtra Tree Act',
            triggered: chkTrees.checked,
            condition: chkTrees.checked ? 'TRIGGERED: Mature trees exist on plot affecting the building footprint or fire driveway.' : 'EXEMPT: No existing mature trees affected on site.',
            action: 'Conduct botanical tree census, submit tree preservation plan, pay compensatory plantation deposit, and plant 2 trees for every 1 tree felled.'
          },
          {
            id: 'railway-noc',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Railway Administration No Objection Certificate (NOC)',
            dept: 'Central / Western / South East Central Railway',
            clause: 'Reg. 2.2.11 & Reg. 3.1.13',
            triggered: chkRailway.checked,
            condition: chkRailway.checked ? 'TRIGGERED: Plot boundary is located within 30.0 meters of railway land boundary.' : 'EXEMPT: Site is outside 30.0m railway buffer corridor.',
            action: 'Submit site plan with track offsets and structural stability verification to Railway Division DRM office before building permission.'
          },
          {
            id: 'airport-noc',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Civil Aviation Height Clearance (AAI NOCAS)',
            dept: 'Airports Authority of India (AAI) / MoCA',
            clause: 'Reg. 2.2.11 & Reg. 3.1.13',
            triggered: chkAirport.checked,
            condition: chkAirport.checked ? 'TRIGGERED: Site is located within the airport obstacle limitation surfaces / CCZM grid.' : 'EXEMPT: Site does not penetrate airport Color Coded Zoning Map.',
            action: 'Obtain online NOCAS elevation clearance certificate certifying AMSL (Above Mean Sea Level) building top height before building sanction.'
          },
          {
            id: 'river-flood',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'River Flood Lines (Blue & Red Line) Demarcation',
            dept: 'Water Resources (Irrigation) Department',
            clause: 'Reg. 3.1.3',
            triggered: chkRiver.checked,
            condition: chkRiver.checked ? 'TRIGGERED: Plot abuts a natural river, nallah, or watercourse shown on Development Plan.' : 'EXEMPT: Site does not abut natural watercourse.',
            action: 'Obtain Irrigation Dept certified plan. Area between river bank and Blue Line is strictly non-buildable; between Blue and Red Line allows restricted plinth.'
          },
          {
            id: 'defense-noc',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Defence Ministry Clearance (Works of Defence Act, 1903)',
            dept: 'Ministry of Defence (MoD) / Station Commander',
            clause: 'Reg. 3.1.11',
            triggered: chkDefense.checked,
            condition: chkDefense.checked ? 'TRIGGERED: Plot falls within notified security buffer of defence/ammunition depot.' : 'EXEMPT: Site outside military/defence notification zones.',
            action: 'Obtain NOC from local Military Station Commander. Restrictive security zones can be counted towards marginal open space under Reg. 3.1.11.'
          },
          {
            id: 'heritage-noc',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Heritage Conservation Committee (HCC) / ASI Permission',
            dept: 'Archaeological Survey of India (ASI) / State Heritage Committee',
            clause: 'Reg. 3.1.10 & Reg. 14.4',
            triggered: chkHeritage.checked,
            condition: chkHeritage.checked ? 'TRIGGERED: Site is near a listed Ancient Monument or inside a designated Heritage Precinct.' : 'EXEMPT: Site not near listed heritage structures.',
            action: 'Strict prohibition within 100m of national monument; regulated permission between 100m and 300m from National Monuments Authority (NMA).'
          },
          {
            id: 'ht-line-noc',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Electricity Transmission Clearance (Table No. 3 Clearance)',
            dept: 'MSEDCL / MSETCL / Power Distribution Utility',
            clause: 'Reg. 3.1.2 & Table No. 3',
            triggered: chkHtLine.checked,
            condition: chkHtLine.checked ? 'TRIGGERED: Overhead electric supply line passes across or adjacent to the plot.' : 'EXEMPT: No overhead high-tension line crossing plot.',
            action: 'Maintain statutory horizontal and vertical clearances from transmission lines per Table 3 (e.g., 2.5m vertical and 1.2m horizontal for up to 11kV lines; 3.7m vertical and 2.0m horizontal for 33kV lines).'
          },
          {
            id: 'prison-noc',
            stage: 'stage1',
            stageLabel: 'Stage 1 • Pre-Sanction',
            badgeClass: 'stage-presanction',
            title: 'Home Department Prison Perimeter Clearance',
            dept: 'Home Department Prison Committee',
            clause: 'Reg. 3.1.7',
            triggered: chkPrison.checked,
            condition: chkPrison.checked ? 'TRIGGERED: Site is within 150m of Central Prison, 100m of District Prison, or 50m of Sub-Prison.' : 'EXEMPT: Site outside prison security perimeter.',
            action: 'Obtain prior consent of the Home Department High-Level Committee before issuing development permission.'
          },

          // STAGE 2: PLINTH LEVEL INSPECTION
          {
            id: 'plinth-certificate',
            stage: 'stage2',
            stageLabel: 'Stage 2 • Ground Zero',
            badgeClass: 'stage-plinth',
            title: 'Notice of Completion up to Plinth Level (Appendix-G)',
            dept: 'Planning Authority Town Planning / Building Scrutiny Dept',
            clause: 'Reg. 2.8.3 & Appendix-G',
            triggered: true,
            condition: 'Universal: Mandatory for all buildings once foundation excavation and plinth casting reaches ground level.',
            action: 'Architect/Owner submits Appendix-G. Authority must inspect within 15 days. If no communication in 15 days, work can proceed (deemed plinth sanction).'
          },
          {
            id: 'structural-soil',
            stage: 'stage2',
            stageLabel: 'Stage 2 • Ground Zero',
            badgeClass: 'stage-plinth',
            title: 'Geotechnical Soil Investigation & Seismic Design Certificate',
            dept: 'Licensed Structural Engineer',
            clause: 'Reg. 2.2.15 & Reg. 12.1 (IS 1893)',
            triggered: true,
            condition: 'Universal: Structural design must comply with National Building Code Part-6, IS 1893 (Earthquake), and soil test report.',
            action: 'Submit soil bore-hole test report and foundation structural design proof-check before casting upper floor columns.'
          },

          // STAGE 3: SUPERSTRUCTURE EXECUTION
          {
            id: 'refuge-execution',
            stage: 'stage3',
            stageLabel: 'Stage 3 • Superstructure',
            badgeClass: 'stage-superstructure',
            title: 'Refuge Floor Execution & FSI Exemption Inspection',
            dept: 'Fire Department & Municipal Scrutiny Officer',
            clause: 'Reg. 9.29.2 & Reg. 6.3.3',
            triggered: H > 24.0,
            condition: H > 24.0 ? ('TRIGGERED: Building Height ' + H.toFixed(1) + 'm > 24.0m requires refuge floor at 24m and every 7th floor thereafter.') : 'EXEMPT: Building height ≤ 24.0m does not require refuge floor.',
            action: 'Cast refuge floor slab with 2-hour fire door, outward panic latch, and zero glass enclosure. 100% free of FSI.'
          },
          {
            id: 'fire-driveway-corridor',
            stage: 'stage3',
            stageLabel: 'Stage 3 • Superstructure',
            badgeClass: 'stage-superstructure',
            title: '6.0m Unobstructed Fire Tender Driveway Maintenance',
            dept: 'Chief Fire Officer (CFO)',
            clause: 'Reg. 6.2.3 & CFO Guidelines',
            triggered: isSpecial,
            condition: isSpecial ? 'TRIGGERED: Special Building requires 6.0m clear paved peripheral driveway capable of bearing 45 tonnes.' : 'EXEMPT: Low-rise residential building.',
            action: 'Ensure no permanent structures, ramps, or surface car parking encroach the 6.0m fire tender driveway around the building.'
          },
          {
            id: 'dual-plumbing',
            stage: 'stage3',
            stageLabel: 'Stage 3 • Superstructure',
            badgeClass: 'stage-superstructure',
            title: 'Dual Plumbing Lines Installation for Grey Water Reuse',
            dept: 'Municipal Plumbing Scrutiny Dept',
            clause: 'Reg. 13.4.1(ii)',
            triggered: (plot >= 10000) || (tenements >= 100) || (occ !== 'residential' && bua >= 1500),
            condition: ((plot >= 10000) || (tenements >= 100) || (occ !== 'residential' && bua >= 1500)) ? 'TRIGGERED: Scheme meets threshold for Grey Water Recycling (≥ 100 flats, ≥ 10,000 sqm plot, or commercial ≥ 1,500 sqm).' : 'EXEMPT: Scheme below grey water treatment thresholds.',
            action: 'Install color-coded distinct drainage and plumbing pipes for treated water used strictly for flushing and gardening.'
          },

          // STAGE 4: OCCUPANCY CERTIFICATE (FINAL OC)
          {
            id: 'fire-final',
            stage: 'stage4',
            stageLabel: 'Stage 4 • Final OC',
            badgeClass: 'stage-oc',
            title: 'Final Fire Safety Clearance Certificate (Final CFO NOC)',
            dept: 'Chief Fire Officer (CFO) / Fire Dept',
            clause: 'Reg. 9.29 & Maharashtra Fire Prevention Act',
            triggered: isSpecial,
            condition: isSpecial ? 'TRIGGERED: Special Building requiring physical operational inspection of fire hydrants, wet riser, and alarms.' : 'EXEMPT: Standard low-rise building without special fire NOC.',
            action: 'Conduct live water pump discharge test, verify refuge area, sprinkler system, and fire lift before requesting Occupancy Certificate.'
          },
          {
            id: 'rwh-completion',
            stage: 'stage4',
            stageLabel: 'Stage 4 • Final OC',
            badgeClass: 'stage-oc',
            title: 'Rain Water Harvesting (RWH) Execution Certificate',
            dept: 'Municipal Engineering / Environmental Dept',
            clause: 'Reg. 13.3',
            triggered: plot >= 500,
            condition: plot >= 500 ? ('TRIGGERED: Plot area (' + plot.toLocaleString() + ' sqm) ≥ 500 sq.m threshold.') : 'EXEMPT: Plot area is under 500 sq.m.',
            action: 'Submit photographical proof, filtration pit layout, and percolation well completion certificate. Municipal deposit refunded upon verification.'
          },
          {
            id: 'solar-swh-completion',
            stage: 'stage4',
            stageLabel: 'Stage 4 • Final OC',
            badgeClass: 'stage-oc',
            title: 'Solar Water Heating (SWH) / Rooftop Solar PV Installation',
            dept: 'Electrical / Renewable Energy Inspector',
            clause: 'Reg. 13.2',
            triggered: plot > 4000 || (occ === 'hospital' || occ === 'hotel'),
            condition: (plot > 4000 || (occ === 'hospital' || occ === 'hotel')) ? 'TRIGGERED: Plot > 4,000 sq.m or Hospital/Hotel occupancy requiring mandatory solar installation.' : 'EXEMPT: Plot ≤ 4,000 sq.m in residential zone.',
            action: 'Certify installation of solar water heating system or grid-tied rooftop solar photovoltaic system on open terrace area.'
          },
          {
            id: 'grey-water-stp-cert',
            stage: 'stage4',
            stageLabel: 'Stage 4 • Final OC',
            badgeClass: 'stage-oc',
            title: 'Grey Water Treatment Plant (STP) Commissioning & Lab Test',
            dept: 'Executive Health Officer (EHO) / MPCB',
            clause: 'Reg. 13.4.1(iv)',
            triggered: (plot >= 10000) || (tenements >= 100) || (occ !== 'residential' && bua >= 1500),
            condition: ((plot >= 10000) || (tenements >= 100) || (occ !== 'residential' && bua >= 1500)) ? 'TRIGGERED: Operational test of Grey Water Treatment Plant is mandatory prior to occupation.' : 'EXEMPT: Grey water treatment plant not required.',
            action: 'Submit chemical/biological laboratory test certificate of treated water to ward health officer. Maintain half-yearly testing commitment.'
          },
          {
            id: 'lift-license',
            stage: 'stage4',
            stageLabel: 'Stage 4 • Final OC',
            badgeClass: 'stage-oc',
            title: 'Lift Inspector Operational License (Form A & B)',
            dept: 'Industry, Energy & Labour Dept (Lift Inspectorate)',
            clause: 'Reg. 9.27 & Bombay Lifts Act',
            triggered: H > 15.0 || tenements >= 20,
            condition: (H > 15.0 || tenements >= 20) ? 'TRIGGERED: Passenger lifts installed for vertical transportation.' : 'EXEMPT: Low-rise walkup without elevator.',
            action: 'Obtain statutory operating license from Government Lift Inspector after speed governor and safety brake load tests.'
          },
          {
            id: 'structural-completion',
            stage: 'stage4',
            stageLabel: 'Stage 4 • Final OC',
            badgeClass: 'stage-oc',
            title: 'Final Structural Stability Certificate (Appendix-C)',
            dept: 'Registered Licensed Structural Engineer',
            clause: 'Reg. 2.2.15, Reg. 2.8.4 & Appendix-C',
            triggered: true,
            condition: 'Universal: Mandatory for all building types. Certifies structure executed per sanctioned design.',
            action: 'Structural engineer signs Appendix-C certifying as-built structural stability for seismic and gravity loads.'
          },
          {
            id: 'occupancy-grant',
            stage: 'stage4',
            stageLabel: 'Stage 4 • Final OC',
            badgeClass: 'stage-oc',
            title: 'Grant of Final Occupancy Certificate (Appendix-J)',
            dept: 'Planning Authority / Municipal Commissioner',
            clause: 'Reg. 2.8.4, Reg. 2.9 & Appendix-J',
            triggered: true,
            condition: 'Universal: Mandatory final legal clearance before any premises can be occupied or water connection released.',
            action: 'Submit Appendix-H completion notice. Authority inspects within 21 days and grants Appendix-J Occupancy Certificate.'
          }
        ];

        // RENDER CARDS & UPDATE COUNTS
        const container = document.getElementById('compliance-cards-container');
        let html = '';
        let counts = { all: 0, stage1: 0, stage2: 0, stage3: 0, stage4: 0 };

        compliances.forEach(c => {
          if (c.triggered) {
            counts.all++;
            counts[c.stage]++;
          }

          const cardClass = c.triggered ? 'compliance-card triggered' : 'compliance-card exempt';
          const triggerBadge = c.triggered ? '<span class="badge badge-status-done" style="margin-left:auto;">MANDATORY REQUIRED</span>' : '<span class="badge" style="background:#f1eee4; color:#5b5748; margin-left:auto;">NOT APPLICABLE</span>';

          html += `
            <div class="${cardClass}" data-stage="${c.stage}">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px; flex-wrap:wrap; gap:6px;">
                <span class="stage-badge ${c.badgeClass}">${c.stageLabel}</span>
                <span class="clause-ref">${c.clause}</span>
                <span class="dept-pill">${c.dept}</span>
                ${triggerBadge}
              </div>
              <h3 style="font-size:1.15rem; margin:6px 0 4px 0; color:var(--ink);">${c.title}</h3>
              <p style="font-size:0.86rem; color:var(--ink); margin:0 0 6px 0; line-height:1.45;"><strong>Trigger Rule:</strong> ${c.condition}</p>
              <div style="background:var(--paper); border:1px dashed var(--line-strong); padding:8px 10px; font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                <strong style="color:var(--blueprint);">STATUTORY ACTION:</strong> ${c.action}
              </div>
            </div>
          `;
        });

        container.innerHTML = html;

        // Update Counter Badges
        document.getElementById('count-all').textContent = counts.all;
        document.getElementById('count-stage1').textContent = counts.stage1;
        document.getElementById('count-stage2').textContent = counts.stage2;
        document.getElementById('count-stage3').textContent = counts.stage3;
        document.getElementById('count-stage4').textContent = counts.stage4;

        // Reapply filter
        filterCompliance(activeFilter);
      }

      // Event listeners
      [hEl, plotEl, buaEl, tenEl, occEl, chkRailway, chkAirport, chkRiver, chkDefense, chkHtLine, chkPrison, chkHeritage, chkTrees].forEach(el => {
        el.addEventListener('input', scanCompliance);
        el.addEventListener('change', scanCompliance);
      });

      scanCompliance();

      // Quiz Engine
      const compQuizQuestions = [
        {
          question: "Under Regulation 2.2.11 and Regulation 1.3(93)(xiv), which of the following buildings legally mandates a prior Fire Clearance (Provisional Fire NOC) from the Chief Fire Officer?",
          options: [
            "Any residential building with height exceeding 12.0 meters",
            "Any multi-storeyed building exceeding 24.0m in height, or educational/assembly/commercial buildings having built-up area ≥ 500 sq.m on any floor",
            "Only industrial chemical factories",
            "All buildings regardless of size or height"
          ],
          correctAnswer: 1,
          explanation: "Under Regulation 1.3(93)(xiv) and Reg. 2.2.11, Special Buildings—defined as buildings exceeding 24m in height, or educational, assembly, commercial, institutional, industrial buildings having BUA ≥ 500 sqm on any floor—mandate clearance from the Fire Officer."
        },
        {
          question: "At what project construction stage must the notice of completion up to plinth level (Appendix-G) be officially submitted under Regulation 2.8.3?",
          options: [
            "Before starting excavation",
            "Upon completion of foundation work up to plinth level, awaiting the Authority's 15-day inspection window",
            "After casting the top terrace slab",
            "At the time of Occupancy Certificate application"
          ],
          correctAnswer: 1,
          explanation: "Under Regulation 2.8.3, upon completing construction work up to the plinth level, the owner must submit Appendix-G notice. The Authority has 15 days to inspect before vertical columns and upper floor slabs can proceed."
        },
        {
          question: "What is the minimum plot area threshold that legally triggers mandatory Rain Water Harvesting (RWH) under Regulation 13.3?",
          options: [
            "200 sq.m",
            "500 sq.m",
            "1,000 sq.m",
            "4,000 sq.m"
          ],
          correctAnswer: 1,
          explanation: "Under Regulation 13.3, all new constructions, reconstructions, and additions on plots measuring not less than 500 sq.m must provide approved Rain Water Harvesting structures."
        },
        {
          question: "Under Regulation 13.4.2, what tenement threshold triggers the mandatory installation of a Grey Water Treatment and Recycling Plant for a Group Housing or multi-storeyed building?",
          options: [
            "25 or more tenements",
            "50 or more tenements",
            "100 or more tenements (150 or more for EWS/LIG)",
            "500 or more tenements"
          ],
          correctAnswer: 2,
          explanation: "Under Regulation 13.4.2, Group Housing schemes or multi-storeyed buildings with 100 or more tenements (or 150 or more tenements for EWS/LIG) must construct an in-situ Grey Water Recycling Plant with dual plumbing."
        }
      ];

      initQuiz('comp-quiz-box', compQuizQuestions, 'topic-building-compliance');
    });
  </script>
</body>
</html>
"""

def main():
    target_path = os.path.join(os.path.dirname(__file__), '..', 'topics', 'building-compliance-and-nocs.html')
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    print(f"✓ Created {target_path} with interactive statutory compliance & NOC engine.")

if __name__ == '__main__':
    main()
