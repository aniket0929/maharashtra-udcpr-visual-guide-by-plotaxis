"""
UDCPR Chapter 13 - Lesson 13.4: Disaster Resilience, Fire Towers & Electrical Safety
Statutory Clauses: Regulation 13.6 (Inserted vide Gazette Notification 10th October, 2024)
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 13.6 (Oct 2024)',
    'title': 'Disaster Resilience, Fire Towers & Electrical Safety',
    'meta_desc': 'Chapter 13 breakthrough regulations under Gazette Notification dt. 10th October, 2024: Reg 13.6 disaster resilience (BUA > 10,000 sqm or 1,000+ occupants), 2-hour Fire Towers with fireman lifts, 90m+ fire break water tanks at 65m intervals, and mandatory Licensed Electrical Engineers.',
    'ch_slug': 'ch13',
    'ch_title': 'Chapter 13: Special Provisions for Certain Buildings',
    'badge_status': '100% COMPLETE',
    'amendment_cite': 'Notification No. CR.45/2022/UD-11 dt. 10-10-2024',
    'filename': 'reg-13-4-disaster-fire-towers-electrical.html',
    'lesson_id': 'ch13_lesson_4',
    'quiz_id': 'quiz_ch13_4',
    'prev_url': '/lessons/reg-13-3-grey-water-and-solid-waste.html',
    'prev_title': 'Reg. 13.4 - 13.5 Grey Water & Solid Waste Management',
    'next_url': '/chapters/ch13.html',
    'next_title': 'Chapter 13 Syllabus',
    'lead_summary': (
        'On 10th October, 2024, the Urban Development Department of Maharashtra issued a landmark statutory notification (No. CR.45/2022/UD-11) '
        'inserting Regulation 13.6 into UDCPR-2020: Special Safety Control Regulations for Buildings Vulnerable to Man-Made Disasters. '
        'Targeting high-consequence structures—developments exceeding 10,000 sq.m built-up area or 1,000 occupants (malls, hospitals, universities, '
        'financial exchanges like BSE/WTC, and police-identified government headquarters)—this regulation establishes three game-changing engineering mandates: '
        'First, mandatory 2-hour fire-resistant Fire Towers with integrated fireman evacuation lifts and ventilated lobbies, which statutorily exempts '
        'the project from duplicate secondary staircases. Second, for super-tall buildings of 90 meters and above, dedicated intermediate fire break water '
        'tanks and booster pumps must be installed at every 65-meter vertical height interval. Third, the regulation mandates the formal appointment of '
        'a Licensed Electrical Engineer, backed by supervisory certificates, mandatory 5-year periodic recertification, and strict statutory penalties '
        'including license revocation, power disconnection, and immediate withdrawal of the Occupancy Certificate.'
    ),
    'plain_summary_html': """
      <p>
        The October 2024 notification fundamentally transforms high-rise fire safety and electrical engineering across urban Maharashtra. 
        Regulation 13.6 establishes the following non-negotiable statutory controls:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Statutory Applicability Criteria (Reg 13.6.A):</strong>
          <br>&bull; <em>Scale Trigger:</em> Any building having a <strong>built-up area exceeding 10,000 sq.m OR an occupancy of over 1,000 persons</strong>.
          <br>&bull; <em>Occupancy Classes:</em> Assembly halls, registered healthcare trusts and hospitals, educational schools/colleges, shopping malls, major markets, religious sanctuaries, tourist landmarks, and corporate business headquarters (e.g. Stock Exchange, World Trade Centre).
          <br>&bull; <em>Vulnerable Government Buildings:</em> Any state/civic building designated as vulnerable by the Police (Additional Commissioner of Police, Protection &amp; Security in Mumbai; DCP Special Branch in Commissionerates; SP in Districts).
        </li>
        <li><strong>Mandatory 2-Hour Fire Towers (Reg 13.6.B):</strong>
          <br>&bull; Every Special Building must provide a <strong>Fire Tower with minimum 2 hours fire resistance</strong>.
          <br>&bull; The Fire Tower must integrate a <strong>fireman evacuation lift with a naturally or mechanically ventilated lobby</strong> directly attached to the fire escape staircase landing.
          <br>&bull; <strong>Major Statutory Exemption (Note to Clause B):</strong> Providing a conforming Fire Tower officially <strong>exempts the building from providing a second lift or second staircase</strong> otherwise required under generic high-rise regulations!
        </li>
        <li><strong>Fire Break Water Tanks at 65m Intervals (Reg 13.6.C):</strong>
          <br>&bull; In all Special Buildings with a <strong>height of 90 meters and above</strong>, the developer must install intermediate <strong>fire break water tanks with independent fire booster pumps at every 65-meter vertical height interval</strong> from ground level.
          <br>&bull; These break tanks can be located on service floors, intermediate refuge floors, or designated MEP staging decks per Annexure-D.
        </li>
        <li><strong>Licensed Electrical Engineer Protocol (Reg 13.6.D to H):</strong>
          <br>&bull; Developers must formally appoint a registered <strong>Licensed Electrical Engineer</strong> under Appendix-C.
          <br>&bull; A Certificate of Supervision must be filed at the initial Notice of Intention, followed by a formal Completion Certificate prior to Occupancy Certificate (OC).
          <br>&bull; Any misrepresentation or execution defect leads to <strong>immediate license revocation and professional debarment</strong>.
        </li>
        <li><strong>Perpetual Post-Completion Inspections &amp; Enforcement (Reg 13.6.I):</strong>
          <br>&bull; <em>5-Year Periodic Recertification:</em> Electrical systems across all flats, shops, and common cores must be physically inspected and certified by a Licensed Electrical Engineer <strong>at least once every 5 years</strong>.
          <br>&bull; <em>Conditions on OC:</em> These maintenance mandates are written directly into the statutory Occupancy Certificate and must be displayed publicly in the building lobby.
          <br>&bull; <em>Drastic Penalties:</em> Failure to maintain fire installations leads to <strong>immediate cancellation/withdrawal of the Occupancy Certificate</strong>; failure to certify electrical systems results in <strong>disconnection of electrical power supply by the power utility company</strong>!
        </li>
      </ul>
    """,
    'statutory_extract': (
        "SPECIAL SAFETY CONTROL REGULATIONS FOR BUILDINGS VULNERABLE TO MAN-MADE DISASTERS (Inserted vide Notification dt. 10th October, 2024)... "
        "applicable for all buildings fulfilling the criteria of: Having built up area exceeding 10,000 sq.m. or occupancy over the 1000 persons... "
        "Every Special building shall be provided with Fire Towers having minimum 2 hours fire resistance, consisting of a fireman evacuation lift "
        "with a ventilated lobby as an integral part of fire escape staircase... Other provisions in the sanctioned DCPR with regards to the applicability "
        "of a second lift, second staircase for high-rise / Special buildings shall not be applicable after provision of a Fire Tower... "
        "Special buildings with height 90 m. and above shall be provided with fire break water tank system with fire pumps at every 65 m. height interval... "
        "electrical installations shall be inspected periodically at least once in 5 year... Failure to maintain fire installations may lead to withdrawal "
        "of Occupation Certificate... Failure to maintain electrical installations may lead to disconnection of power supply by Power Supply Company."
    ),
    'clause_cards_html': """
      <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
        <div class="ruled-card">
          <span class="kicker">OCTOBER 2024 GAZETTE</span>
          <h4 class="ruled-card-title">Reg. 13.6 Disaster Risk Criteria</h4>
          <p class="ruled-card-desc">
            Enacted under Notification No. CR.45/2022/UD-11. Covers buildings &gt; 10,000 sq.m BUA or &gt; 1,000 occupants, 
            including malls, hospitals, universities, corporate headquarters, and police-designated sensitive government complexes.
          </p>
          <div class="ruled-card-footer">
            <span>NOTIFICATION UD-11</span>
            <span class="badge badge-status-done">&gt;10K SQ.M / &gt;1K OCCUPANTS</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">CLAUSE B &amp; NOTE</span>
          <h4 class="ruled-card-title">2-Hour Fire Tower &amp; Staircase Relief</h4>
          <p class="ruled-card-desc">
            Mandates a 2-hour rated Fire Tower combining a fireman evacuation lift, ventilated lobby, and fire escape stair. 
            Crucially, providing this Fire Tower statutorily exempts the project from duplicate 2nd lift/staircase mandates!
          </p>
          <div class="ruled-card-footer">
            <span>FIRE EVACUATION</span>
            <span class="badge badge-status-done">2-HR TOWER / EXEMPTION</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">CLAUSE C</span>
          <h4 class="ruled-card-title">&ge;90m Fire Break Water Tanks</h4>
          <p class="ruled-card-desc">
            In super-tall buildings 90 meters and above, intermediate fire break tanks and booster pumps are legally required at 
            every 65-meter vertical elevation stage to prevent hydraulic pressure failure during upper-level firefighting.
          </p>
          <div class="ruled-card-footer">
            <span>HIGH-RISE HYDRAULICS</span>
            <span class="badge badge-status-done">TANKS @ 65M STAGES</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">CLAUSES D TO I</span>
          <h4 class="ruled-card-title">Licensed Electrical Engineer &amp; 5-Yr Audit</h4>
          <p class="ruled-card-desc">
            Mandatory electrical supervision and completion certificates. Mandatory re-inspection every 5 years. 
            Default triggers immediate power disconnection by the utility and statutory revocation of the Occupancy Certificate.
          </p>
          <div class="ruled-card-footer">
            <span>ELECTRICAL SAFETY</span>
            <span class="badge badge-status-done">5-YR AUDIT / OC REVOCATION</span>
          </div>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 13-D: SPECIAL DISASTER SAFETY &amp; HIGH-RISE FIRE TOWER MATRIX</span>
          <span class="badge badge-status-done">REG. 13.6 (10-OCT-2024)</span>
        </div>

        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono); margin-bottom:16px;">
            <thead>
              <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">REGULATORY COMPONENT</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:160px;">STATUTORY BENCHMARK</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:200px;">TECHNICAL SPECIFICATION</th>
                <th style="padding:8px; text-align:left;">LEGAL CONSEQUENCE OF DEFAULT</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Disaster Risk Applicability</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">BUA &gt; <strong>10,000 sq.m</strong> OR<br>Occupancy &gt; <strong>1,000 persons</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Malls, hospitals, colleges, assembly halls, financial hubs, or police-flagged Govt offices.</td>
                <td style="padding:8px;">Proposal evaluated under Risk Assessment Score (Annexure-A &amp; B).</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Fire Tower System</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);"><strong>2 Hours</strong> Fire Resistance</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Fireman evacuation lift + pressurized/ventilated lobby integrated into fire escape staircase.</td>
                <td style="padding:8px; font-weight:700; color:var(--blueprint);">EXEMPTS the building from duplicate 2nd lift &amp; 2nd staircase requirements!</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Fire Break Water Tanks</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Building Height &ge; <strong>90 meters</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Dedicated water tanks + fire booster pumps at <strong>every 65 m height interval</strong>.</td>
                <td style="padding:8px;">Mandatory staging on service floor or refuge level per Annexure-D.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Electrical Professional</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Licensed Electrical Engineer</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Supervisory cert at building notice; completion cert before Occupancy Certificate.</td>
                <td style="padding:8px; color:var(--brick);">Immediate license revocation and professional debarment for discrepancies.</td>
              </tr>
              <tr style="background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Post-OC Maintenance</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">At least <strong>once every 5 years</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Physical inspection of all flats/shops; audit certificates publicly displayed in lobby.</td>
                <td style="padding:8px; font-weight:700; color:var(--brick);"><strong>Withdrawal of Occupancy Certificate</strong> &amp; <strong>Power supply disconnection</strong>!</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
        <strong>Scenario:</strong> A real estate developer is designing a <strong>120-meter high commercial and financial corporate headquarters</strong> 
        with an aggregate built-up area of <strong>28,000 sq.m</strong> in Navi Mumbai. Evaluate the fire escape, lift configuration, 
        and high-rise fire pump staging under Regulation 13.6 (Oct 2024 Notification).
      </p>
      <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
        <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">ENGINEERING SCRUTINY EVALUATION (REGULATION 13.6):</div>
        <div><strong>Step 1: Check Statutory Applicability (Reg. 13.6.A)</strong></div>
        <div>&bull; Built-Up Area = 28,000 sq.m (&gt; 10,000 sq.m threshold) &amp; Financial Corporate HQ &rarr; <strong>REGULATION 13.6 FULLY APPLIES</strong>.</div>
        <div style="margin-top:8px;"><strong>Step 2: Fire Tower &amp; Staircase Optimization (Reg. 13.6.B)</strong></div>
        <div>&bull; Mandate: Provide Fire Tower having 2 hours fire resistance with fireman evacuation lift and ventilated lobby.</div>
        <div>&bull; Optimization under Note to Clause B: By designing a conforming Fire Tower integrated with the fire escape staircase, the project is <strong>LEGALLY EXEMPT</strong> from providing a duplicate second staircase and second lift!</div>
        <div>&bull; This saves over 150 sq.m of core area per floor while drastically improving occupant survivability.</div>
        <div style="margin-top:8px;"><strong>Step 3: Staging Fire Break Water Tanks (Reg. 13.6.C)</strong></div>
        <div>&bull; Total Building Height = 120 meters (&gt; 90 meters threshold).</div>
        <div>&bull; Rule: Provide intermediate fire break water tanks with fire pumps at <strong>every 65 m height interval</strong>.</div>
        <div>&bull; Calculation: 120 m / 65 m = 1.85 &rarr; <strong>1 Intermediate Fire Break Station required at ~60-65m level</strong>.</div>
        <div>&bull; Staging: Locate fire break water tank (minimum 20,000 litres reserve) and dedicated electrical booster fire pumps on the 18th floor (refuge / service floor at +62.0 m elevation) to supply the upper tower.</div>
        <div style="margin-top:8px;"><strong>Step 4: Electrical Safety &amp; Post-Possession Commitment (Reg. 13.6.D &amp; I)</strong></div>
        <div>&bull; Licensed Electrical Engineer must sign supervision certificate at commencement and completion certificate at OC.</div>
        <div>&bull; Perpetual Condition on OC: Housing society/building management must conduct complete electrical recertification every 5 years; failure triggers power shutoff by the electrical utility company.</div>
      </div>
    """,
    'pitfalls_html': """
      <div>
        <strong>1. Assuming Fire Break Water Tanks are Only Needed at the Terrace (Reg 13.6.C):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          For towers &ge; 90 meters, MEP consultants often place all water tanks in the basement and on the rooftop. Reg. 13.6.C mandates intermediate break tanks with booster pumps at <strong>every 65-meter vertical interval</strong>. Without these intermediate break tanks, extreme static pressure ruptures ground-floor risers or starves upper-level fire hoses.
        </p>
      </div>
      <div>
        <strong>2. Over-Designing Duplicate Staircases Without Utilizing the Fire Tower Relief (Reg 13.6.B Note):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Many architects continue to duplicate staircases and lifts on 12,000 sq.m buildings under older generic high-rise codes. The Note to Reg. 13.6.B explicitly states that once a conforming 2-hour Fire Tower is incorporated, secondary staircase/lift mandates <strong>shall not be applicable</strong>, unlocking immense carpet efficiency.
        </p>
      </div>
      <div>
        <strong>3. Treating the 5-Year Electrical Inspection as an Advisory Recommendation (Reg 13.6.I):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Cooperative societies and facility managers often neglect periodic electrical audits. Reg. 13.6.I carries draconian enforcement: failure to obtain and display the 5-year certificate empowers the power distribution company to <strong>disconnect the building's electrical mains</strong> and allows the Authority to <strong>withdraw the Occupancy Certificate</strong>.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.92rem; line-height:1.6;">
        <strong>Notification u/s. 37(1AA)(c) No. CR.45/2022/UD-11 dated 10th October, 2024:</strong><br>
        Formally inserted Regulation 13.6 ("Special Safety Control Regulations for Buildings Vulnerable to Man-Made Disasters") 
        along with Annexures A through O into UDCPR-2020. This statutory amendment codified the modern Fire Tower doctrine, 
        intermediate 65m break tanks, and professional licensure accountability for electrical engineers in the aftermath 
        of catastrophic commercial and hospital fire incidents across Maharashtra.
      </p>
    """,
    'quiz': [
        {
            'question': 'Under the 10th October 2024 Gazette Notification (Reg. 13.6), what are the scale criteria for buildings considered vulnerable to man-made disasters?',
            'options': [
                'Built-up area exceeding 2,000 sq.m or 200 occupants',
                'Built-up area exceeding 5,000 sq.m or 500 occupants',
                'Built-up area exceeding 10,000 sq.m or occupancy over 1,000 persons',
                'Only buildings higher than 150 meters'
            ],
            'answer': 2,
            'explanation': 'Regulation 13.6.A.c.1 explicitly establishes applicability for buildings "Having built up area exceeding 10,000 sq.m. or occupancy over the 1000 persons."'
        },
        {
            'question': 'What major planning concession is granted when a conforming 2-hour Fire Tower is provided under Regulation 13.6.B Note?',
            'options': [
                'The building gets 20% free commercial FSI',
                'Other provisions regarding applicability of a second lift and second staircase for high-rise/Special buildings shall not be applicable',
                'The building is exempt from municipal property taxes for 10 years',
                'Front road width requirements are waived'
            ],
            'answer': 1,
            'explanation': 'The Note to Reg. 13.6.B explicitly states: "Other provisions in the sanctioned DCPR with regards to the applicability of a second lift, second staircase for high-rise / Special buildings shall not be applicable after provision of a Fire Tower."'
        },
        {
            'question': 'For Special Buildings with a height of 90 meters and above, at what vertical interval must fire break water tanks and fire pumps be provided under Reg. 13.6.C?',
            'options': [
                'At every 30 m height interval',
                'At every 45 m height interval',
                'At every 65 m height interval from ground level',
                'Only at the top terrace level'
            ],
            'answer': 2,
            'explanation': 'Regulation 13.6.C mandates: "Special buildings with height 90 m. and above shall be provided with fire break water tank system with fire pumps at every 65 m. height interval from ground level."'
        },
        {
            'question': 'What are the statutory consequences under Regulation 13.6.I if a building fails to carry out its mandatory 5-year electrical inspection or maintain fire systems?',
            'options': [
                'A minor fine of Rs. 100 on the society chairman',
                'Withdrawal of Occupancy Certificate by the Authority and disconnection of power supply by the Power Supply Company',
                'Conversion of the building into public housing',
                'No legal action can be taken after OC is granted'
            ],
            'answer': 1,
            'explanation': 'Under Reg. 13.6.I Notes (c) & (d), failure to maintain fire installations may lead to withdrawal of the Occupancy Certificate, while failure to maintain electrical installations may lead to disconnection of power supply by the power utility.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
