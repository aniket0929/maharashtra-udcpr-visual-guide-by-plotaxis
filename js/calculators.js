/**
 * UDCPR Interactive Calculators Engine — Enhanced Architectural Sheet System
 * 18 Statutory Mathematical Engines with Plain-Language Visual Pill Equations
 */

document.addEventListener('DOMContentLoaded', async function () {
  const container = document.getElementById('formulas-list-container');
  const countEl = document.getElementById('formula-count-display');
  const statCountEl = document.getElementById('stat-formula-count');
  const searchInput = document.getElementById('formula-search-input');
  const filterTabs = document.getElementById('formula-filter-tabs');
  if (!container) return;

  let allFormulas = [];
  let currentCategory = 'all';
  let searchQuery = '';

  try {
    const res = await fetch('/data/formulas.json');
    allFormulas = await res.json();
    if (statCountEl) statCountEl.textContent = allFormulas.length;

    renderCards();

    // Category Filter Buttons
    if (filterTabs) {
      filterTabs.addEventListener('click', function (e) {
        const btn = e.target.closest('button');
        if (!btn) return;
        filterTabs.querySelectorAll('button').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.getAttribute('data-cat');
        renderCards();
      });
    }

    // Search input
    if (searchInput) {
      searchInput.addEventListener('input', function (e) {
        searchQuery = e.target.value.toLowerCase().trim();
        renderCards();
      });
    }

  } catch (err) {
    console.error("Error loading formulas:", err);
    container.innerHTML = `<p style="color:var(--brick); font-family:var(--mono); padding:40px; text-align:center;">Failed to load formulas data layer.</p>`;
  }

  function renderCards() {
    const filtered = allFormulas.filter(f => {
      const matchCat = currentCategory === 'all' || f.category.toLowerCase() === currentCategory.toLowerCase();
      const matchSearch = !searchQuery || 
        f.title.toLowerCase().includes(searchQuery) ||
        f.clause_ref.toLowerCase().includes(searchQuery) ||
        f.category.toLowerCase().includes(searchQuery) ||
        f.plain_derivation.toLowerCase().includes(searchQuery) ||
        f.exam_trap.toLowerCase().includes(searchQuery);
      return matchCat && matchSearch;
    });

    if (countEl) {
      countEl.textContent = `Showing ${filtered.length} of ${allFormulas.length} statutory calculation engines`;
    }

    if (filtered.length === 0) {
      container.innerHTML = `<div style="text-align:center; padding:60px 20px; color:var(--ink-soft); font-family:var(--mono);">No statutory calculation engines match your search criteria.</div>`;
      return;
    }

    container.innerHTML = '';

    filtered.forEach(f => {
      const card = document.createElement('div');
      card.className = 'panel-info';
      card.style.marginBottom = '36px';
      card.style.border = '1px solid var(--ink)';
      card.style.borderLeft = '5px solid var(--blueprint)';
      card.style.background = 'var(--paper-raised)';
      card.id = f.id;

      // Part A: Visual Pill Equation
      let pillsHtml = '';
      if (f.visual_pills && f.visual_pills.length > 0) {
        pillsHtml = f.visual_pills.map(p => {
          if (p.type === 'op') {
            return `<span class="pill-op">${p.text}</span>`;
          } else if (p.type === 'result') {
            return `<span class="pill-var result">${p.text}</span>`;
          } else if (p.type === 'deduct') {
            return `<span class="pill-var deduct">− ${p.text}</span>`;
          } else if (p.type === 'factor') {
            return `<span class="pill-var factor">${p.text}</span>`;
          } else {
            return `<span class="pill-var">${p.text}</span>`;
          }
        }).join(' ');
      }

      // KaTeX Math Rendering
      let mathHtml = '';
      if (window.katex && f.formula_latex) {
        try {
          mathHtml = window.katex.renderToString(f.formula_latex, { displayMode: true, throwOnError: false });
        } catch (e) {
          mathHtml = `<div style="font-family:var(--mono);">${f.formula_latex}</div>`;
        }
      } else {
        mathHtml = `<div style="font-family:var(--mono);">${f.formula_latex}</div>`;
      }

      // Variables HTML
      let varRows = '';
      if (f.variables) {
        f.variables.forEach(v => {
          let symHtml = v.symbol;
          if (window.katex) {
            try {
              symHtml = window.katex.renderToString(v.symbol, { displayMode: false, throwOnError: false });
            } catch (e) {
              symHtml = v.symbol;
            }
          }
          varRows += `
            <tr>
              <td style="font-family:var(--mono); color:var(--blueprint); font-weight:700;">${symHtml}</td>
              <td style="font-weight:600;">${v.name}</td>
              <td style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">${v.unit}</td>
              <td style="color:var(--ink-soft); font-size:12px;">${v.description}</td>
            </tr>
          `;
        });
      }

      // Calculator Fields HTML
      let fieldsHtml = '';
      if (f.calculator && f.calculator.inputs) {
        f.calculator.inputs.forEach(inp => {
          if (inp.type === 'select') {
            let opts = '';
            inp.options.forEach(o => {
              const sel = o.value == inp.default ? 'selected' : '';
              opts += `<option value="${o.value}" ${sel}>${o.label}</option>`;
            });
            fieldsHtml += `
              <div class="calc-field" style="margin-bottom:12px;">
                <label for="${f.id}-${inp.key}" style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; font-family:var(--mono);">${inp.label}</label>
                <select id="${f.id}-${inp.key}" class="sheet-input" style="width:100%;">${opts}</select>
              </div>
            `;
          } else {
            fieldsHtml += `
              <div class="calc-field" style="margin-bottom:12px;">
                <label for="${f.id}-${inp.key}" style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; font-family:var(--mono);">${inp.label} (${inp.unit || ''})</label>
                <input type="number" id="${f.id}-${inp.key}" class="sheet-input" style="width:100%;" value="${inp.default}" min="${inp.min || 0}" step="${inp.step || 'any'}">
              </div>
            `;
          }
        });
      }

      // Step-by-step steps HTML
      let stepsHtml = '';
      if (f.worked_example && f.worked_example.steps) {
        f.worked_example.steps.forEach(st => {
          stepsHtml += `
            <div class="worked-step" style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px dashed var(--line-strong); padding:6px 0;">
              <span class="step-badge" style="font-family:var(--mono); font-size:12px; font-weight:600;">${st.label}</span>
              <div style="text-align:right;">
                <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">${st.calculation}</span>
                &rarr; <strong style="font-family:var(--mono);">${st.result}</strong>
              </div>
            </div>
          `;
        });
      }

      card.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--line-strong); padding-bottom:10px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <div>
            <span class="kicker">${f.clause_ref}</span>
            <h3 style="font-family:var(--disp); font-size:1.35rem; font-weight:700; color:var(--ink); margin-top:2px;">${f.title}</h3>
          </div>
          <span class="badge badge-clause">${f.category}</span>
        </div>

        <!-- Part A: Visual Pill Equation Banner -->
        <div class="formula-pill-box">
          <div style="font-family:var(--mono); font-size:11px; font-weight:700; color:var(--ink-soft); margin-bottom:10px; text-transform:uppercase; letter-spacing:0.05em;">
            📐 Visual Equation (Plain Language)
          </div>
          <div class="pill-eq">
            ${pillsHtml}
          </div>
        </div>

        <!-- Purpose & Exam Trap Insight Grid -->
        <div class="formula-insight-grid">
          <div class="insight-pane derives">
            <div class="insight-label derives">🎯 What It Derives (Plain English)</div>
            <p class="insight-desc">${f.plain_derivation}</p>
          </div>
          <div class="insight-pane trap">
            <div class="insight-label trap">⚠️ The #1 Exam &amp; Practice Trap</div>
            <p class="insight-desc">${f.exam_trap}</p>
          </div>
        </div>

        <!-- KaTeX Math Block -->
        <div class="math-rendered-block">
          <div style="font-family:var(--mono); font-size:10px; color:var(--ink-soft); margin-bottom:4px; text-transform:uppercase;">
            Academic Statutory Formulation:
          </div>
          ${mathHtml}
        </div>

        <!-- Interactive Calculator Widget -->
        <div style="background:var(--paper); border:1px solid var(--ink); padding:20px; margin:20px 0;">
          <div class="kicker" style="color:var(--blueprint); margin-bottom:12px;">
            ⚡ LIVE INTERACTIVE CALCULATION ENGINE
          </div>
          <div class="calculator-form" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:12px;">
            ${fieldsHtml}
          </div>
          <div class="calc-result-plate" style="margin-top:16px; background:var(--paper-raised); border:1px solid var(--blueprint); padding:12px 16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <span class="calc-result-label" style="font-family:var(--mono); font-size:13px; font-weight:700; color:var(--ink);">${f.calculator.output_label}:</span>
            <span class="calc-result-value" id="${f.id}-output" style="font-family:var(--mono); font-size:1.4rem; font-weight:700; color:var(--blueprint);">--</span>
          </div>
        </div>

        <!-- Variable Glossary Table -->
        <details style="margin:16px 0; border:1px solid var(--line-strong); background:var(--paper); padding:12px 16px;">
          <summary style="cursor:pointer; font-weight:600; font-family:var(--mono); font-size:11px; text-transform:uppercase; color:var(--ink-soft);">
            View Variable Breakdown &amp; Reference Units
          </summary>
          <table class="drawing-table" style="margin-top:12px; width:100%;">
            <thead>
              <tr>
                <th style="width:15%;">Symbol</th>
                <th style="width:30%;">Variable</th>
                <th style="width:15%;">Unit</th>
                <th style="width:40%;">Statutory Definition</th>
              </tr>
            </thead>
            <tbody>
              ${varRows}
            </tbody>
          </table>
        </details>

        <!-- Worked Numerical Example -->
        <div class="panel-example" style="margin-top:16px; background:var(--paper); border:1px solid var(--line-strong); padding:16px;">
          <span class="kicker" style="color:var(--amber);">PRACTICAL BENCHMARK</span>
          <h4 style="font-family:var(--disp); font-size:1.05rem; font-weight:700; margin-bottom:10px; color:var(--ink);">
            Worked Scenario: ${f.worked_example.scenario}
          </h4>
          <div style="margin:12px 0;">
            ${stepsHtml}
          </div>
          <div style="font-family:var(--mono); font-size:0.95rem; font-weight:700; color:var(--ink); border-top:1px solid var(--line-strong); padding-top:8px;">
            ${f.worked_example.final_result}
          </div>
          <p style="font-size:0.85rem; color:var(--ink-soft); margin-top:8px; line-height:1.5;">
            ${f.worked_example.commentary}
          </p>
        </div>

        <!-- Direct Shortcut to Workbench -->
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-top:16px; border-top:1px dashed var(--line-strong); padding-top:12px;">
          <span style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">UDCPR Clause: ${f.clause_ref}</span>
          <a href="${f.workbench_link}" class="tool-btn" style="text-decoration:none; display:inline-flex; align-items:center; gap:6px; color:var(--blueprint); border-color:var(--blueprint); font-weight:600; font-size:12px;">
            Open in Interactive Topic Workbench &rarr;
          </a>
        </div>
      `;

      container.appendChild(card);

      // Wire up calculator logic
      function updateCalculation() {
        const outEl = document.getElementById(`${f.id}-output`);
        if (!outEl) return;

        const getVal = (k) => {
          const el = document.getElementById(`${f.id}-${k}`);
          if (!el) return 0;
          return el.tagName === 'SELECT' ? parseFloat(el.value) || el.value : parseFloat(el.value) || 0;
        };

        let resVal = 0;
        let suffix = f.calculator.output_unit || '';

        switch (f.calculator.type) {
          case 'net_plot': {
            const gross = getVal('gross');
            const dp = getVal('dp_road');
            const res = getVal('res');
            const amenity = getVal('amenity');
            resVal = Math.max(0, gross - dp - res - amenity);
            break;
          }
          case 'fsi_potential': {
            const net = getVal('net_area');
            const gross = getVal('gross_area');
            const basic = getVal('basic_fsi');
            const prem = getVal('premium_fsi');
            const tdr = getVal('tdr_fsi');
            resVal = Math.round((net * basic) + ((prem + tdr) * gross));
            break;
          }
          case 'ancillary_fsi': {
            const basicBua = getVal('basic_bua');
            const factor = getVal('factor');
            resVal = Math.round(basicBua * factor);
            break;
          }
          case 'premium_cost': {
            const bua = getVal('bua');
            const rate = getVal('asr_rate');
            const cost = Math.round(bua * 0.35 * rate);
            resVal = '₹ ' + cost.toLocaleString();
            suffix = '';
            break;
          }
          case 'ros_calc': {
            const area = getVal('layout_area');
            resVal = Math.round(area * 0.10);
            break;
          }
          case 'amenity_space': {
            const area = getVal('net_layout');
            const pct = getVal('percentage');
            resVal = Math.round(area * pct);
            break;
          }
          case 'inclusive_calc': {
            const plot = getVal('plot_size');
            resVal = Math.round(plot * 0.20);
            break;
          }
          case 'h5_calc': {
            const h = getVal('height');
            const stilt = Math.min(6.0, getVal('stilt'));
            const margin = Math.max(6.0, Math.min(12.0, (h - stilt) / 5));
            resVal = margin.toFixed(2);
            break;
          }
          case 'chowk_calc': {
            const h = getVal('height');
            const w = Math.max(3.0, h / 6);
            const area = Math.pow(w, 2);
            resVal = `${w.toFixed(2)} m (Min Area: ${area.toFixed(1)} sq.m)`;
            suffix = '';
            break;
          }
          case 'parking_calc': {
            const s = getVal('units_small');
            const l = getVal('units_large');
            const cars = Math.ceil((s * 0.5 + l * 1.0) * 1.10);
            const scooters = cars * 2;
            resVal = `${cars} Cars + ${scooters} Scooters`;
            suffix = '';
            break;
          }
          case 'ramp_calc': {
            const dh = getVal('delta_h');
            const slope = getVal('slope_type');
            resVal = (dh * slope).toFixed(2);
            break;
          }
          case 'staircase_calc': {
            const occ = getVal('occupants');
            const minWidth = getVal('building_type');
            const calcWidth = Math.max(minWidth, (occ / 100) * 0.50);
            resVal = calcWidth.toFixed(2);
            break;
          }
          case 'amenity_tdr_calc': {
            const bua = getVal('bua');
            const rc = getVal('r_const');
            const rl = getVal('r_land');
            resVal = Math.round(bua * (rc / rl) * 1.35).toLocaleString();
            break;
          }
          case 'tdr_index_calc': {
            const drc = getVal('drc_val');
            const ro = getVal('r_origin');
            const rd = getVal('r_dest');
            resVal = Math.round((ro / rd) * drc).toLocaleString();
            break;
          }
          case 'slum_ratio_calc': {
            const lr = getVal('lr_rate');
            const rc = getVal('rc_rate');
            const ratio = Math.min(1.33, Math.max(0.75, 2.80 - 0.30 * (lr / rc)));
            resVal = `1 : ${ratio.toFixed(2)}`;
            suffix = '';
            break;
          }
          case 'cluster_carpet_calc': {
            const old = getVal('old_carpet');
            resVal = Math.max(30.0, old * 1.25).toFixed(1);
            break;
          }
          case 'water_tank_calc': {
            const flats = getVal('flats');
            const total = flats * 5 * 135;
            resVal = total.toLocaleString();
            break;
          }
          case 'dev_charge_calc': {
            const plot = getVal('plot_area');
            const bua = getVal('bua');
            const rl = getVal('r_land');
            const rc = getVal('r_const');
            const charge = Math.round((plot * 0.005 * rl) + (bua * 0.02 * rc));
            resVal = '₹ ' + charge.toLocaleString();
            suffix = '';
            break;
          }
          default:
            resVal = '--';
        }

        outEl.textContent = `${resVal} ${suffix}`.trim();
      }

      // Attach event listeners
      if (f.calculator && f.calculator.inputs) {
        f.calculator.inputs.forEach(inp => {
          const el = document.getElementById(`${f.id}-${inp.key}`);
          if (el) {
            el.addEventListener('input', updateCalculation);
            el.addEventListener('change', updateCalculation);
          }
        });
      }

      // Initial run
      updateCalculation();
    });
  }
});
