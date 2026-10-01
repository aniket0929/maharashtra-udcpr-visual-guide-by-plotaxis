"""
UDCPR Chapter 15 - Lesson 15.3: Local Area Plans (LAP) & Complete Street Design Guidelines
Statutory Clauses: Regulations 15.3 & 15.4 (Appendix-M)
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 15.3 & 15.4 (Appendix-M)',
    'title': 'Local Area Plans (LAP) & Complete Street Design Guidelines',
    'meta_desc': 'Master UDCPR Regulations 15.3 & 15.4 with Appendix-M: Micro-level Local Area Plans (LAP) under MRTP Section 33 that legally prevail over UDCPR, and Complete Street Design Guidelines for 18m to 60m roads (segregated pedestrian walkways, cycle tracks, multi-utility zones, and universal accessibility).',
    'ch_slug': 'ch15',
    'ch_title': 'Chapter 15: Regulations for Special Activities / Plans',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'UDD Corrigendum No. CR 121/21 dt. 02-Dec-2021 (Appendix-M Insertion)',
    'filename': 'reg-15-3-local-area-plans-and-street-design.html',
    'lesson_id': 'ch15_lesson_3',
    'quiz_id': 'quiz_ch15_3',
    'prev_url': '/lessons/reg-15-2-mobile-towers-and-telecom-infrastructure.html',
    'prev_title': 'Reg. 15.2 Telecommunication Infrastructure & Mobile Towers',
    'next_url': '/chapters/index.html',
    'next_title': 'Statutory Curriculum Index (Chapters 1 to 15 Complete)',
    'lead_summary': (
        'To transition Maharashtra\'s urban centers from car-dominated asphalt corridors into vibrant, human-scale, climate-resilient cities, '
        'Regulations 15.3 and 15.4 establish the twin legal engines of modern master planning: Local Area Plans (LAP) and Complete Street Design. '
        'Under Regulation 15.3, planning authorities can prepare precinct-level Local Area Plans following the procedure of Section 33 of the '
        'MRTP Act 1966. Once sanctioned by the State Government, a Local Area Plan enjoys statutory supremacy—its provisions override the UDCPR '
        'in cases of conflict. Under Regulation 15.4 and Appendix-M, all newly developed or widened roads between 18.0 and 60.0 meters must '
        'incorporate complete street geometry: segregated 1.8m pedestrian sidewalks, dedicated cycle tracks, multi-utility zones (MUZ), '
        'underground utility corridors, and universal barrier-free accessibility.'
    ),
    'plain_summary_html': """
      <p>
        These two regulations represent the statutory culmination of UDCPR-2020, shifting urban governance from broad macro-zoning to granular, 
        people-first neighborhood design:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Local Area Plans - LAP (Reg 15.3):</strong>
          <br>&bull; <em>Purpose:</em> Comprehensive micro-level planning for high-density downtowns, transit station areas, historic bazaars, or waterfront corridors.
          <br>&bull; <em>Statutory Procedure:</em> Prepared by the Planning Authority following the public consultation and notification procedure under <strong>Section 33 of the MRTP Act, 1966</strong>, and formally sanctioned by the State Government.
          <br>&bull; <em>Legal Supremacy Over UDCPR:</em> The statute explicitly decrees: <em>"In the event of provisions of local area plan not consistent with UDCPR, the provisions of local area plan shall prevail."</em> An approved LAP can set custom setbacks, ground coverage, building heights, or pedestrian easements that legally override standard UDCPR chapters.
        </li>
        <li><strong>Complete Street Design Mandate (Reg 15.4):</strong>
          <br>&bull; Streets must be designed as public spaces catering equally to all modes of movement, not merely vehicular traffic.
          <br>&bull; Mandates specific physical provisions for: (i) pedestrians of all age groups, (ii) cyclists, (iii) persons with disabilities (barrier-free universal design), (iv) street retail and active frontage, (v) street furniture and wayfinding, (vi) tree canopies, (vii) energy-efficient illumination, and (viii) underground utility ducts.
        </li>
        <li><strong>Appendix-M Specimen Street Cross-Sections (18m to 60m):</strong>
          <br>&bull; Planning Authorities must engineer all new roads from <strong>18.0 meters up to 60.0 meters width</strong> strictly in accordance with the standardized cross-section plates in Appendix-M:
          <br>&bull; <em>Pedestrian Zone:</em> Continuous, level, shaded sidewalk of minimum <strong>1.80 meters clear width</strong> with tactile paving.
          <br>&bull; <em>Multi-Utility Zone (MUZ):</em> Dedicated buffer strip accommodating tree basins, streetlights, fire hydrants, waste receptacles, and utility service chambers.
          <br>&bull; <em>Cycle Track:</em> Segregated, grade-separated or curb-protected bicycle lane (min <strong>2.0 meters width</strong> for one-way).
          <br>&bull; <em>Carriageway &amp; Transit Lanes:</em> Standardized lane widths (3.25m to 3.50m) preventing erratic vehicular weaving, with dedicated bus priority lanes on 30m+ corridors.
        </li>
        <li><strong>Underground Utility Integration:</strong>
          <br>&bull; Water supply lines, storm sewers, power cables, and telecom fiber must be housed in organized underground service trenches beneath the utility zone, ending chaotic road excavation and trench cutting.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "15.3 PREPARATION OF LOCAL AREA PLAN - A local area plan is a plan for comprehensive development of particular area in city / town... "
        "The local area plan shall be prepared by following procedure similar to that of section 33 of the Maharashtra Regional and Town Planning "
        "Act, 1966. After approval to this plan by State Government, it shall come into force. In the event of provisions of local area plan not "
        "consistent with UDCPR, the provisions of local area plan shall prevail. 15.4 GUIDELINES FOR STREET DESIGN - The authority shall ensure "
        "complete design of street... The specimen plans for development of a street having road width 18 m. and up to 60 m. are given at Appendix-M."
    ),
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:16px;">
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--brick);">REG. 15.3 // LEGAL SUPREMACY</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">LAP Overrides UDCPR</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Once a Local Area Plan is approved by the State Government under MRTP Section 33, its specific regulations legally supersede 
            the general provisions of the UDCPR. Local setbacks, arcade mandates, and street walls take statutory precedence.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">REG. 15.4 // APPENDIX-M</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">18m to 60m Standard Cross-Sections</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Inserted vide Corrigendum dt. 02-Dec-2021, Appendix-M provides engineering cross-sections for 18m, 24m, 30m, 45m, and 60m roads, 
            mandating segregated footpaths, cycle tracks, and multi-utility buffer strips.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">UNIVERSAL URBAN MOBILITY</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Active Frontages &amp; Retail</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Streets are designed to foster pedestrian activity and street retail, with continuous tree shading, barrier-free curb ramps, 
            and zero visual barriers between building frontages and sidewalks.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="overflow-x:auto; margin-top:12px;">
        <div class="kicker" style="color:var(--blueprint); margin-bottom:6px;">APPENDIX-M // COMPLETE STREET CROSS-SECTION COMPONENT MATRIX</div>
        <table class="blueprint-table" style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="background:var(--surface-tint); border-bottom:2px solid var(--line-bold);">
              <th style="padding:10px; text-align:left;">Right of Way (RoW)</th>
              <th style="padding:10px; text-align:center;">Pedestrian Walkway</th>
              <th style="padding:10px; text-align:center;">Multi-Utility Zone (MUZ)</th>
              <th style="padding:10px; text-align:center;">Dedicated Cycle Track</th>
              <th style="padding:10px; text-align:left;">Vehicular Carriageway</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>18.0m Street</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">1.80m both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">1.20m both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--ink-soft);">Shared with NMT</td>
              <td style="padding:10px;">2 &times; 3.50m dual lanes + median (7.0m total)</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>24.0m Street</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">2.50m both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">1.50m both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--blueprint); font-weight:700;">2.00m both sides</td>
              <td style="padding:10px;">4 &times; 3.25m lanes (13.0m total carriageway)</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>30.0m Street</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">3.00m both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono);">2.00m both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); color:var(--blueprint); font-weight:700;">2.20m both sides</td>
              <td style="padding:10px;">4 &times; 3.50m lanes + 2.0m central median</td>
            </tr>
            <tr style="border-bottom:2px solid var(--line-bold); background:var(--surface-tint);">
              <td style="padding:10px;"><strong>45.0m to 60.0m Boulevard</strong></td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700;">3.50m+ both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700;">2.50m both sides</td>
              <td style="padding:10px; text-align:center; font-family:var(--mono); font-weight:700; color:var(--blueprint);">2.50m protected</td>
              <td style="padding:10px;">Dedicated BRT / Transit lanes + 6 vehicular traffic lanes</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div style="font-size:0.82rem; color:var(--ink-soft); margin-top:8px;">
        *Note: All cross-sections mandate continuous tactile guidance paths, curb ramps at 1:12 slope, and underground utility service ducts.
      </div>
    """,
    'worked_example_html': """
      <div style="line-height:1.6; font-size:0.92rem;">
        <h4 style="margin:0 0 8px 0; color:var(--amber-dark);">Scenario: Designing a 24.0-Meter Complete Street Cross-Section under Appendix-M</h4>
        <p>
          A municipal engineering department plans a new <strong>24.0-meter wide DP Road</strong> connecting a newly developed residential zone 
          to a high-frequency bus rapid transit corridor in Pimpri-Chinchwad. 
          Allocate the 24.0-meter right-of-way (RoW) to satisfy all pedestrian, cycle, multi-utility, and vehicular mandates under Regulation 15.4 and Appendix-M.
        </p>
        <div style="background:var(--surface); border:1px solid var(--line); padding:12px; margin:10px 0; font-family:var(--mono); font-size:0.85rem;">
          Total Right of Way (RoW) = 24.00 meters<br><br>
          1. Pedestrian Realm Allocation (Both Sides):<br>
          &nbsp;&nbsp;&bull; Sidewalk width = 2.50m per side (continuous, barrier-free)<br>
          &nbsp;&nbsp;&bull; Total Pedestrian Zone = 2.50m &times; 2 = <strong>5.00 meters (20.8% of RoW)</strong><br><br>
          2. Multi-Utility Zone (MUZ) Allocation (Both Sides):<br>
          &nbsp;&nbsp;&bull; Strip for tree basins, streetlights, fire hydrants &amp; underground ducts = 1.50m per side<br>
          &nbsp;&nbsp;&bull; Total Utility Zone = 1.50m &times; 2 = <strong>3.00 meters (12.5% of RoW)</strong><br><br>
          3. Dedicated Non-Motorized Transport (Cycle Tracks Both Sides):<br>
          &nbsp;&nbsp;&bull; Curb-protected cycle track width = 2.00m per side<br>
          &nbsp;&nbsp;&bull; Total Cycle Realm = 2.00m &times; 2 = <strong>4.00 meters (16.7% of RoW)</strong><br><br>
          4. Vehicular Carriageway &amp; Median:<br>
          &nbsp;&nbsp;&bull; Remaining RoW for vehicles = 24.00 - (5.00 + 3.00 + 4.00) = 12.00 meters<br>
          &nbsp;&nbsp;&bull; Central median with street lighting = 1.00 meter<br>
          &nbsp;&nbsp;&bull; Carriageway = 11.00 meters (divided into two 5.50m two-lane roadways, 2.75m/lane)<br>
          &nbsp;&nbsp;&bull; Total Vehicular Realm = <strong>12.00 meters (50.0% of RoW)</strong><br><br>
          Cross-Section Verification Check:<br>
          &nbsp;&nbsp;&bull; 2.50m (Sidewalk) + 1.50m (MUZ) + 2.00m (Cycle) + 5.50m (Carriageway) + 1.00m (Median) + 5.50m (Carriageway) + 2.00m (Cycle) + 1.50m (MUZ) + 2.50m (Sidewalk) = <strong>24.00 METERS EXACT</strong>
        </div>
        <p style="font-size:0.85rem; color:var(--ink-soft); margin:0;">
          <strong>Design Balance:</strong> Exactly 50% of the public right-of-way is dedicated to pedestrians, cyclists, and civic greening, guaranteeing sustainable, multimodal mobility.
        </p>
      </div>
    """,
    'pitfalls_html': """
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 1: Assuming UDCPR Overrules an Approved Local Area Plan</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under Regulation 15.3, the legal hierarchy is inverted: an approved Local Area Plan (LAP) <strong>prevails over the UDCPR</strong>. Architects submitting plans based on generic Chapter 6 setbacks in an LAP precinct with mandatory continuous building arcades will face statutory rejection.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 2: Eliminating Sidewalks for Carriageway Expansion</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Regulation 15.4 and Appendix-M mandate clear sidewalks (min 1.80m) on all roads &ge; 18m. Municipal road widening projects that pave curb-to-curb without segregated pedestrian footpaths and utility zones violate state town planning guidelines.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 3: Placing Tree Pits and Transformers in the Clear Walking Path</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Street furniture, junction boxes, and tree basins must be consolidated exclusively inside the <strong>Multi-Utility Zone (MUZ)</strong>. Obstructing the 1.8m pedestrian path violates barrier-free accessibility norms.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.9rem; line-height:1.6; margin:0 0 10px 0;">
        <strong>Corrigendum dt. 2nd December 2021:</strong> Formally inserted Appendix-M into Regulation 15.4, providing authoritative specimen engineering 
        drawings for streets between 18.0m and 60.0m width.<br>
        <strong>Statutory Signature Plate:</strong> Regulation 15 represents the final statutory chapter of UDCPR-2020, formally sanctioned and countersigned 
        by Kishor Gokhale (Under Secretary) and N. R. Shende (Director of Town Planning and Joint Secretary).
      </p>
    """,
    'quiz': [
        {
            'question': 'If a provision in an approved Local Area Plan (LAP) conflicts with a provision of the UDCPR, which prevails under Regulation 15.3?',
            'options': [
                'The UDCPR always prevails as the primary state regulation',
                'The provisions of the Local Area Plan shall prevail',
                'The National Building Code (NBC) prevails',
                'Both provisions become null and void'
            ],
            'answer': 1,
            'explanation': 'Regulation 15.3 explicitly states: "In the event of provisions of local area plan not consistent with UDCPR, the provisions of local area plan shall prevail."'
        },
        {
            'question': 'Under which section of the Maharashtra Regional and Town Planning Act, 1966 is a Local Area Plan prepared per Regulation 15.3?',
            'options': [
                'Section 18',
                'Section 20',
                'Section 33',
                'Section 124'
            ],
            'answer': 2,
            'explanation': 'Regulation 15.3 mandates that the Local Area Plan shall be prepared following the procedure similar to that of Section 33 of the MRTP Act, 1966.'
        },
        {
            'question': 'Which statutory appendix provides specimen street development plans for roads from 18m to 60m width under Regulation 15.4?',
            'options': [
                'Appendix - A',
                'Appendix - C',
                'Appendix - K',
                'Appendix - M'
            ],
            'answer': 3,
            'explanation': 'Regulation 15.4 (inserted vide Corrigendum dt. 02-Dec-2021) states: "The specimen plans for development of a street having road width 18 m. and up to 60 m. are given at Appendix-M."'
        },
        {
            'question': 'What is the minimum clear, unobstructed width required for a pedestrian sidewalk under Complete Street Design standards?',
            'options': [
                '0.90 meters',
                '1.20 meters',
                '1.80 meters',
                '3.50 meters'
            ],
            'answer': 2,
            'explanation': 'Under complete street and universal accessibility standards, the dedicated pedestrian walking path must maintain a minimum clear width of 1.80 meters.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
