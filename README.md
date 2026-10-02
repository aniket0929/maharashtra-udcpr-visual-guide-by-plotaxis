# maharashtra-udcpr-visual-guide-by-plotaxis

> **An Interactive Educational Handbook & Reference Platform for Maharashtra’s Unified Development Control and Promotion Regulations (UDCPR-2020)**

[![Static Site](https://img.shields.io/badge/Architecture-100%25%20Static%20Zero--Backend-00d2ff.svg)](#)
[![UDCPR Edition](https://img.shields.io/badge/Single%20Source%20of%20Truth-Updated%20to%20Jan%2030%2C%202025-10b981.svg)](#)
[![Statutory Audit](https://img.shields.io/badge/Verification%20Audit-49%2F49%20Passed-10b981.svg)](#)
[![License](https://img.shields.io/badge/License-Educational%20Open%20Source-f59e0b.svg)](#)

---

## Project Overview

**maharashtra-udcpr-visual-guide-by-plotaxis** is a free, interactive educational website engineered to make Maharashtra’s 20,600-line Unified Development Control and Promotion Regulations (UDCPR-2020) immediately accessible to architects, town planners, civil engineers, developers, and students.

### Why this exists:

- **Plain Language First**: Every regulation is translated into clear, actionable prose before presenting the verbatim legal text.
- **Exact Clause Tracing**: Every statement, table, and formula anchors directly back to a statutory clause in `ucpr_real.md`.
- **Topic-First Architecture**: Learn by the problems architects actually solve (Development Potential, Setbacks, Parking Standards, Open Spaces) alongside the official 15-chapter curriculum.
- **Editorial Blueprint Plates**: Vector SVG technical drawings with numbered figures (`FIG_001` to `FIG_013`) illustrating setbacks, parking bays, and layout geometry.
- **Interactive Calculators**: Real-time mathematical engines for FSI, Net Plot Area, Premium FSI costs, and TDR utilization.
- **Knowledge Verification**: Interactive quizzes with instant scoring and explanations that update a learner's progress bar in `localStorage`.

---

## Repository Structure

```
udcpr_edu/
│
├── ucpr_real.md               # The Single Source of Truth (20,618 lines, ~1.76 MB)
│
├── index.html                 # Landing page (hero, progress tracker, dual-track navigation)
├── glossary.html              # Searchable glossary of all 141 statutory definitions (Reg. 1.3)
├── formulas.html              # 9 Master statutory formulas with live interactive calculators
├── amendments.html            # Tracker for all 52 clarified regulations marked (#)
├── govt-orders.html           # Chronological index of 53 notifications & 16 Marathi orders
│
├── NEEDS_VERIFICATION.md      # Comprehensive 5-section statutory anomaly register & audit log
│
├── topics/                    # 8 Practical Problem-Solving CAD Workbenches
│   ├── index.html             # Practice directory & workbench switcher
│   ├── development-potential.html  # Topic 1: Dynamic FSI Stacking CAD, 35% ASR outlay & Table 6-A
│   ├── setbacks-and-margins.html   # Topic 2: Dynamic Cross-Section CAD, H/5 margins & 6m fire tender path
│   ├── parking-and-circulation.html # Topic 3: 90°/60° CAD stall plates, 1:10 ramp slope & quota engine
│   ├── layout-and-subdivision.html  # Topic 4: Dynamic Layout Partition CAD, 10% ROS, 5% Amenity & Net Plot
│   ├── fire-safety-and-high-rise.html # Topic 5: High-Rise Evacuation CAD, Refuge Floors & 15m/24m/50m steps
│   ├── tdr-and-credit-notes.html   # Topic 6: DRC Generation Multipliers (2x/3x) & Indexation (Rg/Rr)*Y
│   ├── redevelopment-navigator.html # Topic 7: Slum Rehab (1:R), Cluster Renewal (Table 14-X) & Metro TOD
│   └── building-compliance-and-nocs.html # Topic 8: Statutory Clearances, Fire CFO, SEIAA, STP, RWH & 4-Stage Roadmap
│
├── chapters/                  # Statutory Legal Tree
│   ├── index.html             # 15-Chapter curriculum map (All 15 Chapters Active)
│   ├── ch01.html              # Chapter 1: Administration & Definitions (4 Lessons)
│   ├── ch02.html              # Chapter 2: Development Permission & Commencement (5 Lessons)
│   ├── ch03.html              # Chapter 3: General Land Development Requirements (6 Lessons)
│   ├── ch04.html              # Chapter 4: Land Use Classification & Permissible Uses (6 Lessons)
│   ├── ch05.html              # Chapter 5: Additional Provisions for Regional Plans (5 Lessons)
│   ├── ch06.html              # Chapter 6: Setback, Marginal Distance, Height & FSI (6 Lessons)
│   ├── ch07.html              # Chapter 7: Higher FSI for Certain Uses (6 Lessons)
│   ├── ch08.html              # Chapter 8: Parking, Loading and Unloading Spaces (4 Lessons)
│   ├── ch09.html              # Chapter 9: Requirements of Parts of Buildings (5 Lessons)
│   ├── ch10.html              # Chapter 10: City Specific Regulations (7 Lessons)
│   ├── ch11.html              # Chapter 11: Acquisition of Reserved Sites & TDR (4 Lessons)
│   ├── ch12.html              # Chapter 12: Structural Safety, Water Supply & Sanitation (4 Lessons)
│   ├── ch13.html              # Chapter 13: Special Provisions for Certain Buildings (4 Lessons)
│   ├── ch14.html              # Chapter 14: Special Schemes & Mega-Projects (7 Lessons)
│   └── ch15.html              # Chapter 15: Regulations for Special Activities / Plans (3 Lessons)
│
├── lessons/                   # 76 Fully Written Drawing Sheet Lessons (All 15 Chapters)
│   ├── reg-1-1 to reg-1-6     # 4 Core Lessons (Chapter 1)
│   ├── reg-2-1 to reg-2-6     # 5 Core Lessons (Chapter 2)
│   ├── reg-3-1 to reg-3-9     # 6 Core Lessons (Chapter 3)
│   ├── reg-4-1 to reg-4-27    # 6 Core Lessons (Chapter 4)
│   ├── reg-5-1 to reg-5-4     # 5 Core Lessons (Chapter 5)
│   ├── reg-6-1 to reg-6-10    # 6 Core Lessons (Chapter 6)
│   ├── reg-7-1 to reg-7-13    # 6 Core Lessons (Chapter 7)
│   ├── reg-8-1 to reg-8-2-2   # 4 Core Lessons (Chapter 8)
│   ├── reg-9-1 to reg-9-29    # 5 Core Lessons (Chapter 9)
│   ├── reg-10-1 to reg-10-14  # 7 Core Lessons (Chapter 10)
│   ├── reg-11-1 to reg-11-3   # 4 Core Lessons (Chapter 11)
│   ├── reg-12-1 to reg-12-7   # 4 Core Lessons (Chapter 12)
│   ├── reg-13-1 to reg-13-6   # 4 Core Lessons (Chapter 13)
│   ├── reg-14-1 to reg-14-7   # 7 Core Lessons (Chapter 14)
│   └── reg-15-1 to reg-15-3   # 3 Core Lessons (Chapter 15)
│
├── data/                      # Structured JSON Data Layer
│   ├── glossary.json          # 141 Definitions with plain summaries & categories
│   ├── formulas.json          # 9 Master formulas with LaTeX, variables & JS engines
│   ├── amendments.json        # 52 Clarifications (#) with Government Resolution citations
│   ├── govt_orders.json       # 53 Gazette notifications + 32 Marathi orders/annexures
│   └── verification_report.json # 49-point automated statutory verification audit
│
├── css/
│   ├── blueprint.css          # Design system ("Drawing Sheet" flat paper, mono, typography)
│   └── components.css         # Ruled cards, calculators, quiz widgets & dimension plates
│
├── js/
│   ├── app.js                 # Theme toggler & localStorage learner progress tracker (76 lessons)
│   ├── search.js              # Client-side instant search across all data (Ctrl+K or /)
│   ├── calculators.js         # Real-time mathematical calculation engine
│   └── quiz.js                # Interactive quiz widget with instant scoring
│
└── scripts/                   # Rebuild & Verification Pipeline
    ├── build_all.py           # Master 1-click build pipeline (22-stage automated execution)
    ├── build_heading_tree.py  # Hierarchy extractor
    ├── build_glossary.py      # Section 1.3 parser
    ├── build_formulas.py      # Formula builder
    ├── build_amendments.py    # (#) Clarification extractor
    ├── build_govt_orders.py   # Notification compiler
    ├── build_lessons_ch01_full.py to build_lessons_ch15_full.py # Educational generators
    ├── generate_verification_report.py # Automated statutory accuracy checker (49 checks)
    └── audit_links.py         # Link integrity auditor (1,300+ internal links)
```

---

## Design System: "Drawing Sheet"

The entire interface adheres to an architectural surveyor's drawing sheet aesthetic:

- **Ruled Paper Surface**: Warm archival paper background (`#F1EEE4` / `#FAF8F2`) with 28px ruled horizontal guide lines and 14px top ruler ticks.
- **Corner Tick-Marks**: Sharp square amber tick-mark corners on every container card and sheet frame.
- **Square Geometry**: `border-radius: 0px` globally — zero rounded corners, zero soft drop-shadows.
- **Typography Hierarchy**:
  - **Space Grotesk**: Technical title and display headings.
  - **Inter**: Clear, readable pedagogical body text.
  - **IBM Plex Mono**: Mandatory for all numbers, tables, citations, stat readouts, and regulation IDs (`Reg. X.Y.Z`).

---

## How to Run Locally

Because the site is 100% static with zero server dependencies, you can run it immediately using any local web server:

### Option A: Using Python (Recommended)

```bash
# In the repository root directory:
python -m http.server 3000
```

Then open your browser at **`http://localhost:3000`**.

### Option B: Using Node / npx

```bash
npx serve .
```

---

## How to Rebuild from `ucpr_real.md`

Whenever the Government of Maharashtra issues new amendments or updates to `ucpr_real.md`, re-running the master build pipeline takes **just 2.3 seconds**:

```bash
# In repository root:
python scripts/build_all.py
```

### What `build_all.py` automatically executes:

1. Re-scans all 917 headings and parses the 15-chapter legal hierarchy.
2. Extracts and re-indexes all 141 statutory definitions into `data/glossary.json`.
3. Re-compiles all formulas and calculation logic into `data/formulas.json`.
4. Captures all 52 `(#)` clarification footnotes into `data/amendments.json`.
5. Catalogs all gazette notifications into `data/govt_orders.json`.
6. Regenerates all 76 blueprint lessons across Chapters 1 to 15 with exact statutory clauses, diagrams, and worked numerical examples.
7. Executes the **49-point statutory verification audit** to ensure mathematical and statutory accuracy (100% PASS).
8. Verifies all **1,300+ internal links** across all 98 HTML files to guarantee zero broken links.

---

## Statutory Audit & Verification Register

All anomalies, OCR pagination splits, municipal differences (A/B/C/D class vs Regional Plans), and statutory ambiguities encountered during processing of the 20,618-line source are formally registered in:

**[`NEEDS_VERIFICATION.md`](file:///c:/Users/anike/Desktop/plotaxis/udcpr_edu/NEEDS_VERIFICATION.md)**

Key highlights resolved:

- **Table Page-Splits (50 occurrences)**: Stitched seamless markdown tables eliminating phantom headers.
- **Plotted vs Group Housing Road Widths**: Clear differentiation between Table 3A (9.0m min for plotted layouts) and Table 3C (7.50m for Group Housing).
- **10% ROS Non-Deduction Rule**: Strictly preserved Reg. 3.9(ii) logic where Recreational Open Space is not subtracted from net plot FSI calculations.
- **Deemed Permission Scrutiny**: Highlighting that 60-day deemed permission under Reg. 2.6.2 is only legally valid if compliant with all UDCPR norms.

---

## Deployment Instructions

### Deploy to GitHub Pages

1. Push the repository to GitHub:
   ```bash
   git init
   git add .
   git commit -m "feat: complete UDCPR from Scratch platform"
   git branch -M main
   git remote add origin https://github.com/<your-username>/udcpr-from-scratch.git
   git push -u origin main
   ```
2. In your GitHub repository, navigate to **Settings &rarr; Pages**.
3. Under **Build and deployment &rarr; Source**, select **Deploy from a branch**.
4. Set branch to `main` and folder to `/ (root)`. Click **Save**.
5. Your site is live at `https://<your-username>.github.io/udcpr-from-scratch/`.

### Deploy to Vercel

```bash
npx vercel
```

_Vercel automatically detects the static HTML files and deploys globally with instant CDN caching._

### Deploy to Netlify

Drag and drop the folder into the [Netlify Drop](https://app.netlify.com/drop) dashboard, or connect via Git.

---

## Statutory Disclaimer

> _UDCPR from Scratch is an independent educational and research platform created to aid architects, engineers, students, and property owners in understanding planning regulations. It does not constitute legal or municipal advice. For statutory sanctions and building permits, users must always refer to official Gazette Notifications published by the Government of Maharashtra Urban Development Department._
