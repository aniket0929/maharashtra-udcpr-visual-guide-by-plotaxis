import glob
import re
import os

html_files = glob.glob('**/*.html', recursive=True)
print(f"Scanning {len(html_files)} HTML files to remove Orders nav item...")

pattern = re.compile(r'\s*<li class="nav-item">\s*<a href="/govt-orders\.html"[^>]*>.*?</a>\s*</li>', re.IGNORECASE)

modified_count = 0
for hf in html_files:
    if hf == 'govt-orders.html':
        continue
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if pattern.search(content):
        new_content = pattern.sub('', content)
        with open(hf, 'w', encoding='utf-8') as f:
            f.write(new_content)
        modified_count += 1

print(f"Removed Orders nav item from {modified_count} files.")

# Replace govt-orders.html with a clean redirect to /amendments.html
redirect_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=/amendments.html">
  <title>Redirecting to Statutory Clarifications...</title>
  <link rel="canonical" href="/amendments.html">
</head>
<body style="font-family:sans-serif; text-align:center; padding:50px;">
  <h2>Redirecting to Amendments &amp; Clarifications (#)...</h2>
  <p>If you are not redirected automatically, <a href="/amendments.html">click here</a>.</p>
</body>
</html>
"""

with open('govt-orders.html', 'w', encoding='utf-8') as f:
    f.write(redirect_html)

print("Replaced govt-orders.html with instant client redirect to /amendments.html")
