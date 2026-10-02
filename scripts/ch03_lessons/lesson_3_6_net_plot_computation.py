"""
UDCPR Visual Guide - CHAPTER 3: LESSON 3.6
Module: scripts/ch03_lessons/lesson_3_6_net_plot_computation.py
Governing Regulation: Regulation 3.9 through Regulation 3.13
Covers: Net plot area formula, non-deduction of 10% Recreational Open Space from FSI base, in-situ FSI for DP reservations (Reg 3.10), DP road/site realignments (Reg 3.11), amalgamation rules (Reg 3.12), and cycle tracks along rivers (Reg 3.13).
"""

lesson_data = {
    'filename': 'reg-3-9-net-plot-area-computation.html',
    'lesson_id': 'lesson-reg-3-9',
    'quiz_id': 'quiz-reg-3-9',
    'clause': 'Reg. 3.9 – 3.13',
    'title': 'Net Plot Area Computation, In-situ FSI, DP Realignments & Amalgamation',
    'badge_status': 'Core Mathematical Engine',
    'ch_slug': 'ch03',
    'ch_title': 'Chapter 3: General Land Development',
    'meta_desc': 'Mathematical computation of Net Plot Area and FSI under UDCPR 3.9: Gross deductions, non-deduction of 10% ROS, In-Situ FSI compensation for surrendered DP sites (Reg 3.10), DP road realignment limits (Reg 3.11), amalgamation rules, and river cycle tracks.',
    'lead_summary': 'Master the master equation of urban development potential in Maharashtra: calculating Net Plot Area under Regulation 3.9, the golden statutory rule that 10% Recreational Open Space is never deducted from FSI, In-Situ FSI compensation for surrendered DP land (Reg 3.10), statutory boundaries for realigning DP roads and public reservations (Reg 3.11), and plot amalgamation protocols.',
    'amendment_cite': 'CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        Before calculating building heights, floor space, or premium charges, every architect must compute the exact <strong>Net Plot Area</strong>. Regulations 3.9 through 3.13 define the mathematical rules for deductions, surrendered land compensations, DP site adjustments, and plot amalgamations.
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
        <li><strong>The Net Plot Area Formula (Reg. 3.9):</strong>
          <div style="background:var(--paper); border:1px solid var(--ink); padding:10px 14px; margin:8px 0; font-family:var(--mono); font-size:0.9rem; color:var(--ink);">
            <strong>NET PLOT AREA = Gross Plot Area &minus; [ Area under DP Roads / Road Widening + Area under DP Reservations + Area under Surrendered Amenity Space ]</strong>
          </div>
        </li>
        <li><strong>THE GOLDEN RULE OF RECREATIONAL OPEN SPACE (Reg. 3.9):</strong>
          <div style="background:var(--paper-raised); border:1px solid var(--blueprint); border-left:4px solid var(--blueprint); padding:10px 14px; margin:6px 0; font-family:var(--mono); font-size:0.85rem; color:var(--blueprint);">
            "Recreational open space shall not be deducted for the purpose of calculation of FSI."
          </div>
          <em>Significance:</em> Even though 10% of the land is physically reserved as an open green park, its FSI is <strong>not lost</strong>—it floats onto the remaining buildable footprint!
        </li>
        <li><strong>Transfer of Land Under DP Sites for FSI (Reg. 3.10):</strong> When an owner surrenders land reserved for a DP road or public reservation (school, garden, hospital) free of cost and unencumbered to the Authority:
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li>The owner receives <strong>100% In-Situ FSI</strong> of the surrendered land area on the balance holding.</li>
            <li>Alternatively, if the remaining plot cannot absorb the extra area due to height or margin constraints, the owner can claim <strong>Development Rights Certificates (DRC / TDR)</strong> under Chapter 11.</li>
          </ul>
        </li>
        <li><strong>Relocation of DP / RP Sites &amp; Roads (Reg. 3.11):</strong> A public reservation or DP road alignment may be adjusted within the same holding by the Authority provided:
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li>The shifted reservation does not move by more than <strong>100 metres</strong>.</li>
            <li>The total reservation area is not reduced and shape remains functional.</li>
            <li>Direct road access is preserved, and the public purpose is not compromised.</li>
          </ul>
        </li>
        <li><strong>Amalgamation of Plots (Reg. 3.12):</strong> When two or more plots are combined into a single holding:
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li>The amalgamated plot derives its road width entitlement from the widest abutting public road, provided the road has adequate continuous connectivity.</li>
            <li>Permissible FSI, height, and setbacks are evaluated on the newly formed combined holding.</li>
          </ul>
        </li>
        <li><strong>Cycle Track Along Rivers &amp; Nallahs (Reg. 3.13):</strong> Green mobility buffer strip developed along river banks to foster non-motorized transport.</li>
      </ul>
    """,
    'statutory_extract': "3.9 Net Plot Area and Computation of FSI: For the purpose of computing FSI / Built - up area, the net plot area shall be as under :- i) In case of plotted layout... gross area shall be considered after deducting the area under Development Plan roads / Regional Plan roads and road widening therein... ii) Recreational open space shall not be deducted for the purpose of calculation of FSI... 3.10 Transfer of Land under D.P. Sites in Lieu of FSI: If the owner hands over the land reserved for D.P. / R.P. proposal free of cost... he shall be entitled for FSI / TDR as per Chapter - 11...",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 3.9 // FSI BASE INTEGRITY</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">ROS Is Never Deducted</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            In a 10,000 sq.m layout with 1,000 sq.m ROS, FSI is calculated on <strong>10,000 sq.m</strong>, not 9,000 sq.m. The entire developmental potential is preserved and loaded onto the buildable plots.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 3.10 // 100% IN-SITU FSI CREDIT</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Surrendered Road Compensation</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Surrendering land for a DP road or public garden grants <strong>100% In-Situ FSI credit</strong> (or 100% TDR credit under Chapter 11), ensuring zero economic loss from city infrastructure widening.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_018 // NET PLOT AREA &amp; FSI CALCULATION ARCHITECTURE</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 3.9 STATUTORY ENGINE</span>
        </div>
        <div style="padding:14px; font-family:var(--mono); font-size:11.5px; line-height:1.8; color:var(--ink);">
          GROSS HOLDING AS PER CADASTRAL REVENUE / MOJNI RECORD<br>
          ├── [&minus;] Area under Sanctioned DP / RP Road Widening (&sect; 3.9.i)<br>
          ├── [&minus;] Area under Sanctioned DP Public Reservations (&sect; 3.9.i)<br>
          └── [&minus;] Area under Surrendered Amenity Space (&sect; 3.5.1)<br>
          =========================================================================<br>
          = NET PLOT AREA (PHYSICAL LAND BASE)<br>
          <br>
          FSI COMPUTATION MATRIX:<br>
          &bull; Basic FSI Calculated On: Net Plot Area + FSI Credit for Surrendered DP Road / Reservation<br>
          &bull; 10% Recreational Open Space (ROS): PHYSICALLY RESERVED ON SITE, BUT ZERO FSI DEDUCTION!<br>
          &bull; Permissible Built-Up Area = (Net Plot Area &times; Base FSI) + In-Situ Surrender FSI + Premium FSI + TDR
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="margin-bottom:12px;">
        <strong>Comprehensive Development Potential Calculation:</strong> An owner holds a <strong>20,000 sq.m (2.0 Ha)</strong> land parcel in Nashik Municipal Corporation. Road width is 18m; Base FSI is <strong>1.10</strong>.
      </p>
      <div class="worked-step">
        <span class="step-badge">DEDUCTIONS</span>
        <div>
          Gross Land = 20,000 sq.m.
          <br>&bull; 18m DP Road Widening = <strong>2,000 sq.m</strong> (surrendered to PMC).
          <br>&bull; DP Primary School Reservation = <strong>1,500 sq.m</strong> (surrendered to PMC).
          <br>&bull; Qualifying Land for Amenity = 20,000 &minus; 2,000 = 18,000 sq.m &lt; 20,000 sq.m &rarr; Amenity Space = <strong>NIL (0 sq.m)</strong>.
          <br><span style="font-family:var(--mono);">Net Buildable Physical Plot = 20,000 &minus; 2,000 &minus; 1,500 = <strong>16,500 sq.m</strong>.</span>
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">RECREATIONAL OPEN SPACE</span>
        <div>
          Qualifying Area = 18,000 sq.m &ge; 4,000 sq.m.
          <br><span style="font-family:var(--mono);">10% ROS Area = 10% of 18,000 = <strong>1,800 sq.m</strong></span> (kept green on site).
          <br><em>Crucial Rule:</em> The 1,800 sq.m is <strong>NOT deducted</strong> from the FSI base!
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">BUILT-UP POTENTIAL</span>
        <div>
          1. Base FSI on Net Plot: 16,500 sq.m &times; 1.10 = <strong>18,150 sq.m BUA</strong>.
          <br>2. In-Situ FSI for Surrendered DP Road: 2,000 sq.m &times; 1.10 = <strong>2,200 sq.m BUA</strong>.
          <br>3. In-Situ FSI for Surrendered School: 1,500 sq.m &times; 1.10 = <strong>1,650 sq.m BUA</strong>.
          <br><span style="font-family:var(--mono); font-weight:700; color:var(--blueprint);">Total Permissible Base BUA on remaining 16,500 sq.m = 18,150 + 2,200 + 1,650 = <strong>22,000 sq.m BUA</strong>!</span>
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ KEY TAKEAWAY: Surrendering DP land yields 100% in-situ FSI, and keeping 1,800 sq.m ROS green incurs zero FSI penalty.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Deducting Recreational Open Space Area from the FSI Calculation</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Novice architects sometimes calculate Base BUA as `(Net Plot - ROS) * Base FSI`. Under Regulation 3.9(ii), this erroneously deprives the developer of hundreds of square metres of statutory FSI. ROS area is always included in the FSI multiplication base.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Relocating DP Roads Beyond the 100-Metre Statutory Limit</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under Regulation 3.11, the Authority may realign a DP road or public reservation within the holding, but shifting the alignment by <strong>more than 100 metres</strong> or changing its connectivity constitutes a modification of substantial nature requiring formal Section 37 MRTP Act gazette sanction.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 3: Claiming Double Compensation for Surrendered Lands</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          An owner who surrenders DP road widening land and consumes 100% In-Situ FSI on their remaining plot <strong>cannot also apply for TDR (DRC)</strong> on that same land. The Authority stamps the revenue 7/12 extract to prevent double monetization.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">In-situ FSI &amp; TDR Generation Clarifications</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Standardized the formula for computing in-situ FSI credits on plots affected by multiple reservations and clarified the calculation of net plot area where amenity space is surrendered versus retained.
      </p>
    """,
    'quiz': [
        {
            'question': 'Under Regulation 3.9(ii), how is the 10% Recreational Open Space (ROS) treated during the calculation of FSI?',
            'options': [
                'It is deducted from the gross plot area before computing FSI',
                'Recreational open space shall not be deducted for the purpose of calculation of FSI',
                'It is reduced by 50% from the FSI base',
                'It is converted into commercial FSI'
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.9(ii) explicitly mandates: 'Recreational open space shall not be deducted for the purpose of calculation of FSI'. The FSI potential is preserved and loaded onto buildable portions."
        },
        {
            'question': 'What statutory compensation is granted to an owner who surrenders land under a DP road or public reservation under Regulation 3.10?',
            'options': [
                '100% In-situ FSI or Transferable Development Rights (TDR / DRC)',
                'A tax exemption certificate for 5 years',
                '50% cash payment from the Municipal Corporation',
                'No compensation is allowed under the Act'
            ],
            'correctAnswer': 0,
            'explanation': "Regulation 3.10 grants 100% In-Situ FSI or TDR/DRC under Chapter 11 for land surrendered for DP proposals free of cost and unencumbered."
        },
        {
            'question': 'What is the maximum permissible shifting distance when the Authority realigns a DP road or reservation within a land holding under Reg. 3.11?',
            'options': [
                'Up to 25 metres',
                'Up to 50 metres',
                'Up to 100 metres',
                'Any distance across the municipal ward'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.11 allows the Authority to relocate a DP proposal within the same holding provided it is shifted by not more than 100 metres and maintains functional connectivity and area."
        },
        {
            'question': 'Which of the following is DEDUCTED from the gross plot area to arrive at the Net Plot Area under Regulation 3.9?',
            'options': [
                'Area under 10% Recreational Open Space',
                'Area under Sanctioned DP Roads, DP Reservations, and Surrendered Amenity Space',
                'Area under basement parking',
                'Area under clubhouse swimming pool'
            ],
            'correctAnswer': 1,
            'explanation': "Under Regulation 3.9, the Net Plot Area is computed after deducting area under DP Roads, DP Reservations, and Surrendered Amenity Space. Recreational Open Space is NOT deducted."
        }
    ],
    'prev_url': '/lessons/reg-3-8-inclusive-housing.html',
    'prev_title': 'Reg. 3.8 Inclusive Housing',
    'next_url': '/chapters/',
    'next_title': 'Chapters Syllabus Overview'
}
