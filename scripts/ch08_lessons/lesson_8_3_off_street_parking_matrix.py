"""
UDCPR FROM SCRATCH - CHAPTER 8, LESSON 3
Regulation 8.2 & Table 8-B: Off-Street Parking Matrix, Tenement Tiers & Commercial Standards
File: scripts/ch08_lessons/lesson_8_3_off_street_parking_matrix.py
"""

lesson_data = {
    'filename': 'reg-8-2-off-street-parking-matrix-and-residential-norms.html',
    'lesson_id': 'reg-8-2-off-street-parking-matrix-and-residential-norms',
    'quiz_id': 'quiz-8-3',
    'clause': 'Reg. 8.2 & Table 8-B',
    'title': 'Off-Street Parking Matrix, Tenement Tiers & Commercial Standards',
    'badge_status': 'TABLE 8-B • BASE QUOTAS',
    'ch_slug': 'ch08',
    'ch_title': 'Chapter 8: Parking, Loading and Unloading Spaces',
    'meta_desc': 'Master UDCPR Regulation 8.2 and Table 8-B: multi-family residential tenement size tiers (>=150, 80-150, 40-80, 30-40, <30 sqm), 5% visitor parking, hotels, hospitals, assembly, mercantile, IT, and small plot exemptions.',
    
    'lead_summary': (
        'Regulation 8.2 and Table 8-B prescribe the statutory baseline matrix for off-street vehicular accommodation across every occupancy class in Maharashtra. '
        'For multi-family housing, parking entitlements scale dynamically across five strict carpet area tiers: from ultra-luxury units (>= 150 sq.m: 2 cars + 1 scooter) '
        'down to affordable tenements (< 30 sq.m: 0 cars + 2 scooters per 2 units), supplemented by a mandatory 5% visitor parking overlay. '
        'It outlines precise standards for hospitality, medical institutions (including mandatory ambulance bays), auditoriums, retail mercantile, corporate offices, '
        'and specialized IT / Data Center facilities, while exempting small single-family bungalows (<= 300 sq.m) and tiny retail shops (<= 100 sq.m).'
    ),
    
    'amendment_cite': 'Notifications dt. 28-12-2022 (Residential scooter rationalization) & 12-01-2024 (Data Center standard: 1 car / 400 sq.m)',
    
    'plain_summary_html': r'''
<p>
  Table 8-B forms the universal baseline for calculating car and two-wheeler parking in Maharashtra. Unlike earlier regional by-laws that pegged parking to gross built-up area, the UDCPR calibrates parking directly against <strong>unit carpet area</strong> for residential occupancies and <strong>net floor carpet area</strong> for non-residential uses.
</p>
<p>
  <strong>The 5 Residential Tenement Tiers (Per Tenement / Pair):</strong>
</p>
<ul class="rule-list">
  <li><strong>Tier 1 ($\ge 150\text{ sq.m}$ carpet):</strong> 2 Cars + 1 Scooter per tenement (both Congested and Non-Congested).</li>
  <li><strong>Tier 2 ($80\text{ to } <150\text{ sq.m}$ carpet):</strong> 1 Car + 1 Scooter per tenement.</li>
  <li><strong>Tier 3 ($40\text{ to } <80\text{ sq.m}$ carpet):</strong> 1 Car + 2 Scooters for every <em>two tenements</em>.</li>
  <li><strong>Tier 4 ($30\text{ to } <40\text{ sq.m}$ carpet):</strong> For every two tenements: 1 Car + 1 Scooter (Congested) or 1 Car + 2 Scooters (Non-Congested).</li>
  <li><strong>Tier 5 ($<30\text{ sq.m}$ carpet):</strong> For every two tenements: 0 Cars + 2 Scooters.</li>
  <li><strong>Mandatory Visitor Parking:</strong> In addition to the tenement quotas, an extra <strong>5% visitor parking</strong> is legally required across all residential categories.</li>
</ul>
<p>
  <strong>Small Plot &amp; Bungalow Relief:</strong>
  Under Note (ii), independent single-family residential bungalows on plots up to $300\text{ sq.m}$ are exempt from off-street parking layout scrutiny. Instead, a corner garage measuring between $2.5\text{ m} \times 5.0\text{ m}$ ($12.5\text{ sq.m}$) and $3.0\text{ m} \times 6.0\text{ m}$ ($18.0\text{ sq.m}$) built-up area is permitted inside side or rear margins. Similarly, under Note (iii), individual shops and row houses on plots up to $100\text{ sq.m}$ need not provide off-street parking.
</p>
''',

    'statutory_extract': r"""8.2 OFF STREET PARKING REQUIREMENT
8.2.1 Off-street parking requirement:
Off street parking requirement shall be based on Table No.8-B below and factors mentioned in Table No.8-C of Regulation No.8.2.2 for various cities / areas. Total parking requirement for a building shall be worked out as per Table No.8-B, and then factor mentioned in Table No.8-C shall be applied to arrive at required parking for a building.

Table No.8-B - Parking Requirements:
1. Residential:
i) Multi-Family residential:
- For every tenement having carpet area of 150 sq.m. and above: Congested: 2 Car, 1 Scooter | Non Congested: 2 Car, 1 Scooter | In addition 5% visitor parking
- For every tenement having carpet area equal to or above 80 sq.m. but less than 150 sq.m.: Congested: 1 Car, 1 Scooter | Non Congested: 1 Car, 1 Scooter | In addition 5% visitor parking
- For every two tenements with each tenement having carpet area equal to or above 40 sq.m. but less than 80 sq.m.: Congested: 1 Car, 2 Scooter | Non Congested: 1 Car, 2 Scooter | In addition 5% visitor parking
- For every two tenements with each tenement having carpet area less than 40 sq.m. but more than 30 sq.m.: Congested: 1 Car, 1 Scooter | Non Congested: 1 Car, 2 Scooter | In addition 5% visitor parking
- For every two tenements with each tenement having carpet area less than 30 sq.m.: Congested: 0 Car, 2 Scooter | Non Congested: 0 Car, 2 Scooter | In addition 5% visitor parking

ii) Lodging establishments, tourist homes, hotels: For every 5 guest rooms: Congested: 1 Car, 4 Scooter | Non Congested: 1 Car, 6 Scooter
iii) Restaurants: For every 50 sq.m. carpet area: Congested: 0 Car, 8 Scooter | Non Congested: 1 Car, 8 Scooter

2. Institutional (Hospitals, Medical Institutions): For every 10 beds: Congested: 2 Car, 12 Scooter | Non Congested: 3 Car, 10 Scooter | For hospital (special building), space for 1 ambulance per hospital, shall be provided.
3. Assembly (theatres, concert halls, auditoria): For every 40 seats: 4 Car, 16 Scooter | Multiplexes: For every 40 seats: 5 Car, 14 Scooter | Mangal karyalaya / Marriage Halls: For every 100 sq.m. carpet / lawn: 1 Car, 5 Scooter
4. Educational: Schools admin/public area: per 100 sq.m: Congested: 1 Car, 4 Scooter | Non Congested: 2 Car, 4 Scooter. Classrooms: 5 two wheelers for every 3 class rooms. College admin: per 100 sq.m: 1/2 Car, 12/17 Scooter. Classrooms: per 3 classrooms: 1/2 Car, 24 Scooter. Coaching: per 20 students: 1 Car, 9 Scooter.
5. Govt / Business / Private Business: For every 100 sq.m. carpet area: Congested: 1 Car, 12 Scooter | Non Congested: 2 Car, 12 Scooter | In addition 20% visitor parking
6. Mercantile (markets, shops, commercials): For every 100 sq.m. carpet area: Congested: 1 Car, 6 Scooter | Non Congested: 2 Car, 6 Scooter
Office and I.T. building: For every 200 sq.m. carpet area: 3 Car, 11 Scooter
7. Industrial: For every 300 sq.m. carpet area: Congested: 2 Car, 9 Scooter | Non Congested: 3 Car, 9 Scooter
8. Storage: For every 300 sq.m. carpet area: Congested: 0 Car, 4 Scooter | Non Congested: 1 Car, 3 Scooter
9. Data centre: Per 400 sq.m.: 1 Car, 0 Scooter

Note:
ii) In case of independent single family residential bungalows having plot area upto 300 sq.m., parking space need not be insisted separately. Further a garage shall be allowed in rear or side marginal distance at one corner having minimum dimensions of 2.5 m. x 5.0 m. and maximum dimensions 3.0 m. x 6.0 m. i.e. minimum 12.5 sq.m. and maximum 18.0 sq.m. built up area.
iii) In the case of shops, row houses on plots upto 100 sq.m., parking space need not be insisted.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Residential Tenement Scale</h4>
    </div>
    <div class="card-body">
      <p>Residential parking is calibrated to individual flat carpet area. Tenements $\ge 150\text{ sq.m}$ get <strong>2 cars + 1 scooter</strong> each. Units between $80-150\text{ sq.m}$ get <strong>1 car + 1 scooter</strong>. For units below $80\text{ sq.m}$, quotas are calculated for <strong>pairs of tenements</strong> (e.g., 1 car + 2 scooters per 2 units for $40-80\text{ sq.m}$).</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>5% &amp; 20% Visitor Parking</h4>
    </div>
    <div class="card-body">
      <p>Every multi-family residential building must add an extra <strong>5% visitor parking</strong> above the total car and scooter count. Government, semi-public, and private corporate business offices must provide a higher <strong>20% visitor parking overlay</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Commercial, IT &amp; Data Centers</h4>
    </div>
    <div class="card-body">
      <p>Mercantile retail requires <strong>2 cars + 6 scooters per 100 sq.m</strong> carpet (non-congested). Corporate offices &amp; IT complexes require <strong>3 cars + 11 scooters per 200 sq.m</strong> carpet. Dedicated Data Centers (added Jan 2024) require only <strong>1 car per 400 sq.m</strong> with zero mandatory two-wheelers.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Bungalow &amp; Small Shop Relief</h4>
    </div>
    <div class="card-body">
      <p>Independent bungalows on plots $\le 300\text{ sq.m}$ do not require standard parking aisle scrutiny; a corner garage ($12.50\text{ m}^2$ to $18.00\text{ m}^2$) is permitted in marginal distances. Individual retail shops and row houses on plots $\le 100\text{ sq.m}$ are completely exempt from parking requirements.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th rowspan="2">Occupancy Class</th>
        <th rowspan="2">Unit / Area Metric</th>
        <th colspan="2">Congested Area</th>
        <th colspan="2">Non-Congested Area</th>
        <th rowspan="2">Visitor / Special Mandate</th>
      </tr>
      <tr>
        <th>Car</th>
        <th>Scooter</th>
        <th>Car</th>
        <th>Scooter</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Res: Luxury ($\ge 150\text{ sq.m}$)</strong></td>
        <td>Per tenement</td>
        <td><code>2</code></td>
        <td><code>1</code></td>
        <td><code>2</code></td>
        <td><code>1</code></td>
        <td>+5% visitor parking</td>
      </tr>
      <tr>
        <td><strong>Res: Standard ($80 - 150\text{ sq.m}$)</strong></td>
        <td>Per tenement</td>
        <td><code>1</code></td>
        <td><code>1</code></td>
        <td><code>1</code></td>
        <td><code>1</code></td>
        <td>+5% visitor parking</td>
      </tr>
      <tr>
        <td><strong>Res: Mid-segment ($40 - 80\text{ sq.m}$)</strong></td>
        <td>Per 2 tenements</td>
        <td><code>1</code></td>
        <td><code>2</code></td>
        <td><code>1</code></td>
        <td><code>2</code></td>
        <td>+5% visitor parking</td>
      </tr>
      <tr>
        <td><strong>Res: Compact ($30 - 40\text{ sq.m}$)</strong></td>
        <td>Per 2 tenements</td>
        <td><code>1</code></td>
        <td><code>1</code></td>
        <td><code>1</code></td>
        <td><code>2</code></td>
        <td>+5% visitor parking</td>
      </tr>
      <tr>
        <td><strong>Res: Affordable ($< 30\text{ sq.m}$)</strong></td>
        <td>Per 2 tenements</td>
        <td><code>0</code></td>
        <td><code>2</code></td>
        <td><code>0</code></td>
        <td><code>2</code></td>
        <td>+5% visitor parking</td>
      </tr>
      <tr>
        <td><strong>Hospitals / Medical</strong></td>
        <td>Per 10 beds</td>
        <td><code>2</code></td>
        <td><code>12</code></td>
        <td><code>3</code></td>
        <td><code>10</code></td>
        <td>+1 Ambulance space / hospital</td>
      </tr>
      <tr>
        <td><strong>Theatres / Auditoriums</strong></td>
        <td>Per 40 seats</td>
        <td><code>4</code></td>
        <td><code>16</code></td>
        <td><code>4</code></td>
        <td><code>16</code></td>
        <td>Multiplex: 5 cars per 40 seats</td>
      </tr>
      <tr>
        <td><strong>Offices &amp; IT Parks</strong></td>
        <td>Per 200 sq.m carpet</td>
        <td><code>3</code></td>
        <td><code>11</code></td>
        <td><code>3</code></td>
        <td><code>11</code></td>
        <td>High-density corporate ratio</td>
      </tr>
      <tr>
        <td><strong>Mercantile / Retail Shops</strong></td>
        <td>Per 100 sq.m carpet</td>
        <td><code>1</code></td>
        <td><code>6</code></td>
        <td><code>2</code></td>
        <td><code>6</code></td>
        <td>Wholesale: 1 car / 100 sq.m</td>
      </tr>
      <tr>
        <td><strong>Data Centers (Jan 2024)</strong></td>
        <td>Per 400 sq.m carpet</td>
        <td><code>1</code></td>
        <td><code>0</code></td>
        <td><code>1</code></td>
        <td><code>0</code></td>
        <td>Automated server floor quota</td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL STATUTORY CALCULATION: MIXED RESIDENTIAL &amp; RETAIL SCHEME</h4>
  <p><strong>Project Profile:</strong> A proposed mixed-use tower in a non-congested sector comprising:</p>
  <ul>
    <li>$20$ Three-BHK flats of $160\text{ sq.m}$ carpet each.</li>
    <li>$40$ Two-BHK flats of $95\text{ sq.m}$ carpet each.</li>
    <li>$60$ One-BHK flats of $55\text{ sq.m}$ carpet each.</li>
    <li>$1,200\text{ sq.m}$ carpet of ground-floor retail shops.</li>
  </ul>
  
  <div class="step-box">
    <strong>Step 1: Residential Parking Calculation (Table 8-B)</strong>
    <ul>
      <li>$160\text{ sq.m}$ units ($20$ flats): $20 \times 2\text{ cars} = \mathbf{40\text{ cars}}$; $20 \times 1\text{ scooter} = \mathbf{20\text{ scooters}}$.</li>
      <li>$95\text{ sq.m}$ units ($40$ flats): $40 \times 1\text{ car} = \mathbf{40\text{ cars}}$; $40 \times 1\text{ scooter} = \mathbf{40\text{ scooters}}$.</li>
      <li>$55\text{ sq.m}$ units ($60$ flats, Tier 3): $\frac{60}{2} \times 1\text{ car} = \mathbf{30\text{ cars}}$; $\frac{60}{2} \times 2\text{ scooters} = \mathbf{60\text{ scooters}}$.</li>
      <li><strong>Subtotal Residential (Tenants):</strong> $40 + 40 + 30 = \mathbf{110\text{ Cars}}$, and $20 + 40 + 60 = \mathbf{120\text{ Scooters}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Add 5% Mandatory Residential Visitor Parking</strong>
    <ul>
      <li>Visitor Cars: $110 \times 0.05 = 5.5 \rightarrow \mathbf{6\text{ visitor cars}}$.</li>
      <li>Visitor Scooters: $120 \times 0.05 = 6.0 \rightarrow \mathbf{6\text{ visitor scooters}}$.</li>
      <li><strong>Total Residential Requirement:</strong> $110 + 6 = \mathbf{116\text{ Cars}}$ and $120 + 6 = \mathbf{126\text{ Scooters}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Retail Mercantile Calculation</strong>
    <ul>
      <li>$1,200\text{ sq.m}$ carpet @ 2 cars &amp; 6 scooters per 100 sq.m (non-congested):</li>
      <li>Retail Cars: $\frac{1,200}{100} \times 2 = \mathbf{24\text{ cars}}$.</li>
      <li>Retail Scooters: $\frac{1,200}{100} \times 6 = \mathbf{72\text{ scooters}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 4: Total Baseline Building Quota (Before Table 8-C City Multiplier)</strong>
    <ul>
      <li><strong>Total Base Cars:</strong> $116 + 24 = \mathbf{140\text{ Cars}}$.</li>
      <li><strong>Total Base Scooters:</strong> $126 + 72 = \mathbf{198\text{ Scooters}}$.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': '''
<div class="alert-box alert-warning">
  <h4>COMMON TABLE 8-B COMPLIANCE TRAPS</h4>
  <ul class="warning-list">
    <li><strong>Forgetting the 5% Visitor Parking:</strong> Calculating pure flat-by-flat car numbers without adding the mandatory 5% visitor parking buffer will cause scrutiny rejection in all planning authorities.</li>
    <li><strong>Miscalculating the 2-Tenement Bracket:</strong> For flats under 80 sq.m, the quota is per <em>two tenements</em>. If you have an odd number (e.g., 25 flats of 65 sq.m), $\frac{25}{2} = 12.5$, which rounds up to 13 cars under Note (i).</li>
    <li><strong>Omitting Hospital Ambulance Bay:</strong> Institutional hospitals require 1 ambulance stall per hospital (measuring $3.75\text{ m} \times 7.50\text{ m}$) in addition to the bed-based car and scooter stalls.</li>
    <li><strong>Over-parking Small Data Centers:</strong> Using standard IT building norms ($3\text{ cars} / 200\text{ m}^2$) for server farms instead of the January 2024 Data Center provision ($1\text{ car} / 400\text{ m}^2$, $0$ scooters) results in massive over-design and wasted capital expenditure.</li>
  </ul>
</div>
''',

    'amendment_section_html': '''
<div class="amendment-card">
  <h4>Statutory Notifications &amp; Sectoral Clarifications</h4>
  <p><strong>Notification No. CR 236/18 (Part 4) dt. 28-12-2022:</strong></p>
  <p>Rationalized two-wheeler norms for educational institutions (prescribing 5 two-wheelers for every 3 classrooms and linking mini-bus provisions to student capacity) and clarified residential two-wheeler baselines across congested and non-congested zones.</p>
  <p><strong>Notification No. CR 97/2023/UD-13 dt. 12-01-2024:</strong></p>
  <p>Inserted Item 9 for dedicated Data Centers ($1\text{ car} / 400\text{ sq.m}$, $0$ scooters) reflecting the low human-density profile of automated cloud and AI server farms.</p>
</div>
''',

    'quiz': [
      {
        'question': 'For a residential flat having a carpet area of 165 sq.m in a non-congested area, what is the mandatory baseline parking quota under Table 8-B?',
        'options': [
          '1 Car and 1 Scooter',
          '2 Cars and 1 Scooter (plus 5% visitor parking)',
          '2 Cars and 2 Scooters',
          '3 Cars and 2 Scooters'
        ],
        'answer': 1,
        'explanation': 'Table 8-B Item 1(i) prescribes: "For every tenement having carpet area of 150 sq.m. and above: 2 Car, 1 Scooter. In addition 5% visitor parking."'
      },
      {
        'question': 'Under Table 8-B Item 9 (inserted Jan 2024), what is the statutory parking requirement for a Data Center?',
        'options': [
          '3 Cars and 11 Scooters per 200 sq.m',
          '2 Cars and 6 Scooters per 100 sq.m',
          '1 Car and 0 Scooters per 400 sq.m',
          '1 Car and 2 Scooters per 100 sq.m'
        ],
        'answer': 2,
        'explanation': 'Item 9 of Table 8-B (inserted 12th January 2024) mandates 1 Car and 0 Scooters per 400 sq.m of carpet area for Data Centers.'
      },
      {
        'question': 'What visitor parking percentage is mandatory for government, semi-public, or private corporate business office buildings under Table 8-B Item 5?',
        'options': [
          '5 percent',
          '10 percent',
          '15 percent',
          '20 percent'
        ],
        'answer': 3,
        'explanation': 'Table 8-B Item 5 specifies: "In addition 20% visitor parking" for Government or semi public or private business buildings.'
      },
      {
        'question': 'Under Note (ii) of Regulation 8.2.1, what are the permissible dimensions of a marginal garage on a single-family bungalow plot up to 300 sq.m?',
        'options': [
          'Minimum 2.0 m x 4.0 m, Maximum 2.5 m x 5.0 m',
          'Minimum 2.5 m x 5.0 m (12.5 sq.m) and Maximum 3.0 m x 6.0 m (18.0 sq.m)',
          'Strictly 3.75 m x 7.5 m',
          'Garages are prohibited in marginal open distances'
        ],
        'answer': 1,
        'explanation': 'Note (ii) provides that "a garage shall be allowed in rear or side marginal distance at one corner having minimum dimensions of 2.5 m. x 5.0 m. and maximum dimensions 3.0 m. x 6.0 m. i.e. minimum 12.5 sq.m. and maximum 18.0 sq.m. built up area."'
      }
    ],

    'prev_url': '/lessons/reg-8-1-8-loading-spaces-ramps-and-marginal-parking.html',
    'prev_title': 'Reg 8.1.1(vi)-(viii): Loading Berths, Basement Ramps & Marginal Parking',
    'next_url': '/lessons/reg-8-2-2-city-multipliers-and-parking-penalties.html',
    'next_title': 'Reg 8.2.2 & Table 8-C: City Multipliers, 2-Wheeler Exemption & Surcharges'
}
