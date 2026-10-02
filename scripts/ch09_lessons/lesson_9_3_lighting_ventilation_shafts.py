"""
UDCPR Visual Guide - CHAPTER 9, LESSON 3
Regulation 9.14 & 9.20 to 9.26: Light, Ventilation, Shafts, Balconies & Boundary Walls
File: scripts/ch09_lessons/lesson_9_3_lighting_ventilation_shafts.py
"""

lesson_data = {
    'filename': 'reg-9-20-lighting-ventilation-and-shafts.html',
    'lesson_id': 'reg-9-20-lighting-ventilation-and-shafts',
    'quiz_id': 'quiz-9-3',
    'clause': 'Reg. 9.14, 9.20 to 9.26 & 9.30',
    'title': 'Light, Ventilation, Shafts, Balconies & Boundary Walls',
    'badge_status': 'STATUTORY • TABLE 9-C',
    'ch_slug': 'ch09',
    'ch_title': 'Chapter 9: Requirements of Parts of Buildings',
    'meta_desc': 'Master UDCPR Regulations 9.14 to 9.26: 1/10th window opening rule, 7.5m daylight limit, Table 9-C ventilation shaft sizes (1.2 to 9.0 sqm), balcony depths (1-2m), parapets (1-1.2m), and compound wall heights with corner splays.',
    
    'lead_summary': (
        'Regulations 9.14, 9.20 through 9.26, and 9.30 establish environmental comfort, daylight penetration, and perimeter enclosure standards for buildings across Maharashtra. '
        'They dictate the statutory 1/10th floor area window opening rule, impose a strict 7.50 m daylighting depth limit, regulate Table 9-C internal ventilation shafts '
        '(scaling from 1.20 sq.m for 10 m buildings up to 9.00 sq.m with mandatory mechanical induction for towers over 30 m), prescribe balcony widths (1.00 m to 2.00 m) '
        'and enclosure depth caps (maximum 1/3rd of room depth), define safety parapet heights (1.00 m to 1.20 m, up to 2.00 m for schools/hospitals), '
        'and enforce compound wall height controls (maximum 1.50 m solid with 0.90 m open railing, and 0.75 m splay limits at street intersections).'
    ),
    
    'amendment_cite': 'Statutory Table 9-C & Regulation 9.26 (Corner plot visibility splays & internal gate swing mandate)',
    
    'plain_summary_html': r'''
<p>
  Habitability in tropical urban environments depends heavily on natural illumination and cross-ventilation. UDCPR Chapter 9 codifies precise architectural rules to ensure that every living and working environment receives adequate light, fresh air, and safety enclosures:
</p>
<ul class="rule-list">
  <li><strong>The 1/10th Natural Daylighting Rule (Reg 9.20.1):</strong> The total aggregate area of external window openings for any habitable room or kitchen (excluding entry doors) must be at least <strong>1/10th (10%) of the floor area</strong>. Kitchens mandate a minimum window area of <strong>1.00 sq.m</strong>, while bathrooms and WCs require at least <strong>0.30 sq.m</strong> (with no dimension less than 0.30 m).</li>
  <li><strong>The 7.50m Daylighting Depth Limit:</strong> No portion of a habitable room is legally recognized as receiving natural daylight if it is situated more than <strong>7.50 m away from an exterior window opening</strong>. Deep floor plates exceeding 7.50 m require proportionately increased window glazing areas or central light courts.</li>
  <li><strong>Table 9-C Ventilation Shafts for Toilets:</strong> Bathrooms and water closets that do not face an open exterior yard must vent into a dedicated continuous vertical shaft. Shaft cross-sectional areas scale dynamically with building height: from <strong>1.20 sq.m</strong> (min dimension 0.90 m) for low-rises up to 10 m, to <strong>5.40 sq.m</strong> for 24 m buildings, and <strong>9.00 sq.m</strong> (min dimension 3.00 m) for towers above 30 m. For buildings above 30 m, <strong>mechanical ventilation blowers are legally mandatory</strong>.</li>
  <li><strong>Balcony Geometry &amp; Enclosures (Reg 9.14):</strong> Balconies may range from <strong>1.00 m to 2.00 m in width</strong> and are permitted on all upper floors. In buildings &lt; 24 m, balconies cannot reduce the remaining clear marginal setback to less than <strong>2.00 m</strong>. For high-rises ($\ge 24\text{ m}$), the remaining setback must never be less than <strong>6.00 m on the first floor</strong> and <strong>4.50 m on upper floors</strong>. Balconies may be enclosed into the adjoining room during sanction, provided the enclosed depth does not exceed <strong>1/3rd of the total room depth</strong>.</li>
  <li><strong>Boundary Walls &amp; Corner Sight-Lines (Reg 9.26):</strong> Front compound walls are capped at <strong>1.50 m solid masonry</strong> (expandable to 2.40 m if the upper 0.90 m is open railing/grille). At street corners, compound walls must be lowered to <strong>0.75 m solid</strong> along the junction splay to maintain unobstructed vehicular sightlines. Furthermore, <em>compound gates must swing entirely inward</em> into private property and can never open outward onto the public road.</li>
</ul>
''',

    'statutory_extract': r"""9.14 BALCONY
Balcony or balconies of a minimum width of 1.0 m. and maximum of 2.0 m. may be permitted in residential and other buildings at any floor except ground floor:
i) In non-congested area, no balcony shall reduce the marginal open space to less than 2.0 m. upto 24.0 m. building height. For height 24.0 m. and more no balcony shall reduce the marginal open space to less than 6.0 m. on first floor and 4.5 m. on upper floor. In congested area, min 1.0 m. clear from boundary.
iv) The balcony may be allowed to be enclosed in the room... In such case depth of the enclosed balcony shall not exceed 1/3rd of the depth of the room.

9.20 LIGHTING AND VENTILATION OF ROOM
9.20.1 Adequacy and manner of provision:
i) The minimum aggregate area of opening of habitable rooms and kitchens excluding doors shall be not less than 1/10th of the floor area of the room.
ii) No portion of a room shall be assumed to be lighted, if it is more than 7.5 m. away from the opening assumed for light and ventilation.
iii) A staircase shall have opening of not less than 1.0 sq.m. per landing on external wall.
iv) Opening min 1.0 sq.m. in kitchen, and 0.30 sq.m. with one dimension of 0.30 m. for bathroom/WC/store.

9.20.2 Ventilation Shaft: Table No.9-C:
1. Upto 10 m. height: Cross-section 1.2 sq.m. | Min dimension 0.9 m.
2. Upto 12 m. height: Cross-section 2.4 sq.m. | Min dimension 1.2 m.
3. Upto 18 m. height: Cross-section 4.0 sq.m. | Min dimension 1.5 m.
4. Upto 24 m. height: Cross-section 5.4 sq.m. | Min dimension 1.8 m.
5. Upto 30 m. height: Cross-section 8.0 sq.m. | Min dimension 2.4 m.
6. Above 30 m. height: Cross-section 9.0 sq.m. | Min dimension 3.0 m.
Note: Above 30 m., mechanical ventilation system mandatory besides shaft.

9.22 PARAPET: Walls / handrails on terraces, podium, balcony, recreational floor shall be 1.0 m. to 1.2 m. height. In educational, health etc. permitted upto 2.00 m. height.
9.23 CABIN: Min 3.0 sq.m., min width 1.0 m. Clear passage >= 0.9 m. Max travel distance from cabin to exit <= 18.5 m.
9.26 BOUNDARY / COMPOUND WALL:
i) Front compound wall max 1.5 m. above centerline of front street. Up to 2.4 m. permitted if top 0.9 m. is open type. Side and rear max 1.5 m. above average ground level.
ii) Corner plot: Height restricted to 0.75 m. for length equal to fanning of road, remaining 0.75 m. open type railing.
iv) Industrial, sub-stations, hospitals, factories, schools: height up to 2.4 m. permitted.
v) Gates shall open entirely inside the property.
9.30 ARCHITECTURAL PROJECTIONS: Horizontal: H/20 (min 0.3 m., max 3.0 m., exclusive of 6.0 m. fire driveway in Special Buildings). Vertical: H/20 (max 6.0 m.).""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>1/10th Daylighting &amp; 7.5m Depth</h4>
    </div>
    <div class="card-body">
      <p>Window openings in habitable rooms and kitchens must total at least <strong>1/10th of room floor area</strong>. Kitchens mandate a minimum <strong>1.00 sq.m</strong> window. Natural illumination is legally deemed absent beyond <strong>7.50 m</strong> from any exterior glazing source.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Table 9-C Ventilation Shafts</h4>
    </div>
    <div class="card-body">
      <p>Toilet shafts scale with height: <strong>1.2 sq.m</strong> (upto 10m) $\rightarrow$ <strong>4.0 sq.m</strong> (upto 18m) $\rightarrow$ <strong>5.4 sq.m</strong> (upto 24m) $\rightarrow$ <strong>9.0 sq.m</strong> (above 30m). Towers exceeding 30.0 m require mandatory engineered <strong>mechanical exhaust fans / induction blowers</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Balcony Widths &amp; Fire Margins</h4>
    </div>
    <div class="card-body">
      <p>Permitted from <strong>1.00 m to 2.00 m wide</strong>. In buildings $\ge 24\text{ m}$, balconies cannot reduce the clear margin below <strong>6.00 m on the first floor</strong> and <strong>4.50 m on upper floors</strong>. Enclosed balcony depth is capped at <strong>1/3rd of room depth</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Compound Walls &amp; Corner Splays</h4>
    </div>
    <div class="card-body">
      <p>Front walls: Max <strong>1.50 m solid</strong> + <strong>0.90 m open railing</strong> (total 2.40 m). Road intersection corners: Restricted to <strong>0.75 m solid</strong> along the road splay for vision clearance. All driveway gates must <strong>swing inward</strong> into the plot.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Building Height Range</th>
        <th>Shaft Area (Sq.m.)</th>
        <th>Minimum Shaft Dimension</th>
        <th>Applicable Occupancies</th>
        <th>Mechanical Ventilation Rule</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Up to 10.0 m (G+2 / G+3)</strong></td>
        <td><code>1.20 sq.m</code></td>
        <td><code>0.90 m</code></td>
        <td>Bathrooms &amp; Water Closets</td>
        <td>Natural air buoyancy sufficient</td>
      </tr>
      <tr>
        <td><strong>Above 10.0 m &amp; Up to 12.0 m</strong></td>
        <td><code>2.40 sq.m</code></td>
        <td><code>1.20 m</code></td>
        <td>Bathrooms &amp; Water Closets</td>
        <td>Natural air buoyancy sufficient</td>
      </tr>
      <tr>
        <td><strong>Above 12.0 m &amp; Up to 18.0 m</strong></td>
        <td><code>4.00 sq.m</code></td>
        <td><code>1.50 m</code></td>
        <td>Bathrooms &amp; Water Closets</td>
        <td>Natural air buoyancy sufficient</td>
      </tr>
      <tr>
        <td><strong>Above 18.0 m &amp; Up to 24.0 m</strong></td>
        <td><code>5.40 sq.m</code></td>
        <td><code>1.80 m</code></td>
        <td>Mid-rise residential &amp; commercial</td>
        <td>Exhaust louvers recommended</td>
      </tr>
      <tr>
        <td><strong>Above 24.0 m &amp; Up to 30.0 m</strong></td>
        <td><code>8.00 sq.m</code></td>
        <td><code>2.40 m</code></td>
        <td>High-rise towers</td>
        <td>Exhaust louvers recommended</td>
      </tr>
      <tr>
        <td><strong>Above 30.0 m (Towers &gt; 10 Floors)</strong></td>
        <td><code>9.00 sq.m</code></td>
        <td><code>3.00 m</code></td>
        <td>High-rise residential / commercial</td>
        <td><strong>MANDATORY MECHANICAL SYSTEM</strong></td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL AUDIT CALCULATION: APARTMENT DAYLIGHTING &amp; TOILET SHAFT SIZING</h4>
  <p><strong>Apartment Layout:</strong> A living room measuring <strong>4.00 m width x 6.50 m depth</strong> ($26.00\text{ sq.m}$ floor area) in a <strong>45-metre high-rise residential tower</strong> with 2 internal back-to-back attached bathrooms.</p>
  
  <div class="step-box">
    <strong>Step 1: Check Minimum Window Glazing Area (Reg 9.20.1(i))</strong>
    <ul>
      <li>Living Room Floor Area: $26.00\text{ sq.m}$.</li>
      <li>Required aggregate window opening: $\ge \frac{1}{10}\text{th} \times 26.00\text{ sq.m} = \mathbf{2.60\text{ sq.m}}$.</li>
      <li>If providing a sliding window of $1.80\text{ m}$ width and $1.50\text{ m}$ height:</li>
      <li>$\text{Window Glazing Area} = 1.80\text{ m} \times 1.50\text{ m} = 2.70\text{ sq.m} \ge 2.60\text{ sq.m}$ (Compliant).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Check Daylighting Depth Limit (Reg 9.20.1(ii))</strong>
    <ul>
      <li>Room Depth from window wall: $6.50\text{ m}$.</li>
      <li>Statutory maximum distance for assumed natural daylight: <strong>7.50 m</strong>.</li>
      <li>Since $6.50\text{ m} \le 7.50\text{ m}$, the entire living room is legally verified as naturally illuminated.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Size the Internal Toilet Ventilation Shaft (Table 9-C)</strong>
    <ul>
      <li>Total Building Height: $45.00\text{ m}$ (Height falls under Item 6: <em>Above 30.0 m</em>).</li>
      <li>Table 9-C mandates:</li>
      <li>$\text{Minimum Cross-Sectional Area} = \mathbf{9.00\text{ sq.m}}$.</li>
      <li>$\text{Minimum Dimension of Shaft} = \mathbf{3.00\text{ m}}$.</li>
      <li>Statutory Shaft Layout: $3.00\text{ m} \times 3.00\text{ m}$ continuous vertical open duct.</li>
      <li>Note Condition: Because the building is above 30.0 m, an <strong>engineered mechanical ventilation exhaust system</strong> must be installed inside the shaft with backup generator power.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>COMMON SCRUTINY &amp; FIRE SAFETY PITFALLS IN REGULATION 9.14 &amp; 9.20</h4>
  <ul class="warning-list">
    <li><strong>Sizing Shafts for Low-Rise on High-Rise Buildings:</strong> Using a $1.2\text{ m} \times 1.0\text{ m}$ shaft on a 15-storey (45m) tower. Table 9-C requires a massive $9.0\text{ sq.m}$ shaft ($3.0\text{ m} \times 3.0\text{ m}$) once the building exceeds 30 metres.</li>
    <li><strong>Enclosing Balconies Beyond 1/3rd Depth:</strong> Enclosing a 2.0 m deep balcony into a 3.0 m deep bedroom (total depth 5.0m; $\frac{2.0}{5.0} = 40\% > 33.3\%$). Reg 9.14(iv) limits enclosed balcony depth to strictly 1/3rd of the total combined room depth.</li>
    <li><strong>Balcony Infringing Fire Margins Above 24m:</strong> In towers $\ge 24\text{ m}$, cantilever balconies that leave less than 6.0 m on the first floor or 4.5 m on upper floors violate Reg 9.14(i) and will be rejected by the Fire Department.</li>
    <li><strong>Outward-Swinging Driveway Gates:</strong> Installing sliding or hinged gates that swing open into the public sidewalk or roadway is an explicit violation of Regulation 9.26(v).</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; Environmental Quality Safeguards</h4>
  <p><strong>Table 9-C &amp; Regulation 9.20 Provisions:</strong></p>
  <p>The UDCPR unified divergent municipal rules across Maharashtra regarding toilet ducts. Formerly, small municipal councils allowed tiny 0.60 m pipes that accumulated stagnant foul air. Table 9-C introduced scientific height-scaled shafts up to 9.0 sq.m and made mechanical ventilation legally compulsory for towers over 30 metres, guaranteeing healthy cross-air induction across dense urban developments.</p>
</div>
''',

    'quiz': [
      {
        'question': 'What is the minimum aggregate area of window openings required for a habitable room or kitchen under Regulation 9.20.1(i)?',
        'options': [
          'Not less than 1/20th of room floor area',
          'Not less than 1/10th of room floor area',
          'Not less than 1/6th of room floor area',
          'Fixed at a flat 2.0 sq.m regardless of room size'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.20.1(i) states: "The minimum aggregate area of opening of habitable rooms and kitchens excluding doors shall be not less than 1/10th of the floor area of the room."'
      },
      {
        'question': 'Beyond what distance from an exterior window is a room legally deemed NOT to receive natural light under Regulation 9.20.1(ii)?',
        'options': [
          '5.0 m',
          '6.0 m',
          '7.5 m',
          '9.0 m'
        ],
        'answer': 2,
        'explanation': 'Regulation 9.20.1(ii) decrees: "No portion of a room shall be assumed to be lighted, if it is more than 7.5 m. away from the opening assumed for light and ventilation."'
      },
      {
        'question': 'Under Table 9-C, what is the required cross-section and minimum dimension of a ventilation shaft for a building height above 30.0 metres?',
        'options': [
          '4.0 sq.m with minimum dimension 1.5 m',
          '5.4 sq.m with minimum dimension 1.8 m',
          '8.0 sq.m with minimum dimension 2.4 m',
          '9.0 sq.m with minimum dimension 3.0 m (plus mechanical ventilation)'
        ],
        'answer': 3,
        'explanation': 'Table 9-C Item 6 prescribes a cross-section of 9.0 sq.m and a minimum dimension of 3.0 m for buildings above 30 m, with mandatory mechanical ventilation.'
      },
      {
        'question': 'Under Regulation 9.26(ii), what is the maximum permissible solid masonry height of a boundary wall at a road intersection corner splay?',
        'options': [
          '0.50 m',
          '0.75 m',
          '1.20 m',
          '1.50 m'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.26(ii) specifies that at corner plots, "the height of the boundary wall shall be restricted to 0.75 m. for a length equal to fanning of the road".'
      }
    ],

    'prev_url': '/lessons/reg-9-11-basements-podiums-and-vehicular-ramps.html',
    'prev_title': 'Reg 9.11 to 9.16: Basements, Podiums & Vehicular/Pedestrian Ramps',
    'next_url': '/lessons/reg-9-28-exit-requirements-and-staircases.html',
    'next_title': 'Reg 9.27 & 9.28: Exit Requirements, Staircase Widths & Occupant Loads'
}
