"""
UDCPR FROM SCRATCH - CHAPTER 4: LESSON 4.1
Module: scripts/ch04_lessons/lesson_4_1_residential_zones.py
Governing Regulations: Regulations 4.1 to 4.6 (General, Equivalency, R-1, R-2, Low Density, Future Urbanizable)
"""

lesson_data = {
    'filename': 'reg-4-1-residential-zones-r1-r2.html',
    'lesson_id': 'lesson-reg-4-1',
    'quiz_id': 'quiz-reg-4-1',
    'clause': 'Reg. 4.1 – 4.6',
    'title': 'Zoning Classification & Residential Zones (R-1 vs. R-2)',
    'badge_status': 'Core Land Use',
    'ch_slug': 'ch04',
    'ch_title': 'Chapter 4: Land Use Classification & Permissible Uses',
    'meta_desc': 'Statutory rules for Residential Zones R-1 and R-2 under UDCPR Regulations 4.1 to 4.6: road width thresholds, permissible home occupations, professional offices, clinics, and mixed-use commercial shoplines.',
    'lead_summary': 'Learn the governing land use zoning framework under Maharashtra UDCPR-2020: how the statutory threshold between Pure Residential (R-1) and General Mixed-Use Residential (R-2) is determined strictly by road width, what home occupations and professional offices are allowed without commercial conversion, and the rules for clinics and convenience shopping.',
    'amendment_cite': 'CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        Chapter 4 establishes the fundamental legal hierarchy for what can be built where. Every development permission must strictly conform to the land use zone assigned in the sanctioned Development Plan (DP) or Regional Plan (RP).
      </p>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">1. The Road Width Threshold: R-1 vs. R-2</h4>
      <p style="margin-bottom:12px; font-size:0.92rem; color:var(--ink-soft);">
        A common misconception is that R-1 and R-2 are permanently colored differently on every Development Plan. Under UDCPR <strong>Regulation 4.3 &amp; 4.4</strong>, whether a plot is governed by R-1 (pure residential) or R-2 (mixed-use residential) is determined automatically by the <strong>width of the abutting road</strong>:
      </p>

      <div style="overflow-x:auto; margin-bottom:16px;">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>Geographic Location / Planning Authority</th>
              <th>Residential Zone R-1 (Pure Residential)</th>
              <th>Residential Zone R-2 (Mixed-Use Allowed)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="font-weight:600;">Congested Area (Core Gaothan)</td>
              <td>Road width <strong>below 9.0 meters</strong></td>
              <td>Road width <strong>9.0 meters and above</strong></td>
            </tr>
            <tr style="background:var(--paper);">
              <td style="font-weight:600;">Non-Congested Area (Municipal Corporations &amp; A/B Class Councils)</td>
              <td>Road width <strong>below 12.0 meters</strong></td>
              <td>Road width <strong>12.0 meters and above</strong></td>
            </tr>
            <tr>
              <td style="font-weight:600;">C Class Councils, Nagar Panchayats &amp; Regional Plan Areas</td>
              <td>Road width <strong>below 9.0 meters</strong></td>
              <td>Road width <strong>9.0 meters and above</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">2. What is Permitted in Pure Residential Zone (R-1)?</h4>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; font-size:0.92rem; color:var(--ink-soft);">
        <li><strong>Customary Home Occupations (Reg. 4.3(iv)):</strong> Carried out exclusively by household members without hired labor (stitching, embroidery, beauty parlour, button making). Motive electric power must not exceed <strong>1 H.P. (0.75 kW)</strong>.</li>
        <li><strong>Professional Offices (Reg. 4.3(vi)):</strong> Permitted within a residential tenement for the resident's own profession (architects, engineers, lawyers, chartered accountants) up to a maximum carpet area of <strong>50 sq.m</strong>.</li>
        <li><strong>Medical Dispensaries &amp; Clinics (Reg. 4.3(v)):</strong> Permitted on <em>any floor</em>. Maternity homes and nursing homes with indoor patients up to <strong>20 beds</strong> are allowed on any floor, provided they have a separate means of access/staircase (unless the doctor resides on the upper floor).</li>
        <li><strong>Convenience Shops (Reg. 4.3(xvi)):</strong> Permitted <em>only on the ground floor</em> to serve day-to-day neighborhood needs (groceries, vegetables, medical stores, milk booths).</li>
        <li><strong>Educational &amp; Coaching (Reg. 4.3(viii–x)):</strong> Primary and nursery schools, creche/day-care up to 100 sq.m, and private coaching classes up to 100 sq.m with dedicated on-site parking.</li>
        <li><strong>Flour Mills &amp; Masala Grinding (Reg. 4.3(xx)):</strong> Permitted subject to power load not exceeding <strong>10 H.P.</strong></li>
      </ul>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">3. What is Permitted in Mixed-Use Zone (R-2)?</h4>
      <p style="margin-bottom:10px; font-size:0.92rem; color:var(--ink-soft);">
        In R-2 zones, all R-1 uses are permitted, plus unrestricted mixed commercial-residential developments:
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; font-size:0.92rem; color:var(--ink-soft);">
        <li>Commercial shops, departmental stores, shopping malls, and professional offices without floor or area restrictions.</li>
        <li>Hotels, restaurants, lodgings, and boarding houses.</li>
        <li>Service industries listed under Regulation 4.4.2(iv) with electrical power and worker limits.</li>
        <li>Vehicle fuel stations (Petrol/CNG/LPG/EV Charging) subject to Table 6-E road and setback norms.</li>
        <li>IT / ITES establishments and data centers.</li>
      </ul>
    """,
    'statutory_extract': "4.3 RESIDENTIAL ZONE R-1 includes Residential plots abutting on roads below 9.0 m. in width in congested area shown on the Development Plan and on roads below 12.0 m. in width in outside congested area... 4.4 RESIDENTIAL ZONE R-2 includes Residential plots abutting on roads having existing or proposed width of 9.0 m. and above in congested area and 12.0 m. and above in non-congested area... All uses or mix uses may be permitted irrespective of restriction on floor or area, except uses specially mentioned in these regulations.",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 4.3 // R-1 THRESHOLD</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Pure Residential Envelope</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Governs narrow road access (&lt; 12m outside gaothan; &lt; 9m inside gaothan). Protects quiet residential character by barring high-intensity retail and shopping complexes.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 4.4 // R-2 COMMERCIAL LINE</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Unrestricted Mixed Use</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Triggers on roads &ge; 12.0m (&ge; 9.0m in congested/C-class). Unlocks commercial shops across ground, podium, and upper floors, subject only to parking quotas.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_015 // R-1 vs R-2 PERMISSIBLE ACTIVITIES MATRIX</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">CHAPTER 4 SPECIFICATION PLATE</span>
        </div>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11.5px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Activity / Use Category</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Permissibility in R-1</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Permissibility in R-2</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Governing Restrictions / Conditions</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Customary Home Occupation</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Permitted</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Permitted</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Max 1 H.P., family members only, no hired laborers</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Professional Office</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Permitted</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Permitted</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">In R-1: max 50 sq.m carpet in own residence. In R-2: unrestricted.</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Convenience Shopping</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--amber); font-weight:700;">Ground Floor Only</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Any Floor</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">R-1: grocery, medical, milk booths only on ground level</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Nursing Home / Hospital</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--amber); font-weight:700;">Max 20 Beds</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Unrestricted</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">R-1 requires independent staircase/access unless doctor resides above</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Coaching Classes / Creche</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--amber); font-weight:700;">Max 100 sq.m</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Unrestricted</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Requires dedicated on-site parking in premises</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Departmental Store / Mall</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--brick); font-weight:700;">Prohibited</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Permitted</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Subject to Chapter 8 parking standards and road width</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="margin-bottom:12px;">
        <strong>Practical Scrutiny Problem:</strong> An architect is hired to plan a mixed-use commercial and residential building in a Municipal Corporation outside gaothan limits. The existing street in front of the plot is 9.0 meters wide, but the Development Plan proposes a road widening line to 15.0 meters.
      </p>
      <div class="worked-step">
        <span class="step-badge">ZONE CLASSIFICATION</span>
        <div>
          Under Regulation 4.4: <em>"Residential plots abutting on roads having existing OR proposed width of 12.0 m. and above in non-congested area"</em> fall into <strong>R-2 Zone</strong>.
          <br>Because the proposed DP road width is <strong>15.0 meters (&ge; 12.0m)</strong>, the plot qualifies for <strong>full R-2 mixed-use sanction</strong>!
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">COMMERCIAL LAYOUT DESIGN</span>
        <div>
          The architect can design:
          <br>• Ground &amp; 1st Floor: Commercial retail shops, banks, and restaurants.
          <br>• 2nd to 10th Floor: Residential apartments.
          <br>• No need to restrict shops to convenience stores or ground floor only.
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ SANCTION RESULT: Development permission is sanctioned under Regulation 4.4 without any special relaxation.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Placing Commercial Offices on Upper Floors on a Sub-12m Road</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          On an 11.0m road in non-congested areas, the plot remains strictly <strong>R-1 Zone</strong>. Designing commercial offices or coaching classes above 100 sq.m on upper floors violates Reg. 4.3 and will be rejected at municipal scrutiny.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Forgetting the Independent Staircase for 20-Bed Nursing Homes</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under Regulation 4.3(v), maternity homes and clinics with indoor patients up to 20 beds must have a separate staircase access unless the doctor lives on the upper floor. Sharing a single common residential lift and stair will cause scrutiny rejection.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Zoning Equivalency &amp; Infrastructure Cost</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Amended Regulation 4.2 to clarify that R-3 and R-4 zones are treated equivalent to Residential Zone upon payment of infrastructure charges determined by the Planning Authority.
      </p>
    """,
    'quiz': [
      {
        'question': 'In a non-congested area of a Municipal Corporation, what minimum road width is required for a residential plot to be governed by R-2 mixed-use regulations?',
        'options': [
          '6.0 meters',
          '9.0 meters',
          '12.0 meters',
          '15.0 meters'
        ],
        'correctAnswer': 2,
        'explanation': 'Under Regulation 4.4, in non-congested areas of Municipal Corporations, R-2 regulations apply to plots abutting roads having an existing or proposed width of 12.0 meters and above.'
      },
      {
        'question': 'What is the maximum carpet area allowed for a professional office within a residential tenement in an R-1 zone under Regulation 4.3(vi)?',
        'options': [
          '25 sq.m',
          '50 sq.m',
          '100 sq.m',
          'Unrestricted'
        ],
        'correctAnswer': 1,
        'explanation': 'Under Regulation 4.3(vi), professional offices in residential tenements for personal use are permitted up to a maximum carpet area of 50 sq.m.'
      },
      {
        'question': 'What is the maximum electricity power load permitted for customary home occupations under Regulation 4.3(iv)?',
        'options': [
          '1 H.P. (0.75 kW)',
          '5 H.P. (3.75 kW)',
          '10 H.P. (7.5 kW)',
          'No power allowed'
        ],
        'correctAnswer': 0,
        'explanation': 'Regulation 4.3(iv) dictates that if motive power is used for customary home occupations, the total electricity load shall not exceed 1 H.P. (0.75 kW).'
      }
    ],
    'prev_url': '/lessons/reg-3-9-net-plot-area-computation.html',
    'prev_title': 'Reg. 3.9 Net Plot Area',
    'next_url': '/lessons/reg-4-7-commercial-and-industrial-zones.html',
    'next_title': 'Reg. 4.7-4.9 Commercial & Industrial'
}
