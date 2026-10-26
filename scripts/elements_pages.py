"""Writes aultrum.co.uk/elements/ and /elements/book-a-demo/ in the homepage's design.

Elements is the platform (Gateway, Peak, custom modules); the console that
manages it is the Canvas app at canvas.aultrum.co.uk. /canvas/ redirects here.
Header and footer come from the homepage (index.html). CSS: npm run build:home-css.
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
ROOT = SITE / "public" / "elements"
CONSOLE = "https://canvas.aultrum.co.uk"
DEMO = "/elements/book-a-demo/"
CONTACT = "Wisdom@aultrum.co.uk"

home = (SITE / "index.html").read_text(encoding="utf-8")
head = home[: home.index("<header")].replace('<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n', "")
header = home[home.index("<header") : home.index("</header>") + 9]
footer = home[home.index("<footer") : home.index("</footer>") + 9]

NAV = [("Modules", "/elements/#modules", "modules"), ("How it works", "/elements/#how", "how"), ("Custom builds", "/elements/#custom", "custom"), ("Console", "/elements/#console", "console"), ("Pleasant", "/pleasant/", "pleasant")]


def page_head(title, description):
    h = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", head)
    return re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{description}">\n<meta property="og:image" content="https://aultrum.co.uk/elements/img/dashboard.jpg">', h)


def page_header(active):
    """Homepage header as AULTRUM / ELEMENTS, with the Elements menu, demo and console log in."""
    h = header.replace('<span class="text-outline-variant font-body-sm">/</span>', '<span class="text-outline-variant font-body-sm">/</span><span class="text-ink-dark">ELEMENTS</span>', 1)
    nav = re.search(r'<nav class="hidden lg:flex[^"]*"[^>]*>.*?</nav>', h, re.S).group(0)

    def item(t, href, key):
        if key == active:
            return f'<a class="font-body-sm text-body-sm text-ink-primary" aria-current="page" href="{href}">{t}</a>'
        return f'<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-ink-primary transition-colors" href="{href}">{t}</a>'

    h = h.replace(nav, re.sub(r">.*</nav>", ">" + "".join(item(*n) for n in NAV) + "</nav>", nav, flags=re.S))
    h = h.replace('data-path="login" href="https://workspace.aultrum.co.uk"', f'data-path="login" href="{CONSOLE}/login"')
    return h.replace('data-path="book-a-demo" href="/pleasant/book-a-demo/"', f'data-path="book-a-demo" href="{DEMO}"')


def write(path, title, description, active, main, extra=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page_head(title, description) + page_header(active) + main + footer + extra + "\n</body>\n</html>\n", encoding="utf-8")
    print("wrote", path)


W = "max-w-[1320px] mx-auto px-margin md:px-margin-md lg:px-margin-lg"
BAND, CTA = "#001da6", "#0021cc"
PILL_TEXT, DOT, SOFT = "#a5c4ff", "#528eff", "#b8d2ff"
H1 = "font-display-hero text-headline-lg md:text-display-hero text-ink-primary tracking-tight"
H2 = "font-headline-lg text-headline-md md:text-headline-lg text-ink-dark tracking-tight"
H2_WHITE = "font-headline-lg text-headline-md md:text-headline-lg text-white tracking-tight"
BTN = "inline-flex items-center justify-center gap-1.5 bg-ink-primary text-on-primary font-body-sm px-5 py-3 rounded-full hover:bg-primary-container transition-all"
ARROW = '<span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span>'
GRID = '<div class="absolute inset-0 z-0 overflow-hidden pointer-events-none"><div class="absolute inset-0 opacity-15" style="background-image: linear-gradient(to right, #ffffff 1px, transparent 1px), linear-gradient(to bottom, #ffffff 1px, transparent 1px); background-size: 32px 32px;"></div></div>'
SHADOW = "shadow-[0_28px_70px_-24px_rgba(0,16,90,0.55)]"


def eyebrow(t):
    return f'<div class="font-label-mono text-label-mono text-ink-primary uppercase tracking-wider mb-2">{t}</div>'


def chip(t):
    return f'<span class="px-2.5 py-1 bg-surface rounded-full text-ink-secondary font-label-mono text-label-mono border border-border-editorial">{t}</span>'


def pill(t):
    return f'<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-[{PILL_TEXT}] font-label-mono text-label-mono uppercase tracking-wider mb-3"><span class="w-1.5 h-1.5 rounded-full bg-[{DOT}] animate-pulse"></span>{t}</div>'


def frame(src, alt, w=2880, h=1800, base="/elements/img"):
    return f'<figure class="min-w-0 bg-surface-container-low border border-border-editorial rounded-xl p-2 shadow-sm"><img class="w-full h-auto rounded-lg border border-border-editorial" src="{base}/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></figure>'


def check_list(items, dark=False):
    line, icon, text = ("border-white/15", "text-[#b8d2ff]", "text-white/90") if dark else ("border-border-editorial", "text-ink-primary", "text-ink-dark")
    return '<ul class="w-full">' + "".join(f'<li class="flex gap-3 py-3 border-t {line}"><span class="material-symbols-outlined text-[18px] {icon} shrink-0" aria-hidden="true">check</span><span class="font-body-md {text}">{i}</span></li>' for i in items) + "</ul>"


def cell(icon, label, title, text):
    lab = f'<span class="font-label-mono text-label-mono text-ink-primary uppercase tracking-wider">{label}</span>' if label else ""
    return f'<div class="bg-surface-container-lowest p-6 md:p-8 flex flex-col gap-3"><span class="material-symbols-outlined text-[22px] text-ink-primary" aria-hidden="true">{icon}</span>{lab}<h3 class="font-headline-sm text-headline-sm text-ink-dark">{title}</h3><p class="font-body-md text-ink-muted">{text}</p></div>'


def stat(n, label, text, hi=False):
    if hi:
        return f'<div class="relative overflow-hidden bg-gradient-to-b from-[#0021cc]/80 to-[#001490] backdrop-blur-md border border-[#528eff]/40 p-8 rounded-xl flex flex-col justify-between shadow-md"><div class="absolute -top-16 -right-16 w-48 h-48 rounded-full bg-[#528eff]/30 blur-2xl pointer-events-none"></div><div class="relative z-10"><div class="font-stat-number text-stat-number text-white tracking-tight">{n}</div><div class="font-headline-sm text-headline-sm text-[{SOFT}] mt-2">{label}</div><p class="font-body-sm text-white/80 mt-6">{text}</p></div></div>'
    return f'<div class="bg-white/10 backdrop-blur-md border border-white/20 p-8 rounded-xl flex flex-col justify-between shadow-sm"><div><div class="font-stat-number text-stat-number text-white tracking-tight">{n}</div><div class="font-headline-sm text-headline-sm text-[{SOFT}] mt-2">{label}</div></div><p class="font-body-sm text-white/75 mt-6">{text}</p></div>'


def module(id, icon, name, text, chips, points):
    return f'''<article id="{id}" class="scroll-mt-24 bg-surface-container-low rounded-xl p-8 flex flex-col border border-border-editorial shadow-sm min-w-0">
<div class="flex items-center justify-between mb-6"><div class="flex items-center gap-3"><span class="w-10 h-10 rounded-full bg-ink-primary text-on-primary flex items-center justify-center shrink-0"><span class="material-symbols-outlined text-[20px]" aria-hidden="true">{icon}</span></span><h3 class="font-headline-md text-headline-sm md:text-headline-md text-ink-dark">{name}</h3></div><span class="px-2.5 py-1 rounded-full bg-ink-primary/10 text-ink-primary font-label-mono text-[10px] tracking-wider font-medium uppercase">LIVE</span></div>
<p class="font-body-md text-ink-muted mb-6">{text}</p>
<div class="flex flex-wrap gap-2 mb-6">{"".join(chip(c) for c in chips)}</div>
{check_list(points)}
<a class="mt-8 inline-flex items-center gap-2 font-body-sm font-medium text-ink-primary hover:translate-x-1 transition-transform" href="{DEMO}"><span>BOOK A {name.upper()} DEMO</span>{ARROW}</a>
</article>'''


def feature(id, label, title, body, items, image, flip=False):
    text = f'<div class="lg:col-span-5 flex flex-col items-start gap-4 min-w-0">{eyebrow(label)}<h2 class="{H2}">{title}</h2><p class="font-body-lg text-body-lg text-ink-muted">{body}</p>{check_list(items)}</div>'
    pic = f'<div class="lg:col-span-7 min-w-0 {"lg:order-first" if flip else ""}">{image}</div>'
    return f'<section id="{id}" class="w-full scroll-mt-20 border-t border-border-editorial"><div class="{W} py-16 md:py-24 grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">{text}{pic}</div></section>'


def cta_band(title, text, second):
    return f'''<section class="w-full relative overflow-hidden bg-[{CTA}] py-20 md:py-28 text-center flex flex-col items-center">{GRID}<div class="relative z-10 {W} flex flex-col items-center">{pill("DEPLOY_ELEMENTS")}<h2 class="font-display-hero text-headline-lg md:text-display-hero text-white tracking-tight max-w-3xl">{title}</h2><p class="font-body-lg text-white/80 max-w-xl mt-4 mb-8">{text}</p><div class="flex flex-col sm:flex-row items-center gap-4"><a class="inline-flex items-center gap-2 bg-white text-ink-primary font-body-sm font-medium px-8 py-3.5 rounded-full hover:bg-white/90 transition-all shadow-md" href="{DEMO}"><span>Book a demo</span>{ARROW}</a>{second}</div></div></section>'''


def main_wrap(inner):
    return f'<main class="w-full pt-16 bg-surface"><div class="flex flex-col w-full text-on-surface">{inner}</div></main>'


# ---------------------------------------------------------------- Overview
STEPS = [
    ("key", "01", "Get your keys", "Create your organisation in the Elements console and get credentials for your own systems."),
    ("toggle_on", "02", "Switch on what you need", "Add Gateway, Peak or Persona for the services you run, in Flowstate, Pleasant or your own system."),
    ("cable", "03", "Connect your systems", "Show Elements inside your software, exchange signed events, and give Persona the tools it may use, under your own rules."),
    ("monitoring", "04", "Watch it work", "See every installation, conversation and event in one console, with delivery status and an audit trail."),
]
CODE = f'''<span class="text-white/50"># Switch Gateway on for one of your services</span>
curl -X POST {CONSOLE}/api/v1/installations \\
  -u "$CLIENT_ID:$CLIENT_SECRET" \\
  -H "Content-Type: application/json" \\
  -d '{{"module":"gateway","tenantId":"north_branch",
       "tenantName":"North branch"}}'

<span class="text-white/50"># Show it inside your own system</span>
curl -X POST {CONSOLE}/api/v1/embed-tokens \\
  -u "$CLIENT_ID:$CLIENT_SECRET" \\
  -d '{{"installationId":"…","user":{{"id":"u_42","name":"Amara"}}}}'
<span class="text-[#b8d2ff]">→ {{"url":"{CONSOLE}/embed/gateway?token=…"}}</span>'''

art_panel = f'''<figure class="relative overflow-hidden rounded-xl aspect-[4/3] md:aspect-[16/9] bg-[#2a46e0] bg-cover bg-center" style="background-image:url(/img/home/art-wide.jpg)"><img class="absolute left-[6%] top-[10%] w-[112%] max-w-none h-auto rounded-lg ring-1 ring-black/10 {SHADOW}" src="/elements/img/dashboard.jpg" alt="The Elements console: Gateway and Peak, connected systems, installations and recent events" width="2880" height="1800" loading="lazy"><figcaption class="absolute bottom-3 left-3 px-3 py-1.5 rounded-full bg-surface/90 backdrop-blur-md font-body-sm text-body-sm text-ink-dark">The Elements console</figcaption></figure>'''

overview = main_wrap(f'''
<section class="w-full pt-10 pb-16 md:pt-16 md:pb-24 {W}">
<div class="max-w-4xl flex flex-col items-start gap-space-md mb-12">
<h1 class="{H1}">Care modules that run on their own, or inside the platform you use.</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mt-1">Elements is the foundation underneath Aultrum. Gateway answers every call and message; Peak rewards the people who deliver care. Switch them on in Flowstate or Pleasant, or run them on their own.</p>
<div class="w-full max-w-xl mt-4 flex flex-col sm:flex-row items-stretch sm:items-center gap-3"><a class="{BTN}" href="{DEMO}"><span>Book a demo</span><span class="material-symbols-outlined text-[16px]" aria-hidden="true">arrow_forward</span></a><a class="inline-flex items-center justify-center font-body-sm text-ink-primary hover:text-ink-dark px-4 py-3 rounded-full transition-colors font-medium" href="#how">See how it works</a></div>
<div class="flex flex-wrap items-center gap-2 mt-6"><span class="font-label-mono text-label-mono text-ink-muted uppercase tracking-wider mr-1">Runs on its own, or inside</span>{chip("FLOWSTATE")}{chip("PLEASANT")}</div>
</div>
{art_panel}
</section>
<section class="w-full relative overflow-hidden bg-[{BAND}]">{GRID}<div class="relative z-10 {W} pt-16 md:pt-24 pb-16 md:pb-24">
<div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6"><h2 class="{H2_WHITE}">Your phone rings. No one answers.</h2><p class="font-body-md text-white/80 max-w-md">Care agencies lose 20% of potential clients to after-hours gaps and spend 37% more on manual inbound handling.</p></div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">{stat("20%", "CLIENTS LOST", "Potential clients lost to after-hours gaps.")}{stat("37%", "EXTRA COST", "Additional expenses from manual inbound handling.")}{stat("4.2hr", "AVG DELAY", "Before a missed call is returned.")}{stat("68%", "CALLER FRUSTRATION", "Will call a competitor instead.", True)}</div>
</div></section>
<section id="modules" class="w-full scroll-mt-20 py-16 md:py-24 {W}">
<div class="max-w-2xl mb-12">{eyebrow("MODULES")}<h2 class="{H2}">Two modules. One foundation.</h2><p class="font-body-lg text-ink-muted mt-3">Elements closes the gaps between first contact and the people who deliver care. Add the modules you need and only pay for the ones you use.</p></div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
{module("gateway", "call", "Gateway", "One conversation layer for phone, SMS, WhatsApp and web chat. It recognises who is calling, routes to the right agent or person, and hands emergencies straight to a human.", ["LIVE CALLS", "CRM LOGS", "ABILITIES", "PERSONNEL IN LOOP"], ["Answers calls and messages at any hour", "Logs every interaction into your records", "Hands over to your team when a person is needed"])}
{module("peak", "workspace_premium", "Peak", "Recognition that pays. Points for shifts, punctuality, and praise — cashed out, spent on benefits, or unlocked as financial perks.", ["EARN POINTS", "CASH OUT", "PERKS", "FINANCIAL LEDGER"], ["Points for shifts, punctuality and praise", "Cash out, spend on benefits or unlock perks", "Every point recorded in a ledger"])}
</div></section>
{feature("persona", "PERSONA", "The AI that understands care delivery.", "Persona answers questions from your data and prepares work for your team, using the tools you choose to give it. Nothing changes until a person approves it.", ["Works with your systems' tools, inside each person's permissions", "Every change waits for approval, and every action is audited", "Automations such as a morning briefing or a compliance watch"], frame("assist.jpg", "Persona Assist in Pleasant, preparing a shift assignment and waiting for approval", base="/pleasant/img"))}
<section id="how" class="w-full scroll-mt-20 border-t border-border-editorial"><div class="{W} py-16 md:py-24">
<div class="max-w-2xl mb-12">{eyebrow("HOW IT WORKS")}<h2 class="{H2}">Your systems stay in charge.</h2><p class="font-body-lg text-ink-muted mt-3">Elements never writes to your data directly. It asks your system to act through its own tools, so your permissions, approvals and records still apply.</p></div>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">{"".join(cell(*s) for s in STEPS)}</div>
</div></section>
<section class="w-full border-t border-border-editorial"><div class="{W} py-16 md:py-24">
<div class="max-w-2xl mb-12">{eyebrow("WHERE IT RUNS")}<h2 class="{H2}">One set of modules, wherever you work.</h2><p class="font-body-lg text-ink-muted mt-3">Elements is built once and shows up where your team already is.</p></div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">
{cell("hub", "", "On its own", "Run Gateway and Peak alongside the systems you already have, managed from the Elements console.")}
{cell("home_health", "", "Inside Flowstate", "Switch modules on in Flowstate, Aultrum’s platform for home care coordination.")}
{cell("badge", "", "Inside Pleasant", "Switch modules on in Pleasant, the back office for care staffing agencies.")}
</div></div></section>
<section id="custom" class="w-full scroll-mt-20 relative overflow-hidden bg-[{BAND}]">{GRID}<div class="relative z-10 {W} py-16 md:py-24 grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">
<div class="lg:col-span-5 flex flex-col items-start gap-4 min-w-0">{pill("CUSTOM BUILDS")}<h2 class="{H2_WHITE}">Have an idea? We build it on Elements.</h2><p class="font-body-lg text-white/80">Tell us the workflow you wish you had. We build it as a custom module for your organisation, on the same foundations as Gateway and Peak, and it appears in the console alongside them.</p>{check_list(["Private to your organisation by default", "The same security as every Element: signed links, signed events, full audit trail", "Works with Persona, so your AI can use it too"], dark=True)}<a class="mt-2 inline-flex items-center gap-2 bg-white text-ink-primary font-body-sm font-medium px-6 py-3 rounded-full hover:bg-white/90 transition-all" href="{DEMO}"><span>Talk to us about a build</span>{ARROW}</a></div>
<div class="lg:col-span-7 min-w-0"><pre class="overflow-x-auto bg-[#000b63]/70 border border-white/15 rounded-xl p-5 md:p-6 font-label-mono text-[12px] leading-relaxed text-white/90"><code>{CODE}</code></pre></div>
</div></section>
{feature("console", "THE CONSOLE", "Everything in one place.", "Manage your keys, the systems you've connected, what's switched on where, and everything flowing between them.", ["Preview any Element exactly as your team sees it", "Pause an installation, or send a test event to check the connection", "Credentials shown once, rotated or revoked in a click"], frame("installations.jpg", "Installations in the Elements console: each Element and service with its status and events"), flip=True)}
<section class="w-full border-t border-border-editorial"><div class="{W} py-16 md:py-24">
<div class="max-w-2xl mb-12">{eyebrow("SECURITY")}<h2 class="{H2}">Built for care data.</h2></div>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">
{cell("block", "", "No direct writes", "Elements and Persona ask your system to act; your rules decide.")}
{cell("lock", "", "Locked-down screens", "Element screens only open inside the systems you allow.")}
{cell("verified", "", "Signed everything", "Links and events are signed and expire, so they can't be forged or replayed.")}
{cell("history", "", "Full event log", "Every event in and out is recorded, with delivery status.")}
</div></div></section>
{cta_band("Add and only pay for the modules you use.", "Join the Gateway pilot, get early access to Persona, or tell us what you'd like built.", f'<a class="inline-flex items-center justify-center font-body-sm font-medium text-white hover:bg-white/10 border border-white/30 px-8 py-3.5 rounded-full transition-all" href="{CONSOLE}/login"><span>Log in to the console</span></a>')}
''')
write(ROOT / "index.html", "Elements | Aultrum", "Elements: Gateway and Peak, the care modules that run on their own or inside Flowstate and Pleasant, managed from one console.", "", overview)


# ---------------------------------------------------------------- Book a demo
demo = main_wrap(f'''<section class="w-full pt-10 pb-16 md:pt-16 md:pb-24 {W} grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-start">
<div class="lg:col-span-5 flex flex-col items-start gap-space-md min-w-0">{eyebrow("BOOK A DEMO")}<h1 class="{H1}">See Elements at work.</h1><p class="font-body-lg text-body-lg text-on-surface-variant">Pick a time that suits you. We'll confirm straight away and send a calendar invite.</p>
<div class="w-full mt-4">{eyebrow("WHAT WE'LL COVER")}{check_list(["Gateway answering a call and handing it to your team", "Peak turning clock-ins and praise into points", "Switching Elements on in Flowstate, Pleasant or your own system", "Persona working with your systems' tools", "A custom module for the workflow you wish you had"])}</div>
<p class="font-body-sm text-body-sm text-ink-muted mt-2">Prefer email? <a class="text-ink-primary font-medium hover:underline" href="mailto:{CONTACT}?subject=Aultrum%20Elements">{CONTACT}</a></p></div>
<div class="lg:col-span-7 min-w-0 bg-surface-container-lowest border border-border-editorial rounded-xl p-2 sm:p-4 shadow-sm"><div id="cal-elements-demo" style="width:100%;min-height:680px;overflow:auto"></div></div>
</section>''')
demo_js = '''<script>
  (function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if (typeof namespace === "string") { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ["initNamespace", namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
  Cal("init", "elementsdemo", { origin: "https://app.cal.com" });
  const email = new URLSearchParams(location.search).get("email") || undefined;
  Cal.ns.elementsdemo("inline", {
    elementOrSelector: "#cal-elements-demo",
    config: { layout: "month_view", useSlotsViewOnSmallScreen: "true", ...(email ? { email } : {}) },
    calLink: "addyadeyeri/flowstatedemo",
  });
  Cal.ns.elementsdemo("ui", { hideEventTypeDetails: false, layout: "month_view" });
</script>'''
write(ROOT / "book-a-demo" / "index.html", "Book a demo · Elements | Aultrum", "Book a demo of Aultrum Elements: Gateway, Peak, Persona and custom builds.", "", demo, demo_js)


# ---------------------------------------------------------------- /canvas/ moved here
for old, new in [("canvas/index.html", "/elements/"), ("canvas/book-a-demo/index.html", "/elements/book-a-demo/")]:
    p = SITE / "public" / old
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved to Elements</title><link rel="canonical" href="https://aultrum.co.uk{new}"><meta http-equiv="refresh" content="0; url={new}"></head><body><p>Canvas is now <a href="{new}">Elements</a>.</p></body></html>\n', encoding="utf-8")
    print("wrote", p)
