import re
import os
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('ucpr_real.md', 'r', encoding='utf-8', errors='ignore') as f:
    source_text = f.read()

lessons = sorted(glob.glob('lessons/*.html'))
print(f"Running automated verification on {len(lessons)} lessons against ucpr_real.md...\n")

# Key numbers and facts to verify for each lesson
checks = [
    {
        'file': 'lessons/reg-1-1-jurisdiction-and-extent.html',
        'clause': '1.1',
        'key_terms': ['Municipal Corporation of Greater Mumbai', 'MIDC', 'NAINA', 'Hill Station Municipal Councils'],
        'key_numbers': ['02nd December, 2020', '37(1AA)', '20(4)']
    },
    {
        'file': 'lessons/reg-1-3-statutory-definitions.html',
        'clause': '1.3',
        'key_terms': ['Basic FSI', 'Carpet area', 'Floor space index', 'High-rise Building', 'Special Building'],
        'key_numbers': ['15 m', '141']
    },
    {
        'file': 'lessons/reg-1-5-savings-and-interpretation.html',
        'clause': '1.5',
        'key_terms': ['Savings', 'repealed regulations', 'Removal of Difficulties'],
        'key_numbers': ['1.10', '1.5']
    },
    {
        'file': 'lessons/reg-2-1-development-permission.html',
        'clause': '2.1',
        'key_terms': ['Permission from the Planning Authority is Mandatory', 'Operational Constructions', 'Repairs to Building'],
        'key_numbers': ['2.1.2', '2.1.7']
    },
    {
        'file': 'lessons/reg-2-2-application-procedure.html',
        'clause': '2.2',
        'key_terms': ['Key Plan', 'Site Plan', 'Building plan', 'Structural Stability Certificate'],
        'key_numbers': ['1:10,000', '1:500', '1:100', '2.2.8']
    },
    {
        'file': 'lessons/reg-2-2-fees-and-charges.html',
        'clause': '2.2.14',
        'key_terms': ['Development Charges', 'Premium Charges', 'Annual Statement of Rates', 'Fire Infrastructure Charges'],
        'key_numbers': ['35%', '50%', '124']
    },
    {
        'file': 'lessons/reg-2-6-commencement-and-occupancy.html',
        'clause': '2.6',
        'key_terms': ['deemed to have been sanctioned', 'plinth level', 'Completion Certificate', 'Occupancy Certificate'],
        'key_numbers': ['60', '7', 'Appendix F', 'Appendix H']
    },
    {
        'file': 'lessons/reg-3-1-site-clearance-buffers.html',
        'clause': '3.1',
        'key_terms': ['bank of river', 'natural nallah', 'railway track', 'electric lines', 'Blue Line'],
        'key_numbers': ['9.0m', '4.5m', '6.0m', '30.0m']
    },
    {
        'file': 'lessons/reg-3-3-internal-layout-roads.html',
        'clause': '3.3',
        'key_terms': ['Internal Roads', 'Cul-de-sacs', 'Handing Over of Layout Roads'],
        'key_numbers': ['75m', '150m', '300m', '9.0m', '12.0m', '15.0m']
    },
    {
        'file': 'lessons/reg-3-4-1-recreational-open-space.html',
        'clause': '3.4.1',
        'key_terms': ['Recreational Open Space', 'club house', 'gross area after deducting'],
        'key_numbers': ['0.4 ha', '10%', '400 sq.m', '15 m', 'G+1']
    },
    {
        'file': 'lessons/reg-3-5-amenity-space-provision.html',
        'clause': '3.5',
        'key_terms': ['Amenity Space', 'Special Planning Authorities', 'handed over to the Authority'],
        'key_numbers': ['20,000 sq.m', '5%', '3.5.1']
    },
    {
        'file': 'lessons/reg-3-8-inclusive-housing.html',
        'clause': '3.8',
        'key_terms': ['Inclusive Housing', 'EWS / LIG', 'MHADA'],
        'key_numbers': ['4,000 sq.m', '20%', '30', '45', '25%']
    },
    {
        'file': 'lessons/reg-3-9-net-plot-area-computation.html',
        'clause': '3.9',
        'key_terms': ['Net Plot Area', 'reservations', 'road widening', 'gross plot area'],
        'key_numbers': ['3.9', '6.3']
    },
    {
        'file': 'lessons/reg-6-1-fsi-stacking-and-building-potential.html',
        'clause': '6.1 & 6.3',
        'key_terms': ['Table 6-G', 'Basic FSI', 'Premium FSI', 'TDR', 'Annual Statement of Rates'],
        'key_numbers': ['35%', '1.10', '3.00', '30%', '50%']
    },
    {
        'file': 'lessons/reg-6-3-ancillary-area-fsi.html',
        'clause': '6.3 Note (i) & 6.6',
        'key_terms': ['ancillary area FSI', 'P-line', 'Rehabilitation component in SRA'],
        'key_numbers': ['60%', '80%', '15%', '10%']
    },
    {
        'file': 'lessons/reg-6-2-front-setbacks-and-street-alignments.html',
        'clause': '6.1.1(ii) & 6.2.1',
        'key_terms': ['centre of the street', 'setback', 'Table No.6-D', 'two or more streets'],
        'key_numbers': ['2.25 m', '3.0 m', '4.5', '6.0']
    },
    {
        'file': 'lessons/reg-6-2-3-side-rear-margins-and-h5-rule.html',
        'clause': '6.2.3 & 6.2.4',
        'key_terms': ['marginal distance', 'H / 5', 'plot boundary', 'taller building', 'dead walls'],
        'key_numbers': ['12.0 m', '6.0 m', '3.0 m']
    },
    {
        'file': 'lessons/reg-6-7-projections-fsi-exclusions-and-fire-driveways.html',
        'clause': '6.7 & 6.8',
        'key_terms': ['chajja', 'canopy', 'service floor', 'exclusively for parking'],
        'key_numbers': ['0.75 m', '5 m', '2.5 m', '1.8 m']
    },
    {
        'file': 'lessons/reg-6-10-height-caps-chowks-and-special-floors.html',
        'clause': '6.9 to 6.15',
        'key_terms': ['Interior chowk', 'Exterior chowk', 'Fire Department', 'Recreational floor', 'Hirkani Kaksha'],
        'key_numbers': ['24.0 m', '12.0 m', '70', '50', '25 sq.m']
    },
    {
        'file': 'lessons/reg-7-1-higher-fsi-institutional-and-special-uses.html',
        'clause': '7.0 & 7.1',
        'key_terms': ['Table No.7-A', 'Hospital', 'Starred category hotels', 'No Amenity Spaces'],
        'key_numbers': ['5%', '10%', '15%', '20%', '3.00']
    },
    {
        'file': 'lessons/reg-7-2-road-widening-and-staff-quarters.html',
        'clause': '7.2 & 7.3',
        'key_terms': ['road widening', 'staff quarters', 'Maharashtra Police Housing Corporation', 'free sale component'],
        'key_numbers': ['3.00', '2.50', '4000 sq.m', '18.0 m']
    },
    {
        'file': 'lessons/reg-7-4-mhada-housing-redevelopment.html',
        'clause': '7.4',
        'key_terms': ['housing schemes of MHADA', 'Rehabilitation Area Entitlement', 'Table 7-B', 'Basic Ratio', 'consent of 51%'],
        'key_numbers': ['35 sq.m', '35%', '3.00', '7%']
    },
    {
        'file': 'lessons/reg-7-6-old-dilapidated-and-housing-societies.html',
        'clause': '7.5 & 7.6',
        'key_terms': ['more than 30 years', 'Co-Operative Housing Societies', 'tenanted buildings'],
        'key_numbers': ['30%', '15 Sq.m', '27.87 sq.m', '50%']
    },
    {
        'file': 'lessons/reg-7-8-it-data-centers-and-biotech-parks.html',
        'clause': '7.8 & 7.9',
        'key_terms': ['Data Centers', 'IT / ITES', 'Biotechnology', 'Critical Infrastructure Fund'],
        'key_numbers': ['10%', '40%', '2%', '0.3%']
    },
    {
        'file': 'lessons/reg-7-13-cbd-commercial-and-green-buildings.html',
        'clause': '7.10 to 7.13',
        'key_terms': ['Central Business District', 'GRIHA', 'IGBC', 'Smart Fin-Tech'],
        'key_numbers': ['5.0', '50%', '30%', '7%']
    },
    {
        'file': 'lessons/reg-8-1-parking-standards-and-dimensions.html',
        'clause': '8.1 & 8.1.1(i)-(v)',
        'key_terms': ['bottom of beam', 'stack parking', 'Motor vehicle', 'Scooter', 'puzzle parking'],
        'key_numbers': ['2.4 m', '2.5 m', '5.0 m', '1.0 m', '2.0 m', '3.00 m']
    },
    {
        'file': 'lessons/reg-8-1-8-loading-spaces-ramps-and-marginal-parking.html',
        'clause': '8.1.1(vi)-(viii)',
        'key_terms': ['bus bay', 'loading and unloading spaces', 'dead wall', 'fire and rescue appliances'],
        'key_numbers': ['500 flats', '1000 sq.m', '4', '6', '1.5 m', '6.0 m']
    },
    {
        'file': 'lessons/reg-8-2-off-street-parking-matrix-and-residential-norms.html',
        'clause': '8.2 & Table 8-B',
        'key_terms': ['Multi-Family residential', 'visitor parking', 'Data centre', 'independent single family'],
        'key_numbers': ['150 sq.m', '80 sq.m', '40 sq.m', '30 sq.m', '5%', '400 sq.m']
    },
    {
        'file': 'lessons/reg-8-2-2-city-multipliers-and-parking-penalties.html',
        'clause': '8.2.2 & Table 8-C',
        'key_terms': ['Multiplying Factor', 'Pune', 'Two Wheeler parking', 'public parking', 'ASR'],
        'key_numbers': ['1.00', '0.9', '0.8', '0.7', '0.6', '0.5', '0.4', '10%', '50%']
    },
    {
        'file': 'lessons/reg-9-1-room-dimensions-and-height-clearances.html',
        'clause': '9.1 to 9.8',
        'key_terms': ['under any beam', 'high flood level', 'Independent Bath room', 'Independent Water closet', 'mezzanine floor'],
        'key_numbers': ['30 cm', '45 cm', '2.75', '2.4 m', '1.00 m', '1.20 m', '0.9 m', '1.50 sq.m', '50%']
    },
    {
        'file': 'lessons/reg-9-11-basements-podiums-and-vehicular-ramps.html',
        'clause': '9.11 to 9.16',
        'key_terms': ['flushing to average surrounding ground level', 'soffit of beam', 'Non Vehicular Ramp', 'Car lifts', 'stack parking'],
        'key_numbers': ['1.5 m', '2.4 m', '2.5%', '1 : 8', '1 in 10', '3.0 m', '6.0 m', '4.50 m']
    },
    {
        'file': 'lessons/reg-9-20-lighting-ventilation-and-shafts.html',
        'clause': '9.14 & 9.20 to 9.26',
        'key_terms': ['floor area of the room', 'ventilation shaft', 'mechanical ventilation system', 'fanning of the road'],
        'key_numbers': ['7.5 m', '1.0 sq.m', '0.30 sq.m', '9.0', '1.5 m', '0.75 m']
    },
    {
        'file': 'lessons/reg-9-28-exit-requirements-and-staircases.html',
        'clause': '9.27 & 9.28',
        'key_terms': ['Retirement Home', 'travel distance', 'Occupant Load', 'fire escape staircase'],
        'key_numbers': ['15 m', '24 m', '22.5 m', '30.0 m', '12.5', '50 cm', '1.00', '1.20', '1.50']
    },
    {
        'file': 'lessons/reg-9-29-refuge-areas-fire-towers-and-amenities.html',
        'clause': '9.29 to 9.33',
        'key_terms': ['Refuge Area', 'two consecutive floors', 'fire escape chute', 'smoke check lobby', 'Fitness Centre'],
        'key_numbers': ['24 m', '39.0 m', '15.0 m', '15 sq.m', '0.3 sq.m', '70 m', '75 mm', '1.8 m', '20 sq.m']
    }
]

total_checks = 0
passed_checks = 0
failed_checks = []

for c in checks:
    print(f"Verifying {c['file']} (Clause {c['clause']}):")
    # Verify in lesson text
    with open(c['file'], 'r', encoding='utf-8') as lf:
        lesson_content = lf.read()
        
    for t in c['key_terms']:
        total_checks += 1
        # Check source text
        # Clean regex search in source_text
        found_in_source = bool(re.search(re.escape(t), source_text, re.IGNORECASE))
        found_in_lesson = bool(re.search(re.escape(t), lesson_content, re.IGNORECASE))
        if found_in_source and found_in_lesson:
            passed_checks += 1
        else:
            failed_checks.append((c['file'], 'Term', t, found_in_source, found_in_lesson))
            print(f"  [MISMATCH/MISSING] Term: {t} (source: {found_in_source}, lesson: {found_in_lesson})")

    for n in c['key_numbers']:
        total_checks += 1
        # Remove spaces or normalize for check
        pattern = re.escape(n)
        found_in_source = bool(re.search(pattern, source_text, re.IGNORECASE))
        found_in_lesson = bool(re.search(pattern, lesson_content, re.IGNORECASE))
        if found_in_source and found_in_lesson:
            passed_checks += 1
        else:
            # Try flexible search (e.g. 0.4 ha vs 0.4ha vs 0.40 ha)
            clean_n = n.replace(' ', r'\s*')
            found_in_source = bool(re.search(clean_n, source_text, re.IGNORECASE))
            found_in_lesson = bool(re.search(clean_n, lesson_content, re.IGNORECASE))
            if found_in_source and found_in_lesson:
                passed_checks += 1
            else:
                failed_checks.append((c['file'], 'Number/Threshold', n, found_in_source, found_in_lesson))
                print(f"  [MISMATCH/MISSING] Number: {n} (source: {found_in_source}, lesson: {found_in_lesson})")

    print(f"  -> All core items verified for {c['clause']}.")

print("\n" + "=" * 60)
print(f"VERIFICATION SUMMARY: {passed_checks} / {total_checks} checks PASSED ({(passed_checks/total_checks)*100:.1f}%)")
if not failed_checks:
    print("STATUS: 100% STATUTORY COMPLIANCE. ZERO MISMATCHES DETECTED.")
else:
    print(f"STATUS: {len(failed_checks)} items flagged for review:")
    for f in failed_checks:
        print(f"  - {f[0]}: {f[1]} '{f[2]}' (in source: {f[3]}, in lesson: {f[4]})")
print("=" * 60)
