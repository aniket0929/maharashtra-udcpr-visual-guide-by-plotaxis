"""
UDCPR FROM SCRATCH - CHAPTER 4: LESSON 4.6
Module: scripts/ch04_lessons/lesson_4_6_public_semi_public_dp_reservations.py
Governing Regulations: Regulations 4.10, 4.26, and 4.27 (Public / Semi-Public Zone & DP Reservations)
"""

lesson_data = {
    'filename': 'reg-4-27-public-semi-public-and-dp-reservations.html',
    'lesson_id': 'lesson-reg-4-6',
    'quiz_id': 'quiz-reg-4-6',
    'clause': 'Reg. 4.10 & 4.27',
    'title': 'Public / Semi-Public Zones & Development Plan (DP) Reservations',
    'badge_status': 'Core Public Infrastructure',
    'ch_slug': 'ch04',
    'ch_title': 'Chapter 4: Land Use Classification & Permissible Uses',
    'meta_desc': 'Statutory rules for Public/Semi-Public Zones (Reg. 4.10) and development inside DP Reservations (Reg. 4.27): 15% ancillary commercial allowance, sports complexes, playgrounds, markets, and town halls.',
    'lead_summary': 'Learn the regulatory rules governing civic, governmental, and social infrastructure plots under UDCPR Regulations 4.10 and 4.27: institutional campuses in Public/Semi-Public zones, the statutory 15% ancillary commercial area allowance, and permissible construction inside Development Plan (DP) reservations like playgrounds, stadiums, schools, and municipal markets.',
    'amendment_cite': 'CR.121/21',
    'plain_summary_html': """
      <p style="margin-bottom:14px;">
        Civic amenities, hospitals, educational campuses, and civic reservations form the backbone of a city's public life. Regulations 4.10 and 4.27 regulate how Public / Semi-Public (P/SP) zones and statutory Development Plan (DP) reservations are developed.
      </p>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">1. Public / Semi-Public Zone (P/SP Zone) (Reg. 4.10)</h4>
      <p style="margin-bottom:10px; font-size:0.92rem; color:var(--ink-soft);">
        P/SP zones are earmarked for civic, social, institutional, and governmental functions:
      </p>
      <ul style="padding-left:20px; display:flex; flex-direction:column; gap:8px; font-size:0.92rem; color:var(--ink-soft);">
        <li>Schools, colleges, universities, and specialized training institutes.</li>
        <li>Hospitals, clinics, dispensaries, and sanatoriums.</li>
        <li>Government offices, municipal town halls, courts, and civil defence centers.</li>
        <li>Cultural centers, museums, public libraries, auditoriums, and exhibition halls.</li>
        <li>Social welfare institutions, orphanages, old age homes, and destitute centers.</li>
        <li>Public utilities: water treatment plants, electrical sub-stations, and sewage pumping stations.</li>
      </ul>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">2. The 15% Ancillary Commercial Allowance (Reg. 4.10(vi))</h4>
      <div style="background:var(--paper); border:1px solid var(--line-strong); padding:16px; margin-bottom:16px;">
        <p style="font-size:0.92rem; color:var(--ink); margin-bottom:8px;">
          <strong>Commercial Cross-Subsidization Rule:</strong> In educational, medical, and institutional campuses located in Public/Semi-Public zones, up to <strong>15% of the basic FSI</strong> may be utilized for ancillary commercial purposes to support the main institution.
        </p>
        <ul style="padding-left:18px; font-size:0.86rem; color:var(--ink-soft); display:flex; flex-direction:column; gap:4px;">
          <li>Permissible commercial uses: canteens, cafeterias, student bookshops, stationery stores, banks/ATMs, and medical pharmacies.</li>
          <li>Such commercial premises must be primarily integrated into the campus to serve students, staff, and visitors.</li>
        </ul>
      </div>

      <h4 style="font-family:var(--disp); font-size:1rem; margin:16px 0 8px; color:var(--ink);">3. Uses Permissible in Development Plan (DP) Reservations (Reg. 4.27)</h4>
      <div style="overflow-x:auto; margin-bottom:16px;">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>DP Reservation Category</th>
              <th>Statutory Permissible Built Uses</th>
              <th>Ground Coverage / Height Restrictions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="font-weight:600;">Playground (PG) / Garden</td>
              <td>Pavilion, gymnasia, watchman cabin, club facilities, changing rooms, public conveniences.</td>
              <td>Max <strong>15% ground coverage</strong> (FSI 0.15), single or Ground + 1 storey. Remaining 85% must remain completely open green space.</td>
            </tr>
            <tr style="background:var(--paper);">
              <td style="font-weight:600;">Stadium / Sports Complex</td>
              <td>Indoor sports halls, swimming pools, spectator stands, sports hostels, and <strong>commercial shops underneath stadium stands</strong>.</td>
              <td>Commercial shops under stands permitted up to <strong>15% of total built-up area</strong> to fund sports facility maintenance.</td>
            </tr>
            <tr>
              <td style="font-weight:600;">Municipal Market / Shopping Center</td>
              <td>Retail vegetable/meat stalls, cold storage rooms, public conveniences, administrative office.</td>
              <td>Subject to full commercial FSI under Table 6-A with designated delivery truck bays.</td>
            </tr>
            <tr style="background:var(--paper);">
              <td style="font-weight:600;">Town Hall / Cultural Complex</td>
              <td>Auditorium, drama theatre, art exhibition gallery, city archives, public library, meeting halls.</td>
              <td>Full FSI with mandatory assembly hall fire clearances and 1:10 accessible ramps.</td>
            </tr>
            <tr>
              <td style="font-weight:600;">Truck Terminus / Transport Hub</td>
              <td>Freight loading bays, transit warehouses, drivers' rest quarters, canteen, repair garage, EV charging stations.</td>
              <td>Min road width 18.0m. Fueling stations permissible as ancillary use.</td>
            </tr>
          </tbody>
        </table>
      </div>
    """,
    'statutory_extract': "4.10 PUBLIC / SEMI PUBLIC ZONE: The following uses shall be permissible in Public / Semi-public Zone: i) Schools, Colleges, Educational Complex... ii) Hospitals, Dispensaries... vi) In case of educational, medical and institutional use, 15% area may be used for commercial purpose... 4.27 USES PERMISSIBLE IN DEVELOPMENT PLAN RESERVATIONS: a) Play Ground / Garden / Park - Pavilion, Gymnasia, Club House... Ground coverage shall not exceed 15% of reservation area... b) Stadium / Sports Complex - Indoor games, swimming pool, sports hostel, and commercial shops underneath spectators gallery up to 15% of total built up area.",
    'clause_cards_html': """
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px;">
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--blueprint); padding:16px;">
          <span class="kicker">REG. 4.10(vi) // 15% COMMERCIAL</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Campus Ancillary Retail</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Authorizes up to 15% of basic FSI in hospitals and universities for cafeterias, banks, student bookshops, and pharmacies without commercial rezoning.
          </p>
        </div>
        <div style="background:var(--paper-raised); border:1px solid var(--line-strong); border-left:4px solid var(--amber); padding:16px;">
          <span class="kicker" style="color:var(--amber);">REG. 4.27 // DP RESERVATIONS</span>
          <h4 style="font-family:var(--disp); font-size:0.95rem; margin-top:4px; margin-bottom:8px;">Civic Reservation Envelope</h4>
          <p style="font-size:0.85rem; color:var(--ink-soft); line-height:1.5;">
            Enforces that 85% of playground reservations stay open-to-sky (15% max pavilion coverage), while permitting under-stand retail in municipal stadiums.
          </p>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper-raised); padding:16px; margin-top:12px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--line-strong); padding-bottom:8px; margin-bottom:12px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">FIG_020 // DP RESERVATION USES &amp; RESTRICTIONS SPECIFICATION</span>
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">REGULATION 4.27 PLATE</span>
        </div>
        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-family:var(--mono); font-size:11.5px;">
            <thead>
              <tr style="background:var(--ink); color:var(--paper-raised);">
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Reservation Code / Use</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Max Ground Coverage</th>
                <th style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong);">Max Commercial Shop %</th>
                <th style="padding:6px 8px; text-align:left; border:1px solid var(--line-strong);">Ancillary Facilities Permitted</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Play Ground (PG)</strong></td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">15%</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); color:var(--brick); font-weight:700;">0% (Prohibited)</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Pavilion, gymnasia, changing rooms, caretaker room</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Stadium / Sports Complex</strong></td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">As per plan</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">15% of total BUA</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Retail shops underneath spectators' gallery, sports hostel</td>
              </tr>
              <tr>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Institutional Campus (P/SP)</strong></td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">Standard margins</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">15% of basic FSI</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Cafeterias, pharmacies, student stationery, bank/ATM</td>
              </tr>
              <tr style="background:var(--paper);">
                <td style="padding:6px 8px; border:1px solid var(--line-strong);"><strong>Municipal Market</strong></td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); font-weight:700;">Full commercial</td>
                <td style="padding:6px 8px; text-align:right; border:1px solid var(--line-strong); color:var(--blueprint); font-weight:700;">100%</td>
                <td style="padding:6px 8px; border:1px solid var(--line-strong);">Meat/fish stalls, vegetable bays, cold storages</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': r"""
      <p style="margin-bottom:12px;">
        <strong>Practical Scrutiny Problem:</strong> A university plans a new medical college campus in a Public/Semi-Public zone in Nagpur on a <strong>40,000 sq.m plot</strong>. Basic FSI is 1.10.
      </p>
      <div class="worked-step">
        <span class="step-badge">FSI POTENTIAL COMPUTATION</span>
        <div>
          Gross Basic Built-Up Area = $40,000 \times 1.10 = \mathbf{44,000\text{ sq.m BUA}}$.
        </div>
      </div>
      <div class="worked-step">
        <span class="step-badge">ANCILLARY COMMERCIAL QUOTA</span>
        <div>
          Under Regulation 4.10(vi), permissible commercial cross-subsidization area:
          <br>Max Commercial BUA = $44,000 \times 15\% = \mathbf{6,600\text{ sq.m}}$.
          <br>The college designs:
          <br>• 2,500 sq.m student cafeteria &amp; dining hall
          <br>• 1,500 sq.m medical bookshop and student store
          <br>• 1,200 sq.m retail pharmacy serving outpatients
          <br>• 1,400 sq.m bank branch and ATMs.
          <br>Total = 6,600 sq.m. Fully compliant with Reg. 4.10(vi)!
        </div>
      </div>
      <div style="border-top:1px solid var(--line-strong); padding-top:10px; margin-top:14px; font-family:var(--mono); font-size:0.85rem; color:var(--ink);">
        ✓ STATUTORY RESULT: Commercial facilities sanctioned as integral ancillary components of institutional campus.
      </div>
    """,
    'pitfalls_html': """
      <div class="callout callout-amber">
        <strong>Pitfall 1: Exceeding 15% Ground Coverage on Playground (PG) Reservations</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          Architects designing pavilions, indoor badminton courts, or gymnasiums on playground reservations often consume 25% to 30% of the ground. Regulation 4.27(a) strictly caps total ground footprint to <strong>15% of the reservation area</strong>.
        </p>
      </div>
      <div class="callout callout-amber">
        <strong>Pitfall 2: Attempting Standalone Commercial Developments in P/SP Zones</strong>
        <p style="font-size:0.84rem; color:var(--ink-soft); margin-top:4px;">
          The 15% commercial allowance in Regulation 4.10(vi) is strictly ancillary to an active educational, medical, or institutional campus. Proposing a standalone commercial shopping mall without the primary institutional anchor is illegal.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:10px;">
        <span class="badge badge-amended">Corrigendum CR.121/21 (02 Dec 2021)</span>
        <span style="font-family:var(--mono); font-size:12px; color:var(--ink-soft);">Stadium Commercial Shop Clarification</span>
      </div>
      <p style="font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
        Standardized the permissible commercial percentage for retail shops underneath stadium spectator galleries at 15% of total built-up area across all Municipal Corporations and Councils.
      </p>
    """,
    'quiz': [
      {
        'question': 'What maximum percentage of basic FSI can be used for ancillary commercial purposes (canteens, pharmacies, bookshops) in institutional campuses in P/SP zones?',
        'options': [
          '5%',
          '10%',
          '15%',
          '25%'
        ],
        'correctAnswer': 2,
        'explanation': 'Under Regulation 4.10(vi), up to 15% of the area in educational, medical, and institutional campuses in P/SP zones may be used for ancillary commercial purposes.'
      },
      {
        'question': 'What is the maximum permissible ground coverage for pavilions, gymnasia, and club buildings on a designated Playground (PG) reservation under Regulation 4.27(a)?',
        'options': [
          '5%',
          '10%',
          '15%',
          '30%'
        ],
        'correctAnswer': 2,
        'explanation': 'Under Regulation 4.27(a), built structures like pavilions and gymnasia on a playground reservation cannot exceed 15% ground coverage, ensuring 85% remains open play area.'
      },
      {
        'question': 'What maximum percentage of total built-up area may be developed as commercial shops underneath stadium spectator stands under Regulation 4.27(b)?',
        'options': [
          '10%',
          '15%',
          '20%',
          'Commercial shops are prohibited'
        ],
        'correctAnswer': 1,
        'explanation': 'Regulation 4.27(b) permits commercial shops underneath stadium spectators\' galleries up to a maximum of 15% of the total built-up area.'
      }
    ],
    'prev_url': '/lessons/reg-4-12-environmental-and-special-zones.html',
    'prev_title': 'Reg. 4.12-4.25 Environmental Zones',
    'next_url': '/chapters/ch04.html',
    'next_title': 'Chapter 4 Syllabus Index'
}
