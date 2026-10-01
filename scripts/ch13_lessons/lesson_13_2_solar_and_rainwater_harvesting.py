"""
UDCPR Chapter 13 - Lesson 13.2: Rooftop Solar SWH/RTPV & Rainwater Harvesting Infrastructure
Statutory Clauses: Regulation 13.2, Regulation 13.3
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 13.2 & 13.3',
    'title': 'Rooftop Solar SWH / RTPV & Rainwater Harvesting Infrastructure',
    'meta_desc': 'Chapter 13 sustainable building infrastructure under UDCPR-2020: solar water heating and RTPV norms (plot > 4,000 sqm, 25% roof area, 50 kg/sqm loading), and mandatory Rain Water Harvesting (plots >= 500 sqm, 4-layer filter media, 100mm pipes, and complete FSI exemption).',
    'ch_slug': 'ch13',
    'ch_title': 'Chapter 13: Special Provisions for Certain Buildings',
    'badge_status': '100% COMPLETE',
    'amendment_cite': None,
    'filename': 'reg-13-2-solar-and-rainwater-harvesting.html',
    'lesson_id': 'ch13_lesson_2',
    'quiz_id': 'quiz_ch13_2',
    'prev_url': '/lessons/reg-13-1-barrier-free-access-for-differently-abled.html',
    'prev_title': 'Reg. 13.1 Barrier-Free Access & Universal Design',
    'next_url': '/lessons/reg-13-3-grey-water-and-solid-waste.html',
    'next_title': 'Reg. 13.4 - 13.5 Grey Water & Solid Waste Management',
    'lead_summary': (
        'Ecological resilience and decentralized resource management are codified into mandatory building controls under UDCPR Chapter 13. '
        'Regulation 13.2 makes Solar Assisted Water Heating (SWH) or Rooftop Photovoltaic (RTPV) systems mandatory on all plots exceeding 4,000 sq.m, '
        'requiring at least 25% of the terrace footprint, structural roof loading of 50 kg/sq.m, low parapet railings on south/east/west faces to prevent shadows, '
        'and insulated hot water distribution risers. In tandem, Regulation 13.3 mandates Rain Water Harvesting (RWH) on all plots of 500 sq.m or more '
        'and layout amenity spaces. It provides exact statutory engineering templates—including 4-layer percolation pits (40mm aggregate, 20mm stone, '
        'coarse sand, fine sand with 15 cm raised masonry curbs), first-flush bypass valves, dual 100 mm discharge down-takes per 100 sq.m roof, '
        'and a statutory guarantee that all RWH structures are 100% exempt from FSI computations.'
    ),
    'plain_summary_html': """
      <p>
        Sustainable architecture in Maharashtra is governed by strict numerical thresholds rather than generic green-building points. 
        Regulations 13.2 and 13.3 govern two essential rooftop and ground-level utility systems:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Rooftop Solar SWH / RTPV Systems (Reg 13.2):</strong>
          <br>&bull; <em>Applicability:</em> Mandatory for all categories of buildings (residential, commercial, institutional) constructed on a <strong>plot area of more than 4,000 sq.m.</strong>
          <br>&bull; <em>Terrace Footprint:</em> At least <strong>25% of the total roof area</strong> must be dedicated to solar collectors or PV panels.
          <br>&bull; <em>Structural Design Load:</em> The structural engineer must design the roof slab for an additional dead/live load of at least <strong>50 kg per sq.m.</strong>
          <br>&bull; <em>Shadow Prevention Architecture:</em> Parapets on south, east, and west terrace edges must use open railings (above 1 foot solid wall) rather than solid masonry to eliminate shadows.
          <br>&bull; <em>Plumbing Integration:</em> For SWH, insulated hot water down-take pipelines must be pre-installed connecting the roof plant directly to all bathroom and kitchen tapping points.
        </li>
        <li><strong>Rain Water Harvesting Infrastructure (Reg 13.3):</strong>
          <br>&bull; <em>Applicability:</em> Mandatory on all new constructions, reconstructions, and layout open spaces / amenity spaces on <strong>plots of not less than 500 sq.m.</strong>
          <br>&bull; <em>Recharge Well Options:</em> Open recharge wells must be at least <strong>1.0 meter diameter and 6.0 meters deep</strong>. Bore-well recharge pits must be at least 1.0 m wide by <strong>3.0 m deep</strong> filled with aggregate filter media.
          <br>&bull; <em>Standard 4-Layer Percolation Pit Schedule:</em> Pits ($1.2 \times 1.2 \times 2.0-2.5\text{ m}$) or trenches ($0.6 \times 2-6 \times 1.5-2\text{ m}$) must be filled with:
            <br>&nbsp;&nbsp;1. Bottom 50% depth: <strong>40 mm stone aggregate</strong>.
            <br>&nbsp;&nbsp;2. Lower middle 20% depth: <strong>20 mm stone aggregate</strong>.
            <br>&nbsp;&nbsp;3. Upper middle 20% depth: <strong>Coarse sand</strong>.
            <br>&nbsp;&nbsp;4. Top layer: Thin layer of <strong>fine sand</strong>.
            <br>&nbsp;&nbsp;5. Top 10% headspace left empty with a concrete splash pad and <strong>15 cm raised plastered brick wall</strong> to prevent soil contamination.
          <br>&bull; <em>Rooftop Down-Pipes &amp; First Flush:</em> Minimum <strong>two 100 mm diameter pipes per 100 sq.m of roof area</strong>, fitted with mosquito-proof wire mesh and a first-flush diverter valve.
          <br>&bull; <em>100% FSI Exemption:</em> All surface/underground RWH collection tanks and filtration chambers are <strong>completely excluded from FSI computation</strong>.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "SWH or RTPV systems shall be mandatory in all types of buildings to be constructed on plot area of more than 4000 sq.m... "
        "The roof loading adopted in the design of such building should be at least 50 kg. Per sq.m... At least 25% of the roof area shall be utilized... "
        "parapet of south, east and west sides of the terrace shall be of railing type (above 1 feet)... "
        "Rain Water Harvesting: All the layout open spaces / amenity spaces... and plots having area not less than 500 sq.m... "
        "Pits or trenches shall be back filled with filter media: 40 mm stone aggregate as bottom layer upto 50%... 20 mm stone aggregate 20%... "
        "Coarse sand 20%... The projection of the wall above ground shall at least be 15 cm... at least two rain water pipes of 100 mm. dia. for a roof area of 100 sq.m... "
        "The structures constructed under this provision shall not be counted towards FSI computation."
    ),
    'clause_cards_html': """
      <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
        <div class="ruled-card">
          <span class="kicker">REGULATION 13.2</span>
          <h4 class="ruled-card-title">Solar SWH &amp; RTPV Thresholds</h4>
          <p class="ruled-card-desc">
            Mandatory on plots &gt; 4,000 sq.m. Requires min 25% of roof area, 50 kg/sq.m design roof loading, 
            low parapet railings on south/east/west to prevent shadow casting, and insulated hot water distribution piping.
          </p>
          <div class="ruled-card-footer">
            <span>SOLAR ENERGY</span>
            <span class="badge badge-status-done">&gt;4,000 SQ.M PLOT</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 13.3</span>
          <h4 class="ruled-card-title">RWH Mandate (&ge; 500 sq.m Plots)</h4>
          <p class="ruled-card-desc">
            Enforced on all plots &ge; 500 sq.m and all layout amenity spaces. Mandates recharge through open wells (1x6m), 
            bore-wells (&ge;3m pit), or storage tanks with insect-proof covers and overflow connections.
          </p>
          <div class="ruled-card-footer">
            <span>GROUND RECHARGE</span>
            <span class="badge badge-status-done">&ge;500 SQ.M PLOT</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">SCHEDULE TO REG. 13.3</span>
          <h4 class="ruled-card-title">4-Layer Filtration Trench Media</h4>
          <p class="ruled-card-desc">
            Standard filtration pit: 50% depth 40mm aggregate + 20% depth 20mm aggregate + 20% coarse sand + top fine sand. 
            Top 10% empty with splash pad and a 15 cm raised masonry perimeter curb to block surface silt.
          </p>
          <div class="ruled-card-footer">
            <span>FILTRATION MEDIA</span>
            <span class="badge badge-status-done">50-20-20-10 RATIO</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">INCENTIVE &amp; FSI RELIEF</span>
          <h4 class="ruled-card-title">100% Free of FSI Guarantee</h4>
          <p class="ruled-card-desc">
            All filtration pits, trenches, desilting chambers, and rainwater holding tanks (surface or underground) 
            are statutorily excluded from FSI calculations, ensuring green infrastructure does not penalize developable area.
          </p>
          <div class="ruled-card-footer">
            <span>STATUTORY RELIEF</span>
            <span class="badge badge-status-done">100% FSI EXEMPT</span>
          </div>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 13-B: SOLAR ROOFTOP &amp; RAINWATER HARVESTING SPECIFICATION PLATE</span>
          <span class="badge badge-status-done">REG. 13.2 &amp; 13.3</span>
        </div>

        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono); margin-bottom:16px;">
            <thead>
              <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">INFRASTRUCTURE SYSTEM</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:150px;">APPLICABILITY</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">KEY DIMENSIONS &amp; CAPACITY</th>
                <th style="padding:8px; text-align:left;">MANDATORY TECHNICAL PROTOCOL</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Solar SWH / RTPV System</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Plot area &gt; <strong>4,000 sq.m</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">&ge; <strong>25% roof area</strong></td>
                <td style="padding:8px;">50 kg/sq.m structural roof loading; south/east/west parapets must be railing type (&gt;1 ft) to avoid shadows; insulated hot water lines.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">RWH General Mandate</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Plot area &ge; <strong>500 sq.m</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Sized per roof catchment</td>
                <td style="padding:8px;">Compulsory on all layouts and plots &ge; 500 sqm; FSI free; society must maintain filtration chambers periodically.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Open Recharge Well</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Ground recharge option</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">Dia &ge; <strong>1.0 m</strong> | Depth &ge; <strong>6.0 m</strong></td>
                <td style="padding:8px;">Filtered runoff channeled through silt settlement tank; mesh cover against insects.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Bore-Well Recharge Pit</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Aquifer injection option</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">Width &ge; <strong>1.0 m</strong> | Depth &ge; <strong>3.0 m</strong></td>
                <td style="padding:8px;">Excavated around bore casing and refilled with gravel/coarse sand filter media.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Percolation Pit / Trench</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Soil infiltration option</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">Pit: 1.2x1.2x2.5m<br>Trench: 0.6x2-6x2m</td>
                <td style="padding:8px;">50% 40mm metal + 20% 20mm metal + 20% coarse sand + top fine sand. 15 cm raised masonry curb + perforated concrete slab.</td>
              </tr>
              <tr style="background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Terrace Down-Takes</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Roof drainage plumbing</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">Min <strong>two 100 mm &phi;</strong> pipes</td>
                <td style="padding:8px;">Per 100 sq.m roof catchment area; first-flush washing valve; insect-proof wire mesh.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
        <strong>Scenario:</strong> A developer proposes a commercial office tower on a <strong>5,000 sq.m plot</strong> in Pune with a 
        terrace roof area of <strong>1,200 sq.m</strong>. Determine the statutory solar rooftop commitment, structural roof dead-load allowance, 
        and the minimum number of rainwater harvesting down-takes and percolation trenches required.
      </p>
      <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
        <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">ENGINEERING CALCULATIONS (REG. 13.2 &amp; 13.3):</div>
        <div><strong>Part 1: Solar SWH / RTPV System (Reg. 13.2)</strong></div>
        <div>&bull; Plot area = 5,000 sq.m (&gt; 4,000 sq.m threshold) &rarr; <strong>SOLAR SYSTEM IS STATUTORILY MANDATORY</strong>.</div>
        <div>&bull; Minimum Dedicated Roof Area = 25% of 1,200 sq.m = <strong>300 sq.m of clear terrace area</strong>.</div>
        <div>&bull; Structural Design Load: Structural engineer must add at least <strong>50 kg/m&sup2;</strong> over the 300 sq.m zone in the STAAD/ETABS structural load model.</div>
        <div>&bull; Terrace Parapet Elevation: South, East, and West parapet walls must be restricted to 1 foot (300 mm) solid masonry, topped by open steel/aluminum railings to eliminate collector shadows.</div>
        <div style="margin-top:8px;"><strong>Part 2: Rain Water Harvesting Down-Takes (Reg. 13.3.Schedule.v)</strong></div>
        <div>&bull; Total Terrace Roof Catchment = 1,200 sq.m.</div>
        <div>&bull; Statutory Down-Pipe Norm = Minimum two 100 mm diameter pipes per 100 sq.m of roof.</div>
        <div>&bull; Number of 100 sq.m blocks = 1,200 / 100 = 12 blocks.</div>
        <div>&bull; Total Down-Pipes Required = 12 &times; 2 = <strong>24 vertical 100 mm &phi; HDPE/PVC rainwater down-takes</strong>.</div>
        <div>&bull; Each down-take must be fitted with an accessible first-flush bypass diverter valve before connecting into the site recharge trenches.</div>
        <div style="margin-top:8px;"><strong>Part 3: Percolation Filtration Trench Design (Reg. 13.3.Schedule.iv)</strong></div>
        <div>&bull; Trench Depth = 2.0 meters. Sized with 4 statutory layers:</div>
        <div>&nbsp;&nbsp;- Bottom 50% (1.00 m depth): 40 mm crushed stone aggregate.</div>
        <div>&nbsp;&nbsp;- Lower middle 20% (0.40 m depth): 20 mm crushed stone aggregate.</div>
        <div>&nbsp;&nbsp;- Upper middle 20% (0.40 m depth): Coarse river sand.</div>
        <div>&nbsp;&nbsp;- Top: Thin layer of fine sand with 200 mm freeboard (10% splash pad).</div>
        <div>&bull; Surface Protection: Brick wall projecting <strong>15 cm above ground</strong> plastered with cement mortar, capped with heavy-duty perforated concrete slabs.</div>
      </div>
    """,
    'pitfalls_html': """
      <div>
        <strong>1. Solid 1.2m Parapets Shadowing Solar Collector Panels (Reg 13.2.iv):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Architects often wrap the terrace with standard 1.2-meter solid parapets for safety. On south, east, and west exposures, solid walls cast massive winter shadows across the roof, reducing solar PV efficiency by up to 40%. UDCPR mandates open railing-type parapets above 1 foot on these orientations.
        </p>
      </div>
      <div>
        <strong>2. Omitting the 15 cm Raised Masonry Curb on Percolation Pits:</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Percolation pits built flush with adjacent driveways collect surface runoff contaminated with engine oil, road silt, and garden debris, clogging the filter sand within months. Reg. 13.3 strictly mandates that the pit wall must project <strong>at least 15 cm above the finished ground level</strong>.
        </p>
      </div>
      <div>
        <strong>3. Counting Rainwater Storage Tanks in FSI Calculations:</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Municipal scrutinizers occasionally question surface rainwater collection cisterns in open setbacks. Regulation 13.3 explicitly provides: <em>"The structures constructed under this provision shall not be counted towards FSI computation."</em> They are 100% exempt.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.92rem; line-height:1.6;">
        Regulations 13.2 and 13.3 operationalize the Maharashtra State Solar Energy Policy and Central Ground Water Authority (CGWA) guidelines. 
        Under municipal performance audits, failure to maintain operational RWH recharge structures carries severe penalties, including 
        withholding of the final Occupancy Certificate and forfeiture of security deposits placed during building sanction.
      </p>
    """,
    'quiz': [
        {
            'question': 'Under UDCPR Regulation 13.2, what is the plot area threshold where Solar SWH or Rooftop PV systems become mandatory?',
            'options': [
                'Plots of more than 1,000 sq.m.',
                'Plots of more than 2,000 sq.m.',
                'Plots of more than 4,000 sq.m.',
                'Plots of more than 10,000 sq.m.'
            ],
            'answer': 2,
            'explanation': 'Regulation 13.2 explicitly states: "SWH or RTPV systems shall be mandatory in all types of buildings to be constructed on plot area of more than 4000 sq.m."'
        },
        {
            'question': 'What minimum percentage of the roof area must be utilized for SWH/RTPV installations under Regulation 13.2(iii)?',
            'options': [
                'At least 10%',
                'At least 25%',
                'At least 50%',
                'At least 75%'
            ],
            'answer': 1,
            'explanation': 'Regulation 13.2(iii) mandates: "At least 25% of the roof area shall be utilized for installation of the SWH / RTPV system."'
        },
        {
            'question': 'What is the minimum statutory piping provision for discharging terrace rainwater under Regulation 13.3 (Schedule Item v)?',
            'options': [
                'One 75 mm pipe per 50 sq.m roof area',
                'At least two rain water pipes of 100 mm. dia. for a roof area of 100 sq.m.',
                'One 150 mm pipe per 200 sq.m roof area',
                'Pipes can be of any diameter as decided by the plumber'
            ],
            'answer': 1,
            'explanation': 'Schedule Item v to Reg. 13.3 explicitly dictates: "For the efficient discharge of rain water, there shall be at least two rain water pipes of 100 mm. dia. for a roof area of 100 sq.m."'
        },
        {
            'question': 'How are rainwater harvesting storage tanks and percolation structures treated with respect to FSI computation under Regulation 13.3?',
            'options': [
                'Counted at 50% FSI',
                'Counted against Ancillary FSI',
                'The structures constructed under this provision shall not be counted towards FSI computation',
                'Subject to Premium FSI payment'
            ],
            'answer': 2,
            'explanation': 'Regulation 13.3 explicitly provides: "The structures constructed under this provision shall not be counted towards FSI computation."'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
