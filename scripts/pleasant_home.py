"""Writes aultrum.co.uk/pleasant/ in the homepage's layout, in Pleasant purple.

The header and footer are taken from the homepage (index.html) so they stay in
step. CSS: npm run build:pleasant-home-css (tailwind.pleasant-home.config.cjs).
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
OUT = SITE / "public" / "pleasant" / "index.html"
APP = "https://pleasant.aultrum.co.uk"
DEMO = "/pleasant/book-a-demo/"

home = (SITE / "index.html").read_text(encoding="utf-8")
head = home[: home.index("<header")]
header = home[home.index("<header") : home.index("</header>") + 9]
footer = home[home.index("<footer") : home.index("</footer>") + 9]

head = head.replace("<title>Aultrum | Competent, compliant and consistent care</title>", "<title>Pleasant · The operating system for care staffing agencies | Aultrum</title>")
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Pleasant runs rota, compliance, timesheets, payroll and client invoicing for care staffing agencies, with Persona and Elements built in.">\n<meta property="og:image" content="https://aultrum.co.uk/pleasant/img/oversight.jpg">', head)
head = head.replace('<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n', "")
head = head.replace('href="/assets/home.css"', 'href="/pleasant/assets/pleasant-home.css"')

# Header: AULTRUM / PLEASANT, Pleasant's own menu, log in to the app
header = header.replace('<span class="text-outline-variant font-body-sm">/</span>', '<span class="text-outline-variant font-body-sm">/</span><span class="text-ink-dark">PLEASANT</span>', 1)
nav = re.search(r'<nav class="hidden lg:flex[^"]*"[^>]*>.*?</nav>', header, re.S).group(0)
link = 'font-body-sm text-body-sm text-on-surface-variant hover:text-ink-primary transition-colors'
new_nav = re.sub(r">.*</nav>", ">" + "".join(f'<a class="{link}" href="{h}">{t}</a>' for t, h in [("Product", "#product"), ("Persona", "#assist"), ("Elements", "#elements"), ("Pricing", "/pleasant/pricing/"), ("Changelog", "/pleasant/changelog/")]) + "</nav>", nav, flags=re.S)
header = header.replace(nav, new_nav)
header = header.replace('data-path="login" href="https://workspace.aultrum.co.uk"', f'data-path="login" href="{APP}/login"')

W = "max-w-[1320px] mx-auto px-margin md:px-margin-md lg:px-margin-lg"
BAND, CTA, DEEP = "#4c1d95", "#5b21b6", "#2e1065"
PILL_TEXT, DOT, SOFT = "#ddd6fe", "#a78bfa", "#e9d5ff"
ARROW = '<span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span>'
GRID = '<div class="absolute inset-0 z-0 overflow-hidden pointer-events-none"><div class="absolute inset-0 opacity-15" style="background-image: linear-gradient(to right, #ffffff 1px, transparent 1px), linear-gradient(to bottom, #ffffff 1px, transparent 1px); background-size: 32px 32px;"></div></div>'


def eyebrow(t):
    return f'<div class="font-label-mono text-label-mono text-ink-primary uppercase tracking-wider mb-2">{t}</div>'


def chip(t):
    return f'<span class="px-2.5 py-1 bg-surface rounded-full text-ink-secondary font-label-mono text-label-mono border border-border-editorial">{t}</span>'


def pill(t):
    return f'<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-[{PILL_TEXT}] font-label-mono text-label-mono uppercase tracking-wider mb-3"><span class="w-1.5 h-1.5 rounded-full bg-[{DOT}] animate-pulse"></span>{t}</div>'


def frame(src, alt, w=2880, h=1800):
    return f'<figure class="min-w-0 bg-surface-container-low border border-border-editorial rounded-xl p-2 shadow-sm"><img class="w-full h-auto rounded-lg border border-border-editorial" src="/pleasant/img/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></figure>'


def check_list(items):
    return '<ul class="w-full">' + "".join(f'<li class="flex gap-3 py-3 border-t border-border-editorial"><span class="material-symbols-outlined text-[18px] text-ink-primary shrink-0" aria-hidden="true">check</span><span class="font-body-md text-ink-dark">{i}</span></li>' for i in items) + "</ul>"


def feature(id, label, title, body, items, image, flip=False):
    text = f'<div class="lg:col-span-5 flex flex-col items-start gap-4 min-w-0">{eyebrow(label)}<h2 class="font-headline-lg text-headline-md md:text-headline-lg text-ink-dark tracking-tight">{title}</h2><p class="font-body-lg text-body-lg text-ink-muted">{body}</p>{check_list(items)}</div>'
    pic = f'<div class="lg:col-span-7 min-w-0 {"lg:order-first" if flip else ""}">{image}</div>'
    return f'<section id="{id}" class="w-full scroll-mt-20 border-t border-border-editorial"><div class="{W} py-16 md:py-24 grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-center">{text}{pic}</div></section>'


def step(n, title, text):
    return f'<div class="bg-white/10 backdrop-blur-md border border-white/20 p-8 rounded-xl flex flex-col shadow-sm"><div class="font-stat-number text-stat-number text-white tracking-tight">{n}</div><div class="font-headline-sm text-headline-sm text-[{SOFT}] mt-2 uppercase">{title}</div><p class="font-body-sm text-white/75 mt-6">{text}</p></div>'


def element(id, icon, label, name, text, chips):
    return f'''<div class="group relative bg-surface-container-low rounded-xl p-8 flex flex-col justify-between transition-all hover:bg-surface-container shadow-sm border border-border-editorial">
<div><div class="flex items-center justify-between mb-6"><div class="flex items-center gap-3"><span class="w-10 h-10 rounded-full bg-ink-primary text-on-primary flex items-center justify-center shrink-0"><span class="material-symbols-outlined text-[20px]" aria-hidden="true">{icon}</span></span><div><h3 class="font-headline-md text-headline-sm md:text-headline-md text-ink-dark">{name}</h3></div></div><span class="px-2.5 py-1 rounded-full bg-ink-primary/10 text-ink-primary font-label-mono text-[10px] tracking-wider font-medium uppercase">SWITCH ON</span></div>
<p class="font-body-md text-ink-muted mb-6">{text}</p><div class="flex flex-wrap gap-2 mb-8">{"".join(chip(c) for c in chips)}</div></div>
<div class="pt-6 border-t border-border-editorial flex items-center justify-between"><a class="inline-flex items-center gap-2 font-body-sm font-medium text-ink-primary group-hover:translate-x-1 transition-transform" href="/elements/#{id}"><span>EXPLORE {name.upper()}</span>{ARROW}</a></div>
</div>'''


def cell(icon, label, title, text):
    lab = f'<span class="font-label-mono text-label-mono text-ink-primary uppercase tracking-wider">{label}</span>' if label else ""
    return f'<div class="bg-surface-container-lowest p-6 md:p-8 flex flex-col gap-3"><span class="material-symbols-outlined text-[22px] text-ink-primary" aria-hidden="true">{icon}</span>{lab}<h3 class="font-headline-sm text-headline-sm text-ink-dark">{title}</h3><p class="font-body-md text-ink-muted">{text}</p></div>'


SEGMENTS = ["Care homes", "Nursing homes", "Domiciliary care", "Supported living", "NHS &amp; local authority frameworks"]
LOOP = [
    ("01", "Request", "A care home or provider asks for cover, by phone or through their Pleasant Link."),
    ("02", "Match", "Pleasant suggests carers who are free, cleared to work and right for the role."),
    ("03", "Clock in", "Carers clock in and out on their phone against the real shift."),
    ("04", "Sign off", "The client's named signatory approves the hours. No sign-off, no invoice."),
    ("05", "Pay", "PAYE, NI and pension calculated from approved hours, with RTI and BACS files ready."),
    ("06", "Invoice", "The client invoice comes from the same hours, with your margin on every shift."),
]

body = f'''<main class="w-full pt-16 bg-surface"><div class="flex flex-col w-full text-on-surface">
<!-- Hero -->
<section id="product" class="w-full scroll-mt-20 pt-10 pb-16 md:pt-16 md:pb-24 {W}">
<div class="max-w-4xl flex flex-col items-start gap-space-md mb-12">
<a class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-surface-container-highest text-ink-primary font-label-mono text-label-mono tracking-wider uppercase hover:bg-surface-container-high transition-colors" href="/pleasant/changelog/"><span class="w-1.5 h-1.5 rounded-full bg-ink-primary animate-pulse"></span>New: Persona Assist and the Needs attention centre</a>
<h1 class="font-display-hero text-headline-lg md:text-display-hero text-ink-primary tracking-tight">The operating system for care staffing agencies.</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mt-1">Pleasant runs the whole loop for agencies supplying care homes, nursing homes and domiciliary providers. Rota, compliance, timesheets, payroll and client invoicing in one place, with Persona, the AI that works alongside your team.</p>
<div class="w-full max-w-xl mt-4 flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
<form class="flex-1 flex items-center bg-surface-container-lowest rounded-full p-1.5 shadow-sm focus-within:ring-2 focus-within:ring-ink-primary min-w-0" action="{DEMO}" method="get">
<label class="sr-only" for="work-email">Work email</label>
<input class="w-full min-w-0 bg-transparent px-4 py-2 font-body-md text-ink-dark placeholder:text-ink-muted focus:outline-none" id="work-email" name="email" placeholder="Enter your work email..." required type="email">
<button class="inline-flex items-center justify-center gap-1.5 bg-ink-primary text-on-primary font-body-sm px-5 py-2.5 rounded-full hover:bg-primary-container transition-all shrink-0 cursor-pointer" type="submit"><span>Book a demo</span><span class="material-symbols-outlined text-[16px]" aria-hidden="true">arrow_forward</span></button>
</form>
<a class="inline-flex items-center justify-center font-body-sm text-ink-primary hover:text-ink-dark px-4 py-3 rounded-full transition-colors font-medium text-center" href="/pleasant/pricing/">See pricing</a>
</div>
</div>
<div class="w-full bg-surface-container-low/70 border border-border-editorial rounded-xl p-6 mb-12 shadow-sm flex flex-col gap-4">
<div class="flex items-center gap-2 border-b border-border-editorial pb-3"><span class="w-1.5 h-1.5 rounded-full bg-ink-primary"></span><span class="font-label-mono text-label-mono text-ink-muted uppercase tracking-wider text-xs">BUILT FOR AGENCIES SUPPLYING</span></div>
<ul class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-x-6 gap-y-3 py-2">{"".join(f'<li class="font-body-md text-ink-dark">{s}</li>' for s in SEGMENTS)}</ul>
</div>
{frame("oversight.jpg", "Pleasant's Oversight dashboard, showing the Needs attention list and today's numbers")}
</section>
<!-- One closed loop -->
<section class="w-full relative overflow-hidden bg-[{BAND}]">{GRID}<div class="relative z-10 {W} pt-16 md:pt-24 pb-16 md:pb-24">
<div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6"><div class="max-w-2xl">{pill("ONE CLOSED LOOP")}<h2 class="font-headline-lg text-headline-md md:text-headline-lg text-white tracking-tight">From a shift request to a paid invoice, without re-keying anything.</h2></div><p class="font-body-md text-white/80 max-w-md">Most agencies stitch together a rota tool, a timesheet app, payroll software and a spreadsheet of invoices. Pleasant is one record from start to finish, so your margin is visible the moment a carer clocks in.</p></div>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">{"".join(step(*s) for s in LOOP)}</div>
</div></section>
{feature("oversight", "OVERSIGHT", "Know what needs you before the phone rings.", "Oversight opens on the problems, most urgent first, each with the button that fixes it.", ["Shifts starting in the next 48 hours with no carer, and unattended shifts", "Carers who aren't cleared to work: missing or expired DBS or right to work", "Clients missing a rate card or a timesheet signatory", "Timesheets to approve, and overdue invoices for admins", "Cover for the next 7 days, compared with the last 7"], '<div class="max-w-[300px] mx-auto">' + frame("mobile.jpg", "The Needs attention list on a phone", 780, 1688) + "</div>", flip=True)}
{feature("clients", "CLIENTPOINTE", "Clients are organisations, not names on a list.", "Every care home and provider has its units or branches, its contacts and its own rate card, so every shift is priced and signed off correctly.", ["Rate cards by role: day, night, weekend, bank holiday and a flat sleep-in charge", "Rates for the whole client or for one unit", "Named signatories approve timesheets through a 24-hour Pleasant Link", "Framework or PO references and payment terms on every invoice"], frame("client.jpg", "A client in Pleasant with its rate card, Pleasant Link and contacts"))}
{feature("payroll", "PAYROLL AND BILLING", "Pay carers and bill clients from the same approved hours.", "Payroll and invoices come from one set of approved, client-signed timesheets, so they always agree.", ["UK PAYE, National Insurance and pension for every carer, with payslips", "FPS-ready RTI file for HMRC, plus BACS STD18 and bank payment files", "Client invoices with sleep-ins shown as flat charges, not hours", "Xero sales-invoice export for your accounts"], frame("payroll.jpg", "A Pleasant payroll run with PAYE, NI, pension and payment files"), flip=True)}
{feature("assist", "PERSONA ASSIST", "Assist does the work. You approve it.", "Ask in plain English: fill tomorrow's open shifts, chase unsigned timesheets, set up a new care home. Assist finds the answer in your live data and prepares the change. Nothing happens until someone approves it.", ["Every change waits on an Approve or Decline card, and is written to the audit log", "Works within each person's role. Admins choose which areas Assist can read or change", "Scheduled automations such as a morning briefing or a compliance watch, which can only read", "Saved, searchable chat history, private to each user"], frame("assist.jpg", "Persona Assist preparing a shift assignment and waiting for approval"))}
<!-- Elements inside Pleasant -->
<section id="elements" class="w-full scroll-mt-20 border-t border-border-editorial"><div class="{W} py-16 md:py-24">
<div class="max-w-2xl mb-12">{eyebrow("ELEMENTS")}<h2 class="font-headline-lg text-headline-md md:text-headline-lg text-ink-dark tracking-tight">Add the modules you need, inside Pleasant.</h2><p class="font-body-lg text-ink-muted mt-3">Gateway and Peak are Aultrum Elements. Switch them on in Pleasant and they work on the same carers, clients and shifts.</p></div>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6">
{element("gateway", "call", "", "Gateway", "The always-on contact centre that logs every interaction straight into your CRM. Live calls, Abilities, and your people in the loop.", ["LIVE CALLS", "CRM LOGS", "ABILITIES", "PERSONNEL IN LOOP"])}
{element("peak", "workspace_premium", "", "Peak", "Recognition that pays. Points for shifts, punctuality, and praise — cashed out, spent on benefits, or unlocked as financial perks.", ["EARN POINTS", "CASH OUT", "PERKS", "FINANCIAL LEDGER"])}
</div></div></section>
<!-- First layers of quality care -->
<section class="w-full border-t border-border-editorial"><div class="{W} py-16 md:py-24">
<div class="max-w-2xl mb-12">{eyebrow("PERSONA")}<h2 class="font-headline-lg text-headline-md md:text-headline-lg text-ink-dark tracking-tight">Built on the first layers of quality care.</h2><p class="font-body-lg text-ink-muted mt-3">Persona maps every carer's abilities to every client's needs. Pleasant starts where care must start: is this carer capable, lawful and fit for this shift?</p></div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">
{cell("school", "LAYER I", "Competence", "Skills matched to this client's needs, not just credentials held. Anchored in the Care Certificate, the RQF, the Core Skills Training Framework and NICE guidance.")}
{cell("verified_user", "LAYER II", "Compliance", "A gate, not a trade-off. DBS, right to work and training are checked on every carer, and gaps surface before anyone is booked.")}
{cell("health_and_safety", "LAYER III", "Shift Readiness", "Protecting the carer's capacity to care is protecting the client. Pleasant already refuses overlapping bookings; fatigue-aware readiness is next.")}
</div>
<a class="inline-flex items-center gap-2 font-body-sm font-medium text-ink-primary hover:translate-x-1 transition-transform mt-8" href="/manifesto.html"><span>READ THE AULTRUM MANIFESTO</span>{ARROW}</a>
</div></section>
<!-- Security -->
<section class="w-full border-t border-border-editorial"><div class="{W} py-16 md:py-24">
<div class="max-w-2xl mb-12">{eyebrow("SECURITY")}<h2 class="font-headline-lg text-headline-md md:text-headline-lg text-ink-dark tracking-tight">Secure and accountable by design.</h2></div>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">
{cell("admin_panel_settings", "", "Roles and permissions", "Admins, managers and carers each see only what their role allows, enforced on the server.")}
{cell("history", "", "Full audit trail", "Sign-ins, approvals, payroll, invoices, exports and every change made through Assist are recorded.")}
{cell("shield_lock", "", "GDPR-aligned", "Worker and client data handled under UK GDPR rules and isolated per agency.")}
{cell("lock", "", "Session security", "Sign-in lockout, revocable sessions and “sign out of all devices”.")}
</div></div></section>
<!-- CTA -->
<section class="w-full relative overflow-hidden bg-[{CTA}] py-20 md:py-28 text-center flex flex-col items-center">{GRID}<div class="relative z-10 {W} flex flex-col items-center">{pill("DEPLOY_PLEASANT")}<h2 class="font-display-hero text-headline-lg md:text-display-hero text-white tracking-tight max-w-3xl">See Pleasant run your week.</h2><p class="font-body-lg text-white/80 max-w-xl mt-4 mb-8">A short demo with real workflows: a shift request, a clock-in, a signed timesheet, a payroll run and an invoice.</p><div class="flex flex-col sm:flex-row items-center gap-4"><a class="inline-flex items-center gap-2 bg-white text-ink-primary font-body-sm font-medium px-8 py-3.5 rounded-full hover:bg-white/90 transition-all shadow-md" href="{DEMO}"><span>Book a demo</span>{ARROW}</a><a class="inline-flex items-center justify-center font-body-sm font-medium text-white hover:bg-white/10 border border-white/30 px-8 py-3.5 rounded-full transition-all" href="/pleasant/pricing/"><span>From £149 a month</span></a></div></div></section>
</div></main>'''

OUT.write_text(head + header + body + footer + "\n</body>\n</html>\n", encoding="utf-8")
print("wrote", OUT)
