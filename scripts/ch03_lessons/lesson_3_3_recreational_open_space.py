"""
UDCPR FROM SCRATCH - CHAPTER 3: LESSON 3.3
Module: scripts/ch03_lessons/lesson_3_3_recreational_open_space.py
Governing Regulation: Regulation 3.4 (Recreational Open Spaces)
Covers: Reg 3.4.1 to 3.4.8 - 0.40 Ha threshold, 10% statutory quota, pocket standards (min 400 sq.m, 15m width, 2.5:1 ratio), 10% clubhouse construction (G+1), and Green Belt ROS rules.
"""

lesson_data = {
    'filename': 'reg-3-4-1-recreational-open-space.html',
    'lesson_id': 'lesson-reg-3-4-1',
    'quiz_id': 'quiz-reg-3-4-1',
    'clause': 'Reg. 3.4',
    'title': 'Recreational Open Space (ROS) & Clubhouse Construction',
    'badge_status': 'Core Landscape Standards',
    'ch_slug': 'ch03',
    'ch_title': 'Chapter 3: General Land Development',
    'meta_desc': 'Recreational Open Space regulations under UDCPR 3.4: 10% mandatory quota on plots >= 0.4 ha, minimum pocket area 400 sq.m, 15m width rule, 2.5:1 length-to-width ratio, and 10% clubhouse construction (G+1).',
    'lead_summary': 'Learn the complete statutory requirements for providing Recreational Open Space in Maharashtra: the 0.40 Ha (4,000 sq.m) threshold, calculating the 10% statutory quota, geometric pocket rules (min 400 sq.m, 15m width, 2.5:1 ratio), permissible clubhouse structures (max 10% of ROS, Ground + 1 floor), and Green Belt open space integration under Order CR.104/22.',
    'amendment_cite': 'CR.104/22 & CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        To guarantee healthy urban living, fresh air, and social interaction, UDCPR-2020 enforces mandatory recreational open green spaces in every major residential, commercial, and industrial layout across Maharashtra.
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
        <li><strong>Applicability Threshold (Reg. 3.4.1):</strong> Mandatory in any land sub-division, plotted layout, or group housing scheme on a land parcel having an area of <strong>0.40 Hectare (4,000 sq.m) or more</strong>.</li>
        <li><strong>Statutory Quota (Reg. 3.4.1):</strong> Exactly <strong>10% of the gross land area</strong> (after deducting area under Development Plan roads and road widening proposals).</li>
        <li><strong>Geometric Pocket Rules (Reg. 3.4.6):</strong> An open space cannot be a leftover sliver or narrow passage:
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li><strong>Minimum Pocket Size:</strong> No individual ROS pocket can be less than <strong>400 sq.m</strong>.</li>
            <li><strong>Minimum Average Width:</strong> Must be at least <strong>15.0 metres</strong> average width (in exceptional irregular plots, never less than 10.0 m).</li>
            <li><strong>Length to Width Ratio:</strong> Shall not exceed <strong>2.5 : 1</strong> (prevents narrow corridor shapes).</li>
          </ul>
        </li>
        <li><strong>Permitted Structures in ROS (Reg. 3.4.7):</strong> A maximum of <strong>10% of the Recreational Open Space area</strong> may be built upon for community amenities:
          <ul style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li><em>Permitted Uses:</em> Clubhouse, gymnasium, pavilion, swimming pool, indoor sports, society office, creche, reading room, or security cabin.</li>
            <li><em>Height Limitation:</em> Strictly restricted to <strong>Ground + 1 upper floor only</strong> (maximum 8.0 m height).</li>
            <li><em>Boundary Setback:</em> The structure must maintain a minimum open setback of <strong>3.0 metres</strong> from the boundary of the open space pocket.</li>
            <li><em>Ownership:</em> Vests exclusively in the cooperative housing society or condominium; cannot be alienated or sold.</li>
          </ul>
        </li>
        <li><strong>Green Belt Open Spaces (Reg. 3.4.5 &amp; Order CR.104/22):</strong> Land falling in river/nallah green belts may be counted towards the 10% Recreational Open Space quota under specific conditions, provided it remains unbuilt and landscaped.</li>
        <li><strong>Means of Access (Reg. 3.4.8):</strong> Every open space pocket must have direct road frontage abutting an internal layout street or public road.</li>
      </ul>
    """,
    'statutory_extract': "3.4.1 Recreational Open Space: In any layout or sub-division or any development of land for any use / zone having an area 0.4 ha. or more, 10% of the gross area after deducting area under proposed D.P. / R.P. Roads, if any, shall be reserved as recreational open space... 3.4.6 Minimum Dimensions: No such recreational open space shall be less than 400 sq.m. The minimum dimension of such open space shall not be less than 15.0 m... The length to breadth ratio shall not exceed 2.5:1... 3.4.7 Structures permitted in Open Space: Maximum 10% of the area of recreational open space may be built upon... Ground plus one floor only with height not exceeding 8.0 m...",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 3.4.6 // POCKET GEOMETRY</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Three Geometric Rules</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            1. Area &ge; <strong>400 sq.m</strong>
            <br>2. Width &ge; <strong>15.0 metres</strong>
            <br>3. Length : Width ratio &le; <strong>2.5 : 1</strong>
            <br>No narrow ribbons, unusable corners, or residual boundary setbacks can masquerade as open space.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 3.4.7 // CLUBHOUSE CONSTRAINTS</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">10% Built-Up &amp; G+1 Ceiling</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Clubhouses, gymnasia, and pavilions are capped at <strong>10% of ROS footprint</strong>, Ground + 1 upper floor (&le; 8.0m height), with a mandatory <strong>3.0 m open perimeter setback</strong> from the ROS edge.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_001 // RECREATIONAL OPEN SPACE (ROS) GEOMETRIC SPECIFICATION</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 3.4 BLUEPRINT PLATE</span>
        </div>
        <div style="padding:14px; font-family:var(--mono); font-size:11px; line-height:1.8; color:var(--ink);">
          +-------------------------------------------------------------------------------+<br>
          |&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;RECREATIONAL OPEN SPACE (ROS) POCKET&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|<br>
          |&emsp;MINIMUM AREA: &ge; 400 SQ.M&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;LENGTH : WIDTH RATIO &le; 2.5 : 1&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|<br>
          |&emsp;&lt;--------------------------- AVERAGE WIDTH &ge; 15.0 M ----------------------------&gt;&emsp;|<br>
          |&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|<br>
          |&emsp;&emsp;+----------------------------- 3.0 M SETBACK ---------------------------+&emsp;&emsp;|<br>
          |&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;|<br>
          |&emsp;&emsp;|&emsp;&emsp;[ CLUBHOUSE / GYMNASIUM / PAVILION ]&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;|<br>
          |&emsp;&emsp;|&emsp;&emsp;&bull; Max Footprint: 10% of ROS Pocket Area&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;|<br>
          |&emsp;&emsp;|&emsp;&emsp;&bull; Height: Ground + 1 Floor Only (&le; 8.0 m)&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;|<br>
          |&emsp;&emsp;|&emsp;&emsp;&bull; Mandatory 3.0 m all-around open margin inside ROS pocket&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;|<br>
          |&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|&emsp;&emsp;|<br>
          |&emsp;&emsp;+-----------------------------------------------------------------------+&emsp;&emsp;|<br>
          |&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|<br>
          +=========================== ABUTTING INTERNAL ROAD &ge; 9.0 M ===================+
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="margin-bottom:12px;">
        <strong>Step-by-Step ROS Computation:</strong> A residential layout project in Nagpur has a Gross Plot Area of <strong>12,000 sq.m (1.20 Ha)</strong>. A 24m DP road widening affects <strong>2,000 sq.m</strong> of the land.
      </p>
      <div class="worked-step">
        <span class="step-badge">NET QUALIFYING AREA</span>
        <div>
          Gross Land = 12,000 sq.m.
          <br>Deduct DP Road Widening = 2,000 sq.m.
          <br><span style="font-family:var(--mono);">Qualifying Plot Area = 12,000 &minus; 2,000 = <strong>10,000 sq.m</strong>.</span>
          <br>Since 10,000 sq.m &ge; 4,000 sq.m (0.40 Ha), Regulation 3.4.1 triggers.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">10% STATUTORY QUOTA</span>
        <div>
          <span style="font-family:var(--mono);">Required ROS Area = 10% of 10,000 sq.m = <strong>1,000 sq.m</strong>.</span>
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">POCKET SUBDIVISION</span>
        <div>
          The architect provides two green pockets:
          <br>&bull; <strong>Pocket 1:</strong> 600 sq.m (Width: 20 m, Length: 30 m; Ratio = 1.5:1 &le; 2.5:1) &rarr; <span style="color:var(--blueprint);">&#10003; Compliant</span>.
          <br>&bull; <strong>Pocket 2:</strong> 400 sq.m (Width: 16 m, Length: 25 m; Ratio = 1.56:1 &le; 2.5:1) &rarr; <span style="color:var(--blueprint);">&#10003; Compliant</span>.
          <br>Both pockets exceed the 400 sq.m minimum area and 15m minimum average width rules.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">CLUBHOUSE ENTITLEMENT</span>
        <div>
          Total ROS = 1,000 sq.m.
          <br><span style="font-family:var(--mono);">Max Permissible Clubhouse Footprint = 10% of 1,000 = <strong>100 sq.m</strong>.</span>
          <br>Max Total Built-Up Area (G+1) = 100 sq.m &times; 2 = <strong>200 sq.m</strong>.
          <br>Setback around clubhouse = <strong>3.0 m clear open space</strong> from Pocket 1 boundaries.
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ STATUTORY COMPLIANCE: 1,000 sq.m open space is fully secured, dimensionally compliant, and non-alienable.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Providing a Long Narrow Strip Less than 15.0 Metres Wide</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Developers often attempt to designate peripheral boundary buffers (e.g., 6m wide &times; 70m long) as Recreational Open Space. Even if the area exceeds 400 sq.m, it violates the <strong>15.0 m minimum average width</strong> and the <strong>2.5:1 length-to-width ratio</strong>, leading to immediate rejection.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Constructing Commercial Banquet Halls or Rental Facilities in ROS</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Regulation 3.4.7 permits clubhouses, gymnasia, and pavilions solely for the common use of the society occupants. Commercial leasing of open space clubhouses to outside parties for marriage events or banquets is an actionable offence and grounds for demolition.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 3: Deducting 10% ROS Area from the FSI Computation Base</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Architects sometimes mistakenly deduct the 10% Recreational Open Space from the plot area when calculating permissible FSI. Under Regulation 3.9, <strong>Recreational Open Space is NOT deducted</strong> from the net plot area—full FSI entitlement remains on the balance buildable land!
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Order CR.104/22 (23 May 2022)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Green Belt Recreational Open Space Guidelines</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Clarified conditions under which river and nallah green belts may be integrated into the 10% Recreational Open Space quota without reducing required open spaces in the buildable portion of large layouts.
      </p>
    """,
    'quiz': [
        {
            'question': 'What is the minimum land area threshold that triggers mandatory 10% Recreational Open Space under Regulation 3.4.1?',
            'options': [
                '0.10 Hectare (1,000 sq.m)',
                '0.20 Hectare (2,000 sq.m)',
                '0.40 Hectare (4,000 sq.m)',
                '1.00 Hectare (10,000 sq.m)'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.4.1 explicitly states that in any layout or sub-division or development having an area of '0.4 ha. (4,000 sq.m) or more', 10% of the gross area (minus DP roads) must be reserved as recreational open space."
        },
        {
            'question': 'What is the statutory minimum area and minimum average width for any single Recreational Open Space pocket under Reg. 3.4.6?',
            'options': [
                'Minimum 200 sq.m area and 10.0 m width',
                'Minimum 300 sq.m area and 12.0 m width',
                'Minimum 400 sq.m area and 15.0 m width',
                'Minimum 500 sq.m area and 20.0 m width'
            ],
            'correctAnswer': 2,
            'explanation': "Under Regulation 3.4.6, 'No such recreational open space shall be less than 400 sq.m. The minimum dimension of such open space shall not be less than 15.0 m'."
        },
        {
            'question': 'What is the maximum permissible built-up ground coverage and height for a clubhouse structure inside an open space under Reg. 3.4.7?',
            'options': [
                'Max 5% of ROS area, single storey (G only)',
                'Max 10% of ROS area, Ground + 1 upper floor (&le; 8.0 m height)',
                'Max 20% of ROS area, Ground + 2 upper floors',
                'Zero construction is permitted under any circumstances'
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.4.7 stipulates: 'Maximum 10% of the area of recreational open space may be built upon... Ground plus one floor only with height not exceeding 8.0 m'."
        },
        {
            'question': 'What is the statutory length to width ratio limit for a Recreational Open Space pocket under Regulation 3.4.6?',
            'options': [
                'Shall not exceed 1.5 : 1',
                'Shall not exceed 2.0 : 1',
                'Shall not exceed 2.5 : 1',
                'Shall not exceed 4.0 : 1'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.4.6 explicitly mandates: 'The length to breadth ratio shall not exceed 2.5:1' to ensure well-proportioned, usable open space pockets."
        }
    ],
    'prev_url': '/lessons/reg-3-3-internal-layout-roads.html',
    'prev_title': 'Reg. 3.2-3.3 Layout Roads',
    'next_url': '/lessons/reg-3-5-amenity-space-provision.html',
    'next_title': 'Reg. 3.5 Amenity Space'
}
