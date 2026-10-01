"""
UDCPR Chapter 12 - Lesson 12.4: Commercial, Hospitality & Transit Sanitation & Outdoor Display Signs
Statutory Clauses: Regulation 12.6.3 (Tables 12-K to 12-P), Regulation 12.7.1, 12.7.2
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
        'clause': 'Reg. 12.6.3 (Tables 12-K to 12-P) & Reg. 12.7',
        'title': 'Commercial, Transit Sanitation & Outdoor Display Signs',
        'meta_desc': 'Chapter 12 sanitary fitments for Hotels (12-K), Restaurants (12-L), Schools (12-M), Hostels (12-N), Shopping Malls (12-O), Airports/Railways (12-P with disabled WC quotas), and Reg. 12.7 outdoor display prohibitions on heritage & government buildings.',
        'ch_slug': 'ch12',
        'ch_title': 'Chapter 12: Structural Safety & Sanitation',
        'badge_status': '100% COMPLETE',
        'amendment_cite': None,
        'filename': 'reg-12-6-commercial-hospitality-sanitation-and-signs.html',
        'lesson_id': 'ch12_lesson_4',
        'quiz_id': 'quiz_ch12_4',
        'prev_url': '/lessons/reg-12-6-drainage-and-institutional-sanitation.html',
        'prev_title': 'Reg. 12.6 Drainage & Institutional Sanitation',
        'next_url': '/lessons/reg-13-1-barrier-free-access-for-differently-abled.html',
        'next_title': 'Reg. 13.1: Barrier-Free Access & Universal Design',
        'lead_summary': (
            'The culmination of Chapter 12 addresses the intense sanitary demands of mass-transit hubs, commercial shopping malls, '
            'hospitality establishments, and educational institutions, while regulating outdoor advertisements across urban streetscapes. '
            'Under Tables 12-K through 12-P, statutory fixture schedules scale from intimate nursery schools (1 WC per 15 pupils) '
            'to high-density shopping malls (1 WC per 50 floating visitors) and major airports. In transit infrastructure, Regulation 12.6 '
            'mandates universal accessibility with a dedicated disabled toilet quota of 1 per 4,000 persons. Finally, Regulation 12.7 '
            'governs billboards and sky-signs under NBC Part-10 Section-2, enforcing a strict statutory ban on commercial hoardings on '
            'heritage structures and government buildings.'
        ),
        'plain_summary_html': """
          <p>
            Public commercial environments and transit gateways require careful calculation to avoid unhygienic queues and municipal non-compliance. 
            Tables 12-K through 12-P, combined with Regulation 12.7 outdoor display rules, establish the following mandates:
          </p>
          <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
            <li><strong>Hospitality Fitments (Tables 12-K &amp; 12-L):</strong>
              <br>&bull; <em>Hotels (Table 12-K):</em> Guest rooms must have attached toilet suites. For common facilities, male WCs are 1 per 100 (up to 400), while female WCs are <strong>2 per 100 (up to 200)</strong>. Urinals: 1 per 50.
              <br>&bull; <em>Restaurants (Table 12-L):</em> Public dining rooms require 1 male WC per 50 seats (up to 200) and <strong>2 female WCs per 50 seats (up to 200)</strong>. Non-residential kitchen/service staff follow stepped employee ratios.
            </li>
            <li><strong>Educational &amp; Student Housing (Tables 12-M &amp; 12-N):</strong>
              <br>&bull; <em>Nursery Schools:</em> <strong>1 WC per 15 pupils</strong> (unisex).
              <br>&bull; <em>Non-Residential Day Schools:</em> Boys require 1 WC per 40 pupils + 1 urinal per 20 boys. Girls require <strong>1 WC per 25 pupils</strong>.
              <br>&bull; <em>Boarding Schools &amp; Hostels:</em> Residential boys require 1 WC per 8; residential girls require <strong>1 WC per 6</strong>.
            </li>
            <li><strong>Mercantile Complexes &amp; Malls (Table 12-O):</strong>
              <br>&bull; <em>Shop Owners:</em> 1 WC per 8 persons.
              <br>&bull; <em>Common Mall Toilets:</em> Stepped ratios for retail staff.
              <br>&bull; <em>Floating Shoppers:</em> <strong>1 WC per 50 persons (Minimum 2)</strong> for males, <strong>1 WC per 50 persons (Minimum 2)</strong> for females, and 1 urinal per 50 males.
            </li>
            <li><strong>Transit Stations &amp; Airports (Table 12-P):</strong>
              <br>&bull; Sized according to average daily passenger footfalls.
              <br>&bull; <em>Airports:</em> High-density progressive tiers (min 2 for 200, jumping to 18 WCs for 1,000+ passengers) and 1 urinal per 40 passengers.
              <br>&bull; <em>Universal Accessibility:</em> Mandatory <strong>Toilet for Disabled at 1 per 4,000 persons (Minimum 1)</strong> across all railway stations, bus terminals, and airports!
            </li>
            <li><strong>Signs &amp; Outdoor Display Structures (Reg 12.7):</strong>
              <br>&bull; Commercial hoardings and outdoor displays must obey <strong>NBC Part-10, Section-2</strong> and municipal advertisement by-laws.
              <br>&bull; <em>Absolute Heritage &amp; Civic Ban (Reg 12.7.2):</em> <strong>No advertising signs or outdoor display structures are permitted on buildings of architectural, aesthetical, historical, or heritage importance</strong>, or on Government buildings (except signs solely identifying the building's own official purpose).
            </li>
          </ul>
        """,
        'statutory_extract': (
            "Table No.12-O Sanitation Requirements - Mercantile Buildings, Commercial Complexes, Shopping Malls... Public Toilet for Floating Population: "
            "Water Closets: 1 per 50 (Minimum 2) Male / Female... Table No.12-P... Toilet for Disabled: 1 per 4000 (Minimum 1)... "
            "12.7.2 Prohibition of advertising signs and outdoor display structure in certain cases: Notwithstanding the provisions of sub-regulations, "
            "no advertising sign or outdoor display structures shall be permitted on buildings of architectural, aesthetical, historical or heritage "
            "importance as may be decided by the Authority or on Government Buildings save that in the case of Government buildings only advertising signs "
            "or outdoor display structure may be permitted if they relate to the activities for the said buildings' own purposes."
        ),
        'clause_cards_html': """
          <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
            <div class="ruled-card">
              <span class="kicker">TABLE 12-M &amp; 12-N</span>
              <h4 class="ruled-card-title">Schools, Colleges &amp; Student Hostels</h4>
              <p class="ruled-card-desc">
                Enforces distinct daylight vs residential quotas: day schools mandate 1 WC per 25 girls and 1 WC per 40 boys (with 1 urinal per 20). 
                Hostels tighten the ratio to 1 WC per 6 female residents and 1 WC per 8 male residents.
              </p>
              <div class="ruled-card-footer">
                <span>EDUCATIONAL</span>
                <span class="badge badge-status-done">TABLES 12-M / 12-N</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">TABLE 12-O</span>
              <h4 class="ruled-card-title">Shopping Malls &amp; Mercantile Hubs</h4>
              <p class="ruled-card-desc">
                Distinguishes between shopkeepers (1 WC per 8), permanent retail mall staff, and the floating public. 
                Public shopper amenities require 1 WC per 50 patrons (min 2) for each sex, with 1 urinal per 50 males.
              </p>
              <div class="ruled-card-footer">
                <span>RETAIL COMMERCE</span>
                <span class="badge badge-status-done">TABLE 12-O</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">TABLE 12-P</span>
              <h4 class="ruled-card-title">Airports, Rail &amp; Universal Access</h4>
              <p class="ruled-card-desc">
                Dimensioned by daily passenger volumes. Airports require high-frequency WCs and urinals (1 per 40). 
                Critically mandates at least 1 barrier-free Accessible Toilet for Disabled persons per 4,000 passengers.
              </p>
              <div class="ruled-card-footer">
                <span>MASS TRANSIT</span>
                <span class="badge badge-status-done">1 DISABLED / 4K</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">REGULATION 12.7</span>
              <h4 class="ruled-card-title">Outdoor Signs &amp; Heritage Ban</h4>
              <p class="ruled-card-desc">
                Governs commercial billboards and sky-signs per NBC Part-10 Section-2. 
                Reg. 12.7.2 enacts an absolute statutory ban against commercial hoardings on heritage structures, historic landmarks, and Government secretariats.
              </p>
              <div class="ruled-card-footer">
                <span>URBAN AESTHETICS</span>
                <span class="badge badge-status-done">HERITAGE BAN</span>
              </div>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 12-C: COMMERCIAL, EDUCATIONAL, TRANSIT SANITATION &amp; SIGNAGE RULES</span>
              <span class="badge badge-status-done">TABLES 12-K TO 12-P &amp; REG 12.7</span>
            </div>

            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono); margin-bottom:16px;">
                <thead>
                  <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:130px;">BUILDING USE</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">CATEGORY</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">WATER CLOSETS (MALE)</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">WATER CLOSETS (FEMALE)</th>
                    <th style="padding:8px; text-align:left;">URINALS (MALE)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);" rowspan="2">Schools (Table 12-M)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Day Schools</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 40 boys</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--brick);">1 per 25 girls</td>
                    <td style="padding:8px;">1 per 20 boys</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Residential Boarding</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 8 boys</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--brick);">1 per 6 girls</td>
                    <td style="padding:8px;">1 per 25 boys</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);" rowspan="2">Hostels (Table 12-N)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Residents</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 8 residents</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--brick);">1 per 6 residents</td>
                    <td style="padding:8px;">1 per 25 residents</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Visitors</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 100 (up to 400)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 200 (up to 200)</td>
                    <td style="padding:8px;">1 per 50 visitors</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);" rowspan="2">Malls &amp; Retail (Table 12-O)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Shop Owners</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 8 persons</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 8 persons</td>
                    <td style="padding:8px;">In common blocks</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Floating Shoppers</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">1 per 50 (Min 2)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">1 per 50 (Min 2)</td>
                    <td style="padding:8px;">1 per 50 persons</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);" rowspan="2">Airports &amp; Rail (Table 12-P)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Terminal Stations</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">4 per 1,000 (+1/1,000)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">5 per 1,000 (+1/1,000)</td>
                    <td style="padding:8px;">6 per 1,000 (+1/1,000)</td>
                  </tr>
                  <tr style="background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Accessible Toilet</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--amber);" colspan="3">MANDATORY DISABLED ACCESSIBLE TOILET: 1 PER 4,000 PERSONS (MINIMUM 1)</td>
                  </tr>
                </tbody>
              </table>

              <div style="font-size:12px; font-weight:700; color:var(--blueprint); margin-bottom:8px;">REGULATION 12.7: STATUTORY DISPLAY ADVERTISEMENT CHECKLIST</div>
              <div style="border:1px dashed var(--ink); padding:12px; font-size:0.86rem; line-height:1.6;">
                <div>&bull; <strong>Statutory Standard (Reg 12.7.1):</strong> Must comply with National Building Code Part-10 Section-2 ("Signs and Outdoor Display Structures") + local Municipal Advertisement By-laws.</div>
                <div>&bull; <strong>Heritage Structures Prohibition (Reg 12.7.2):</strong> Strictly zero commercial advertising signs, billboards, LED video walls, or hoardings allowed on classified heritage buildings, monuments, or within precincts of architectural and historical importance.</div>
                <div>&bull; <strong>Government Buildings Prohibition (Reg 12.7.2):</strong> Advertising on government secretariats, courts, and civic administrative offices is prohibited, <em>EXCEPT</em> for official departmental signage and public notifications directly relating to the institution's own statutory functions.</div>
              </div>
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
            <strong>Scenario:</strong> Calculate the statutory public floating sanitary fixtures for a new <strong>Shopping Mall in Nashik</strong> 
            designed to accommodate an estimated peak floating shopper population of <strong>300 males and 300 females</strong> under Table 12-O, 
            and evaluate an application by a retail tenant to erect a 40-foot illuminated commercial billboard on an adjacent municipal heritage town hall.
          </p>
          <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
            <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">SCRUTINY COMPUTATION &amp; LEGAL VERIFICATION:</div>
            <div><strong>Part 1: Shopping Mall Public Toilets (Table 12-O Floating Population)</strong></div>
            <div>&bull; Statutory Norm: <em>"1 per 50 (Minimum 2)"</em> for both Male and Female Water Closets; 1 Urinal per 50 Males.</div>
            <div>&bull; <strong>Male Water-Closets (W.C.):</strong> 300 / 50 = <strong>6 Male W.C.s</strong> (Exceeds min 2, fully compliant).</div>
            <div>&bull; <strong>Female Water-Closets (W.C.):</strong> 300 / 50 = <strong>6 Female W.C.s</strong> (Exceeds min 2, fully compliant).</div>
            <div>&bull; <strong>Male Urinals:</strong> 300 / 50 = <strong>6 Urinals</strong>.</div>
            <div>&bull; Note: In addition, shop owners (at 1 WC per 8 persons) and permanent retail staff require dedicated separate fixtures.</div>
            <div style="margin-top:8px;"><strong>Part 2: Commercial Billboard Scrutiny (Reg. 12.7.2)</strong></div>
            <div>&bull; Proposal: Erect private commercial advertising billboard on the adjacent Municipal Heritage Town Hall facade.</div>
            <div>&bull; Statutory Ruling under Reg 12.7.2: <em>"no advertising sign or outdoor display structures shall be permitted on buildings of architectural, aesthetical, historical or heritage importance... or on Government Buildings"</em>.</div>
            <div>&bull; <strong>Sanction Verdict: REJECTED IN TOTO</strong>. Private commercial display on heritage or government property is an explicit statutory violation. The billboard can only be permitted on the private commercial mall facade subject to NBC Part-10 Section-2 clearance.</div>
          </div>
        """,
        'pitfalls_html': """
          <div>
            <strong>1. Omitting Mandatory Accessible Toilets for the Disabled in Transit Hubs (Table 12-P):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              Architects designing intercity bus terminals, metro stations, or airport annexes frequently provide ample male and female stalls but forget the mandatory <strong>1 per 4,000 Accessible Toilet for Disabled</strong>. Under Table 12-P, providing at least 1 fully dimensioned wheelchair toilet (with outward swinging doors and grab rails) is a mandatory condition for building occupancy.
            </p>
          </div>
          <div>
            <strong>2. Applying Uniform Girls and Boys Toilets in Schools (Table 12-M):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              In non-residential schools, Table 12-M prescribes 1 WC per 40 boys (who also have urinals at 1 per 20), but requires <strong>1 WC per 25 girls</strong>. Designing equal WC counts for boys and girls will result in a statutory shortage of girls' facilities and lead to an immediate plan rejection by municipal school scrutiny committees.
            </p>
          </div>
          <div>
            <strong>3. Misinterpreting Floating vs Shop Owner Sanitations in Malls:</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              Under Table 12-O, shop owners cannot be expected to share the floating public customer toilets. Shop owners require 1 WC per 8 persons, while the floating public requires 1 WC per 50 persons. Both schedules must be satisfied concurrently in the sanction drawings.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.92rem; line-height:1.6;">
            The outdoor advertisement restrictions in Regulation 12.7 reaffirm Supreme Court and Bombay High Court directives 
            prohibiting visual clutter, sky-sign hazards, and illegal commercial hoardings on historic civic landmarks. 
            Local Planning Authorities (such as BMC, PMC, and NMMC) maintain separate outdoor advertising policy guidelines 
            under NBC Part-10 Section-2 that operate concurrently with UDCPR Reg. 12.7.
          </p>
        """,
        'quiz': [
            {
                'question': 'Under Table 12-M, what is the required ratio of water-closets for girls in non-residential day schools?',
                'options': [
                    '1 for every 15 girls',
                    '1 for every 25 girls or part thereof',
                    '1 for every 40 girls or part thereof',
                    '1 for every 50 girls'
                ],
                'answer': 1,
                'explanation': 'Table 12-M Item i stipulates 1 WC for 40 pupils for boys, but a higher provision of 1 per 25 pupils for girls in non-residential schools.'
            },
            {
                'question': 'In mercantile buildings and shopping malls, what is the minimum statutory provision of water-closets for the floating public under Table 12-O?',
                'options': [
                    '1 per 100 persons (Minimum 1)',
                    '1 per 50 persons (Minimum 2)',
                    '1 per 25 persons (Minimum 4)',
                    '1 per 200 persons'
                ],
                'answer': 1,
                'explanation': 'Table 12-O explicitly mandates for the floating population: "1 per 50 (Minimum 2)" for both Male and Female water-closets.'
            },
            {
                'question': 'What is the mandatory statutory ratio for providing specialized Accessible Toilets for the Disabled in railway stations and airports under Table 12-P?',
                'options': [
                    '1 per 1,000 persons',
                    '1 per 2,000 persons',
                    '1 per 4,000 persons (Minimum 1)',
                    '1 per 10,000 persons'
                ],
                'answer': 2,
                'explanation': 'Table 12-P Item iii specifies "Toilet for Disabled: 1 per 4000 (Minimum 1)" across junction stations, bus stations, terminal railway stations, and airports.'
            },
            {
                'question': 'Under Regulation 12.7.2, which category of buildings is strictly prohibited from displaying commercial advertising signs and outdoor display structures?',
                'options': [
                    'Industrial warehouses and factories',
                    'Buildings of architectural, aesthetical, historical or heritage importance, and Government buildings',
                    'Shopping malls located on 24-meter roads',
                    'Commercial high-rises exceeding 50 meters'
                ],
                'answer': 1,
                'explanation': 'Regulation 12.7.2 explicitly states: "no advertising sign or outdoor display structures shall be permitted on buildings of architectural, aesthetical, historical or heritage importance as may be decided by the Authority or on Government Buildings..."'
            }
        ]
    }

if __name__ == '__main__':
    create_lesson_page(lesson_data)
