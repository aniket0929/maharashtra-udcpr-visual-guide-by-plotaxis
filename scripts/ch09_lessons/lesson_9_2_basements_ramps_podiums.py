"""
UDCPR Visual Guide - CHAPTER 9, LESSON 2
Regulation 9.11, 9.12, 9.13 & 9.16: Basements, Podiums, Vehicular Ramps & Stilt Clearances
File: scripts/ch09_lessons/lesson_9_2_basements_ramps_podiums.py
"""

lesson_data = {
    'filename': 'reg-9-11-basements-podiums-and-vehicular-ramps.html',
    'lesson_id': 'reg-9-11-basements-podiums-and-vehicular-ramps',
    'quiz_id': 'quiz-9-2',
    'clause': 'Reg. 9.11, 9.12, 9.13 & 9.16',
    'title': 'Basements, Podiums, Vehicular Ramps & Stilt Clearances',
    'badge_status': 'STATUTORY • FREE VS COUNTED FSI',
    'ch_slug': 'ch09',
    'ch_title': 'Chapter 9: Requirements of Parts of Buildings',
    'meta_desc': 'Master UDCPR Regulations 9.11 to 9.16: basement FSI exemptions vs counted commercial uses, 1.5m boundary flush extension, 1:8/1:10 ramp slopes, 3.0m/6.0m widths, car lifts, podium fire load capacity, and 2.4m/4.5m stilt heights.',
    
    'lead_summary': (
        'Regulations 9.11, 9.12, 9.13, and 9.16 govern the high-load subterranean and podium infrastructure of modern developments in Maharashtra. '
        'They delineate which basement operations are legally 100% free of FSI (parking, electrical substations, D.G. sets, ETP plants, suction tanks, and Data Center storage) '
        'versus those counted in FSI (commercial malls in first basement, strong rooms, bank lockers, mortuaries, and hospital nursing quarters), '
        'authorize flushed basements to extend into side/rear setbacks up to 1.50 m from the plot boundary, codify vehicular ramp slopes (maximum 1:8 to 1:10) '
        'and circulation widths (minimum 3.00 m one-way, 6.00 m two-way, or paired car lifts), enforce 45-tonne fire engine deck ratings, and prescribe non-negotiable '
        '2.40 m beam soffit and 4.50 m stack parking clearances.'
    ),
    
    'amendment_cite': 'Corrigendum CR 79/2021 & CR 121/21 dt. 02-12-2021 (Plot thresholds for car lifts) & Jan 2024 (Data Center storage)',
    
    'plain_summary_html': r'''
<p>
  Subterranean basements, podium parking decks, and elevated stilts represent the most capital-intensive elements of building engineering. Regulation 9 establishes strict architectural, structural, and life-safety rules to ensure functional efficiency and fire safety:
</p>
<ul class="rule-list">
  <li><strong>Basement FSI Accounting (Reg 9.11.1):</strong> Basements are strictly <strong>100% Free of FSI</strong> when utilized for: (1) vehicular parking, (2) air-conditioning plant and machinery, (3) DG generator sets, electric substations, and meter rooms, (4) Effluent Treatment Plants (ETP), water suction tanks, and pump rooms, and (5) storage dedicated exclusively to Data Centers (Jan 2024 amendment). Conversely, any commercial retail in the first basement, bank safety vaults, strong rooms, hospital diagnostic labs/cold storages, or incidental tenant storage is <strong>fully counted in FSI</strong>.</li>
  <li><strong>Flushed Basement Setback Extension:</strong> Where a basement roof slab is constructed completely flush to the surrounding ground level, it may extend into the mandatory side and rear marginal distances up to <strong>1.50 m from the plot boundary</strong>. In Special Buildings, this flush basement top slab must be structurally engineered to support the dynamic axle weight of municipal fire fighting engines.</li>
  <li><strong>Basement Ventilation &amp; Drainage (Reg 9.11.2):</strong> Minimum clear height must be <strong>2.40 m from finished floor to the soffit (bottom) of structural beams</strong>. Natural ventilation openings must equal at least <strong>2.5% of the basement floor area</strong>, or be compensated by an engineered mechanical ventilation system (exhaust fans/fresh air blowers). Staircase shafts connecting basements to upper floors must be protected by fire-rated self-closing doors and ventilated draught lobbies.</li>
  <li><strong>Ramp Geometry &amp; Car Lifts (Reg 9.12):</strong>
    <ul style="margin-top:6px;">
      <li><em>Non-Vehicular Ramps:</em> Slope not steeper than <strong>1:10</strong> (max <strong>1:12 for hospitals and public assembly</strong>; minimum hospital width <strong>2.25 m</strong>).</li>
      <li><em>Vehicular Ramps:</em> Maximum slope of <strong>1 in 8</strong>. Requires at least <strong>two separate 3.00 m wide ramps</strong> at opposite ends, or <strong>one two-way ramp of minimum 6.00 m width</strong>.</li>
      <li><em>Small Plot Concessions:</em> For plots $\le 1,000\text{ sq.m}$, a single $3.00\text{ m}$ ramp or minimum <strong>2 Car Lifts</strong> is permitted. For plots up to $2,000\text{ sq.m}$, a single $6.00\text{ m}$ ramp or minimum 2 Car Lifts is permitted.</li>
    </ul>
  </li>
  <li><strong>Podiums &amp; Stilts (Reg 9.13 &amp; 9.16):</strong> Podiums must preserve a minimum <strong>6.00 m setback</strong> around the building for fire tender access. Recreational Open Space (ROS) may be placed on top of podium decks, with up to 15% covered by permissible clubhouse/gymnasium structures. Stilt floors mandate at least two sides completely open, a finished plinth $\le 15\text{ cm}$, and clear heights of <strong>2.40 m for conventional parking</strong> and <strong>4.50 m for hydraulic stack parking</strong>.</li>
</ul>
''',

    'statutory_extract': r"""9.11 BASEMENTS
9.11.1 Basement shall generally be constructed within the prescribed setbacks / margins with one or more level.
Following uses shall be permissible at free of FSI:
i) Air-conditioning equipment’s and other machines used for services and utilities of the building;
ii) Parking spaces;
iii) D.G. set room, meter room and electric substation, Effluent Treatment Plant, suction tank, pump room;
iv) Storage (only for use of Data Centre)

Following uses shall be permissible and counted in FSI:
a) Storage of household or other goods or ordinarily non-combustible material incidental to principle use;
b) Strong rooms, bank lockers, safe deposit vaults, laundry room, Radio / laser therapy, post mortem room, mortuary, medical shop and cold storage for hospital building etc.
c) Commercial use in first basement in case of shopping centre / shopping malls.
d) Uses strictly ancillary to the Principal use.
e) Nursing quarters as ancillary use to hospital in first basement, if it is 0.9 m. to 1.2 m. above ground level with proper ventilation.

Provided that,
i) If the basement is proposed flushing to average surrounding ground level, then such basement can be extended in side and rear margins upto 1.5 m. from the plot boundary.
ii) Multilevel basements may be permitted if the basement is used for parking.

9.11.2 Requirements of Basement:
a) Height >= 2.4 m. in every part from floor to soffit of beam.
b) Adequate ventilation area not less than 2.5% of basement area or mechanical ventilation.
c) Ceiling height min 0.9 m. and max 1.2 m. above ground level (does not apply to mechanically ventilated flushing basement).
d) Slab designed to withstand pressure of fire fighting vehicle where movement is proposed.
e) Separate access from main/alternate staircase with fire separation.

9.12 RAMP
9.12.1 Non Vehicular Ramp: Slope not steeper than 1 in 10 (1 in 12 for public offices, hospitals, assembly). Hospital ramp min width 2.25 m. Smoke stop door for height > 24 m.
9.12.2 Ramp to basements and upper storeys for vehicles: At least two ramps of min 3.0 m. width with slope not more than 1 : 8, preferably at opposite ends, OR one ramp of 6.0 m. width. Car lifts optional.
For two-wheeler: Two ramps of 2.0 m. or one ramp of 4.0 m. (slope <= 1:8).
Plot <= 1000 sq.m.: Only one ramp of 3.0 m. for car/two wheeler, or min 2 Car lifts.
Plot <= 2000 sq.m.: One ramp of min 6.0 m. width, or min 2 Car lifts.

9.13 PODIUM: Clear height >= 2.4 m. to beam soffit. 6.0 m. setback from boundary in special buildings. Designed for fire engine load. ROS on podium permitted per Reg 3.4.1(iii), with up to 15% structures.
9.16 STILT: Height below soffit of beam >= 2.4 m. At least two sides open. Stack parking height 4.50 m. Plinth <= 15 cm.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Free of FSI vs Counted Basement Uses</h4>
    </div>
    <div class="card-body">
      <p><strong>100% Free of FSI:</strong> Parking, AC plants, DG rooms, substations, ETPs, pump rooms, suction tanks, and Data Center storage. <strong>Counted in FSI:</strong> Mall retail in 1st basement, bank lockers, safe deposit vaults, cold storages, mortuaries, and tenant storage.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Flushed Basement Boundary Rule (1.50m)</h4>
    </div>
    <div class="card-body">
      <p>If a basement roof is completely flush with the ground, it can extend into side and rear marginal distances up to <strong>1.50 m from the plot boundary</strong>. The slab must be structurally certified to carry municipal fire engine axle loads in Special Buildings.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Vehicular Ramps &amp; Car Lift Options</h4>
    </div>
    <div class="card-body">
      <p>Standard vehicular ramps require a maximum slope of <strong>1 in 8</strong>. Provide <strong>two 3.00 m ramps</strong> at opposite ends or <strong>one 6.00 m ramp</strong>. On plots $\le 1,000\text{ sq.m}$, a single $3.00\text{ m}$ ramp or <strong>2 car lifts</strong> satisfies statutory compliance.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Podiums &amp; Stilt Headrooms</h4>
    </div>
    <div class="card-body">
      <p>Podiums and stilts mandate a minimum clear vertical clearance of <strong>2.40 m to the soffit of structural beams</strong>. Where mechanized stack parking tiers are deployed, clear height must be expanded up to <strong>4.50 m</strong>. Ground stilts must have plinths $\le 15\text{ cm}$.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Building Element</th>
        <th>Statutory Dimension / Minimum Width</th>
        <th>Permissible Gradient / Slope</th>
        <th>Beam Soffit Clear Height</th>
        <th>FSI Treatment &amp; Special Conditions</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Basement (Services &amp; Parking)</strong></td>
        <td>Within margins (or 1.5m flush)</td>
        <td>Level floor + drainage slope</td>
        <td><code>2.40 m</code> minimum</td>
        <td><strong>100% FREE OF FSI</strong> (Parking, AC, DG, ETP, Data Storage)</td>
      </tr>
      <tr>
        <td><strong>Basement (Commercial / Vaults)</strong></td>
        <td>First basement only for retail</td>
        <td>Level floor</td>
        <td><code>2.40 m - 3.00 m</code></td>
        <td><strong>COUNTED IN FSI</strong> (Retail malls, bank vaults, mortuary)</td>
      </tr>
      <tr>
        <td><strong>Vehicular Ramp (Two-Way)</strong></td>
        <td><code>6.00 m</code> width</td>
        <td>Max <code>1 : 8</code> (12.5%)</td>
        <td><code>2.40 m</code> headroom</td>
        <td>Can serve both basements and multi-level podiums</td>
      </tr>
      <tr>
        <td><strong>Vehicular Ramps (Opposed Pair)</strong></td>
        <td><code>3.00 m</code> width each</td>
        <td>Max <code>1 : 8</code> (12.5%)</td>
        <td><code>2.40 m</code> headroom</td>
        <td>Placed at opposite ends for continuous one-way loops</td>
      </tr>
      <tr>
        <td><strong>Two-Wheeler Dedicated Ramp</strong></td>
        <td><code>2.00 m</code> (pair) or <code>4.00 m</code> (single)</td>
        <td>Max <code>1 : 8</code> (12.5%)</td>
        <td><code>2.20 m</code> headroom</td>
        <td>Dedicated scooter ingress/egress</td>
      </tr>
      <tr>
        <td><strong>Hospital Pedestrian Ramp</strong></td>
        <td><code>2.25 m</code> width minimum</td>
        <td>Max <code>1 : 12</code> (8.33%)</td>
        <td><code>2.40 m</code> headroom</td>
        <td>Smoke stop doors mandatory for height &gt; 24.0 m</td>
      </tr>
      <tr>
        <td><strong>Podium Deck</strong></td>
        <td>Min 6.00 m setback from boundary</td>
        <td>Level slab with waterproofing</td>
        <td><code>2.40 m</code> (parking level)</td>
        <td>Must support 45-tonne fire engine; 15% ROS structures</td>
      </tr>
      <tr>
        <td><strong>Stilt Floor (Stack Parking)</strong></td>
        <td>Open on at least 2 sides</td>
        <td>Plinth &le; 15 cm above ground</td>
        <td><code>4.50 m</code> clear headroom</td>
        <td>Free of FSI if used strictly for vehicle parking / play</td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL ENGINEERING AUDIT: BASEMENT RAMP DESIGN &amp; FSI DETERMINATION</h4>
  <p><strong>Site Specifications:</strong> A commercial complex on a <strong>1,850 sq.m</strong> plot proposes a 2-level basement ($B_1$ and $B_2$) with floor-to-floor heights of $3.50\text{ m}$ (slab-to-slab) and $600\text{ mm}$ structural transfer beams.</p>
  
  <div class="step-box">
    <strong>Step 1: Verify Finished Headroom under Beams (Reg 9.11.2(a))</strong>
    <ul>
      <li>Floor-to-floor height: $3.50\text{ m}$.</li>
      <li>Deduct floor finish ($0.05\text{ m}$) + structural beam depth ($0.60\text{ m}$):</li>
      <li>$\text{Net Headroom under Soffit} = 3.50\text{ m} - 0.05\text{ m} - 0.60\text{ m} = \mathbf{2.85\text{ m}}$.</li>
      <li>Compliance: $2.85\text{ m} \ge 2.40\text{ m}$ required minimum (Compliant).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Vehicular Ramp Geometry &amp; Run Length (Reg 9.12.2)</strong>
    <ul>
      <li>Because the plot area ($1,850\text{ sq.m}$) is less than $2,000\text{ sq.m}$, the developer has two legal options:</li>
      <li><em>Option A:</em> Provide <strong>one single two-way ramp of minimum 6.00 m width</strong>.</li>
      <li><em>Option B:</em> Provide minimum <strong>2 Car Lifts</strong> instead of a vehicular ramp.</li>
      <li>Assuming Option A (6.00 m ramp) at maximum permissible slope of $1:8$ (12.5%):</li>
      <li>Vertical drop per floor: $3.50\text{ m}$.</li>
      <li>$\text{Required Ramp Horizontal Run} = 3.50\text{ m} \times 8 = \mathbf{28.00\text{ m}}$.</li>
      <li>Total horizontal straight ramp run needed from ground to $B_1$ is $28.00\text{ m}$ (or a curved circular ramp with an inner radius $\ge 4.50\text{ m}$).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: FSI Categorization of Basement Uses (Reg 9.11.1)</strong>
    <ul>
      <li>$B_2$ Level: $1,200\text{ sq.m}$ Parking + $150\text{ sq.m}$ DG/Substation/Pump room = <strong>100% Free of FSI</strong>.</li>
      <li>$B_1$ Level: $700\text{ sq.m}$ Parking + $500\text{ sq.m}$ Supermarket Retail:</li>
      <li>The $700\text{ sq.m}$ parking is <strong>Free of FSI</strong>.</li>
      <li>The $500\text{ sq.m}$ supermarket in the first basement is <strong>Strictly Counted in FSI</strong> under Regulation 9.11.1(c).</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>CRITICAL STRUCTURAL &amp; LIFE-SAFETY TRAPS IN BASEMENTS &amp; PODIUMS</h4>
  <ul class="warning-list">
    <li><strong>Ramp Slopes Steeper than 1:8:</strong> Designing vehicular ramps at 1:6 or 1:7 slope to save basement space. Municipal scrutiny software (BPAMS) strictly validates ramp grade lines and will automatically fail any proposal exceeding a 1:8 gradient.</li>
    <li><strong>Failing to Isolate Basement Staircases:</strong> Continuous internal staircases connecting basements to upper residential floors without a 2-hour fire-rated cut-off lobby or fire door will be instantly rejected by the Chief Fire Officer (CFO).</li>
    <li><strong>Extending Normal Basements into Setbacks:</strong> Only basements that are <em>completely flush with the surrounding ground level</em> are allowed to extend up to 1.50 m from the plot boundary under Reg 9.11.1 Proviso (i). A basement protruding 1.2 m above ground cannot infringe the standard setback!</li>
    <li><strong>Single Ramp on Plots &gt; 2,000 sq.m:</strong> On plots exceeding $2,000\text{ sq.m}$, providing a single 3.0 m ramp is illegal; the project must provide either two separate 3.0 m ramps at opposite ends, or a single 6.0 m wide ramp.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; Car Lift Modernization</h4>
  <p><strong>Corrigendum / Addendum No. CR 79/2021 &amp; CR 121/21 dt. 02-12-2021:</strong></p>
  <p>Under the original UDCPR-2020 text, narrow urban plots struggled to accommodate long ramp runs ($28\text{ m}+$ per basement level). The Government amended Regulation 9.12.2 to allow developers on plots up to $1,000\text{ sq.m}$ and $2,000\text{ sq.m}$ to install minimum <strong>2 Car Lifts</strong> in lieu of constructed vehicular ramps, unlocking efficient mechanized multi-level basement car parking.</p>
</div>
''',

    'quiz': [
      {
        'question': 'Which of the following basement uses is strictly COUNTED towards FSI under Regulation 9.11.1?',
        'options': [
          'Electrical substation and DG set room',
          'Suction tank and pump room',
          'Commercial shopping center use in the first basement',
          'Effluent Treatment Plant (ETP)'
        ],
        'answer': 2,
        'explanation': 'Regulation 9.11.1(c) explicitly dictates that "Commercial use in first basement in case of shopping centre / shopping malls" is permissible and counted in FSI.'
      },
      {
        'question': 'How close to the plot boundary can a basement extend in side and rear margins if its roof slab is flushing to ground level?',
        'options': [
          'Up to 0.0 m (touching the boundary line)',
          'Up to 1.5 m from the plot boundary',
          'Up to 3.0 m from the plot boundary',
          'Basements cannot extend into marginal distances under any condition'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.11.1 Proviso (i) states: "If the basement is proposed flushing to average surrounding ground level, then such basement can be extended in side and rear margins upto 1.5 m. from the plot boundary."'
      },
      {
        'question': 'What is the maximum permissible slope for a vehicular ramp to a basement or upper parking floor under Regulation 9.12.2?',
        'options': [
          '1 in 5 (20%)',
          '1 in 8 (12.5%)',
          '1 in 10 (10%)',
          '1 in 12 (8.33%)'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.12.2 mandates vehicular ramps with "slope not more than 1 : 8".'
      },
      {
        'question': 'What clear vertical height below the soffit of beams must be maintained in a stilt floor deploying hydraulic stack parking under Regulation 9.16?',
        'options': [
          '2.40 m',
          '3.00 m',
          '3.60 m',
          '4.50 m'
        ],
        'answer': 3,
        'explanation': 'Regulation 9.16 specifies: "In case of stack parking, clear height of 4.50 m. shall be maintained."'
      }
    ],

    'prev_url': '/lessons/reg-9-1-room-dimensions-and-height-clearances.html',
    'prev_title': 'Reg 9.1 to 9.8: Plinth Standards, Room Heights, Sanitary Sizes & Mezzanines',
    'next_url': '/lessons/reg-9-20-lighting-ventilation-and-shafts.html',
    'next_title': 'Reg 9.14 & 9.20 to 9.26: Light, Ventilation, Shafts & External Elements'
}
