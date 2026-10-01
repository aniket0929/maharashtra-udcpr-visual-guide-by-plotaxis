"""
UDCPR FROM SCRATCH - CHAPTER 9, LESSON 4
Regulation 9.27 & 9.28: Exit Requirements, Staircase Widths, Occupant Loads & Travel Distances
File: scripts/ch09_lessons/lesson_9_4_exits_staircases_occupant_load.py
"""

lesson_data = {
    'filename': 'reg-9-28-exit-requirements-and-staircases.html',
    'lesson_id': 'reg-9-28-exit-requirements-and-staircases',
    'quiz_id': 'quiz-9-4',
    'clause': 'Reg. 9.27 & 9.28',
    'title': 'Exit Requirements, Staircase Widths, Occupant Loads & Travel Distances',
    'badge_status': 'FIRE EVACUATION • TABLES 9-D, 9-E, 9-F, 9-G',
    'ch_slug': 'ch09',
    'ch_title': 'Chapter 9: Requirements of Parts of Buildings',
    'meta_desc': 'Master UDCPR Regulation 9.27 & 9.28: lift thresholds (>15m, >24m, senior housing), Table 9-D travel distances (22.5m/30m + 50% sprinkler bonus), Table 9-E occupant loads, Table 9-F exit unit capacities (50cm), and Table 9-G staircase widths.',
    
    'lead_summary': (
        'Regulations 9.27 and 9.28 constitute the core life-safety evacuation engine of the UDCPR, harmonizing Maharashtra’s planning laws with Part IV of the National Building Code (NBC-2016). '
        'They govern passenger lift thresholds (at least 1 lift for buildings > 15 m; at least 2 lifts for buildings > 24 m; compulsory for senior citizen homes regardless of height), '
        'define Table 9-D travel distances (22.50 m for residential/institutional and 30.00 m for commercial/assembly, with a statutory 50% extension for fully sprinklered buildings), '
        'establish Table 9-E occupant load factors (12.5 sq.m/person for residential, 4.0 for schools, 10.0 for business), compute emergency egress capacity via 50 cm exit units (Table 9-F), '
        'enforce dual fire escape staircases for Special Buildings, and dictate non-negotiable Table 9-G staircase widths (from 1.00 m up to 2.00 m).'
    ),
    
    'amendment_cite': 'Corrigendum CR 79/2021 (+50% travel distance with sprinklers) & CR 121/21 (Internal duplex & mezzanine stairs)',
    
    'plain_summary_html': r'''
<p>
  Building evacuation during a fire or structural emergency is governed by strict mathematical laws under Regulation 9.28. Architects must calculate the population of each floor, verify that the furthest occupant can reach a fire-isolated exit within permitted travel distances, and size staircases, ramps, and doorways to evacuate that population without bottleneck surges:
</p>
<ul class="rule-list">
  <li><strong>Passenger Lifts &amp; Senior Housing (Reg 9.27):</strong> At least <strong>1 lift</strong> is mandatory for any building taller than <strong>15.0 m</strong>. For buildings exceeding <strong>24.0 m</strong>, at least <strong>2 lifts</strong> must be provided. For Senior Citizen Housing or Retirement Homes, lifts are legally mandatory <em>regardless of the building height</em>. Lifts must feature a ground-floor fireman switch, but can never be counted as statutory emergency exits.</li>
  <li><strong>Table 9-D Travel Distances &amp; Sprinkler Concession:</strong> The travel distance from the farthest corner of a floor to the nearest protected exit cannot exceed <strong>22.50 m</strong> for residential, educational, institutional, and hazardous buildings, or <strong>30.00 m</strong> for commercial, assembly, business, and industrial occupancies. Under Corrigendum CR 79/2021, if a building is protected by a <strong>100% comprehensive fire sprinkler system</strong>, these travel distances may be increased by <strong>50%</strong> (to <strong>33.75 m</strong> and <strong>45.00 m</strong> respectively).</li>
  <li><strong>Table 9-E Occupant Loads:</strong> Used to determine design population:
    <ul style="margin-top:6px;">
      <li><em>Residential:</em> <strong>12.5 sq.m carpet area per person</strong>.</li>
      <li><em>Educational:</em> <strong>4.0 sq.m per person</strong> (classrooms).</li>
      <li><em>Assembly:</em> <strong>0.6 sq.m per person</strong> (with fixed seating / dance floors) or <strong>1.5 sq.m</strong> (dining/loose seats).</li>
      <li><em>Mercantile (Retail):</em> <strong>3.0 sq.m per person</strong> on street floors/sales basements; <strong>6.0 sq.m</strong> on upper retail floors.</li>
      <li><em>Corporate Business &amp; Offices:</em> <strong>10.0 sq.m per person</strong>.</li>
    </ul>
  </li>
  <li><strong>Table 9-F Unit Exit Width Capacity:</strong> Exit widths are calculated in standard units of <strong>50 cm (0.50 m)</strong>. In residential buildings, one 50 cm unit discharges <strong>25 persons via stairways</strong>, <strong>50 persons via ramps</strong>, and <strong>75 persons via doors</strong>. In commercial/office buildings, one unit discharges <strong>50 persons via stairways</strong>.</li>
  <li><strong>Table 9-G Minimum Staircase Widths:</strong>
    <ul style="margin-top:6px;">
      <li><em>Multi-storied Residential $\le 15\text{ m}$:</em> Minimum <strong>1.00 m</strong>.</li>
      <li><em>Multi-storied Residential $15\text{ m} - 24\text{ m}$:</em> Minimum <strong>1.20 m</strong>.</li>
      <li><em>Multi-storied Residential &gt; 24\text{ m}$:</em> Minimum <strong>1.50 m</strong>.</li>
      <li><em>Assembly &amp; Institutional / Schools:</em> Minimum <strong>2.00 m</strong>.</li>
      <li><em>All other commercial/industrial:</em> Minimum <strong>1.50 m</strong>.</li>
      <li><em>Internal duplex stairs:</em> Minimum <strong>0.75 m</strong>; Mezzanines: Minimum <strong>0.90 m</strong>.</li>
    </ul>
  </li>
  <li><strong>Two Staircases for Special Buildings (Reg 9.28.7):</strong> All Special Buildings (towers $>15\text{m}$, assembly, commercial $>500\text{ sq.m}$, hospitals, hazardous) must provide <strong>at least two separate staircases</strong>, one of which must be a dedicated external fire escape staircase. Enclosing staircases around lift shafts is prohibited unless isolated by 1-hour fire stop doors at every level.</li>
</ul>
''',

    'statutory_extract': r"""9.27 PROVISION OF LIFT
9.27.1 Planning and Design: Atleast one lift shall be provided in every building more than 15 m. in height. In case of buildings more than 24 m. height, atleast two lifts shall be provided... For building or floors of the building to be constructed for Retirement Home or Senior Citizen Housing, lift shall be provided irrespective of height of building... The lifts provided in the buildings shall not be considered as a means of escape in case of emergency. Grounding switch at ground floor level to enable the fire service to ground the lift cars in an emergency shall also be provided.

9.28 EXIT REQUIREMENTS
9.28.4 Arrangement of Exits: Exits shall be so located that the travel distance on the floor shall not exceed as given below:
Table No.9-D:
- Residential, Educational, institutional and Hazardous: 22.5 m.
- Assembly, business, mercantile, Industrial and Storage: 30.0 m.
Note: For the buildings where sprinkler system has been provided in entire building for fire fighting, the travel distance may be increased by 50% of the value specified in above table.

9.28.5 Occupant Load: Table No.9-E:
1. Residential: 12.5 sq.m. per person
2. Educational: 4.0 sq.m. per person
3. Institutional: 15 sq.m. per person (dormitories 7.5 sq.m.)
4. Assembly: a) With fixed/loose seat: 0.6 sq.m. | b) Without seating: 1.5 sq.m.
5. Mercantile: a) Street floor & sales basement: 3 sq.m. | b) Upper sale floors: 6 sq.m.
6. Business and industrial: 10 sq.m. per person
7. Storage: 30 sq.m. per person
8. Hazardous: 10 sq.m. per person

9.28.6 Capacity of Exits: Unit of exit width = 50 cm. (25 cm = half unit).
Table No.9-F - Number of Occupants per unit exit width:
- Residential/Educational/Institutional: Stairways 25 | Ramps 50 | Doors 75
- Assembly: Stairways 40 | Ramps 50 | Doors 60
- Business/Mercantile/Industrial/Storage: Stairways 50 | Ramps 60 | Doors 75
- Hazardous: Stairways 25 | Ramps 30 | Doors 40

9.28.7 Provision for Staircase: All buildings > ground floor need 1 staircase. Special buildings shall have two staircases out of which one shall be fire escape staircase. Enclosed type. At least one on external walls. Not provided around lift shaft unless fire stop door of 1 hour rating provided at every floor.

9.28.8 Width of staircase: Table No.9-G:
1. Residential: a) Individual upto G+2: 0.75 m. | b) Multi-storied upto 15 m.: 1.00 m. | c) Multi-storied 15m to 24m: 1.20 m. | d) Multi-storied above 24m: 1.50 m.
2. Residential hotel: 1.50 m.
3. Assembly Building (theatres, auditoriums, multiplex, mangal karyalaya): 2.00 m.
4. Institutional & Educational: 2.00 m.
5. All other buildings: 1.50 m.
Note: Internal staircase for duplex min 0.75 m.; mezzanine min 0.90 m.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Lift Thresholds &amp; Fire Controls</h4>
    </div>
    <div class="card-body">
      <p>Mandatory <strong>$\ge 1$ lift for $>15\text{ m}$</strong> height; <strong>$\ge 2$ lifts for $>24\text{ m}$</strong> height. Senior housing mandates lifts at any height. Lifts require a ground-floor fireman recall switch and can never be counted as means of escape.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Travel Distance &amp; Sprinkler Bonus</h4>
    </div>
    <div class="card-body">
      <p>Table 9-D: Max <strong>22.50 m</strong> for residential/educational/institutional; <strong>30.00 m</strong> for commercial/business/assembly. <strong>+50% bonus with complete sprinkler protection</strong> (extending limits to <strong>33.75 m</strong> and <strong>45.00 m</strong>).</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Exit Units &amp; Occupant Population</h4>
    </div>
    <div class="card-body">
      <p>Occupant load: <strong>12.5 sq.m/person</strong> for residential, <strong>10.0 sq.m</strong> for offices, <strong>4.0 sq.m</strong> for schools, <strong>0.6 sq.m</strong> for auditoriums. Capacity: 1 exit unit ($50\text{ cm}$) evacuates <strong>25 residential</strong> or <strong>50 commercial</strong> persons per flight.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Table 9-G Minimum Staircase Widths</h4>
    </div>
    <div class="card-body">
      <p>Multi-family residential: <strong>1.00 m</strong> ($\le 15\text{m}$), <strong>1.20 m</strong> ($15-24\text{m}$), <strong>1.50 m</strong> ($>24\text{m}$). Assembly and Educational: <strong>2.00 m</strong>. Duplex internal stairs: <strong>0.75 m</strong>. Mezzanines: <strong>0.90 m</strong>. Special Buildings mandate <strong>two separate staircases</strong>.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Building Occupancy Type</th>
        <th>Occupant Load (Sq.m / Person)</th>
        <th>Max Travel Distance (Standard)</th>
        <th>Max Travel Distance (Sprinklered)</th>
        <th>Minimum Staircase Width (Table 9-G)</th>
        <th>Stairway Capacity (Persons / 50cm Unit)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Residential ($\le 15\text{ m}$)</strong></td>
        <td><code>12.5 sq.m</code></td>
        <td><code>22.50 m</code></td>
        <td><code>33.75 m</code> (+50%)</td>
        <td><code>1.00 m</code> (2 units)</td>
        <td>25 persons / unit</td>
      </tr>
      <tr>
        <td><strong>Residential ($15\text{ m} - 24\text{ m}$)</strong></td>
        <td><code>12.5 sq.m</code></td>
        <td><code>22.50 m</code></td>
        <td><code>33.75 m</code> (+50%)</td>
        <td><code>1.20 m</code></td>
        <td>25 persons / unit</td>
      </tr>
      <tr>
        <td><strong>Residential High-Rise ($&gt; 24\text{ m}$)</strong></td>
        <td><code>12.5 sq.m</code></td>
        <td><code>22.50 m</code></td>
        <td><code>33.75 m</code> (+50%)</td>
        <td><code>1.50 m</code> (3 units)</td>
        <td>25 persons / unit</td>
      </tr>
      <tr>
        <td><strong>Commercial Office / IT</strong></td>
        <td><code>10.0 sq.m</code></td>
        <td><code>30.00 m</code></td>
        <td><code>45.00 m</code> (+50%)</td>
        <td><code>1.50 m</code> (3 units)</td>
        <td>50 persons / unit</td>
      </tr>
      <tr>
        <td><strong>Mercantile (Ground / Street)</strong></td>
        <td><code>3.0 sq.m</code></td>
        <td><code>30.00 m</code></td>
        <td><code>45.00 m</code> (+50%)</td>
        <td><code>1.50 m</code></td>
        <td>50 persons / unit</td>
      </tr>
      <tr>
        <td><strong>Educational / School</strong></td>
        <td><code>4.0 sq.m</code></td>
        <td><code>22.50 m</code></td>
        <td><code>33.75 m</code> (+50%)</td>
        <td><code>2.00 m</code> (4 units)</td>
        <td>25 persons / unit</td>
      </tr>
      <tr>
        <td><strong>Assembly / Theatres / Banquets</strong></td>
        <td><code>0.6 - 1.5 sq.m</code></td>
        <td><code>30.00 m</code></td>
        <td><code>45.00 m</code> (+50%)</td>
        <td><code>2.00 m</code> (4 units)</td>
        <td>40 persons / unit</td>
      </tr>
      <tr>
        <td><strong>Institutional / Hospital</strong></td>
        <td><code>15.0 sq.m</code> (7.5 dorm)</td>
        <td><code>22.50 m</code></td>
        <td><code>33.75 m</code> (+50%)</td>
        <td><code>2.00 m</code> (4 units)</td>
        <td>25 persons / unit</td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL LIFE-SAFETY CALCULATION: COMMERCIAL FLOOR POPULATION &amp; STAIRCASE SIZING</h4>
  <p><strong>Building Profile:</strong> A 6-storey commercial corporate office building in Pune. Each typical upper office floor has a net carpet area of <strong>1,200 sq.m</strong>. The building is fitted with a complete automated fire sprinkler system.</p>
  
  <div class="step-box">
    <strong>Step 1: Calculate Floor Design Population (Occupant Load - Table 9-E)</strong>
    <ul>
      <li>Business / Corporate Office Occupant Load Factor: <strong>10.0 sq.m carpet area per person</strong>.</li>
      <li>$\text{Floor Population} = \frac{1,200\text{ sq.m}}{10.0\text{ sq.m/person}} = \mathbf{120\text{ Persons per floor}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Determine Required Units of Exit Width (Table 9-F)</strong>
    <ul>
      <li>Under Table 9-F, for Business occupancies, the capacity of stairways is <strong>50 persons per unit of exit width (50 cm)</strong>:</li>
      <li>$\text{Exit Units Required} = \frac{120\text{ persons}}{50\text{ persons/unit}} = 2.4\text{ units}$.</li>
      <li>Rounding up to nearest half unit (25 cm): 2.4 rounds up to <strong>2.5 units</strong>.</li>
      <li>$\text{Total Required Staircase Width} = 2.5 \times 0.50\text{ m} = \mathbf{1.25\text{ m total width}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Apply Special Building Dual Staircase &amp; Table 9-G Baselines</strong>
    <ul>
      <li>Because this is a commercial office building with carpet area $> 500\text{ sq.m}$, it is classified as a <strong>Special Building</strong> under Regulation 1.3(93)(xiv).</li>
      <li>Regulation 9.28.7 requires <strong>at least two separate staircases</strong> (one internal, one fire escape).</li>
      <li>Table 9-G Item 5 prescribes that the minimum width for commercial buildings is <strong>1.50 m per staircase</strong>.</li>
      <li>Therefore, although 1.25 m is mathematically enough for the occupant load, the statute dictates:</li>
      <li><strong>Final Architecture: Exactly 2 Staircases of 1.50 m width each (Total Exit Width = 3.00 m)</strong>.</li>
      <li>Travel Distance Check: With complete sprinkler coverage, the permissible travel distance is $30.0\text{ m} \times 1.50 = \mathbf{45.00\text{ m}}$ to either staircase door.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>COMMON EVACUATION &amp; LIFE-SAFETY DESIGN DEFECTS</h4>
  <ul class="warning-list">
    <li><strong>Single Staircase in Buildings &gt; 15m or &gt; 500 sq.m:</strong> Providing only one central staircase in a building categorized as a Special Building. Reg 9.28.7 makes two separate, isolated staircases legally non-negotiable.</li>
    <li><strong>Enclosing Staircase Around Open Lift Shaft:</strong> Wrapping a staircase flight around an unprotected glass or mesh lift shaft without 1-hour fire rated enclosure walls and doors. CFO clearance will be withheld until fire-rated compartmentation is built.</li>
    <li><strong>Relying on Sprinkler Bonus Without 100% Coverage:</strong> Applying the 50% travel distance extension (45m instead of 30m) when sprinklers are only installed in basements and lobbies. Corrigendum CR 79/2021 requires sprinklers in the <em>entire building</em>.</li>
    <li><strong>Omitting Lifts in 2-Storey Senior Citizen Housing:</strong> Assuming lifts are only required above 15m. Reg 9.27.1 explicitly mandates lifts for Retirement Homes and Senior Citizen Housing <em>irrespective of building height</em>.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; Sprinkler Safety Incentives</h4>
  <p><strong>Corrigendum / Addendum No. CR 79/2021 dt. 02-12-2021:</strong></p>
  <p>Added the Note to Table 9-D authorizing a 50% extension in statutory travel distances for buildings equipped with comprehensive automatic sprinkler networks. This aligned the UDCPR with modern international performance-based fire codes, encouraging developers to invest in active sprinkler suppression systems across high-density floor plates.</p>
</div>
''',

    'quiz': [
      {
        'question': 'At what building height does the provision of at least two passenger lifts become mandatory under Regulation 9.27.1?',
        'options': [
          'More than 15.0 m',
          'More than 24.0 m',
          'More than 36.0 m',
          'More than 45.0 m'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.27.1 explicitly specifies: "Atleast one lift shall be provided in every building more than 15 m. in height. In case of buildings more than 24 m. height, atleast two lifts shall be provided."'
      },
      {
        'question': 'What is the maximum permissible travel distance for a residential floor protected by a complete automatic sprinkler system under Table 9-D?',
        'options': [
          '22.50 m',
          '30.00 m',
          '33.75 m (22.5 m + 50%)',
          '45.00 m'
        ],
        'answer': 2,
        'explanation': 'Table 9-D prescribes 22.5 m for residential occupancies, and the Note inserted via Corrigendum CR 79/2021 permits a 50% increase for fully sprinklered buildings: 22.5 m x 1.50 = 33.75 m.'
      },
      {
        'question': 'What is the statutory minimum width of a staircase in a multi-storied residential building having a height above 24.0 metres under Table 9-G?',
        'options': [
          '1.00 m',
          '1.20 m',
          '1.50 m',
          '2.00 m'
        ],
        'answer': 2,
        'explanation': 'Table 9-G Item 1(d) dictates a minimum width of 1.50 m for multi-storied residential buildings above 24 m in height.'
      },
      {
        'question': 'Under Table 9-E, what occupant load floor area factor is assigned per person for corporate business and office buildings?',
        'options': [
          '4.0 sq.m per person',
          '6.0 sq.m per person',
          '10.0 sq.m per person',
          '12.5 sq.m per person'
        ],
        'answer': 2,
        'explanation': 'Table 9-E Item 6 prescribes an occupant load of 10 sq.m floor area per person for Business and industrial occupancies.'
      }
    ],

    'prev_url': '/lessons/reg-9-20-lighting-ventilation-and-shafts.html',
    'prev_title': 'Reg 9.14 & 9.20 to 9.26: Light, Ventilation, Shafts & External Elements',
    'next_url': '/lessons/reg-9-29-refuge-areas-fire-towers-and-amenities.html',
    'next_title': 'Reg 9.29 to 9.33: Refuge Areas, Fire Towers, Chutes & Housing Amenities'
}
