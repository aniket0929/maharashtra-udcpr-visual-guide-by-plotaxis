"""
UDCPR Chapter 14 - Lesson 14.3: Affordable Housing Scheme (AHS) & Pradhan Mantri Awas Yojana (PMAY)
Statutory Clauses: Regulations 14.3 & 14.4 (Tables 14-S, 14-T)
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 14.3 & 14.4 (Tables 14-S, 14-T)',
    'title': 'Affordable Housing Scheme (AHS) & Pradhan Mantri Awas Yojana (PMAY)',
    'meta_desc': 'Master UDCPR Regulations 14.3 & 14.4: 4,000 sqm min plot, 18m road frontage, 3.00 gross FSI, 1:3 land pocket partition (25% Affordable vs 75% Free Sale), 27.88 sqm unit caps, Table 14-S staged FSI release, off-site infrastructure charges, and PMAY up to 2.50 FSI without premium or TDR.',
    'ch_slug': 'ch14',
    'ch_title': 'Chapter 14: Special Schemes',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'UDD Corrigendum No. CR.121/21 dt. 02-Dec-2021 & Clarification dt. 23-Dec-2021',
    'filename': 'reg-14-3-affordable-housing-and-pmay.html',
    'lesson_id': 'ch14_lesson_3',
    'quiz_id': 'quiz_ch14_3',
    'prev_url': '/lessons/reg-14-2-transit-oriented-development.html',
    'prev_title': 'Reg. 14.2 Transit Oriented Development (TOD)',
    'next_url': '/lessons/reg-14-4-heritage-conservation-and-tdr.html',
    'next_title': 'Reg. 14.5 Heritage Conservation & Heritage TDR',
    'lead_summary': (
        'To address the severe urban housing deficit for Economically Weaker Sections (EWS) and Lower Income Groups (LIG), '
        'Regulations 14.3 and 14.4 establish Maharashtra\'s statutory mass-housing incentive mechanisms: the Affordable Housing Scheme (AHS) '
        'and the Pradhan Mantri Awas Yojana (PMAY). Under AHS, private developers possessing at least 4,000 sq.m. of contiguous land fronting '
        'an 18.0-meter road are granted a massive FSI of 3.00 on gross plot area. The developer physically partitions the land in a 1:3 ratio, '
        'constructing and handing over 27.88 sq.m. self-contained tenements on the 25% pocket to the Urban Local Body (ULB) completely free of cost, '
        'subsidized by the lucrative 75% free-sale residential/commercial component. Under PMAY, the state unlocks up to 2.50 basic FSI without '
        'charging any premium or requiring TDR loading, making social housing economically viable across both municipal and regional plan areas.'
    ),
    'plain_summary_html': """
      <p>
        Regulations 14.3 and 14.4 leverage private capital and public land value capture to manufacture free social housing stock. 
        Instead of direct municipal construction, the state provides massive FSI incentives linked to physical handover milestones:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>AHS Site Pre-requisites (Reg 14.3.i):</strong>
          <br>&bull; <em>Location:</em> Must be within Municipal Corporation limits in a <strong>Residential Zone</strong> (or Industrial zone converted to residential). Strictly barred in congested gaothans.
          <br>&bull; <em>Minimum Plot Scale:</em> Minimum <strong>4,000 sq.m.</strong> contiguous unencumbered land (excluding DP roads/reservations).
          <br>&bull; <em>Road Access:</em> Minimum <strong>18.0 meters width</strong> from an existing or sanctioned DP road or declared street line.
        </li>
        <li><strong>FSI &amp; Physical Partitioning (Reg 14.3.i.e):</strong>
          <br>&bull; Maximum permissible FSI is <strong>3.00 on gross plot area</strong>.
          <br>&bull; <em>Spatial Division:</em> Land is carved into two independent buildable pockets in a <strong>1:3 ratio</strong>.
          <br>&bull; <em>Affordable Pocket (25% Land):</em> Consumes 3.00 FSI on its 1/4th land share, completely constructed and handed over free to the ULB.
          <br>&bull; <em>Free Sale Pocket (75% Land):</em> Consumes 3.00 FSI on its 3/4th land share, monetized as market housing or commercial spaces.
        </li>
        <li><strong>Tenement Specifications &amp; Amenities (Reg 14.3.i.g &amp; ii):</strong>
          <br>&bull; Each affordable tenement is a self-contained unit of exactly <strong>27.88 sq.m. (300 sq.ft.) carpet area</strong>.
          <br>&bull; Up to <strong>15% BUA</strong> of the affordable component may be built as convenience shops handed over free to the ULB.
          <br>&bull; Mandatory Balwadi &amp; Welfare Hall of <strong>30 sq.m. per 200 units</strong>, and Society Office of <strong>30 sq.m. per 500 units</strong>, both 100% FSI-free.
        </li>
        <li><strong>Off-Site Infrastructure Charges (Reg 14.3.iii):</strong>
          <br>&bull; Developer pays <strong>5% of ASR land rate</strong> (minimum <strong>&#8377;2,000 / sq.m.</strong>) on the built-up area consumed over and above normal permissible FSI to fund city-level water/sewerage connections.
        </li>
        <li><strong>PMAY Scheme Incentives (Reg 14.4):</strong>
          <br>&bull; <em>Developable Zones:</em> Permissible FSI equals the maximum building potential up to <strong>2.50 FSI as basic allowable FSI</strong> with <strong>ZERO premium and ZERO TDR</strong>.
          <br>&bull; <em>Commercial Share:</em> 10% of basic FSI permitted for commercial shops to generate maintenance endowments.
          <br>&bull; <em>Regional Plan Green/Agri Zones:</em> Permitted with <strong>1.00 FSI</strong> within 2.0 km of Municipal Corporation boundaries and 1.0 km of Municipal Council limits on a 9.0m road.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "14.3 AFFORDABLE HOUSING SCHEME - Maximum permissible FSI under the Scheme shall be 3.00 on the gross plot area... "
        "The FSI to be utilized shall be in the proportion of 1:3 for the Affordable Housing Component and the Free Sale Housing Component "
        "on 1/4th and 3/4th part of the land respectively... Affordable Housing Unit shall be a self-contained dwelling unit of 27.88 sq.m. "
        "carpet area... 14.4 PRADHAN MANTRI AWAS YOJANA - Permissible FSI for such projects shall be maximum building potential subject to "
        "maximum 2.5 which shall be treated as allowable basic FSI. No premium FSI or TDR shall be required to be loaded."
    ),
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:16px;">
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.3 // TABLE 14-S</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">FSI Release Milestones</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            To prevent developers from abandoning social housing after completing market towers, Free Sale FSI is unlocked strictly 
            in phases: <strong>1.00 at plinth</strong>, <strong>0.75 at 50% affordable BUA</strong>, <strong>0.75 at 100% affordable BUA</strong>, 
            and the final <strong>0.50 only upon physical handover</strong> of the 25% land and completed units.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.3 // TABLE 14-T</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Statutory Stock Distribution</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            The handed-over affordable units are statutorily divided: <strong>50% to the ULB</strong> for Project Affected Persons (PAP) / transit staff, 
            <strong>25% to the State Government</strong> for public undertakings, and <strong>25% to MHADA</strong> for transparent computerized public lottery allotment.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 14.4 // GREEN BELTS</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">PMAY Peripheral Corridors</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            PMAY can be approved even in Agricultural / Green Zones within <strong>2.0 km of Municipal Corporation limits</strong> or 
            <strong>1.0 km of Municipal Council boundaries</strong> on 9.0m roads with 1.00 FSI, opening affordable land banks outside congested urban cores.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="overflow-x:auto; margin-top:12px;">
        <div class="kicker" style="color:var(--blueprint); margin-bottom:6px;">TABLE 14-S // STAGES OF FSI RELEASE</div>
        <table class="blueprint-table" style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="background:var(--surface-tint); border-bottom:2px solid var(--line-bold);">
              <th style="padding:10px; text-align:left;">Stage No.</th>
              <th style="padding:10px; text-align:left;">Construction Milestone</th>
              <th style="padding:10px; text-align:center;">Affordable FSI Released</th>
              <th style="padding:10px; text-align:center;">Free Sale FSI Released</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px; font-family:var(--mono);">Stage 1</td>
              <td style="padding:10px;">Grant of Building Permission / Plinth CC by Commissioner</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint);">3.00</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">1.00</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px; font-family:var(--mono);">Stage 2</td>
              <td style="padding:10px;">Completion of 50% Built-Up Area of Affordable Component</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">--</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">0.75</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px; font-family:var(--mono);">Stage 3</td>
              <td style="padding:10px;">Completion of 100% Built-Up Area of Affordable Component</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">--</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">0.75</td>
            </tr>
            <tr style="border-bottom:2px solid var(--line-bold); background:var(--surface-tint);">
              <td style="padding:10px; font-family:var(--mono);">Stage 4</td>
              <td style="padding:10px;">Handing over 25% land and completed Affordable Component to ULB</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">--</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint);">0.50</td>
            </tr>
            <tr style="background:var(--surface); font-weight:700;">
              <td style="padding:10px;" colspan="2">Total Admissible FSI (Calculated on respective 1/4th &amp; 3/4th plot shares)</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--blueprint);">3.00</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--blueprint);">3.00</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,
    'worked_example_html': """
      <div style="line-height:1.6; font-size:0.92rem;">
        <h4 style="margin:0 0 8px 0; color:var(--amber-dark);">Scenario: 4,000 sq.m. Affordable Housing Scheme (AHS) Master Calculation</h4>
        <p>
          A developer proposes an Affordable Housing Scheme under Regulation 14.3 on a <strong>4,000 sq.m. net residential plot</strong> 
          fronting a <strong>18.0-meter DP road</strong> in Nashik Municipal Corporation. The ASR land rate is <strong>&#8377;15,000 / sq.m.</strong>
          Calculate the land pocket partition, tenement count, free-sale potential, and the off-site infrastructure charges.
        </p>
        <div style="background:var(--surface); border:1px solid var(--line); padding:12px; margin:10px 0; font-family:var(--mono); font-size:0.85rem;">
          1. Land Pocket Partition (1:3 Ratio per Reg 14.3.i.e):<br>
          &nbsp;&nbsp;&bull; Affordable Housing Land Share (1/4th) = 4,000 sq.m. &times; 0.25 = <strong>1,000 sq.m.</strong><br>
          &nbsp;&nbsp;&bull; Free Sale Land Share (3/4th) = 4,000 sq.m. &times; 0.75 = <strong>3,000 sq.m.</strong><br><br>
          2. Built-Up Area (BUA) Allocation (FSI 3.00):<br>
          &nbsp;&nbsp;&bull; Affordable BUA = 1,000 sq.m. &times; 3.00 = <strong>3,000 sq.m.</strong><br>
          &nbsp;&nbsp;&bull; Free Sale BUA = 3,000 sq.m. &times; 3.00 = <strong>9,000 sq.m.</strong><br>
          &nbsp;&nbsp;&bull; Total Scheme BUA = 3,000 + 9,000 = <strong>12,000 sq.m.</strong><br><br>
          3. Affordable Housing Units Yield:<br>
          &nbsp;&nbsp;&bull; Commercial shops allowed (15% max per Reg 14.3.i.f) = 3,000 &times; 15% = 450 sq.m.<br>
          &nbsp;&nbsp;&bull; Net Residential BUA = 3,000 - 450 = 2,550 sq.m.<br>
          &nbsp;&nbsp;&bull; Average BUA per 27.88 sqm carpet flat &approx; 34.85 sq.m. (at 1.25 BUA factor)<br>
          &nbsp;&nbsp;&bull; Number of EWS/LIG Tenements = 2,550 / 34.85 &approx; <strong>73 Tenements</strong><br>
          &nbsp;&nbsp;&bull; Handover Stock: 37 units to ULB (50%), 18 units to GoM (25%), 18 units to MHADA (25%)<br><br>
          4. Social Amenities Mandate:<br>
          &nbsp;&nbsp;&bull; Welfare Hall &amp; Balwadi (30 sqm per 200 units) = 1 &times; 30 = 30 sq.m. (FSI Free)<br>
          &nbsp;&nbsp;&bull; Society Office (30 sqm per 500 units) = 1 &times; 30 = 30 sq.m. (FSI Free)<br><br>
          5. Off-Site Infrastructure Charges (Reg 14.3.iii):<br>
          &nbsp;&nbsp;&bull; Normal Permissible FSI = 1.10 &rarr; Normal BUA = 4,000 &times; 1.10 = 4,400 sq.m.<br>
          &nbsp;&nbsp;&bull; BUA over normal FSI = 12,000 - 4,400 = 7,600 sq.m.<br>
          &nbsp;&nbsp;&bull; Charge Rate = 5% of ASR (5% &times; &#8377;15,000 = &#8377;750/sqm, but minimum is &#8377;2,000/sqm!)<br>
          &nbsp;&nbsp;&bull; Rate applied = <strong>&#8377;2,000 / sq.m.</strong><br>
          &nbsp;&nbsp;&bull; Total Off-site Infra Charge = 7,600 sq.m. &times; &#8377;2,000 = <strong>&#8377;1,52,00,000 (&#8377;1.52 Cr)</strong>
        </div>
        <p style="font-size:0.85rem; color:var(--ink-soft); margin:0;">
          <strong>Milestone Guardrail:</strong> The developer cannot obtain the final 0.50 FSI (1,500 sq.m. free-sale BUA) until the 1,000 sq.m. plot, 73 flats, and convenience shops are completely conveyed to the ULB.
        </p>
      </div>
    """,
    'pitfalls_html': """
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 1: Applying for AHS on Sub-4,000 Sq.m. or Narrow Road Plots</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under Reg 14.3.i, the 4,000 sq.m. land threshold and 18.0-meter road width are non-negotiable statutory baselines. Proposals on 3,500 sq.m. plots or 15m roads will be rejected outright at initial scrutiny.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 2: Neglecting the &#8377;2,000/sqm Off-site Infra Charge Minimum</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          While the rule cites 5% of ASR land rate, it contains a strict statutory floor: <em>"subject to a minimum of Rs. 2,000/- per Sq.m."</em> Developers in peripheral zones where 5% of ASR works out to &#8377;500 or &#8377;800 must still pay the full &#8377;2,000/sqm floor.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 3: Assuming PMAY 2.50 FSI Requires Premium Payments</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under Reg 14.4.1.i(3), building potential up to 2.50 is treated as <strong>basic FSI</strong> for 100% EWS/LIG PMAY schemes. Municipal scrutiny officers cannot demand premium FSI challans or TDR utilization certificates up to 2.50.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.9rem; line-height:1.6; margin:0 0 10px 0;">
        <strong>Corrigendum dt. 2nd December 2021:</strong> Formally substituted Table No. 14-S, restructuring the free-sale release into 4 concrete construction milestones, 
        and confirmed 27.88 sq.m. as the standardized carpet area.<br>
        <strong>Clarification dt. 23rd December 2021:</strong> Confirmed that PMAY building potential up to 2.50 is allowable without loading premium or TDR, 
        with 10% permissible commercial BUA.
      </p>
    """,
    'quiz': [
        {
            'question': 'What is the minimum plot area required to implement an Affordable Housing Scheme under Regulation 14.3?',
            'options': [
                '1,000 sq.m.',
                '2,000 sq.m.',
                '4,000 sq.m.',
                '10,000 sq.m.'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.3.i(b) stipulates that the minimum plot area for the Affordable Housing Scheme shall be 4,000 sq.m., excluding DP roads and reservations.'
        },
        {
            'question': 'In what land proportion is an AHS site partitioned between the Affordable Housing Component and Free Sale Component?',
            'options': [
                '50% Affordable : 50% Free Sale',
                '25% Affordable (1/4th) : 75% Free Sale (3/4th)',
                '30% Affordable : 70% Free Sale',
                '20% Affordable : 80% Free Sale'
            ],
            'answer': 1,
            'explanation': 'Regulation 14.3.i(e) requires FSI to be utilized in the proportion of 1:3 for the Affordable Housing Component and Free Sale Component on 1/4th and 3/4th part of the land respectively.'
        },
        {
            'question': 'What is the statutory carpet area of an Affordable Housing unit under Regulation 14.3.i.g?',
            'options': [
                '20.00 sq.m.',
                '27.88 sq.m. (300 sq.ft.)',
                '45.00 sq.m.',
                '60.00 sq.m.'
            ],
            'answer': 1,
            'explanation': 'Regulation 14.3.i(g) mandates that an Affordable Housing Unit shall be a self-contained dwelling unit of 27.88 sq.m. carpet area.'
        },
        {
            'question': 'What is the minimum statutory floor for off-site infrastructure charges under Regulation 14.3.iii?',
            'options': [
                'Rs. 500 per sq.m.',
                'Rs. 1,000 per sq.m.',
                'Rs. 2,000 per sq.m.',
                'Rs. 5,000 per sq.m.'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.3.iii mandates 5% of ASR land rate, subject to a minimum of Rs. 2,000/- per sq.m.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
