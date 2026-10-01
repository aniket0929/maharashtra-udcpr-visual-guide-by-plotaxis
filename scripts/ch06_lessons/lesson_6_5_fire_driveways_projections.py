"""
UDCPR FROM SCRATCH - CHAPTER 6, LESSON 5
Module: scripts/ch06_lessons/lesson_6_5_fire_driveways_projections.py
Statutory Anchor: Regulation 6.7, Regulation 6.8, Regulation 6.4 (Table 6-H), & Regulation 1.3(93)(xiv)
Content: Permissible Projections, Complete Statutory FSI Exclusions (Reg 6.8), and Special Building 6.0m Fire Driveways
"""

lesson_data = {
    'filename': 'reg-6-7-projections-fsi-exclusions-and-fire-driveways.html',
    'lesson_id': '6.5',
    'quiz_id': 'quiz-6-5',
    'clause': 'Regulation 6.4, 6.7 & 6.8',
    'title': 'Permissible Projections, FSI Exclusions & Fire Driveways',
    'badge_status': 'CORE STATUTORY SPECIFICATION',
    'ch_slug': 'ch06',
    'ch_title': 'Chapter 6: General Building Requirements - Setback, Marginal Distance, Height and Permissible FSI',
    'meta_desc': 'Detailed guide to UDCPR permissible projections under Reg 6.7 (chajjas, canopies, watchman booths), 100% FSI exclusions under Reg 6.8 (parking podiums, refuge areas, service floors), and 6.0m fire driveways.',
    'lead_summary': 'Master the statutory boundary between what is buildable, what can project into mandatory open margins, what is 100% exempt from FSI calculations, and how the non-negotiable 6.0m fire driveway dictates site circulation.',
    'amendment_cite': 'UDCPR-2020 Reg 6.7 & 6.8, Corrigendum CR 121/21 dt. 02nd Dec 2021',

    'plain_summary_html': """
      <p>
        Building margins under UDCPR are primarily reserved for light, ventilation, and emergency fire apparatus movement. However, architectural functionality requires specific projections and site services. <strong>Regulation 6.7</strong> strictly defines which architectural features may encroach into marginal open spaces without violating development permissions.
      </p>
      <p>
        Simultaneously, <strong>Regulation 6.8</strong> establishes the statutory catalog of <strong>Exclusions from FSI</strong>: areas that do not count against your basic, premium, or ancillary FSI balances. These include basements, stilts, and multi-storey podiums used exclusively for parking, designated refuge areas, service floors up to 1.8m height, STP/ETP plants, and substations.
      </p>
      <p>
        Crucially, for any <strong>Special Building</strong> (including all residential towers &ge; 15.0m height, malls, hospitals, and large assembly buildings), <strong>a continuous 6.0-meter wide unobstructed motorable driveway</strong> must encircle the structure. Projections, stairs, or ramps that compromise this 6.0m emergency path are strictly illegal.
      </p>
    """,

    'statutory_extract': """
### 6.7 PERMISSIBLE PROJECTIONS IN MARGINAL OPEN SPACES
(a) Cornice, chajja, roof or weather shade: Not more than 0.75 m. wide overhanging marginal open spaces... Sloping / horizontal chajja over balcony permitted up to balcony projections.
(d) Canopy or porch: Not exceeding 5.0 m. in length and 2.5 m. in width in the form of cantilever and unenclosed over main/subsidiary entrances; minimum clear height of 2.4 m. below beam bottom. Minimum clearance of 1.5 m. between plot boundaries and canopy. More than one canopy permitted for special buildings.
(f) Accessory buildings:
  i) Toilet in existing building: Single storeyed max 4.0 sq.m. in rear/side margin, 7.5 m. from road line and 1.5 m. from other boundaries.
  ii) Parking lock-up garage: Max 2.4 m. height in rear corner of bungalow plot. Counted in FSI.
  iv) Watchman's cabin / booth: Not more than 6.0 sq.m. in built up area, minimum width/diameter of 1.80 m. Allowed at every entrance and/or exit.
(h) Fire escape staircase: Single flight not less than 1.2 m. width excluding marginal distance required for special building.
(i) Staircase mid-landing: 1.2 m. width with clear headroom 2.1 m. Clear distance from landing edge to plot boundary not less than 1.8 m. for non-special and 6.0 m. for special buildings.
(k) Steps or otta: May project upto 1.2 m. from the building line.

### 6.8 EXCLUSION OF STRUCTURES / PROJECTIONS FOR FSI CALCULATION
The following are excluded from FSI:
i) Structures / Projections permitted in marginal open spaces under Reg 6.7.
ii) Stilt / Multi-storeyed floors / podium / basement, if used exclusively for parking including passages, staircase, Lift Duct / Lobby therein.
iii) Porches, Canopies, lofts, ledges, AC Plant Rooms, Lift Well, Lift Machine Room, and Service Floor of height not exceeding 1.8 m. below beam for hospitals, malls, star hotels, and buildings above 15.0 m.
iv) Water, grey water, STP / ETP, rainwater harvesting pump rooms, electric substations, DG rooms, electric meter rooms, refuge / garbage chutes.
v) Rockery, well, fountain, ramps, compound wall, domestic working place (open to sky), overhead water tank, Refuge area for high-rise buildings as per Reg 9.29.6.
vii) Atrium in any type of building.
viii) Open to sky terraces, top of podium, open swimming pool on terrace/podium with plant room.
    """,

    'clause_cards_html': """
      <div class="card-grid">
        <div class="card">
          <span class="kicker-card">SPECIAL BUILDING MANDATE</span>
          <h3 class="card-title">6.0m Fire Tender Driveway</h3>
          <p class="card-body">
            For all buildings &ge; 15.0m height, institutional buildings, and commercial special buildings, a <strong>continuous 6.0m clear driveway</strong> capable of bearing a 45-tonne fire engine axle load must surround the building. No permanent architectural obstructions are allowed in this zone.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">MARGINAL PROJECTIONS</span>
          <h3 class="card-title">Canopies, Chajjas & Ottas</h3>
          <p class="card-body">
            • <strong>Chajjas:</strong> Max 0.75m overhang in required margins.<br>
            • <strong>Canopies:</strong> Max 5.0m length &times; 2.5m width; min 2.4m headroom; <strong>min 1.5m clearance to plot boundary</strong>.<br>
            • <strong>Ottas / Steps:</strong> May project up to 1.2m from building line.<br>
            • <strong>Watchman Booth:</strong> Max 6.0 sq.m area, min 1.80m width.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">100% FSI EXEMPTION</span>
          <h3 class="card-title">Podiums, Stilts & Basements</h3>
          <p class="card-body">
            Under Reg 6.8(ii), basement levels, ground stilts, and multi-deck parking podiums are <strong>100% excluded from FSI</strong>, provided they are dedicated to vehicular parking, access driveways, ramps, and associated lift lobbies/staircases.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">HIGH-RISE ESSENTIALS</span>
          <h3 class="card-title">Refuge & Service Floors</h3>
          <p class="card-body">
            • <strong>Refuge Areas:</strong> Excluded from FSI per Reg 9.29.6.<br>
            • <strong>Service Floors:</strong> Clear height &le; 1.8m below beam in buildings &gt; 15.0m, star hotels, and malls are completely exempt from FSI.<br>
            • <strong>Environmental Services:</strong> STPs, ETPs, and electrical substations are zero-FSI.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">GREEN BELT FSI • REG 6.5</span>
          <h3 class="card-title">Green Belt In-Situ Transfer</h3>
          <p class="card-body">
            Under <strong>Regulation 6.5</strong>, Basic FSI along with full potential of Premium FSI and TDR of the green belt zone may be consumed on the remaining un-affected land of the owner. Condition: The owner must plant <strong>minimum 100 trees per hectare</strong> that must survive for at least one year before issuance of the Occupancy Certificate.
          </p>
        </div>

        <div class="card">
          <span class="kicker-card">DEFENSE / RESTRICTED • REG 6.13</span>
          <h3 class="card-title">HEMRL & Defense Buffer FSI</h3>
          <p class="card-body">
            Under <strong>Regulation 6.13</strong>, lands affected by safety buffers of the High Energy Material Research Laboratory (HEMRL) or other Central/State statutory restrictions can transfer their full FSI entitlement onto the remaining contiguous portion of the land. However, formal sub-division of such parcels is strictly prohibited.
          </p>
        </div>
      </div>
    """,

    'plate_or_table_html': """
      <div class="table-container">
        <table class="drawing-table">
          <thead>
            <tr>
              <th>Building Element / Space</th>
              <th>Permissible Projection / Dimension</th>
              <th>Clearance to Plot Boundary</th>
              <th>FSI Counting Status (Reg 6.8)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Weather Chajjas / Cornices</strong></td>
              <td>Max 0.75 m projection</td>
              <td>Cannot reduce min required margin</td>
              <td><strong>EXCLUDED</strong> from FSI</td>
            </tr>
            <tr>
              <td><strong>Entrance Canopy / Porch</strong></td>
              <td>Max 5.0 m length &times; 2.5 m width</td>
              <td><strong>Min 1.5 m</strong> from plot boundary</td>
              <td><strong>EXCLUDED</strong> from FSI</td>
            </tr>
            <tr>
              <td><strong>Watchman's Cabin / Booth</strong></td>
              <td>Max 6.0 sq.m area (min 1.80m width)</td>
              <td>Permitted at each gate / entry</td>
              <td><strong>EXCLUDED</strong> from FSI</td>
            </tr>
            <tr>
              <td><strong>Steps & Plinth Otta</strong></td>
              <td>Max 1.2 m projection from building line</td>
              <td>Maintains margin beyond 1.2m</td>
              <td><strong>EXCLUDED</strong> from FSI</td>
            </tr>
            <tr>
              <td><strong>Basement & Podium Parking</strong></td>
              <td>As per parking layout requirements</td>
              <td>As per basement setback rules</td>
              <td><strong>EXCLUDED</strong> from FSI</td>
            </tr>
            <tr>
              <td><strong>Service Floor (&le; 15m bldgs)</strong></td>
              <td>Clear height &le; 1.8 m below beam</td>
              <td>Within building envelope</td>
              <td><strong>EXCLUDED</strong> from FSI</td>
            </tr>
            <tr>
              <td><strong>Refuge Floor / Area</strong></td>
              <td>As per Reg 9.29.6 fire norms</td>
              <td>Cantilever or floor cutout</td>
              <td><strong>EXCLUDED</strong> from FSI</td>
            </tr>
            <tr>
              <td><strong>Bungalow Lock-up Garage</strong></td>
              <td>Max 2.4 m height in rear corner</td>
              <td>7.5 m from front road line</td>
              <td><strong>COUNTED IN FSI</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
    """,

    'worked_example_html': r"""
      <div class="math-box">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:12px; color:var(--ink);">
          Worked Compliance Audit: Evaluating Projections & Driveway Clearances
        </h4>
        <p><strong>Design Scenario:</strong></p>
        <ul>
          <li>Special Building: 14-storey residential tower ($H = 44.0\text{ m}$) on a $2,500\text{ sq.m}$ plot.</li>
          <li>Side Margin provided = $H/5 = 44 / 5 = \mathbf{8.80\text{ meters}}$.</li>
          <li>Architect proposes:
            <ol>
              <li>Cantilever entrance canopy of $4.8\text{m} \times 2.4\text{m}$ with 2.6m headroom projecting towards the side driveway.</li>
              <li>External fire escape staircase of 1.2m width landing in the side open space.</li>
              <li>A 1.0m wide continuous sun-shading chajja extending along all upper floors.</li>
            </ol>
          </li>
        </ul>

        <div style="margin: 16px 0; border-left: 3px solid var(--blueprint); padding-left: 14px;">
          <p><strong>Audit 1: Entrance Canopy Verification (Reg 6.7d)</strong></p>
          <p>• Length &amp; Width: $4.8\text{m} \le 5.0\text{m}$ and $2.4\text{m} \le 2.5\text{m}$. &rarr; <strong>Complies.</strong></p>
          <p>• Clear Headroom: $2.6\text{m} \ge 2.4\text{m}$ below beam bottom. &rarr; <strong>Complies.</strong></p>
          <p>• Boundary Clearance: Side margin is 8.8m, projection is 2.4m &rarr; Remaining clearance $= 8.8 - 2.4 = 6.4\text{m} \ge 1.5\text{m}$. &rarr; <strong>Complies.</strong></p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--brick); padding-left: 14px;">
          <p><strong>Audit 2: Weather Chajja Overhang (Reg 6.7a) - DEFECT IDENTIFIED</strong></p>
          <p>• Architect proposed a <strong>1.0-meter chajja</strong>.</p>
          <p>• Reg 6.7(a) limits chajjas in required open margins strictly to <strong>0.75 meters</strong>!</p>
          <p>• <em>Correction Mandate:</em> The chajja must be reduced to 0.75m unless it sits directly over an authorized balcony.</p>
        </div>

        <div style="margin: 16px 0; border-left: 3px solid var(--amber); padding-left: 14px;">
          <p><strong>Audit 3: Special Building Fire Driveway Clearance</strong></p>
          <p>• Required clear driveway width for Special Buildings &ge; 15m = <strong>6.0 meters</strong>.</p>
          <p>• Fire escape stair projects 1.2m into the 8.8m side margin.</p>
          <p>• Clear space remaining $= 8.80\text{m} - 1.20\text{m} = \mathbf{7.60\text{ meters}} \ge 6.0\text{m}$. &rarr; <strong>Fire drive is fully compliant!</strong></p>
        </div>
      </div>
    """,

    'pitfalls_html': """
      <div class="panel-alert">
        <h4 style="font-family:var(--disp); font-weight:700; color:var(--brick); margin-bottom:8px;">
          LETHAL DESIGN DEFECTS IN MARGINS & EXCLUSIONS
        </h4>
        <ul style="margin-left: 18px; line-height: 1.6;">
          <li>
            <strong>Encroaching into the 6.0m Fire Driveway:</strong> Constructing generator pads, LPG banks, or low canopy columns that pinch the driveway to under 6.0m will result in immediate refusal of the Chief Fire Officer (CFO) NOC.
          </li>
          <li>
            <strong>Exceeding 1.8m Height for Service Floors:</strong> Reg 6.8(iii) grants FSI exclusion to service floors <em>only</em> if the clear height below the beam does not exceed <strong>1.8 meters</strong>. If it is 1.9m or 2.1m, the entire floor is counted in FSI!
          </li>
          <li>
            <strong>Assuming Bungalow Garages are Free of FSI:</strong> Unlike basement/podium parking which is 100% exempt under Reg 6.8(ii), independent bungalow lock-up garages permitted under Reg 6.7(f)(ii) are <em>explicitly counted in FSI</em>!
          </li>
          <li>
            <strong>Violating the 1.5m Canopy-to-Boundary Gap:</strong> Even if a canopy is within 5m &times; 2.5m, its outer cantilever edge must maintain at least <strong>1.5 meters</strong> of clear distance to the plot boundary.
          </li>
        </ul>
      </div>
    """,

    'amendment_section_html': """
      <div class="panel-info">
        <h4 style="font-family:var(--disp); font-weight:700; margin-bottom:8px;">Amendment Highlights</h4>
        <ul style="font-size:0.92rem; line-height:1.6; margin-left:18px;">
          <li><strong>Corrigendum CR 121/21 (dt. 02 Dec 2021):</strong> Deleted the 10 sq.m limitation on electric meter rooms and generator areas, allowing full exclusion as per actual statutory utility board requirements.</li>
          <li><strong>Notification dt. 12 Oct 2022:</strong> Clarified that service floor exclusions apply uniformly to all commercial buildings above 15.0m height.</li>
        </ul>
      </div>
    """,

    'quiz': [
      {
        'question': 'What is the maximum permissible overhang for a standard window chajja/cornice projecting into required marginal open spaces under Regulation 6.7(a)?',
        'options': [
          '0.45 meters',
          '0.60 meters',
          '0.75 meters',
          '1.20 meters'
        ],
        'answer': 2,
        'explanation': 'Regulation 6.7(a) dictates that no cornice, chajja, roof or weather shade more than 0.75 m wide shall overhang or project over required marginal open spaces.'
      },
      {
        'question': 'What is the maximum clear height below the beam bottom for a Service Floor to remain exempt from FSI under Regulation 6.8(iii)?',
        'options': [
          '1.5 meters',
          '1.8 meters',
          '2.1 meters',
          '2.4 meters'
        ],
        'answer': 1,
        'explanation': 'Under Regulation 6.8(iii), service floors are excluded from FSI provided their height does not exceed 1.8 meters below the beam.'
      },
      {
        'question': 'What is the minimum clear driveway width required around Special Buildings (including buildings >= 15m height) for fire tender access?',
        'options': [
          '3.0 meters',
          '4.5 meters',
          '6.0 meters',
          '9.0 meters'
        ],
        'answer': 2,
        'explanation': 'Under UDCPR regulations for Special Buildings and fire safety, a continuous unobstructed motorable driveway of at least 6.0 meters width must be maintained.'
      },
      {
        'question': 'Under Regulation 6.7(d), what is the minimum clearance that must be maintained between the outer edge of an entrance canopy and the plot boundary?',
        'options': [
          '0.9 meters',
          '1.5 meters',
          '2.25 meters',
          '3.0 meters'
        ],
        'answer': 1,
        'explanation': 'Regulation 6.7(d) specifically provides that there shall be a minimum clearance of 1.5 meters between the plot boundaries and the canopy.'
      }
    ],

    'prev_url': '/lessons/reg-6-2-3-side-rear-margins-and-h5-rule.html',
    'prev_title': 'Reg 6.2.3: Side & Rear Margins, Building Separation & H/5 Rule',
    'next_url': '/lessons/reg-6-10-height-caps-chowks-and-special-floors.html',
    'next_title': 'Reg 6.9 to 6.15: Height Caps, Chowks & Special Amenities'
}
