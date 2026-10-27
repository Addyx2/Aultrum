"""Writes aultrum.co.uk/statements/: Aultrum's statements (formerly the blog), in the
homepage's design. Header and footer come from index.html. CSS: npm run build:home-css.
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
ROOT = SITE / "public" / "statements"

home = (SITE / "index.html").read_text(encoding="utf-8")
head = home[: home.index("<header")].replace('<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n', '<link rel="icon" href="/brand/icon.svg" type="image/svg+xml">\n')
header = home[home.index("<header") : home.index("</header>") + 9]
footer = home[home.index("<footer") : home.index("</footer>") + 9]

W = "max-w-[1320px] mx-auto px-margin md:px-margin-md lg:px-margin-lg"
EYEBROW = "font-label-mono text-label-mono text-ink-primary uppercase tracking-wider"
ARROW = '<span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span>'

STATEMENTS = [
    {
        "slug": "quality-yardstick",
        "kind": "Thesis",
        "date": "October 2026",
        "title": "The Quality Yardstick",
        "summary": "Why “is quality care being delivered, and is it consistent?” is the right question to automate.",
        "body": [
            "Aultrum is built on the premise that the hardest and most important question in social care is this: is quality care being delivered, and is it consistent?",
            "Most systems record activity. The Quality Yardstick measures judgement.",
            "Persona Intelligence learns from expert decisions to codify that standard, and applies it continuously.",
        ],
    },
    {
        "slug": "persona-intelligence",
        "kind": "Research",
        "date": "October 2026",
        "title": "Persona Intelligence: Judgement Computerised",
        "summary": "A new category of system that learns to judge by doing.",
        "body": [
            "Persona Intelligence is the discipline of computerising judgement: learning what good looks like from expert decisions, and applying it consistently at scale.",
            "It builds a living model of quality that evolves with the organisation.",
        ],
    },
]


def page_head(title, description):
    h = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", head)
    return re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{description}">', h)


def page_header():
    nav = re.search(r'<nav class="hidden lg:flex[^"]*"[^>]*>.*?</nav>', header, re.S).group(0)
    marked = nav.replace('class="font-body-sm text-body-sm text-on-surface-variant hover:text-ink-primary transition-colors" data-path="statements"', 'class="font-body-sm text-body-sm text-ink-primary" aria-current="page" data-path="statements"')
    return header.replace(nav, marked)


def write(path, title, description, main):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page_head(title, description) + page_header() + main + footer + "\n</body>\n</html>\n", encoding="utf-8")
    print("wrote", path)


def main_wrap(inner):
    return f'<main class="w-full pt-16 bg-surface min-h-[calc(100vh-4rem)]"><div class="flex flex-col w-full text-on-surface">{inner}</div></main>'


def card(s):
    return f'''<a class="group bg-surface-container-low rounded-xl p-8 flex flex-col gap-3 border border-border-editorial shadow-sm hover:border-ink-primary transition-colors min-w-0" href="/statements/{s["slug"]}/">
<p class="{EYEBROW}">{s["kind"]} · {s["date"]}</p>
<h2 class="font-headline-md text-headline-sm md:text-headline-md text-ink-dark tracking-tight">{s["title"]}</h2>
<p class="font-body-md text-ink-muted">{s["summary"]}</p>
<span class="mt-auto pt-4 inline-flex items-center gap-2 font-body-sm font-medium text-ink-primary group-hover:translate-x-1 transition-transform">Read{ARROW}</span>
</a>'''


also = f'''<section class="w-full border-t border-border-editorial"><div class="{W} py-16 grid grid-cols-1 md:grid-cols-2 gap-6">
<a class="flex items-center justify-between gap-4 p-6 rounded-xl border border-border-editorial hover:border-ink-primary transition-colors" href="/vision.html"><span><span class="block {EYEBROW}">Vision</span><span class="block mt-1 font-body-lg text-ink-dark">Our invitation to partners</span></span>{ARROW}</a>
<a class="flex items-center justify-between gap-4 p-6 rounded-xl border border-border-editorial hover:border-ink-primary transition-colors" href="/manifesto.html"><span><span class="block {EYEBROW}">Manifesto</span><span class="block mt-1 font-body-lg text-ink-dark">What we believe about care</span></span>{ARROW}</a>
</div></section>'''

index = main_wrap(f'''<section class="w-full pt-10 pb-16 md:pt-16 md:pb-24 {W}">
<div class="max-w-3xl flex flex-col items-start gap-space-md mb-12"><p class="{EYEBROW}">Statements</p><h1 class="font-display-hero text-headline-lg md:text-display-hero text-ink-primary tracking-tight">What we think about quality in care.</h1><p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">Short statements on Persona Intelligence, and how quality care can be measured.</p></div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">{"".join(card(s) for s in STATEMENTS)}</div>
</section>{also}''')
write(ROOT / "index.html", "Statements | Aultrum", "Aultrum's statements on Persona Intelligence and quality in social care.", index)

for s in STATEMENTS:
    body = "".join(f'<p>{p}</p>' for p in s["body"])
    article = main_wrap(f'''<article class="w-full pt-10 pb-16 md:pt-16 md:pb-24 {W}"><div class="max-w-3xl">
<a class="inline-flex items-center gap-1 font-body-sm text-ink-muted hover:text-ink-primary" href="/statements/"><span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_back</span>Statements</a>
<p class="mt-8 {EYEBROW}">{s["kind"]} · {s["date"]}</p>
<h1 class="mt-3 font-display-hero text-headline-lg md:text-display-hero text-ink-primary tracking-tight">{s["title"]}</h1>
<p class="mt-4 font-body-lg text-body-lg text-on-surface-variant">{s["summary"]}</p>
<div class="mt-10 pt-10 border-t border-border-editorial flex flex-col gap-5 font-body-lg text-body-lg text-ink-dark">{body}</div>
</div></article>{also}''')
    write(ROOT / s["slug"] / "index.html", f'{s["title"]} · Statements | Aultrum', s["summary"].replace("“", "").replace("”", ""), article)
