"""
UDCPR Visual Guide - CHAPTER 6, LESSON 4
Module: scripts/ch06_lessons/lesson_6_4_side_rear_margins.py
Statutory Anchor: Regulation 6.1.1(iii) Table 6-C, Regulation 6.2.1 Table 6-D, Regulation 6.2.3(b), & Regulation 6.2.4
Content: Side & Rear Marginal Distances, The H/5 High-Rise Formula (12m Cap), Building Separation, Dead Walls, and Step Margins
"""

lesson_data = {
    'filename': 'reg-6-2-3-side-rear-margins-and-h5-rule.html',
    'lesson_id': '6.4',
    'quiz_id': 'quiz-6-4',
    'clause': 'Regulation 6.1.1(iii), 6.2.3 & 6.2.4',
    'title': 'Side & Rear Margins, Building Separation & The H/5 Rule',
    'badge_status': 'CORE STATUTORY SPECIFICATION',
    'ch_slug': 'ch06',
    'ch_title': 'Chapter 6: General Building Requirements - Setback, Marginal Distance, Height and Permissible FSI',
    'meta_desc': 'Master UDCPR side and rear marginal distances: the H/5 high-rise formula, the 12.0m plot boundary cap, building-to-building separation rules, dead-wall concessions, and step margins.',
    'lead_summary': 'Learn the mathematical and legal framework governing side and rear margins: how Table 6-D transitions into the H/5 height formula, the statutory 12.0m boundary ceiling, the taller-building separation rule, and step-margin terracing.',
    'amendment_cite': 'UDCPR-2020 Reg 6.2.3 & 6.2.4, amended dt. 02nd Dec 2021 and 23rd Dec 2021',

    'plain_summary_html': """
      <p>
        While front setbacks are anchored to road widths, <strong>Side and Rear Margins</strong> are directly linked to building height, structural separation, fire safety, and natural light/ventilation.
      </p>
      <p>
        In low-rise construction (&le; 15.0m height), margins are fixed by <strong>Table 6-D</strong> (typically 1.5m to 3.0m). However, once a building exceeds the heights specified in Table 6-D, <strong>Regulation 6.2.3(b)</strong> activates Maharashtra's celebrated <strong>H/5 Rule</strong>:
      </p>
      <div style="background:var(--paper-raised); border-left:4px solid var(--blueprint); padding:12px; margin:14px 0; font-family:var(--mono);">
        $$\\text{Side or Rear Marginal Distance} = \\frac{H}{5} \\quad (\\text{subject to a statutory ceiling of } \\mathbf{12.0\\text{ meters}})$$
      </div>
      <p>
        Here, $H$ is the total building height above ground, but critically excludes <strong>up to 6.0m of parking podium/stilt floors</strong>! Furthermore, when two buildings stand on the same layout plot under <strong>Regulation 6.2.4</strong>, the clear distance between them must equal the full side/rear margin required for the <em>taller of the two buildings</em>.
      </p>
    """,

    'statutory_extract': """
### 6.1.1(iii) Side and Rear Marginal Distances in Congested Area (Table No. 6-C)
| Plot Area | Side Margin | Rear Margin |
| --- | --- | --- |
| Up to 1000 Sq.m. | 0.00 | 0.00 |
| Above 1000 & upto 4000 Sq.m. | 1.00 m. | 1.00 m. |
| Above 4000 Sq.m. | As per Regulation for non-congested area |

Note 2: Irrespective of the area of a plot, if the width thereof is 7.0 m. or less, then the side margin shall be nil.
vi) Height: Above setback and marginal distances shall be applicable for buildings less than 15.0 m. in height. Marginal distances shall be increased by 1.0 m. for buildings having height 15.0 m. and more but less than 24.0 m. For buildings having height 24.0 m. and more, marginal distances shall be as per regulations of non-congested area.

### 6.2.3(b) Side or rear marginal distance (Non-Congested Area)
The marginal distance on all sides shall be as per Table No.6-D / Table No.6-E for building height or floors mentioned therein. For height more than stipulated in Table No.6-D / Table No.6-E, the marginal distance on all sides, except the front side of a building, shall be minimum H / 5 (Where H = Height of the building above ground level).

Provided that, such marginal distance shall be subject to a maximum of 12.0 m. from the plot boundary and distance between two buildings shall be as per Regulation No.6.2.4.

Provided further that, such marginal distance from recreational open space shall be 3.0 m. in case of non-special buildings and 6.0 m. in case of special buildings, irrespective of its height.

Provided further that, the building height for the purposes of this regulation and for calculating the marginal distances shall be exclusive of height of parking floors upto 6.0 m.

Provided further that, where rooms do not derive light and ventilation from the exterior open space, i.e. dead walls, such marginal distance may be reduced to 6.0 m. in case of special building and 3.0 m. in case of other buildings.

### 6.2.3(c) Provision for Step Margin
Step margins may be allowed to be provided on upper floors to achieve required side or rear marginal distances as mentioned in these regulations subject to minimum marginal distance of 6.0 m. on ground level in case of special building.

### 6.2.4 Distance between two buildings
The distance between two buildings shall be the side / rear marginal distance required for the taller building between the two adjoining buildings.
    """,

    'clause_cards_html': r"""
      <div class="card-grid">
        <div class="card">
          <span class="kicker-card">CORE FORMULA</span>
          <h3 class="card-title">The H/5 High-Rise Rule</h3>
          <p class="card-body">
            For heights exceeding Table 6-D limits, all side and rear margins equal <strong>H / 5</strong>. If a tower is 45m tall (with no stilt parking), required margin is $45 / 5 = \mathbf{9.0\text{ m}}$. Applies symmetrically to all non-front plot boundaries.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">STATUTORY CEILING</span>
          <h3 class="card-title">The 12.0m Boundary Cap</h3>
          <p class="card-body">
            No matter how tall a skyscraper rises—even 80m, 100m, or 150m tall—the required setback from the <strong>plot boundary is capped at 12.0 meters</strong>. Developers are never forced to leave 20m or 30m offsets from their outer perimeter.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">EXCLUSION BENEFIT</span>
          <h3 class="card-title">Parking Height Deduction</h3>
          <p class="card-body">
            When computing $H$ for marginal distances, the height of <strong>parking podiums/stilts up to 6.0 meters is deducted</strong>! If a building has total height of 36m including a 6m parking stilt, effective $H = 30\text{m}$, requiring a margin of $30 / 5 = \mathbf{6.0\text{ m}}$ instead of 7.2m.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">LAYOUT SEPARATION</span>
          <h3 class="card-title">Taller Building Principle (Reg 6.2.4)</h3>
          <p class="card-body">
            When two towers (e.g. Tower A at 30m and Tower B at 60m) stand in the same layout, the clear spacing between them is governed strictly by the <strong>taller building</strong> ($60 / 5 = \mathbf{12.0\text{ m}}$), preventing narrow light-starved canyons between unequal towers.
          </p>
        </div>
      </div>
    """,

    'plate_or_table_html': """
      <div class="table-container">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>Building Height (above ground)</th>
              <th>Parking Floor Deduction (up to 6m)</th>
              <th>Effective Height ($H$) for Margins</th>
              <th>Calculated Side/Rear Margin ($H/5$)</th>
              <th>Statutory Plot Boundary Margin Required</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>15.0 m</strong> (Low-Rise)</td>
              <td>0.0 m</td>
              <td>15.0 m</td>
              <td>Table 6-D</td>
              <td><strong>1.5 m to 3.0 m</strong> (as per Table 6-D)</td>
            </tr>
            <tr>
              <td><strong>25.0 m</strong> (Mid-Rise)</td>
              <td>5.0 m stilt</td>
              <td>20.0 m</td>
              <td>20.0 / 5 = 4.0 m</td>
              <td><strong>6.0 m</strong> (Special Bldg min fire driveway)</td>
            </tr>
            <tr>
              <td><strong>36.0 m</strong> (High-Rise)</td>
              <td>6.0 m podium</td>
              <td>30.0 m</td>
              <td>30.0 / 5 = 6.0 m</td>
              <td><strong>6.0 m</strong></td>
            </tr>
            <tr>
              <td><strong>50.0 m</strong> (High-Rise)</td>
              <td>5.0 m stilt</td>
              <td>45.0 m</td>
              <td>45.0 / 5 = 9.0 m</td>
              <td><strong>9.0 m</strong></td>
            </tr>
            <tr>
              <td><strong>70.0 m</strong> (High-Rise)</td>
              <td>6.0 m podium</td>
              <td>64.0 m</td>
              <td>64.0 / 5 = 12.8 m</td>
              <td><strong>12.0 m</strong> (Statutory Cap Applied)</td>
            </tr>
            <tr>
              <td><strong>100.0 m</strong> (Skyscraper)</td>
              <td>6.0 m podium</td>
              <td>94.0 m</td>
              <td>94.0 / 5 = 18.8 m</td>
              <td><strong>12.0 m</strong> (Statutory Cap Applied)</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,

    'worked_example_html': r"""
      <div class="math-box">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:12px; color:var(--ink);">
          Worked Case: Setting Out Margins for a Mixed-Height Layout with Step Margins
        </h4>
        <p><strong>Site Setup:</strong></p>
        <ul>
          <li>Plot in PCMC non-congested area. Two residential towers proposed on a shared 5.0m parking podium.</li>
          <li><strong>Tower 1:</strong> Total height = <strong>35.0 meters</strong>.</li>
          <li><strong>Tower 2:</strong> Total height = <strong>55.0 meters</strong>.</li>
        </ul>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint); padding-left: 14px;">
          <p><strong>Step 1: Effective Heights for Marginal Distances</strong></p>
          <p>Under Reg 6.2.3(b), the 5.0m parking podium is deducted from height calculations:
            $$\text{Effective } H_1 = 35.0 - 5.0 = \mathbf{30.0\text{ meters}}$$
            $$\text{Effective } H_2 = 55.0 - 5.0 = \mathbf{50.0\text{ meters}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--amber); padding-left: 14px;">
          <p><strong>Step 2: Plot Boundary Margins for Each Tower</strong></p>
          <p>For Tower 1 facing the southern plot boundary:
            $$\text{Margin}_1 = \frac{H_1}{5} = \frac{30.0}{5} = \mathbf{6.0\text{ meters}}$$
          </p>
          <p>For Tower 2 facing the northern plot boundary:
            $$\text{Margin}_2 = \frac{H_2}{5} = \frac{50.0}{5} = \mathbf{10.0\text{ meters}}$$
          </p>
          <p><em>Step Margin Option (Reg 6.2.3c):</em> Tower 2 could maintain a 6.0m margin at ground/podium level, and step back to 10.0m on upper floors above 35m height!</p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint-soft); padding-left: 14px;">
          <p><strong>Step 3: Distance Between Tower 1 and Tower 2 (Reg 6.2.4)</strong></p>
          <p>Under Reg 6.2.4, the separation distance equals the side/rear margin required for the <em>taller building</em>:
            $$\text{Taller Building} = \text{Tower 2 with required margin of } \mathbf{10.0\text{ meters}}$$
            $$\text{Mandatory Clear Separation Between Towers} = \mathbf{10.0\text{ meters}}$$
          </p>
        </div>
      </div>
    """,

    'pitfalls_html': """
      <div class="panel-alert">
        <h4 style="font-family:var(--disp); font-weight:700; color:var(--brick); margin-bottom:8px;">
          FATAL ARCHITECTURAL PITFALLS IN MARGIN COMPUTATION
        </h4>
        <ul style="margin-left: 18px; line-height: 1.6;">
          <li>
            <strong>Averaging Margins for Building Separation:</strong> Many architects wrongly average the heights or margins of two towers ($(6.0 + 10.0)/2 = 8.0\text{m}$). Reg 6.2.4 strictly mandates the full margin of the <em>taller building</em> (10.0m).
          </li>
          <li>
            <strong>Violating the 6.0m Fire Driveway Floor Base:</strong> While Step Margins (Reg 6.2.3c) allow upper floor terracing, the ground level margin for any Special Building (&ge; 15m height) can <em>never</em> drop below <strong>6.0 meters</strong>.
          </li>
          <li>
            <strong>Forgetting Dead-Wall Concessions:</strong> If an entire facade has zero windows or ventilation openings (a pure dead wall), you do not need the full $H/5$ margin. Under Reg 6.2.3(b), it can be reduced to <strong>6.0m</strong> for special buildings and <strong>3.0m</strong> for normal buildings, saving massive site area!
          </li>
          <li>
            <strong>Failing to Keep 6.0m Clear from ROS:</strong> For special buildings, the margin between the building footprint and the internal Recreational Open Space (ROS) must be at least <strong>6.0 meters</strong>, irrespective of whether it is a front or side edge.
          </li>
        </ul>
      </div>
    """,

    'amendment_section_html': """
      <div class="panel-info">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:8px;">Statutory Amendments & Orders</h4>
        <ul style="font-size:0.92rem; line-height:1.6; margin-left:18px;">
          <li><strong>Corrigendum CR 79/2021 (dt. 02 Dec 2021):</strong> Clarified building separation references under Regulation 6.2.4 and dead-wall clearances.</li>
          <li><strong>Order CR 236/18 Part-2 (dt. 23 Dec 2021):</strong> Formal clarification confirming the exclusion of up to 6.0m parking floors when computing building height for $H/5$ margins.</li>
        </ul>
      </div>
    """,

    'quiz': [
      {
        'question': 'For a building exceeding Table 6-D low-rise heights, what is the statutory formula for side and rear marginal distances under Regulation 6.2.3(b)?',
        'options': [
          'H / 3',
          'H / 4',
          'H / 5 (subject to a maximum of 12.0 meters)',
          'H / 6 with no upper ceiling'
        ],
        'answer': 2,
        'explanation': 'Under Reg 6.2.3(b), the marginal distance on all sides (except front) shall be minimum H / 5, subject to a statutory maximum cap of 12.0 meters from the plot boundary.'
      },
      {
        'question': 'When calculating building height (H) for the H/5 marginal distance formula, what height exemption is granted under Reg 6.2.3(b)?',
        'options': [
          'Total height of the top 3 penthouses',
          'Height of parking floors up to 6.0 meters',
          'Height of all basement levels combined',
          'Height of the lift machine room and water tank'
        ],
        'answer': 1,
        'explanation': 'Reg 6.2.3(b) explicitly provides that the building height for calculating marginal distances shall be exclusive of the height of parking floors up to 6.0 meters.'
      },
      {
        'question': 'In a layout with two adjoining buildings of heights 25m and 60m, what is the mandatory separation distance between them under Regulation 6.2.4?',
        'options': [
          'The side margin required for the shorter building (25m)',
          'The average of the side margins of both buildings',
          'The side/rear marginal distance required for the taller building (60m)',
          'A flat 4.5 meters in all cases'
        ],
        'answer': 2,
        'explanation': 'Regulation 6.2.4 mandates that the distance between two buildings shall be the side/rear marginal distance required for the taller building between the two adjoining buildings.'
      },
      {
        'question': 'Under Regulation 6.2.3(b), what is the permissible reduced marginal distance for a Special Building if the wall is a pure dead wall (no light or ventilation openings)?',
        'options': [
          '1.5 meters',
          '3.0 meters',
          '6.0 meters',
          'Dead walls receive no reduction'
        ],
        'answer': 2,
        'explanation': 'Reg 6.2.3(b) provides that where rooms do not derive light and ventilation from the exterior open space (dead walls), the marginal distance may be reduced to 6.0 m in case of special buildings and 3.0 m in case of other buildings.'
      }
    ],

    'prev_url': '/lessons/reg-6-2-front-setbacks-and-street-alignments.html',
    'prev_title': 'Reg 6.1.1(ii) & 6.2.1: Front Road Setbacks & Street Alignments',
    'next_url': '/lessons/reg-6-7-projections-fsi-exclusions-and-fire-driveways.html',
    'next_title': 'Reg 6.7 & 6.8: Projections, FSI Exclusions & Fire Driveways'
}
