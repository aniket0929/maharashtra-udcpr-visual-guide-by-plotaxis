"""
UDCPR Chapter 15 - Lesson 15.1: Quarrying Operations & Natural Resource Extraction
Statutory Clauses: Regulation 15.1
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 15.1',
    'title': 'Quarrying Operations & Natural Resource Extraction',
    'meta_desc': 'Master UDCPR Regulation 15.1 for Quarrying Operations: Permitted in Agricultural zones outside CRZ/ESZ/Heritage, 1:5,000 location and 1:500 contour excavation plans, 200m separation buffer from roads/settlements (500m for blasting), 500m labor camp offset, 0.50% ASR development charge, and 1-year annual revalidation up to 3 years max.',
    'ch_slug': 'ch15',
    'ch_title': 'Chapter 15: Regulations for Special Activities / Plans',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'Urban Development Department Standardized Guidelines on Minor Minerals',
    'filename': 'reg-15-1-quarrying-and-mining-operations.html',
    'lesson_id': 'ch15_lesson_1',
    'quiz_id': 'quiz_ch15_1',
    'prev_url': '/lessons/reg-14-7-special-industrial-logistics-ecosystems.html',
    'prev_title': 'Reg. 14.9 to 14.13 Special Industrial & Logistics Ecosystems',
    'next_url': '/lessons/reg-15-2-mobile-towers-and-telecom-infrastructure.html',
    'next_title': 'Reg. 15.2 Telecommunication Infrastructure & Mobile Towers',
    'lead_summary': (
        'To regulate the extraction of stone, sand, and murum while mitigating air pollution, slope destabilization, '
        'and ecological degradation, Regulation 15.1 establishes Maharashtra\'s statutory controls for quarrying and mining operations. '
        'Quarrying is permitted exclusively on private lands in Agricultural Zones situated outside Coastal Regulation Zones (CRZ), '
        'notified Eco-Sensitive Zones (ESZ), and heritage precincts. Proposals mandate joint approval from the Director of Geology and Mining, '
        'Maharashtra Pollution Control Board (MPCB), and Revenue Authorities. To protect public safety, the UDCPR enforces strict buffer '
        'distances—200 meters from 30m roads or settlements, expanding to 500 meters where blasting is utilized—combined with mandatory '
        'restoration bonds, 0.50m soil capping, and Development Charges at 0.50% of developed land ASR.'
    ),
    'plain_summary_html': """
      <p>
        Quarrying provides essential raw aggregate for construction but poses severe environmental hazards. Regulation 15.1 governs the entire 
        lifecycle from geological application to site restoration:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Zoning &amp; Environmental Ineligibility (Reg 15.1.1):</strong>
          <br>&bull; Permitted <strong>exclusively in Agricultural Zones</strong>.
          <br>&bull; Strictly barred within Coastal Regulation Zones (CRZ), notified Eco-Sensitive Zones (ESZ) around national parks, and heritage precincts.
          <br>&bull; Requires valid mining lease orders under the Minor Minerals Act and an official consent / NOC from the Maharashtra Pollution Control Board (MPCB).
        </li>
        <li><strong>Mandatory Technical Application Submissions (Reg 15.1.2 &amp; 15.1.3):</strong>
          <br>&bull; <em>Location Plan (1:5,000 scale):</em> Covering <strong>500 meters around the site</strong> showing all natural contours, watercourses, and structures.
          <br>&bull; <em>Excavation Plan (1:500 scale):</em> Detailing phasing, benching slopes, equipment locations, topsoil storage, screen mounds, and drainage channels. <strong>Must be approved by the Director of Geology and Mining, GoM</strong>.
          <br>&bull; <em>Restoration &amp; Re-greening Plan:</em> Outlining post-mining landscape restoration carried out in consultation with the Conservator of Forests / DFO.
        </li>
        <li><strong>Statutory Safety Separation Buffers (Reg 15.1.10 &amp; 15.1.11):</strong>
          <br>&bull; <em>Standard Buffer:</em> Minimum <strong>200 meters</strong> from any highway or public road of width &ge; 30m, railway track, or human settlement.
          <br>&bull; <em>Blasting Operations Buffer:</em> Buffer expands to a minimum of <strong>500 meters</strong> where explosive blasting is conducted.
          <br>&bull; <em>Labor Camp Safety:</em> Temporary worker barracks and residences must be situated <strong>at least 500 meters away</strong> from active quarrying and blasting faces. Heavy machinery blasting is prohibited.
        </li>
        <li><strong>Topsoil &amp; Slope Conservation (Reg 15.1.5 &amp; 15.1.6):</strong>
          <br>&bull; <em>0.50m Murum Capping:</em> In murum excavation, stripping down to bare rock is prohibited; a <strong>capping of at least half a meter (0.50m)</strong> must be retained to support future afforestation.
          <br>&bull; <em>Slope Stabilization:</em> Foot-wall slopes must be stabilized with deep-rooted soil-binding vegetation. Natural watercourses must be diverted around the perimeter.
          <br>&bull; <em>Dust Suppression:</em> Water must be sprayed at least once daily across haul roads, with dust-extraction hoods installed at conveyor transfer joints.
        </li>
        <li><strong>Development Charges &amp; 3-Year Time Limit (Reg 15.1.2.g &amp; 15.1.12):</strong>
          <br>&bull; Development Charge payable under MRTP Section 124-B is <strong>0.50% of the developed land rate in the ASR</strong>.
          <br>&bull; Permissions are issued for <strong>1 year</strong> and may be revalidated annually up to a <strong>maximum period of 3 years</strong>, after which a fresh application is mandatory.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "15.1 QUARRYING OPERATIONS - Permitted in Agriculture Zone outside CRZ and notified eco-sensitive zone and heritage precinct... "
        "No quarrying shall commence until excavation plan is approved by Director of Geology and Mining... No quarrying and crushing shall be "
        "permitted if a highway or public road having width of 30 m. or more, railway line or human settlement is located within 200 m... "
        "for quarrying with blasting operations, distance shall be at least 500 m... Development Charge shall be paid at 0.50% of the rates of "
        "developed land mentioned in A.S.R... Permission granted for period of 1 year and may be revalidated every year for maximum 3 years."
    ),
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:16px;">
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--brick);">REG. 15.1.10 // DUAL SAFETY BUFFERS</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">200m vs 500m Blast Setback</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Mechanical excavation requires a <strong>200-meter buffer</strong> from settlements, railways, and 30m highways. 
            The moment explosives or blasting operations are utilized, this buffer statutorily expands to <strong>500 meters</strong>.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 15.1.6 // SOIL PROTECTION</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">0.50m Murum Capping Rule</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Excavation operators cannot expose bare bedrock. The statute mandates preserving at least <strong>half a meter (0.50m)</strong> 
            of weathered murum topsoil to provide biological substrate for mandatory post-quarry tree planting.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 15.1.12 // 3-YEAR SUNSET</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Annual Revalidation Cycle</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Quarry sanctions are valid for <strong>1 year only</strong>, renewable annually up to a hard ceiling of <strong>3 years</strong>. 
            Extensions require proof of satisfactory compliance with the approved Forest Department restoration plan.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="overflow-x:auto; margin-top:12px;">
        <div class="kicker" style="color:var(--blueprint); margin-bottom:6px;">REGULATION 15.1 // STATUTORY CLEARANCES &amp; BUFFER PLATE</div>
        <table class="blueprint-table" style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="background:var(--surface-tint); border-bottom:2px solid var(--line-bold);">
              <th style="padding:10px; text-align:left;">Parameter</th>
              <th style="padding:10px; text-align:center;">Statutory Dimension / Value</th>
              <th style="padding:10px; text-align:left;">Approving Authority / Code</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Permissible Zone</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--blueprint); font-weight:700;">Agricultural Zone Only</td>
              <td style="padding:10px;">Barred in CRZ, ESZ, and Heritage Precincts</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Non-Blasting Safety Buffer</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700;">200.0 meters</td>
              <td style="padding:10px;">From 30m+ roads, railway tracks, settlements</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Blasting Operation Buffer</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--brick); font-weight:700;">500.0 meters</td>
              <td style="padding:10px;">From any road, railway, or human settlement</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Worker Housing Offset</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700;">500.0 meters</td>
              <td style="padding:10px;">Distance from active blasting and excavation pit</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Topsoil Murum Capping</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--amber-dark); font-weight:700;">Min. 0.50 meters</td>
              <td style="padding:10px;">Soil binding vegetation substrate preservation</td>
            </tr>
            <tr style="border-bottom:2px solid var(--line-bold); background:var(--surface-tint);">
              <td style="padding:10px;"><strong>Section 124-B Development Charge</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint);">0.50% of Developed ASR</td>
              <td style="padding:10px;">Paid to Planning Authority / Revenue Dept</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,
    'worked_example_html': """
      <div style="line-height:1.6; font-size:0.92rem;">
        <h4 style="margin:0 0 8px 0; color:var(--amber-dark);">Scenario: Quarrying Permission &amp; Development Charge Computation in Pune Rural</h4>
        <p>
          An aggregate operator applies for development permission under Regulation 15.1 to quarry basalt stone across a 
          <strong>20,000 sq.m. (2.0 Hectare)</strong> agricultural land parcel in Pune District. 
          The applicant proposes periodic controlled blasting. The nearest national highway (45m wide) is <strong>350 meters away</strong>, 
          and a village settlement is <strong>600 meters away</strong>. 
          The applicable ASR rate for developed land in the village registration zone is <strong>&#8377;8,000 / sq.m.</strong>
          Evaluate site buffer compliance, worker housing placement, and calculate the Section 124-B Development Charge.
        </p>
        <div style="background:var(--surface); border:1px solid var(--line); padding:12px; margin:10px 0; font-family:var(--mono); font-size:0.85rem;">
          1. Buffer Distance Scrutiny (Reg 15.1.10):<br>
          &nbsp;&nbsp;&bull; Village settlement distance = 600m (&gt; 500m mandatory blasting buffer) &rarr; <strong>COMPLIANT</strong><br>
          &nbsp;&nbsp;&bull; National Highway distance = 350m.<br>
          &nbsp;&nbsp;&bull; For non-blasting quarrying, 200m is required (350m &gt; 200m).<br>
          &nbsp;&nbsp;&bull; BUT because <strong>blasting operations</strong> are proposed, the statutory buffer is <strong>500 meters</strong>!<br>
          &nbsp;&nbsp;&bull; <strong>Finding:</strong> Blasting cannot be sanctioned on the portion of the pit within 500m of the highway.<br>
          &nbsp;&nbsp;&bull; The applicant must either amend the excavation plan to maintain a 500m blast buffer or restrict the nearest section to purely non-blasting mechanical ripping.<br><br>
          2. Labor Accommodation Placement (Reg 15.1.11):<br>
          &nbsp;&nbsp;&bull; Temporary labor barracks must be situated at least <strong>500 meters</strong> away from the active quarry face and blast zones.<br><br>
          3. Section 124-B Development Charge Calculation (Reg 15.1.2.g):<br>
          &nbsp;&nbsp;&bull; Land Area under quarrying = 20,000 sq.m.<br>
          &nbsp;&nbsp;&bull; ASR Rate of Developed Land = &#8377;8,000 / sq.m.<br>
          &nbsp;&nbsp;&bull; Statutory Charge Rate = <strong>0.50% of Developed Land ASR</strong><br>
          &nbsp;&nbsp;&bull; Charge per sq.m. = 0.50% &times; &#8377;8,000 = &#8377;40 / sq.m.<br>
          &nbsp;&nbsp;&bull; Total Development Charge = 20,000 sq.m. &times; &#8377;40 = <strong>&#8377;8,00,000 (&#8377;8.0 Lakhs)</strong><br><br>
          4. Sanction Validity &amp; Phasing (Reg 15.1.12):<br>
          &nbsp;&nbsp;&bull; Initial permission granted for exactly <strong>1 year</strong>.<br>
          &nbsp;&nbsp;&bull; Renewable for maximum 2 additional 1-year terms subject to Forest Dept restoration progress.
        </div>
        <p style="font-size:0.85rem; color:var(--ink-soft); margin:0;">
          <strong>Technical Guardrail:</strong> No excavation can commence until the Director of Geology and Mining formally countersigns the 1:500 phased extraction plan.
        </p>
      </div>
    """,
    'pitfalls_html': """
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 1: Conducting Blasting Operations Within the 500-Meter Highway Buffer</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          While mechanical digging is permissible up to 200m from a 30m+ road, using explosives triggers a strict <strong>500-meter statutory buffer</strong> under Reg 15.1.10. Conducting blasting within 500m of a highway or railway line constitutes a non-compoundable public hazard.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 2: Stripping All Soil and Exposing Bare Bedrock</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Regulation 15.1.6 prohibits excavating the entire weathered soil layer. Failing to leave the mandatory <strong>0.50m murum capping</strong> prevents vegetation regrowth, violates the Forest Restoration Plan, and leads to immediate forfeiture of security deposits.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 3: Assuming Permissions Automatically Extend Beyond 3 Years</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under Reg 15.1.12, revalidation is capped at a hard statutory ceiling of <strong>3 years total</strong>. Operating after 36 months without submitting a fresh development permission and updated restoration report is deemed illegal mining.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.9rem; line-height:1.6; margin:0 0 10px 0;">
        <strong>Statutory Harmonization:</strong> Regulation 15.1 aligns Maharashtra town planning with the Minor Minerals Act, 
        formalizing the tripartite approval mechanism between the Collector, Director of Geology and Mining, and the Local Planning Authority.<br>
        <strong>Section 124-B Standard:</strong> Standardized the development charge across all districts at exactly 0.50% of the developed land ASR.
      </p>
    """,
    'quiz': [
        {
            'question': 'In which land-use zone is quarrying and mining permitted under Regulation 15.1?',
            'options': [
                'Industrial Zone only',
                'Agricultural Zone only',
                'No Development Zone and Forest Land',
                'Residential Zone on plots > 10,000 sq.m.'
            ],
            'answer': 1,
            'explanation': 'Regulation 15.1 explicitly states that mining or quarrying operations may be permitted exclusively in the Agricultural Zone, outside CRZ, ESZ, and heritage precincts.'
        },
        {
            'question': 'What is the minimum statutory safety buffer required between a blasting quarry site and a 30m+ highway, railway, or human settlement?',
            'options': [
                '100 meters',
                '200 meters',
                '500 meters',
                '1,000 meters'
            ],
            'answer': 2,
            'explanation': 'Regulation 15.1.10 mandates a 200m buffer for standard quarrying, but explicitly specifies: "However, for quarrying with blasting operations, the distance shall be at least 500 m."'
        },
        {
            'question': 'How much weathered soil capping must be left during murum quarrying under Regulation 15.1.6 to support future afforestation?',
            'options': [
                'At least 0.10 meters',
                'At least 0.25 meters',
                'At least 0.50 meters (half a meter)',
                'No capping required'
            ],
            'answer': 2,
            'explanation': 'Regulation 15.1.6 requires that "a capping of at least half a meter (0.50m) be left so that it can support vegetation and plantation that be done later on."'
        },
        {
            'question': 'What is the rate of Development Charge payable for quarrying under Section 124-B of the MRTP Act per Regulation 15.1.2(g)?',
            'options': [
                '0.10% of developed land ASR',
                '0.50% of developed land ASR',
                '2.00% of agricultural land ASR',
                '5.00% of construction cost'
            ],
            'answer': 1,
            'explanation': 'Regulation 15.1.2(g) mandates development charges under Section 124-B at 0.50% of the rates of developed land mentioned in the ASR.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
