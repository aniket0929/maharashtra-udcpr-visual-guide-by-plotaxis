"""
UDCPR Chapter 15 - Lesson 15.2: Telecommunication Infrastructure & Mobile Towers
Statutory Clauses: Regulation 15.2 & Section 154 Directives dt. 25-Aug-2023
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 15.2',
    'title': 'Telecommunication Infrastructure & Mobile Towers',
    'meta_desc': 'Master UDCPR Regulation 15.2 for Mobile Towers and Telecom Infrastructure: Ground-based towers, rooftop Base Transceiver Stations (BTS), DoT norms, the 25-Aug-2023 Section 154 Directives adopting Model Building Bye-Laws 2016, 5G small cells on street furniture, in-building fiber ducts, and structural safety certifications.',
    'ch_slug': 'ch15',
    'ch_title': 'Chapter 15: Regulations for Special Activities / Plans',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'Govt Order No. CR.179/2022/UD-13 dt. 25-Aug-2023 (Sec 154 MRTP Directives)',
    'filename': 'reg-15-2-mobile-towers-and-telecom-infrastructure.html',
    'lesson_id': 'ch15_lesson_2',
    'quiz_id': 'quiz_ch15_2',
    'prev_url': '/lessons/reg-15-1-quarrying-and-mining-operations.html',
    'prev_title': 'Reg. 15.1 Quarrying Operations',
    'next_url': '/lessons/reg-15-3-local-area-plans-and-street-design.html',
    'next_title': 'Reg. 15.3 & 15.4 Local Area Plans & Street Design Guidelines',
    'lead_summary': (
        'As high-speed digital connectivity and 5G cellular networks have become vital public infrastructure equivalent to roads and electricity, '
        'Regulation 15.2 establishes the statutory sanctioning framework for telecommunication towers, rooftop masts, and optical fiber rollouts. '
        'Permitted across all land-use zones in Maharashtra, cellular infrastructure is governed by Department of Telecommunications (DoT) '
        'guidelines and the landmark Government Order dt. 25th August 2023 issued under Section 154 of the MRTP Act. This directive mandates '
        'the inclusion of the Addendum to Model Building Bye-Laws 2016, establishing fast-track permissions for 5G small cells mounted on public '
        'street furniture, deemed Right-of-Way (RoW) for fiber optics, compulsory In-Building Solutions (IBS) for new developments, and mandatory '
        'structural stability certifications to ensure public safety.'
    ),
    'plain_summary_html': """
      <p>
        Regulation 15.2 treats cellular telecommunication as essential public utility infrastructure. Rather than subjecting mobile towers to 
        traditional building FSI scrutiny, it operates under specialized national and state digital deployment bylaws:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Universal Permissibility Across Zones (Reg 15.2):</strong>
          <br>&bull; Telecommunication Cell Sites, Base Transceiver Stations (BTS), and Ground-Based Towers (GBT) are permissible in <strong>all land-use zones</strong> (Residential, Commercial, Industrial, Agricultural, and Public-Semi-Public).
          <br>&bull; Governed strictly by the technical norms of the Department of Telecommunications (DoT), Ministry of Communications, Government of India, and the State IT Policy.
        </li>
        <li><strong>The 25th August 2023 Section 154 Directives (Model Building Bye-Laws 2016):</strong>
          <br>&bull; <em>5G Small Cell Deployment:</em> Telecommunication service providers (TSPs) and infrastructure providers (IPs) are permitted to mount <strong>low-power 5G micro-cells and small antennas</strong> on municipal street furniture, electric utility poles, bus shelters, and government buildings without undergoing cumbersome building permit procedures.
          <br>&bull; <em>Deemed Right-of-Way (RoW):</em> Clear timelines are codified for underground fiber cable trenching and overhead cabling via national portal single-window clearances.
        </li>
        <li><strong>In-Building Solutions (IBS) for New Buildings:</strong>
          <br>&bull; All newly constructed commercial complexes, high-rises, malls, and group housing projects must provide dedicated <strong>Common Telecom Ducts (CTD)</strong>, telecommunication equipment closets, and rooftop fiber access points.
          <br>&bull; Builders cannot sign exclusive access pacts with a single broadband provider; infrastructure must be open-access and shared among all licensed operators.
        </li>
        <li><strong>Rooftop Safety &amp; Structural Stability:</strong>
          <br>&bull; Any rooftop tower or antenna mast requires a <strong>Stability Certificate issued by a Licensed Structural Engineer</strong> confirming that the building slab can support the combined dead load, wind shear, and seismic forces.
          <br>&bull; Towers must be safely anchored and set back from terrace parapets to prevent hazard to pedestrians below.
        </li>
        <li><strong>EMF Radiation Compliance &amp; Billboard Ban:</strong>
          <br>&bull; Operators must submit self-declarations verifying that Electro-Magnetic Field (EMF) radiation levels conform to the stringent safety limits prescribed by the Telecom Enforcement, Resource and Monitoring (TERM) cell (1/10th of international ICNIRP levels).
          <br>&bull; <strong>Advertising Prohibitions:</strong> No commercial advertising hoardings, neon signboards, or displays are permitted on telecommunication towers or cell masts.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "15.2 ERECTION OF MOBILE TOWERS - Erection / setting up Telecommunication Cell Sites / Base Stations and installation of the equipment "
        "for Telecommunication network shall be permissible as per the norms of Department of Telecommunication / Information Technology or "
        "concerned Department of the Central / State Government. Directives u/s.154 of the M.R. & T.P. Act, 1966 by the Govt. vide Order "
        "No.CR.179/2022/UD-13, dt. 25th August, 2023 regarding inclusion of Addendum to Model Building Bye-Laws – 2016."
    ),
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-top:16px;">
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">SEC. 154 DIRECTIVES // AUG 2023</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">5G Small Cell Deployment</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            The 25-Aug-2023 Order under Section 154 MRTP Act allows low-power 5G antennas to be mounted directly on lampposts, 
            traffic poles, and transit shelters with nominal administrative fees, eliminating traditional planning permission bottlenecks.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--brick);">STRUCTURAL COMPLIANCE</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Rooftop Stability Certificates</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Every rooftop cell mast requires a structural stability audit from a Licensed Structural Engineer confirming slab 
            load-bearing capacity under maximum wind velocities. Installing rooftop steel towers without this certificate attracts immediate sealing.
          </p>
        </div>
        <div class="panel-card" style="border:1px solid var(--line); padding:16px; background:var(--surface);">
          <div class="kicker" style="color:var(--blueprint);">DIGITAL INFRASTRUCTURE</div>
          <h4 style="margin:6px 0 10px 0; font-size:1.05rem;">Mandatory In-Building Ducts</h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Architects must include shared vertical telecom risers, cable trays, and ground-floor telecommunication utility rooms in building plans. 
            Monopolistic exclusive provider agreements are legally prohibited.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="overflow-x:auto; margin-top:12px;">
        <div class="kicker" style="color:var(--blueprint); margin-bottom:6px;">DIGITAL INFRASTRUCTURE CLASSIFICATION PLATE // TELECOM &amp; 5G DEPLOYMENT</div>
        <table class="blueprint-table" style="width:100%; border-collapse:collapse; font-size:0.88rem;">
          <thead>
            <tr style="background:var(--surface-tint); border-bottom:2px solid var(--line-bold);">
              <th style="padding:10px; text-align:left;">Facility Type</th>
              <th style="padding:10px; text-align:left;">Permissible Location</th>
              <th style="padding:10px; text-align:left;">Key Technical Pre-requisites</th>
              <th style="padding:10px; text-align:left;">Regulatory Approvals Required</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Ground-Based Tower (GBT)</strong></td>
              <td style="padding:10px;">All zones on independent plots or layout open spaces</td>
              <td style="padding:10px;">Setback equal to height/clear fall zone; perimeter security fencing; lightning arrestor.</td>
              <td style="padding:10px;">Planning Authority permission, SACFA clearance, TERM cell EMF registration.</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>Rooftop Tower / Pole (RTT)</strong></td>
              <td style="padding:10px;">Terraces of authorized buildings in any zone</td>
              <td style="padding:10px;">Licensed Structural Engineer Stability Certificate; building age and dead-load verification.</td>
              <td style="padding:10px;">Building owner / CHS NOC, Municipal telecom registration, TERM cell filing.</td>
            </tr>
            <tr style="border-bottom:1px solid var(--line);">
              <td style="padding:10px;"><strong>5G Small Cells (Aug 2023 Order)</strong></td>
              <td style="padding:10px;">Street lights, utility poles, bus stops, civic kiosks</td>
              <td style="padding:10px;">Low-power non-ionizing radiation; aesthetic camouflage; compact form factor.</td>
              <td style="padding:10px;">Nominal Right-of-Way (RoW) administrative intimation; fast-track single window.</td>
            </tr>
            <tr style="border-bottom:2px solid var(--line-bold); background:var(--surface-tint);">
              <td style="padding:10px;"><strong>In-Building Solutions (IBS)</strong></td>
              <td style="padding:10px;">Internal shafts in all buildings &gt; 15m or commercial</td>
              <td style="padding:10px;">Shared vertical telecom conduits, fiber distribution boxes, multi-operator access.</td>
              <td style="padding:10px;">Mandatory verification prior to grant of final Occupancy Certificate (OC).</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,
    'worked_example_html': """
      <div style="line-height:1.6; font-size:0.92rem;">
        <h4 style="margin:0 0 8px 0; color:var(--amber-dark);">Scenario: Rooftop Cellular Antenna Sanction on an Existing Commercial Tower</h4>
        <p>
          A licensed telecom infrastructure provider applies under Regulation 15.2 to install a <strong>9.0-meter rooftop tubular steel mast</strong> 
          with three directional 5G antennas and equipment cabins on a <strong>24.0-meter tall commercial building</strong> in Chhatrapati Sambhajinagar. 
          The building was constructed 12 years ago with an approved OC. 
          Outline the technical scrutiny verification steps and mandatory documentation required.
        </p>
        <div style="background:var(--surface); border:1px solid var(--line); padding:12px; margin:10px 0; font-family:var(--mono); font-size:0.85rem;">
          1. Legal Title &amp; Zoning Scrutiny:<br>
          &nbsp;&nbsp;&bull; Zoning = Commercial Zone &rarr; Cellular infrastructure is permissible in all zones per Reg 15.2.<br>
          &nbsp;&nbsp;&bull; Property Status = Authorized building with valid Occupancy Certificate (OC).<br>
          &nbsp;&nbsp;&bull; Consent = Registered Leave &amp; License agreement with the building owner / society.<br><br>
          2. Structural Stability Verification (Mandatory Safety Gate):<br>
          &nbsp;&nbsp;&bull; Building Height = 24.0 meters; New Tower Height = 9.0 meters (Total top elevation = 33.0m).<br>
          &nbsp;&nbsp;&bull; The applicant must submit a <strong>Structural Stability Certificate</strong> signed by a registered Licensed Structural Engineer.<br>
          &nbsp;&nbsp;&bull; The certificate must certify that the existing RCC roof slab and columns have adequate reserve capacity to sustain:<br>
          &nbsp;&nbsp;&nbsp;&nbsp;&bull; Equipment dead load (approx. 2,500 kg including base frames and battery banks)<br>
          &nbsp;&nbsp;&nbsp;&nbsp;&bull; Design wind pressure for 39 m/s zone per IS:875 (Part 3) acting on the 9m lattice mast.<br><br>
          3. Height &amp; Aviation Clearance:<br>
          &nbsp;&nbsp;&bull; Total structure height = 33.0m.<br>
          &nbsp;&nbsp;&bull; If within Airport Colour Coded Zoning Map (CCZM) funnel, verify with AAI NOC or online self-declaration.<br><br>
          4. Radiation &amp; Commercial Restrictions (Reg 15.2):<br>
          &nbsp;&nbsp;&bull; Operator submits self-declaration of adherence to DoT/TERM cell EMF radiation thresholds.<br>
          &nbsp;&nbsp;&bull; <strong>Strict Prohibition:</strong> No commercial hoardings or advertising signs may be mounted on the tower mast.<br><br>
          5. Municipal Telecom Registration Fee:<br>
          &nbsp;&nbsp;&bull; One-time administrative fee remitted to the Municipal Corporation under prevailing municipal telecom policy.
        </div>
        <p style="font-size:0.85rem; color:var(--ink-soft); margin:0;">
          <strong>Compliance Verdict:</strong> Upon submission of the Structural Engineer stability endorsement and TERM cell self-declaration, the Planning Authority issues an administrative permit without deducting any FSI from the building potential.
        </p>
      </div>
    """,
    'pitfalls_html': """
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 1: Installing Rooftop Towers Without a Structural Stability Certificate</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Erecting heavy steel lattice towers and generator sets on residential roof slabs without an authenticated Licensed Structural Engineer stability certificate poses extreme collapse hazards during cyclones. Uncertified towers are subject to immediate municipal disconnection and demolition.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 2: Treating Telecom Towers as Countable Floor Space (FSI)</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Telecommunication towers, antenna masts, and prefabricated equipment shelters are essential infrastructure and are <strong>100% exempt from FSI computation</strong>. Municipal scrutiny officers cannot demand premium FSI or TDR loading for mobile tower installation.
        </p>
      </div>
      <div style="border-left:3px solid var(--brick); padding-left:12px;">
        <strong>Pitfall 3: Monopolistic In-Building Broadband Agreements</strong>
        <p style="font-size:0.88rem; color:var(--ink-soft); margin:4px 0 0 0;">
          Under the 25-Aug-2023 directives adopting Model Building Bye-Laws, developers cannot enter into exclusive single-operator agreements that block competing telecom or fiber providers from accessing common internal conduit shafts.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.9rem; line-height:1.6; margin:0 0 10px 0;">
        <strong>Directives u/s 154 MRTP Act dt. 25th August 2023:</strong> Formally incorporated the Addendum to Model Building Bye-Laws 2016 for 
        Digital Communication Infrastructure, standardizing 5G small cell deployment, deemed Right-of-Way (RoW) clearances, and mandatory in-building telecom shafts across Maharashtra.
      </p>
    """,
    'quiz': [
        {
            'question': 'In which land-use zones is the erection of telecommunication cell sites and mobile towers permissible under Regulation 15.2?',
            'options': [
                'Commercial and Industrial zones only',
                'Exclusively on government-owned plots',
                'All land-use zones across Maharashtra',
                'Only outside municipal limits'
            ],
            'answer': 2,
            'explanation': 'Under Regulation 15.2 and DoT guidelines, telecommunication infrastructure is an essential public utility permissible across all land-use zones.'
        },
        {
            'question': 'What key reform did the Government Order dt. 25th August 2023 introduce under Section 154 of the MRTP Act?',
            'options': [
                'Complete ban on mobile towers in residential areas',
                'Adoption of the Addendum to Model Building Bye-Laws 2016 for fast-track 5G small cells and digital infrastructure',
                'Levying 50% extra development charge on mobile towers',
                'Transfer of all mobile towers to the Public Works Department'
            ],
            'answer': 1,
            'explanation': 'The 25-Aug-2023 Order incorporated the Addendum to Model Building Bye-Laws 2016, enabling streamlined 5G small cell deployment on street furniture and mandatory in-building telecom ducts.'
        },
        {
            'question': 'What mandatory technical document must be submitted before installing a rooftop mobile tower on any building?',
            'options': [
                'Environmental Impact Assessment (EIA) report',
                'Structural Stability Certificate issued by a Licensed Structural Engineer',
                'Property tax exemption receipt',
                'Traffic congestion study'
            ],
            'answer': 1,
            'explanation': 'A Structural Stability Certificate from a Licensed Structural Engineer is mandatory to certify that the building slab can support the dead load and wind shear forces of the tower.'
        },
        {
            'question': 'Are commercial advertising display signs and hoardings permitted on telecommunication towers?',
            'options': [
                'Yes, on paying additional municipal advertising fees',
                'Yes, if illuminated with LED panels',
                'Strictly prohibited on telecommunication towers and cell masts',
                'Permitted in industrial zones only'
            ],
            'answer': 2,
            'explanation': 'Commercial advertisements and outdoor display hoardings are strictly prohibited on telecommunication infrastructure.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
