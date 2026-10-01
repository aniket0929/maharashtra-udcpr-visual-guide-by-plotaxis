"""
UDCPR Chapter 13 - Lesson 13.3: Grey Water Recycling, Dual Plumbing & Solid Waste Management
Statutory Clauses: Regulation 13.4, Regulation 13.5
"""

import sys
sys.path.append('scripts')
from generate_lessons import create_lesson_page

lesson_data = {
    'clause': 'Reg. 13.4 & 13.5',
    'title': 'Grey Water Recycling, Dual Plumbing & Solid Waste Management',
    'meta_desc': 'Chapter 13 environmental engineering rules under UDCPR-2020: Grey Water Recycling thresholds (>= 100 flats, >= 1,500 sqm commercial, >= 40 hospital beds), dual plumbing, 5% property tax rebate, water disconnection penalties, and on-site Organic Waste Composting (OWC >= 4,000 sqm).',
    'ch_slug': 'ch13',
    'ch_title': 'Chapter 13: Special Provisions for Certain Buildings',
    'badge_status': '100% COMPLETE',
    'amendment_cite': None,
    'filename': 'reg-13-3-grey-water-and-solid-waste.html',
    'lesson_id': 'ch13_lesson_3',
    'quiz_id': 'quiz_ch13_3',
    'prev_url': '/lessons/reg-13-2-solar-and-rainwater-harvesting.html',
    'prev_title': 'Reg. 13.2 - 13.3 Solar Rooftop & Rainwater Harvesting',
    'next_url': '/lessons/reg-13-4-disaster-fire-towers-electrical.html',
    'next_title': 'Reg. 13.6 Disaster Resilience & Fire Towers (Oct 2024)',
    'lead_summary': (
        'To prevent municipal sewage overload and promote circular urban metabolism, Maharashtra UDCPR enforces decentralized wastewater '
        'treatment and on-site solid waste processing. Regulation 13.4 establishes non-negotiable thresholds for Grey Water Treatment & Recycling Plants '
        '(GWTP/STP): group housing with 100 or more tenements (150 for EWS/LIG), commercial/educational facilities of 1,500 sq.m or 20,000 litres/day demand, '
        'hospitals with 40 or more beds, and 100% vehicle-wash recycling in garages. Recycled water must feed dual-plumbing networks for toilet flushing, '
        'gardening, and car washing, supported by mandatory 6-month lab testing. Operating societies enjoy a statutory 5% Property Tax rebate, while '
        'non-operating plants face daily fines of Rs. 300 and disconnection of municipal water supplies. Complementing this, Regulation 13.5 makes 100% '
        'on-site wet waste treatment via Organic Waste Composters (OWC) mandatory for all developments exceeding 4,000 sq.m built-up area.'
    ),
    'plain_summary_html': """
      <p>
        Modern municipal scrutiny in Maharashtra treats environmental utilities as critical life-support infrastructure. 
        Regulations 13.4 and 13.5 establish mandatory thresholds, design protocols, fiscal incentives, and punitive enforcement:
      </p>
      <ul style="padding-left: 20px; margin-top: 10px; display:flex; flex-direction:column; gap:8px;">
        <li><strong>Grey Water vs. Black Water Definition (Reg 13.4):</strong> "Grey Water" is specifically defined as wastewater originating from bathrooms, sinks, showers, and wash places. Black water (toilet sewage) must either be treated in a full STP or directed to municipal sewer trunks.</li>
        <li><strong>Statutory Applicability Thresholds (Reg 13.4.1 to 13.4.6):</strong>
          <br>&bull; <em>Large Residential Layouts:</em> Layouts admeasuring <strong>10,000 sq.m or more</strong> must earmark a dedicated plot for a central Grey Water Treatment Plant (which may be accommodated within the Reg. 3.5 Amenity Space).
          <br>&bull; <em>Group Housing &amp; Apartments:</em> Mandatory for any building or complex containing <strong>100 or more tenements</strong> (or <strong>150 or more tenements for EWS / LIG housing</strong>).
          <br>&bull; <em>Commercial, Institutional &amp; Hotels:</em> Mandatory for all educational, commercial, governmental, industrial, and hotel buildings having a built-up area of <strong>1,500 sq.m or more</strong>, OR where daily water consumption reaches <strong>20,000 litres/day</strong>.
          <br>&bull; <em>Hospitals:</em> Mandatory for all healthcare facilities having <strong>40 or more inpatient beds</strong>.
          <br>&bull; <em>Vehicle Servicing Garages:</em> <strong>100% of vehicle-wash wastewater</strong> must be trapped via oil/grease interceptors, treated, and recycled back into the washing cycle.
        </li>
        <li><strong>Permitted Uses &amp; Statutory Agreements (Reg 13.4.1.iii &amp; iv):</strong>
          <br>&bull; <em>Allowed Uses:</em> Toilet flushing, landscape gardening, vehicle washing, and construction curing.
          <br>&bull; <em>Strict Prohibition:</em> In no case can recycled grey water be connected to drinking, bathing, cooking, or clothes-washing fixtures.
          <br>&bull; <em>Agreement Clause:</em> Developer sale agreements must include a binding clause mandating that the society conduct <strong>laboratory testing of recycled water every 6 months</strong> in an approved municipal lab, with test certificates accessible to the Ward Executive Health Officer (EHO).
        </li>
        <li><strong>Carrots &amp; Sticks: Fiscal Incentive vs. Water Disconnection (Reg 13.4.7 &amp; 13.4.8):</strong>
          <br>&bull; <em>Incentive:</em> A permanent <strong>5% rebate in annual Property Tax</strong> is granted to tenement holders and cooperative societies that operate and maintain an active recycling plant.
          <br>&bull; <em>Penalties:</em> Violating bye-laws invites an immediate fine of <strong>Rs. 2,500/-</strong> plus <strong>Rs. 100/- per day</strong> of continuing failure. If the plant is shut down or abandoned, the penalty escalates to <strong>Rs. 300/- per day</strong> plus <strong>immediate physical disconnection of the municipal potable water connection</strong>!
        </li>
        <li><strong>On-Site Solid Waste Management (Reg 13.5):</strong>
          <br>&bull; <em>Mandatory Threshold:</em> Housing complexes, commercial establishments, hostels, and hospitals with aggregate built-up area of <strong>4,000 sq.m or more</strong>, and all <strong>3-star or higher hotels</strong>.
          <br>&bull; <em>100% Wet Waste Composting:</em> Must treat 100% of organic kitchen/wet waste on-site using mechanical <strong>Organic Waste Composters (OWC)</strong> or vermiculture pits installed through reputed vendors.
          <br>&bull; <em>Dry &amp; Hazardous Segregation:</em> Dry waste, e-waste, and sanitary/hazardous waste must be segregated at source and handed over exclusively to authorized municipal recyclers.
        </li>
      </ul>
    """,
    'statutory_extract': (
        "Grey Water - It means waste water from bathrooms, sinks, shower and wash areas, etc... In case of Residential layouts, area admeasuring 10000 sq.m. "
        "or more... a separate space for Grey Water Treatment and Recycling Plant should be proposed... In case of Group Housing scheme or a multi-storeyed "
        "building having 100 or more tenements... In case of EWS / LIG tenements, this shall be provided for tenements 150 or more... "
        "For all above buildings having built-up area 1500 sq.m. or more or if water consumption is 20,000 litre per day... Hospitals having 40 or more beds... "
        "The recycled water is tested every six months... fiscal benefits in Property Tax to the extent of 5%... If any person fails to operate... "
        "penalty of Rs.300/- per day and disconnection of Water connection also... Solid Waste Management: It shall be mandatory for housing complexes, "
        "commercial establishments... having aggregate built up area more than 4,000 sq.m... to treat 100% wet waste through organic waste composters/ vermiculture pits."
    ),
    'clause_cards_html': """
      <div class="ruled-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px;">
        <div class="ruled-card">
          <span class="kicker">REGULATION 13.4.2 &amp; 13.4.3</span>
          <h4 class="ruled-card-title">Residential &amp; Commercial Quotas</h4>
          <p class="ruled-card-desc">
            Mandatory for apartment buildings &ge; 100 tenements (or &ge; 150 EWS/LIG), commercial/educational facilities &ge; 1,500 sq.m BUA 
            (or &ge; 20,000 L/day demand), and healthcare facilities with &ge; 40 hospital beds.
          </p>
          <div class="ruled-card-footer">
            <span>STATUTORY TRIGGER</span>
            <span class="badge badge-status-done">&ge;100 FLATS / &ge;1,500 SQ.M</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 13.4.1</span>
          <h4 class="ruled-card-title">Dual Plumbing &amp; Layout Siting</h4>
          <p class="ruled-card-desc">
            Layouts &ge; 10,000 sq.m must earmark a dedicated plant plot in amenity spaces. 
            Dual-colored plumbing risers must separate recycled water lines (flushing/gardening) from potable drinking supplies.
          </p>
          <div class="ruled-card-footer">
            <span>PLUMBING ISOLATION</span>
            <span class="badge badge-status-done">DUAL RISERS</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 13.4.7 &amp; 13.4.8</span>
          <h4 class="ruled-card-title">5% Tax Rebate vs. Disconnection</h4>
          <p class="ruled-card-desc">
            Active plants earn a 5% Property Tax rebate for society members. Shutting down the plant triggers a 
            Rs. 300/day municipal fine and punitive physical disconnection of the municipal fresh water main.
          </p>
          <div class="ruled-card-footer">
            <span>FISCAL &amp; PUNITIVE</span>
            <span class="badge badge-status-done">5% REBATE / RS.300 FINE</span>
          </div>
        </div>

        <div class="ruled-card">
          <span class="kicker">REGULATION 13.5</span>
          <h4 class="ruled-card-title">On-Site Wet Waste OWC (&ge; 4,000 sq.m)</h4>
          <p class="ruled-card-desc">
            Mandatory for complexes &ge; 4,000 sq.m BUA and 3-star+ hotels. 100% of organic wet waste must be converted 
            on-site via mechanical Organic Waste Composters or vermiculture pits before municipal dry collection.
          </p>
          <div class="ruled-card-footer">
            <span>SOLID WASTE</span>
            <span class="badge badge-status-done">&ge;4,000 SQ.M BUA</span>
          </div>
        </div>
      </div>
    """,
    'plate_or_table_html': """
      <div style="border:1px solid var(--ink); background:var(--paper); padding:20px; margin-top:16px;">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--ink); padding-bottom:8px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <span style="font-family:var(--mono); font-size:12px; font-weight:700; color:var(--blueprint);">PLATE 13-C: GREY WATER RECYCLING &amp; SOLID WASTE MANAGEMENT AUDIT TABLE</span>
          <span class="badge badge-status-done">REG. 13.4 &amp; 13.5</span>
        </div>

        <div style="overflow-x:auto;">
          <table style="width:100%; border-collapse:collapse; font-size:0.86rem; font-family:var(--mono);">
            <thead>
              <tr style="background:var(--paper-raised); border-bottom:1px solid var(--ink);">
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">BUILDING / LAYOUT TYPE</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:160px;">MANDATORY THRESHOLD</th>
                <th style="padding:8px; text-align:left; border-right:1px solid var(--ink-soft); width:180px;">STATUTORY REQUIREMENT</th>
                <th style="padding:8px; text-align:left;">INCENTIVE / PENALTY</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Residential Layout</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Land Area &ge; <strong>10,000 sq.m</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Dedicated plot for centralized GWTP/STP in layout or amenity space.</td>
                <td style="padding:8px;">5% Property Tax rebate if maintained; Rs. 2,500 fine + Rs. 100/day for default.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Group Housing / Apartments</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">&ge; <strong>100 Tenements</strong><br>(&ge; 150 for EWS/LIG)</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Dual plumbing system; 100% recycling to flushing &amp; landscape gardening.</td>
                <td style="padding:8px;">5% Property tax rebate for flats; Rs. 300/day fine + <strong>Water cut-off</strong> if shut down.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Commercial, IT, Hotels &amp; Govt</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">BUA &ge; <strong>1,500 sq.m</strong> OR<br>Water &ge; <strong>20,000 L/Day</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">On-site recycling plant; separate color-coded drainage and supply lines.</td>
                <td style="padding:8px;">Mandatory 6-month lab test submission to Ward EHO; Rs. 300/day fine.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft); background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Hospitals &amp; Healthcare</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">&ge; <strong>40 Inpatient Beds</strong></td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">Grey water treatment with disinfection plant; zero untreated discharge.</td>
                <td style="padding:8px;">Disconnection of municipal water connection if plant operation is abandoned.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--ink-soft);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Automobile Service Garages</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">All vehicle wash centers</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">100% closed-loop vehicle wash water recycling with oil/grease traps.</td>
                <td style="padding:8px;">Immediate revocation of trade license and trade sewer disconnection.</td>
              </tr>
              <tr style="background:var(--paper-raised);">
                <td style="padding:8px; border-right:1px solid var(--ink-soft); font-weight:700; color:var(--blueprint);">Solid Waste Management (OWC)</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">BUA &ge; <strong>4,000 sq.m</strong> OR<br>3-Star+ Hotels</td>
                <td style="padding:8px; border-right:1px solid var(--ink-soft);">100% on-site organic wet waste composting via OWC machines or vermiculture.</td>
                <td style="padding:8px;">Municipal refusal to collect wet garbage; prerequisite for final Occupancy Certificate.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    """,
    'worked_example_html': """
      <p style="font-size:0.92rem; line-height:1.6; margin-bottom:14px;">
        <strong>Scenario:</strong> A residential developer in Thane is designing a gated community consisting of <strong>120 residential apartments</strong> 
        with an aggregate built-up area of <strong>8,500 sq.m</strong>. What are the statutory environmental engineering obligations regarding grey water 
        recycling and solid waste composting?
      </p>
      <div style="background:var(--paper); border:1px solid var(--ink); padding:14px; font-family:var(--mono); font-size:0.86rem; line-height:1.7;">
        <div style="color:var(--blueprint); font-weight:700; margin-bottom:6px;">STATUTORY COMPLIANCE EVALUATION (REG. 13.4 &amp; 13.5):</div>
        <div><strong>Part 1: Grey Water Treatment &amp; Recycling (Reg. 13.4.2)</strong></div>
        <div>&bull; Project Scale = 120 tenements (&gt; 100 tenement threshold) &rarr; <strong>ON-SITE GREY WATER RECYCLING IS COMPULSORY</strong>.</div>
        <div>&bull; Hydraulic Sizing: Under Reg. 12.5, population = 120 flats &times; 5 persons = 600 residents. Total water demand @ 135 lpcd = 81,000 L/day.</div>
        <div>&bull; Estimated Grey Water Generation (~65% of domestic supply) = <strong>~52,600 Litres/Day</strong>.</div>
        <div>&bull; Plant Specification: Minimum 55 KLD (kilolitres per day) secondary treatment plant with chlorination/ozonation.</div>
        <div>&bull; Dual-Plumbing Network: Recycled water must be plumbed via independent purple/green color-coded risers feeding 120 toilet flushing cisterns (~27,000 L/day) and garden irrigation lines.</div>
        <div>&bull; Mandatory Agreement Clause: Flat purchase agreements must incorporate the clause requiring bi-annual water testing in a municipal lab.</div>
        <div style="margin-top:8px;"><strong>Part 2: On-Site Solid Waste Management (Reg. 13.5)</strong></div>
        <div>&bull; Aggregate Built-Up Area = 8,500 sq.m (&gt; 4,000 sq.m threshold) &rarr; <strong>ON-SITE COMPOSTING IS COMPULSORY</strong>.</div>
        <div>&bull; Waste Estimation: 600 residents generating ~0.45 kg MSW/head/day = ~270 kg/day, of which ~60% is organic wet waste (~162 kg/day).</div>
        <div>&bull; Equipment Requirement: Fully automatic Organic Waste Composter (OWC) with minimum 200 kg/day processing capacity, located in a ventilated ground-level utility enclave with anti-rodent flooring.</div>
        <div>&bull; Occupancy Condition: Satisfactory installation and test-run of both the GWTP and OWC are mandatory pre-conditions for the grant of final Occupancy Certificate (OC).</div>
      </div>
    """,
    'pitfalls_html': """
      <div>
        <strong>1. Cross-Connecting Recycled Grey Water to Potable Bathroom Fixtures (Reg 13.4.1.iii):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Plumbing contractors under budget pressure sometimes merge treated grey water lines into domestic overhead distribution loops. Reg. 13.4.1(iii) strictly prohibits recycled water for bathing, clothes-washing, or cooking. Separate color-coded piping and air-gap breaks are mandatory to prevent deadly bacterial backflow.
        </p>
      </div>
      <div>
        <strong>2. Shutting Down the STP / GWTP Post-Possession to Save Electricity (Reg 13.4.8):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Cooperative housing societies often power down their treatment plants to cut maintenance charges. When municipal Ward Health Officers detect un-operated plants, they levy a <strong>Rs. 300/- daily fine and physically disconnect the municipal drinking water supply</strong> until full operational compliance is re-established.
        </p>
      </div>
      <div>
        <strong>3. Forgetting the OWC Mandate for Small Commercial Towers Exceeding 4,000 sq.m (Reg 13.5):</strong>
        <p style="margin:4px 0 0; font-size:0.88rem; color:var(--ink-soft); line-height:1.5;">
          Architects designing 4,200 sq.m commercial office buildings often assume on-site composting only applies to residential colonies or hotels. Regulation 13.5 explicitly applies to <em>"Commercial establishments... having aggregate built up area more than 4,000 sq.m."</em> Omitting the OWC room on ground/basement drawings halts OC issuance.
        </p>
      </div>
    """,
    'amendment_section_html': """
      <p style="font-size:0.92rem; line-height:1.6;">
        Regulations 13.4 and 13.5 operationalize the National Green Tribunal (NGT) and Maharashtra Pollution Control Board (MPCB) 
        mandates on urban sewage treatment and Solid Waste Management Rules, 2016. The 5% Property Tax rebate under Reg. 13.4.7 provides 
        a permanent fiscal incentive that offsets annual electricity and maintenance expenses for conforming cooperative societies.
      </p>
    """,
    'quiz': [
        {
            'question': 'Under UDCPR Regulation 13.4.2, what is the tenement threshold where Grey Water Recycling becomes mandatory for residential apartment buildings?',
            'options': [
                '25 or more tenements',
                '50 or more tenements',
                '100 or more tenements (150 for EWS/LIG)',
                '500 or more tenements'
            ],
            'answer': 2,
            'explanation': 'Regulation 13.4.2 states: "In case of Group Housing scheme or a multi-storeyed building having 100 or more tenements... In case of EWS / LIG tenements, this shall be provided for tenements 150 or more."'
        },
        {
            'question': 'What fiscal incentive is granted to societies that operate and maintain an active Grey Water Recycling Plant under Regulation 13.4.7?',
            'options': [
                '10% additional free FSI',
                '5% rebate in Property Tax to tenement holders / society',
                'Free electricity for pumping',
                'Exemption from stamp duty'
            ],
            'answer': 1,
            'explanation': 'Regulation 13.4.7 provides an incentive in the form of "fiscal benefits in Property Tax to the extent of 5% to Tenement holder / Society."'
        },
        {
            'question': 'What severe administrative penalty can the Authority levy if a society fails to operate its Grey Water Recycling Plant under Regulation 13.4.8?',
            'options': [
                'Demolition of the top floor',
                'Penalty of Rs. 300/- per day and disconnection of municipal water connection',
                'Cancellation of land registration',
                'Imprisonment of all flat owners'
            ],
            'answer': 1,
            'explanation': 'Regulation 13.4.8 explicitly mandates: "he will be charged a penalty of Rs.300/- per day and disconnection of Water connection also."'
        },
        {
            'question': 'Under UDCPR Regulation 13.5, which developments are statutorily required to establish an on-site Solid Waste Management system to treat 100% of wet waste?',
            'options': [
                'Only municipal garbage dump sites',
                'Housing complexes, commercial establishments, hostels, and hospitals >= 4,000 sq.m BUA, and all 3-star+ hotels',
                'Plots smaller than 500 sq.m',
                'Only industrial manufacturing plants'
            ],
            'answer': 1,
            'explanation': 'Regulation 13.5 explicitly mandates 100% wet waste treatment for complexes with built-up area of 4,000 sq.m or more, and all three-star or higher category hotels.'
        }
    ]
}

if __name__ == '__main__':
    create_lesson_page(lesson_data)
