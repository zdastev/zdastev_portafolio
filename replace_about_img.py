import re

file_path = r'f:\Aplicaciones\zdastev\zdastev_portfolio.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(<img class="about-photo"\s*src=")data:image/[^"]+(")'
replacement = r'\1foto-grande.jpeg\2'

new_content, count = re.subn(pattern, replacement, content)

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Replaced about-photo successfully {count} times.")
else:
    print("Pattern not found for about-photo.")
