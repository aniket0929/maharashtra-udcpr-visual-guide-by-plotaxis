"""
UDCPR FROM SCRATCH - CHAPTER 3: LESSON 3.2
Module: scripts/ch03_lessons/lesson_3_2_internal_roads.py
Governing Regulation: Regulation 3.2 (Means of Access) & Regulation 3.3 (Land Sub-division and Layout)
Covers: Internal layout roads (Tables 3A, 3B, 3C, 3D, 3E), cul-de-sacs (9m radius), Special Building fire driveways, road chamfers/splays, and handover to Authority.
"""

lesson_data = {
    'filename': 'reg-3-3-internal-layout-roads.html',
    'lesson_id': 'lesson-reg-3-3',
    'quiz_id': 'quiz-reg-3-3',
    'clause': 'Reg. 3.2 & 3.3',
    'title': 'Means of Access, Internal Layout Roads & Special Building Driveways',
    'badge_status': 'Core Infrastructure',
    'ch_slug': 'ch03',
    'ch_title': 'Chapter 3: General Land Development',
    'meta_desc': 'Internal road width standards under UDCPR Regulation 3.2 & 3.3: Tables 3A to 3E (Residential, Commercial, Group Housing, Industrial), cul-de-sac 9m turning radius, acute junctions, and road handover.',
    'lead_summary': 'Master the statutory engineering standards for designing access roads and internal street networks in Maharashtra: Table 3A residential layout widths based on length, Table 3C group housing standards, pathway specifications, 9.0m radius cul-de-sacs, Special Building emergency fire driveways, junction splays, and public road handover protocols.',
    'amendment_cite': 'CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        Every plot or building in Maharashtra must have direct lawful access from a public or private street. Regulation 3.2 and 3.3 dictate the exact right-of-way (ROW) widths for internal roads based on length, land use, and traffic intensity.
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
        <li><strong>Means of Access (Reg. 3.2):</strong> Every building or plot must derive direct access from an existing or proposed public street or a private layout street of statutory width. Land-locked plots cannot obtain building permission until a legally registered right-of-way is secured (Reg. 3.3.14).</li>
        <li><strong>Residential Layout Roads (Reg. 3.3.2 &amp; Table 3A):</strong>
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li>Length up to <strong>150 m</strong> &rarr; Minimum <strong>9.00 m width</strong></li>
            <li>Length <strong>150 m to 300 m</strong> &rarr; Minimum <strong>12.00 m width</strong></li>
            <li>Length <strong>above 300 m</strong> &rarr; Minimum <strong>15.00 m width</strong></li>
          </ul>
        </li>
        <li><strong>Group Housing Scheme Roads (Reg. 3.3.2 &amp; Table 3C):</strong>
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li>Length up to <strong>150 m</strong> &rarr; Minimum <strong>7.50 m width</strong></li>
            <li>Length <strong>150 m to 300 m</strong> &rarr; Minimum <strong>9.00 m width</strong></li>
            <li>Length <strong>above 300 m</strong> &rarr; Minimum <strong>12.00 m width</strong></li>
          </ul>
        </li>
        <li><strong>Commercial &amp; Industrial Roads (Tables 3B &amp; 3D):</strong>
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li>Commercial: Minimum <strong>12.00 m</strong> up to 150m length; <strong>15.00 m</strong> above 150m.</li>
            <li>Industrial: Minimum <strong>12.00 m</strong> up to 150m; <strong>15.00 m</strong> for 150-300m; <strong>18.00 m</strong> above 300m.</li>
          </ul>
        </li>
        <li><strong>Pedestrian Pathways (Reg. 3.3.2(D) &amp; Table 3E):</strong> For accessing row-housing or low-income clusters: up to 20m length = 2.0m; up to 50m length = <strong>3.0m</strong>; up to 100m length = <strong>4.5m</strong>.</li>
        <li><strong>Measurement of Road Length (Reg. 3.3.3):</strong> Road length is measured along the centerline from the point of intersection with the wider main access road to the farthest dead-end or secondary junction.</li>
        <li><strong>Cul-de-sacs (Reg. 3.3.10):</strong> Dead-end streets are permitted up to a maximum length of <strong>150 m</strong>, provided an end turnaround circle with a <strong>radius not less than 9.0 meters</strong> (18m diameter) is provided for emergency and fire vehicle turning.</li>
        <li><strong>Intersections &amp; Splays (Reg. 3.3.12 &amp; 3.3.13):</strong> Road junctions must provide corner chamfers / splays. For acute-angled junctions (&lt; 60&deg;), rounded corners must be enlarged to maintain smooth sightlines and vehicular turning radii.</li>
        <li><strong>Handing Over of Layout Roads (Reg. 3.3.11):</strong> All internal layout roads in plotted subdivisions must be completely leveled, paved with water-bound macadam (WBM) or asphalt/concrete, provided with streetlights, storm drains, and sewer mains, and <strong>handed over to the Planning Authority free of cost</strong>.</li>
      </ul>
    """,
    'statutory_extract': "3.3.2 Roads / streets in Land Sub-division or Layout: The width of roads / streets / avenues including pathway shall conform to the tables given below... Table 3A Residential: Upto 150m = 9.00m; 150m to 300m = 12.00m; Above 300m = 15.00m... Table 3C Group Housing: Upto 150m = 7.50m; 150m to 300m = 9.00m; Above 300m = 12.00m... 3.3.10 Cul-de-sacs: Cul-de-sacs giving access to plots and extending upto 150 m. shall be allowed... with a turnaround area not less than 9.0 m. radius...",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 3.3.2 // TABLE 3A vs TABLE 3C</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Plotted Layout vs Group Housing</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            In plotted layouts (Table 3A), minimum road width starts at <strong>9.0 m</strong> because plots are independently titled and handed over to the municipality. In group housing (Table 3C), roads remain privately maintained on a single holding, so minimum width starts at <strong>7.5 m</strong>.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 3.3.10 // DEAD-END TURNAROUND</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Cul-de-sac 9.0m Radius</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Dead-end streets longer than 50m must terminate in a circular turning bulb with a <strong>minimum radius of 9.0 meters</strong> (or an equivalent T-turnaround) to allow municipal garbage trucks and fire engines to turn without reversing.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_015 // STATUTORY INTERNAL ROAD WIDTH MATRIX</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">TABLES 3A, 3B, 3C, 3D &amp; 3E SPECIFICATION</span>
        </div>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11.5px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Development Type</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Governing Table</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Length &le; 150 m</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">150 m &lt; Length &le; 300 m</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Length &gt; 300 m</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Residential Plotted Layout</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Table 3A</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">9.00 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">12.00 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">15.00 m</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Commercial Layout</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Table 3B</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">12.00 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">15.00 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">18.00 m</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Group Housing Scheme</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Table 3C</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700; color:var(--blueprint);">7.50 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700; color:var(--blueprint);">9.00 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700; color:var(--blueprint);">12.00 m</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Industrial Layout</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Table 3D</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">12.00 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">15.00 m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">18.00 m</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Pedestrian Pathway</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Table 3E</td>
                <td colspan="3" style="padding:6px 8px; text-align:center; border:1px solid var(--line-strong);">
                  Length &le; 20m: 2.0m &bull; Length &le; 50m: 3.0m &bull; Length &le; 100m: 4.5m
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="margin-bottom:12px;">
        <strong>Layout Road Engineering Case Study:</strong> A developer designs a plotted residential subdivision on a <strong>3.5 Ha land parcel</strong>. The main spine road extends <strong>280 metres</strong> from the municipal 24m DP road and then forks into two branch roads:
      </p>
      <div class="worked-step">
        <span class="step-badge">SPINE ROAD</span>
        <div>
          The spine road length is <strong>280 m (between 150m and 300m)</strong>.
          <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; TABLE 3A RULE:</span> Minimum road width must be <strong>12.00 metres</strong>.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">DEAD-END BRANCH</span>
        <div>
          Branch Road 'A' is a dead-end cul-de-sac of length <strong>110 metres (&le; 150 m)</strong> serving 14 plots.
          <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; TABLE 3A RULE:</span> Minimum width = <strong>9.00 metres</strong>.
          <br><span style="font-family:var(--mono); color:var(--amber);">&#10003; CUL-DE-SAC MANDATE (Reg. 3.3.10):</span> At the 110m terminus, a turnaround bulb with a <strong>minimum radius of 9.0 m</strong> (18m diameter) is provided.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">JUNCTION SPLAY</span>
        <div>
          At the intersection of the 12m spine road and the 9m branch road, <strong>corner splays of 3m &times; 3m</strong> are carved out of corner plots under Reg. 3.3.12 to ensure sightlines.
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ STATUTORY COMPLIANCE: The layout satisfies all width, length measurement, cul-de-sac turning, and junction splay regulations.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Applying Group Housing Road Widths (Table 3C) to Plotted Subdivisions</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Draftsmen frequently attempt to provide 7.5 m roads in plotted subdivisions to maximize saleable land. Table 3C (7.5m) applies <strong>exclusively to Group Housing Schemes</strong>. Plotted layouts are governed by Table 3A, where the absolute minimum road width is <strong>9.00 m</strong>.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Cul-de-sac Exceeding 150 Metres Without Turnaround</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under Regulation 3.3.10, dead-end roads can extend up to <strong>150 m maximum</strong> and must provide a <strong>9.0m radius turning circle</strong>. Creating 180m dead-end roads or omitting the turning bulb prevents emergency fire tender entry and triggers layout rejection.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 3: Failing to Coordinate Roads with Adjoining Land Holdings</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under Regulation 3.3.4, internal layout roads must be coordinated with existing or approved roads in adjoining lands to ensure street network continuity. Terminating an internal road against a neighbor's boundary without connecting to an existing right-of-way will be rejected by the Planning Authority.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Group Housing Table 3C &amp; Special Building Alignment</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Harmonized Group Housing internal road widths under Table 3C with CFO fire engine access pathways, confirming that a 7.5 m road satisfies the 6.0 m clear motorable requirement for Special Buildings.
      </p>
    """,
    'quiz': [
        {
            'question': 'In a Residential Plotted Layout under Table 3A, what is the mandatory road width for an internal street with a length between 150 m and 300 m?',
            'options': [
                '7.50 metres',
                '9.00 metres',
                '12.00 metres',
                '15.00 metres'
            ],
            'correctAnswer': 2,
            'explanation': "Table 3A mandates that for internal residential layout roads with lengths between 150 m and 300 m, the required width is 12.00 metres."
        },
        {
            'question': 'What is the minimum statutory turning circle radius for a cul-de-sac (dead-end road) under Regulation 3.3.10?',
            'options': [
                'Radius not less than 4.5 metres',
                'Radius not less than 6.0 metres',
                'Radius not less than 9.0 metres',
                'Radius not less than 15.0 metres'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.3.10 explicitly provides that cul-de-sacs extending up to 150 m must terminate with a turnaround area having a 'radius not less than 9.0 meters'."
        },
        {
            'question': 'What is the minimum permissible road width for internal roads in a Group Housing Scheme for lengths up to 150 m under Table 3C?',
            'options': [
                '6.00 metres',
                '7.50 metres',
                '9.00 metres',
                '12.00 metres'
            ],
            'correctAnswer': 1,
            'explanation': "Under Table 3C of Regulation 3.3.2, internal roads in Group Housing Schemes with length up to 150 m require a minimum width of 7.50 metres."
        },
        {
            'question': 'What is the maximum permissible length of a pedestrian pathway with a width of 3.0 metres under Table 3E?',
            'options': [
                'Up to 20 metres',
                'Up to 50 metres',
                'Up to 100 metres',
                'Unlimited length'
            ],
            'correctAnswer': 1,
            'explanation': "Table 3E (Pathways) specifies that a 3.0 m wide pathway is permissible for lengths up to 50 metres."
        }
    ],
    'prev_url': '/lessons/reg-3-1-site-clearance-buffers.html',
    'prev_title': 'Reg. 3.1 Site Buffers',
    'next_url': '/lessons/reg-3-4-1-recreational-open-space.html',
    'next_title': 'Reg. 3.4 Recreational Open Space'
}
