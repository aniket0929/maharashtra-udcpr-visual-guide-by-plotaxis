"""
UDCPR Visual Guide - TOPIC 3 WORKBENCH GENERATOR
Builds topics/parking-and-circulation.html with dynamic interactive CAD stall layout plates,
basement ramp cross-section, tenement quota engine, and verification quiz.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Parking Standards, Bay Geometry &amp; Circulation Ramps | UDCPR Visual Guide</title>
  <meta name="description" content="Interactive Parking Calculator &amp; Layout Engineering Engine for Maharashtra UDCPR. Vehicle bay dimensions, tenement quotas, 10% visitor spaces, and basement ramp slope drawings.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/blueprint.css">
  <link rel="stylesheet" href="/css/components.css">
  <style>
    .svg-dimension-text {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      fill: var(--ink);
    }
    .svg-witness-line {
      stroke: var(--ink-soft);
      stroke-width: 1;
      stroke-dasharray: 2, 2;
    }
    .breakdown-card {
      border: 1px solid var(--line-strong);
      background: var(--paper);
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .tab-btn {
      background: var(--paper);
      border: 1px solid var(--ink);
      padding: 6px 14px;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      color: var(--ink);
    }
    .tab-btn.active {
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
      <strong>STATUTORY SPECIFICATION:</strong> UDCPR Chapter 8 (Reg. 8.1 &amp; 8.2), Table 8-A (Residential), Table 8-B (Commercial), and Basement Ramp Safety Engineering Standards.
    </div>

    <!-- Sheet Navigation -->
    <nav class="sheet-nav">
      <a href="/" class="brand-block">
        <span class="brand-stamp">PLOTAXIS</span>
        <div class="brand-title-group">
          <h1>UDCPR Visual Guide by Plotaxis</h1>
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
        <span style="color:var(--blueprint);">PARKING STANDARDS &amp; CIRCULATION</span>
      </div>

      <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
        <span class="badge badge-clause">Chapter 8 • Table 8-A &amp; 8-B</span>
        <span class="badge badge-clause">Reg. 8.1 (Stall Geometry)</span>
        <span class="badge badge-status-done">CAD Layout Engine</span>
      </div>

      <h1 style="font-size:2.2rem; margin-bottom:12px; line-height:1.2;">
        Off-Street Parking Standards, Stall CAD &amp; Circulation Ramps
      </h1>

      <p style="font-size:1.05rem; color:var(--ink-soft); line-height:1.6; margin-bottom:28px;">
        Design compliant vehicular circulation and off-street parking systems under Chapter 8. Calculate required car and scooter quotas, verify <strong>10% visitor parking additions</strong>, master <strong>2.5m &times; 5.0m stall layouts</strong>, and engineer <strong>1:10 basement ramps</strong> with smooth transition slopes.
      </p>

      <!-- SECTION 1: STATUTORY DIMENSIONAL ENVELOPES -->
      <section style="margin-bottom:32px;">
        <span class="kicker">01 // DIMENSIONAL ENVELOPES</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Statutory Vehicle Stall Envelopes (Reg. 8.1.1)</h2>
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:12px; margin-bottom:8px;">
          <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
            <span class="kicker" style="color:var(--blueprint);">FOUR-WHEELER (CAR)</span>
            <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:6px 0; color:var(--ink);">2.5m &times; 5.0m</div>
            <p style="font-size:0.82rem; color:var(--ink-soft);">Min area 12.5 sq.m. Clear driving aisle &ge; 3.0m (one-way) or 6.0m (two-way). Vertical clearance &ge; 2.40m.</p>
          </div>
          <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
            <span class="kicker" style="color:var(--amber);">TWO-WHEELER (SCOOTER)</span>
            <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:6px 0; color:var(--ink);">1.0m &times; 2.0m</div>
            <p style="font-size:0.82rem; color:var(--ink-soft);">Min area 2.0 sq.m. Provided at 2 spaces per residential tenement. Maneuvering aisle &ge; 1.50m.</p>
          </div>
          <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
            <span class="kicker" style="color:var(--ink);">BICYCLE</span>
            <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:6px 0; color:var(--ink);">0.7m &times; 1.4m</div>
            <p style="font-size:0.82rem; color:var(--ink-soft);">Min area 1.0 sq.m. Compulsory green transit amenity for commercial and institutional layouts.</p>
          </div>
          <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
            <span class="kicker" style="color:var(--teal);">FREIGHT / LOADING BAY</span>
            <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:6px 0; color:var(--ink);">3.75m &times; 7.5m</div>
            <p style="font-size:0.82rem; color:var(--ink-soft);">Min area 28.12 sq.m. Mandatory for commercial complexes &gt; 1,000 sqm. Vertical clearance &ge; 4.50m.</p>
          </div>
        </div>
      </section>

      <!-- SECTION 2: INTERACTIVE CAD STALL LAYOUT VIEWER -->
      <section style="margin-bottom:32px;">
        <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--ink); padding-bottom:6px; margin-bottom:14px;">
          <div>
            <span class="kicker">02 // ARCHITECTURAL CAD PLATE</span>
            <h2 style="font-size:1.35rem; margin:0;">Interactive Parking Stall CAD &amp; Circulation Aisle Plate</h2>
          </div>
          <div style="display:flex; gap:8px;">
            <button class="tab-btn active" id="btn-stall-90" onclick="switchStallView('90')">90° PERPENDICULAR</button>
            <button class="tab-btn" id="btn-stall-60" onclick="switchStallView('60')">60° ANGLED</button>
            <button class="tab-btn" id="btn-stall-bike" onclick="switchStallView('bike')">TWO-WHEELERS</button>
          </div>
        </div>

        <div class="blueprint-plate" style="margin-bottom:20px;">
          <div class="blueprint-plate-header">
            <span class="fig-number" id="plate-fig-number">FIG_004A // 90° PERPENDICULAR CAR STALLS</span>
            <span class="fig-title" id="plate-fig-title">Stall Geometry (2.50m &times; 5.00m) &amp; Mandatory 6.00m Two-Way Driveway Aisle</span>
          </div>

          <div class="plate-content" style="padding:16px 8px; overflow-x:auto;">
            <svg id="parking-cad-svg" viewBox="0 0 860 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="min-width:680px; font-family:var(--mono); display:block; margin:0 auto;">
              <defs>
                <marker id="parkArrowStart" markerWidth="6" markerHeight="6" refX="0" refY="3" orient="auto">
                  <path d="M 6 0 L 0 3 L 6 6 z" fill="#2B4C7E"/>
                </marker>
                <marker id="parkArrowEnd" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
                  <path d="M 0 0 L 6 3 L 0 6 z" fill="#2B4C7E"/>
                </marker>
                <pattern id="asphaltHatch" width="8" height="8" patternUnits="userSpaceOnUse">
                  <circle cx="4" cy="4" r="0.8" fill="#5B5748" opacity="0.2"/>
                </pattern>
              </defs>

              <!-- CAD Plate Paper -->
              <rect width="860" height="360" fill="#FAF8F2"/>

              <!-- DYNAMIC CONTENT GROUP -->
              <g id="dynamic-stall-group">
                <!-- Will be dynamically populated via JS -->
              </g>
            </svg>
          </div>

          <div class="plate-caption" id="plate-caption-text">
            FIG_004A: Perpendicular 90-degree parking stall dimensions (2.50m &times; 5.00m) with 6.0m central two-way circulation aisle, end curb radii, and wheel-stop setbacks under Regulation 8.1.
          </div>
        </div>
      </section>

      <!-- SECTION 3: BASEMENT RAMP ENGINEERING SECTION -->
      <section style="margin-bottom:32px;">
        <span class="kicker">03 // SECTIONAL RAMP GEOMETRY</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Basement Access Ramp Engineering (1:10 Max Slope &amp; 1:20 Transitions)</h2>
        <div class="blueprint-plate">
          <div class="blueprint-plate-header">
            <span class="fig-number">FIG_004B // VEHICULAR RAMP PROFILE</span>
            <span class="fig-title">Gradient Envelope: 1:10 Main Incline, 1:20 Break-Over Transitions &amp; 2.40m Headroom</span>
          </div>

          <div class="plate-content" style="padding:16px 8px; overflow-x:auto;">
            <svg viewBox="0 0 860 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="min-width:680px; font-family:var(--mono); display:block; margin:0 auto;">
              <defs>
                <marker id="rampArrow" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
                  <path d="M 0 0 L 6 3 L 0 6 z" fill="#2B4C7E"/>
                </marker>
              </defs>

              <rect width="860" height="300" fill="#FAF8F2"/>

              <!-- Ground Level Surface (Level 0) -->
              <line x1="40" y1="90" x2="220" y2="90" stroke="#181D24" stroke-width="2.5"/>
              <text x="50" y="80" fill="#181D24" font-size="11" font-weight="700">GROUND PLINTH ± 0.00m</text>

              <!-- Transition Slope Top (1:20 for 3.0m length) -->
              <line x1="220" y1="90" x2="300" y2="105" stroke="#DD7A0E" stroke-width="2.5"/>
              <text x="225" y="125" fill="#DD7A0E" font-size="9" font-weight="700">1:20 TRANSITION (3m)</text>

              <!-- Main Incline (1:10 Slope for 3.0m basement drop) -->
              <line x1="300" y1="105" x2="600" y2="225" stroke="#2B4C7E" stroke-width="3"/>
              <text x="410" y="150" fill="#2B4C7E" font-size="12" font-weight="700">1:10 (10%) MAIN INCLINE</text>
              <text x="410" y="170" fill="#5B5748" font-size="10">Length = 30.0m for 3.0m Drop</text>

              <!-- Transition Slope Bottom (1:20 for 3.0m length) -->
              <line x1="600" y1="225" x2="680" y2="240" stroke="#DD7A0E" stroke-width="2.5"/>
              <text x="610" y="215" fill="#DD7A0E" font-size="9" font-weight="700">1:20 TRANSITION (3m)</text>

              <!-- Basement Level Surface (Level -1) -->
              <line x1="680" y1="240" x2="820" y2="240" stroke="#181D24" stroke-width="2.5"/>
              <text x="700" y="260" fill="#181D24" font-size="11" font-weight="700">BASEMENT LEVEL -3.00m</text>

              <!-- Headroom Clearance Dimension Line (2.40m Min) -->
              <line x1="450" y1="165" x2="450" y2="75" stroke="#2B4C7E" stroke-width="1.5" marker-start="url(#cadSecArrowStart)" marker-end="url(#cadSecArrowEnd)"/>
              <line x1="440" y1="75" x2="460" y2="75" stroke="#2B4C7E" stroke-width="1.5"/>
              <text x="460" y="120" fill="#2B4C7E" font-size="10" font-weight="700">CLEAR HEADROOM &ge; 2.40m</text>

              <!-- Turning Radius Callout Box -->
              <rect x="50" y="160" width="220" height="90" fill="#FAF8F2" stroke="#181D24" stroke-width="1.2"/>
              <text x="60" y="180" fill="#5B5748" font-size="9" font-weight="700">CURVED RAMP RADIUS (REG. 8.2):</text>
              <text x="60" y="200" fill="#2B4C7E" font-size="12" font-weight="700">Min 9.0m Inner Turning Radius</text>
              <text x="60" y="218" fill="#181D24" font-size="10">Outer Radius: 15.0m (Two-Way 6m width)</text>
              <text x="60" y="235" fill="#DD7A0E" font-size="10" font-weight="700">Max Slope: 1:8 (12.5% for Curved)</text>
            </svg>
          </div>

          <div class="plate-caption">
            FIG_004B: Longitudinal section of basement vehicular ramp showing 1:10 main incline, 1:20 break-over transition slopes, 2.40m clear vertical headroom, and curved ramp radius parameters.
          </div>
        </div>
      </section>

      <!-- SECTION 4: INTERACTIVE APARTMENT & COMMERCIAL QUOTA ENGINE -->
      <section style="margin-bottom:32px;">
        <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--ink); padding-bottom:6px; margin-bottom:14px;">
          <div>
            <span class="kicker">04 // INTERACTIVE CALCULATOR</span>
            <h2 style="font-size:1.35rem; margin:0;">Statutory Parking Quota Calculator (Tables 8-A &amp; 8-B)</h2>
          </div>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">LIVE STATUTORY ENGINE</span>
        </div>

        <div style="background:var(--paper-raised); border:1px solid var(--ink); padding:20px;">
          <!-- Inputs Grid -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:16px; margin-bottom:20px;">
            <div class="calc-field">
              <label for="units-45" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Flats &le; 45 sq.m (1BHK)</label>
              <input type="number" id="units-45" class="sheet-input" value="40" min="0" step="1">
              <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);">1 Car per 4 flats</span>
            </div>

            <div class="calc-field">
              <label for="units-60" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Flats 45 to &le; 60 sq.m (2BHK)</label>
              <input type="number" id="units-60" class="sheet-input" value="60" min="0" step="1">
              <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);">1 Car per 2 flats</span>
            </div>

            <div class="calc-field">
              <label for="units-100" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Flats 60 to &le; 100 sq.m (3BHK)</label>
              <input type="number" id="units-100" class="sheet-input" value="30" min="0" step="1">
              <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);">1 Car per flat</span>
            </div>

            <div class="calc-field">
              <label for="comm-carpet" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Commercial Carpet (sq.m)</label>
              <input type="number" id="comm-carpet" class="sheet-input" value="500" min="0" step="50">
              <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);">1 Car per 100 sq.m</span>
            </div>
          </div>

          <!-- SUMMARY BREAKDOWN METRICS -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--blueprint);">1. RESIDENTIAL CARS</span>
                <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:4px 0;" id="calc-res-cars">70 Bays</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                Base Residential Requirement
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--amber);">2. VISITOR CAR PARKING (+10%)</span>
                <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:4px 0; color:var(--amber);" id="calc-visitor-cars">8 Bays</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                Mandatory under Reg. 8.1
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--ink);">3. TWO-WHEELERS (SCOOTERS)</span>
                <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:4px 0;" id="calc-scooters">272 Bays</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                2 spaces per flat + comm
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--teal);">4. EV CHARGING BAYS (20% MIN)</span>
                <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:4px 0; color:var(--teal);" id="calc-ev-bays">17 Bays</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                Equipped with EV conduit points
              </div>
            </div>
          </div>

          <!-- TOTAL PARKING STRIP -->
          <div style="background:var(--paper); border:2px solid var(--ink); padding:16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
            <div>
              <span class="kicker" style="color:var(--blueprint);">STATUTORY PARKING TOTAL</span>
              <div style="font-family:var(--disp); font-size:1.8rem; font-weight:700; color:var(--ink);" id="calc-grand-cars">83 Four-Wheeler Stalls Required</div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft); margin-top:2px;" id="calc-total-area-needed">
                Approx. 2,075 sq.m parking footprint (including 6.0m driveways @ 25 sqm / car).
              </div>
            </div>

            <div style="text-align:right;">
              <span class="kicker-muted">LOADING DOCKS REQUIRED</span>
              <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; color:var(--amber);" id="calc-loading-bays">1 Freight Bay (3.75 &times; 7.5m)</div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                Mandatory for commercial &gt; 500 sqm
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- SECTION 5: SCRUTINY WATCHOUTS -->
      <section style="margin-bottom:32px;">
        <span class="kicker">05 // SCRUTINY WATCHOUTS</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Top 5 Parking Layout Mistakes Causing Sanction Rejection</h2>
        <div class="panel-warning">
          <ul style="padding-left:18px; margin:0; display:flex; flex-direction:column; gap:10px; font-size:0.92rem; line-height:1.55;">
            <li>
              <strong>1. Providing Tandem / Dependent Stacks for Visitor Parking:</strong> Under Reg. 8.1, visitor parking must be 100% independent. Placing visitor cars in mechanical stack parking or tandem spots where one car blocks another is an automatic ground for rejection.
            </li>
            <li>
              <strong>2. Driveway Aisle Narrower than 6.0m for Two-Way Circulation:</strong> When two rows of 90-degree parking face each other, the central driving aisle must measure a <strong>minimum clear width of 6.00 meters</strong>. Reducing this to 4.5m or 5.0m triggers plan revision.
            </li>
            <li>
              <strong>3. Failure to Include Transition Slopes on Basement Ramps:</strong> Designing a straight 1:10 ramp without the <strong>3.0m length of 1:20 transition slope</strong> at the top plinth and bottom basement slab results in car underbodies scraping the concrete crest.
            </li>
            <li>
              <strong>4. Placing Car Parking Bays Inside the 6.0m Fire Tender Path:</strong> Surface parking bays cannot overlap the 6.0m clear fire tender driveway required for high-rise buildings (Reg. 6.2.3).
            </li>
            <li>
              <strong>5. Omitting Mandatory EV Charging Infrastructure:</strong> Under recent state government green directives, at least <strong>20% of all sanctioned parking bays</strong> must be pre-wired with dedicated electrical conduits and distribution boards for Electric Vehicle (EV) chargers.
            </li>
          </ul>
        </div>
      </section>

      <!-- SECTION 6: VERIFICATION QUIZ -->
      <section style="margin-bottom:32px;">
        <span class="kicker">06 // VERIFICATION QUIZ</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Knowledge Check: Parking Standards &amp; Circulation</h2>
        <div class="quiz-container" id="parking-quiz-box"></div>
      </section>

    </main>

    <!-- Sheet Footer -->
    <footer class="sheet-footer">
      <div>UDCPR Visual Guide • TOPIC 03: PARKING STANDARDS &amp; CIRCULATION RAMPS</div>
      <div>DRAWING SHEET ARCHITECTURAL SPECIFICATION • MAHARASHTRA STATE</div>
    </footer>
  </div>

  <!-- Universal Search Modal -->
  <div class="search-modal-backdrop" id="search-modal-backdrop" onclick="if(event.target === this) closeSearchModal()">
    <div class="search-modal">
      <div class="search-modal-header">
        <span style="font-family:var(--mono); font-size:13px; font-weight:700;">SEARCH //</span>
        <input type="text" id="search-modal-input" class="search-modal-input" placeholder="Search clauses, topics, formulas..." autocomplete="off">
        <button onclick="closeSearchModal()" class="tool-btn" style="padding:2px 8px;">ESC</button>
      </div>
      <ul class="search-results-list" id="search-results-list"></ul>
    </div>
  </div>

  <script src="/js/app.js"></script>
  <script src="/js/search.js"></script>
  <script src="/js/quiz.js"></script>
  <script>
    // Tabbed SVG Drawing Switcher
    function switchStallView(type) {
      document.getElementById('btn-stall-90').classList.remove('active');
      document.getElementById('btn-stall-60').classList.remove('active');
      document.getElementById('btn-stall-bike').classList.remove('active');

      const g = document.getElementById('dynamic-stall-group');
      const figNum = document.getElementById('plate-fig-number');
      const figTitle = document.getElementById('plate-fig-title');
      const capText = document.getElementById('plate-caption-text');

      if (type === '90') {
        document.getElementById('btn-stall-90').classList.add('active');
        figNum.textContent = 'FIG_004A // 90° PERPENDICULAR CAR STALLS';
        figTitle.textContent = 'Stall Geometry (2.50m × 5.00m) & Mandatory 6.00m Two-Way Driveway Aisle';
        capText.textContent = 'FIG_004A: Perpendicular 90-degree parking stall dimensions (2.50m × 5.00m) with 6.0m central two-way circulation aisle, end curb radii, and wheel-stop setbacks under Regulation 8.1.';

        g.innerHTML = `
          <!-- Top Row of Stalls (3 bays) -->
          <rect x="180" y="40" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
          <line x1="280" y1="40" x2="280" y2="130" stroke="#2B4C7E" stroke-width="1.8"/>
          <rect x="280" y="40" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
          <line x1="380" y1="40" x2="380" y2="130" stroke="#2B4C7E" stroke-width="1.8"/>
          <rect x="380" y="40" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
          <line x1="480" y1="40" x2="480" y2="130" stroke="#2B4C7E" stroke-width="1.8"/>
          <rect x="480" y="40" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>

          <!-- Stall text & wheel stops -->
          <text x="210" y="85" fill="#2B4C7E" font-size="12" font-weight="700">BAY 01</text>
          <text x="310" y="85" fill="#2B4C7E" font-size="12" font-weight="700">BAY 02</text>
          <text x="410" y="85" fill="#2B4C7E" font-size="12" font-weight="700">BAY 03</text>
          <text x="510" y="85" fill="#2B4C7E" font-size="12" font-weight="700">BAY 04</text>

          <rect x="200" y="50" width="60" height="8" fill="#5B5748"/>
          <rect x="300" y="50" width="60" height="8" fill="#5B5748"/>
          <rect x="400" y="50" width="60" height="8" fill="#5B5748"/>
          <rect x="500" y="50" width="60" height="8" fill="#5B5748"/>

          <!-- Central Driveway Aisle (6.0m width) -->
          <rect x="180" y="130" width="400" height="100" fill="#EAE5D7" stroke="#181D24" stroke-width="1.2"/>
          <line x1="180" y1="180" x2="580" y2="180" stroke="#DD7A0E" stroke-width="1.5" stroke-dasharray="8,5"/>
          <text x="300" y="172" fill="#181D24" font-size="12" font-weight="700">TWO-WAY CIRCULATION AISLE: 6.00m</text>
          <text x="345" y="195" fill="#5B5748" font-size="10">Minimum Turning Clearway</text>

          <!-- Bottom Row of Stalls (3 bays) -->
          <rect x="180" y="230" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
          <rect x="280" y="230" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
          <rect x="380" y="230" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
          <rect x="480" y="230" width="100" height="90" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>

          <text x="210" y="280" fill="#2B4C7E" font-size="12" font-weight="700">BAY 05</text>
          <text x="310" y="280" fill="#2B4C7E" font-size="12" font-weight="700">BAY 06</text>
          <text x="410" y="280" fill="#2B4C7E" font-size="12" font-weight="700">BAY 07</text>
          <text x="510" y="280" fill="#2B4C7E" font-size="12" font-weight="700">BAY 08</text>

          <rect x="200" y="302" width="60" height="8" fill="#5B5748"/>
          <rect x="300" y="302" width="60" height="8" fill="#5B5748"/>
          <rect x="400" y="302" width="60" height="8" fill="#5B5748"/>
          <rect x="500" y="302" width="60" height="8" fill="#5B5748"/>

          <!-- Dimension Lines -->
          <!-- Stall Width: 2.50m -->
          <line x1="180" y1="25" x2="280" y2="25" stroke="#2B4C7E" stroke-width="1.5" marker-start="url(#parkArrowStart)" marker-end="url(#parkArrowEnd)"/>
          <text x="210" y="18" fill="#2B4C7E" font-size="11" font-weight="700">WIDTH: 2.50m</text>

          <!-- Stall Depth: 5.00m -->
          <line x1="160" y1="40" x2="160" y2="130" stroke="#2B4C7E" stroke-width="1.5" marker-start="url(#parkArrowStart)" marker-end="url(#parkArrowEnd)"/>
          <text x="90" y="90" fill="#2B4C7E" font-size="11" font-weight="700">DEPTH: 5.00m</text>

          <!-- Aisle Width: 6.00m -->
          <line x1="600" y1="130" x2="600" y2="230" stroke="#181D24" stroke-width="1.8" marker-start="url(#parkArrowStart)" marker-end="url(#parkArrowEnd)"/>
          <text x="615" y="185" fill="#181D24" font-size="12" font-weight="700">AISLE: 6.00m</text>
        `;
      } else if (type === '60') {
        document.getElementById('btn-stall-60').classList.add('active');
        figNum.textContent = 'FIG_004B // 60° ANGLED HERRINGBONE STALLS';
        figTitle.textContent = '60-Degree Angled Stall (2.50m Width) & Compact 4.50m One-Way Driving Aisle';
        capText.textContent = 'FIG_004B: Angled 60-degree parking layout under Regulation 8.1. Reduces required drive aisle width from 6.0m to 4.50m for efficient one-way basement circulation.';

        g.innerHTML = `
          <!-- Angled Stalls Path -->
          <g transform="translate(180, 50)">
            <!-- Angled stall 1 -->
            <polygon points="0,0 80,0 130,85 50,85" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
            <text x="45" y="50" fill="#2B4C7E" font-size="11" font-weight="700">BAY 01 (60°)</text>

            <!-- Angled stall 2 -->
            <polygon points="80,0 160,0 210,85 130,85" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
            <text x="125" y="50" fill="#2B4C7E" font-size="11" font-weight="700">BAY 02</text>

            <!-- Angled stall 3 -->
            <polygon points="160,0 240,0 290,85 210,85" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
            <text x="205" y="50" fill="#2B4C7E" font-size="11" font-weight="700">BAY 03</text>

            <!-- Angled stall 4 -->
            <polygon points="240,0 320,0 370,85 290,85" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.8"/>
            <text x="285" y="50" fill="#2B4C7E" font-size="11" font-weight="700">BAY 04</text>
          </g>

          <!-- 4.50m One-Way Aisle -->
          <rect x="180" y="135" width="450" height="75" fill="#EAE5D7" stroke="#181D24" stroke-width="1.2"/>
          <text x="270" y="178" fill="#181D24" font-size="12" font-weight="700">ONE-WAY CIRCULATION AISLE: 4.50m</text>
          <!-- One way arrow -->
          <line x1="220" y1="172" x2="250" y2="172" stroke="#DD7A0E" stroke-width="2.5" marker-end="url(#parkArrowEnd)"/>

          <!-- Callout -->
          <rect x="660" y="80" width="180" height="130" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.5"/>
          <text x="670" y="105" fill="#2B4C7E" font-size="11" font-weight="700">60° EFFICIENCY GAINS:</text>
          <text x="670" y="130" fill="#181D24" font-size="10">• Aisle width: 4.50m</text>
          <text x="670" y="150" fill="#181D24" font-size="10">• Easier entry angle</text>
          <text x="670" y="170" fill="#181D24" font-size="10">• One-way loop required</text>
          <text x="670" y="190" fill="#DD7A0E" font-size="10" font-weight="700">• 15% space saving</text>
        `;
      } else if (type === 'bike') {
        document.getElementById('btn-stall-bike').classList.add('active');
        figNum.textContent = 'FIG_004C // TWO-WHEELER (SCOOTER) CLUSTERS';
        figTitle.textContent = 'Scooter Bay Geometry (1.00m × 2.00m) with 1.50m Pedestrian Maneuvering Aisle';
        capText.textContent = 'FIG_004C: Two-wheeler parking clusters under Table 8-A. Each bay measures 1.0m × 2.0m (2.0 sq.m) with 1.50m central access pathway.';

        g.innerHTML = `
          <!-- Scooter Bay Cluster -->
          <g transform="translate(140, 50)">
            <!-- 8 Scooter Bays Top -->
            ${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `
              <rect x="${i * 50}" y="0" width="50" height="80" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.2"/>
              <text x="${i * 50 + 10}" y="45" fill="#5B5748" font-size="9" transform="rotate(-90 ${i * 50 + 15} 45)">2-WHEELER</text>
            `).join('')}

            <!-- 1.50m Maneuvering Aisle -->
            <rect x="0" y="80" width="400" height="60" fill="#EAE5D7" stroke="#181D24" stroke-width="1"/>
            <text x="100" y="115" fill="#181D24" font-size="11" font-weight="700">1.50m PEDESTRIAN ACCESS AISLE</text>

            <!-- 8 Scooter Bays Bottom -->
            ${[0, 1, 2, 3, 4, 5, 6, 7].map(i => `
              <rect x="${i * 50}" y="140" width="50" height="80" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.2"/>
              <text x="${i * 50 + 10}" y="185" fill="#5B5748" font-size="9" transform="rotate(-90 ${i * 50 + 15} 185)">2-WHEELER</text>
            `).join('')}
          </g>

          <!-- Dimension Lines -->
          <line x1="140" y1="35" x2="190" y2="35" stroke="#2B4C7E" stroke-width="1.2" marker-start="url(#parkArrowStart)" marker-end="url(#parkArrowEnd)"/>
          <text x="145" y="28" fill="#2B4C7E" font-size="9" font-weight="700">WIDTH: 1.0m</text>

          <line x1="120" y1="50" x2="120" y2="130" stroke="#2B4C7E" stroke-width="1.2" marker-start="url(#parkArrowStart)" marker-end="url(#parkArrowEnd)"/>
          <text x="60" y="95" fill="#2B4C7E" font-size="9" font-weight="700">LENGTH: 2.0m</text>
        `;
      }
    }

    document.addEventListener('DOMContentLoaded', function () {
      switchStallView('90');

      // Calculator Elements
      const u45El = document.getElementById('units-45');
      const u60El = document.getElementById('units-60');
      const u100El = document.getElementById('units-100');
      const commEl = document.getElementById('comm-carpet');

      function updateParkingQuota() {
        const n45 = parseInt(u45El.value) || 0;
        const n60 = parseInt(u60El.value) || 0;
        const n100 = parseInt(u100El.value) || 0;
        const comm = parseFloat(commEl.value) || 0;

        // Table 8-A Residential Rules
        // <= 45 sqm: 1 car per 4 tenements
        const cars45 = Math.ceil(n45 / 4);
        // 45 to 60 sqm: 1 car per 2 tenements
        const cars60 = Math.ceil(n60 / 2);
        // > 60 to 100 sqm: 1 car per tenement
        const cars100 = n100 * 1;

        const resCarsBase = cars45 + cars60 + cars100;

        // Table 8-B Commercial: 1 car per 100 sq.m
        const commCars = Math.ceil(comm / 100);

        const totalBaseCars = resCarsBase + commCars;

        // 10% Visitor Parking Addition (Mandatory under Reg 8.1)
        const visitorCars = Math.ceil(totalBaseCars * 0.10);
        const grandTotalCars = totalBaseCars + visitorCars;

        // Two-Wheelers: 2 per tenement + 1 per 40 sqm commercial
        const scootersRes = (n45 + n60 + n100) * 2;
        const scootersComm = Math.ceil(comm / 40);
        const totalScooters = scootersRes + scootersComm;

        // EV Charging Bays: 20% of total car bays (Reg 8.1.3)
        const evBays = Math.ceil(grandTotalCars * 0.20);

        // Loading BUA: 1 dock per 500 sqm commercial
        const loadingBays = comm > 0 ? Math.max(1, Math.floor(comm / 500)) : 0;

        // Approx area needed: ~25 sq.m per car stall including driveway allocation
        const totalAreaNeeded = grandTotalCars * 25 + totalScooters * 3.5;

        // Update Readouts
        document.getElementById('calc-res-cars').textContent = resCarsBase + ' Bays';
        document.getElementById('calc-visitor-cars').textContent = visitorCars + ' Bays';
        document.getElementById('calc-scooters').textContent = totalScooters + ' Bays';
        document.getElementById('calc-ev-bays').textContent = evBays + ' Bays';
        document.getElementById('calc-grand-cars').textContent = grandTotalCars + ' Four-Wheeler Stalls Required';
        document.getElementById('calc-total-area-needed').textContent = 'Estimated parking footprint: ~' + totalAreaNeeded.toLocaleString('en-IN') + ' sq.m (including 6.0m driveways & maneuvering space).';
        document.getElementById('calc-loading-bays').textContent = loadingBays > 0 ? (loadingBays + ' Freight Bay(s) [3.75 × 7.5m]') : 'None Required';
      }

      u45El.addEventListener('input', updateParkingQuota);
      u60El.addEventListener('input', updateParkingQuota);
      u100El.addEventListener('input', updateParkingQuota);
      commEl.addEventListener('input', updateParkingQuota);
      updateParkingQuota();

      // Quiz Engine
      const parkingQuizQuestions = [
        {
          question: "Under Regulation 8.1.1, what are the minimum statutory dimensions of an off-street four-wheeler (car) parking stall?",
          options: [
            "2.00m × 4.50m",
            "2.50m × 5.00m",
            "3.00m × 6.00m",
            "2.20m × 4.80m"
          ],
          correctAnswer: 1,
          explanation: "Under Regulation 8.1.1 of UDCPR, the minimum size of an off-street car parking bay is strictly 2.50 meters in width by 5.00 meters in length (12.50 sq.m)."
        },
        {
          question: "What is the maximum permissible slope (gradient) for a straight vehicular ramp leading to a basement under Regulation 8.2?",
          options: [
            "1:5 (20%)",
            "1:8 (12.5%)",
            "1:10 (10%)",
            "1:15 (6.67%)"
          ],
          correctAnswer: 2,
          explanation: "Under Regulation 8.2, straight vehicular ramps to basements must have a slope not exceeding 1:10 (10%), provided with a 1:20 transition slope for a length of 3.0m at the top and bottom."
        },
        {
          question: "Can visitor parking bays be provided in mechanical dependent stack parking systems?",
          options: [
            "Yes, if signage is clearly posted",
            "No, visitor parking must be 100% independent and easily accessible",
            "Yes, with special Municipal Commissioner permission",
            "Only in commercial shopping malls"
          ],
          correctAnswer: 1,
          explanation: "Under Regulation 8.1, visitor parking must always be 100% independent and unobstructed so visitors can park and exit without requiring another vehicle to be moved."
        }
      ];

      initQuiz('parking-quiz-box', parkingQuizQuestions, 'topic-parking-standards');
    });
  </script>
</body>
</html>
"""

def main():
    target_path = os.path.join(os.path.dirname(__file__), '..', 'topics', 'parking-and-circulation.html')
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    print(f"✓ Rebuilt {target_path} with dynamic interactive CAD stall layout engine.")

if __name__ == '__main__':
    main()
