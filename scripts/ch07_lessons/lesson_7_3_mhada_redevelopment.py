"""
UDCPR FROM SCRATCH - CHAPTER 7, LESSON 3
Module: scripts/ch07_lessons/lesson_7_3_mhada_redevelopment.py
Statutory Anchor: Regulation 7.4 (Tables 7-B, 7-C, 7-D & 7-E)
Content: Redevelopment of MHADA Housing Schemes, Rehabilitation Entitlements, Basic Ratio Math, and 51% Consent Rules
"""

lesson_data = {
    'filename': 'reg-7-4-mhada-housing-redevelopment.html',
    'lesson_id': '7.3',
    'quiz_id': 'quiz-7-3',
    'clause': 'Regulation 7.4',
    'title': 'Redevelopment of MHADA Housing Schemes (Reg. 7.4)',
    'badge_status': 'CORE STATUTORY SPECIFICATION',
    'ch_slug': 'ch07',
    'ch_title': 'Chapter 7: Higher FSI for Certain Uses',
    'meta_desc': 'Complete architectural and legal guide to MHADA colony redevelopment under UDCPR Reg 7.4: 3.00 FSI on gross plot, carpet + 35% rehab formula, Table 7-B plot bonuses, Basic Ratio LR/RC sharing, and 51% member consent.',
    'lead_summary': 'Demystify Maharashtra’s most prolific urban renewal framework: how aging MHADA colonies unlock 3.00 gross FSI, compute member carpet entitlements with plot-size bonuses, share incentive FSI via LR/RC ratios, and legally bind non-cooperating members with 51% consent.',
    'amendment_cite': 'UDCPR-2020 Reg 7.4, Notification No. CR 236/18 Part-3 dt. 16th June 2021',

    'plain_summary_html': r"""
      <p>
        Tens of thousands of families across Maharashtra reside in aging housing colonies developed by the <strong>Maharashtra Housing and Area Development Authority (MHADA)</strong>. Under <strong>Regulation 7.4</strong>, the State offers an expansive statutory framework to redevelop these low-density, deteriorating colonies into modern high-rises with a blanket <strong>3.00 FSI on the gross layout area</strong>.
      </p>
      <p>
        For existing residents, redevelopment guarantees a massive upgrade under the <strong>Rehabilitation Area Entitlement formula</strong>:
      </p>
      <div style="background:var(--paper-raised); border-left:4px solid var(--blueprint); padding:12px; margin:14px 0; font-family:var(--mono);">
        $$\text{Rehab Carpet Area} = (\text{Existing Carpet Area} + 35\%) + \text{Table 7-B Plot Bonus (up to 45\%)}$$
        $$\text{Statutory Floor: Minimum Carpet Area} = \mathbf{35.0\text{ sq.m}}\text{ (exclusive of balcony!)}$$
      </div>
      <p>
        To make the project financially feasible, developers receive <strong>Incentive FSI</strong> (40% to 70%) calculated from the <strong>Basic Ratio</strong> ($LR / RC$ = Land Rate divided by Construction Rate from ASR). Any surplus balance FSI is shared between the society and MHADA under Table 7-D.
      </p>
      <p>
        Crucially, under <strong>Regulation 7.4.8</strong>, the scheme requires the written consent of only <strong>51% of members</strong>. Once 51% approve, it becomes legally mandatory for 100% of occupants to vacate, with non-cooperating members subject to summary eviction under the MHADA Act!
      </p>
    """,

    'statutory_extract': """
### 7.4 DEVELOPMENT / REDEVELOPMENT OF HOUSING SCHEMES OF MHADA
7.4.1 ii) For redevelopment of existing housing schemes of MHADA... the total permissible FSI shall be 3.00 on the gross plot area.

7.4.2 i) Rehabilitation Area Entitlement:
a) Basic entitlement equivalent to carpet area of existing tenement plus 35% thereof, subject to a minimum carpet area of 35 sq.m.
b) Additional entitlement governed by the size of the plot under Table 7-B:
- Upto 4000 sq.m.: Nil
- Above 4000 sq.m. to 2.0 hect.: 15%
- Above 2.0 hect. to 5.0 hect.: 25%
- Above 5 hect. to 10 hect.: 35%
- Above 10 hect.: 45%

7.4.2 ii) Incentive FSI (Table 7-C): Based on Basic Ratio (LR / RC):
- Above 6.00: 40% incentive
- Above 4.00 and up to 6.00: 50% incentive
- Above 2.00 and up to 4.00: 60% incentive
- Up to 2.00: 70% incentive

7.4.6 i) Infrastructure Charge: Rate of 7% of Land Rate as per ASR chargeable for extra FSI granted over basic FSI. 50% transferred to Authority for offsite infrastructure.
7.4.8 i) Consent Threshold: With consent of 51% of members and alternative accommodation provided, it shall be obligatory for all occupiers/members to participate and vacate.
7.4.9 Corpus Fund: Created by developer for 10-year building maintenance.
    """,

    'clause_cards_html': r"""
      <div class="card-grid">
        <div class="card">
          <span class="kicker-card">MEMBER ENTITLEMENT</span>
          <h3 class="card-title">Carpet + 35% (Min 35 sq.m)</h3>
          <p class="card-body">
            Every existing resident is guaranteed their current carpet area plus <strong>35% extra area</strong>, with an absolute statutory minimum of <strong>35.0 sq.m (376.7 sq.ft)</strong>. Balconies cannot be deducted from this entitlement.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">LARGE LAYOUT BONUS</span>
          <h3 class="card-title">Table 7-B Plot Incentives</h3>
          <p class="card-body">
            Consolidating large layouts brings massive bonuses:<br>
            • 4,000 sqm to 2.0 Ha: <strong>+15%</strong> extra carpet.<br>
            • 2.0 Ha to 5.0 Ha: <strong>+25%</strong> extra carpet.<br>
            • 5.0 Ha to 10.0 Ha: <strong>+35%</strong> extra carpet.<br>
            • Above 10.0 Ha: <strong>+45%</strong> extra carpet!
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">FINANCIAL MECHANICS</span>
          <h3 class="card-title">Basic Ratio ($LR / RC$)</h3>
          <p class="card-body">
            Incentive FSI is linked to market economics: dividing ASR Land Rate ($LR$) by ASR Construction Rate ($RC$). In lower-value land markets ($LR/RC \le 2$), developers get <strong>70% incentive FSI</strong> to ensure project feasibility.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">LEGAL ENFORCEMENT</span>
          <h3 class="card-title">51% Consent Eviction Power</h3>
          <p class="card-body">
            Under Reg 7.4.8, once <strong>51% of society members</strong> execute the redevelopment NOC and alternative transit accommodation is arranged, holdout members lose injunction rights and face summary eviction under the MHADA Act.
          </p>
        </div>
      </div>
    """,

    'plate_or_table_html': """
      <div class="table-container">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>Basic Ratio ($LR / RC$)</th>
              <th>Market Characteristic</th>
              <th>Incentive FSI (% of Rehab Area)</th>
              <th>Sharing of Balance FSI (Society : MHADA)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Above 6.00</strong></td>
              <td>Prime Metro City Core (High Land Value)</td>
              <td><strong>40%</strong></td>
              <td><strong>30% Society : 70% MHADA</strong></td>
            </tr>
            <tr>
              <td><strong>Above 4.00 to 6.00</strong></td>
              <td>Established Urban Suburbs</td>
              <td><strong>50%</strong></td>
              <td><strong>35% Society : 65% MHADA</strong></td>
            </tr>
            <tr>
              <td><strong>Above 2.00 to 4.00</strong></td>
              <td>Emerging Developing Peripheral Belts</td>
              <td><strong>60%</strong></td>
              <td><strong>40% Society : 60% MHADA</strong></td>
            </tr>
            <tr>
              <td><strong>Up to 2.00</strong></td>
              <td>Tier-2/3 Towns (High Construction Cost relative to Land)</td>
              <td><strong>70%</strong></td>
              <td><strong>45% Society : 55% MHADA</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
      <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft); margin-top:8px;">
        * Note: For plots up to 4,000 sq.m, MHADA may convert its BUA share into premium as per Table 7-E (20% to 71% of ASR).
      </div>
    """,

    'worked_example_html': r"""
      <div class="math-box">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:12px; color:var(--ink);">
          Worked Case: MHADA Colony Redevelopment & Member Carpet Allocation
        </h4>
        <p><strong>Baseline Scenario:</strong></p>
        <ul>
          <li>MHADA Colony Layout Area = <strong>15,000 sq.m (1.50 Hectares)</strong> in Nagpur.</li>
          <li>Existing Society: 100 members occupying 100 tenements of <strong>25 sq.m carpet area</strong> each.</li>
          <li>ASR Land Rate ($LR$) = Rs 18,000 / sq.m; ASR Construction Rate ($RC$) = Rs 6,000 / sq.m.</li>
          <li>Basic Ratio $= LR / RC = 18,000 / 6,000 = \mathbf{3.00}$ (falls in 2.00 to 4.00 bracket).</li>
        </ul>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint); padding-left: 14px;">
          <p><strong>Step 1: Compute Member Carpet Area Entitlement</strong></p>
          <p>• Basic Entitlement $= \text{Carpet} + 35\% = 25 \times 1.35 = 33.75\text{ sq.m}$.</p>
          <p>• Statutory Minimum Check: Minimum is <strong>35.0 sq.m</strong> &rarr; Entitlement rises to 35.0 sq.m.</p>
          <p>• Table 7-B Plot Bonus for 1.5 Ha (falls in 4,000 sqm to 2.0 Ha tier) $= \mathbf{+15\%}$ of existing carpet:
            $$\text{Plot Bonus} = 25\text{ sq.m} \times 15\% = \mathbf{3.75\text{ sq.m}}$$
            $$\text{Final Guaranteed Carpet per Member} = 35.0 + 3.75 = \mathbf{38.75\text{ sq.m (417.1 sq.ft)}}$$
          </p>
          <p>Each member receives an instant <strong>55% increase</strong> in living space completely free of cost!</p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--amber); padding-left: 14px;">
          <p><strong>Step 2: Calculate Total Gross Permissible BUA (3.00 FSI)</strong></p>
          <p>Under Reg 7.4.1(ii), permissible FSI on gross plot is 3.00:
            $$\text{Total Layout BUA} = 15,000\text{ sq.m} \times 3.00 = \mathbf{45,000\text{ sq.m}}$$
            $$\text{Rehab BUA for 100 Members (with circulation factor 1.25)} = 100 \times (38.75 \times 1.25) \approx \mathbf{4,844\text{ sq.m}}$$
          </p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint-soft); padding-left: 14px;">
          <p><strong>Step 3: Incentive FSI for Developer (Table 7-C)</strong></p>
          <p>For Basic Ratio 3.00, Table 7-C allows <strong>60% incentive FSI</strong> on the rehab component:
            $$\text{Developer Incentive BUA} = 4,844\text{ sq.m} \times 60\% = \mathbf{2,906\text{ sq.m}}$$
            $$\text{Total Rehab + Incentive BUA} = 4,844 + 2,906 = \mathbf{7,750\text{ sq.m}}$$
          </p>
          <p>Surplus Balance BUA $= 45,000 - 7,750 = \mathbf{37,250\text{ sq.m}}$ shared 40% Society (14,900 sqm) : 60% MHADA (22,350 sqm)!</p>
        </div>
      </div>
    """,

    'pitfalls_html': """
      <div class="panel-alert">
        <h4 style="font-family:var(--disp); font-weight:700; color:var(--brick); margin-bottom:8px;">
          CRITICAL RISK FACTORS IN MHADA REDEVELOPMENT PROJECTS
        </h4>
        <ul style="margin-left: 18px; line-height: 1.6;">
          <li>
            <strong>Deducting Balcony Area from 35 sq.m Minimum:</strong> The proviso to Reg 7.4.2(i) explicitly mandates that the 35 sq.m minimum carpet entitlement is <em>exclusive of balcony</em>. Enclosing balconies to meet the 35 sq.m threshold violates the regulation.
          </li>
          <li>
            <strong>Failing to Escrow the 10-Year Maintenance Corpus:</strong> Reg 7.4.9 requires a developer-funded corpus fund for 10 years of post-handover maintenance. Failure to deposit this fund blocks final Occupancy Certificates.
          </li>
          <li>
            <strong>Overlooking the 7% ASR Infrastructure Charge:</strong> Under Reg 7.4.6, extra FSI beyond the basic potential incurs an infrastructure fee of <strong>7% of the ASR land rate</strong>, split 50:50 between MHADA and the municipal corporation.
          </li>
          <li>
            <strong>Miscalculating Multi-Zone Land Rates:</strong> If a large MHADA layout spans multiple ASR survey numbers with differing land values, you must compute a <em>weighted average land rate</em> to determine the Basic Ratio.
          </li>
        </ul>
      </div>
    """,

    'amendment_section_html': """
      <div class="panel-info">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:8px;">Statutory Amendments</h4>
        <ul style="font-size:0.92rem; line-height:1.6; margin-left:18px;">
          <li><strong>Notification CR 236/18 Part-3 (dt. 16 June 2021):</strong> Fixed permissible FSI for MHADA colony redevelopment at a blanket 3.00 on the gross plot area across all municipal corporation regions.</li>
          <li><strong>MHADA Act Amendment (2022):</strong> Codified the binding nature of 51% member consent and authorized summary eviction procedures for uncooperative occupants.</li>
        </ul>
      </div>
    """,

    'quiz': [
      {
        'question': 'Under Regulation 7.4.2(i)(a), what is the statutory minimum carpet area guaranteed to an existing MHADA tenement in a redevelopment scheme?',
        'options': [
          '25.0 sq.m',
          '27.87 sq.m',
          '35.0 sq.m (exclusive of balcony)',
          '50.0 sq.m'
        ],
        'answer': 2,
        'explanation': 'Regulation 7.4.2(i)(a) mandates a basic entitlement of existing carpet plus 35% thereof, subject to an absolute minimum carpet area of 35 sq.m exclusive of balcony.'
      },
      {
        'question': 'What is the member consent threshold required to sanction an additional FSI redevelopment scheme under Regulation 7.4.8(i)?',
        'options': [
          '51% of members',
          '66% of members',
          '75% of members',
          '100% unanimous consent'
        ],
        'answer': 0,
        'explanation': 'Regulation 7.4.8(i) explicitly establishes that obtaining No Objection Certificate from MHADA requires the consent of 51% of its members.'
      },
      {
        'question': 'How is the Incentive FSI percentage for a MHADA redevelopment project determined under Table 7-C?',
        'options': [
          'Fixed at 50% for all buildings',
          'Based on the Basic Ratio (Land Rate LR / Construction Rate RC)',
          'Determined solely by the building height',
          'Decided by the Municipal Commissioner'
        ],
        'answer': 1,
        'explanation': 'Under Table 7-C, incentive FSI ranges from 40% to 70% based on the Basic Ratio of Land Rate (LR) to Rate of Construction (RC) from the ASR.'
      },
      {
        'question': 'What infrastructure charge is levied on extra FSI granted over basic FSI in MHADA redevelopment under Regulation 7.4.6?',
        'options': [
          '2% of construction cost',
          '7% of the Land Rate as per ASR (shared 50:50 with Authority)',
          '15% of the ready reckoner rate',
          'Zero charge'
        ],
        'answer': 1,
        'explanation': 'Reg 7.4.6(i) mandates an infrastructure charge of 7% of the Land Rate as per ASR, with 50% transferred to the local Authority for off-site infrastructure.'
      }
    ],

    'prev_url': '/lessons/reg-7-2-road-widening-and-staff-quarters.html',
    'prev_title': 'Reg 7.2 & 7.3: Road Widening Surrender & Staff Quarters FSI',
    'next_url': '/lessons/reg-7-6-old-dilapidated-and-housing-societies.html',
    'next_title': 'Reg 7.5 & 7.6: Redevelopment of 30-Year-Old Societies & Dilapidated Buildings'
}
