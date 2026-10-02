"""
UDCPR Visual Guide - CHAPTER 6, LESSON 2
Module: scripts/ch06_lessons/lesson_6_2_ancillary_fsi.py
Statutory Anchor: Regulation 6.3 Note (i), Regulation 6.1.1 Note (1), & Regulation 6.6
Content: Ancillary Area FSI (60% Res / 80% Non-Res), Premium Tariffs, and Floor-Wise P-Line Accounting
"""

lesson_data = {
    'filename': 'reg-6-3-ancillary-area-fsi.html',
    'lesson_id': '6.2',
    'quiz_id': 'quiz-6-2',
    'clause': 'Regulation 6.3 Note (i) & 6.6',
    'title': 'Ancillary Area FSI (60% Res / 80% Non-Res) & P-Line Accounting',
    'badge_status': 'CORE STATUTORY SPECIFICATION',
    'ch_slug': 'ch06',
    'ch_title': 'Chapter 6: General Building Requirements - Setback, Marginal Distance, Height and Permissible FSI',
    'meta_desc': 'Understand UDCPR Ancillary Area FSI rules: 60% residential, 80% non-residential quotas, 10% to 15% ASR premium rates, and P-line outer periphery measurement under Reg 6.6.',
    'lead_summary': 'How UDCPR-2020 eradicated arbitrary "free-of-FSI" exemptions by introducing an upfront, transparent 60% (residential) and 80% (commercial) Ancillary Area FSI allowance measured through floor-by-floor P-lines.',
    'amendment_cite': 'UDCPR-2020 Reg 6.1.1 Note (1), Reg 6.3 Note (i), and Notification dt. 12th Oct 2022',

    'plain_summary_html': """
      <p>
        Prior to UDCPR-2020, planning permissions in Maharashtra were plagued by complex, disputed lists of features that were claimed to be "free of FSI" (balconies, flower beds, service verandas, niches, double-height voids). This generated endless litigation, arbitrary officer discretion, and corruption.
      </p>
      <p>
        UDCPR revolutionised development control with a single master formula under <strong>Regulation 6.3 Note (i)</strong>: <strong>Ancillary Area FSI</strong>. Instead of item-by-item exemptions, developers are granted an automatic, optional ancillary quota of <strong>up to 60%</strong> of the proposed consumed FSI for residential developments, and <strong>up to 80%</strong> for non-residential developments, upon payment of a modest premium.
      </p>
      <p>
        Coupled with <strong>Regulation 6.6 (P-Line Rule)</strong>, any space enclosed within the outer periphery of a floor slab—including balconies, cupboards, and covered terraces—is counted in the gross built-up area. If it is not strictly excluded under Regulation 6.8 (like parking or fire towers), it is simply absorbed by this massive 60% or 80% Ancillary FSI cushion.
      </p>
    """,

    'statutory_extract': """
### 6.3 Permissible FSI - Note (i)
In addition to above, ancillary area FSI up to the extent of 60% of the proposed FSI in the development permission (including Basic FSI, Premium FSI, TDR but excluding the area covered in Regulation No.6.8) shall be allowed with the payment of premium as specified in Regulation No.6.1.1. This shall be applicable to all buildings in all zones.

Provided that in case of non-residential use, the extent of ancillary area FSI shall be upto 80%. No separate calculation shall be required to be done for this ancillary area FSI. Entire FSI in the development permission shall be calculated and shall be measured with reference to permissible FSI, premium FSI, TDR, additional FSI including ancillary area FSI added therein.

Provided further that, this ancillary area FSI shall be applicable to all other schemes like TOD, PMAY, ITP, IT, MHADA, etc. except Rehabilitation component in SRA. In the result, free of FSI items in the said schemes, if any, other than mentioned in UDCPR, shall stand deleted.

### 6.1.1 (Rate of Premium for Ancillary Area FSI)
| Sr. No. | Authority / Area | Rate of Premium |
| --- | --- | --- |
| 1 | Pune, Pimpri-Chinchwad, Municipal Corporations in MMR, Nagpur | 15% of ASR land rate |
| 2 | Other Municipal Corporations | 10% of ASR land rate |
| 3 | Municipal Councils, Nagar Panchayats and R.P. area | 10% of ASR land rate |

### 6.6 CALCULATION OF BUILT UP AREA FOR THE PURPOSES OF FSI
Outer periphery of the construction floor wise (P-line) including everything but excluding ducts, voids, and items in Regulation No. 6.8, shall be calculated for the purpose of computation of FSI. The open balcony, double height terraces and cupboard shall also be included in P-line of respective floor, irrespective of its use / function.
    """,

    'clause_cards_html': """
      <div class="card-grid">
        <div class="card">
          <span class="kicker-card">RESIDENTIAL QUOTA</span>
          <h3 class="card-title">60% Residential Ancillary</h3>
          <p class="card-body">
            Available on all residential buildings across all zones. Developers can load up to <strong>60%</strong> on top of the total proposed in-situ FSI (Basic + Premium + TDR). Absorbs all living extensions, balconies, internal lobbies, and habitable terraces without complicated individual calculations.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">COMMERCIAL QUOTA</span>
          <h3 class="card-title">80% Non-Residential Ancillary</h3>
          <p class="card-body">
            For mercantile, commercial offices, IT parks, retail, and mixed-use commercial portions, the allowance expands up to <strong>80%</strong>. This generous multiplier accommodates wide retail atriums, deep service corridors, and extensive customer amenities essential for modern commerce.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">PREMIUM TARIFF</span>
          <h3 class="card-title">10% to 15% ASR Rate</h3>
          <p class="card-body">
            Extremely affordable compared to regular Premium FSI (35% ASR). In MMR, Pune, PCMC, and Nagpur Corporations, the premium is strictly <strong>15% of ASR land rate</strong>. In all other Municipal Corporations, Councils, and RP areas, it is just <strong>10% of ASR land rate</strong>.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">MEASUREMENT STANDARD</span>
          <h3 class="card-title">The P-Line Rule (Reg 6.6)</h3>
          <p class="card-body">
            Total Built-Up Area is measured strictly floor-by-floor along the <strong>outermost perimeter line (P-line)</strong>. Open balconies, double-height terraces, and cupboards are automatically included in the P-line. Only vertical voids, ducts, and Reg 6.8 items are punched out.
          </p>
        </div>
      </div>
    """,

    'plate_or_table_html': """
      <div class="table-container">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>User Category</th>
              <th>Ancillary FSI Quota</th>
              <th>Planning Authority / Jurisdiction</th>
              <th>Applicable Premium (% of ASR Land Rate)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="2"><strong>Residential Buildings</strong><br>(Single, multi-family, group housing)</td>
              <td rowspan="2"><strong>Up to 60%</strong> of proposed FSI</td>
              <td>Pune, PCMC, MMR Corporations, Nagpur</td>
              <td><strong>15%</strong> of unguided ASR land rate</td>
            </tr>
            <tr>
              <td>Other Municipal Corporations, Councils, NPs, & Regional Plans</td>
              <td><strong>10%</strong> of unguided ASR land rate</td>
            </tr>
            <tr>
              <td rowspan="2"><strong>Non-Residential Buildings</strong><br>(Commercial, offices, retail, hospitality)</td>
              <td rowspan="2"><strong>Up to 80%</strong> of proposed FSI</td>
              <td>Pune, PCMC, MMR Corporations, Nagpur</td>
              <td><strong>15%</strong> of unguided ASR land rate</td>
            </tr>
            <tr>
              <td>Other Municipal Corporations, Councils, NPs, & Regional Plans</td>
              <td><strong>10%</strong> of unguided ASR land rate</td>
            </tr>
            <tr>
              <td><strong>Special Schemes</strong><br>(TOD, PMAY, ITP, IT Parks, MHADA)</td>
              <td>As per use (60% res / 80% comm)</td>
              <td>All jurisdictions across Maharashtra</td>
              <td>Free-of-FSI items abolished; uniform Ancillary rules apply. (Exempts SRA rehab)</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,

    'worked_example_html': r"""
      <div class="math-box">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:12px; color:var(--ink);">
          Worked Case: Calculating Total Carpet Potential with 60% Ancillary FSI
        </h4>
        <p><strong>Project Baseline:</strong></p>
        <ul>
          <li>Plot Area = <strong>3,000 sq.m</strong> in Pune Municipal Corporation on an 18.0m road.</li>
          <li>Net Retained Plot = 3,000 sq.m. ASR Land Rate = <strong>Rs 30,000 / sq.m</strong>.</li>
          <li>Basic FSI = 1.10. Developer loads 0.50 Premium FSI and 0.90 TDR (Total proposed = 2.50 FSI).</li>
        </ul>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint); padding-left: 14px;">
          <p><strong>Step 1: Baseline Proposed Built-Up Area</strong></p>
          <p>Proposed regular FSI potential = $1.10 + 0.50 + 0.90 = \mathbf{2.50}$.
            $$\text{Proposed Regular BUA} = 3,000\text{ sq.m} \times 2.50 = \mathbf{7,500\text{ sq.m}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--amber); padding-left: 14px;">
          <p><strong>Step 2: 60% Ancillary Area FSI Quota (Reg 6.3 Note i)</strong></p>
          <p>Residential development allows up to 60% Ancillary FSI:
            $$\text{Ancillary FSI} = 2.50 \times 0.60 = \mathbf{1.50}$$
            $$\text{Ancillary BUA} = 7,500\text{ sq.m} \times 0.60 = \mathbf{4,500\text{ sq.m}}$$
            $$\text{Total Gross Potential (P-Line)} = 7,500 + 4,500 = \mathbf{12,000\text{ sq.m (Effective FSI = 4.00!)}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint-soft); padding-left: 14px;">
          <p><strong>Step 3: Financial Premium Cost for Ancillary Area FSI</strong></p>
          <p>Under Reg 6.1.1, Pune Municipal Corporation rate = 15% of ASR:
            $$\text{Premium Rate per sq.m} = \text{Rs } 30,000 \times 15\% = \mathbf{\text{Rs } 4,500 / \text{sq.m}}$$
            $$\text{Total Ancillary Premium} = 4,500\text{ sq.m} \times \text{Rs } 4,500 = \mathbf{\text{Rs } 20,250,000}$$
          </p>
          <p>Notice that while 0.50 Premium FSI costs $35\% \times 30,000 = \text{Rs } 10,500/\text{sq.m}$, Ancillary FSI costs less than half at Rs 4,500/sq.m!</p>
        </div>
      </div>
    """,

    'pitfalls_html': """
      <div class="panel-alert">
        <h4 style="font-family:var(--disp); font-weight:700; color:var(--brick); margin-bottom:8px;">
          COMMON COMPLIANCE PITFALLS IN ANCILLARY FSI & P-LINE MAPPING
        </h4>
        <ul style="margin-left: 18px; line-height: 1.6;">
          <li>
            <strong>Claiming Balconies or Flower Beds as Free of FSI:</strong> Under UDCPR Reg 6.6, flower beds, balconies, and enclosed niches are <em>never</em> free of FSI. They must fall within the P-line and be covered by your Ancillary FSI pool.
          </li>
          <li>
            <strong>Compounding Ancillary on Ancillary:</strong> Ancillary FSI is calculated strictly as 60% of the <em>proposed FSI</em> (Basic + Premium + TDR). You cannot calculate 60% on top of another Ancillary layer.
          </li>
          <li>
            <strong>Attempting Ancillary on SRA Rehabilitation Component:</strong> Note (i) expressly excludes the rehabilitation component in Slum Rehabilitation Schemes (SRA). SRA rehab continues under special scheme rules.
          </li>
          <li>
            <strong>Confusing Ancillary Premium with Regular Premium FSI:</strong> Regular Premium FSI (Table 6-G Col 4) is charged at 35% of ASR. Ancillary Area FSI is charged at only 10% to 15% of ASR. Do not mix their challans or valuation ledgers.
          </li>
        </ul>
      </div>
    """,

    'amendment_section_html': """
      <div class="panel-info">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:8px;">Regulatory Chronology</h4>
        <ul style="font-size:0.92rem; line-height:1.6; margin-left:18px;">
          <li><strong>UDCPR-2020 Sanction (02 Dec 2020):</strong> Formal introduction of unified 60% Ancillary FSI and abolishment of old DCR free-of-FSI loopholes.</li>
          <li><strong>Addendum CR 236/18 (dt. 14 Jan 2021):</strong> Clarified exclusion of SRA rehabilitation component from Ancillary FSI rules.</li>
          <li><strong>Notification CR 236/18 Part-6 (dt. 12 Oct 2022):</strong> Explicit insertion of CIDCO NTDA alongside Municipal Corporations for the 15% premium tariff tier.</li>
        </ul>
      </div>
    """,

    'quiz': [
      {
        'question': 'What is the maximum permissible Ancillary Area FSI for a pure residential building under Regulation 6.3 Note (i)?',
        'options': [
          '35% of the proposed FSI',
          '50% of the basic FSI',
          '60% of the proposed FSI',
          '80% of the proposed FSI'
        ],
        'answer': 2,
        'explanation': 'Under Reg 6.3 Note (i), ancillary area FSI up to 60% of the proposed FSI is permissible for residential use, and up to 80% for non-residential use.'
      },
      {
        'question': 'What is the statutory premium rate charged for Ancillary Area FSI in Municipal Councils and Regional Plan areas?',
        'options': [
          '5% of ASR land rate',
          '10% of ASR land rate',
          '15% of ASR land rate',
          '35% of ASR land rate'
        ],
        'answer': 1,
        'explanation': 'Under the tariff table in Reg 6.1.1, the premium rate for Municipal Councils, Nagar Panchayats and Regional Plan areas is strictly 10% of the unguided ASR land rate.'
      },
      {
        'question': 'Under Regulation 6.6, how are open balconies, double-height terraces, and cupboards treated during FSI scrutiny?',
        'options': [
          'They are fully exempt from FSI without any condition',
          'They are included in the floor-wise P-line and counted towards FSI',
          'They are counted at 50% of their actual area',
          'They are permitted only with Municipal Commissioner special waiver'
        ],
        'answer': 1,
        'explanation': 'Reg 6.6 explicitly dictates that open balconies, double height terraces, and cupboards shall be included in the P-line of the respective floor, irrespective of use/function.'
      },
      {
        'question': 'Which special scheme is explicitly EXCLUDED from availing Ancillary Area FSI under Note (i)?',
        'options': [
          'Transit Oriented Development (TOD)',
          'Pradhan Mantri Awas Yojana (PMAY)',
          'Rehabilitation component in SRA',
          'Integrated Township Projects (ITP)'
        ],
        'answer': 2,
        'explanation': 'The proviso to Note (i) states that ancillary area FSI applies to all other schemes like TOD, PMAY, ITP, IT, MHADA, etc., EXCEPT the rehabilitation component in SRA.'
      }
    ],

    'prev_url': '/lessons/reg-6-1-fsi-stacking-and-building-potential.html',
    'prev_title': 'Reg 6.1 & 6.3: FSI Stacking, Premium FSI & TDR Building Potential',
    'next_url': '/lessons/reg-6-2-front-setbacks-and-street-alignments.html',
    'next_title': 'Reg 6.1.1(ii) & 6.2.1: Front Road Setbacks & Street Alignments'
}
