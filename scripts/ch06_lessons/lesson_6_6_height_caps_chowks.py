"""
UDCPR FROM SCRATCH - CHAPTER 6, LESSON 6
Module: scripts/ch06_lessons/lesson_6_6_height_caps_chowks.py
Statutory Anchor: Regulation 6.9, Regulation 6.10, Regulation 6.11, Regulation 6.12, Regulation 6.14, & Regulation 6.15
Content: Height Limitations, Aviation CCZM, Interior/Exterior Chowks (H/6 & H/7), Recreational Floors, and Hirkani Kaksha
"""

lesson_data = {
    'filename': 'reg-6-10-height-caps-chowks-and-special-floors.html',
    'lesson_id': '6.6',
    'quiz_id': 'quiz-6-6',
    'clause': 'Regulation 6.9 to 6.15',
    'title': 'Building Height Limitations, Chowks & Special Amenities',
    'badge_status': 'CORE STATUTORY SPECIFICATION',
    'ch_slug': 'ch06',
    'ch_title': 'Chapter 6: General Building Requirements - Setback, Marginal Distance, Height and Permissible FSI',
    'meta_desc': 'Complete guide to UDCPR building height limits under Reg 6.10, road-width restrictions, ventilation chowk formulas under Reg 6.9, recreational floors (Reg 6.14), and Hirkani Kaksha (Reg 6.15).',
    'lead_summary': 'Master the vertical and internal dimensions of UDCPR: tiered jurisdictional height caps, mandatory 12m roads for towers > 24m, interior chowk formulas (H/6)^2, zero-FSI recreational floors, and the Hirkani Kaksha room mandate.',
    'amendment_cite': 'UDCPR-2020 Reg 6.9–6.15, amended dt. 02nd Dec 2021, 12th Oct 2022, 25th Sept 2024, and 27th Nov 2024',

    'plain_summary_html': r"""
      <p>
        The vertical envelope and interior habitability of any building in Maharashtra are governed by the concluding regulations of Chapter 6. <strong>Regulation 6.10</strong> specifies permissible building heights based on local firefighting capabilities: in metropolitan hubs (MMR, Pune, PCMC, Nagpur, Nashik), building height is governed strictly by <strong>Chief Fire Officer (CFO) clearance</strong>; in other Corporations, it is capped at <strong>70 meters</strong>, and in Municipal Councils/RP areas at <strong>50 meters</strong>.
      </p>
      <p>
        Regardless of city tier, an absolute road-width trigger applies under <strong>Regulation 6.10(ii)</strong>: any building exceeding <strong>24.0 meters in height</strong> must front on an existing or planned road of <strong>at least 12.0 meters width</strong>.
      </p>
      <p>
        Internally, <strong>Regulation 6.9</strong> establishes strict geometric formulas for light and ventilation courtyards: Interior chowks must be at least $3.0\text{m} \times 3.0\text{m}$ with area $\ge (H/6)^2$, while exterior chowks must have a width $\ge 2.4\text{m}$ and scale to $H/7 \times H/7$ for heights above 17.0m.
      </p>
      <p>
        Finally, modern urban wellness is codified via two dedicated amenities: <strong>Regulation 6.14</strong> permits zero-FSI <strong>Recreational Floors</strong> (4.5m clear height) in residential towers above 30m, and <strong>Regulation 6.15</strong> (mandated Nov 2024) allows a zero-FSI <strong>Hirkani Kaksha</strong> (up to 25 sq.m) for lactating mothers and infant care in all commercial and public buildings.
      </p>
    """,

    'statutory_extract': """
### 6.9 INTERIOR & EXTERIOR CHOWK
(a) Interior chowk: Wherever habitable rooms or kitchen derive ventilation from inner chowk, minimum size shall not be less than 3.0 m. x 3.0 m. Further such interior chowk shall have an area of not less than the square of one sixth of the height of the highest wall abutting the chowk considered from the lowest point of the chowk, at all levels.
(b) Exterior chowk: Minimum width shall not be less than 2.4 m. and depth shall not exceed 2 times the width, for buildings up to 17.0 m. height. For height more than 17.0 m., the exterior open space shall not be less than H / 7 m. x H / 7 m. where H = Height of highest wall of the Chowk from ground level. If width is less than 2.4 m., it shall be treated as a notch and shall not be considered for deriving ventilation.
Provided that, for (a) and (b) above maximum distance shall be subject to 16.0 m.

### 6.10 HEIGHT OF BUILDING
(i) Height of building (excluding parking floor upto 6.0 m. height):
1. Pune, PCMC, Nagpur, Nashik, MMR Corporations & Metropolitan Authorities: Permissible height as per approval from Fire Department.
2. Remaining Municipal Corporations: 70 m.
3. Municipal Councils, Nagar Panchayats and Regional Plan areas: 50 m.
(ii) The building height upto 24.0 m. shall be allowed on roads less than 12.0 m. For a building having height more than 24.0 m., the minimum road width shall be 12.0 m.
(iii) Vicinity of aerodromes: Subject to Civil Aviation Authorities NOC.
(v) Buildings of height more than 70.0 m. shall be allowed subject to Regulation No.6.12.

### 6.11 HEIGHT EXEMPTIONS
Roof tanks, two toilets on terrace not exceeding 8 sq.m. built-up area and height upto 3.0 m. in residential building, AC plant, lift rooms, stair cover, parapet walls, and Solar panels not exceeding 1.8 m. in height shall not be included in computation of height of building.

### 6.14 PROVISION OF RECREATIONAL FLOOR
In case of residential building having height more than 30.0 m., recreational floor may be allowed subject to:
i) Height of floor shall be upto 4.5 m. and shall be open on all sides.
ii) Used for recreational activities including swimming pool, in addition to required ROS.
iii) One such floor at every 50.0 m. height; first floor allowed after 30.0 m. height.
iv) Shall not be counted in FSI.

### 6.15 PROVISION OF HIRKANI KAKSHA (LADIES ROOM)
In any Public / Semi Public, Institutional, Educational, Commercial, Assembly, Mercantile, Business and Office building area upto 25 sq.m. may be allowed for the use of ladies with children under 6 years, pregnant women and nursing mothers. Shall not be counted in FSI.
    """,

    'clause_cards_html': r"""
      <div class="card-grid">
        <div class="card">
          <span class="kicker-card">VERTICAL BOUNDARIES</span>
          <h3 class="card-title">CFO & Road Width Triggers</h3>
          <p class="card-body">
            In MMR, Pune, PCMC, and Nagpur, heights are uncapped by fixed meters and governed by <strong>Fire CFO operational clearance</strong>. In smaller Corps, the cap is <strong>70m</strong>; in Councils, <strong>50m</strong>. Crucially, any tower <strong>taller than 24.0 meters requires an abutting road &ge; 12.0 meters</strong>!
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">LIGHT & VENTILATION</span>
          <h3 class="card-title">Chowk Dimension Formulas</h3>
          <p class="card-body">
            • <strong>Interior Chowk:</strong> Min $3.0\text{m} \times 3.0\text{m}$ and $\text{Area} \ge (H/6)^2$.<br>
            • <strong>Exterior Chowk:</strong> Min width $2.4\text{m}$; depth $\le 2\times\text{width}$ (up to 17m height). For $>17$m height, opening must be at least $H/7 \times H/7$.<br>
            • <strong>Statutory Cap:</strong> Maximum required distance capped at 16.0 meters.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">HIGH-RISE AMENITY</span>
          <h3 class="card-title">Recreational Floor (Reg 6.14)</h3>
          <p class="card-body">
            Permissible in residential towers above 30.0m height. Floor height up to <strong>4.5 meters</strong>, completely open on all sides. Can house swimming pools, yoga decks, and gymnasiums. <strong>100% exempt from FSI</strong> (ancillary washrooms counted). First floor after 30m, and one every 50m thereafter.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">SOCIAL INFRASTRUCTURE</span>
          <h3 class="card-title">Hirkani Kaksha (Reg 6.15)</h3>
          <p class="card-body">
            Mandatory welfare provision inserted in November 2024. In all commercial, institutional, and public buildings, a dedicated room of <strong>up to 25 sq.m</strong> for lactating mothers and infants is <strong>completely excluded from FSI</strong>, equipped with proper ventilation and attached toilet.
          </p>
        </div>
      </div>
    """,

    'plate_or_table_html': """
      <div class="table-container">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>Authority / Region</th>
              <th>Permissible Height Ceiling (excl. 6m parking)</th>
              <th>Road Width Requirement</th>
              <th>Governing Approval Body</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pune, PCMC, Nagpur, Nashik, MMR Corporations & Metro Authorities</strong></td>
              <td><strong>Uncapped</strong> (As per Fire NOC)</td>
              <td>&ge; 12.0 m road if height &gt; 24.0 m</td>
              <td>Chief Fire Officer (CFO) / Fire Director</td>
            </tr>
            <tr>
              <td><strong>Other Municipal Corporations & Special Planning Authorities</strong></td>
              <td><strong>70.0 meters</strong></td>
              <td>&ge; 12.0 m road if height &gt; 24.0 m</td>
              <td>CFO &amp; Planning Authority</td>
            </tr>
            <tr>
              <td><strong>Municipal Councils, Nagar Panchayats & Regional Plan Areas</strong></td>
              <td><strong>50.0 meters</strong></td>
              <td>&ge; 12.0 m road if height &gt; 24.0 m</td>
              <td>Fire Services &amp; Collector / Town Planning</td>
            </tr>
            <tr>
              <td><strong>Integrated Township Projects (ITP)</strong></td>
              <td>Higher height permitted with on-site fire station</td>
              <td>Internal layout master plan</td>
              <td>Director of Fire Services, Maharashtra</td>
            </tr>
            <tr>
              <td><strong>Airport Vicinity / CCZM</strong></td>
              <td>Strictly as per Colour Coded Zoning Map (CCZM)</td>
              <td>As per zoning</td>
              <td>Airports Authority of India (AAI) NOC</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,

    'worked_example_html': r"""
      <div class="math-box">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:12px; color:var(--ink);">
          Worked Case: Designing an Interior Ventilation Chowk for a 48m Tower
        </h4>
        <p><strong>Design Parameters:</strong></p>
        <ul>
          <li>Building Type: High-rise residential tower in Nashik.</li>
          <li>Highest abutting wall of the inner courtyard $H = 48.0\text{ meters}$.</li>
          <li>Habitable bedrooms and kitchens open onto this interior courtyard.</li>
        </ul>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint); padding-left: 14px;">
          <p><strong>Step 1: Check Baseline Minimum Dimensions</strong></p>
          <p>Under Reg 6.9(a), the absolute minimum physical dimension of an interior chowk is:
            $$\text{Minimum Width} = \mathbf{3.0\text{ meters}}$$
            $$\text{Minimum Length} = \mathbf{3.0\text{ meters}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--amber); padding-left: 14px;">
          <p><strong>Step 2: Calculate Height-Based Minimum Area</strong></p>
          <p>Reg 6.9(a) requires the area to be not less than the square of one-sixth of the height of the highest abutting wall:
            $$\text{Side Dimension Factor} = \frac{H}{6} = \frac{48.0}{6} = \mathbf{8.0\text{ meters}}$$
            $$\text{Minimum Chowk Area} = \left(\frac{H}{6}\right)^2 = 8.0^2 = \mathbf{64.0\text{ sq.m}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint-soft); padding-left: 14px;">
          <p><strong>Step 3: Verification with Statutory 16m Cap</strong></p>
          <p>The calculated dimension ($8.0\text{m}$) is well below the statutory maximum cap of <strong>16.0 meters</strong>.</p>
          <p><em>Final Specification:</em> The architect must provide an interior courtyard of at least <strong>$8.0\text{m} \times 8.0\text{m}$ (64.0 sq.m)</strong> at all levels to legally ventilate the habitable rooms.</p>
        </div>
      </div>
    """,

    'pitfalls_html': """
      <div class="panel-alert">
        <h4 style="font-family:var(--disp); font-weight:700; color:var(--brick); margin-bottom:8px;">
          CRITICAL STATUTORY TRAPS IN HEIGHT & CHOWK PLANNING
        </h4>
        <ul style="margin-left: 18px; line-height: 1.6;">
          <li>
            <strong>Exceeding 24.0m Height on Roads &lt; 12.0m:</strong> Under Regulation 6.10(ii), it is legally impossible to construct a building taller than 24.0m on a road narrower than 12.0m, even if you have unlimited FSI or TDR potential!
          </li>
          <li>
            <strong>Treating Narrow Exterior Notches as Ventilation Chowks:</strong> Under Reg 6.9(b), any exterior courtyard narrower than <strong>2.4 meters</strong> is legally defined as a "notch" and cannot be used to satisfy natural ventilation requirements for habitable rooms.
          </li>
          <li>
            <strong>Enclosing Recreational Floors:</strong> Reg 6.14 requires that recreational floors must be <em>open on all sides</em> (except safety railings). Enclosing them with glazing or masonry turns them into regular habitable floors, triggering full FSI consumption and back-penalties.
          </li>
          <li>
            <strong>Including Rooftop Solar Panels in Building Height:</strong> Under Reg 6.11, solar panels up to <strong>1.8m in height</strong> are completely exempt from building height computation. Do not let scrutiny officers include solar panels in the height envelope!
          </li>
        </ul>
      </div>
    """,

    'amendment_section_html': """
      <div class="panel-info">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:8px;">Statutory Evolution</h4>
        <ul style="font-size:0.92rem; line-height:1.6; margin-left:18px;">
          <li><strong>Corrigendum CR 79/2021 (dt. 02 Dec 2021):</strong> Clarified interior chowk area formula $(H/6)^2$ considered from the lowest point of the chowk at all levels.</li>
          <li><strong>Notification dt. 12 Oct 2022:</strong> Added CIDCO NTDA to the CFO-approved height category.</li>
          <li><strong>Directives u/s 154 (dt. 25 Sept 2024):</strong> Issued government directives regarding high-rise building clearances.</li>
          <li><strong>Notification CR 35/2023/UD-13 (dt. 27 Nov 2024):</strong> Formally inserted <strong>Regulation 6.15</strong> mandating the Hirkani Kaksha (Ladies Room) up to 25 sq.m as an FSI-exempt facility in all commercial and public buildings.</li>
        </ul>
      </div>
    """,

    'quiz': [
      {
        'question': 'Under Regulation 6.10(ii), what is the minimum road width required for any building having a height exceeding 24.0 meters?',
        'options': [
          '9.0 meters',
          '12.0 meters',
          '15.0 meters',
          '18.0 meters'
        ],
        'answer': 1,
        'explanation': 'Regulation 6.10(ii) explicitly mandates: "The building height upto 24.0 m. shall be allowed on roads less than 12.0 m. For a building having height more than 24.0 m., the minimum road width shall be 12.0 m."'
      },
      {
        'question': 'How is the minimum area of an Interior Chowk calculated for habitable rooms under Regulation 6.9(a)?',
        'options': [
          'Not less than 3.0m x 3.0m and not less than (H/6)^2',
          'Not less than 2.4m x 2.4m and not less than (H/5)^2',
          'A flat 10 sq.m irrespective of height',
          'Equal to 10% of the floor area'
        ],
        'answer': 0,
        'explanation': 'Under Reg 6.9(a), the chowk must be at least 3.0m x 3.0m and have an area not less than the square of one-sixth of the height of the highest wall abutting the chowk, (H/6)^2.'
      },
      {
        'question': 'What is the maximum permissible height for rooftop solar panel installations to remain EXEMPT from building height computation under Regulation 6.11?',
        'options': [
          '1.2 meters',
          '1.5 meters',
          '1.8 meters',
          '2.4 meters'
        ],
        'answer': 2,
        'explanation': 'Regulation 6.11 explicitly exempts "Solar panels not exceeding 1.8 m. in height" from the computation of building height.'
      },
      {
        'question': 'What is the maximum area allowed for a "Hirkani Kaksha" (Ladies Room) under Regulation 6.15, and is it counted in FSI?',
        'options': [
          '15 sq.m, counted in FSI',
          '25 sq.m, NOT counted in FSI',
          '50 sq.m, counted in Ancillary FSI',
          'Unlimited area, subject to Collector NOC'
        ],
        'answer': 1,
        'explanation': 'Under Regulation 6.15 (inserted Nov 2024), area up to 25 sq.m may be allowed for Hirkani Kaksha, and Note 5 explicitly mandates that "It shall not be counted in FSI."'
      }
    ],

    'prev_url': '/lessons/reg-6-7-projections-fsi-exclusions-and-fire-driveways.html',
    'prev_title': 'Reg 6.7 & 6.8: Projections, FSI Exclusions & Fire Driveways',
    'next_url': '/lessons/reg-7-1-higher-fsi-institutional-and-special-uses.html',
    'next_title': 'Reg 7.0 & 7.1: Higher FSI for Institutional & Special Uses'
}

