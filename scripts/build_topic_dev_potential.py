"""
UDCPR FROM SCRATCH - TOPIC 1 WORKBENCH GENERATOR
Builds topics/development-potential.html with interactive dynamic CAD-style dimension-line SVG diagram,
authority tier switcher, financial ASR calculation, scrutiny watchouts, and verification quiz.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Development Potential &amp; FSI Calculation Engine | UDCPR from Scratch</title>
  <meta name="description" content="Interactive FSI Calculation Engine for Maharashtra UDCPR. Calculate Basic FSI, Premium FSI, TDR loading caps, Ancillary FSI, and ASR financial charges with dynamic CAD dimension drawings.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/blueprint.css">
  <link rel="stylesheet" href="/css/components.css">
  <style>
    .dynamic-elevation-container {
      background: var(--paper-raised);
      border: 1px solid var(--ink);
      padding: 20px;
      margin-top: 16px;
      position: relative;
    }
    .svg-dimension-text {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      fill: var(--ink);
    }
    .svg-witness-line {
      stroke: var(--ink-soft);
      stroke-width: 1;
      stroke-dasharray: 2, 2;
    }
    .svg-dimension-line {
      stroke: var(--blueprint);
      stroke-width: 1.5;
      marker-start: url(#cadArrowStart);
      marker-end: url(#cadArrowEnd);
    }
    .fsi-summary-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border: 1px solid var(--line-strong);
      background: var(--paper);
      font-family: var(--mono);
      font-size: 11px;
    }
    .breakdown-card {
      border: 1px solid var(--line-strong);
      background: var(--paper);
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
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
      <strong>STATUTORY SPECIFICATION:</strong> Reg. 6.3 (Table 6-A &amp; 6-G), Reg. 2.2.14, Reg. 6.4, and Reg. 11.2 of Maharashtra UDCPR-2020. Verify with Sanctioned Development Plan &amp; ASR Ready Reckoner.
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
        <span style="color:var(--blueprint);">DEVELOPMENT POTENTIAL &amp; FSI ENGINE</span>
      </div>

      <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
        <span class="badge badge-clause">Reg. 6.3 &amp; Table 6-A</span>
        <span class="badge badge-clause">Reg. 2.2.14 (35% ASR)</span>
        <span class="badge badge-status-done">Interactive CAD Engine</span>
      </div>

      <h1 style="font-size:2.2rem; margin-bottom:12px; line-height:1.2;">
        Development Potential &amp; FSI Calculation Engine
      </h1>

      <p style="font-size:1.05rem; color:var(--ink-soft); line-height:1.6; margin-bottom:28px;">
        Master the mathematical stacking rules that govern every plot in Maharashtra. Determine permissible Built-Up Area (BUA) across the four statutory layers: <strong>Basic FSI</strong>, <strong>Premium FSI (35% ASR)</strong>, <strong>TDR Loading Caps</strong>, and <strong>Ancillary FSI (+60%/80%)</strong>.
      </p>

      <!-- SECTION 1: THE FOUR-TIER FSI EQUATION -->
      <section style="margin-bottom:32px;">
        <span class="kicker">01 // PEDAGOGICAL BREAKDOWN</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">The Four Stacking Layers of Building Potential</h2>
        <div class="panel-info">
          <p style="margin-bottom:14px;">
            Unlike legacy municipal by-laws with a single uniform FSI multiplier, UDCPR establishes an <strong>additive stacking hierarchy</strong> where your plot's abutting road width dictates how high your building potential can legally climb:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:12px; margin-bottom:8px;">
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="kicker" style="color:var(--blueprint);">Layer 1 • As-of-Right</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Basic FSI</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Available by law without additional premium charges (typically 1.10 for Municipal Corporations, 1.00 for Municipal Councils &amp; Regional Plans).</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="kicker" style="color:var(--amber);">Layer 2 • Municipal Purchase</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Premium FSI</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Purchased directly from the Planning Authority at exactly <strong>35% of prevailing ASR land rate</strong> (Reg. 2.2.14). Up to 0.50 FSI.</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="kicker" style="color:var(--ink);">Layer 3 • Market DRC</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">TDR Loading</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Purchased from the open market as DRCs generated from surrendered reservations under Reg. 11.2. Allowed only on roads &ge; 12.0m.</p>
            </div>
            <div style="background:var(--paper); border:1px solid var(--line-strong); padding:12px;">
              <span class="kicker" style="color:var(--teal);">Layer 4 • Non-FSI Areas</span>
              <div style="font-family:var(--disp); font-weight:700; font-size:1rem; margin-top:2px;">Ancillary Area FSI</div>
              <p style="font-size:0.82rem; color:var(--ink-soft); margin-top:4px;">Up to <strong>60% (residential)</strong> or <strong>80% (commercial)</strong> additional area above total consumed FSI at premium for balconies, ducts, &amp; lobbies (Reg. 6.3.3).</p>
            </div>
          </div>
        </div>
      </section>

      <!-- SECTION 2: INTERACTIVE CAD CALCULATION WORKBENCH -->
      <section style="margin-bottom:32px;">
        <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--ink); padding-bottom:6px; margin-bottom:14px;">
          <div>
            <span class="kicker">02 // INTERACTIVE WORKBENCH</span>
            <h2 style="font-size:1.35rem; margin:0;">Live Building Potential &amp; Dimension CAD Engine</h2>
          </div>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REACTIVE CAD SECTION</span>
        </div>

        <div style="background:var(--paper-raised); border:1px solid var(--ink); padding:20px;">
          <!-- Controls Grid -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-bottom:20px;">
            <div class="calc-field">
              <label for="workbench-authority" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Planning Authority Jurisdiction</label>
              <select id="workbench-authority" class="sheet-input">
                <option value="corporation" selected>Municipal Corporation (Table 6-A • Base 1.10)</option>
                <option value="council">Municipal Council (Table 6-A • Base 1.00/1.10)</option>
                <option value="regional">Regional Plan Authority (Table 6-G • Base 1.00)</option>
                <option value="congested">Congested / Gaothan Core (Table 6-D • Base 1.50/2.00)</option>
              </select>
            </div>

            <div class="calc-field">
              <label for="workbench-road" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Abutting Road Width</label>
              <select id="workbench-road" class="sheet-input">
                <option value="9">Below 9.0 meters (No Premium, No TDR)</option>
                <option value="12">9.0m to &lt; 12.0m (0.30 Premium, No TDR)</option>
                <option value="15">12.0m to &lt; 15.0m (0.30 Prem + 0.20 TDR)</option>
                <option value="18">15.0m to &lt; 18.0m (0.40 Prem + 0.30 TDR)</option>
                <option value="24" selected>18.0m to &lt; 24.0m (0.50 Prem + 0.40 TDR)</option>
                <option value="30">24.0m to &lt; 30.0m (0.50 Prem + 0.50 TDR)</option>
                <option value="36">30.0m and above (0.50 Prem + 0.65 TDR)</option>
              </select>
            </div>

            <div class="calc-field">
              <label for="workbench-plot-size" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">Net Plot Area (sq.m)</label>
              <input type="number" id="workbench-plot-size" class="sheet-input" value="2000" min="50" max="50000" step="25">
            </div>

            <div class="calc-field">
              <label for="workbench-asr" style="font-family:var(--mono); font-size:11px; font-weight:700; text-transform:uppercase;">ASR Land Rate (₹ / sq.m)</label>
              <input type="number" id="workbench-asr" class="sheet-input" value="35000" min="1000" max="500000" step="500">
            </div>
          </div>

          <!-- DYNAMIC CAD DIMENSION PLATE -->
          <div class="blueprint-plate" style="margin-bottom:20px;">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_002A // DYNAMIC ELEVATION STACK</span>
              <span class="fig-title">Permissible Built-Up Area Tranches &amp; Dimension Chains (Scale 1:Dynamic)</span>
            </div>

            <div class="plate-content" style="padding:16px 8px; overflow-x:auto;">
              <svg id="cad-elevation-svg" viewBox="0 0 860 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="min-width:680px; font-family:var(--mono); display:block; margin:0 auto;">
                <defs>
                  <marker id="cadArrowStart" markerWidth="6" markerHeight="6" refX="0" refY="3" orient="auto">
                    <path d="M 6 0 L 0 3 L 6 6 z" fill="#2B4C7E"/>
                  </marker>
                  <marker id="cadArrowEnd" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
                    <path d="M 0 0 L 6 3 L 0 6 z" fill="#2B4C7E"/>
                  </marker>
                  <marker id="cadMasterArrowStart" markerWidth="6" markerHeight="6" refX="0" refY="3" orient="auto">
                    <path d="M 6 0 L 0 3 L 6 6 z" fill="#181D24"/>
                  </marker>
                  <marker id="cadMasterArrowEnd" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto">
                    <path d="M 0 0 L 6 3 L 0 6 z" fill="#181D24"/>
                  </marker>

                  <pattern id="baseHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
                    <line x1="0" y1="0" x2="0" y2="10" stroke="#2B4C7E" stroke-width="1.2" stroke-opacity="0.3"/>
                  </pattern>
                  <pattern id="premHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">
                    <line x1="0" y1="0" x2="0" y2="10" stroke="#DD7A0E" stroke-width="1.2" stroke-opacity="0.4"/>
                  </pattern>
                  <pattern id="tdrHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(90)">
                    <line x1="0" y1="0" x2="0" y2="10" stroke="#181D24" stroke-width="1.2" stroke-opacity="0.3"/>
                  </pattern>
                  <pattern id="ancillaryHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(30)">
                    <line x1="0" y1="0" x2="0" y2="10" stroke="#008080" stroke-width="1.2" stroke-opacity="0.35"/>
                  </pattern>
                </defs>

                <!-- Architectural Drawing Sheet Background -->
                <rect width="860" height="380" fill="#FAF8F2"/>

                <!-- Ground Level Baseline -->
                <line x1="40" y1="320" x2="820" y2="320" stroke="#181D24" stroke-width="2.5"/>
                <text x="50" y="342" fill="#5B5748" font-size="10" font-weight="700">GROUND LEVEL ± 0.00m // PLINTH BASE</text>

                <!-- Abutting Road Indicator on Left -->
                <rect x="40" y="270" width="130" height="50" fill="#F1EEE4" stroke="#5B5748" stroke-width="1"/>
                <text x="50" y="295" fill="#181D24" font-size="10" font-weight="700" id="svg-road-label">18.0m ROAD</text>
                <text x="50" y="310" fill="#5B5748" font-size="9" id="svg-authority-label">CORP TABLE 6-A</text>

                <!-- BUILDING MASS STACK (DYNAMIC RECTANGLES) -->
                <!-- 1. Basic FSI Block -->
                <rect id="rect-basic" x="220" y="210" width="340" height="110" fill="url(#baseHatch)" stroke="#2B4C7E" stroke-width="2"/>
                <text id="text-basic-fsi" x="235" y="270" fill="#2B4C7E" font-size="13" font-weight="700">LAYER 1: BASIC FSI = 1.10</text>
                <text id="text-basic-area" x="235" y="290" fill="#2B4C7E" font-size="11">2,200.00 sq.m (Statutory Baseline)</text>

                <!-- 2. Premium FSI Block -->
                <rect id="rect-premium" x="220" y="160" width="340" height="50" fill="url(#premHatch)" stroke="#DD7A0E" stroke-width="2"/>
                <text id="text-prem-fsi" x="235" y="188" fill="#DD7A0E" font-size="12" font-weight="700">LAYER 2: PREMIUM FSI = 0.50</text>
                <text id="text-prem-area" x="235" y="202" fill="#DD7A0E" font-size="10">1,000.00 sq.m (@ 35% ASR Rate)</text>

                <!-- 3. TDR Block -->
                <rect id="rect-tdr" x="220" y="120" width="340" height="40" fill="url(#tdrHatch)" stroke="#181D24" stroke-width="2"/>
                <text id="text-tdr-fsi" x="235" y="145" fill="#181D24" font-size="12" font-weight="700">LAYER 3: TDR LOADING = 0.40</text>
                <text id="text-tdr-area" x="235" y="157" fill="#5B5748" font-size="10">800.00 sq.m (Market DRC Transfer)</text>

                <!-- 4. Ancillary Area FSI Block -->
                <rect id="rect-ancillary" x="220" y="70" width="340" height="50" fill="url(#ancillaryHatch)" stroke="#008080" stroke-width="2"/>
                <text id="text-ancillary-fsi" x="235" y="96" fill="#008080" font-size="12" font-weight="700">LAYER 4: ANCILLARY FSI (60% RESIDENTIAL)</text>
                <text id="text-ancillary-area" x="235" y="110" fill="#008080" font-size="10">2,400.00 sq.m (Balconies, Ducts, Terraces)</text>

                <!-- LEFT CAD DIMENSION CHAIN (Sub-Tranches) -->
                <!-- Witness lines -->
                <line x1="205" y1="320" x2="195" y2="320" class="svg-witness-line"/>
                <line x1="205" y1="210" x2="195" y2="210" class="svg-witness-line"/>
                <line x1="205" y1="160" x2="195" y2="160" class="svg-witness-line"/>
                <line x1="205" y1="120" x2="195" y2="120" class="svg-witness-line"/>
                <line x1="205" y1="70" x2="195" y2="70" class="svg-witness-line"/>

                <!-- Left Dimension line for Total FSI without Ancillary -->
                <line x1="200" y1="320" x2="200" y2="120" stroke="#2B4C7E" stroke-width="1.5" marker-start="url(#cadArrowStart)" marker-end="url(#cadArrowEnd)"/>
                <text x="145" y="225" fill="#2B4C7E" font-size="10" font-weight="700" transform="rotate(-90 145 225)" id="dim-total-fsi-left">TOTAL FSI = 2.00</text>

                <!-- RIGHT MASTER CAD DIMENSION BRACKET (TOTAL GROSS POTENTIAL) -->
                <line x1="575" y1="320" x2="615" y2="320" class="svg-witness-line"/>
                <line x1="575" y1="70" x2="615" y2="70" class="svg-witness-line"/>

                <line x1="605" y1="320" x2="605" y2="70" stroke="#181D24" stroke-width="2" marker-start="url(#cadMasterArrowStart)" marker-end="url(#cadMasterArrowEnd)"/>
                
                <!-- Dimension Leader Box -->
                <rect x="625" y="165" width="215" height="60" fill="#FAF8F2" stroke="#181D24" stroke-width="1.5"/>
                <text x="635" y="185" fill="#5B5748" font-size="9" font-weight="700">MAX GROSS CONSTRUCTION:</text>
                <text x="635" y="204" fill="#2B4C7E" font-size="15" font-weight="700" id="dim-gross-total-sqm">6,400.00 sq.m</text>
                <text x="635" y="218" fill="#181D24" font-size="10" id="dim-gross-factor">Gross Factor: 3.20x Plot</text>
              </svg>
            </div>

            <div class="plate-caption">
              FIG_002A: Dynamic multi-layer building potential envelope showing Basic, Premium, TDR, and Ancillary FSI tranches with statutory dimension chains.
            </div>
          </div>

          <!-- SUMMARY BALANCE SHEET -->
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:16px;">
            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--blueprint);">1. BASIC FSI POTENTIAL</span>
                <div style="font-family:var(--disp); font-size:1.4rem; font-weight:700; margin:4px 0;" id="out-basic-bua">2,200.00 sq.m</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                FSI: <strong id="out-basic-factor">1.10</strong> • Premium: <strong style="color:var(--green);">₹ 0 (Free)</strong>
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--amber);">2. PREMIUM FSI ENTITLEMENT</span>
                <div style="font-family:var(--disp); font-size:1.4rem; font-weight:700; margin:4px 0; color:var(--amber);" id="out-prem-bua">1,000.00 sq.m</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                FSI: <strong id="out-prem-factor">0.50</strong> • Payable: <strong id="out-prem-cost" style="color:var(--ink);">₹ 1.22 Cr</strong>
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--ink);">3. TDR LOADING CAPACITY</span>
                <div style="font-family:var(--disp); font-size:1.4rem; font-weight:700; margin:4px 0;" id="out-tdr-bua">800.00 sq.m</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                FSI: <strong id="out-tdr-factor">0.40</strong> • Open Market DRC
              </div>
            </div>

            <div class="breakdown-card">
              <div>
                <span class="kicker" style="color:var(--teal);">4. ANCILLARY AREA FSI (+60%)</span>
                <div style="font-family:var(--disp); font-size:1.4rem; font-weight:700; margin:4px 0; color:var(--teal);" id="out-ancillary-bua">2,400.00 sq.m</div>
              </div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                Payable: <strong id="out-ancillary-cost">₹ 2.94 Cr</strong> (@ 35% ASR)
              </div>
            </div>
          </div>

          <!-- TOTAL SUMMARY STRIP -->
          <div style="background:var(--paper); border:2px solid var(--ink); padding:16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
            <div>
              <span class="kicker" style="color:var(--blueprint);">STATUTORY RESULT SUMMARY</span>
              <div style="font-family:var(--disp); font-size:1.8rem; font-weight:700; color:var(--ink);" id="out-master-total-bua">6,400.00 sq.m Gross Potential</div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft); margin-top:2px;">
                Permissible Plot FSI: <strong id="out-fsi-multiplier">2.00</strong> + Ancillary Area Bonus (60%): <strong id="out-gross-multiplier">3.20 Gross FSI</strong>
              </div>
            </div>

            <div style="text-align:right;">
              <span class="kicker-muted">ESTIMATED CORP REVENUE (35% ASR)</span>
              <div style="font-family:var(--disp); font-size:1.6rem; font-weight:700; color:var(--amber);" id="out-total-premium-payable">₹ 4.16 Crore</div>
              <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">
                Staged installment option available under Reg. 2.2.14
              </div>
            </div>
          </div>

        </div>
      </section>

      <!-- SECTION 3: STATUTORY REFERENCE TABLE 6-A -->
      <section style="margin-bottom:32px;">
        <span class="kicker">03 // STATUTORY CITATION</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Statutory Table No. 6-A: Non-Congested FSI Matrix</h2>
        <div style="overflow-x:auto;">
          <table class="drawing-table">
            <thead>
              <tr>
                <th>Abutting Road Width</th>
                <th class="num-col">Basic FSI</th>
                <th class="num-col">Premium FSI</th>
                <th class="num-col">Max TDR</th>
                <th class="num-col">Total Permissible FSI</th>
                <th>Ancillary Area Potential (60%)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight:600;">Below 9.0 m</td>
                <td class="num-col">1.10</td>
                <td class="num-col" style="color:var(--ink-soft);">--</td>
                <td class="num-col" style="color:var(--ink-soft);">--</td>
                <td class="num-col" style="font-weight:700; color:var(--blueprint);">1.10</td>
                <td style="font-family:var(--mono); font-size:11px;">+0.66 Gross (1.76 Total)</td>
              </tr>
              <tr>
                <td style="font-weight:600;">9.0 m to &lt; 12.0 m</td>
                <td class="num-col">1.10</td>
                <td class="num-col" style="color:var(--amber);">0.30</td>
                <td class="num-col" style="color:var(--ink-soft);">--</td>
                <td class="num-col" style="font-weight:700; color:var(--blueprint);">1.40</td>
                <td style="font-family:var(--mono); font-size:11px;">+0.84 Gross (2.24 Total)</td>
              </tr>
              <tr>
                <td style="font-weight:600;">12.0 m to &lt; 15.0 m</td>
                <td class="num-col">1.10</td>
                <td class="num-col" style="color:var(--amber);">0.30</td>
                <td class="num-col">0.20</td>
                <td class="num-col" style="font-weight:700; color:var(--blueprint);">1.60</td>
                <td style="font-family:var(--mono); font-size:11px;">+0.96 Gross (2.56 Total)</td>
              </tr>
              <tr>
                <td style="font-weight:600;">15.0 m to &lt; 18.0 m</td>
                <td class="num-col">1.10</td>
                <td class="num-col" style="color:var(--amber);">0.40</td>
                <td class="num-col">0.30</td>
                <td class="num-col" style="font-weight:700; color:var(--blueprint);">1.80</td>
                <td style="font-family:var(--mono); font-size:11px;">+1.08 Gross (2.88 Total)</td>
              </tr>
              <tr style="background:rgba(214, 208, 191, 0.4);">
                <td style="font-weight:600;">18.0 m to &lt; 24.0 m</td>
                <td class="num-col">1.10</td>
                <td class="num-col" style="color:var(--amber);">0.50</td>
                <td class="num-col">0.40</td>
                <td class="num-col" style="font-weight:700; color:var(--blueprint);">2.00</td>
                <td style="font-family:var(--mono); font-size:11px;">+1.20 Gross (3.20 Total)</td>
              </tr>
              <tr>
                <td style="font-weight:600;">24.0 m to &lt; 30.0 m</td>
                <td class="num-col">1.10</td>
                <td class="num-col" style="color:var(--amber);">0.50</td>
                <td class="num-col">0.50</td>
                <td class="num-col" style="font-weight:700; color:var(--blueprint);">2.10</td>
                <td style="font-family:var(--mono); font-size:11px;">+1.26 Gross (3.36 Total)</td>
              </tr>
              <tr>
                <td style="font-weight:600;">30.0 m and above</td>
                <td class="num-col">1.10</td>
                <td class="num-col" style="color:var(--amber);">0.50</td>
                <td class="num-col">0.65</td>
                <td class="num-col" style="font-weight:700; color:var(--blueprint);">2.25</td>
                <td style="font-family:var(--mono); font-size:11px;">+1.35 Gross (3.60 Total)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- SECTION 4: SCRUTINY WATCHOUTS -->
      <section style="margin-bottom:32px;">
        <span class="kicker">04 // MUNICIPAL SCRUTINY</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Top 5 Plan Scrutiny Pitfalls that Trigger Rejection</h2>
        <div class="panel-warning">
          <ul style="padding-left:18px; margin:0; display:flex; flex-direction:column; gap:10px; font-size:0.92rem; line-height:1.55;">
            <li>
              <strong>1. Measuring Road Width at Plot Center instead of Narrowest Bottleneck:</strong> Under Reg. 1.3(104), road width is verified across the entire access route from the nearest arterial road. A single 7.5m bottleneck before your 18m frontage caps your potential at the 7.5m tier.
            </li>
            <li>
              <strong>2. Attempting TDR on Roads Under 12.0m:</strong> Table 6-A strictly forbids any TDR loading on roads narrower than 12.0m. Any proposal claiming TDR on a 9m road will be summarily rejected.
            </li>
            <li>
              <strong>3. Failure to Deduct DP Reservations before Calculating Net Area:</strong> If a 24m DP road reservation cuts 300 sq.m through your 2,000 sq.m holding, in-situ FSI can only be consumed on the <strong>Net Plot Area (1,700 sq.m)</strong> unless Accommodation Reservation (Reg. 11.1) is officially granted.
            </li>
            <li>
              <strong>4. Miscalculating Ancillary Area Cap:</strong> Ancillary FSI (60% residential) is capped against the <strong>actual consumed FSI</strong>, not hypothetical gross envelopes. If you only consume 1.10 Base FSI, your ancillary entitlement is $1.10 \times 60\% = 0.66$, not $2.00 \times 60\%$.
            </li>
            <li>
              <strong>5. Ignoring Staged Payment Default Penalty:</strong> Under Reg. 2.2.14, opting for installment payments of Premium FSI incurs <strong>8.5% simple annual interest</strong>. Failure to pay before the Occupancy Certificate halts OC issuance immediately.
            </li>
          </ul>
        </div>
      </section>

      <!-- SECTION 5: KNOWLEDGE CHECK QUIZ -->
      <section style="margin-bottom:32px;">
        <span class="kicker">05 // VERIFICATION QUIZ</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Knowledge Check: Development Potential &amp; FSI</h2>
        <div class="quiz-container" id="fsi-quiz-box"></div>
      </section>

    </main>

    <!-- Sheet Footer -->
    <footer class="sheet-footer">
      <div>UDCPR FROM SCRATCH • TOPIC 01: DEVELOPMENT POTENTIAL &amp; FSI CALCULATION</div>
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
    document.addEventListener('DOMContentLoaded', function () {
      const authEl = document.getElementById('workbench-authority');
      const roadEl = document.getElementById('workbench-road');
      const plotEl = document.getElementById('workbench-plot-size');
      const asrEl = document.getElementById('workbench-asr');

      // Table 6-A Master Matrix for Municipal Corporations
      const fsiMatrixCorp = {
        '9':  { base: 1.10, prem: 0.00, tdr: 0.00, total: 1.10, label: '< 9.0m' },
        '12': { base: 1.10, prem: 0.30, tdr: 0.00, total: 1.40, label: '9.0–12m' },
        '15': { base: 1.10, prem: 0.30, tdr: 0.20, total: 1.60, label: '12–15m' },
        '18': { base: 1.10, prem: 0.40, tdr: 0.30, total: 1.80, label: '15–18m' },
        '24': { base: 1.10, prem: 0.50, tdr: 0.40, total: 2.00, label: '18–24m' },
        '30': { base: 1.10, prem: 0.50, tdr: 0.50, total: 2.10, label: '24–30m' },
        '36': { base: 1.10, prem: 0.50, tdr: 0.65, total: 2.25, label: '30m+' }
      };

      // Table 6-G for Regional Plans (Rural/Peri-urban)
      const fsiMatrixRegional = {
        '9':  { base: 1.00, prem: 0.00, tdr: 0.00, total: 1.00, label: '< 9.0m' },
        '12': { base: 1.00, prem: 0.20, tdr: 0.00, total: 1.20, label: '9.0–12m' },
        '15': { base: 1.00, prem: 0.30, tdr: 0.10, total: 1.40, label: '12–15m' },
        '18': { base: 1.00, prem: 0.30, tdr: 0.20, total: 1.50, label: '15–18m' },
        '24': { base: 1.00, prem: 0.40, tdr: 0.30, total: 1.70, label: '18–24m' },
        '30': { base: 1.00, prem: 0.40, tdr: 0.40, total: 1.80, label: '24–30m' },
        '36': { base: 1.00, prem: 0.50, tdr: 0.50, total: 2.00, label: '30m+' }
      };

      // Congested Core (Gaothan Table 6-D)
      const fsiMatrixCongested = {
        '9':  { base: 1.50, prem: 0.00, tdr: 0.00, total: 1.50, label: '< 9.0m' },
        '12': { base: 1.50, prem: 0.30, tdr: 0.00, total: 1.80, label: '9.0–12m' },
        '15': { base: 1.50, prem: 0.40, tdr: 0.10, total: 2.00, label: '12–15m' },
        '18': { base: 1.50, prem: 0.50, tdr: 0.20, total: 2.20, label: '15–18m' },
        '24': { base: 1.50, prem: 0.50, tdr: 0.30, total: 2.30, label: '18–24m' },
        '30': { base: 1.50, prem: 0.50, tdr: 0.40, total: 2.40, label: '24–30m' },
        '36': { base: 1.50, prem: 0.50, tdr: 0.50, total: 2.50, label: '30m+' }
      };

      function formatCr(val) {
        if (val >= 10000000) {
          return '₹ ' + (val / 10000000).toFixed(2) + ' Cr';
        } else if (val >= 100000) {
          return '₹ ' + (val / 100000).toFixed(2) + ' Lakh';
        }
        return '₹ ' + Math.round(val).toLocaleString('en-IN');
      }

      function updateWorkbench() {
        const auth = authEl.value;
        const road = roadEl.value;
        const plot = parseFloat(plotEl.value) || 0;
        const asr = parseFloat(asrEl.value) || 0;

        let matrix = fsiMatrixCorp;
        let authLabel = 'CORP TABLE 6-A';
        if (auth === 'regional') {
          matrix = fsiMatrixRegional;
          authLabel = 'REGIONAL TAB 6-G';
        } else if (auth === 'congested') {
          matrix = fsiMatrixCongested;
          authLabel = 'GAOTHAN TAB 6-D';
        } else if (auth === 'council') {
          matrix = fsiMatrixCorp;
          authLabel = 'COUNCIL TAB 6-A';
        }

        const tier = matrix[road] || matrix['24'];

        const baseBua = plot * tier.base;
        const premBua = plot * tier.prem;
        const tdrBua = plot * tier.tdr;
        const totalFsiBua = plot * tier.total;
        
        // Ancillary Area FSI is 60% of total consumed FSI (Reg 6.3.3)
        const ancillaryFactor = 0.60;
        const ancillaryBua = totalFsiBua * ancillaryFactor;
        const grossBua = totalFsiBua + ancillaryBua;
        const grossFsiFactor = tier.total * (1 + ancillaryFactor);

        // Premium Financials (Reg 2.2.14: 35% of ASR land rate)
        const premCost = premBua * (0.35 * asr);
        const ancillaryCost = ancillaryBua * (0.35 * asr);
        const totalGovtCost = premCost + ancillaryCost;

        // Update Text Readouts
        document.getElementById('out-basic-bua').textContent = baseBua.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' sq.m';
        document.getElementById('out-basic-factor').textContent = tier.base.toFixed(2);

        document.getElementById('out-prem-bua').textContent = premBua.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' sq.m';
        document.getElementById('out-prem-factor').textContent = tier.prem.toFixed(2);
        document.getElementById('out-prem-cost').textContent = formatCr(premCost);

        document.getElementById('out-tdr-bua').textContent = tdrBua.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' sq.m';
        document.getElementById('out-tdr-factor').textContent = tier.tdr.toFixed(2);

        document.getElementById('out-ancillary-bua').textContent = ancillaryBua.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' sq.m';
        document.getElementById('out-ancillary-cost').textContent = formatCr(ancillaryCost);

        document.getElementById('out-master-total-bua').textContent = grossBua.toLocaleString('en-IN', {minimumFractionDigits: 2, maximumFractionDigits: 2}) + ' sq.m Gross Potential';
        document.getElementById('out-fsi-multiplier').textContent = tier.total.toFixed(2);
        document.getElementById('out-gross-multiplier').textContent = grossFsiFactor.toFixed(2) + ' Gross Factor';
        document.getElementById('out-total-premium-payable').textContent = formatCr(totalGovtCost);

        // Update SVG Dimension Labels & Block Heights
        const baseY = 320;
        const scalePx = 70; // 1.0 FSI = 70px

        const hBase = tier.base * scalePx;
        const hPrem = tier.prem * scalePx;
        const hTdr = tier.tdr * scalePx;
        const hAncillary = (tier.total * ancillaryFactor) * (scalePx * 0.45); // visually scaled

        const yBase = baseY - hBase;
        const yPrem = yBase - hPrem;
        const yTdr = yPrem - hTdr;
        const yAncillary = yTdr - hAncillary;

        // Base Rect
        const rBase = document.getElementById('rect-basic');
        rBase.setAttribute('y', yBase);
        rBase.setAttribute('height', hBase);
        document.getElementById('text-basic-fsi').textContent = 'LAYER 1: BASIC FSI = ' + tier.base.toFixed(2);
        document.getElementById('text-basic-area').textContent = baseBua.toFixed(1) + ' sq.m (Statutory Baseline)';
        document.getElementById('text-basic-fsi').setAttribute('y', yBase + (hBase / 2) + 2);
        document.getElementById('text-basic-area').setAttribute('y', yBase + (hBase / 2) + 16);

        // Premium Rect
        const rPrem = document.getElementById('rect-premium');
        rPrem.setAttribute('y', yPrem);
        rPrem.setAttribute('height', Math.max(hPrem, 0));
        rPrem.style.display = tier.prem > 0 ? 'block' : 'none';
        const tPremFsi = document.getElementById('text-prem-fsi');
        const tPremArea = document.getElementById('text-prem-area');
        tPremFsi.style.display = tier.prem > 0 ? 'block' : 'none';
        tPremArea.style.display = tier.prem > 0 ? 'block' : 'none';
        if (tier.prem > 0) {
          tPremFsi.textContent = 'LAYER 2: PREMIUM FSI = ' + tier.prem.toFixed(2);
          tPremArea.textContent = premBua.toFixed(1) + ' sq.m (@ 35% ASR: ' + formatCr(premCost) + ')';
          tPremFsi.setAttribute('y', yPrem + (hPrem / 2) + 2);
          tPremArea.setAttribute('y', yPrem + (hPrem / 2) + 14);
        }

        // TDR Rect
        const rTdr = document.getElementById('rect-tdr');
        rTdr.setAttribute('y', yTdr);
        rTdr.setAttribute('height', Math.max(hTdr, 0));
        rTdr.style.display = tier.tdr > 0 ? 'block' : 'none';
        const tTdrFsi = document.getElementById('text-tdr-fsi');
        const tTdrArea = document.getElementById('text-tdr-area');
        tTdrFsi.style.display = tier.tdr > 0 ? 'block' : 'none';
        tTdrArea.style.display = tier.tdr > 0 ? 'block' : 'none';
        if (tier.tdr > 0) {
          tTdrFsi.textContent = 'LAYER 3: TDR CAP = ' + tier.tdr.toFixed(2);
          tTdrArea.textContent = tdrBua.toFixed(1) + ' sq.m (Market DRC)';
          tTdrFsi.setAttribute('y', yTdr + (hTdr / 2) + 2);
          tTdrArea.setAttribute('y', yTdr + (hTdr / 2) + 14);
        }

        // Ancillary Rect
        const rAnc = document.getElementById('rect-ancillary');
        rAnc.setAttribute('y', yAncillary);
        rAnc.setAttribute('height', hAncillary);
        document.getElementById('text-ancillary-fsi').textContent = 'LAYER 4: ANCILLARY AREA FSI (+60%)';
        document.getElementById('text-ancillary-area').textContent = ancillaryBua.toFixed(1) + ' sq.m (Balconies & Services)';
        document.getElementById('text-ancillary-fsi').setAttribute('y', yAncillary + (hAncillary / 2) + 2);
        document.getElementById('text-ancillary-area').setAttribute('y', yAncillary + (hAncillary / 2) + 14);

        // Update Right Master Dimension Line & Leader
        document.getElementById('dim-gross-total-sqm').textContent = grossBua.toLocaleString('en-IN', {maximumFractionDigits: 1}) + ' sq.m';
        document.getElementById('dim-gross-factor').textContent = 'Gross Factor: ' + grossFsiFactor.toFixed(2) + 'x Plot';
        document.getElementById('dim-total-fsi-left').textContent = 'PERMISSIBLE FSI = ' + tier.total.toFixed(2);

        // Update Left Witness line and labels
        document.getElementById('svg-road-label').textContent = tier.label + ' ROAD';
        document.getElementById('svg-authority-label').textContent = authLabel;
      }

      authEl.addEventListener('change', updateWorkbench);
      roadEl.addEventListener('change', updateWorkbench);
      plotEl.addEventListener('input', updateWorkbench);
      asrEl.addEventListener('input', updateWorkbench);
      updateWorkbench();

      // Quiz Engine
      const fsiQuizQuestions = [
        {
          question: "Under Table 6-A of UDCPR-2020, can Transferable Development Rights (TDR) be loaded on a plot with an abutting road width of 9.0 meters?",
          options: [
            "Yes, up to 0.20 FSI",
            "No, statutory TDR loading is 0.00 on roads under 12.0m",
            "Yes, if additional premium is paid to the Municipal Commissioner",
            "Only for commercial and IT park developments"
          ],
          correctAnswer: 1,
          explanation: "Under Table 6-A (Regulation 6.3), maximum permissible TDR loading is 0.00 for roads below 12.0 meters in width. TDR loading only becomes legal once road width is 12.0m or wider."
        },
        {
          question: "At what rate is Premium FSI purchased from the Planning Authority under Regulation 2.2.14?",
          options: [
            "100% of the Annual Statement of Rates (ASR) land value",
            "50% of the ASR land value",
            "35% of the prevailing ASR land value",
            "Fixed nominal flat rate of ₹2,000 per sq.m"
          ],
          correctAnswer: 2,
          explanation: "Under Regulation 2.2.14 and Regulation 6.3, Premium FSI is purchased directly from the Planning Authority at exactly 35% of the prevailing Annual Statement of Rates (Ready Reckoner) for non-agricultural developed land."
        },
        {
          question: "How is the Ancillary Area FSI entitlement (60% for residential) calculated under Regulation 6.3.3?",
          options: [
            "60% of the Gross Plot Area",
            "60% of the Basic FSI area only",
            "60% of the total actually consumed FSI on the plot (Base + Premium + TDR)",
            "60% of the maximum theoretical envelope irrespective of consumed FSI"
          ],
          correctAnswer: 2,
          explanation: "Under Regulation 6.3.3, Ancillary Area FSI (60% for residential, 80% for commercial) is strictly calculated on the actual consumed FSI (Basic + Premium + TDR), payable at 35% of ASR land rate."
        }
      ];

      initQuiz('fsi-quiz-box', fsiQuizQuestions, 'topic-dev-potential');
    });
  </script>
</body>
</html>
"""

def main():
    target_path = os.path.join(os.path.dirname(__file__), '..', 'topics', 'development-potential.html')
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    print(f"✓ Rebuilt {target_path} with dynamic interactive CAD dimension engine.")

if __name__ == '__main__':
    main()
