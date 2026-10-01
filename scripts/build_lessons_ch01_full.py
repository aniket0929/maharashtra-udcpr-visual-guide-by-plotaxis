"""
UDCPR FROM SCRATCH - CHAPTER 1 FULL LESSON BUILDER
Generates the complete 4-lesson curriculum for Chapter 1: Administration
Covers Reg 1.0 through 1.10 in exhaustive educational detail.
"""

import os
import sys
from generate_lessons import create_lesson_page

sys.stdout.reconfigure(encoding='utf-8')

ch01_lessons = [
    # -------------------------------------------------------------------------
    # LESSON 1.1: REG. 1.0, 1.1, 1.2 & 1.4
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-1-1-jurisdiction-and-extent.html',
        'lesson_id': 'lesson-reg-1-1',
        'quiz_id': 'quiz-reg-1-1',
        'clause': 'Reg. 1.0, 1.1, 1.2 & 1.4',
        'title': 'Extent, Jurisdiction & Operational Scope of UDCPR',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Jurisdictional boundaries of Maharashtra UDCPR-2020: Where the regulations apply, the 9 excluded areas (MCGM, MIDC, NAINA), TPS rules, and operational scope under Reg 1.4.',
        'lead_summary': 'Learn the geographic, administrative, and operational boundaries of UDCPR-2020 across Maharashtra: which planning authorities are governed, the 9 exempt special areas, Town Planning Scheme interactions, and rules governing part-constructions, reconstructions, and layout alterations.',
        'amendment_cite': 'CR.121/21',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            The <strong>Unified Development Control and Promotion Regulations (UDCPR-2020)</strong> replaced dozens of disparate municipal building by-laws and regional planning DCRs with a single standardized regulatory code across the State of Maharashtra.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Sanction &amp; Commencement:</strong> Sanctioned by the Government of Maharashtra under Section 37(1AA)(c) and Section 20(4) of the Maharashtra Regional and Town Planning Act, 1966 (MRTP Act). Came into force on <strong>02<sup>nd</sup> December, 2020</strong>.</li>
            <li><strong>Territorial Scope:</strong> Applies to building activities and developments within the jurisdiction of all Planning Authorities, Special Planning Authorities (SPAs), and Regional Plan areas across Maharashtra.</li>
            <li><strong>The 9 Statutory Exclusions (Reg. 1.1):</strong> UDCPR does NOT apply to:
              <ol style="padding-left:18px; margin-top:6px; display:flex; flex-direction:column; gap:4px;">
                <li>Municipal Corporation of Greater Mumbai (MCGM / BMC) &rarr; governed exclusively by <em>DCPR-2034</em>.</li>
                <li>Other Planning Authorities / SPAs within MCGM limits.</li>
                <li>Maharashtra Industrial Development Corporation (MIDC) notified industrial areas.</li>
                <li>Navi Mumbai Airport Influence Notified Area (NAINA).</li>
                <li>Jawaharlal Nehru Port Trust (JNPT) township and port area.</li>
                <li>Hill Station Municipal Councils (Mahabaleshwar, Panchgani, Matheran).</li>
                <li>Chikhaldara notified area (consisting of Chikhaldara Hill Station M.C. &amp; four villages — <em>inserted vide Corrigendum CR.121/21</em>).</li>
                <li>Eco-sensitive / Eco-fragile regions notified by MoEF&amp;CC (e.g., Matheran Eco-Sensitive Zone, Dahanu Taluka).</li>
                <li>Lonavala Municipal Council.</li>
              </ol>
            </li>
            <li><strong>Town Planning Schemes (Reg. 1.1(ii)):</strong> Applicable to Town Planning Scheme (TPS) areas; however, permission may still be granted as per the specific TPS regulations in toto at the owner's option.</li>
            <li><strong>Operational Scope (Reg. 1.4):</strong>
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><em>New Construction:</em> Regulations apply fully to all new buildings, erections, additions, and change of user.</li>
                <li><em>Part Construction / Alteration:</em> If a building is partially demolished or reconstructed, UDCPR applies <strong>only to the extent of the work involved</strong>.</li>
                <li><em>Reconstruction:</em> Lawful reconstruction of buildings destroyed by fire, collapse, or declared unsafe is explicitly permitted subject to UDCPR standards.</li>
                <li><em>Layouts &amp; Subdivisions:</em> Applies to the entire layout land. If altering an earlier approved layout, it applies <strong>only to that part being altered</strong>.</li>
                <li><em>Revised Permission &amp; RERA:</em> Earlier permissions may be revised, but third-party rights created under RERA 2016 cannot be adversely affected without the consent of affected buyers. Earlier plans are stamped <strong>'SUPERSEDED'</strong>.</li>
              </ul>
            </li>
          </ul>
        """,
        'statutory_extract': "These regulations shall apply to the building activities and development works on lands within the jurisdiction of all Planning Authorities and Regional Plan areas in Maharashtra State, excluding the Municipal Corporation of Greater Mumbai, other Planning Authorities / Special Planning Authorities within the limit of MCGM, MIDC, NAINA, Jawaharlal Nehru Port Trust, Hill Station Municipal Councils, Chikhaldara notified area... Eco-sensitive / Eco-fragile region notified by MoEF & CC, and Lonavala Municipal Council in Maharashtra...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--blueprint);">INCLUDED JURISDICTIONS (UDCPR)</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                Pune (PMC), Thane (TMC), Nagpur (NMC/NMRDA), Nashik (NMC), Pimpri-Chinchwad (PCMC), Navi Mumbai (NMMC), Kalyan-Dombivli (KDMC), Vasai-Virar, Kolhapur, Solapur, Chhatrapati Sambhajinagar (Aurangabad), Amravati, Akola, all 'A', 'B', 'C' Class Municipal Councils, Nagar Panchayats, and all Regional Plan villages under PMRDA and district planning offices.
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--brick);">EXCLUDED JURISDICTIONS (INDEPENDENT CODES)</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                Mumbai City &amp; Suburbs (MCGM DCPR-2034), MIDC industrial estates, NAINA special planning area, JNPT port limits, Lonavala Municipal Council, Mahabaleshwar/Panchgani/Matheran Hill Station Councils, Chikhaldara notified area, and MoEF&amp;CC eco-sensitive zones.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_005 // JURISDICTION MATRIX</span>
              <span class="fig-title">Maharashtra Planning Code Applicability &amp; Authority Tree</span>
            </div>
            <div class="plate-content" style="padding:16px 8px; font-family:var(--mono); font-size:12px; color:var(--ink); line-height:1.8;">
              MAHARASHTRA STATE DEVELOPMENT CONTROL JURISDICTION<br>
              ├── [APPLICABLE] UDCPR-2020 (Sanctioned 02 Dec 2020)<br>
              │    ├── Tier 1: All Municipal Corporations (Pune, Thane, Nagpur, Nashik, PCMC, etc.) [EXCEPT MCGM]<br>
              │    ├── Tier 2: All 'A', 'B', 'C' Class Municipal Councils &amp; Nagar Panchayats [EXCEPT Lonavala &amp; Hill Stations]<br>
              │    ├── Tier 3: Non-Municipal Regional Plan Areas (PMRDA, NMRDA, Zilla Parishad Areas)<br>
              │    └── Tier 4: Town Planning Schemes (TPS) [Option to use TPS rules in toto maintained]<br>
              │<br>
              └── [EXCLUDED] INDEPENDENT STATUTORY REGIMES<br>
                   ├── Mumbai Metropolis &rarr; MCGM DCPR-2034 (Municipal Corporation of Greater Mumbai)<br>
                   ├── Industrial Hubs &rarr; MIDC Regulations (Maharashtra Industrial Development Corp)<br>
                   ├── Navi Mumbai Airport Belt &rarr; NAINA Regulations (CIDCO SPA)<br>
                   ├── Port Jurisdiction &rarr; JNPT Regulations (Jawaharlal Nehru Port Trust)<br>
                   ├── Hill Station Councils &rarr; Mahabaleshwar, Panchgani, Matheran Special DCR<br>
                   ├── Chikhaldara Area &rarr; Chikhaldara Hill Station M.C. &amp; 4 villages (CR.121/21)<br>
                   ├── Western Ghats / Sensitive &rarr; MoEF&amp;CC Notified Eco-Sensitive Zones<br>
                   └── Lonavala &rarr; Lonavala Municipal Council Sanctioned DCR
            </div>
            <div class="plate-caption">
              FIG_005: Statutory authority classification tree across Maharashtra showing UDCPR-2020 scope vs. excluded special planning authorities (Reg. 1.1).
            </div>
          </div>
        """,
        'worked_example_html': """
          <h4 style="font-size:1.05rem; margin-bottom:10px; color:var(--ink);">
            Scenario: Planning Jurisdiction Audit for a Multi-Plot Real Estate Portfolio
          </h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); margin-bottom:14px;">
            A consulting town planner is advising an investment group acquiring four separate development land parcels across Western Maharashtra:
          </p>
          <div class="worked-step">
            <span class="step-badge">PLOT A</span>
            <div>
              <strong>Location: Hinjawadi Phase 1, Pune</strong><br>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">
                Status: Inside MIDC Notified Industrial Area.
              </span><br>
              <span style="font-size:0.85rem; color:var(--ink-soft);">
                <strong>Ruling:</strong> UDCPR does NOT apply. The project must strictly comply with MIDC Building Regulations.
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">PLOT B</span>
            <div>
              <strong>Location: Wagholi, Pune</strong><br>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">
                Status: Merged into Pune Municipal Corporation (PMC) limits.
              </span><br>
              <span style="font-size:0.85rem; color:var(--ink-soft);">
                <strong>Ruling:</strong> UDCPR applies 100%. Governed by Municipal Corporation standards under Chapter 6 (Table 6-A).
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">PLOT C</span>
            <div>
              <strong>Location: Panvel Peripheral Belt</strong><br>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">
                Status: Inside NAINA (CIDCO Special Planning Authority).
              </span><br>
              <span style="font-size:0.85rem; color:var(--ink-soft);">
                <strong>Ruling:</strong> UDCPR does NOT apply. Governed by sanctioned NAINA DCPR regulations.
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">PLOT D</span>
            <div>
              <strong>Location: Mulshi Taluka (Rural Village)</strong><br>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">
                Status: Outside municipal limits in PMRDA Regional Plan area.
              </span><br>
              <span style="font-size:0.85rem; color:var(--ink-soft);">
                <strong>Ruling:</strong> UDCPR Chapter 5 (Additional Provisions for Regional Plan Areas) applies fully.
              </span>
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ SUMMARY: 2 of 4 plots govern under UDCPR; 2 require independent authority approvals.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Applying UDCPR FSI Tables in Mumbai City or Suburbs</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Architects new to Maharashtra often attempt to cite UDCPR Table 6-A or ancillary FSI rules for projects in Mumbai (Bandra, Andheri, Chembur, etc.). MCGM is governed exclusively by <em>DCPR-2034</em>. UDCPR has zero legal jurisdiction within Mumbai Municipal limits.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Overlooking Town Planning Scheme (TPS) Regulations</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 1.1(ii), if your plot is situated within an approved Town Planning Scheme, you are NOT forced into UDCPR if the sanctioned TPS regulations provide more advantageous layout or setback parameters. The owner has the statutory right to develop as per the TPS regulations in toto.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Submitting Revised Layouts without RERA Consent</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 1.4(vi), while an earlier development permission can be revised under UDCPR, if units have been sold and third-party rights created, the developer MUST obtain consent from affected purchasers as required under Section 14 of RERA 2016. Failure to obtain consent invalidates the municipal revision.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">(#) Corrigendum No. CR.121/21</span>
            <span style="font-family:var(--mono); font-size:0.8rem; color:var(--ink-soft);">Dated 02nd December, 2021</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.6;">
            <strong>Statutory Insertion:</strong> In Regulation 1.1(i), after the words 'Hill Station Municipal Councils,', the Government explicitly inserted: <em>'Chikhaldara notified area (consisting Chikhaldara Hill Station M.C. &amp; four villages)'</em>.
          </p>
          <p style="font-size:0.88rem; color:var(--ink); margin-top:8px; line-height:1.6;">
            <strong>Significance:</strong> Chikhaldara Hill Station and its adjoining four peripheral villages maintain their own environmentally protective building by-laws and are completely exempt from the high-density provisions of UDCPR.
          </p>
        """,
        'quiz': [
          {
            'question': "Which of the following major municipal jurisdictions is EXCLUDED from the scope of Maharashtra UDCPR-2020?",
            'options': [
              "Pune Municipal Corporation (PMC)",
              "Municipal Corporation of Greater Mumbai (MCGM / BMC)",
              "Thane Municipal Corporation (TMC)",
              "Nagpur Municipal Corporation (NMC)"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.1, the Municipal Corporation of Greater Mumbai (MCGM) is explicitly excluded from UDCPR and is governed by its own independent code, DCPR-2034."
          },
          {
            'question': "On what date did the Unified Development Control and Promotion Regulations (UDCPR-2020) come into legal force across Maharashtra?",
            'options': [
              "01st January, 2020",
              "02nd December, 2020",
              "15th August, 2021",
              "31st March, 2021"
            ],
            'correctAnswer': 1,
            'explanation': "UDCPR-2020 was published in the Official Gazette and came into force on 02nd December, 2020, repealing all earlier operating municipal building regulations."
          },
          {
            'question': "If an architect is altering only one wing of an existing multi-building layout, how does UDCPR apply under Regulation 1.4(v)?",
            'options': [
              "The entire layout and all existing buildings must be brought into compliance with UDCPR",
              "The entire layout is automatically exempt from all building regulations",
              "These Regulations shall apply ONLY to that part of the layout which is being altered",
              "The layout must be surrendered to the municipal corporation"
            ],
            'correctAnswer': 2,
            'explanation': "Under Regulation 1.4(v), where an existing layout or sub-division plan is being altered, UDCPR applies only to the specific part that is being altered, leaving unaltered portions unaffected."
          },
          {
            'question': "What special planning option is available to developers whose land falls within an approved Town Planning Scheme (TPS)?",
            'options': [
              "They must pay a 50% penalty to use UDCPR",
              "Development permission may be granted as per the Regulations of the Town Planning Scheme in toto",
              "They are strictly prohibited from building any residential structures",
              "They can only build government offices"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 1.1(ii) clarifies that while UDCPR applies to TPS areas, it does not bar development permission from being granted as per the regulations of the Town Planning Scheme in toto."
          }
        ],
        'prev_url': '/chapters/ch01.html',
        'prev_title': 'Chapter 1 Overview',
        'next_url': '/lessons/reg-1-3-statutory-definitions.html',
        'next_title': 'Reg. 1.3 Definitions'
    },

    # -------------------------------------------------------------------------
    # LESSON 1.2: REG. 1.3
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-1-3-statutory-definitions.html',
        'lesson_id': 'lesson-reg-1-3',
        'quiz_id': 'quiz-reg-1-3',
        'clause': 'Reg. 1.3',
        'title': 'The Statutory Vocabulary of Maharashtra Planning (141 Terms)',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Regulation 1.3 definitions in Maharashtra UDCPR-2020. The 10 parent acts, and the 6 essential conceptual distinctions: FSI, Carpet Area, Built-up Area, High-Rise, and Amenity Space.',
        'lead_summary': 'Master the 141 legal definitions of Regulation 1.3 that govern every calculation, plan submission, and municipal scrutiny in Maharashtra. Understand the 10 parent acts and the 6 foundational conceptual distinctions.',
        'amendment_cite': None,
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            In statutory planning, words do not carry their colloquial dictionary meanings — they carry strict legal definitions. Regulation 1.3 establishes <strong>141 numbered statutory definitions</strong> that form the foundational vocabulary for development control across Maharashtra.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>The 10 Parent Acts (Gap-Filling Rule):</strong> Where a term is not explicitly defined in UDCPR, its definition is legally imported from one of 10 designated statutes:
              <span style="display:block; font-family:var(--mono); font-size:11px; color:var(--blueprint); margin-top:4px;">
                1. MRTP Act 1966 • 2. MMC Act 1949 • 3. Nagpur Improvement Trust Act 1936 • 4. Municipal Councils Act 1965 • 5. MMRDA Act 2016 • 6. MLR Code 1966 • 7. RERA 2016 • 8. NBC 2016 • 9. MHADA Act 1976 • 10. Slum Act 1971.
              </span>
            </li>
            <li><strong>The 6 Critical Conceptual Distinctions:</strong>
              <ol style="padding-left:18px; margin-top:6px; display:flex; flex-direction:column; gap:6px;">
                <li><strong>FSI vs Built-up Area vs Carpet Area:</strong>
                  <em>Carpet Area</em> (Reg 1.3(26)) is the net usable floor area excluding external walls, service shafts, and exclusive balconies (aligned with RERA).
                  <em>Built-up Area</em> (Reg 1.3(23)) is the total area covered by the building on all floors.
                  <em>FSI Area</em> is the built-up area counted towards the permissible plot ratio (excluding statutory free-of-FSI exemptions).
                </li>
                <li><strong>Gross Plot Area vs Net Plot Area (Reg 1.3(80)):</strong>
                  Gross area is the total cadastral survey number area. Net Plot Area is the balance developable land after deducting DP roads, public reservations, and surrendered amenity spaces.
                </li>
                <li><strong>Recreational Open Space (ROS, Reg 1.3(106)) vs Amenity Space (Reg 1.3(7)):</strong>
                  ROS is 10% mandatory layout green space for residents' recreation. Amenity Space is civic infrastructure land (schools, clinics, substations) provided in addition to ROS.
                </li>
                <li><strong>High-Rise Building Threshold (Reg 1.3(61)):</strong>
                  Defined as any building having a height of <strong>15.0 meters or more</strong> above average ground level (distinct from low-rise structures &lt; 15m).
                </li>
                <li><strong>Congested (Gaothan) vs Non-Congested Area (Reg 1.3(34)):</strong>
                  Congested areas represent core old village settlements/bazaars with relaxed setbacks and higher baseline FSI, versus planned outer suburban layouts.
                </li>
                <li><strong>Transferable Development Rights (TDR, Reg 1.3(134)) &amp; DRC (Reg 1.3(41)):</strong>
                  Compensation in the form of FSI certificates awarded for surrendering reserved land or road widening to the Planning Authority.
                </li>
              </ol>
            </li>
          </ul>
        """,
        'statutory_extract': "Words and expressions which are not defined in these Regulations, shall have the same meaning or sense as in the Maharashtra Regional and Town Planning Act, 1966... the Maharashtra Municipal Corporations Act, 1949... Real Estate (Regulation and Development) Act, 2016; National Building Code of India, 2016...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--blueprint);">REG. 1.3(26) CARPET AREA (RERA ALIGNED)</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                "The net usable floor area of an apartment, excluding the area covered by the external walls, areas under services shafts, exclusive balcony or verandah area and exclusive open terrace area, but includes the area covered by the internal partition walls of the apartment."
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--blueprint);">REG. 1.3(61) HIGH-RISE BUILDING</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                "High-rise Building means a building having a height of 15 m. or more above the average surrounding ground level." Buildings crossing 15m immediately trigger mandatory 6.0m fire tender driveways and H/5 setbacks.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_006 // AREA ENVELOPES</span>
              <span class="fig-title">Spatial Hierarchy: Gross Plot, Net Plot, Built-up &amp; Carpet Area</span>
            </div>
            <div class="plate-content" style="padding:16px 8px; font-family:var(--mono); font-size:12px; color:var(--ink); line-height:1.8;">
              LAND &amp; BUILDING AREA COMPARATIVE HIERARCHY<br>
              ├── PLOT LEVEL (REG. 1.3(80) &amp; REG. 3.9)<br>
              │    ├── GROSS PLOT AREA (Cadastral / 7/12 Extract Total Area)<br>
              │    │    ├── DEDUCTION 1: Sanctioned DP Road Widening Area<br>
              │    │    ├── DEDUCTION 2: Sanctioned DP Public Reservations (Schools, Gardens, etc.)<br>
              │    │    └── DEDUCTION 3: Amenity Space Surrendered (Reg. 3.5)<br>
              │    └── = NET PLOT AREA (Eligible Base for Basic FSI Calculation)<br>
              │<br>
              └── FLOOR LEVEL (REG. 1.3(23), 1.3(26) &amp; 1.3(53))<br>
                   ├── PLINTH AREA &rarr; Footprint of structure touching ground<br>
                   ├── BUILT-UP AREA (BUA) &rarr; Total covered area including walls and balconies<br>
                   ├── FSI CHARGEABLE AREA &rarr; BUA minus Free-of-FSI Exemptions (Lifts, Stairs, Voids)<br>
                   └── RERA CARPET AREA &rarr; Net usable apartment floor inside external walls
            </div>
            <div class="plate-caption">
              FIG_006: Area taxonomy illustrating the legal differences between land calculation bases and building floor takeoff areas under UDCPR Regulation 1.3.
            </div>
          </div>
        """,
        'worked_example_html': """
          <h4 style="font-size:1.05rem; margin-bottom:10px; color:var(--ink);">
            Scenario: Area Takeoff for a 2-BHK Tenement Floor Plan
          </h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); margin-bottom:14px;">
            A student architect is preparing drawings for a 2-BHK unit with an enclosed living room, two bedrooms, kitchen, internal partition walls, an attached utility balcony, and an external wall envelope:
          </p>
          <div class="worked-step">
            <span class="step-badge">RERA CARPET</span>
            <div>
              <strong>Net Internal Floor Area:</strong> Living (22 sq.m) + Bed 1 (14 sq.m) + Bed 2 (12 sq.m) + Kitchen (9 sq.m) + Toilets (7 sq.m) + Internal Walls (4 sq.m) = <strong>68.00 sq.m RERA Carpet Area.</strong>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">BALCONY / UTILITY</span>
            <div>
              <strong>Balcony Area (Enclosed):</strong> 6.00 sq.m attached utility balcony. Excluded from RERA carpet, but included in UDCPR Built-up Area.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">EXTERNAL WALLS</span>
            <div>
              <strong>External Perimeter Walls:</strong> 6.50 sq.m of exterior building skin masonry.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">BUA TOTAL</span>
            <div>
              <strong>Total Built-up Area (BUA):</strong> 68.00 (Carpet) + 6.00 (Balcony) + 6.50 (Ext Walls) = <strong>80.50 sq.m Built-up Area.</strong>
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ KEY LESSON: RERA Carpet (68 sq.m) &ne; Built-up Area (80.5 sq.m). FSI is computed on BUA minus permitted deductions.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Confusing Amenity Space with Recreational Open Space (ROS)</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Recreational Open Space (10% ROS under Reg. 3.4) and Amenity Space (Reg. 3.5) have two completely separate definitions under Reg 1.3(106) and Reg 1.3(7). ROS belongs exclusively to the residents of the layout, while Amenity Space is civic infrastructure that can be surrendered to the municipal corporation for public utilities. They cannot be merged or substituted.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Overlooking the 15.0m High-Rise Classification</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 1.3(61), a building measuring 15.10m is legally a <strong>High-Rise Building</strong>. Many designers design a Ground + 4 storey structure with decorative parapets that exceeds 15.0m, suddenly triggering mandatory 6.0m all-round fire access driveways and H/5 setbacks that make the scheme unviable on smaller plots.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Using Commercial Advertised "Super Built-up" in Sanctions</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              The term "Super Built-up Area" does NOT exist anywhere in UDCPR-2020 or RERA. It is an unregulated real estate marketing term. Municipal approval scrutiny strictly checks Built-up Area (Reg. 1.3(23)) and Net Plot Area (Reg. 1.3(80)).
            </p>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.6;">
            Regulation 1.3 definitions have been clarified across numerous government directives (such as the inclusion of senior citizen housing in Amenity Space, and clarification on carpet area measurement under RERA harmonization). Use our dedicated <a href="/glossary.html" style="color:var(--blueprint); font-weight:600;">Statutory Glossary (141 Terms)</a> to search every single definition verbatim.
          </p>
        """,
        'quiz': [
          {
            'question': "What is the statutory threshold height at which a structure is classified as a 'High-Rise Building' under UDCPR Regulation 1.3(61)?",
            'options': [
              "12.0 meters",
              "15.0 meters",
              "24.0 meters",
              "36.0 meters"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.3(61), any building having a height of 15.0 meters or more above the average surrounding ground level is classified as a High-Rise Building."
          },
          {
            'question': "Which statute provides the definition of 'Carpet Area' as incorporated into UDCPR Regulation 1.3(26)?",
            'options': [
              "Maharashtra Regional & Town Planning Act, 1966",
              "Real Estate (Regulation and Development) Act, 2016 (RERA)",
              "Indian Contract Act, 1872",
              "Transfer of Property Act, 1882"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 1.3(26) explicitly harmonizes the definition of Carpet Area with the Real Estate (Regulation and Development) Act, 2016 (RERA)."
          },
          {
            'question': "If a planning or architectural term is NOT defined in UDCPR-2020, which of the following is an authorized parent act for its legal meaning under Regulation 1.3?",
            'options': [
              "National Building Code of India (NBC) 2016",
              "Maharashtra Municipal Corporations Act, 1949",
              "Maharashtra Land Revenue Code, 1966",
              "All of the above"
            ],
            'correctAnswer': 3,
            'explanation': "Regulation 1.3 lists 10 governing acts including the MRTP Act, MMC Act, NBC 2016, and MLR Code 1966 to fill legal definition gaps."
          },
          {
            'question': "What is the key legal difference between Recreational Open Space (ROS) and Amenity Space under Regulation 1.3?",
            'options': [
              "ROS is for private layout residents, while Amenity Space is civic infrastructure that may be surrendered to the municipal authority",
              "ROS must be paved with asphalt, while Amenity Space must be a lawn",
              "There is no difference; the terms are 100% interchangeable",
              "ROS only applies in Mumbai, while Amenity Space applies in Pune"
            ],
            'correctAnswer': 0,
            'explanation': "Under Reg. 1.3(106) and 1.3(7), Recreational Open Space is mandatory layout greenery for residents, whereas Amenity Space is civic public infrastructure (schools, clinics, substations) provided in addition to ROS."
          }
        ],
        'prev_url': '/lessons/reg-1-1-jurisdiction-and-extent.html',
        'prev_title': 'Reg. 1.1 Extent & Scope',
        'next_url': '/lessons/reg-1-5-savings-and-interpretation.html',
        'next_title': 'Reg. 1.5 Savings Clause'
    },

    # -------------------------------------------------------------------------
    # LESSON 1.3: REG. 1.5
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-1-5-savings-and-interpretation.html',
        'lesson_id': 'lesson-reg-1-5',
        'quiz_id': 'quiz-reg-1-5',
        'clause': 'Reg. 1.5',
        'title': 'The Savings Clause, Transition & Migration Framework',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Regulation 1.5 Savings Clause in UDCPR-2020. Transition rules for earlier approved projects, 1-year validity, balance potential calculation, step-margin rules, and fee adjustments.',
        'lead_summary': 'Learn how projects approved before December 2, 2020 transition to UDCPR-2020. Understand permission validity periods, the choice between erstwhile regulations vs UDCPR, balance potential calculation, step-margin rules, and fee adjustments.',
        'amendment_cite': 'CR.236/18',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            When a new statewide building code is enacted, thousands of projects are already in various stages of sanction and construction. <strong>Regulation 1.5 (Savings)</strong> establishes the transitional bridge between legacy municipal regulations and UDCPR-2020.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Legal Protection of Prior Actions:</strong> Any development permission granted or development proposal where <em>action is taken</em> under erstwhile regulations remains valid. "Action taken" explicitly includes the issuance of a formal demand letter for development charges following in-principle plan approval.</li>
            <li><strong>Validity &amp; Lapsing Clock:</strong>
              If a permission was issued before UDCPR and work did NOT commence within its 1-year validity period, it lapses unless renewed in time. A valid permission may be renewed annually, but the <strong>total extended period shall in no case exceed 3 years</strong>.
            </li>
            <li><strong>The Two Developer Paths:</strong>
              <ul style="padding-left:18px; margin-top:6px; display:flex; flex-direction:column; gap:6px;">
                <li><strong>Option A: Continue under Erstwhile Regulations in Toto:</strong>
                  The developer may proceed strictly as per the old sanction. (During COVID-19, orders CR.236/18 permitted pending erstwhile proposals to be disposed until 31<sup>st</sup> January, 2022).
                </li>
                <li><strong>Option B: Migrate to UDCPR-2020 (The Expansion Path):</strong>
                  If the project is ongoing and full Occupation Certificate has not been issued, the owner can apply for revised permission under UDCPR to unlock higher FSI.
                </li>
              </ul>
            </li>
            <li><strong>The 6 Statutory Rules of Migration:</strong>
              <ol style="padding-left:18px; margin-top:6px; display:flex; flex-direction:column; gap:6px;">
                <li><em>Balance Development Potential Math (Reg. 1.5(c)):</em> Total development potential is computed for the entire plot under UDCPR-2020. From this, the sanctioned FSI of retained buildings is deducted. The resulting figure is the <strong>Balance Development Potential</strong>.</li>
                <li><em>Ancillary FSI Restriction:</em> Ancillary Area FSI (up to 60% for residential) is permissible <strong>strictly on the balance development potential</strong>, NOT on the earlier consumed FSI!</li>
                <li><em>Fee Adjustment &amp; No Refunds (Reg. 1.5(b)):</em> Premiums and charges paid earlier against FSI or industrial conversions are credited against revised UDCPR fees. However, <strong>no cash refund is permitted in any circumstance</strong>.</li>
                <li><em>Step-Margin Rule (Reg. 1.5(d)):</em> If a building was sanctioned up to 16.0m with 3.0m side margins under old rules and work is in progress, the 3.0m margin is allowed up to 16m. Height above 16m must provide $H/5$ setbacks in the form of a step-margin.</li>
                <li><em>Fire CFO NOC Waiver (Reg. 1.5(c) Proviso):</em> For approved group housing layouts with buildings having heights between 15.0m and 24.0m that comply with Reg 1.3(93)(xiv), fresh CFO NOC is NOT required on migration!</li>
                <li><em>Minor Amendments on OC (Reg. 1.5(h)):</em> When applying for Occupancy Certificate, internal locational shifts and area variations up to <strong>5% per floor</strong> within permissible FSI may be approved as minor amendments.</li>
              </ol>
            </li>
          </ul>
        """,
        'statutory_extract': "Notwithstanding anything contained in these regulations, any development permission granted or any development proposal for which any action is taken under the erstwhile regulations shall be valid and continue to be so valid... In case the development is started with due permission before these regulations have come into force, and if the owner / developer, at his option, thereafter seeks further development... then the provision of these regulations shall apply to the balance development...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--amber);">THE STEP-MARGIN RULE (REG. 1.5(d))</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                "In case of a building sanctioned under the erstwhile regulations as non-special one with a height of 16 m. with 3.0 m. setbacks and the construction work is in progress, then while revising the plan under these regulations, for height up to 16.0 m., the setbacks as per the erstwhile regulations shall be allowed to be continued and for the height above 16.0 m. (instead of 15.0 m.), setback as per H / 5 requirement shall be insisted in the form of step-margin."
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--brick);">FEE ADJUSTMENT &amp; NO REFUNDS (REG. 1.5(b))</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                "The charges / premium under these regulations shall be leviable against the revised permission and the charges / premium paid earlier shall be adjusted against the revised charges / premium under these regulations. Provided that no refund is permissible in any case."
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_007 // TRANSITION LOGIC</span>
              <span class="fig-title">UDCPR Migration Decision Flowchart &amp; Balance Potential Distribution</span>
            </div>
            <div class="plate-content" style="padding:16px 8px; font-family:var(--mono); font-size:12px; color:var(--ink); line-height:1.8;">
              ONGOING DEVELOPMENT TRANSITION WORKFLOW (REG. 1.5)<br>
              ├── Project Approved Prior to 02 Dec 2020<br>
              │    ├── Check Commencement Validity (1 Year Base, Max 3 Years Extended)<br>
              │    │    ├── IF Expired &amp; Not Renewed &rarr; Permission Lapsed (Submit fresh proposal under UDCPR)<br>
              │    │    └── IF Valid &amp; Work Commenced &rarr; Choose Strategic Path:<br>
              │    │<br>
              │    ├── OPTION A: RETAIN ERSTWHILE CODE IN TOTO<br>
              │    │    ├── Keep earlier FSI, earlier setbacks, earlier premium receipts<br>
              │    │    └── Complete construction and obtain OC under legacy by-laws<br>
              │    │<br>
              │    └── OPTION B: MIGRATE TO UDCPR-2020 (REVISED SANCTION)<br>
              │         ├── 1. Compute Total Potential under UDCPR (e.g. 2.00 FSI)<br>
              │         ├── 2. Deduct Sanctioned FSI of Retained Buildings (e.g. 1.10 FSI)<br>
              │         ├── 3. Arrive at Balance Potential (0.90 FSI)<br>
              │         ├── 4. Apply Ancillary FSI (60%) ONLY to Balance Potential<br>
              │         ├── 5. Credit earlier premium payments against UDCPR fees (No refunds)<br>
              │         ├── 6. Apply Step-Margin for height above 16.0m ($H/5$ setback)<br>
              │         └── 7. If height &le; 24m &amp; layout approved &rarr; Fire CFO NOC waived!
            </div>
            <div class="plate-caption">
              FIG_007: Statutory decision architecture governing ongoing projects transitioning from legacy municipal by-laws to UDCPR-2020 under Regulation 1.5.
            </div>
          </div>
        """,
        'worked_example_html': """
          <h4 style="font-size:1.05rem; margin-bottom:10px; color:var(--ink);">
            Scenario: Migrating an Ongoing 5,000 sq.m Pune Housing Project to UDCPR
          </h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); margin-bottom:14px;">
            A developer in Pune has an ongoing residential project on a 5,000 sq.m net plot abutting an 18m road. Under erstwhile PMC DCR, they were sanctioned Basic FSI 1.00 (5,000 sq.m BUA), which is currently built up to the 4th floor. They now apply to migrate to UDCPR to add a new tower:
          </p>
          <div class="worked-step">
            <span class="step-badge">STEP 1</span>
            <div>
              <strong>Total UDCPR Potential on 18m Road (Table 6-A):</strong><br>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">
                Maximum Permissible FSI = 2.00 (Basic 1.10 + Premium 0.50 + TDR 0.40).<br>
                Total Gross Potential = 5,000 sq.m &times; 2.00 = <strong>10,000.00 sq.m.</strong>
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">STEP 2</span>
            <div>
              <strong>Compute Balance Development Potential (Reg. 1.5(c)):</strong><br>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">
                Balance Potential = Total Potential (10,000 sq.m) - Retained Sanctioned BUA (5,000 sq.m) = <strong>5,000.00 sq.m.</strong>
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">STEP 3</span>
            <div>
              <strong>Permissible Ancillary Area FSI (Reg. 1.5(c) Proviso):</strong><br>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">
                Residential Ancillary FSI is 60%.<br>
                Permissible Ancillary FSI = 5,000 sq.m (Balance Potential) &times; 0.60 = <strong>3,000.00 sq.m.</strong><br>
                <em>(Note: Developer CANNOT claim 60% on the earlier 5,000 sq.m!)</em>
              </span>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">STEP 4</span>
            <div>
              <strong>Premium Adjustment &amp; Final Sanction:</strong><br>
              <span style="font-size:0.85rem; color:var(--ink-soft);">
                Earlier paid premium charges are adjusted against the new premium FSI fees. The developer can construct the new 5,000 sq.m tower + 3,000 sq.m ancillary area.
              </span>
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ FINAL TALLY: 5,000 sq.m existing retained + 5,000 sq.m balance BUA + 3,000 sq.m ancillary BUA approved.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Claiming Ancillary FSI on the Entire Plot Potential</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Architects frequently calculate the 60% Ancillary FSI on the total 10,000 sq.m (claiming 6,000 sq.m ancillary). Regulation 1.5(c) strictly states: <em>"ancillary FSI shall be permissible only on such balance potential."</em> On a 5,000 sq.m balance, only 3,000 sq.m ancillary can be granted.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Demanding Cash Refunds for Excess Past Payments</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              If a developer paid a very high premium under an older special scheme and the new UDCPR calculation results in a lower liability, Regulation 1.5(b) unequivocally specifies: <em>"Provided that no refund is permissible in any case."</em> The excess is absorbed by the authority.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Missing the 3-Year Maximum Extension Ceiling</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              While Regulation 1.5 allows annual renewal of development permissions, it adds a hard ceiling: <em>"such extended period shall in no case exceed three years."</em> If construction has not commenced within 3 years of extensions, the permission lapses entirely, requiring a fresh proposal under UDCPR.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">(#) Govt Orders CR.236/18 (Part 1)</span>
            <span style="font-family:var(--mono); font-size:0.8rem; color:var(--ink-soft);">Issued 01 March 2021, 26 July 2021 &amp; 02 Dec 2021</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.6;">
            <strong>Transitional Orders:</strong> Regulation 1.5 was amended multiple times during 2021 to protect projects delayed by the COVID-19 pandemic.
          </p>
          <p style="font-size:0.88rem; color:var(--ink); margin-top:8px; line-height:1.6;">
            <strong>Key Amendments:</strong> (1) The deadline for disposing pending proposals under erstwhile regulations was extended up to 31<sup>st</sup> January, 2022. (2) Explicit wording was inserted allowing fee adjustments without refund. (3) Provisos were added granting Fire CFO NOC waivers for group housing buildings between 15m and 24m.
          </p>
        """,
        'quiz': [
          {
            'question': "How is 'Balance Development Potential' calculated when an ongoing project migrates to UDCPR-2020 under Regulation 1.5(c)?",
            'options': [
              "Total UDCPR potential minus the sanctioned FSI of retained buildings",
              "By doubling the carpet area of the existing building",
              "By ignoring the existing buildings completely and building fresh",
              "By taking 50% of the gross cadastral plot area"
            ],
            'correctAnswer': 0,
            'explanation': "Regulation 1.5(c) stipulates that the development potential of the entire plot is computed under UDCPR, from which the sanctioned FSI of retained buildings is deducted to arrive at the balance potential."
          },
          {
            'question': "On what quantum of area is the 60% residential Ancillary Area FSI permissible in a migrated ongoing project?",
            'options': [
              "On the total gross plot potential",
              "Strictly on the Balance Development Potential only",
              "On the retained old building only",
              "Ancillary FSI is completely prohibited for migrated projects"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 1.5(c) explicitly mandates that 'ancillary FSI shall be permissible only on such balance potential', preventing developers from claiming ancillary FSI on already constructed structures."
          },
          {
            'question': "What happens if premium charges paid earlier under erstwhile DCR exceed the revised charges payable under UDCPR-2020?",
            'options': [
              "The planning authority issues an immediate bank refund with interest",
              "The excess amount can be transferred to any other plot in Maharashtra",
              "No refund is permissible in any case under Regulation 1.5(b)",
              "The municipal commissioner receives a personal surcharge"
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 1.5(b) explicitly establishes that earlier charges are adjusted against revised fees, 'Provided that no refund is permissible in any case'."
          },
          {
            'question': "What is the maximum cumulative period for which a valid development permission can be extended before it lapses under Regulation 1.5?",
            'options': [
              "1 year",
              "2 years",
              "3 years",
              "5 years"
            ],
            'correctAnswer': 2,
            'explanation': "Under Regulation 1.5, valid permissions can be renewed annually, 'but such extended period shall in no case exceed three years'."
          }
        ],
        'prev_url': '/lessons/reg-1-3-statutory-definitions.html',
        'prev_title': 'Reg. 1.3 Definitions',
        'next_url': '/lessons/reg-1-6-legal-hierarchy-and-interpretations.html',
        'next_title': 'Reg. 1.6-1.10 Hierarchy & Directives'
    },

    # -------------------------------------------------------------------------
    # LESSON 1.4: REG. 1.6 TO 1.10
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-1-6-legal-hierarchy-and-interpretations.html',
        'lesson_id': 'lesson-reg-1-6',
        'quiz_id': 'quiz-reg-1-6',
        'clause': 'Reg. 1.6 to 1.10',
        'title': 'Legal Hierarchy, Environmental Overrides & Dispute Interpretation',
        'badge_status': 'Core Foundation',
        'ch_slug': 'ch01',
        'ch_title': 'Chapter 1: Administration',
        'meta_desc': 'Regulations 1.6 to 1.10 of Maharashtra UDCPR-2020: CRZ & Eco-sensitive overrides, document supremacy, ASR timing rule, English language supremacy, and State Government dispute resolution.',
        'lead_summary': 'Master the legal hierarchy and dispute mechanisms of UDCPR: external environmental overrides (CRZ, Western Ghats), document supremacy (text vs appendices), ASR timing rules, the English language supremacy doctrine, and the State Government dispute resolution authority.',
        'amendment_cite': 'CR.121/21',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            In architectural practice and municipal scrutiny, conflicts routinely arise between different planning documents, between regional and national statutes, between English and Marathi gazettes, or over the interpretation of a clause. Regulations 1.6 through 1.10 establish the <strong>legal hierarchy, supremacy rules, and appellate mechanisms</strong> that govern all disputes.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Overriding Environmental Regimes (Reg. 1.6):</strong>
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><em>Coastal Regulation Zone (CRZ):</em> Development within CRZ areas is strictly governed by MoEF&amp;CC Notifications (2011 and 2019). Where CRZ norms are more restrictive, CRZ prevails.</li>
                <li><em>Western Ghats Eco-Sensitive Area:</em> Environmental restrictions issued by the Central Government for the Western Ghats corridor override local municipal allowances.</li>
              </ul>
            </li>
            <li><strong>Statutory Document Supremacy (Reg. 1.7):</strong>
              <em>"Notwithstanding anything contained in any Appendices / Proformas, provision in respective regulations shall prevail."</em> If an Appendix form or calculation sheet (Appendices A to M) contains a contradiction or discrepancy with the main regulation text, the <strong>main regulation text is legally supreme</strong>.
            </li>
            <li><strong>The Ready Reckoner (ASR) Year Rule (Reg. 1.8):</strong>
              Where premium FSI or municipal charges are calculated as a percentage of the Annual Statement of Rates (ASR), the rate applied must be the <strong>ASR rate of the year of granting the permission</strong>, NOT the year of application submission!
            </li>
            <li><strong>The 4 Foundational Rules of Interpretation (Reg. 1.9):</strong>
              <ol style="padding-left:18px; margin-top:6px; display:flex; flex-direction:column; gap:6px;">
                <li><em>Clear Dimensions Rule:</em> Room sizes and spatial dimensions specify <strong>clear internal dimensions</strong>. Normal plastering, tile-cladding, and surface finishes cannot be disputed by scrutiny inspectors unless they alter the external building footprint.</li>
                <li><em>Grammatical Construction:</em> Present tense includes future tense; masculine gender includes feminine and neuter; singular includes plural; 'writing' includes digital communication and electronic signatures.</li>
                <li><em>Language Conflict Rule (Reg. 1.9(vii)):</em> If both English and Marathi versions of UDCPR exist and any conflict or ambiguity arises between the two, the <strong>interpretation of the ENGLISH VERSION SHALL PREVAIL</strong>.</li>
                <li><em>Final Appellate Authority (Reg. 1.9(v)):</em> If any dispute arises between an applicant and a Planning Authority regarding the interpretation of any clause, the matter must be referred to the <strong>State Government (Urban Development Department)</strong>. The Government's decision is <strong>final, conclusive, and binding</strong> on all parties.</li>
              </ol>
            </li>
            <li><strong>Removal of Difficulties &amp; Clarification Directives (Reg. 1.10):</strong>
              Empowers the State Government to issue gazetted orders and directives to remove operational difficulties — the legal foundation of all 52 government clarifications marked with the <strong>(#)</strong> symbol throughout UDCPR.
            </li>
          </ul>
        """,
        'statutory_extract': "Notwithstanding anything contained in any Appendices / Proformas, provision in respective regulations shall prevail... Wherever the rate of premium is to be decided based on rates mentioned in ASR, rate in the ASR shall be of the year of granting the permission... If a Marathi version of these Regulations exists and if there is a conflict in interpretation of any clause between English & Marathi versions of these Regulations, then the interpretation of English version shall prevail... The decision of the Government on the interpretation of these regulations shall be final and binding...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--blueprint);">REG. 1.9(vii) ENGLISH SUPREMACY</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                "If a Marathi version of these Regulations exists and if there is a conflict in interpretation of any clause between English &amp; Marathi versions of these Regulations, then the interpretation of English version shall prevail."
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); padding:16px;">
              <span class="kicker" style="color:var(--blueprint);">REG. 1.9(v) STATE GOVERNMENT ARBITRATION</span>
              <p style="font-size:0.86rem; color:var(--ink-soft); line-height:1.55; margin-top:6px;">
                "If any question or dispute arises with regard to interpretation of any of these regulations the matter shall be referred to the State Government, who, after considering the matter... shall give a decision... The decision of the Government shall be final and binding."
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div class="blueprint-plate">
            <div class="blueprint-plate-header">
              <span class="fig-number">FIG_008 // LEGAL HIERARCHY</span>
              <span class="fig-title">Maharashtra Planning Document Legal Precedence Pyramid</span>
            </div>
            <div class="plate-content" style="padding:16px 8px; font-family:var(--mono); font-size:12px; color:var(--ink); line-height:1.8;">
              STATUTORY PRECEDENCE &amp; CONFLICT RESOLUTION LADDER<br>
              LEVEL 1: CONSTITUTIONAL &amp; CENTRAL ENVIRONMENTAL ACTS (CRZ 2019, MoEF&amp;CC Western Ghats, RERA 2016)<br>
              ▲ Overrides all state development control rules in designated environmental zones<br>
              │<br>
              LEVEL 2: PARENT ENABLING STATUTE (MRTP Act, 1966 &amp; MMC Act, 1949)<br>
              ▲ Statutory parent under which UDCPR is enacted and sanctioned<br>
              │<br>
              LEVEL 3: MAIN REGULATION CLAUSES OF UDCPR-2020 (English Gazette Text)<br>
              ▲ Legally supreme over Marathi translations and overrides all attached Appendices<br>
              │<br>
              LEVEL 4: GOVERNMENT ORDERS &amp; DIRECTIVES UNDER REG. 1.10 (Symbol '#' Clauses)<br>
              ▲ Executive clarifications issued by Urban Development Department to resolve ambiguities<br>
              │<br>
              LEVEL 5: APPENDICES &amp; PROFORMAS (Appendices A to M)<br>
              ▲ Standard forms and application templates; subordinate to main regulation text (Reg. 1.7)
            </div>
            <div class="plate-caption">
              FIG_008: Hierarchy of legal authority showing that main regulation clauses prevail over Appendices, English text prevails over translations, and UDD is the sole final arbiter.
            </div>
          </div>
        """,
        'worked_example_html': """
          <h4 style="font-size:1.05rem; margin-bottom:10px; color:var(--ink);">
            Scenario: Resolving an ASR Rate Dispute between Financial Years
          </h4>
          <p style="font-size:0.88rem; color:var(--ink-soft); margin-bottom:14px;">
            An architect submitted a building proposal for Premium FSI in PMC on 15<sup>th</sup> March 2024 when the land ASR rate was ₹40,000/sq.m. Due to departmental backlog, the municipal scrutiny was completed and the formal Commencement Certificate (CC) was granted on 18<sup>th</sup> April 2024 — after the state notified new ASR rates of ₹44,000/sq.m on 1<sup>st</sup> April 2024:
          </p>
          <div class="worked-step">
            <span class="step-badge">ISSUE</span>
            <div>
              The developer argues that premium should be calculated at the submission rate of ₹40,000/sq.m because the delay was caused by the municipal corporation.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">RULING</span>
            <div>
              <strong>Regulation 1.8 Mandate:</strong> <em>"Wherever the rate of premium is to be decided based on rates mentioned in ASR, rate in the ASR shall be of the year of granting the permission."</em>
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">OUTCOME</span>
            <div>
              Since the formal permission was granted in financial year 2024-25 (18<sup>th</sup> April 2024), the legally mandated rate is <strong>₹44,000/sq.m</strong>. The municipal corporation's demand note based on the new rate is fully lawful.
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ KEY TAKEAWAY: Budgeting for premium FSI must always anticipate ASR revisions if approval is expected near the April 1st fiscal boundary.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Relying on Subordinate Appendices over Main Regulation Clauses</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 1.7, if an architectural draftsman follows a format in Appendix A or an older calculation sheet that contradicts a specific clause in Chapters 3, 6, or 8, the proposal will be rejected. The main regulation text explicitly overrides all attached Appendices.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Disputing Minor Internal Wall Finishes</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 1.9(iv), room dimensions mean clear internal dimensions, but the code explicitly protects architects against hyper-technical scrutiny: <em>"sizes and dimensions may not be disputed with reference to finished/unfinished surfaces unless they affect overall dimensions of the building."</em> A 15mm difference from thick wall plaster cannot be cited by an inspector to reject an Occupancy Certificate.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Citing Local Circulars Against State Government Rulings</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Municipal corporations occasionally issue internal administrative circulars that misinterpret UDCPR provisions. Regulation 1.9(v) reserves the power of authoritative interpretation exclusively to the State Government (Urban Development Department). Local circulars conflicting with state clarifications are ultra vires and void.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">(#) Corrigendum CR.121/21</span>
            <span style="font-family:var(--mono); font-size:0.8rem; color:var(--ink-soft);">Dated 02nd December, 2021</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.6;">
            <strong>Proforma Supremacy Clarification:</strong> In Regulation 1.7, the Government inserted the opening clarification: <em>'Notwithstanding anything contained in any Appendices / Proformas, provision in respective regulations shall prevail.'</em> This firmly eliminated scrutiny confusion between application forms and substantive building rules.
          </p>
        """,
        'quiz': [
          {
            'question': "If a conflict or discrepancy arises between the English and Marathi gazette texts of UDCPR-2020, which version legally prevails under Regulation 1.9(vii)?",
            'options': [
              "The Marathi version always prevails",
              "The English version shall prevail",
              "Both versions are cancelled and referred to the High Court",
              "Whichever version benefits the builder more"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.9(vii), 'If a Marathi version of these Regulations exists and if there is a conflict in interpretation of any clause between English & Marathi versions of these Regulations, then the interpretation of English version shall prevail.'"
          },
          {
            'question': "Which ASR (Annual Statement of Rates / Ready Reckoner) year must be used when calculating premium FSI charges under Regulation 1.8?",
            'options': [
              "The ASR rate of the year when the plot was first purchased",
              "The ASR rate of the year when the application was originally submitted",
              "The ASR rate of the year of granting the permission",
              "The lowest ASR rate over the past five years"
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 1.8 explicitly mandates that 'Wherever the rate of premium is to be decided based on rates mentioned in ASR, rate in the ASR shall be of the year of granting the permission.'"
          },
          {
            'question': "If a form or proforma in Appendix A contradicts a clause in the main body of UDCPR-2020, which document prevails under Regulation 1.7?",
            'options': [
              "The proforma in the Appendix prevails",
              "The main regulation clause prevails over the Appendix",
              "The architect chooses either one arbitrarily",
              "The local police department decides"
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 1.7 states: 'Notwithstanding anything contained in any Appendices / Proformas, provision in respective regulations shall prevail.'"
          },
          {
            'question': "Who is the final, conclusive appellate authority for resolving disputes regarding the interpretation of UDCPR regulations under Regulation 1.9(v)?",
            'options': [
              "The local Municipal Ward Officer",
              "The State Government (Urban Development Department)",
              "The Indian Institute of Architects (IIA)",
              "The local Police Commissioner"
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 1.9(v), all interpretation disputes are referred to the State Government, whose decision is final, conclusive, and binding on all parties."
          }
        ],
        'prev_url': '/lessons/reg-1-5-savings-and-interpretation.html',
        'prev_title': 'Reg. 1.5 Savings Clause',
        'next_url': '/lessons/reg-2-1-development-permission.html',
        'next_title': 'Reg. 2.1 Development Permission'
    }
]

print("================================================================")
print("🚀 GENERATING FULL CHAPTER 1 BLUEPRINT LESSONS (4 LESSONS)")
print("================================================================\n")

for lesson in ch01_lessons:
    create_lesson_page(lesson)

print("\n✓ Chapter 1 lesson suite successfully built and rendered.")
