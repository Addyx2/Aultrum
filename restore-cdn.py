import os
import re

for root, dirs, files in os.walk('flowstatebeta'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file).replace('\\', '/')
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove index.css and main.js properly
            content = re.sub(r'<link rel="stylesheet" href="(\.\./)+index\.css">\n?', '', content)
            content = re.sub(r'<script type="module" src="(\.\./)+main\.js"></script>\n?', '', content)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

print("Fixed CDN removal.")
