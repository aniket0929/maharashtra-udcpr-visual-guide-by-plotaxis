"""
UDCPR FROM SCRATCH - CHAPTER 11, LESSON 2
Regulation 11.2.1 to 11.2.5: TDR Generation, Surrender Multipliers & Construction Amenity Formula
File: scripts/ch11_lessons/lesson_11_2_tdr_generation_amenities.py
"""

lesson_data = {
    'filename': 'reg-11-2-tdr-generation-and-amenity-construction.html',
    'lesson_id': 'reg-11-2-tdr-generation-and-amenity-construction',
    'quiz_id': 'quiz-11-2',
    'clause': 'Reg. 11.2.1 to 11.2.5',
    'title': 'TDR Generation, Surrender Multipliers & Construction Amenity Formula',
    'badge_status': 'STATUTORY • TDR GENERATION',
    'ch_slug': 'ch11',
    'ch_title': 'Chapter 11: Acquisition of Reserved Sites & TDR',
    'meta_desc': 'Master UDCPR Regulations 11.2.1 to 11.2.5 for Transferable Development Rights (TDR) Generation: DRC issuance, 2x non-congested and 3x congested multipliers, 1.85/2.85 compound wall factors, 8% BDP, and the Construction Amenity TDR formula: A/B * 1.35.',
    
    'lead_summary': (
        'Transferable Development Rights (TDR) serve as Maharashtra’s statutory virtual currency for urban infrastructure acquisition. '
        'Regulations 11.2.1 through 11.2.5 establish the rigorous rules governing how a Development Rights Certificate (DRC) is born. '
        'When land under a Development Plan reservation or road widening is surrendered free of cost and encumbrances, the owner receives '
        'a DRC computed at statutory multipliers: 2.00 times the land area in non-congested zones, and 3.00 times in congested zones '
        '(reduced to 1.85 and 2.85 if the mandatory 1.5 m compound wall is omitted, though DP roads receive full credit without compound walls). '
        'Furthermore, when an owner constructs the public amenity or DP road at their own expense, Regulation 11.2.5 awards Construction Amenity '
        'TDR using the formula (A / B) * 1.35, factoring comprehensive PWD DSR rates against the local ASR land value.'
    ),
    
    'amendment_cite': 'Notification u/s 37(1AA)(c) No. CR 96/2024/UD-13 dt. 05-09-2024 (1.35 multiplier & comprehensive DSR cost)',
    
    'plain_summary_html': r'''
<p>
  TDR generation separates the right to build from the physical parcel of land. Rather than accepting slow, discounted cash compensation under eminent domain, landowners surrender their land to the Municipal Corporation and receive tradable <strong>Development Rights Certificates (DRC)</strong>:
</p>
<ul class="rule-list">
  <li><strong>Development Rights Certificate (DRC) Mechanics (Reg 11.2.1):</strong>
    <ul>
      <li>Issued directly under the signature of the Municipal Commissioner or Chief Officer.</li>
      <li>Endorses in words and figures: (1) FSI credit in square meters, (2) the geographic origin/plot of generation, and (3) the official <strong>Annual Statement of Rates (ASR) land rate</strong> for the generating plot in the year of generation.</li>
      <li>TDR generated within an authority's jurisdiction must be utilized within the same municipal territory.</li>
    </ul>
  </li>
  <li><strong>Statutory Land Surrender Multipliers (Reg 11.2.4):</strong>
    <ul>
      <li><strong>Non-Congested Area:</strong> <strong>2.00 times (2x)</strong> the area of surrendered land.</li>
      <li><strong>Congested Area:</strong> <strong>3.00 times (3x)</strong> the area of surrendered land.</li>
      <li><strong>Compound Wall Factor (Clause b):</strong> Surrendered land must be leveled and secured with a <strong>1.50 m high compound wall</strong> (0.60 m brick/stone plinth + upper fencing and gate). If omitted, the generation multiplier drops to <strong>1.85</strong> (non-congested) or <strong>2.85</strong> (congested), unless the owner pays the cash cost of the wall.</li>
      <li><strong>DP Roads Exemption:</strong> Land surrendered for Development Plan roads is <strong>exempt from compound walls</strong> and receives the full 2.00x / 3.00x multiplier with zero reduction!</li>
      <li><strong>Special Ecological/Legal Zones:</strong> Bio-Diversity Park (BDP) reservations generate <strong>8% of gross area (0.08 FSI)</strong>. Lands under legal impediments (CRZ, Hazardous, Low Density) generate <strong>50% of standard TDR</strong>.</li>
      <li><strong>Long-Term Government Leases:</strong> Government land leased for > 30 years remaining earns <strong>90% of private land TDR</strong>.</li>
    </ul>
  </li>
  <li><strong>Construction Amenity TDR Formula (Reg 11.2.5):</strong> When the landowner voluntarily builds the public facility (or new DP road) at their own cost and delivers it to the public:
    $$\text{Construction Amenity TDR (sq.m)} = \left(\frac{A}{B}\right) \times 1.35$$
    <ul>
      <li><strong>A = Comprehensive Cost of Construction (Rs.):</strong> Calculated per PWD District Schedule of Rates (DSR) for the year construction commences, encompassing civil, electrical, plumbing, site leveling, ramps, parking, municipal fees, and labor cess (movables excluded).</li>
      <li><strong>B = Land Rate (Rs./sq.m):</strong> Official ASR land rate per square meter for the year construction commences.</li>
      <li><strong>1.35 = Statutory Incentive Factor:</strong> Upgraded from earlier 1.00 / 1.25 benchmarks via the landmark September 2024 gazette notification!</li>
    </ul>
  </li>
</ul>
''',

    'statutory_extract': r"""11.2 REGULATIONS FOR GRANT OF TRANSFERABLE DEVELOPMENT RIGHTS
11.2.1 Transferable Development Rights:
Transferable Development Rights (TDR) is compensation in the form of Floor Space Index (FSI) or Development Rights which shall entitle the owner for construction of built-up area... This FSI credit shall be issued in a certificate which shall be called as Development Right Certificate (DRC).

11.2.4 Generation of the Transferable Development Rights (TDR):
a. For surrender of the gross area of the land which is subjected to acquisition, free of cost and free from all encumbrances, the owner shall be entitled for TDR or DR:
- Non-Congested Area: 2 times the area of surrendered land.
- Congested Area: 3 times the area of surrendered land.
Note:
i) The quantum of TDR generated for reservation in area having total legal impediment / constraint... like CRZ / Hazardous / Low Density zone, shall be 50% of TDR generated as prescribed above.
ii) The quantum of TDR generated for Bio Diversity Park reservation shall be 8% of gross area.
Provided that, if levelling of land and construction/erection of compound wall... is not desirable... quantum of TDR shall be reduced to 1 : 1.85 and 1 : 2.85 in non congested area and congested area respectively...
Provided further that such construction / erection of compound wall / fencing shall not be necessary for area under development plan roads. In such cases TDR equivalent to entitlement as mentioned above shall be granted without any reduction.

11.2.5 Transferable Development Rights (TDR) against Construction of Amenity:
Construction Amenity TDR in Sq.m. = A / B * 1.35
Where,
A = cost of construction of amenity in rupees for all type of buildings and roads, should be calculated as per DSR prepared by PWD for the year in which construction of amenity is commenced...
B = land rate per Sq.m. as per ASR prepared by IGR for the year in which construction of amenity is commenced.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Land Multipliers (2x &amp; 3x) (Reg 11.2.4)</h4>
    </div>
    <div class="card-body">
      <p>Surrender of unencumbered DP land yields <strong>2.00 times</strong> the land area in non-congested zones, and <strong>3.00 times</strong> in congested urban cores, establishing double and triple value compensation.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Compound Wall Factor (1.85 / 2.85)</h4>
    </div>
    <div class="card-body">
      <p>Omitting the mandatory 1.5m perimeter compound wall drops the credit to <strong>1.85x</strong> (non-congested) and <strong>2.85x</strong> (congested). However, <strong>DP roads receive 100% full credit without compound walls</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Construction Amenity Formula (Reg 11.2.5)</h4>
    </div>
    <div class="card-body">
      <p>Constructing the public building or road generates bonus TDR: <strong>Construction TDR = (A / B) &times; 1.35</strong>, indexing comprehensive PWD DSR expenditure against the base ASR land value.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Bio-Diversity &amp; Legal Buffers</h4>
    </div>
    <div class="card-body">
      <p>Bio-Diversity Park (BDP) reservations generate <strong>8% of gross area (0.08 FSI)</strong>. Legal constraint belts (CRZ, chemical hazards, low density) generate <strong>50% of standard TDR</strong>.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="drawing-sheet-plate">
  <div class="plate-header">
    <span class="plate-num">PLATE 11.2-A: TDR GENERATION MULTIPLIERS &amp; FORMULA METRICS</span>
    <span class="plate-scale">STATUTORY MULTIPLIERS &bull; REGULATION 11.2</span>
  </div>
  
  <div class="table-responsive">
    <table class="data-table">
      <thead>
        <tr>
          <th>Category of Land Surrendered</th>
          <th>Physical Boundary Condition</th>
          <th>TDR Generation Multiplier</th>
          <th>Statutory Remarks &amp; Conditions</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Non-Congested DP Land</strong></td>
          <td>With 1.5 m compound wall &amp; leveled</td>
          <td><strong>2.00 &times; Land Area</strong></td>
          <td>Standard land surrender benchmark</td>
        </tr>
        <tr>
          <td><strong>Non-Congested DP Land</strong></td>
          <td>Without compound wall</td>
          <td><strong>1.85 &times; Land Area</strong></td>
          <td>Owner has option to pay wall cost instead</td>
        </tr>
        <tr>
          <td><strong>Congested Area DP Land</strong></td>
          <td>With 1.5 m compound wall &amp; leveled</td>
          <td><strong>3.00 &times; Land Area</strong></td>
          <td>Triple credit for core city acquisitions</td>
        </tr>
        <tr>
          <td><strong>Congested Area DP Land</strong></td>
          <td>Without compound wall</td>
          <td><strong>2.85 &times; Land Area</strong></td>
          <td>Owner has option to pay wall cost instead</td>
        </tr>
        <tr>
          <td><strong>DP Road / Road Widening</strong></td>
          <td>Open road corridor</td>
          <td><strong>2.00&times; / 3.00&times; Full Credit</strong></td>
          <td><strong>Exempt from compound wall requirement</strong></td>
        </tr>
        <tr>
          <td><strong>Bio-Diversity Park (BDP)</strong></td>
          <td>Hilltop / Green corridor</td>
          <td><strong>0.08 &times; Gross Area (8%)</strong></td>
          <td>Strict environmental conservation ceiling</td>
        </tr>
        <tr>
          <td><strong>CRZ / Hazardous / Low-Density</strong></td>
          <td>Legal restriction zones</td>
          <td><strong>50% of Standard Multiplier</strong></td>
          <td>1.00x non-congested / 1.50x congested</td>
        </tr>
        <tr>
          <td><strong>Amenity Construction TDR</strong></td>
          <td>Turn-key finished public amenity</td>
          <td><strong>(A / B) &times; 1.35</strong></td>
          <td>A = PWD DSR cost, B = ASR land rate</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL SCRUTINY CALCULATION: LAND TDR &amp; AMENITY CONSTRUCTION TDR</h4>
  <p><strong>Scenario: DP School Reservation Surrender &amp; Construction in Thane</strong></p>
  <p>A landowner in Thane (non-congested area) owns a <strong>5,000 sq.m land parcel</strong> reserved for a "Primary School". The local ASR land rate is <strong>Rs. 25,000 per sq.m</strong>. The owner levels the land, constructs a 1.5 m compound wall, and with municipal sanction, constructs a 2-storey school building having a comprehensive PWD DSR cost of <strong>Rs. 6,75,00,000 (Rs. 6.75 Crores)</strong>. How much Land TDR and Construction Amenity TDR are generated?</p>
  
  <div class="step-box">
    <strong>Step 1: Calculate Land Surrender TDR (Reg 11.2.4)</strong>
    <ul>
      <li>Surrendered Land Area = $5,000\text{ sq.m}$ (Non-congested).</li>
      <li>Compound wall constructed: Yes (1.5 m wall provided).</li>
      <li>Statutory Multiplier = <strong>2.00</strong>.</li>
      <li>$\text{Land TDR} = 5,000\text{ sq.m} \times 2.00 = \mathbf{10,000\text{ sq.m of FSI Credit}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Calculate Construction Amenity TDR (Reg 11.2.5)</strong>
    <ul>
      <li>$A$ = PWD DSR Cost of Construction = $\text{Rs. 6,75,00,000}$.</li>
      <li>$B$ = ASR Land Rate = $\text{Rs. 25,000 / sq.m}$.</li>
      <li>Statutory Formula: $\text{Construction TDR} = \left(\frac{A}{B}\right) \times 1.35$.</li>
      <li>Cost-to-Land Ratio: $\frac{6,75,00,000}{25,000} = 2,700\text{ sq.m}$.</li>
      <li>Apply 1.35 Incentive Multiplier: $2,700 \times 1.35 = \mathbf{3,645\text{ sq.m of FSI Credit}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Total Development Rights Certificate (DRC) Issued</strong>
    <ul>
      <li>$\text{Total DRC Quantum} = 10,000\text{ sq.m (Land)} + 3,645\text{ sq.m (Construction)} = \mathbf{13,645\text{ sq.m}}$.</li>
      <li>The Municipal Commissioner issues a DRC for <strong>13,645 sq.m</strong>, endorsing the generating ASR rate of <strong>Rs. 25,000 / sq.m</strong>.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>COMMON SANCTION &amp; SCRUTINY PITFALLS IN TDR GENERATION</h4>
  <ul class="warning-list">
    <li><strong>Demanding Compound Walls on DP Roads:</strong> Scrutiny officers cutting road widening TDR from 2.0x down to 1.85x because no compound wall was built along the road. Reg 11.2.4 Proviso explicitly clarifies: <em>"construction / erection of compound wall / fencing shall not be necessary for area under development plan roads. In such cases TDR equivalent to entitlement... shall be granted without any reduction."</em></li>
    <li><strong>Using Outdated 1.00 / 1.25 Multipliers for Amenity TDR:</strong> Calculating Construction Amenity TDR without the 1.35 multiplier. The September 2024 statutory gazette notification substituted the multiplier with <strong>1.35</strong>.</li>
    <li><strong>Including Movable Furniture in Amenity Cost:</strong> Project proponents including benches, projectors, and desks in school estimates. Reg 11.2.5(ii) strictly bars movable items from the PWD DSR calculation.</li>
    <li><strong>Claiming Land TDR for Internal Layout Roads:</strong> Applying for TDR on internal 9m layout roads or 10% recreational open spaces. Under Reg 11.2.3, sub-divided layout roads and mandatory layout open spaces are strictly <strong>ineligible for TDR</strong>.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; Clarifications for TDR Generation</h4>
  <p><strong>Notification u/s 37(1AA)(c) No. CR 96/2024/UD-13 dt. 05-09-2024 &amp; Corrigendum dt. 11-10-2024:</strong></p>
  <p>Standardized the Construction Amenity TDR multiplier at <strong>1.35</strong> across all authorities and explicitly directed that PWD DSR estimates must comprehensively include civil, electrical, plumbing, site leveling, ramps, parking, environmental infrastructure, and municipal consultant/BOCW charges.</p>
</div>
''',

    'quiz': [
      {
        'question': 'What is the standard TDR generation multiplier for surrendering unencumbered reserved land in a non-congested area with compound wall (Reg 11.2.4)?',
        'options': ['1.00 times', '1.50 times', '2.00 times', '3.00 times'],
        'answer': 2,
        'explanation': 'Under Regulation 11.2.4(a), the owner is entitled to 2 times the area of surrendered land in non-congested areas.'
      },
      {
        'question': 'If a landowner in a congested area surrenders DP land without erecting a 1.5m compound wall, what is the reduced TDR multiplier?',
        'options': ['2.00 times', '2.50 times', '2.85 times', '3.00 times'],
        'answer': 2,
        'explanation': 'Under Regulation 11.2.4 Proviso, if compound wall is not erected, the multiplier reduces from 3.00 to 2.85 in congested areas (and from 2.00 to 1.85 in non-congested areas).'
      },
      {
        'question': 'Are compound walls required for land surrendered under Development Plan roads to receive full TDR?',
        'options': [
          'Yes, compound wall is compulsory on both sides',
          'No, DP road land is statutorily exempt and receives full TDR without reduction',
          'Only if the road is wider than 24 meters',
          'Only in congested areas'
        ],
        'answer': 1,
        'explanation': 'Regulation 11.2.4 Proviso explicitly provides that compound wall / fencing is not necessary for area under development plan roads, and full TDR is granted without reduction.'
      },
      {
        'question': 'What is the statutory incentive multiplier in the Construction Amenity TDR formula under the September 2024 notification (Reg 11.2.5)?',
        'options': ['1.00', '1.20', '1.25', '1.35'],
        'answer': 3,
        'explanation': 'Under Regulation 11.2.5 as amended on 05-09-2024, Construction Amenity TDR = (A / B) * 1.35.'
      }
    ],

    'prev_url': '/lessons/reg-11-1-manner-of-development-and-accommodation-reservation.html',
    'prev_title': 'Reg 11.1 & Table 11-A: Accommodation Reservation Principle & Land-Sharing',
    'next_url': '/lessons/reg-11-2-6-tdr-utilisation-indexation-and-restrictions.html',
    'next_title': 'Reg 11.2.6 to 11.2.13: TDR Utilisation, ASR Indexation & Receiving Caps'
}
