"""
UDCPR Chapter 12 - Lesson 12.1: Structural Safety, Quality of Materials & Building Services
Statutory Clauses: Regulations 12.1, 12.2, 12.3, 12.4
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
        'clause': 'Reg. 12.1 - 12.4',
        'title': 'Structural Safety, Materials Quality & Building Services',
        'meta_desc': 'Chapter 12 statutory requirements for structural design per NBC Part-6, BIS seismic standards, PWD material standards, mosquito-safe borrow pits, alternative material testing, and NBC Part-8 electrical, HVAC and lift provisions.',
        'ch_slug': 'ch12',
        'ch_title': 'Chapter 12: Structural Safety & Sanitation',
        'badge_status': '100% COMPLETE',
        'amendment_cite': None,
        'filename': 'reg-12-1-structural-design-materials-and-building-services.html',
        'lesson_id': 'ch12_lesson_1',
        'quiz_id': 'quiz_ch12_1',
        'prev_url': '/lessons/reg-11-3-reservation-credit-certificate-and-financial-offsets.html',
        'prev_title': 'Reg. 11.3 Reservation Credit Certificate',
        'next_url': '/lessons/reg-12-5-water-supply-and-flushing-storage-capacities.html',
        'next_title': 'Reg. 12.5 Water Supply & Flushing Storage',
        'lead_summary': (
            'Every structure erected under Maharashtra UDCPR-2020 must adhere to strict structural integrity, '
            'seismic resilience, material standards, and engineering safety benchmarks. Regulation 12.1 mandates compliance '
            'with National Building Code (NBC) Part-6 and BIS earthquake/fire codes backed by a Licensed Structural Engineer\'s certificate. '
            'Regulation 12.2 enforces PWD specifications and introduces anti-malaria mandates for construction borrow pits. '
            'Regulation 12.3 provides a formal pathway for alternative materials via advance accredited laboratory testing (with mandatory '
            '2-year record retention), while Regulation 12.4 governs electrical, mechanical, and elevator installations per NBC Part-8, '
            'featuring a crucial statutory lift relief for single-floor vertical additions.'
        ),
        'plain_summary_html': """
          <p>
            Before an architect can concern themselves with aesthetics or FSI consumption, a building must stand strong, resist seismic shocks, 
            protect occupants from fires and structural collapse, and guarantee dependable life safety services. Regulations 12.1 through 12.4 establish 
            the statutory bridge between Maharashtra town planning permissions and Indian engineering codes:
          </p>
          <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
            <li><strong>Structural Design (Reg 12.1):</strong> Foundations, masonry, timber, bamboo, plain concrete, reinforced concrete (RCC), pre-stressed concrete (PSC), and structural steel must strictly obey <strong>NBC of India Part-6 (Sections 1 to 7)</strong>. All structures must comply with Bureau of Indian Standards (BIS) earthquake resistance and natural calamity codes. Development permission proposals must include a signed certificate from an empanelled <strong>Licensed Structural Engineer</strong>.</li>
            <li><strong>Materials &amp; Workmanship (Reg 12.2.1):</strong> Materials must conform to Maharashtra Public Works Department (PWD) specifications and NBC Part-5 (Materials) and Part-7 (Construction Practices and Safety). Substandard steel or aggregate is ground for immediate work-stop orders.</li>
            <li><strong>Borrow Pit Sanitation Mandate (Reg 12.2.2):</strong> A unique public-health mandate: borrow pits excavated during building or road construction cannot be left isolated to collect stagnant water and breed mosquitoes. They must be dug deep, interconnected into channels graded toward the lowest site contour, and drained into a stream or storm sewer.</li>
            <li><strong>Alternative Materials &amp; Testing Protocol (Reg 12.3):</strong> UDCPR explicitly permits innovative construction techniques (precast, 3D printing, composite panels) provided they are proven equivalent in strength, durability, fire rating, and safety. The Authority can require advance tests at the developer's cost through approved agencies. Crucially, the Authority must <strong>retain test results for at least 2 years</strong>.</li>
            <li><strong>Building Services &amp; Lift Addition Concession (Reg 12.4):</strong> Electrical, air-conditioning, and mechanical ventilation must satisfy NBC Part-8 (Sections 2 &amp; 3). Lift and escalator installations are determined by NBC Part-8 Section-5 based on building height and floor occupant loads. <strong>Statutory Relief:</strong> If an existing building proposes <em>one additional floor</em>, the existing elevator is legally exempt from being extended to that new top floor!</li>
          </ul>
        """,
        'statutory_extract': (
            "The structural design of foundations, elements made of masonry, timber, plain concrete; reinforced concrete, pre-stressed concrete "
            "and structural steel shall be carried out in accordance with Part-6... Certificate to that effect shall be submitted by the Licensed "
            "Structural Engineer of the developer / land owner, along with the proposal for development permission... All borrow pits dug in the "
            "course of construction... shall be deep and connected with each other in the formation of a drain directed towards the lowest level... "
            "In existing buildings, in case of proposal for one additional floor, existing lift may not be raised to the additional floor."
        ),
        'clause_cards_html': """
          <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
            <div class="ruled-card">
              <span class="kicker">REGULATION 12.1</span>
              <h4 class="ruled-card-title">NBC Part-6 Structural Compliance</h4>
              <p class="ruled-card-desc">
                Mandates full compliance with NBC Part-6 across all 7 subsections: Loads (Sec 1), Soils &amp; Foundations (Sec 2), Timber/Bamboo (Sec 3), 
                Masonry (Sec 4), Plain/Reinforced Concrete (Sec 5), Structural Steel (Sec 6), and Prefabrication/Composite Systems (Sec 7). 
                Requires mandatory seismic resilience certification under IS 1893 and IS 13920.
              </p>
              <div class="ruled-card-footer">
                <span>STATUTORY REQUIREMENT</span>
                <span class="badge badge-status-done">MANDATORY CERT</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">REGULATION 12.2</span>
              <h4 class="ruled-card-title">PWD Standards &amp; Anti-Malaria Pits</h4>
              <p class="ruled-card-desc">
                Materials must conform to Maharashtra PWD standard book of specifications and NBC Part-5/7. Reg 12.2(2) strictly bans isolated borrow pits: 
                contractors must connect all ground excavations into linked drainage trenches sloping to the lowest discharge outfall to prevent malaria/dengue mosquito breeding.
              </p>
              <div class="ruled-card-footer">
                <span>HEALTH &amp; SAFETY</span>
                <span class="badge badge-status-done">ANTI-STAGNATION</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">REGULATION 12.3</span>
              <h4 class="ruled-card-title">Alternative Materials &amp; 2-Year Record</h4>
              <p class="ruled-card-desc">
                Innovative materials and design schemes are encouraged if proven equivalent in strength, fire rating, and durability. 
                Testing must occur in advance through government-approved testing agencies at developer expense. 
                All test certificates must be archived by the Planning Authority for a minimum of 24 months.
              </p>
              <div class="ruled-card-footer">
                <span>INNOVATION GATEWAY</span>
                <span class="badge badge-status-done">2-YEAR RETENTION</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">REGULATION 12.4</span>
              <h4 class="ruled-card-title">NBC Part-8 Services &amp; Lift Exemption</h4>
              <p class="ruled-card-desc">
                Electrical installations, HVAC, and mechanical ventilation must obey NBC Part-8 (Sec 2 &amp; 3). Lift quantity, speed, and capacity follow 
                NBC Part-8 (Sec 5). For existing permitted buildings adding an approved single vertical floor, the existing lift machine room/shaft is not required to be retrofitted to the top level.
              </p>
              <div class="ruled-card-footer">
                <span>ELECTRO-MECHANICAL</span>
                <span class="badge badge-status-done">LIFT RELIEF</span>
              </div>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 12-A: STATUTORY CODES &amp; BUILDING SERVICES MATRIX</span>
              <span class="badge badge-status-done">REG. 12.1 TO 12.4</span>
            </div>

            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono);">
                <thead>
                  <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                    <th style="padding:10px 8px; text-align:left; border-right:1px solid var(--ink-soft);">REGULATION</th>
                    <th style="padding:10px 8px; text-align:left; border-right:1px solid var(--ink-soft);">SUBJECT</th>
                    <th style="padding:10px 8px; text-align:left; border-right:1px solid var(--ink-soft);">GOVERNING STATUTORY CODE</th>
                    <th style="padding:10px 8px; text-align:left;">MANDATORY SUBMISSION / COMPLIANCE</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Reg. 12.1</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Structural Design &amp; Natural Calamities</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">NBC Part-6 (Sec 1 to 7) &amp; BIS Codes (IS 456, IS 1893, IS 13920, IS 800)</td>
                    <td style="padding:8px;">Certificate of Structural Stability signed by Empanelled Licensed Structural Engineer with Building Permission application.</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Reg. 12.2.1</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Materials &amp; Workmanship</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Maharashtra PWD Red Book &amp; NBC Part-5 (Materials) + Part-7 (Construction Safety)</td>
                    <td style="padding:8px;">Site supervision log, mill test certificates for TMT rebar, concrete cube 7/28-day crushing tests.</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Reg. 12.2.2</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Borrow Pits &amp; Site Drainage</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Anti-Malaria By-laws &amp; UDCPR Environmental Sanitation</td>
                    <td style="padding:8px;">All borrow pits must be interconnected by continuous graded trenches draining to natural storm nallah; no isolated standing water allowed.</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Reg. 12.3</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Alternative Materials &amp; Testing</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Bureau of Indian Standards testing norms &amp; approved testing labs</td>
                    <td style="padding:8px;">Proof of equivalence (fire resistance, load capacity, durability). Authority must maintain test dossiers on file for &ge; 2 years.</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Reg. 12.4.1</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Electrical &amp; HVAC Systems</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">NBC Part-8, Section 2 (Electrical) &amp; Section 3 (Air Conditioning / Ventilation)</td>
                    <td style="padding:8px;">Electrical safety inspector clearance, earthing pits, dedicated smoke extraction, and fire dampers in AC ducts.</td>
                  </tr>
                  <tr style="background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Reg. 12.4.2</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Lifts, Escalators &amp; Vertical Expansion</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">NBC Part-8, Section 5 (Lifts &amp; Escalators) &amp; Maharashtra Lifts Act</td>
                    <td style="padding:8px;">Lift license, passenger capacity per occupant load. In existing buildings adding +1 floor, lift is not required to be extended to top floor.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft); margin-top:12px; line-height:1.5;">
              <strong>KEY STATUTORY HIGHLIGHT:</strong> Under Reg 12.4.2, existing G+4 or higher buildings utilizing balance FSI or TDR to construct one single additional vertical floor are legally protected from the prohibitive capital cost of raising the concrete lift core, motor room, and elevator rails.
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
            <strong>Scenario:</strong> An existing 4-storey residential apartment building (G+4) with an active 8-passenger elevator in Pune has 
            unutilized potential FSI under Table 6-A. The housing society proposes to construct <strong>one additional vertical floor (5th floor)</strong> 
            comprising two 3-BHK flats. Simultaneously, the contractor proposes to use a new glass-fiber reinforced polymer (GFRP) lightweight roof 
            composite system instead of conventional RCC.
          </p>
          <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
            <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">ENGINEERING SCRUTINY EVALUATION (REG. 12.1 TO 12.4):</div>
            <div><strong>1. Structural Integrity &amp; Retrofit Certificate (Reg. 12.1):</strong></div>
            <div>&bull; Addition of the 5th floor increases gravity and lateral seismic loads on existing columns and footings.</div>
            <div>&bull; Mandatory requirement: Licensed Structural Engineer must perform structural audit, soil/footing load-bearing capacity check, and non-destructive rebound hammer tests on existing concrete.</div>
            <div>&bull; Engineer must issue statutory Certificate of Seismic and Structural Safety per IS 1893 &amp; IS 13920 before planning sanction.</div>
            <div style="margin-top:8px;"><strong>2. Alternative Material Compliance (Reg. 12.3):</strong></div>
            <div>&bull; Proposed GFRP lightweight composite slab is not explicitly enumerated in conventional PWD schedules.</div>
            <div>&bull; Under Reg 12.3(3) &amp; 12.3(4), the developer must submit laboratory test certificates from an authorized BIS-approved testing agency proving equivalence in:</div>
            <div>&nbsp;&nbsp;- Structural load-bearing capacity (bending &amp; shear)</div>
            <div>&nbsp;&nbsp;- 2-Hour Fire Rating (NBC Part-4 fire resistance)</div>
            <div>&nbsp;&nbsp;- Durability &amp; weathering resistance under thermal cycling.</div>
            <div>&bull; The Planning Authority must preserve this testing dossier on official record for a minimum of <strong>2 years (24 months)</strong>.</div>
            <div style="margin-top:8px;"><strong>3. Elevator Extension Exemption (Reg. 12.4.2):</strong></div>
            <div>&bull; Clause: <em>"In existing buildings, in case of proposal for one additional floor, existing lift may not be raised to the additional floor."</em></div>
            <div>&bull; Statutory Ruling: The housing society is <strong>LEGALLY EXEMPT</strong> from demolishing the existing lift machine room on the 4th floor to raise the hoistway to the 5th floor.</div>
            <div>&bull; The 5th-floor occupants access their apartments via the statutory fire escape staircase from the 4th-floor lift landing, saving immense structural modification costs while remaining 100% compliant.</div>
          </div>
        """,
        'pitfalls_html': """
          <div>
            <strong>1. Borrow Pit Abandonment &amp; Municipal Malaria Notices (Reg 12.2.2):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              During basement excavation or earth filling, contractors often dig isolated borrow pits for rainwater collection or mixing. If left disconnected and water accumulates, local municipal health departments (e.g. PMC, BMC, TMC) issue stop-work notices and heavy daily fines under anti-malaria by-laws. Pits must be continuously graded and connected to site storm drains.
            </p>
          </div>
          <div>
            <strong>2. Applying the Lift Exemption to 2-Floor Additions (Reg 12.4.2):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              The lift extension waiver under Reg. 12.4.2 strictly applies to <em>"one additional floor"</em>. If a redevelopment proposal adds two or more vertical floors (e.g., G+4 expanded to G+6), the elevator shaft and machine room <strong>MUST</strong> be raised to service the upper habitable levels in compliance with NBC Part-8 Section-5.
            </p>
          </div>
          <div>
            <strong>3. Submitting Architectural Drawings Without Structural License Endorsement (Reg 12.1):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              Architects cannot self-certify structural, seismic, or soil safety. Under Reg. 12.1, development permission proposals lacking the formal structural endorsement and registration number of a Licensed Structural Engineer are automatically flagged as invalid during initial scrutiny.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.92rem; line-height:1.6;">
            Regulations 12.1 through 12.4 represent standard structural and life-safety anchors anchored directly to National Building Code 
            revisions. The Bureau of Indian Standards (BIS) earthquake codes (IS 1893:2016 and ductile detailing IS 13920:2016) are automatically 
            incorporated by reference into Reg. 12.1. The 1-floor lift extension concession in Reg. 12.4.2 was specifically codified to facilitate 
            brownfield vertical extensions of older 4-storey cooperative housing societies across Maharashtra without requiring elevator core reconstruction.
          </p>
        """,
        'quiz': [
            {
                'question': 'Which Part of the National Building Code (NBC) of India governs the structural design of foundations, concrete, steel, and masonry under UDCPR Regulation 12.1?',
                'options': [
                    'Part-3: Development Control Rules',
                    'Part-6: Structural Design',
                    'Part-8: Building Services',
                    'Part-9: Plumbing Services'
                ],
                'answer': 1,
                'explanation': 'Regulation 12.1 mandates that structural design of foundations, masonry, timber, concrete, steel, and composite construction must follow NBC Part-6 (Sections 1 through 7).'
            },
            {
                'question': 'Under Regulation 12.2(2), how must borrow pits excavated during building or road construction be treated on site?',
                'options': [
                    'They must be filled with municipal solid waste within 48 hours',
                    'They must be left isolated to act as natural percolation ponds',
                    'They must be deep and interconnected to form a drain directed to the lowest level to prevent mosquito breeding',
                    'They must be paved with asphalt before building work begins'
                ],
                'answer': 2,
                'explanation': 'Regulation 12.2(2) strictly prohibits isolated borrow pits that collect stagnant water, requiring them to be connected as a continuous drain sloping towards the lowest discharge point.'
            },
            {
                'question': 'How long must the Planning Authority preserve the test results and documentation of approved alternative materials on official record under Regulation 12.3(6)?',
                'options': [
                    'Not less than 6 months',
                    'Not less than 1 year',
                    'Not less than 2 years',
                    'Indefinitely for 50 years'
                ],
                'answer': 2,
                'explanation': 'Under Reg. 12.3(6), copies of the results of all such alternative material tests shall be retained by the authority for a period of not less than two years after acceptance.'
            },
            {
                'question': 'Under Regulation 12.4(2), what statutory concession is granted regarding elevator installations in existing buildings?',
                'options': [
                    'Existing buildings are never required to install an elevator',
                    'In case of a proposal for one additional floor, the existing lift is not required to be raised to the additional floor',
                    'All elevators can be replaced with mechanical dumbwaiters',
                    'Lifts only need to run during daytime hours'
                ],
                'answer': 1,
                'explanation': 'Regulation 12.4(2) specifically provides: "In existing buildings, in case of proposal for one additional floor, existing lift may not be raised to the additional floor."'
            }
        ]
    }

if __name__ == '__main__':
    create_lesson_page(lesson_data)
