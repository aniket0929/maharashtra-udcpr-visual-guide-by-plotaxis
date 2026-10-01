import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

formulas_data = [
    {
        "id": "formula-net-plot-area",
        "title": "Net Plot Area Calculation",
        "category": "Land & Layout",
        "clause_ref": "Reg. 3.9",
        "formula_latex": "\\text{Net Plot Area} = A_{\\text{gross}} - A_{\\text{dp\\_road}} - A_{\\text{reservation}} - A_{\\text{amenity}}",
        "plain_explanation": "Net Plot Area is the actual buildable site area left after deducting any land surrendered for Development Plan (DP) road widening, statutory public reservations, and surrendered amenity spaces.",
        "variables": [
            {"symbol": "A_{\\text{gross}}", "name": "Gross Plot Area", "unit": "sq.m", "description": "Total registered cadastral or demarcation area of the land parcel."},
            {"symbol": "A_{\\text{dp\\_road}}", "name": "DP Road / Road Widening Area", "unit": "sq.m", "description": "Portion of the plot affected by sanctioned Development Plan roads or road widening."},
            {"symbol": "A_{\\text{reservation}}", "name": "Public Reservation Area", "unit": "sq.m", "description": "Portion designated for public reservations (playgrounds, municipal schools, hospitals) under DP."},
            {"symbol": "A_{\\text{amenity}}", "name": "Amenity Space Handed Over", "unit": "sq.m", "description": "Statutory amenity space handed over to the local authority under Regulation 3.5.1."}
        ],
        "worked_example": {
            "scenario": "A residential layout proposal on a 10,000 sq.m land in Pune Municipal Corporation limits. A 24m DP road affects 800 sq.m, and a municipal garden reservation covers 1,200 sq.m. The 5% mandatory amenity space (400 sq.m) is surrendered to the authority.",
            "inputs": {
                "Gross Plot Area": "10,000 sq.m",
                "DP Road Widening Area": "800 sq.m",
                "DP Reservation Area": "1,200 sq.m",
                "Amenity Space Surrendered": "400 sq.m"
            },
            "steps": [
                {"label": "Step 1: Sum all statutory deductions", "calculation": "800 + 1,200 + 400", "result": "2,400 sq.m"},
                {"label": "Step 2: Subtract deductions from Gross Plot Area", "calculation": "10,000 - 2,400", "result": "7,600 sq.m"}
            ],
            "final_result": "Net Plot Area = 7,600 sq.m",
            "commentary": "Note: Under UDCPR Reg. 3.9 and Reg. 6.3, even though Net Plot Area is 7,600 sq.m, the Basic FSI potential is calculated on the Gross Plot Area minus DP roads, and in-situ FSI/TDR is awarded for the surrendered land."
        },
        "calculator": {
            "inputs": [
                {"key": "gross", "label": "Gross Plot Area", "type": "number", "default": 10000, "unit": "sq.m", "min": 50},
                {"key": "dp_road", "label": "DP Road / Widening Area", "type": "number", "default": 800, "unit": "sq.m", "min": 0},
                {"key": "reservation", "label": "DP Reservation Area", "type": "number", "default": 1200, "unit": "sq.m", "min": 0},
                {"key": "amenity", "label": "Amenity Space Surrendered", "type": "number", "default": 400, "unit": "sq.m", "min": 0}
            ],
            "output_label": "Calculated Net Plot Area",
            "output_unit": "sq.m",
            "calc_js": "return Math.max(0, gross - dp_road - reservation - amenity);"
        }
    },
    {
        "id": "formula-fsi-potential",
        "title": "Total Maximum Building Potential & Permissible FSI",
        "category": "FSI & Density",
        "clause_ref": "Reg. 6.3 & Table 6-A",
        "formula_latex": "\\text{Total Permissible FSI} = \\text{Basic FSI} + \\text{Premium FSI} + \\text{Max TDR Loading} + \\text{In-Situ FSI}",
        "plain_explanation": "In Maharashtra UDCPR, total building potential is unlocked in tiers based on abutting road width. The total built-up area is the sum of free Basic FSI, purchased Premium FSI, and loaded Transferable Development Rights (TDR).",
        "variables": [
            {"symbol": "\\text{Basic FSI}", "name": "Basic FSI", "unit": "ratio", "description": "Base FSI available as of right (typically 1.10 for Municipal Corporations on roads >= 9m)."},
            {"symbol": "\\text{Premium FSI}", "name": "Premium FSI", "unit": "ratio", "description": "Additional FSI purchasable from the authority at 35% of ASR land rate (e.g. 0.50 on 18m road)."},
            {"symbol": "\\text{Max TDR}", "name": "Maximum TDR Loading", "unit": "ratio", "description": "Maximum Transferable Development Rights that can be consumed on the plot (e.g. 0.40 on 18m road)."},
            {"symbol": "\\text{In-Situ FSI}", "name": "In-Situ Surrender FSI", "unit": "ratio", "description": "Additional FSI credited directly for surrendering road widening land on the same plot."}
        ],
        "worked_example": {
            "scenario": "A residential building proposed on a 1,500 sq.m plot abutting an 18-meter wide road in Municipal Corporation 'A' class. Under Table 6-A for road width >= 18m & < 24m: Basic FSI = 1.10, Premium FSI = 0.50, Max TDR = 0.40. Total Potential = 2.00.",
            "inputs": {
                "Plot Area": "1,500 sq.m",
                "Road Width": "18.0 m",
                "Basic FSI": "1.10",
                "Premium FSI": "0.50",
                "Max TDR Loading": "0.40"
            },
            "steps": [
                {"label": "Step 1: Calculate Total Permissible FSI ratio", "calculation": "1.10 + 0.50 + 0.40", "result": "2.00 FSI"},
                {"label": "Step 2: Calculate Total Permissible Built-up Area", "calculation": "1,500 \\times 2.00", "result": "3,000 sq.m"},
                {"label": "Step 3: Component breakdown", "calculation": "Base: 1,650 sq.m | Premium: 750 sq.m | TDR: 600 sq.m", "result": "3,000 sq.m total"}
            ],
            "final_result": "Total Permissible Built-up Area = 3,000 sq.m (FSI 2.00)",
            "commentary": "Under UDCPR Reg. 6.3 Note xiv, in non-congested areas, the building potential is calculated on the Gross Plot Area after deducting only DP road area."
        },
        "calculator": {
            "inputs": [
                {"key": "plot_area", "label": "Plot Area", "type": "number", "default": 1500, "unit": "sq.m", "min": 50},
                {"key": "road_width", "label": "Abutting Road Width", "type": "select", "default": "18", "options": [
                    {"label": "Below 9.0m (FSI: 1.10 Base, 0.00 Prem, 0.00 TDR = 1.10)", "value": "9"},
                    {"label": "9.0m to < 12.0m (FSI: 1.10 Base, 0.30 Prem, 0.00 TDR = 1.40)", "value": "12"},
                    {"label": "12.0m to < 15.0m (FSI: 1.10 Base, 0.30 Prem, 0.20 TDR = 1.60)", "value": "15"},
                    {"label": "15.0m to < 18.0m (FSI: 1.10 Base, 0.40 Prem, 0.30 TDR = 1.80)", "value": "18"},
                    {"label": "18.0m to < 24.0m (FSI: 1.10 Base, 0.50 Prem, 0.40 TDR = 2.00)", "value": "24"},
                    {"label": "24.0m to < 30.0m (FSI: 1.10 Base, 0.50 Prem, 0.50 TDR = 2.10)", "value": "30"},
                    {"label": "30.0m and above (FSI: 1.10 Base, 0.50 Prem, 0.65 TDR = 2.25)", "value": "31"}
                ]}
            ],
            "output_label": "Total Permissible Built-up Area",
            "output_unit": "sq.m",
            "calc_js": "const fsiMap = {'9': 1.10, '12': 1.40, '15': 1.60, '18': 1.80, '24': 2.00, '30': 2.10, '31': 2.25}; const fsi = fsiMap[road_width] || 1.10; return (plot_area * fsi).toFixed(2);"
        }
    },
    {
        "id": "formula-premium-fsi-cost",
        "title": "Premium FSI Cost Estimation",
        "category": "FSI & Density",
        "clause_ref": "Reg. 2.2.14 & Reg. 6.3",
        "formula_latex": "\\text{Premium Payable} = A_{\\text{premium}} \\times \\text{ASR}_{\\text{land}} \\times 0.35",
        "plain_explanation": "Premium FSI is purchased from the Planning Authority. By statute, the rate of premium is exactly 35% of the prevailing Annual Statement of Rates (Ready Reckoner rate) for open non-agricultural land.",
        "variables": [
            {"symbol": "A_{\\text{premium}}", "name": "Premium Built-up Area", "unit": "sq.m", "description": "The exact quantum of premium built-up area consumed."},
            {"symbol": "\\text{ASR}_{\\text{land}}", "name": "ASR Land Rate", "unit": "₹ / sq.m", "description": "Ready Reckoner land valuation rate for the specific survey number or zone."},
            {"symbol": "0.35", "name": "Statutory Rate Factor", "unit": "factor", "description": "35% statutory multiplier mandated by the Maharashtra State Government under Reg. 2.2.14."}
        ],
        "worked_example": {
            "scenario": "A builder consumes 750 sq.m of Premium FSI on a plot where the government ASR land rate is ₹30,000 per sq.m.",
            "inputs": {
                "Premium FSI Area": "750 sq.m",
                "ASR Land Rate": "₹ 30,000 / sq.m",
                "Statutory Rate": "35%"
            },
            "steps": [
                {"label": "Step 1: Calculate 35% of ASR land rate", "calculation": "30,000 \\times 0.35", "result": "₹ 10,500 / sq.m"},
                {"label": "Step 2: Multiply by Premium FSI Area", "calculation": "750 \\times 10,500", "result": "₹ 78,75,000"}
            ],
            "final_result": "Total Premium Payable = ₹ 78,75,000 (Rupees Seventy-Eight Lakh Seventy-Five Thousand)",
            "commentary": "Under Reg. 2.2.14, 50% of this premium goes to the State Government and 50% remains with the Local Planning Authority."
        },
        "calculator": {
            "inputs": [
                {"key": "prem_area", "label": "Premium FSI Area", "type": "number", "default": 750, "unit": "sq.m", "min": 1},
                {"key": "asr_rate", "label": "ASR Land Rate (Ready Reckoner)", "type": "number", "default": 30000, "unit": "₹ / sq.m", "min": 100}
            ],
            "output_label": "Total Premium Amount Payable",
            "output_unit": "₹",
            "calc_js": "return Math.round(prem_area * asr_rate * 0.35);"
        }
    },
    {
        "id": "formula-recreational-open-space",
        "title": "Recreational Open Space (ROS) & Club House Entitlement",
        "category": "Land & Layout",
        "clause_ref": "Reg. 3.4.1",
        "formula_latex": "\\text{ROS Area} = 0.10 \\times A_{\\text{gross}} \\quad (\\text{when } A_{\\text{gross}} \\ge 4,000\\text{ sq.m})",
        "plain_explanation": "Any layout or subdivision of land measuring 0.40 hectares (4,000 sq.m) or more must dedicate 10% of the land as contiguous recreational green open space. Up to 10% of this open space may be built upon for a residents' club house or gym (Ground + 1 storey).",
        "variables": [
            {"symbol": "A_{\\text{gross}}", "name": "Gross Layout Area", "unit": "sq.m", "description": "Total area of the layout or plotted development."},
            {"symbol": "0.10", "name": "ROS Percentage", "unit": "ratio", "description": "10% statutory reservation."},
            {"symbol": "\\text{Club House BUA}", "name": "Permissible Club House Area", "unit": "sq.m", "description": "10% of the ROS area may be built upon for ancillary sports/gymnasium/club facilities."}
        ],
        "worked_example": {
            "scenario": "A residential group housing project of 12,000 sq.m gross land area.",
            "inputs": {
                "Gross Land Area": "12,000 sq.m"
            },
            "steps": [
                {"label": "Step 1: Check applicability threshold", "calculation": "12,000 \\ge 4,000", "result": "Applicable (10% mandatory ROS)"},
                {"label": "Step 2: Calculate Mandatory ROS", "calculation": "12,000 \\times 0.10", "result": "1,200 sq.m"},
                {"label": "Step 3: Calculate Permissible Club House footprint/built-up", "calculation": "1,200 \\times 0.10", "result": "120 sq.m (G+1 allowed)"}
            ],
            "final_result": "Mandatory Green Open Space = 1,200 sq.m | Club House Max Area = 120 sq.m",
            "commentary": "Under Reg. 3.4.1, the open space must not be less than 400 sq.m in any single pocket and the minimum width must not be less than 15 meters."
        },
        "calculator": {
            "inputs": [
                {"key": "layout_area", "label": "Layout / Plot Area", "type": "number", "default": 12000, "unit": "sq.m", "min": 500}
            ],
            "output_label": "Mandatory Recreational Open Space (ROS)",
            "output_unit": "sq.m",
            "calc_js": "if (layout_area < 4000) return '0 (Exempt: Plot < 0.40 ha)'; return (layout_area * 0.10).toFixed(2);"
        }
    },
    {
        "id": "formula-amenity-space",
        "title": "Mandatory Amenity Space Provision",
        "category": "Land & Layout",
        "clause_ref": "Reg. 3.5.1",
        "formula_latex": "\\text{Amenity Space Area} = \\text{Gross Land Area} \\times \\text{Rate Factor}",
        "plain_explanation": "In layouts or development proposals, amenity space must be provided on the gross area after deducting DP roads and DP reservations. The percentage varies from 1% to 5% based on authority tier and plot size.",
        "variables": [
            {"symbol": "\\text{Gross Area}", "name": "Gross Plot Area", "unit": "sq.m", "description": "Area after deducting DP road widening and reservations."},
            {"symbol": "\\text{Rate Factor}", "name": "Statutory Percentage", "unit": "ratio", "description": "5% for Municipal Corporations on plots > 20,000 sq.m (or tiered as per Reg. 3.5.1)."}
        ],
        "worked_example": {
            "scenario": "A 25,000 sq.m development in a Municipal Corporation area where DP road deductions are 2,000 sq.m. Remaining area is 23,000 sq.m, requiring 5% amenity space surrender.",
            "inputs": {
                "Eligible Land Area": "23,000 sq.m",
                "Amenity Percentage": "5%"
            },
            "steps": [
                {"label": "Step 1: Calculate Amenity Space", "calculation": "23,000 \\times 0.05", "result": "1,150 sq.m"}
            ],
            "final_result": "Mandatory Amenity Space = 1,150 sq.m",
            "commentary": "Under Reg. 3.5.1, the developer can hand over this land to the Planning Authority against FSI/TDR credit, or retain it for approved civic utilities."
        },
        "calculator": {
            "inputs": [
                {"key": "eligible_area", "label": "Eligible Area (Gross - DP Roads)", "type": "number", "default": 23000, "unit": "sq.m", "min": 1000},
                {"key": "rate", "label": "Authority Category", "type": "select", "default": "0.05", "options": [
                    {"label": "Municipal Corporation (Plots > 20,000 sq.m) - 5%", "value": "0.05"},
                    {"label": "Municipal Corporation (Plots 4,000 to 20,000 sq.m) - Retention/Surrender - 3%", "value": "0.03"},
                    {"label": "Municipal Councils / Nagar Panchayats - 2%", "value": "0.02"}
                ]}
            ],
            "output_label": "Required Amenity Space",
            "output_unit": "sq.m",
            "calc_js": "return (eligible_area * parseFloat(rate)).toFixed(2);"
        }
    },
    {
        "id": "formula-marginal-distances",
        "title": "Marginal Open Spaces (Setbacks) for Buildings",
        "category": "Setbacks & Margins",
        "clause_ref": "Reg. 6.2.1, 6.2.3 & Table 6-C",
        "formula_latex": "\\text{Side / Rear Margin} = \\max\\left(3.0\\text{ m}, \\frac{H}{5}\\right) \\quad (\\text{for } H > 15\\text{ m})",
        "plain_explanation": "Marginal distances guarantee adequate light, ventilation, and emergency fire rescue paths. For buildings up to 15m, fixed minimum margins apply. For higher buildings, side and rear margins increase as a fraction of total height H, with a minimum 6.0m clear driveway for fire engines once height exceeds 15m or 24m.",
        "variables": [
            {"symbol": "H", "name": "Total Building Height", "unit": "meters", "description": "Height from average ground level to terrace roof slab level."},
            {"symbol": "H / 5", "name": "Height-based margin", "unit": "meters", "description": "One-fifth of total height for side and rear setbacks."}
        ],
        "worked_example": {
            "scenario": "A residential high-rise building with a total height of 45.0 meters.",
            "inputs": {
                "Building Height (H)": "45.0 m"
            },
            "steps": [
                {"label": "Step 1: Calculate H / 5", "calculation": "45.0 / 5", "result": "9.0 meters"},
                {"label": "Step 2: Check fire tender clear pathway requirement", "calculation": "Required clear driveway >= 6.0m", "result": "Satisfied (9.0m >= 6.0m)"}
            ],
            "final_result": "Required Side & Rear Marginal Distance = 9.0 meters",
            "commentary": "Under Reg. 6.2.3 and CFO fire safety regulations, no permanent structure, podium obstruction, or cantilever projecting more than permissible may choke this fire path."
        },
        "calculator": {
            "inputs": [
                {"key": "bldg_height", "label": "Proposed Building Height (H)", "type": "number", "default": 45, "unit": "meters", "min": 3, "max": 150}
            ],
            "output_label": "Required Side & Rear Margin",
            "output_unit": "meters",
            "calc_js": "if (bldg_height <= 15) return '3.00 m (Low-rise standard)'; const m = Math.max(6.0, bldg_height / 5); return m.toFixed(2) + ' m (Fire tender path enforced)';"
        }
    },
    {
        "id": "formula-parking-requirements",
        "title": "Off-Street Parking Bay Computation",
        "category": "Parking & Vehicles",
        "clause_ref": "Reg. 8.2 & Table 8-1",
        "formula_latex": "\\text{Total Car Spaces} = (N_{\\text{tenements}} \\times \\text{Ratio}) \\times 1.10 \\quad (10\\% \\text{ Visitor Parking})",
        "plain_explanation": "Parking is determined by tenement carpet area in residential buildings, or per 100 sq.m of carpet area in commercial buildings. A mandatory 10% additional spaces must be provided for visitors.",
        "variables": [
            {"symbol": "N_{\\text{tenements}}", "name": "Number of Tenements / Flats", "unit": "units", "description": "Count of apartments in the category."},
            {"symbol": "\\text{Ratio}", "name": "Statutory Car Ratio", "unit": "ratio", "description": "1 car per tenement for carpet area > 75 sq.m; 1 car per 2 tenements for 50-75 sq.m; 1 car per 4 tenements for < 50 sq.m."},
            {"symbol": "1.10", "name": "Visitor Addition Factor", "unit": "factor", "description": "Mandatory 10% visitor parking under Reg. 8.1.1."}
        ],
        "worked_example": {
            "scenario": "A residential building containing 50 luxury flats each with a carpet area of 90 sq.m (> 75 sq.m threshold).",
            "inputs": {
                "Number of flats": "50 units",
                "Carpet area": "90 sq.m each (> 75 sq.m)",
                "Base ratio": "1 car per tenement"
            },
            "steps": [
                {"label": "Step 1: Calculate resident car bays", "calculation": "50 \\times 1", "result": "50 car bays"},
                {"label": "Step 2: Add 10% visitor parking", "calculation": "50 \\times 0.10", "result": "5 visitor bays"},
                {"label": "Step 3: Total required parking", "calculation": "50 + 5", "result": "55 car bays"}
            ],
            "final_result": "Total Required Car Parking = 55 bays (50 Resident + 5 Visitor)",
            "commentary": "Each car bay must measure at least 2.5m x 5.0m with an independent driving aisle of minimum 3.0m width (or 6.0m for two-way)."
        },
        "calculator": {
            "inputs": [
                {"key": "large_flats", "label": "Flats > 75 sq.m carpet (1 car / flat)", "type": "number", "default": 50, "unit": "units", "min": 0},
                {"key": "medium_flats", "label": "Flats 50–75 sq.m carpet (1 car / 2 flats)", "type": "number", "default": 20, "unit": "units", "min": 0},
                {"key": "small_flats", "label": "Flats < 50 sq.m carpet (1 car / 4 flats)", "type": "number", "default": 0, "unit": "units", "min": 0}
            ],
            "output_label": "Total Required Car Parking (Incl. 10% Visitor)",
            "output_unit": "car bays",
            "calc_js": "const resCars = (large_flats * 1.0) + (medium_flats * 0.5) + (small_flats * 0.25); const total = Math.ceil(resCars * 1.10); return total + ' bays (Resident: ' + Math.ceil(resCars) + ', Visitor: ' + Math.ceil(resCars * 0.10) + ')';"
        }
    },
    {
        "id": "formula-tdr-utilization",
        "title": "TDR Receiving Zone Utilization Factor",
        "category": "FSI & Density",
        "clause_ref": "Reg. 11.2.5 & Reg. 11.2.10",
        "formula_latex": "\\text{TDR Area on Receiving Plot} = \\text{DRC Area} \\times \\left(\\frac{\\text{ASR}_{\\text{generating}}}{\\text{ASR}_{\\text{receiving}}}\\right)",
        "plain_explanation": "Transferable Development Rights (TDR) value is equalized based on land price disparity between where the TDR was generated (surrendered land) and where it is being loaded (receiving plot), using their respective Ready Reckoner (ASR) land rates.",
        "variables": [
            {"symbol": "\\text{DRC Area}", "name": "Development Rights Certificate Area", "unit": "sq.m", "description": "Face value of TDR credit in the DRC certificate."},
            {"symbol": "\\text{ASR}_{\\text{generating}}", "name": "ASR Rate of Generating Land", "unit": "₹ / sq.m", "description": "Ready Reckoner land rate of the originating surrendered plot."},
            {"symbol": "\\text{ASR}_{\\text{receiving}}", "name": "ASR Rate of Receiving Land", "unit": "₹ / sq.m", "description": "Ready Reckoner land rate of the destination development site."}
        ],
        "worked_example": {
            "scenario": "A developer holds a DRC for 500 sq.m generated in an outer zone with an ASR rate of ₹20,000/sq.m. They wish to utilize this TDR on a prime plot with an ASR rate of ₹40,000/sq.m.",
            "inputs": {
                "DRC Area": "500 sq.m",
                "Generating Zone ASR Rate": "₹ 20,000 / sq.m",
                "Receiving Zone ASR Rate": "₹ 40,000 / sq.m"
            },
            "steps": [
                {"label": "Step 1: Compute ASR ratio (Rg / Rr)", "calculation": "20,000 / 40,000", "result": "0.50"},
                {"label": "Step 2: Multiply by DRC Area", "calculation": "500 \\times 0.50", "result": "250 sq.m"}
            ],
            "final_result": "Effective TDR Available on Receiving Site = 250 sq.m",
            "commentary": "Under Reg. 11.2.10, if the receiving zone land rate is higher, the quantum of TDR shrinks proportionately to maintain economic equilibrium."
        },
        "calculator": {
            "inputs": [
                {"key": "drc_area", "label": "DRC Face Value Area", "type": "number", "default": 500, "unit": "sq.m", "min": 1},
                {"key": "rg_rate", "label": "Generating Zone Land Rate (Rg)", "type": "number", "default": 20000, "unit": "₹ / sq.m", "min": 100},
                {"key": "rr_rate", "label": "Receiving Zone Land Rate (Rr)", "type": "number", "default": 40000, "unit": "₹ / sq.m", "min": 100}
            ],
            "output_label": "Effective TDR Loaded on Receiving Plot",
            "output_unit": "sq.m",
            "calc_js": "const effective = (drc_area * (rg_rate / rr_rate)); return effective.toFixed(2);"
        }
    },
    {
        "id": "formula-inclusive-housing",
        "title": "Inclusive Housing (EWS / LIG) Quota Obligation",
        "category": "Land & Layout",
        "clause_ref": "Reg. 3.8.2",
        "formula_latex": "\\text{Affordable Housing BUA} = 0.20 \\times \\text{Basic FSI Area} \\quad (\\text{Plots } \\ge 4,000\\text{ sq.m})",
        "plain_explanation": "For any residential layout or group housing scheme on gross land area of 4,000 sq.m or more in Municipal Corporation areas, 20% of the basic FSI must be constructed as affordable Economically Weaker Section (EWS) or Low Income Group (LIG) tenements with carpet areas between 30 and 45 sq.m.",
        "variables": [
            {"symbol": "\\text{Basic FSI Area}", "name": "Basic Permissible Built-up Area", "unit": "sq.m", "description": "Gross Plot Area multiplied by Basic FSI (1.10)."},
            {"symbol": "0.20", "name": "Inclusive Housing Ratio", "unit": "ratio", "description": "Mandatory 20% affordable housing quota."}
        ],
        "worked_example": {
            "scenario": "A 5,000 sq.m residential plot in a Municipal Corporation with Basic FSI 1.10. Basic BUA = 5,500 sq.m.",
            "inputs": {
                "Plot Area": "5,000 sq.m",
                "Basic FSI": "1.10",
                "Basic Built-up Area": "5,500 sq.m"
            },
            "steps": [
                {"label": "Step 1: Check plot threshold", "calculation": "5,000 \\ge 4,000 sq.m", "result": "Mandatory Inclusive Housing applies"},
                {"label": "Step 2: Compute 20% quota", "calculation": "5,500 \\times 0.20", "result": "1,100 sq.m of affordable BUA"},
                {"label": "Step 3: Approximate tenement count (at 35 sq.m carpet)", "calculation": "1,100 / 40", "result": "~27 EWS/LIG tenements"}
            ],
            "final_result": "Mandatory EWS/LIG Construction = 1,100 sq.m BUA (~27 tenements)",
            "commentary": "Under Reg. 3.8.2, these tenements are handed over to MHADA at pre-fixed construction cost, or sold to eligible beneficiaries as per MHADA lottery list."
        },
        "calculator": {
            "inputs": [
                {"key": "plot_size", "label": "Gross Plot Area", "type": "number", "default": 5000, "unit": "sq.m", "min": 500},
                {"key": "base_fsi", "label": "Basic FSI Ratio", "type": "number", "default": 1.10, "unit": "ratio", "min": 0.5, "max": 2.0}
            ],
            "output_label": "Mandatory EWS / LIG Built-up Area",
            "output_unit": "sq.m",
            "calc_js": "if (plot_size < 4000) return '0 (Exempt: Plot < 4,000 sq.m)'; const baseBua = plot_size * base_fsi; return (baseBua * 0.20).toFixed(2) + ' sq.m (~' + Math.floor((baseBua * 0.20) / 40) + ' flats)';"
        }
    }
]

with open('data/formulas.json', 'w', encoding='utf-8') as f:
    json.dump(formulas_data, f, indent=2, ensure_ascii=False)

print(f"Saved {len(formulas_data)} interactive formulas to data/formulas.json")
