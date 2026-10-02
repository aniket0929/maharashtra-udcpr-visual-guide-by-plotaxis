"""
UDCPR Visual Guide - CHAPTER 11, LESSON 4
Regulation 11.3: Reservation Credit Certificate (RCC) & Municipal Financial Offsets
File: scripts/ch11_lessons/lesson_11_4_reservation_credit_certificate.py
"""

lesson_data = {
    'filename': 'reg-11-3-reservation-credit-certificate-and-financial-offsets.html',
    'lesson_id': 'reg-11-3-reservation-credit-certificate-and-financial-offsets',
    'quiz_id': 'quiz-11-4',
    'clause': 'Reg. 11.3',
    'title': 'Reservation Credit Certificate (RCC) & Municipal Financial Offsets',
    'badge_status': 'STATUTORY • MONETARY CREDITS',
    'ch_slug': 'ch11',
    'ch_title': 'Chapter 11: Acquisition of Reserved Sites & TDR',
    'meta_desc': 'Master UDCPR Regulation 11.3 for Reservation Credit Certificates (RCC): monetary credit compensation in lieu of reserved land, transferability, redemption against development charges, premiums, property taxes, and the 10% discount rule after 6 months.',
    
    'lead_summary': (
        'For landowners who surrender reserved land but do not intend to build or trade FSI in the open market, Regulation 11.3 creates a revolutionary '
        'fiscal instrument: the Reservation Credit Certificate (RCC). An RCC is a rupee-denominated, non-interest bearing, transferable municipal '
        'credit note issued in lieu of compulsory land acquisition. It empowers holders to offset municipal financial obligations across their '
        'entire operational portfolio—including statutory Development Charges, Premium FSI fees, fire infrastructure cess, and annual Property Taxes. '
        'Crucially, Regulation 11.3 introduces an aggressive incentive for planned holding: any payment made to the Authority using an RCC after '
        'six months from issuance enjoys a statutory 10% discount, turning RCCs into a liquid and highly prized asset for developers and institutional investors.'
    ),
    
    'amendment_cite': 'Statutory UDCPR-2020 Sanction (Urban Development Department, Maharashtra)',
    
    'plain_summary_html': r'''
<p>
  While TDR grants compensation in physical floor space ($m^2$), many institutional landowners, trusts, and corporate entities prefer monetary liquidity. <strong>Regulation 11.3 establishes the Reservation Credit Certificate (RCC) as a municipal bond-like offset mechanism</strong>:
</p>
<ul class="rule-list">
  <li><strong>Definition &amp; Issuance (Reg 11.3):</strong>
    <ul>
      <li>Issued by the Municipal Commissioner or Chief Officer when reserved land is immediately required for urgent civic infrastructure, public utilities, or social amenities.</li>
      <li>The certificate specifies the exact monetary compensation in Rupees, calculated under the <em>Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013 (RFCTLARR)</em>.</li>
      <li>The surrendered land must be transferred free of all encumbrances.</li>
    </ul>
  </li>
  <li><strong>Permissible Municipal Redemptions:</strong> The rupee balance on an RCC can be drawn down incrementally to pay:
    <ul>
      <li><strong>Development Charges</strong> levied under Section 124 of the MRTP Act, 1966.</li>
      <li><strong>Premium FSI payments</strong> under Table 6-A and Table 6-G.</li>
      <li><strong>Special Premiums:</strong> Industrial-to-Residential (I-to-R) conversion fees, accommodation reservation composite premiums, and layout compounding fees.</li>
      <li><strong>Municipal Property Taxes:</strong> Annual assessment taxes on any holding owned by the certificate bearer within the municipal corporation!</li>
      <li><strong>Infrastructure &amp; Betterment Levies:</strong> Water connection charges, sewerage deposits, and drainage fees.</li>
    </ul>
  </li>
  <li><strong>The Statutory 10% Discount Incentive (Clause ii):</strong>
    The certificate does not earn interest. However, to incentivize orderly redemption:
    $$\text{Discounted Value} = \text{Payment via RCC after 6 Months gets a 10% Discount}$$
    If an RCC is presented for municipal payments after <strong>six months from the date of issue</strong>, the payment required under the UDCPR is discounted by <strong>10%</strong>, effectively giving the developer a 10% subsidy on their municipal dues!</li>
  <li><strong>Open Market Transferability:</strong>
    RCCs are <strong>fully transferable</strong>. A landowner who surrenders a DP garden plot can sell the RCC to an active developer constructing a commercial mall in another part of the city, who then uses the credit to offset crores of rupees in Premium FSI fees. The Authority maintains an official endorsement ledger tracking debits and ownership transfers.</li>
</ul>
''',

    'statutory_extract': r"""11.3 RESERVATION CREDIT CERTIFICATE (RCC)
The reservation credit certificate is a certificate specifying the amount of compensation in lieu of handing over of reserved land to the Corporation and shall be issued by the Authority.

The amount mentioned in this credit certificate may be used for payment of various charges like development charges, premium, property tax, infrastructure charges etc. to the authority from time to time in future till exhausting the amount mentioned therein. Reservation Credit Certificate shall be issued subject to the following conditions:

i) The authority shall acquire the land under reservation in lieu of RCC only when it is immediately required for development or creation of amenity or services or utilities.

ii) Such certificate shall not bear any interest on the amount mentioned therein and shall be transferable. However, payment being made to the authority through the amount from RCC after six months from the date of issue of RCC shall be discounted @ 10% for the payments to be made under provisions of these UDCPR.

iii) The amount of compensation to be paid to the owner shall be as per the provisions of the relevant Acts dealing with land acquisition as amended from time to time.

iv) The land to be handed over to the Corporation shall be free from all encumbrances and procedure laid down in TDR regulations shall be followed.

The Authority shall endorse the entries of payment on such certificate from time to time. It shall maintain a record in a form considered appropriate by it of all transactions relating to grant of utilisation of reservation credit certificate.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Rupee-Denominated Credit (Reg 11.3)</h4>
    </div>
    <div class="card-body">
      <p>Issued in lieu of cash compensation under the Land Acquisition Act 2013 for immediately needed civic infrastructure. Expressed in Indian Rupees without interest accrual.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Universal Municipal Offsets</h4>
    </div>
    <div class="card-body">
      <p>Directly redeemable against municipal financial obligations: Development Charges, Premium FSI costs, conversion fees, and annual civic Property Taxes until the credit balance is exhausted.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>The 10% Holding Discount (Clause ii)</h4>
    </div>
    <div class="card-body">
      <p>Payments made through an RCC after <strong>six months from date of issuance</strong> enjoy a mandatory <strong>10% statutory discount</strong> against payments required under UDCPR provisions.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Full Transferability &amp; Trading</h4>
    </div>
    <div class="card-body">
      <p>RCC certificates are freely negotiable and transferable in the open market. The Planning Authority maintains an official ledger tracking successive holders and partial debits.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="drawing-sheet-plate">
  <div class="plate-header">
    <span class="plate-num">PLATE 11.4-A: RESERVATION CREDIT CERTIFICATE (RCC) VS TDR MATRIX</span>
    <span class="plate-scale">STATUTORY COMPARISON &bull; REGULATION 11.3</span>
  </div>
  
  <div class="table-responsive">
    <table class="data-table">
      <thead>
        <tr>
          <th>Regulatory Dimension</th>
          <th>Transferable Development Rights (TDR)</th>
          <th>Reservation Credit Certificate (RCC)</th>
          <th>Strategic Best-Use Application</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Statutory Currency</strong></td>
          <td><strong>Floor Space Index (m&sup2; of BUA)</strong></td>
          <td><strong>Financial Currency (Rupees &bull; INR)</strong></td>
          <td>TDR for builders; RCC for funds/investors</td>
        </tr>
        <tr>
          <td><strong>Primary Usability</strong></td>
          <td>Loaded onto receiving plots for tall buildings</td>
          <td>Offset Development Charges, Premium FSI, Taxes</td>
          <td>RCC reduces direct project cash outflows</td>
        </tr>
        <tr>
          <td><strong>Location Indexation</strong></td>
          <td>Indexed by ASR ratio: <code>X = (Rg / Rr) &times; Y</code></td>
          <td>Direct face value deduction in Rupees</td>
          <td>RCC has no geographical zone friction</td>
        </tr>
        <tr>
          <td><strong>Holding Benefit</strong></td>
          <td>Market appreciation of TDR price</td>
          <td><strong>10% Discount on municipal dues</strong> after 6 mos</td>
          <td>RCC guarantees 10% savings on city charges</td>
        </tr>
        <tr>
          <td><strong>Transferability</strong></td>
          <td>Transferable via registered DRC deed</td>
          <td>Transferable via Authority endorsement</td>
          <td>Both freely tradable in the private market</td>
        </tr>
        <tr>
          <td><strong>Land Precondition</strong></td>
          <td>Any DP reservation or road widening</td>
          <td><strong>Immediately required</strong> for civic infrastructure</td>
          <td>RCC requires urgent public utility demand</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL SCRUTINY CALCULATION: PREMIUM FSI PAYMENT USING RCC AFTER 6 MONTHS</h4>
  <p><strong>Scenario:</strong> A commercial real estate developer in Nagpur owes <strong>Rs. 1,00,00,000 (Rs. 1.00 Crore)</strong> to Nagpur Municipal Corporation (NMC) as Premium FSI charges for a new corporate complex. The developer purchases an unexhausted Reservation Credit Certificate (RCC) with a face value of <strong>Rs. 1.00 Crore</strong> from a hospital trust that surrendered land 8 months ago. How much RCC credit is consumed under the 10% discount rule?</p>
  
  <div class="step-box">
    <strong>Step 1: Verify Holding Period &amp; Discount Eligibility (Reg 11.3.ii)</strong>
    <ul>
      <li>Date of RCC Issuance: 8 months prior ($> 6\text{ months}$ statutory threshold).</li>
      <li>Statutory Mandate: <em>"payment being made to the authority through the amount from RCC after six months from the date of issue of RCC shall be discounted @ 10% for the payments to be made under provisions of these UDCPR."</em></li>
      <li>Eligibility: Fully eligible for the 10% statutory discount.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Calculate Discounted Payment Obligation</strong>
    <ul>
      <li>Gross Premium FSI Dues = $\text{Rs. 1,00,00,000}$.</li>
      <li>10% Statutory Discount = $10\% \times \text{Rs. 1,00,00,000} = \mathbf{\text{Rs. 10,00,000}}$.</li>
      <li>Net Amount Settled via RCC = $\text{Rs. 1,00,00,000} - \text{Rs. 10,00,000} = \mathbf{\text{Rs. 90,00,000}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Endorsement on the RCC Certificate</strong>
    <ul>
      <li>NMC debits <strong>Rs. 90,00,000</strong> from the RCC ledger to extinguish the full Rs. 1.00 Crore Premium FSI obligation.</li>
      <li>Remaining unexhausted RCC balance = $\text{Rs. 1,00,00,000} - \text{Rs. 90,00,000} = \mathbf{\text{Rs. 10,00,000}}$ retained by the developer for future development charges or property taxes!</li>
      <li>The developer effectively saves Rs. 10 Lakhs in cash simply by utilizing the matured RCC instrument.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>COMMON SANCTION &amp; SCRUTINY PITFALLS IN RESERVATION CREDIT CERTIFICATES (RCC)</h4>
  <ul class="warning-list">
    <li><strong>Claiming the 10% Discount within the First 6 Months:</strong> Attempting to redeem an RCC at a 10% discount 2 months after issuance. Clause (ii) expressly restricts the 10% discount to redemptions made <strong>after six months from the date of issue</strong>.</li>
    <li><strong>Demanding Interest on Unused RCC Balances:</strong> Requesting statutory interest from the Municipal Corporation on an RCC held for 3 years. Clause (ii) explicitly decrees: <em>"Such certificate shall not bear any interest on the amount mentioned therein."</em></li>
    <li><strong>Refusing Property Tax Offsets:</strong> Municipal revenue departments refusing to accept RCCs for annual property taxes. Reg 11.3 explicitly authorizes the certificate for <em>"development charges, premium, property tax, infrastructure charges etc."</em></li>
    <li><strong>Issuing RCCs for Non-Urgent Reservations:</strong> Landowners demanding RCCs for land the municipality has no budget or immediate plan to develop. Clause (i) restricts RCC issuance strictly to land <strong>immediately required</strong> for development or creation of amenities.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory History &amp; Clarifications for Reservation Credit Certificates</h4>
  <p><strong>UDCPR-2020 Statutory Inception:</strong></p>
  <p>Regulation 11.3 was enacted to overcome the fiscal paralysis of municipal corporations unable to raise cash for statutory land acquisition under the 2013 Land Acquisition Act. By transforming municipal acquisition liabilities into tradeable tax credits, Maharashtra established India's first fully codified municipal credit offset architecture.</p>
</div>
''',

    'quiz': [
      {
        'question': 'What is a Reservation Credit Certificate (RCC) under UDCPR Regulation 11.3?',
        'options': [
          'A certificate granting additional FSI in square meters',
          'A certificate specifying monetary compensation in rupees in lieu of surrendered reserved land',
          'A bank guarantee issued by a developer',
          'A building occupancy permit'
        ],
        'answer': 1,
        'explanation': 'Under Regulation 11.3, an RCC is a certificate specifying the amount of monetary compensation in rupees in lieu of handing over reserved land to the Corporation.'
      },
      {
        'question': 'What statutory discount is applied when making payments to the Authority using an RCC after 6 months from issuance (Reg 11.3.ii)?',
        'options': ['5% discount', '10% discount', '15% discount', '20% discount'],
        'answer': 1,
        'explanation': 'Regulation 11.3(ii) explicitly mandates: "payment being made to the authority through the amount from RCC after six months from the date of issue of RCC shall be discounted @ 10%."'
      },
      {
        'question': 'Does an unexhausted Reservation Credit Certificate (RCC) accrue interest while being held by the owner?',
        'options': [
          'Yes, at bank lending rates',
          'Yes, at 6% simple interest per annum',
          'No, such certificate shall not bear any interest on the amount mentioned therein',
          'Only if held for more than 3 years'
        ],
        'answer': 2,
        'explanation': 'Regulation 11.3(ii) explicitly dictates: "Such certificate shall not bear any interest on the amount mentioned therein and shall be transferable."'
      },
      {
        'question': 'Which of the following municipal obligations CANNOT be paid using an RCC under Reg 11.3?',
        'options': [
          'Development charges under Section 124',
          'Premium FSI charges',
          'Annual Municipal Property Taxes',
          'None of the above (all can be paid using RCC)'
        ],
        'answer': 3,
        'explanation': 'Under Regulation 11.3, the amount may be used for payment of various charges like development charges, premium, property tax, infrastructure charges etc. All are permitted.'
      }
    ],

    'prev_url': '/lessons/reg-11-2-6-tdr-utilisation-indexation-and-restrictions.html',
    'prev_title': 'Reg 11.2.6 to 11.2.13: TDR Utilisation, ASR Indexation & Receiving Caps',
    'next_url': '/lessons/reg-12-1-structural-design-materials-and-building-services.html',
    'next_title': 'Reg. 12.1 - 12.4: Structural Safety, Materials Quality & Building Services'
}
