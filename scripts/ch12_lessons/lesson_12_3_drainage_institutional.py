"""
UDCPR Chapter 12 - Lesson 12.3: Drainage Standards & Institutional Sanitation Fitments
Statutory Clauses: Regulation 12.6.1, 12.6.2, 12.6.3, Tables 12-C to 12-J
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
        'clause': 'Reg. 12.6.1 - 12.6.3, Tables 12-C to 12-J',
        'title': 'Drainage Standards & Institutional Sanitation Fitments',
        'meta_desc': 'Chapter 12 drainage and sanitary fitments under UDCPR-2020: residential fitment baselines, crèche ratios, decontamination showers, and statutory fixture schedules for Offices (12-C), Factories (12-D), Cinemas (12-E), and Hospitals (12-G to 12-J).',
        'ch_slug': 'ch12',
        'ch_title': 'Chapter 12: Structural Safety & Sanitation',
        'badge_status': '100% COMPLETE',
        'amendment_cite': None,
        'filename': 'reg-12-6-drainage-and-institutional-sanitation.html',
        'lesson_id': 'ch12_lesson_3',
        'quiz_id': 'quiz_ch12_3',
        'prev_url': '/lessons/reg-12-5-water-supply-and-flushing-storage-capacities.html',
        'prev_title': 'Reg. 12.5 Water Supply & Flushing Storage',
        'next_url': '/lessons/reg-12-6-commercial-hospitality-sanitation-and-signs.html',
        'next_title': 'Reg. 12.6 - 12.7 Commercial Sanitation & Display Signs',
        'lead_summary': (
            'Sanitary fitments and drainage connections form the frontline of environmental hygiene and life safety in building planning. '
            'Regulation 12.6 governs the precise number of water-closets, urinals, washbasins, and decontamination fixtures required '
            'across Maharashtra. For residential dwellings, every unit requires individual bathing, water-closet, and kitchen sink fitments '
            '(or 1 WC and 1 bath per 2 tenements in shared housing). In institutional and public buildings, Reg. 12.6.3 mandates vital health safeguards: '
            'a total ban on drinking fountains inside toilet cores, mandatory emergency eyewash and decontamination showers with wheelchair access in toxic areas, '
            'dedicated crèche toilet ratios, and rigorous statutory fixture schedules for Offices (Table 12-C), Factories (Table 12-D), '
            'Cinemas (Table 12-E with a 2/3 male to 1/3 female demographic split), and Healthcare facilities (Tables 12-G to 12-J).'
        ),
        'plain_summary_html': """
          <p>
            Plumbing and sanitary layout errors are among the most frequent reasons architectural plans fail municipal scrutiny. 
            Regulation 12.6 provides comprehensive rules governing residential drainage and institutional fixture quantities:
          </p>
          <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
            <li><strong>Residential Minimum Fitments (Reg 12.6.1 &amp; 12.6.2):</strong>
              <br>&bull; <em>Individual Dwellings:</em> Must have at least 1 bathroom with tap &amp; floor trap, 1 water-closet with flushing cistern &amp; ablution tap, and 1 kitchen sink or wash place tap with floor trap.
              <br>&bull; <em>Shared / Chawl Housing:</em> Where individual conveniences are absent, the statutory minimum is <strong>1 water tap with floor trap inside each tenement</strong>, plus <strong>1 WC and 1 bathroom for every 2 tenements</strong>.
            </li>
            <li><strong>Critical Health &amp; Safety Mandates (Reg 12.6.3):</strong>
              <br>&bull; <em>Drinking Water Ban in Toilets (Clause c):</em> <strong>Drinking fountains or coolers are strictly prohibited inside toilet blocks</strong>. Where food is consumed, separate water stations must be provided outside.
              <br>&bull; <em>Hazardous Exposure Decontamination (Clause d):</em> Wherever workers handle poisonous, infectious, or corrosive materials, developers must install a <strong>washbasin with eye-wash jet and emergency shower</strong> with an unobstructed, wheelchair-accessible route.
              <br>&bull; <em>Crèche Sanitary Standard (Clause g):</em> Workplaces offering crèches must provide <strong>1 WC per 10 persons</strong>, <strong>1 washbasin per 15 persons</strong>, and a kitchen sink with a dedicated drinking water tap for milk and infant meal preparation.
              <br>&bull; <em>Floor Accessibility &amp; Construction Workers (Clause e):</em> Pure aggregate numbers are invalid if fixtures are clustered on one floor—toilets must be provided on every floor in schools and multistory offices. Developers must also provide temporary on-site sanitation (min 1 WC + 1 washbasin) for construction workers.
            </li>
            <li><strong>Institutional Fixture Schedules (Tables 12-C to 12-J):</strong>
              <br>&bull; <em>Office Buildings (Table 12-C):</em> Staff WCs: <strong>1 per 25 males</strong>, <strong>1 per 15 females</strong>. Urinals: progressive up to 100, then +3% (101-200) and +2.5% (>200).
              <br>&bull; <em>Factories (Table 12-D):</em> Workers WCs: 1 for up to 15 males, 1 for up to 12 females, with stepped additions up to 100 (+3% / +5%).
              <br>&bull; <em>Cinemas, Multiplexes &amp; Theatres (Table 12-E):</em> Male WCs: 1 per 100 (up to 400), +1 per 250 thereafter. Female WCs: <strong>3 per 100 (up to 200)</strong>, +2 per 100 thereafter. Urinals: 1 per 25 males. <em>Demographic split: 2/3 male, 1/3 female.</em>
              <br>&bull; <em>Hospitals (Tables 12-G to 12-J):</em> Indoor general wards: <strong>1 WC per 8 beds</strong> for both males and females; Urinals: 1 per 30 beds. Outdoor Patient Departments (OPD Table 12-H): 1 WC per 100 males, 2 per 100 females. Staff quarters: 1 WC per 4 persons.
            </li>
          </ul>
        """,
        'statutory_extract': (
            "Drinking fountains shall not be installed in the toilets. Where there is the danger of exposure to skin contamination with poisonous, "
            "infectious or irritating material, washbasin with eye wash jet and an emergency shower located in an area accessible at all times with the passage / "
            "right of way suitable for access to a wheel chair, shall be provided... Workplaces where crèches are provided, they shall be provided with one WC "
            "for 10 persons or part thereof, one washbasin for 15 persons or part thereof, one kitchen sink with floor tap for preparing food / milk preparations... "
            "NOTE - Male population may be assumed as two-third and female population as one-third."
        ),
        'clause_cards_html': """
          <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
            <div class="ruled-card">
              <span class="kicker">REGULATION 12.6.2</span>
              <h4 class="ruled-card-title">Residential Tenement Standards</h4>
              <p class="ruled-card-desc">
                Sets the baseline for home hygiene: each self-contained unit requires 1 bath with floor trap, 1 WC with flushing &amp; ablution tap, 
                and 1 kitchen wash tap/sink. For shared/chawl housing, 1 WC and 1 bath are legally required for every 2 tenements.
              </p>
              <div class="ruled-card-footer">
                <span>RESIDENTIAL</span>
                <span class="badge badge-status-done">1 BATH/WC : 2 UNITS</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">REGULATION 12.6.3(c) &amp; (d)</span>
              <h4 class="ruled-card-title">Health, Eye-Wash &amp; Crèche Rules</h4>
              <p class="ruled-card-desc">
                Drinking fountains strictly barred inside toilets. Hazardous material zones must have an emergency deluge shower and eye-wash jet with wheelchair passage. 
                Crèches mandate 1 WC per 10, 1 basin per 15, and kitchen sink with drinking tap.
              </p>
              <div class="ruled-card-footer">
                <span>SAFETY PROTOCOLS</span>
                <span class="badge badge-status-done">DECONTAMINATION</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">TABLE 12-C &amp; 12-D</span>
              <h4 class="ruled-card-title">Offices &amp; Factory Workplaces</h4>
              <p class="ruled-card-desc">
                Office staff toilets require 1 WC per 25 males and 1 WC per 15 females. Factories require higher worker ratios (1 WC per 12 females, 1 WC per 15 males) 
                with progressive additions for large industrial workforces.
              </p>
              <div class="ruled-card-footer">
                <span>WORKPLACE HYGIENE</span>
                <span class="badge badge-status-done">TABLES 12-C / 12-D</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">TABLES 12-E TO 12-J</span>
              <h4 class="ruled-card-title">Assembly &amp; Hospital Ecosystems</h4>
              <p class="ruled-card-desc">
                Cinemas and theatres apply the statutory 2/3 male to 1/3 female ratio with female WCs enhanced to 3 per 100 up to 200. 
                Hospital wards mandate 1 WC per 8 beds, 1 urinal per 30 beds, and 1 WC per 4 residents in staff/nurse quarters.
              </p>
              <div class="ruled-card-footer">
                <span>PUBLIC &amp; HEALTH</span>
                <span class="badge badge-status-done">TABLES 12-E / 12-G</span>
              </div>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 12-B: INSTITUTIONAL &amp; PUBLIC SANITARY FITMENTS MATRIX</span>
              <span class="badge badge-status-done">TABLES 12-C, 12-D, 12-E &amp; 12-G</span>
            </div>

            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono);">
                <thead>
                  <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">OCCUPANCY</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">MALE W.C. RATIO</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">FEMALE W.C. RATIO</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">URINALS (MALE)</th>
                    <th style="padding:8px; text-align:left;">DEMOGRAPHIC BASIS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Offices (Table 12-C)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 25 males</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 15 females</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Nil up to 6; 1 for 7-20; 2 for 21-45; 3 for 46-70; 4 for 71-100; +3% (101-200)</td>
                    <td style="padding:8px;">Actual staff census or Table 9-E occupant load</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Factories (Table 12-D)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 up to 15; 2 for 16-35; 3 for 36-65; 4 for 66-100; +3% (101-200)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 up to 12; 2 for 13-25; 3 for 26-40; 4 for 41-57; 5 for 58-77; 6 for 78-100; +5%</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Nil up to 6; 1 for 7-20; 2 for 21-45; 3 for 46-70; 4 for 71-100; +3%</td>
                    <td style="padding:8px;">Maximum worker shift count</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Cinemas &amp; Theatres (Table 12-E)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 100 up to 400; over 400 add 1 per 250</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--brick);">3 per 100 up to 200; over 200 add 2 per 100</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 25 males or part thereof</td>
                    <td style="padding:8px;">Statutory split: <strong>2/3 Male, 1/3 Female</strong></td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Museums &amp; Galleries (Table 12-F)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 200 up to 400; over 400 add 1 per 250</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 100 up to 200; over 200 add 1 per 150</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 50 males</td>
                    <td style="padding:8px;">Statutory split: <strong>2/3 Male, 1/3 Female</strong></td>
                  </tr>
                  <tr style="background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Hospital In-Patients (Table 12-G)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">1 per 8 beds or part thereof</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">1 per 8 beds or part thereof</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">1 per 30 beds</td>
                    <td style="padding:8px;">Total sanctioned general bed capacity</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div style="font-family:var(--mono); font-size:11px; color:var(--ink-soft); margin-top:12px; line-height:1.5;">
              <strong>UNIVERSAL SCRUTINY DIRECTIVE:</strong> Reg 12.6.3(e) states that using purely numerical totals is forbidden if it results in an unsuited installation. Toilet blocks cannot be consolidated exclusively in basements or ground floors; in educational institutions and multistory corporate buildings, functional male, female, and universal accessible toilets must be provided on <strong>every occupied floor</strong>.
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
            <strong>Scenario:</strong> Calculate the mandatory public sanitary fitments for a new <strong>600-seat multiplex auditorium</strong> 
            under Regulation 12.6.3 and Table 12-E.
          </p>
          <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
            <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">STEP-BY-STEP CALCULATION (TABLE 12-E):</div>
            <div><strong>Step 1: Determine Demographic Population Breakdown</strong></div>
            <div>&bull; Per Note to Table 12-E: <em>"Male population may be assumed as two-third and female population as one-third."</em></div>
            <div>&bull; Male Public Audience = 600 &times; (2/3) = <strong>400 Males</strong>.</div>
            <div>&bull; Female Public Audience = 600 &times; (1/3) = <strong>200 Females</strong>.</div>
            <div style="margin-top:8px;"><strong>Step 2: Male Sanitary Fitments</strong></div>
            <div>&bull; <strong>Male Water-Closets (W.C.):</strong> Rule = 1 per 100 up to 400; over 400 add 1 per 250.</div>
            <div>&nbsp;&nbsp;For 400 males = 400 / 100 = <strong>4 Male W.C.s</strong>.</div>
            <div>&bull; <strong>Male Urinals:</strong> Rule = 1 per 25 or part thereof.</div>
            <div>&nbsp;&nbsp;For 400 males = 400 / 25 = <strong>16 Urinals</strong>.</div>
            <div style="margin-top:8px;"><strong>Step 3: Female Sanitary Fitments</strong></div>
            <div>&bull; <strong>Female Water-Closets (W.C.):</strong> Rule = 3 per 100 up to 200; over 200 add 2 per 100.</div>
            <div>&nbsp;&nbsp;For 200 females = 2 &times; 3 = <strong>6 Female W.C.s</strong>.</div>
            <div style="margin-top:8px;"><strong>Step 4: Summary of Required Public Fixtures</strong></div>
            <div>&bull; <strong>Male Toilet Core:</strong> 4 W.C.s + 16 Urinals + Washbasins.</div>
            <div>&bull; <strong>Female Toilet Core:</strong> 6 W.C.s + Washbasins.</div>
            <div>&bull; <strong>Accessibility Check:</strong> Under Chapter 13 &amp; NBC norms, at least 1 unisex wheelchair-accessible toilet must also be provided.</div>
            <div>&bull; <strong>Health Check (Reg 12.6.3(c)):</strong> Ensure zero drinking water coolers are located within either the male or female toilet ante-rooms!</div>
          </div>
        """,
        'pitfalls_html': """
          <div>
            <strong>1. Installing Drinking Water Dispensers Inside Toilet Ante-Rooms (Reg 12.6.3(c)):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              Architects frequently position water coolers or filtered drinking fountains in the corridor or ante-room leading to toilet blocks for plumbing drainage convenience. Reg. 12.6.3(c) explicitly dictates: <em>"Drinking fountains shall not be installed in the toilets."</em> This constitutes an immediate municipal health and sanction rejection.
            </p>
          </div>
          <div>
            <strong>2. Applying a 50:50 Gender Split to Cinema Calculations:</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              Designing a theatre with 300 men and 300 women will severely distort the required fitments. UDCPR Table 12-E mandates a statutory demographic baseline of <strong>2/3 male and 1/3 female</strong>. However, note that women receive a higher ratio (3 per 100 up to 200) to compensate for usage duration.
            </p>
          </div>
          <div>
            <strong>3. Forgetting Wheelchair Passages to Emergency Showers (Reg 12.6.3(d)):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              In industrial chemical storage, testing laboratories, or pharmaceutical plants, providing an emergency eye-wash and body shower is mandatory. Architects often tuck it into a tight corner behind machinery. UDCPR specifically mandates that the right of way to this fixture must be wide enough and clear for <strong>wheelchair access at all times</strong>.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.92rem; line-height:1.6;">
            Sanitation fixture tables 12-C through 12-P are based on harmonized National Building Code Part-9 standards. 
            The statutory requirement for crèche sanitation under Reg. 12.6.3(g) (1 WC per 10, 1 basin per 15, and kitchen sink with drinking tap) 
            was reaffirmed to align with the Maternity Benefit (Amendment) Act, making on-site crèche infrastructure fully compliant with state labor welfare directives.
          </p>
        """,
        'quiz': [
            {
                'question': 'Under Regulation 12.6.3(c), what is the statutory rule regarding drinking fountains in building toilets?',
                'options': [
                    'They must be provided in all public toilets with at least 2 fountains',
                    'They shall NOT be installed in the toilets',
                    'They are permitted only in male executive toilets',
                    'They can be installed provided they have hands-free sensor taps'
                ],
                'answer': 1,
                'explanation': 'Regulation 12.6.3(c) unequivocally states: "Drinking fountains shall not be installed in the toilets."'
            },
            {
                'question': 'In shared residential chawl-type housing without individual conveniences, what is the required baseline for water-closets and bathrooms under Regulation 12.6.2(2)?',
                'options': [
                    'One WC and one bath for every 5 tenements',
                    'One WC and one bath for every 4 tenements',
                    'One WC and one bath for every 2 tenements',
                    'One WC and one bath per floor regardless of tenements'
                ],
                'answer': 2,
                'explanation': 'Regulation 12.6.2(2) stipulates: "One water closet with flushing apparatus... for every two tenements, and One bath with water tap and floor trap for every two tenements."'
            },
            {
                'question': 'What demographic population distribution does Table 12-E mandate when calculating public sanitary fitments for cinemas, multiplexes, and concert halls?',
                'options': [
                    '50% Male and 50% Female',
                    'Two-third (2/3) Male and one-third (1/3) Female',
                    'Three-fourth (3/4) Male and one-fourth (1/4) Female',
                    'Based purely on local electoral rolls'
                ],
                'answer': 1,
                'explanation': 'The Note to Table 12-E explicitly dictates: "NOTE - Male population may be assumed as two-third and female population as one-third."'
            },
            {
                'question': 'Under Regulation 12.6.3(g), what are the statutory sanitary fixture requirements for workplaces providing crèches?',
                'options': [
                    '1 WC for 25 persons and 1 urinal',
                    '1 WC for 10 persons, 1 washbasin for 15 persons, and 1 kitchen sink with drinking tap',
                    '2 WCs and 2 showers per 50 children',
                    'Only 1 baby bath tub per 20 infants'
                ],
                'answer': 1,
                'explanation': 'Regulation 12.6.3(g) mandates: "one WC for 10 persons or part thereof, one washbasin for 15 persons or part thereof, one kitchen sink with floor tap for preparing food / milk preparations. The sink provided shall be with a drinking water tap."'
            }
        ]
    }

if __name__ == '__main__':
    create_lesson_page(lesson_data)
