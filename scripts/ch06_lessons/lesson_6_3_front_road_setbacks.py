"""
UDCPR Visual Guide - CHAPTER 6, LESSON 3
Module: scripts/ch06_lessons/lesson_6_3_front_road_setbacks.py
Statutory Anchor: Regulation 6.1.1(ii) Table 6-B, Regulation 6.2.1 Table 6-D, & Regulation 6.2.6
Content: Front Road Setbacks, Congested vs Non-Congested Street Alignments, Corner Plots, and Height-Invariance
"""

lesson_data = {
    'filename': 'reg-6-2-front-setbacks-and-street-alignments.html',
    'lesson_id': '6.3',
    'quiz_id': 'quiz-6-3',
    'clause': 'Regulation 6.1.1(ii), 6.2.1 & 6.2.6',
    'title': 'Front Road Setbacks & Street Alignments',
    'badge_status': 'CORE STATUTORY SPECIFICATION',
    'ch_slug': 'ch06',
    'ch_title': 'Chapter 6: General Building Requirements - Setback, Marginal Distance, Height and Permissible FSI',
    'meta_desc': 'Understand UDCPR front road setback rules: Table 6-B congested street alignments, Table 6-D non-congested road widths, corner plot frontages, and height-invariance under Reg 6.2.3(a).',
    'lead_summary': 'Master the statutory street-front geometry of UDCPR: how front setbacks are determined strictly by abutting road width, how congested lanes require centerline widenings, and why front margins never increase with building height.',
    'amendment_cite': 'UDCPR-2020 Tables 6-B & 6-D, Clarification Order dt. 23rd Dec 2021, and Notification dt. 02nd Dec 2021',

    'plain_summary_html': """
      <p>
        Under UDCPR-2020, the <strong>Front Marginal Distance</strong> (or road setback) serves two statutory purposes: ensuring adequate light and air to the street canyon, and safeguarding the future right-of-way for vehicular circulation and municipal services.
      </p>
      <p>
        In <strong>Congested (Core) Areas</strong>, setbacks are governed by <strong>Table 6-B</strong>. For narrow lanes under 4.5m width, buildings must surrender an automatic setback of <strong>2.25m from the centerline</strong> of the street to establish an eventual 4.5m right-of-way. On streets between 4.5m and 6.0m, pure residential buildings enjoy a <strong>NIL</strong> front setback, while mixed-use requires 1.50m.
      </p>
      <p>
        In <strong>Outside Congested Areas</strong>, setbacks are governed by <strong>Table 6-D</strong>. On roads &lt; 15.0m, the front margin is <strong>3.0m</strong>; on roads 15.0m to &lt; 30.0m, it is <strong>4.5m</strong>; and on roads &ge; 30.0m, it expands to <strong>6.0m</strong> in A, B, and C Class Municipal Corporations.
      </p>
      <p>
        A foundational legal rule codified under <strong>Regulation 6.2.3(a)</strong> is that <em>front setbacks never scale with building height</em>: whether a tower is 15 meters or 100 meters tall, its front road margin remains anchored to Table 6-D!
      </p>
    """,

    'statutory_extract': """
### 6.1.1(ii) Front Marginal Distances / Setback in Congested Area (Table No. 6-B)
| Sr. No. | Road width | For Residential building | For Residential Buildings with mixed use |
| --- | --- | --- | --- |
| (i) | For streets / lane less than 4.5 m. width | 2.25 m. from the centre of the street / lane | 2.25 m. + 1.50 m. from the centre of the street / lane |
| (ii) | For streets 4.5 m. to less than 6.0 m. in width | NIL | 1.50 m. |
| (iii) | For streets 6.0 m. to less than 12.0 m. in width | 1.00 m. | 2.00 m. |
| (iv) | For streets 12.0 m. in width and above | 2.00 m. | 2.50 m. |

iv) For the lanes having width less than 4.5 m. abutting to any side of plot, a setback of 2.25 m. from the centre of lane shall be provided to make such lane 4.5 m. wide. No projections shall be permissible on such widened lane.

### 6.2.1 Marginal Distances and Set-back (Outside Congested Area - Table 6-D)
| Sr. No | Description of the road | Min. Plot Size | Min. width | Min. setback from road side in meters |
| --- | --- | --- | --- | --- |
| 1 | Roads of width 30.0 m. and above in local authority area | 450 sq.m. | 15 m | 6.0 m in A, B, C class Municipal Corporations; 4.50 m in other areas |
| 2 | Regional Plan area: NH / SH | 450 sq.m. | 15 m | 4.5 m or as specified by Highway rules whichever is more |
| 3 | Roads of width 18.0 m. and above but below 30.0 m. | 250 sq.m. | 10 m | 4.5 m |
| 4 | Roads of width 15.0 m. and above but below 18.0 m. | 200 sq.m. | 10 m | 3.0 m |
| 5 | Roads of width less than 15.0 m. | 80 sq.m. | 6 m | 3.0 m |
| 6 | Row Housing on roads of 12.0 m. and below | 30 sq.m. | 3.5 m | 2.25 m |
| 7 | Row Housing for EWS / LIG | 20 sq.m. | 3.0 m | 0.9 m from pathway or 2.25 m from road boundary |

### 6.2.3(a) Front Margin - Height Invariance
Front margin shall be as given in Table No.6-D shall be applicable to a building irrespective of its height.

### 6.2.6 Buildings Abutting Two or More Streets
When a Building abuts two or more streets, the setbacks from the streets shall be such as if the building is fronting on each of such streets.
    """,

    'clause_cards_html': """
      <div class="card-grid">
        <div class="card">
          <span class="kicker-card">CONGESTED LANES</span>
          <h3 class="card-title">Centerline Widening (Table 6-B)</h3>
          <p class="card-body">
            Where a gaothan lane is under 4.5m wide, construction must set back <strong>2.25m from the physical center line</strong> of the lane to widen it to 4.5m. For mixed-use, an extra 1.50m margin is required ($2.25\text{m} + 1.50\text{m} = 3.75\text{m}$ from center). No chajjas or balconies may project over this widened strip.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">NON-CONGESTED STANDARDS</span>
          <h3 class="card-title">Road-Width Tiers (Table 6-D)</h3>
          <p class="card-body">
            Front setbacks step up progressively based on road hierarchy:<br>
            • Roads &lt; 18.0m: <strong>3.0 m</strong> setback.<br>
            • Roads 18.0m to &lt; 30.0m: <strong>4.5 m</strong> setback.<br>
            • Roads &ge; 30.0m: <strong>6.0 m</strong> in Major Corps (4.5m in Councils).<br>
            • NH / SH in Regional Plans: <strong>4.5 m</strong> or Highway Ribbon rules.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">CRITICAL STATUTORY DOCTRINE</span>
          <h3 class="card-title">Height-Invariance (Reg 6.2.3a)</h3>
          <p class="card-body">
            Unlike side and rear margins that expand according to building height ($H/5$), the <strong>front road margin never changes with height</strong>. A 100-meter skyscraper on an 18.0m road requires the exact same 4.5m front setback as a 10-meter low-rise bungalow!
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">CORNER PLOTS</span>
          <h3 class="card-title">Multi-Street Frontages (Reg 6.2.6)</h3>
          <p class="card-body">
            If a plot abuts two or more roads (e.g., a corner plot on an 18m road and a 12m road), the building cannot designate one side as a "rear margin". It must provide the full statutory <strong>front setback applicable to each respective street</strong> (4.5m on the 18m road, and 3.0m on the 12m road).
          </p>
        </div>
      </div>
    """,

    'plate_or_table_html': """
      <div class="table-container">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>Zone / Setting</th>
              <th>Road Width Category</th>
              <th>Use Category</th>
              <th>Statutory Front Setback</th>
              <th>Governing Clause</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="4"><strong>Congested Area</strong><br>(Gaothan / Core)</td>
              <td>Lane &lt; 4.5 m</td>
              <td>Residential / Mixed</td>
              <td><strong>2.25 m from centerline</strong> (+ 1.5m for mixed)</td>
              <td>Table 6-B (i)</td>
            </tr>
            <tr>
              <td>4.5 m to &lt; 6.0 m</td>
              <td>Residential / Mixed</td>
              <td><strong>NIL</strong> for Res; <strong>1.50 m</strong> for Mixed</td>
              <td>Table 6-B (ii)</td>
            </tr>
            <tr>
              <td>6.0 m to &lt; 12.0 m</td>
              <td>Residential / Mixed</td>
              <td><strong>1.00 m</strong> for Res; <strong>2.00 m</strong> for Mixed</td>
              <td>Table 6-B (iii)</td>
            </tr>
            <tr>
              <td>12.0 m and above</td>
              <td>Residential / Mixed</td>
              <td><strong>2.00 m</strong> for Res; <strong>2.50 m</strong> for Mixed</td>
              <td>Table 6-B (iv)</td>
            </tr>
            <tr>
              <td rowspan="4"><strong>Outside Congested</strong><br>(Non-Congested Area)</td>
              <td>Roads &lt; 18.0 m</td>
              <td>All Permissible</td>
              <td><strong>3.00 m</strong></td>
              <td>Table 6-D (4, 5)</td>
            </tr>
            <tr>
              <td>18.0 m to &lt; 30.0 m</td>
              <td>All Permissible</td>
              <td><strong>4.50 m</strong></td>
              <td>Table 6-D (3)</td>
            </tr>
            <tr>
              <td>30.0 m and above</td>
              <td>Major Corporations</td>
              <td><strong>6.00 m</strong> (4.50 m in other areas)</td>
              <td>Table 6-D (1)</td>
            </tr>
            <tr>
              <td>NH / SH in RP Area</td>
              <td>National / State Hwy</td>
              <td><strong>4.50 m</strong> or Highway rules, whichever higher</td>
              <td>Table 6-D (2)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div style="margin-top: 24px;">
        <span class="kicker-card">TABLE 6-E • NON-RESIDENTIAL &amp; SPECIALIZED USE SETBACKS</span>
        <h4 style="font-family:var(--disp); font-size:1.1rem; font-weight:700; margin: 8px 0 12px 0;">
          Table 6-E: Margins for Institutional, Commercial, Assembly &amp; Utility Buildings
        </h4>
        <div class="table-container">
          <table class="drawing-table">
            <thead>
              <tr>
                <th>Category of Building</th>
                <th>Minimum Road Width</th>
                <th>Statutory Marginal Distances</th>
                <th>Special Stipulations</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Hospitals &amp; Clinics</strong><br>(Non-Special Building)</td>
                <td>9.0 m (Corps) / 7.5 m (Others)</td>
                <td>Table 6-D margins (min 3.0m side margin)</td>
                <td>Height subject to Fire Safety Act</td>
              </tr>
              <tr>
                <td><strong>Hospitals / Medical</strong><br>(Special Building &ge; 15m)</td>
                <td>Road for Special Bldgs (Reg 3.3.9)</td>
                <td><strong>6.0 m on all sides</strong></td>
                <td>Continuous 6.0m fire driveway mandatory</td>
              </tr>
              <tr>
                <td><strong>Schools (Primary &amp; Higher)</strong></td>
                <td>6.0 m (Primary) / 9.0 m (Others)</td>
                <td>Table 6-D (Primary); <strong>3.0 m on all sides</strong> (Other)</td>
                <td>Pre-primary allowed on any road</td>
              </tr>
              <tr>
                <td><strong>Cinema / Multiplex / Malls</strong></td>
                <td><strong>12.0 meters</strong></td>
                <td><strong>Front: 12.0 m</strong> (on 1 major road); <strong>6.0 m</strong> remaining sides</td>
                <td>Redevelopment: retain 1/3 seats (min 150); 20% ASR rate for extra capacity</td>
              </tr>
              <tr>
                <td><strong>Mangal Karyalaya / Banquets</strong></td>
                <td>R-2 road (Non-special) / 12.0 m (Special)</td>
                <td><strong>3.0 m on all sides</strong> (Non-special); <strong>6.0 m</strong> (Special)</td>
                <td>Special bldg fire tender access required</td>
              </tr>
              <tr>
                <td><strong>Fuel / EV Charging Stations</strong></td>
                <td><strong>9.0 meters</strong></td>
                <td><strong>4.5 m on all sides</strong></td>
                <td>NOC from CCOE/PESO; ancillary kiosk FSI &le; 0.25 (exempt from FSI)</td>
              </tr>
              <tr>
                <td><strong>Mercantile / Commercial</strong><br>(Special Building &ge; 15m)</td>
                <td>Road for Special Buildings</td>
                <td><strong>Front: 6.0 m</strong>; <strong>Side &amp; Rear: 6.0 m</strong></td>
                <td>Shops may face side/rear of plot</td>
              </tr>
              <tr>
                <td><strong>Stadium with Pavilion</strong></td>
                <td><strong>12.0 meters</strong></td>
                <td><strong>6.0 m on all sides</strong></td>
                <td>Spectator gallery &le; 25% exempt from FSI; under-stand shops exempt</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,

    'worked_example_html': r"""
      <div class="math-box">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:12px; color:var(--ink);">
          Worked Case: Setting Out Front Setbacks for a Corner Skyscraper
        </h4>
        <p><strong>Site Parameters:</strong></p>
        <ul>
          <li>Plot Location: Pune Municipal Corporation (Outside Congested Area).</li>
          <li>Plot Dimensions: Corner plot of <strong>40 m frontage &times; 50 m depth</strong> ($2,000\text{ sq.m}$).</li>
          <li>Abutting Roads: North side faces a <strong>24.0 m DP Road</strong>; East side faces a <strong>12.0 m Internal Layout Road</strong>.</li>
          <li>Proposed Building: High-rise residential tower of height $H = 60.0\text{ meters}$.</li>
        </ul>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint); padding-left: 14px;">
          <p><strong>Step 1: North Road Front Setback Determination</strong></p>
          <p>North road is 24.0m (falls in the 18.0m to &lt; 30.0m bracket of Table 6-D Sr. No. 3).
            $$\text{Statutory Front Setback (North)} = \mathbf{4.50\text{ meters}}$$
          </p>
          <p>Under Reg 6.2.3(a), does the 60m height increase this front margin? <strong>No.</strong> Front margins are strictly invariant with height.</p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--amber); padding-left: 14px;">
          <p><strong>Step 2: East Road Front Setback Determination (Reg 6.2.6)</strong></p>
          <p>Under Reg 6.2.6, because the building abuts two streets, the East side is treated as a fronting street, NOT a side margin!
            $$\text{East Road Width} = 12.0\text{ meters (falls in } < 15.0\text{m tier of Table 6-D Sr. No. 5)}$$
            $$\text{Statutory Front Setback (East)} = \mathbf{3.00\text{ meters}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint-soft); padding-left: 14px;">
          <p><strong>Step 3: Verification with Special Building Fire Driveway Rule</strong></p>
          <p>Because the building height is $60\text{m} \ge 15.0\text{m}$, it is a Special Building under Reg 1.3(93)(xiv). It requires a 6.0m clear unobstructed motorable driveway on all sides for fire tender access.</p>
          <p>Therefore, while statutory Table 6-D demands 4.5m and 3.0m, the fire driveway requirement mandates that the physical driveway layout accommodates at least <strong>6.0m clear width</strong> for firefighting apparatus!</p>
        </div>
      </div>
    """,

    'pitfalls_html': """
      <div class="panel-alert">
        <h4 style="font-family:var(--disp); font-weight:700; color:var(--brick); margin-bottom:8px;">
          HIGH-RISK PITFALLS IN FRONT SETBACK INTERPRETATION
        </h4>
        <ul style="margin-left: 18px; line-height: 1.6;">
          <li>
            <strong>Treating Corner Plot Secondary Frontage as a Side Margin:</strong> Architects often try to treat the narrower road of a corner plot as a side boundary to claim smaller offsets or allow projections. Under Regulation 6.2.6, <em>every abutting road requires full front setback</em>.
          </li>
          <li>
            <strong>Scaling Front Setbacks with H/5:</strong> Side and rear margins expand with $H/5$, but front margins are governed strictly by Table 6-D. Attempting to force $H/5$ on the front boundary wastes valuable plot footprint.
          </li>
          <li>
            <strong>Permitting Projections into Gaothan Centerline Widening:</strong> In congested lanes &lt; 4.5m, the 2.25m centerline setback strip must be kept completely clear. Projections, balconies, or canopies extending over this line are strictly prohibited by Table 6-B Note (iv).
          </li>
          <li>
            <strong>Overlooking Highway Ribbon Rules in RP Areas:</strong> For plots along National and State Highways in Regional Plan areas, if PWD Ribbon Development rules specify a 12.0m building line, it supersedes UDCPR Table 6-D's 4.5m setback. Always apply whichever is more restrictive.
          </li>
        </ul>
      </div>
    """,

    'amendment_section_html': """
      <div class="panel-info">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:8px;">Legal Directives & Clarifications</h4>
        <ul style="font-size:0.92rem; line-height:1.6; margin-left:18px;">
          <li><strong>Clarification Order CR 236/18 Part-2 (dt. 23 Dec 2021):</strong> Re-affirmed that front margins under Table 6-D are completely independent of building height and apply uniformly to towers of any height.</li>
          <li><strong>Corrigendum CR 79/2021 (dt. 02 Dec 2021):</strong> Clarified road widening surrender entitlement in congested lanes under the 4.5m centerline rule.</li>
        </ul>
      </div>
    """,

    'quiz': [
      {
        'question': 'Under Table 6-D, what is the minimum front setback required for a residential building fronting a 24.0m road in an outside-congested area?',
        'options': [
          '3.0 meters',
          '4.5 meters',
          '6.0 meters',
          'Depends on the building height (H/5)'
        ],
        'answer': 1,
        'explanation': 'Under Table 6-D Sr. No. 3, roads between 18.0m and below 30.0m require a minimum front setback of 4.5 meters.'
      },
      {
        'question': 'How does building height impact the front road setback under UDCPR Regulation 6.2.3(a)?',
        'options': [
          'Front setback increases by 1 meter for every 10 meters of height',
          'Front setback must equal H/5 for buildings above 15 meters',
          'Front setback is invariant and remains as given in Table 6-D irrespective of height',
          'Front setback doubles for buildings taller than 70 meters'
        ],
        'answer': 2,
        'explanation': 'Regulation 6.2.3(a) explicitly mandates that the front margin shall be as given in Table 6-D and is applicable to a building irrespective of its height.'
      },
      {
        'question': 'In a congested gaothan area, if a plot abuts a narrow street of 3.6m width, what front setback must be provided under Table 6-B for a pure residential building?',
        'options': [
          'NIL setback',
          '1.00 m from the plot boundary',
          '2.25 m from the centre of the street/lane',
          '4.5 m from the opposite building'
        ],
        'answer': 2,
        'explanation': 'Under Table 6-B Sr. No. (i), for streets/lanes less than 4.5m width, the setback must be 2.25m from the centre of the street/lane to make the lane 4.5m wide.'
      },
      {
        'question': 'If a building abuts two intersecting public streets, how are the setbacks determined under Regulation 6.2.6?',
        'options': [
          'The wider street gets a front setback; the narrower gets a side margin',
          'The owner can choose which side is front and which is rear',
          'The setbacks shall be such as if the building is fronting on each of such streets',
          'A uniform 6.0m setback is applied on both streets'
        ],
        'answer': 2,
        'explanation': 'Under Regulation 6.2.6, when a building abuts two or more streets, the setbacks from the streets shall be such as if the building is fronting on each of such streets.'
      }
    ],

    'prev_url': '/lessons/reg-6-3-ancillary-area-fsi.html',
    'prev_title': 'Reg 6.3: Ancillary Area FSI (60% Res / 80% Non-Res)',
    'next_url': '/lessons/reg-6-2-3-side-rear-margins-and-h5-rule.html',
    'next_title': 'Reg 6.2.3: Side & Rear Margins, Building Separation & H/5 Rule'
}
