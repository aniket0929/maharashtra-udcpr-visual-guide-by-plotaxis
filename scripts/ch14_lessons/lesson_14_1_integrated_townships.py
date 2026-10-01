"""
UDCPR Chapter 14 - Lesson 14.1: Integrated Township Projects (ITP) - Mega-City Master Planning
Statutory Clauses: Regulation 14.1 (14.1.1.1 to 14.1.1.16, Tables 14-A to 14-J)
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 14.1 & Tables 14-A to 14-J',
    'title': 'Integrated Township Projects (ITP) - Mega-City Master Planning',
    'meta_desc': 'Master UDCPR Regulation 14.1 for Integrated Township Projects (ITP): 40-Hectare minimum contiguous land threshold, 18m access roads, zoning balance (60% Res, 10% Comm, 10% Open, 15% Roads), Tables 14-A to 14-J public amenity plates, 20% social housing handover, and up to 2.00 FSI.',
    'ch_slug': 'ch14',
    'ch_title': 'Chapter 14: Special Schemes',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'Urban Development Department Notifications on ITP Policy',
    'filename': 'reg-14-1-integrated-township-projects.html',
    'lesson_id': 'ch14_lesson_1',
    'quiz_id': 'quiz_ch14_1',
    'prev_url': '/lessons/reg-13-4-disaster-fire-towers-electrical.html',
    'prev_title': 'Reg. 13.6 Disaster Resilience & Fire Towers (Oct 2024)',
    'next_url': '/lessons/reg-14-2-transit-oriented-development.html',
    'next_title': 'Reg. 14.2 Transit Oriented Development (TOD)',
    'lead_summary': (
        'To prevent chaotic urban sprawl and establish self-sustaining, high-technology satellite cities across Maharashtra, '
        'Regulation 14.1 codifies the Integrated Township Projects (ITP) policy. An ITP is a comprehensive private smart-city development '
        'mandating a minimum contiguous land area of 40 Hectares (approx. 100 acres) accessed by an 18-meter public road. '
        'The developer operates as a master infrastructure provider, constructing self-reliant water treatment, electrical substations, '
        'and zero-discharge sewage systems. In exchange for surrendering 20% of residential area for EWS/LIG social housing and providing '
        'full civic amenities under Tables 14-A to 14-J (schools, 50-bed hospitals, fire stations, police headquarters), the state unlocks '
        'massive economic benefits: total permissible FSI up to 2.00 on gross land, floating FSI across the masterplan, deemed Non-Agricultural '
        '(NA) status, and a 50% concession on stamp duty.'
    ),
    'plain_summary_html': """
      <p>
        Building a standalone building is architecture; building an Integrated Township Project is regional nation-building. 
        Regulation 14.1 provides the statutory legal and spatial framework for master-planned smart cities in both Regional Plan (RP) 
        and Development Plan (DP) areas across Maharashtra:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Scale &amp; Access Pre-requisites (Reg 14.1.1.2):</strong>
          <br>&bull; <em>Minimum Contiguous Area:</em> The project must have a single contiguous land holding of at least <strong>40 Hectares (100 Acres)</strong>. (Can be in agricultural, residential, or industrial zones).
          <br>&bull; <em>External Access Road:</em> Must connect directly to an existing or proposed public road of at least <strong>18.0 meters width</strong>.
          <br>&bull; <em>Water Autonomy:</em> The project proponent must establish an independent, verified water source (dams, rivers, or bore fields) capable of supplying the entire town; it cannot rely on existing municipal water quotas.
        </li>
        <li><strong>Mandatory Land Use Zoning Balance (Reg 14.1.1.7):</strong>
          <br>&bull; <em>Residential Zone:</em> Maximum <strong>60% of gross layout area</strong>.
          <br>&bull; <em>Commercial Zone:</em> Minimum <strong>10% of gross layout area</strong> (retail, corporate offices, IT parks, hospitality).
          <br>&bull; <em>Public Parks &amp; Open Spaces:</em> Minimum <strong>10% of gross layout area</strong> (exclusive of individual plot open spaces).
          <br>&bull; <em>Road Network &amp; Circulation:</em> Minimum <strong>15% of gross layout area</strong> (arterial roads min 18m, sub-arterials min 12m).
          <br>&bull; <em>Public Amenities &amp; Utilities:</em> Balance <strong>5% of gross area</strong> dedicated to social infrastructure.
        </li>
        <li><strong>Civic Infrastructure Schedules (Tables 14-A to 14-J):</strong> The developer must construct and hand over key public amenities:
          <br>&bull; <em>Education (Table 14-A):</em> Primary schools, high schools, and technical junior colleges per population tier.
          <br>&bull; <em>Healthcare (Table 14-C):</em> Community health center and a <strong>minimum 50-bed hospital</strong>.
          <br>&bull; <em>Civic Security (Tables 14-E &amp; 14-F):</em> Dedicated <strong>Fire Brigade Station</strong> (equipped with fire engines) and <strong>Police Station</strong> with staff quarters.
          <br>&bull; <em>Utilities (Tables 14-G to 14-J):</em> 100% underground sewerage network, Sewage Treatment Plant (STP), Water Treatment Plant (WTP), and a dedicated 33/11 kV Electric Sub-station.
        </li>
        <li><strong>Social Housing Obligation (Reg 14.1.1.9):</strong>
          <br>&bull; Exactly <strong>20% of the total residential built-up area</strong> must be developed as Social Housing for Economically Weaker Sections (EWS, carpet area up to 30 sq.m) and Low Income Groups (LIG, carpet area up to 50 sq.m).
          <br>&bull; EWS/LIG tenements must be handed over to MHADA or allotted through transparent lottery at subsidized PWD DSR construction rates.
        </li>
        <li><strong>FSI Mechanics &amp; State Concessions (Reg 14.1.1.8 &amp; 14.1.1.13):</strong>
          <br>&bull; <em>FSI Potential:</em> Basic FSI of <strong>1.00 on the entire gross land area</strong>, expandable up to <strong>1.70 or 2.00 FSI</strong> upon payment of a concessional premium (calculated at 10% to 20% of ASR land rate).
          <br>&bull; <em>Floating FSI:</em> Built-up potential can be floated freely between clusters and high-density sectors across the 40-Ha masterplan.
          <br>&bull; <em>Statutory Concessions:</em> <strong>50% exemption on Stamp Duty</strong> for the first sale of land/tenements, deemed Non-Agricultural (NA) conversion, and single-window sanction by a Special High Power Committee.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "Applicability of Integrated Township Projects (ITP): The project shall have a minimum contiguous area of 40.0 Ha. (100 Acres)... "
        "The project shall have an access by public road of width not less than 18.0 m... Planning Considerations: Residential: Maximum 60% of gross layout area; "
        "Commercial: Minimum 10%; Public Open Space: Minimum 10%; Roads and Circulation: Minimum 15%... The developer shall construct social housing "
        "to the extent of 20% of the residential built up area for EWS / LIG... Permissible FSI: Basic FSI of 1.00 on gross area... Additional FSI up to "
        "1.70 / 2.00 on payment of premium... 50% concession in stamp duty for the first transaction."
    ),
    'clause_cards_html': """
      <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
        <div class="ruled-card">
          <span class="kicker">REGULATION 14.1.1.2</span>
          <h4 class="ruled-card-title">40 Hectares &amp; 18m Access Road</h4>
          <p class="ruled-card-desc">
            Establishes the entry barrier: minimum 40 Ha (100 acres) of contiguous unencumbered land accessed by an 18-meter road. 
            Permitted in Agricultural and Regional Plan zones, unlocking massive land value through masterplan conversion.
          </p>
          <div class="ruled-card-footer">
            <span>SITE CRITERIA</span>
            <span class="badge badge-status-done">40 HA / 18M ROAD</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 14.1.1.7</span>
          <h4 class="ruled-card-title">Masterplan Zoning Ratios (60-10-10-15)</h4>
          <p class="ruled-card-desc">
            Statutory land allocation: max 60% Residential, min 10% Commercial, min 10% Public Green Parks, min 15% Roads &amp; Transport, 
            and 5% Social Utilities, creating an intrinsically balanced walk-to-work urban fabric.
          </p>
          <div class="ruled-card-footer">
            <span>ZONING MIX</span>
            <span class="badge badge-status-done">60:10:10:15 RATIO</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 14.1.1.9</span>
          <h4 class="ruled-card-title">20% EWS / LIG Social Housing</h4>
          <p class="ruled-card-desc">
            Developer must construct 20% of total residential built-up area as affordable housing (EWS up to 30 sqm, LIG up to 50 sqm). 
            Units are surrendered to MHADA or allotted to qualifying low-income citizens at controlled PWD rates.
          </p>
          <div class="ruled-card-footer">
            <span>SOCIAL INCLUSION</span>
            <span class="badge badge-status-done">20% AFFORDABLE</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 14.1.1.8 &amp; 13</span>
          <h4 class="ruled-card-title">2.00 FSI Potential &amp; 50% Stamp Rebate</h4>
          <p class="ruled-card-desc">
            Base FSI 1.00 on gross plot, expandable to 2.00 FSI with floating FSI across sectors. 
            Supported by 50% stamp duty exemption, automatic deemed NA conversion, and fast-track single-window sanctions.
          </p>
          <div class="ruled-card-footer">
            <span>FISCAL &amp; DENSITY</span>
            <span class="badge badge-status-done">2.00 FSI / 50% STAMP</span>
          </div>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 14-A: INTEGRATED TOWNSHIP (ITP) MASTERPLAN ALLOCATION &amp; AMENITIES</span>
          <span class="badge badge-status-done">REG. 14.1 &amp; TABLES 14-A TO 14-J</span>
        </div>

        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono); margin-bottom:16px;">
            <thead>
              <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">LAND USE COMPONENT</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:150px;">STATUTORY SHARE</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">40-HA BASELINE AREA</th>
                <th style="padding:8px; text-align:left;">MANDATORY PLANNING CONDITIONS</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Residential Zone</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Maximum <strong>60%</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">24.0 Hectares (max)</td>
                <td style="padding:8px;">Exactly 20% of built-up residential area reserved for EWS (&le;30 sqm) &amp; LIG (&le;50 sqm) social housing.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Commercial &amp; Business</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Minimum <strong>10%</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">4.0 Hectares (min)</td>
                <td style="padding:8px;">Corporate offices, IT/ITES hubs, organized retail malls, hotels, and entertainment complexes.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Public Open Spaces &amp; Parks</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Minimum <strong>10%</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">4.0 Hectares (min)</td>
                <td style="padding:8px;">Central public parks, green corridors, and sports complexes. Completely free from building footprints.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Roads &amp; Circulation</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Minimum <strong>15%</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">6.0 Hectares (min)</td>
                <td style="padding:8px;">Main arterial roads min 18m width; sub-arterials min 12m; dedicated cycle tracks and pedestrian walkways.</td>
              </tr>
              <tr style="background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Public Amenities &amp; Utilities</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Balance <strong>5%</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">2.0 Hectares</td>
                <td style="padding:8px;">Schools (14-A), 50-bed hospital (14-C), Fire Station (14-E), Police Station (14-F), STP, WTP &amp; Substation.</td>
              </tr>
            </tbody>
          </table>

          <div style="font-size:12px; font-weight:700; color:var(--blueprint); margin-bottom:8px;">KEY CIVIC AMENITY SIZING BENCHMARKS (TABLES 14-A TO 14-J)</div>
          <div style="border:1px dashed var(--ink); padding:12px; font-size:0.86rem; line-height:1.6;">
            <div>&bull; <strong>Schools (Table 14-A):</strong> 1 Primary School (min 2,000 sqm plot) + 1 High School (min 4,000 sqm plot with playground) per 5,000 population.</div>
            <div>&bull; <strong>Hospital (Table 14-C):</strong> Minimum 1 Community Hospital of 50-bed capacity on a minimum 4,000 sqm site, fully equipped with casualty and ambulance bays.</div>
            <div>&bull; <strong>Fire Brigade Station (Table 14-E):</strong> Minimum 1 Fire Station on a 2,000 sqm plot with 2 bays and staff quarters, handed over to the local Authority.</div>
            <div>&bull; <strong>Police Station (Table 14-F):</strong> Minimum 1 Police Station (min 1,000 sqm plot) with lock-up and control room, handed over to Home Department.</div>
            <div>&bull; <strong>Zero-Discharge Utilities (Table 14-G to 14-J):</strong> 100% STP treated effluent reused in township flushing/gardening; municipal solid waste processing on site.</div>
          </div>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
        <strong>Scenario:</strong> A consortium of land owners and a developer assemble a contiguous parcel of <strong>50 Hectares (500,000 sq.m)</strong> 
        in a Regional Plan area abutting a 24-meter state highway near Pune. They apply for sanction as an Integrated Township Project (ITP) 
        seeking the maximum permissible FSI of <strong>1.80</strong>. Calculate the statutory land use budget, social housing allocation, 
        and total development potential.
      </p>
      <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
        <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">MASTERPLAN COMPUTATION &amp; SOCIAL HOUSING BUDGET (REG. 14.1):</div>
        <div><strong>Step 1: Check Statutory Thresholds (Reg. 14.1.1.2)</strong></div>
        <div>&bull; Land Area = 50 Ha (&gt; 40 Ha minimum requirement) &amp; Access Road = 24m (&gt; 18m minimum requirement) &rarr; <strong>ELIGIBLE FOR ITP SANCTION</strong>.</div>
        <div style="margin-top:8px;"><strong>Step 2: Land Use Budget (Reg. 14.1.1.7)</strong></div>
        <div>&bull; Gross Land Footprint = 500,000 sq.m (50 Hectares).</div>
        <div>&bull; <strong>Residential Area (Max 60%):</strong> 500,000 &times; 60% = <strong>300,000 sq.m (30 Ha)</strong>.</div>
        <div>&bull; <strong>Commercial Area (Min 10%):</strong> 500,000 &times; 10% = <strong>50,000 sq.m (5 Ha)</strong>.</div>
        <div>&bull; <strong>Public Open Space (Min 10%):</strong> 500,000 &times; 10% = <strong>50,000 sq.m (5 Ha)</strong>.</div>
        <div>&bull; <strong>Roads &amp; Transport (Min 15%):</strong> 500,000 &times; 15% = <strong>75,000 sq.m (7.5 Ha)</strong>.</div>
        <div>&bull; <strong>Public Civic Amenities (5%):</strong> 500,000 &times; 5% = <strong>25,000 sq.m (2.5 Ha)</strong> (Schools, Hospital, Fire Station, STP).</div>
        <div style="margin-top:8px;"><strong>Step 3: Total Permissible Built-Up Area (Reg. 14.1.1.8)</strong></div>
        <div>&bull; Total Permissible FSI = 1.80 on Gross Land Area (500,000 sq.m).</div>
        <div>&bull; <strong>Total Permissible Built-Up Area</strong> = 500,000 &times; 1.80 = <strong>900,000 sq.m</strong>.</div>
        <div>&bull; Basic FSI component (1.00) = 500,000 sq.m (Premium free).</div>
        <div>&bull; Premium FSI component (0.80) = 400,000 sq.m (Paid at 20% ASR rate).</div>
        <div style="margin-top:8px;"><strong>Step 4: Social Housing Allocation (Reg. 14.1.1.9)</strong></div>
        <div>&bull; Assuming 75% of total BUA is built in residential sectors = 900,000 &times; 75% = 675,000 sq.m residential BUA.</div>
        <div>&bull; Mandatory Social Housing (20%): 675,000 &times; 20% = <strong>135,000 sq.m of EWS / LIG tenements</strong>.</div>
        <div>&bull; If divided equally: 67,500 sq.m for EWS (30 sqm each = 2,250 units) + 67,500 sq.m for LIG (50 sqm each = 1,350 units).</div>
        <div>&bull; <strong>Total Social Tenements Created: 3,600 affordable homes</strong> handed over to MHADA / Authority.</div>
      </div>
    """,
    'pitfalls_html': """
      <div>
        <strong>1. Submitting Non-Contiguous Parcels Separated by Private Lands (Reg 14.1.1.2):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Developers often assemble 45 Hectares consisting of two 22.5-Ha pockets separated by unacquired private agricultural fields. Regulation 14.1.1.2 explicitly mandates that the 40 Hectares must be <strong>strictly contiguous</strong>. If parcels are bisected by private lands (other than state highways or natural canals with approved bridge crossings), the application is rejected.
        </p>
      </div>
      <div>
        <strong>2. Commercial Zone Under-Allocation (Reg 14.1.1.7):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Attempting to allocate 80% to residential housing and only 5% to commercial use is an automatic ground for rejection. The minimum 10% commercial land allocation is non-negotiable, ensuring that the township generates local employment rather than acting as a dormitory suburb.
        </p>
      </div>
      <div>
        <strong>3. Treating Social Housing (20%) as an Optional Cash Buyout:</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Unlike standard municipal Inclusive Housing (Reg. 3.8) where small plots can pay premium in lieu of land, Regulation 14.1.1.9 mandates the <strong>physical construction and delivery</strong> of 20% EWS/LIG tenements. Developers cannot buy out this obligation with monetary compensation.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.92rem; line-height:1.6;">
        The Integrated Township Project policy was comprehensively updated under UDCPR-2020 and subsequent Urban Development Department 
        directives. Key modifications streamlined the transition policy (Reg. 14.1.1.14) for older Special Township Projects sanctioned under 
        pre-2020 regional plans, permitting them to migrate to the enhanced 2.00 FSI potential upon harmonizing their civic amenity reserves 
        with Tables 14-A to 14-J and fulfilling the 20% social housing quota.
      </p>
    """,
    'quiz': [
        {
            'question': 'Under UDCPR Regulation 14.1.1.2, what is the minimum contiguous land area required to establish an Integrated Township Project (ITP)?',
            'options': [
                '10 Hectares (25 Acres)',
                '20 Hectares (50 Acres)',
                '40 Hectares (100 Acres)',
                '100 Hectares (250 Acres)'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.1.1.2 explicitly dictates: "The project shall have a minimum contiguous area of 40.0 Ha. (100 Acres)."'
        },
        {
            'question': 'What is the minimum width of the public access road required to connect an Integrated Township Project under Regulation 14.1.1.2?',
            'options': [
                '12.0 meters',
                '15.0 meters',
                '18.0 meters',
                '24.0 meters'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.1.1.2 mandates that the project must have access by a public road of width not less than 18.0 meters.'
        },
        {
            'question': 'What percentage of the residential built-up area must be developed as EWS / LIG Social Housing under Regulation 14.1.1.9?',
            'options': [
                '10% of residential built-up area',
                '15% of residential built-up area',
                '20% of residential built-up area',
                '30% of residential built-up area'
            ],
            'answer': 2,
            'explanation': 'Regulation 14.1.1.9 explicitly states: "The developer shall construct social housing to the extent of 20% of the residential built up area for EWS / LIG."'
        },
        {
            'question': 'What statutory stamp duty concession is granted for the first transaction in an Integrated Township Project under Regulation 14.1.1.13?',
            'options': [
                '10% concession',
                '25% concession',
                '50% concession in stamp duty',
                '100% full waiver for 20 years'
            ],
            'answer': 2,
            'explanation': 'Under Reg. 14.1.1.13(a), the developer and purchasers enjoy a "50% concession in stamp duty for the first transaction."'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
