"""
UDCPR FROM SCRATCH - CHAPTER 8, LESSON 2
Regulation 8.1.1(vi)-(viii): Loading-Unloading Berths, Basement Ramps & Marginal Open Space Parking
File: scripts/ch08_lessons/lesson_8_2_loading_spaces_marginal_parking.py
"""

lesson_data = {
    'filename': 'reg-8-1-8-loading-spaces-ramps-and-marginal-parking.html',
    'lesson_id': 'reg-8-1-8-loading-spaces-ramps-and-marginal-parking',
    'quiz_id': 'quiz-8-2',
    'clause': 'Reg. 8.1.1(vi)-(viii)',
    'title': 'Loading-Unloading Berths, Basement Ramps & Marginal Open Space Parking',
    'badge_status': 'FIRE CLEARANCES • NBC-2016',
    'ch_slug': 'ch08',
    'ch_title': 'Chapter 8: Parking, Loading and Unloading Spaces',
    'meta_desc': 'Master UDCPR Regulation 8.1.1(vi)-(viii): loading & unloading spaces (1 per 1000 sqm over 200 sqm carpet, office cap of 4, other cap of 6), bus bays (>500 flats), dual basement ramps, 3m/6m marginal fire clearances, and mechanical parking towers at 1.5m.',
    
    'lead_summary': (
        'Regulation 8.1.1(vi) through 8.1.1(viii) bridges the critical gap between vehicular accommodation and site-level life-safety. '
        'It mandates dedicated heavy vehicle loading/unloading berths for mercantile, commercial, and industrial facilities (scaled at 1 berth per '
        '1,000 sq.m of carpet area exceeding the first 200 sq.m, with statutory caps of 4 berths for offices and 6 for others), enforces internal or curbside bus bays '
        'for group housing schemes exceeding 500 units, mandates dual opposed ramps for basement parking, regulates surface parking within marginal open spaces '
        '(protecting inviolable 3.00 m and 6.00 m fire engine driveways), and sets stringent NBC-2016 fire standards for mechanical parking towers located at 1.50 m setbacks.'
    ),
    
    'amendment_cite': 'Corrigendum / Addendum No. CR 79/2021 dt. 02nd December, 2021 (Mechanical parking towers in margins & office loading caps)',
    
    'plain_summary_html': '''
<p>
  While passenger cars and two-wheelers dominate residential parking counts, high-density developments generate substantial logistical friction from delivery trucks, emergency ambulances, and school/transit buses. Regulation 8.1.1 clauses (vi) through (viii) resolve this through specialized spatial provisions:
</p>
<ul class="rule-list">
  <li><strong>Loading / Unloading Berths:</strong> Every mercantile building (offices, shopping malls, department stores, markets) and industrial/storage complex must provide dedicated loading berths measuring at least <strong>3.75 m x 7.50 m</strong> ($28.125\\text{ m}^2$). The calculation rate is 1 berth per $1,000\\text{ sq.m}$ of floor carpet area (or fraction) beyond the first $200\\text{ sq.m}$. However, to prevent oversized loading docks in commercial towers, Corrigendum CR 79/2021 imposed an absolute statutory ceiling of <strong>maximum 4 berths for office buildings</strong> and <strong>maximum 6 berths for other commercial/industrial uses</strong>.</li>
  <li><strong>Bus Bays for Large Developments:</strong> Schools, multiplexes, malls, assembly halls, and any group housing project containing <strong>more than 500 flats</strong> must construct an internal dedicated bus bay or an off-street deceleration bay along the abutting main road.</li>
  <li><strong>Basement Ramps:</strong> Basement parking lots must provide at least <strong>two separate ramps</strong> for independent entry and exit, preferably placed at opposite ends of the site to establish one-way vehicular loops and eliminate subterranean deadlocks.</li>
  <li><strong>Inviolable Fire Margins:</strong> Surface parking may be arranged within side and rear marginal open spaces, but only on the condition that a clear, unencumbered fire driveway of at least <strong>3.00 m (6.00 m for Special Buildings &amp; High-Rises)</strong> is maintained completely free of any parked vehicles, curbs, or canopies around the building perimeter.</li>
  <li><strong>Mechanical Parking Towers at 1.50m Margin:</strong> Stack parking towers or automated car silos may be positioned up to <strong>1.50 m from side and rear boundaries</strong>, provided an unobstructed 6.00 m driveway (with 9.00 m turning circles for Special Buildings) is kept clear, the adjacent building facade is a 2-hour fire-rated dead wall, and NBC-2016 Table 7 storage-building fire suppression is installed.</li>
</ul>
''',

    'statutory_extract': r"""8.1.1 General Space Requirements (Contd.)
vi) Bus bay for schools / multiplex / malls / assembly buildings / group housing:
For these occupancies, being a special building, a bus bay of required size shall be provided within premise or along main road on which plot abuts. This shall be applicable for housing scheme having more than 500 flats.

vii) Ramps for Basement Parking:
Ramps for parking in basement should conform to the requirement of Regulation No.9.12

viii) Other Parking Requirements:
a) To meet the parking requirements as per these regulations, common parking area for group of buildings, open or multi-storeyed, may be allowed in the same premises.

b) In addition to the parking spaces provided for building of Mercantile (Commercial) like office, market, departmental store, shopping mall and building of industrial and storage, loading and unloading spaces shall be provided at the rate of one space for each 1000 sq.m. of floor carpet area or fraction thereof exceeding the first 200 sq.m. of floor area, shall be provided. The space shall not be less than 3.75 m. x 7.5 m. (1) subject to maximum requirement of 4 such parking spaces for office buildings and 6 parking spaces for other buildings. However, in case of office building, such parking spaces shall not exceed more than 4.

c) Parking lock up garages shall be included in the calculation for F.S.I. calculations.

d) The space to be left out for parking as given in this regulation shall be in addition to the marginal open spaces left out for lighting and ventilation purposes as given in these regulations. These spaces may be used for parking provided minimum distance of 3.0 m. (6.0 m. in case of special building mentioned in Regulation No.2.2.8) around the buildings is kept free of any parking or loading and unloading spaces, excepting the building as mentioned in Clause (c) above. Such parking area adjoining the plot boundary may be allowed to be covered on top by sheet roofing, so as not to infringe the marginal distance to be kept open as specified above. Further such sheet roofing shall not include the area adjoining the plot boundary to be used for tree plantation as mentioned in Regulation No.3.4.1(iii), if any.

e) In case of parking spaces provided in basements, at least two separate ramps of adequate width and slope for entry and exit shall be provided preferably at opposite ends. One ramp may be provided as specified in Regulation No.9.12.

(1) f) Mechanical / Hydraulic / Stack parking / Parking tower may be permitted at 1.5 m. in side and rear margin under following circumstances -
1. Minimum 6.0 m. drive way shall be kept clear from all kind of obstruction for easy manoeuvrability of fire and rescue appliances like ambulance. For building defined as High Rise building and special building in these regulations, 9.0 m. turning circle around the building shall be maintained.
2. For Non Special building as defined in these regulations, such distance shall not be less than 3.0 m.
3. Such mechanical / hydraulic / parking tower may be permitted touching the building on dead wall side. Provided that the dead wall must be 2 hours fire rated wall.
4. The fire protection arrangement as per storage building will be made applicable to such parking towers as per Table - 7 of Part - 4 of NBC - 2016.""",

    'clause_cards_html': '''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Loading / Unloading Berths</h4>
    </div>
    <div class="card-body">
      <p>Applies to Mercantile, Commercial, Industrial, and Storage buildings. Rate: <strong>1 space per 1,000 sq.m carpet area</strong> (or fraction exceeding the initial 200 sq.m). Stall size: <strong>3.75 m x 7.50 m</strong>. <strong>Statutory Cap:</strong> Maximum <strong>4 spaces</strong> for office buildings, and maximum <strong>6 spaces</strong> for shopping malls, markets, and industrial premises.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Bus Bay Mandate (&gt;500 Flats)</h4>
    </div>
    <div class="card-body">
      <p>Mandatory for Schools, Multiplexes, Malls, Assembly Buildings, and Group Housing layouts exceeding <strong>500 residential flats</strong>. The developer must integrate a designated bus drop-off bay either inside the plot layout or recessed into the frontage along the abutting DP/RP road.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Dual Basement Ramps</h4>
    </div>
    <div class="card-body">
      <p>Basement parking levels must provide at least <strong>two separate ramps</strong> located at opposite ends to allow uninterrupted one-way circulation loops. Ramps must comply with <strong>Regulation 9.12</strong> (standard slopes of 1:10; maximum 1:8 for short transitions).</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Mechanical Parking in Margins (1.50m)</h4>
    </div>
    <div class="card-body">
      <p>Mechanical towers and hydraulic stackers may sit at a <strong>1.50 m setback</strong> in side/rear margins. Conditions: Maintain <strong>6.0 m clear driveway</strong> with <strong>9.0 m turning circle</strong> for fire tenders; if touching the building, it must be on a <strong>2-hour fire-rated dead wall</strong>; full compliance with <strong>NBC-2016 Part 4 Table 7</strong>.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': '''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Statutory Category</th>
        <th>Provision / Formula</th>
        <th>Dimension / Clear Width</th>
        <th>Maximum Cap / Ceiling</th>
        <th>Life-Safety Mandatory Condition</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Office Loading Spaces</strong></td>
        <td>1 per 1,000 sq.m carpet (over 200 sq.m)</td>
        <td><code>3.75 m x 7.50 m</code></td>
        <td><code>Max 4 spaces</code></td>
        <td>Cannot obstruct vehicular ingress or fire path</td>
      </tr>
      <tr>
        <td><strong>Mall / Industrial Loading</strong></td>
        <td>1 per 1,000 sq.m carpet (over 200 sq.m)</td>
        <td><code>3.75 m x 7.50 m</code></td>
        <td><code>Max 6 spaces</code></td>
        <td>Dedicated docking bay separated from customer parking</td>
      </tr>
      <tr>
        <td><strong>Bus Bay Requirement</strong></td>
        <td>Mandatory for &gt;500 flats &amp; Assembly</td>
        <td>Standard heavy bus bay</td>
        <td>As approved by CFO</td>
        <td>Located inside premises or recessed on abutting road</td>
      </tr>
      <tr>
        <td><strong>Marginal Parking (Special Bldg)</strong></td>
        <td>Permitted in open setbacks</td>
        <td>Stalls along boundary</td>
        <td>Boundary sheet roof allowed</td>
        <td><code>6.00 m</code> driveway around building kept 100% free</td>
      </tr>
      <tr>
        <td><strong>Mechanical Parking Tower</strong></td>
        <td>Side/rear margin installation</td>
        <td><code>1.50 m</code> from plot boundary</td>
        <td>Vertical stack height</td>
        <td><code>9.0 m</code> turning circle + 2-hr fire rated dead wall</td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL AUDIT CALCULATION: COMMERCIAL TOWER LOADING &amp; MARGINAL BUFFER</h4>
  <p><strong>Project Specification:</strong> A 15-storey IT Office tower in Navi Mumbai with a total carpet area of <strong>8,600 sq.m</strong>, classified as a Special High-Rise Building under Regulation 2.2.8.</p>
  
  <div class="step-box">
    <strong>Step 1: Calculate Raw Loading / Unloading Berths (Reg 8.1.1(viii)(b))</strong>
    <ul>
      <li>Deduct the initial threshold: $8,600\text{ sq.m} - 200\text{ sq.m} = 8,400\text{ sq.m}$.</li>
      <li>Compute berths at 1 per 1,000 sq.m or fraction thereof:</li>
      <li>$\frac{8,400}{1,000} = 8.4 \rightarrow \text{rounds up to } \mathbf{9\text{ loading berths}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Apply the Statutory Office Cap (Corrigendum CR 79/2021)</strong>
    <ul>
      <li>Regulation 8.1.1(viii)(b) explicitly states: <em>"subject to maximum requirement of 4 such parking spaces for office buildings"</em>.</li>
      <li>While the raw mathematical requirement is 9 berths, the statutory cap applies:</li>
      <li><strong>Final Mandatory Requirement: Exactly 4 Loading Berths</strong> @ $3.75\text{ m} \times 7.50\text{ m}$ each ($28.125\text{ m}^2 \times 4 = 112.50\text{ m}^2$).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Marginal Open Space &amp; Fire Driveway Compliance</strong>
    <ul>
      <li>Because this is a Special High-Rise Building, <strong>Regulation 8.1.1(viii)(d)</strong> dictates that a <strong>6.00 m wide driveway</strong> around the entire perimeter of the building must remain 100% clear and unencumbered.</li>
      <li>If surface parking stalls or loading berths are placed in the side marginal open space, the side margin must be at least:</li>
      <li>$\text{Minimum Side Margin} = 6.00\text{ m (Fire Driveway)} + 7.50\text{ m (Loading Bay Length)} = \mathbf{13.50\text{ m}}$.</li>
      <li>If the side margin is only $9.00\text{ m}$, loading berths CANNOT be placed there without violating the mandatory 6.00 m fire engine driveway!</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': '''
<div class="alert-box alert-warning">
  <h4>COMMON SCRUTINY &amp; FIRE NOC PITFALLS</h4>
  <ul class="warning-list">
    <li><strong>Violating the 6.0m Fire Driveway:</strong> Architects often try to squeeze surface parking or loading bays within an 8.0 m margin of a Special Building, leaving only 3.0 m or 4.0 m of driveable space. The Chief Fire Officer (CFO) will immediately reject the plan—the 6.0 m strip around the building must be entirely free of parking.</li>
    <li><strong>Exceeding Office Loading Dock Requisitions:</strong> Providing more than 4 loading bays for an office building consumes valuable ground space needlessly; the statute caps office loading at exactly 4 spaces.</li>
    <li><strong>Omitting Bus Bays in 500+ Flat Townships:</strong> Group housing projects containing 501 or more units must include a dedicated bus bay. Omitting this triggers a non-compliance notice during environmental and CFO clearances.</li>
    <li><strong>Attaching Mechanical Towers to Glazed Facades:</strong> Under Reg 8.1.1(viii)(f)(3), a mechanical parking tower can only touch the building envelope if that facade is an unpunctured, <strong>2-hour fire-rated dead wall</strong>. It cannot sit against window openings, balconies, or glass curtain walls.</li>
  </ul>
</div>
''',

    'amendment_section_html': '''
<div class="amendment-card">
  <h4>Statutory History &amp; Office Loading Cap</h4>
  <p><strong>Corrigendum / Addendum No. CR 79/2021 (Dated 02-12-2021):</strong></p>
  <p>Initially, commercial buildings with hundreds of thousands of square feet of IT office carpet area faced unworkable loading dock requirements (e.g., 50,000 sq.m office requiring 50 loading bays). Corrigendum CR 79/2021 recognized that corporate office buildings handle document couriers and light deliveries, not heavy shipping freight, and established a rational statutory ceiling of <strong>maximum 4 loading berths for office buildings</strong> and <strong>maximum 6 berths for other commercial/industrial uses</strong>.</p>
</div>
''',

    'quiz': [
      {
        'question': 'What is the absolute maximum statutory cap on loading/unloading spaces for an office building under Regulation 8.1.1(viii)(b)?',
        'options': [
          '2 spaces',
          '4 spaces',
          '6 spaces',
          'No cap; strictly 1 space per 1,000 sq.m without limit'
        ],
        'answer': 1,
        'explanation': 'Regulation 8.1.1(viii)(b) explicitly states: "subject to maximum requirement of 4 such parking spaces for office buildings and 6 parking spaces for other buildings."'
      },
      {
        'question': 'At what residential project scale does a bus bay become legally mandatory under Regulation 8.1.1(vi)?',
        'options': [
          'Housing schemes having more than 100 flats',
          'Housing schemes having more than 250 flats',
          'Housing schemes having more than 500 flats',
          'Only schemes with over 1,000 flats'
        ],
        'answer': 2,
        'explanation': 'Regulation 8.1.1(vi) mandates: "This shall be applicable for housing scheme having more than 500 flats."'
      },
      {
        'question': 'What minimum clear distance around a Special Building must be kept completely free of any parking or loading spaces under Regulation 8.1.1(viii)(d)?',
        'options': [
          '3.0 m',
          '4.5 m',
          '6.0 m',
          '9.0 m'
        ],
        'answer': 2,
        'explanation': 'Regulation 8.1.1(viii)(d) mandates keeping a minimum distance of "3.0 m. (6.0 m. in case of special building mentioned in Regulation No.2.2.8) around the buildings" completely free of parking.'
      },
      {
        'question': 'Under Regulation 8.1.1(viii)(f), what setback is permitted for mechanical parking towers in side and rear margins, provided fire clearances are met?',
        'options': [
          '0.0 m (on boundary)',
          '1.5 m from boundary',
          '3.0 m from boundary',
          '4.5 m from boundary'
        ],
        'answer': 1,
        'explanation': 'Regulation 8.1.1(viii)(f) states: "Mechanical / Hydraulic / Stack parking / Parking tower may be permitted at 1.5 m. in side and rear margin under following circumstances..."'
      }
    ],

    'prev_url': '/lessons/reg-8-1-parking-standards-and-dimensions.html',
    'prev_title': 'Reg 8.1 & 8.1.1: Parking Locations, Minimum Bay Dimensions & Circulation Aisles',
    'next_url': '/lessons/reg-8-2-off-street-parking-matrix-and-residential-norms.html',
    'next_title': 'Reg 8.2 & Table 8-B: Off-Street Parking Matrix & Tenement Tiers'
}
