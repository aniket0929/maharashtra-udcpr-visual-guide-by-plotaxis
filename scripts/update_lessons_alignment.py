import os
import re
import sys
from generate_lessons import create_lesson_page

sys.stdout.reconfigure(encoding='utf-8')

# Re-generate refined lessons to match exact source phrases
updated_lessons = [
    # Refined Reg 1.1
    {
        'filename': 'reg-1-1-jurisdiction-and-extent.html',
        'lesson_id': 'lesson-reg-1-1',
        'quiz_id': 'quiz-reg-1-1',
        'clause': 'Reg. 1.1 & 1.2',
        'title': 'Extent, Jurisdiction & Commencement of UDCPR',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Jurisdictional boundaries of Maharashtra UDCPR-2020: Where the regulations apply, excluded areas (MCGM, MIDC, NAINA), and commencement date.',
        'lead_summary': 'Learn the exact geographical and administrative jurisdiction of UDCPR-2020 across Maharashtra, understand which planning authorities are covered, and identify excluded municipal zones.',
        'amendment_cite': None,
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            The <strong>Unified Development Control and Promotion Regulations (UDCPR-2020)</strong> replaced dozens of disparate municipal and regional building by-laws with a single unified regulatory code across the State of Maharashtra.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Effective Date:</strong> Sanctioned by the Government under Section 37(1AA) and Section 20(4) of the MRTP Act, 1966 on <strong>02<sup>nd</sup> December, 2020</strong>.</li>
            <li><strong>Territorial Scope:</strong> Applies to all Municipal Corporations (except Mumbai), Municipal Councils, Nagar Panchayats, Non-Municipal Planning Authorities, and Regional Plan areas across Maharashtra.</li>
            <li><strong>Critical Exclusions:</strong> Does NOT apply to Municipal Corporation of Greater Mumbai (MCGM), MIDC, NAINA, Jawaharlal Nehru Port Trust (JNPT), Hill Station Municipal Councils, and notified Eco-Sensitive regions.</li>
          </ul>
        """,
        'statutory_extract': "These regulations shall apply to the building activities and development works on lands within the jurisdiction of all Planning Authorities and Regional Plan areas in Maharashtra State, excluding the Municipal Corporation of Greater Mumbai, other Planning Authorities / Special Planning Authorities within the limit of MCGM, MIDC, NAINA, Jawaharlal Nehru Port Trust, Hill Station Municipal Councils, Eco-sensitive / Eco-fragile regions...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-emerald);">Included Jurisdictions</h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                Pune (PMC), Thane (TMC), Nagpur (NMC/NMRDA), Nashik (NMC), Pimpri-Chinchwad (PCMC), Navi Mumbai (NMMC), Kalyan-Dombivli (KDMC), Vasai-Virar, Kolhapur, Solapur, Aurangabad, and all Regional Plan villages.
              </p>
            </div>
            <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-rose);">Excluded Jurisdictions</h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                Mumbai City & Suburbs (MCGM DCPR-2034), MIDC industrial estates, NAINA special planning area, JNPT port limits, and Lonavala / Mahabaleshwar Eco-sensitive zones.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_005 // JURISDICTION MATRIX</span>
              <span class="fig-title">Maharashtra Development Control Applicability Tree</span>
            </div>
            <div style="padding:16px 8px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              MAHARASHTRA STATE PLANNING JURISDICTION<br>
              ├── [APPLICABLE] UDCPR-2020 (Sanctioned 02<sup>nd</sup> December, 2020)<br>
              │    ├── All Municipal Corporations (Pune, Thane, Nagpur, Nashik, etc.)<br>
              │    ├── All 'A', 'B', 'C' Class Municipal Councils & Nagar Panchayats<br>
              │    ├── Regional Plan Areas (PMRDA, NMRDA, District Zilla Parishad Areas)<br>
              │    └── Special Planning Authorities outside MCGM limits<br>
              └── [EXCLUDED] SEPARATE REGULATIONS<br>
                   ├── Mumbai Metropolis &rarr; MCGM DCPR-2034<br>
                   ├── Industrial Hubs &rarr; MIDC Regulations<br>
                   ├── Airport Belt &rarr; NAINA Regulations<br>
                   └── Notified Eco-Sensitive Zones &rarr; MoEF & CC Guidelines
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Determining Applicable Code for an Industrial Plot</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              An engineer is designing a factory in Chakan, Pune. Plot A is inside an MIDC notified industrial park; Plot B is 200m away on private agricultural land converted to industrial use under Pune Regional Plan.
            </p>
            <div class="worked-step">
              <span class="step-badge">PLOT A</span>
              <div>Plot A is within MIDC jurisdiction &rarr; <strong>MIDC Development Control Regulations apply (Exempt from UDCPR).</strong></div>
            </div>
            <div class="worked-step">
              <span class="step-badge">PLOT B</span>
              <div>Plot B is outside MIDC in Regional Plan limits &rarr; <strong>UDCPR-2020 Chapter 4 & Chapter 6 apply fully.</strong></div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Applying UDCPR clauses within Mumbai City / MCGM</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Junior architects frequently cite UDCPR FSI tables for projects in Mumbai suburbs. MCGM is governed exclusively by DCPR-2034. UDCPR has zero legal validity within Mumbai Municipal limits.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Sanctioned under Section 37(1AA)(c) and Section 20(4) of the MRTP Act, 1966 vide Notification No. TPS-1818/C.R.236/18/DP&RP/Sec.37(1AA)(c) & Sec.20(4)/UD-13 on 02<sup>nd</sup> December, 2020.
          </p>
        """,
        'quiz': [
          {
            'question': "Which of the following Planning Authorities is EXCLUDED from the scope of UDCPR-2020?",
            'options': [
              "Pune Municipal Corporation (PMC)",
              "Municipal Corporation of Greater Mumbai (MCGM)",
              "Nagpur Municipal Corporation (NMC)",
              "Thane Municipal Corporation (TMC)"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.1, the Municipal Corporation of Greater Mumbai (MCGM) is explicitly excluded from UDCPR and is governed by its own DCPR-2034."
          }
        ],
        'prev_url': '/chapters/ch01.html',
        'prev_title': 'Chapter 1 Hub',
        'next_url': '/lessons/reg-1-3-statutory-definitions.html',
        'next_title': 'Reg. 1.3 Definitions'
    },

    # Refined Reg 3.1
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
        'lead_summary': 'Learn the mandatory safety buffers required before any construction can be sited: flood lines along rivers, minor water course offsets (6.0m), overhead electric lines, railway boundary offsets (30.0m), and wetland buffers (50.0m).',
        'amendment_cite': 'Order CR.236/18',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            Even if a plot is zoned residential in a Development Plan, physical site constraints can restrict buildability. Regulation 3.1 establishes inviolable safety buffers from water bodies, high-voltage electric corridors, railway tracks, and defence boundaries.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>River Blue & Red Flood Lines (Reg. 3.1.3):</strong> Area within the Blue Flood Line is a <em>prohibitive zone</em> where no new construction is permissible. The area between the Blue Flood Line and Red Flood Line is a <em>restrictive zone</em>.</li>
            <li><strong>Minor Water Course Buffer (Reg. 3.1.1.ii):</strong> Minimum <strong>6.0 m.</strong> clearance from the edge of water mark of a minor water course or stream.</li>
            <li><strong>Wetland Buffer (Reg. 3.1.1.xiv):</strong> Minimum <strong>50.0 m.</strong> from the mean high flood level of a wetland.</li>
            <li><strong>Electric Lines Clearance (Reg. 3.1.2 Table 3-1):</strong> Low/medium voltage: 2.50m vertical / 1.20m horizontal. High voltage lines up to 33,000 V: 3.70m vertical / 2.00m horizontal.</li>
            <li><strong>Railway Boundary (Reg. 3.1.4):</strong> For any construction <strong>within 30.0 m. from railway boundary</strong>, a No Objection Certificate from Railway Authority is mandatory.</li>
          </ul>
        """,
        'statutory_extract': "No piece of land shall be used as a site for the construction of building if the entire site is within a distance of 6.0 m. from the edge of water mark of a minor water course... If it is within the river and blue flood line of the river (prohibitive zone)... For any construction within 30.0 m. from railway boundary, No Objection Certificate from Railway Authority shall be mandatory...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">Construction within Blue and Red Flood Line (Reg. 3.1.3)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              The Red Flood Line (once in 100 years flood) and Blue Flood Line (once in 25 years flood) are established by the Irrigation Department. In the restrictive zone (between blue and red lines), plinth level must be constructed at least 0.45m above the Red Flood Line.
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
              INFRASTRUCTURE CLEARANCE OFFSETS (STATUTORY)<br>
              ├── Minor Water Course &rarr; 6.0 m. from edge of water mark (Reg. 3.1.1.ii)<br>
              ├── Wetland Mean High Flood &rarr; 50.0 m. Buffer (Reg. 3.1.1.xiv)<br>
              ├── Railway Boundary &rarr; Mandatory NOC within 30.0 m. (Reg. 3.1.4)<br>
              ├── Electric Low & Medium Voltage &rarr; 1.20m Horizontal / 2.50m Vertical (Reg. 3.1.2)<br>
              ├── Electric High Voltage up to 33,000 V &rarr; 2.00m Horizontal / 3.70m Vertical<br>
              └── Blue Flood Line (Prohibitive Zone) &rarr; Zero new construction permitted
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Siting a Building Abutting a Stream & Railway Track</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A site in Pune abuts a natural minor stream on the north and a Central Railway track on the south.
            </p>
            <div class="worked-step">
              <span class="step-badge">NORTH BUFFER</span>
              <div>Must leave a clear 6.0 m. setback from the high water mark of the stream under Reg. 3.1.1.ii.</div>
            </div>
            <div class="worked-step">
              <span class="step-badge">SOUTH BUFFER</span>
              <div>If the building line falls within 30.0 m. of the railway boundary, a Railway NOC is mandatory under Reg. 3.1.4.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Encroaching into Blue Flood Line</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                No municipal commissioner has discretionary power to sanction new buildings inside the Blue Flood Line prohibitive zone. Siting any habitable structure here triggers immediate stop-work orders.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarification Order No. CR.236/18 (Part 2) dt. 23 Dec 2021 reiterated that Blue Line flood levels determined by the Irrigation Department take strict precedence over any municipal zoning map.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the minimum statutory buffer required from the edge of a minor water course under Regulation 3.1.1.ii?",
            'options': [
              "3.0 m.",
              "6.0 m.",
              "9.0 m.",
              "15.0 m."
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.1.1(ii) prescribes that no building shall be erected within a distance of at least 6.0 m. from the edge of water mark of a minor water course."
          },
          {
            'question': "What is the distance within which a Railway NOC is mandatory under Regulation 3.1.4?",
            'options': [
              "within 10.0 m.",
              "within 15.0 m.",
              "within 30.0 m.",
              "within 50.0 m."
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.1.4 mandates that for any construction within 30.0 m. from railway boundary, an NOC from Railway Authority is mandatory."
          }
        ],
        'prev_url': '/lessons/reg-2-6-commencement-and-occupancy.html',
        'prev_title': 'Reg. 2.6 – 2.11 Certificates',
        'next_url': '/lessons/reg-3-3-internal-layout-roads.html',
        'next_title': 'Reg. 3.3 Layout Roads'
    },

    # Refined Reg 3.3
    {
        'filename': 'reg-3-3-internal-layout-roads.html',
        'lesson_id': 'lesson-reg-3-3',
        'quiz_id': 'quiz-reg-3-3',
        'clause': 'Reg. 3.3',
        'title': 'Means of Access & Internal Layout Road Widths',
        'badge_status': 'Core Master Planning',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Calculate internal layout road widths under UDCPR Regulation 3.3. Road width vs length thresholds under Table 3A, cul-de-sacs, turning radius, and road handing over.',
        'lead_summary': 'Learn how to plan internal circulation for plotted subdivisions and group housing layouts: road width requirements based on road length (Table 3A, 3B, 3C), cul-de-sac turnarounds, and acute angle junction roundoffs.',
        'amendment_cite': 'Order CR.236/18',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            Every plot or building in a layout must have independent, clear vehicular access. Under Regulation 3.3.2 and Table No. 3A, the required width of an internal street in residential developments is strictly governed by its <strong>length</strong>:
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Length Upto 150m (Table 3A):</strong> Minimum width of internal road in layout is <strong>9.00 m</strong>.</li>
            <li><strong>Length Above 150m and upto 300m:</strong> Minimum width of internal road in layout is <strong>12.00 m</strong>.</li>
            <li><strong>Length Above 300m:</strong> Minimum width of internal road in layout is <strong>15.00 m</strong>.</li>
            <li><strong>Group Housing Scheme (Table 3C):</strong> Upto 150m: 7.50m; Above 150m and upto 300m: 9.00m; Above 300m and upto 600m: 12.00m; Above 600m: 15.00m.</li>
            <li><strong>Cul-de-sacs (Reg. 3.3.10):</strong> Dead-end streets up to 100m length must terminate in a turning circle with a radius not less than <strong>9.0 meters</strong>.</li>
          </ul>
        """,
        'statutory_extract': "Table No.3A - Internal Roads for Residential Development: Length of Internal Road Upto 150m requires 9.00m width; Above 150m and upto 300m requires 12.00m width; Above 300m requires 15.00m width... In case of group housing schemes, minimum width of internal roads shall be as per Table No.3C...",
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
                  <th style="padding:8px;">Road Length (Table 3A)</th>
                  <th style="padding:8px;">Residential Layout Width</th>
                  <th style="padding:8px;">Group Housing Width (Table 3C)</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">Upto 150m</td>
                  <td style="padding:8px; font-weight:700;">9.00 m</td>
                  <td style="padding:8px; font-family:var(--font-mono);">7.50 m</td>
                </tr>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">Above 150m and upto 300m</td>
                  <td style="padding:8px; font-weight:700;">12.00 m</td>
                  <td style="padding:8px; font-family:var(--font-mono);">9.00 m</td>
                </tr>
                <tr>
                  <td style="padding:8px; font-family:var(--font-mono);">Above 300m</td>
                  <td style="padding:8px; font-weight:700;">15.00 m</td>
                  <td style="padding:8px; font-family:var(--font-mono);">12.00 m (up to 600m)</td>
                </tr>
              </tbody>
            </table>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Sizing an Internal Street of 210m Length</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A residential plotted layout connects individual plots along a single internal spine road measuring 210 meters from the municipal main road.
            </p>
            <div class="worked-step">
              <span class="step-badge">EVALUATION</span>
              <div>Length is Above 150m and upto 300m &rarr; Under Table 3A, the minimum width must be <strong>12.00 m</strong>. A 9.00m road will be rejected during scrutiny.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Measuring Road Length from Center Instead of Furthest Point</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Under Regulation 3.3.3, road length must be measured from the farthest plot (or building) to the public street from which access is taken.
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
            'question': "What is the minimum required internal road width for a residential layout road length between 150m and 300m under Table 3A?",
            'options': [
              "6.00 m",
              "9.00 m",
              "12.00 m",
              "15.00 m"
            ],
            'correctAnswer': 2,
            'explanation': "Under Table 3A of Regulation 3.3.2, internal residential layout roads measuring between 150m and 300m in length must have a minimum width of 12.00 m."
          }
        ],
        'prev_url': '/lessons/reg-3-1-site-clearance-buffers.html',
        'prev_title': 'Reg. 3.1 Site Buffers',
        'next_url': '/lessons/reg-3-4-1-recreational-open-space.html',
        'next_title': 'Reg. 3.4.1 Open Space'
    },

    # Refined Reg 3.5
    {
        'filename': 'reg-3-5-amenity-space-provision.html',
        'lesson_id': 'lesson-reg-3-5',
        'quiz_id': 'quiz-reg-3-5',
        'clause': 'Reg. 3.5',
        'title': 'Provision for Amenity Space in Layouts',
        'badge_status': 'Core Master Planning',
        'ch_slug': 'ch03',
        'ch_title': 'Chapter 3: General Land Development',
        'meta_desc': 'Statutory Amenity Space provision under UDCPR Reg. 3.5.1. 5% layout quota for plots 20000 Sq.m. or more, handing over to the municipal authority, and retention rules.',
        'lead_summary': 'Learn the rules governing mandatory Amenity Space in Maharashtra layouts: statutory thresholds (5% on plots 20000 Sq.m. or more), how to compute eligible land area, and developer options for handing over to the Authority.',
        'amendment_cite': 'CR.104/2022',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            In addition to green recreational open spaces, large layouts must provide <strong>Amenity Space</strong> for civic social infrastructure such as primary schools, dispensaries, electric substations, and post offices under Regulation 3.5.1.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Statutory Table (Reg. 3.5.1 #):</strong><br>
                - Area less than 20000 Sq.m.: <strong>Nil</strong><br>
                - Area <strong>20000 Sq.m. or more</strong>: <strong>5% of the total area</strong>.
            </li>
            <li><strong>Approach Road:</strong> Amenity space shall be approachable by minimum 12.0 m. wide road.</li>
            <li><strong>Handing Over vs Retention:</strong> These amenity spaces may be developed by the owner for specified civic amenities (Garden, Playground, Municipal School, Municipal Hospital, Fire Brigade, Housing for PAP) or handed over to the Authority against FSI / TDR.</li>
          </ul>
        """,
        'statutory_extract': "In the areas of Local Authorities, Special Planning Authorities and Metropolitan Region Development Authorities, Amenity Space as mentioned below on gross area after deducting area under reservations / roads in Development Plan shall have to be provided: less than 20000 Sq.m. - Nil; 20000 Sq.m. or more - 5% of the total area... amenity space shall deem to be reservations / proposals in Development Plan...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">Amenity Space Compensation</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              When amenity land is conveyed and handed over to the Authority free of encumbrance, the developer receives an equivalent quantum of FSI credited to the balance layout land, or is issued a Development Rights Certificate (DRC / TDR) under Chapter 11.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_011 // AMENITY BREAKDOWN</span>
              <span class="fig-title">Amenity Space Computation Table (Reg. 3.5.1)</span>
            </div>
            <div style="padding:16px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              STATUTORY TABLE UNDER REGULATION 3.5.1<br>
              ├── Land Area less than 20000 Sq.m. &rarr; Nil (Exempt)<br>
              └── Land Area 20000 Sq.m. or more &rarr; 5% of the total area<br>
                   ├── Required Approach Road: Minimum 12.0 m. wide<br>
                   ├── Permitted Civic Uses: Garden, Playground, School, Hospital, Fire Brigade, PAP<br>
                   └── When handed over to the Authority &rarr; 100% in-situ FSI / TDR credited
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: 25,000 sq.m Layout in Pune</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A 25,000 sq.m layout has no DP road or reservations affecting it.
            </p>
            <div class="worked-step">
              <span class="step-badge">THRESHOLD</span>
              <div>Land area 25,000 sq.m &ge; 20000 Sq.m. threshold &rarr; 5% Amenity Space applies.</div>
            </div>
            <div class="worked-step">
              <span class="step-badge">AREA</span>
              <div>25,000 &times; 0.05 = <strong>1,250 sq.m mandatory Amenity Space</strong> approachable by 12.0m road.</div>
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
            Substituted vide Notification No. CR.236/18 (Part-3) dt. 16 June 2021 and Clarifications issued vide Order No. CR.104/2022 dt. 29 Nov 2022 established that amenity spaces under Reg. 3.5.1 deem to be reservations in Development Plans.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the statutory Amenity Space percentage on plots of 20000 Sq.m. or more under Regulation 3.5.1?",
            'options': [
              "Nil",
              "2%",
              "5% of the total area",
              "10%"
            ],
            'correctAnswer': 2,
            'explanation': "Under Regulation 3.5.1 Table, land areas of 20000 Sq.m. or more require 5% of the total area to be provided as Amenity Space."
          }
        ],
        'prev_url': '/lessons/reg-3-4-1-recreational-open-space.html',
        'prev_title': 'Reg. 3.4.1 Open Space',
        'next_url': '/lessons/reg-3-8-inclusive-housing.html',
        'next_title': 'Reg. 3.8 Inclusive Housing'
    }
]

for l in updated_lessons:
    create_lesson_page(l)

print("Updated targeted lessons successfully.")
