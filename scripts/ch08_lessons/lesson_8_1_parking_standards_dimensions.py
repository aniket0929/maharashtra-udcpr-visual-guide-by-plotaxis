"""
UDCPR Visual Guide - CHAPTER 8, LESSON 1
Regulation 8.1 & 8.1.1(i)-(v): Parking Locations, Minimum Bay Dimensions & Circulation Aisles
File: scripts/ch08_lessons/lesson_8_1_parking_standards_dimensions.py
"""

lesson_data = {
    'filename': 'reg-8-1-parking-standards-and-dimensions.html',
    'lesson_id': 'reg-8-1-parking-standards-and-dimensions',
    'quiz_id': 'quiz-8-1',
    'clause': 'Reg. 8.1 & 8.1.1(i)-(v)',
    'title': 'Parking Locations, Minimum Bay Dimensions & Circulation Aisles',
    'badge_status': 'STATUTORY • TABLE 8-A',
    'ch_slug': 'ch08',
    'ch_title': 'Chapter 8: Parking, Loading and Unloading Spaces',
    'meta_desc': 'Master UDCPR Regulation 8.1: permissible parking locations (stilt, basement, podium), Table 8-A bay sizes (2.5x5.0m, 50% small car concession 2.3x4.5m, puzzle parking), 3.0m driveways, and composite conversions.',
    
    'lead_summary': (
        'Regulation 8.1 establishes the foundational engineering geometry for off-street vehicular parking across Maharashtra. '
        'It governs where parking can be sited (basements, stilts, podiums, separate multi-level garages), prescribes clear vertical headrooms '
        '(minimum 2.40 m under beam soffits; up to 4.50 m for stack parking), defines strict Table 8-A vehicle stall footprints (standard 2.50 m x 5.00 m '
        'with a statutory 50% concession for 2.30 m x 4.50 m compact stalls), mandates distinct circulation aisle widths (minimum 3.00 m for cars, 2.00 m for scooters), '
        'and permits modular composite stall substitutions.'
    ),
    
    'amendment_cite': 'Corrigendum / Addendum No. CR 79/2021 dt. 02nd December, 2021 (Stall downsizing & Mechanized puzzle parking dimensions)',
    
    'plain_summary_html': '''
<p>
  Every sanctioned building plan submitted under the UDCPR must contain a dedicated, dimensioned <strong>Vehicular Parking &amp; Circulation Layout</strong>. 
  Regulation 8.1.1 mandates that parking stalls must not exist in isolation; they must be paired with independent, unobstructed maneuvering aisles and driveways that connect directly to a public or private access street.
</p>
<p>
  Crucially, parking stalls may be sited across diverse building envelopes: in basements, on stilt floors, on podium decks, on upper floors of multi-level car parks (MLCP), in open surface yards, or within dedicated lock-up garages. However, architectural plans frequently encounter rejection due to structural headrooms: <strong>the 2.40 m minimum height under stilt parking is measured strictly from the underside (soffit) of the lowest structural beam</strong>, not the bottom of the slab. Where mechanical stack systems are introduced, a clear floor-to-beam height of up to 4.50 m is permissible.
</p>
<p>
  To optimize basement and podium space efficiency, the State Government issued Corrigendum CR 79/2021 on December 2, 2021, introducing two major relaxations:
</p>
<ul class="rule-list">
  <li><strong>50% Compact Car Allowance:</strong> Up to 50% of the mandatory four-wheeler parking stalls may be sized down from the standard 2.50 m x 5.00 m ($12.50\\text{ m}^2$) to 2.30 m x 4.50 m ($10.35\\text{ m}^2$).</li>
  <li><strong>Puzzle &amp; Mechanized Parking Sizes:</strong> Mechanized puzzle parking bays require 2.30 m x 5.80 m for large passenger vehicles (SUVs/sedans) and 2.10 m x 5.00 m for small passenger vehicles.</li>
  <li><strong>Independent Circulation:</strong> The parking bay footprint is purely for vehicle storage. Driveways (aisles) must measure at least 3.00 m clear width for four-wheelers and 2.00 m for two-wheelers, without column encroachments.</li>
</ul>
''',

    'statutory_extract': r"""8.1 PARKING SPACES
Wherever a property is to be developed or redeveloped, parking spaces at the scale laid down in these Regulations shall be provided. A parking plan showing the parking spaces along with manoeuvring spaces / aisles shall be submitted as a part of building plan. When additions are made to an existing building, the new parking requirements will be reckoned with reference to the additional space only and not to the whole of building but this concession shall not apply where the use is changed. The provisions for parking of vehicles for different occupancies shall be as given in Table No.8-A

8.1.1 General Space Requirements
i) Location of Parking Spaces: The parking spaces include parking spaces in basements or on a floor supported by stilts, podium or on upper floors, covered or uncovered spaces or in separate building in the plot and / or lock up garages. The height of the stilt shall not be less than 2.4 m. from the bottom of beam. In case of stack parking, height up to 4.5 m. may be allowed.

ii) Size of Parking Space: The minimum sizes of parking spaces to be provided shall be as shown below in Table No.8-A:
Table No.8-A - Parking Space Requirement:
1. Motor vehicle: 2.5 m. x 5.0 m.
2. Scooter, Motor Cycle: 1.0 m. x 2.0 m.
3. Transport vehicle / Ambulance / Mini Bus: 3.75 m. x 7.5 m.

Note:
(1) (a) In the case of parking spaces for motor vehicle, upto 50 percent of the prescribed space may be of the size of 2.3 m. x 4.5 m.
(1) (b) Minimum size of parking space in mechanized / puzzle parking system shall be 2.3 m. x 5.8 m. for big cars and 2.1 m. x 5.0 m. for small cars.

iii) Marking of Parking Spaces: Parking space shall be paved and clearly marked for different types of vehicles.

iv) Manoeuvring and Other Ancillary Spaces: Off street parking space must have adequate vehicular access to a street and the area shall be exclusive of drives, aisles and such other provisions required for adequate manoeuvring of vehicles. The width of drive for motor vehicles and scooter, motor cycle shall be minimum 3.00 m. and 2.00 m. respectively.

v) Composite parking: The composite parking of vehicles like one car with two scooters may be allowed. Also, six scooters' parking may be allowed to be converted in one car parking. In such cases, drives or aisles shall be required taking into consideration entire composite parking.""",

    'clause_cards_html': '''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Vertical Headroom Thresholds</h4>
    </div>
    <div class="card-body">
      <p>Stilt parking floors must guarantee a minimum vertical clearance of <strong>2.40 m</strong> measured from the finished floor to the <em>soffit (bottom) of the lowest structural beam</em> or fire-sprinkler header pipe. For hydraulic stack parking tiers, stilt or basement floor-to-beam clearances up to <strong>4.50 m</strong> are permitted.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Table 8-A Stall Dimensions</h4>
    </div>
    <div class="card-body">
      <p>Standard four-wheeler bays are <strong>2.50 m x 5.00 m</strong> ($12.50\\text{ m}^2$). Under Note (1)(a), exactly <strong>50%</strong> of the required car bays may be reduced to <strong>2.30 m x 4.50 m</strong> ($10.35\\text{ m}^2$). Two-wheelers mandate <strong>1.00 m x 2.00 m</strong> ($2.00\\text{ m}^2$). Commercial transport / ambulance bays mandate <strong>3.75 m x 7.50 m</strong> ($28.125\\text{ m}^2$).</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Driveway &amp; Aisle Geometry</h4>
    </div>
    <div class="card-body">
      <p>Parking stall dimensions are strictly net vehicle storage areas and cannot overlap maneuvering aisles. Internal one-way circulation driveways for four-wheelers must measure at least <strong>3.00 m clear width</strong>. Dedicated two-wheeler circulation aisles require a minimum of <strong>2.00 m clear width</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Composite Conversion Equivalence</h4>
    </div>
    <div class="card-body">
      <p>Regulation 8.1.1(v) legally authorizes modular stall swaps: an architect may design a tandem composite bay hosting <strong>1 Car + 2 Scooters</strong>. Furthermore, developers may substitute <strong>6 Scooter stalls</strong> into <strong>1 standard Car stall</strong> (or vice-versa), provided circulation aisles satisfy the larger vehicle requirement.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': '''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Vehicle Type / System</th>
        <th>Standard Dimension (W x L)</th>
        <th>Net Floor Area</th>
        <th>Concession / Variant (Corrigendum 2021)</th>
        <th>Clear Driveway Aisle</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Motor Vehicle (Standard Car)</strong></td>
        <td><code>2.50 m x 5.00 m</code></td>
        <td><code>12.50 sq.m</code></td>
        <td>Upto 50% stalls can be <code>2.30 m x 4.50 m</code> (10.35 sq.m)</td>
        <td><code>3.00 m</code> minimum</td>
      </tr>
      <tr>
        <td><strong>Mechanized / Puzzle (Big Car / SUV)</strong></td>
        <td><code>2.30 m x 5.80 m</code></td>
        <td><code>13.34 sq.m</code></td>
        <td>Platform clear tray size; pit/headroom per manufacturer</td>
        <td><code>3.00 m</code> minimum</td>
      </tr>
      <tr>
        <td><strong>Mechanized / Puzzle (Small Car)</strong></td>
        <td><code>2.10 m x 5.00 m</code></td>
        <td><code>10.50 sq.m</code></td>
        <td>Compact tray platform for hatchbacks/sedans</td>
        <td><code>3.00 m</code> minimum</td>
      </tr>
      <tr>
        <td><strong>Scooter / Motorcycle (Two-Wheeler)</strong></td>
        <td><code>1.00 m x 2.00 m</code></td>
        <td><code>2.00 sq.m</code></td>
        <td>6 Scooter stalls = 1 Car stall equivalent</td>
        <td><code>2.00 m</code> minimum</td>
      </tr>
      <tr>
        <td><strong>Transport / Ambulance / Mini Bus</strong></td>
        <td><code>3.75 m x 7.50 m</code></td>
        <td><code>28.13 sq.m</code></td>
        <td>Heavy transport vehicle &amp; hospital ambulance bay</td>
        <td><code>4.50 m - 6.00 m</code></td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL ARCHITECTURAL CALCULATION: BASEMENT STALL &amp; AISLE ALLOCATION</h4>
  <p><strong>Project Profile:</strong> A proposed multi-family residential building in Pune requires <strong>120 Car parking spaces</strong> and <strong>150 Two-Wheeler spaces</strong> as per Table 8-B.</p>
  
  <div class="step-box">
    <strong>Step 1: Applying the 50% Compact Car Allowance (Note 1a)</strong>
    <p>Under Note (1)(a) to Table 8-A (Corrigendum CR 79/2021), up to 50% of car bays may be compact size:</p>
    <ul>
      <li>Standard Car Stalls (50%): $120 \times 0.50 = 60\text{ stalls}$ @ $2.50\text{ m} \times 5.00\text{ m} = 12.50\text{ m}^2/\text{stall}$ (Total = $750.00\text{ m}^2$)</li>
      <li>Compact Car Stalls (50%): $120 \times 0.50 = 60\text{ stalls}$ @ $2.30\text{ m} \times 4.50\text{ m} = 10.35\text{ m}^2/\text{stall}$ (Total = $621.00\text{ m}^2$)</li>
      <li><strong>Total Net Car Bay Footprint:</strong> $750.00 + 621.00 = 1,371.00\text{ m}^2$</li>
      <li><em>Space Saved compared to all-standard:</em> $(120 \times 12.5) - 1,371 = 1,500 - 1,371 = \mathbf{129.00\text{ m}^2}$ (enough space for 12 extra compact cars or 64 scooters).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Scooter Bay Space Requirements</strong>
    <p>150 Scooters @ $1.00\text{ m} \times 2.00\text{ m} = 2.00\text{ m}^2/\text{stall}$:</p>
    <ul>
      <li>Net Two-Wheeler Footprint: $150 \times 2.00\text{ m}^2 = \mathbf{300.00\text{ m}^2}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Maneuvering Driveways &amp; Column Grid Coordination</strong>
    <ul>
      <li>Car Aisle Width: Mandatory minimum $3.00\text{ m}$ unobstructed aisle between double rows of parking.</li>
      <li>Structural Grid Recommendation: A column-to-column grid of $7.50\text{ m}$ clear span accommodates exactly $3$ standard car bays ($3 \times 2.50\text{ m}$) or $3$ compact bays plus columns ($3 \times 2.30\text{ m} = 6.90\text{ m} + 0.60\text{ m}$ column width).</li>
      <li>Clear Height Verification: Finished basement floor to underside of transfer beams must measure $\ge 2.40\text{ m}$.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': '''
<div class="alert-box alert-warning">
  <h4>CRITICAL COMPLIANCE TRAPS IN REGULATION 8.1</h4>
  <ul class="warning-list">
    <li><strong>Column Encroachment into 2.50m Width:</strong> Scrutiny officers will reject plans where a structural column (e.g., $300\text{ mm} \times 600\text{ mm}$) encroaches into the $2.50\text{ m}$ width of a parking bay. The $2.50\text{ m} \times 5.00\text{ m}$ rectangle must be completely unencumbered inside clear paint lines.</li>
    <li><strong>Measuring Stilt Clearance from Slab:</strong> Measuring stilt height from the ceiling slab rather than the bottom of structural beams. If the beam drops $600\text{ mm}$ and the floor-to-slab height is $2.80\text{ m}$, the net clear height is only $2.20\text{ m}$, which violates the statutory $2.40\text{ m}$ clear stilt requirement.</li>
    <li><strong>Overusing Compact Car Allowance:</strong> Note (1)(a) restricts compact stalls ($2.30\text{ m} \times 4.50\text{ m}$) to a maximum of <strong>50%</strong> of the total prescribed car spaces. Providing 60% compact cars will trigger a statutory deficit objection.</li>
    <li><strong>Counting Driveway Space as Bay Length:</strong> Parking stalls must not infringe upon the $3.00\text{ m}$ maneuvering driveway. The rear bumper of a parked car cannot overhang into the required $3.00\text{ m}$ circulation aisle.</li>
  </ul>
</div>
''',

    'amendment_section_html': '''
<div class="amendment-card">
  <h4>Statutory History &amp; Corrigendum CR 79/2021</h4>
  <p><strong>Corrigendum / Addendum No. CR 79/2021 (Dated 02-12-2021):</strong></p>
  <p>Under the initial UDCPR publication in December 2020, all four-wheeler parking stalls were strictly mandated at $2.5\text{ m} \times 5.0\text{ m}$, creating severe layout friction on constrained urban plots with deep column grids. The Urban Development Department added Note (1)(a) permitting 50% compact cars ($2.3\text{ m} \times 4.5\text{ m}$) and Note (1)(b) standardizing puzzle/mechanized pallet trays ($2.3\text{ m} \times 5.8\text{ m}$ for large cars, $2.1\text{ m} \times 5.0\text{ m}$ for small cars).</p>
</div>
''',

    'quiz': [
      {
        'question': 'What is the statutory minimum clear height required for a stilt parking floor under Regulation 8.1.1(i)?',
        'options': [
          '2.10 m from finished floor to ceiling slab',
          '2.40 m measured from finished floor to the bottom of the structural beam',
          '3.00 m from floor to floor',
          '2.75 m clear of all electrical conduits'
        ],
        'answer': 1,
        'explanation': 'Regulation 8.1.1(i) explicitly mandates that "The height of the stilt shall not be less than 2.4 m. from the bottom of beam."'
      },
      {
        'question': 'Under Note (1)(a) of Table 8-A (Corrigendum CR 79/2021), what percentage of motor vehicle parking spaces may be reduced to 2.3 m x 4.5 m?',
        'options': [
          'Up to 25 percent',
          'Up to 33.33 percent',
          'Up to 50 percent',
          '100 percent in congested areas only'
        ],
        'answer': 2,
        'explanation': 'Note (1)(a) provides that "In the case of parking spaces for motor vehicle, upto 50 percent of the prescribed space may be of the size of 2.3 m. x 4.5 m."'
      },
      {
        'question': 'What is the minimum clear driveway width required for four-wheeler motor vehicles under Regulation 8.1.1(iv)?',
        'options': [
          '2.50 m',
          '3.00 m',
          '3.75 m',
          '4.50 m'
        ],
        'answer': 1,
        'explanation': 'Regulation 8.1.1(iv) specifies: "The width of drive for motor vehicles and scooter, motor cycle shall be minimum 3.00 m. and 2.00 m. respectively."'
      },
      {
        'question': 'According to Regulation 8.1.1(v), how many scooter parking spaces may be converted into one car parking space?',
        'options': [
          '3 scooters',
          '4 scooters',
          '6 scooters',
          '8 scooters'
        ],
        'answer': 2,
        'explanation': 'Regulation 8.1.1(v) states: "Also, six scooters\' parking may be allowed to be converted in one car parking."'
      }
    ],

    'prev_url': '/lessons/reg-7-13-cbd-commercial-and-green-buildings.html',
    'prev_title': 'Reg 7.10 to 7.13: CBD Commercial Towers & Green Incentives',
    'next_url': '/lessons/reg-8-1-8-loading-spaces-ramps-and-marginal-parking.html',
    'next_title': 'Reg 8.1.1(vi)-(viii): Loading Berths, Basement Ramps & Marginal Parking'
}
