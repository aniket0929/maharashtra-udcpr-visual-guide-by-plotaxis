import os
import sys
from generate_lessons import create_lesson_page

sys.stdout.reconfigure(encoding='utf-8')

# Definition of the lessons for Chapters 1, 2, and 3
lessons = [
    # -------------------------------------------------------------
    # LESSON 1: Reg. 1.1 & 1.2
    # -------------------------------------------------------------
    {
        'filename': 'reg-1-1-jurisdiction-and-extent.html',
        'lesson_id': 'lesson-reg-1-1',
        'quiz_id': 'quiz-reg-1-1',
        'clause': 'Reg. 1.1 & 1.2',
        'title': 'Extent, Jurisdiction & Commencement of UDCPR',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Jurisdictional boundaries of Maharashtra UDCPR-2020: Where the regulations apply, excluded areas (MCGM, MIDC, NAINA), and commencement date.',
        'lead_summary': 'Learn the exact geographical and administrative jurisdiction of UDCPR-2020 across Maharashtra, understand which planning authorities are covered, and identify excluded municipal zones.',
        'amendment_cite': None,
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            The <strong>Unified Development Control and Promotion Regulations (UDCPR-2020)</strong> replaced dozens of disparate municipal and regional building by-laws with a single unified regulatory code across the State of Maharashtra.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Effective Date:</strong> Sanctioned by the Government on <strong>02nd December, 2020</strong>.</li>
            <li><strong>Territorial Scope:</strong> Applies to all Municipal Corporations (except Mumbai), Municipal Councils, Nagar Panchayats, Non-Municipal Planning Authorities, and Regional Plan areas across Maharashtra.</li>
            <li><strong>Critical Exclusions:</strong> Does NOT apply to Municipal Corporation of Greater Mumbai (MCGM), MIDC, NAINA (Navi Mumbai Airport Influence Notified Area), JNPT, Hill Station Councils, and notified Eco-Sensitive regions.</li>
          </ul>
        """,
        'statutory_extract': "These regulations shall apply to the building activities and development works on lands within the jurisdiction of all Planning Authorities and Regional Plan areas in Maharashtra State, excluding the Municipal Corporation of Greater Mumbai, other Planning Authorities / Special Planning Authorities within the limit of MCGM, MIDC, NAINA, Jawaharlal Nehru Port Trust, Hill Station Municipal Councils, Eco-sensitive / Eco-fragile regions...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-emerald);">Included Jurisdictions</h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                Pune (PMC), Thane (TMC), Nagpur (NMC/NMRDA), Nashik (NMC), Pimpri-Chinchwad (PCMC), Navi Mumbai (NMMC), Kalyan-Dombivli (KDMC), Vasai-Virar, Kolhapur, Solapur, Aurangabad, and all Regional Plan villages.
              </p>
            </div>
            <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-rose);">Excluded Jurisdictions</h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                Mumbai City & Suburbs (MCGM DCPR-2034), MIDC industrial estates, NAINA special planning area, JNPT port limits, and Lonavala / Mahabaleshwar Eco-sensitive zones.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_005 // JURISDICTION MATRIX</span>
              <span class="fig-title">Maharashtra Development Control Applicability Tree</span>
            </div>
            <div style="padding:16px 8px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              MAHARASHTRA STATE PLANNING JURISDICTION<br>
              ├── [APPLICABLE] UDCPR-2020 (Dec 2, 2020)<br>
              │    ├── All Municipal Corporations (Pune, Thane, Nagpur, Nashik, etc.)<br>
              │    ├── All 'A', 'B', 'C' Class Municipal Councils & Nagar Panchayats<br>
              │    ├── Regional Plan Areas (PMRDA, NMRDA, District Zilla Parishad Areas)<br>
              │    └── Special Planning Authorities outside MCGM limits<br>
              └── [EXCLUDED] SEPARATE REGULATIONS<br>
                   ├── Mumbai Metropolis &rarr; MCGM DCPR-2034<br>
                   ├── Industrial Hubs &rarr; MIDC Regulations<br>
                   ├── Airport Belt &rarr; NAINA Regulations<br>
                   └── Notified Eco-Sensitive Zones &rarr; MoEF & CC Guidelines
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Determining Applicable Code for an Industrial Plot</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              An engineer is designing a factory in Chakan, Pune. Plot A is inside an MIDC notified industrial park; Plot B is 200m away on private agricultural land converted to industrial use under Pune Regional Plan.
            </p>
            <div class="worked-step">
              <span class="step-badge">PLOT A</span>
              <div>Plot A is within MIDC jurisdiction &rarr; <strong>MIDC Development Control Regulations apply (Exempt from UDCPR).</strong></div>
            </div>
            <div class="worked-step">
              <span class="step-badge">PLOT B</span>
              <div>Plot B is outside MIDC in Regional Plan limits &rarr; <strong>UDCPR-2020 Chapter 4 & Chapter 6 apply fully.</strong></div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Applying UDCPR clauses within Mumbai City / MCGM</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Junior architects frequently cite UDCPR FSI tables for projects in Mumbai suburbs. MCGM is governed exclusively by DCPR-2034. UDCPR has zero legal validity within Mumbai Municipal limits.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Sanctioned under Section 37(1AA)(c) and Section 20(4) of the MRTP Act, 1966 vide Notification No. TPS-1818/C.R.236/18/DP&RP/Sec.37(1AA)(c) & Sec.20(4)/UD-13 on 2nd December, 2020.
          </p>
        """,
        'quiz': [
          {
            'question': "Which of the following Planning Authorities is EXCLUDED from the scope of UDCPR-2020?",
            'options': [
              "Pune Municipal Corporation (PMC)",
              "Municipal Corporation of Greater Mumbai (MCGM)",
              "Nagpur Municipal Corporation (NMC)",
              "Thane Municipal Corporation (TMC)"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.1, the Municipal Corporation of Greater Mumbai (MCGM) is explicitly excluded from UDCPR and is governed by its own DCPR-2034."
          },
          {
            'question': "On which exact date did the Maharashtra UDCPR-2020 officially commence?",
            'options': [
              "1st January, 2020",
              "2nd December, 2020",
              "15th August, 2021",
              "30th January, 2025"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.2, these regulations came into force on 02nd December, 2020 vide Government Notification No. TPS-1818/C.R.236/18."
          },
          {
            'question': "Does UDCPR-2020 apply to industrial developments situated inside MIDC notified industrial areas?",
            'options': [
              "Yes, UDCPR overrides MIDC",
              "No, MIDC areas are explicitly excluded under Regulation 1.1",
              "Only if the plot is larger than 10 acres",
              "Only on payment of premium to MIDC"
            ],
            'correctAnswer': 1,
            'explanation': "MIDC areas are specifically listed as an excluded jurisdiction under Regulation 1.1; they follow separate MIDC regulations."
          }
        ],
        'prev_url': '/chapters/ch01.html',
        'prev_title': 'Chapter 1 Hub',
        'next_url': '/lessons/reg-1-3-statutory-definitions.html',
        'next_title': 'Reg. 1.3 Definitions'
      },

    # -------------------------------------------------------------
    # LESSON 2: Reg. 1.3
    # -------------------------------------------------------------
    {
        'filename': 'reg-1-3-statutory-definitions.html',
        'lesson_id': 'lesson-reg-1-3',
        'quiz_id': 'quiz-reg-1-3',
        'clause': 'Reg. 1.3',
        'title': 'The Statutory Definitions Compendium',
        'badge_status': '141 Terms',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Detailed study of Section 1.3 definitions in UDCPR-2020. FSI, Carpet Area, Built-up Area, TDR, DRC, and the amended definition of Special Building.',
        'lead_summary': 'Master the core vocabulary of Maharashtra planning. Learn how definitions dictate legal interpretations, and explore key statutory terms like FSI, Carpet Area, and Special Building.',
        'amendment_cite': 'CR.44/21',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            Section 1.3 contains <strong>141 numbered definitions</strong>. In municipal law, a defined term carries strict statutory meaning that overrides dictionary definitions or common trade usage.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>FSI (Reg. 1.3.63):</strong> Total covered built-up area of all floors divided by the gross or net plot area.</li>
            <li><strong>Carpet Area (Reg. 1.3.25):</strong> Net usable floor area of an apartment, aligning with RERA 2016.</li>
            <li><strong>Special Building (Reg. 1.3.93.xiv #):</strong> High-rise buildings (> 15m), educational, assembly, or hazardous occupancies triggering CFO fire clearance.</li>
          </ul>
        """,
        'statutory_extract': "Words and expressions which are not defined in these Regulations shall have the same meaning or sense as in the Maharashtra Regional and Town Planning Act, 1966, the Maharashtra Land Revenue Code, 1966, RERA 2016, and National Building Code of India 2016...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-amber);">Amended Definition: Special Building (#)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              Under Clarification CR 44/21 (10th June 2021), a 'Special Building' is explicitly defined as any building exceeding 15 meters in height, or educational, institutional, or assembly buildings with built-up area exceeding statutory thresholds, requiring dedicated fire lifts and Chief Fire Officer (CFO) approvals.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div style="overflow-x:auto; background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-md); padding:16px; margin:20px 0;">
            <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
              <thead>
                <tr style="border-bottom:1px solid var(--border-dim); color:var(--accent-cyan); font-family:var(--font-mono); text-align:left;">
                  <th style="padding:8px;">Clause</th>
                  <th style="padding:8px;">Term</th>
                  <th style="padding:8px;">Legal Significance</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">Reg. 1.3(17)</td>
                  <td style="padding:8px; font-weight:700;">Basic FSI</td>
                  <td style="padding:8px; color:var(--text-secondary);">Inherent entitlement on plot without purchasing premium or loading TDR.</td>
                </tr>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">Reg. 1.3(25)</td>
                  <td style="padding:8px; font-weight:700;">Carpet Area</td>
                  <td style="padding:8px; color:var(--text-secondary);">Usable floor area excluding external walls, service shafts, and open balconies.</td>
                </tr>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-family:var(--font-mono);">Reg. 1.3(40)</td>
                  <td style="padding:8px; font-weight:700;">Development Rights</td>
                  <td style="padding:8px; color:var(--text-secondary);">Authorised potential to carry out development up to total permissible FSI.</td>
                </tr>
                <tr>
                  <td style="padding:8px; font-family:var(--font-mono);">Reg. 1.3(74)</td>
                  <td style="padding:8px; font-weight:700;">High-rise Building</td>
                  <td style="padding:8px; color:var(--text-secondary);">Any building height exceeding 15.0 meters from surrounding ground level.</td>
                </tr>
              </tbody>
            </table>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Carpet Area vs. Built-up Area Computation</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A 2-BHK apartment has an internal room area of 65.0 sq.m, internal partition walls of 3.0 sq.m, external perimeter walls of 6.0 sq.m, and a cantilevered balcony of 8.0 sq.m.
            </p>
            <div class="worked-step">
              <span class="step-badge">CARPET AREA</span>
              <div>Internal room area (65 sq.m) + internal partition walls (3 sq.m) = <strong>68.0 sq.m Carpet Area (Reg. 1.3.25).</strong></div>
            </div>
            <div class="worked-step">
              <span class="step-badge">BUILT-UP AREA</span>
              <div>Carpet Area (68) + external walls (6) + balcony (8) = <strong>82.0 sq.m Built-up Area (Reg. 1.3.21).</strong></div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Confusing Height of Building with Storey Count</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Height is measured strictly in vertical meters from average road/ground level to top roof slab. A stilt plus 4-floor building reaching 15.2 meters is classified as a High-Rise Special Building, requiring full fire safety clearances.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarification CR 44/21 dated 10th June, 2021 amended sub-clause xiv of definition 93 regarding Special Buildings to harmonize fire protection rules with the National Building Code (NBC-2016).
          </p>
        """,
        'quiz': [
          {
            'question': "Under Regulation 1.3(74), at what height threshold is a building classified as a High-Rise Building?",
            'options': [
              "Above 12 meters",
              "Above 15 meters",
              "Above 24 meters",
              "Above 30 meters"
            ],
            'correctAnswer': 1,
            'explanation': "Under UDCPR Regulation 1.3(74), any building with a height exceeding 15 meters from average ground level is classified as a High-rise Building."
          },
          {
            'question': "What is the relationship between Carpet Area defined in UDCPR and the RERA Act 2016?",
            'options': [
              "They are completely contradictory",
              "UDCPR includes external walls, RERA excludes them",
              "UDCPR Regulation 1.3(25) harmonizes directly with RERA 2016 net usable floor area",
              "UDCPR measures from center of exterior walls"
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 1.3(25) explicitly adopts the RERA 2016 standard: net usable floor area excluding external walls, service shafts, and exclusive balconies."
          }
        ],
        'prev_url': '/lessons/reg-1-1-jurisdiction-and-extent.html',
        'prev_title': 'Reg. 1.1 Jurisdiction',
        'next_url': '/lessons/reg-1-5-savings-and-interpretation.html',
        'next_title': 'Reg. 1.5 Savings'
      },

    # -------------------------------------------------------------
    # LESSON 3: Reg. 1.5 – 1.10
    # -------------------------------------------------------------
    {
        'filename': 'reg-1-5-savings-and-interpretation.html',
        'lesson_id': 'lesson-reg-1-5',
        'quiz_id': 'quiz-reg-1-5',
        'clause': 'Reg. 1.5 – 1.10',
        'title': 'Legal Savings, Hierarchy & Removal of Difficulties',
        'badge_status': 'Core Legal',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Grandfathering prior approvals under Reg. 1.5 Savings, interpretation powers under Reg. 1.9, and government addenda under Reg. 1.10.',
        'lead_summary': 'Understand how previously approved building plans are protected under the Savings clause, how conflicts between acts are resolved, and how the State Government exercises its power to issue Corrigenda under Regulation 1.10.',
        'amendment_cite': None,
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            When a major new planning code is published, active construction sites and sanctioned layouts need legal certainty. Regulation 1.5 provides the "Savings" shield, while Regulation 1.10 establishes the mechanism to fix ambiguities without re-enacting the entire act.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Savings (Reg. 1.5):</strong> Any building permission, commencement certificate, or layout approved before Dec 2, 2020 remains fully valid. You can complete construction under your old sanction.</li>
            <li><strong>Opting into UDCPR:</strong> If you revise your plan, you must adopt UDCPR in its entirety; you cannot cherry-pick between old and new rules.</li>
            <li><strong>Removal of Difficulties (Reg. 1.10):</strong> Empowers the Director of Town Planning and Urban Development Department to issue binding clarifications and corrigenda.</li>
          </ul>
        """,
        'statutory_extract': "Neither the sanction of these regulations nor anything contained in these regulations shall affect, invalidate or invalidate any permission issued or any order made under the repealed regulations, and development permission granted prior to coming into force of these regulations shall remain valid...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">The Non-Selective Rule (Reg. 1.5)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              If a developer desires to avail higher FSI benefits under UDCPR on an existing ongoing project, the entire project must conform to UDCPR setback, parking, and open space requirements. Mixing clauses is strictly forbidden.
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_006 // REGULATORY TRANSITION</span>
              <span class="fig-title">Savings Clause Decision Tree for Pre-2020 Approvals</span>
            </div>
            <div style="padding:16px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              PROJECT SANCTIONED BEFORE 02-DEC-2020<br>
              │<br>
              ├── Build as per original sanction &rarr; [VALID] Proceed under Old Sanction (Reg. 1.5)<br>
              │<br>
              └── Seek revision for higher FSI?<br>
                   └── Must apply UDCPR completely &rarr; [MANDATORY] Entire layout, parking & setbacks re-assessed under UDCPR
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Revising a 2019 Sanctioned Layout</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              A developer in Nashik holds a 2019 Commencement Certificate granting 1.20 FSI with 2.0m side margins. They wish to utilize 2.00 FSI under UDCPR Table 6-A.
            </p>
            <div class="worked-step">
              <span class="step-badge">RULING</span>
              <div>They can consume 2.00 FSI, but their building height will increase, triggering the UDCPR H/5 side setback and Chapter 8 parking standards. They cannot retain the old 2.0m margins while taking higher FSI.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Cherry-Picking FSI without Meeting Parking</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Town planning officers will reject any revised submission that takes UDCPR higher FSI while relying on grandfathered, smaller parking bay quotas from 2015 by-laws.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Regulation 1.10 has been utilized for multiple addenda (notably CR.121/21 dt. 02 Dec 2021 and CR.79/2021) to rectify drafting errors and issue statewide guidance.
          </p>
        """,
        'quiz': [
          {
            'question': "What happens to a building permission legally granted prior to December 2, 2020?",
            'options': [
              "It becomes void immediately",
              "It remains valid and construction can proceed to completion",
              "It must pay a 25% penalty fee",
              "It is limited to ground floor only"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.5 (Savings), any development permission granted prior to UDCPR remains fully valid for execution."
          },
          {
            'question': "Can an applicant apply old setback rules while claiming new higher FSI under UDCPR?",
            'options': [
              "Yes, at the discretion of the architect",
              "No, UDCPR must be accepted in its entirety if revised benefits are claimed",
              "Only in gaothan congested areas",
              "Only on payment of double scrutiny fee"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 1.5 explicitly mandates that if a revision is sought under UDCPR, the entire proposal must comply with UDCPR provisions in toto."
          }
        ],
        'prev_url': '/lessons/reg-1-3-statutory-definitions.html',
        'prev_title': 'Reg. 1.3 Definitions',
        'next_url': '/lessons/reg-2-1-development-permission.html',
        'next_title': 'Reg. 2.1 Permission'
      },

    # -------------------------------------------------------------
    # LESSON 4: Reg. 2.1
    # -------------------------------------------------------------
    {
        'filename': 'reg-2-1-development-permission.html',
        'lesson_id': 'lesson-reg-2-1',
        'quiz_id': 'quiz-reg-2-1',
        'clause': 'Reg. 2.1',
        'title': 'Mandatory Development Permission & Exempted Works',
        'badge_status': 'Core Workflow',
        'ch_slug': 'ch02',
        'ch_title': 'Chapter 2: Development Permissions',
        'meta_desc': 'When is development permission mandatory under UDCPR Regulation 2.1? Exempted internal repairs, government operational constructions, and temporary works.',
        'lead_summary': 'Learn what constitutes development under the MRTP Act, when written building permission is strictly mandatory, and which minor repairs and operational constructions are legally exempt.',
        'amendment_cite': None,
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            Under Section 44 and 45 of the MRTP Act and UDCPR Regulation 2.1, no person or authority can carry out any development, construction, or land subdivision without obtaining a valid written <strong>Commencement Certificate (CC)</strong>.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Mandatory Permission:</strong> Required for new buildings, structural alterations, additions, change of occupancy, and land subdivision / layouts.</li>
            <li><strong>Exempted Works (Reg. 2.1.2):</strong> Gardening, white washing, painting, plastering, internal retiling, and minor repair works not affecting structural columns/beams.</li>
            <li><strong>Government Works (Reg. 2.1.3):</strong> Departments of State/Central Government must inform the authority and submit plans for record, even when exempted from full sanction.</li>
          </ul>
        """,
        'statutory_extract': "No person shall carry out any development, erect, re-erect or make alterations or demolish any building or cause the same to be done without first obtaining a separate building permit / commencement certificate for each such development work / building from the Authority...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-emerald);">Exempted Repairs (Reg. 2.1.7)</h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                Re-roofing existing roofs, repairing parapets, internal false ceilings, sanitary replacements, and fixing weather-shed chajjas within permissible projections.
              </p>
            </div>
            <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px;">
              <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-rose);">Never Exempt</h4>
              <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
                Cutting load-bearing beams or columns, removing fire staircases, adding extra floor slabs, or changing residential flat into commercial shop.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_007 // PERMISSION MATRIX</span>
              <span class="fig-title">Classification of Permitted vs Exempted Works</span>
            </div>
            <div style="padding:16px; font-family:var(--font-mono); font-size:0.85rem; color:var(--text-secondary); line-height:1.8;">
              DEVELOPMENT PERMISSION CLASSIFICATION<br>
              ├── [MANDATORY CC] New Construction, Wing Addition, Demolition & Rebuild<br>
              ├── [MANDATORY CC] Land Layout, Plotted Sub-division, Amalgamation<br>
              ├── [MANDATORY CC] Structural Retrofit, Changing Load-bearing Walls<br>
              ├── [SELF-CERTIFIED] Plots &le; 150 sq.m (Appendix K-1 Fast Track)<br>
              └── [EXEMPTED] Plastering, Painting, Retiling, Non-structural Partition
            </div>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Office Partition vs. Structural Modification</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              An office tenant installs drywall gypsum partitions and a glass door without altering RCC columns.
            </p>
            <div class="worked-step">
              <span class="step-badge">STATUS</span>
              <div>Permitted without fresh building permit under Reg. 2.1.2, provided exit travel distances and emergency door widths of Regulation 9.28 are not choked.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Enclosing Open Balconies without Municipal Sanction</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                Homeowners often enclose cantilevered open balconies with brickwork assuming it is minor repair. Under Regulation 2.1, this alters external wall envelope and consumes FSI, constituting unauthorized construction.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarifications issued under Section 154 emphasize that risk-based self-certification for plots up to 150 sq.m (Appendix K-1) eliminates delays for small residential owners.
          </p>
        """,
        'quiz': [
          {
            'question': "Which of the following activities requires a mandatory Commencement Certificate?",
            'options': [
              "White-washing and external painting",
              "Erecting a new 3-storey residential wing",
              "Gardening and landscape returfing",
              "Replacing broken sanitary fittings inside a toilet"
            ],
            'correctAnswer': 1,
            'explanation': "Erecting a new wing or structure is development under Section 44 and strictly requires a formal building permit / CC under Reg. 2.1."
          },
          {
            'question': "Does replacing damaged internal floor tiles require prior building permission?",
            'options': [
              "Yes, always",
              "No, internal retiling is explicitly exempted under Regulation 2.1.2",
              "Only if done in commercial complexes",
              "Only if approved by structural engineer"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 2.1.2 explicitly provides that internal painting, plastering, retiling, and minor surface finishes do not constitute structural alteration."
          }
        ],
        'prev_url': '/lessons/reg-1-5-savings-and-interpretation.html',
        'prev_title': 'Reg. 1.5 Savings',
        'next_url': '/lessons/reg-2-2-application-procedure.html',
        'next_title': 'Reg. 2.2 Application'
      },

    # -------------------------------------------------------------
    # LESSON 5: Reg. 2.2
    # -------------------------------------------------------------
    {
        'filename': 'reg-2-2-application-procedure.html',
        'lesson_id': 'lesson-reg-2-2',
        'quiz_id': 'quiz-reg-2-2',
        'clause': 'Reg. 2.2',
        'title': 'Building Permission Application & Submission Drawings',
        'badge_status': 'Core Workflow',
        'ch_slug': 'ch02',
        'ch_title': 'Chapter 2: Development Permissions',
        'meta_desc': 'Mandatory submission drawings under UDCPR Reg. 2.2: Key plan, site plan, building plans, special building requirements, and licensed professional signing.',
        'lead_summary': 'Master the technical submission requirements for building scrutiny in Maharashtra: drawing scales, required architectural sheets, structural stability undertakings, and Special Building fire clearances.',
        'amendment_cite': 'CR.42/21',
        'plain_summary_html': """
          <p style="margin-bottom:12px;">
            To obtain development sanction, an applicant must submit a formal Notice accompanied by statutory architectural plans, ownership documents (7/12 extract / Property Card), and certifications by licensed technical professionals.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; color:var(--text-secondary);">
            <li><strong>Mandatory Plans:</strong> Key Plan (1:10,000), Site Plan (1:500 or 1:1,000), Sub-division / Layout Plan, Detailed Floor Plans & Sections (1:100), Service Plan (drainage/water).</li>
            <li><strong>Special Buildings (Reg. 2.2.8 #):</strong> Plans for buildings &gt; 15m height must show dedicated fire escapes, refuge areas, fire tower, and receive clearance from the Chief Fire Officer.</li>
            <li><strong>Signatures (Reg. 2.2.16):</strong> Plans must be co-signed by the registered Owner, Licensed Architect, Structural Engineer, and Site Supervisor.</li>
          </ul>
        """,
        'statutory_extract': "Every person who intends to carry out development and erect, re-erect or make alterations in any place in a building shall give notice in writing to the Authority of his said intention in the proforma given in Appendix A-1 or A-2 and such notice shall be accompanied by the plans and statements in sufficient copies...",
        'clause_cards_html': """
          <div style="background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-sm); padding:16px; margin-top:16px;">
            <h4 style="font-size:0.95rem; margin-bottom:8px; color:var(--accent-cyan);">Drawing Sheet Specifications (Reg. 2.2.17 #)</h4>
            <p style="font-size:0.85rem; color:var(--text-secondary); line-height:1.5;">
              Plans must follow standard ISO drawing formats (A0, A1, A2, A3) and specify exact colour coding: Existing work (black), Proposed work (red), Work to be demolished (yellow), Open spaces (green).
            </p>
          </div>
        """,
        'plate_or_table_html': """
          <div style="overflow-x:auto; background:var(--bg-card); border:1px solid var(--border-dim); border-radius:var(--radius-md); padding:16px; margin:20px 0;">
            <table style="width:100%; border-collapse:collapse; font-size:0.85rem;">
              <thead>
                <tr style="border-bottom:1px solid var(--border-dim); color:var(--accent-cyan); font-family:var(--font-mono); text-align:left;">
                  <th style="padding:8px;">Plan Type</th>
                  <th style="padding:8px;">Prescribed Scale</th>
                  <th style="padding:8px;">Mandatory Features to Show</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-weight:700;">Key Plan (Reg. 2.2.4)</td>
                  <td style="padding:8px; font-family:var(--font-mono);">Not less than 1:10,000</td>
                  <td style="padding:8px; color:var(--text-secondary);">North point, connecting highways, landmarks, surrounding boundaries.</td>
                </tr>
                <tr style="border-bottom:1px solid var(--border-dim);">
                  <td style="padding:8px; font-weight:700;">Site Plan (Reg. 2.2.6)</td>
                  <td style="padding:8px; font-family:var(--font-mono);">1:500 or 1:1,000</td>
                  <td style="padding:8px; color:var(--text-secondary);">Road widening line, front/side/rear setbacks, open space pockets, trees.</td>
                </tr>
                <tr>
                  <td style="padding:8px; font-weight:700;">Building Plan (Reg. 2.2.7)</td>
                  <td style="padding:8px; font-family:var(--font-mono);">1:100</td>
                  <td style="padding:8px; color:var(--text-secondary);">Room dimensions, carpet area statement, staircase width, lift shafts, plinth.</td>
                </tr>
              </tbody>
            </table>
          </div>
        """,
        'worked_example_html': """
          <div class="worked-example-box">
            <h4 style="font-size:1.05rem; margin-bottom:10px;">Scenario: Special Building Submissions Checklist</h4>
            <p style="font-size:0.88rem; color:var(--text-secondary); margin-bottom:14px;">
              An architect submits plans for an 18-meter residential tower.
            </p>
            <div class="worked-step">
              <span class="step-badge">CHECKLIST</span>
              <div>Because height &gt; 15m, it is a Special Building under Reg. 2.2.8. Must submit: Provisional Fire NOC from CFO, 6.0m clear driveway on site plan, lift rescue hatch details, and structural design calculation sheet.</div>
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <span class="callout-icon">⚡</span>
            <div>
              <strong>Pitfall: Incomplete Area Statement in Proforma-I</strong>
              <p style="font-size:0.84rem; color:var(--text-secondary); margin-top:4px;">
                The single most common scrutiny query arises when the drawing sheet area statement does not explicitly reconcile Basic FSI, Premium FSI, and non-FSI deductions against Net Plot Area.
              </p>
            </div>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6;">
            Clarifications issued vide Order No. CR.236/18 (Part 2) dt. 23 Dec 2021 streamlined digital online scrutiny (AutoDCR/BIMS) procedures across all Municipal Councils.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the minimum scale prescribed for a Site Plan under Regulation 2.2.6?",
            'options': [
              "1:10,000",
              "1:500 (or 1:1,000 for large sites)",
              "1:100",
              "1:50"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 2.2.6 mandates that a Site Plan must be drawn to a scale not less than 1:500 (or 1:1,000 for plots exceeding 10 hectares)."
          },
          {
            'question': "Who among the following MUST co-sign the building drawings under Regulation 2.2.16?",
            'options': [
              "Only the land owner",
              "Only the municipal corporator",
              "Owner, Licensed Architect, and Structural Engineer",
              "Only the local police inspector"
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 2.2.16 mandates that all drawings must be signed by the Owner and the qualified Licensed Architect / Engineer / Structural Engineer."
          }
        ],
        'prev_url': '/lessons/reg-2-1-development-permission.html',
        'prev_title': 'Reg. 2.1 Permission',
        'next_url': '/lessons/reg-2-2-fees-and-charges.html',
        'next_title': 'Reg. 2.2.12 Fees'
      }
]

# Write out the lessons
for l in lessons:
    create_lesson_page(l)

print(f"Successfully generated {len(lessons)} core lessons.")
