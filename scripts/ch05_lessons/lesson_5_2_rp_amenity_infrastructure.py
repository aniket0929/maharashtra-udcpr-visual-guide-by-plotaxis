"""
UDCPR Visual Guide - CHAPTER 5: LESSON 5.2
Module: scripts/ch05_lessons/lesson_5_2_rp_amenity_infrastructure.py
Governing Regulations: Regulations 5.1.3 to 5.1.9 & 5.11 (Committed Development, Errors, Station Areas, RP Amenity, Board of Appeals)
"""

lesson_data = {
    'filename': 'reg-5-1-8-rp-amenity-and-infrastructure.html',
    'lesson_id': 'lesson-reg-5-2',
    'quiz_id': 'quiz-reg-5-2',
    'clause': 'Reg. 5.1.3 – 5.1.9 & 5.11',
    'title': 'Committed Development, Station Belts & RP Amenity Space',
    'badge_status': 'Core Infrastructure',
    'ch_slug': 'ch05',
    'ch_title': 'Chapter 5: Regional Plan Areas',
    'meta_desc': 'UDCPR Regional Plan infrastructure rules under Reg 5.1.3 to 5.1.9: Committed development grandfathering, 10% RP amenity space on plots >4,000 sqm, 500m railway station zones, and Board of Appeals.',
    'lead_summary': 'Learn the administrative and infrastructure framework governing Regional Plan layouts across Maharashtra: protecting grandfathered layouts through Committed Development (Reg. 5.1.3), the 10% amenity space surrender threshold on plots exceeding 4,000 sq.m, the 500m high-density railway station development radius, and appealing collector decisions under Regulation 5.11.',
    'amendment_cite': 'CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        Unlike municipal corporations with dense municipal staff, Regional Plan areas are administered through District Collectorates and Town Planning Branch Offices. Regulations 5.1.3 to 5.1.9 and 5.11 establish the operating rules for grandfathered approvals, public amenities, and rural transit corridors.
      </p>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">1. Committed Development Grandfathering (Reg. 5.1.3)</h4>
      <p style="margin-bottom:10px; font-size:0.92rem; color:var(--ink-soft);">
        When a new Regional Plan is published, what happens to previously sanctioned agricultural conversions and layout approvals?
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; font-size:0.92rem; color:var(--ink-soft);">
        <li><strong>Full Validity:</strong> Any layout approval or N.A. permission recommended or granted prior to draft RP publication remains 100% legally valid.</li>
        <li><strong>Owner's Choice:</strong> The owner can either:
          <br>a) Continue with the permission <strong>in-toto</strong> under the earlier rules; OR
          <br>b) Apply for revised permissions under UDCPR <strong>without paying any premium</strong> for previously approved areas!</li>
      </ul>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">2. Amenity Space in Regional Plan Areas (Reg. 5.1.8)</h4>
      <div style="background:var(--paper); border:1px solid var(--line-strong); padding:16px; margin-bottom:16px;">
        <p style="font-size:0.92rem; color:var(--ink); margin-bottom:8px;">
          <strong>Statutory Amenity Threshold:</strong> In any residential layout or subdivision in an RP area:
        </p>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11.5px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Gross Plot Area (excluding RP roads)</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Amenity Space Required</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Compensation &amp; Surrender Rights</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Up to 4,000 sq.m (0.40 Ha)</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">NIL (0%)</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">100% buildable residential plots</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">More than 4,000 sq.m</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700; color:var(--blueprint);">10% of Land Area</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Owner can develop approved amenities or surrender for 100% in-situ FSI/TDR</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">3. Railway Station Area Development (Reg. 5.1.6)</h4>
      <p style="margin-bottom:10px; font-size:0.92rem; color:var(--ink-soft);">
        To foster rural connectivity, agricultural land within <strong>500 meters of any functional railway station</strong> may be developed upon paying a <strong>30% ASR premium</strong>:
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:6px; font-size:0.92rem; color:var(--ink-soft);">
        <li><strong>Inner 100m Periphery:</strong> Only transit-oriented and commercial uses (no residential).</li>
        <li><strong>Outer 100m to 500m Belt:</strong> Full residential and mixed-use development permitted.</li>
      </ul>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">4. Board of Appeals (Reg. 5.11)</h4>
      <p style="font-size:0.92rem; color:var(--ink-soft);">
        Any developer aggrieved by an arbitrary sanction rejection or premium demand by the District Collector or Town Planning Office can lodge a statutory appeal before the <strong>Board of Appeals (Divisional Commissioner)</strong> for quasi-judicial review.
      </p>
    """,
    'statutory_extract': "5.1.3 Committed Development: Any development permission granted or any proposal for which approval has been recommended before publication of draft R.P. shall continue to be valid for that respective purpose... it shall be permissible for owner either continue with permission in toto or apply for revised permissions under these regulations without premium... 5.1.8 Provision of Amenity Space: In any layout for residential purpose: upto 4000 sq.m: Nil; more than 4000 sq.m: 10%... 5.1.6 Station Area Development: Development in agriculture zone around functional railway station upto 500m permitted by charging premium at 30% of ASR.",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 5.1.8 // 10% AMENITY</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">4,000 sq.m Cutoff</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Plots &le; 4,000 sq.m are completely exempt from amenity space surrender in RP areas. Above 4,000 sq.m, 10% must be earmarked with full in-situ FSI credit.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 5.1.6 // STATION RADIUS</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">500m Transit Hub</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Unlocks agricultural lands within 500m of railway stations into vibrant commercial and residential hubs on paying 30% ASR premium.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_022 // RP AMENITY &amp; COMMITTED APPROVAL SPECIFICATION</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">CHAPTER 5 INFRASTRUCTURE</span>
        </div>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11.5px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Regulatory Mechanism</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Governing Clause</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Threshold / Percentage</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Statutory Relief / Rights</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Committed Development</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 5.1.3</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">Pre-RP approvals</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Grandfathered in-toto or revised under UDCPR without premium</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>RP Amenity Space</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 5.1.8</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">10% on &gt; 4000 sqm</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">100% In-situ compensatory FSI or TDR upon handover</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Station Area Development</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 5.1.6</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">500m radius</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">30% ASR premium; commercial inside 100m, residential in 500m</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Draftsman Error Correction</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 5.1.4</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">District Collector</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Rectified with prior approval of Divisional Joint Director TP</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Board of Appeals</strong></td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Reg. 5.11</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">Div. Commissioner</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Quasi-judicial redressal against Collector / Authority orders</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': r"""
      <p style="margin-bottom:12px;">
        <strong>Practical Scrutiny Problem:</strong> An owner holds a <strong>15,000 sq.m</strong> land parcel in a Regional Plan residential layout. 1,000 sq.m is affected by an RP road widening line.
      </p>
      <div class="worked-step">
        <span class="step-badge">NET AMENITY BASE</span>
        <div>
          Gross plot area = 15,000 sq.m.
          <br>Deduct RP road widening = 1,000 sq.m.
          <br>Net base area for amenity calculation = <strong>14,000 sq.m</strong>.
          <br>Because $14,000\text{ sq.m} > 4,000\text{ sq.m}$, the plot triggers the 10% amenity requirement under Reg. 5.1.8.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">AMENITY SURRENDER &amp; FSI CREDIT</span>
        <div>
          Amenity Space required = $14,000 \times 10\% = \mathbf{1,400\text{ sq.m}}$.
          <br>The developer surrenders the 1,400 sq.m amenity parcel to the Collectorate for a public primary school.
          <br><strong>FSI Benefit:</strong> Full 1,400 sq.m is credited back as <strong>In-Situ FSI</strong> for utilization across the remaining 12,600 sq.m plotted layout!
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ STATUTORY COMPLIANCE: 1,400 sqm amenity surrendered with 100% compensatory FSI credit.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Demanding Amenity Space on Plots Below 4,000 sq.m</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Under municipal corporation rules (Reg. 3.5), amenity space triggers above 20,000 sq.m. But in Regional Plan areas (Reg. 5.1.8), the table clearly establishes: <em>"upto 4000 sq.m. : Nil"</em>. Plots below 4,000 sq.m in RP areas do not surrender any amenity space.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Re-charging Premium on Previously Sanctioned N.A. Layouts</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          When an architect applies to revise a pre-existing layout to incorporate UDCPR building norms, scrutiny officers often re-levy gaothan expansion or conversion premiums. Regulation 5.1.3(i) categorically bans this: <em>"the premium, if any, shall not be applicable, for approved permissions"</em>.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Station Area Premium &amp; In-situ Amenity FSI</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Clarified that 30% premium applies around functional railway stations in agricultural zones, and harmonized the in-situ FSI transfer mechanism for surrendered RP amenity spaces with Chapter 11 TDR rules.
      </p>
    """,
    'quiz': [
      {
        'question': 'Under Regulation 5.1.8, what is the amenity space requirement for a residential layout of 3,500 sq.m in a Regional Plan area?',
        'options': [
          '5%',
          '10%',
          '15%',
          'Nil (0%)'
        ],
        'correctAnswer': 3,
        'explanation': 'Under Regulation 5.1.8, layouts up to 4,000 sq.m in Regional Plan areas are completely exempt from amenity space surrender (Nil).'
      },
      {
        'question': 'What is the permissible development radius around a functional railway station in an agricultural zone under Regulation 5.1.6?',
        'options': [
          '100 meters',
          '200 meters',
          '500 meters',
          '1,000 meters'
        ],
        'correctAnswer': 2,
        'explanation': 'Under Regulation 5.1.6, development in agricultural zones is permissible up to a distance of 500 meters around any functional railway station upon payment of 30% ASR premium.'
      },
      {
        'question': 'If a landowner with a pre-RP approved layout applies for revised permission under UDCPR, is conversion premium payable under Regulation 5.1.3?',
        'options': [
          'Yes, full 15% premium must be paid',
          'No, premium shall not be applicable for previously approved permissions',
          '50% premium is payable',
          'Only scrutiny fees are waived'
        ],
        'correctAnswer': 1,
        'explanation': 'Under Regulation 5.1.3(i), in cases of revised permissions for grandfathered approvals, premium shall not be applicable for already approved permissions.'
      }
    ],
    'prev_url': '/lessons/reg-5-1-gaothan-expansion-scheme.html',
    'prev_title': 'Reg. 5.1.1 Gaothan Expansion',
    'next_url': '/lessons/reg-5-3-konkan-coastal-regional-plans.html',
    'next_title': 'Reg. 5.3 & 5.7 Konkan & Coastal Plans'
}
