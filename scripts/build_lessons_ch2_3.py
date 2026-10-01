import os
import sys
from generate_lessons import create_lesson_page

sys.stdout.reconfigure(encoding='utf-8')

lessons_batch2 = [
    # -------------------------------------------------------------
    # LESSON 8: Reg. 3.1
    # -------------------------------------------------------------
    {
        'filename': 'reg-3-1-site-clearance-buffers.html',
        'lesson_id': 'lesson-reg-3-1',
        'quiz_id': 'quiz-reg-3-1',
        'clause': 'Reg. 3.1',
        'title': 'Site Requirements & Statutory Clearance Buffers',
        'badge_status': 'Core Safety',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Statutory site clearance buffers under UDCPR Regulation 3.1: River blue and red flood lines, high-tension electrical line clearances, railway buffers, and defence zones.',
        'lead_summary': 'Learn the mandatory safety buffers required before any construction can be sited: flood lines along rivers and nallahs, overhead high-voltage electric line clearances, railway boundary offsets, and defence installations.',
        'amendment_cite': 'Order CR.236/18',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            Even if a plot is zoned residential in a Development Plan, physical site constraints can restrict buildability. Regulation 3.1 establishes inviolable safety buffers from water bodies, high-voltage electric corridors, railway tracks, and defence boundaries.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>River Blue & Red Flood Lines (Reg. 3.1.1):</strong> No construction is permitted inside the Blue Line (prohibitive zone). Between the Blue Line and Red Line (restrictive zone), construction is allowed strictly above the flood line with plinth restrictions.</li>
            <li><strong>Nallah Buffers:</strong> Minimum <strong>9.0 meters</strong> buffer from defined river banks; <strong>4.5 to 6.0 meters</strong> buffer from natural nallahs.</li>
            <li><strong>High-Tension Electric Lines (Reg. 3.1.2):</strong> Horizontal clearance of 1.2m to 2.5m for 11kV/33kV, up to 4.6m for 220kV lines. Vertical clearance of 3.7m to 5.5m minimum.</li>
            <li><strong>Railway Track Clearance (Reg. 3.1.3):</strong> Minimum <strong>30.0 meters</strong> buffer from the railway property boundary without prior Railway NOC.</li>
          </ul>
        """,
        'statutory_extract': "No piece of land shall be used as a site for the construction of building if the Authority considers that the site is insanitary or that it is dangerous to construct a building on it... River / Nallah buffer: The building shall be at a distance not less than 9.0m from the bank of river and 4.5m / 6.0m from natural nallah...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">Defence Clearances (Reg. 3.1.4)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              Sites situated within 500 meters (or 100m/50m depending on military installation category) of defence establishments require written No Objection Certificate (NOC) from the local Military Station Commander.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_010 // SITE CLEARANCE BUFFERS</span>
              <span class="fig-title">Inviolable Clearance Zones Around Infrastructure (Reg. 3.1)</span>
            </div>
            <div style="padding:16px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              INFRASTRUCTURE CLEARANCE OFFSETS (MINIMUM)<br>
              ├── Natural River Bank &rarr; 9.0m Clear Buffer (Reg. 3.1.1)<br>
              ├── Major Nallah &rarr; 6.0m Clear Buffer (Canalized: 4.5m)<br>
              ├── Railway Property Boundary &rarr; 30.0m Buffer (or NOC from Railways)<br>
              ├── Electric Line 11 kV &rarr; 1.2m Horizontal / 3.7m Vertical (Reg. 3.1.2)<br>
              ├── Electric Line 33 kV &rarr; 2.0m Horizontal / 3.7m Vertical<br>
              └── Electric Line 132–220 kV &rarr; 4.6m Horizontal / 5.5m Vertical
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Siting a Building Abutting a 66kV Transmission Corridor</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A 66 kV overhead line passes across the eastern boundary of a residential plot.
            </p>
            <div class="worked-step">
              <span class="step-badge">STATUTORY BUFFER</span>
              <div>Under Reg. 3.1.2 Table No. 3-1, the building wall must maintain at least <strong>2.6 meters horizontal clearance</strong> from the outermost conductor line, and no balcony projection may encroach into this corridor.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Culverting or Shifting Natural Nallahs Without Irrigation Approval</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Developers frequently attempt to box or divert natural nallahs to enlarge building footprints. Shifting or canalizing a water course requires prior permission from the Chief Engineer, Water Resources Department.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarification CR.236/18 (Part 2) dt. 23 Dec 2021 reiterated that Blue Line flood levels determined by the Irrigation Department take strict precedence over any municipal zoning map.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the minimum statutory buffer required from the bank of a river under Regulation 3.1.1?",
            'options': [
              "3.0 meters",
              "6.0 meters",
              "9.0 meters",
              "15.0 meters"
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.1.1 prescribes that no building shall be erected within a distance of at least 9.0 meters from the defined bank of a river."
          },
          {
            'question': "What is the standard clearance distance required from a railway boundary without railway NOC under Regulation 3.1.3?",
            'options': [
              "10 meters",
              "15 meters",
              "30 meters",
              "50 meters"
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.1.3 mandates that any development within 30 meters of a railway property boundary requires prior NOC from Railway authorities."
          }
        ],
        'prev_url': '/lessons/reg-2-6-commencement-and-occupancy.html',
        'prev_title': 'Reg. 2.6 – 2.11 Certificates',
        'next_url': '/lessons/reg-3-3-internal-layout-roads.html',
        'next_title': 'Reg. 3.3 Layout Roads'
      },

    # -------------------------------------------------------------
    # LESSON 9: Reg. 3.3
    # -------------------------------------------------------------
    {
        'filename': 'reg-3-3-internal-layout-roads.html',
        'lesson_id': 'lesson-reg-3-3',
        'quiz_id': 'quiz-reg-3-3',
        'clause': 'Reg. 3.3',
        'title': 'Means of Access & Internal Layout Road Widths',
        'badge_status': 'Core Master Planning',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Calculate internal layout road widths under UDCPR Regulation 3.3. Road width vs length thresholds, cul-de-sacs, turning radius, and road handing over.',
        'lead_summary': 'Learn how to plan internal circulation for plotted subdivisions and group housing layouts: road width requirements based on road length, cul-de-sac turnarounds, and acute angle junction roundoffs.',
        'amendment_cite': 'Order CR.236/18',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            Every plot or building in a layout must have independent, clear vehicular access. Under Regulation 3.3, the required width of an internal street is directly proportional to its <strong>length</strong>:
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Length up to 75m:</strong> Minimum road width is <strong>6.0m</strong> (for residential cul-de-sacs) or <strong>9.0m</strong> (general).</li>
            <li><strong>Length 75m to 150m:</strong> Minimum road width is <strong>9.0 meters</strong>.</li>
            <li><strong>Length 150m to 300m:</strong> Minimum road width is <strong>12.0 meters</strong>.</li>
            <li><strong>Length above 300m:</strong> Minimum road width is <strong>15.0 meters</strong>.</li>
            <li><strong>Cul-de-sacs (Reg. 3.3.10):</strong> Dead-end streets up to 100m length must terminate in a turning circle with a radius not less than <strong>9.0 meters</strong>.</li>
          </ul>
        """,
        'statutory_extract': "The width of internal layout roads shall be as given in Table No.3-2... For residential and commercial layout: Length up to 75m requires 9.0m road; length up to 150m requires 9.0m road; length up to 300m requires 12.0m road; length more than 300m requires 15.0m road...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">Handing Over of Layout Roads (Reg. 3.3.11)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              In plotted subdivisions, all internal roads must be formed, paved with storm drains and street lighting, and handed over to the Planning Authority free of cost through a registered deed. In Group Housing schemes, roads can remain private common property of the society.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div style="overflow-x:auto; background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-md); padding:16px; margin:20px 0;">
            <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
              <thead>
                <tr style="border-bottom:1px solid var(--border-dim); color:var(--accent-cyan); font-family:var(--font-mono); text-align:left;">
                  <th style="padding:8px;">Road Length</th>
                  <th style="padding:8px;">Residential / Commercial</th>
                  <th style="padding:8px;">Industrial Layout</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">Up to 75 meters</td>
                  <td style="padding:8px; font-weight:700;">9.0 m (6.0m cul-de-sac)</td>
                  <td style="padding:8px; font-family:var(--font-mono);">12.0 m</td>
                </tr>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">75 m to 150 meters</td>
                  <td style="padding:8px; font-weight:700;">9.0 m</td>
                  <td style="padding:8px; font-family:var(--font-mono);">12.0 m</td>
                </tr>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">150 m to 300 meters</td>
                  <td style="padding:8px; font-weight:700;">12.0 m</td>
                  <td style="padding:8px; font-family:var(--font-mono);">15.0 m</td>
                </tr>
                <tr>
                  <td style="padding:8px; font-family:var(--font-mono);">Over 300 meters</td>
                  <td style="padding:8px; font-weight:700;">15.0 m</td>
                  <td style="padding:8px; font-family:var(--font-mono);">18.0 m</td>
                </tr>
              </tbody>
            </table>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Sizing an Internal Street of 210m Length</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A residential layout connects a series of row houses along a single internal spine road measuring 210 meters from the municipal main road.
            </p>
            <div class="worked-step">
              <span class="step-badge">EVALUATION</span>
              <div>Length is between 150m and 300m &rarr; Under Table 3-2, the minimum width must be <strong>12.0 meters</strong>. A 9.0m road will be rejected during scrutiny.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Measuring Road Length from Center Instead of Furthest Point</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Road length is measured from the public street entrance to the furthest corner of the furthest plot served by that street (Reg. 3.3.3).
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarification Order No. CR.236/18 dt. 23 Dec 2021 addressed road width transitions when a layout abuts existing narrow classified village roads being widened under Regional Plans.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the minimum required internal layout road width for a road length between 150m and 300m?",
            'options': [
              "6.0 meters",
              "9.0 meters",
              "12.0 meters",
              "15.0 meters"
            ],
            'correctAnswer': 2,
            'explanation': "Under Table 3-2 of Regulation 3.3, residential internal layout roads measuring between 150m and 300m in length must have a minimum width of 12.0 meters."
          },
          {
            'question': "What turnaround geometry is required for a cul-de-sac dead end street?",
            'options': [
              "Square box of 5m x 5m",
              "Turning circle with radius not less than 9.0 meters",
              "No turnaround is required",
              "Only a 2-meter pedestrian pathway"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.3.10 requires cul-de-sacs to terminate in a turning circle with a radius of not less than 9.0 meters for fire tenders and garbage trucks."
          }
        ],
        'prev_url': '/lessons/reg-3-1-site-clearance-buffers.html',
        'prev_title': 'Reg. 3.1 Site Buffers',
        'next_url': '/lessons/reg-3-4-1-recreational-open-space.html',
        'next_title': 'Reg. 3.4.1 Open Space'
      },

    # -------------------------------------------------------------
    # LESSON: Reg. 3.4.1 Recreational Open Space
    # -------------------------------------------------------------
    {
        'filename': 'reg-3-4-1-recreational-open-space.html',
        'lesson_id': 'lesson-reg-3-4-1',
        'quiz_id': 'quiz-reg-3-4-1',
        'clause': 'Reg. 3.4.1',
        'title': 'Recreational Open Space (ROS) & Layout Greenery',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Master Regulation 3.4.1: The 10% Recreational Open Space (ROS) mandate, 0.4 ha threshold, clubhouse construction, and Green Belt rules under Maharashtra UDCPR-2020.',
        'lead_summary': 'Learn the statutory 10% open space mandate, applicability thresholds, minimum pocket dimensions, clubhouse building entitlements, and how Government Clarification CR.104/22 resolved area measurement rules.',
        'amendment_cite': 'CR.104/22',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            Whenever you subdivide land or develop a large group housing project in Maharashtra, you cannot pave over the entire property. The law requires you to leave a portion of the land open to the sky as a <strong>Recreational Open Space (ROS)</strong> for gardens, parks, and children's play areas.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--ink-soft);">
            <li><strong>The General Rule:</strong> If your net plot or layout area is <strong>0.40 hectares (4,000 sq.m) or more</strong>, you must dedicate at least <strong>10% of the land</strong> as contiguous open space.</li>
            <li><strong>Small Layouts (0.2 ha to 0.4 ha):</strong> You must provide <strong>5% open space</strong> (or 10% in certain municipal council limits).</li>
            <li><strong>Very Small Plots (&lt; 0.2 ha):</strong> Zero statutory layout open space is required (building setbacks still apply).</li>
            <li><strong>The Clubhouse Bonus:</strong> You are permitted to construct a residents' clubhouse, swimming pool dressing room, or gymnasium occupying up to <strong>10% of the ROS area</strong>, limited to Ground + 1 upper floor.</li>
          </ul>
        """,
        'statutory_extract': "In any layout or sub-division of land or development proposal for residential, commercial or industrial use, having area 0.4 ha. or more, recreational open space shall have to be provided at the rate of 10% on gross area after deducting area under reservations / roads in Development Plan / Regional Plan...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--blueprint);">Dimension Minimums (Reg. 3.4.6)</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                No single recreational open space pocket shall be less than <strong>400 sq.m</strong>. Furthermore, the minimum average width of this open pocket must not be less than <strong>15 meters</strong>.
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--blueprint);">Means of Access (Reg. 3.4.8)</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                Every open space must abut an internal layout road or public street of minimum required width. It cannot be situated as a landlocked interior courtyard.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_001 // REGULATORY GEOMETRY</span>
              <span class="fig-title">Recreational Open Space (10%) &amp; Permissible Clubhouse Footprint</span>
            </div>
            <div class="plate-content">
              <svg viewBox="0 0 740 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width:700px; font-family:var(--mono);">
                <defs>
                  <pattern id="cadGrid" width="20" height="20" patternUnits="userSpaceOnUse">
                    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#D6D0BF" stroke-width="0.5"/>
                  </pattern>
                </defs>
                <rect width="740" height="380" fill="#FAF8F2"/>
                <rect width="740" height="380" fill="url(#cadGrid)"/>
                <rect x="40" y="40" width="660" height="300" fill="none" stroke="#181D24" stroke-width="2" stroke-dasharray="8,4"/>
                <text x="50" y="32" fill="#181D24" font-size="11" font-weight="700">GROSS SITE BOUNDARY [12,000 SQ.M]</text>
                <rect x="40" y="270" width="660" height="50" fill="#F1EEE4" stroke="#5B5748" stroke-width="1.5"/>
                <text x="310" y="300" fill="#181D24" font-size="11" font-weight="600">12.0m INTERNAL LAYOUT ROAD (REG. 3.3)</text>
                <line x1="40" y1="295" x2="700" y2="295" stroke="#5B5748" stroke-width="0.8" stroke-dasharray="4,4"/>
                <rect x="70" y="70" width="240" height="170" fill="#FAF8F2" stroke="#2B4C7E" stroke-width="1.5"/>
                <text x="130" y="150" fill="#181D24" font-size="12" font-weight="700">RESIDENTIAL WING A &amp; B</text>
                <text x="145" y="170" fill="#5B5748" font-size="11">BUILT-UP ENVELOPE</text>
                <rect x="360" y="70" width="310" height="170" fill="#EAE5D7" stroke="#2B4C7E" stroke-width="2"/>
                <text x="410" y="95" fill="#2B4C7E" font-size="12" font-weight="700">RECREATIONAL OPEN SPACE (ROS)</text>
                <text x="445" y="115" fill="#5B5748" font-size="11">AREA = 1,200 SQ.M (10% OF GROSS)</text>
                <line x1="360" y1="60" x2="670" y2="60" stroke="#2B4C7E" stroke-width="1"/>
                <line x1="360" y1="55" x2="360" y2="65" stroke="#2B4C7E" stroke-width="1"/>
                <line x1="670" y1="55" x2="670" y2="65" stroke="#2B4C7E" stroke-width="1"/>
                <text x="480" y="52" fill="#2B4C7E" font-size="11" text-anchor="middle">WIDTH &ge; 15.0m (REG. 3.4.6)</text>
                <line x1="685" y1="70" x2="685" y2="240" stroke="#2B4C7E" stroke-width="1"/>
                <line x1="680" y1="70" x2="690" y2="70" stroke="#2B4C7E" stroke-width="1"/>
                <line x1="680" y1="240" x2="690" y2="240" stroke="#2B4C7E" stroke-width="1"/>
                <text x="700" y="160" fill="#2B4C7E" font-size="10" transform="rotate(90, 700, 160)">MIN POCKET &ge; 400 SQ.M</text>
                <rect x="380" y="150" width="100" height="70" fill="#FAF8F2" stroke="#DD7A0E" stroke-width="1.5"/>
                <text x="390" y="180" fill="#DD7A0E" font-size="10" font-weight="700">CLUB HOUSE / GYM</text>
                <text x="400" y="195" fill="#5B5748" font-size="9">MAX 10% OF ROS</text>
                <text x="410" y="210" fill="#5B5748" font-size="9">[G+1 STOREY]</text>
                <path d="M 515 240 L 515 270" stroke="#2B4C7E" stroke-width="2" stroke-dasharray="2,2"/>
                <text x="525" y="260" fill="#2B4C7E" font-size="10">ABUTS ROAD</text>
              </svg>
            </div>
            <div class="plate-caption">
              FIG_001: Statutory geometry showing 10% mandatory ROS pocket, minimum 15m dimension, road frontage, and permissible G+1 clubhouse footprint (Reg. 3.4.1 &amp; 3.4.7).
            </div>
          </div>
        """,
        'worked_example_html': """
          <h4 style="font-size:1.05rem; margin-bottom:10px; color:var(--ink);">
            Scenario: Residential Group Housing on a 12,000 sq.m Plot in Pune
          </h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); margin-bottom:16px;">
            An architect is preparing a layout for a 12,000 sq.m vacant land parcel abutting a 12m municipal road. No DP road or public reservations affect the land.
          </p>
          <div class="worked-step">
            <span class="step-badge">STEP 1</span>
            <div>
              <strong>Check Applicability Threshold (Reg. 3.4.1):</strong><br>
              <span style="font-family:var(--mono); font-size:0.88rem; color:var(--blueprint);">
                Gross Area = 12,000 sq.m &ge; 4,000 sq.m (0.40 ha) &rarr; 10% Mandatory ROS applies.
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">STEP 2</span>
            <div>
              <strong>Compute Mandatory Open Space Area:</strong><br>
              <span style="font-family:var(--mono); font-size:0.88rem; color:var(--blueprint);">
                ROS Area = 12,000 sq.m &times; 0.10 = 1,200.00 sq.m
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">STEP 3</span>
            <div>
              <strong>Pocket Distribution Verification (Reg. 3.4.6):</strong><br>
              <span style="font-size:0.85rem; color:var(--ink-soft);">
                The architect designs two open spaces: Pocket A = 700 sq.m, Pocket B = 500 sq.m.<br>
                Both pockets &ge; 400 sq.m minimum pocket size and both maintain a width &ge; 15.0m &rarr; <strong>Compliant.</strong>
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">STEP 4</span>
            <div>
              <strong>Clubhouse Construction Entitlement (Reg. 3.4.7):</strong><br>
              <span style="font-family:var(--mono); font-size:0.88rem; color:var(--blueprint);">
                Permissible Clubhouse Built-up Area = 1,200 sq.m &times; 0.10 = 120.00 sq.m
              </span><br>
              <span style="font-size:0.85rem; color:var(--ink-soft);">
                Maximum height allowed: Ground + 1 upper floor. Ground coverage can be 60 sq.m with 60 sq.m first floor gym.
              </span>
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ FINAL VERDICT: 1,200 sq.m Green Open Space provided + 120 sq.m Clubhouse sanctioned.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Splitting Open Space into Narrow Residual Strips</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Architects often attempt to combine front marginal setbacks or residual triangles into the ROS count. Under Reg. 3.4.6, every individual pocket must have a standalone area of at least 400 sq.m and a clear minimum width of 15 meters. Leftover strips cannot be counted.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Counting River / Nallah Green Belt as Mandatory ROS</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Reg. 3.4.5, open space in a designated Green Belt along a river or nallah can only be counted towards the layout ROS if it is explicitly accessible and usable, and subject to prior irrigation authority clearances.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Designing Multi-Storey Clubhouses</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              The 10% clubhouse entitlement is strictly capped at Ground + 1 upper floor. Commercial banquets, party halls rented to outsiders, or multi-storey structures are grounds for immediate plan rejection.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">(#) Government Order No. CR.104/2022</span>
            <span style="font-family:var(--mono); font-size:0.8rem; color:var(--ink-soft);">Dated 29th November, 2022</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.6;">
            <strong>Issue Clarified:</strong> Multiple planning authorities across Maharashtra had conflicting interpretations on whether the 0.40-hectare threshold was calculated on gross cadastral area or net developable area.
          </p>
          <p style="font-size:0.88rem; color:var(--ink); margin-top:8px; line-height:1.6;">
            <strong>Ruling:</strong> The Government clarified that the 0.40 ha threshold must be measured with reference to the <em>gross plot area</em> after deducting only sanctioned DP road widening.
          </p>
        """,
        'quiz': [
          {
            'question': "At what layout or plot area threshold does the 10% Recreational Open Space (ROS) mandate become statutory?",
            'options': [
              "0.10 hectares (1,000 sq.m)",
              "0.20 hectares (2,000 sq.m)",
              "0.40 hectares (4,000 sq.m)",
              "1.00 hectare (10,000 sq.m)"
            ],
            'correctAnswer': 2,
            'explanation': "Under UDCPR Reg. 3.4.1, the 10% recreational open space requirement is mandatory for layouts or subdivisions measuring 0.40 hectares (4,000 sq.m) or more."
          },
          {
            'question': "What is the absolute minimum area and average width for any individual Recreational Open Space pocket under Reg. 3.4.6?",
            'options': [
              "200 sq.m and 10 meters width",
              "400 sq.m and 15 meters width",
              "500 sq.m and 12 meters width",
              "300 sq.m and 18 meters width"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.4.6 stipulates that no single ROS pocket shall be less than 400 sq.m, and the average width must not be less than 15 meters."
          },
          {
            'question': "How much built-up area can be constructed for a resident clubhouse/gym within the Recreational Open Space?",
            'options': [
              "Up to 5% of ROS area, Ground floor only",
              "Up to 10% of ROS area, Ground + 1 upper floor",
              "Up to 25% of ROS area, up to 15m height",
              "Zero — ROS must strictly remain open to sky"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 3.4.7, structures like a club house, gym, or pavilion are permitted occupying up to 10% of the ROS area, restricted to Ground + 1 storey."
          },
          {
            'question': "Government Clarification CR.104/2022 clarified that the 0.40 ha threshold is measured with reference to which area?",
            'options': [
              "Gross plot area minus DP road widening",
              "Carpet area of all proposed tenements",
              "Net plot area after deducting amenity space and internal roads",
              "Surrendered TDR land area only"
            ],
            'correctAnswer': 0,
            'explanation': "Clarification CR.104/2022 established that the 0.40 ha threshold is measured against gross plot area after deducting only sanctioned DP road widening."
          }
        ],
        'prev_url': '/lessons/reg-3-3-internal-layout-roads.html',
        'prev_title': 'Reg. 3.3 Layout Roads',
        'next_url': '/lessons/reg-3-5-amenity-space-provision.html',
        'next_title': 'Reg. 3.5 Amenity Space'
      },

    # -------------------------------------------------------------
    # LESSON 11: Reg. 3.5
    # -------------------------------------------------------------
    {
        'filename': 'reg-3-5-amenity-space-provision.html',
        'lesson_id': 'lesson-reg-3-5',
        'quiz_id': 'quiz-reg-3-5',
        'clause': 'Reg. 3.5',
        'title': 'Provision for Amenity Space in Layouts',
        'badge_status': 'Core Master Planning',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Statutory Amenity Space provision under UDCPR Reg. 3.5.1. 1% to 5% layout quotas, handing over to the municipal authority, and retention rules.',
        'lead_summary': 'Learn the rules governing mandatory Amenity Space in Maharashtra layouts: statutory percentages (1% to 5%), how to compute eligible land area, and developer options for handing over vs. retaining.',
        'amendment_cite': 'CR.42/21',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            In addition to green recreational open spaces, large layouts must provide <strong>Amenity Space</strong> for civic social infrastructure such as primary schools, dispensaries, electric substations, and post offices under Regulation 3.5.1.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Municipal Corporation Tier:</strong> On plots &gt; 20,000 sq.m (2 ha), <strong>5% of gross area</strong> (minus DP roads/reservations) must be surrendered or provided as Amenity Space.</li>
            <li><strong>Municipal Councils & Nagar Panchayats:</strong> Reduced statutory percentage, typically <strong>2% to 3%</strong>.</li>
            <li><strong>Surrender vs Retention:</strong> If handed over to the Planning Authority, the owner receives 100% in-situ FSI or TDR credit. Alternatively, the owner can develop permitted public amenities directly on site.</li>
          </ul>
        """,
        'statutory_extract': "In the areas of Local Authorities, Special Planning Authorities and Metropolitan Region Development Authorities, Amenity Space on gross area after deducting area under reservations / roads in Development Plan shall have to be provided in any layout or sub-division of land or proposal for development...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">Amenity Space Compensation</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              When amenity land is conveyed to the Planning Authority free of encumbrance, the developer receives an equivalent quantum of FSI credited to the balance layout land, or is issued a Development Rights Certificate (DRC / TDR) under Chapter 11.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_011 // AMENITY BREAKDOWN</span>
              <span class="fig-title">Amenity Space Computation and Surrender Mechanics (Reg. 3.5)</span>
            </div>
            <div style="padding:16px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              AMENITY SPACE DEDUCTION (MUNICIPAL CORPORATIONS)<br>
              ├── Plots &lt; 4,000 sq.m &rarr; 0% (Exempt)<br>
              ├── Plots 4,000 to 20,000 sq.m &rarr; Retention or Surrender as per local schedule<br>
              └── Plots &gt; 20,000 sq.m (2.0 ha) &rarr; Mandatory 5% Amenity Space<br>
                   ├── Option A: Hand over land to Authority &rarr; Get 100% FSI / TDR Credit<br>
                   └── Option B: Retain and construct approved civic utility
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: 30,000 sq.m Layout in PMC limits</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A 30,000 sq.m plot has a 24m DP road passing through it occupying 2,000 sq.m.
            </p>
            <div class="worked-step">
              <span class="step-badge">STEP 1</span>
              <div>Eligible Gross Area = 30,000 - 2,000 (DP Road) = 28,000 sq.m.</div>
            </div>
            <div class="worked-step">
              <span class="step-badge">STEP 2</span>
              <div>Plot &gt; 20,000 sq.m &rarr; Amenity Space = 28,000 &times; 0.05 = <strong>1,400 sq.m mandatory Amenity Space.</strong></div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Overlapping Recreational Open Space with Amenity Space</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Recreational Open Space (10% ROS under Reg. 3.4.1) and Amenity Space (Reg. 3.5.1) are two completely separate statutory requirements. They must be demarcated as separate pockets and cannot be merged into a single pocket.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarifications issued under letter CR.42/21/UD-12 settled the procedure for earlier sanctioned layouts seeking revision where amenity space was already provided or surrendered.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the statutory Amenity Space percentage on plots exceeding 20,000 sq.m in Municipal Corporation areas?",
            'options': [
              "2%",
              "5%",
              "10%",
              "15%"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 3.5.1, layouts exceeding 20,000 sq.m in Municipal Corporation jurisdictions require a mandatory 5% amenity space provision."
          },
          {
            'question': "Can an applicant count the 10% Recreational Open Space (ROS) as part of their Amenity Space?",
            'options': [
              "Yes, always",
              "No, ROS (Reg. 3.4) and Amenity Space (Reg. 3.5) are separate statutory requirements",
              "Only in gaothan congested areas",
              "Only if an electric substation is built"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.5 explicitly states that Amenity Space is in addition to the Recreational Open Space mandated under Regulation 3.4."
          }
        ],
        'prev_url': '/lessons/reg-3-4-1-recreational-open-space.html',
        'prev_title': 'Reg. 3.4.1 Open Space',
        'next_url': '/lessons/reg-3-8-inclusive-housing.html',
        'next_title': 'Reg. 3.8 Inclusive Housing'
      },

    # -------------------------------------------------------------
    # LESSON 12: Reg. 3.8
    # -------------------------------------------------------------
    {
        'filename': 'reg-3-8-inclusive-housing.html',
        'lesson_id': 'lesson-reg-3-8',
        'quiz_id': 'quiz-reg-3-8',
        'clause': 'Reg. 3.8',
        'title': 'Provision for Inclusive Housing (EWS / LIG)',
        'badge_status': 'Core Affordable Housing',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Mandatory 20% affordable housing (EWS/LIG) obligation under UDCPR Reg. 3.8 on plots >= 4,000 sq.m in Municipal Corporations.',
        'lead_summary': 'Master the social housing mandate in Maharashtra: the 4,000 sq.m plot threshold, 20% affordable housing reservation, handing over tenements to MHADA, and the 25% incentive FSI perk.',
        'amendment_cite': None,
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            To ensure balanced social development, Regulation 3.8 imposes a statutory <strong>Inclusive Housing obligation</strong> on all large private residential developments in Municipal Corporation jurisdictions.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Applicability Threshold:</strong> Any residential layout or building proposal on land measuring <strong>4,000 sq.m or more</strong>.</li>
            <li><strong>The 20% Mandate:</strong> Exactly <strong>20% of the Basic FSI area</strong> must be constructed as affordable tenements for Economically Weaker Sections (EWS) and Low Income Groups (LIG).</li>
            <li><strong>Tenement Sizes:</strong> Carpet area strictly between <strong>30.0 sq.m and 45.0 sq.m</strong>.</li>
            <li><strong>Handover to MHADA:</strong> Built units are handed over to the Maharashtra Housing and Area Development Authority (MHADA) at pre-determined construction rates, or alloted to beneficiaries via MHADA lottery.</li>
            <li><strong>Incentive FSI (Reg. 3.8.3):</strong> If a developer provides inclusive housing, they receive an additional <strong>25% incentive FSI</strong> of the inclusive housing land on their remaining plot.</li>
          </ul>
        """,
        'statutory_extract': "The provision regarding inclusive housing shall be applicable in the areas of Municipal Corporations... for layout or sub-division of land or proposal for development having area 4,000 sq.m or more for residential purpose, 20% of the basic FSI area shall be constructed for EWS / LIG tenements...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-emerald);">Incentive FSI Entitlement (Reg. 3.8.3)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              In addition to basic entitlement, the developer is entitled to an extra 25% FSI of the land area covered under inclusive housing, usable on their balance market-sale plot.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_012 // INCLUSIVE HOUSING</span>
              <span class="fig-title">Affordable Housing Allocation on Plots &ge; 4,000 sq.m</span>
            </div>
            <div style="padding:16px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              INCLUSIVE HOUSING OBLIGATION (REG. 3.8)<br>
              ├── Plot Area &lt; 4,000 sq.m &rarr; EXEMPT (Zero affordable units required)<br>
              └── Plot Area &ge; 4,000 sq.m (Municipal Corporations)<br>
                   ├── Mandatory: 20% of Basic FSI Area built as EWS/LIG flats<br>
                   ├── Flat Carpet Sizes: 30 to 45 sq.m<br>
                   └── Developer Benefit: 25% Incentive FSI of affordable land
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: 6,000 sq.m Residential Scheme in Thane</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A developer has a 6,000 sq.m plot in TMC limits. Basic FSI is 1.10. Basic BUA = 6,600 sq.m.
            </p>
            <div class="worked-step">
              <span class="step-badge">CALCULATION</span>
              <div>20% of Basic BUA = 6,600 &times; 0.20 = <strong>1,320.00 sq.m</strong> built-up area for affordable housing.</div>
            </div>
            <div class="worked-step">
              <span class="step-badge">UNITS SIZING</span>
              <div>At an average carpet area of 35 sq.m (~40 sq.m BUA), this yields <strong>approx. 33 affordable homes</strong>.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Selling Inclusive Housing Units on the Open Market</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Developers cannot sell these units privately. They must obtain MHADA NOC and hand over list to MHADA for allotment via official state government lottery lists.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Regulation 3.8.4 was clarified to exempt public auction plots if auctioned without inclusive housing conditions prior to the commencement of UDCPR-2020.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the plot area threshold for mandatory Inclusive Housing under Regulation 3.8?",
            'options': [
              "1,000 sq.m",
              "2,000 sq.m",
              "4,000 sq.m",
              "10,000 sq.m"
            ],
            'correctAnswer': 2,
            'explanation': "Under Regulation 3.8, the 20% Inclusive Housing obligation triggers on residential plots measuring 4,000 sq.m or more in Municipal Corporation areas."
          },
          {
            'question': "What is the permitted carpet area range for EWS/LIG tenements under Regulation 3.8?",
            'options': [
              "15 to 25 sq.m",
              "30 to 45 sq.m",
              "60 to 75 sq.m",
              "Any size the developer chooses"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.8 stipulates that inclusive housing flats must have a carpet area between 30 sq.m and 45 sq.m."
          }
        ],
        'prev_url': '/lessons/reg-3-5-amenity-space-provision.html',
        'prev_title': 'Reg. 3.5 Amenity Space',
        'next_url': '/lessons/reg-3-9-net-plot-area-computation.html',
        'next_title': 'Reg. 3.9 Net Plot Area'
      },

    # -------------------------------------------------------------
    # LESSON 13: Reg. 3.9
    # -------------------------------------------------------------
    {
        'filename': 'reg-3-9-net-plot-area-computation.html',
        'lesson_id': 'lesson-reg-3-9',
        'quiz_id': 'quiz-reg-3-9',
        'clause': 'Reg. 3.9',
        'title': 'Net Plot Area & Computation of FSI',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Compute Net Plot Area under UDCPR Regulation 3.9. Statutory deductions for DP road widening, public reservations, and surrendered amenity spaces.',
        'lead_summary': 'Learn how to accurately compute Net Plot Area from gross survey measurements: deductions for DP road widening, public reservations, and amenity surrenders, and how FSI potential applies.',
        'amendment_cite': None,
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            The starting point for every building sanction drawing in Maharashtra is the <strong>Net Plot Area</strong> computation under Regulation 3.9. Net Plot Area is the physical land envelope left for development after carving out public municipal encumbrances.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Gross Plot Area:</strong> Total certified area from 7/12 land revenue extract or CTS property card.</li>
            <li><strong>Deductions:</strong> Land affected by DP road widening + Land affected by DP public reservations + Amenity space surrendered to authority.</li>
            <li><strong>FSI Calculation Rule (Reg. 6.3 Note xiv):</strong> Even though Net Plot Area is smaller, building potential is calculated on the gross area after deducting only DP road area, while surrendered land is compensated via in-situ FSI or TDR!</li>
          </ul>
        """,
        'statutory_extract': "Net Plot Area: For the purpose of computing FSI / built-up area, the net plot area shall be the gross plot area after deducting the area under Development Plan roads / road widening, reservations in Development Plan and amenity space handed over to the Authority...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">In-Situ FSI Compensation (Reg. 3.10)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              When land is surrendered for DP roads or reservations without monetary compensation, the owner receives 100% in-situ FSI or TDR credit, ensuring zero loss of development potential.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_013 // NET PLOT DERIVATION</span>
              <span class="fig-title">Net Plot Area Deduction Formula (Reg. 3.9)</span>
            </div>
            <div style="padding:16px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              NET PLOT COMPUTATION FORMULA<br>
              GROSS PLOT AREA (from Property Card)<br>
              ├── [-] Area under Sanctioned DP Road / Road Widening<br>
              ├── [-] Area under Public DP Reservations (Gardens, Schools)<br>
              ├── [-] Area under Amenity Space handed over (Reg. 3.5)<br>
              └── [=] NET PLOT AREA (Buildable Site Footprint)
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Computing Net Plot Area on a 15,000 sq.m Plot</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A plot in PCMC measures 15,000 sq.m. A 30m DP road affects 1,500 sq.m, and a school reservation affects 2,000 sq.m. The 5% amenity space (575 sq.m) is surrendered.
            </p>
            <div class="worked-step">
              <span class="step-badge">DEDUCTIONS</span>
              <div>Total Deductions = 1,500 (Road) + 2,000 (School) + 575 (Amenity) = 4,075 sq.m.</div>
            </div>
            <div class="worked-step">
              <span class="step-badge">NET AREA</span>
              <div>Net Plot Area = 15,000 - 4,075 = <strong>10,925 sq.m.</strong></div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Deducting Recreational Open Space (ROS) from Net Plot</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Recreational Open Space (10% ROS) is NOT surrendered to the authority; it remains private common property of the housing society. It must never be subtracted when arriving at Net Plot Area.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarifications issued under Section 154 confirmed that where amenity space is retained by the developer under Reg. 3.5.1, it remains part of the net plot for FSI computation.
          </p>
        """,
        'quiz': [
          {
            'question': "Which of the following items is NOT deducted from gross plot area to calculate Net Plot Area under Reg. 3.9?",
            'options': [
              "DP Road widening area",
              "Public DP reservation area",
              "Recreational Open Space (10% ROS)",
              "Amenity space surrendered to authority"
            ],
            'correctAnswer': 2,
            'explanation': "Recreational Open Space (ROS) is retained as private common property of the residents and is NOT deducted from Net Plot Area."
          },
          {
            'question': "How is a landowner compensated when they surrender land for a DP road under Regulation 3.10?",
            'options': [
              "They receive no compensation",
              "They receive 100% in-situ FSI on their balance land or TDR credit",
              "They are given a free municipal flat",
              "Their property tax is waived for 50 years"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 3.10 and Chapter 11, landowners surrendering land for DP roads receive 100% equivalent in-situ FSI or TDR credit."
          }
        ],
        'prev_url': '/lessons/reg-3-8-inclusive-housing.html',
        'prev_title': 'Reg. 3.8 Inclusive Housing',
        'next_url': '/chapters/ch03.html',
        'next_title': 'Chapter 3 Hub'
      }
]

for l in lessons_batch2:
    create_lesson_page(l)

print(f"Successfully generated batch 2: {len(lessons_batch2)} lessons.")
