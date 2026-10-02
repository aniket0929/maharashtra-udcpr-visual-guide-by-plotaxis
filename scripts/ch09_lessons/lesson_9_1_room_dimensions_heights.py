"""
UDCPR Visual Guide - CHAPTER 9, LESSON 1
Regulation 9.1 to 9.8: Plinth Standards, Room Heights, Sanitary Sizes & Mezzanines
File: scripts/ch09_lessons/lesson_9_1_room_dimensions_heights.py
"""

lesson_data = {
    'filename': 'reg-9-1-room-dimensions-and-height-clearances.html',
    'lesson_id': 'reg-9-1-room-dimensions-and-height-clearances',
    'quiz_id': 'quiz-9-1',
    'clause': 'Reg. 9.1 to 9.8',
    'title': 'Plinth Standards, Room Heights, Sanitary Sizes & Mezzanines',
    'badge_status': 'STATUTORY • TABLE 9-A & 9-B',
    'ch_slug': 'ch09',
    'ch_title': 'Chapter 9: Requirements of Parts of Buildings',
    'meta_desc': 'Master UDCPR Regulations 9.1 to 9.8: plinth levels (30cm / 45cm flood), Table 9-A room heights (2.75m flat roof, 2.4m beam soffit, 3.0m commercial), bathroom/WC sizes, Table 9-B loft coverage, and 50% mezzanine rules.',
    
    'lead_summary': (
        'Regulations 9.1 through 9.8 form the bedrock of architectural spatial planning in Maharashtra, codifying mandatory minimum dimensions, '
        'drainage plinths, and vertical headroom clearances for all human-occupied spaces. It governs finished plinth heights (minimum 30 cm above '
        'surrounding ground, raised to 45 cm above high flood levels, and 15 cm for covered garages), enforces Table 9-A clear vertical heights '
        '(standard 2.75 m for flat-roof habitable rooms, with 2.40 m under beam soffits and 3.00 m for commercial/assembly halls), establishes non-negotiable '
        'sanitary stall footprints (bathrooms, WCs, combined units), regulates Table 9-B storage lofts, restricts cantilever cupboards to 0.60 m projections, '
        'and caps mezzanine floors to 50% of the room carpet area.'
    ),
    
    'amendment_cite': 'Corrigendum / Addendum No. CR 121/21 dt. 02-12-2021 (Mezzanine carpet area basis & duplex internal staircases)',
    
    'plain_summary_html': r'''
<p>
  Every architectural floor plan submitted for scrutiny must demonstrate rigorous compliance with internal spatial geometry. Regulation 9.1 to 9.8 removes arbitrary design guesswork by establishing statutory minimums and maximums across all habitable, service, and ancillary spaces:
</p>
<ul class="rule-list">
  <li><strong>Plinth Elevation &amp; Flood Safeguards (Reg 9.1):</strong> The building plinth must be at least <strong>30 cm above surrounding ground level</strong> to guarantee gravity storm-water discharge. In flood-prone or riverine zones, the plinth must be elevated to at least <strong>45 cm above the High Flood Level (HFL)</strong>. Covered parking stilts and garages require a minimum <strong>15 cm elevation</strong>.</li>
  <li><strong>Habitable Room Heights (Table 9-A):</strong> Standard flat-roof residential rooms mandate a minimum height of <strong>2.75 m</strong> (maximum 4.50 m). For air-conditioned rooms, the clear ceiling can reduce to <strong>2.40 m</strong>. However, regardless of architectural ceiling design, the clear headroom under any structural beam must never be less than <strong>2.40 m</strong>. Assembly halls, starred hotels, corporate offices, and shopping malls require a minimum clear height of <strong>3.00 m</strong> (up to 6.00 m or higher without FSI penalty).</li>
  <li><strong>Sanitary Stall Dimensions (Reg 9.4):</strong> Independent bathrooms must measure at least <strong>1.00 m x 1.20 m</strong> ($1.20\text{ m}^2$); independent water closets (WCs) require at least <strong>0.90 m x 0.90 m</strong> ($0.81\text{ m}^2$); combined toilet units require at least <strong>1.50 sq.m</strong> with a minimum internal width of <strong>1.00 m</strong>. All sanitary stalls require a minimum clear ceiling height of <strong>2.10 m</strong>.</li>
  <li><strong>Lofts &amp; Ledges (Table 9-B &amp; Reg 9.5):</strong> Storage lofts must preserve a clear headroom of <strong>2.10 m beneath the loft slab</strong> and have a maximum loft height of <strong>1.50 m</strong>. Coverage is restricted to <strong>25%</strong> over kitchens/habitable rooms, <strong>100%</strong> over bathrooms/corridors, and <strong>33% to 50%</strong> over commercial shops. AC ledges are limited to <strong>0.50 m x 1.00 m</strong> per unit.</li>
  <li><strong>Mezzanine Floors (Reg 9.7):</strong> Permitted up to an aggregate area of <strong>50% of the room carpet area</strong>, preserving at least <strong>2.10 m headroom below</strong> and set back at least <strong>1.80 m from the front entrance wall</strong>. Mezzanines are strictly counted in FSI.</li>
</ul>
''',

    'statutory_extract': r"""9.1 PLINTH
i) The plinth of building shall be so located with respect to the surrounding ground level that adequate drainage of the site is assured. The height of the plinth shall not be less than 30 cm. above the surrounding ground level. In areas subjected to flooding, the height of the plinth shall be at least 45 cm. above the high flood level.
ii) Covered parking spaces and garages shall be raised at least 15 cm. above the surrounding ground level and shall be satisfactory drained.

9.2 HABITABLE ROOMS
9.2.1 Size and Dimension of Habitable Rooms: Size and dimension of habitable rooms, shall be as per requirement and convenience of the owner.
9.2.2 Height of Habitable Rooms: The minimum and maximum height of a habitable room shall be given in Table No.9-A hereunder:
Table No.9-A:
1. Flat Roof -
a) Any habitable room: Min 2.75 m. | Max 4.5 m.
a1) Habitable room in EWS / LIG Housing: Min 2.75 m. | Max 4.2 m.
b) Air-conditioned habitable room: Min 2.4 m. | Max 4.5 m.
c) Assembly Halls, Residential Hotels 3 star and above, Institutional, Educational, Industrial, Hazardous, Malls, IT, Office Buildings, Theatres: Min 3.0 m. (2.4 m. in case of AC room) | Max 6.00 m. or higher.
d) Shops: Min 3.00 m. | Max 4.5 m.
2. Pitched roof -
a) Any habitable room: Min 2.75 m. (average with 2.0 m. at lowest point) | Max 4.5 m. (average with 3.2 m. at lowest point)
Provided that the minimum head-way under any beam shall be 2.4 m.
Provided further that height more than that specified above, if required for particular occupancy, shall not be counted towards calculation of FSI.

9.3 KITCHEN
9.3.2 Height of Kitchen: The height of a kitchen measured from the surface of the floor, to the lowest point in the ceiling (bottom of slab) shall not be less than 2.75 m. except for the portion to accommodate floor trap of the upper floor.

9.4 BATH ROOMS, WATER CLOSETS, COMBINED BATH ROOM AND WATER CLOSET
9.4.1 Size: i) Independent Bath room 1.00 m. x 1.20 m. ii) Independent Water closet 0.9 m. x 0.9 m. iii) Combined bath room and water closet 1.50 sq.m. with minimum width of 1.00 m.
9.4.2 Height: Not less than 2.1 m.
9.4.3 Other requirements: Ventilation shaft or external air window of min 0.3 sq.m. (min side 0.3 m.).

9.5 LEDGE OR TAND / LOFT
Table No.9-B - Provision of Loft:
1. Kitchen / Habitable room: Max Coverage 25%
2. Bathroom, water closet, corridor: Max Coverage 100%
3. Shops with width up to 3.0 m.: Max Coverage 33%
4. Shops with width exceeding 3.0 m.: Max Coverage 50%
5. Industrial: Max Coverage 33%
Clear head room under Loft >= 2.1 m. Max height of loft = 1.5 m. AC ledge max 0.5 m. x 1.0 m.

9.6 CUPBOARD: Cantilever projections upto 0.60 m. in setbacks for residential buildings except ground floor. Window frame placed inner side. Allowed only on one wall. At least 6.0 m. from boundary in special buildings. For height >= 24 m., margin shall not reduce to less than 6.0 m. on 1st floor and 4.5 m. on upper floors. In congested areas, min 1.0 m. from boundary.

9.7 MEZZANINE FLOOR: Aggregate area shall not exceed 50% of carpet area of that room. Headroom >= 2.1 m. Counted towards FSI. At least 1.8 m. away from front wall. Not allowed if loft is provided in same room.""",

    'clause_cards_html': r'''
<div class="card-grid">
  <div class="card">
    <div class="card-header">
      <span class="card-num">01</span>
      <h4>Plinth Elevation Levels</h4>
    </div>
    <div class="card-body">
      <p>Standard building plinths require a minimum height of <strong>30 cm</strong> above ground. In designated flood zones, plinths must be raised to <strong>45 cm above High Flood Level (HFL)</strong>. Covered parking garages and stilts require at least <strong>15 cm</strong> finished plinth height.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">02</span>
      <h4>Room Height &amp; Beam Clearances</h4>
    </div>
    <div class="card-body">
      <p>Habitable rooms and kitchens require a minimum clear ceiling height of <strong>2.75 m</strong> (flat roof). Air-conditioned rooms allow <strong>2.40 m</strong>. Headway under any structural beam must be at least <strong>2.40 m</strong>. Assembly halls, malls, and offices require <strong>3.00 m</strong> clear height.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">03</span>
      <h4>Sanitary Dimensions &amp; Shafts</h4>
    </div>
    <div class="card-body">
      <p>Independent Bath: <strong>1.00 m x 1.20 m</strong> ($1.20\text{ m}^2$). Independent WC: <strong>0.90 m x 0.90 m</strong> ($0.81\text{ m}^2$). Combined Toilet: <strong>1.50 sq.m</strong> (min width <strong>1.00 m</strong>). Ceiling height must be $\ge 2.10\text{ m}$. Every toilet requires an external window or shaft ventilator of at least <strong>0.30 sq.m</strong>.</p>
    </div>
  </div>

  <div class="card">
    <div class="card-header">
      <span class="card-num">04</span>
      <h4>Mezzanines &amp; Lofts</h4>
    </div>
    <div class="card-body">
      <p>Mezzanines are capped at <strong>50% of room carpet area</strong>, mandate <strong>2.10 m clear height below</strong>, must sit <strong>1.80 m back from the front wall</strong>, and are <em>strictly counted in FSI</em>. Lofts allow <strong>25% coverage</strong> in living/kitchens and <strong>100%</strong> over toilets (headroom $\ge 2.10\text{ m}$, max height <strong>1.50 m</strong>).</p>
    </div>
  </div>
</div>
''',

    'plate_or_table_html': r'''
<div class="table-wrap">
  <table class="drawing-table">
    <thead>
      <tr>
        <th>Room / Component Type</th>
        <th>Minimum Size / Dimension</th>
        <th>Minimum Height (m.)</th>
        <th>Maximum Height (m.)</th>
        <th>FSI &amp; Coverage Rules</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Habitable Room (Residential)</strong></td>
        <td>As per convenience of owner</td>
        <td><code>2.75 m</code> (2.40 m if AC)</td>
        <td><code>4.50 m</code> (4.20 m EWS)</td>
        <td>Counted in FSI; Beam soffit min 2.40 m</td>
      </tr>
      <tr>
        <td><strong>Commercial Shop</strong></td>
        <td>As per architectural layout</td>
        <td><code>3.00 m</code></td>
        <td><code>4.50 m</code></td>
        <td>Counted in FSI; Mezzanine/loft permitted</td>
      </tr>
      <tr>
        <td><strong>Offices / Malls / Assembly</strong></td>
        <td>Occupant load dependent</td>
        <td><code>3.00 m</code> (2.40 m if AC)</td>
        <td><code>6.00 m+</code> (as required)</td>
        <td>Excess height does NOT count towards FSI</td>
      </tr>
      <tr>
        <td><strong>Kitchen / Cooking Alcove</strong></td>
        <td>As per convenience of owner</td>
        <td><code>2.75 m</code></td>
        <td><code>4.50 m</code></td>
        <td>Floor trap drop exempt; 25% loft allowed</td>
      </tr>
      <tr>
        <td><strong>Independent Bathroom</strong></td>
        <td><code>1.00 m x 1.20 m</code></td>
        <td><code>2.10 m</code></td>
        <td>Floor-to-slab level</td>
        <td>100% loft permitted over top slab</td>
      </tr>
      <tr>
        <td><strong>Independent Water Closet (WC)</strong></td>
        <td><code>0.90 m x 0.90 m</code></td>
        <td><code>2.10 m</code></td>
        <td>Floor-to-slab level</td>
        <td>100% loft permitted over top slab</td>
      </tr>
      <tr>
        <td><strong>Combined Bath &amp; WC</strong></td>
        <td><code>1.50 sq.m</code> (width &ge; 1.00 m)</td>
        <td><code>2.10 m</code></td>
        <td>Floor-to-slab level</td>
        <td>Must ventilate to shaft or open air</td>
      </tr>
      <tr>
        <td><strong>Mezzanine Floor</strong></td>
        <td>Max 50% carpet area of room</td>
        <td><code>2.10 m</code> (headroom below)</td>
        <td>Restricted by main room</td>
        <td><strong>COUNTED IN FSI</strong>; 1.8m setback from front</td>
      </tr>
      <tr>
        <td><strong>Cantilever Cupboard</strong></td>
        <td>Max <code>0.60 m</code> projection</td>
        <td>Floor to floor</td>
        <td>Floor level</td>
        <td>1 wall/room; Min 6.0m boundary buffer in Special</td>
      </tr>
      <tr>
        <td><strong>AC Ledge</strong></td>
        <td>Max <code>0.50 m x 1.00 m</code></td>
        <td>External wall ledge</td>
        <td>External wall ledge</td>
        <td>Free of FSI; Must not obstruct fire tender</td>
      </tr>
    </tbody>
  </table>
</div>
''',

    'worked_example_html': r"""
<div class="example-box">
  <h4>PRACTICAL ARCHITECTURAL CALCULATION: COMMERCIAL SHOP MEZZANINE &amp; LOFT COMPLIANCE</h4>
  <p><strong>Scenario:</strong> A retail shop in a commercial complex has a carpet area of <strong>40.00 sq.m</strong> (dimensions $4.00\text{ m} \times 10.00\text{ m}$) with a floor-to-ceiling slab height of <strong>4.80 m</strong>.</p>
  
  <div class="step-box">
    <strong>Step 1: Check Maximum Permissible Mezzanine Size (Reg 9.7.1)</strong>
    <ul>
      <li>Under Regulation 9.7.1 (as amended Dec 2021), mezzanine floor area is capped at <strong>50% of the room carpet area</strong>:</li>
      <li>$\text{Maximum Mezzanine Area} = 40.00\text{ sq.m} \times 50\% = \mathbf{20.00\text{ sq.m}}$.</li>
      <li>Proposed mezzanine dimensions: $4.00\text{ m} \times 5.00\text{ m} = 20.00\text{ sq.m}$ (Compliant).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 2: Check Clear Vertical Heights &amp; Headrooms (Reg 9.7.2 &amp; Table 9-A)</strong>
    <ul>
      <li>Total available vertical height: $4.80\text{ m}$.</li>
      <li>Required clear headroom below mezzanine: Minimum $\ge 2.10\text{ m}$ (Assume $2.30\text{ m}$ provided).</li>
      <li>Mezzanine intermediate slab thickness: $0.15\text{ m}$.</li>
      <li>Remaining headroom on top of mezzanine: $4.80\text{ m} - 2.30\text{ m} - 0.15\text{ m} = \mathbf{2.35\text{ m}}$ (Well above the minimum $2.10\text{ m}$ required).</li>
    </ul>
  </div>

  <div class="step-box">
    <strong>Step 3: Verification of Front Setback &amp; Loft Prohibition (Reg 9.7.3)</strong>
    <ul>
      <li>Front Setback: The mezzanine must terminate at least <strong>1.80 m away from the front entrance wall</strong> of the shop. Since the shop is $10.00\text{ m}$ deep and the mezzanine is $5.00\text{ m}$ deep, placing it at the rear leaves $5.00\text{ m}$ open to the front, easily satisfying the 1.80 m setback rule!</li>
      <li>Loft Restriction: Regulation 9.7.1 dictates: <em>"Where loft is provided in the room, the mezzanine floor shall not be allowed."</em> Therefore, no additional storage loft can be built in this shop.</li>
      <li>FSI Accounting: The $20.00\text{ sq.m}$ mezzanine floor area <strong>must be added to the building's consumed FSI</strong>.</li>
    </ul>
  </div>
</div>
""",

    'pitfalls_html': r'''
<div class="alert-box alert-warning">
  <h4>COMMON ARCHITECTURAL SCRUTINY DEFECTS IN REGULATION 9.1 TO 9.8</h4>
  <ul class="warning-list">
    <li><strong>Beam Soffit Height vs Slab Height:</strong> Stating a room height of $2.75\text{ m}$ on the drawing while a deep structural beam leaves only $2.25\text{ m}$ of clear headspace. UDCPR Regulation 9.2.2 strictly mandates: <em>"Provided that the minimum head-way under any beam shall be 2.4 m."</em></li>
    <li><strong>Providing Both Loft and Mezzanine:</strong> Introducing a 25% storage loft and a 50% mezzanine in the same commercial or residential room. Under Regulation 9.7.1, providing a loft completely disqualifies that room from having a mezzanine floor.</li>
    <li><strong>Treating Mezzanine as Free of FSI:</strong> Architects frequently confuse storage lofts (which are free of FSI) with mezzanine floors. Regulation 9.7 Note explicitly states: <em>"Mezzanine floor area shall be counted towards FSI."</em></li>
    <li><strong>Encroaching Cupboards in Special Building Margins:</strong> Under Reg 9.6.1, a cantilever cupboard cannot project into the mandatory $6.0\text{ m}$ perimeter fire margin of a Special Building.</li>
    <li><strong>Undersized Combined Toilets:</strong> Submitting a combined toilet with an area of $1.50\text{ sq.m}$ but a width of only $0.85\text{ m}$. Reg 9.4.1(iii) mandates an absolute minimum internal width of <strong>1.00 m</strong>.</li>
  </ul>
</div>
''',

    'amendment_section_html': r'''
<div class="amendment-card">
  <h4>Statutory Corrigenda &amp; Clarifications</h4>
  <p><strong>Corrigendum / Addendum No. CR 121/21 dt. 02-12-2021:</strong></p>
  <p>Substituted the word "built-up area" with "carpet area" in Regulation 9.7.1 to establish that the 50% mezzanine ceiling is strictly calibrated against the <strong>net carpet area</strong> of the host room. In addition, Note to Reg 9.28.8 was inserted to standardize internal duplex stairs (min width $0.75\text{ m}$) and mezzanine access stairs (min width $0.90\text{ m}$).</p>
</div>
''',

    'quiz': [
      {
        'question': 'What is the statutory minimum clear headway required under any structural beam in a habitable room under Regulation 9.2.2?',
        'options': [
          '2.10 m',
          '2.20 m',
          '2.40 m',
          '2.75 m'
        ],
        'answer': 2,
        'explanation': 'Regulation 9.2.2 proviso explicitly decrees: "Provided that the minimum head-way under any beam shall be 2.4 m."'
      },
      {
        'question': 'What are the minimum dimensions required for a combined bathroom and water closet under Regulation 9.4.1(iii)?',
        'options': [
          '1.20 sq.m with minimum width of 0.90 m',
          '1.50 sq.m with minimum width of 1.00 m',
          '1.80 sq.m with minimum width of 1.20 m',
          '2.00 sq.m with minimum width of 1.00 m'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.4.1(iii) mandates: "Combined bath room and water closet 1.50 sq.m. with minimum width of 1.00 m."'
      },
      {
        'question': 'Under Table 9-B, what is the maximum percentage coverage permitted for a storage loft over a residential kitchen or habitable room?',
        'options': [
          '25 percent',
          '33.33 percent',
          '50 percent',
          '100 percent'
        ],
        'answer': 0,
        'explanation': 'Table 9-B Item 1 specifies that the maximum coverage of a loft over a kitchen or habitable room is 25% of the room area below.'
      },
      {
        'question': 'Under Regulation 9.7.1 and 9.7.3, what is the maximum permissible area of a mezzanine floor, and is it counted in FSI?',
        'options': [
          '33% of room area, free of FSI',
          '50% of carpet area of that room, and it is strictly counted towards FSI',
          '50% of built-up area, free of FSI if used for storage',
          '25% of carpet area, counted towards FSI'
        ],
        'answer': 1,
        'explanation': 'Regulation 9.7.1 limits the mezzanine floor to 50% of the carpet area of that room, and the Note to 9.7.1 explicitly states: "Mezzanine floor area shall be counted towards FSI."'
      }
    ],

    'prev_url': '/lessons/reg-8-2-2-city-multipliers-and-parking-penalties.html',
    'prev_title': 'Reg 8.2.2 & Table 8-C: City Multipliers, 2-Wheeler Exemption & Surcharges',
    'next_url': '/lessons/reg-9-11-basements-podiums-and-vehicular-ramps.html',
    'next_title': 'Reg 9.11 to 9.16: Basements, Podiums & Vehicular/Pedestrian Ramps'
}
