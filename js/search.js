/**
 * UDCPR From Scratch - Client-Side Instant Search Engine
 * Full indexing across all 76 Core Blueprint Lessons (Chapters 1-15 Complete), 141 Glossary Definitions,
 * 9 Master Formulas, 79 Amendments (#), and Practical Topic Workbenches.
 */

(function () {
  'use strict';

  let searchIndex = [];
  let isLoaded = false;

  async function initSearchIndex() {
    if (isLoaded) return;
    try {
      // 1. Index All 15 Core Curriculum Lessons (Chapters 1-3)
      const coreLessons = [
        // Chapter 1
        {
          type: 'lesson',
          title: 'Extent, Jurisdiction & Operational Scope of UDCPR',
          badge: 'Reg. 1.0, 1.1, 1.2 & 1.4',
          snippet: 'Territorial scope across Maharashtra, 9 excluded special areas (MCGM, MIDC, NAINA), TPS rules, and part reconstruction.',
          url: '/lessons/reg-1-1-jurisdiction-and-extent.html'
        },
        {
          type: 'lesson',
          title: 'Statutory Definitions Compendium & Six Critical Distinctions',
          badge: 'Reg. 1.3',
          snippet: 'FSI vs Built-Up Area vs RERA Carpet, Gross vs Net Plot, 15m High-Rise threshold, Gaothan vs Non-Gaothan, TDR.',
          url: '/lessons/reg-1-3-statutory-definitions.html'
        },
        {
          type: 'lesson',
          title: 'Savings Clause, Migration to UDCPR & Balance Potential Math',
          badge: 'Reg. 1.5',
          snippet: 'Option A in-toto vs Option B migration, 1-year lapsing, 3-year extension ceiling, Ancillary FSI on balance area only.',
          url: '/lessons/reg-1-5-savings-and-interpretation.html'
        },
        {
          type: 'lesson',
          title: 'Legal Hierarchy, ASR Timing & Government Clarifications',
          badge: 'Reg. 1.6 to 1.10',
          snippet: 'CRZ overrides, Main Regulations prevailing over Appendices, ASR rate of year of grant, English text supremacy.',
          url: '/lessons/reg-1-6-legal-hierarchy-and-interpretations.html'
        },

        // Chapter 2
        {
          type: 'lesson',
          title: 'Development Permission Mandate, Exemptions & Operational Works',
          badge: 'Reg. 2.1',
          snippet: '16 statutory exemptions (solar <= 1.8m, drywall partitions, labor camps, agro-tourism), operational railways/metro vs non-exempt staff quarters.',
          url: '/lessons/reg-2-1-development-permission.html'
        },
        {
          type: 'lesson',
          title: 'Application Procedure, Drawing Standards, Special Buildings & Clearances',
          badge: 'Reg. 2.2.1 – 2.2.11',
          snippet: 'Appendix A-1/A-2, 7/12 & Mojni verification (< 6 months), drawing scales (1:4000, 1:500, 1:100), Special Buildings (>=15m) fire driveway, Table 2-A & 2-B.',
          url: '/lessons/reg-2-2-application-procedure.html'
        },
        {
          type: 'lesson',
          title: 'Scrutiny Fees, Development Charges & Premium Infrastructure Levies',
          badge: 'Reg. 2.2.12 – 2.2.14',
          snippet: 'Tiered scrutiny fees, Sec 124 MRTP Development Charges, 50:50 premium FSI revenue split, 8.5% interest installment schedule.',
          url: '/lessons/reg-2-2-fees-and-charges.html'
        },
        {
          type: 'lesson',
          title: 'Discretionary Powers, Hardship Relaxations & Drafting Errors',
          badge: 'Reg. 2.3, 2.4 & 2.5',
          snippet: '50% split-zone rule, demonstrable hardship relaxations (JDTP consultation in councils), strict prohibition on relaxing Road Setbacks, FSI, or Parking.',
          url: '/lessons/reg-2-3-discretionary-powers-and-relaxations.html'
        },
        {
          type: 'lesson',
          title: 'Sanction Timelines, Deemed Permission, Plinth Checking & Occupancy',
          badge: 'Reg. 2.6 – 2.15',
          snippet: '60-day sanction deadline, Deemed Permission mechanics, CC validity (1 year, max 4, perpetual on plinth), QR code board, Appendix F, G & H.',
          url: '/lessons/reg-2-6-commencement-and-occupancy.html'
        },

        // Chapter 3
        {
          type: 'lesson',
          title: 'Site Requirements & Statutory Clearance Buffers',
          badge: 'Reg. 3.1',
          snippet: 'River flood lines (Blue Prohibitive vs Red Restrictive Plinth +0.45m), Table 3-1 high-tension lines, railway 30m buffer, prison offsets, and airport CCZM.',
          url: '/lessons/reg-3-1-site-clearance-buffers.html'
        },
        {
          type: 'lesson',
          title: 'Means of Access, Internal Layout Roads & Special Building Driveways',
          badge: 'Reg. 3.2 & 3.3',
          snippet: 'Table 3A residential widths (9m/12m/15m), Table 3C group housing (7.5m/9m/12m), 9.0m cul-de-sac turning circle, junction splays, and road handover.',
          url: '/lessons/reg-3-3-internal-layout-roads.html'
        },
        {
          type: 'lesson',
          title: 'Recreational Open Space (ROS) & Clubhouse Construction',
          badge: 'Reg. 3.4',
          snippet: '0.40 Ha threshold, mandatory 10% ROS quota, pocket geometry (min 400 sq.m, 15m width, 2.5:1 ratio), 10% clubhouse footprint (G+1, 3m margin).',
          url: '/lessons/reg-3-4-1-recreational-open-space.html'
        },
        {
          type: 'lesson',
          title: 'Amenity Space Surrender, Electric Substations & Plot Standards',
          badge: 'Reg. 3.5, 3.6 & 3.7',
          snippet: '20,000 sq.m threshold, 5% quota in Municipal Corporations, 12.0m road access mandate, 100% in-situ FSI/TDR surrender credit, substations (Reg 3.6).',
          url: '/lessons/reg-3-5-amenity-space-provision.html'
        },
        {
          type: 'lesson',
          title: 'Inclusive Housing (20% Affordable EWS/LIG Quota)',
          badge: 'Reg. 3.8',
          snippet: '4,000 sq.m plot threshold in Municipal Corporations, 20% Basic FSI quota for EWS/LIG, 30-45 sq.m carpet sizes, and +25% developer incentive FSI.',
          url: '/lessons/reg-3-8-inclusive-housing.html'
        },
        {
          type: 'lesson',
          title: 'Net Plot Area Computation, In-situ FSI, DP Realignments & Amalgamation',
          badge: 'Reg. 3.9 – 3.13',
          snippet: 'Net Plot Area formula, non-deduction of 10% Recreational Open Space from FSI base, 100% in-situ FSI for DP surrender, 100m realignment limit.',
          url: '/lessons/reg-3-9-net-plot-area-computation.html'
        },

        // Chapter 4
        {
          type: 'lesson',
          title: 'Zoning Classification & Residential Zones (R-1 vs. R-2)',
          badge: 'Reg. 4.1 – 4.6',
          snippet: 'Road width thresholds (<12m R1 vs >=12m R2), home occupations up to 1 H.P., 50 sqm professional offices, 20-bed maternity home access.',
          url: '/lessons/reg-4-1-residential-zones-r1-r2.html'
        },
        {
          type: 'lesson',
          title: 'Commercial & Industrial Zones: Permissible Uses & Buffer Envelopes',
          badge: 'Reg. 4.7 – 4.9',
          snippet: 'Commercial C-Zone, Industrial I-Zone, mandatory 23.0m industrial buffer strip to residential zones (not deducted from FSI), 25% worker housing.',
          url: '/lessons/reg-4-7-commercial-and-industrial-zones.html'
        },
        {
          type: 'lesson',
          title: 'Industrial-to-Residential (I-to-R) Conversion Masterclass',
          badge: 'Reg. 4.8.1',
          snippet: '5% ASR land value conversion premium, Labour Commissioner NOC, 10%/15% tiered amenity surrender, 5% built-up option, Inclusive Housing exemption.',
          url: '/lessons/reg-4-8-1-industrial-to-residential-conversion.html'
        },
        {
          type: 'lesson',
          title: 'Agricultural & Green Zones: Farmhouses & Permissible Non-Agri Uses',
          badge: 'Reg. 4.11',
          snippet: 'Farmhouse rules (0.40 Ha min, 0.04 FSI, 400 sqm ceiling, G+1), 44+ permissible non-agricultural uses, 1.00 FSI institutional campuses, solar farms.',
          url: '/lessons/reg-4-11-agricultural-and-green-zone.html'
        },
        {
          type: 'lesson',
          title: 'Environmental Buffers, Hill Slopes & Special Purpose Zones',
          badge: 'Reg. 4.12 – 4.25',
          snippet: 'River protection green belts (15m river / 9m nallah buffer), non-buildable HTHS slopes > 1:5 gradient, Afforestation forest houses (150 sqm), Defence NOC.',
          url: '/lessons/reg-4-12-environmental-and-special-zones.html'
        },
        {
          type: 'lesson',
          title: 'Public / Semi-Public Zones & Development Plan (DP) Reservations',
          badge: 'Reg. 4.10 & 4.27',
          snippet: 'P/SP campus regulations, 15% basic FSI ancillary commercial allowance, 15% max ground coverage on playground reservations, under-stand stadium shops.',
          url: '/lessons/reg-4-27-public-semi-public-and-dp-reservations.html'
        },

        // Chapter 5
        {
          type: 'lesson',
          title: 'Gaothan Expansion Scheme & Peri-Urban Development Belts',
          badge: 'Reg. 5.1.1',
          snippet: 'Village expansion belts (500m/1500m), 2.0km municipal corporation buffers, 15% ASR premium, 50% gut rule, personal house exemptions.',
          url: '/lessons/reg-5-1-gaothan-expansion-scheme.html'
        },
        {
          type: 'lesson',
          title: 'Committed Development, Station Belts & RP Amenity Space',
          badge: 'Reg. 5.1.3 – 5.1.9 & 5.11',
          snippet: 'Grandfathered pre-RP layouts without premium, 10% RP amenity space on plots >4,000 sqm with in-situ FSI, 500m railway station development.',
          url: '/lessons/reg-5-1-8-rp-amenity-and-infrastructure.html'
        },
        {
          type: 'lesson',
          title: 'Konkan Coastal Regional Plans: Ratnagiri, Sindhudurg & Raigad',
          badge: 'Reg. 5.3 & 5.7',
          snippet: 'Sindhudurg tourism zones T-1 to T-5 (G+1 height cap), CRZ overlays, Raigad 1.0 km coastal wadi land safeguards, 200m Sindhudurg gaothan cap.',
          url: '/lessons/reg-5-3-konkan-coastal-regional-plans.html'
        },
        {
          type: 'lesson',
          title: 'Western Ghats, Hill Stations & High Altitude Zones (>1000m MSL)',
          badge: 'Reg. 5.5 & 5.9',
          snippet: 'Mahabaleshwar-Panchgani 2.5km buffer, Sahyadri Tiger Project, Satara >1000m MSL (Appendix O), Pune Sector-R min 500 sqm villa plots.',
          url: '/lessons/reg-5-5-western-ghats-and-hill-stations.html'
        },
        {
          type: 'lesson',
          title: 'District-Specific Regional Plans: Kolhapur, LIGO Hingoli & Marathwada',
          badge: 'Reg. 5.4, 5.6 & 5.12',
          snippet: 'Kolhapur committed textile layouts, LIGO-India gravitational wave observatory vibration quiet zone in Hingoli, Atomic Energy rules.',
          url: '/lessons/reg-5-4-special-regional-plans.html'
        },
        {
          type: 'lesson',
          title: 'FSI Stacking, Premium FSI & TDR Building Potential',
          badge: 'Reg. 6.1 & 6.3',
          snippet: 'Table 6-A & 6-G stacking pyramid, 35% unguided ASR premium levy, TDR caps, mandatory 30%–50% Slum TDR, Note (xiv) gross vs net plot area.',
          url: '/lessons/reg-6-1-fsi-stacking-and-building-potential.html'
        },
        {
          type: 'lesson',
          title: 'Ancillary Area FSI (60% Res / 80% Non-Res) & P-Line Accounting',
          badge: 'Reg. 6.3 Note (i) & 6.6',
          snippet: 'Abolishing free-of-FSI loopholes: 60% residential / 80% commercial ancillary quota, 10%–15% ASR premium, floor-by-floor P-line measurement.',
          url: '/lessons/reg-6-3-ancillary-area-fsi.html'
        },
        {
          type: 'lesson',
          title: 'Front Road Setbacks & Street Alignments',
          badge: 'Reg. 6.1.1(ii) & 6.2.1',
          snippet: 'Table 6-B congested lane widenings (2.25m from centerline), Table 6-D road hierarchy (3.0m, 4.5m, 6.0m), multi-street corner plots, height-invariance.',
          url: '/lessons/reg-6-2-front-setbacks-and-street-alignments.html'
        },
        {
          type: 'lesson',
          title: 'Side & Rear Margins, Building Separation & The H/5 Rule',
          badge: 'Reg. 6.1.1(iii), 6.2.3 & 6.2.4',
          snippet: 'H/5 high-rise setback formula, statutory 12.0m plot boundary cap, parking floor deductions up to 6.0m, taller building separation, dead-wall reductions.',
          url: '/lessons/reg-6-2-3-side-rear-margins-and-h5-rule.html'
        },
        {
          type: 'lesson',
          title: 'Permissible Projections, FSI Exclusions & Fire Driveways',
          badge: 'Reg. 6.4, 6.7 & 6.8',
          snippet: '0.75m chajjas, 5m x 2.5m canopies, 1.2m ottas, watchman booths, 100% FSI exclusions (parking podiums, service floors <= 1.8m), 6.0m fire driveways.',
          url: '/lessons/reg-6-7-projections-fsi-exclusions-and-fire-driveways.html'
        },
        {
          type: 'lesson',
          title: 'Building Height Limitations, Chowks & Special Amenities',
          badge: 'Reg. 6.9 to 6.15',
          snippet: 'CFO clearance, 70m/50m height caps, 12m road requirement for > 24m, interior/exterior chowks (H/6)^2, zero-FSI recreational floors, Hirkani Kaksha.',
          url: '/lessons/reg-6-10-height-caps-chowks-and-special-floors.html'
        },
        {
          type: 'lesson',
          title: 'Higher FSI for Institutional, Medical & Special Uses (Table 7-A)',
          badge: 'Reg. 7.0 & 7.1',
          snippet: 'Table 7-A concessions: schools (5% premium), charitable hospitals (10% premium, 3.00 FSI), starred hotels (20% with 1-step road width bonus), zero amenity space.',
          url: '/lessons/reg-7-1-higher-fsi-institutional-and-special-uses.html'
        },
        {
          type: 'lesson',
          title: 'Road Widening Surrender & Staff Quarters FSI',
          badge: 'Reg. 7.2 & 7.3',
          snippet: 'Compensatory FSI/TDR for unencumbered road surrender, Govt and Police Housing staff quarters up to 3.00 FSI, zero scrutiny fees, 1/3rd free sale.',
          url: '/lessons/reg-7-2-road-widening-and-staff-quarters.html'
        },
        {
          type: 'lesson',
          title: 'Redevelopment of MHADA Housing Schemes',
          badge: 'Reg. 7.4',
          snippet: 'Blanket 3.00 gross FSI, carpet + 35% rehab (min 35 sqm), Table 7-B plot bonuses up to 45%, Basic Ratio (LR/RC) incentive sharing, 51% member consent.',
          url: '/lessons/reg-7-4-mhada-housing-redevelopment.html'
        },
        {
          type: 'lesson',
          title: 'Redevelopment of 30-Year-Old Societies & Dilapidated Buildings',
          badge: 'Reg. 7.5 & 7.6',
          snippet: 'Protected consumed FSI (Reg 7.5), 30% incentive BUA or 15 sqm/flat for 30-year-old societies, 27.87 sqm minimum carpet, 50% tenant rehab incentives.',
          url: '/lessons/reg-7-6-old-dilapidated-and-housing-societies.html'
        },
        {
          type: 'lesson',
          title: 'IT Establishments, Data Centers & Biotech Parks',
          badge: 'Reg. 7.8 & 7.9',
          snippet: 'IT Policy 2023: FSI up to 4.00 for IT parks and hyperscale data centers, 10% ASR premium, 40% support services, zero amenity surrender, 0.3%/day penalty.',
          url: '/lessons/reg-7-8-it-data-centers-and-biotech-parks.html'
        },
        {
          type: 'lesson',
          title: 'CBD Commercial Buildings, Green Incentives & Fin-Tech Hubs',
          badge: 'Reg. 7.10 to 7.13',
          snippet: 'Commercial towers up to 5.00 FSI in Central Business Districts (50% ASR premium, 30% residential cap), Green Building bonuses (3% to 7%), Smart Fin-Tech.',
          url: '/lessons/reg-7-13-cbd-commercial-and-green-buildings.html'
        },
        {
          type: 'lesson',
          title: 'Parking Locations, Minimum Bay Dimensions & Circulation Aisles',
          badge: 'Reg. 8.1 & 8.1.1(i)-(v)',
          snippet: 'Table 8-A stall geometry (2.5x5.0m), 50% compact car concession (2.3x4.5m), mechanized puzzle sizes, 3.0m car / 2.0m scooter driveways, composite swaps.',
          url: '/lessons/reg-8-1-parking-standards-and-dimensions.html'
        },
        {
          type: 'lesson',
          title: 'Loading-Unloading Berths, Basement Ramps & Marginal Open Space Parking',
          badge: 'Reg. 8.1.1(vi)-(viii)',
          snippet: 'Commercial loading berths (3.75x7.5m, max 4 office, max 6 others), bus bays (>500 flats), dual basement ramps, 3m/6m clear fire margins, mechanical towers at 1.5m.',
          url: '/lessons/reg-8-1-8-loading-spaces-ramps-and-marginal-parking.html'
        },
        {
          type: 'lesson',
          title: 'Off-Street Parking Matrix, Tenement Tiers & Commercial Standards',
          badge: 'Reg. 8.2 & Table 8-B',
          snippet: 'Table 8-B matrix: 5 residential carpet tiers (>=150, 80-150, 40-80, 30-40, <30 sqm), 5% visitor parking, hotels, hospitals (ambulance bays), Data Centers (1 car / 400 sqm).',
          url: '/lessons/reg-8-2-off-street-parking-matrix-and-residential-norms.html'
        },
        {
          type: 'lesson',
          title: 'City Multipliers (Table 8-C), 2-Wheeler Exemption & Excess Parking Surcharges',
          badge: 'Reg. 8.2.2 & Table 8-C',
          snippet: 'Table 8-C geographic factor (1.00 to 0.40), Note (vii) residential two-wheeler non-reduction freeze, Note (v) 10% ASR excess parking fee, Jan 2024 phased OC public surrender.',
          url: '/lessons/reg-8-2-2-city-multipliers-and-parking-penalties.html'
        },
        {
          type: 'lesson',
          title: 'Plinth Standards, Room Heights, Sanitary Sizes & Mezzanines',
          badge: 'Reg. 9.1 to 9.8',
          snippet: 'Plinth levels (30cm / 45cm flood), Table 9-A room heights (2.75m flat, 2.40m beam soffit, 3.00m commercial), bathroom/WC sizes, Table 9-B lofts, and 50% mezzanines.',
          url: '/lessons/reg-9-1-room-dimensions-and-height-clearances.html'
        },
        {
          type: 'lesson',
          title: 'Basements, Podiums, Vehicular Ramps & Stilt Clearances',
          badge: 'Reg. 9.11 to 9.16',
          snippet: 'Basement FSI exemptions vs counted retail/vaults, 1.50m flush boundary extensions, vehicular ramps (max 1:8), 3m/6m widths, 2 car lifts option, and 2.4m/4.5m stilt heights.',
          url: '/lessons/reg-9-11-basements-podiums-and-vehicular-ramps.html'
        },
        {
          type: 'lesson',
          title: 'Light, Ventilation, Shafts, Balconies & Boundary Walls',
          badge: 'Reg. 9.14 & 9.20 to 9.26',
          snippet: 'The 1/10th window opening rule, 7.50m daylight depth limit, Table 9-C ventilation shaft geometry (1.2 to 9.0 sq.m), balcony depths, 1.0-1.2m parapets, and compound wall sightlines.',
          url: '/lessons/reg-9-20-lighting-ventilation-and-shafts.html'
        },
        {
          type: 'lesson',
          title: 'Exit Requirements, Staircase Widths, Occupant Loads & Travel Distances',
          badge: 'Reg. 9.27 & 9.28',
          snippet: 'Passenger lifts (>15m, >24m, senior housing), Table 9-D travel distances (22.5m/30m + 50% sprinkler bonus), Table 9-E occupant loads, Table 9-F exit units, and Table 9-G staircase widths.',
          url: '/lessons/reg-9-28-exit-requirements-and-staircases.html'
        },
        {
          type: 'lesson',
          title: 'Refuge Areas, High-Rise Fire Towers, Chutes & Society Amenities',
          badge: 'Reg. 9.29 to 9.33',
          snippet: 'Staircase treads/risers, Refuge Areas (>24m, stacked every 15m thereafter, 15 sq.m / 0.3 sqm/person), >70m fire towers (75mm water barrier), 1.8m service floors, and Reg 9.31 society amenities.',
          url: '/lessons/reg-9-29-refuge-areas-fire-towers-and-amenities.html'
        },
        {
          type: 'lesson',
          title: 'Pune City Municipal Corporation: Koregaon Park Sanad, Heights & Defense Zones',
          badge: 'Reg. 10.1',
          snippet: 'PMC road width vs building height (12m for >36m, 15m for >=50m), Koregaon Park British-era Collector Sanad Rules (G+1, 1/3 coverage, 20ft setbacks), Parvati/Chatushrungi 21m view caps, and ARDE (75m) / HEMRL (457.2m) defense envelopes.',
          url: '/lessons/reg-10-1-pune-municipal-corporation.html'
        },
        {
          type: 'lesson',
          title: 'Thane Municipal Corporation: High-Density Corridors, Metro PPL & Redevelopment Matrix',
          badge: 'Reg. 10.2 (Part I)',
          snippet: 'Ram Maruti & Gokhale Road stepped setbacks, Eastern Express Highway 7.5m setback, Metro Public Parking Lots (PPL) with 50% incentive FSI, and dilapidated building redevelopment (70m height on 9-12m roads, 1.5m podium margins, 0.8 parking factor).',
          url: '/lessons/reg-10-2-thane-urban-corridors-and-redevelopment.html'
        },
        {
          type: 'lesson',
          title: 'Thane Hazard Zones, Defence Envelopes & Yeur Forest',
          badge: 'Reg. 10.2.4 to 10.2.8',
          snippet: 'Hazardous Chemical Industries concentric safety rings (100m Green Belt + 150m Low Density Zone 0.50 FSI with suo-moto cessation upon closure), Air Force Station 100m security zone, Kolshet/Kavesar radar obstacle height plates, and Yeur forest controls.',
          url: '/lessons/reg-10-2-4-thane-environmental-and-defence-buffers.html'
        },
        {
          type: 'lesson',
          title: 'Nagpur Municipal Corporation (NMC) & NMRDA Special Schemes',
          badge: 'Reg. 10.3 & 10.4',
          snippet: 'NMC Commercial Zone 2.50 base FSI, Industrial 2.50 FSI, NIT leased I-to-R conversion premiums (15% res / 20% comm), NMRDA 250m Outer Ring Road corridor, 15-Hectare Agricultural townships with 10% free land handover, and rural Gaothan expansions.',
          url: '/lessons/reg-10-3-nagpur-nmc-and-nmrda.html'
        },
        {
          type: 'lesson',
          title: 'Nashik Riverfronts & Kolhapur Heritage Enclaves (Mahalaxmi Kiranotsav Marg)',
          badge: 'Reg. 10.5 & 10.9',
          snippet: 'Nashik Godavari river cycle tracks, Gangapur-Ambad 36m DP road 3.0m setback plate, Kolhapur Table 10-B historic layouts (Rajarampuri, Shahupuri, Laxmipuri, Tarabai Park), and the sacred Mahalaxmi Temple Kiranotsav Marg sun-ray solar height restrictions.',
          url: '/lessons/reg-10-5-nashik-and-kolhapur-heritage-enclaves.html'
        },
        {
          type: 'lesson',
          title: 'Navi Mumbai (NMMC) & CIDCO Ecosystem: 10.10.2 Mega-Redevelopment & 12.5% GES',
          badge: 'Reg. 10.10 & 10.14',
          snippet: 'Base FSI 1.50 (+0.50 potential bonus), Regulation 10.10.2 renewal for CIDCO housing >30 years old (FSI up to 3.00, 35% carpet expansion, Table 10-D cluster incentives up to 20%), 12.5% Land Compensation Schemes, and Pushpak Node TDR.',
          url: '/lessons/reg-10-10-navi-mumbai-and-cidco-ecosystem.html'
        },
        {
          type: 'lesson',
          title: 'MMR Growth Centers, Logistics & Special Authorities (Vasai, Ulhasnagar, Bhiwandi & Panvel)',
          badge: 'Reg. 10.6 to 10.16',
          snippet: 'Vasai-Virar Low Density Zone (0.50 max FSI), Mira-Bhayandar agricultural ribbons, Ulhasnagar Regularisation Act (4.00 FSI + Ancillary), Bhiwandi BSNA 3.00 FSI Affordable Housing Scheme, Panvel 75% TDR conversion @ 60% ASR premium, and sunset clauses.',
          url: '/lessons/reg-10-14-mmr-growth-centers-and-special-authorities.html'
        },
        {
          type: 'lesson',
          title: 'Accommodation Reservation & Surrender Mechanics (Table 11-A)',
          badge: 'Reg. 11.1',
          snippet: 'Table 11-A surrender options (40% land / 50% built amenity handover in A/B/C Class MCs), 100% gross plot FSI and TDR transferred to remaining plot with NO CAP on in-situ consumption under Note xi, deemed rezoning under Note xiii, and composite building premium.',
          url: '/lessons/reg-11-1-manner-of-development-and-accommodation-reservation.html'
        },
        {
          type: 'lesson',
          title: 'TDR Generation & Amenity Construction Incentive ((A/B) × 1.35)',
          badge: 'Reg. 11.2.1 - 11.2.5',
          snippet: 'Surrender multipliers (2.0x non-congested, 3.0x congested), compound wall reduction factors (1.85 / 2.85), DP road surrender exemptions, 8% BDP statutory cap, and Amenity Construction TDR formula (A/B) x 1.35 based on PWD DSR per Sep 2024 notification.',
          url: '/lessons/reg-11-2-tdr-generation-and-amenity-construction.html'
        },
        {
          type: 'lesson',
          title: 'TDR Utilisation, Universal ASR Indexation & Receiving Prohibitions',
          badge: 'Reg. 11.2.6 - 11.2.13',
          snippet: 'Universal ASR indexation formula X = (Rg / Rr) x Y pegged to generating year, road width loading caps under Table 6-A and 6-G, zero infrastructure charges guarantee under Reg 11.2.11, and prohibited receiving zones (NDZ, CRZ-I, Grade-I Heritage).',
          url: '/lessons/reg-11-2-6-tdr-utilisation-indexation-and-restrictions.html'
        },
        {
          type: 'lesson',
          title: 'Reservation Credit Certificate (RCC) & Statutory Financial Offsets',
          badge: 'Reg. 11.3',
          snippet: 'Regulation 11.3 rupee-denominated credit notes, 100% surrender valuation at current ASR, redemption against Development Charges, Premium FSI, and municipal property taxes, 10% statutory discount for redemptions after 6 months, and open-market transferability.',
          url: '/lessons/reg-11-3-reservation-credit-certificate-and-financial-offsets.html'
        },
        {
          type: 'lesson',
          title: 'Structural Safety, Materials Quality & Building Services',
          badge: 'Reg. 12.1 - 12.4',
          snippet: 'NBC Part-6 structural engineering compliance, BIS seismic certificates, PWD material standards, mosquito-safe borrow pits, alternative material testing (2-year retention), and NBC Part-8 building services with 1-floor vertical lift extension waiver.',
          url: '/lessons/reg-12-1-structural-design-materials-and-building-services.html'
        },
        {
          type: 'lesson',
          title: 'Water Supply Demands & Statutory Flushing Storage Capacities',
          badge: 'Reg. 12.5, Table 12-A & 12-B',
          snippet: 'Population calculation (5 persons/tenement), Table 12-A daily per capita demands (135 lpcd residential, 180 lpcd hotel, 340/450 lpcd hospital, 70 lpcd restaurant), and Table 12-B mandatory separate flushing cistern storage quotas.',
          url: '/lessons/reg-12-5-water-supply-and-flushing-storage-capacities.html'
        },
        {
          type: 'lesson',
          title: 'Drainage Standards & Institutional Sanitation Fitments',
          badge: 'Reg. 12.6.1 - 12.6.3',
          snippet: 'Residential drainage standards, strict ban on drinking fountains inside toilets, emergency decontamination showers with wheelchair access, crèche sanitary ratios, and fixture schedules for Offices (12-C), Factories (12-D), Theatres (12-E), and Hospitals (12-G to 12-J).',
          url: '/lessons/reg-12-6-drainage-and-institutional-sanitation.html'
        },
        {
          type: 'lesson',
          title: 'Commercial, Transit Sanitation & Outdoor Display Signs',
          badge: 'Reg. 12.6.3 & 12.7',
          snippet: 'Sanitation for Hotels (12-K), Restaurants (12-L), Schools (12-M), Hostels (12-N), Shopping Malls (12-O), Airports/Railways (12-P with disabled WC quotas of 1 per 4,000), and Regulation 12.7 billboard prohibitions on heritage and government structures.',
          url: '/lessons/reg-12-6-commercial-hospitality-sanitation-and-signs.html'
        },
        {
          type: 'lesson',
          title: 'Barrier-Free Access & Universal Design for Differently Abled Persons',
          badge: 'Reg. 13.1',
          snippet: 'Universal accessibility on public plots > 2,000 sqm: standard wheelchair dimensions (1050x750mm), 1,800mm walkways, 3.6m parking bays within 30m, 1:12 ramps, 13-pax BIS lifts, and 1,500x1,750mm outward-swinging accessible toilet cubicles.',
          url: '/lessons/reg-13-1-barrier-free-access-for-differently-abled.html'
        },
        {
          type: 'lesson',
          title: 'Rooftop Solar SWH / RTPV & Rainwater Harvesting Infrastructure',
          badge: 'Reg. 13.2 & 13.3',
          snippet: 'Mandatory solar heating and PV (plot > 4,000 sqm, 25% roof area, 50 kg/sqm loading), and mandatory Rain Water Harvesting (plots >= 500 sqm, 4-layer filter percolation pits, two 100mm pipes per 100 sqm, and 100% free of FSI).',
          url: '/lessons/reg-13-2-solar-and-rainwater-harvesting.html'
        },
        {
          type: 'lesson',
          title: 'Grey Water Recycling, Dual Plumbing & Solid Waste Management',
          badge: 'Reg. 13.4 & 13.5',
          snippet: 'Grey water recycling thresholds (>= 100 flats, >= 1,500 sqm commercial, >= 40 hospital beds), dual plumbing, 5% property tax rebate, water disconnection penalties, and on-site Organic Waste Composting (OWC >= 4,000 sqm BUA).',
          url: '/lessons/reg-13-3-grey-water-and-solid-waste.html'
        },
        {
          type: 'lesson',
          title: 'Disaster Resilience, Fire Towers & Electrical Safety (Oct 2024 Gazette)',
          badge: 'Reg. 13.6',
          snippet: 'Breakthrough 10th October 2024 Gazette Notification: Reg 13.6 disaster resilience (BUA > 10,000 sqm or 1,000+ occupants), 2-hour Fire Towers exempting duplicate staircases, 90m+ fire break water tanks at 65m stages, and mandatory 5-year electrical safety audits.',
          url: '/lessons/reg-13-4-disaster-fire-towers-electrical.html'
        },
        {
          type: 'lesson',
          title: 'Integrated Township Projects (ITP) - Mega-City Master Planning',
          badge: 'Reg. 14.1 & Tables 14-A to 14-J',
          snippet: '40-Hectare minimum contiguous land threshold, 18m access roads, zoning balance (60% Res, 10% Comm, 10% Open, 15% Roads), Tables 14-A to 14-J public amenity plates (50-bed hospital, fire station, police station), 20% social housing handover, and up to 2.00 FSI.',
          url: '/lessons/reg-14-1-integrated-township-projects.html'
        },
        {
          type: 'lesson',
          title: 'Transit Oriented Development (TOD) - Metro & BRT Corridor Densification',
          badge: 'Reg. 14.2 (14.2.1 to 14.2.5)',
          snippet: '500m Metro station influence zones, road-based FSI scaling up to 4.00, 50% premium revenue sharing to Metro SPVs (MahaMetro), 1/4th TDR loading ratio, 50% statutory parking cuts, split-plot rules, and 200m public parking incentives.',
          url: '/lessons/reg-14-2-transit-oriented-development.html'
        },
        {
          type: 'lesson',
          title: 'Affordable Housing Scheme (AHS) & Pradhan Mantri Awas Yojana (PMAY)',
          badge: 'Reg. 14.3 & 14.4',
          snippet: '4,000 sqm min plot, 18m road frontage, 3.00 gross FSI, 1:3 land pocket partition (25% Affordable vs 75% Free Sale), 27.88 sqm unit caps, Table 14-S staged FSI release, off-site infrastructure charges (min Rs. 2,000/sqm), and PMAY up to 2.50 FSI without premium or TDR.',
          url: '/lessons/reg-14-3-affordable-housing-and-pmay.html'
        },
        {
          type: 'lesson',
          title: 'Conservation of Heritage Buildings, Precincts & Heritage TDR',
          badge: 'Reg. 14.5',
          snippet: 'Appendix-L listing process, Grade I (preservation), Grade II (adaptive reuse & harmony), Grade III (townscape character), Heritage Conservation Committee (HCC), non-delegable overrule, skyline covenants, billboard bans, and unconsumed FSI compensation via Heritage TDR.',
          url: '/lessons/reg-14-4-heritage-conservation-and-tdr.html'
        },
        {
          type: 'lesson',
          title: 'Slum Rehabilitation Schemes (SRS) - In-Situ & Slum TDR Economics',
          badge: 'Reg. 14.6 & 14.7',
          snippet: '51% dweller consent, 27.88 sqm (300 sq.ft) free carpet rehab units for protected occupiers (01-Jan-2000), statutory incentive formula [1:R = 2.8 - 0.3n], high-density bonuses (+20% to +30%), Oct 2024 staircase caps (60%), and Slum TDR formula (X = Rg/Rr * Y).',
          url: '/lessons/reg-14-5-slum-rehabilitation-schemes.html'
        },
        {
          type: 'lesson',
          title: 'Urban Renewal Schemes (URS) - Cluster Redevelopment & Master Renewal',
          badge: 'Reg. 14.8 & Table 14-X',
          snippet: '10,000 sqm non-congested vs 4,000 sqm congested cluster thresholds, 18m road access, 30-year building age criteria, Table 14-X rehab entitlements (min 30 sqm + 25% bonus for authorized owners), incentive FSI matrices based on LR/RC ratios, FSI 4.00+, and Urban Renewal TDR (URT).',
          url: '/lessons/reg-14-6-urban-renewal-cluster-redevelopment.html'
        },
        {
          type: 'lesson',
          title: 'Special Industrial, Logistics & Eco-Tourism Ecosystems',
          badge: 'Reg. 14.9 to 14.13',
          snippet: 'Reg 14.9 Eco-Tourism & Nature Conservancy (5km buffer, 10% BUA, 9m height, open fencing), Reg 14.10 Integrated IT Townships (IITP - min 10 acres / 4 Ha, 50:50 IT vs support split, up to 2.50 FSI), Reg 14.11 Integrated Logistics Parks (ILP - min 5 acres, 15m road, 70:30 split, up to 200% additional FSI with 0-15% premium, 24m height), Reg 14.12 Aerospace & Defense Townships, and Reg 14.13 Integrated Industrial Areas under MIDC.',
          url: '/lessons/reg-14-7-special-industrial-logistics-ecosystems.html'
        },
        {
          type: 'lesson',
          title: 'Quarrying Operations & Natural Resource Extraction',
          badge: 'Reg. 15.1',
          snippet: 'Permitted in Agricultural zones outside CRZ/ESZ/Heritage, 1:5,000 location and 1:500 contour excavation plans, 200m separation buffer from roads/settlements (500m for blasting), 500m labor camp offset, 0.50m soil capping, 0.50% ASR development charge, and 1-year annual revalidation up to 3 years max.',
          url: '/lessons/reg-15-1-quarrying-and-mining-operations.html'
        },
        {
          type: 'lesson',
          title: 'Telecommunication Infrastructure & Mobile Towers',
          badge: 'Reg. 15.2',
          snippet: 'Ground-based towers, rooftop Base Transceiver Stations (BTS), DoT norms, the 25-Aug-2023 Section 154 Directives adopting Model Building Bye-Laws 2016, 5G small cells on street furniture, in-building fiber ducts, and structural safety certifications.',
          url: '/lessons/reg-15-2-mobile-towers-and-telecom-infrastructure.html'
        },
        {
          type: 'lesson',
          title: 'Local Area Plans (LAP) & Complete Street Design Guidelines',
          badge: 'Reg. 15.3 & 15.4 (Appendix-M)',
          snippet: 'Micro-level Local Area Plans (LAP) under MRTP Section 33 that legally prevail over UDCPR, and Complete Street Design Guidelines for 18m to 60m roads (segregated pedestrian walkways, cycle tracks, multi-utility zones, carriageways, and universal accessibility).',
          url: '/lessons/reg-15-3-local-area-plans-and-street-design.html'
        }
      ];

      coreLessons.forEach(l => searchIndex.push(l));

      // 2. Index Practical Topic Workbenches (7 CAD Engines)
      const topicPages = [
        {
          type: 'topic',
          title: 'Development Potential & FSI Stacking Engine',
          badge: 'CAD Workbench 01',
          snippet: 'Master FSI stacking calculator, Table 6-A base FSI, Premium FSI purchase at 35% ASR rate, Ancillary BUA 60%/80%, and TDR loading caps with live CAD dimension plate.',
          url: '/topics/development-potential.html'
        },
        {
          type: 'topic',
          title: 'Setbacks, Margins & High-Rise Fire Clearances',
          badge: 'CAD Workbench 02',
          snippet: 'Dynamic CAD section: front road setback (3.0m/4.5m/6.0m), side/rear H/5 margin equation, and mandatory 6.0m clear peripheral fire tender driveway envelope.',
          url: '/topics/setbacks-and-margins.html'
        },
        {
          type: 'topic',
          title: 'Off-Street Parking Standards, Stall CAD & Circulation Ramps',
          badge: 'CAD Workbench 03',
          snippet: 'Interactive CAD stall plates (90°/60° car bays, two-wheeler clusters), 1:10 basement ramp profile with 1:20 transitions, and apartment quota engine.',
          url: '/topics/parking-and-circulation.html'
        },
        {
          type: 'topic',
          title: 'Layout Planning, Land Subdivision & Net Plot Area',
          badge: 'CAD Workbench 04',
          snippet: 'Dynamic CAD subdivision partition plan: DP road surrender, internal layout roads (Table 3-A vs 3-C), 10% ROS retention, 5% Amenity Space, and 20% Inclusive Housing.',
          url: '/topics/layout-and-subdivision.html'
        },
        {
          type: 'topic',
          title: 'High-Rise Fire Safety, Evacuation Stairs & Refuge Floors',
          badge: 'CAD Workbench 05',
          snippet: 'Interactive CAD high-rise elevation: statutory 15m/24m/50m height steps, refuge floors (every 7th floor above 24m), pressurized stairs, and dedicated fire water storage.',
          url: '/topics/fire-safety-and-high-rise.html'
        },
        {
          type: 'topic',
          title: 'TDR Generation Multipliers, Indexation & Credit Notes',
          badge: 'CAD Workbench 06',
          snippet: 'Interactive DRC generation flow (2.00x non-congested vs 3.00x congested), statutory indexation formula X = (Rg/Rr) * Y, receiving road restrictions, and Reservation Credit Notes.',
          url: '/topics/tdr-and-credit-notes.html'
        },
        {
          type: 'topic',
          title: 'Urban Redevelopment, Cluster Schemes & TOD Corridors',
          badge: 'CAD Workbench 07',
          snippet: 'Interactive feasibility engine: Slum Rehabilitation (SRS 51% consent, 1:R formula), Cluster Redevelopment (Table 14-X, 10,000 sqm holding), and Metro TOD corridors (FSI 4.00).',
          url: '/topics/redevelopment-navigator.html'
        },
        {
          type: 'topic',
          title: 'Building Compliance, Statutory NOCs & Approval Roadmap',
          badge: 'CAD Workbench 08',
          snippet: 'Interactive clearance scanner: Fire CFO NOC, SEIAA Environmental Clearance, Grey Water STP, RWH, Airport, Railway & Tree Authority across 4 approval stages.',
          url: '/topics/building-compliance-and-nocs.html'
        }
      ];
      topicPages.forEach(t => searchIndex.push(t));

      // 3. Load Glossary Definitions (141 items)
      const glossRes = await fetch('/data/glossary.json');
      const glossary = await glossRes.json();
      glossary.forEach(g => {
        searchIndex.push({
          type: 'glossary',
          title: g.term,
          badge: g.clause_ref,
          snippet: g.plain_summary,
          url: `/glossary.html#def-${g.id}`
        });
      });

      // 4. Load Master Formulas (9 engines)
      const formRes = await fetch('/data/formulas.json');
      const formulas = await formRes.json();
      formulas.forEach(f => {
        searchIndex.push({
          type: 'formula',
          title: f.title,
          badge: f.clause_ref,
          snippet: f.plain_explanation,
          url: `/formulas.html#${f.id}`
        });
      });

      // 5. Load Clarifications & Amendments (#)
      try {
        const amendRes = await fetch('/data/amendments.json');
        const amendments = await amendRes.json();
        amendments.forEach(a => {
          searchIndex.push({
            type: 'amendment',
            title: `Clarification (#) on ${a.clause}`,
            badge: a.clause,
            snippet: a.subject || a.description || 'Statutory government clarification or corrigendum.',
            url: `/amendments.html#clause-${a.clause.toLowerCase().replace(/[^a-z0-9]/g, '-')}`
          });
        });
      } catch (err) {
        // Non-blocking fallback
      }

      isLoaded = true;
    } catch (e) {
      console.warn('Could not load full search index:', e);
    }
  }

  window.openSearchModal = function () {
    const modal = document.getElementById('search-modal-backdrop');
    if (!modal) return;
    modal.classList.add('open');
    initSearchIndex();
    const input = document.getElementById('search-modal-input');
    if (input) {
      input.value = '';
      input.focus();
      renderSearchResults('');
    }
  };

  window.closeSearchModal = function () {
    const modal = document.getElementById('search-modal-backdrop');
    if (modal) modal.classList.remove('open');
  };

  function renderSearchResults(query) {
    const list = document.getElementById('search-results-list');
    if (!list) return;
    list.innerHTML = '';

    const clean = query.trim().toLowerCase();
    if (!clean) {
      list.innerHTML = '<li style="padding:16px; color:var(--ink-soft); font-family:var(--mono); font-size:12px; text-align:center;">Type any clause (e.g. 3.4.1), term (e.g. FSI, TDR, ROS, Setback), or formula...</li>';
      return;
    }

    const matches = searchIndex.filter(item => {
      return (item.title && item.title.toLowerCase().includes(clean)) ||
             (item.badge && item.badge.toLowerCase().includes(clean)) ||
             (item.snippet && item.snippet.toLowerCase().includes(clean));
    }).slice(0, 12);

    if (matches.length === 0) {
      list.innerHTML = '<li style="padding:16px; color:var(--brick); font-family:var(--mono); font-size:12px; text-align:center;">No matching regulations, definitions, or formulas found.</li>';
      return;
    }

    matches.forEach(m => {
      const li = document.createElement('li');
      li.style.borderBottom = '1px solid var(--line-strong)';
      li.innerHTML = `
        <a href="${m.url}" class="search-result-item" onclick="closeSearchModal()" style="display:block; padding:12px 14px; text-decoration:none; color:var(--ink); background:var(--paper-raised);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px; gap:8px;">
            <span style="font-family:var(--disp); font-weight:700; font-size:14px; color:var(--ink);">${m.title}</span>
            <span class="badge badge-clause" style="font-size:11px;">${m.badge}</span>
          </div>
          <div style="font-size:12px; color:var(--ink-soft); line-height:1.4;">${m.snippet}</div>
        </a>
      `;
      list.appendChild(li);
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    const input = document.getElementById('search-modal-input');
    if (input) {
      input.addEventListener('input', function (e) {
        renderSearchResults(e.target.value);
      });
    }

    // Keyboard shortcuts: Ctrl+K or Cmd+K or /
    document.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        openSearchModal();
      } else if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openSearchModal();
      } else if (e.key === 'Escape') {
        closeSearchModal();
      }
    });
  });
})();
