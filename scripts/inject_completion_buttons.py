import os

COMPLETION_BLOCK = """      <!-- Lesson Completion Bar -->
      <div class="lesson-completion-card" id="completion-block">
        <div class="lesson-completion-info">
          <span class="kicker-muted">LESSON PROGRESSION</span>
          <div class="lesson-completion-title" id="completion-title">Lesson In Progress</div>
          <div class="lesson-completion-subtitle" id="completion-sub">
            Click to mark this lesson complete, or score &ge; 75% on the verification quiz to complete automatically.
          </div>
        </div>
        <button type="button" class="btn-mark-complete" id="btn-mark-complete">
          <span class="btn-icon" id="btn-completion-icon">○</span>
          <span class="btn-text" id="btn-completion-text">Mark as Completed</span>
        </button>
      </div>

"""

def inject():
    lessons = [f for f in sorted(os.listdir('lessons')) if f.endswith('.html')]
    print(f"Processing {len(lessons)} lesson files...")
    
    injected_count = 0
    already_has = 0
    
    for f in lessons:
        path = os.path.join('lessons', f)
        with open(path, 'r', encoding='utf-8') as fl:
            content = fl.read()
            
        if 'class="lesson-completion-card"' in content or 'id="completion-block"' in content:
            already_has += 1
            continue
            
        target = '<!-- Back / Next Navigation'
        if target in content:
            new_content = content.replace(target, COMPLETION_BLOCK + '      ' + target, 1)
            with open(path, 'w', encoding='utf-8') as fl:
                fl.write(new_content)
            injected_count += 1
        else:
            print(f"WARNING: Target not found in {f}")
            
    print(f"Injection complete! Injected: {injected_count}, Already present: {already_has}, Total: {len(lessons)}")

inject()
