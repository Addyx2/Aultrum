"""Tidies the original dark pages (manifesto, research, privacy, apply, shop, vision...)
for launch: the Aultrum logo instead of the typed name, the current footer, and
text that was saved with the wrong encoding put right. Safe to run more than once.
CSS for these pages comes from index.css through Vite (npm run build).
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
PAGES = ["manifesto.html", "privacy.html", "apply.html", "success.html", "shop.html", "vision.html", *[str(p.relative_to(SITE)) for p in sorted((SITE / "research").rglob("*.html"))]]

LOGO = '<span class="brand-logo h-6 text-on-surface" aria-hidden="true"></span>'
LINK = "text-on-surface-variant hover:text-on-surface transition-colors"
HEAD = "font-label-sm text-label-sm text-on-surface-variant/70 uppercase tracking-widest mb-4"


def col(title, links):
    items = "".join(f'<a class="{LINK}" href="{href}">{text}</a>' for text, href in links)
    return f'<div><h4 class="{HEAD}">{title}</h4><div class="flex flex-col gap-2">{items}</div></div>'


FOOTER = f'''<footer class="w-full relative bg-surface-container-lowest border-t border-white/5 mt-auto z-20">
<div class="max-w-7xl mx-auto px-container-padding pt-stack-lg pb-8 w-full">
<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-8 mb-12">
<div class="col-span-2 lg:col-span-2 flex flex-col gap-4">
<a href="/" class="hover:opacity-80 transition-opacity" aria-label="Aultrum home">{LOGO.replace("h-6", "h-7")}</a>
<p class="font-body-md text-body-md text-on-surface-variant max-w-xs">Proactive care through Empathetic Intelligence. AI-native infrastructure for social care.</p>
<div class="flex flex-wrap gap-x-4 gap-y-2"><a class="{LINK} flex items-center gap-2" href="https://x.com/aultrumai"><span class="material-symbols-outlined text-[18px]" aria-hidden="true">alternate_email</span>X (Twitter)</a><a class="{LINK} flex items-center gap-2" href="https://instagram.com/aultrumai"><span class="material-symbols-outlined text-[18px]" aria-hidden="true">photo_camera</span>Instagram</a></div>
</div>
{col("Products", [("Elements", "/elements/"), ("Pleasant", "/pleasant/"), ("Pricing", "/pleasant/pricing/")])}
{col("Resources", [("Statements", "/statements/"), ("Editorials", "/research/index.html"), ("Merch", "/shop.html")])}
{col("Company", [("Vision", "/vision.html"), ("Manifesto", "/manifesto.html"), ("Careers", "https://clumsy-bellflower-61e.notion.site/Careers-3d8547e8d49a808e9582e864183d1d9f?source=copy_link"), ("Contact", "/apply.html")])}
{col("Privacy", [("Privacy Policy", "/privacy.html")])}
</div>
<div class="border-t border-white/5 pt-6 flex flex-col md:flex-row justify-between items-center gap-4">
<p class="font-body-md text-body-md text-on-surface-variant/60">© 2026 Aultrum. All rights reserved.</p>
<a href="/manifesto.html" class="bg-accent-blue text-on-primary px-6 py-2 rounded-full font-label-sm transition-all duration-200 active:scale-95 text-center inline-block">Manifesto</a>
</div>
</div>
</footer>'''


def fix_encoding(text):
    """Undo UTF-8 that was read as Windows-1252 and saved again (â€” for —)."""
    def undo(m):
        try:
            return m.group(0).encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            return m.group(0)
    return re.sub(r"[ÂÃâ][\u0080-¿Œ-™]{1,2}", undo, text)


for name in PAGES:
    path = SITE / name
    s = path.read_text(encoding="utf-8-sig")
    s = fix_encoding(s)
    # The typed name in headers becomes the logo.
    s = re.sub(r'<a href="([^"]*)" class="flex items-center gap-2 hover:opacity-80 transition-opacity"><span class="font-headline-md[^"]*">Aultrum</span></a>',
               lambda m: f'<a href="{m.group(1)}" class="flex items-center hover:opacity-80 transition-opacity" aria-label="Aultrum home">{LOGO}</a>', s)
    s = re.sub(r'<a href="([^"]*)" class="font-headline-md[^"]*hover:opacity-80">Aultrum</a>',
               lambda m: f'<a href="{m.group(1)}" class="flex items-center hover:opacity-80 transition-opacity" aria-label="Aultrum home">{LOGO}</a>', s)
    # Retired pages point to what replaced them.
    for old, new in [('href="../honor.html">Honor</a>', 'href="/elements/">Elements</a>'), ('href="honor.html">Honor</a>', 'href="/elements/">Elements</a>'),
                     ('href="../../flowstatebeta/peak/"', 'href="/elements/#peak"'), ('href="index.html#manifesto"', 'href="/manifesto.html"'), ('href="/blog/"', 'href="/statements/"')]:
        s = s.replace(old, new)
    # One footer per page, the current one.
    footers = list(re.finditer(r"<footer\b.*?</footer>", s, re.S))
    for f in reversed(footers[:-1]):
        s = s[: f.start()] + s[f.end():]
    if footers:
        s = re.sub(r"<footer\b.*?</footer>", lambda m: FOOTER, s, count=1, flags=re.S)
    path.write_text(s, encoding="utf-8")
    print("tidied", name, "| footers:", len(footers), "| mojibake left:", len(re.findall("â€|Â", s)))
