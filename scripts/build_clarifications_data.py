import json
import os

# Curated statutory clarifications directly from ucpr_real.md (Order CR 42/21, CR 44/21, and Sec 154 MRTP Directives)
CLARIFICATIONS = [
    {
        "id": "clarification-14-8-7",
        "clause": "Reg. 14.8.7",
        "chapter_num": 14,
        "chapter": "Chapter 14: Special Schemes",
        "chapter_file": "/chapters/ch14.html",
        "anchor": "clarification-14-8-7",
        "title": "DP Reservations Falling inside Urban Renewal Clusters (URC)",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 17)",
        "ambiguity": "Under Regulation 14.8.7, an Implementing Agency must construct public amenities designated on the Development Plan (e.g. municipal schools, health centers, parking lots) and hand them over free of cost and free of FSI to the Municipal Corporation. Practitioners and developers were deadlocked: Does the agency receive Construction Amenity TDR to recover construction costs, or must they bear 100% of the expenditure without compensation?",
        "ruling": "The Urban Development Department ruled that under Regulation 14.8.14(xvi), any development aspect not expressly barred under URS is governed by general UDCPR provisions. Consequently, for constructing and handing over the built-up amenity area to the Corporation, the Implementing Agency IS STATUTORILY ENTITLED to Construction Amenity TDR under Regulation 11.2.5.",
        "takeaway": "Cluster redevelopment feasibility is protected: building required DP public amenities inside a cluster scheme does not drain capital, as the built area is compensated via market-saleable Construction Amenity TDR under Chapter 11.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-14-4-1",
        "clause": "Reg. 14.4.1",
        "chapter_num": 14,
        "chapter": "Chapter 14: Special Schemes",
        "chapter_file": "/chapters/ch14.html",
        "anchor": "clarification-14-4-1",
        "title": "PMAY Affordable Housing: Basic FSI vs Road Potential Stacking",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 13)",
        "ambiguity": "Prior to UDCPR, PMAY schemes received a flat 2.50 FSI on roads 15m or wider. Under UDCPR 14.4.1 Condition 3, permissible FSI is capped at maximum building potential under Reg 6.1 or 6.3 subject to max 2.5 treated as allowable basic FSI without premium or TDR. Planners were confused about road width thresholds and whether potential beyond 2.5 could be loaded.",
        "ruling": "The Government clarified that: (1) In congested areas (Table 6-A), max 2.50 FSI is permissible on minimum 9.0m roads; (2) In non-congested areas (Table 6-G), max 2.50 FSI is permissible on minimum 15.0m roads. Any residual building potential above 2.50 permitted by road width can still be availed by paying Premium FSI or loading TDR.",
        "takeaway": "PMAY projects enjoy 2.50 free basic FSI without paying premium or TDR charges on >=9m roads in gaothan or >=15m outside gaothan. If the road allows higher potential (e.g. 3.00 FSI on 24m road), the top 0.50 FSI can be unlocked via standard premium/TDR.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-6-3-xii",
        "clause": "Reg. 6.3 (Note xii)",
        "chapter_num": 6,
        "chapter": "Chapter 6: General Building Requirements",
        "chapter_file": "/chapters/ch06.html",
        "anchor": "clarification-6-3-xii",
        "title": "Point Access & Dead-End Roads: Building Potential vs Building Height",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 16)",
        "ambiguity": "Table 6-G Note (xii) allows plots accessed via a dead-end road (point access) <= 100m in length to enjoy the full FSI potential of the main road. Architects assumed this meant they could also build high-rise towers up to unlimited height, ignoring access widths required for fire engines.",
        "ruling": "The Government ruled that while FSI potential is derived from the main road, building height is NOT unrestricted. Permissions must jointly comply with Reg 3.3.9 (Special Building access width), Reg 6.10.1 (general height limitations), and for Pune Municipal Corporation, Reg 10.1.1 specific height ceilings. Fire tender maneuverability cannot be compromised.",
        "takeaway": "You can get high FSI from the arterial road on a short cul-de-sac (<=100m), but your structure's vertical height is still strictly bounded by physical access width and CFO fire tender road norms.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-6-3-xiv",
        "clause": "Reg. 6.3 (Note xiv)",
        "chapter_num": 6,
        "chapter": "Chapter 6: General Building Requirements",
        "chapter_file": "/chapters/ch06.html",
        "anchor": "clarification-6-3-xiv",
        "title": "Gross vs Net Plot Area for Calculating Premium FSI & TDR Potential",
        "order_ref": "Order No. CR 236/18 (Part 2) dt. 17th September, 2021",
        "ambiguity": "When a plot loses land to DP road widening, public reservations, or mandatory amenity space handed over to the Authority, should Premium FSI and TDR loading caps be calculated on the original gross plot area or the net balance plot area?",
        "ruling": "The Government clarified that Basic FSI is calculated strictly on the net plot remaining with the owner after deducting surrendered areas. However, the ENTIRE gross area of the plot may be considered for calculating permissible Premium FSI + TDR potential, provided the reservation or amenity space was handed over to the Authority.",
        "takeaway": "Land surrendered for public amenities or road widening is not a total FSI loss: the owner retains the legal right to load Premium FSI and TDR over the surrendered area onto their remaining net land parcel.",
        "date": "17/09/2021"
    },
    {
        "id": "clarification-6-2-3-a",
        "clause": "Reg. 6.2.3(a)",
        "chapter_num": 6,
        "chapter": "Chapter 6: General Building Requirements",
        "chapter_file": "/chapters/ch06.html",
        "anchor": "clarification-6-2-3-a",
        "title": "Front Margins for Special Buildings vs High-Rise Height Formulas",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 8)",
        "ambiguity": "For buildings taller than standard height, Reg 6.2.3 requires increasing margins. Municipal officers were demanding that the front road setback also be stepped back proportionally to building height, breaking street building lines.",
        "ruling": "The Government clarified that for Special Buildings, front margin shall be strictly as specified in Table 6-D IRRESPECTIVE of building height to maintain a uniform street line. However, side and rear marginal distances must strictly provide a minimum 6.0m clear motorable access way for fire appliances as per Reg 2.2.8(a) and Reg 3.3.9.",
        "takeaway": "Front setbacks follow the road width table uniformly so your facade aligns with the street; side and rear setbacks must maintain the mandatory 6.00m unobstructed fire-fighting ring corridor.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-6-2-3-b",
        "clause": "Reg. 6.2.3(b)",
        "chapter_num": 6,
        "chapter": "Chapter 6: General Building Requirements",
        "chapter_file": "/chapters/ch06.html",
        "anchor": "clarification-6-2-3-b",
        "title": "Exemption of Stilt Parking Height When Housing Society Amenities",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 9)",
        "ambiguity": "Reg 6.2.3(b) allows stilt parking height up to 6.0m to be deducted when calculating overall building height for marginal distances. Scrutiny officers objected when developers placed mandatory society amenities (fitness center, crèche, society office, driver's room under Reg 9.31) in part of the stilt, claiming the stilt was no longer purely parking.",
        "ruling": "The Government clarified that amenities permitted under Regulation 9.31(i) to (iii) located within part of the parking stilt are considered ancillary to parking. Therefore, stilt height up to 6.0m continues to be excluded when measuring building height for marginal distances.",
        "takeaway": "Locating society offices, gyms, driver restrooms, or daycare rooms in the stilt floor under Reg 9.31 does not disqualify the 6m height exemption for marginal distance calculations.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-2-2-13-transfer",
        "clause": "Reg. 2.2.13",
        "chapter_num": 2,
        "chapter": "Chapter 2: Development Permissions",
        "chapter_file": "/chapters/ch02.html",
        "anchor": "clarification-2-2-13-transfer",
        "title": "Transferability of Development Charges on Land Sale",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 3)",
        "ambiguity": "When an earlier development permission lapsed and the plot was sold to a new buyer, municipal corporations demanded fresh development charges under Sec 124A from the new buyer, refusing to credit payments made by the prior owner.",
        "ruling": "The Government ruled that Development Charges under Section 124A of the MRTP Act, 1966 attach to the development and the land parcel, NOT to the individual applicant. Even if the land is sold, the new owner is entitled to full adjustment/credit of all previously deposited development charges when applying for revised permission.",
        "takeaway": "Development charges run with the land. A new buyer or developer does not have to repay charges already remitted for approved built-up areas.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-2-2-13-pline",
        "clause": "Reg. 2.2.13(ii)",
        "chapter_num": 2,
        "chapter": "Chapter 2: Development Permissions",
        "chapter_file": "/chapters/ch02.html",
        "anchor": "clarification-2-2-13-pline",
        "title": "Levy of Development Charges on Total P-Line Built-Up Area",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 15)",
        "ambiguity": "Controversy existed regarding whether Sec 124A development charges should be assessed only on Basic FSI, or on Ancillary FSI, or on total gross slab area including balconies and passages.",
        "ruling": "The Government clarified that Section 124A requires charges on all development requiring permission. In UDCPR, development charges must be levied on the entire built-up area encompassed within the P-line (which includes Ancillary FSI), categorized according to the principal use of land and building.",
        "takeaway": "Budget for statutory development charges against the entire P-line construction envelope, including all Ancillary FSI components.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-2-2-14",
        "clause": "Reg. 2.2.14",
        "chapter_num": 2,
        "chapter": "Chapter 2: Development Permissions",
        "chapter_file": "/chapters/ch02.html",
        "anchor": "clarification-2-2-14",
        "title": "50:50 Apportionment of Premium Charges to State Government",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 4)",
        "ambiguity": "Several UDCPR regulations (e.g. Table 6-G Note viii) state that premium sharing between the Planning Authority and Government shall be 'as decided by Government from time to time.' Authorities retained 100% of the funds in the absence of explicit local circulars.",
        "ruling": "The Government directed that wherever a specific percentage is not explicitly stated in any regulation, 50% of all premium charges recovered by the Authority must be deposited with the State Government pursuant to Regulation 2.2.14.",
        "takeaway": "All statutory premiums (Premium FSI, special user conversions) are uniformly split 50% to the Local Planning Authority civic infrastructure fund and 50% to the State Government exchequer.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-2-7-1",
        "clause": "Reg. 2.7.1",
        "chapter_num": 2,
        "chapter": "Chapter 2: Development Permissions",
        "chapter_file": "/chapters/ch02.html",
        "anchor": "clarification-2-7-1",
        "title": "Statutory Commencement in Multi-Building Group Housing Schemes",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 5)",
        "ambiguity": "Under Reg 2.7.1, commencement requires work up to plinth level within 1 year. For township and group housing schemes containing 10-20 towers, authorities were declaring permissions lapsed for buildings that had not reached plinth individually within the first year.",
        "ruling": "The Government clarified that a group housing layout has a single integrated development permission. It is impossible to begin all towers simultaneously. Completing the plinth of ANY single building within the valid period constitutes statutory commencement for the ENTIRE scheme, and the sanction does not lapse partially or building-by-building.",
        "takeaway": "Achieving plinth level on Phase 1 / Tower 1 legally protects the entire approved multi-tower master layout against statutory lapsing.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-2-2-12",
        "clause": "Reg. 2.2.12",
        "chapter_num": 2,
        "chapter": "Chapter 2: Development Permissions",
        "chapter_file": "/chapters/ch02.html",
        "anchor": "clarification-2-2-12",
        "title": "Remittance of Scrutiny Fees in Regional Plan Gaothan Areas",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 2)",
        "ambiguity": "In Regional Plan jurisdictions, Section 18(1)(ii) empowers Gram Panchayats to issue gaothan permissions with Town Planning approval. Applicants were confused about whether scrutiny fees should be paid to the Gram Panchayat or the District Town Planning Office.",
        "ruling": "The Government clarified that because dedicated Town Planning cadres are not yet deployed at the Zilla Parishad / Panchayat Samiti level, scrutiny is conducted by the District Branch Office of the Town Planning and Valuation Department. Scrutiny fees must be deposited directly with the District Town Planning Office.",
        "takeaway": "For rural and gaothan layouts in Regional Plan areas, pay scrutiny fees directly to the District ADTP/DDTP branch office that performs technical plan examination.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-3-3-8-b",
        "clause": "Reg. 3.3.8(b)",
        "chapter_num": 3,
        "chapter": "Chapter 3: Land Sub-division and Layout",
        "chapter_file": "/chapters/ch03.html",
        "anchor": "clarification-3-3-8-b",
        "title": "Classified Highway Road Widths: DP / RP Width vs UDCPR Table",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 6)",
        "ambiguity": "Disputes arose when the Development Plan or Regional Plan showed a State Highway with a planned widening of 30m, but Reg 3.3.8(b) listed standard State Highways as 45m. Planners argued over which width took legal precedence.",
        "ruling": "The Government ruled that where the DP, RP, Planning Proposal, or Town Planning Scheme explicitly indicates an existing or widening road width, that statutory DP/RP width strictly prevails. The standard widths in Table 3.3.8(b) (e.g. 45m for SH, 60m for NH) apply ONLY if no road width is designated on the sanctioned statutory plan.",
        "takeaway": "Sanctioned DP/RP road lines always supersede UDCPR default classified road widths.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-4-11-ix",
        "clause": "Reg. 4.11(ix)",
        "chapter_num": 4,
        "chapter": "Chapter 4: Permissible Uses Across Zones",
        "chapter_file": "/chapters/ch04.html",
        "anchor": "clarification-4-11-ix",
        "title": "Farm Houses in Agricultural Zones: Separate Accessory Structures",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 7)",
        "ambiguity": "Regulation 4.11(ix) allows one farmhouse per holding with FSI 0.04 up to max 400 sqm. Authorities insisted that all built area—including cattle sheds, tractor/implement garages, and fertilizer stores—must be joined under one single roof/building.",
        "ruling": "The Government clarified that farming operations require separating human dwelling from cattle barns, agro-equipment, and crop storage. The allowable 400 sqm built-up area does NOT need to be in a single building; the residential farmhouse and separate accessory agricultural buildings are permissible across the plot holding.",
        "takeaway": "You can design a separate farmhouse residence and detached farm shed/barn, provided total aggregate built-up area remains within 400 sq.m. and FSI 0.04.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-4-8-1-xvi",
        "clause": "Reg. 4.8.1(xvi)",
        "chapter_num": 4,
        "chapter": "Chapter 4: Permissible Uses Across Zones",
        "chapter_file": "/chapters/ch04.html",
        "anchor": "clarification-4-8-1-xvi",
        "title": "Inclusive Housing in Industrial-to-Residential Conversions",
        "order_ref": "Order No. CR 72/23/UD-12 dt. 25th August, 2023",
        "ambiguity": "When converting obsolete industrial land to residential or commercial use, developers asked whether standard 20% Inclusive Housing under Regulation 3.8 applies as land surrender or tenement quota.",
        "ruling": "The Government clarified that regular Regulation 3.8 surrender does not apply directly. Instead, 20% of the land or FSI proposed for residential use must be earmarked for small plots (<100 sq.m.) in plotted layouts or affordable tenements (<50 sq.m. built-up) in group housing.",
        "takeaway": "Industrial zone conversions carry an inescapable affordable housing mandate: allocate at least 20% of residential potential to units under 50 sq.m.",
        "date": "25/08/2023"
    },
    {
        "id": "clarification-9-13",
        "clause": "Reg. 9.13",
        "chapter_num": 9,
        "chapter": "Chapter 9: General Building Requirements - Parts of Building",
        "chapter_file": "/chapters/ch09.html",
        "anchor": "clarification-9-13",
        "title": "Podium Setbacks for Special Buildings vs Non-Special Buildings",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 10)",
        "ambiguity": "Regulation 9.13(ii) requires a 6m distance from plot boundaries for podiua in Special Buildings. Clarification was sought on whether the front margin must also be 6m or if Table 6-D applies.",
        "ruling": "The Government clarified that for Special Buildings, the front setback for a parking podium is governed by Table 6-D front margin, while side and rear boundaries must leave minimum 6.0m clear for fire tenders. For Non-Special Buildings, regular marginal setbacks under the regulations apply.",
        "takeaway": "Podiums can align with the Table 6-D front building line, but must step back at least 6.00m on all side and rear edges for high-rise fire circulation.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-9-27-1",
        "clause": "Reg. 9.27.1 & 9.29.8",
        "chapter_num": 9,
        "chapter": "Chapter 9: General Building Requirements - Parts of Building",
        "chapter_file": "/chapters/ch09.html",
        "anchor": "clarification-9-27-1",
        "title": "Fire Lift Requirement for Buildings Between 15m and 24m Height",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 11)",
        "ambiguity": "For mid-rise buildings between 15m and 24m height, scrutiny officers insisted on two separate lifts (one passenger lift AND one dedicated fire lift), increasing core costs and structural load for smaller developments.",
        "ruling": "The Government clarified that for buildings between 15.0m and 24.0m height, providing ONE fire lift is mandatory. An additional passenger lift is NOT required by law for this height category, provided Fire CFO NOC is secured.",
        "takeaway": "Mid-rise buildings (15m to 24m) can operate with a single high-spec Fire Lift serving daily passenger traffic as well as emergency evacuation.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-9-28-8",
        "clause": "Reg. 9.28.8",
        "chapter_num": 9,
        "chapter": "Chapter 9: General Building Requirements - Parts of Building",
        "chapter_file": "/chapters/ch09.html",
        "anchor": "clarification-9-28-8",
        "title": "1.20m Staircase Width Relief for Existing Buildings Crossing 24m",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 12)",
        "ambiguity": "When an existing sanctioned building with a 1.20m staircase sought vertical expansion using newly available UDCPR FSI, the height exceeded 24m, triggering a requirement for a 1.50m wide staircase under Table 9-G. Relocating existing load-bearing RCC columns was physically impossible.",
        "ruling": "The Government provided hardship relief: If floor-wise gross built area is under 750 sq.m. and occupant load calculations support egress, the existing 1.20m staircase is permissible above 24m, PROVIDED an independent external fire escape staircase is provided.",
        "takeaway": "Brownfield vertical extensions above 24m are not killed by RCC staircase columns if floor plates are <=750 sqm and an external fire staircase is installed.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-10-4-1",
        "clause": "Reg. 10.4.1",
        "chapter_num": 10,
        "chapter": "Chapter 10: Special Provisions for Specified Authorities",
        "chapter_file": "/chapters/ch10.html",
        "anchor": "clarification-10-4-1",
        "title": "NMRDA Outer Ring Road 250m Corridor Development Premium",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 1)",
        "ambiguity": "Regulation 10.4.1 allows development within the 250m residential belt along Nagpur's 60m Outer Ring Road subject to payment of premium 'as decided by Government.' Inquiries arose on what specific percentage must be charged.",
        "ruling": "The Government clarified that the 15% land valuation premium previously sanctioned under Order TPS-2416/CR 122(Part-3)/2016/UD-9 dt. 20/11/2018 remains applicable.",
        "takeaway": "Development permissions in the NMRDA 250m Outer Ring Road corridor require a 15% land rate premium payable to the Authority.",
        "date": "14/06/2021"
    },
    {
        "id": "clarification-11-2-6",
        "clause": "Reg. 11.2.6",
        "chapter_num": 11,
        "chapter": "Chapter 11: Transferable Development Rights (TDR)",
        "chapter_file": "/chapters/ch11.html",
        "anchor": "clarification-11-2-6",
        "title": "Road Width Eligibility for TDR Loading: 9.0m vs 12.0m Corridors",
        "order_ref": "Order No. CR 44/21 dt. 10th June, 2021 & CR 42/21",
        "ambiguity": "Conflicts occurred across municipal corporations regarding whether plots fronting 9.0m roads were eligible for TDR loading, or if TDR was restricted only to roads 12.0m and wider.",
        "ruling": "The Government clarified the permissible TDR caps aligned with Table 6-A (congested) and Table 6-G (non-congested). In non-congested areas, roads below 9.0m cannot load TDR; 9.0m to <12.0m roads can utilize limited TDR up to the permissible cap in Table 6-G.",
        "takeaway": "TDR cannot be loaded on roads below 9.0m in non-congested areas. Road width strictly governs maximum permissible TDR generation and utilization.",
        "date": "10/06/2021"
    },
    {
        "id": "clarification-c-7",
        "clause": "Appendix C (Reg C-7)",
        "chapter_num": 15,
        "chapter": "Chapter 15: Appendices (Appendix C)",
        "chapter_file": "/chapters/ch15.html",
        "anchor": "clarification-c-7",
        "title": "Uniform Statewide Licensing Fees for Technical Personnel (BPMS)",
        "order_ref": "Order No. CR 42/21/UD 12 dt. 14th June, 2021 (Item 14)",
        "ambiguity": "Several Municipal Corporations (e.g. PMC, PCMC, TMC) had passed local general body resolutions charging exorbitant annual licensing fees from architects and structural engineers, far exceeding UDCPR rates.",
        "ruling": "The Government directed that with statewide implementation of the online BPMS (Building Plan Management System), uniform standards must prevail. Local authorities are strictly prohibited from charging licensing fees higher than the statutory fees in Reg C-7.2 (Rs. 3,000 for 3 years for Architects/Engineers/Planners; Rs. 1,500 for Supervisors).",
        "takeaway": "Architects licensed with the Town Planning Department are licensed across Maharashtra. Municipalities cannot charge arbitrary local registration levies beyond UDCPR Appendix C.",
        "date": "14/06/2021"
    }
]

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Save to data/clarifications.json
    clarifications_path = os.path.join(base_dir, 'data', 'clarifications.json')
    with open(clarifications_path, 'w', encoding='utf-8') as f:
        json.dump(CLARIFICATIONS, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {len(CLARIFICATIONS)} curated clarifications to {clarifications_path}")

    # Also update data/amendments.json with enriched data
    # Format each into an amendment card
    amendments = []
    for item in CLARIFICATIONS:
        amendments.append({
            "clause": item["clause"],
            "title": item["title"],
            "chapter": item["chapter"],
            "chapter_num": item["chapter_num"],
            "chapter_file": item["chapter_file"],
            "anchor": item["anchor"],
            "order_ref": item["order_ref"],
            "ambiguity": item["ambiguity"],
            "ruling": item["ruling"],
            "takeaway": item["takeaway"],
            "citation": f"{item['order_ref']} • {item['clause']}",
            "impact_summary": f"{item['ambiguity']} Ruling: {item['ruling']}",
            "occurrences_count": 1,
            "date": item["date"]
        })

    amendments_path = os.path.join(base_dir, 'data', 'amendments.json')
    with open(amendments_path, 'w', encoding='utf-8') as f:
        json.dump(amendments, f, indent=2, ensure_ascii=False)
    print(f"Successfully updated {len(amendments)} records in {amendments_path}")

if __name__ == '__main__':
    main()
