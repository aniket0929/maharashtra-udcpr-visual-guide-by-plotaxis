import os
import re

def audit_progress():
    print("=== AUDITING LESSON PROGRESS MECHANISM ===")
    lessons = [f for f in sorted(os.listdir('lessons')) if f.endswith('.html')]
    print(f"Total lesson files: {len(lessons)}")

    init_quiz_pattern = re.compile(r'initQuiz\s*\(\s*["\']([^"\']+)["\']\s*,\s*questions\s*,\s*["\']([^"\']+)["\']')
    
    with_quiz = []
    missing_quiz = []
    unique_ids = set()

    for f in lessons:
        path = os.path.join('lessons', f)
        with open(path, 'r', encoding='utf-8') as fl:
            content = fl.read()
        m = init_quiz_pattern.search(content)
        if m:
            container_id, lesson_id = m.group(1), m.group(2)
            with_quiz.append((f, container_id, lesson_id))
            unique_ids.add(lesson_id)
        else:
            missing_quiz.append(f)

    print(f"Lessons with initQuiz: {len(with_quiz)}")
    print(f"Lessons missing initQuiz: {len(missing_quiz)}")
    if missing_quiz:
        print(f"  Missing: {missing_quiz}")
    print(f"Unique lesson IDs registered in initQuiz: {len(unique_ids)}")

audit_progress()
