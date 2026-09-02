import os
import re

for root, dirs, files in os.walk('flowstatebeta'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file).replace('\\', '/')
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Calculate depth for relative paths
            depth = path.count('/')
            prefix = '../' * depth if depth > 0 else './'
            aultrum_root = '../' * depth if depth > 0 else '../' # actually, from flowstatebeta/index.html it is ../index.html. Wait, depth of flowstatebeta/index.html is 1. So '../' * depth works (1 -> ../).
            
            flowstate_footer = f"""<footer class="border-t border-outline-variant bg-surface-container-lowest">
<div class="max-w-[1400px] mx-auto px-6 md:px-16 py-12">
<div class="flex flex-col md:flex-row justify-between items-center gap-4">
<div class="flex items-center gap-4"><a href="{prefix}index.html" class="font-mono text-label tracking-[0.2em] text-on-surface-variant hover:text-primary transition-colors">AULTRUM</a><span class="text-outline">/</span><span class="font-mono text-label tracking-[0.15em] text-primary">FLOWSTATE</span></div>
<div class="font-mono text-telemetry text-on-surface-variant/40">&copy; 2026 Aultrum Technologies Ltd.</div>
</div>
</div>
</footer>"""

            # Replace the Aultrum footer load tag with the Flowstate footer
            content = re.sub(r'<load src="(\.\./)+components/footer\.html" />', flowstate_footer, content)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

print("Restored Flowstate specific footer.")
