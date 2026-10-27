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

head = head.replace('<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n', "")
head = head.replace('href="/assets/home.css"', 'href="/pleasant/assets/pleasant-home.css"')
NAV = [("Product", "/pleasant/#product", "product"), ("Persona", "/pleasant/#assist", "persona"), ("Elements", "/pleasant/#elements", "elements"), ("Pricing", "/pleasant/pricing/", "pricing"), ("Changelog", "/pleasant/changelog/", "changelog")]


def page_head(title, description):
    h = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", head)
    return re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{description}">\n<meta property="og:image" content="https://aultrum.co.uk/pleasant/img/oversight.jpg">', h)


def page_header(active):
    """Homepage header with the Aultrum logo and Pleasant, Pleasant's menu and log in to the app."""
    lockup = '<span class="brand-logo h-5 sm:h-6" aria-hidden="true"></span><span class="w-px h-5 bg-border-editorial" aria-hidden="true"></span><span class="font-headline-sm text-[17px] sm:text-[19px] leading-none tracking-tight text-ink-dark">Pleasant</span>'
    h = header.replace('<span class="brand-logo h-5 sm:h-6" aria-hidden="true"></span>', lockup, 1).replace('aria-label="Aultrum home"', 'aria-label="Pleasant home"', 1)
    h = h.replace('data-path="ecosystem" href="/"', 'data-path="ecosystem" href="/pleasant/"', 1)
    nav = re.search(r'<nav class="hidden lg:flex[^"]*"[^>]*>.*?</nav>', h, re.S).group(0)
    def item(t, href, key):
        if key == active:
            return f'<a class="font-body-sm text-body-sm text-ink-primary" aria-current="page" href="{href}">{t}</a>'
        return f'<a class="font-body-sm text-body-sm text-on-surface-variant hover:text-ink-primary transition-colors" href="{href}">{t}</a>'
    h = h.replace(nav, re.sub(r">.*</nav>", ">" + "".join(item(*n) for n in NAV) + "</nav>", nav, flags=re.S))
    h = h.replace('href="https://workspace.aultrum.co.uk" aria-label="Aultrum Workspace"', f'href="{APP}/login" aria-label="Log in to Pleasant"')
    return h.replace('data-path="login" href="https://workspace.aultrum.co.uk"', f'data-path="login" href="{APP}/login"')


def write(path, title, description, active, main, extra=""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page_head(title, description) + page_header(active) + main + footer + extra + "\n</body>\n</html>\n", encoding="utf-8")
    print("wrote", path)


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

write(OUT, "Pleasant · The operating system for care staffing agencies | Aultrum", "Pleasant runs rota, compliance, timesheets, payroll and client invoicing for care staffing agencies, with Persona and Elements built in.", "product", body)


# ---------------------------------------------------------------- Shared pieces for the inner pages
CONTACT = "Wisdom@aultrum.co.uk"
H1 = "font-display-hero text-headline-lg md:text-display-hero text-ink-primary tracking-tight"
H2 = "font-headline-lg text-headline-md md:text-headline-lg text-ink-dark tracking-tight"
BTN = "inline-flex items-center justify-center gap-1.5 bg-ink-primary text-on-primary font-body-sm px-5 py-3 rounded-full hover:bg-primary-container transition-all"
BTN_LINE = "inline-flex items-center justify-center gap-1.5 border border-border-editorial bg-surface-container-lowest text-ink-dark font-body-sm px-5 py-3 rounded-full hover:border-ink-primary hover:text-ink-primary transition-all"


def hero(label, title, lead, extra=""):
    return f'''<section class="w-full pt-10 pb-12 md:pt-16 md:pb-16 {W}"><div class="max-w-4xl flex flex-col items-start gap-space-md">{eyebrow(label)}<h1 class="{H1}">{title}</h1><p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mt-1">{lead}</p>{extra}</div></section>'''


def cta_band(title, text):
    return f'''<section class="w-full relative overflow-hidden bg-[{CTA}] py-20 md:py-28 text-center flex flex-col items-center">{GRID}<div class="relative z-10 {W} flex flex-col items-center"><h2 class="font-display-hero text-headline-lg md:text-display-hero text-white tracking-tight max-w-3xl">{title}</h2><p class="font-body-lg text-white/80 max-w-xl mt-4 mb-8">{text}</p><div class="flex flex-col sm:flex-row items-center gap-4"><a class="inline-flex items-center gap-2 bg-white text-ink-primary font-body-sm font-medium px-8 py-3.5 rounded-full hover:bg-white/90 transition-all shadow-md" href="{DEMO}"><span>Book a demo</span>{ARROW}</a><a class="inline-flex items-center justify-center font-body-sm font-medium text-white hover:bg-white/10 border border-white/30 px-8 py-3.5 rounded-full transition-all" href="mailto:{CONTACT}?subject=Pleasant"><span>Contact Sales</span></a></div></div></section>'''


def main_wrap(inner):
    return f'<main class="w-full pt-16 bg-surface"><div class="flex flex-col w-full text-on-surface">{inner}</div></main>'


# ---------------------------------------------------------------- Pricing
PLANS = [
    ("Starter", "Scheduling and timesheets for a growing team.", 149, "£4 per active carer", False,
     ["Worker app: clock in and out, e-sign-off", "Shift scheduling and open-shift offers", "Timesheet approvals and audit trail", "Email support"]),
    ("Pro", "The full back office for a staffing agency.", 524, "40 active carers included, then £4 each", False,
     ["Everything in Starter", "Open-shift marketplace and matching", "UK payroll engine, PAYE and NI, payslips", "Client billing and margin on every placement", "Limited automations"]),
    ("Scale", "Advanced placements, automations and finance sync.", 1236, "150 active carers included, then £3 each", True,
     ["Everything in Pro", "Placement tracking and shift matching", "Expanded automations", "Xero / QuickBooks sync", "Priority support and dedicated CSM"]),
    ("Enterprise", "Multi-branch, HR suite and enterprise controls.", 2500, "Tailored to your agency", False,
     ["Everything in Scale", "HR suite: records, policies, onboarding", "Multi-branch and multi-agency", "Unlimited automations", "SLA, API, SSO, dedicated account team"]),
]
FAQ = [
    ("Who counts as an active carer?", "Only carers who worked a shift in the month. Carers on your books who didn't work aren't charged."),
    ("Does Pleasant file RTI with HMRC?", "Pleasant calculates PAYE, NI and pension to current HMRC thresholds and produces an FPS-ready RTI file for you or your accountant to submit. Direct submission is being piloted with early agencies, and final liability remains with the agency that files."),
    ("Is Persona Assist included?", "Yes. Assist is part of Pleasant. It works within each person's role, every change it prepares waits for approval, and admins choose which areas it can read or change."),
    ("Can I bring my existing data?", "Yes. Workers and clients can be imported from CSV files."),
]


def plan_card(name, tagline, monthly, seats, popular, features):
    enterprise = name == "Enterprise"
    border = "border-ink-primary ring-1 ring-ink-primary" if popular else "border-border-editorial"
    badge = '<span class="absolute -top-3 left-6 px-2.5 py-1 rounded-full bg-ink-primary text-on-primary font-label-mono text-[10px] tracking-wider uppercase">Most popular</span>' if popular else ""
    price = f'<span class="font-stat-number text-stat-number text-ink-dark" data-monthly="{monthly}">£{monthly:,}</span>' if not enterprise else f'<span class="font-stat-number text-stat-number text-ink-dark">£{monthly:,}</span><span class="font-body-sm text-ink-muted ml-1">from</span>'
    note = '<span data-billing-note>per month</span>' if not enterprise else "per month"
    href = f"mailto:{CONTACT}?subject=Pleasant%20Enterprise" if enterprise else DEMO
    label = "Contact us" if enterprise else "Book a demo"
    items = "".join(f'<li class="flex gap-2.5 py-2"><span class="material-symbols-outlined text-[18px] text-ink-primary shrink-0" aria-hidden="true">check</span><span class="font-body-sm text-body-sm text-ink-dark">{f}</span></li>' for f in features)
    return f'''<div class="relative flex flex-col bg-surface-container-low rounded-xl p-6 md:p-8 border {border} shadow-sm min-w-0">{badge}
<h3 class="font-headline-md text-headline-sm md:text-headline-md text-ink-dark">{name}</h3><p class="font-body-sm text-body-sm text-ink-muted mt-1 min-h-[36px]">{tagline}</p>
<p class="mt-6">{price}</p><p class="font-body-sm text-body-sm text-ink-muted">{note}</p><p class="font-label-mono text-label-mono text-ink-secondary mt-1">{seats}</p>
<a class="{BTN if popular else BTN_LINE} mt-6" href="{href}">{label}</a>
<ul class="mt-6 pt-4 border-t border-border-editorial">{items}</ul></div>'''


toggle = '''<div class="mt-6 inline-flex rounded-full border border-border-editorial bg-surface-container-lowest p-1 font-body-sm text-body-sm" role="group" aria-label="Billing period"><button type="button" data-billing="monthly" aria-pressed="true" class="rounded-full px-4 py-1.5 transition-colors">Monthly</button><button type="button" data-billing="annual" aria-pressed="false" class="rounded-full px-4 py-1.5 transition-colors">Annual <span class="text-ink-primary">−17%</span></button></div>'''
compare = "".join(f'<div class="flex justify-between gap-4 py-3.5 border-b border-white/15"><span class="text-white/85">{t}</span><span class="text-white/70 shrink-0">{c}</span></div>' for t, c in [("Roster and scheduling", "≈ £150/mo"), ("Time and attendance, timesheets", "≈ £100/mo"), ("UK payroll run", "≈ £200/mo"), ("Client invoicing", "≈ £100/mo")])
addons = "".join(cell(i, "", t, b) for i, t, b in [
    ("group_add", "Extra active carers", "£4 per extra carer a month on Pro, £3 on Scale. Only carers who worked count."),
    ("workspace_premium", "Peak", "Rewards engine from £49 a month. Points for clock-ins, praise and streaks, fed from Pleasant."),
    ("call", "Gateway", "AI contact centre. Takes the call and books cover straight into your rota."),
])
faq = "".join(f'''<details class="group border-t border-border-editorial py-5"><summary class="flex items-center justify-between gap-4 cursor-pointer list-none font-headline-sm text-headline-sm text-ink-dark">{q}<span class="material-symbols-outlined text-[20px] text-ink-primary transition-transform group-open:rotate-45" aria-hidden="true">add</span></summary><p class="font-body-md text-ink-muted mt-3 max-w-3xl">{a}</p></details>''' for q, a in FAQ)

pricing_main = main_wrap(
    hero("PRICING", "Simple pricing that scales with your agency.", "One platform replacing roster, timesheet, payroll and invoicing tools, priced per active carer, so you only pay for carers who actually worked.", toggle)
    + f'''<section class="w-full pb-16 md:pb-24 {W}"><div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">{"".join(plan_card(*p) for p in PLANS)}</div><p class="font-body-sm text-body-sm text-ink-muted mt-6">Prices exclude VAT.</p></section>
<section class="w-full relative overflow-hidden bg-[{BAND}]">{GRID}<div class="relative z-10 {W} py-16 md:py-24 grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-start">
<div>{pill("THE COST OF A TOOL STACK")}<h2 class="font-headline-lg text-headline-md md:text-headline-lg text-white tracking-tight">What it costs to piece it together.</h2><p class="font-body-md text-white/80 mt-4 max-w-md">Agencies running four separate tools pay for four sales teams, four logins and four sets of reconciliation.</p></div>
<div class="bg-white/10 backdrop-blur-md border border-white/20 rounded-xl px-6 py-2 font-body-md">{compare}<div class="flex justify-between gap-4 py-3.5 border-b border-white/15 text-white"><span>Typical 3–4 tool stack</span><span class="shrink-0">≈ £550–£900/mo</span></div><div class="flex justify-between gap-4 py-3.5 text-[{SOFT}] font-medium"><span>Pleasant: matching, payroll and billing</span><span class="shrink-0">from £524/mo</span></div></div>
</div></section>
<section class="w-full {W} py-16 md:py-24"><div class="max-w-2xl mb-12">{eyebrow("ADD-ONS")}<h2 class="{H2}">Add-ons from the Aultrum family.</h2></div><div class="grid grid-cols-1 md:grid-cols-3 gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">{addons}</div></section>
<section class="w-full border-t border-border-editorial"><div class="{W} py-16 md:py-24 grid grid-cols-1 lg:grid-cols-12 gap-10"><div class="lg:col-span-4">{eyebrow("QUESTIONS")}<h2 class="{H2}">Questions, answered.</h2><a class="inline-flex items-center gap-2 font-body-sm font-medium text-ink-primary mt-6 hover:translate-x-1 transition-transform" href="mailto:{CONTACT}?subject=Pleasant%20pricing"><span>ASK ABOUT PRICING</span>{ARROW}</a></div><div class="lg:col-span-8 border-b border-border-editorial">{faq}</div></div></section>'''
    + cta_band("See Pleasant run your week.", "A short demo with real workflows: a shift request, a clock-in, a signed timesheet, a payroll run and an invoice.")
)
pricing_js = '''<script>(()=>{const btns=[...document.querySelectorAll("[data-billing]")];const set=m=>{for(const b of btns){const on=b.dataset.billing===m;b.setAttribute("aria-pressed",String(on));b.classList.toggle("bg-ink-primary",on);b.classList.toggle("text-on-primary",on);b.classList.toggle("text-ink-muted",!on);}
for(const el of document.querySelectorAll("[data-monthly]")){const v=Number(el.dataset.monthly);el.textContent="£"+(m==="annual"?Math.round(v*0.83):v).toLocaleString("en-GB");}
for(const el of document.querySelectorAll("[data-billing-note]"))el.textContent=m==="annual"?"per month, billed annually":"per month";};
btns.forEach(b=>b.addEventListener("click",()=>set(b.dataset.billing)));set("monthly");})();</script>'''
write(SITE / "public" / "pleasant" / "pricing" / "index.html", "Pricing · Pleasant | Aultrum", "Simple pricing for UK care staffing agencies. One platform for rota, timesheets, payroll and client invoicing, priced per active carer.", "pricing", pricing_main, pricing_js)


# ---------------------------------------------------------------- Book a demo
demo_main = main_wrap(f'''<section class="w-full pt-10 pb-16 md:pt-16 md:pb-24 {W} grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-start">
<div class="lg:col-span-5 flex flex-col items-start gap-space-md min-w-0">{eyebrow("BOOK A DEMO")}<h1 class="{H1}">See Pleasant run your week.</h1><p class="font-body-lg text-body-lg text-on-surface-variant">Pick a time that suits you. We'll confirm straight away and send a calendar invite.</p>
<div class="w-full mt-4">{eyebrow("WHAT WE'LL COVER")}{check_list(["A care home's shift request, matched to a carer who is cleared to work", "Clock-in, client sign-off through a Pleasant Link, and approval", "A payroll run and the client invoice from the same hours", "Persona Assist preparing work for you to approve", "Moving your workers and clients across"])}</div>
<p class="font-body-sm text-body-sm text-ink-muted mt-2">Prefer email? <a class="text-ink-primary font-medium hover:underline" href="mailto:{CONTACT}?subject=Pleasant%20demo">{CONTACT}</a></p></div>
<div class="lg:col-span-7 min-w-0 bg-surface-container-lowest border border-border-editorial rounded-xl p-2 sm:p-4 shadow-sm"><div id="cal-pleasant-demo" style="width:100%;min-height:680px;overflow:auto"></div></div>
</section>''')
demo_js = '''<script>
  (function (C, A, L) { let p = function (a, ar) { a.q.push(ar); }; let d = C.document; C.Cal = C.Cal || function () { let cal = C.Cal; let ar = arguments; if (!cal.loaded) { cal.ns = {}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; } if (ar[0] === L) { const api = function () { p(api, arguments); }; const namespace = ar[1]; api.q = api.q || []; if (typeof namespace === "string") { cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ["initNamespace", namespace]); } else p(cal, ar); return; } p(cal, ar); }; })(window, "https://app.cal.com/embed/embed.js", "init");
  Cal("init", "pleasantdemo", { origin: "https://app.cal.com" });
  const email = new URLSearchParams(location.search).get("email") || undefined;
  Cal.ns.pleasantdemo("inline", {
    elementOrSelector: "#cal-pleasant-demo",
    config: { layout: "month_view", useSlotsViewOnSmallScreen: "true", ...(email ? { email } : {}) },
    calLink: "addyadeyeri/flowstatedemo",
  });
  Cal.ns.pleasantdemo("ui", { hideEventTypeDetails: false, layout: "month_view" });
</script>'''
write(SITE / "public" / "pleasant" / "book-a-demo" / "index.html", "Book a demo · Pleasant | Aultrum", "Book a demo of Pleasant, the operating system for UK care staffing agencies.", "", demo_main, demo_js)


# ---------------------------------------------------------------- Changelog
TAG = {
    "New": "bg-ink-primary/10 text-ink-primary",
    "Improved": "bg-surface-container-highest text-ink-secondary",
    "Fixed": "bg-[#fdf1d8] text-[#8a5a00]",
}
RELEASES = [
    ("24 October 2026", "Persona, Assist and an action-driven Oversight", "oversight.jpg", [
        ("New", "Needs attention", "Oversight now opens on every blocker, most urgent first: uncovered shifts, carers who aren't cleared to work, clients missing a rate card or signatory, overdue invoices and timesheets to approve. Each has the button that fixes it, and client-signed timesheets can be approved right there."),
        ("New", "Persona and Assist", "Persona is Pleasant's AI suite. Assist answers questions from live data and prepares changes for you to approve. It has a full chat page with saved history, scheduled read-only automations such as a morning briefing, and an admin page to choose what Assist can read or change."),
        ("New", "Clients as organisations", "Clients are now care homes and providers, with units or branches, contacts, named timesheet signatories and per-role rate cards for day, night, weekend, bank holiday and sleep-ins."),
        ("New", "Roles, team and audit log", "Admin and Manager roles, team invites, an audit log with CSV export, sign-in lockout, revocable sessions and a ⌘K command palette."),
        ("Improved", "KPIs with context", "Shifts today vs last week, cover for the next 7 days, the oldest timesheet waiting, and carers who joined this week."),
        ("Improved", "Sidebar and account menu", "Collapse the sidebar to icons, show or hide each section, and find Settings, Import and Add-ons under your account name."),
        ("Improved", "Sleep-ins and rota pricing", "Clients can be charged a separate flat sleep-in rate, and recurring rota shifts are priced from the client's rate card for each date."),
        ("Fixed", "Xero export", "Invoices now export to Xero as sales invoices with the correct amounts, UK tax rates and dates, instead of bills."),
        ("Fixed", "Sleep-in invoice lines", "Sleep-ins show as a flat charge on invoices and lender packs, not as hours at an hourly rate."),
    ]),
    ("8 October 2026", "Overnight shifts and safer imports", None, [
        ("Fixed", "Overnight shifts", "Shifts that run past midnight are handled correctly."),
        ("Fixed", "Imports", "CSV imports run as a single transaction, so a bad row no longer leaves a half-finished import."),
    ]),
    ("3 October 2026", "Dispatch, rota, compliance and payroll files", None, [
        ("New", "Dispatch and recurring rota", "Offer open shifts to carers, handle shift requests, and generate weeks from recurring rota templates."),
        ("New", "Compliance", "DBS, right to work and training expiry tracked for every carer."),
        ("New", "Payroll and invoicing files", "BACS payment files, Xero export, CSV import and agency settings."),
    ]),
]


def release(date, title, image, items):
    rows = "".join(f'<li class="flex flex-col sm:flex-row gap-2 sm:gap-4 py-4 border-t border-border-editorial"><span class="inline-flex h-6 w-[92px] shrink-0 items-center justify-center rounded-full font-label-mono text-[11px] tracking-wider uppercase {TAG[tag]}">{tag}</span><div class="min-w-0"><h3 class="font-headline-sm text-headline-sm text-ink-dark">{name}</h3><p class="font-body-md text-ink-muted mt-1">{text}</p></div></li>' for tag, name, text in items)
    pic = f'<div class="mt-6">{frame(image, title)}</div>' if image else ""
    slug = date.lower().replace(" ", "-")
    return f'''<article id="{slug}" class="scroll-mt-24 grid grid-cols-1 md:grid-cols-[200px_minmax(0,1fr)] gap-4 md:gap-8 border-t border-border-editorial py-12">
<div class="md:sticky md:top-24 md:self-start"><time class="font-label-mono text-label-mono text-ink-muted uppercase tracking-wider">{date}</time></div>
<div class="min-w-0"><h2 class="{H2}">{title}</h2>{pic}<ul class="mt-6">{rows}</ul></div></article>'''


changelog_main = main_wrap(
    hero("CHANGELOG", "What's new in Pleasant.", "New features, improvements and fixes, as they ship.")
    + f'<section class="w-full {W} pb-16 md:pb-24">{"".join(release(*r) for r in RELEASES)}</section>'
    + cta_band("See Pleasant run your week.", "A short demo with real workflows: a shift request, a clock-in, a signed timesheet, a payroll run and an invoice.")
)
write(SITE / "public" / "pleasant" / "changelog" / "index.html", "Changelog · Pleasant | Aultrum", "What's new in Pleasant: new features, improvements and fixes.", "changelog", changelog_main)
