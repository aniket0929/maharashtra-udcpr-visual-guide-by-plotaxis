"""
UDCPR Visual Guide - CHAPTER 8, LESSON 4
Regulation 8.2.2, Table 8-C & Notes: City Multipliers, 2-Wheeler Exemption & Excess Parking Surcharges
File: scripts/ch08_lessons/lesson_8_4_city_multipliers_penalties.py
"""

lesson_data = {
    'filename': 'reg-8-2-2-city-multipliers-and-parking-penalties.html',
    'lesson_id': 'reg-8-2-2-city-multipliers-and-parking-penalties',
    'quiz_id': 'quiz-8-4',
    'clause': 'Reg. 8.2.2, Table 8-C & Notes',
    'title': 'City Multipliers (Table 8-C), 2-Wheeler Exemption & Excess Parking Surcharges',
    'badge_status': 'TABLE 8-C • AMENDMENTS 2022-2024',
    'ch_slug': 'ch08',
    'ch_title': 'Chapter 8: Parking, Loading and Unloading Spaces',
    'meta_desc': 'Master UDCPR Regulation 8.2.2, Table 8-C city multipliers (1.00 down to 0.40), Note vii two-wheeler non-reduction rule, Note v 50% excess parking fee (10% land ASR) and Jan 2024 phased OC public surrender rule.',
    
    'lead_summary': (
        'Regulation 8.2.2 and Table 8-C establish Maharashtra’s geographic parking discount matrix, reducing baseline Table 8-B quotas via multipliers '
        'ranging from 1.00 in Tier-1 metros (Pune, PCMC, Thane) down to 0.40 in Nagar Panchayats and Regional Plan areas. '
        'However, landmark amendments fundamentally alter this formula: under Note (vii), residential two-wheeler parking is completely exempt from Table 8-C '
        'and must be provided at 100% full quota across every jurisdiction in the State. Furthermore, Note (v) levies a heavy 10% Land ASR surcharge on any parking '
        'exceeding requirements by more than 50%, while the January 2024 notification decrees that phased projects constructing full potential parking upfront must surrender '
        'unapplied bays to the local authority as free public parking if subsequent phases are delayed.'
    ),
    
    'amendment_cite': 'Notifications dt. 28-12-2022 / 12-01-2023 (Note vii: Two-wheeler freeze) & 12-01-2024 (Note v: Phased OC public surrender / 10% ASR)',
    
    'plain_summary_html': '''
<p>
  Once an architect calculates the raw base vehicular count from Table 8-B, Regulation 8.2.2 mandates applying the <strong>Geographic Multiplying Factor from Table 8-C</strong>. This reflects real-world transit densities: a residential project in rural Konkan or a small Nagar Panchayat does not require the same car-to-flat density as a tower in Pune or Thane.
</p>
<p>
  <strong>The 8-Tier City Multiplying Hierarchy (Table 8-C):</strong>
</p>
<ul class="rule-list">
  <li><strong>1.00 (No Reduction):</strong> Pune MC, Pimpri-Chinchwad MC (PCMC), Thane MC, and PCNTDA.</li>
  <li><strong>0.90 (10% Discount):</strong> Nagpur MC and Nashik MC.</li>
  <li><strong>0.80 (20% Discount):</strong> Other Municipal Corporations in Mumbai Metropolitan Region (MMR) (e.g., Navi Mumbai, Kalyan-Dombivli, Mira-Bhayandar, Vasai-Virar) and CIDCO NTDA areas.</li>
  <li><strong>0.70 (30% Discount):</strong> All remaining Municipal Corporations (e.g., Chhatrapati Sambhajinagar, Solapur, Amravati, Kolhapur), Metropolitan Authorities (PMRDA, NMRDA), and Special Planning Authorities (SPA).</li>
  <li><strong>0.60 (40% Discount):</strong> 'D' Class Municipal Corporations (outside MMR, e.g., Dhule, Jalgaon, Ahmednagar, Latur, Parbhani, Chandrapur) and 'A' Class Municipal Councils.</li>
  <li><strong>0.50 (50% Discount):</strong> 'B' Class and 'C' Class Municipal Councils.</li>
  <li><strong>0.40 (60% Discount):</strong> Nagar Panchayats, Non-Municipal Town DP areas, and Regional Plan (RP) rural areas.</li>
</ul>
<p>
  <strong>CRITICAL LEGAL TRAP — Note (vii) Two-Wheeler Non-Reduction:</strong>
  Under statutory Notification dt. 28-12-2022 and Corrigendum dt. 12-01-2023, <strong>Table 8-C factors SHALL NOT APPLY to Two-Wheeler parking for Multi-Family Residential</strong>. While four-wheeler parking in an RP area is discounted to 40%, two-wheeler residential stalls must be provided at the full 100% rate!
</p>
<p>
  <strong>Excess Parking Penalties &amp; Public Surrender (Note v &amp; Jan 2024 Notification):</strong>
  Providing luxury parking beyond 50% of the prescribed quota triggers a statutory financial penalty: <strong>10% of the prevailing Land Annual Statement of Rates (ASR)</strong> charged on the net footprint of the excess stalls (exempt for public, hospital, hotel, and school uses). If a developer builds full-potential parking in Phase 1 but fails to submit building proposals for subsequent phases before obtaining Phase 1 final OC, the surplus parking is <strong>deemed treated as Public Parking and surrendered to the Municipal Corporation free of cost</strong>!
</p>
''',

    'statutory_extract': r"""8.2.2 Off street parking requirement for various Planning Authorities / Areas
Off street parking requirement for various Planning Authorities / Areas shall be worked out by applying multiplying factor given in Table No.8-C below. This multiplying factor shall be applied to the total quantum of parking spaces worked out as per Table No.8-B above.

Table No.8-C:
1. Pune, Pimpri-Chinchwad and Thane Municipal Corporation area and PCNTDA area: Multiplying Factor = 1.00
2. Nagpur, Nashik Municipal Corporation area: Multiplying Factor = 0.9
3. Other Municipal Corporations in MMR area except Thane M.C., CIDCO as Planning Authority by Virtue of NTDA: Multiplying Factor = 0.8
4. Remaining Municipal Corporations not covered at Sr.No.1 to 3 and 5, Metropolitan Area Development Authority / Area Development Authority / SPA area: Multiplying Factor = 0.7
5. 'D' Class Municipal Corporation area except at Sr.No.3: Multiplying Factor = 0.6
6. 'A' Class Municipal Council area: Multiplying Factor = 0.6
7. 'B' and 'C' Class Municipal Council area: Multiplying Factor = 0.5
8. Nagar Panchayat, Non Municipal Town Development Plan area and areas in Regional Plan: Multiplying Factor = 0.4

Note -
i) After calculating the parking for entire building, multiplying factor given in Table 8-C shall be applied. Fraction of parking spaces more than 0.5 shall be rounded to next digit.

v) Parking more than 50% over and above stipulated in table 8-B and 8-C, shall be liable for payment of charges at the rate of 10% of land rate mentioned in the ASR without taking into account guidelines therein. Such charges shall be recovered on the area covered under car / scooter parking over and above the requirement. However, for public semi-public, hotel, hospital, educational buildings, such charges shall not be leviable.

(1) Parking requirement as stipulated in Table 8-B and Table 8-C, may be permitted for full permissible potential of the plot even though Building permission is sought for and sanctioned for only part of the full potential. In such cases the difference between number of parking required for such part potential and full permissible potential shall be liable for payment of charges as above, at the time of final occupancy certificate for such sanctioned permission,
Or
If the building permission proposal for the balance potential is not submitted before such final occupancy certificate, then such excess parking shall deemed to be treated as public parking and shall be handed over for the same purpose to the Authority free of cost.

vi) In case of plan for additional built-up area on existing building and where existing built-up is to be retained as per earlier sanction - off-street parking requirement (number of units) shall be calculated only for the newly proposed additional built-up area as per this regulation and existing parking area shall be retained as per approved plan. If the additional built-up area along with existing built-up area is proposed to be revised as per these regulations (UDCPR) then total parking requirement shall be calculated as per this regulation and existing parking units are to be deducted to arrive the new number of parking units required.

(1) vii) Multiplying factor as per regulation No.8.2.2, Table No.8-C shall not be applicable for Two Wheeler parking (2) for Sr.No.(i) - Multi Family residential of Sr.No.1 - Residential in Table No.8-B of Regulation No.8.2.1.""",

    'clause_cards_html': '''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>The 8-Tier City Factor</h4>
    </div>
    <div class="card-body">
      <p>Applies to the total quantum of Table 8-B spaces: <strong>1.00</strong> in Pune, PCMC &amp; Thane; <strong>0.90</strong> in Nagpur &amp; Nashik; <strong>0.80</strong> in MMR/CIDCO; <strong>0.70</strong> in PMRDA/NMRDA and other MCs; <strong>0.60</strong> in 'D' Class MCs &amp; 'A' Councils; <strong>0.50</strong> in 'B'/'C' Councils; <strong>0.40</strong> in Regional Plans &amp; Nagar Panchayats.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Residential Scooter Freeze (Note vii)</h4>
    </div>
    <div class="card-body">
      <p>By Notification dt. 28-12-2022 and 12-01-2023, <strong>Table 8-C does NOT apply to Two-Wheelers in Multi-Family Residential</strong>. Whether a residential building is in central Pune or a rural Regional Plan village, 100% of the Table 8-B scooter spaces must be provided without any fractional discount.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Excess Parking Surcharge (Note v)</h4>
    </div>
    <div class="card-body">
      <p>Any parking provided in excess of <strong>150% (50% over requirement)</strong> of the final statutory quota is liable to a cash penalty of <strong>10% of Land ASR rate</strong> calculated on the total stall area. Public/semi-public, hotels, hospitals, and educational buildings are strictly exempt from this charge.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Phased OC Public Surrender (Jan 2024)</h4>
    </div>
    <div class="card-body">
      <p>If full-potential parking is built upfront during a phased construction, the developer must submit sanction proposals for the balance phase before obtaining final OC for Phase 1. If not submitted, the surplus parking is <strong>deemed treated as public parking and surrendered to the Authority FREE OF COST</strong>, or surcharged @ 10% ASR.</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': '''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Sr.</th>
        <th>Planning Authority / Geographic Jurisdiction</th>
        <th>Multiplying Factor</th>
        <th>Applicability to Four-Wheelers</th>
        <th>Applicability to Res Two-Wheelers (Note vii)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong>PMC, PCMC, Thane MC, PCNTDA</strong></td>
        <td><code>1.00</code></td>
        <td>100% of Table 8-B</td>
        <td>100% (No reduction)</td>
      </tr>
      <tr>
        <td>2</td>
        <td><strong>Nagpur MC, Nashik MC</strong></td>
        <td><code>0.90</code></td>
        <td>90% of Table 8-B</td>
        <td>100% (Note vii freeze)</td>
      </tr>
      <tr>
        <td>3</td>
        <td><strong>MMR MCs (Navi Mumbai, KDMC, MBMC, VVMC) &amp; CIDCO</strong></td>
        <td><code>0.80</code></td>
        <td>80% of Table 8-B</td>
        <td>100% (Note vii freeze)</td>
      </tr>
      <tr>
        <td>4</td>
        <td><strong>Other MCs (Chh. Sambhajinagar, Solapur), PMRDA, NMRDA, SPAs</strong></td>
        <td><code>0.70</code></td>
        <td>70% of Table 8-B</td>
        <td>100% (Note vii freeze)</td>
      </tr>
      <tr>
        <td>5-6</td>
        <td><strong>'D' Class MCs (Dhule, Jalgaon, Latur, etc.) &amp; 'A' Class Councils</strong></td>
        <td><code>0.60</code></td>
        <td>60% of Table 8-B</td>
        <td>100% (Note vii freeze)</td>
      </tr>
      <tr>
        <td>7</td>
        <td><strong>'B' and 'C' Class Municipal Councils</strong></td>
        <td><code>0.50</code></td>
        <td>50% of Table 8-B</td>
        <td>100% (Note vii freeze)</td>
      </tr>
      <tr>
        <td>8</td>
        <td><strong>Nagar Panchayats, Non-Municipal Town DPs &amp; Regional Plan Areas</strong></td>
        <td><code>0.40</code></td>
        <td>40% of Table 8-B</td>
        <td>100% (Note vii freeze)</td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>COMPARATIVE MULTI-CITY AUDIT: TABLE 8-C FACTOR &amp; NOTE (VII) DYNAMICS</h4>
  <p><strong>Common Project:</strong> A residential layout of 100 flats of $90\text{ sq.m}$ carpet each ($80-150\text{ sq.m}$ bracket) located in two different jurisdictions:</p>
  <ul>
    <li><strong>Location A:</strong> Pune Municipal Corporation (PMC) [Factor = 1.00]</li>
    <li><strong>Location B:</strong> PMRDA / Solapur MC [Factor = 0.70]</li>
    <li><strong>Location C:</strong> Alibaug Regional Plan Area [Factor = 0.40]</li>
  </ul>
  
  <div class="step-box">
    <strong>Step 1: Raw Table 8-B Base Calculation</strong>
    <ul>
      <li>$100\text{ flats} \times 1\text{ car} = 100\text{ cars}$. Visitor: $100 \times 0.05 = 5\text{ cars}$. <strong>Total Base Cars = 105</strong>.</li>
      <li>$100\text{ flats} \times 1\text{ scooter} = 100\text{ scooters}$. Visitor: $100 \times 0.05 = 5\text{ scooters}$. <strong>Total Base Scooters = 105</strong>.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Location A - Pune Municipal Corporation (Factor 1.00)</strong>
    <ul>
      <li>Cars: $105 \times 1.00 = \mathbf{105\text{ Cars}}$.</li>
      <li>Scooters: $105 \times 1.00 = \mathbf{105\text{ Scooters}}$.</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Location B - PMRDA / Solapur MC (Factor 0.70)</strong>
    <ul>
      <li>Cars: $105 \times 0.70 = 73.5 \rightarrow \mathbf{74\text{ Cars}}$ (Note i: $>0.5$ rounds up to 74).</li>
      <li>Scooters: Under Note (vii), <em>Table 8-C factor does not apply to multi-family residential two-wheelers</em>!</li>
      <li>Mandatory Scooters: $105 \times 1.00 = \mathbf{105\text{ Scooters}}$ (NOT $105 \times 0.70 = 74$).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 4: Location C - Regional Plan Area (Factor 0.40)</strong>
    <ul>
      <li>Cars: $105 \times 0.40 = \mathbf{42\text{ Cars}}$ (60% car reduction!).</li>
      <li>Scooters: Under Note (vii), factor 0.40 is legally void for residential scooters.</li>
      <li>Mandatory Scooters: Still exactly $\mathbf{105\text{ Scooters}}$!</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 5: Excess Parking Surcharge Scenario (Note v)</strong>
    <p>Suppose the developer in Location B (PMRDA, requiring 74 cars) provides <strong>140 cars</strong> to market luxury amenities:</p>
    <ul>
      <li>Allowable buffer without fee (up to 150%): $74 \times 1.50 = 111\text{ cars}$.</li>
      <li>Excess over 150%: $140 - 111 = 29\text{ excess cars}$.</li>
      <li>Stall area penalized: $29 \times 12.50\text{ m}^2 = 362.50\text{ m}^2$.</li>
      <li>If prevailing Land ASR is ₹40,000 / sq.m:</li>
      <li><strong>Mandatory Cash Surcharge:</strong> $362.50\text{ m}^2 \times (10\% \text{ of ₹40,000}) = 362.50 \times ₹4,000 = \mathbf{₹14,50,000}$.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': '''
<div class="alert-box alert-warning">
  <h4>HIGH-STAKE STATUTORY PENALTY TRAPS</h4>
  <ul class="warning-list">
    <li><strong>Illegally Discounting Residential Scooters:</strong> Software tools or architects unaware of the 2022/2023 amendment still apply the 0.70 or 0.40 factor to residential scooters. Scrutiny software (BPAMS) will immediately flag a "Deficit Two-Wheeler Parking" objection and halt building permission.</li>
    <li><strong>Forfeiting Free Public Parking in Phased Schemes:</strong> Under the Jan 2024 amendment, building a 5-level multi-storey car park for a 4-phase master plan during Phase 1 without submitting Phase 2/3/4 sanction files before Phase 1 final OC results in the Municipal Corporation confiscating the excess bays as <em>free public parking</em>.</li>
    <li><strong>Disregarding the 10% ASR Surcharge on Luxury Parking:</strong> If client marketing demands 2 cars per flat in a mid-segment scheme where the statute only requires 0.7 cars, the developer must budget for the 10% Land ASR surcharge on all bays exceeding 150% of the statutory requirement.</li>
    <li><strong>Rounding Errors:</strong> Note (i) specifies that only fractions <em>strictly greater than 0.5</em> round to the next digit. A calculated car quota of 42.49 rounds down to 42, but 42.51 rounds up to 43.</li>
  </ul>
</div>
''',

    'amendment_section_html': '''
<div class="amendment-card">
  <h4>Statutory History &amp; Landmark Parking Reforms</h4>
  <p><strong>Notification No. CR 236/18 (Part 4) dt. 28-12-2022 &amp; Corrigendum dt. 12-01-2023:</strong></p>
  <p>Inserted Note (vii) providing that the Table 8-C discount factor does not apply to two-wheeler parking for Multi-Family Residential. This was introduced after municipal corporations outside Pune/MMR reported catastrophic on-street two-wheeler congestion caused by developers discounting scooter bays by 30% to 60%.</p>
  <p><strong>Notification No. CR 97/2023/UD-13 dt. 12-01-2024:</strong></p>
  <p>Substituted Note (v) to address developer speculation in phased developments. It established that surplus parking built upfront must either be matched with immediate phased expansion filings before final OC or be formally surrendered to the Authority as free public parking.</p>
</div>
''',

    'quiz': [
      {
        'question': 'What is the Table 8-C multiplying factor for Nagpur and Nashik Municipal Corporation areas?',
        'options': [
          '1.00',
          '0.90',
          '0.80',
          '0.70'
        ],
        'answer': 1,
        'explanation': 'Table 8-C Item 2 specifies a Multiplying Factor of 0.9 for Nagpur, Nashik Municipal Corporation area.'
      },
      {
        'question': 'Under Note (vii) of Regulation 8.2.2 (inserted 2022/2023), which type of parking is strictly EXEMPT from Table 8-C discount factors?',
        'options': [
          'Four-wheeler parking in IT parks',
          'Two-wheeler parking for Multi-Family Residential',
          'Commercial mall loading berths',
          'Hospital ambulance spaces'
        ],
        'answer': 1,
        'explanation': 'Note (vii) unambiguously decrees that "Multiplying factor as per regulation No.8.2.2, Table No.8-C shall not be applicable for Two Wheeler parking for Sr.No.(i) - Multi Family residential."'
      },
      {
        'question': 'What surcharge is levied under Note (v) when parking is provided more than 50% over and above the statutory requirement?',
        'options': [
          '5% of ASR land rate',
          '10% of land rate mentioned in the ASR on the excess stall area',
          '20% scrutiny fee premium',
          'Flat Rs 50,000 per excess car stall'
        ],
        'answer': 1,
        'explanation': 'Note (v) mandates that parking more than 50% over requirement "shall be liable for payment of charges at the rate of 10% of land rate mentioned in the ASR... on the area covered under car / scooter parking over and above the requirement."'
      },
      {
        'question': 'Under the January 2024 amendment to Note (v), what happens if full potential parking is built in Phase 1, but balance potential proposals are NOT submitted before final OC?',
        'options': [
          'The entire building permission is cancelled',
          'The excess parking is sealed by the Fire Department',
          'The excess parking is deemed treated as public parking and handed over to the Authority free of cost (or pays 10% ASR)',
          'The developer is forced to convert it into residential flats'
        ],
        'answer': 2,
        'explanation': 'The 12th January 2024 amendment dictates that if the balance proposal is not submitted before final OC, "such excess parking shall deemed to be treated as public parking and shall be handed over for the same purpose to the Authority free of cost."'
      }
    ],

    'prev_url': '/lessons/reg-8-2-off-street-parking-matrix-and-residential-norms.html',
    'prev_title': 'Reg 8.2 & Table 8-B: Off-Street Parking Matrix & Tenement Tiers',
    'next_url': '/lessons/reg-9-1-room-dimensions-and-height-clearances.html',
    'next_title': 'Reg 9.1 to 9.8: Plinth Standards, Room Heights, Sanitary Sizes & Mezzanines'
}
