import os

def check_injection_points():
    lessons = [f for f in sorted(os.listdir('lessons')) if f.endswith('.html')]
    print(f"Checking {len(lessons)} lesson files...")
    
    missing_nav = []
    for f in lessons:
        p = os.path.join('lessons', f)
        with open(p, 'r', encoding='utf-8') as fl:
            c = fl.read()
        if '<!-- Back / Next Navigation' not in c:
            missing_nav.append(f)
            
    print(f"Missing Back / Next Navigation: {len(missing_nav)}")
    if missing_nav:
        print("Files:", missing_nav)

check_injection_points()
