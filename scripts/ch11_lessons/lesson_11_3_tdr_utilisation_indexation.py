"""
UDCPR FROM SCRATCH - CHAPTER 10 / 11, LESSON 3
Regulation 11.2.6 to 11.2.13: TDR Utilisation, ASR Indexation Formula & Receiving Caps
File: scripts/ch11_lessons/lesson_11_3_tdr_utilisation_indexation.py
"""

lesson_data = {
    'filename': 'reg-11-2-6-tdr-utilisation-indexation-and-restrictions.html',
    'lesson_id': 'reg-11-2-6-tdr-utilisation-indexation-and-restrictions',
    'quiz_id': 'quiz-11-3',
    'clause': 'Reg. 11.2.6 to 11.2.13',
    'title': 'TDR Utilisation, ASR Indexation Formula & Receiving Caps',
    'badge_status': 'STATUTORY • TDR UTILISATION',
    'ch_slug': 'ch11',
    'ch_title': 'Chapter 11: Acquisition of Reserved Sites & TDR',
    'meta_desc': 'Master UDCPR Regulations 11.2.6 to 11.2.13 for TDR Utilisation: the universal ASR ratio formula X = (Rg / Rr) * Y, receiving road width caps under Table 6-A & 6-G, zero infrastructure charges (Reg 11.2.11), restricted zones (NDZ, CRZ, Heritage-I), and DRC transfer ledgers.',
    
    'lead_summary': (
        'Transferable Development Rights are not consumed at face value across disparate urban zones; they are indexed to prevent economic windfalls '
        'and infrastructure strain. Regulation 11.2.6 codifies the foundational ASR Indexation Formula: X = (Rg / Rr) * Y, normalizing the value of '
        'TDR debited from a DRC by comparing the Annual Statement of Rates (ASR) of the generating site against the receiving site for the year of generation. '
        'This lesson covers how indexed TDR is stacked within the maximum building potential caps of Table 6-A and Table 6-G, explores the statutory '
        'guarantee that no municipal infrastructure improvement charges can be levied on TDR (Reg 11.2.11), maps the geographic zones legally barred '
        'from receiving TDR (NDZ, CRZ-I, Grade-I Heritage), and details the official transfer ledger protocol for trading DRC certificates.'
    ),
    
    'amendment_cite': 'Directives u/s 154 No. CR 07/2023 dt. 27-02-2023 & Corrigendum No. CR 121/21 dt. 02-12-2021',
    
    'plain_summary_html': r'''
<p>
  When an architect or developer purchases TDR on the open market, 1,000 sq.m of TDR generated in an outer fringe village cannot simply be loaded as 1,000 sq.m of luxury high-rise construction in a prime city center. <strong>Regulation 11.2.6 establishes mathematical equilibrium through ASR indexation</strong>:
</p>
<ul class="rule-list">
  <li><strong>The Universal ASR Ratio Indexation Formula (Reg 11.2.6):</strong>
    $$X = \left(\frac{R_g}{R_r}\right) \times Y$$
    <ul>
      <li><strong>X:</strong> Permissible quantum of TDR / built-up area in square meters permitted on the <em>receiving plot</em>.</li>
      <li><strong>Rg:</strong> Land rate (Rs./sq.m) as per the Annual Statement of Rates (ASR) of the <em>generating plot</em> in the <strong>generating year</strong>.</li>
      <li><strong>Rr:</strong> Land rate (Rs./sq.m) as per the ASR of the <em>receiving plot</em> in the <strong>generating year</strong>.</li>
      <li><strong>Y:</strong> Quantum of TDR in square meters debited from the Development Rights Certificate (DRC).</li>
      <li><strong>Critical Safeguard:</strong> Both $R_g$ and $R_r$ are pegged to the <em>same historic year of generation</em>, immunizing the transaction against erratic, asymmetrical year-on-year ready reckoner inflation!</li>
    </ul>
  </li>
  <li><strong>Road Width Receiving Limits (Reg 11.2.7):</strong> TDR cannot be dumped onto narrow streets. The maximum quantum of TDR that can be consumed on any receiving plot is strictly capped by the road-width potential brackets established in <strong>Table 6-A (Non-Congested) and Table 6-G (Congested)</strong> of Chapter 6.</li>
  <li><strong>Zero Infrastructure Improvement Charges (Reg 11.2.11):</strong>
    In a major statutory relief for urban developers, Regulation 11.2.11 decrees unequivocally: <em>"No infrastructure improvement charges shall be paid for utilisation of TDR."</em> Planning authorities are legally barred from collecting separate betterment levies on TDR loading.</li>
  <li><strong>Areas Restricted from Receiving TDR (Reg 11.2.8):</strong> Loading of TDR is strictly prohibited in:
    <ul>
      <li>No Development Zones (NDZ), Agricultural Zones, and Green Zones.</li>
      <li>Coastal Regulation Zone (CRZ-I) and areas within the prohibited Blue Flood Line of rivers.</li>
      <li>Grade-I Heritage structures and sensitive precincts (without specific Heritage Committee sanction).</li>
      <li>Congested Gaothan pockets where road access is below 9.0 meters without widening.</li>
    </ul>
  </li>
  <li><strong>DRC Trading &amp; Municipal Transfer Register (Reg 11.2.10):</strong> DRCs are fully negotiable and transferable assets. The Authority maintains a statutory register recording every sale, partial debit, and balance endorsement before issuing building permissions and occupancy certificates.</li>
</ul>
''',

    'statutory_extract': r"""11.2.6 Utilisation of Transferable Development Rights (TDR):
ii) The Transferable Development Rights (TDR) generated from any land use zone shall be utilised on any receiving plot irrespective of the land use zone... anywhere in congested or non-congested area...
The equivalent quantum of Transferable Development Rights (TDR) to be permitted on receiving plot shall be governed by the formula given below :-
Formula: X = (Rg / Rr) x Y
Where,
X = Permissible Utilisation of TDR / DR in sq.m. on receiving plot.
Rg = Rate for land in Rs. per sq.m. as per ASR of generating plots in generating year.
Rr = Rate for land in Rs. per sq.m. as per ASR of receiving plot in generating year.
Y = TDR debited from DRC in sq.m.

11.2.7 Utilisation of Transferable Development Rights (TDR) and Road Width Relation:
The maximum permissible TDR on receiving plot shall be as per Regulation No.6.1, Table 6-A or Regulation No.6.3, Table 6-G, as the case may be.

11.2.8 Areas Restricted from Utilisation of Transferable Development Rights (TDR):
Utilisation of TDR shall not be permitted in following areas :-
i) Agricultural / Green Zone / No Development Zone.
ii) Area under CRZ-I.
iii) In Heritage building / Heritage Precincts... except with approval of Heritage Conservation Committee.
iv) Any area where development is restricted by Government or Authority.

11.2.11 Infrastructure Improvement Charges:
No infrastructure improvement charges shall be paid for utilisation of TDR.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>ASR Ratio Formula: X = (Rg / Rr) &times; Y</h4>
    </div>
    <div class="card-body">
      <p>Normalizes land values: The TDR usable on the receiving plot ($X$) equals the face value TDR ($Y$) multiplied by the ratio of the generating plot's ASR ($R_g$) to the receiving plot's ASR ($R_r$) in the <strong>generating year</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Road-Width Receiving Caps (Reg 11.2.7)</h4>
    </div>
    <div class="card-body">
      <p>TDR consumption cannot exceed the statutory limits of Chapter 6 (Table 6-A and Table 6-G). Road widths below 9.0 m cannot absorb TDR; wider arterial corridors allow progressively higher TDR stacking.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Zero Infrastructure Levies (Reg 11.2.11)</h4>
    </div>
    <div class="card-body">
      <p>Municipalities are explicitly forbidden from charging infrastructure improvement fees on TDR utilization: <em>"No infrastructure improvement charges shall be paid for utilisation of TDR."</em></p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Restricted Zones (Reg 11.2.8)</h4>
    </div>
    <div class="card-body">
      <p>Total legal ban on utilizing TDR in No Development Zones (NDZ), Agricultural belts, Coastal CRZ-I, river blue flood lines, and Grade-I Heritage precincts without committee clearance.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="drawing-sheet-plate">
  <div class="plate-header">
    <span class="plate-num">PLATE 11.3-A: TDR ASR INDEXATION RATIOS &amp; RESTRICTED ZONES</span>
    <span class="plate-scale">MATHEMATICAL BALANCING &bull; REGULATION 11.2.6</span>
  </div>
  
  <div class="table-responsive">
    <table class="data-table">
      <thead>
        <tr>
          <th>Indexation Factor / Area</th>
          <th>Mathematical Variable</th>
          <th>Statutory Definition &amp; Source</th>
          <th>Regulatory Effect on Receiving Plot</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Permissible Receiving TDR</strong></td>
          <td><code>X</code></td>
          <td>Target BUA usable on receiving plot</td>
          <td>Credited directly into building potential</td>
        </tr>
        <tr>
          <td><strong>Generating Plot Land Rate</strong></td>
          <td><code>Rg</code></td>
          <td>ASR rate (Rs./sq.m) of origin plot</td>
          <td>Fixed at the historic <strong>generating year</strong></td>
        </tr>
        <tr>
          <td><strong>Receiving Plot Land Rate</strong></td>
          <td><code>Rr</code></td>
          <td>ASR rate (Rs./sq.m) of destination plot</td>
          <td>Evaluated for the same historic generating year</td>
        </tr>
        <tr>
          <td><strong>Debited DRC Quantum</strong></td>
          <td><code>Y</code></td>
          <td>Face value area deducted from DRC</td>
          <td>Endorsed on physical certificate and ledger</td>
        </tr>
        <tr>
          <td><strong>Infrastructure Improvement Fee</strong></td>
          <td><code>Nil (Rs. 0)</code></td>
          <td>Exempted under Regulation 11.2.11</td>
          <td>No municipal betterment tax on TDR</td>
        </tr>
        <tr>
          <td><strong>Restricted Zones (Banned)</strong></td>
          <td><code>X = 0</code></td>
          <td>NDZ, CRZ-I, Agri, Heritage-I, Floodplains</td>
          <td>Absolute bar on loading TDR certificates</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL ARCHITECTURAL CALCULATION: TDR ASR INDEXATION FROM FRINGE TO PRIME CBD</h4>
  <p><strong>Scenario:</strong> A developer in Pune is constructing a commercial tower on a 2,000 sq.m plot fronting a 24.0 m road on Senapati Bapat Road (Shivajinagar). Under Table 6-G, the permissible TDR component is <strong>1,000 sq.m of built-up area</strong>. The developer purchases a DRC on the market that was generated in 2021 from a DP road widening in Hadapsar. Calculate how much DRC face value ($Y$) must be debited to achieve the required 1,000 sq.m ($X$) on Senapati Bapat Road.</p>
  
  <div class="step-box">
    <strong>Step 1: Retrieve Statutory ASR Land Rates for Generating Year (2021)</strong>
    <ul>
      <li>$R_g$ = ASR rate of generating plot (Hadapsar) in 2021 = <strong>Rs. 20,000 per sq.m</strong>.</li>
      <li>$R_r$ = ASR rate of receiving plot (Senapati Bapat Road) in 2021 = <strong>Rs. 50,000 per sq.m</strong>.</li>
      <li>Target BUA required on receiving plot ($X$) = <strong>1,000 sq.m</strong>.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Apply the Statutory Formula (Reg 11.2.6)</strong>
    $$X = \left(\frac{R_g}{R_r}\right) \times Y \implies Y = X \times \left(\frac{R_r}{R_g}\right)$$
    <ul>
      <li>Price Ratio $\frac{R_r}{R_g} = \frac{50,000}{20,000} = \mathbf{2.50}$.</li>
      <li>Required DRC Face Value ($Y$) = $1,000\text{ sq.m} \times 2.50 = \mathbf{2,500\text{ sq.m}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Verification &amp; Endorsement</strong>
    <ul>
      <li>To construct $1,000\text{ sq.m}$ of prime commercial space on Senapati Bapat Road, the developer must surrender and debit <strong>2,500 sq.m of face value TDR</strong> from the Hadapsar DRC.</li>
      <li>The Municipal Commissioner debits 2,500 sq.m from the DRC and endorses the credit of 1,000 sq.m onto the building approval.</li>
      <li>Under Regulation 11.2.11, Pune Municipal Corporation collects <strong>Rs. 0</strong> as infrastructure improvement charges for this TDR.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>COMMON SANCTION &amp; SCRUTINY PITFALLS IN TDR UTILISATION</h4>
  <ul class="warning-list">
    <li><strong>Mixing Up ASR Rates from Different Years:</strong> Taking the generating plot's ASR rate from 2020 and comparing it to the receiving plot's current 2024 ASR rate. Reg 11.2.6 explicitly requires both $R_g$ and $R_r$ to be taken from the <strong>generating year</strong> of the DRC.</li>
    <li><strong>Levying Infrastructure Charges on TDR:</strong> Municipalities attempting to collect 5% infrastructure or betterment fees on TDR consumption. Reg 11.2.11 explicitly decrees: <em>"No infrastructure improvement charges shall be paid for utilisation of TDR."</em></li>
    <li><strong>Attempting to Load TDR in Agricultural / No Development Zones:</strong> Submitting building plans in green belts or NDZ utilizing TDR. Reg 11.2.8 completely bars TDR in non-urbanized zones.</li>
    <li><strong>Exceeding Table 6-A / 6-G Road Width Caps:</strong> Purchasing excess TDR hoping to build beyond the maximum permissible building potential for the road width. TDR is strictly capped by the road width brackets of Chapter 6.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; Clarifications for TDR Utilisation</h4>
  <p><strong>Government Directives u/s 154 No. CR 07/2023 dt. 27-02-2023:</strong></p>
  <p>Clarified that TDR generated from any zone (residential, commercial, industrial) is universally fungible and can be utilized on any receiving plot irrespective of zoning designations, provided the receiving plot conforms to road-width building potentials and is outside the restricted zones of Reg 11.2.8.</p>
</div>
''',

    'quiz': [
      {
        'question': 'In the TDR indexation formula X = (Rg / Rr) * Y, what does Rg represent (Reg 11.2.6)?',
        'options': [
          'Current land rate of receiving plot',
          'ASR land rate of generating plot in the year of generation',
          'ASR land rate of generating plot in the current year',
          'Cost of construction of the amenity'
        ],
        'answer': 1,
        'explanation': 'Under Regulation 11.2.6, Rg is the rate for land in Rs. per sq.m as per the ASR of the generating plot in the generating year.'
      },
      {
        'question': 'Are both Rg and Rr in the TDR formula evaluated for the same historic generating year or current year?',
        'options': [
          'Both are evaluated for the current year of development permission',
          'Both are evaluated for the historic generating year of the DRC',
          'Rg is generating year and Rr is current year',
          'Rg is current year and Rr is generating year'
        ],
        'answer': 1,
        'explanation': 'Regulation 11.2.6 explicitly defines Rr as the "Rate for land in Rs. per sq.m. as per ASR of receiving plot in generating year" to maintain economic equivalence.'
      },
      {
        'question': 'Under Regulation 11.2.11, what infrastructure improvement charge is payable for utilizing TDR on a receiving plot?',
        'options': [
          '2% of ASR land rate',
          '5% of ASR land rate',
          '10% of ASR land rate',
          'No infrastructure improvement charges shall be paid'
        ],
        'answer': 3,
        'explanation': 'Regulation 11.2.11 explicitly decrees: "No infrastructure improvement charges shall be paid for utilisation of TDR."'
      },
      {
        'question': 'Which of the following areas is strictly RESTRICTED from receiving TDR under Regulation 11.2.8?',
        'options': [
          'Commercial zones along 18m roads',
          'Non-congested residential zones',
          'No Development Zone (NDZ) and CRZ-I',
          'Redevelopment projects in Municipal Corporations'
        ],
        'answer': 2,
        'explanation': 'Under Regulation 11.2.8, TDR utilization is strictly barred in Agricultural/Green/No Development Zones and Coastal CRZ-I areas.'
      }
    ],

    'prev_url': '/lessons/reg-11-2-tdr-generation-and-amenity-construction.html',
    'prev_title': 'Reg 11.2: TDR Generation, Multipliers & Construction Amenity Formula',
    'next_url': '/lessons/reg-11-3-reservation-credit-certificate-and-financial-offsets.html',
    'next_title': 'Reg 11.3: Reservation Credit Certificate (RCC) & Financial Offsets'
}
