"""
UDCPR Chapter 12 - Lesson 12.2: Water Supply Demands & Flushing Storage Capacities
Statutory Clauses: Regulation 12.5, Table 12-A, Table 12-B
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
        'clause': 'Reg. 12.5, Table 12-A & 12-B',
        'title': 'Water Supply Demands & Statutory Flushing Storage Capacities',
        'meta_desc': 'UDCPR-2020 Regulation 12.5 water supply computations: 5 persons per tenement, Table 12-A per capita rates (135 lpcd residential, 180 lpcd hotel, 340/450 lpcd hospital), and Table 12-B mandatory flushing cistern storage quotas.',
        'ch_slug': 'ch12',
        'ch_title': 'Chapter 12: Structural Safety & Sanitation',
        'badge_status': '100% COMPLETE',
        'amendment_cite': 'Corrigendum 02-12-2021',
        'filename': 'reg-12-5-water-supply-and-flushing-storage-capacities.html',
        'lesson_id': 'ch12_lesson_2',
        'quiz_id': 'quiz_ch12_2',
        'prev_url': '/lessons/reg-12-1-structural-design-materials-and-building-services.html',
        'prev_title': 'Reg. 12.1 - 12.4 Structural Safety & Building Services',
        'next_url': '/lessons/reg-12-6-drainage-and-institutional-sanitation.html',
        'next_title': 'Reg. 12.6 Drainage & Institutional Sanitation',
        'lead_summary': (
            'Water security and storage dimensioning are statutory prerequisites for municipal building sanction across Maharashtra. '
            'Regulation 12.5 establishes the exact mathematical basis for sizing domestic and fire-fighting water infrastructure under '
            'National Building Code Part-9 (Plumbing Services). For residential developments, population is fixed at 5 persons per tenement, '
            'consuming 135 litres per head per day (lpcd) under Table 12-A. Non-residential occupancies derive populations from Table 9-E occupant load '
            'factors. In tandem, Table 12-B enforces separate, dedicated flushing storage cistern capacities (such as 270 litres for the first WC plus '
            '180 litres per additional WC in an apartment) to guarantee continuous sanitation during civic supply interruptions.'
        ),
        'plain_summary_html': """
          <p>
            Designing water infrastructure under UDCPR is not a guessing game—it is an exact statutory calculation that dictates 
            the volume of your Underground Water Tank (UGWT) and Overhead Water Tank (OHWT). Regulation 12.5 divides water demands into 
            <strong>domestic consumption (Table 12-A)</strong> and <strong>dedicated flushing cistern storage (Table 12-B)</strong>:
          </p>
          <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
            <li><strong>Residential Population Multiplier (Reg 12.5.2):</strong> All residential apartments are calculated on a flat standard of <strong>5 persons per tenement</strong>, regardless of whether it is a 1-BHK or 3-BHK.</li>
            <li><strong>Non-Residential Occupant Load:</strong> Commercial, institutional, and assembly populations are calculated using the net carpet area divided by the occupant load factors in <strong>Table 9-E</strong> (substituted vide Corrigendum dated 02nd December, 2021).</li>
            <li><strong>Daily Per Capita Consumption (Table 12-A):</strong>
              <br>&bull; <em>Residential Living Units:</em> <strong>135 lpcd</strong> (litres per capita per day).
              <br>&bull; <em>Hotels with Lodging:</em> <strong>180 lpcd</strong> per bed.
              <br>&bull; <em>Day Schools:</em> <strong>45 lpcd</strong> | <em>Boarding Schools:</em> <strong>135 lpcd</strong>.
              <br>&bull; <em>Hospitals (&le; 100 beds):</em> <strong>340 lpcd</strong> | <em>Hospitals (&gt; 100 beds):</em> <strong>450 lpcd</strong> | <em>Medical Staff Quarters:</em> <strong>135 lpcd</strong>.
              <br>&bull; <em>Cinemas, Auditoriums &amp; Theatres:</em> <strong>15 lpcd</strong> per seat of accommodation.
              <br>&bull; <em>Restaurants:</em> <strong>70 lpcd</strong> per seat | <em>General Business Offices:</em> <strong>45 lpcd</strong>.
              <br>&bull; <em>Airports:</em> <strong>70 lpcd</strong> | <em>Railway Junction Stations:</em> <strong>70 (45) lpcd</strong> | <em>Terminals:</em> <strong>45 lpcd</strong>.
            </li>
            <li><strong>Flushing Storage Capacities (Table 12-B):</strong> In addition to domestic storage, buildings must provide separate reserve flushing cistern volume:
              <br>&bull; <em>Individual Residential Flats:</em> <strong>270 litres net</strong> for the first WC seat + <strong>180 litres</strong> for each additional WC seat in the same flat.
              <br>&bull; <em>Tenements with Common Convenience:</em> <strong>900 litres net per WC seat</strong>.
              <br>&bull; <em>Factories &amp; Workshops:</em> <strong>900 litres per WC seat</strong> + <strong>180 litres per urinal seat</strong>.
              <br>&bull; <em>Cinemas &amp; Assembly Halls:</em> <strong>900 litres per WC seat</strong> + <strong>350 litres per urinal seat</strong>.
            </li>
          </ul>
        """,
        'statutory_extract': (
            "The total requirements of water supply shall be calculated based on the population as given below : "
            "Residential Building: 5 persons per tenement; Other Buildings: No. of persons on occupant load and area of floors given in Table No. 9-E. "
            "The requirements of water supply for various occupancies shall be as given in Table No.12-A and Table No.12-B or as specified by the Authority... "
            "Flushing Storage Capacities: For residential premises other than tenements having common convenience: 270 litres net for one w.c. seat and 180 litres "
            "for each additional seat in the same flat."
        ),
        'clause_cards_html': """
          <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
            <div class="ruled-card">
              <span class="kicker">POPULATION BASIS</span>
              <h4 class="ruled-card-title">Residential Standard: 5 Persons / Tenement</h4>
              <p class="ruled-card-desc">
                Reg. 12.5(2) mandates that every residential tenement houses an assumed population of 5 persons. 
                A 100-flat residential tower has an official design population of 500 persons. For non-residential buildings, 
                carpet area is divided by occupant load benchmarks under Table 9-E.
              </p>
              <div class="ruled-card-footer">
                <span>REG. 12.5(2)</span>
                <span class="badge badge-status-done">5 PERS / UNIT</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">TABLE 12-A</span>
              <h4 class="ruled-card-title">Daily Per Capita Demands (LPCD)</h4>
              <p class="ruled-card-desc">
                Sets non-negotiable daily water demand per head: 135 lpcd for homes, 180 lpcd for hotel beds, 
                450 lpcd for large hospitals, 70 lpcd per dining seat in restaurants, and 15 lpcd per cinema seat. 
                Determines the daily fresh water intake requirement from municipal mains.
              </p>
              <div class="ruled-card-footer">
                <span>STATUTORY NORM</span>
                <span class="badge badge-status-done">TABLE 12-A</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">TABLE 12-B</span>
              <h4 class="ruled-card-title">Dedicated Flushing Cistern Reserves</h4>
              <p class="ruled-card-desc">
                Sanitary fixtures require independent flushing storage to prevent bio-hazard dry traps during main tank cleaning. 
                Flats require 270L for the 1st WC + 180L for each subsequent WC. Public assembly halls require 900L per WC plus 350L per urinal.
              </p>
              <div class="ruled-card-footer">
                <span>STATUTORY NORM</span>
                <span class="badge badge-status-done">TABLE 12-B</span>
              </div>
            </div>

            <div class="ruled-card">
              <span class="kicker">PLUMBING INTEGRATION</span>
              <h4 class="ruled-card-title">NBC Part-9 Dual Water Sizing</h4>
              <p class="ruled-card-desc">
                In modern green building and dual-plumbing designs across Maharashtra, municipal potable water feeds domestic 
                consumption, while recycled STP treated water fills the dedicated Table 12-B flushing storage tanks, optimizing total site utility bills.
              </p>
              <div class="ruled-card-footer">
                <span>NBC PART-9</span>
                <span class="badge badge-status-done">DUAL PLUMBING</span>
              </div>
            </div>
          </div>
        """,
        'plate_or_table_html': """
          <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
              <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">TABLE 12-A: PER CAPITA WATER CONSUMPTION &amp; TABLE 12-B FLUSHING STORAGE</span>
              <span class="badge badge-status-done">STATUTORY SCHEDULES</span>
            </div>

            <div style="overflow-x:auto;">
              <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono); margin-bottom:16px;">
                <thead>
                  <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:60px;">SR.</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">OCCUPANCY CLASSIFICATION</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">STATUTORY BASIS</th>
                    <th style="padding:8px; text-align:right; width:160px;">CONSUMPTION (LPCD)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">1(a)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Residential Living Units</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per resident (5 persons / tenement)</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">135</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">1(b)</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Hotels with lodging accommodation</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per guest bed</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">180</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">2</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Educational: (a) Day Schools / (b) Boarding</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per pupil</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">45 / 135</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">3</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Hospitals: (a) &le; 100 beds / (b) &gt; 100 beds / (c) Quarters</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per bed / Per staff resident</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">340 / 450 / 135</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">4</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Assembly: Cinemas, Theatres, Auditoriums</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per seat of accommodation</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">15</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">5</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Government &amp; Semi-public business offices</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per employee / occupant load</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">45</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">6</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Mercantile: (a) Restaurants / (b) Other business</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per dining seat / Per occupant load</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">70 / 45</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">7</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Industrial: (a) With bathrooms / (b) Without baths</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per worker shift</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">45 / 30</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">8-9</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Storage Warehousing / Hazardous</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per worker shift</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">30</td>
                  </tr>
                  <tr style="background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">10-13</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Transit: Intermediate / Junction / Terminal / Airport</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Per daily passenger &amp; staff load</td>
                    <td style="padding:8px; text-align:right; font-weight:700; color:var(--blueprint);">45(25) / 70(45) / 45 / 70</td>
                  </tr>
                </tbody>
              </table>

              <div style="font-size:12px; font-weight:700; color:var(--blueprint); margin-bottom:8px;">TABLE 12-B: DEDICATED FLUSHING STORAGE CAPACITIES</div>
              <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono);">
                <thead>
                  <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:60px;">SR.</th>
                    <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft);">BUILDING CLASSIFICATION</th>
                    <th style="padding:8px; text-align:left;">DEDICATED FLUSHING STORAGE CAPACITY</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">1</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Tenements with common convenience</td>
                    <td style="padding:8px; font-weight:700; color:var(--blueprint);">900 litres net per W.C. seat</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">2</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Residential individual flats (other than common convenience)</td>
                    <td style="padding:8px; font-weight:700; color:var(--blueprint);">270 litres net for 1st W.C. seat + 180 litres for each additional seat in the same flat</td>
                  </tr>
                  <tr style="border-bottom:1px solid var(--ink-soft);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">3</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Factories and Workshops</td>
                    <td style="padding:8px; font-weight:700; color:var(--blueprint);">900 litres per W.C. seat + 180 litres per urinal seat</td>
                  </tr>
                  <tr style="background:var(--paper-raised);">
                    <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700;">4</td>
                    <td style="padding:8px; border-right:1px solid var(--ink-soft);">Cinemas, public assembly halls, etc.</td>
                    <td style="padding:8px; font-weight:700; color:var(--blueprint);">900 litres per W.C. seat + 350 litres per urinal seat</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        """,
        'worked_example_html': """
          <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
            <strong>Scenario:</strong> Calculate the statutory daily domestic water demand and the dedicated flushing cistern storage capacity 
            for a new residential housing complex in Thane comprising <strong>80 apartments (all 2-BHK units, each containing 2 W.C.s)</strong>, 
            plus a ground-floor commercial restaurant licensed for <strong>60 dining seats</strong>.
          </p>
          <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
            <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">STEP-BY-STEP WATER STORAGE SIZING (REG. 12.5):</div>
            <div><strong>Step 1: Determine Design Populations (Reg. 12.5.2)</strong></div>
            <div>&bull; Residential Tenements = 80 units &times; 5 persons/tenement = <strong>400 residents</strong>.</div>
            <div>&bull; Restaurant Occupancy = <strong>60 seats</strong>.</div>
            <div style="margin-top:8px;"><strong>Step 2: Calculate Daily Domestic Water Demands (Table 12-A)</strong></div>
            <div>&bull; Residential Daily Consumption = 400 residents &times; 135 lpcd = <strong>54,000 Litres/Day</strong>.</div>
            <div>&bull; Restaurant Daily Consumption = 60 seats &times; 70 lpcd = <strong>4,200 Litres/Day</strong>.</div>
            <div>&bull; <strong>Total Daily Domestic Demand</strong> = 54,000 + 4,200 = <strong>58,200 Litres/Day</strong> (58.2 m&sup3;).</div>
            <div style="margin-top:8px;"><strong>Step 3: Calculate Mandatory Dedicated Flushing Storage (Table 12-B)</strong></div>
            <div>&bull; Each of the 80 flats has 2 W.C. seats.</div>
            <div>&bull; Under Table 12-B Item 2: Storage per flat = 270 L (1st WC) + 180 L (2nd WC) = <strong>450 Litres / flat</strong>.</div>
            <div>&bull; Total Residential Flushing Reserve = 80 flats &times; 450 L = <strong>36,000 Litres</strong>.</div>
            <div>&bull; (Note: Restaurant restaurant toilets calculate per Table 12-B Item 3/4 based on fitted WC/urinal count).</div>
            <div style="margin-top:8px;"><strong>Step 4: Tank Allocation Engineering Breakdown</strong></div>
            <div>&bull; <strong>Underground Water Tank (UGWT):</strong> Sized for at least 1 day's domestic reserve (58,200 L) + Fire Reserve (50,000 L to 100,000 L as per NBC Part-4 height class).</div>
            <div>&bull; <strong>Overhead Water Tank (OHWT):</strong> Sized for domestic gravity distribution (~30,000 L) + Dedicated Flushing Compartment (<strong>36,000 L</strong>) partitioned with non-cross-connected distribution risers.</div>
          </div>
        """,
        'pitfalls_html': """
          <div>
            <strong>1. Sizing Flats by Carpet Area Instead of 5 Persons / Tenement (Reg 12.5.2):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              A common MEP engineering mistake is assuming 3 persons for a 1-BHK and 6 persons for a 3-BHK. Reg. 12.5(2) is categorical: <em>"Residential Building: 5 persons per tenement."</em> Municipal scrutiny engineers will reject PHE drawings that undercount occupants in studio or 1-BHK layouts.
            </p>
          </div>
          <div>
            <strong>2. Omitting the Dedicated Table 12-B Flushing Storage Compartment:</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              Plumbing consultants often lump all water storage into one general domestic tank. UDCPR Table 12-B legally mandates dedicated flushing storage (270L + 180L/WC). Without a separate physical partition or dedicated flushing overhead compartment, the submission will receive scrutiny objections for life-safety hygiene non-compliance.
            </p>
          </div>
          <div>
            <strong>3. Miscalculating Hospital Water Tiers (&le; 100 vs &gt; 100 beds):</strong>
            <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
              Table 12-A Item 3 draws a sharp line: small hospitals (&le; 100 beds) require 340 lpcd per bed, while large hospitals (&gt; 100 beds) jump to <strong>450 lpcd per bed</strong> due to extensive ICU, dialysis, and central sterilization (CSSD) demands. Using 340 lpcd on a 150-bed hospital will fail municipal water connection vetting.
            </p>
          </div>
        """,
        'amendment_section_html': """
          <p style="font-size:0.92rem; line-height:1.6;">
            <strong>Corrigendum / Addendum No. CR 121/21 dated 02nd December, 2021:</strong><br>
            Formally substituted the occupant load reference in Regulation 12.5(2) to align directly with <em>Table No. 9-E</em> 
            (Occupant Load per person per floor area). This ensures complete harmony between Chapter 9 (Means of Egress &amp; Occupancy) 
            and Chapter 12 (Water Supply sizing), eliminating ambiguities where older municipal corporations attempted to apply obsolete 1991 DCR occupant factors.
          </p>
        """,
        'quiz': [
            {
                'question': 'Under UDCPR Regulation 12.5(2), what is the statutory population assumption used to compute water demand for residential buildings?',
                'options': [
                    '3 persons per tenement',
                    '4 persons per tenement',
                    '5 persons per tenement',
                    'Based on 1 person per 10 square meters of carpet area'
                ],
                'answer': 2,
                'explanation': 'Regulation 12.5(2) explicitly mandates: "Residential Building: 5 persons per tenement."'
            },
            {
                'question': 'According to Table 12-A, what is the daily per capita water consumption rate for residential living units?',
                'options': [
                    '45 litres per head per day',
                    '70 litres per head per day',
                    '100 litres per head per day',
                    '135 litres per head per day'
                ],
                'answer': 3,
                'explanation': 'Table 12-A Item 1(a) stipulates 135 litres per head per day (lpcd) for residential living units.'
            },
            {
                'question': 'For a multi-family apartment with individual conveniences, what is the required dedicated flushing storage capacity under Table 12-B for a flat containing 2 W.C. seats?',
                'options': [
                    '270 litres total',
                    '360 litres total',
                    '450 litres total (270 L for the first + 180 L for the second)',
                    '900 litres total'
                ],
                'answer': 2,
                'explanation': 'Under Table 12-B Item 2, storage is 270 litres net for the first W.C. seat plus 180 litres for each additional seat in the same flat (270 + 180 = 450 litres).'
            },
            {
                'question': 'Under Table 12-A, what is the daily water consumption rate required for a hospital having more than 100 patient beds?',
                'options': [
                    '135 lpcd',
                    '180 lpcd',
                    '340 lpcd',
                    '450 lpcd per bed'
                ],
                'answer': 3,
                'explanation': 'Table 12-A Item 3(b) requires 450 litres per bed per day for hospitals with beds exceeding 100 (compared to 340 lpcd for hospitals up to 100 beds).'
            }
        ]
    }

if __name__ == '__main__':
    create_lesson_page(lesson_data)
