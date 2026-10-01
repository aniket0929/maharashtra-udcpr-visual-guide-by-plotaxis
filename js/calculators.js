/**
 * UDCPR Interactive Calculators Engine — Drawing Sheet System
 */

document.addEventListener('DOMContentLoaded', async function () {
  const container = document.getElementById('formulas-list-container');
  if (!container) return;

  try {
    const res = await fetch('/data/formulas.json');
    const formulas = await res.json();

    container.innerHTML = '';

    formulas.forEach(f => {
      const card = document.createElement('div');
      card.className = 'panel-info';
      card.style.marginBottom = '32px';
      card.style.border = '1px solid var(--ink)';
      card.style.borderLeft = '4px solid var(--blueprint)';
      card.style.background = 'var(--paper-raised)';
      card.id = f.id;

      // Variables HTML
      let varRows = '';
      f.variables.forEach(v => {
        varRows += `
          <tr>
            <td style="font-family:var(--mono); color:var(--blueprint); font-weight:700;">${v.symbol}</td>
            <td style="font-weight:600;">${v.name}</td>
            <td style="font-family:var(--mono); font-size:11px; color:var(--ink-soft);">${v.unit}</td>
            <td style="color:var(--ink-soft); font-size:12px;">${v.description}</td>
          </tr>
        `;
      });

      // Calculator Fields HTML
      let fieldsHtml = '';
      f.calculator.inputs.forEach(inp => {
        if (inp.type === 'select') {
          let opts = '';
          inp.options.forEach(o => {
            const sel = o.value === inp.default ? 'selected' : '';
            opts += `<option value="${o.value}" ${sel}>${o.label}</option>`;
          });
          fieldsHtml += `
            <div class="calc-field">
              <label for="${f.id}-${inp.key}">${inp.label}</label>
              <select id="${f.id}-${inp.key}" class="sheet-input">${opts}</select>
            </div>
          `;
        } else {
          fieldsHtml += `
            <div class="calc-field">
              <label for="${f.id}-${inp.key}">${inp.label} (${inp.unit})</label>
              <input type="number" id="${f.id}-${inp.key}" class="sheet-input" value="${inp.default}" min="${inp.min || 0}">
            </div>
          `;
        }
      });

      // Step-by-step steps HTML
      let stepsHtml = '';
      f.worked_example.steps.forEach(st => {
        stepsHtml += `
          <div class="worked-step">
            <span class="step-badge">${st.label}</span>
            <div>
              <span style="font-family:var(--mono); font-size:12px; color:var(--blueprint);">${st.calculation}</span>
              &rarr; <strong style="font-family:var(--mono);">${st.result}</strong>
            </div>
          </div>
        `;
      });

      card.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:baseline; border-bottom:1px solid var(--line-strong); padding-bottom:10px; margin-bottom:14px; flex-wrap:wrap; gap:8px;">
          <div>
            <span class="kicker">${f.clause_ref}</span>
            <h3 style="font-family:var(--disp); font-size:1.35rem; font-weight:700; color:var(--ink);">${f.title}</h3>
          </div>
          <span class="badge badge-clause">${f.category}</span>
        </div>

        <p style="color:var(--ink-soft); font-size:0.95rem; margin-bottom:16px; line-height:1.6;">
          ${f.plain_explanation}
        </p>

        <!-- Formula Math Display -->
        <div class="math-block">
          $$ ${f.formula_latex} $$
        </div>

        <!-- Interactive Calculator Widget -->
        <div style="background:var(--paper); border:1px solid var(--ink); padding:20px; margin:20px 0;">
          <div class="kicker" style="color:var(--blueprint); margin-bottom:12px;">
            ⚡ LIVE CALCULATOR ENGINE
          </div>
          <div class="calculator-form">
            ${fieldsHtml}
          </div>
          <div class="calc-result-plate">
            <span class="calc-result-label">${f.calculator.output_label}:</span>
            <span class="calc-result-value" id="${f.id}-output">--</span>
          </div>
        </div>

        <!-- Variable Glossary Table -->
        <details style="margin:16px 0; border:1px solid var(--line-strong); background:var(--paper); padding:12px 16px;">
          <summary style="cursor:pointer; font-weight:600; font-family:var(--mono); font-size:11px; text-transform:uppercase; color:var(--ink-soft);">
            View Variable Breakdown &amp; Reference Units
          </summary>
          <table class="drawing-table" style="margin-top:12px;">
            <thead>
              <tr>
                <th>Symbol</th>
                <th>Variable</th>
                <th>Unit</th>
                <th>Statutory Definition</th>
              </tr>
            </thead>
            <tbody>
              ${varRows}
            </tbody>
          </table>
        </details>

        <!-- Worked Numerical Example -->
        <div class="panel-example" style="margin-top:16px;">
          <span class="kicker" style="color:var(--amber);">PRACTICAL BENCHMARK</span>
          <h4 style="font-family:var(--disp); font-size:1.05rem; font-weight:700; margin-bottom:10px; color:var(--ink);">
            Worked Example: ${f.worked_example.scenario}
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
      `;

      container.appendChild(card);

      // Wire up calculator logic
      function updateCalculation() {
        const argValues = {};
        f.calculator.inputs.forEach(inp => {
          const el = document.getElementById(`${f.id}-${inp.key}`);
          if (inp.type === 'select') {
            argValues[inp.key] = el ? el.value : inp.default;
          } else {
            argValues[inp.key] = el ? parseFloat(el.value) || 0 : inp.default;
          }
        });

        try {
          const fn = new Function(...Object.keys(argValues), f.calculator.calc_js);
          const resVal = fn(...Object.values(argValues));
          const outEl = document.getElementById(`${f.id}-output`);
          if (outEl) {
            outEl.textContent = resVal + (f.calculator.output_unit && typeof resVal === 'number' ? ' ' + f.calculator.output_unit : '');
          }
        } catch (e) {
          console.error("Calc error:", e);
        }
      }

      // Attach event listeners to all inputs
      f.calculator.inputs.forEach(inp => {
        const el = document.getElementById(`${f.id}-${inp.key}`);
        if (el) {
          el.addEventListener('input', updateCalculation);
          el.addEventListener('change', updateCalculation);
        }
      });

      // Initial run
      updateCalculation();
    });

  } catch (err) {
    console.error("Error loading formulas:", err);
    container.innerHTML = `<p style="color:var(--brick); font-family:var(--mono);">Failed to load formulas data layer.</p>`;
  }
});
