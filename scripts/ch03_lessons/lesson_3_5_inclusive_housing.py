"""
UDCPR Visual Guide - CHAPTER 3: LESSON 3.5
Module: scripts/ch03_lessons/lesson_3_5_inclusive_housing.py
Governing Regulation: Regulation 3.8 (Provision for Inclusive Housing)
Covers: Reg 3.8.1 to 3.8.4 - 4,000 sq.m threshold in Municipal Corporations, 20% Basic FSI quota for EWS/LIG, carpet area limits (30.0 to 45.0 sq.m), 3 implementation pathways, and 25% incentive FSI.
"""

lesson_data = {
    'filename': 'reg-3-8-inclusive-housing.html',
    'lesson_id': 'lesson-reg-3-8',
    'quiz_id': 'quiz-reg-3-8',
    'clause': 'Reg. 3.8',
    'title': 'Inclusive Housing (20% Affordable EWS/LIG Quota)',
    'badge_status': 'Social Housing Mandate',
    'ch_slug': 'ch03',
    'ch_title': 'Chapter 3: General Land Development',
    'meta_desc': 'Inclusive Housing regulations under UDCPR 3.8: 4,000 sq.m plot threshold in Municipal Corporations, 20% Basic FSI quota for EWS/LIG, tenement carpet sizes (30 to 45 sq.m), 3 implementation options, and 25% incentive FSI.',
    'lead_summary': 'Learn Maharashtra\'s statutory mandate for affordable housing under Regulation 3.8: the 4,000 sq.m plot threshold across Municipal Corporations, calculating the mandatory 20% Basic FSI quota for EWS/LIG families, tenement carpet area limits (30.0 to 45.0 sq.m), the three implementation pathways (constructed handover, independent wing, or 10% land surrender), and developer incentive FSI entitlements.',
    'amendment_cite': 'CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        To prevent socio-spatial segregation and address Maharashtra's urban housing shortage, Regulation 3.8 mandates that large private residential developments reserve a substantial proportion of their built area for Economically Weaker Sections (EWS) and Lower Income Groups (LIG).
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:10px; color:var(--ink-soft);">
        <li><strong>Statutory Applicability Threshold (Reg. 3.8.2):</strong> Mandatory for any land sub-division, plotted layout, or group housing scheme on a gross plot area of <strong>4,000 sq.m or more</strong> within all <strong>Municipal Corporation limits</strong> across Maharashtra.</li>
        <li><strong>Mandatory Affordable Quota (Reg. 3.8.2):</strong> Exactly <strong>20% of the Basic FSI</strong> constructed area must be provided for affordable EWS / LIG housing.</li>
        <li><strong>Statutory Tenement Carpet Area:</strong> Each inclusive housing tenement must have a finished carpet area between <strong>30.0 sq.m and 45.0 sq.m</strong> (maximum 45.0 sq.m).</li>
        <li><strong>Three Statutory Implementation Pathways (Reg. 3.8.2):</strong>
          <ol style="padding-left:18px; margin-top:4px; display:flex; flex-direction:column; gap:4px;">
            <li><strong>Path 1: Handover to MHADA / Authority:</strong> Constructed tenements are transferred to MHADA or the Planning Authority at the prevailing ASR construction rate. MHADA distributes them to eligible EWS/LIG citizens via transparent computerized lottery.</li>
            <li><strong>Path 2: Developer Sells on Direct Lottery:</strong> The developer constructs the 20% tenements in an independent wing or building and sells them directly to eligible EWS/LIG buyers on a lottery basis supervised by the municipal housing committee.</li>
            <li><strong>Path 3: Land Surrender Option (in Plotted Layouts):</strong> The owner surrenders <strong>10% of the gross layout land</strong> to MHADA / Planning Authority free of cost for developing independent affordable housing schemes.</li>
          </ol>
        </li>
        <li><strong>Developer Incentive FSI (Reg. 3.8.3):</strong> To encourage robust participation and offset subsidization costs:
          <div style="background:var(--paper); border:1px solid var(--blueprint); border-left:4px solid var(--blueprint); padding:10px 14px; margin:6px 0; font-family:var(--mono); font-size:0.85rem; color:var(--blueprint);">
            "In addition to basic entitlement he shall be entitled for, additional 25% FSI of the land covered under Inclusive Housing on his remaining land."
          </div>
        </li>
        <li><strong>Auctioned Plots Safeguard (Reg. 3.8.4):</strong> Inclusive housing does not apply retrospectively to public land parcels auctioned without this condition prior to UDCPR-2020. However, all subsequent municipal land auctions must incorporate this condition.</li>
      </ul>
    """,
    'statutory_extract': "3.8.2 Inclusive Housing: For the sub-division or layout of the land admeasuring 4000 sq.m. or more for residential purpose and group housing scheme having plot area 4000 sq.m. or more... provision for inclusive housing shall be mandatory... to the extent of 20% of the basic FSI... carpet area of the tenement shall be 30.0 to 45.0 sq.m... 3.8.3 If owner / developer desires to construct inclusive housing... in addition to basic entitlement he shall be entitled for, additional 25% FSI of the land covered under Inclusive Housing on his remaining land...",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 3.8.2 // 20% BASIC FSI QUOTA</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Affordable Carpet Standards</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            20% of the basic permissible FSI must be designed as self-contained residential flats between <strong>30.0 sq.m and 45.0 sq.m</strong> RERA carpet area, with individual toilet and water connections.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 3.8.3 // 25% INCENTIVE FSI</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Developer Bonus</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            The developer is rewarded with an <strong>extra 25% FSI</strong> calculated on the proportionate land footprint utilized for the inclusive housing units, loadable directly onto market-sale towers.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_017 // INCLUSIVE HOUSING STATUTORY COMPLIANCE FLOWCHART</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 3.8 BLUEPRINT PLATE</span>
        </div>
        <div style="padding:14px; font-family:var(--mono); font-size:11.5px; line-height:1.8; color:var(--ink);">
          GROSS RESIDENTIAL PLOT AREA &ge; 4,000 SQ.M IN MUNICIPAL CORPORATION<br>
          &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr;<br>
          CALCULATE STATUTORY QUOTA = 20% OF BASIC PERMISSIBLE FSI<br>
          &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr;<br>
          TENEMENT SIZING SPECIFICATION: 30.0 SQ.M &le; CARPET AREA &le; 45.0 SQ.M<br>
          &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr;<br>
          CHOOSE ONE OF THREE STATUTORY IMPLEMENTATION PATHWAYS (&sect; 3.8.2):<br>
          ├── [OPTION A] Construct tenements &amp; transfer to MHADA / Authority at ASR construction rate<br>
          ├── [OPTION B] Construct in independent wing &amp; allot to EWS/LIG via supervised lottery<br>
          └── [OPTION C] Surrender 10% gross land area to MHADA / Authority (plotted layouts only)<br>
          &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&darr;<br>
          DEVELOPER INCENTIVE CLAIM (&sect; 3.8.3): Receive +25% Incentive FSI on remaining land!
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="margin-bottom:12px;">
        <strong>Numerical Case Study:</strong> A developer proposes a residential group housing project on a <strong>6,000 sq.m plot</strong> in Thane Municipal Corporation. Basic FSI in the zone is <strong>1.10</strong>.
      </p>
      <div class="worked-step">
        <span class="step-badge">APPLICABILITY</span>
        <div>
          Plot size = 6,000 sq.m &ge; 4,000 sq.m in Municipal Corporation.
          <br><span style="font-family:var(--mono); color:var(--blueprint);">&#10003; INCLUSIVE HOUSING MANDATORY under Reg. 3.8.2.</span>
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">20% QUOTA CALCULATION</span>
        <div>
          Total Basic FSI BUA = 6,000 sq.m &times; 1.10 = <strong>6,600 sq.m BUA</strong>.
          <br><span style="font-family:var(--mono);">Mandatory Inclusive Housing BUA = 20% of 6,600 sq.m = <strong>1,320 sq.m</strong>.</span>
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">TENEMENT ALLOCATION</span>
        <div>
          The developer designs 1BHK units of <strong>33 sq.m carpet area</strong> (approx 40 sq.m BUA with walls/circulations).
          <br><span style="font-family:var(--mono);">Number of EWS/LIG Tenements = 1,320 sq.m / 40 sq.m = <strong>33 Tenements</strong>.</span>
          <br>These 33 units are grouped in a dedicated Wing 'C' with independent staircase and lift.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">INCENTIVE FSI BONUS</span>
        <div>
          Under Reg. 3.8.3, the developer earns an additional <strong>25% Incentive FSI</strong> on the land footprint of the inclusive wing (approx 300 sq.m extra FSI) loadable onto luxury Towers A &amp; B.
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ STATUTORY COMPLIANCE: 33 EWS/LIG families gain permanent urban housing and the developer secures incentive FSI.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Designing Tenements with Carpet Area Larger than 45.0 sq.m</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Regulation 3.8.2 specifies that the carpet area of inclusive housing tenements must strictly be between <strong>30.0 and 45.0 sq.m</strong>. Designing 52 sq.m or 60 sq.m units will be disqualified by MHADA / municipal scrutiny squads, voiding the inclusive housing quota compliance.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Attempting to Scatter Inclusive Units Across Luxury Penthouse Floors</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          MHADA and local authorities require inclusive tenements to be concentrated in an independent wing or separate vertical stack with separate entrance/lift access or independent building. This prevents maintenance fee disputes between luxury owners and EWS/LIG residents.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 3: Claiming Exemption by Artificially Subdividing Plots into 3,900 sq.m Parcels</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Subdividing an 8,000 sq.m parcel into two 4,000 sq.m plots to evade inclusive housing is prohibited under the anti-fragmentation provisions of the MRTP Act. The 4,000 sq.m threshold is evaluated on the original continuous holding.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Inclusive Housing Pricing &amp; MHADA Handover</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Clarified the valuation formula for tenements surrendered to MHADA under Option A, basing compensation on the prevailing ASR construction cost schedule and streamlining the computerized public allotment lottery.
      </p>
    """,
    'quiz': [
        {
            'question': 'What is the minimum gross plot area threshold in Municipal Corporations that makes Inclusive Housing mandatory under Reg. 3.8.2?',
            'options': [
                '1,000 sq.m or more',
                '2,000 sq.m or more',
                '4,000 sq.m or more',
                '10,000 sq.m or more'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.8.2 explicitly stipulates that for sub-division or layout or group housing having a plot area of '4000 sq.m. or more', provision for inclusive housing is mandatory in Municipal Corporations."
        },
        {
            'question': 'What percentage of the Basic FSI must be reserved for Inclusive Housing (EWS/LIG) under Regulation 3.8.2?',
            'options': [
                '5% of Basic FSI',
                '10% of Basic FSI',
                '20% of Basic FSI',
                '35% of Basic FSI'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.8.2 provides that inclusive housing must be provided 'to the extent of 20% of the basic FSI'."
        },
        {
            'question': 'What is the statutory carpet area range for an Inclusive Housing tenement under Regulation 3.8.2?',
            'options': [
                '15.0 to 25.0 sq.m',
                '30.0 to 45.0 sq.m',
                '50.0 to 65.0 sq.m',
                'Any size chosen by the developer'
            ],
            'correctAnswer': 1,
            'explanation': "Regulation 3.8.2 mandates that the 'carpet area of the tenement shall be 30.0 to 45.0 sq.m'."
        },
        {
            'question': 'What additional incentive FSI is granted to the developer under Regulation 3.8.3 for providing Inclusive Housing?',
            'options': [
                'No incentive FSI is granted',
                'Additional 10% FSI of the inclusive housing land',
                'Additional 25% FSI of the land covered under Inclusive Housing on the remaining land',
                'Double FSI for the whole layout'
            ],
            'correctAnswer': 2,
            'explanation': "Regulation 3.8.3 explicitly entitles the developer to 'additional 25% FSI of the land covered under Inclusive Housing on his remaining land'."
        }
    ],
    'prev_url': '/lessons/reg-3-5-amenity-space-provision.html',
    'prev_title': 'Reg. 3.5 Amenity Space',
    'next_url': '/lessons/reg-3-9-net-plot-area-computation.html',
    'next_title': 'Reg. 3.9 Net Plot Computation'
}
