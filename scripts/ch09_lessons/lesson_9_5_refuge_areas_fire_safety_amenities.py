"""
UDCPR FROM SCRATCH - CHAPTER 9, LESSON 5
Regulation 9.29 to 9.33: Refuge Areas, High-Rise Fire Towers, Chutes & Housing Amenities
File: scripts/ch09_lessons/lesson_9_5_refuge_areas_fire_safety_amenities.py
"""

lesson_data = {
    'filename': 'reg-9-29-refuge-areas-fire-towers-and-amenities.html',
    'lesson_id': 'reg-9-29-refuge-areas-fire-towers-and-amenities',
    'quiz_id': 'quiz-9-5',
    'clause': 'Reg. 9.29 to 9.33',
    'title': 'Refuge Areas, High-Rise Fire Towers, Chutes & Society Amenities',
    'badge_status': 'HIGH-RISE EVACUATION • REG 9.29 TO 9.33',
    'ch_slug': 'ch09',
    'ch_title': 'Chapter 9: Requirements of Parts of Buildings',
    'meta_desc': 'Master UDCPR Regulations 9.29 to 9.33: refuge areas (above 24m, every 15m thereafter, 15 sqm / 0.3 sqm/person), >70m fire evacuation towers & chutes (4-hr shaft, 75mm water barrier), service floor 1.8m height, and mandatory society amenities.',
    
    'lead_summary': (
        'Regulations 9.29 through 9.33 govern high-rise survival infrastructure, structural fire barriers, and compulsory residential community amenities across Maharashtra. '
        'They prescribe staircase ergonomics (treads, risers, handrails, and external fire escape stairways), regulate cantilever Refuge Areas for all buildings exceeding 24.0 m '
        '(mandating 15 sq.m or 0.3 sq.m per person for two consecutive floors, stacked at 24 m, 39 m, and every 15 m thereafter with 100% planning FSI relief), '
        'decree advanced evacuation towers and 4-hour fire chute shafts for mega-towers taller than 70.0 m, regulate 1.80 m technical service floors, and mandate '
        'society fitness centers, creches, driver restrooms, servant toilets, and grand entrance lobbies under Regulation 9.31.'
    ),
    
    'amendment_cite': 'Corrigendum CR 79/2021 (Fire doors) & Notifications dt. 12-10-2022 (Fire chute rules) and CR 121/21 (Housing amenities from 30 flats)',
    
    'plain_summary_html': r'''
<p>
  When building heights cross 24 metres and 70 metres, conventional municipal fire department ladder trucks cannot reach upper floors from the ground. Regulations 9.29 to 9.33 enforce self-contained, internal life-safety survival architecture:
</p>
<ul class="rule-list">
  <li><strong>Staircase Construction &amp; Ergonomics (Reg 9.29.3):</strong>
    <ul style="margin-top:6px;">
      <li><em>Treads:</em> Minimum <strong>25 cm</strong> for residential; minimum <strong>30 cm</strong> for commercial/public buildings.</li>
      <li><em>Risers:</em> Maximum <strong>19 cm</strong> for residential; maximum <strong>15 cm</strong> for commercial/public buildings. Flight limit: maximum <strong>15 risers per flight</strong>.</li>
      <li><em>Fire Doors:</em> Access into stairwells must be protected by <strong>30-minute fire-resisting, automatic self-closing swing doors</strong> opening in the direction of escape.</li>
      <li><em>Headroom:</em> Minimum <strong>2.20 m clear headroom</strong> under intermediate landings.</li>
    </ul>
  </li>
  <li><strong>Refuge Area Stacking Hierarchy (Reg 9.29.6):</strong> Compulsory for all buildings taller than <strong>24.0 m</strong>.
    <ul style="margin-top:6px;">
      <li><em>Sizing:</em> Minimum <strong>15.00 sq.m</strong> or <strong>0.30 sq.m per person</strong> to accommodate the population of <em>two consecutive floors</em>, whichever is higher.</li>
      <li><em>Vertical Placement:</em> First refuge area on the floor <strong>immediately above 24.0 m</strong> (approx. 8th floor). Second refuge area on the floor <strong>immediately above 39.0 m</strong> (approx. 13th floor). Subsequent refuge areas placed <strong>every 15.0 m vertically thereafter</strong> (54m, 69m, 84m, etc.).</li>
      <li><em>FSI Exemption:</em> Standard refuge areas are 100% free of FSI. If planning constraints cause excess area, it remains free of FSI up to <strong>100% of the statutory requirement</strong>.</li>
    </ul>
  </li>
  <li><strong>High-Rise Evacuation Towers for Towers &gt; 70.0m (Reg 9.29.9):</strong> Mega-towers exceeding 70 metres must provide either:
    <ul style="margin-top:6px;">
      <li><em>Option 1:</em> Dedicated <strong>Fire Escape Chute Shafts</strong> ($2.50\text{ m} \times 1.50\text{ m}$, 4-hour fire resistance, ventilated on external face, with landings every 21 m).</li>
      <li><em>Option 2:</em> A dedicated <strong>Fire Evacuation Tower</strong> with a pressurized smoke-check lobby and an external evacuation lift. Crucially, the smoke lobby must have a <strong>positive step-up level difference of at least 75 mm</strong> above the stair landing to prevent firefighting water from flooding the lift shaft.</li>
    </ul>
  </li>
  <li><strong>Technical Service Floors (Reg 9.33):</strong> A dedicated service floor with a clear height <strong>not exceeding 1.80 m</strong> is permissible 100% free of FSI. Heights exceeding 1.80 m are permitted only in hospitals or buildings taller than 70.0 m with special municipal sanction.</li>
  <li><strong>Mandatory Housing Scheme Amenities (Reg 9.31):</strong> Residential developments must provide dedicated community infrastructure (counted in FSI):
    <ul style="margin-top:6px;">
      <li><em>Fitness Centre / Creche / Society Office:</em> <strong>20 sq.m</strong> for schemes with 30 to 100 flats, plus <strong>20 sq.m for every additional 300 flats</strong>.</li>
      <li><em>Servant Sanitary Block:</em> <strong>3.0 sq.m</strong> for 30–100 flats, plus <strong>3.0 sq.m for every additional 200 flats</strong>.</li>
      <li><em>Drivers Room with Toilet:</em> <strong>12.0 sq.m</strong> for 30–100 flats, plus <strong>10.0 sq.m for every additional 300 flats</strong>.</li>
      <li><em>Entrance Lobby:</em> Minimum <strong>9.0 sq.m</strong> (minimum width <strong>2.50 m</strong>) on the ground floor for any residential building containing more than 6 tenements.</li>
    </ul>
  </li>
</ul>
''',

    'statutory_extract': r"""9.29 OTHER REQUIREMENTS OF INDIVIDUAL EXIT AT EACH FLOOR
9.29.1 Doorways: Exit doorway min 90 cm. width (200 cm. assembly; 75 cm. bath/WC). Doorway height min 200 cm. Open outwards. Landing equal to width of door. No sliding or overhead doors on exits. Openable from inside without key. No mirrors.

9.29.3 Stairways:
iv) Tread min 25 cm. without nosing for residential; min 30 cm. for other buildings.
v) Riser max 19 cm. for residential; max 15 cm. for other buildings. Limited to 15 per flight.
vi) Handrails min 100 cm. height from centre of tread.
viii) Headroom under landing >= 2.2 m.
ix) Special building access through 30-min fire resisting automatic closing swing doors.
x) No living space, store or fire risk shall open directly into staircase.
xiii) Single staircase terminates at ground level. Basements separated by 2-hr fire rated cut-off lobby.

9.29.4 Fire escape or external stairs: Straight flight >= 1250 mm. wide, 250 mm. treads, risers <= 190 mm. (max 15/flight). Inclination <= 45 degree. Handrails 1000 - 1200 mm. Spiral stairs limited to low occupant load & <= 9 m. height (min 1500 mm. diameter). Unprotected steel prohibited.

9.29.6 Refuge Area: For buildings > 24 m. in height, refuge area of 15 sq.m. or 0.3 sq.m. per person to accommodate occupants of two consecutive floors, whichever is higher:
a) Floors above 24.0 m. and upto 39.0 m. height - One refuge area on the floor immediately above 24.0 m.
b) Floors above 39.0 m. height - One refuge area on the floor immediately above 39.0 m. and so on after every 15.0 m.
Refuge area in excess of requirements counted in FSI, except excess up to 100% due to planning constraints is free of FSI.

9.29.8 Fire lift: For buildings >= 15.0 m. Minimum 8 passengers capacity, automated with emergency switch on ground level, intercom to ground control room.

9.29.9 Fire Escape Chutes / High Rise Evacuation (> 70 m.):
i) Chute shaft for every wing adjacent to staircase: 4 hours fire resistance, external face ventilated, size >= 2.5 m. x 1.5 m., landings at vertical height <= 21.0 m.
Alternatively: Fire tower with smoke check lobby with fireman lift / evacuation lift on external face. Positive level difference of minimum 75 mm. with respect to staircase landing.

9.31 ADDITIONAL REQUIREMENTS IN CASE OF HOUSING SCHEMES: Counted in FSI:
i) Fitness Centre, Creche, society office: 20 sq.m. in scheme having 30 to 100 flats, + 20 sq.m. for every 300 flats.
ii) Sanitary block for servants: 3.0 sq.m. in schemes having 30 to 100 flats, + 3.0 sq.m. for every 200 flats.
iii) Drivers room with toilet: 12.0 sq.m. in schemes having 30 to 100 flats, + 10.0 sq.m. for every 300 flats.
iv) Entrance lobby of min 9.0 sq.m. (min dimension 2.50 m.) at ground floor for > 6 flats.

9.33 SERVICE FLOOR: Height not exceeding 1.8 m. free of FSI. Exceeding 1.8 m. allowed for medical or > 70 m. height with special permission.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Staircase Treads &amp; Risers</h4>
    </div>
    <div class="card-body">
      <p>Residential: Min <strong>25 cm tread</strong>, Max <strong>19 cm riser</strong>. Commercial/Public: Min <strong>30 cm tread</strong>, Max <strong>15 cm riser</strong>. Flight ceiling: Max <strong>15 risers per flight</strong>. Protected by <strong>30-minute self-closing fire doors</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Refuge Area Stacking (&gt;24m)</h4>
    </div>
    <div class="card-body">
      <p>Required above 24.0 m: Min <strong>15 sq.m</strong> or <strong>0.3 sq.m per person</strong> for 2 consecutive floors. Stacking: 1st above <strong>24.0 m</strong>, 2nd above <strong>39.0 m</strong>, and every <strong>15.0 m thereafter</strong>. Free of FSI (+100% planning buffer).</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Towers &gt; 70m Evacuation Systems</h4>
    </div>
    <div class="card-body">
      <p>Mega-towers mandate <strong>4-hour fire chute shafts</strong> ($2.5\text{ m} \times 1.5\text{ m}$) or external <strong>Fire Evacuation Towers</strong> with a pressurized smoke lobby raised <strong>75 mm step-up</strong> to prevent firefighting water ingress.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Society Community Amenities (Reg 9.31)</h4>
    </div>
    <div class="card-body">
      <p>Mandatory for schemes starting from <strong>30 flats</strong>: Fitness/office (<strong>20 sq.m</strong> + 20 sqm/300 flats), Servant toilet (<strong>3 sq.m</strong> + 3 sqm/200 flats), Drivers room (<strong>12 sq.m</strong> + 10 sqm/300 flats), and Entrance lobby ($\ge 9.0\text{ sq.m}$, min width <strong>2.50 m</strong>).</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Building Level / Height</th>
        <th>Mandatory Life-Safety Element</th>
        <th>Statutory Size / Dimension</th>
        <th>Fire Rating / Technical Condition</th>
        <th>FSI Exemption Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Ground Floor (&gt;6 flats)</strong></td>
        <td>Entrance Lobby</td>
        <td><code>9.00 sq.m</code> (min width 2.50 m)</td>
        <td>Ground access foyer</td>
        <td>Counted in FSI</td>
      </tr>
      <tr>
        <td><strong>Height &ge; 15.0 m</strong></td>
        <td>Fire Lift</td>
        <td>Min <code>8 passengers</code> capacity</td>
        <td>Automated + Ground fireman switch</td>
        <td>Shaft free of FSI</td>
      </tr>
      <tr>
        <td><strong>Height &gt; 24.0 m (Floor 8)</strong></td>
        <td>1st Refuge Area</td>
        <td><code>15 sq.m</code> or 0.3 sqm/person</td>
        <td>Cantilever / Peripheral open air</td>
        <td><strong>100% FREE OF FSI</strong></td>
      </tr>
      <tr>
        <td><strong>Height &gt; 39.0 m (Floor 13)</strong></td>
        <td>2nd Refuge Area</td>
        <td><code>15 sq.m</code> or 0.3 sqm/person</td>
        <td>Cantilever / Peripheral open air</td>
        <td><strong>100% FREE OF FSI</strong></td>
      </tr>
      <tr>
        <td><strong>Every +15.0 m (54m, 69m...)</strong></td>
        <td>Subsequent Refuge Areas</td>
        <td><code>15 sq.m</code> or 0.3 sqm/person</td>
        <td>Every 5th typical floor</td>
        <td><strong>100% FREE OF FSI</strong></td>
      </tr>
      <tr>
        <td><strong>Height &gt; 70.0 m (Mega-Tower)</strong></td>
        <td>Fire Chute Shaft OR Evacuation Tower</td>
        <td><code>2.50 m x 1.50 m</code> shaft</td>
        <td>4-hour fire wall; 75 mm step-up lobby</td>
        <td>Shaft free of FSI</td>
      </tr>
      <tr>
        <td><strong>Intermediate Level</strong></td>
        <td>Technical Service Floor</td>
        <td>Height &le; <code>1.80 m</code> clear</td>
        <td>Exclusively for MEP pipelines/ducts</td>
        <td><strong>100% FREE OF FSI</strong></td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL HIGH-RISE COMPLIANCE AUDIT: 60-METRE TOWER REFUGE &amp; AMENITY SCHEDULE</h4>
  <p><strong>Tower Profile:</strong> A 20-storey residential high-rise building with a total height of <strong>60.0 metres</strong> containing <strong>160 apartments</strong> (8 flats per floor, each flat averaging $100\text{ sq.m}$ carpet area).</p>
  
  <div class="step-box">
    <strong>Step 1: Calculate Refuge Area Stacking Schedule (Reg 9.29.6)</strong>
    <ul>
      <li>Population of 1 typical floor: 8 flats @ $12.5\text{ sq.m/person} = \frac{8 \times 100}{12.5} = 64\text{ persons}$.</li>
      <li>Population of 2 consecutive floors: $64 \times 2 = \mathbf{128\text{ persons}}$.</li>
      <li>Area by occupant load: $128 \times 0.30\text{ sq.m/person} = \mathbf{38.40\text{ sq.m}}$.</li>
      <li>Statutory comparison: $\max(15.00\text{ sq.m}, 38.40\text{ sq.m}) = \mathbf{38.40\text{ sq.m per refuge floor}}$.</li>
      <li><em>Vertical Stacking Locations:</em></li>
      <li>Refuge Area 1: Floor immediately above $24.0\text{ m}$ (Floor 8) $\rightarrow 38.40\text{ sq.m}$ (Free of FSI).</li>
      <li>Refuge Area 2: Floor immediately above $39.0\text{ m}$ (Floor 13) $\rightarrow 38.40\text{ sq.m}$ (Free of FSI).</li>
      <li>Refuge Area 3: Floor immediately above $54.0\text{ m}$ (Floor 18) $\rightarrow 38.40\text{ sq.m}$ (Free of FSI).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Calculate Mandatory Housing Amenities (Reg 9.31)</strong>
    <p>Total flats = 160 units (falls in the 30–100 flat base tier + 60 additional flats):</p>
    <ul>
      <li><strong>Society Office / Fitness Centre / Creche:</strong></li>
      <li>Base for 100 flats = $20.00\text{ sq.m}$.</li>
      <li>Excess flats = 60 flats (less than 300 additional threshold).</li>
      <li>$\text{Total Required Society Office / Fitness} = \mathbf{20.00\text{ sq.m}}$ (Counted in FSI).</li>
      <li><strong>Servant Sanitary Block:</strong></li>
      <li>Base for 100 flats = $3.00\text{ sq.m}$.</li>
      <li>$\text{Total Required Servant Toilet} = \mathbf{3.00\text{ sq.m}}$ (Counted in FSI).</li>
      <li><strong>Drivers Room with Toilet:</strong></li>
      <li>Base for 100 flats = $12.00\text{ sq.m}$.</li>
      <li>$\text{Total Required Drivers Restroom} = \mathbf{12.00\text{ sq.m}}$ (Counted in FSI).</li>
      <li><strong>Entrance Lobby:</strong> Ground floor entrance lobby of $\ge \mathbf{9.00\text{ sq.m}}$ with minimum dimension of $2.50\text{ m}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Fire Lift &amp; Evacuation Verification</strong>
    <ul>
      <li>Building height is $60.0\text{ m} \ge 15.0\text{ m}$: Dedicated <strong>8-passenger Fire Lift</strong> is mandatory.</li>
      <li>Building height is $60.0\text{ m} \le 70.0\text{ m}$: The special 4-hour fire chute shaft / evacuation tower under Reg 9.29.9 is <em>not required</em> (mandatory only above 70 m).</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>CRITICAL HIGH-RISE LIFE-SAFETY COMPLIANCE DEFECTS</h4>
  <ul class="warning-list">
    <li><strong>Missing Intermediate Refuge Floors:</strong> Placing only one refuge floor at 24 metres and ignoring the mandatory stacking at 39 m and every 15 m thereafter. CFO approval will be completely blocked.</li>
    <li><strong>Sizing Refuge for Only 15 sq.m on Large Floors:</strong> Providing a flat 15 sq.m refuge terrace on a floor with 12 large apartments. The formula requires 0.3 sq.m per person for <em>two consecutive floors</em>, which often requires 30 to 45 sq.m!</li>
    <li><strong>Enclosing Refuge Areas with Glazing:</strong> Refuge areas must be located on the periphery or a cantilever slab and be <strong>open to the external air on at least one side</strong> protected only by railings. They cannot be enclosed with glass windows.</li>
    <li><strong>Water Ingress in High-Rise Fireman Lifts:</strong> Omitting the <strong>75 mm positive step-up difference</strong> in smoke-check lobbies for evacuation lifts in towers $>70\text{m}$. During firefighting, thousands of litres of water pour down stairwells; without the 75 mm threshold, water floods the lift pit and disables the emergency evacuation elevator.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; High-Rise Evacuation Mandates</h4>
  <p><strong>Notification No. CR 236/18 (Part 6) dt. 12-10-2022:</strong></p>
  <p>Inserted sub-clause (xiii) to Regulation 9.29.4 explicitly establishing that fire escape chutes cannot be used as an alternate or replacement for mandatory external fire escape staircases, but may only be installed as an additional safety system. It also standardized the 4-hour fire resistance rating and 75 mm water ingress step for evacuation towers in 70m+ mega-towers.</p>
</div>
''',

    'quiz': [
      {
        'question': 'At what building height does the provision of a statutory Refuge Area first become legally mandatory under Regulation 9.29.6?',
        'options': [
          'Above 15.0 m',
          'Above 24.0 m',
          'Above 36.0 m',
          'Above 70.0 m'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.29.6 mandates that: "For buildings more than 24 m. in height, refuge area of 15 sq.m. or an area equivalent to 0.3 sq.m. per person to accommodate the occupants of two consecutive floors, whichever is higher, shall be provided".'
      },
      {
        'question': 'Following the first refuge area above 24.0 m and the second above 39.0 m, at what vertical intervals must subsequent refuge areas be provided?',
        'options': [
          'Every 9.0 m',
          'Every 12.0 m',
          'Every 15.0 m',
          'Every 24.0 m'
        ],
        'answer': 2,
        'explanation': 'Regulation 9.29.6(b) mandates: "One refuge area on the floor immediately above 39.0 m. and so on after every 15.0 m."'
      },
      {
        'question': 'What is the maximum permissible clear height of a technical service floor to remain 100% free of FSI under Regulation 9.33?',
        'options': [
          '1.50 m',
          '1.80 m',
          '2.10 m',
          '2.40 m'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.33 states: "A service floor of height not exceeding 1.8 m. may be provided in a building exclusively for provision / diversion of services" free of FSI.'
      },
      {
        'question': 'Under Regulation 9.29.9, what positive level difference must be maintained between the smoke check lobby of an evacuation lift and the staircase landing in towers > 70m?',
        'options': [
          'Minimum 25 mm',
          'Minimum 50 mm',
          'Minimum 75 mm to prevent water ingress into the fireman lift shaft',
          'Minimum 150 mm'
        ],
        'answer': 2,
        'explanation': 'The Note to Regulation 9.29.9 dictates: "Both the smoke check lobby with evacuation lift shall have positive level difference of minimum 75 mm. with respect to staircase landing or mid-landing level to avoid ingress of water in fireman lift shaft."'
      }
    ],

    'prev_url': '/lessons/reg-9-28-exit-requirements-and-staircases.html',
    'prev_title': 'Reg 9.27 & 9.28: Exit Requirements, Staircase Widths & Occupant Loads',
    'next_url': '/chapters/ch09.html',
    'next_title': 'Chapter 9 Syllabus • Requirements of Parts of Buildings'
}
