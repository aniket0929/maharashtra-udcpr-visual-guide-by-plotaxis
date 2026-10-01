"""
UDCPR FROM SCRATCH - CHAPTER 7, LESSON 4
Module: scripts/ch07_lessons/lesson_7_4_old_dilapidated_societies.py
Statutory Anchor: Regulation 7.5 & Regulation 7.6 (7.6.1 & 7.6.2)
Content: Protection of Authorised FSI, Redevelopment of 30-Year-Old Housing Societies (30% Incentive / 15 sqm), and Tenanted Buildings (50% Incentive)
"""

lesson_data = {
    'filename': 'reg-7-6-old-dilapidated-and-housing-societies.html',
    'lesson_id': '7.4',
    'quiz_id': 'quiz-7-4',
    'clause': 'Regulation 7.5 & 7.6',
    'title': 'Redevelopment of 30-Year-Old Societies & Dilapidated Buildings',
    'badge_status': 'CORE STATUTORY SPECIFICATION',
    'ch_slug': 'ch07',
    'ch_title': 'Chapter 7: Higher FSI for Certain Uses',
    'meta_desc': 'Guide to Co-operative Housing Society redevelopment under UDCPR Reg 7.5 and 7.6: 30-year age trigger, 30% incentive FSI / 15 sqm per tenement, 27.87 sqm minimum carpet, and 50% tenant rehab incentives.',
    'lead_summary': 'How Maharashtra’s private housing societies and tenanted chawls rebuild safely: unlocking the 30-year statutory age threshold, protecting previously consumed FSI, claiming 30% society incentive BUA, and upgrading to 27.87 sq.m minimum carpet homes.',
    'amendment_cite': 'UDCPR-2020 Reg 7.5 & 7.6, Notification No. CR 236/18 Part-3 dt. 02nd Dec 2021, Order dt. 07th Oct 2024',

    'plain_summary_html': r"""
      <p>
        Across Mumbai, Pune, Thane, Nashik, and Nagpur, thousands of private <strong>Co-operative Housing Societies (CHS)</strong> and rent-controlled tenanted buildings face structural aging. Under <strong>Regulation 7.5</strong> and <strong>Regulation 7.6</strong>, UDCPR provides powerful statutory guarantees to redevelop these buildings safely without loss of floor space.
      </p>
      <p>
        First, <strong>Regulation 7.5 (Protection of FSI)</strong> establishes that no building will ever lose its previously authorized FSI. If an older building lawfully consumed 2.40 FSI through past schemes or TDR, that full 2.40 FSI is legally protected as the base for redevelopment, even if the current road width only allows 2.00 FSI under Table 6-G!
      </p>
      <p>
        Second, <strong>Regulation 7.6.1</strong> creates a dedicated redevelopment route for <strong>buildings having an age of more than 30 years</strong> (or declared dangerous/dilapidated by a municipal structural audit). Under this clause, the society is granted:
      </p>
      <div style="background:var(--paper-raised); border-left:4px solid var(--blueprint); padding:12px; margin:14px 0; font-family:var(--mono);">
        $$\text{FSI Allowed} = \text{Existing Authorized BUA} + \mathbf{\max(30\%\text{ of Existing BUA},\; 15\text{ sq.m per tenement})}$$
        $$\text{Statutory Floor: Minimum Carpet Area} = \mathbf{27.87\text{ sq.m (300 sq.ft)}}\text{ per residential member}$$
      </div>
      <p>
        For <strong>Tenanted Buildings (Regulation 7.6.2)</strong>, developers who rehouse protected tenants with at least 27.87 sq.m carpet are awarded a massive <strong>50% incentive FSI</strong> on the rehabilitation component, financed by 51% occupant consent agreements.
      </p>
    """,

    'statutory_extract': """
### 7.5 PROTECTION OF FSI IN REDEVELOPMENT OF EXISTING BUILDINGS
For redevelopment or reconstruction of existing buildings, the FSI to be allowed shall be FSI permissible under Regulation No.6.1 or 6.3, or the FSI consumed by the existing authorized building including TDR, premium FSI etc., whichever is more. (Such TDR, Premium FSI etc. utilised in existing building shall be treated as authorisedly consumed FSI entitled for redevelopment.)

### 7.6 REDEVELOPMENT OF OLD DILAPIDATED / DANGEROUS BUILDINGS
Reconstruction / Redevelopment in whole or in part of any building which has ceased to exist in consequence of accidental fire / natural collapse or demolition for the reasons of the same having been declared dangerous or dilapidated... or building having age of more than 30 years...

7.6.1 Redevelopment of Multi-Dwelling Buildings of Co-Operative Housing Societies / Apartments
i) FSI allowed for redevelopment shall be FSI of existing authorized building and incentive FSI to the extent of 30% of existing built up area or 15 Sq.m. per tenement, whichever is more... Such incentive FSI shall not be applicable for redevelopment of existing bungalow.
ii) In cases where carpet area occupied by residential tenement in existing building is less than carpet area of 27.87 sq.m. then such tenement shall be entitled for minimum carpet area of 27.87 sq.m. and difference of these areas shall be allowed as additional FSI without any premium.

7.6.2 Redevelopment of Tenanted Buildings
i) In addition to consumed FSI, 50% incentive FSI of the rehab area required for rehabilitation of tenants shall be allowed. Provided that rehab area shall be authorisedly utilised area or 27.87 sq.m. carpet area per tenement, whichever is more.
ii) All eligible tenants shall be re-accommodated in redeveloped building.
2) Agreement on stamp paper by at least 51% of landlord / occupants shall be deposited with Authority.
    """,

    'clause_cards_html': r"""
      <div class="card-grid">
        <div class="card">
          <span class="kicker-card">RIGHT PRESERVATION</span>
          <h3 class="card-title">Protected Consumed FSI (Reg 7.5)</h3>
          <p class="card-body">
            Reconstruction is guaranteed to retain the full historically consumed authorized FSI (including loaded TDR and premium). Redevelopment can never result in a smaller building than what lawfully existed before.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">SOCIETY INCENTIVE</span>
          <h3 class="card-title">30% BUA / 15 sq.m Bonus (Reg 7.6.1)</h3>
          <p class="card-body">
            For multi-dwelling societies &gt; 30 years old, the developer receives an extra <strong>30% incentive FSI</strong> on existing BUA, or a flat <strong>15 sq.m per flat</strong>, whichever is higher, providing the free-sale inventory needed to finance reconstruction.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">MINIMUM HABITATION</span>
          <h3 class="card-title">27.87 sq.m (300 sq.ft) Floor</h3>
          <p class="card-body">
            Small flat owners living in 150 or 200 sq.ft homes are elevated to a statutory minimum carpet area of <strong>27.87 sq.m (300 sq.ft)</strong>. The area difference is granted as free additional FSI without any municipal premium.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">TENANTED CHAWLS</span>
          <h3 class="card-title">50% Tenant Rehab Incentive (Reg 7.6.2)</h3>
          <p class="card-body">
            Landlords/developers rehousing protected tenants receive <strong>50% incentive FSI</strong> on total rehab area. An agreement signed by <strong>51% of occupants</strong> legally validates the project, backed by a 10-year maintenance corpus fund.
          </p>
        </div>
      </div>
    """,

    'plate_or_table_html': """
      <div class="table-container">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>Building Category</th>
              <th>Statutory Trigger / Eligibility</th>
              <th>Permissible Base FSI</th>
              <th>Statutory Incentive FSI Entitlement</th>
              <th>Minimum Member Carpet Guarantee</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Authorized Existing Building</strong><br>(Regulation 7.5)</td>
              <td>Lawfully sanctioned plan / OC on record</td>
              <td>Table 6-G potential OR historically consumed FSI, <strong>whichever is more</strong></td>
              <td>Balance potential via Table 6-G</td>
              <td>Existing authorized carpet area</td>
            </tr>
            <tr>
              <td><strong>Co-operative Housing Society (CHS)</strong><br>(Regulation 7.6.1)</td>
              <td><strong>Age &gt; 30 years</strong>, or structural audit declaring dilapidated / dangerous</td>
              <td>Existing authorized BUA</td>
              <td><strong>30% of existing BUA</strong> OR <strong>15 sq.m per flat</strong> (whichever is more)</td>
              <td><strong>27.87 sq.m</strong> (300 sq.ft) free of premium</td>
            </tr>
            <tr>
              <td><strong>Tenanted Building / Chawl</strong><br>(Regulation 7.6.2)</td>
              <td>Protected tenants under Rent Control Act; 51% consent</td>
              <td>Existing authorized BUA</td>
              <td><strong>50% incentive FSI</strong> of the total rehabilitation component</td>
              <td><strong>27.87 sq.m</strong> (300 sq.ft) per tenant family</td>
            </tr>
            <tr>
              <td><strong>Gram Panchayat Old Buildings</strong><br>(Directives Oct 2024)</td>
              <td>Age &gt; 30 years in village merged into ULB/Authority</td>
              <td>Authorized BUA as per GP property tax bill</td>
              <td>Same as Reg 7.6.1 / 7.6.2</td>
              <td>27.87 sq.m minimum carpet</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,

    'worked_example_html': r"""
      <div class="math-box">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:12px; color:var(--ink);">
          Worked Case: Redeveloping a 35-Year-Old Housing Society under Reg 7.6.1
        </h4>
        <p><strong>Society Parameters:</strong></p>
        <ul>
          <li>Building: 4-storey residential society constructed in 1988 (Age: 36 years) in Pune.</li>
          <li>Number of Flats: <strong>24 members</strong>.</li>
          <li>Existing Authorized BUA = <strong>1,800 sq.m</strong> (average 75 sq.m BUA / 58 sq.m carpet per flat).</li>
          <li>Plot Area = 1,200 sq.m fronting a 15.0m road (Table 6-G potential = 2.50 FSI = 3,000 sq.m).</li>
        </ul>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint); padding-left: 14px;">
          <p><strong>Step 1: Calculate Society Incentive BUA (Reg 7.6.1)</strong></p>
          <p>Under Reg 7.6.1, incentive FSI is the greater of:
            $$\text{Option A (30\% of BUA)} = 1,800\text{ sq.m} \times 30\% = \mathbf{540\text{ sq.m}}$$
            $$\text{Option B (15 sq.m per flat)} = 24 \times 15\text{ sq.m} = \mathbf{360\text{ sq.m}}$$
            $$\text{Incentive BUA Granted} = \mathbf{540\text{ sq.m}}$$
          </p>
          <p>Total Base Redevelopment BUA $= 1,800 + 540 = \mathbf{2,340\text{ sq.m}}$.</p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--amber); padding-left: 14px;">
          <p><strong>Step 2: Utilization of Balance Table 6-G Potential</strong></p>
          <p>The plot potential on a 15.0m road is $1,200 \times 2.50 = \mathbf{3,000\text{ sq.m}}$.</p>
          <p>Since the base entitlement ($2,340\text{ sq.m}$) is less than maximum potential ($3,000\text{ sq.m}$), the society/developer can purchase:
            $$\text{Balance Permissible Potential} = 3,000 - 2,340 = \mathbf{660\text{ sq.m (via Premium FSI / TDR)}}$$
            $$\text{Total Project Potential} = \mathbf{3,000\text{ sq.m (before Ancillary Area FSI!)}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint-soft); padding-left: 14px;">
          <p><strong>Step 3: Member Living Space Upgrade</strong></p>
          <p>Existing carpet was already 58 sq.m (&gt; 27.87 sq.m minimum). Members can divide the 540 sq.m incentive BUA among themselves or allow the developer to sell it to cover 100% of construction and transit rent!</p>
        </div>
      </div>
    """,

    'pitfalls_html': """
      <div class="panel-alert">
        <h4 style="font-family:var(--disp); font-weight:700; color:var(--brick); margin-bottom:8px;">
          LETHAL TRAPS IN SOCIETY & CHAWL REDEVELOPMENT
        </h4>
        <ul style="margin-left: 18px; line-height: 1.6;">
          <li>
            <strong>Claiming 30% Incentive on Independent Bungalows:</strong> The proviso to Reg 7.6.1(i) explicitly bars single-family bungalows from claiming the 30% or 15 sq.m incentive FSI. It applies strictly to multi-dwelling apartment buildings.
          </li>
          <li>
            <strong>Missing Proof of 30-Year Age:</strong> Age must be substantiated through municipal completion certificates, assessment tax ledgers, or registered Sanad documents. Uncertified structures cannot avail Reg 7.6 incentives.
          </li>
          <li>
            <strong>Ignoring the 10-Year Maintenance Corpus:</strong> Reg 7.6 Note 3 mandates that the developer must create a corpus fund to maintain the building for <strong>10 years</strong> post-possession. Omitting this escrow halts Occupancy Certificates.
          </li>
          <li>
            <strong>Failing to Re-accommodate All Tenants:</strong> In tenanted redevelopment under Reg 7.6.2, 100% of eligible protected tenants must be provided permanent re-accommodation. Evicting tenants without housing triggers immediate revocation of sanction.
          </li>
        </ul>
      </div>
    """,

    'amendment_section_html': """
      <div class="panel-info">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:8px;">Statutory Amendments</h4>
        <ul style="font-size:0.92rem; line-height:1.6; margin-left:18px;">
          <li><strong>Notification CR 236/18 Part-3 (dt. 02 Dec 2021):</strong> Inserted Regulation 7.6.1 formalizing the 30% / 15 sq.m incentive FSI formula for multi-dwelling co-operative societies.</li>
          <li><strong>Government Order UOR 38/CR 118/2024 (dt. 07 Oct 2024):</strong> Extended Regulation 7.6.1 incentives to 30-year-old structures in former Gram Panchayat areas merged into urban local bodies, using property tax bills as proof of authorized area.</li>
        </ul>
      </div>
    """,

    'quiz': [
      {
        'question': 'Under Regulation 7.6.1, what is the statutory incentive FSI granted to a Co-operative Housing Society for redeveloping a building more than 30 years old?',
        'options': [
          '10% of existing BUA',
          '20% of existing BUA',
          '30% of existing BUA or 15 sq.m per tenement, whichever is more',
          '50% of the gross plot area'
        ],
        'answer': 2,
        'explanation': 'Regulation 7.6.1(i) explicitly grants incentive FSI to the extent of 30% of existing built-up area or 15 sq.m per tenement, whichever is more.'
      },
      {
        'question': 'What is the statutory minimum carpet area guaranteed to an existing residential member in a society redevelopment scheme under Regulation 7.6.1(ii)?',
        'options': [
          '20.0 sq.m',
          '25.0 sq.m',
          '27.87 sq.m (300 sq.ft)',
          '35.0 sq.m'
        ],
        'answer': 2,
        'explanation': 'Reg 7.6.1(ii) provides that if an existing residential flat is smaller than 27.87 sq.m, the member is entitled to a minimum carpet area of 27.87 sq.m without paying any premium.'
      },
      {
        'question': 'Under Regulation 7.6.2, what incentive FSI is granted to a developer for redeveloping a Tenanted Building?',
        'options': [
          '25% of the plot area',
          '50% incentive FSI of the rehab area required for rehabilitation of tenants',
          '70% of the construction cost',
          'Flat 1.00 FSI'
        ],
        'answer': 1,
        'explanation': 'Regulation 7.6.2(i) dictates that "50% incentive FSI of the rehab. area required for rehabilitation of tenants shall be allowed."'
      },
      {
        'question': 'How does Regulation 7.5 protect an existing building being redeveloped if it had previously consumed more FSI than current road tables allow?',
        'options': [
          'It forces the building to reduce to current road potential',
          'It protects the full FSI consumed by the existing authorized building, whichever is more',
          'It requires purchasing 100% TDR for the difference',
          'It requires a special cabinet waiver'
        ],
        'answer': 1,
        'explanation': 'Regulation 7.5 guarantees that the FSI allowed shall be the FSI permissible under Reg 6.1/6.3 or the FSI consumed by the existing authorized building (including TDR and premium), whichever is more.'
      }
    ],

    'prev_url': '/lessons/reg-7-4-mhada-housing-redevelopment.html',
    'prev_title': 'Reg 7.4: Redevelopment of MHADA Housing Schemes',
    'next_url': '/lessons/reg-7-8-it-data-centers-and-biotech-parks.html',
    'next_title': 'Reg 7.8 & 7.9: IT Establishments, Data Centers & Biotech Parks'
}
