"""
UDCPR Visual Guide - CHAPTER 2 FULL LESSON BUILDER
Generates the complete 5-lesson curriculum for Chapter 2: Development Permission and Commencement Certificate
Covers Reg 2.1 through 2.15 in exhaustive statutory and educational detail.
"""

import os
import sys
from generate_lessons import create_lesson_page

sys.stdout.reconfigure(encoding='utf-8')

ch02_lessons = [
    # -------------------------------------------------------------------------
    # LESSON 2.1: REG. 2.1 (2.1.1 to 2.1.7)
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-2-1-development-permission.html',
        'lesson_id': 'lesson-reg-2-1',
        'quiz_id': 'quiz-reg-2-1',
        'clause': 'Reg. 2.1',
        'title': 'Development Permission Mandate, Exemptions & Operational Works',
        'badge_status': 'Statutory Foundation',
        'ch_slug': 'ch02',
        'ch_title': 'Chapter 2: Development Permission',
        'meta_desc': 'When is development permission strictly mandatory under UDCPR-2020? Comprehensive guide to the 16 statutory exemptions under Reg 2.1.2, operational constructions under Reg 2.1.4, temporary structures, and tenantable repairs.',
        'lead_summary': 'Master the statutory requirements for obtaining building permissions and commencement certificates under Section 18 and 46 of the MRTP Act, 1966. Learn the 16 explicit statutory exemptions, operational construction boundaries for railways, highways, ports, metro rail, and telecommunications, temporary construction rules, and repair intimations.',
        'amendment_cite': 'CR.121/21 & CR.04/022',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            Under the Maharashtra Regional and Town Planning Act, 1966 (MRTP Act), no land development, subdivision, amalgamation, building erection, re-erection, alteration, or demolition can lawfully commence without prior written permission from the Planning Authority.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Mandatory Permission (Reg. 2.1.1):</strong> A separate Development Permission / Commencement Certificate (CC) must be obtained for each development work or building. The permission must strictly conform to the Regional Plan / Development Plan (MRTP Sec 18 / 46).</li>
            <li><strong>16 Statutory Exemptions (Reg. 2.1.2):</strong> Situations where no formal permission is required, including:
              <ol style="padding-left:18px; margin-top:6px; display:flex; flex-direction:column; gap:4px;">
                <li>Court orders or statutory directions by any lawful authority.</li>
                <li>Statutory works executed by any Authority under governing laws.</li>
                <li>Agricultural excavations (including digging of irrigation wells) in the ordinary course of farming.</li>
                <li>Construction of access roads solely intended for agricultural purposes.</li>
                <li>Temporary use of private land for marriage pandals, religious functions, or festive gatherings.</li>
                <li>Window / ventilator safety grills.</li>
                <li>Electric supply distribution / receiving substations.</li>
                <li>Solar panels on terraces with base height &le; 1.8 m (subject to structural engineer certificate).</li>
                <li>Internal lightweight partitions / dry-wall cabins in commercial buildings (subject to structural engineer stability certificate).</li>
                <li>Temporary on-site storage godowns for building materials during active construction.</li>
                <li>Temporary site offices, sample flats, and watchman chowkies within the project site during construction.</li>
                <li>Temporary machinery storage sheds for factories in industrial zones.</li>
                <li>Labour camps on construction sites provided adequate sanitation, water supply, and safety are ensured.</li>
                <li>Temporary sets for film, TV serial, or advertisement shooting (&le; 1 year, subject to written intimation).</li>
                <li>Low-risk buildings (&le; 150 sq.m) and moderate-risk buildings (150 to 300 sq.m) under fast-track <em>Appendix K</em> self-certification.</li>
                <li><em>Agro-Tourism Centres (inserted dt. 02 June 2022):</em> Construction up to 8 rooms in Agricultural Zone under Maharashtra Tourism Policy-2016 per <em>Appendix K-2</em>.</li>
              </ol>
            </li>
            <li><strong>Government Works (Reg. 2.1.3):</strong> Departments of State/Central Govt must submit plans and measurement sheets to the Authority 60 days prior to commencement under Section 58 of MRTP Act.</li>
            <li><strong>Operational Constructions (Reg. 2.1.4):</strong> Total exemption from permission for operational services: Railways, National Highways, National Waterways, Airports, Ports, Telecom (excluding mobile towers), Power Grids/Substations, Defence, and Metro/Mono Rail infrastructure. Road restoration charges must be reimbursed within 1 month.</li>
            <li><strong>Non-Operational Constructions (Reg. 2.1.5):</strong> Residential staff quarters, colony roads, hospitals, clubs, and schools built by government undertakings <em>DO require full municipal permissions</em>.</li>
            <li><strong>Temporary Constructions (Reg. 2.1.6):</strong> Permissions granted for maximum 6 months at a time, aggregate 1 year (monsoon terrace coverings, exhibition circuses, RMC batching plants, transit rehab camps).</li>
            <li><strong>Repairs to Buildings (Reg. 2.1.7):</strong> Changing doors/windows in same position and strengthening existing walls/roofs in same position requires only written intimation with a licensed engineer certificate, not full building permission.</li>
          </ul>
        """,
        'statutory_extract': "2.1.1 Necessity of Obtaining Permission: No person shall carry out any development work including development of land by laying out into suitable plots or amalgamation of plots or development of any land as group housing scheme or to erect, re-erect or make alterations or demolish any building or cause the same to be done without first obtaining a separate building permit / development permission / commencement certificate for each such development work / building from the Authority... 2.1.2 Permission Not Necessary: No such permission shall be necessary for [the 16 enumerated items]...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
              <span class="kicker">REG. 2.1.4 // EXEMPT OPERATIONAL WORKS</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Operational Infrastructure</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                Railways, National Highways, Aerodromes, Major Ports, Power Grids, Metro Tracks, Viaducts, Metro Stations, Traction Substations, and Underground utilities. No building permit needed, but plans must be shared for record and road restoration paid within 30 days.
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--brick); padding:16px;">
              <span class="kicker" style="color:var(--brick);">REG. 2.1.5 // STRICTLY NON-EXEMPT</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Commercial &amp; Residential Govt Works</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                New residential quarters (except essential gate lodges), railway colony roads, hospitals, clubs, schools, commercial complexes, and telecommunication <strong>mobile towers</strong> are explicitly excluded from operational exemptions and require full sanction.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_009 // PERMISSION &amp; EXEMPTION CLASSIFICATION MATRIX</span>
              <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 2.1 BLUEPRINT</span>
            </div>
            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:12px;">
                <thead>
                  <tr style="background:var(--ink); color:var(--paper-raised);">
                    <th style="padding:8px 10px; text-align:left; border:1px solid var(--line-strong);">Category</th>
                    <th style="padding:8px 10px; text-align:left; border:1px solid var(--line-strong);">Statutory Clause</th>
                    <th style="padding:8px 10px; text-align:left; border:1px solid var(--line-strong);">Regulatory Status</th>
                    <th style="padding:8px 10px; text-align:left; border:1px solid var(--line-strong);">Mandatory Conditions / Filings</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">General Real Estate &amp; Layouts</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.1</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--brick); font-weight:700;">Full CC Mandatory</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Appendix A-1 / A-2 + Scrutiny Fees + Development Charges</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Solar Panels (Terrace)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.2(viii)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Exempt from CC</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Base &le; 1.8m from terrace + Structural Stability Certificate</td>
                  </tr>
                  <tr>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Commercial Internal Cabins</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.2(ix)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Exempt from CC</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Lightweight partitions only + Structural Stability Certificate</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Site Office / Sample Flat / Chowky</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.2(xi)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Exempt from CC</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Within site boundaries only; restricted to construction phase</td>
                  </tr>
                  <tr>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Low-Risk Plots (&le; 150 sq.m)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.2(xv)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--amber); font-weight:700;">Fast-Track / Self-Cert</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Instant acknowledgement under Appendix K; fees deposited</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Agro-Tourism (&le; 8 rooms)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.2(xvi)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Exempt from CC</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Agricultural Zone; compliance with Appendix K-2 &amp; Tourism Policy 2016</td>
                  </tr>
                  <tr>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Operational Rail/Road/Metro</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.4</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Operational Exemption</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Written intimation; road restoration charges paid within 1 month</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Temporary RMC Batching Plant</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.6(viii)</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--amber); font-weight:700;">Temporary Permit</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Max 6 months at a time, aggregate 1 year; removed on completion</td>
                  </tr>
                  <tr>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Structural &amp; Door/Window Repairs</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Reg. 2.1.7</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Intimation Only</td>
                    <td style="padding:8px 10px; border:1px solid var(--line-strong);">Same position only; certificate of licensed personnel required</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="margin-bottom:12px;">
            <strong>Practical Site Scenario:</strong> A developer receives sanctioned Commencement Certificate for a 12-storey residential tower in Pune. Before commencing casting of the building, the developer constructs:
          </p>
          <div class="worked-step">
            <span class="step-badge">ITEM A</span>
            <div>
              <strong>Sample Flat &amp; Site Sales Office (120 sq.m):</strong> Erected on ground within the plot boundary.
              <br><span style="font-family:var(--mono); font-size:0.84rem; color:var(--blueprint);">&#10003; LAWFUL EXEMPTION under Reg. 2.1.2(xi):</span> No separate building permit required. Must be dismantled upon completion of the main building.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">ITEM B</span>
            <div>
              <strong>RMC (Ready Mix Concrete) Batching Plant:</strong> Erected on the rear corner of the site.
              <br><span style="font-family:var(--mono); font-size:0.84rem; color:var(--amber);">&#9888; REQUIRES TEMPORARY PERMISSION under Reg. 2.1.6(viii):</span> Requires formal temporary permission with scrutiny fees, granted for 6 months at a time, renewable up to completion of the main structure.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">ITEM C</span>
            <div>
              <strong>Labour Camp for 60 Construction Workers:</strong> Erected on an adjacent vacant plot owned by another party.
              <br><span style="font-family:var(--mono); font-size:0.84rem; color:var(--brick);">&#10007; VIOLATION under Reg. 2.1.2(xiii):</span> Labour camps are exempt <em>only on the construction site itself</em>. Placing it on an external plot without separate land development approval and sanitation NOC constitutes unauthorized development under Section 52 of MRTP Act.
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ STATUTORY RULE: Ancillary temporary facilities must strictly reside within the sanctioned project boundary and comply with water/sanitation health mandates.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Assuming Mobile Towers are Exempt Operational Utilities</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 2.1.4(e), Posts, Telegraphs, Telephones, Wireless, and Broadcasting are exempt operational constructions, but the clause explicitly states: <em>"excluding Mobile Towers"</em>. Telecommunication mobile towers require formal municipal permission and structural verification under Chapter 14.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Solar Panels Exceeding 1.8m Height from Terrace Slab</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Regulation 2.1.2(viii) exempts solar panel installations only if the base of the panel is at a height up to 1.8 m from the terrace level and accompanied by a Licensed Structural Engineer stability certificate. Installing elevated solar pergolas at 2.4 m to 3.0 m height to create habitable covered terrace space violates building height/FSI rules and requires full building permission.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Altering Wall Positions Under the Guise of "Repairs"</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Regulation 2.1.7 permits door/window replacement and wall/roof strengthening without building permission <em>strictly "in the same position"</em>. Shifting door openings into common lobbies, breaking load-bearing walls, or shifting internal partition walls amounts to alterations requiring formal revised sanction.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">GR CR.04/022 (02 June 2022)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Agro-Tourism 8-Room Exemption</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Inserted item (xvi) into Regulation 2.1.2: Construction up to 8 rooms for an Agro-Tourism Centre and allied activities as per Maharashtra Tourism Policy-2016 in the Agricultural Zone is exempt from regular development permission, subject to compliance with fast-track Appendix K-2.
          </p>
          <div style="display:flex; align-items:center; gap:10px; margin-top:14px; margin-bottom:10px;">
            <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Subdivision &amp; Appendix K Alignment</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Streamlined risk-based classification thresholds for low-risk (&le; 150 sq.m) and moderate-risk (150 to 300 sq.m) residential developments under Appendix K.
          </p>
        """,
        'quiz': [
            {
                'question': 'Which of the following telecom/communication structures is explicitly EXCLUDED from operational exemptions under Regulation 2.1.4(e)?',
                'options': [
                    'Wireless transmission towers of Defence authorities',
                    'Mobile Towers',
                    'Post and Telegraph receiving equipment',
                    'Doordarshan broadcasting antennas'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.1.4(e) exempts Posts, Telegraphs, Telephones, Wireless, and Broadcasting, but specifically notes: 'excluding Mobile Towers'. Mobile towers require formal municipal building permission."
            },
            {
                'question': 'What is the maximum permissible base height for solar panels installed on a terrace to remain exempt from building permission under Reg. 2.1.2(viii)?',
                'options': [
                    'Up to 1.2 m from terrace slab',
                    'Up to 1.8 m from terrace slab (with structural stability cert)',
                    'Up to 2.4 m from terrace slab',
                    'Any height provided it does not cast shadow'
                ],
                'correctAnswer': 1,
                'explanation': "Under Regulation 2.1.2(viii), installation of solar panels having a base at a height up to 1.8 m from the terrace is exempt, provided structural stability is certified by a Licensed Structural Engineer."
            },
            {
                'question': 'For what initial and aggregate maximum duration may the Planning Authority grant permission for temporary constructions like RMC plants or exhibition pandals under Reg. 2.1.6?',
                'options': [
                    '3 months at a time, aggregate 6 months',
                    '6 months at a time, aggregate not exceeding 1 year',
                    '1 year at a time, aggregate 3 years',
                    'Indefinitely until the project finishes'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.1.6 stipulates that the Authority may grant permission for temporary construction for a period not exceeding six months at a time and in aggregate not exceeding one year."
            },
            {
                'question': 'Under Regulation 2.1.7, which of the following repairs can be executed with only a written intimation and licensed personnel certificate rather than a full building permit?',
                'options': [
                    'Adding an extra floor on an existing terrace',
                    'Changing doors and windows in the same position and strengthening existing walls/roof in same position',
                    'Demolishing an internal load-bearing RCC column to widen the living room',
                    'Converting a ground-floor stilt parking area into residential flats'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.1.7 allows changing doors and windows in the same position and strengthening existing walls or roofs in the same position with only written intimation and a licensed personnel certificate."
            }
        ],
        'prev_url': '/lessons/reg-1-6-legal-hierarchy-and-interpretations.html',
        'prev_title': 'Reg. 1.6-1.10 Legal Hierarchy',
        'next_url': '/lessons/reg-2-2-application-procedure.html',
        'next_title': 'Reg. 2.2 Application Procedure'
    },

    # -------------------------------------------------------------------------
    # LESSON 2.2: REG. 2.2 (2.2.1 to 2.2.11 & 2.2.15 to 2.2.19)
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-2-2-application-procedure.html',
        'lesson_id': 'lesson-reg-2-2',
        'quiz_id': 'quiz-reg-2-2',
        'clause': 'Reg. 2.2.1 – 2.2.11 & 2.2.15 – 2.2.19',
        'title': 'Application Procedure, Drawing Standards, Special Buildings & Clearances',
        'badge_status': 'Architectural Standards',
        'ch_slug': 'ch02',
        'ch_title': 'Chapter 2: Development Permission',
        'meta_desc': 'Mandatory submission protocols for UDCPR-2020: Appendix A-1/A-2 notices, 7/12 title verification, drawing scales (Key, Layout, Site, Building plans), Special Building fire requirements, drawing sheet sizes (Table 2-A), and color codes (Table 2-B).',
        'lead_summary': 'Step-by-step statutory procedure for preparing and submitting building and layout proposals in Maharashtra: ownership documents, mandatory drawing scales, requirements for Special Buildings (height >= 15m), inter-departmental clearances (AAI, Railway, Defense, Flood lines), drawing sheet standards, Table 2-B color notations, and professional signing qualifications.',
        'amendment_cite': 'CR.42/21 & CR.121/21',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            Obtaining development sanction requires formal notice accompanied by title records, authenticated cadastral measurements, and standardized technical drawings. Regulation 2.2 establishes an uncompromising statutory template for submissions across Maharashtra.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Notice Form (Reg. 2.2.1):</strong> Application submitted via <strong>Appendix A-1</strong> (land sub-division / layout) or <strong>Appendix A-2</strong> (building erection / alterations) through a registered Architect, Town Planner, Licensed Engineer, or Supervisor. Submissions are mandatorily online via the Authority's portal.</li>
            <li><strong>Ownership &amp; Title Verification (Reg. 2.2.3):</strong>
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li>Latest <strong>7/12 extract</strong> or <strong>Property Register (PR) Card</strong> dated not earlier than <strong>6 months</strong> prior to submission.</li>
                <li>Original <strong>Measurement Plan (Mojni Sheet)</strong> authenticated by the Land Records Department (TILR / City Survey). For un-surveyed Gaothans, an architect-certified plan signed by all adjacent holders is accepted (CR.121/21).</li>
                <li>Area statement by triangulation / CADD verified with an owner's affidavit.</li>
                <li><em>RERA Consent:</em> Where third-party rights (agreements to sale/lease) exist in revised permissions, registered buyer consent under RERA Act, 2016 is mandatory.</li>
              </ul>
            </li>
            <li><strong>Mandatory Drawing Scales:</strong>
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><strong>Key / Location Plan (Reg. 2.2.4):</strong> Scale not less than <strong>1:4000</strong>; showing landmarks within 200 m radius.</li>
                <li><strong>Sub-division / Layout Plan (Reg. 2.2.5):</strong> Scale not less than <strong>1:500</strong> (or <strong>1:1000</strong> for layouts &ge; 4.0 Ha).</li>
                <li><strong>Amalgamation Plan (Reg. 2.2.5(b)):</strong> Scale not less than <strong>1:500</strong>.</li>
                <li><strong>Site Plan (Reg. 2.2.6):</strong> Scale <strong>1:500</strong> (or 1:1000 for plots &gt; 1 Ha) showing boundaries, street widths, HT lines, water courses, and all premises within <strong>12.0 m</strong>.</li>
                <li><strong>Building Plans (Reg. 2.2.7):</strong> Scale <strong>1:100</strong>; all floor plans with P-line (periphery line), carpet area statements, parking layouts, relative street levels, terrace drainage, and at least <strong>two sections with one through the staircase/toilet</strong>.</li>
              </ul>
            </li>
            <li><strong>Special Buildings Mandate (Reg. 2.2.8):</strong> Buildings &ge; 15 m height, educational/assembly/mercantile &ge; 500 sq.m, and hazardous occupancies must provide: minimum <strong>6.0 m clear motorable fire driveway</strong> around the building, fire lifts, smoke-stop lobbies, refuge areas, static water tanks, wet risers, sprinklers, and Provisional CFO Fire NOC.</li>
            <li><strong>Drawing Standards (Reg. 2.2.17 &amp; 2.2.18):</strong> Sheet sizes from A0 (841 &times; 1189 mm) to A4 (210 &times; 297 mm) with standard metric dimensions. Standard color notations under <strong>Table 2-B</strong>: Yellow hatched for demolition, Red filled-in for proposed work, Green for existing street, Red dotted for drainage/sewer, and Thin black dotted for water supply.</li>
            <li><strong>Professional Competence (Reg. 2.2.19 &amp; Appendix C):</strong> COA-registered Architects have unrestricted planning rights statewide without separate municipal licensing. Engineers, Structural Engineers, Town Planners, and Supervisors Grade I/II/III must hold valid registration licenses from the Authority.</li>
          </ul>
        """,
        'statutory_extract': "2.2.1 Notice / Application: Every person who intends to carry out development or redevelopment, erect or re-erect or make alterations in any place in a building or demolish any building, shall give notice / application in writing, through registered Architect, Town Planner or Licensed Engineer / Supervisor, to the Authority of his said intention in the prescribed form (See Appendix A1 or A2)... 2.2.3 Ownership title and area: Latest 7/12 extracts or property register card of a date not earlier than six months prior to the date of submission... Original measurement plan / city survey sheet... 2.2.8 Building plans for Special Buildings: clear motorable access way around the building of minimum 6.0 m. width... Table No.2-B Colouring Notations...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
              <span class="kicker">REG. 2.2.8 // SPECIAL BUILDINGS THRESHOLD</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Fire &amp; Life Safety Mandate</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                Any building &ge; 15m height, or assembly/mercantile/educational buildings &ge; 500 sq.m require: 6.0m clear peripheral motorable fire path, fire lifts with 8-passenger capacity, refuge areas, fire control room, and mandatory CFO Provisional NOC before CC.
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
              <span class="kicker" style="color:var(--amber);">REG. 2.2.11 // STATUTORY CLEARANCES</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">External NOC Checklist</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                AAI (Civil Aviation height NOC), Railway authority (for plots within 30m of railway boundary), Defence establishment NOC, MPCB consent to establish, Forest department, Heritage committee, and Irrigation Dept (Blue/Red flood line demarcations).
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_010 // DRAWING SPECIFICATION &amp; COLORING STANDARDS</span>
              <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">TABLE 2-A &amp; TABLE 2-B SPECIFICATION</span>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1.3fr; gap:16px;">
              <div>
                <span class="kicker-muted">TABLE 2-A // DRAWING SHEET SIZES</span>
                <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px; margin-top:6px;">
                  <thead>
                    <tr style="background:var(--ink); color:var(--paper-raised);">
                      <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Designation</th>
                      <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Trimmed Size (mm)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>A0</strong></td><td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">841 &times; 1189</td></tr>
                    <tr style="background:var(--paper);"><td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>A1</strong></td><td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">594 &times; 841</td></tr>
                    <tr><td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>A2</strong></td><td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">420 &times; 594</td></tr>
                    <tr style="background:var(--paper);"><td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>A3</strong></td><td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">297 &times; 420</td></tr>
                    <tr><td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>A4</strong></td><td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">210 &times; 297</td></tr>
                  </tbody>
                </table>
              </div>
              <div>
                <span class="kicker-muted">TABLE 2-B // STATUTORY COLOR NOTATIONS</span>
                <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px; margin-top:6px;">
                  <thead>
                    <tr style="background:var(--ink); color:var(--paper-raised);">
                      <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Feature</th>
                      <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">White Plan Notation</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr><td style="padding:6px 8px; border:1px solid var(--line-strong);">Plot Boundary Lines</td><td style="padding:6px 8px; border:1px solid var(--line-strong);">Thick Black Line</td></tr>
                    <tr style="background:var(--paper);"><td style="padding:6px 8px; border:1px solid var(--line-strong);">Existing Street / Access</td><td style="padding:6px 8px; border:1px solid var(--line-strong); color:green; font-weight:700;">Green Solid Line</td></tr>
                    <tr><td style="padding:6px 8px; border:1px solid var(--line-strong);">Future Street / DP Road</td><td style="padding:6px 8px; border:1px solid var(--line-strong); color:green; font-weight:700;">Green Dotted Line</td></tr>
                    <tr style="background:var(--paper);"><td style="padding:6px 8px; border:1px solid var(--line-strong);">Proposed Construction</td><td style="padding:6px 8px; border:1px solid var(--line-strong); color:red; font-weight:700;">Red Filled-in</td></tr>
                    <tr><td style="padding:6px 8px; border:1px solid var(--line-strong);">Work to be Demolished</td><td style="padding:6px 8px; border:1px solid var(--line-strong); color:#b8860b; font-weight:700;">Yellow Hatched</td></tr>
                    <tr style="background:var(--paper);"><td style="padding:6px 8px; border:1px solid var(--line-strong);">Drainage &amp; Sewer Lines</td><td style="padding:6px 8px; border:1px solid var(--line-strong); color:red; font-weight:700;">Red Dotted Line</td></tr>
                    <tr><td style="padding:6px 8px; border:1px solid var(--line-strong);">Water Supply Pipelines</td><td style="padding:6px 8px; border:1px solid var(--line-strong);">Black Dotted Thin</td></tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="margin-bottom:12px;">
            <strong>Architectural Submission Case Study:</strong> An architect prepares drawings for a G+6 storey commercial building (Height: 22.5 m, Plot: 1,800 sq.m) in Nashik.
          </p>
          <div class="worked-step">
            <span class="step-badge">CLASSIFICATION</span>
            <div>
              Since the height is <strong>22.5 m (&ge; 15.0 m)</strong> and commercial use, the project qualifies as a <strong>Special Building</strong> under Regulation 2.2.8.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">MANDATORY DRAWINGS</span>
            <div>
              1. <strong>Key Plan:</strong> Scale 1:4000 showing 200 m radius features.
              <br>2. <strong>Site Plan:</strong> Scale 1:500 showing all buildings within 12.0 m, existing 18m road, and authenticated TILR Mojni sheet boundaries.
              <br>3. <strong>Building Plans:</strong> Scale 1:100 floor plans with P-line, RERA carpet area schedule, and 2 sections (1 cut through staircase and lift core).
              <br>4. <strong>Service Plans:</strong> Scale 1:100 showing underground static water tank, fire pump room, and STP.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">CLEARANCES CHECK</span>
            <div>
              - Minimum <strong>6.0 m clear motorable driveway</strong> around the building structure.
              <br>- Provisional Fire NOC from Chief Fire Officer (CFO).
              <br>- Structural Stability Certificate from Licensed Structural Engineer per Reg. 2.2.15.
              <br>- All plans signed by Owner and COA-registered Architect with registration number.
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ SCRUTINY CHECK: All drawings must strictly conform to Table 2-B color notations and Table 2-A metric sheet sizes.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: 7/12 Extract or PR Card Older than 6 Months</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 2.2.3(i), the 7/12 extract or Property Register Card must be dated <strong>not earlier than six months</strong> prior to the date of submission. Online portals automatically reject applications with expired revenue extracts.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Omitting the Staircase Section in Building Plans</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Regulation 2.2.7(v) strictly mandates: <em>"At least one section should be taken through the staircase."</em> Submitting cross-sections only through habitable rooms without detailing the staircase risers, treads, landings, headroom, and handrail heights causes scrutiny objection.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Failing to Show Adjacent Features within 12.0 m on the Site Plan</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Regulation 2.2.6(vii) requires the site plan to depict all adjacent streets, buildings (with number of storeys and height), and premises within a distance of <strong>12.0 m</strong> of the plot boundary. Ignoring neighboring structures prevents municipal officers from evaluating fire access and light/ventilation buffers.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">Letter CR.42/21 (14 June 2021)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Departmental Clearances &amp; Title Clarification</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Clarified documentation requirements under Reg. 2.2.3 and departmental NOC pathways under Reg. 2.2.11 for civil aviation, railways, and industrial pollution.
          </p>
          <div style="display:flex; align-items:center; gap:10px; margin-top:14px; margin-bottom:10px;">
            <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Gaothan Measurement Sheets &amp; Layout Submissions</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Permitted architect-authenticated measurement sheets with adjacent landowner signatures where city surveys have not been completed by the Land Records Department in Gaothan areas.
          </p>
        """,
        'quiz': [
            {
                'question': 'What is the maximum permissible age of a 7/12 extract or Property Register Card at the time of submitting a development application under Reg. 2.2.3(i)?',
                'options': [
                    'Not earlier than 1 month prior to submission',
                    'Not earlier than 3 months prior to submission',
                    'Not earlier than 6 months prior to submission',
                    'Not earlier than 1 year prior to submission'
                ],
                'correctAnswer': 2,
                'explanation': "Regulation 2.2.3(i) explicitly mandates that the 7/12 extracts or property register card must be 'of a date not earlier than six months prior to the date of submission of development proposal'."
            },
            {
                'question': 'What is the minimum statutory width of the clear motorable access driveway around a Special Building for fire appliances under Reg. 2.2.8(a)?',
                'options': [
                    '3.0 metres',
                    '4.5 metres',
                    '6.0 metres',
                    '9.0 metres'
                ],
                'correctAnswer': 2,
                'explanation': "Under Regulation 2.2.8(a), Special Buildings must provide 'clear motorable access way around the building of minimum 6.0 m. width' for fire fighting vehicles."
            },
            {
                'question': 'According to Table No. 2-B (Colouring Notations for Plans), how must proposed new construction work be colored on a white plan?',
                'options': [
                    'Thick Black Line',
                    'Red filled-in',
                    'Yellow Hatched',
                    'Green Dotted'
                ],
                'correctAnswer': 1,
                'explanation': "Table 2-B specifies that 'Proposed work' must be shown as 'Red filled in' on white plans (and Red on blueprints/ammonia prints)."
            },
            {
                'question': 'Under Regulation 2.2.19 and Appendix C, does an Architect registered with the Council of Architecture (COA) need a separate license from the local Planning Authority to practice?',
                'options': [
                    'Yes, they must pass a municipal licensing exam every 3 years',
                    'No, an Architect registered with the Council of Architecture shall not be required to register with the Authority',
                    'Yes, but only in Municipal Corporation areas',
                    'Only if the building exceeds 15 metres in height'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.2.19 explicitly confirms: 'An Architect registered with the Council of Architecture shall not be required to register with the Authority.' Their national COA registration grants statutory competence."
            }
        ],
        'prev_url': '/lessons/reg-2-1-development-permission.html',
        'prev_title': 'Reg. 2.1 Development Permission',
        'next_url': '/lessons/reg-2-2-fees-and-charges.html',
        'next_title': 'Reg. 2.2.12-2.2.14 Fees & Charges'
    },

    # -------------------------------------------------------------------------
    # LESSON 2.3: REG. 2.2.12 to 2.2.14
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-2-2-fees-and-charges.html',
        'lesson_id': 'lesson-reg-2-2-fees',
        'quiz_id': 'quiz-reg-2-2-fees',
        'clause': 'Reg. 2.2.12 – 2.2.14',
        'title': 'Scrutiny Fees, Development Charges & Premium Infrastructure Levies',
        'badge_status': 'Financial Calculations',
        'ch_slug': 'ch02',
        'ch_title': 'Chapter 2: Development Permission',
        'meta_desc': 'Financial statutory levies under UDCPR-2020: Scrutiny fee slab rates, Development Charges under Section 124A-124L MRTP Act, 50:50 Premium FSI sharing, and the 8.5% interest installment payment facility.',
        'lead_summary': 'Comprehensive guide to calculating building scrutiny fees, statutory development charges, premium FSI rates, and fire infrastructure cess under UDCPR-2020. Understand the 10 statutory exemptions for development charges, the 50:50 State-Authority revenue sharing ratio, and the 8.5% reducing balance installment payment options.',
        'amendment_cite': 'CR.121/21, CR.236/18 & CR.94/2024',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            Development in Maharashtra entails three distinct statutory financial obligations: scrutiny fees for administrative processing, development charges for civic impact under the MRTP Act, and premium charges for consuming extra FSI or ancillary area.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Building &amp; Layout Scrutiny Fees (Reg. 2.2.12):</strong>
              <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px; margin-top:8px;">
                <thead>
                  <tr style="background:var(--ink); color:var(--paper-raised);">
                    <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Planning Authority Tier</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Plotted Layout Rate</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Building Construction Rate</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Tier 1:</strong> Pune, PCMC, Nagpur, Nashik, MMR Municipal Corps &amp; Metropolitan Authorities</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">₹ 2,000 / 0.4 Ha</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">₹ 5.00 / sq.m BUA</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Tier 2:</strong> Other Municipal Corporations, A-Class Councils &amp; MMR Regional Plan</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">₹ 1,500 / 0.4 Ha</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">₹ 4.00 / sq.m BUA</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Tier 3:</strong> B &amp; C Class Councils, Nagar Panchayats, Non-Municipal DP &amp; RP areas</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">₹ 500 / 0.4 Ha</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">₹ 2.00 / sq.m BUA</td>
                  </tr>
                </tbody>
              </table>
              <span style="font-size:0.84rem; color:var(--ink-soft); display:block; margin-top:6px;">
                <em>Provisos:</em> No fee on compliance resubmission. In revised plans, fee applies only to additional proposed BUA. Government projects are 100% exempt.
              </span>
            </li>
            <li><strong>Development Charges (Reg. 2.2.13):</strong> Levied under Sections 124A through 124L of the MRTP Act, 1966. Charged as a statutory percentage of the Annual Statement of Rates (ASR / Ready Reckoner) for land development and building construction.
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><em>Lapsed Permission Credit:</em> Fees already paid on lapsed permissions are fully adjusted against future permissions on the site.</li>
                <li><em>Zero Charge for Renewals:</em> No development charge can be levied for renewal of valid permissions.</li>
                <li><em>Compound Walls:</em> Completely exempt from development charges.</li>
                <li><em>Repairs / Maintenance:</em> Internal repairs and strengthening without extra FSI incur no development charges.</li>
                <li><em>Demolition &amp; Reconstruction:</em> Reconstruction after complete demolition attracts 100% full development charges.</li>
                <li><em>MHADA Society Exemption:</em> Authorized tenant societies reconstructing dilapidated buildings without consuming extra FSI pay zero development charges.</li>
              </ul>
            </li>
            <li><strong>Premium FSI &amp; Sharing Ratio (Reg. 2.2.14):</strong> Premium collected is split <strong>50% to the State Government</strong> and <strong>50% to the Planning Authority</strong> (in Regional Plan areas, 100% goes to the State). Funds must be kept in a separate dedicated account exclusively for civic amenities and infrastructure.</li>
            <li><strong>Installment Payment Facility (Reg. 2.2.14):</strong> Premium can be paid in installments with <strong>8.5% per annum interest</strong> on reducing balance:
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><strong>Option 1 (Height &lt; 70 m):</strong> 10% Initial + 4 annual installments of 22.5% each (end of 12th, 24th, 36th, 48th month).</li>
                <li><strong>Option 1 (Height &ge; 70 m):</strong> 10% Initial + 5 annual installments of 18.0% each (end of 12th, 24th, 36th, 48th, 60th month).</li>
                <li><strong>Option 2:</strong> 20% Initial at Commencement Certificate + 80% balance at Occupancy Certificate with 8.5% interest.</li>
                <li><em>Conditions:</em> Post-dated cheques mandatory; Occupancy Certificate is released strictly in proportion to payments cleared. Minimum 1st installment threshold of ₹50 Lakhs (A/B/C Corps) or ₹25 Lakhs (others) may be reduced by local Authority policy (CR.94/2024).</li>
              </ul>
            </li>
            <li><strong>Fire Infrastructure Charges:</strong> Special infrastructure cess recovered as notified by the Government.</li>
          </ul>
        """,
        'statutory_extract': "2.2.12 Building / Layout Permission Scrutiny Fee: The notice shall be accompanied by a self-attested copy of receipt of payment of building / layout permission Scrutiny Fee... 2.2.13 Development Charges: Development charges as required under Section 124 A to 124 L of the Maharashtra Regional and Town Planning Act, 1966 shall be deposited with the Authority before issue of development permission / commencement certificate... 2.2.14 Premium Charges and Fire Infrastructure Charges: The 50% Premium share of the Government shall be deposited by the Authority in a specified head of account of the Government... allowed to be paid in instalments with interest @ 8.5% per annum...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
              <span class="kicker">REG. 2.2.14 // 50:50 REVENUE SPLIT</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Premium FSI Sharing</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                50% is credited to the State Government Consolidated Fund and 50% retained by the Municipal Corporation / Authority in an escrow infrastructure fund. In Regional Plan areas, 100% goes to the State.
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
              <span class="kicker" style="color:var(--amber);">REG. 2.2.14 // INSTALLMENT FACILITY</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">8.5% Reducing Balance Interest</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                Developers can defer 90% of premium across 4 to 5 years (or defer 80% to Occupancy under Option 2) against post-dated cheques, paying 8.5% p.a. interest. Occupancy is released strictly pro-rata.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_011 // PREMIUM INSTALLMENT PAYMENT SCHEDULE</span>
              <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 2.2.14 SPECIFICATION</span>
            </div>
            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px;">
                <thead>
                  <tr style="background:var(--ink); color:var(--paper-raised);">
                    <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Building Height Category</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Initial at CC</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">End of 12M</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">End of 24M</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">End of 36M</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">End of 48M</th>
                    <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">End of 60M</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Below 70.0 m Height</strong></td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700; color:var(--blueprint);">10%</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">22.5% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">22.5% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">22.5% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">22.5% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); color:var(--ink-soft);">&mdash;</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>70.0 m &amp; Above (High-Rise)</strong></td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700; color:var(--blueprint);">10%</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">18.0% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">18.0% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">18.0% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">18.0% + Int</td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">18.0% + Int</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Option 2 (Any Height)</strong></td>
                    <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700; color:var(--amber);">20%</td>
                    <td colspan="5" style="padding:6px 8px; text-align:center; border:1px solid var(--line-strong); color:var(--amber);">
                      Remaining 80% payable at time of Occupancy Certificate with interest @ 8.5% p.a.
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="margin-bottom:12px;">
            <strong>Real-World Financial Computation:</strong> A commercial building in Pune Municipal Corporation has a proposed Built-Up Area of <strong>4,000 sq.m</strong> (Height: 32 m &lt; 70 m). The project purchases 1,000 sq.m of Premium FSI at a total calculated premium of <strong>₹ 1,00,00,000 (₹ 1.00 Crore)</strong>.
          </p>
          <div class="worked-step">
            <span class="step-badge">SCRUTINY FEE</span>
            <div>
              PMC is Tier 1 (&sect; 2.2.12): Rate = <strong>₹ 5.00 / sq.m</strong>
              <br><span style="font-family:var(--mono);">Scrutiny Fee = 4,000 sq.m &times; ₹ 5 = <strong>₹ 20,000</strong></span> (non-refundable).
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">PREMIUM OPTION 1</span>
            <div>
              Total Premium = <strong>₹ 1,00,00,000</strong>. Opts for Option 1 (&lt; 70 m):
              <br>1. <strong>Initial Payment (at CC):</strong> 10% = <strong>₹ 10,00,000</strong>.
              <br>2. <strong>Balance to be deferred:</strong> ₹ 90,00,000 split across 4 installments of 22.5% = ₹ 22,50,000 each.
              <br>3. <strong>Installment 1 (Month 12):</strong> ₹ 22,50,000 + 8.5% interest on ₹ 90 Lakhs (₹ 7,65,000) = <strong>₹ 30,15,000</strong>.
              <br>4. <strong>Installment 2 (Month 24):</strong> ₹ 22,50,000 + 8.5% interest on ₹ 67.5 Lakhs (₹ 5,73,750) = <strong>₹ 28,23,750</strong>.
              <br>5. <strong>Installment 3 (Month 36):</strong> ₹ 22,50,000 + 8.5% interest on ₹ 45.0 Lakhs (₹ 3,82,500) = <strong>₹ 26,32,500</strong>.
              <br>6. <strong>Installment 4 (Month 48):</strong> ₹ 22,50,000 + 8.5% interest on ₹ 22.5 Lakhs (₹ 1,91,250) = <strong>₹ 24,41,250</strong>.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">REVENUE ALLOCATION</span>
            <div>
              50% (₹ 50,00,000) is remitted to Maharashtra State Government Account; 50% (₹ 50,00,000) is retained in Pune Municipal Corporation's Infrastructure Fund.
            </div>
          </div>
          <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
            ✓ STATUTORY RULE: Pro-rata Occupancy Certificate cannot exceed 10% of total building area until Installment 1 clears.
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Expecting Full Occupancy Certificate While Premium Installments are Pending</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 2.2.14 Note (iii): <em>"Occupation Certificate shall be granted in proportion to the payments made."</em> If only the initial 10% and first installment (total 32.5%) have been paid, the Authority will legally refuse a full Occupancy Certificate. Full OC requires either 100% clearance or early prepayment.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Demanding Cash Refunds for Development Charges on Lapsed Permissions</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 2.2.13 proviso (ix), if no work is carried out and permission lapses or is cancelled, the development charges paid <strong>are adjusted in future permissions</strong>, but are never refunded in cash. Developers must track credit receipts across corporate restructuring.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Levying Scrutiny Fees on Objection Compliance Resubmissions</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Regulation 2.2.12 Note (i) explicitly prohibits scrutiny fee levies: <em>"No scrutiny fee shall be levied if the proposal is received after compliance of the objections raised by the authority."</em> Officers cannot charge duplicate scrutiny fees during regular compliance iterations.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">Directives CR.94/2024 (11 Oct 2024)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Relaxation of First Installment Minimum Threshold</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Authorized Planning Authorities to relax or reduce the statutory first installment limits (₹ 50 Lakhs for A/B/C Corps and ₹ 25 Lakhs for others) as a policy measure considering local market conditions, apportioning the remainder across subsequent installments.
          </p>
          <div style="display:flex; align-items:center; gap:10px; margin-top:14px; margin-bottom:10px;">
            <span class="badge badge-amended">Notification CR.236/18 (Part 6) (12 Oct 2022)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Special Planning Authorities in Tier 1</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Explicitly included Special Planning Authorities (SPAs), NTDAs, and Area Development Authorities (ADAs) within Tier 1 scrutiny fee schedules.
          </p>
        """,
        'quiz': [
            {
                'question': 'What is the statutory scrutiny fee rate for building construction in Pune, Pimpri-Chinchwad, Nagpur, and MMR Municipal Corporations under Reg. 2.2.12?',
                'options': [
                    '₹ 2.00 per sq.m of built-up area',
                    '₹ 4.00 per sq.m of built-up area',
                    '₹ 5.00 per sq.m of built-up area',
                    '₹ 10.00 per sq.m of built-up area'
                ],
                'correctAnswer': 2,
                'explanation': "Table under Regulation 2.2.12 mandates a scrutiny fee of 'Rs. 5/- Per Sq.m. of built-up area' for Pune, PCMC, Nagpur, Nashik, MMR Municipal Corporations, and Metropolitan Authorities."
            },
            {
                'question': 'How are Premium FSI charges shared between the State Government and the local Planning Authority under Regulation 2.2.14(i)?',
                'options': [
                    '100% to the Planning Authority',
                    '50% to State Government and 50% to Planning Authority',
                    '70% to State Government and 30% to Planning Authority',
                    '25% to State Government and 75% to Planning Authority'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.2.14(i) states: 'The 50% Premium share of the Government shall be deposited by the Authority in a specified head of account of the Government. The amount of premium collected by the Authority shall be kept in a separate account and it shall be utilized for development of civic amenities and infrastructure.'"
            },
            {
                'question': 'What is the statutory interest rate charged on deferred reducing balance premium installments under Reg. 2.2.14?',
                'options': [
                    '6.0% per annum',
                    '8.5% per annum',
                    '12.0% per annum',
                    '18.0% per annum compound interest'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.2.14 explicitly mandates that premium charges allowed to be paid in installments carry interest '@ 8.5% per annum' on the reducing outstanding balance."
            },
            {
                'question': 'Under Regulation 2.2.13 proviso (v), which of the following works is completely EXEMPT from development charges?',
                'options': [
                    'Commercial shopping mall development',
                    'Construction or repairs of a compound wall meant for property protection',
                    'Reconstructing a collapsed cinema hall',
                    'Residential group housing project'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.2.13 proviso (v) provides: 'construction of compound wall is meant for protection of property and as such no development charge shall be levied for construction of compound wall or for repairs of compound wall.'"
            }
        ],
        'prev_url': '/lessons/reg-2-2-application-procedure.html',
        'prev_title': 'Reg. 2.2 Application Procedure',
        'next_url': '/lessons/reg-2-3-discretionary-powers-and-relaxations.html',
        'next_title': 'Reg. 2.3-2.5 Discretionary Powers'
    },

    # -------------------------------------------------------------------------
    # LESSON 2.4: REG. 2.3 to 2.5
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-2-3-discretionary-powers-and-relaxations.html',
        'lesson_id': 'lesson-reg-2-3',
        'quiz_id': 'quiz-reg-2-3',
        'clause': 'Reg. 2.3, 2.4 & 2.5',
        'title': 'Discretionary Powers, Hardship Relaxations & Drafting Errors',
        'badge_status': 'Legal Hierarchy',
        'ch_slug': 'ch02',
        'ch_title': 'Chapter 2: Development Permission',
        'meta_desc': 'Discretionary powers under UDCPR-2020: Interpretation authority under Reg 2.3, the 50% split-zone rule, hardship relaxations under Reg 2.4, the strictly non-relaxable core (Setbacks, FSI, Parking), and drafting error corrections.',
        'lead_summary': 'Learn the exact legal scope of discretionary powers vested in Planning Authorities under UDCPR-2020: resolving Development Plan road and zone boundary discrepancies, the statutory 50% dominant zone rule, demonstrable hardship relaxations under Reg 2.4, the absolute non-relaxability of Road Setbacks, FSI, and Parking, and drafting error rectifications under Reg 2.5.',
        'amendment_cite': 'CR.236/18 & CR.128/22',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            Regulations 2.3, 2.4, and 2.5 govern administrative discretion, statutory interpretation, and hardship relaxations in Maharashtra. They establish clear legal guardrails preventing arbitrary municipal concessions while resolving genuine on-ground planning anomalies.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Discretionary Interpretation Powers (Reg. 2.3):</strong> In conformity with the intent and spirit of UDCPR, the Authority may issue written orders to:
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li>Correct administrative, clerical, or grammatical errors in past orders.</li>
                <li>Decide the boundary of a DP / RP proposal where revenue records, measurement sheets, or City Survey lines conflict with the DP map.</li>
                <li>Determine and establish zonal boundaries in cases of ambiguity or dispute.</li>
                <li>Adjust DP / RP road alignments where the actual street layout on ground differs from the sanctioned plan.</li>
                <li>Correct Blue and Red flood lines based on latest determinations by the Irrigation Department.</li>
                <li><em>The 50% Split Zone Rule (Reg. 2.3(vi)):</em> Where a zonal boundary line divides a single plot, <strong>the zone covering more than 50% of the area shall be considered for the entire plot</strong>!</li>
                <li>Authorize public utility premises or buildings in any land use classification for public convenience and welfare.</li>
              </ul>
            </li>
            <li><strong>Hardship Relaxations (Reg. 2.4):</strong> In specific cases of <strong>clearly demonstrable hardship</strong>, the Authority may relax dimensions or technical requirements, provided:
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li>The relaxation does <strong>NOT</strong> violate health safety, fire safety, structural safety, or public safety.</li>
                <li>In Municipal Councils and Regional Plan areas, relaxation can only be granted in consultation with the <strong>Divisional Joint Director of Town Planning (JDTP)</strong>.</li>
                <li>Conditions, limitations, forfeiture of security deposits, and premium charges may be imposed.</li>
              </ul>
            </li>
            <li><strong>THE ABSOLUTE NON-RELAXABLE CORE (Reg. 2.4):</strong> The regulation establishes an unconditional statutory prohibition:
              <div style="background:var(--paper); border:1px solid var(--brick); border-left:4px solid var(--brick); padding:10px 14px; margin:6px 0; font-family:var(--mono); font-size:0.85rem; color:var(--brick);">
                "No relaxation in the setback required from the road boundary or FSI or parking requirements shall be granted under any circumstances, unless otherwise specified in these Regulations."
              </div>
            </li>
            <li><strong>Overriding Legal Effect (Reg. 2.4):</strong> This provision explicitly supersedes and prevails over all past Government Orders, Resolutions, or Notifications regarding relaxation powers.</li>
            <li><strong>Drafting Errors (Reg. 2.5):</strong> Drafting errors in DP/RP can be corrected by the Authority after site verification and City Survey record checks (with JDTP consultation for Municipal Councils and Regional Plans).</li>
          </ul>
        """,
        'statutory_extract': "2.3 Discretionary Powers - Interpretation: In conformity with the intent and spirit of these Regulations, the Authority may by order in writing... vi) Modify the limit of a zone where the boundary line of the zone divides a plot. In such cases, the zone covering area more than 50% shall be considered... 2.4 Discretionary Powers - Relaxations in Specific Cases: In specific cases where clearly demonstrable hardship is caused, the Authority may permit any of the dimensions / provisions prescribed by these regulations to be modified... No relaxation in the setback required from the road boundary or FSI or parking requirements shall be granted under any circumstances...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
              <span class="kicker">REG. 2.3(vi) // THE 50% SPLIT-ZONE RULE</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Dominant Zone Governs</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                When a Development Plan zone boundary cuts across an individual holding, the applicant is spared split zoning. If 51% of the plot lies in Residential Zone and 49% in Agricultural/Green Zone, the entire holding can be developed as Residential Zone.
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--brick); padding:16px;">
              <span class="kicker" style="color:var(--brick);">REG. 2.4 // THE STRICT PROHIBITION</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Zero Discretion on 3 Items</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                Municipal Commissioners and Planning Authorities possess <strong>ZERO legal power</strong> to relax: (1) Road Setback / Building Line, (2) Floor Space Index (FSI), and (3) Mandatory Parking numbers. Any order attempting to do so is ultra vires and void.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_012 // ADMINISTRATIVE DISCRETION &amp; RELAXATION MATRIX</span>
              <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 2.3 &amp; 2.4 SPECIFICATION</span>
            </div>
            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px;">
                <thead>
                  <tr style="background:var(--ink); color:var(--paper-raised);">
                    <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Regulatory Element</th>
                    <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Governing Clause</th>
                    <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Discretionary Authority</th>
                    <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Legal Scope &amp; Constraints</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Road Setback / Building Line</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 2.4</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--brick); font-weight:700;">PROHIBITED</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--brick);">Cannot be relaxed under any circumstances</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Floor Space Index (FSI)</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 2.4</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--brick); font-weight:700;">PROHIBITED</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--brick);">No commissioner can grant extra FSI via hardship</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Parking Space Requirements</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 2.4</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--brick); font-weight:700;">PROHIBITED</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--brick);">Mandatory parking counts cannot be reduced</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Side &amp; Rear Marginal Spaces</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 2.4</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Permissible (Hardship)</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Can be modified for odd/narrow plots without fire risk</td>
                  </tr>
                  <tr>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Plot Split by Zone Boundary</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 2.3(vi)</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Permissible (Statutory)</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Zone covering &gt; 50% area applies to entire plot</td>
                  </tr>
                  <tr style="background:var(--paper);">
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Blue / Red Flood Lines</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 2.3(v)</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Correction Permissible</td>
                    <td style="padding:6px 8px; border:1px solid var(--line-strong);">Aligned strictly with Irrigation Department data</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="margin-bottom:12px;">
            <strong>Demonstrable Hardship &amp; Zoning Case Study:</strong> An owner holds a registered plot of <strong>1,200 sq.m</strong> in an urban area.
          </p>
          <div class="worked-step">
            <span class="step-badge">SCENARIO A: SPLIT ZONE</span>
            <div>
              On the Development Plan, the zonal boundary cuts through the plot: <strong>700 sq.m (58.33%)</strong> falls within the Residential Zone (R-Zone), while <strong>500 sq.m (41.67%)</strong> falls in the No Development / Agricultural Zone.
              <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; STATUTORY RESOLUTION (Reg. 2.3(vi)):</span> Since the Residential Zone covers more than 50% (58.33%), the <strong>entire 1,200 sq.m plot is legally considered as Residential Zone</strong>.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">SCENARIO B: MARGIN HARDSHIP</span>
            <div>
              The plot is an irregular trapezoid with a narrow 10m rear width. To construct a residential building, the required rear margin is 3.0 m, which leaves an unbuildable sliver of 2.2 m width.
              <br><span style="font-family:var(--mono); color:var(--amber);">&#9888; LAWFUL RELAXATION (Reg. 2.4):</span> The Municipal Commissioner grants a marginal space relaxation reducing the rear margin to 2.25 m against payment of hardship premium, having verified that fire vehicle movement (6.0m on front) and neighbor ventilation are unaffected.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">SCENARIO C: ILLEGAL FSI REQUEST</span>
            <div>
              The owner requests the Commissioner to grant 15% extra FSI without paying premium or purchasing TDR, citing severe economic hardship.
              <br><span style="font-family:var(--mono); color:var(--brick);">&#10007; ULTRA VIRES REJECTION (Reg. 2.4):</span> <em>"No relaxation in... FSI... shall be granted under any circumstances."</em> The Commissioner has zero legal authority to relax FSI. Any such order is void ab initio.
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Applying for Relaxation in Municipal Councils without JDTP Consultation</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 2.4: <em>"In areas of Municipal Councils and Regional plan, such relaxation shall be granted in consultation with concerned Divisional Joint Director of Town Planning."</em> A Chief Officer of a Municipal Council who issues a relaxation order unilaterally without written concurrence from the JDTP acts unlawfully.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Confusing Discretionary DP Realignment with De-reservation</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Regulation 2.3(iv) allows the Authority to decide DP road alignment where actual ground street layout varies from the DP. This power cannot be used to delete a DP road, shift it outside the applicant's plot to a neighbor's plot, or eliminate a public reservation. Modifications of substantial nature require formal Section 37 MRTP Act procedures.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Claiming 50% Rule for Plots Artificially Amalgamated</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              The 50% rule under Regulation 2.3(vi) applies to an authentic, single holding divided by a zone boundary. Artificially purchasing or amalgamating an adjacent agricultural land parcel with a residential plot after the DP sanction date to claim the 50% rule will be rejected as an unlawful evasion of zoning control.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">Directives CR.236/18 (Part 2) (26 Sept 2022)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Section 154 Directives on Hardship Relaxations</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            State Government issued comprehensive directions under Section 154 of the MRTP Act clarifying the strict limits of relaxation under Regulation 2.4 and mandating uniform documentation across all Planning Authorities.
          </p>
          <div style="display:flex; align-items:center; gap:10px; margin-top:14px; margin-bottom:10px;">
            <span class="badge badge-amended">Clarification Order CR.128/22 (26 Sept 2022)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Drafting Errors &amp; Road Re-alignments</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Standardized the procedure for correcting DP road alignments and revenue survey boundary mismatches under Regulation 2.3 and 2.5.
          </p>
        """,
        'quiz': [
            {
                'question': 'When a Development Plan zone boundary line divides a single plot of land, how is the applicable zone decided under Regulation 2.3(vi)?',
                'options': [
                    'The entire plot is automatically deemed Agricultural Zone',
                    'The zone covering area more than 50% shall be considered for the entire plot',
                    'The plot must be split and divided with a 3m compound wall',
                    'The owner must pay a de-zoning premium to the Collector'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.3(vi) explicitly provides: 'Modify the limit of a zone where the boundary line of the zone divides a plot. In such cases, the zone covering area more than 50% shall be considered.'"
            },
            {
                'question': 'Which three development parameters can NEVER be relaxed by the Planning Authority under any circumstances under Regulation 2.4?',
                'options': [
                    'Marginal open space, plinth height, and compound wall height',
                    'Road Setback, FSI, and Parking requirements',
                    'Staircase width, lift machine room height, and water tank size',
                    'Basement ramp slope, parapet height, and meter room location'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.4 strictly stipulates: 'No relaxation in the setback required from the road boundary or FSI or parking requirements shall be granted under any circumstances, unless otherwise specified in these Regulations.'"
            },
            {
                'question': 'In Municipal Councils and Regional Plan areas, with whom must the Planning Authority consult before granting any hardship relaxation under Reg. 2.4?',
                'options': [
                    'The District Collector',
                    'The Divisional Joint Director of Town Planning (JDTP)',
                    'The local Police Commissioner',
                    'The Member of Legislative Assembly (MLA)'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.4 explicitly mandates: 'In areas of Municipal Councils and Regional plan, such relaxation shall be granted in consultation with concerned Divisional Joint Director of Town Planning.'"
            },
            {
                'question': 'Under Regulation 2.3(v), based on whose determinations can the Planning Authority correct the alignment of Blue and Red flood lines on the Development Plan?',
                'options': [
                    'Private environmental consultants',
                    'The Irrigation Department or other Government institutions dealing with the subject',
                    'The local builders association',
                    'The Fire Brigade department'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.3(v) authorizes the Authority to correct Blue and Red flood lines where they vary with lines given by the 'Irrigation Department or any other Govt. institutions dealing with the subject, from time to time'."
            }
        ],
        'prev_url': '/lessons/reg-2-2-fees-and-charges.html',
        'prev_title': 'Reg. 2.2.12-2.2.14 Fees & Charges',
        'next_url': '/lessons/reg-2-6-commencement-and-occupancy.html',
        'next_title': 'Reg. 2.6-2.15 Commencement & Occupancy'
    },

    # -------------------------------------------------------------------------
    # LESSON 2.5: REG. 2.6 to 2.15
    # -------------------------------------------------------------------------
    {
        'filename': 'reg-2-6-commencement-and-occupancy.html',
        'lesson_id': 'lesson-reg-2-6',
        'quiz_id': 'quiz-reg-2-6',
        'clause': 'Reg. 2.6 – 2.15',
        'title': 'Sanction Timelines, Deemed Permission, Plinth Checking & Occupancy',
        'badge_status': 'Site Lifecycle',
        'ch_slug': 'ch02',
        'ch_title': 'Chapter 2: Development Permission',
        'meta_desc': 'The statutory execution roadmap under UDCPR-2020: 60-day sanction timeline, Deemed Permission mechanics under Reg 2.6.2, CC validity and 4-year limit under Reg 2.7, site display boards, plinth checking (Appendix F), Completion (Appendix G), Occupancy Certificate (Appendix H), and penalties for offences.',
        'lead_summary': 'Master the entire operational lifecycle of a building project under UDCPR-2020: the 60-day statutory sanction window, the deemed permission procedure under Section 45 MRTP Act, validity and renewal of Commencement Certificates, mandatory plinth level intimation, substantial deviations during construction, final Completion Certificates, full and part Occupancy Certificates, and statutory penalties under Sections 52-54.',
        'amendment_cite': 'CR.121/21 & CR.18/21',
        'plain_summary_html': """
          <p style="margin-bottom:14px;">
            From the moment a development notice is logged to the final issuance of an Occupancy Certificate, UDCPR-2020 enforces rigorous operational timelines, mandatory inspection milestones, and severe penalties for non-compliance.
          </p>
          <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
            <li><strong>Sanction Timelines (Reg. 2.6.1):</strong> The Authority must grant or refuse permission within <strong>60 days</strong> of receipt of a complete notice or resubmission after compliance. Two-stage approval applies to layouts: tentative demarcation first, followed by final approval upon Land Records measurement. All sanctions must be displayed on the Authority's official website until 1 month after the final Occupancy Certificate.</li>
            <li><strong>Deemed Permission (Reg. 2.6.2):</strong>
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li>If the Authority fails to communicate approval or refusal within <strong>60 days</strong>, the applicant sends written intimation claiming deemed permission.</li>
                <li>The Authority must respond within <strong>15 days</strong>. If it fails, the Commencement Certificate and approved plans <em>shall be issued within 15 days thereafter</em>.</li>
                <li><em>Crucial Statutory Proviso:</em> Deemed permission is lawful <strong>ONLY if the proposal strictly conforms to UDCPR and DP/RP proposals</strong>! Any construction violating rules under the pretext of deemed approval is treated as unauthorized development under Sections 52 to 57 of the MRTP Act. Defaulter municipal officers face statutory disciplinary action.</li>
              </ul>
            </li>
            <li><strong>Commencement Certificate Validity (Reg. 2.7.1):</strong> Valid for <strong>1 year</strong>, renewable annually up to a maximum aggregate of <strong>4 years</strong>. Delayed renewals attract a penalty fee of <strong>1/3 of the scrutiny fee</strong> per year (CR.121/21).
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><em>Perpetual Validity upon Commencement:</em> If work is commenced within the valid period, <strong>no further renewal is necessary</strong>—the CC remains valid until completion!</li>
                <li><em>Statutory Definition of "Commencement":</em> For buildings, commencement means <strong>construction up to plinth level</strong> (or upper level of lower basement / stilt). For bridges/tanks: foundation up to base floor. For layouts: final demarcation and complete water-bound macadam (WBM) roads.</li>
              </ul>
            </li>
            <li><strong>Layout Infrastructure &amp; Phased Plot Release (Reg. 2.7.2):</strong> Developer must build internal roads, storm drains, water, sewer lines, and develop open spaces. In layouts, plots are released in phases based on completed infrastructure (typically 80% released; 20% mortgaged to Authority or covered by Bank Guarantee until final infrastructure handover).</li>
            <li><strong>Construction Milestones (Reg. 2.8):</strong>
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><em>Site Display Board (Reg. 2.8.3):</em> Conspicuous board stating Owner, Developer, Architect, Struct Eng, Sanction Order No. &amp; Date, Permitted BUA, RERA No., and online software <strong>QR Code</strong> (CR.121/21).</li>
                <li><em>Plinth Checking Notice (Reg. 2.8.4):</em> Owner must submit <strong>Appendix F</strong> intimation upon completing plinth. Authority officers inspect ~10% of cases on a random audit basis. Work can proceed after intimation.</li>
                <li><em>Deviations (Reg. 2.8.5):</em> Substantial deviations require prior revised sanction. Internal unit layout changes that do not violate FSI or regulations are non-unauthorized and regularized at completion.</li>
              </ul>
            </li>
            <li><strong>Completion &amp; Occupancy Certificates (Reg. 2.9, 2.10 &amp; 2.11):</strong>
              <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
                <li><em>Completion Certificate (Reg. 2.9):</em> Submitted by licensed supervisor via <strong>Appendix G</strong> with 3 plan sets, lift inspector NOC, and structural stability certificate (+ Final CFO Fire NOC for Special Buildings).</li>
                <li><em>Occupancy Certificate (Reg. 2.10):</em> Authority inspects and must grant (<strong>Appendix H</strong>) or refuse (<strong>Appendix I</strong>) within <strong>21 days</strong>. If not decided, Deemed Occupancy triggers within 15 days of applicant's notice. Occupation without OC is strictly prohibited.</li>
                <li><em>Part Occupancy Certificate (Reg. 2.11):</em> Permissible for completed portions under <strong>Appendix J</strong> indemnity bond, provided public safety, safe access, and firefighting systems are fully operational.</li>
              </ul>
            </li>
            <li><strong>Offences, Penalties &amp; Revocation (Reg. 2.14 &amp; 2.15):</strong> Punishable under MRTP Act Sec 52 (fines/imprisonment), Sec 53-54 (demolition). Defaulting Engineers/Supervisors are <strong>debarred for the entire district</strong> (CR.121/21); defaulting Architects are referred to COA for license cancellation. Permissions obtained via fraud or misrepresentation may be revoked with zero compensation.</li>
          </ul>
        """,
        'statutory_extract': "2.6.2 Deemed Permission: If within sixty (60) days of receipt of the notice... the Authority fails to intimate in writing to the person... the notice with its plan and statements shall be deemed to have been sanctioned... 2.7.1 Commencement: The commencement certificate / development permission... shall remain valid for 4 years in the aggregate but shall have to be renewed every year... For the purpose of this regulation, 'Commencement' shall mean... Upto plinth level or where there is no plinth upto upper level of lower basement or stilt... 2.8.4 Plinth Checking: The owner shall give intimation in the prescribed form in Appendix - F... 2.10 Occupancy Certificate: issue an occupancy certificate in the form in Appendix - H or refuse... within 21 days from the date of receipt...",
        'clause_cards_html': """
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
              <span class="kicker">REG. 2.7.1 // STATUTORY COMMENCEMENT</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Plinth Reached = CC Perpetual</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                Under UDCPR, reaching plinth level (or top of lower basement/stilt) constitutes statutory "commencement". Once plinth is achieved within the valid 1-year window, annual CC renewal fees are permanently eliminated!
              </p>
            </div>
            <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--brick); padding:16px;">
              <span class="kicker" style="color:var(--brick);">REG. 2.10 // MANDATORY OCCUPANCY</span>
              <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">No Possession Without Appendix H</h4>
              <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
                Handing over possession to buyers or occupying a building before receiving the official Occupancy Certificate (Appendix H) is a criminal offence under Section 52 of MRTP Act. Utility providers are legally barred from granting permanent connections.
              </p>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_013 // PROJECT EXECUTION CHRONOLOGY &amp; STATUTORY MILESTONES</span>
              <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">CHAPTER 2 OPERATIONAL ROADMAP</span>
            </div>
            <div style="padding:10px 0; font-family:var(--mono); font-size:11.5px; line-height:1.9; color:var(--ink);">
              [STAGE 1] APPLICATION NOTICE (Appendix A-1 / A-2) &rarr; Scrutiny fees deposited &rarr; Online portal logging.<br>
              &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr; <em>60 Days Statutory Window (&sect; 2.6.1)</em><br>
              [STAGE 2] COMMENCEMENT CERTIFICATE (Appendix E-1 / E-2) &rarr; Valid for 1 year; max 4 years total.<br>
              &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr; <em>Excavation, Foundations &amp; Casting Plinth</em><br>
              [STAGE 3] PLINTH CHECKING NOTICE (Appendix F per &sect; 2.8.4) &rarr; Reaching plinth secures perpetual CC validity.<br>
              &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr; <em>Superstructure, Brickwork, MEP Services &amp; Fire Installations</em><br>
              [STAGE 4] COMPLETION CERTIFICATE (Appendix G per &sect; 2.9) &rarr; Architect filing + Lift NOC + Final CFO NOC.<br>
              &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr; <em>21 Days Statutory Inspection Window (&sect; 2.10)</em><br>
              [STAGE 5] OCCUPANCY CERTIFICATE (Appendix H) &rarr; Lawful handover, power/water connections, and buyer possession.
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="margin-bottom:12px;">
            <strong>Operational Timeline Case Study:</strong> A developer receives Commencement Certificate for a 15-storey building on <strong>01st February 2024</strong>.
          </p>
          <div class="worked-step">
            <span class="step-badge">MILESTONE 1</span>
            <div>
              <strong>Reaching Plinth (01st October 2024):</strong> Within 8 months, foundation and plinth beams are cast. The architect submits <strong>Appendix F</strong> intimation.
              <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; STATUTORY EFFECT (Reg. 2.7.1):</span> Because plinth was completed within the initial 1-year validity (before 31st January 2025), work has legally "commenced". The developer <strong>never needs to apply for annual CC renewals again</strong>.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">MILESTONE 2</span>
            <div>
              <strong>Internal Wall Alignment Adjustment (March 2025):</strong> While constructing the 5th floor, internal bedroom partition walls are shifted by 400 mm to enlarge wardrobe niches without altering BUA, FSI, or window light.
              <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; COMPLIANCE (Reg. 2.8.5):</span> Internal unit changes not violating FSI or regulations are non-unauthorized and can be reflected directly in completion drawings without stopping work.
            </div>
          </div>
          <div class="worked-step">
            <span class="step-badge">MILESTONE 3</span>
            <div>
              <strong>Completion &amp; Part OC (June 2026):</strong> Wing A (Floors 1-8) is completed with functioning fire systems and independent lift access, while Wing B superstructure continues.
              <br><span style="font-family:var(--mono); color:var(--amber);">&#10003; PART OCCUPANCY (Reg. 2.11):</span> Developer files Appendix G and an indemnity bond in <strong>Appendix J</strong>. The Authority grants Part Occupancy Certificate for Wing A within 21 days, allowing lawful possession of finished units.
            </div>
          </div>
        """,
        'pitfalls_html': """
          <div class="callout callout-amber">
            <strong>Pitfall 1: Assuming Deemed Permission Permits Deviations from UDCPR</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Under Regulation 2.6.2: <em>"any development carried out in pursuance of such deemed permission which is in contravention of the above provisions, shall be deemed to be an unauthorized development for purposes of Section 52 to 57 of the MRTP Act."</em> Deemed permission is not a blank cheque; if the submitted drawing has a 1.8m margin where 3.0m is statutory, the building will be ordered demolished.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 2: Forgetting the Plinth Checking Intimation (Appendix F)</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Regulation 2.8.4 requires formal intimation in Appendix F upon completing plinth. If a developer proceeds directly to cast 1st and 2nd floor slabs without filing Appendix F, the Authority can halt construction, issue stop-work notices, and demand independent foundation re-verification.
            </p>
          </div>
          <div class="callout callout-amber">
            <strong>Pitfall 3: Failing to Display the Mandatory QR Code on the Site Board</strong>
            <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
              Inserted vide Corrigendum CR.121/21 into Regulation 2.8.3(vi): The site display board must mandatorily incorporate the <em>"Software QR Code for the Project generated in online building permission"</em>. Flying inspection squads penalize projects displaying traditional text boards lacking readable online sanction QR codes.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
            <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">CC Renewal Penalty &amp; Professional Debarment</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Instituted a late renewal condonation fee equal to 1/3 of the scrutiny fee under Reg. 2.7.1, mandated online QR codes on display boards under Reg. 2.8.3, and enacted district-wide debarment penalties for defaulting licensed engineers and supervisors under Reg. 2.14.
          </p>
          <div style="display:flex; align-items:center; gap:10px; margin-top:14px; margin-bottom:10px;">
            <span class="badge badge-amended">Clarification Letter CR.18/21 (23 Dec 2021)</span>
            <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Deemed Permission Strict Compliance Safeguards</span>
          </div>
          <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
            Reiterated that deemed permissions under Reg. 2.6.2 cannot validate proposals violating Regional Plans, Development Plans, or core UDCPR safety dimensions.
          </p>
        """,
        'quiz': [
            {
                'question': 'What is the statutory deadline for the Planning Authority to grant or refuse development permission under Regulation 2.6.1(iv)?',
                'options': [
                    'Within 30 days from date of receipt/resubmission',
                    'Within 60 days from date of receipt/resubmission',
                    'Within 90 days from date of receipt/resubmission',
                    'Within 6 months from date of receipt/resubmission'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.6.1(iv) stipulates that 'The authority shall grant or refuse the commencement certificate / building permit within 60 days from the date of resubmission' (or initial submission)."
            },
            {
                'question': 'Under Regulation 2.7.1, what constitutes statutory "Commencement" of work for a building?',
                'options': [
                    'Erecting a tin barricade and temporary site office',
                    'Digging foundation pits with a JCB',
                    'Construction up to plinth level (or upper level of lower basement or stilt)',
                    'Casting the first residential floor slab'
                ],
                'correctAnswer': 2,
                'explanation': "Regulation 2.7.1 defines 'Commencement' for a building work as: 'Upto plinth level or where there is no plinth upto upper level of lower basement or stilt as the case may be.'"
            },
            {
                'question': 'Within how many days must the Authority inspect and grant or refuse an Occupancy Certificate after receiving the completion certificate under Reg. 2.10?',
                'options': [
                    'Within 7 days',
                    'Within 14 days',
                    'Within 21 days',
                    'Within 45 days'
                ],
                'correctAnswer': 2,
                'explanation': "Regulation 2.10 mandates that the Authority shall 'issue an occupancy certificate in the form in Appendix - H or refuse to sanction the occupancy certificate in Appendix - I within 21 days from the date of receipt of the said completion certificate'."
            },
            {
                'question': 'Under Regulation 2.14(i)(c) (as amended by Corrigendum CR.121/21), what disciplinary penalty can be imposed on a Licensed Engineer or Supervisor convicted of contravening UDCPR regulations?',
                'options': [
                    'A warning letter on their website',
                    'Cancellation of license and debarring from practice for the entire respective district',
                    'Only a nominal fine of ₹ 500',
                    'Re-taking their university engineering degree'
                ],
                'correctAnswer': 1,
                'explanation': "Regulation 2.14(i)(c) provides that action may include 'cancellation of license and debarring him from further practice/ business for a period as may be decided by the Authority. Thereupon such Licensed Engineer / Structural Engineer / Town Planner / Supervisor shall be considered debarred for respective district'."
            }
        ],
        'prev_url': '/lessons/reg-2-3-discretionary-powers-and-relaxations.html',
        'prev_title': 'Reg. 2.3-2.5 Discretionary Powers',
        'next_url': '/lessons/reg-3-1-site-clearance-buffers.html',
        'next_title': 'Reg. 3.1 Site Clearance Buffers'
    }
]

def build_all_ch02():
    print("==================================================================")
    print("🏗️  BUILDING COMPLETE CHAPTER 2 CURRICULUM (5 LESSONS)")
    print("==================================================================")
    for lesson in ch02_lessons:
        create_lesson_page(lesson)
    print("==================================================================")
    print("🎉 CHAPTER 2 LESSON SUITE SUCCESSFULLY GENERATED!")
    print("==================================================================")

if __name__ == '__main__':
    build_all_ch02()
