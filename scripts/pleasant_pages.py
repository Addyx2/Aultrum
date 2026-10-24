"""Writes the static Pleasant product pages into the Aultrum site (public/pleasant).

Each page shares one head, the Aultrum main menu, the floating Pleasant
sub-menu and the footer, so they stay identical across pages. Edit the copy
here, then run:

    python3 scripts/pleasant_pages.py && npm run build:pleasant-css
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public" / "pleasant"
APP = "https://pleasant.aultrum.co.uk"
CONTACT = "Wisdom@aultrum.co.uk"

ARROW = '<svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg class="mt-0.5 h-4 w-4 shrink-0 text-brand-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
EXTERNAL = '<svg class="h-3.5 w-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
MARK = '<span class="flex h-7 w-7 items-center justify-center rounded-full bg-gradient-to-b from-brand-500 to-brand-700 text-[13px] font-bold text-white">P</span>'


def head(title: str, description: str, path: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://aultrum.co.uk{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://aultrum.co.uk/pleasant/img/oversight.jpg">
<meta name="theme-color" content="#fbfcfc">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Space+Grotesk:wght@500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/pleasant/assets/pleasant.css">
<script defer src="/pleasant/assets/site.js"></script>
</head>
<body class="font-sans">
<a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[60] focus:rounded-lg focus:bg-white focus:px-3 focus:py-2 focus:text-sm focus:shadow">Skip to content</a>
"""


MAIN_LINKS = [
    ("/flowstatebeta/", "Flowstate"),
    ("/pleasant/", "Pleasant"),
    ("/canvas/", "Canvas"),
    ("/research/index.html", "Research"),
    ("/blog/", "Blog"),
    ("/manifesto.html", "Manifesto"),
]

SUB_LINKS = [
    ("/pleasant/pricing/", "Pricing", "pricing"),
    ("/pleasant/book-a-demo/", '<span class="sm:hidden">Demo</span><span class="hidden sm:inline">Book demo</span>', "demo"),
    ("/pleasant/changelog/", "Changelog", "changelog"),
]


def header(active: str) -> str:
    main = "\n".join(
        f'<a href="{href}" class="rounded-full px-3 py-1.5 text-sm font-medium transition {"text-ink" if label == "Pleasant" else "text-slate-500 hover:text-ink"}"'
        f'{" aria-current=\"page\"" if label == "Pleasant" else ""}>{label}</a>'
        for href, label in MAIN_LINKS
    )
    mobile = "\n".join(
        f'<a href="{href}" class="block rounded-lg px-3 py-2 text-base font-medium {"bg-brand-50 text-brand-800" if label == "Pleasant" else "text-slate-700"}">{label}</a>'
        for href, label in MAIN_LINKS
    )
    sub = "\n".join(
        f'<a href="{href}" class="subnav-link"{" aria-current=\"page\"" if key == active else ""}>{label}</a>'
        for href, label, key in SUB_LINKS
    )
    return f"""<header class="relative z-50 border-b border-slate-200/70 bg-white/80 backdrop-blur">
  <div class="mx-auto flex h-16 max-w-6xl items-center justify-between px-4 sm:px-6">
    <a href="/" class="font-display text-lg font-bold tracking-tight text-ink">Aultrum</a>
    <nav aria-label="Aultrum" class="hidden items-center gap-1 md:flex">
{main}
    </nav>
    <div class="flex items-center gap-2">
      <a href="/pleasant/book-a-demo/" class="hidden rounded-full bg-ink px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-800 sm:inline-flex">Book a demo</a>
      <button id="menu-button" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Menu" class="flex h-9 w-9 items-center justify-center rounded-full border border-slate-200 text-slate-700 md:hidden">
        <svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
  <nav id="mobile-menu" aria-label="Aultrum" class="hidden border-t border-slate-200 bg-white px-4 py-3 md:hidden">
{mobile}
  </nav>
</header>
<div class="subnav pt-3">
  <nav aria-label="Pleasant" class="subnav-pill">
    <a href="/pleasant/" class="subnav-brand" aria-label="Pleasant overview"{' aria-current="page"' if active == "home" else ""}>{MARK}<span class="hidden sm:inline">Pleasant</span></a>
{sub}
    <a href="{APP}/login" class="subnav-cta inline-flex items-center gap-1">Log in {EXTERNAL}</a>
  </nav>
</div>
"""


FOOTER = f"""<footer class="mt-24 border-t border-slate-200 bg-white">
  <div class="mx-auto grid max-w-6xl gap-10 px-4 py-14 sm:px-6 md:grid-cols-4">
    <div>
      <a href="/" class="font-display text-lg font-bold tracking-tight">Aultrum</a>
      <p class="mt-3 max-w-xs text-sm text-slate-500">Quality care is computable. Personalised care is protectable.</p>
    </div>
    <div>
      <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Pleasant</p>
      <ul class="mt-3 space-y-2 text-sm text-slate-600">
        <li><a class="hover:text-ink" href="/pleasant/">Overview</a></li>
        <li><a class="hover:text-ink" href="/pleasant/pricing/">Pricing</a></li>
        <li><a class="hover:text-ink" href="/pleasant/book-a-demo/">Book a demo</a></li>
        <li><a class="hover:text-ink" href="/pleasant/changelog/">Changelog</a></li>
        <li><a class="hover:text-ink" href="{APP}/login">Log in</a></li>
      </ul>
    </div>
    <div>
      <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Aultrum</p>
      <ul class="mt-3 space-y-2 text-sm text-slate-600">
        <li><a class="hover:text-ink" href="/manifesto.html">Manifesto</a></li>
        <li><a class="hover:text-ink" href="/research/index.html">Research</a></li>
        <li><a class="hover:text-ink" href="/canvas/">Canvas</a></li>
        <li><a class="hover:text-ink" href="/flowstatebeta/">Flowstate</a></li>
        <li><a class="hover:text-ink" href="/blog/">Blog</a></li>
      </ul>
    </div>
    <div>
      <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Company</p>
      <ul class="mt-3 space-y-2 text-sm text-slate-600">
        <li><a class="hover:text-ink" href="mailto:{CONTACT}">{CONTACT}</a></li>
        <li><a class="hover:text-ink" href="/privacy.html">Privacy</a></li>
      </ul>
    </div>
  </div>
  <div class="border-t border-slate-100">
    <p class="mx-auto max-w-6xl px-4 py-6 text-xs text-slate-400 sm:px-6">&copy; 2026 Aultrum Technologies Ltd. Pleasant is part of the Aultrum family.</p>
  </div>
</footer>
</body>
</html>
"""


def frame(src: str, alt: str, url: str, extra: str = "") -> str:
    return f"""<div class="frame shadow-frame {extra}">
  <div class="frame-bar"><span></span><span></span><span></span><p class="frame-url">{url}</p></div>
  <img src="/pleasant/img/{src}" alt="{alt}" width="2880" height="1800" loading="lazy">
</div>"""


def button(href: str, label: str, dark: bool = True) -> str:
    cls = (
        "bg-ink text-white hover:bg-slate-800"
        if dark
        else "border border-slate-300 bg-white text-ink hover:border-slate-400"
    )
    return f'<a href="{href}" class="inline-flex items-center gap-2 rounded-full px-5 py-3 text-sm font-semibold transition {cls}">{label} {ARROW}</a>'


def feature(eyebrow: str, title: str, body: str, bullets: list[str], image: str, flip: bool = False) -> str:
    items = "\n".join(f'<li class="flex gap-2.5">{CHECK}<span>{b}</span></li>' for b in bullets)
    text = f"""<div class="reveal">
  <p class="text-sm font-semibold text-brand-700">{eyebrow}</p>
  <h2 class="mt-3 font-display text-3xl font-bold tracking-tight text-ink sm:text-4xl">{title}</h2>
  <p class="mt-4 text-lg leading-relaxed text-slate-600">{body}</p>
  <ul class="mt-6 space-y-3 text-[15px] text-slate-700">
{items}
  </ul>
</div>"""
    pic = f'<div class="reveal">{image}</div>'
    order = (pic, text) if flip else (text, pic)
    return f"""<section class="mx-auto mt-28 grid max-w-6xl items-center gap-12 px-4 sm:px-6 lg:grid-cols-[0.9fr_1.1fr]{' lg:grid-cols-[1.1fr_0.9fr]' if flip else ''}">
{order[0]}
{order[1]}
</section>"""


# ---------------------------------------------------------------- Overview
LOOP = [
    ("Request", "A care home or provider asks for cover, by phone or through their Pleasant Link."),
    ("Match", "Pleasant suggests carers who are free, cleared to work and right for the role."),
    ("Clock in", "Carers clock in and out on their phone against the real shift."),
    ("Sign off", "The client's named signatory approves the hours. No sign-off, no invoice."),
    ("Pay", "PAYE, NI and pension calculated from approved hours, with RTI and BACS files ready."),
    ("Invoice", "The client invoice comes from the same hours, with your margin on every shift."),
]

overview = head(
    "Pleasant · The operating system for care staffing agencies | Aultrum",
    "Pleasant runs the whole loop for agencies supplying care homes, nursing homes and domiciliary providers: rota, compliance, timesheets, payroll and client invoicing, with Persona AI.",
    "/pleasant/",
) + header("home") + f"""<main id="main">
<section class="hero-glow relative -mt-16 overflow-hidden pt-28">
  <div class="grid-lines pointer-events-none absolute inset-0 [mask-image:radial-gradient(70%_60%_at_50%_0%,black,transparent)]"></div>
  <div class="relative mx-auto max-w-4xl px-4 text-center sm:px-6">
    <a href="/pleasant/changelog/" class="inline-flex items-center gap-2 rounded-full border border-brand-200 bg-white/80 px-3 py-1 text-xs font-medium text-brand-800 transition hover:border-brand-300">
      <span class="rounded-full bg-brand-600 px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide text-white">New</span>
      Persona Assist and the Needs attention centre are live {ARROW}
    </a>
    <h1 class="mt-7 font-display text-[44px] font-bold leading-[1.02] tracking-tight text-ink sm:text-6xl lg:text-7xl">
      The operating system for <span class="font-serif font-normal italic text-brand-700">care</span> staffing agencies.
    </h1>
    <p class="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-slate-600">
      Pleasant runs the whole loop for agencies supplying care homes, nursing homes and domiciliary providers. Rota, compliance, timesheets, payroll and client invoicing in one place, with Persona, the AI that works alongside your team.
    </p>
    <div class="mt-9 flex flex-wrap items-center justify-center gap-3">
      {button("/pleasant/book-a-demo/", "Book a demo")}
      {button("/pleasant/pricing/", "See pricing", dark=False)}
    </div>
    <p class="mt-4 text-xs text-slate-500">Pilot programme: founder pricing for our first agencies in Q4 2026.</p>
  </div>
  <div class="relative mx-auto mt-16 max-w-6xl px-4 sm:px-6">
    {frame("oversight.jpg", "Pleasant's Oversight dashboard, showing the Needs attention list and today's numbers", "pleasant.aultrum.co.uk/oversight", "reveal")}
  </div>
</section>

<section class="mx-auto mt-16 max-w-6xl px-4 sm:px-6">
  <p class="text-center text-xs font-semibold uppercase tracking-[0.2em] text-slate-400">Built for agencies supplying</p>
  <ul class="mt-5 flex flex-wrap items-center justify-center gap-x-10 gap-y-3 font-display text-lg font-semibold text-slate-400">
    <li>Care homes</li><li>Nursing homes</li><li>Domiciliary care</li><li>Supported living</li><li>NHS &amp; local authority frameworks</li>
  </ul>
</section>

<section class="mx-auto mt-28 max-w-6xl px-4 sm:px-6">
  <div class="reveal max-w-2xl">
    <p class="text-sm font-semibold text-brand-700">One closed loop</p>
    <h2 class="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">From a shift request to a paid invoice, without re-keying anything.</h2>
    <p class="mt-4 text-lg leading-relaxed text-slate-600">Most agencies stitch together a rota tool, a timesheet app, payroll software and a spreadsheet of invoices. Pleasant is one record from start to finish, so your margin is visible the moment a carer clocks in.</p>
  </div>
  <ol class="mt-12 grid gap-px overflow-hidden rounded-2xl border border-slate-200 bg-slate-200 sm:grid-cols-2 lg:grid-cols-3">
""" + "\n".join(
    f"""    <li class="reveal bg-white p-6">
      <p class="font-display text-sm font-semibold text-brand-600">0{i + 1}</p>
      <h3 class="mt-2 font-display text-xl font-semibold">{name}</h3>
      <p class="mt-2 text-[15px] leading-relaxed text-slate-600">{text}</p>
    </li>"""
    for i, (name, text) in enumerate(LOOP)
) + """
  </ol>
</section>
""" + feature(
    "Oversight",
    "Know what needs you before the phone rings.",
    "Oversight opens on the problems, most urgent first, each with the button that fixes it.",
    [
        "Shifts starting in the next 48 hours with no carer, and unattended shifts",
        "Carers who aren't cleared to work: missing or expired DBS or right to work",
        "Clients missing a rate card or a timesheet signatory",
        "Timesheets to approve, and overdue invoices for admins",
        "Cover for the next 7 days, compared with the last 7",
    ],
    f'<div class="mx-auto max-w-[300px]"><div class="overflow-hidden rounded-[2.2rem] border-[10px] border-ink bg-ink shadow-frame"><img src="/pleasant/img/mobile.jpg" alt="The Needs attention list on a phone" width="780" height="1688" loading="lazy" class="block w-full rounded-[1.5rem]"></div></div>',
    flip=True,
) + feature(
    "Clientpointe",
    "Clients are organisations, not names on a list.",
    "Every care home and provider has its units or branches, its contacts and its own rate card, so every shift is priced and signed off correctly.",
    [
        "Rate cards by role: day, night, weekend, bank holiday and a flat sleep-in charge",
        "Rates for the whole client or for one unit",
        "Named signatories approve timesheets through a 24-hour Pleasant Link",
        "Framework or PO references and payment terms on every invoice",
    ],
    frame("client.jpg", "A client in Pleasant with its rate card, Pleasant Link and contacts", "pleasant.aultrum.co.uk/clients"),
) + feature(
    "Payroll and billing",
    "Pay carers and bill clients from the same approved hours.",
    "Payroll and invoices come from one set of approved, client-signed timesheets, so they always agree.",
    [
        "UK PAYE, National Insurance and pension for every carer, with payslips",
        "FPS-ready RTI file for HMRC, plus BACS STD18 and bank payment files",
        "Client invoices with sleep-ins shown as flat charges, not hours",
        "Xero sales-invoice export for your accounts",
    ],
    frame("payroll.jpg", "A Pleasant payroll run with PAYE, NI, pension and payment files", "pleasant.aultrum.co.uk/payroll"),
    flip=True,
) + f"""
<section class="mt-28 bg-ink py-24 text-white">
  <div class="mx-auto grid max-w-6xl items-center gap-12 px-4 sm:px-6 lg:grid-cols-[0.9fr_1.1fr]">
    <div class="reveal">
      <p class="text-sm font-semibold text-brand-300">Persona Assist</p>
      <h2 class="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">Assist does the work. <span class="font-serif font-normal italic text-brand-300">You</span> approve it.</h2>
      <p class="mt-4 text-lg leading-relaxed text-slate-300">Ask in plain English: fill tomorrow's open shifts, chase unsigned timesheets, set up a new care home. Assist finds the answer in your live data and prepares the change. Nothing happens until someone approves it.</p>
      <ul class="mt-6 space-y-3 text-[15px] text-slate-200">
        <li class="flex gap-2.5">{CHECK.replace("text-brand-600", "text-brand-300")}<span>Every change waits on an Approve or Decline card, and is written to the audit log</span></li>
        <li class="flex gap-2.5">{CHECK.replace("text-brand-600", "text-brand-300")}<span>Works within each person's role. Admins choose which areas Assist can read or change</span></li>
        <li class="flex gap-2.5">{CHECK.replace("text-brand-600", "text-brand-300")}<span>Scheduled automations such as a morning briefing or a compliance watch, which can only read</span></li>
        <li class="flex gap-2.5">{CHECK.replace("text-brand-600", "text-brand-300")}<span>Saved, searchable chat history, private to each user</span></li>
      </ul>
    </div>
    <div class="reveal">{frame("assist.jpg", "Persona Assist preparing a shift assignment and waiting for approval", "pleasant.aultrum.co.uk/persona/assist")}</div>
  </div>
</section>

<section class="mx-auto mt-28 max-w-6xl px-4 sm:px-6">
  <div class="reveal max-w-2xl">
    <p class="text-sm font-semibold text-brand-700">Persona</p>
    <h2 class="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">Built on the first layers of quality care.</h2>
    <p class="mt-4 text-lg leading-relaxed text-slate-600">Persona maps every carer's abilities to every client's needs. Pleasant starts where care must start: is this carer capable, lawful and fit for this shift?</p>
  </div>
  <div class="mt-10 grid gap-4 md:grid-cols-3">
    <div class="reveal rounded-2xl border border-slate-200 bg-white p-6">
      <p class="font-display text-sm font-semibold text-slate-400">Layer I</p>
      <h3 class="mt-1 font-display text-xl font-semibold">Competence</h3>
      <p class="mt-2 text-[15px] leading-relaxed text-slate-600">Skills matched to this client's needs, not just credentials held. Anchored in the Care Certificate, the RQF, the Core Skills Training Framework and NICE guidance.</p>
    </div>
    <div class="reveal rounded-2xl border border-slate-200 bg-white p-6">
      <p class="font-display text-sm font-semibold text-slate-400">Layer II</p>
      <h3 class="mt-1 font-display text-xl font-semibold">Compliance</h3>
      <p class="mt-2 text-[15px] leading-relaxed text-slate-600">A gate, not a trade-off. DBS, right to work and training are checked on every carer, and gaps surface before anyone is booked.</p>
    </div>
    <div class="reveal rounded-2xl border border-slate-200 bg-white p-6">
      <p class="font-display text-sm font-semibold text-slate-400">Layer III</p>
      <h3 class="mt-1 font-display text-xl font-semibold">Shift Readiness</h3>
      <p class="mt-2 text-[15px] leading-relaxed text-slate-600">Protecting the carer's capacity to care is protecting the client. Pleasant already refuses overlapping bookings; fatigue-aware readiness is next.</p>
    </div>
  </div>
  <a href="/manifesto.html" class="mt-6 inline-flex items-center gap-1.5 text-sm font-semibold text-brand-700 hover:text-brand-800">Read the Aultrum manifesto {ARROW}</a>
</section>

<section class="mx-auto mt-28 max-w-6xl px-4 sm:px-6">
  <h2 class="reveal font-display text-3xl font-bold tracking-tight sm:text-4xl">Secure and accountable by design.</h2>
  <div class="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
""" + "\n".join(
    f"""    <div class="reveal rounded-2xl border border-slate-200 bg-white p-6">
      <h3 class="font-semibold">{t}</h3>
      <p class="mt-2 text-sm leading-relaxed text-slate-600">{b}</p>
    </div>"""
    for t, b in [
        ("Roles and permissions", "Admins, managers and carers each see only what their role allows, enforced on the server."),
        ("Full audit trail", "Sign-ins, approvals, payroll, invoices, exports and every change made through Assist are recorded."),
        ("GDPR-aligned", "Worker and client data handled under UK GDPR rules and isolated per agency."),
        ("Session security", "Sign-in lockout, revocable sessions and “sign out of all devices”."),
    ]
) + f"""
  </div>
</section>

<section class="mx-auto mt-28 max-w-6xl px-4 sm:px-6">
  <div class="reveal relative overflow-hidden rounded-3xl bg-gradient-to-br from-brand-700 to-brand-950 px-6 py-16 text-center text-white sm:px-12">
    <div class="grid-lines pointer-events-none absolute inset-0 opacity-20"></div>
    <h2 class="relative font-display text-3xl font-bold tracking-tight sm:text-5xl">See Pleasant run your week.</h2>
    <p class="relative mx-auto mt-4 max-w-xl text-lg text-brand-100">A short demo with real workflows: a shift request, a clock-in, a signed timesheet, a payroll run and an invoice.</p>
    <div class="relative mt-8 flex flex-wrap justify-center gap-3">
      <a href="/pleasant/book-a-demo/" class="inline-flex items-center gap-2 rounded-full bg-white px-5 py-3 text-sm font-semibold text-ink transition hover:bg-brand-50">Book a demo {ARROW}</a>
      <a href="/pleasant/pricing/" class="inline-flex items-center gap-2 rounded-full border border-white/30 px-5 py-3 text-sm font-semibold text-white transition hover:bg-white/10">From £149 a month</a>
    </div>
  </div>
</section>
</main>
""" + FOOTER

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


def plan_card(name, tagline, monthly, seats, popular, features):
    ring = "border-ink ring-1 ring-ink" if popular else "border-slate-200"
    badge = '<span class="absolute -top-3 left-6 rounded-full bg-ink px-2.5 py-1 text-[11px] font-semibold text-white">Most popular</span>' if popular else ""
    cta_href = f"mailto:{CONTACT}?subject=Pleasant%20Enterprise" if name == "Enterprise" else "/pleasant/book-a-demo/"
    cta_label = "Contact us" if name == "Enterprise" else "Book a demo"
    cta_cls = "bg-ink text-white hover:bg-slate-800" if popular else "border border-slate-300 text-ink hover:border-slate-400"
    items = "\n".join(f'<li class="flex gap-2.5">{CHECK}<span>{f}</span></li>' for f in features)
    price = (
        f'<span class="font-display text-4xl font-bold tracking-tight" data-monthly="{monthly}">£{monthly:,}</span>'
        if name != "Enterprise"
        else f'<span class="font-display text-4xl font-bold tracking-tight">From £{monthly:,}</span>'
    )
    note = '<span class="text-sm text-slate-500" data-billing-note>per month</span>' if name != "Enterprise" else '<span class="text-sm text-slate-500">per month</span>'
    return f"""<div class="reveal relative flex flex-col rounded-2xl border {ring} bg-white p-6">
  {badge}
  <h3 class="font-display text-xl font-semibold">{name}</h3>
  <p class="mt-1 min-h-[40px] text-sm text-slate-600">{tagline}</p>
  <p class="mt-5">{price}</p>
  <p>{note}</p>
  <p class="mt-1 text-xs text-slate-500">{seats}</p>
  <a href="{cta_href}" class="mt-6 inline-flex justify-center rounded-full px-4 py-2.5 text-sm font-semibold transition {cta_cls}">{cta_label}</a>
  <ul class="mt-6 space-y-2.5 text-sm text-slate-700">
{items}
  </ul>
</div>"""


FAQ = [
    ("Who counts as an active carer?", "Only carers who worked a shift in the month. Carers on your books who didn't work aren't charged."),
    ("What is the pilot programme?", "We're onboarding our first agencies in Q4 2026 at founder pricing, with hands-on setup and direct access to the team building Pleasant."),
    ("Does Pleasant file RTI with HMRC?", "Pleasant calculates PAYE, NI and pension to current HMRC thresholds and produces an FPS-ready RTI file for you or your accountant to submit. Direct submission is being piloted with early agencies, and final liability remains with the agency that files."),
    ("Is Persona Assist included?", "Yes. Assist is part of Pleasant. It works within each person's role, every change it prepares waits for approval, and admins choose which areas it can read or change."),
    ("Can I bring my existing data?", "Yes. Workers and clients can be imported from CSV files."),
]

pricing = head(
    "Pricing · Pleasant | Aultrum",
    "Simple pricing for UK care staffing agencies. One platform for rota, timesheets, payroll and client invoicing, priced per active carer.",
    "/pleasant/pricing/",
) + header("pricing") + f"""<main id="main">
<section class="hero-glow -mt-16 pt-28">
  <div class="mx-auto max-w-3xl px-4 text-center sm:px-6">
    <p class="text-sm font-semibold text-brand-700">Pricing</p>
    <h1 class="mt-3 font-display text-4xl font-bold tracking-tight sm:text-6xl">Simple pricing that scales <span class="font-serif font-normal italic text-brand-700">with</span> your agency.</h1>
    <p class="mt-5 text-lg text-slate-600">One platform replacing roster, timesheet, payroll and invoicing tools, priced per active carer, so you only pay for carers who actually worked.</p>
    <div class="mt-8 inline-flex rounded-full border border-slate-200 bg-white p-1 text-sm font-medium shadow-sm" role="group" aria-label="Billing period">
      <button type="button" data-billing="monthly" aria-pressed="true" class="rounded-full bg-ink px-4 py-1.5 text-white transition">Monthly</button>
      <button type="button" data-billing="annual" aria-pressed="false" class="rounded-full px-4 py-1.5 text-slate-600 transition">Annual <span class="text-brand-600">−17%</span></button>
    </div>
  </div>
</section>
<section class="mx-auto mt-12 grid max-w-6xl gap-5 px-4 sm:px-6 md:grid-cols-2 lg:grid-cols-4">
""" + "\n".join(plan_card(*p) for p in PLANS) + f"""
</section>
<p class="mx-auto mt-6 max-w-6xl px-4 text-center text-xs text-slate-500 sm:px-6">Prices exclude VAT. Pilot programme: founder pricing for our first agencies in Q4 2026.</p>

<section class="mx-auto mt-24 grid max-w-6xl gap-10 px-4 sm:px-6 lg:grid-cols-2">
  <div class="reveal">
    <h2 class="font-display text-3xl font-bold tracking-tight">What it costs to piece it together</h2>
    <p class="mt-3 text-slate-600">Agencies running four separate tools pay for four sales teams, four logins and four sets of reconciliation.</p>
    <div class="mt-6 overflow-hidden rounded-2xl border border-slate-200 bg-white text-sm">
""" + "\n".join(
    f'<div class="flex justify-between border-b border-slate-100 px-5 py-3.5"><span class="text-slate-700">{t}</span><span class="text-slate-500">{c}</span></div>'
    for t, c in [("Roster and scheduling", "≈ £150/mo"), ("Time and attendance, timesheets", "≈ £100/mo"), ("UK payroll run", "≈ £200/mo"), ("Client invoicing", "≈ £100/mo")]
) + f"""
      <div class="flex justify-between bg-slate-50 px-5 py-3.5 font-semibold"><span>Typical 3–4 tool stack</span><span>≈ £550–£900/mo</span></div>
      <div class="flex justify-between bg-brand-50 px-5 py-3.5 font-semibold text-brand-900"><span>Pleasant: matching, payroll and billing</span><span>from £524/mo</span></div>
    </div>
  </div>
  <div class="reveal">
    <h2 class="font-display text-3xl font-bold tracking-tight">Add-ons from the Aultrum family</h2>
    <div class="mt-6 space-y-4">
""" + "\n".join(
    f'<div class="rounded-2xl border border-slate-200 bg-white p-5"><h3 class="font-semibold">{t}</h3><p class="mt-1 text-sm text-slate-600">{b}</p></div>'
    for t, b in [
        ("Extra active carers", "£4 per extra carer a month on Pro, £3 on Scale. Only carers who worked count."),
        ("Peak", "Rewards engine from £49 a month. Points for clock-ins, praise and streaks, fed from Pleasant."),
        ("Gateway", "AI contact centre. Takes the call and books cover straight into your rota."),
    ]
) + f"""
    </div>
  </div>
</section>

<section class="mx-auto mt-24 max-w-3xl px-4 sm:px-6">
  <h2 class="font-display text-3xl font-bold tracking-tight">Questions</h2>
  <div class="mt-6 divide-y divide-slate-200 rounded-2xl border border-slate-200 bg-white">
""" + "\n".join(
    f"""    <details class="group px-5 py-4">
      <summary class="flex items-center justify-between gap-4 font-medium">{q}<span class="faq-chevron text-xl leading-none text-slate-400 transition-transform">+</span></summary>
      <p class="mt-3 text-[15px] leading-relaxed text-slate-600">{a}</p>
    </details>"""
    for q, a in FAQ
) + f"""
  </div>
  <div class="mt-10 flex flex-wrap justify-center gap-3">{button("/pleasant/book-a-demo/", "Book a demo")}{button(f"mailto:{CONTACT}?subject=Pleasant%20pricing", "Ask about pricing", dark=False)}</div>
</section>
</main>
""" + FOOTER

# ---------------------------------------------------------------- Book a demo
demo = head(
    "Book a demo · Pleasant | Aultrum",
    "Book a demo of Pleasant, the operating system for UK care staffing agencies.",
    "/pleasant/book-a-demo/",
) + header("demo") + f"""<main id="main">
<section class="hero-glow -mt-16 pt-28">
  <div class="mx-auto grid max-w-6xl gap-12 px-4 sm:px-6 lg:grid-cols-[0.8fr_1.2fr]">
    <div>
      <p class="text-sm font-semibold text-brand-700">Book a demo</p>
      <h1 class="mt-3 font-display text-4xl font-bold tracking-tight sm:text-5xl">See Pleasant run <span class="font-serif font-normal italic text-brand-700">your</span> week.</h1>
      <p class="mt-5 text-lg text-slate-600">Pick a time that suits you. We'll confirm straight away and send a calendar invite.</p>
      <h2 class="mt-10 text-sm font-semibold uppercase tracking-wider text-slate-400">What we'll cover</h2>
      <ul class="mt-4 space-y-3 text-[15px] text-slate-700">
        <li class="flex gap-2.5">{CHECK}<span>A care home's shift request, matched to a carer who is cleared to work</span></li>
        <li class="flex gap-2.5">{CHECK}<span>Clock-in, client sign-off through a Pleasant Link, and approval</span></li>
        <li class="flex gap-2.5">{CHECK}<span>A payroll run and the client invoice from the same hours</span></li>
        <li class="flex gap-2.5">{CHECK}<span>Persona Assist preparing work for you to approve</span></li>
        <li class="flex gap-2.5">{CHECK}<span>Moving your workers and clients across</span></li>
      </ul>
      <p class="mt-10 text-sm text-slate-500">Prefer email? <a href="mailto:{CONTACT}?subject=Pleasant%20demo" class="font-semibold text-brand-700 hover:text-brand-800">{CONTACT}</a></p>
    </div>
    <div class="rounded-3xl border border-slate-200 bg-white p-2 shadow-frame sm:p-4">
      <div id="cal-pleasant-demo" style="width:100%;min-height:680px;overflow:auto"></div>
    </div>
  </div>
</section>
</main>
<script>
  (function (C, A, L) {{ let p = function (a, ar) {{ a.q.push(ar); }}; let d = C.document; C.Cal = C.Cal || function () {{ let cal = C.Cal; let ar = arguments; if (!cal.loaded) {{ cal.ns = {{}}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; }} if (ar[0] === L) {{ const api = function () {{ p(api, arguments); }}; const namespace = ar[1]; api.q = api.q || []; if (typeof namespace === "string") {{ cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ["initNamespace", namespace]); }} else p(cal, ar); return; }} p(cal, ar); }}; }})(window, "https://app.cal.com/embed/embed.js", "init");
  Cal("init", "pleasantdemo", {{ origin: "https://app.cal.com" }});
  Cal.ns.pleasantdemo("inline", {{
    elementOrSelector: "#cal-pleasant-demo",
    config: {{ layout: "month_view", useSlotsViewOnSmallScreen: "true" }},
    calLink: "addyadeyeri/flowstatedemo",
  }});
  Cal.ns.pleasantdemo("ui", {{ hideEventTypeDetails: false, layout: "month_view" }});
</script>
""" + FOOTER

# ---------------------------------------------------------------- Changelog
TAG = {
    "New": "bg-brand-50 text-brand-800 ring-brand-600/20",
    "Improved": "bg-blue-50 text-blue-800 ring-blue-600/20",
    "Fixed": "bg-amber-50 text-amber-800 ring-amber-600/20",
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
    rows = "\n".join(
        f"""      <li class="flex flex-col gap-1.5 sm:flex-row sm:gap-4">
        <span class="inline-flex h-6 w-fit shrink-0 items-center rounded-full px-2.5 text-xs font-semibold ring-1 ring-inset {TAG[tag]}">{tag}</span>
        <div><h3 class="font-semibold">{name}</h3><p class="mt-1 text-[15px] leading-relaxed text-slate-600">{text}</p></div>
      </li>"""
        for tag, name, text in items
    )
    pic = f'<div class="mt-6">{frame(image, title, "pleasant.aultrum.co.uk")}</div>' if image else ""
    slug = date.lower().replace(" ", "-")
    return f"""<article id="{slug}" class="reveal grid gap-6 border-t border-slate-200 py-12 md:grid-cols-[200px_1fr]">
  <div class="md:sticky md:top-24 md:self-start"><time class="text-sm font-medium text-slate-500">{date}</time></div>
  <div>
    <h2 class="font-display text-2xl font-bold tracking-tight">{title}</h2>
    {pic}
    <ul class="mt-6 space-y-5">
{rows}
    </ul>
  </div>
</article>"""


changelog = head(
    "Changelog · Pleasant | Aultrum",
    "What's new in Pleasant: new features, improvements and fixes.",
    "/pleasant/changelog/",
) + header("changelog") + f"""<main id="main">
<section class="hero-glow -mt-16 pt-28">
  <div class="mx-auto max-w-4xl px-4 sm:px-6">
    <p class="text-sm font-semibold text-brand-700">Changelog</p>
    <h1 class="mt-3 font-display text-4xl font-bold tracking-tight sm:text-6xl">What's new in Pleasant.</h1>
    <p class="mt-5 max-w-2xl text-lg text-slate-600">New features, improvements and fixes, as they ship.</p>
  </div>
</section>
<section class="mx-auto mt-12 max-w-4xl px-4 sm:px-6">
""" + "\n".join(release(*r) for r in RELEASES) + """
</section>
</main>
""" + FOOTER

PAGES = {
    ROOT / "index.html": overview,
    ROOT / "pricing" / "index.html": pricing,
    ROOT / "book-a-demo" / "index.html": demo,
    ROOT / "changelog" / "index.html": changelog,
}
for path, html in PAGES.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", path, len(html))
