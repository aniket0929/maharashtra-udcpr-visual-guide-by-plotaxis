import json
import os

FORMULAS = [
    {
        "id": "formula-net-plot-area",
        "title": "Net Plot Area Calculation",
        "category": "Land & Layout",
        "clause_ref": "Reg. 3.9",
        "workbench_link": "/topics/layout-and-subdivision.html",
        "visual_pills": [
            {"type": "result", "text": "Net Plot Area"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Gross Cadastral Plot"},
            {"type": "op", "text": "−"},
            {"type": "deduct", "text": "DP Road Widening"},
            {"type": "op", "text": "−"},
            {"type": "deduct", "text": "Public DP Reservations"},
            {"type": "op", "text": "−"},
            {"type": "deduct", "text": "Surrendered Amenity Space"}
        ],
        "formula_latex": "\\text{Net Plot Area} = A_{\\text{gross}} - A_{\\text{dp\\_road}} - A_{\\text{reservation}} - A_{\\text{amenity}}",
        "plain_derivation": "Calculates the net buildable land parcel left inside boundary walls on which physical building footprints and basic FSI are calculated.",
        "exam_trap": "Basic FSI is calculated on this Net Plot Area, but under Reg 6.3 Note xiv, Premium FSI and TDR loading potential are calculated on the full Gross Plot Area! Never calculate TDR capacity on the net plot.",
        "variables": [
            {"symbol": "A_{\\text{gross}}", "name": "Gross Plot Area", "unit": "sq.m", "description": "Total registered land holding as per 7/12 extract or City Survey Property Card."},
            {"symbol": "A_{\\text{dp\\_road}}", "name": "DP Road Widening Area", "unit": "sq.m", "description": "Portion of plot falling within sanctioned DP road line to be surrendered free of cost."},
            {"symbol": "A_{\\text{reservation}}", "name": "Public Reservation Area", "unit": "sq.m", "description": "Portion designated for municipal public reservations (schools, parks, hospitals)."},
            {"symbol": "A_{\\text{amenity}}", "name": "Amenity Space Surrendered", "unit": "sq.m", "description": "Mandatory 5% to 15% amenity space physically handed over to the Planning Authority under Reg 3.5.1."}
        ],
        "worked_example": {
            "scenario": "A 10,000 sq.m layout proposal in Pune Municipal Corporation limits. A 24m DP road affects 800 sq.m, a municipal garden reservation affects 1,200 sq.m, and 5% amenity space (400 sq.m) is handed over to PMC.",
            "inputs": {"Gross Plot": "10,000 sq.m", "DP Road Widening": "800 sq.m", "DP Reservation": "1,200 sq.m", "Amenity Surrendered": "400 sq.m"},
            "steps": [
                {"label": "Step 1: Sum public surrenders", "calculation": "800 + 1,200 + 400", "result": "2,400 sq.m"},
                {"label": "Step 2: Subtract from Gross Plot", "calculation": "10,000 - 2,400", "result": "7,600 sq.m"}
            ],
            "final_result": "Net Plot Area = 7,600 sq.m",
            "commentary": "Under Reg 6.3 Note xiv, the developer loads Basic FSI (1.10) on 7,600 sq.m (8,360 BUA), but gets TDR and Premium loading potential on the full 10,000 sq.m gross area!"
        },
        "calculator": {
            "output_label": "Calculated Net Plot Area",
            "output_unit": "sq.m",
            "type": "net_plot",
            "inputs": [
                {"key": "gross", "label": "Gross Plot Area", "type": "number", "default": 10000, "unit": "sq.m", "min": 50},
                {"key": "dp_road", "label": "DP Road Widening", "type": "number", "default": 800, "unit": "sq.m", "min": 0},
                {"key": "res", "label": "Public DP Reservation", "type": "number", "default": 1200, "unit": "sq.m", "min": 0},
                {"key": "amenity", "label": "Amenity Space Surrendered", "type": "number", "default": 400, "unit": "sq.m", "min": 0}
            ]
        }
    },
    {
        "id": "formula-fsi-potential",
        "title": "Total Building Potential & Permissible FSI",
        "category": "Building Potential",
        "clause_ref": "Reg. 6.3 & Table 6-G",
        "workbench_link": "/topics/development-potential.html",
        "visual_pills": [
            {"type": "result", "text": "Total Built-Up Potential"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Basic FSI BUA"},
            {"type": "op", "text": "+"},
            {"type": "var", "text": "Premium FSI BUA"},
            {"type": "op", "text": "+"},
            {"type": "var", "text": "TDR Loading BUA"}
        ],
        "formula_latex": "\\text{Max BUA} = (\\text{Basic FSI} \\times A_{\\text{net}}) + (\\text{Premium FSI} + \\text{TDR}) \\times A_{\\text{gross}}",
        "plain_derivation": "Determines the absolute maximum legal built-up area (BUA) that can be constructed on a plot based strictly on road width.",
        "exam_trap": "Road width is a hard statutory ceiling! You cannot buy extra Premium FSI or load more TDR beyond the road width cap in Table 6-A / 6-G, no matter how much fee is paid.",
        "variables": [
            {"symbol": "A_{\\text{net}}", "name": "Net Plot Area", "unit": "sq.m", "description": "Actual buildable plot area after all public surrenders."},
            {"symbol": "A_{\\text{gross}}", "name": "Gross Plot Area", "unit": "sq.m", "description": "Original cadastral area used for Premium and TDR potential calculation under Note xiv."},
            {"symbol": "\\text{Basic FSI}", "name": "Base Statutory FSI", "unit": "ratio", "description": "1.10 in non-congested areas (Table 6-G) or 1.30/1.50 in congested gaothans."},
            {"symbol": "\\text{Premium FSI}", "name": "Paid Premium Allowance", "unit": "ratio", "description": "Up to 0.50 FSI available upon paying 35% Ready Reckoner rate."},
            {"symbol": "\\text{TDR}", "name": "Transferable Rights Loading", "unit": "ratio", "description": "Up to 0.40 to 1.40 FSI depending on road width hierarchy."}
        ],
        "worked_example": {
            "scenario": "A 2,000 sq.m net plot (2,200 gross) fronting an 18.0m road in a Municipal Corporation outside congested area.",
            "inputs": {"Net Plot": "2,000 sq.m", "Gross Plot": "2,200 sq.m", "Road Width": "18.0m (Table 6-G: Basic 1.10, Premium 0.50, TDR 0.60, Max 2.20)"},
            "steps": [
                {"label": "Step 1: Calculate Basic FSI BUA", "calculation": "2,000 × 1.10", "result": "2,200 sq.m"},
                {"label": "Step 2: Calculate Premium FSI BUA (on Gross)", "calculation": "2,200 × 0.50", "result": "1,100 sq.m"},
                {"label": "Step 3: Calculate TDR Loading BUA (on Gross)", "calculation": "2,200 × 0.60", "result": "1,320 sq.m"},
                {"label": "Step 4: Sum Total Building Potential", "calculation": "2,200 + 1,100 + 1,320", "result": "4,620 sq.m"}
            ],
            "final_result": "Total Permissible BUA = 4,620 sq.m (Effective FSI = 2.31 on Net)",
            "commentary": "Road width of 18m allows 2.20 total building potential on gross plot, creating 4,620 sq.m BUA before Ancillary FSI."
        },
        "calculator": {
            "output_label": "Total Maximum Built-Up Potential",
            "output_unit": "sq.m",
            "type": "fsi_potential",
            "inputs": [
                {"key": "net_area", "label": "Net Plot Area", "type": "number", "default": 2000, "unit": "sq.m", "min": 50},
                {"key": "gross_area", "label": "Gross Plot Area", "type": "number", "default": 2200, "unit": "sq.m", "min": 50},
                {"key": "basic_fsi", "label": "Basic FSI (Table 6-G)", "type": "number", "default": 1.10, "unit": "ratio", "step": 0.05},
                {"key": "premium_fsi", "label": "Premium FSI Permissible", "type": "number", "default": 0.50, "unit": "ratio", "step": 0.05},
                {"key": "tdr_fsi", "label": "TDR Loading Permissible", "type": "number", "default": 0.60, "unit": "ratio", "step": 0.05}
            ]
        }
    },
    {
        "id": "formula-ancillary-fsi",
        "title": "Ancillary Area FSI (P-Line Allowance)",
        "category": "Building Potential",
        "clause_ref": "Reg. 6.3 Note (i) & Reg. 6.6",
        "workbench_link": "/topics/development-potential.html",
        "visual_pills": [
            {"type": "result", "text": "Max Ancillary BUA"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Basic FSI BUA Utilized"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "60% (Residential) or 80% (Commercial)"}
        ],
        "formula_latex": "\\text{Ancillary BUA} = \\text{Basic FSI BUA} \\times (0.60 \\text{ or } 0.80)",
        "plain_derivation": "Calculates the statutory additional floor space allowed for balconies, passages, lift lobbies, and flower beds that replaced the abolished 'free-of-FSI' exemptions.",
        "exam_trap": "Ancillary FSI is NOT free! It requires paying 10% (residential) or 15% (commercial) of the ASR Land Rate. All construction must be measured within the floor-wise P-line envelope.",
        "variables": [
            {"symbol": "\\text{Basic BUA}", "name": "Basic FSI BUA Consumed", "unit": "sq.m", "description": "Actual basic floor area consumed in the proposed design."},
            {"symbol": "0.60 / 0.80", "name": "Statutory Ancillary Factor", "unit": "factor", "description": "60% for residential buildings; 80% for commercial and hospitality buildings."}
        ],
        "worked_example": {
            "scenario": "A residential project consuming 3,000 sq.m of Basic FSI in Thane.",
            "inputs": {"Basic FSI BUA": "3,000 sq.m", "Occupancy": "Residential (60% Ancillary Factor)", "ASR Land Rate": "₹20,000 / sq.m"},
            "steps": [
                {"label": "Step 1: Compute permissible Ancillary BUA", "calculation": "3,000 × 0.60", "result": "1,800 sq.m"},
                {"label": "Step 2: Calculate statutory premium cost (10% ASR)", "calculation": "1,800 × 0.10 × ₹20,000", "result": "₹36,00,000"}
            ],
            "final_result": "Ancillary Area = 1,800 sq.m (Premium Cost = ₹36.00 Lakhs)",
            "commentary": "The developer can design 1,800 sq.m of balconies, double-height terraces, and grand entrance lobbies without consuming main FSI."
        },
        "calculator": {
            "output_label": "Max Ancillary BUA Permissible",
            "output_unit": "sq.m",
            "type": "ancillary_fsi",
            "inputs": [
                {"key": "basic_bua", "label": "Basic FSI BUA Consumed", "type": "number", "default": 3000, "unit": "sq.m", "min": 50},
                {"key": "factor", "label": "Use Category Factor", "type": "select", "default": 0.60, "options": [
                    {"label": "Residential (60%)", "value": 0.60},
                    {"label": "Commercial / Non-Residential (80%)", "value": 0.80}
                ]}
            ]
        }
    },
    {
        "id": "formula-premium-fsi-cost",
        "title": "Premium FSI Cost (35% ASR Formula)",
        "category": "Fees & Charges",
        "clause_ref": "Reg. 2.2.14 & Reg. 6.3",
        "workbench_link": "/topics/development-potential.html",
        "visual_pills": [
            {"type": "result", "text": "Premium FSI Cost (₹)"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Premium Built-Up Area"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "35% Statutory Levy"},
            {"type": "op", "text": "×"},
            {"type": "var", "text": "ASR Land Rate (₹/sq.m)"}
        ],
        "formula_latex": "\\text{Premium Cost} = A_{\\text{premium\\_bua}} \\times 0.35 \\times R_{\\text{ASR}}",
        "plain_derivation": "Computes the exact statutory payment owed to the Municipal Corporation to unlock and purchase Premium FSI.",
        "exam_trap": "The ASR rate must be the unguided open land rate from the Annual Statement of Rates (Ready Reckoner), not the constructed unit rate. 50% is retained locally and 50% goes to the State Government.",
        "variables": [
            {"symbol": "A_{\\text{premium\\_bua}}", "name": "Premium Built-Up Area", "unit": "sq.m", "description": "Quantum of Premium FSI sought in the architectural proposal."},
            {"symbol": "0.35", "name": "Statutory Rate Factor", "unit": "constant", "description": "Standard 35% rate sanctioned uniformly across Maharashtra."},
            {"symbol": "R_{\\text{ASR}}", "name": "Annual Statement of Rates", "unit": "₹/sq.m", "description": "Prevailing Government Ready Reckoner open land rate for the specific survey number / CTS."}
        ],
        "worked_example": {
            "scenario": "A developer purchases 1,000 sq.m of Premium FSI in Nashik where the open land ASR rate is ₹15,000 / sq.m.",
            "inputs": {"Premium BUA": "1,000 sq.m", "ASR Land Rate": "₹15,000 / sq.m"},
            "steps": [
                {"label": "Step 1: Multiply BUA by 35% rate", "calculation": "1,000 × 0.35 × ₹15,000", "result": "₹52,50,000"}
            ],
            "final_result": "Total Premium Fee = ₹52,50,000",
            "commentary": "Can be paid in lump-sum or under the 8.5% reducing balance installment option under Reg 2.2.14."
        },
        "calculator": {
            "output_label": "Total Premium FSI Outlay",
            "output_unit": "₹",
            "type": "premium_cost",
            "inputs": [
                {"key": "bua", "label": "Premium Built-Up Area", "type": "number", "default": 1000, "unit": "sq.m", "min": 10},
                {"key": "asr_rate", "label": "ASR Open Land Rate", "type": "number", "default": 15000, "unit": "₹/sq.m", "min": 500}
            ]
        }
    },
    {
        "id": "formula-recreational-open-space",
        "title": "Recreational Open Space (ROS) & Clubhouse",
        "category": "Layout Mandates",
        "clause_ref": "Reg. 3.4.1",
        "workbench_link": "/topics/layout-and-subdivision.html",
        "visual_pills": [
            {"type": "result", "text": "Recreational Open Space (ROS)"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Gross Layout Area (≥ 0.40 Ha)"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "10% Mandatory Reservation"}
        ],
        "formula_latex": "\\text{ROS Area} = A_{\\text{layout}} \\times 0.10 \\quad (\\text{applicable if } A_{\\text{layout}} \\ge 4,000\\text{ sq.m})",
        "plain_derivation": "Determines the unpaved open green ground that must be retained in layouts of 0.40 Hectare (4,000 sq.m) or more for recreation and percolation.",
        "exam_trap": "Minimum dimension of any ROS pocket is 15.0m. At least 50% must be contiguous open ground for sports. Clubhouses are capped at 15% of ROS area and restricted to G+1 floor.",
        "variables": [
            {"symbol": "A_{\\text{layout}}", "name": "Gross Layout Area", "unit": "sq.m", "description": "Total area of the land parcel being subdivided or planned as group housing."},
            {"symbol": "0.10", "name": "Statutory 10% Quota", "unit": "percentage", "description": "Mandatory green reservation under UDCPR Reg 3.4.1."}
        ],
        "worked_example": {
            "scenario": "A 12,000 sq.m residential layout scheme in Aurangabad.",
            "inputs": {"Layout Area": "12,000 sq.m"},
            "steps": [
                {"label": "Step 1: Compute mandatory 10% ROS", "calculation": "12,000 × 0.10", "result": "1,200 sq.m"},
                {"label": "Step 2: Check 50% sports ground rule", "calculation": "1,200 × 0.50", "result": "Min 600 sq.m contiguous"},
                {"label": "Step 3: Compute max clubhouse construction (15%)", "calculation": "1,200 × 0.15", "result": "Max 180 sq.m BUA (G+1)"}
            ],
            "final_result": "Total ROS = 1,200 sq.m (Clubhouse BUA = 180 sq.m)",
            "commentary": "Clubhouse FSI is free of FSI and does not count towards the net plot BUA."
        },
        "calculator": {
            "output_label": "Mandatory ROS Area Required",
            "output_unit": "sq.m",
            "type": "ros_calc",
            "inputs": [
                {"key": "layout_area", "label": "Gross Layout Area", "type": "number", "default": 12000, "unit": "sq.m", "min": 4000}
            ]
        }
    },
    {
        "id": "formula-amenity-space",
        "title": "Mandatory Amenity Space Provision",
        "category": "Layout Mandates",
        "clause_ref": "Reg. 3.5.1",
        "workbench_link": "/topics/layout-and-subdivision.html",
        "visual_pills": [
            {"type": "result", "text": "Amenity Land Surrendered"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Net Layout Area"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "5% (Local Authority) or 10%–15% (RP)"}
        ],
        "formula_latex": "\\text{Amenity Area} = A_{\\text{net}} \\times 0.05 \\quad (\\text{or } 0.10 \\text{ / } 0.15)",
        "plain_derivation": "Calculates the physical land parcel to be deeded to the local authority for civic infrastructure (substations, public gardens, schools).",
        "exam_trap": "Surrendering amenity land yields 100% FSI credit in-situ or Amenity TDR under Chapter 11. In Municipal Corporations, amenity requirement is 5% for plots > 20,000 sq.m.",
        "variables": [
            {"symbol": "A_{\\text{net}}", "name": "Net Layout Area", "unit": "sq.m", "description": "Plot area after deducting DP roads and public reservations."},
            {"symbol": "0.05", "name": "Amenity Percentage", "unit": "percentage", "description": "5% in municipal areas for plots > 2.0 Ha; 10% to 15% in Regional Plan areas."}
        ],
        "worked_example": {
            "scenario": "A 25,000 sq.m layout in Kalyan-Dombivli Municipal Corporation limits.",
            "inputs": {"Net Layout Area": "25,000 sq.m", "Authority": "Municipal Corporation (> 2.0 Ha = 5%)"},
            "steps": [
                {"label": "Step 1: Compute 5% amenity space", "calculation": "25,000 × 0.05", "result": "1,250 sq.m"}
            ],
            "final_result": "Amenity Space Required = 1,250 sq.m",
            "commentary": "If handed over to KDMC, the owner gets 1,250 sq.m of FSI credit to build on the remaining 23,750 sq.m plot!"
        },
        "calculator": {
            "output_label": "Amenity Space To Be Provided",
            "output_unit": "sq.m",
            "type": "amenity_space",
            "inputs": [
                {"key": "net_layout", "label": "Net Layout Area", "type": "number", "default": 25000, "unit": "sq.m", "min": 4000},
                {"key": "percentage", "label": "Planning Jurisdiction Category", "type": "select", "default": 0.05, "options": [
                    {"label": "Municipal Corporation > 2.0 Ha (5%)", "value": 0.05},
                    {"label": "Regional Plan Area 1.0 to 2.0 Ha (10%)", "value": 0.10},
                    {"label": "Regional Plan Area > 2.0 Ha (15%)", "value": 0.15}
                ]}
            ]
        }
    },
    {
        "id": "formula-inclusive-housing",
        "title": "Inclusive Housing (20% Social Quota)",
        "category": "Social Housing",
        "clause_ref": "Reg. 3.8",
        "workbench_link": "/topics/layout-and-subdivision.html",
        "visual_pills": [
            {"type": "result", "text": "Social Housing Quota"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Gross Plot Area (≥ 4,000 sq.m)"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "20% Land or Tenement Quota"}
        ],
        "formula_latex": "\\text{Inclusive Housing Quota} = \\text{Area or BUA} \\times 0.20",
        "plain_derivation": "Mandates cross-subsidized social housing on private developments $\ge 4,000\text{ sq.m}$ to accommodate EWS and LIG families.",
        "exam_trap": "In plotted layouts, surrender 20% land in small plots $\le 100\text{ sq.m}$; in building schemes, construct 20% BUA as tenements $30\text{--}50\text{ sq.m}$ handed over to MHADA at ASR construction rate!",
        "variables": [
            {"symbol": "A_{\\text{plot}}", "name": "Plot Area", "unit": "sq.m", "description": "Applicable on layouts with gross area of 4,000 sq.m or more."},
            {"symbol": "0.20", "name": "Social Mandate Ratio", "unit": "percentage", "description": "Mandatory 20% reservation under UDCPR Reg 3.8."}
        ],
        "worked_example": {
            "scenario": "A 5,000 sq.m plotted layout scheme in Pimpri-Chinchwad.",
            "inputs": {"Layout Area": "5,000 sq.m"},
            "steps": [
                {"label": "Step 1: Compute 20% land surrender", "calculation": "5,000 × 0.20", "result": "1,000 sq.m"},
                {"label": "Step 2: Subdivide into EWS plots (< 100 sq.m)", "calculation": "1,000 ÷ 50 sq.m per plot", "result": "20 affordable plots"}
            ],
            "final_result": "Inclusive Land = 1,000 sq.m (Yields 20 EWS Plots)",
            "commentary": "The surrendered land is handed over to MHADA or local housing authority for allotment to economically weaker sections."
        },
        "calculator": {
            "output_label": "Mandatory Inclusive Housing Allocation",
            "output_unit": "sq.m",
            "type": "inclusive_calc",
            "inputs": [
                {"key": "plot_size", "label": "Gross Plot Area", "type": "number", "default": 5000, "unit": "sq.m", "min": 4000}
            ]
        }
    },
    {
        "id": "formula-marginal-distances",
        "title": "High-Rise Setback Formula (H/5 Rule)",
        "category": "Setbacks & Margins",
        "clause_ref": "Reg. 6.2.3 & Table 6-D",
        "workbench_link": "/topics/setbacks-and-margins.html",
        "visual_pills": [
            {"type": "result", "text": "Side / Rear Setback"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "( Building Height (H) − 6.0m Stilt )"},
            {"type": "op", "text": "÷"},
            {"type": "factor", "text": "5 (H/5 Divisor)"}
        ],
        "formula_latex": "\\text{Setback}_{\\text{side/rear}} = \\max\\left(6.00, \\min\\left(12.00, \\frac{H - 6.00}{5}\\right)\\right)",
        "plain_derivation": "Computes the side and rear marginal distances required around a tower to ensure ventilation and fire tender access.",
        "exam_trap": "Front margin follows Table 6-D road width IRRESPECTIVE of height. Side/rear margins cannot exceed 12.0m, but for Special Buildings (≥ 15m), they can never drop below the 6.0m fire driveway!",
        "variables": [
            {"symbol": "H", "name": "Total Building Height", "unit": "m", "description": "Height from average ground level to roof slab."},
            {"symbol": "6.00", "name": "Stilt Height Deduction", "unit": "m", "description": "Statutory exclusion for parking stilt up to 6.0m under Reg 6.2.3(b)."},
            {"symbol": "5", "name": "Formula Divisor", "unit": "constant", "description": "Standard H/5 ratio for light and ventilation."}
        ],
        "worked_example": {
            "scenario": "A 46.0m tall residential tower with ground stilt parking of 4.5m.",
            "inputs": {"Building Height": "46.0m", "Stilt Deduction": "4.5m (max 6.0m)"},
            "steps": [
                {"label": "Step 1: Deduct stilt parking height", "calculation": "46.0 - 4.5", "result": "41.5m net height"},
                {"label": "Step 2: Apply H/5 formula", "calculation": "41.5 ÷ 5", "result": "8.30m margin"},
                {"label": "Step 3: Check bounds (min 6.0m, max 12.0m)", "calculation": "6.0m ≤ 8.30m ≤ 12.0m", "result": "8.30m side/rear margin"}
            ],
            "final_result": "Required Side & Rear Margin = 8.30 m",
            "commentary": "Because building is > 15m (Special Building), the 8.30m setback fully accommodates the required 6.0m fire tender driveway."
        },
        "calculator": {
            "output_label": "Required Side & Rear Margin",
            "output_unit": "meters",
            "type": "h5_calc",
            "inputs": [
                {"key": "height", "label": "Building Height (H)", "type": "number", "default": 46.0, "unit": "meters", "min": 15.0},
                {"key": "stilt", "label": "Parking Stilt Height Excluded", "type": "number", "default": 4.5, "unit": "meters", "max": 6.0}
            ]
        }
    },
    {
        "id": "formula-chowk-dimensions",
        "title": "Ventilation Chowk Geometry (Light Wells)",
        "category": "Light & Ventilation",
        "clause_ref": "Reg. 6.11 & Reg. 9.20",
        "workbench_link": "/topics/setbacks-and-margins.html",
        "visual_pills": [
            {"type": "result", "text": "Inner Chowk Width"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Building Height (H)"},
            {"type": "op", "text": "÷"},
            {"type": "factor", "text": "6  (Min 3.0m)  |  Min Area = (H/6)²"}
        ],
        "formula_latex": "W_{\\text{inner}} = \\frac{H}{6} \\quad (\\text{Min } 3.00\\text{m}), \\quad \\text{Area}_{\\text{inner}} = \\left(\\frac{H}{6}\\right)^2",
        "plain_derivation": "Calculates the minimum width and floor area of an interior light well when habitable bedrooms or kitchens ventilate into an internal courtyard.",
        "exam_trap": "Exterior chowks (open on one side) have a relaxed width of H/8 (min 2.4m). If an inner chowk is smaller than (H/6)², municipal scrutiny will deem any room opening into it unventilated!",
        "variables": [
            {"symbol": "H", "name": "Height of Surrounding Building", "unit": "m", "description": "Height of the highest wall abutting the ventilation court."},
            {"symbol": "H/6", "name": "Inner Chowk Ratio", "unit": "ratio", "description": "Statutory rule ensuring sunlight reaches lower floors."}
        ],
        "worked_example": {
            "scenario": "A 24.0m mid-rise apartment building designing an internal light well for kitchen and toilet ventilation.",
            "inputs": {"Building Height": "24.0m"},
            "steps": [
                {"label": "Step 1: Compute minimum chowk width (H/6)", "calculation": "24.0 ÷ 6", "result": "4.00m width"},
                {"label": "Step 2: Compute minimum chowk area (H/6)²", "calculation": "4.00 × 4.00", "result": "16.00 sq.m"}
            ],
            "final_result": "Inner Chowk: Min Width = 4.00 m, Min Area = 16.00 sq.m",
            "commentary": "If this was an exterior chowk open to the rear setback, the width requirement drops to H/8 = 3.00m."
        },
        "calculator": {
            "output_label": "Inner Chowk Minimum Width",
            "output_unit": "meters",
            "type": "chowk_calc",
            "inputs": [
                {"key": "height", "label": "Building Height Surrounding Chowk", "type": "number", "default": 24.0, "unit": "meters", "min": 6.0}
            ]
        }
    },
    {
        "id": "formula-parking-requirements",
        "title": "Off-Street Parking Bay Computation",
        "category": "Circulation & Parking",
        "clause_ref": "Reg. 8.2 & Table 8-1",
        "workbench_link": "/topics/parking-and-circulation.html",
        "visual_pills": [
            {"type": "result", "text": "Total Car Bays"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Base Residential Bays"},
            {"type": "op", "text": "+"},
            {"type": "factor", "text": "10% Mandatory Visitor Bays"}
        ],
        "formula_latex": "\\text{Bays}_{\\text{car}} = \\text{Tenements} \\times \\text{Norm} \\times 1.10_{\\text{visitor}}",
        "plain_derivation": "Determines the total number of off-street car, two-wheeler, and visitor parking spaces required based on apartment carpet areas.",
        "exam_trap": "1 car stall = 2.5m × 5.0m. For every 1 car stall, 2 scooter stalls (1m × 2m) are mandatory! In TOD Metro 500m influence zones, total parking quotas are cut by 50%.",
        "variables": [
            {"symbol": "N_{\\text{tenements}}", "name": "Number of Apartments", "unit": "units", "description": "Count of residential flats in the project categorized by carpet size."},
            {"symbol": "1.10", "name": "Visitor Surcharge", "unit": "multiplier", "description": "Mandatory 10% extra visitor parking bays under Table 8-1 Note (vi)."}
        ],
        "worked_example": {
            "scenario": "A 100-flat residential development: 60 flats of 2-BHK (65 sq.m carpet) and 40 flats of 3-BHK (95 sq.m carpet) in a Municipal Corporation.",
            "inputs": {"Flats ≤ 70 sq.m": "60 units (Norm = 1 car per 2 flats)", "Flats > 70 sq.m": "40 units (Norm = 1 car per 1 flat)"},
            "steps": [
                {"label": "Step 1: Compute bays for ≤ 70 sq.m flats", "calculation": "60 ÷ 2", "result": "30 car bays"},
                {"label": "Step 2: Compute bays for > 70 sq.m flats", "calculation": "40 × 1", "result": "40 car bays"},
                {"label": "Step 3: Add 10% visitor parking", "calculation": "(30 + 40) × 10%", "result": "7 visitor bays"},
                {"label": "Step 4: Compute two-wheeler stalls (2:1 ratio)", "calculation": "77 car bays × 2", "result": "154 scooter bays"}
            ],
            "final_result": "Total Parking Required = 77 Car Bays + 154 Scooter Bays",
            "commentary": "Visitor parking must be demarcated on the ground level or upper stilt for open public access."
        },
        "calculator": {
            "output_label": "Total Required Car Parking Bays",
            "output_unit": "stalls",
            "type": "parking_calc",
            "inputs": [
                {"key": "units_small", "label": "Units ≤ 70 sq.m (1 bay / 2 flats)", "type": "number", "default": 60, "unit": "units", "min": 0},
                {"key": "units_large", "label": "Units > 70 sq.m (1 bay / 1 flat)", "type": "number", "default": 40, "unit": "units", "min": 0}
            ]
        }
    },
    {
        "id": "formula-vehicular-ramps",
        "title": "Basement & Podium Vehicular Ramps",
        "category": "Circulation & Parking",
        "clause_ref": "Reg. 9.12",
        "workbench_link": "/topics/parking-and-circulation.html",
        "visual_pills": [
            {"type": "result", "text": "Ramp Length Needed"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Floor-to-Floor Height (Δh)"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "10 (Straight 1:10) or 8 (Curved 1:8)"}
        ],
        "formula_latex": "L_{\\text{ramp}} = \\Delta h \\times 10 \\quad (\\text{straight}) \\quad \\text{or} \\quad \\Delta h \\times 8 \\quad (\\text{curved})",
        "plain_derivation": "Calculates the horizontal linear run required for vehicular ramps descending into basements or ascending to parking podiums.",
        "exam_trap": "Maximum slope is 1:10 for straight runs and 1:8 for curved ramps. Two-way ramps must be minimum 6.00m wide; one-way paired ramps must be minimum 3.00m wide each.",
        "variables": [
            {"symbol": "\\Delta h", "name": "Vertical Travel Height", "unit": "m", "description": "Finished floor level difference between ground level and basement/podium level."},
            {"symbol": "1:10 / 1:8", "name": "Statutory Ramp Gradient", "unit": "slope", "description": "Maximum slope allowed by UDCPR Reg 9.12."}
        ],
        "worked_example": {
            "scenario": "A 3.5m deep lower basement parking level served by a straight vehicular ramp.",
            "inputs": {"Vertical Drop": "3.5m", "Ramp Type": "Straight (1:10 max gradient)"},
            "steps": [
                {"label": "Step 1: Multiply drop by slope factor", "calculation": "3.5m × 10", "result": "35.00m horizontal run"}
            ],
            "final_result": "Required Ramp Length = 35.00 m (Clear Width = 6.00 m)",
            "commentary": "Transition slopes of 1:20 for a distance of 3.0m must be provided at the top and bottom to avoid car chassis scraping."
        },
        "calculator": {
            "output_label": "Required Linear Ramp Run",
            "output_unit": "meters",
            "type": "ramp_calc",
            "inputs": [
                {"key": "delta_h", "label": "Vertical Travel Height (Δh)", "type": "number", "default": 3.5, "unit": "meters", "min": 1.5},
                {"key": "slope_type", "label": "Ramp Alignment Type", "type": "select", "default": 10, "options": [
                    {"label": "Straight Ramp (Max 1:10)", "value": 10},
                    {"label": "Curved Ramp (Max 1:8)", "value": 8}
                ]}
            ]
        }
    },
    {
        "id": "formula-exit-staircase-width",
        "title": "Occupant Load & Emergency Egress Width",
        "category": "Evacuation & Egress",
        "clause_ref": "Reg. 9.28.5 & 9.28.8",
        "workbench_link": "/topics/fire-safety-and-high-rise.html",
        "visual_pills": [
            {"type": "result", "text": "Total Exit Staircase Width"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "( Floor Population ÷ 100 )"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "0.50m Unit Width (Table 9-F)"}
        ],
        "formula_latex": "W_{\\text{exit}} = \\max\\left(W_{\\text{table9G}}, \\frac{\\text{Occupants}}{100} \\times 0.50\\right)",
        "plain_derivation": "Derives the total clear width of fire staircases needed to safely evacuate all occupants during an emergency.",
        "exam_trap": "Table 9-G establishes absolute minimums: 1.20m for residential < 24m, 1.50m for residential > 24m, and 2.00m for commercial! Staircase width can never be narrower than Table 9-G even if occupant load is small.",
        "variables": [
            {"symbol": "\\text{Occupants}", "name": "Calculated Floor Population", "unit": "persons", "description": "Floor area divided by occupant load factor from Table 9-E (12.5 sq.m/person for residential, 10 for commercial)."},
            {"symbol": "0.50", "name": "Unit Exit Width", "unit": "m", "description": "Standard 50cm evacuation width unit per 100 persons under Table 9-F."}
        ],
        "worked_example": {
            "scenario": "A 1,000 sq.m commercial office floor plate in a high-rise building.",
            "inputs": {"Gross Floor Area": "1,000 sq.m", "Occupant Factor": "10 sq.m / person (Table 9-E)", "Building Category": "Commercial"},
            "steps": [
                {"label": "Step 1: Compute occupant load", "calculation": "1,000 ÷ 10", "result": "100 occupants"},
                {"label": "Step 2: Apply unit exit capacity (Table 9-F)", "calculation": "(100 ÷ 100) × 0.50m", "result": "0.50m width required by math"},
                {"label": "Step 3: Apply Table 9-G statutory minimum floor", "calculation": "Table 9-G Commercial Minimum", "result": "2.00m minimum staircase"}
            ],
            "final_result": "Statutory Staircase Width = 2.00 m (or two 1.50m stairs)",
            "commentary": "Buildings > 24m require at least two separate, pressurized fire escape staircases."
        },
        "calculator": {
            "output_label": "Statutory Minimum Staircase Width",
            "output_unit": "meters",
            "type": "staircase_calc",
            "inputs": [
                {"key": "occupants", "label": "Design Floor Population (Occupants)", "type": "number", "default": 100, "unit": "persons", "min": 10},
                {"key": "building_type", "label": "Occupancy Category", "type": "select", "default": 2.0, "options": [
                    {"label": "Commercial / Mercantile (Min 2.00m)", "value": 2.0},
                    {"label": "Residential Tower > 24m (Min 1.50m)", "value": 1.5},
                    {"label": "Residential Building ≤ 24m (Min 1.20m)", "value": 1.2}
                ]}
            ]
        }
    },
    {
        "id": "formula-amenity-tdr",
        "title": "Construction Amenity TDR Generation",
        "category": "Redevelopment & TDR",
        "clause_ref": "Reg. 11.2.5",
        "workbench_link": "/topics/tdr-and-credit-notes.html",
        "visual_pills": [
            {"type": "result", "text": "Amenity TDR Generated (sq.m)"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "BUA of Handed Over Amenity"},
            {"type": "op", "text": "×"},
            {"type": "var", "text": "( ASR Construction Rate ÷ ASR Land Rate )"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "1.35 Incentive Factor"}
        ],
        "formula_latex": "\\text{TDR}_{\\text{amenity}} = \\text{BUA} \\times \\left(\\frac{R_{\\text{construction}}}{R_{\\text{land}}}\\right) \\times 1.35",
        "plain_derivation": "Computes the exact quantum of market-saleable Development Rights Certificate (DRC) issued to an owner who constructs a public amenity and hands it over to the city.",
        "exam_trap": "The 1.35 multiplier is statutory—it guarantees a 35% margin on top of pure RCC construction costs to incentivize private builders. In Clarification Reg 14.8.7, this formula applies to cluster reservations too!",
        "variables": [
            {"symbol": "\\text{BUA}", "name": "Constructed Amenity BUA", "unit": "sq.m", "description": "Built-up area of the municipal school, hospital, or public parking facility handed over."},
            {"symbol": "R_{\\text{construction}}", "name": "ASR Construction Rate", "unit": "₹/sq.m", "description": "Annual Statement of Rates basic RCC construction rate (typically ₹18,000–₹24,000/sq.m)."},
            {"symbol": "R_{\\text{land}}", "name": "ASR Land Rate", "unit": "₹/sq.m", "description": "Annual Statement of Rates land rate for the specific plot."},
            {"symbol": "1.35", "name": "Statutory Incentive Factor", "unit": "multiplier", "description": "Mandatory 35% premium incentive under Reg 11.2.5."}
        ],
        "worked_example": {
            "scenario": "A builder constructs a 1,000 sq.m municipal dispensary in Pune. ASR construction rate is ₹20,000/sq.m and plot ASR land rate is ₹30,000/sq.m.",
            "inputs": {"Built Amenity Area": "1,000 sq.m", "Construction Rate": "₹20,000/sq.m", "Land Rate": "₹30,000/sq.m"},
            "steps": [
                {"label": "Step 1: Compute rate ratio", "calculation": "20,000 ÷ 30,000", "result": "0.667"},
                {"label": "Step 2: Multiply by BUA and 1.35 factor", "calculation": "1,000 × 0.667 × 1.35", "result": "900 sq.m"}
            ],
            "final_result": "Construction Amenity TDR Issued = 900 sq.m",
            "commentary": "The builder receives a tradeable DRC for 900 sq.m that can be sold on the open market or loaded on another project."
        },
        "calculator": {
            "output_label": "Amenity TDR Certificate Issued",
            "output_unit": "sq.m",
            "type": "amenity_tdr_calc",
            "inputs": [
                {"key": "bua", "label": "Constructed Amenity BUA", "type": "number", "default": 1000, "unit": "sq.m", "min": 50},
                {"key": "r_const", "label": "ASR Construction Rate", "type": "number", "default": 20000, "unit": "₹/sq.m", "min": 5000},
                {"key": "r_land", "label": "ASR Land Rate", "type": "number", "default": 30000, "unit": "₹/sq.m", "min": 5000}
            ]
        }
    },
    {
        "id": "formula-tdr-utilization",
        "title": "TDR Receiving Zone Indexation (ASR Ratio)",
        "category": "Redevelopment & TDR",
        "clause_ref": "Reg. 11.2.6 & Reg. 11.2.10",
        "workbench_link": "/topics/tdr-and-credit-notes.html",
        "visual_pills": [
            {"type": "result", "text": "Loaded TDR Area (X)"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "( ASR Land Rate at Origin (Rg) ÷ ASR Land Rate at Destination (Rr) )"},
            {"type": "op", "text": "×"},
            {"type": "var", "text": "DRC Certificate Area (Y)"}
        ],
        "formula_latex": "X = \\left(\\frac{R_g}{R_r}\\right) \\times Y",
        "plain_derivation": "Equalizes financial land values when transferring TDR from low-cost peripheral zones to high-value city centers, preventing market distortions.",
        "exam_trap": "If you buy 1,000 sq.m of TDR from an outer fringe (Rg = ₹5,000) and load it in a prime downtown corridor (Rr = ₹20,000), you only get 1,000 × (5000/20000) = 250 sq.m of buildable area!",
        "variables": [
            {"symbol": "X", "name": "Effective Permissible BUA", "unit": "sq.m", "description": "Actual buildable floor area allowed to be loaded on the receiving plot."},
            {"symbol": "R_g", "name": "ASR Land Rate at Origin Plot", "unit": "₹/sq.m", "description": "Ready Reckoner land value where the TDR was originally generated."},
            {"symbol": "R_r", "name": "ASR Land Rate at Receiving Plot", "unit": "₹/sq.m", "description": "Ready Reckoner land value of the destination plot."},
            {"symbol": "Y", "name": "Face Value of DRC", "unit": "sq.m", "description": "Area stated on the physical Development Rights Certificate."}
        ],
        "worked_example": {
            "scenario": "A developer buys a 1,000 sq.m DRC generated in an outer municipal suburb (ASR Rg = ₹10,000/sq.m) to load on a high-value core city plot (ASR Rr = ₹25,000/sq.m).",
            "inputs": {"DRC Face Value (Y)": "1,000 sq.m", "Origin Land Rate (Rg)": "₹10,000/sq.m", "Destination Land Rate (Rr)": "₹25,000/sq.m"},
            "steps": [
                {"label": "Step 1: Compute value index ratio", "calculation": "10,000 ÷ 25,000", "result": "0.40"},
                {"label": "Step 2: Multiply by DRC face value", "calculation": "0.40 × 1,000", "result": "400 sq.m"}
            ],
            "final_result": "Effective TDR Area = 400 sq.m",
            "commentary": "Because the receiving land is 2.5 times more expensive, the 1,000 sq.m certificate indexes down to 400 sq.m of actual construction."
        },
        "calculator": {
            "output_label": "Effective Permissible TDR BUA",
            "output_unit": "sq.m",
            "type": "tdr_index_calc",
            "inputs": [
                {"key": "drc_val", "label": "DRC Certificate Face Area (Y)", "type": "number", "default": 1000, "unit": "sq.m", "min": 10},
                {"key": "r_origin", "label": "Origin Plot ASR Land Rate (Rg)", "type": "number", "default": 10000, "unit": "₹/sq.m", "min": 1000},
                {"key": "r_dest", "label": "Destination Plot ASR Land Rate (Rr)", "type": "number", "default": 25000, "unit": "₹/sq.m", "min": 1000}
            ]
        }
    },
    {
        "id": "formula-slum-incentive-ratio",
        "title": "Slum Rehabilitation Incentive Ratio (1:R)",
        "category": "Redevelopment & TDR",
        "clause_ref": "Reg. 14.7",
        "workbench_link": "/topics/redevelopment-navigator.html",
        "visual_pills": [
            {"type": "result", "text": "Incentive Ratio (1:R)"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "2.80"},
            {"type": "op", "text": "−"},
            {"type": "factor", "text": "0.30 × ( Ready Reckoner Land Rate ÷ Construction Rate )"}
        ],
        "formula_latex": "\\text{Ratio } (1:R) = 2.80 - 0.30 \\times \\left(\\frac{\\text{LR}}{\\text{RC}}\\right) \\quad (0.75 \\le R \\le 1.33)",
        "plain_derivation": "Establishes the exact free-sale incentive FSI awarded to a developer for every 1 sq.m of free slum rehabilitation tenements constructed.",
        "exam_trap": "Governed by the Land Rate to Construction Rate (LR/RC) ratio. In high land value zones, the incentive ratio drops towards 1:0.75; in low land value zones, it rises up to 1:1.33 to maintain developer viability.",
        "variables": [
            {"symbol": "R", "name": "Incentive Ratio", "unit": "multiplier", "description": "Free-sale BUA allowed per unit of rehab BUA constructed."},
            {"symbol": "\\text{LR}", "name": "ASR Land Rate", "unit": "₹/sq.m", "description": "Ready Reckoner land value of the slum plot."},
            {"symbol": "\\text{RC}", "name": "ASR Construction Rate", "unit": "₹/sq.m", "description": "Ready Reckoner RCC building construction rate."}
        ],
        "worked_example": {
            "scenario": "A slum rehabilitation project where ASR Land Rate is ₹35,000/sq.m and Construction Rate is ₹20,000/sq.m.",
            "inputs": {"Land Rate (LR)": "₹35,000/sq.m", "Construction Rate (RC)": "₹20,000/sq.m", "Rehab BUA Constructed": "5,000 sq.m"},
            "steps": [
                {"label": "Step 1: Compute LR/RC ratio", "calculation": "35,000 ÷ 20,000", "result": "1.75"},
                {"label": "Step 2: Apply 1:R formula", "calculation": "2.80 - (0.30 × 1.75)", "result": "2.80 - 0.525 = 2.275 (normalized to 1:0.80)"},
                {"label": "Step 3: Compute free-sale BUA", "calculation": "5,000 × 0.80", "result": "4,000 sq.m Free-Sale BUA"}
            ],
            "final_result": "Incentive Ratio = 1:0.80 (Free-Sale BUA = 4,000 sq.m)",
            "commentary": "The builder builds 5,000 sq.m of free rehab housing and receives 4,000 sq.m of market sale units to recover costs and profit."
        },
        "calculator": {
            "output_label": "Free-Sale Incentive Ratio (R)",
            "output_unit": "multiplier",
            "type": "slum_ratio_calc",
            "inputs": [
                {"key": "lr_rate", "label": "ASR Land Rate (LR)", "type": "number", "default": 35000, "unit": "₹/sq.m", "min": 5000},
                {"key": "rc_rate", "label": "ASR Construction Rate (RC)", "type": "number", "default": 20000, "unit": "₹/sq.m", "min": 5000}
            ]
        }
    },
    {
        "id": "formula-cluster-bonus-carpet",
        "title": "Urban Renewal Cluster (URS) Bonus Carpet",
        "category": "Redevelopment & TDR",
        "clause_ref": "Reg. 14.8 & Table 14-X",
        "workbench_link": "/topics/redevelopment-navigator.html",
        "visual_pills": [
            {"type": "result", "text": "Rehab Carpet Entitlement"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Existing Authorized Carpet Area"},
            {"type": "op", "text": "+"},
            {"type": "factor", "text": "25% Mandatory Bonus Carpet (Min 30.0 sq.m)"}
        ],
        "formula_latex": "\\text{Carpet}_{\\text{rehab}} = \\max\\left(30.00, \\text{Carpet}_{\\text{old}} \\times 1.25\\right)",
        "plain_derivation": "Determines the free-of-cost new apartment size guaranteed to legal owners residing in old dilapidated buildings inside a cluster renewal scheme.",
        "exam_trap": "The 25% bonus is non-negotiable and free of cost. If an owner had an old 18 sq.m tenement, they automatically jump to the 30.0 sq.m statutory minimum carpet size.",
        "variables": [
            {"symbol": "\\text{Carpet}_{\\text{old}}", "name": "Existing Authorized Carpet Area", "unit": "sq.m", "description": "Existing documented legal carpet area occupied by tenant/owner."},
            {"symbol": "1.25", "name": "Statutory 25% Bonus", "unit": "multiplier", "description": "Mandatory bonus entitlement under Table 14-X."},
            {"symbol": "30.00", "name": "Statutory Minimum Floor", "unit": "sq.m", "description": "Absolute minimum self-contained rehab unit carpet area."}
        ],
        "worked_example": {
            "scenario": "An authorized tenant occupying an old 40.0 sq.m chawl tenement in a notified Thane Urban Renewal Cluster.",
            "inputs": {"Existing Carpet Area": "40.0 sq.m"},
            "steps": [
                {"label": "Step 1: Multiply by 1.25 (25% bonus)", "calculation": "40.0 × 1.25", "result": "50.00 sq.m"},
                {"label": "Step 2: Compare against 30.0 sq.m minimum", "calculation": "max(30.0, 50.0)", "result": "50.00 sq.m"}
            ],
            "final_result": "New Rehab Apartment = 50.00 sq.m carpet (Free of Cost)",
            "commentary": "The tenant receives a brand-new 50 sq.m 2-BHK apartment with ownership title completely free of cost."
        },
        "calculator": {
            "output_label": "New Free Rehab Apartment Carpet",
            "output_unit": "sq.m",
            "type": "cluster_carpet_calc",
            "inputs": [
                {"key": "old_carpet", "label": "Existing Authorized Carpet Area", "type": "number", "default": 40.0, "unit": "sq.m", "min": 10.0}
            ]
        }
    },
    {
        "id": "formula-water-storage-tanks",
        "title": "Domestic & Flushing Water Tank Storage",
        "category": "Services & Sustainability",
        "clause_ref": "Reg. 12.5 & Table 12-A",
        "workbench_link": "/topics/building-compliance-and-nocs.html",
        "visual_pills": [
            {"type": "result", "text": "Daily Domestic Water Demand"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "Number of Flats"},
            {"type": "op", "text": "×"},
            {"type": "factor", "text": "5 Persons / Flat"},
            {"type": "op", "text": "×"},
            {"type": "var", "text": "135 Litres / Capita / Day"}
        ],
        "formula_latex": "V_{\\text{domestic}} = N_{\\text{flats}} \\times 5 \\times 135 \\quad (\\text{Litres/day})",
        "plain_derivation": "Sizes the underground (UGT) and overhead (OHT) water storage tanks required for municipal water connection sanctions.",
        "exam_trap": "Domestic water (90 LPCD) and flushing water (45 LPCD) must have separate compartmentalized tanks. Fire-fighting static reserve tanks are added separately (50,000L to 200,000L based on building height).",
        "variables": [
            {"symbol": "N_{\\text{flats}}", "name": "Total Residential Tenements", "unit": "units", "description": "Number of residential flats in the development."},
            {"symbol": "5", "name": "Occupancy Assumption", "unit": "persons/flat", "description": "Standard planning assumption of 5 members per household."},
            {"symbol": "135", "name": "Daily Water Standard", "unit": "LPCD", "description": "Standard per capita consumption (90L domestic + 45L flushing) under NBC & Table 12-A."}
        ],
        "worked_example": {
            "scenario": "A 100-flat residential apartment complex seeking municipal plumbing NOC.",
            "inputs": {"Flats": "100 units", "Rate": "135 Litres / person / day", "Household size": "5 persons"},
            "steps": [
                {"label": "Step 1: Compute total design population", "calculation": "100 × 5", "result": "500 residents"},
                {"label": "Step 2: Multiply by 135 Litres daily demand", "calculation": "500 × 135", "result": "67,500 Litres / day"},
                {"label": "Step 3: Split into Domestic and Flushing", "calculation": "Domestic (90L) = 45,000L | Flushing (45L) = 22,500L", "result": "45,000L + 22,500L"}
            ],
            "final_result": "Total Daily Water Storage = 67,500 Litres (67.5 m³)",
            "commentary": "Underground tank (UGT) typically holds 100% of daily demand while Overhead tank (OHT) holds 50% (33,750L)."
        },
        "calculator": {
            "output_label": "Daily Domestic Water Storage Needed",
            "output_unit": "Litres",
            "type": "water_tank_calc",
            "inputs": [
                {"key": "flats", "label": "Number of Residential Flats", "type": "number", "default": 100, "unit": "units", "min": 1}
            ]
        }
    },
    {
        "id": "formula-development-charges",
        "title": "Statutory Development Charges (Sec. 124B MRTP)",
        "category": "Fees & Charges",
        "clause_ref": "Reg. 2.2.13 & Sec. 124B MRTP",
        "workbench_link": "/topics/building-compliance-and-nocs.html",
        "visual_pills": [
            {"type": "result", "text": "Total Development Charge"},
            {"type": "op", "text": "="},
            {"type": "var", "text": "( Gross Land Area × 0.50% ASR Land Rate )"},
            {"type": "op", "text": "+"},
            {"type": "var", "text": "( Total P-Line BUA × 2.00% ASR Construction Rate )"}
        ],
        "formula_latex": "\\text{Charge} = (A_{\\text{land}} \\times 0.005 \\times R_{\\text{land}}) + (\\text{BUA}_{\\text{pline}} \\times 0.02 \\times R_{\\text{const}})",
        "plain_derivation": "Computes the mandatory statutory development infrastructure charges due before the Commencement Certificate (CC) can be released.",
        "exam_trap": "As clarified in Clarification 15 (Order CR 42/21), development charges are levied on all built-up area inside the P-line (including Ancillary FSI). Payments run with the land and are adjusted on revised plans.",
        "variables": [
            {"symbol": "A_{\\text{land}}", "name": "Gross Plot Area", "unit": "sq.m", "description": "Total area of the plot parcel being developed."},
            {"symbol": "\\text{BUA}_{\\text{pline}}", "name": "Total P-Line Built-Up Area", "unit": "sq.m", "description": "Entire proposed construction area including Ancillary FSI."},
            {"symbol": "R_{\\text{land}}", "name": "ASR Open Land Rate", "unit": "₹/sq.m", "description": "Ready Reckoner land valuation."},
            {"symbol": "R_{\\text{const}}", "name": "ASR Construction Rate", "unit": "₹/sq.m", "description": "Ready Reckoner building construction rate."}
        ],
        "worked_example": {
            "scenario": "A 1,000 sq.m plot proposing 2,500 sq.m of total P-line construction. ASR land rate is ₹20,000/sq.m and construction rate is ₹18,000/sq.m.",
            "inputs": {"Land Area": "1,000 sq.m", "P-Line BUA": "2,500 sq.m", "Land ASR": "₹20,000/sq.m", "Construction ASR": "₹18,000/sq.m"},
            "steps": [
                {"label": "Step 1: Compute land charge (0.50% ASR)", "calculation": "1,000 × 0.005 × ₹20,000", "result": "₹1,00,000"},
                {"label": "Step 2: Compute building charge (2.00% ASR)", "calculation": "2,500 × 0.02 × ₹18,000", "result": "₹9,00,000"},
                {"label": "Step 3: Sum total development charges", "calculation": "₹1,00,000 + ₹9,00,000", "result": "₹10,00,000"}
            ],
            "final_result": "Total Section 124B Charge = ₹10,00,000",
            "commentary": "Payment receipt must be attached to the Commencement Certificate (CC) application."
        },
        "calculator": {
            "output_label": "Total Statutory Development Charge",
            "output_unit": "₹",
            "type": "dev_charge_calc",
            "inputs": [
                {"key": "plot_area", "label": "Gross Plot Area", "type": "number", "default": 1000, "unit": "sq.m", "min": 50},
                {"key": "bua", "label": "Total Proposed P-Line BUA", "type": "number", "default": 2500, "unit": "sq.m", "min": 50},
                {"key": "r_land", "label": "ASR Land Rate", "type": "number", "default": 20000, "unit": "₹/sq.m", "min": 1000},
                {"key": "r_const", "label": "ASR Construction Rate", "type": "number", "default": 18000, "unit": "₹/sq.m", "min": 5000}
            ]
        }
    }
]

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_path = os.path.join(base_dir, 'data', 'formulas.json')
    with open(target_path, 'w', encoding='utf-8') as f:
        json.dump(FORMULAS, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote {len(FORMULAS)} master formulas to {target_path}")

if __name__ == '__main__':
    main()
