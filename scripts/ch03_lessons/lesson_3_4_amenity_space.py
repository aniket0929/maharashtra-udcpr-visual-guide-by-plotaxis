"""
UDCPR FROM SCRATCH - CHAPTER 3: LESSON 3.4
Module: scripts/ch03_lessons/lesson_3_4_amenity_space.py
Governing Regulation: Regulation 3.5 (Amenity Space), Regulation 3.6 (Electric Substation), Regulation 3.7 (Plot Area Standards)
Covers: Reg 3.5.1 to 3.5.3, 3.6 & 3.7 - 20,000 sq.m (2.0 Ha) threshold, 5% statutory amenity quota, 12m access road rule, in-situ FSI / TDR surrender compensation, electric substation spaces, and Table of minimum plot sizes.
"""

lesson_data = {
    'filename': 'reg-3-5-amenity-space-provision.html',
    'lesson_id': 'lesson-reg-3-5',
    'quiz_id': 'quiz-reg-3-5',
    'clause': 'Reg. 3.5, 3.6 & 3.7',
    'title': 'Amenity Space Surrender, Electric Substations & Plot Standards',
    'badge_status': 'Civic Infrastructure',
    'ch_slug': 'ch03',
    'ch_title': 'Chapter 3: General Land Development',
    'meta_desc': 'Statutory Amenity Space rules under UDCPR 3.5: 20,000 sq.m threshold, 5% quota in Municipal Corporations, 12.0m road access mandate, in-situ FSI/TDR compensation, transformer/substation allocations (Reg 3.6), and minimum plot sizes (Reg 3.7).',
    'lead_summary': 'Master the statutory requirements for providing and surrendering Amenity Space in Maharashtra: the 20,000 sq.m (2.0 Ha) threshold, calculating the 5% civic quota, surrender vs developer-retention options, 100% in-situ FSI or TDR compensation, mandatory 12.0m access road frontage, transformer space allocations (Reg 3.6), and minimum plot dimensions under Reg 3.7.',
    'amendment_cite': 'CR.236/18 & CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        While Recreational Open Space (ROS) is reserved for the private enjoyment of layout residents, <strong>Amenity Space</strong> is a statutory civic contribution dedicated to public municipal services such as primary schools, dispensaries, fire stations, community halls, and public utility substations.
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
        <li><strong>Statutory Threshold &amp; Quota (Reg. 3.5.1 &amp; Table #):</strong>
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px; margin-top:8px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Planning Authority Type</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Plot Area Threshold</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Amenity Space Percentage</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);" rowspan="2"><strong>Municipal Corporations, SPAs &amp; Metropolitan Authorities</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Less than 20,000 sq.m (2.0 Ha)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">NIL (0%)</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">20,000 sq.m or more (&ge; 2.0 Ha)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); color:var(--amber); font-weight:700;">5% of Gross Area minus DP Roads</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);" rowspan="2"><strong>Municipal Councils &amp; Regional Plan Areas</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">As per tiered local authority tables</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">1% to 5% based on land size</td>
              </tr>
            </tbody>
          </table>
        </li>
        <li><strong>Access Road Requirement (Reg. 3.5.1):</strong> The Amenity Space pocket must mandatorily abut a public street or internal layout road having a <strong>minimum width of 12.0 metres</strong> to ensure seamless public and municipal vehicle ingress.</li>
        <li><strong>Surrender vs Developer Development Options:</strong>
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li><strong>Option A: Surrender to Authority:</strong> The land is transferred free of cost and unencumbered to the Planning Authority. The owner receives <strong>100% in-situ FSI</strong> on the balance buildable land or <strong>Transferable Development Rights (TDR / DRC)</strong> under Chapter 11.</li>
            <li><strong>Option B: Retention by Owner:</strong> The owner develops an approved public amenity (e.g. school, medical clinic, maternity home, cr&egrave;che, library) as prescribed by the Authority, retaining title while serving the community.</li>
          </ul>
        </li>
        <li><strong>Electric Substation Space (Reg. 3.6):</strong> In layouts exceeding <strong>2,000 sq.m</strong> or where total power demand exceeds 50 kVA:
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li>11 kV Distribution Substation: Minimum <strong>5.0 m &times; 5.0 m</strong> space on road frontage.</li>
            <li>33 kV Receiving Substation: Minimum <strong>10.0 m &times; 10.0 m</strong> space dedicated to the power distribution utility.</li>
          </ul>
        </li>
        <li><strong>Minimum Plot Area Standards (Reg. 3.7):</strong>
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li><em>Detached Bunglows:</em> Minimum <strong>250 sq.m</strong> area, minimum frontage <strong>12.0 m</strong>.</li>
            <li><em>Semi-Detached (Twin):</em> Minimum <strong>125 sq.m</strong> area, minimum frontage <strong>8.0 m</strong>.</li>
            <li><em>Row Houses:</em> Minimum <strong>50 to 100 sq.m</strong>, minimum frontage <strong>4.5 to 6.0 m</strong>.</li>
            <li><em>Commercial / Cinema:</em> Minimum <strong>1,000 sq.m</strong>, minimum frontage <strong>20.0 m</strong>.</li>
          </ul>
        </li>
      </ul>
    """,
    'statutory_extract': "3.5.1 In the areas of Local Authorities, Special Planning Authorities and Metropolitan Region Development Authorities, Amenity Space as mentioned below on gross area after deducting area under reservations / roads in Development Plan... shall have to be provided in any layout or sub division of land or proposal for development: less than 20000 Sq.m. = Nil; 20000 Sq.m. or more = 5%... Such amenity space shall be provided with approach of minimum 12.0 m. wide road... in-situ FSI or TDR shall be permissible for the surrendered land...",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 3.5.1 // THE 20,000 SQ.M THRESHOLD</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Zero Amenity Below 2.0 Ha</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            In Municipal Corporations and Metropolitan Authorities, layouts under <strong>20,000 sq.m (2.0 Ha)</strong> have a <strong>NIL (0%)</strong> amenity space requirement. Once the plot reaches or exceeds 20,000 sq.m, exactly <strong>5%</strong> must be dedicated.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 3.5.1 // IN-SITU FSI / TDR CREDIT</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">100% Compensation</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            When the developer surrenders the 5% amenity space to the Planning Authority, they receive <strong>100% FSI credit</strong> of the surrendered land area to be utilized in-situ on the remaining buildable plots or claimed as TDR!
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_016 // AMENITY SPACE VS RECREATIONAL OPEN SPACE COMPARISON</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 3.4 VS 3.5 ARCHITECTURAL MATRIX</span>
        </div>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Regulatory Attribute</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Recreational Open Space (Reg. 3.4)</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Amenity Space (Reg. 3.5)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Applicability Threshold</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); font-weight:700;">&ge; 0.40 Ha (4,000 sq.m)</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); font-weight:700;">&ge; 2.00 Ha (20,000 sq.m) in Corps</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Statutory Quota</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">10% of Gross Area minus DP Roads</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">5% of Gross Area minus DP Roads</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Beneficiary / Ownership</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Private common use of layout residents</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Public municipal utility or civic amenity</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Minimum Road Access Width</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Internal layout road (&ge; 7.5m / 9.0m)</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">Minimum 12.0 metres wide road</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>FSI Deduction from Gross</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong); color:green; font-weight:700;">NOT deducted from buildable base</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Deducted from net plot; compensated via in-situ FSI/TDR</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="margin-bottom:12px;">
        <strong>Amenity Space &amp; FSI Calculation:</strong> A developer proposes a township on a <strong>30,000 sq.m (3.0 Ha)</strong> plot in Pune Municipal Corporation. A 30m DP road takes <strong>4,000 sq.m</strong>.
      </p>
      <div class="worked-step">
        <span class="step-badge">QUALIFYING AREA</span>
        <div>
          Gross Land = 30,000 sq.m.
          <br>Deduct DP Road = 4,000 sq.m.
          <br><span style="font-family:var(--mono);">Qualifying Plot Area = 30,000 &minus; 4,000 = <strong>26,000 sq.m</strong>.</span>
          <br>Since 26,000 sq.m &ge; 20,000 sq.m, the 5% Amenity Space rule applies.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">5% AMENITY SPACE</span>
        <div>
          <span style="font-family:var(--mono);">Amenity Space Quota = 5% of 26,000 sq.m = <strong>1,300 sq.m</strong>.</span>
          <br>The developer carves out a rectangular 1,300 sq.m plot (26m &times; 50m) abutting the 30m DP road (satisfying the &ge; 12.0m road access mandate).
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">SURRENDER &amp; IN-SITU FSI</span>
        <div>
          The developer surrenders the 1,300 sq.m Amenity Space to PMC for a municipal public school.
          <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; STATUTORY BENEFIT (Reg. 3.5.1):</span> 100% of the surrendered 1,300 sq.m area is granted as <strong>In-Situ FSI credit</strong>, which can be loaded directly onto the developer's residential towers on the remaining 24,700 sq.m land!
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ STATUTORY RESULT: Zero FSI loss occurs to the project while the city gains a fully accessible 1,300 sq.m public facility.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Locating Amenity Space on an Access Road Narrower than 12.0 Metres</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Regulation 3.5.1 explicitly mandates: <em>"Such amenity space shall be provided with approach of minimum 12.0 m. wide road."</em> Placing the amenity space on a 7.5m or 9.0m branch street violates the statutory access requirement and prevents acceptance by the Authority.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Demanding Amenity Space on Municipal Corporation Plots Below 20,000 sq.m</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Scrutiny officers sometimes erroneously demand a 5% amenity space on 8,000 sq.m or 15,000 sq.m plots in Municipal Corporations. Under Regulation 3.5.1 Table, for areas <strong>less than 20,000 sq.m</strong>, the statutory requirement is explicitly <strong>NIL</strong>.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 3: Failing to Demarcate Electric Substation Space on Road Frontage</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under Regulation 3.6, the electric distribution substation space (min 5m &times; 5m) must be situated at a location directly accessible from the public street. Placing the substation deep in the layout interior without truck access leads to MSEDCL rejection and power delay.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Directives CR.236/18 (Part 2) (26 Sept 2022)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Amenity Space Retention &amp; In-situ FSI Guidelines</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        State Government issued comprehensive directions regulating the conditions under which developers may retain amenity spaces for user development versus surrendering them for TDR / in-situ FSI under Section 154 of the MRTP Act.
      </p>
    """,
    'quiz': [
        {
            'question': 'In Municipal Corporation and Metropolitan Authority areas, what is the plot area threshold below which the Amenity Space requirement is NIL under Reg. 3.5.1?',
            'options': [
                'Less than 4,000 sq.m (0.40 Ha)',
                'Less than 10,000 sq.m (1.00 Ha)',
                'Less than 20,000 sq.m (2.00 Ha)',
                'Less than 50,000 sq.m (5.00 Ha)'
            ],
            'correctAnswer': 2,
            'explanation': "The Table under Regulation 3.5.1 explicitly states that for plot areas 'less than 20000 Sq.m.', the required Amenity Space is 'Nil'."
        },
        {
            'question': 'What is the mandatory minimum approach road width for an Amenity Space pocket under Regulation 3.5.1?',
            'options': [
                'Minimum 6.0 m wide road',
                'Minimum 9.0 m wide road',
                'Minimum 12.0 m wide road',
                'Minimum 18.0 m wide road'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.5.1 states: 'Such amenity space shall be provided with approach of minimum 12.0 m. wide road'."
        },
        {
            'question': 'When a developer surrenders the 5% Amenity Space to the Planning Authority, what statutory compensation is provided under Reg. 3.5.1?',
            'options': [
                'A cash subsidy from the State Treasury',
                'In-situ FSI or Transferable Development Rights (TDR) for 100% of the surrendered land',
                'Exemption from property taxes for 10 years',
                'Only an honorary civic commendation'
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.5.1 provides: 'in-situ FSI or TDR shall be permissible for the surrendered land' equal to 100% of the surrendered area."
        },
        {
            'question': 'What are the minimum dimensions required for an 11 kV electric distribution substation space under Regulation 3.6?',
            'options': [
                '2.5 m x 2.5 m',
                '5.0 m x 5.0 m',
                '10.0 m x 10.0 m',
                '15.0 m x 15.0 m'
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.6 mandates a minimum space of 5.0 m x 5.0 m for an 11 kV distribution transformer / substation located on road frontage."
        }
    ],
    'prev_url': '/lessons/reg-3-4-1-recreational-open-space.html',
    'prev_title': 'Reg. 3.4 Recreational Open Space',
    'next_url': '/lessons/reg-3-8-inclusive-housing.html',
    'next_title': 'Reg. 3.8 Inclusive Housing'
}
