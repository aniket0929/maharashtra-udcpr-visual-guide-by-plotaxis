import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('lessons', exist_ok=True)

def create_lesson_page(lesson_data):
    quiz_js_questions = json.dumps(lesson_data['quiz'], ensure_ascii=False)
    
    amend_badge = f'<span class="badge badge-amended">Amended (#) {lesson_data["amendment_cite"]}</span>' if lesson_data.get('amendment_cite') else ''
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{lesson_data['clause']} {lesson_data['title']} | UDCPR from Scratch</title>
  <meta name="description" content="{lesson_data['meta_desc']}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/blueprint.css">
  <link rel="stylesheet" href="/css/components.css">
</head>
<body>

  <!-- THE DRAWING SHEET CONTAINER -->
  <div class="sheet">
    <div class="ruler-top"></div>
    <div class="corner-tick tl"></div>
    <div class="corner-tick tr"></div>
    <div class="corner-tick bl"></div>
    <div class="corner-tick br"></div>

    <!-- Statutory Disclaimer Strip -->
    <div class="disclaimer-strip">
      <strong>DISCLAIMER:</strong> Educational summary and reference guide only, not legal or municipal advice. Always verify with official Government Notifications and sanctioned Development Plans.
    </div>

    <!-- Sheet Navigation -->
    <nav class="sheet-nav">
      <a href="/" class="brand-block">
        <span class="brand-stamp">UDCPR</span>
        <div class="brand-title-group">
          <h1>UDCPR from Scratch</h1>
          <span>Drawing Sheet • Lesson Blueprint</span>
        </div>
      </a>

      <ul class="nav-menu">
        <li class="nav-item"><a href="/topics/">Topics</a></li>
        <li class="nav-item"><a href="/chapters/{lesson_data['ch_slug']}.html" class="active">{lesson_data['ch_title']}</a></li>
        <li class="nav-item"><a href="/glossary.html">Glossary</a></li>
        <li class="nav-item"><a href="/formulas.html">Formulas</a></li>
        <li class="nav-item"><a href="/amendments.html">Amendments (#)</a></li>
        <li class="nav-item"><a href="/govt-orders.html">Orders</a></li>
      </ul>

      <div class="nav-tools">
        <button class="tool-btn" onclick="openSearchModal()">Search <kbd style="font-family:var(--mono);">Ctrl+K</kbd></button>
      </div>
    </nav>

    <!-- Lesson Body -->
    <main style="max-width: 960px; margin: 0 auto; padding-top: 10px;">

      <!-- Breadcrumbs & Kicker Tags -->
      <div class="kicker-muted" style="margin-bottom: 10px;">
        <a href="/" style="color:var(--ink-soft); text-decoration:none;">HOME</a> / 
        <a href="/chapters/{lesson_data['ch_slug']}.html" style="color:var(--ink-soft); text-decoration:none;">{lesson_data['ch_title'].upper()}</a> / 
        <span style="color:var(--blueprint);">{lesson_data['clause']}</span>
      </div>

      <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
        <span class="badge badge-clause">{lesson_data['clause']}</span>
        {amend_badge}
        <span class="badge badge-status-done">{lesson_data['badge_status']}</span>
      </div>

      <h1 style="font-size:2.2rem; margin-bottom:12px; line-height:1.2;">
        {lesson_data['title']}
      </h1>

      <p style="font-size:1.05rem; color:var(--ink-soft); line-height:1.6; margin-bottom:28px;">
        {lesson_data['lead_summary']}
      </p>

      <!-- 1. PLAIN LANGUAGE SUMMARY -->
      <section style="margin-bottom:32px;">
        <span class="kicker">01 // EXECUTIVE SUMMARY</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Plain-Language Executive Summary</h2>
        <div class="panel-info">
          {lesson_data['plain_summary_html']}
        </div>
      </section>

      <!-- 2. THE STATUTORY RULE -->
      <section style="margin-bottom:32px;">
        <span class="kicker">02 // STATUTORY RULE</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Statutory Rule &amp; Clause Breakdown</h2>
        <div class="panel-info" style="border-left-color: var(--blueprint);">
          <div class="kicker" style="color:var(--blueprint); margin-bottom:6px;">UDCPR {lesson_data['clause']} STATUTORY PROVISION</div>
          <p style="font-size:0.92rem; color:var(--ink); font-style:italic; line-height:1.6;">
            "{lesson_data['statutory_extract']}"
          </p>
        </div>
        {lesson_data['clause_cards_html']}
      </section>

      <!-- 3. BLUEPRINT PLATE / KEY NUMBERS TABLE -->
      <section style="margin-bottom:32px;">
        <span class="kicker">03 // SPECIFICATION &amp; DATA PLATE</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Blueprint Plate &amp; Key Numbers Table</h2>
        {lesson_data['plate_or_table_html']}
      </section>

      <!-- 4. WORKED NUMERICAL EXAMPLE -->
      <section style="margin-bottom:32px;">
        <span class="kicker" style="color:var(--amber);">04 // WORKED PRACTICAL EXAMPLE</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Worked Practical Calculation</h2>
        <div class="panel-example">
          {lesson_data['worked_example_html']}
        </div>
      </section>

      <!-- 5. COMMON PITFALLS & SITE WATCHOUTS -->
      <section style="margin-bottom:32px;">
        <span class="kicker" style="color:var(--brick);">05 // SCRUTINY WATCHOUTS</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Common Pitfalls &amp; Sanction Watchouts</h2>
        <div class="panel-alert">
          <div style="display:flex; flex-direction:column; gap:12px;">
            {lesson_data['pitfalls_html']}
          </div>
        </div>
      </section>

      <!-- 6. AMENDMENT / CLARIFICATION HISTORY -->
      <section style="margin-bottom:32px;">
        <span class="kicker">06 // AMENDMENT HISTORY</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Amendment &amp; Clarification History (#)</h2>
        <div class="panel-info">
          {lesson_data['amendment_section_html']}
        </div>
      </section>

      <!-- 7. INTERACTIVE QUIZ -->
      <section style="margin-bottom:32px;">
        <span class="kicker">07 // VERIFICATION QUIZ</span>
        <h2 style="font-size:1.25rem; margin-bottom:12px;">Quick Quiz: Check Your Understanding</h2>
        <div class="quiz-container" id="{lesson_data['quiz_id']}"></div>
      </section>

      <!-- Back / Next Navigation (Bordered Button Group) -->
      <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--ink); padding-top:20px; margin-top:36px; flex-wrap:wrap; gap:12px;">
        <a href="{lesson_data['prev_url']}" class="tool-btn" style="padding:8px 16px; text-decoration:none;">
          ← {lesson_data['prev_title']}
        </a>
        <a href="{lesson_data['next_url']}" class="tool-btn" style="background:var(--ink); color:var(--paper-raised); padding:8px 16px; text-decoration:none;">
          {lesson_data['next_title']} →
        </a>
      </div>

    </main>

    <!-- Sheet Footer -->
    <footer class="sheet-footer">
      <div>UDCPR FROM SCRATCH • MAHARASHTRA UNIFIED DCRP-2020</div>
      <div>REG. {lesson_data['clause']} • DRAWING SHEET SYSTEM</div>
    </footer>
  </div>

  <!-- Universal Search Modal -->
  <div class="search-modal-backdrop" id="search-modal-backdrop" onclick="if(event.target === this) closeSearchModal()">
    <div class="search-modal">
      <div class="search-modal-header">
        <span style="font-family:var(--mono); font-size:13px; font-weight:700;">SEARCH //</span>
        <input type="text" id="search-modal-input" class="search-modal-input" placeholder="Type clause (e.g. 3.4.1), term (e.g. FSI), or keyword..." autocomplete="off">
        <button onclick="closeSearchModal()" class="tool-btn" style="padding:2px 8px;">ESC</button>
      </div>
      <ul class="search-results-list" id="search-results-list"></ul>
    </div>
  </div>

  <script src="/js/app.js"></script>
  <script src="/js/search.js"></script>
  <script src="/js/quiz.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {{
      const questions = {quiz_js_questions};
      initQuiz('{lesson_data['quiz_id']}', questions, '{lesson_data['lesson_id']}');
    }});
  </script>
</body>
</html>"""
    
    file_path = os.path.join('lessons', lesson_data['filename'])
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated lesson: {file_path}")
