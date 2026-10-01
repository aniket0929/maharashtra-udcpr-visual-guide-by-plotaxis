"""
UDCPR Chapter 14 - Lesson 14.5: Slum Rehabilitation Scheme (SRS)
Statutory Clauses: Regulations 14.6 & 14.7
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 14.6 & 14.7',
    'title': 'Slum Rehabilitation Schemes (SRS) - In-Situ & Slum TDR Economics',
    'meta_desc': 'Master UDCPR Regulations 14.6 & 14.7 for Slum Rehabilitation Schemes (SRS): 51% dweller consent, 27.88 sqm (300 sq.ft) free carpet rehab units, statutory incentive formula (1:R where R = 2.8 - 0.3n), high-density bonuses (+20% to +30%), Oct 2024 staircase caps (60%), and Slum TDR formula (X = Rg/Rr * Y).',
    'ch_slug': 'ch14',
    'ch_title': 'Chapter 14: Special Schemes',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'Urban Development Dept RoD Order dt. 11-Oct-2024 & Notification dt. 05-Dec-2023',
    'filename': 'reg-14-5-slum-rehabilitation-schemes.html',
    'lesson_id': 'ch14_lesson_5',
    'quiz_id': 'quiz_ch14_5',
    'prev_url': '/lessons/reg-14-4-heritage-conservation-and-tdr.html',
    'prev_title': 'Reg. 14.5 Heritage Conservation & Heritage TDR',
    'next_url': '/lessons/reg-14-6-urban-renewal-cluster-redevelopment.html',
    'next_title': 'Reg. 14.8 Urban Renewal Scheme (Cluster Redevelopment)',
    'lead_summary': (
        'To transform informal urban settlements into formal, resilient, dignified neighborhoods while eradicating sub-human living conditions, '
        'Regulations 14.6 and 14.7 establish Maharashtra\'s Slum Rehabilitation Scheme (SRS) framework across Pune, PCMC, Nagpur, and all other '
        'Municipal Corporations. Under SRS, eligible slum dwellers receive a free-of-cost, self-contained ownership apartment of 27.88 sq.m. '
        '(300 sq.ft.) carpet area in modern multi-storey buildings equipped with elevators, community halls, and balwadis. To make 100% free '
        'rehabilitation commercially viable for private developers, the state grants an incentive free-sale component governed by a precise '
        'statutory formula [1 : R = 2.8 - 0.3n] tied to Annual Statement of Rates (ASR), with density bonuses up to +30% and marketable Slum TDR '
        'for unconsumed floor space.'
    ),
    'plain_summary_html': """
      <p>
        Slum Rehabilitation Schemes replace haphazard shanties with engineered high-rises through cross-subsidization: the revenue from market-rate 
        apartments finances free homes and civil infrastructure for slum dwellers. Key statutory mechanics include:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Eligibility Cut-Off Dates (Reg 14.6.9):</strong>
          <br>&bull; <em>Protected Occupiers (Cut-off: 01-Jan-2000):</em> Inhabitants residing on or prior to 1st January 2000 are legally protected and receive a <strong>free-of-cost ownership tenement</strong> in-situ.
          <br>&bull; <em>Non-Protected Occupiers (Cut-off: 01-Jan-2011):</em> Inhabitants residing between 2000 and 1st January 2011 are eligible for rehabilitation on payment of subsidized construction cost.
          <br>&bull; <em>Post-2011 Inhabitants:</em> Ineligible under SRS, but may apply independently under PMAY.
        </li>
        <li><strong>Tenement Specifications &amp; Density (Reg 14.6.15):</strong>
          <br>&bull; <em>Rehab Unit Carpet Area:</em> Minimum <strong>27.88 sq.m. (300 sq.ft.)</strong> carpet area including self-contained bath and water closet.
          <br>&bull; <em>Minimum Tenement Density:</em> Mandatory <strong>450 Tenements / Hectare</strong> (relaxable to 360 T/Ha for severe site hardships). Maximum density capped at <strong>1,440 T/Ha</strong>.
          <br>&bull; <em>Mandatory Consent:</em> Developer or Society must submit proposals backed by registered consent of at least <strong>51% of eligible slum dwellers</strong>.
        </li>
        <li><strong>The Statutory Incentive Formula (Reg 14.6.16):</strong>
          <br>&bull; For every 1.0 sq.m. of rehab built-up area, the developer receives an incentive free-sale BUA ratio of <code>1 : R</code>:
          <br>&bull; <code>R = 2.8 - (n &times; 0.3)</code>, where <code>n = (Y / X) - 2</code>
          <br>&bull; <code>Y</code> = ASR Market Rate of Residential Flat per sq.m.; <code>X</code> = ASR Rate of Construction per sq.m.
          <br>&bull; The incentive ratio is bounded between a minimum of <strong>1 : 1.50</strong> and a maximum of <strong>1 : 3.00</strong>.
        </li>
        <li><strong>High-Density &amp; Cluster Bonuses:</strong>
          <br>&bull; <em>Density 650 to 850 T/Ha:</em> Additional <strong>+20% incentive</strong> on free sale component.
          <br>&bull; <em>Density &gt; 850 T/Ha:</em> Additional <strong>+30% incentive</strong> on free sale component.
          <br>&bull; <em>Cluster SRS (&ge; 1.0 Ha contiguous):</em> Additional <strong>+10% FSI</strong> on free sale component.
        </li>
        <li><strong>Slum TDR Generation &amp; 11-Oct-2024 RoD Cap:</strong>
          <br>&bull; Unconsumed FSI due to site geometry is released as Slum TDR using the indexation formula: <code>X = (Rg / Rr) &times; Y</code>.
          <br>&bull; <em>Oct 2024 Gazette RoD:</em> Staircase, lift, lobbies, and passages free of FSI are strictly capped at <strong>60% of rehab built-up area</strong>.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "14.6.15 DEVELOPMENT CONTROL REGULATIONS FOR S.R.S. - FSI that can be sanctioned on any slum site shall be 4.00 or sum total "
        "of rehabilitation component plus free sale component whichever is more with minimum rehabilitation tenement density of 450 T/Ha... "
        "14.6.16 Rehab : Incentive built up area shall be 1 : R, where R = [2.8 - (n x 0.3)] and n = (Y/X) - 2... "
        "Minimum and maximum ratio of incentive built up area shall be 1:1.50 and 3.0 respectively. Formula for Slum TDR: X = (Rg / Rr) x Y."
    ),
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:16px;">
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.6.15.7 // STAGED TDR RELEASE</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Four Milestone Gates</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Slum TDR is released strictly against physical progress: <strong>25% at Plinth CC</strong>, 
            <strong>35% at RCC &amp; Brickwork</strong>, <strong>30% at Rehab OC &amp; Society Registration</strong>, 
            and the final <strong>10% upon complete physical rehabilitation &amp; land conveyance</strong>.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--brick);">OCT 2024 GAZETTE // ROD AMENDMENT</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">60% Common Area Cap</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Per RoD Order dt. 11-Oct-2024, FSI exemption for staircases, lifts, lobbies, passages, and refuge areas in rehab towers 
            is capped at <strong>60% of rehab BUA</strong>. Any excess common area cannot generate incentive free-sale FSI.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.6.14 // TRANSIT CAMPS</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Temporary Accommodation</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            The developer must provide temporary transit tenements or pay monthly transit rent directly to eligible dwellers until 
            the rehabilitation tower receives full Occupation Certificate and keys are physically handed over.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="overflow-x:auto; margin-top:12px;">
        <div class="kicker" style="color:var(--blueprint); margin-bottom:6px;">REGULATION 14.6.16 // INCENTIVE RATIO &amp; DENSITY PLATES</div>
        <table class="blueprint-table" style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="background:var(--surface-tint); border-bottom:2px solid var(--line-bold);">
              <th style="padding:10px; text-align:left;">Settlement Density Tier</th>
              <th style="padding:10px; text-align:center;">Base Incentive Ratio (1 : R)</th>
              <th style="padding:10px; text-align:center;">Density Bonus</th>
              <th style="padding:10px; text-align:center;">Cluster Bonus (&ge;1.0 Ha)</th>
              <th style="padding:10px; text-align:left;">Minimum Carpet Mandate</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Standard Density</strong> (&le; 650 T/Ha)</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">Formula [2.8 - 0.3n] (Min 1.50 : Max 3.00)</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">0%</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">+10% Free Sale FSI</td>
              <td style="padding:10px;">27.88 sq.m. (300 sq.ft.)</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>High Density</strong> (650 to 850 T/Ha)</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">Formula [2.8 - 0.3n]</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--amber-dark); font-weight:700;">+20% Free Sale</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">+10% Free Sale FSI</td>
              <td style="padding:10px;">27.88 sq.m. (300 sq.ft.)</td>
            </tr>
            <tr style="border-bottom:2px solid var(--line-bold); background:var(--surface-tint);">
              <td style="padding:10px;"><strong>Extreme Density</strong> (&gt; 850 T/Ha)</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">Formula [2.8 - 0.3n]</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--brick); font-weight:700;">+30% Free Sale</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">+10% Free Sale FSI</td>
              <td style="padding:10px;">27.88 sq.m. (300 sq.ft.)</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div style="font-size:0.82rem; color:var(--ink-soft); margin-top:8px;">
        *Note: If local planning constraints limit in-situ consumption, the unconsumed balance generates Slum TDR under formula X = (Rg / Rr) &times; Y.
      </div>
    """,
    'worked_example_html': """
      <div style="line-height:1.6; font-size:0.92rem;">
        <h4 style="margin:0 0 8px 0; color:var(--amber-dark);">Scenario: Comprehensive SRS Free-Sale &amp; Slum TDR Calculation in Pune</h4>
        <p>
          A developer undertakes an in-situ Slum Rehabilitation Scheme in Pune SRA on a plot of <strong>10,000 sq.m. (1.0 Hectare)</strong>. 
          The slum accommodates <strong>500 eligible protected hutments</strong>. 
          The applicable ASR flat rate (<code>Y</code>) is <strong>&#8377;60,000 / sq.m.</strong>, and the ASR construction rate (<code>X</code>) is <strong>&#8377;20,000 / sq.m.</strong>
          Calculate the Rehab Component, Incentive Ratio, Free Sale Entitlement, and Slum TDR if only 3.50 FSI can be consumed on-site.
        </p>
        <div style="background:var(--surface); border:1px solid var(--line); padding:12px; margin:10px 0; font-family:var(--mono); font-size:0.85rem;">
          1. Rehabilitation Component (500 Tenements):<br>
          &nbsp;&nbsp;&bull; Carpet area per unit = 27.88 sq.m.<br>
          &nbsp;&nbsp;&bull; Total Carpet Area = 500 &times; 27.88 = 13,940 sq.m.<br>
          &nbsp;&nbsp;&bull; Rehab Built-Up Area (BUA at 1.25 multiplier) = 13,940 &times; 1.25 = <strong>17,425 sq.m.</strong><br><br>
          2. Incentive Ratio [1 : R] per Reg 14.6.16:<br>
          &nbsp;&nbsp;&bull; n = (Y / X) - 2 = (&#8377;60,000 / &#8377;20,000) - 2 = 3.0 - 2 = <strong>1.0</strong><br>
          &nbsp;&nbsp;&bull; R = [ 2.8 - (n &times; 0.3) ] = 2.8 - (1.0 &times; 0.3) = <strong>2.50</strong><br>
          &nbsp;&nbsp;&bull; Base Free Sale Incentive = 17,425 sq.m. &times; 2.50 = <strong>43,562.5 sq.m.</strong><br><br>
          3. Cluster Bonus (1.0 Ha Contiguous Land):<br>
          &nbsp;&nbsp;&bull; +10% Cluster Bonus on Free Sale = 43,562.5 &times; 10% = <strong>4,356.25 sq.m.</strong><br>
          &nbsp;&nbsp;&bull; Total Free Sale Entitlement = 43,562.5 + 4,356.25 = <strong>47,918.75 sq.m.</strong><br><br>
          4. Total Scheme Permissible BUA &amp; FSI:<br>
          &nbsp;&nbsp;&bull; Total Sanctioned BUA = 17,425 (Rehab) + 47,918.75 (Free Sale) = <strong>65,343.75 sq.m.</strong><br>
          &nbsp;&nbsp;&bull; Equivalent Scheme FSI on 10,000 sqm plot = 65,343.75 / 10,000 = <strong>6.534 FSI</strong><br><br>
          5. On-Site Consumption vs Slum TDR Generation:<br>
          &nbsp;&nbsp;&bull; Site height/setback restriction limits in-situ FSI consumption to <strong>3.50</strong>.<br>
          &nbsp;&nbsp;&bull; Maximum Consumed On-Site BUA = 10,000 &times; 3.50 = 35,000 sq.m.<br>
          &nbsp;&nbsp;&bull; In-situ Rehab BUA = 17,425 sq.m. &rarr; Balance on-site Free Sale = 35,000 - 17,425 = 17,575 sq.m.<br>
          &nbsp;&nbsp;&bull; <strong>Unconsumed Free Sale BUA = 47,918.75 - 17,575 = 30,343.75 sq.m.</strong><br><br>
          6. Slum TDR DRC Entitlement:<br>
          &nbsp;&nbsp;&bull; <strong>Slum TDR Issued = 30,343.75 sq.m. DRC</strong>, released in 4 milestones (25%, 35%, 30%, 10%)!
        </div>
        <p style="font-size:0.85rem; color:var(--ink-soft); margin:0;">
          <strong>Capital Yield:</strong> The developer constructs 500 free modern apartments for slum dwellers and monetizes 17,575 sq.m. on-site plus 30,343 sq.m. of tradable Slum TDR.
        </p>
      </div>
    """,
    'pitfalls_html': """
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 1: Proceeding Without 51% Registered Slum Dweller Consent</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Regulation 14.6.10 mandates a minimum of 51% registered consent from eligible hutment dwellers. Proposals submitted with fabricated or unverified consent forms are rejected and can lead to developer blacklisting by the SRA CEO.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 2: Violating the Oct-2024 60% Common Area Exemption Ceiling</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under the Removal of Difficulties (RoD) Order dt. 11-Oct-2024, common areas (staircase, lift lobbies, corridors) are exempt from FSI only up to 60% of rehab BUA. Designing 80% common circulation spaces will result in the excess 20% being deducted from the free-sale incentive component.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 3: Claiming Non-Protected Occupants as Free Allottees</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Only Protected Occupiers (residing on or before 1st Jan 2000) are entitled to free ownership tenements. Post-2000 up to 2011 dwellers must pay subsidized construction costs; counting them as free units distorts project cash flows.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.9rem; line-height:1.6; margin:0 0 10px 0;">
        <strong>Notification u/s 37(1AA)(c) dt. 5th December 2023:</strong> Overhauled Pune/PCMC SRS regulations, standardizing the incentive ratio formula and 
        integrating Slum TDR indexation.<br>
        <strong>Removal of Difficulties (RoD) Order dt. 11th October 2024:</strong> Capped FSI exemption for staircases, lifts, and lobbies at 60% of rehab BUA, 
        and clarified balcony computations across all ongoing SRS schemes without full OC.
      </p>
    """,
    'quiz': [
        {
            'question': 'What is the statutory cut-off date to qualify as a Protected Occupier entitled to a free tenement under Regulation 14.6.9?',
            'options': [
                '1st January 1995',
                '1st January 2000',
                '1st January 2011',
                '2nd December 2020'
            ],
            'answer': 1,
            'explanation': 'Regulation 14.6.9(1) defines Protected Occupiers as inhabitants residing on or before 1st January 2000, who are entitled to free in-situ ownership tenements.'
        },
        {
            'question': 'What is the statutory carpet area of a free rehabilitation tenement under Regulation 14.6 and 14.7?',
            'options': [
                '20.00 sq.m.',
                '25.00 sq.m.',
                '27.88 sq.m. (300 sq.ft.)',
                '35.00 sq.m.'
            ],
            'answer': 2,
            'explanation': 'Under Regulations 14.6 and 14.7, rehabilitation tenements are mandated to have a minimum carpet area of 27.88 sq.m. (300 sq.ft.).'
        },
        {
            'question': 'What is the minimum percentage of consent required from slum dwellers to initiate an SRS proposal under Regulation 14.6.10?',
            'options': [
                '33%',
                '51%',
                '70%',
                '100%'
            ],
            'answer': 1,
            'explanation': 'Regulation 14.6.10 mandates that a Registered Developer or Society must submit the scheme with the consent of at least 51% of the slum dwellers.'
        },
        {
            'question': 'Under the 11th October 2024 RoD Order, what is the maximum permissible FSI exemption cap for staircases, lifts, and lobbies in rehab buildings?',
            'options': [
                '30% of rehab BUA',
                '40% of rehab BUA',
                '60% of rehab BUA',
                '100% full exemption without limits'
            ],
            'answer': 2,
            'explanation': 'The RoD Order dt. 11th October 2024 strictly restricts FSI exemption of staircase, lift, lobbies, machine rooms, and passages to 60% of the built-up area of the rehabilitation component.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
