import os
import re
import shutil

# 1. Move public/flowstatebeta to flowstatebeta
if os.path.exists('public/flowstatebeta'):
    if os.path.exists('flowstatebeta'):
        shutil.rmtree('flowstatebeta')
    shutil.move('public/flowstatebeta', 'flowstatebeta')

# 2. Extract footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

footer_match = re.search(r'(<footer.*?</footer>)', content, re.DOTALL)
if footer_match:
    footer_html = footer_match.group(1)
    
    footer_html = re.sub(r'href="\.\./', 'href="/', footer_html)
    footer_html = re.sub(r'href="index\.html"', 'href="/"', footer_html)
    footer_html = re.sub(r'href="flowstatebeta/"', 'href="/flowstatebeta/"', footer_html)
    footer_html = re.sub(r'href="honor\.html"', 'href="/honor.html"', footer_html)
    footer_html = re.sub(r'href="flowstatebeta/pricing/index\.html"', 'href="/flowstatebeta/pricing/index.html"', footer_html)
    footer_html = re.sub(r'href="research/index\.html"', 'href="/research/index.html"', footer_html)
    footer_html = re.sub(r'href="shop\.html"', 'href="/shop.html"', footer_html)
    footer_html = re.sub(r'href="manifesto\.html"', 'href="/manifesto.html"', footer_html)
    footer_html = re.sub(r'href="apply\.html"', 'href="/apply.html"', footer_html)
    footer_html = re.sub(r'href="privacy\.html"', 'href="/privacy.html"', footer_html)
    footer_html = footer_html.replace('href="//', 'href="/')
    
    with open('components/footer.html', 'w', encoding='utf-8') as f:
        f.write(footer_html)

# 3. Replace footer in all HTML files
def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    depth = filepath.count('/')
    prefix = '../' * depth if depth > 0 else './'
    load_tag = f'<load src="{prefix}components/footer.html" />'
    
    new_html = re.sub(r'<footer.*?</footer>', load_tag, html, flags=re.DOTALL)
    
    if 'flowstatebeta' in filepath:
        new_html = re.sub(r'<script src="https://cdn\.tailwindcss\.com[^>]*></script>', '', new_html)
        css_path = f'{prefix}index.css'
        js_path = f'{prefix}main.js'
        
        if '<link rel="stylesheet"' not in new_html:
            new_html = new_html.replace('</head>', f'<link rel="stylesheet" href="{css_path}">\n</head>')
        
        if 'main.js' not in new_html:
            new_html = new_html.replace('</head>', f'<script type="module" src="{js_path}"></script>\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)

for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or 'dist' in root or 'components' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file).replace('\\', '/')
            path = path.replace('./', '', 1)
            process_html_file(path)

print("Done refactoring HTML.")
