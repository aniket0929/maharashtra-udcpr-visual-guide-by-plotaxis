"""
UDCPR FROM SCRATCH - TOPIC 7 WORKBENCH GENERATOR
Builds topics/redevelopment-navigator.html with interactive CAD redevelopment scheme comparison,
feasibility calculator (SRS 1:R, URS Table 14-X, TOD FSI 4.00), and verification quiz.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Redevelopment &amp; Special Schemes Navigator | UDCPR from Scratch</title>
  <meta name="description" content="Master Maharashtra redevelopment regulations under UDCPR Chapter 14: Slum Rehabilitation (SRS 1:R formula), Cluster Redevelopment (URS Table 14-X), and Transit-Oriented Development (TOD FSI 4.00).">
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
    .breakdown-card {
      border: 1px solid var(--line-strong);
      background: var(--paper);
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .scheme-tab-btn {
      background: var(--paper);
      border: 1px solid var(--ink);
      padding: 6px 14px;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
      color: var(--ink);
    }
    .scheme-tab-btn.active {
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
      <strong>STATUTORY SPECIFICATION:</strong> Reg. 14.5 (Slum Rehabilitation), Reg. 14.6 (Cluster Redevelopment), Reg. 14.2 (TOD), and Tables 14-T, 14-X of Maharashtra UDCPR-2020.
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
        <span style="color:var(--blueprint);">REDEVELOPMENT &amp; SPECIAL SCHEMES</span>
      </div>

      <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
        <span class="badge badge-clause">Chapter 14 • Reg. 14.2, 14.5, 14.6</span>
        <span class="badge badge-clause">Incentive Formulas (1:R &amp; Table 14-X)</span>
        <span class="badge badge-status-done">CAD Feasibility Engine</span>
      </div>

      <h1 style="font-size:2.2rem; margin-bottom:12px; line-height:1.2;">
        Urban Redevelopment, Cluster Schemes &amp; TOD Corridors
      </h1>

      <p style="font-size:1.05rem; color:var(--ink-soft); line-height:1.6; margin-bottom:28px;">
        Navigate high-density urban transformation in Maharashtra: <strong>Slum Rehabilitation Schemes (SRS)</strong> with the $1 : R = [2.8 - 0.3n]$ incentive ratio, <strong>Cluster Redevelopment (URS)</strong> under Table 14-X, and <strong>Transit-Oriented Development (TOD)</strong> granting up to 4.00 FSI along Metro corridors.
      </p>

      <!-- SECTION 1: THE THREE STATUTORY PATHWAYS -->
      <section style="margin-bottom:32px;">
        <span class="kicker">01 // STATUTORY SCHEMES</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Three Major Redevelopment Mechanisms</h2>
        <div class="panel-info">
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:12px;">
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="kicker" style="color:var(--amber);">Scheme 1 • Reg. 14.5</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Slum Rehabilitation (SRS)</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">51% dweller consent, 27.88 sqm free carpet flats, $1:R$ incentive BUA formula, and Slum TDR generation for unconsumed potential.</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="kicker" style="color:var(--blueprint);">Scheme 2 • Reg. 14.6</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Cluster Renewal (URS)</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Min 10,000 sqm cluster, 18m road, buildings &gt; 30 years old. Grants existing carpet + 25% bonus, with FSI climbing up to 4.00+ based on Table 14-X.</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="kicker" style="color:var(--teal);">Scheme 3 • Reg. 14.2</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Transit Oriented (TOD)</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">500m Metro station buffer. Up to 4.00 FSI based on road width, 50% parking reduction, and 50:50 premium sharing with the Metro SPV.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 2: INTERACTIVE CAD REDEVELOPMENT FEASIBILITY ENGINE -->
      <section style="margin-bottom:32px;">
        <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--ink); padding-bottom:6px; margin-bottom:14px;">
          <div>
            <span class="kicker">02 // INTERACTIVE WORKBENCH</span>
            <h2 style="font-size:1.35rem; margin:0;">Live Redevelopment Feasibility &amp; Incentive CAD Engine</h2>
          </div>
          <div style="display:flex; gap:8px;">
            <button class="scheme-tab-btn active" id="tab-srs" onclick="selectScheme('srs')">SLUM REHAB (SRS)</button>
            <button class="scheme-tab-btn" id="tab-urs" onclick="selectScheme('urs')">CLUSTER (URS)</button>
            <button class="scheme-tab-btn" id="tab-tod" onclick="selectScheme('tod')">METRO TOD</button>
          </div>
        </div>

        <div style="background:var(--paper-raised); border:1px solid var(--ink); padding:20px;">
          <!-- Controls Grid -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:16px; margin-bottom:20px;">
            <div class="calc-field">
              <label for="redev-plot-area" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Scheme Plot Area (sq.m)</label>
              <input type="number" id="redev-plot-area" class="sheet-input" value="8000" min="500" max="100000" step="500">
            </div>

            <div class="calc-field">
              <label for="redev-tenants" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Eligible Tenants / Slum Dwellers</label>
              <input type="number" id="redev-tenants" class="sheet-input" value="150" min="10" max="2000" step="10">
            </div>

            <div class="calc-field">
              <label for="redev-road-width" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Abutting Road Width</label>
              <select id="redev-road-width" class="sheet-input">
                <option value="12">12.0 meters (Min for small schemes)</option>
                <option value="18" selected>18.0 meters (Standard URS / TOD Road)</option>
                <option value="24">24.0 meters (High-Capacity Corridor)</option>
                <option value="30">30.0 meters and above (Max Potential)</option>
              </select>
            </div>

            <div class="calc-field">
              <label for="redev-land-ratio" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Land Rate to Construction Cost Ratio (n)</label>
              <input type="number" id="redev-land-ratio" class="sheet-input" value="2.5" min="0.5" max="8.0" step="0.1">
              <span style="font-family:var(--mono); font-size:10px; color:var(--ink-soft);">n = Land ASR / Construction Rate</span>
            </div>
          </div>

          <!-- DYNAMIC CAD REDEVELOPMENT PARTITION PLATE -->
          <div class="blueprint-plate" style="margin-bottom:20px;">
            <div class="blueprint-plate-header">
              <span class="fig-number" id="redev-fig-num">FIG_007A // SLUM REHABILITATION (SRS) PARTITION</span>
              <span class="fig-title" id="redev-fig-title">Rehabilitation Component (Free Carpet) vs Free-Sale Incentive Component</span>
            </div>

            <div class="plate-content" style="padding:16px 8px; overflow-x:auto;">
              <svg id="redev-cad-svg" viewBox="0 0 860 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="min-width:680px; font-family:var(--mono); display:block; margin:0 auto;">
                <defs>
                  <marker id="redevArrow" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
                    <path d="M 0 0 L 6 3 L 0 6 z" fill="#2B4C7E"/>
                  </marker>
                  <pattern id="rehabHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
                    <line x1="0" y1="0" x2="0" y2="10" stroke="#DD7A0E" stroke-width="1.2" stroke-opacity="0.4"/>
                  </pattern>
                  <pattern id="saleHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">
                    <line x1="0" y1="0" x2="0" y2="10" stroke="#2B4C7E" stroke-width="1.2" stroke-opacity="0.4"/>
                  </pattern>
                </defs>

                <rect width="860" height="300" fill="#FAF8F2"/>

                <!-- Ground Baseline -->
                <line x1="40" y1="260" x2="820" y2="260" stroke="#181D24" stroke-width="2"/>
                <text x="50" y="282" fill="#5B5748" font-size="10" font-weight="700">GROUND LEVEL ± 0.00m // ROAD FRONTAGE</text>

                <!-- 1. Rehab Building Block (Left) -->
                <rect id="svg-rehab-rect" x="80" y="60" width="300" height="200" fill="url(#rehabHatch)" stroke="#DD7A0E" stroke-width="2.5"/>
                <text x="95" y="90" fill="#DD7A0E" font-size="14" font-weight="700">REHABILITATION COMPONENT</text>
                <text id="svg-rehab-bua" x="95" y="115" fill="#181D24" font-size="15" font-weight="700">Rehab BUA: 5,018 sq.m</text>
                <text id="svg-rehab-tenants" x="95" y="140" fill="#5B5748" font-size="11">150 Flats @ 27.88 sq.m Carpet</text>
                <text x="95" y="160" fill="#137333" font-size="10" font-weight="700">100% Free of Cost to Protected Dwellers</text>
                <text x="95" y="180" fill="#5B5748" font-size="9">Includes Common Areas &amp; Staircases</text>

                <!-- Plus / Equals sign -->
                <circle cx="410" cy="160" r="20" fill="#FAF8F2" stroke="#181D24" stroke-width="1.5"/>
                <text x="403" y="166" fill="#181D24" font-size="18" font-weight="700">+</text>

                <!-- 2. Free-Sale Incentive Building Block (Right) -->
                <rect id="svg-sale-rect" x="440" y="60" width="360" height="200" fill="url(#saleHatch)" stroke="#2B4C7E" stroke-width="2.5"/>
                <text x="455" y="90" fill="#2B4C7E" font-size="14" font-weight="700">FREE-SALE INCENTIVE COMPONENT</text>
                <text id="svg-sale-bua" x="455" y="115" fill="#181D24" font-size="15" font-weight="700">Incentive BUA: 10,287 sq.m</text>
                <text id="svg-sale-ratio" x="455" y="140" fill="#DD7A0E" font-size="11" font-weight="700">Incentive Ratio 1 : 2.05 (1:R)</text>
                <text x="455" y="160" fill="#5B5748" font-size="10">Sold in Open Market to Fund Rehab</text>
                <text id="svg-sale-tdr" x="455" y="180" fill="#181D24" font-size="9">Surplus potential generated as Slum TDR</text>
              </svg>
            </div>

            <div class="plate-caption" id="redev-caption">
              FIG_007A: Slum Rehabilitation Scheme (SRS) partitioning under Regulation 14.5. Free rehabilitation carpet for protected dwellers generates commercial incentive free-sale BUA based on the statutory $1:R$ ratio.
            </div>
          </div>

          <!-- SUMMARY BREAKDOWN METRICS -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--amber);">1. REHABILITATION BUA</span>
                <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:4px 0; color:var(--amber);" id="metric-rehab-bua">5,018.00 sq.m</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);" id="metric-rehab-note">
                150 Flats @ 27.88 sqm carpet
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--blueprint);">2. FREE-SALE INCENTIVE BUA</span>
                <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:4px 0; color:var(--blueprint);" id="metric-sale-bua">10,287.00 sq.m</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);" id="metric-incentive-ratio">
                Incentive Ratio: 1 : 2.05
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--green);">3. TOTAL SCHEME POTENTIAL</span>
                <div style="font-family:var(--disp); font-size:1.5rem; font-weight:700; margin:4px 0; color:var(--green);" id="metric-total-scheme-bua">15,305.00 sq.m</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);" id="metric-effective-fsi">
                Effective Scheme FSI: 1.91
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--teal);">4. PARKING &amp; DENSITY CONCESSIONS</span>
                <div style="font-family:var(--disp); font-size:1.4rem; font-weight:700; margin:4px 0; color:var(--teal);" id="metric-concession">+20% Density</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);" id="metric-concession-note">
                Statutory SRS density bonus
              </div>
            </div>
          </div>

          <!-- SUMMARY STRIP -->
          <div style="background:var(--paper); border:2px solid var(--ink); padding:16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
            <div>
              <span class="kicker" style="color:var(--blueprint);">STATUTORY FEASIBILITY STATUS</span>
              <div style="font-family:var(--disp); font-size:1.6rem; font-weight:700; color:var(--ink);" id="calc-feasibility-title">Feasible High-Yield Redevelopment Scheme</div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft); margin-top:2px;" id="calc-feasibility-desc">
                Incentive free-sale BUA of 10,287 sq.m generates robust cross-subsidy covering 100% construction costs of 150 rehabilitation tenements.
              </div>
            </div>

            <div style="text-align:right;">
              <span class="kicker-muted">CONSENT MANDATE</span>
              <div style="font-family:var(--disp); font-size:1.4rem; font-weight:700; color:var(--amber);" id="calc-consent-mandate">51% Consent Required</div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                Registered agreements before SRA submission
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- SECTION 3: COMPARATIVE STATUTORY MATRIX -->
      <section style="margin-bottom:32px;">
        <span class="kicker">03 // COMPARATIVE MATRIX</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Redevelopment Policies Matrix: SRS vs URS vs TOD</h2>
        <div style="overflow-x:auto;">
          <table class="drawing-table">
            <thead>
              <tr>
                <th>Statutory Parameter</th>
                <th>Slum Rehabilitation (Reg. 14.5)</th>
                <th>Cluster Redevelopment (Reg. 14.6)</th>
                <th>Transit Oriented (Reg. 14.2)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Minimum Plot Threshold</strong></td>
                <td style="font-family:var(--mono);">No minimum (declared slum)</td>
                <td style="font-family:var(--mono); font-weight:700; color:var(--blueprint);">10,000 sq.m (4,000 sqm Gaothan)</td>
                <td style="font-family:var(--mono);">Standard plot inside 500m buffer</td>
              </tr>
              <tr>
                <td><strong>Minimum Access Road</strong></td>
                <td style="font-family:var(--mono);">9.0 meters</td>
                <td style="font-family:var(--mono); font-weight:700; color:var(--blueprint);">18.0 meters</td>
                <td style="font-family:var(--mono);">12.0m to 30.0m+</td>
              </tr>
              <tr style="background:rgba(214, 208, 191, 0.4);">
                <td><strong>Maximum Permissible FSI</strong></td>
                <td style="font-family:var(--mono);">Formula 1:R (Up to 4.00)</td>
                <td style="font-family:var(--mono); font-weight:700; color:var(--blueprint);">Table 14-X (4.00+ FSI)</td>
                <td style="font-family:var(--mono); font-weight:700; color:var(--blueprint);">Up to 4.00 FSI</td>
              </tr>
              <tr>
                <td><strong>Tenant Entitlement</strong></td>
                <td style="font-family:var(--mono);">27.88 sq.m (300 sq.ft) free carpet</td>
                <td style="font-family:var(--mono);">Existing Carpet + 25% Bonus</td>
                <td style="font-family:var(--mono);">Standard ownership development</td>
              </tr>
              <tr>
                <td><strong>Parking Concession</strong></td>
                <td style="font-family:var(--mono);">1 scooter per 2 tenements</td>
                <td style="font-family:var(--mono);">Standard UDCPR Chapter 8</td>
                <td style="font-family:var(--mono); font-weight:700; color:var(--green);">50% Statutory Reduction</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- SECTION 4: SCRUTINY WATCHOUTS -->
      <section style="margin-bottom:32px;">
        <span class="kicker">04 // SCRUTINY WATCHOUTS</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Top 5 Scrutiny Pitfalls in Urban Redevelopment</h2>
        <div class="panel-warning">
          <ul style="padding-left:18px; margin:0; display:flex; flex-direction:column; gap:10px; font-size:0.92rem; line-height:1.55;">
            <li>
              <strong>1. Disputed Cut-Off Date for Protected Dwellers:</strong> Under Maharashtra SRA norms, only slum dwellers with documentary proof residing on or prior to <strong>01-January-2000</strong> are eligible for free rehabilitation flats. Post-2000 occupants require PMAY/Pradhan Mantri Awas Yojana verification.
            </li>
            <li>
              <strong>2. Bypassing 18.0m Road Mandate for Cluster URS:</strong> Regulation 14.6 strictly mandates that an Urban Renewal Cluster must abut an existing or sanctioned road of at least <strong>18.0 meters width</strong>. Clusters on 12m or 15m roads will be denied cluster incentives.
            </li>
            <li>
              <strong>3. Failure to Split TOD Premium with Metro SPV:</strong> Under Reg. 14.2, 50% of all premium collected on TOD FSI must be directly credited to the special account of the Mass Rapid Transit Corporation (Maha-Metro / MMRDA) for transit infrastructure maintenance.
            </li>
            <li>
              <strong>4. Neglecting Staircase/Lift Premium Exemption Caps:</strong> Under the latest Government Gazette amendments (Oct 2024), staircase, lift, and lobby area free-of-FSI allowances are capped at <strong>60% of the consumed FSI</strong>.
            </li>
            <li>
              <strong>5. TDR Ratio Requirement in TOD Corridors:</strong> On TOD plots, the developer cannot consume 100% of higher potential via government premium; <strong>at least 1/4th (25%) of the additional potential</strong> must be loaded as open-market TDR.
            </li>
          </ul>
        </div>
      </section>

      <!-- SECTION 5: VERIFICATION QUIZ -->
      <section style="margin-bottom:32px;">
        <span class="kicker">05 // VERIFICATION QUIZ</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Knowledge Check: Redevelopment &amp; Special Schemes</h2>
        <div class="quiz-container" id="redev-quiz-box"></div>
      </section>

    </main>

    <!-- Sheet Footer -->
    <footer class="sheet-footer">
      <div>UDCPR FROM SCRATCH • TOPIC 07: REDEVELOPMENT, CLUSTER SCHEMES &amp; TOD CORRIDORS</div>
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
    let currentScheme = 'srs';

    function selectScheme(scheme) {
      currentScheme = scheme;
      document.getElementById('tab-srs').classList.remove('active');
      document.getElementById('tab-urs').classList.remove('active');
      document.getElementById('tab-tod').classList.remove('active');

      document.getElementById('tab-' + scheme).classList.add('active');
      updateRedevCalc();
    }

    function updateRedevCalc() {
      const plot = parseFloat(document.getElementById('redev-plot-area').value) || 0;
      const tenants = parseInt(document.getElementById('redev-tenants').value) || 0;
      const road = parseFloat(document.getElementById('redev-road-width').value) || 18;
      const n = parseFloat(document.getElementById('redev-land-ratio').value) || 2.5;

      const figNum = document.getElementById('redev-fig-num');
      const figTitle = document.getElementById('redev-fig-title');
      const capText = document.getElementById('redev-caption');

      if (currentScheme === 'srs') {
        figNum.textContent = 'FIG_007A // SLUM REHABILITATION (SRS) PARTITION';
        figTitle.textContent = 'Rehabilitation Component (Free Carpet) vs Free-Sale Incentive Component';
        capText.textContent = 'FIG_007A: Slum Rehabilitation Scheme (SRS) partitioning under Regulation 14.5. Free rehabilitation carpet for protected dwellers generates commercial incentive free-sale BUA based on the statutory 1:R ratio.';

        // SRS Math: 27.88 sqm carpet + 20% circulation = ~33.45 sqm BUA per tenant
        const rehabBua = tenants * 33.45;
        // Incentive ratio: 1 : R = [2.8 - 0.3 * n] (min 1:1.0, max 1:2.05)
        const R = Math.max(1.0, Math.min(2.05, 2.8 - (0.3 * n)));
        const saleBua = rehabBua * R;
        const totalBua = rehabBua + saleBua;
        const effectiveFsi = totalBua / plot;

        document.getElementById('metric-rehab-bua').textContent = rehabBua.toLocaleString('en-IN', {minimumFractionDigits: 1, maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-rehab-note').textContent = tenants + ' Flats @ 27.88 sqm carpet';

        document.getElementById('metric-sale-bua').textContent = saleBua.toLocaleString('en-IN', {minimumFractionDigits: 1, maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-incentive-ratio').textContent = 'Incentive Ratio: 1 : ' + R.toFixed(2);

        document.getElementById('metric-total-scheme-bua').textContent = totalBua.toLocaleString('en-IN', {minimumFractionDigits: 1, maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-effective-fsi').textContent = 'Effective Scheme FSI: ' + effectiveFsi.toFixed(2);

        document.getElementById('metric-concession').textContent = '+20% to +30% Density';
        document.getElementById('metric-concession-note').textContent = 'Statutory SRS density bonus';

        document.getElementById('calc-feasibility-title').textContent = 'Feasible SRS Scheme (Formula 1:R)';
        document.getElementById('calc-feasibility-desc').textContent = 'Incentive free-sale BUA of ' + Math.round(saleBua).toLocaleString('en-IN') + ' sq.m cross-subsidizes 100% of ' + tenants + ' rehabilitation tenements.';
        document.getElementById('calc-consent-mandate').textContent = '51% Consent Mandate';

        // Update SVG Readouts
        document.getElementById('svg-rehab-bua').textContent = 'Rehab BUA: ' + Math.round(rehabBua).toLocaleString('en-IN') + ' sq.m';
        document.getElementById('svg-rehab-tenants').textContent = tenants + ' Flats @ 27.88 sq.m Carpet';
        document.getElementById('svg-sale-bua').textContent = 'Incentive BUA: ' + Math.round(saleBua).toLocaleString('en-IN') + ' sq.m';
        document.getElementById('svg-sale-ratio').textContent = 'Incentive Ratio 1 : ' + R.toFixed(2) + ' (1:R)';
      } else if (currentScheme === 'urs') {
        figNum.textContent = 'FIG_007B // CLUSTER REDEVELOPMENT (URS) PARTITION';
        figTitle.textContent = 'Authorized Tenant Carpet (+25% Bonus) & Table 14-X Incentive FSI (Up to 4.00+)';
        capText.textContent = 'FIG_007B: Urban Renewal Cluster Scheme under Regulation 14.6. Minimum 10,000 sqm holding with 18m road grants existing carpet + 25% bonus and high incentive FSI under Table 14-X.';

        // URS Math: assume avg 50 sqm authorized carpet + 25% bonus = 62.5 sqm carpet -> ~75 sqm BUA per tenant
        const rehabBua = tenants * 75;
        // Table 14-X FSI: typically 4.00 or higher based on road width & cluster size
        let clusterFsi = 3.00;
        if (road >= 18.0) clusterFsi = 4.00;
        if (road >= 24.0) clusterFsi = 4.50;

        const totalBua = plot * clusterFsi;
        const saleBua = Math.max(0, totalBua - rehabBua);

        document.getElementById('metric-rehab-bua').textContent = rehabBua.toLocaleString('en-IN', {maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-rehab-note').textContent = tenants + ' Tenants (Existing + 25% Bonus)';

        document.getElementById('metric-sale-bua').textContent = saleBua.toLocaleString('en-IN', {maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-incentive-ratio').textContent = 'Table 14-X Incentive Multiplier';

        document.getElementById('metric-total-scheme-bua').textContent = totalBua.toLocaleString('en-IN', {maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-effective-fsi').textContent = 'Cluster FSI: ' + clusterFsi.toFixed(2) + ' (Table 14-X)';

        document.getElementById('metric-concession').textContent = '18m Road Access';
        document.getElementById('metric-concession-note').textContent = 'Mandatory for Cluster Sanction';

        document.getElementById('calc-feasibility-title').textContent = 'Urban Renewal Cluster Scheme (URS)';
        document.getElementById('calc-feasibility-desc').textContent = 'Table 14-X grants ' + clusterFsi.toFixed(2) + ' FSI on ' + road + 'm road, generating ' + Math.round(saleBua).toLocaleString('en-IN') + ' sq.m of free-sale potential.';
        document.getElementById('calc-consent-mandate').textContent = '51% Registered Consent';

        // Update SVG Readouts
        document.getElementById('svg-rehab-bua').textContent = 'Rehab BUA: ' + Math.round(rehabBua).toLocaleString('en-IN') + ' sq.m';
        document.getElementById('svg-rehab-tenants').textContent = tenants + ' Tenants (Carpet + 25%)';
        document.getElementById('svg-sale-bua').textContent = 'Incentive BUA: ' + Math.round(saleBua).toLocaleString('en-IN') + ' sq.m';
        document.getElementById('svg-sale-ratio').textContent = 'Cluster FSI: ' + clusterFsi.toFixed(2) + ' (Table 14-X)';
      } else if (currentScheme === 'tod') {
        figNum.textContent = 'FIG_007C // TRANSIT-ORIENTED DEVELOPMENT (TOD)';
        figTitle.textContent = '500m Metro Station Buffer: FSI up to 4.00 & 50% Statutory Parking Reduction';
        capText.textContent = 'FIG_007C: Transit-Oriented Development (TOD) corridor under Regulation 14.2. Grants higher FSI based on road width, 50% parking cut, and 50:50 premium split with the Metro Authority.';

        // TOD Math: FSI based on road width
        let todFsi = 2.50;
        if (road >= 18.0) todFsi = 3.00;
        if (road >= 24.0) todFsi = 3.50;
        if (road >= 30.0) todFsi = 4.00;

        const totalBua = plot * todFsi;
        const basicBua = plot * 1.10;
        const premiumTodBua = totalBua - basicBua;

        document.getElementById('metric-rehab-bua').textContent = basicBua.toLocaleString('en-IN', {maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-rehab-note').textContent = 'Basic FSI (1.10) Baseline';

        document.getElementById('metric-sale-bua').textContent = premiumTodBua.toLocaleString('en-IN', {maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-incentive-ratio').textContent = 'TOD Premium Potential';

        document.getElementById('metric-total-scheme-bua').textContent = totalBua.toLocaleString('en-IN', {maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('metric-effective-fsi').textContent = 'TOD Corridor FSI: ' + todFsi.toFixed(2);

        document.getElementById('metric-concession').textContent = '50% Parking Cut';
        document.getElementById('metric-concession-note').textContent = 'Encourages Mass Metro Transit';

        document.getElementById('calc-feasibility-title').textContent = 'Transit Oriented Development (TOD)';
        document.getElementById('calc-feasibility-desc').textContent = 'Located inside 500m Metro buffer. Abutting ' + road + 'm road unlocks ' + todFsi.toFixed(2) + ' FSI with 50% parking concession.';
        document.getElementById('calc-consent-mandate').textContent = '50:50 Metro SPV Split';

        // Update SVG Readouts
        document.getElementById('svg-rehab-bua').textContent = 'Basic BUA: ' + Math.round(basicBua).toLocaleString('en-IN') + ' sq.m';
        document.getElementById('svg-rehab-tenants').textContent = 'Basic FSI 1.10 Baseline';
        document.getElementById('svg-sale-bua').textContent = 'TOD Potential: ' + Math.round(premiumTodBua).toLocaleString('en-IN') + ' sq.m';
        document.getElementById('svg-sale-ratio').textContent = 'TOD FSI: ' + todFsi.toFixed(2) + ' (500m Buffer)';
      }
    }

    document.addEventListener('DOMContentLoaded', function () {
      document.getElementById('redev-plot-area').addEventListener('input', updateRedevCalc);
      document.getElementById('redev-tenants').addEventListener('input', updateRedevCalc);
      document.getElementById('redev-road-width').addEventListener('change', updateRedevCalc);
      document.getElementById('redev-land-ratio').addEventListener('input', updateRedevCalc);
      updateRedevCalc();

      // Quiz Engine
      const redevQuizQuestions = [
        {
          question: "Under Regulation 14.5, what is the mandatory consent threshold required from slum dwellers to initiate a Slum Rehabilitation Scheme (SRS)?",
          options: [
            "51% of eligible slum dwellers",
            "70% of eligible slum dwellers",
            "75% of eligible slum dwellers",
            "100% unanimous consent"
          ],
          correctAnswer: 0,
          explanation: "Under Regulation 14.5 of UDCPR-2020, the statutory consent threshold required to initiate a Slum Rehabilitation Scheme is strictly 51% of eligible protected dwellers."
        },
        {
          question: "What is the minimum access road width required for an Urban Renewal Cluster Redevelopment Scheme (URS) under Regulation 14.6?",
          options: [
            "9.0 meters",
            "12.0 meters",
            "18.0 meters",
            "24.0 meters"
          ],
          correctAnswer: 2,
          explanation: "Under Regulation 14.6, an Urban Renewal Cluster must abut an existing or sanctioned road of at least 18.0 meters in width to ensure adequate high-density urban circulation."
        },
        {
          question: "What parking concession is granted to developments located within the 500-meter Transit-Oriented Development (TOD) buffer under Regulation 14.2?",
          options: [
            "No parking concession",
            "25% reduction in parking quotas",
            "50% statutory reduction in mandatory parking quotas",
            "Complete exemption from all vehicular parking"
          ],
          correctAnswer: 2,
          explanation: "To incentivize mass transit ridership and reduce car dependency, Regulation 14.2 grants an automatic 50% statutory reduction in mandatory off-street parking quotas."
        }
      ];

      initQuiz('redev-quiz-box', redevQuizQuestions, 'topic-redevelopment-navigator');
    });
  </script>
</body>
</html>
"""

def main():
    target_path = os.path.join(os.path.dirname(__file__), '..', 'topics', 'redevelopment-navigator.html')
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    print(f"✓ Created {target_path} with interactive CAD redevelopment navigator engine.")

if __name__ == '__main__':
    main()
