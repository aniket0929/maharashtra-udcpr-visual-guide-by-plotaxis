"""
UDCPR FROM SCRATCH - CHAPTER 11, LESSON 1
Regulation 11.1: Accommodation Reservation Principle & DP Land-Sharing (Table 11-A)
File: scripts/ch11_lessons/lesson_11_1_accommodation_reservation.py
"""

lesson_data = {
    'filename': 'reg-11-1-manner-of-development-and-accommodation-reservation.html',
    'lesson_id': 'reg-11-1-manner-of-development-and-accommodation-reservation',
    'quiz_id': 'quiz-11-1',
    'clause': 'Reg. 11.1 & Table 11-A',
    'title': 'Accommodation Reservation Principle & DP Land-Sharing (Table 11-A)',
    'badge_status': 'STATUTORY • TABLE 11-A',
    'ch_slug': 'ch11',
    'ch_title': 'Chapter 11: Acquisition of Reserved Sites & TDR',
    'meta_desc': 'Master UDCPR Regulation 11.1 and Table 11-A Accommodation Reservation: how private owners develop DP reservations (schools, hospitals, public housing, markets), hand over built amenities free to the Authority, and unlock the remaining plot with 100% gross FSI and deemed zoning conversion.',
    
    'lead_summary': (
        'Development Plan reservations for public amenities (schools, dispensaries, gardens, markets, fire stations, and public housing) '
        'have historically been stalled by costly and litigious compulsory land acquisition. Regulation 11.1 introduces the transformative '
        'Accommodation Reservation Principle under Table 11-A: empowering private landowners to develop the designated reservation themselves. '
        'By surrendering an earmarked portion of the land (typically 40% in A/B/C Class Corporations) along with a fully constructed, turn-key '
        'public amenity (typically 50% built-up area), the landowner retains the balance land, achieves 100% full permissible FSI and TDR potential '
        'calculated on the entire gross plot without any utilization cap, and benefits from automatic deemed rezoning of the residual land into '
        'a residential or commercial zone upon grant of the final Occupancy Certificate.'
    ),
    
    'amendment_cite': 'Corrigendum / Addendum No. CR 121/21 dt. 02-12-2021 (Notes vi, xi & Table 11-A composite permissions)',
    
    'plain_summary_html': r'''
<p>
  Under Maharashtra’s planning statutes, when land is designated for a public reservation in a Development Plan, the local authority rarely has the budget to acquire it outright with cash. <strong>Regulation 11.1 solves this deadlock through public-private partnership (Accommodation Reservation)</strong>:
</p>
<ul class="rule-list">
  <li><strong>The Accommodation Reservation Trade-Off:</strong>
    <ul>
      <li>Instead of waiting decades for monetary acquisition, the private landowner enters into a registered tripartite agreement with the Planning Authority.</li>
      <li>The owner physically subdivides the plot, constructs the public amenity (e.g. school, maternity home, or vegetable market) to statutory PWD standards at their own expense, and hands over both the amenity land and the finished building to the Authority <strong>completely free of cost</strong>.</li>
      <li>In return, the owner retains the remainder of the land and is entitled to develop it for residential or commercial use.</li>
    </ul>
  </li>
  <li><strong>Surrender Quotas by Municipal Class (Table 11-A Note 1):</strong>
    <ul>
      <li><strong>A, B, C Class Municipal Corporations &amp; Development Authorities (PMC, TMC, NMC, NMMC, MMRDA):</strong>
        Owner surrenders <strong>40% of the land area</strong> and constructs an amenity measuring <strong>50% of the surrendered land area</strong>. (Bus stands: 50% land / 20% built; Education: 40% land / 50% built).</li>
      <li><strong>D Class Corporations &amp; A Class Municipal Councils:</strong>
        Owner surrenders <strong>35% of the land area</strong> and constructs an amenity measuring <strong>25% of the surrendered land area</strong>. (Education: 40% land / 40% built).</li>
      <li><strong>B &amp; C Class Municipal Councils &amp; Nagar Panchayats:</strong>
        Owner surrenders <strong>30% of the land area</strong> and constructs an amenity measuring <strong>20% of the surrendered land area</strong>. (Education: 40% land / 30% built).</li>
    </ul>
  </li>
  <li><strong>The 100% Gross FSI Stacking Incentive (Note xi):</strong>
    $$\text{Permissible FSI on Remaining Plot} = \text{Total FSI of Gross Original Plot} + \text{Permissible TDR Potential}$$
    Crucially, Note (xi) explicitly states: <em>"Notwithstanding anything contained in these regulations, there shall be no cap for utilization of available in-situ FSI, Premium FSI, and TDR potential of the entire plot on the remaining plot."</em> The owner can consume all the development rights of the surrendered land right on their retained parcel!</li>
  <li><strong>Amenity TDR Compensation (Note ii &amp; vi):</strong> In addition to retaining full gross FSI, the owner is awarded <strong>Construction Amenity TDR</strong> under Regulation 11.2.5 for the capital expenditure incurred in constructing the public building.</li>
  <li><strong>Composite Buildings (Note iv):</strong> On constrained urban sites where an independent plot cannot be physically subdivided, the Authority permits a composite structure. The owner hands over the prescribed amenity built-up area on the ground or first floor with independent public access, and pays a <strong>premium equal to 40% of the ASR land rate</strong> for the land component not surrendered.</li>
  <li><strong>Automatic Deemed Rezoning (Note xiii):</strong> Upon completion and issuance of the final Occupancy Certificate, the retained land automatically converts into a compliant <strong>Residential or Commercial Zone</strong> by operation of law, requiring no separate Section 37 DP amendment.</li>
</ul>
''',

    'statutory_extract': r"""11.1 MANNER OF DEVELOPMENT OF RESERVED SITE IN DEVELOPMENT PLAN (ACCOMMODATION RESERVATION PRINCIPLE)
The Planning Authority / Appropriate Authority may acquire and develop the reservation site for the same purpose. OR
The Authority may allow the owner to develop the reservation, subject to:
i) Handing over to the Planning Authority an independent plot along with constructed amenity of total area, mentioned in Note-1 below this table & as per norms prescribed by the Authority.
ii) The owner shall be entitled to develop remaining land for the uses permissible in adjoining zone with full permissible FSI of the entire Plot and permissible TDR potential of the entire Plot.
iii) The Authority, if required, shall allow the TDR for the unutilized FSI, if any (after deducting in-situ FSI), to be utilised as per TDR Regulations.
iv) Reservation may be allowed to be developed in parts.

Note 1: Percentage of total land and constructed amenity to be surrendered free of cost:
- Commercial, Health, Residential, Assembly, Public-Semi Public:
  * A, B, C Class Municipal Corporations & Dev Authorities: 40% Land | 50% Built Amenity
  * D Class MCs & A Class Municipal Councils: 35% Land | 25% Built Amenity
  * B & C Class Municipal Councils: 30% Land | 20% Built Amenity
- Education: 40% Land | 50% Built Amenity (A/B/C Class)

Note xi: Notwithstanding anything contained in these regulations, there shall be no cap for utilization of available in-situ FSI / and Premium FSI and TDR potential of the entire plot on the remaining plot.

Note xiii: ...the portion / location designated for respective reservation is continued to be in said reservation and rest of land on which residential / commercial development permission is granted is deemed to be converted into residential / commercial zone to the extent of that area.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Land &amp; Amenity Surrender Quotas (Note 1)</h4>
    </div>
    <div class="card-body">
      <p>In major corporations (A/B/C Class), private developers surrender <strong>40% of land</strong> and construct a finished public amenity measuring <strong>50% of the surrendered land area</strong> free of cost to the planning authority.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>100% Gross FSI Transfer (Note xi)</h4>
    </div>
    <div class="card-body">
      <p>The entire development potential (Basic FSI + Premium FSI + TDR) of the <strong>gross original plot</strong> is transferred onto the retained 60% parcel. Note (xi) eliminates all in-situ FSI stacking caps on the residual land.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Construction Amenity TDR (Note ii)</h4>
    </div>
    <div class="card-body">
      <p>The capital expenditure spent by the developer to construct the civil, electrical, plumbing, and structural work of the public amenity is reimbursed via <strong>Construction Amenity TDR</strong> under Reg 11.2.5 ($A/B \times 1.35$).</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Deemed Rezoning &amp; Composite Relief (Notes iv &amp; xiii)</h4>
    </div>
    <div class="card-body">
      <p>The retained plot is legally <strong>deemed converted into Residential or Commercial zone</strong> without Section 37 procedures. Small plots can build composite towers by surrendering ground floors and paying 40% ASR land premium.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="drawing-sheet-plate">
  <div class="plate-header">
    <span class="plate-num">PLATE 11.1-A: ACCOMMODATION RESERVATION SURRENDER &amp; FSI TRANSFER</span>
    <span class="plate-scale">STATUTORY TABLE 11-A &bull; NOTE 1 MATRIX</span>
  </div>
  
  <div class="table-responsive">
    <table class="data-table">
      <thead>
        <tr>
          <th>Authority Category</th>
          <th>Eligible Reservations</th>
          <th>Land Surrender (% of Gross Plot)</th>
          <th>Constructed Amenity (% of Surrendered Land)</th>
          <th>FSI Entitlement on Retained Land</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>A, B, C Class Corporations &amp; Authorities</strong> (PMC, TMC, NMC, NMMC, MMRDA)</td>
          <td>Commercial, Health, Housing, Assembly, Public-Semi Public</td>
          <td><strong>40% of Plot Area</strong></td>
          <td><strong>50% Built Amenity</strong></td>
          <td><strong>100% FSI of Gross Original Plot</strong> (No In-Situ Cap)</td>
        </tr>
        <tr>
          <td><strong>D Class Corporations &amp; A Class Councils</strong> (e.g. Akola, Dhule, Solapur)</td>
          <td>Commercial, Health, Housing, Assembly, Public-Semi Public</td>
          <td><strong>35% of Plot Area</strong></td>
          <td><strong>25% Built Amenity</strong></td>
          <td><strong>100% FSI of Gross Original Plot</strong> (No In-Situ Cap)</td>
        </tr>
        <tr>
          <td><strong>B &amp; C Class Councils &amp; Nagar Panchayats</strong></td>
          <td>Commercial, Health, Housing, Assembly, Public-Semi Public</td>
          <td><strong>30% of Plot Area</strong></td>
          <td><strong>20% Built Amenity</strong></td>
          <td><strong>100% FSI of Gross Original Plot</strong> (No In-Situ Cap)</td>
        </tr>
        <tr>
          <td><strong>Educational Complex (&gt; 1.0 Ha)</strong></td>
          <td>High School, College, Technical Academy</td>
          <td><strong>40% of Plot Area</strong></td>
          <td><strong>50% Built Amenity</strong></td>
          <td>Full Gross Plot Potential + Remaining Land Deemed Resi/Comm</td>
        </tr>
        <tr>
          <td><strong>Bus Stand (MSRTC)</strong></td>
          <td>State Transport Depot &amp; Terminus</td>
          <td><strong>50% of Plot Area</strong></td>
          <td><strong>20% Built Amenity</strong></td>
          <td>Up to 2.00 FSI commercial allied user permitted</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL SCRUTINY CALCULATION: ACCOMMODATION RESERVATION ON A 10,000 SQ.M DP SITE</h4>
  <p><strong>Scenario:</strong> A developer owns a <strong>10,000 sq.m land parcel</strong> in Pune Municipal Corporation (A Class Corporation) zoned under the DP for a "Public Health Center / Maternity Hospital". The adjoining zone is Residential (R-2), and the abutting road is 18.0 meters wide (Maximum building potential under Table 6-G = 2.00 FSI). The developer opts for Accommodation Reservation under Regulation 11.1.</p>
  
  <div class="step-box">
    <strong>Step 1: Calculate Land Surrender &amp; Retained Plot Area (Table 11-A Note 1)</strong>
    <ul>
      <li>Gross Plot Area = $10,000\text{ sq.m}$.</li>
      <li>Mandatory Land Surrender for A Class MC = <strong>40% of gross area</strong>.</li>
      <li>Surrendered Amenity Land = $10,000 \times 40\% = \mathbf{4,000\text{ sq.m}}$ (Handed over free of cost with clear title).</li>
      <li>Retained Development Land = $10,000 - 4,000 = \mathbf{6,000\text{ sq.m}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Calculate Constructed Amenity to be Handed Over</strong>
    <ul>
      <li>Required Constructed Amenity = <strong>50% of surrendered land area</strong>.</li>
      <li>Mandatory Built-up Amenity = $4,000\text{ sq.m} \times 50\% = \mathbf{2,000\text{ sq.m Built-Up Area}}$.</li>
      <li>The developer constructs a turn-key 2,000 sq.m hospital building on the 4,000 sq.m plot to PWD specifications and delivers it free to PMC.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Calculate Permissible Built-Up Area on Retained 6,000 sq.m Plot (Note xi)</strong>
    <ul>
      <li>Standard FSI potential on 18m road under Table 6-G = $2.00\text{ FSI}$.</li>
      <li>Under Note (xi), the FSI is calculated on the <strong>Gross 10,000 sq.m plot</strong>, not the reduced 6,000 sq.m net plot!</li>
      <li>Total Admissible BUA = $10,000\text{ sq.m} \times 2.00 = \mathbf{20,000\text{ sq.m BUA}}$.</li>
      <li>Effective In-Situ FSI on retained parcel = $\frac{20,000\text{ sq.m}}{6,000\text{ sq.m}} = \mathbf{3.33\text{ FSI}}$!</li>
      <li>Note (xi) explicitly confirms there is <strong>no cap</strong> on consuming this 20,000 sq.m potential on the 6,000 sq.m parcel.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 4: Additional Amenity TDR Entitlement</strong>
    <ul>
      <li>In addition to developing 20,000 sq.m of residential apartments, the developer claims <strong>Construction Amenity TDR</strong> for constructing the 2,000 sq.m hospital building under Reg 11.2.5, generating tradable DRC certificates for the market!</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>COMMON SANCTION &amp; SCRUTINY PITFALLS IN ACCOMMODATION RESERVATION</h4>
  <ul class="warning-list">
    <li><strong>Restricting FSI to the Net Retained Plot:</strong> Scrutiny officers mistakenly calculating FSI on the retained 60% plot area ($6,000 \times 2.00 = 12,000\text{ sq.m}$). Reg 11.1(ii) and Note (xi) unequivocally entitle the owner to the full FSI potential of the <strong>entire gross plot</strong> ($10,000 \times 2.00 = 20,000\text{ sq.m}$).</li>
    <li><strong>Imposing Layout Amenity Space Deductions:</strong> Demanding an additional 5% amenity space under Reg 3.5. Note (x) explicitly mandates: <em>"Provisions of Regulations of Inclusive Housing, Amenity Space, if any, shall not be applicable for development under this Regulation."</em></li>
    <li><strong>Issuing OC to Private Buildings Before Amenity Handover:</strong> Granting Occupancy Certificate to the developer's residential towers while the public hospital is still under construction. Note (viii) strictly dictates that the private OC cannot be granted until the public amenity is fully completed, conveyed, and handed over.</li>
    <li><strong>Forgetting 40% ASR Land Premium on Composite Towers:</strong> In composite buildings where land cannot be subdivided, failing to collect the mandatory 40% ASR land premium under Note (iv) for the retained ground footprint.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; Clarifications for Accommodation Reservation</h4>
  <p><strong>Corrigendum / Addendum No. CR 121/21 dt. 02-12-2021:</strong></p>
  <p>Inserted crucial operational amendments: (1) Added Note (vi) allowing developers who construct amenity area exceeding statutory minimums up to full Table 6-G potential to earn additional Amenity TDR; (2) Modified Note (xi) to clarify that there is no cap on utilizing in-situ FSI, Premium FSI, and TDR on the remaining retained plot; and (3) clarified composite building ground-floor handovers with 40% ASR land premium.</p>
</div>
''',

    'quiz': [
      {
        'question': 'In A, B, and C Class Municipal Corporations, what percentage of the gross plot area must be surrendered under Accommodation Reservation for buildable reservations (Table 11-A Note 1)?',
        'options': ['25%', '30%', '40%', '50%'],
        'answer': 2,
        'explanation': 'Under Table 11-A Note 1, in A, B, and C Class Municipal Corporations and Development Authorities, the landowner surrenders 40% of the total land area free of cost.'
      },
      {
        'question': 'How much constructed amenity area must be delivered to the Authority on the surrendered land in an A-Class Corporation under Table 11-A Note 1?',
        'options': [
          '20% of the surrendered land area',
          '25% of the surrendered land area',
          '50% of the surrendered land area',
          '100% of the surrendered land area'
        ],
        'answer': 2,
        'explanation': 'Under Table 11-A Note 1, the developer must construct and hand over an amenity measuring 50% of the surrendered land area free of cost.'
      },
      {
        'question': 'Under Table 11-A Note (xi), what is the statutory cap on utilizing the gross FSI and TDR potential of the entire original plot on the remaining retained parcel?',
        'options': [
          'Capped at 2.00 FSI',
          'Capped at 3.00 FSI',
          'Capped by Table 6-G road width',
          'There is NO CAP on utilization of available FSI on the remaining plot'
        ],
        'answer': 3,
        'explanation': 'Note (xi) explicitly states: "Notwithstanding anything contained in these regulations, there shall be no cap for utilization of available in-situ FSI / and Premium FSI and TDR potential of the entire plot on the remaining plot."'
      },
      {
        'question': 'When does the retained portion of a reserved site achieve deemed conversion into a Residential or Commercial zone under Table 11-A Note (xiii)?',
        'options': [
          'Upon submission of the layout plan',
          'Upon execution of the registered agreement',
          'Upon grant of Commencement Certificate',
          'Upon grant of full and final Occupancy Certificate after handing over the amenity'
        ],
        'answer': 3,
        'explanation': 'Under Note (xiii), the retained land is deemed to be converted into a residential/commercial zone once full and final occupation certificate is issued and the amenity is handed over.'
      }
    ],

    'prev_url': '/lessons/reg-10-14-mmr-growth-centers-and-special-authorities.html',
    'prev_title': 'Reg 10.6 to 10.16: MMR Growth Centers, Logistics & Special Authorities',
    'next_url': '/lessons/reg-11-2-tdr-generation-and-amenity-construction.html',
    'next_title': 'Reg 11.2: TDR Generation, Multipliers & Construction Amenity Formula'
}
