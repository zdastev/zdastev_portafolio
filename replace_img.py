import re

file_path = r'f:\Aplicaciones\zdastev\zdastev_portfolio.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(<div class="hero-photo">)\s*<img[^>]+>\s*(</div>)'
replacement = r'\1\n        <img src="foto-grande.jpeg" alt="zdastev">\n      \2'

new_content, count = re.subn(pattern, replacement, content)

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Replaced successfully {count} times.")
else:
    print("Pattern not found.")
