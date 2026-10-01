"""
UDCPR Chapter 14 - Lesson 14.2: Transit Oriented Development (TOD)
Statutory Clauses: Regulation 14.2 (14.2.1 to 14.2.5)
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 14.2 (14.2.1 to 14.2.5)',
    'title': 'Transit Oriented Development (TOD) - Metro & BRT Corridor Densification',
    'meta_desc': 'Master UDCPR Regulation 14.2 for Transit Oriented Development (TOD): 500m Metro station influence zone, road-based FSI scaling up to 4.00, 50% premium revenue sharing to Metro SPV, 1/4th TDR loading ratio, 50% parking reduction, and 200m public parking incentives.',
    'ch_slug': 'ch14',
    'ch_title': 'Chapter 14: Special Schemes',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'UDD Notification No. CR.158/19 (10-Oct-2022) & No. CR.105/2022 (05-Sep-2024)',
    'filename': 'reg-14-2-transit-oriented-development.html',
    'lesson_id': 'ch14_lesson_2',
    'quiz_id': 'quiz_ch14_2',
    'prev_url': '/lessons/reg-14-1-integrated-township-projects.html',
    'prev_title': 'Reg. 14.1 Integrated Township Projects (ITP)',
    'next_url': '/lessons/reg-14-3-affordable-housing-and-pmay.html',
    'next_title': 'Reg. 14.3 & 14.4 Affordable Housing Scheme & PMAY',
    'lead_summary': (
        'To curb vehicular congestion, combat carbon emissions, and promote mass public rapid transit, Regulation 14.2 establishes '
        'the Transit Oriented Development (TOD) framework across Maharashtra. Centered around a statutory 500-meter buffer from mass '
        'transit stations (Pune Metro, Nagpur Metro, PCMC BRT), TOD permits vertical densification with total permissible FSI up to 4.00. '
        'To ensure financial sustainability of mega-transit infrastructure, additional FSI is unlocked via premium payments split evenly '
        '(50:50) between the local municipal authority and the Metro Rail Corporation. Crucially, TOD mandates compact living by requiring '
        '50% of residential FSI to be dedicated to small tenements (<=60 sqm) and slashes mandatory parking norms by 50% to actively '
        'discourage private automobile reliance.'
    ),
    'plain_summary_html': """
      <p>
        Transit Oriented Development (TOD) reimagines urban planning by placing high-density, mixed-use living directly within walking distance 
        of rapid mass transit stations. Instead of pushing growth to the fringes, Regulation 14.2 channels floor space along transit spines:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>TOD Zone Delineation (Reg 14.2.1.1):</strong>
          <br>&bull; <em>Standard Buffer:</em> Defined as the area within a <strong>500-meter radius</strong> measured from the boundary of the proposed or operational Metro station.
          <br>&bull; <em>Amenity Expansion:</em> Where reservations or amenity spaces are utilized for transit infrastructure, this boundary can be relaxed outward by up to <strong>30%</strong>.
          <br>&bull; <em>PCMC BRT Corridors (Reg 14.2.5):</em> Extends <strong>100 meters</strong> on either side from the center line of notified BRT routes.
        </li>
        <li><strong>Road-Width Dependent FSI Tiers (Reg 14.2.1.2):</strong> Maximum total permissible FSI scales strictly with fronting road width:
          <br>&bull; <em>9.0m to &lt;12.0m:</em> Max FSI <strong>2.50</strong>
          <br>&bull; <em>12.0m to &lt;15.0m:</em> Max FSI <strong>3.00</strong>
          <br>&bull; <em>15.0m to &lt;24.0m:</em> Max FSI <strong>3.50</strong>
          <br>&bull; <em>24.0m and above:</em> Max FSI <strong>4.00</strong>
        </li>
        <li><strong>Equal Premium Revenue Sharing (Reg 14.2.1.2.1):</strong>
          <br>&bull; Premium is charged at <strong>30% of ASR land rate</strong> for tenements &le; 60 sq.m. carpet area.
          <br>&bull; Premium is charged at <strong>35% of ASR land rate</strong> for tenements &gt; 60 sq.m. and commercial built-up area.
          <br>&bull; <strong>50%</strong> of the collected premium is transferred to the Planning Authority / Government, and <strong>50%</strong> is directly remitted to the Project Implementing Authority (e.g., MahaMetro SPV) for capital expenditure.
        </li>
        <li><strong>Split Plot Rules (Reg 14.2.1.2.4):</strong>
          <br>&bull; <em>&ge; 50% plot area inside TOD:</em> The <strong>entire plot</strong> qualifies for TOD FSI and regulations.
          <br>&bull; <em>&lt; 50% plot area inside TOD:</em> TOD FSI applies strictly to the portion inside the TOD zone; the outer portion follows standard Chapter 6 base rules.
          <br>&bull; <em>Marginal overlap (&lt; 10% or &lt; 500 sqm):</em> Landowner has the legal option to opt in or out of TOD.
        </li>
        <li><strong>Compact Housing &amp; Parking Halving (Reg 14.2.1.3 &amp; 14.2.1.6):</strong>
          <br>&bull; Tenement carpet areas must be between <strong>25 sq.m. and 120 sq.m.</strong>
          <br>&bull; At least <strong>50% of residential FSI</strong> must be consumed by compact flats of <strong>&le; 60 sq.m. carpet area</strong>.
          <br>&bull; Statutory vehicle parking requirements under UDCPR Chapter 10 are slashed by <strong>50%</strong>. No on-street parking is permitted.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "14.2 TRANSIT ORIENTED DEVELOPMENT (TOD) - Maximum Permissible FSI: The maximum permissible total FSI in TOD zone shall be 4.00 "
        "including base permissible FSI... Rate of premium shall be 30% for tenements equal to or less than 60 sq.m. and 35% for remaining FSI... "
        "50% of premium collected should be paid to Planning Authority and remaining 50% to Project Implementing Authority. Parking provisions "
        "in TOD Zone shall be at 50% of those mentioned in UDCPR."
    ),
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:16px;">
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.2.1.2 // FSI &amp; TDR RATIO</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">1/4th TDR Loading Rule</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Additional potential above base FSI must be consumed in a statutory ratio: <strong>1/4th (25%) via TDR</strong> and 
            <strong>3/4th (75%) via Premium FSI</strong> at every step. If TDR is unavailable locally, the Municipal Commissioner 
            may permit 100% premium consumption, compensating the Metro SPV accordingly.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.2.1.6.1 // 200M RADIUS</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Public Parking Bonus</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Plots within <strong>200 meters</strong> of a Metro station providing public parking handed over free to the ULB enjoy 
            two benefits: the parking built-up area is <strong>100% FSI-free</strong>, and the overall premium payable on additional FSI is 
            <strong>discounted by 50% of that parking area</strong>.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.2.1.4 // MIXED USES</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Commercial &amp; IT Integration</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Mixed residential-commercial use is permitted on residential plots fronting roads of <strong>12.0m or more</strong>. 
            Standalone office towers, mercantile centers, hotels, hospitals, and IT buildings are permissible on independent plots.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="overflow-x:auto; margin-top:12px;">
        <table class="blueprint-table" style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="background:var(--surface-tint); border-bottom:2px solid var(--line-bold);">
              <th style="padding:10px; text-align:left;">Road Width Frontage</th>
              <th style="padding:10px; text-align:center;">Max Total FSI</th>
              <th style="padding:10px; text-align:left;">Tenement Premium (&le;60 sqm)</th>
              <th style="padding:10px; text-align:left;">Commercial / Other Premium</th>
              <th style="padding:10px; text-align:left;">Parking Mandate</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>9.0m to &lt; 12.0m</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint);">2.50</td>
              <td style="padding:10px; font-family:var(--mono);">30% of ASR Land Rate</td>
              <td style="padding:10px; font-family:var(--mono);">35% of ASR Land Rate</td>
              <td style="padding:10px;">50% of Chapter 10 Norms</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>12.0m to &lt; 15.0m</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint);">3.00</td>
              <td style="padding:10px; font-family:var(--mono);">30% of ASR Land Rate</td>
              <td style="padding:10px; font-family:var(--mono);">35% of ASR Land Rate</td>
              <td style="padding:10px;">50% of Chapter 10 Norms</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>15.0m to &lt; 24.0m</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint);">3.50</td>
              <td style="padding:10px; font-family:var(--mono);">30% of ASR Land Rate</td>
              <td style="padding:10px; font-family:var(--mono);">35% of ASR Land Rate</td>
              <td style="padding:10px;">50% of Chapter 10 Norms</td>
            </tr>
            <tr style="border-bottom:2px solid var(--line-bold); background:var(--surface-tint);">
              <td style="padding:10px;"><strong>24.0m and Above</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint); font-size:1.05rem;">4.00</td>
              <td style="padding:10px; font-family:var(--mono);">30% of ASR Land Rate</td>
              <td style="padding:10px; font-family:var(--mono);">35% of ASR Land Rate</td>
              <td style="padding:10px;">50% of Chapter 10 Norms</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div style="font-size:0.82rem; color:var(--ink-soft); margin-top:8px;">
        *Note: Premium revenue collected is statutorily split 50:50 between the Local Planning Authority and the Metro SPV. Ancillary BUA per Reg 6.6 applies on top of this FSI.
      </div>
    """,
    'worked_example_html': """
      <div style="line-height:1.6; font-size:0.92rem;">
        <h4 style="margin:0 0 8px 0; color:var(--amber-dark);">Scenario: High-Density Mixed Development near Pune Metro Station</h4>
        <p>
          A developer owns a contiguous plot of <strong>2,000 sq.m.</strong> located entirely within <strong>350 meters</strong> of an operational Pune Metro Station. 
          The plot abuts a <strong>24.0-meter wide DP Road</strong>. The Annual Statement of Rates (ASR) land rate is <strong>&#8377;40,000 / sq.m.</strong>
          Calculate the maximum permissible BUA, the additional FSI components, and the premium payable.
        </p>
        <div style="background:var(--surface); border:1px solid var(--line); padding:12px; margin:10px 0; font-family:var(--mono); font-size:0.85rem;">
          1. Road Width &amp; Max Permissible FSI:<br>
          &nbsp;&nbsp;&bull; Road width &ge; 24.0m &rarr; Max Permissible FSI = <strong>4.00</strong><br>
          &nbsp;&nbsp;&bull; Total Gross Potential = 2,000 sq.m. &times; 4.00 = <strong>8,000 sq.m. BUA</strong><br><br>
          2. Base FSI vs Additional Potential:<br>
          &nbsp;&nbsp;&bull; Base Permissible FSI (Zone R-2) = 1.10 &rarr; Base BUA = 2,000 &times; 1.10 = 2,200 sq.m.<br>
          &nbsp;&nbsp;&bull; Additional TOD Potential = 8,000 - 2,200 = <strong>5,800 sq.m.</strong><br><br>
          3. TDR vs Premium FSI Split (Reg 14.2.1.2.4):<br>
          &nbsp;&nbsp;&bull; Mandatory TDR share (1/4th) = 5,800 &times; 0.25 = <strong>1,450 sq.m. TDR</strong><br>
          &nbsp;&nbsp;&bull; Premium FSI share (3/4th) = 5,800 &times; 0.75 = <strong>4,350 sq.m. Premium FSI</strong><br><br>
          4. Tenement Size Distribution (Reg 14.2.1.3):<br>
          &nbsp;&nbsp;&bull; At least 50% of Premium FSI for &le;60 sqm flats: 4,350 &times; 50% = 2,175 sq.m.<br>
          &nbsp;&nbsp;&bull; Balance Premium FSI (&gt;60 sqm or Commercial): 4,350 &times; 50% = 2,175 sq.m.<br><br>
          5. Premium Calculation (Reg 14.2.1.2.1):<br>
          &nbsp;&nbsp;&bull; Premium on &le;60 sqm: 2,175 sq.m. &times; (30% &times; &#8377;40,000) = 2,175 &times; &#8377;12,000 = &#8377;2,61,00,000<br>
          &nbsp;&nbsp;&bull; Premium on &gt;60 sqm: 2,175 sq.m. &times; (35% &times; &#8377;40,000) = 2,175 &times; &#8377;14,000 = &#8377;3,04,50,000<br>
          &nbsp;&nbsp;&bull; Total Premium Payable = &#8377;2.61 Cr + &#8377;3.045 Cr = <strong>&#8377;5,65,50,000 (&#8377;5.655 Cr)</strong><br><br>
          6. Revenue Split Disbursement:<br>
          &nbsp;&nbsp;&bull; Share to Pune Municipal Corporation (50%) = <strong>&#8377;2,82,75,000</strong><br>
          &nbsp;&nbsp;&bull; Share to MahaMetro SPV (50%) = <strong>&#8377;2,82,75,000</strong>
        </div>
        <p style="font-size:0.85rem; color:var(--ink-soft); margin:0;">
          <strong>Design Audit:</strong> Statutory parking spaces required under Chapter 10 are halved (50%), and 50% of all residential flats must have carpet areas &le;60 sq.m.
        </p>
      </div>
    """,
    'pitfalls_html': """
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 1: Assuming 4.00 FSI is Available on Narrow Roads</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          FSI 4.00 is strictly reserved for roads of <strong>24.0 meters and above</strong>. A plot on an 11-meter road is capped at <strong>2.50 FSI</strong>, even if it is directly adjacent to the Metro Station gate.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 2: Neglecting the 50% Compact Tenement Rule</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under Reg 14.2.1.3, at least 50% of residential FSI must comprise units of &le;60 sq.m. carpet area. Designing exclusively 3BHK/4BHK luxury units (>120 sqm) violates TOD bylaws and will lead to plan rejection during scrutiny.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 3: Failing to Remit 50% to Metro Implementing SPV</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          The premium challan is legally split into two separate escrow accounts: 50% to the ULB and 50% directly to MahaMetro / Project Implementing Authority. Challans paying 100% to municipal revenue will block the issuance of the Commencement Certificate.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.9rem; line-height:1.6; margin:0 0 10px 0;">
        <strong>Notification u/s 37(1AA)(c) dt. 10th October 2022:</strong> Fully replaced Regulation 14.2.1 for PMC, clarifying the 1/4th TDR loading ratio, 
        introducing the 50:50 premium split with MahaMetro, and capping tenement sizes at 120 sq.m.<br>
        <strong>Government Order dt. 28th August 2023:</strong> Clarified the split-plot rule: where less than 50% falls in TOD, only that part enjoys TOD FSI, 
        while the remainder utilizes standard DCPR FSI.<br>
        <strong>Notification dt. 5th September 2024:</strong> Mandated complete pedestrianisation street designs within the TOD zone within 1 year.
      </p>
    """,
    'quiz': [
        {
            'question': 'What is the standard radius around a Metro station boundary that defines the TOD Zone?',
            'options': [
                '200 meters',
                '300 meters',
                '500 meters',
                '1,000 meters'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.2.1.1(i) defines the TOD zone as the area 500 meters around the proposed Metro station boundary.'
        },
        {
            'question': 'What is the maximum permissible total FSI for a plot in a TOD zone abutting a 24.0m or wider road?',
            'options': [
                '2.50 FSI',
                '3.00 FSI',
                '3.50 FSI',
                '4.00 FSI'
            ],
            'answer': 3,
            'explanation': 'Under Regulation 14.2.1.2, road widths of 24.0m and above qualify for the ceiling FSI of 4.00.'
        },
        {
            'question': 'How is the TOD additional FSI premium shared under Regulation 14.2.1.2.1?',
            'options': [
                '100% goes to the Municipal Corporation',
                '75% to Municipal Corporation, 25% to State Government',
                '50% to Planning Authority, 50% to Metro Project Implementing Authority',
                '100% to Metro Project Implementing Authority'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.2.1.2.1 mandates that 50% of the premium collected goes to the Planning Authority and 50% to the Project Implementing Authority.'
        },
        {
            'question': 'How are statutory vehicle parking requirements modified in the TOD Zone under Regulation 14.2.1.6?',
            'options': [
                'Increased by 50% to cater to density',
                'Reduced to 50% of standard UDCPR requirements',
                'Completely exempted (0 parking required)',
                'Unchanged from standard UDCPR norms'
            ],
            'answer': 1,
            'explanation': 'Regulation 14.2.1.6 states: "Parking provisions in the TOD Zone shall be at 50% of those as mentioned in UDCPR" to discourage private vehicle ownership.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
