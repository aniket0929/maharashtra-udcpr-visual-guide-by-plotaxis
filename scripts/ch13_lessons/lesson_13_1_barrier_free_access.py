"""
UDCPR Chapter 13 - Lesson 13.1: Barrier-Free Access & Universal Design for Differently Abled Persons
Statutory Clauses: Regulation 13.1 (13.1.1 to 13.1.4)
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 13.1.1 - 13.1.4',
    'title': 'Barrier-Free Access & Universal Design for Differently Abled Persons',
    'meta_desc': 'Chapter 13 barrier-free accessibility norms under UDCPR-2020: wheelchair standards (1050x750mm), 1800mm walkways, 3.6m parking bays within 30m, 1:12 ramps, 13-passenger accessible lifts, and 1500x1750mm accessible toilet specifications.',
    'ch_slug': 'ch13',
    'ch_title': 'Chapter 13: Special Provisions for Certain Buildings',
    'badge_status': '100% COMPLETE',
    'amendment_cite': None,
    'filename': 'reg-13-1-barrier-free-access-for-differently-abled.html',
    'lesson_id': 'ch13_lesson_1',
    'quiz_id': 'quiz_ch13_1',
    'prev_url': '/lessons/reg-12-6-commercial-hospitality-sanitation-and-signs.html',
    'prev_title': 'Reg. 12.6 - 12.7 Commercial Sanitation & Display Signs',
    'next_url': '/lessons/reg-13-2-solar-and-rainwater-harvesting.html',
    'next_title': 'Reg. 13.2 - 13.3 Solar Rooftop & Rainwater Harvesting',
    'lead_summary': (
        'Universal design and barrier-free access are statutory human-rights imperatives woven directly into building sanctioning. '
        'Regulation 13.1 makes accessible architecture mandatory for all public, commercial, educational, institutional, and assembly buildings '
        'erected on plots exceeding 2,000 sq.m. From the property gate to the top floor, UDCPR establishes non-negotiable dimensions: '
        '1,800 mm wide level approach paths (max 5% slope), two dedicated 3.6-meter wide disabled parking bays located within 30 meters '
        'of the main entrance, 1:12 non-slip ramps with 800 mm handrails extending 300 mm at ends, 900 mm clear doorways with low 12 mm thresholds, '
        '1,350 mm stairways with max 12 risers, 13-passenger BIS wheelchair elevators, and fully equipped accessible toilet cubicles (min 1,500 x 1,750 mm) '
        'with 500 mm seat heights and grab rails.'
    ),
    'plain_summary_html': """
      <p>
        Barrier-free access ensures that individuals with non-ambulatory, semi-ambulatory, hearing, or visual impairments can navigate, enter, 
        and use public buildings independently and with dignity. Regulation 13.1 establishes exact architectural metrics that every municipal 
        scrutiny engineer verifies prior to building permission:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Applicability Scope (Reg 13.1.2):</strong> Applies to all buildings used by the public—including schools, colleges, hospitals, malls, commercial complexes, government offices, and theatres—<strong>constructed on plots exceeding 2,000 sq.m.</strong> (Private individual residences are exempt).</li>
        <li><strong>Standard Wheelchair Metric (Reg 13.1.1.v):</strong> The statutory dimensional baseline for all clearances is <strong>1,050 mm &times; 750 mm</strong>.</li>
        <li><strong>Site Access &amp; Surface Parking (Reg 13.1.3):</strong>
          <br>&bull; <em>Walkways:</em> Minimum <strong>1,800 mm width</strong> with an even, non-slip surface and max 5% gradient. Must incorporate tactile guiding floor materials (differing color/texture) leading from the plot gate to the building foyer.
          <br>&bull; <em>Reserved Parking:</em> Minimum <strong>2 dedicated accessible car parking bays</strong> located within a <strong>maximum travel distance of 30.0 meters</strong> from the building entrance. Each bay must have a minimum width of <strong>3.6 meters</strong> and clear wheelchair signage.
        </li>
        <li><strong>Plinth Entry &amp; Vertical Ramps (Reg 13.1.4.i to v):</strong>
          <br>&bull; <em>Ramped Approach:</em> Every building must have at least one ramped entrance. Ramp width must be at least <strong>1,800 mm</strong> with a <strong>maximum gradient of 1 : 12</strong>. Unbroken ramp length cannot exceed <strong>9.0 meters</strong> without an intermediate landing.
          <br>&bull; <em>Handrails:</em> <strong>800 mm high handrails</strong> must run on both sides, extending <strong>300 mm beyond the top and bottom</strong>, with a clear <strong>50 mm wall gap</strong>.
          <br>&bull; <em>Entrance Landing &amp; Doors:</em> Landing size must be at least <strong>1,800 mm &times; 2,000 mm</strong>. Entrance doors must provide a <strong>clear opening of at least 900 mm</strong> with raised thresholds capped at <strong>12 mm</strong>.
        </li>
        <li><strong>Internal Stairs &amp; Lifts (Reg 13.1.4.vii &amp; viii):</strong>
          <br>&bull; <em>Stairways:</em> Minimum width of <strong>1,350 mm</strong>, max 150 mm riser, min 300 mm tread (no square nosing), and <strong>maximum 12 risers per flight</strong>.
          <br>&bull; <em>Accessible Lift:</em> At least one wheelchair-compliant elevator based on a <strong>13-passenger BIS cage</strong> (clear internal dimensions <strong>1,100 mm width &times; 2,000 mm depth</strong>, 900 mm door). Lift lobby must be at least <strong>1,800 mm &times; 1,800 mm</strong>, auto door closing delay minimum <strong>5 seconds</strong>, equipped with audio floor announcements and Braille control buttons.
        </li>
        <li><strong>Accessible Toilet Core (Reg 13.1.4.ix):</strong> In every public toilet cluster, at least one unisex accessible toilet must be provided:
          <br>&bull; Minimum dimensions: <strong>1,500 mm &times; 1,750 mm</strong>.
          <br>&bull; Door must be at least 900 mm wide and <strong>must swing outward</strong> for emergency retrieval.
          <br>&bull; W.C. seat height fixed at <strong>500 mm above finished floor</strong>; vertical and horizontal grab bars with 50 mm wall clearance.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "These regulations are applicable to all buildings and facilities used by the public... constructed on plot having an area of more than 2000 sq.m... "
        "Access path from plot entry and surface parking to building entrance shall be minimum of 1800 mm. wide... Surface parking for two car spaces "
        "shall be provided near entrance for the physically handicapped persons with maximum travel distance of 30.0 m... width of parking bay shall be minimum 3.6 meter... "
        "Minimum width of ramp shall be 1800mm. with maximum gradient 1 : 12. Length of ramp shall not exceed 9.0 m. having 800 mm. high hand rail on both sides "
        "extending 300 mm. beyond top and bottom... Toilets: One special W.C. in a set of toilets... minimum size shall be 1500 mm. x 1750 mm... "
        "clear opening of the door shall be 900 mm. and the door shall swing out... W.C. seat shall be 500 mm. from the floor."
    ),
    'clause_cards_html': """
      <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
        <div class="ruled-card">
          <span class="kicker">REGULATION 13.1.2 &amp; 13.1.3</span>
          <h4 class="ruled-card-title">Scope &amp; Accessible Site Plan</h4>
          <p class="ruled-card-desc">
            Mandatory on public plots &gt; 2,000 sq.m. Site layout must feature 1,800 mm wide level walkways (max 5% slope) and 
            2 reserved accessible car parking spaces (3.6m wide) within 30 meters of the entrance porch.
          </p>
          <div class="ruled-card-footer">
            <span>SITE GEOMETRY</span>
            <span class="badge badge-status-done">3.6M PARKING &le;30M</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 13.1.4(ii) to (v)</span>
          <h4 class="ruled-card-title">Ramps, Handrails &amp; Landings</h4>
          <p class="ruled-card-desc">
            Ramps must be 1,800 mm wide with a maximum slope of 1:12 and flights capped at 9.0 meters. 
            Dual handrails at 800 mm height with 50 mm wall gaps must project 300 mm at ends. Entrance landing: 1,800 x 2,000 mm.
          </p>
          <div class="ruled-card-footer">
            <span>RAMP GEOMETRY</span>
            <span class="badge badge-status-done">1:12 / 800MM RAIL</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 13.1.4(vii) &amp; (viii)</span>
          <h4 class="ruled-card-title">13-Passenger Lifts &amp; Stairways</h4>
          <p class="ruled-card-desc">
            Stairs require 1,350 mm width, 150 mm risers, 300 mm treads, and max 12 risers/flight. 
            Wheelchair elevator requires a 13-passenger BIS cage (1,100 x 2,000 mm, 900 mm door, 5-sec door hold, and audio floor chime).
          </p>
          <div class="ruled-card-footer">
            <span>VERTICAL MOBILITY</span>
            <span class="badge badge-status-done">13-PAX BIS LIFT</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 13.1.4(ix)</span>
          <h4 class="ruled-card-title">Accessible Toilet Cubicle</h4>
          <p class="ruled-card-desc">
            Must measure at least 1,500 mm x 1,750 mm. The 900 mm clear door must swing outwards. 
            The WC pan is elevated to 500 mm height, flanked by horizontal/vertical grab rails with a 50 mm wall gap.
          </p>
          <div class="ruled-card-footer">
            <span>SANITARY CORE</span>
            <span class="badge badge-status-done">1500x1750MM OUTWARD</span>
          </div>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 13-A: BARRIER-FREE STATUTORY ARCHITECTURAL SPECIFICATIONS</span>
          <span class="badge badge-status-done">REG. 13.1</span>
        </div>

        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono);">
            <thead>
              <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:160px;">ELEMENT</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">STATUTORY MINIMUM</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">MAXIMUM THRESHOLD</th>
                <th style="padding:8px; text-align:left;">MANDATORY TECHNICAL DETAIL</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Access Walkway</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Width: <strong>1,800 mm</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Gradient: <strong>5% (1:20)</strong></td>
                <td style="padding:8px;">Even, non-slip surface, no steps, tactile guiding pavers connecting gate to foyer.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Disabled Parking</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Bay Width: <strong>3.6 meters</strong> (2 bays)</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Travel: <strong>30.0 meters</strong></td>
                <td style="padding:8px;">Nearest to main entrance, international wheelchair symbol, audible/guiding pavers.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Entry Ramp</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Width: <strong>1,800 mm</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Slope: <strong>1 : 12</strong> | Run: <strong>9.0 m</strong></td>
                <td style="padding:8px;">800 mm high handrails on both sides extending 300 mm at top/bottom; 50 mm wall gap.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Entrance Door</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Clear Opening: <strong>900 mm</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Threshold: <strong>12 mm</strong></td>
                <td style="padding:8px;">Landing min 1,800 x 2,000 mm with tactile warning floor material at top of slope.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Corridors</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Clear Width: <strong>1,500 mm</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Level Slope: <strong>1 : 12</strong></td>
                <td style="padding:8px;">Continuous tactile guiding floor material leading directly to reception, lifts &amp; toilets.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Accessible Stairs</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Width: <strong>1,350 mm</strong> | Tread: <strong>300 mm</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Riser: <strong>150 mm</strong> | Flight: <strong>12 risers</strong></td>
                <td style="padding:8px;">No abrupt square nosing; continuous handrails on both sides extending 300 mm.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Wheelchair Elevator</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Internal: <strong>1,100 &times; 2,000 mm</strong> (13-Pax)</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Door speed: <strong>0.25 m/s</strong></td>
                <td style="padding:8px;">Door hold min 5s; 900 mm door; 1,800x1,800 lobby; handrail @ 1,000 mm; audio floor voice.</td>
              </tr>
              <tr style="background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Accessible Toilet</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Internal: <strong>1,500 &times; 1,750 mm</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Seat Height: <strong>500 mm</strong></td>
                <td style="padding:8px;">Door 900 mm <strong>MUST SWING OUT</strong>; grab bars with 50 mm wall gap; washbasin inside.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
        <strong>Scenario:</strong> An architect is designing a new 5-storey Community Health &amp; Commercial Center on a <strong>3,200 sq.m plot</strong> in Aurangabad. 
        The ground floor finished plinth level is <strong>+1,200 mm above the entrance road level</strong>. 
        Dimension the statutory barrier-free access ramp, landing, parking, and toilet core under Regulation 13.1.
      </p>
      <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
        <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">STEP-BY-STEP BARRIER-FREE GEOMETRIC SIZING (REG. 13.1):</div>
        <div><strong>Step 1: Check Statutory Applicability (Reg. 13.1.2)</strong></div>
        <div>&bull; Plot area = 3,200 sq.m (&gt; 2,000 sq.m threshold) &amp; Public/Commercial occupancy &rarr; <strong>REGULATION 13.1 FULLY APPLIES</strong>.</div>
        <div style="margin-top:8px;"><strong>Step 2: Parking Allocation (Reg. 13.1.3.2)</strong></div>
        <div>&bull; Minimum 2 car parking bays reserved exclusively for wheelchair users.</div>
        <div>&bull; Width of each bay = <strong>3.60 meters</strong> (Total parking footprint = 7.20 m &times; 5.0 m).</div>
        <div>&bull; Maximum permissible distance from parking bay to building entrance porch = <strong>&le; 30.0 meters</strong>.</div>
        <div style="margin-top:8px;"><strong>Step 3: Entrance Ramp Sizing (Reg. 13.1.4.ii)</strong></div>
        <div>&bull; Total Vertical Rise = 1,200 mm (1.20 meters).</div>
        <div>&bull; Maximum Permissible Slope = 1 : 12.</div>
        <div>&bull; Total Required Ramp Run = 1.20 m &times; 12 = <strong>14.40 meters</strong>.</div>
        <div>&bull; Maximum unbroken ramp flight length = 9.0 meters &rarr; Must provide an intermediate rest landing!</div>
        <div>&bull; Design: Two equal ramp flights of <strong>7.20 meters each</strong> (1:12 slope, 1,800 mm clear width).</div>
        <div>&bull; Intermediate Landing: 1,800 mm &times; 1,800 mm. Top Entrance Landing: <strong>1,800 mm &times; 2,000 mm</strong>.</div>
        <div>&bull; Handrails: 800 mm high on both sides with 50 mm wall clearance, extending 300 mm past ends.</div>
        <div style="margin-top:8px;"><strong>Step 4: Toilet Core Sizing (Reg. 13.1.4.ix)</strong></div>
        <div>&bull; Internal Toilet Cubicle: Clear <strong>1,500 mm &times; 1,750 mm</strong>.</div>
        <div>&bull; Door: 900 mm clear leaf, fitted to <strong>SWING OUTWARD</strong> with D-pull handles.</div>
        <div>&bull; WC Pan: Centerline 450 mm from wall, seat raised to <strong>500 mm height</strong> with L-shaped 32mm dia grab rails.</div>
      </div>
    """,
    'pitfalls_html': """
      <div>
        <strong>1. Inward Swinging Toilet Doors in Accessible Cubicles (Reg 13.1.4.ix.b):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          The single most common compliance failure during site inspection is hanging an accessible toilet door to swing inwards. If a wheelchair user falls or faints inside, their body blocks an inward-opening door, preventing rescue. Reg. 13.1.4(ix)(b) mandates that the door <strong>MUST swing out</strong>.
        </p>
      </div>
      <div>
        <strong>2. Designing Ramps with Unbroken Runs Exceeding 9.0 Meters:</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Even if the slope is 1:12, a continuous uninterrupted ramp exceeding 9.0 meters causes severe physical exhaustion for self-propelled wheelchair users. Intermediate level landings of at least 1,800 mm length are mandatory every 9.0 meters of run.
        </p>
      </div>
      <div>
        <strong>3. Standard 2.5m Parking Bays for Disabled Stalls (Reg 13.1.3.2):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Marking regular 2.5m x 5.0m parking spaces with a painted wheelchair stencil is a statutory violation. A wheelchair driver requires a <strong>minimum 3.6-meter bay width</strong> to open the car door fully and deploy a wheelchair transfer hoist or ramp.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.92rem; line-height:1.6;">
        Regulation 13.1 aligns Maharashtra town planning with the statutory mandate of the 
        <strong>Rights of Persons with Disabilities (RPwD) Act, 2016</strong> and the Harmonised Guidelines 
        and Space Standards for Barrier Free Built Environment. The 13-passenger BIS elevator standard and 
        audible floor indication were specifically incorporated to ensure multi-sensory accessibility for both 
        visually and hearing impaired occupants.
      </p>
    """,
    'quiz': [
        {
            'question': 'Under UDCPR Regulation 13.1.2, what is the plot area threshold above which barrier-free provisions become mandatory for public buildings?',
            'options': [
                'Plots having an area of more than 500 sq.m.',
                'Plots having an area of more than 1,000 sq.m.',
                'Plots having an area of more than 2,000 sq.m.',
                'Plots having an area of more than 5,000 sq.m.'
            ],
            'answer': 2,
            'explanation': 'Regulation 13.1.2 explicitly restricts applicability to "all buildings and facilities used by the public... constructed on plot having an area of more than 2000 sq.m."'
        },
        {
            'question': 'What are the statutory requirements for reserved disabled car parking spaces under Regulation 13.1.3(2)?',
            'options': [
                '1 bay of 2.5m width within 50m of entrance',
                'Surface parking for 2 car spaces, minimum 3.6m width, within 30.0m of building entrance',
                '4 basement bays near the elevator core',
                'Parking is not mandatory if valet service is provided'
            ],
            'answer': 1,
            'explanation': 'Regulation 13.1.3(2) mandates surface parking for 2 car spaces near the entrance with a maximum travel distance of 30.0 meters and a minimum bay width of 3.6 meters.'
        },
        {
            'question': 'What is the maximum permissible slope and maximum unbroken flight length for an entrance ramp under Regulation 13.1.4(ii)?',
            'options': [
                'Slope 1:10, length up to 6.0 m',
                'Slope 1:12, length not exceeding 9.0 m',
                'Slope 1:15, length up to 12.0 m',
                'Slope 1:8, length not exceeding 5.0 m'
            ],
            'answer': 1,
            'explanation': 'Under Reg. 13.1.4(ii), the ramp must have a minimum width of 1,800 mm with a maximum gradient of 1:12, and its unbroken length shall not exceed 9.0 meters.'
        },
        {
            'question': 'What is the mandatory door swing direction and minimum room size for an accessible toilet under Regulation 13.1.4(ix)?',
            'options': [
                'Minimum size 1200 x 1200 mm, door must swing inward',
                'Minimum size 1500 x 1750 mm, door must swing out',
                'Minimum size 1800 x 2000 mm, sliding door only',
                'Minimum size 1000 x 1500 mm, door can swing either way'
            ],
            'answer': 1,
            'explanation': 'Regulation 13.1.4(ix) explicitly specifies: "The minimum size shall be 1500 mm. x 1750 mm... and the door shall swing out."'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
