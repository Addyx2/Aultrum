"""Writes the static Aultrum Canvas pages into the Aultrum site (public/canvas).

Same layout as the Pleasant pages: the Aultrum main menu, a floating Canvas
sub-menu and a shared footer. Edit the copy here, then run:

    python3 scripts/canvas_pages.py && npm run build:canvas-css
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public" / "canvas"
APP = "https://canvas.aultrum.co.uk"
CONTACT = "Wisdom@aultrum.co.uk"

ARROW = '<svg class="h-4 w-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg class="mt-0.5 h-4 w-4 shrink-0 text-brand-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
EXTERNAL = '<svg class="h-3.5 w-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
MARK = """<span class="grid h-7 w-7 grid-cols-2 gap-[2px] rounded-full bg-ink p-[6px]" aria-hidden="true"><span class="rounded-[2px] bg-brand-400"></span><span class="rounded-[2px] bg-white/30"></span><span class="rounded-[2px] bg-white/30"></span><span class="rounded-[2px] bg-white/70"></span></span>"""


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
<meta property="og:image" content="https://aultrum.co.uk/canvas/img/dashboard.jpg">
<meta name="theme-color" content="#fbfbfe">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Space+Grotesk:wght@500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/canvas/assets/canvas.css">
<script defer src="/canvas/assets/site.js"></script>
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
    ("/canvas/#modules", "Modules", "modules"),
    ("/canvas/#platforms", '<span class="sm:hidden">Platforms</span><span class="hidden sm:inline">For platforms</span>', "platforms"),
    ("/canvas/book-a-demo/", '<span class="sm:hidden">Demo</span><span class="hidden sm:inline">Book demo</span>', "demo"),
]


def header(active: str) -> str:
    main = "\n".join(
        f'<a href="{href}" class="rounded-full px-3 py-1.5 text-sm font-medium transition {"text-ink" if label == "Canvas" else "text-slate-500 hover:text-ink"}"'
        f'{" aria-current=\"page\"" if label == "Canvas" else ""}>{label}</a>'
        for href, label in MAIN_LINKS
    )
    mobile = "\n".join(
        f'<a href="{href}" class="block rounded-lg px-3 py-2 text-base font-medium {"bg-brand-50 text-brand-800" if label == "Canvas" else "text-slate-700"}">{label}</a>'
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
      <a href="/canvas/book-a-demo/" class="hidden rounded-full bg-ink px-4 py-2 text-sm font-semibold text-white transition hover:bg-slate-800 sm:inline-flex">Book a demo</a>
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
  <nav aria-label="Canvas" class="subnav-pill">
    <a href="/canvas/" class="subnav-brand" aria-label="Canvas overview"{' aria-current="page"' if active == "home" else ""}>{MARK}<span class="hidden sm:inline">Canvas</span></a>
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
      <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Products</p>
      <ul class="mt-3 space-y-2 text-sm text-slate-600">
        <li><a class="hover:text-ink" href="/canvas/">Canvas</a></li>
        <li><a class="hover:text-ink" href="/pleasant/">Pleasant</a></li>
        <li><a class="hover:text-ink" href="/flowstatebeta/">Flowstate</a></li>
        <li><a class="hover:text-ink" href="{APP}/login">Log in to Canvas</a></li>
      </ul>
    </div>
    <div>
      <p class="text-xs font-semibold uppercase tracking-wider text-slate-400">Aultrum</p>
      <ul class="mt-3 space-y-2 text-sm text-slate-600">
        <li><a class="hover:text-ink" href="/manifesto.html">Manifesto</a></li>
        <li><a class="hover:text-ink" href="/research/index.html">Research</a></li>
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
    <p class="mx-auto max-w-6xl px-4 py-6 text-xs text-slate-400 sm:px-6">&copy; 2026 Aultrum Technologies Ltd.</p>
  </div>
</footer>
</body>
</html>
"""


def frame(src: str, alt: str, url: str, extra: str = "") -> str:
    return f"""<div class="frame shadow-frame {extra}">
  <div class="frame-bar"><span></span><span></span><span></span><p class="frame-url">{url}</p></div>
  <img src="/canvas/img/{src}" alt="{alt}" width="2880" height="1800" loading="lazy">
</div>"""


def button(href: str, label: str, dark: bool = True) -> str:
    cls = "bg-ink text-white hover:bg-slate-800" if dark else "border border-slate-300 bg-white text-ink hover:border-slate-400"
    return f'<a href="{href}" class="inline-flex items-center gap-2 rounded-full px-5 py-3 text-sm font-semibold transition {cls}">{label} {ARROW}</a>'


def checks(items: list[str], dark: bool = False) -> str:
    icon = CHECK.replace("text-brand-600", "text-brand-300") if dark else CHECK
    return "\n".join(f'<li class="flex gap-2.5">{icon}<span>{i}</span></li>' for i in items)


STEPS = [
    ("Install", "A platform switches a module on for one of its customers with one API call. Repeating it is safe."),
    ("Show", "The module's screens appear inside the platform, signed in as the platform's user, on links that last five minutes and only open on that platform's site."),
    ("Exchange", "Events flow both ways: the platform tells the module what changed, and the module sends signed webhooks back."),
    ("Act", "Modules never touch a platform's data. They ask the platform to act through its own tools, so its permissions, approvals and audit trail still apply."),
]

overview = head(
    "Aultrum Canvas · Build once, stream everywhere | Aultrum",
    "Aultrum Canvas runs modules such as Gateway and Peak once, and streams them into Pleasant and the other platforms your teams already use.",
    "/canvas/",
) + header("home") + f"""<main id="main">
<section class="hero-glow relative -mt-16 overflow-hidden pt-28">
  <div class="grid-lines pointer-events-none absolute inset-0 [mask-image:radial-gradient(70%_60%_at_50%_0%,black,transparent)]"></div>
  <div class="relative mx-auto max-w-4xl px-4 text-center sm:px-6">
    <p class="inline-flex items-center gap-2 rounded-full border border-brand-200 bg-white/80 px-3 py-1 text-xs font-medium text-brand-800">
      <span class="rounded-full bg-brand-600 px-2 py-0.5 text-[10px] font-bold uppercase tracking-wide text-white">New</span>
      The module platform behind Gateway and Peak
    </p>
    <h1 class="mt-7 font-display text-[44px] font-bold leading-[1.02] tracking-tight text-ink sm:text-6xl lg:text-7xl">
      Build once. <span class="font-serif font-normal italic text-brand-600">Stream</span> everywhere.
    </h1>
    <p class="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-slate-600">
      Aultrum Canvas runs our modules once and streams them into Pleasant and the other platforms your teams already use: their screens, their events and their actions, always under the platform's own rules.
    </p>
    <div class="mt-9 flex flex-wrap items-center justify-center gap-3">
      {button("/canvas/book-a-demo/", "Book a demo")}
      {button("#platforms", "Connect a platform", dark=False)}
    </div>
  </div>
  <div class="relative mx-auto mt-16 max-w-6xl px-4 sm:px-6">
    {frame("dashboard.jpg", "The Aultrum Canvas console: modules, connected platforms, installations and recent events", "canvas.aultrum.co.uk/dashboard", "reveal")}
  </div>
</section>

<section class="mx-auto mt-28 max-w-6xl px-4 sm:px-6">
  <div class="reveal max-w-2xl">
    <p class="text-sm font-semibold text-brand-700">How streaming works</p>
    <h2 class="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">One contract between every module and every platform.</h2>
    <p class="mt-4 text-lg leading-relaxed text-slate-600">A module is written once against the Canvas contract. Any platform that speaks the same contract can install it, show it and work with it, without rebuilding anything.</p>
  </div>
  <ol class="mt-12 grid gap-px overflow-hidden rounded-2xl border border-slate-200 bg-slate-200 sm:grid-cols-2 lg:grid-cols-4">
""" + "\n".join(
    f"""    <li class="reveal bg-white p-6">
      <p class="font-display text-sm font-semibold text-brand-600">0{i + 1}</p>
      <h3 class="mt-2 font-display text-xl font-semibold">{name}</h3>
      <p class="mt-2 text-[15px] leading-relaxed text-slate-600">{text}</p>
    </li>"""
    for i, (name, text) in enumerate(STEPS)
) + f"""
  </ol>
</section>

<section id="modules" class="mx-auto mt-28 max-w-6xl scroll-mt-24 px-4 sm:px-6">
  <div class="reveal max-w-2xl">
    <p class="text-sm font-semibold text-brand-700">Modules</p>
    <h2 class="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">Add-ons that work wherever your teams work.</h2>
  </div>
  <div class="mt-10 grid grid-cols-1 items-start gap-6 lg:grid-cols-[1.2fr_0.8fr]">
    <div class="reveal rounded-3xl border border-slate-200 bg-white p-6 sm:p-8">
      <div class="flex items-center justify-between gap-3">
        <h3 class="font-display text-2xl font-semibold">Gateway</h3>
        <span class="rounded-full bg-brand-50 px-2.5 py-1 text-xs font-semibold text-brand-800 ring-1 ring-inset ring-brand-600/15">Pilot programme open</span>
      </div>
      <p class="mt-3 text-[15px] leading-relaxed text-slate-600">One conversation layer for every channel, agent and person. Gateway takes calls and messages on phone, SMS, WhatsApp and web chat, works out who is speaking, and routes the conversation to the right AI agent or person. Agents such as Persona Assist join as participants; staff watch, take over and hand back.</p>
      <ul class="mt-5 space-y-2.5 text-[15px] text-slate-700">
{checks(["A carer rings in sick at 6am: the shift is marked uncovered and offered to carers who are free and cleared to work", "Emergencies are told to ring 999 and handed to a person straight away", "Every message, handover and action recorded in one audit trail"])}
      </ul>
      <div class="mt-6">{frame("embed.jpg", "Gateway shown inside a platform, streamed from Canvas", "Inside Pleasant · streamed from Canvas")}</div>
    </div>
    <div class="reveal rounded-3xl border border-dashed border-slate-300 bg-white/60 p-6 sm:p-8">
      <div class="flex items-center justify-between gap-3">
        <h3 class="font-display text-2xl font-semibold">Peak</h3>
        <span class="rounded-full bg-slate-100 px-2.5 py-1 text-xs font-semibold text-slate-700">Coming soon</span>
      </div>
      <p class="mt-3 text-[15px] leading-relaxed text-slate-600">Recognition that pays. Points, streaks and rewards for carers, built from clock-ins and client praise, and the reliability record that feeds Shift Readiness.</p>
      <p class="mt-6 text-sm text-slate-500">More modules follow the same contract, so they arrive in every connected platform at once.</p>
    </div>
  </div>
</section>

<section id="platforms" class="mt-28 scroll-mt-24 bg-ink py-24 text-white">
  <div class="mx-auto grid max-w-6xl grid-cols-1 items-center gap-12 px-4 sm:px-6 lg:grid-cols-[0.9fr_1.1fr]">
    <div class="reveal">
      <p class="text-sm font-semibold text-brand-300">For platforms</p>
      <h2 class="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">Connect once. Every module <span class="font-serif font-normal italic text-brand-300">follows</span>.</h2>
      <p class="mt-4 text-lg leading-relaxed text-slate-300">Pleasant is the first platform on Canvas. Any product can join with a client ID, a few API calls and an iframe.</p>
      <ul class="mt-6 space-y-3 text-[15px] text-slate-200">
{checks(["Install and uninstall modules per customer with one call", "Show module screens with five-minute links that only open on your own site", "Signed webhooks with timestamps, so you can verify every event", "Credentials shown once, rotated or revoked in a click"], dark=True)}
      </ul>
    </div>
    <div class="reveal min-w-0">
      <pre class="overflow-x-auto rounded-2xl border border-white/10 bg-white/5 p-5 text-[13px] leading-relaxed text-slate-200"><code><span class="text-slate-500"># Switch Gateway on for one of your customers</span>
curl -X POST {APP}/api/v1/installations \\
  -u "$CLIENT_ID:$CLIENT_SECRET" \\
  -H "Content-Type: application/json" \\
  -d '{{"module":"gateway","tenantId":"agency_123",
       "tenantName":"Brightwater Care"}}'

<span class="text-slate-500"># Show it inside your app</span>
curl -X POST {APP}/api/v1/embed-tokens \\
  -u "$CLIENT_ID:$CLIENT_SECRET" \\
  -d '{{"installationId":"…","user":{{"id":"u_42","name":"Amara"}}}}'
<span class="text-brand-300">→ {{"url":"{APP}/embed/gateway?token=…"}}</span></code></pre>
    </div>
  </div>
</section>

<section class="mx-auto mt-28 grid max-w-6xl grid-cols-1 items-center gap-12 px-4 sm:px-6 lg:grid-cols-[0.9fr_1.1fr]">
  <div class="reveal">
    <p class="text-sm font-semibold text-brand-700">The console</p>
    <h2 class="mt-3 font-display text-3xl font-bold tracking-tight sm:text-4xl">See every installation and every event.</h2>
    <p class="mt-4 text-lg leading-relaxed text-slate-600">One place to manage modules, connected platforms and their customers, and to follow everything flowing between them.</p>
    <ul class="mt-6 space-y-3 text-[15px] text-slate-700">
{checks(["Preview any module exactly as the customer sees it", "Pause a customer's module, or send a test event to check the connection", "Delivery status on every webhook, with one-click retry"])}
    </ul>
  </div>
  <div class="reveal">{frame("installations.jpg", "Canvas installations: each module and customer with its status and events", "canvas.aultrum.co.uk/installations")}</div>
</section>

<section class="mx-auto mt-28 max-w-6xl px-4 sm:px-6">
  <h2 class="reveal font-display text-3xl font-bold tracking-tight sm:text-4xl">The platform stays in charge.</h2>
  <div class="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
""" + "\n".join(
    f"""    <div class="reveal rounded-2xl border border-slate-200 bg-white p-6">
      <h3 class="font-semibold">{t}</h3>
      <p class="mt-2 text-sm leading-relaxed text-slate-600">{b}</p>
    </div>"""
    for t, b in [
        ("No direct writes", "Modules ask; the platform acts, with its own permissions and approvals."),
        ("Locked-down screens", "Module screens only open inside the platform they were issued for."),
        ("Signed everything", "Embed links and webhooks are signed and expire, so they can't be forged or replayed."),
        ("Full event log", "Every event in and out is recorded, with delivery status."),
    ]
) + f"""
  </div>
</section>

<section class="mx-auto mt-28 max-w-6xl px-4 sm:px-6">
  <div class="reveal relative overflow-hidden rounded-3xl bg-gradient-to-br from-brand-700 to-brand-950 px-6 py-16 text-center text-white sm:px-12">
    <div class="grid-lines pointer-events-none absolute inset-0 opacity-20"></div>
    <h2 class="relative font-display text-3xl font-bold tracking-tight sm:text-5xl">Bring Aultrum modules to your platform.</h2>
    <p class="relative mx-auto mt-4 max-w-xl text-lg text-brand-100">Join the Gateway pilot, or talk to us about connecting your product to Canvas.</p>
    <div class="relative mt-8 flex flex-wrap justify-center gap-3">
      <a href="/canvas/book-a-demo/" class="inline-flex items-center gap-2 rounded-full bg-white px-5 py-3 text-sm font-semibold text-ink transition hover:bg-brand-50">Book a demo {ARROW}</a>
      <a href="{APP}/login" class="inline-flex items-center gap-2 rounded-full border border-white/30 px-5 py-3 text-sm font-semibold text-white transition hover:bg-white/10">Log in to Canvas</a>
    </div>
  </div>
</section>
</main>
""" + FOOTER

demo = head(
    "Book a demo · Aultrum Canvas | Aultrum",
    "Book a demo of Aultrum Canvas and the Gateway pilot.",
    "/canvas/book-a-demo/",
) + header("demo") + f"""<main id="main">
<section class="hero-glow -mt-16 pt-28">
  <div class="mx-auto grid max-w-6xl gap-12 px-4 sm:px-6 lg:grid-cols-[0.8fr_1.2fr]">
    <div>
      <p class="text-sm font-semibold text-brand-700">Book a demo</p>
      <h1 class="mt-3 font-display text-4xl font-bold tracking-tight sm:text-5xl">See a module <span class="font-serif font-normal italic text-brand-600">stream</span> into your platform.</h1>
      <p class="mt-5 text-lg text-slate-600">Pick a time that suits you. We'll confirm straight away and send a calendar invite.</p>
      <h2 class="mt-10 text-sm font-semibold uppercase tracking-wider text-slate-400">What we'll cover</h2>
      <ul class="mt-4 space-y-3 text-[15px] text-slate-700">
{checks(["The Gateway pilot, and the calls and messages it handles", "How a module appears inside Pleasant, or inside your own product", "The contract: install, show, exchange events, act", "Security: signed links, signed webhooks, origin-locked screens"])}
      </ul>
      <p class="mt-10 text-sm text-slate-500">Prefer email? <a href="mailto:{CONTACT}?subject=Aultrum%20Canvas" class="font-semibold text-brand-700 hover:text-brand-800">{CONTACT}</a></p>
    </div>
    <div class="rounded-3xl border border-slate-200 bg-white p-2 shadow-frame sm:p-4">
      <div id="cal-canvas-demo" style="width:100%;min-height:680px;overflow:auto"></div>
    </div>
  </div>
</section>
</main>
<script>
  (function (C, A, L) {{ let p = function (a, ar) {{ a.q.push(ar); }}; let d = C.document; C.Cal = C.Cal || function () {{ let cal = C.Cal; let ar = arguments; if (!cal.loaded) {{ cal.ns = {{}}; cal.q = cal.q || []; d.head.appendChild(d.createElement("script")).src = A; cal.loaded = true; }} if (ar[0] === L) {{ const api = function () {{ p(api, arguments); }}; const namespace = ar[1]; api.q = api.q || []; if (typeof namespace === "string") {{ cal.ns[namespace] = cal.ns[namespace] || api; p(cal.ns[namespace], ar); p(cal, ["initNamespace", namespace]); }} else p(cal, ar); return; }} p(cal, ar); }}; }})(window, "https://app.cal.com/embed/embed.js", "init");
  Cal("init", "canvasdemo", {{ origin: "https://app.cal.com" }});
  Cal.ns.canvasdemo("inline", {{
    elementOrSelector: "#cal-canvas-demo",
    config: {{ layout: "month_view", useSlotsViewOnSmallScreen: "true" }},
    calLink: "addyadeyeri/flowstatedemo",
  }});
  Cal.ns.canvasdemo("ui", {{ hideEventTypeDetails: false, layout: "month_view" }});
</script>
""" + FOOTER

PAGES = {
    ROOT / "index.html": overview,
    ROOT / "book-a-demo" / "index.html": demo,
}
for path, html in PAGES.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", path, len(html))
