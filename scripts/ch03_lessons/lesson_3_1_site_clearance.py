"""
UDCPR FROM SCRATCH - CHAPTER 3: LESSON 3.1
Module: scripts/ch03_lessons/lesson_3_1_site_clearance.py
Governing Regulation: Regulation 3.1 (Requirements of Site)
Covers: Reg 3.1.1 to 3.1.13 - Site eligibility, high-tension lines (Table 3-1), Blue/Red flood lines, railway 30m offset, classified highways, prison offsets, and airport CCZM.
"""

lesson_data = {
    'filename': 'reg-3-1-site-clearance-buffers.html',
    'lesson_id': 'lesson-reg-3-1',
    'quiz_id': 'quiz-reg-3-1',
    'clause': 'Reg. 3.1',
    'title': 'Site Requirements & Statutory Clearance Buffers',
    'badge_status': 'Core Safety Clearance',
    'ch_slug': 'ch03',
    'ch_title': 'Chapter 3: General Land Development',
    'meta_desc': 'Statutory site clearance buffers under UDCPR Regulation 3.1: River blue and red flood lines, high-tension electrical line clearances (Table 3-1), railway 30m buffers, prison offsets, and highway control lines.',
    'lead_summary': 'Learn the mandatory safety buffers required before any construction can be sited in Maharashtra: river flood lines (Blue Prohibitive vs Red Restrictive), high-voltage overhead electric transmission clearances, railway boundary offsets, highway control lines, prison buffer perimeters, and airport height restrictions.',
    'amendment_cite': 'CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        Before preparing any architectural or layout plan, an engineer must verify whether the land parcel is legally and physically eligible for construction. Regulation 3.1 establishes rigid safety clearances from natural hazards, public utilities, and critical infrastructure.
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
        <li><strong>Ineligible Sites (Reg. 3.1.1):</strong> No building can be erected on ground made up of organic refuse, night soil, or toxic fill until certified sanitary by the Authority; on sites within water courses or prone to landslides; or within prohibited buffer zones of heritage monuments.</li>
        <li><strong>Electric Transmission Line Clearances (Reg. 3.1.2 &amp; Table 3-1):</strong>
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px; margin-top:8px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Line Voltage Category</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Vertical Clearance</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Horizontal Clearance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Low &amp; Medium Voltage (&le; 650 V)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">2.50 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">1.20 m</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">High Voltage (up to 11 kV)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">3.70 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">1.20 m</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">High Voltage (11 kV to 33 kV)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">3.70 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">2.00 m</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Extra High Voltage (&gt; 33 kV)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">3.70 m + 0.30 m per 33 kV</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">2.00 m + 0.30 m per 33 kV</td>
              </tr>
            </tbody>
          </table>
        </li>
        <li><strong>Blue &amp; Red River Flood Lines (Reg. 3.1.3):</strong>
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li><strong>Inside Blue Flood Line (Prohibitive Zone):</strong> Reflects 1-in-25 year flood frequency. <em>Zero permanent building construction permitted</em> (only open gardens, playfields, or surface parking without structures).</li>
            <li><strong>Between Blue &amp; Red Flood Line (Restrictive Zone):</strong> Reflects 1-in-100 year flood frequency. Construction is permissible, <strong>provided the plinth level is constructed at least 0.45 m above the Red Flood Line</strong>!</li>
            <li><strong>Nallahs &amp; Minor Water Courses:</strong> Mandatory non-buildable buffer of <strong>6.0 m</strong> from the defined edge/bank of minor nallahs.</li>
            <li><strong>Lakes &amp; Dams (Reg. 3.1.12):</strong> Mandatory <strong>100 m buffer</strong> from Highest Flood Level (HFL) or Full Reservoir Level (FRL).</li>
          </ul>
        </li>
        <li><strong>Railway Tracks (Reg. 3.1.4):</strong> Any plot within <strong>30.0 m of the railway boundary</strong> requires mandatory prior No Objection Certificate (NOC) from the concerned Railway Administration.</li>
        <li><strong>Highways &amp; Classified Roads (Reg. 3.1.6):</strong> Buildings must observe building line and control line offsets from National Highways, State Highways, and Major District Roads (MDR) as per PWD standards.</li>
        <li><strong>Security &amp; Institutional Buffers:</strong>
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li><strong>Prisons (Reg. 3.1.7):</strong> 150 m buffer from Central Prisons, 100 m from District Prisons, and 50 m from Sub-Jails.</li>
            <li><strong>Landfills (Reg. 3.1.8):</strong> 500 m buffer from municipal solid waste dump sites.</li>
            <li><strong>Airports (Reg. 3.1.9):</strong> Strict adherence to Colour Coded Zoning Maps (CCZM) and height clearances from the Airports Authority of India (AAI).</li>
            <li><strong>Ancient Monuments (Reg. 3.1.10):</strong> 100 m prohibited zone + 200 m regulated zone under the Archaeological Survey of India (ASI).</li>
          </ul>
        </li>
      </ul>
    """,
    'statutory_extract': "3.1.2 Distance of site from Electric Lines: No verandah, balcony, or any part of a building shall be constructed within the distance specified in Table 3-1... 3.1.3 Construction within Blue and Red Flood Line: Area between the river bank and blue flood line (prohibitive zone) shall be maintained open... The area between blue flood line and red flood line (restrictive zone) may be permitted to be developed provided the plinth of the building is kept 0.45 m. above the red flood line... 3.1.4 Development within 30.0 m. Distance from Railway Boundary: No development within 30.0 m... without prior NOC of the concerned Railway Authority...",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 3.1.3 // FLOOD LINE ZONING</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Blue vs Red Line Rule</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            <strong>Blue Line (Prohibitive Zone):</strong> 100% non-buildable open zone.
            <br><strong>Red Line (Restrictive Zone):</strong> Building permitted only if the finished plinth level is cast <strong>&ge; 0.45 m above the Red Flood Level</strong>.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 3.1.2 // ELECTRICAL CLEARANCE</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Table 3-1 Safety Clearance</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            For 33 kV lines: 3.70 m vertical &amp; 2.00 m horizontal. For every additional 33 kV (e.g. 66 kV, 110 kV, 220 kV), add 0.30 m to both vertical and horizontal buffers from the outermost conductor.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_014 // STATUTORY SITE CLEARANCE BUFFERS PLATE</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 3.1 ARCHITECTURAL PLATE</span>
        </div>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11.5px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Statutory Clearance Entity</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Governing Clause</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Mandatory Offset Distance</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Statutory Requirement / Constraint</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Minor Water Course / Nallah</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 3.1.1(ii)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">6.0 m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">From edge of defined bank; non-buildable buffer</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Wetlands / Marshes</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 3.1.1(xiv)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">50.0 m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">From Mean High Flood Level; ecological reserve</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Natural Lake / Dam HFL</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 3.1.12</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">100.0 m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">From Highest Flood Level of reservoir / dam water body</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Railway Land Boundary</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 3.1.4</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">30.0 m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Mandatory prior NOC from Railway Administration</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Central Prison Perimeter</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 3.1.7</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">150.0 m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Height &amp; surveillance security clearance zone</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Municipal Landfill Site</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 3.1.8</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">500.0 m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Health &amp; odor buffer from active/closed solid waste site</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Ancient Monument (ASI)</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 3.1.10</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">100m / 200m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">100 m prohibited (zero work) + 200 m regulated (NMA NOC)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="margin-bottom:12px;">
        <strong>Practical Site Scrutiny Problem:</strong> An architect is preparing a layout for a <strong>15,000 sq.m plot</strong> in Pune abutting the Mula River.
      </p>
      <div class="worked-step">
        <span class="step-badge">FLOOD LINE AUDIT</span>
        <div>
          The Irrigation Department plan shows the <strong>Blue Flood Line</strong> passes 20 m inside the riverward plot boundary, covering <strong>2,500 sq.m</strong>. The <strong>Red Flood Line</strong> covers an additional <strong>3,000 sq.m</strong>.
          <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; BLUE LINE RULE (Reg. 3.1.3):</span> The 2,500 sq.m prohibitive zone cannot have buildings. The architect designs it as open landscaping and tree plantation.
          <br><span style="font-family:var(--mono); color:var(--amber);">&#10003; RED LINE RULE (Reg. 3.1.3):</span> The 3,000 sq.m restrictive zone can have residential buildings, provided the <strong>finished plinth is at least 0.45 m above the Red Flood Level</strong> (RL + 542.45 m).
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">HIGH TENSION CLEARANCE</span>
        <div>
          A <strong>110 kV transmission line</strong> cuts diagonally across the plot corner.
          <br>Table 3-1 Formula for &gt; 33 kV:
          <br><span style="font-family:var(--mono);">Base vertical = 3.70 m + [0.30 m &times; ceil((110 - 33) / 33)] = 3.70 + (0.30 &times; 3) = <strong>4.60 m vertical clearance</strong>.</span>
          <br><span style="font-family:var(--mono);">Base horizontal = 2.00 m + [0.30 m &times; ceil((110 - 33) / 33)] = 2.00 + (0.30 &times; 3) = <strong>2.90 m horizontal clearance</strong>.</span>
          <br>The building envelope is pulled back 3.0 m from the outermost conductor line.
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ STATUTORY COMPLIANCE: Both flood line plinth elevations and 110 kV conductors clearances are satisfied on the sanctioned site plan.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Casting Habitable Plinth Below 0.45 m Above the Red Flood Level</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Regulation 3.1.3 allows construction between the Blue and Red flood lines, but strictly requires that the plinth be kept <strong>0.45 m above the Red Flood Line</strong>. Providing plinths at normal ground level in restrictive flood zones violates building permission and voids disaster insurance.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Encroaching Balconies into High-Tension Wire Clearance Buffers</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under Regulation 3.1.2: <em>"No verandah, balcony, or any part of a building shall be constructed within the distance specified in Table 3-1."</em> Architects frequently ensure ground walls clear the line, but cantilever upper-floor balconies or chajjas into the prohibited clearance corridor, triggering immediate stop-work notices.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 3: Failing to Apply for Railway NOC on Plots Within 30.0 Metres</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under Regulation 3.1.4, any construction within 30.0 m of the railway boundary requires prior railway clearance. Commencing work without Railway NOC halts construction at plinth stage and exposes the project to demolition by railway enforcement squads.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Highway Offsets &amp; Flood Line Clarifications</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Standardized building line and control line offsets for classified state and national highways passing through Municipal Corporation limits under Reg. 3.1.6, and harmonized flood line demarcations with the State Water Resources Department.
      </p>
    """,
    'quiz': [
        {
            'question': 'Under Regulation 3.1.3, what is the mandatory plinth height requirement for a building constructed between the Blue and Red Flood Lines?',
            'options': [
                'At least 0.15 m above normal road level',
                'At least 0.45 m above the Red Flood Line',
                'At least 1.0 m above the Blue Flood Line',
                'At the same level as the river bank'
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.1.3 explicitly mandates that development between the blue and red flood lines is permitted 'provided the plinth of the building is kept 0.45 m. above the red flood line'."
        },
        {
            'question': 'What is the required horizontal and vertical safety clearance from a 33 kV high-voltage electric transmission line under Table 3-1?',
            'options': [
                '1.20 m horizontal and 2.50 m vertical',
                '2.00 m horizontal and 3.70 m vertical',
                '3.00 m horizontal and 5.00 m vertical',
                '5.00 m horizontal and 7.50 m vertical'
            ],
            'correctAnswer': 1,
            'explanation': "Table 3-1 under Regulation 3.1.2 mandates a vertical clearance of 3.70 m and a horizontal clearance of 2.00 m for High Voltage lines between 11 kV and 33 kV."
        },
        {
            'question': 'Within what distance from a Railway land boundary is prior No Objection Certificate (NOC) mandatory under Regulation 3.1.4?',
            'options': [
                'Within 10.0 metres',
                'Within 20.0 metres',
                'Within 30.0 metres',
                'Within 100.0 metres'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.1.4 states: 'No development within 30.0 m. distance from the railway boundary shall be permitted without prior NOC of the concerned Railway Authority'."
        },
        {
            'question': 'What is the mandatory non-buildable safety buffer strip to be left along minor water courses or nallahs under Regulation 3.1.1(ii)?',
            'options': [
                '3.0 metres from the edge of the water mark',
                '6.0 metres from the edge of the water mark',
                '9.0 metres from the edge of the water mark',
                '15.0 metres from the center of the nallah'
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 3.1.1(ii), a minimum buffer of 6.0 m from the defined edge/bank of minor water courses (nallahs) must be kept open and free of building construction."
        }
    ],
    'prev_url': '/lessons/reg-2-6-commencement-and-occupancy.html',
    'prev_title': 'Reg. 2.6-2.15 Commencement & Occupancy',
    'next_url': '/lessons/reg-3-3-internal-layout-roads.html',
    'next_title': 'Reg. 3.2-3.3 Layout Roads'
}
