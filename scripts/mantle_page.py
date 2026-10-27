"""Writes aultrum.co.uk/mantle/: Mantle, the golden foundation for Aultrum.

Mantle sets out the duty of care everything Aultrum builds rests on, and the
research underneath it (from MANTORIUM_BRIEF.md): how time changes people, and
why AI is only a means to deliver care more accurately and with more insight.
Header and footer come from index.html. CSS: npm run build:home-css.
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
OUT = SITE / "public" / "mantle" / "index.html"

home = (SITE / "index.html").read_text(encoding="utf-8")
head = home[: home.index("<header")].replace('<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n', '<link rel="icon" href="/brand/icon.svg" type="image/svg+xml">\n')
header = home[home.index("<header") : home.index("</header>") + 9]
footer = home[home.index("<footer") : home.index("</footer>") + 9]

W = "max-w-[1320px] mx-auto px-margin md:px-margin-md lg:px-margin-lg"
GOLD, GOLD_LIGHT, GOLD_BAND = "#8a6514", "#e6c36a", "#17130a"
EYEBROW = f"font-label-mono text-label-mono text-[{GOLD}] uppercase tracking-wider"
H2 = "font-headline-lg text-headline-md md:text-headline-lg text-ink-dark tracking-tight"
LEAD = "font-body-lg text-body-lg text-ink-muted"


def section(id, eyebrow, title, intro, inner, border=True):
    top = "border-t border-border-editorial" if border else ""
    return f'''<section id="{id}" class="w-full scroll-mt-20 {top}"><div class="{W} py-16 md:py-24">
<div class="max-w-3xl mb-10 flex flex-col gap-3"><p class="{EYEBROW}">{eyebrow}</p><h2 class="{H2}">{title}</h2>{f'<p class="{LEAD}">{intro}</p>' if intro else ""}</div>
{inner}
</div></section>'''


def table(heads, rows):
    th = "".join(f'<th class="text-left font-label-mono text-label-mono uppercase tracking-wider text-ink-muted px-4 py-3">{h}</th>' for h in heads)
    tr = "".join("<tr class=\"border-t border-border-editorial align-top\">" + "".join(f'<td class="px-4 py-4 font-body-md text-ink-dark {"font-medium" if i == 0 else "text-ink-muted"}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="overflow-x-auto rounded-xl border border-border-editorial bg-surface-container-lowest"><table class="w-full min-w-[720px]"><thead class="bg-surface-container-low"><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def cards(items, cols="md:grid-cols-2 lg:grid-cols-3"):
    cells = "".join(f'<div class="bg-surface flex flex-col gap-2 p-6 md:p-8"><h3 class="font-headline-sm text-headline-sm text-ink-dark">{t}</h3><p class="font-body-md text-ink-muted">{b}</p></div>' for t, b in items)
    return f'<div class="grid grid-cols-1 {cols} gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">{cells}</div>'


PRINCIPLES = [
    ("The duty stays with people.", "Carers, nurses, managers, families, commissioners, and the people who build their tools all carry a duty of care. No system carries it for them, and none of ours tries to."),
    ("AI makes care more accurate.", "It shows what is true about a person now, not what was written down years ago, so decisions rest on current evidence rather than old records."),
    ("AI makes care more insightful.", "It sees patterns across thousands of shifts, calls and visits that no one person could hold in mind, and brings them to the person who needs them."),
    ("Signals, never decisions.", "Our models produce evidence and flags. People weigh them and decide. Every action is approved by a person and recorded."),
    ("Time changes people.", "Skills fade without practice, trust grows with continuity, and tiredness builds up over a run of shifts. Care that ignores time treats people as they were, not as they are."),
    ("Records must not hold people back.", "When a constraint has outlived its reason, the duty of care is to notice, and to give people the evidence to release it."),
]

TIME_ROWS = [
    ("Care work", "A carer’s skill fades without training; rapport builds through continuity; burnout accrues over shifts", "Treats carers as interchangeable and measures hours, not quality", "Follows skill drift, bond maturity and burnout risk over time"),
    ("Employment", "Experience loses relevance; skills expire", "Hires on “years of experience” and never models how skills fade", "Treats competence as something that changes, not a credential"),
    ("Finance", "Income varies; obligations weigh differently over time; debt grows", "Takes a snapshot of income and penalises normal ups and downs", "Reads income as a pattern over time"),
    ("Health", "Conditions change; sticking with treatment fades; risk shifts", "Static assessments, re-checked only at appointments", "Continuous views of risk that move with the person"),
    ("Compliance", "Risk changes; rehabilitation takes time", "Checks freeze a moment and keep flagging it", "Weighs risk by what has happened since"),
]

EXAMPLES = [
    ("The expired certificate", "A CV says “five years’ experience”, but the training behind it lapsed two years ago. The five years reassures; the lapse goes unseen."),
    ("The overlooked carer", "A carer isn’t matched to a client because their years served don’t fit a profile, though their recent work shows they are the better fit."),
    ("The flag that stayed", "A compliance flag that no longer applies keeps someone out of work. The person changed; the record didn’t."),
]

PHASES = [
    ("M0: Foundations", "Sep–Oct 2026", "How skills fade, how obligations age, and how to describe each person’s pattern of change", "Mantle thesis paper"),
    ("M1: In Aultrum", "Nov 2026", "Shift readiness and rapport, from Peak, read as signals over time", "A time-aware signal of care quality"),
    ("M2: A second field", "Q1 2027", "The same model applied to employment or finance", "Evidence that it holds outside care"),
    ("M3: Publication", "Q2 2027", "Temporal modelling of human attributes: architecture and evidence", "Peer-reviewed paper and published architecture"),
]

hero = f'''<section class="w-full pt-10 pb-16 md:pt-16 md:pb-24 {W}">
<div class="max-w-4xl flex flex-col items-start gap-space-md">
<p class="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-[{GOLD}]/30 bg-[{GOLD_LIGHT}]/15 {EYEBROW}"><span class="w-1.5 h-1.5 rounded-full bg-[{GOLD}]"></span>Mantle · The golden foundation</p>
<h1 class="font-display-hero text-headline-lg md:text-display-hero text-ink-dark tracking-tight">Everyone has a <span class="text-[{GOLD}]">duty of care.</span></h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mt-1">Mantle is the foundation beneath everything Aultrum builds. Care is a duty we all carry. AI does not carry it for us. It is a means to deliver care more accurately, and with more insight.</p>
<div class="w-full max-w-2xl mt-6 pt-6 border-t border-[{GOLD}]/30 grid grid-cols-1 sm:grid-cols-3 gap-4">
<a class="font-body-sm text-ink-dark hover:text-[{GOLD}]" href="#principles"><span class="block {EYEBROW}">01</span>Our principles</a>
<a class="font-body-sm text-ink-dark hover:text-[{GOLD}]" href="#time">
<span class="block {EYEBROW}">02</span>Time changes people</a>
<a class="font-body-sm text-ink-dark hover:text-[{GOLD}]" href="#research"><span class="block {EYEBROW}">03</span>The research</a>
</div>
</div></section>'''

principles = f'''<section id="principles" class="w-full scroll-mt-20 relative overflow-hidden bg-[{GOLD_BAND}]"><div class="{W} py-16 md:py-24">
<div class="max-w-3xl mb-12 flex flex-col gap-3"><p class="font-label-mono text-label-mono text-[{GOLD_LIGHT}] uppercase tracking-wider">Principles</p><h2 class="font-headline-lg text-headline-md md:text-headline-lg text-white tracking-tight">The duty is ours. AI helps us meet it.</h2><p class="font-body-lg text-white/70">Six rules every Aultrum product is held to, from the first line of code to the last phone call.</p></div>
<ol class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-px bg-white/10 border border-white/10 rounded-xl overflow-hidden">{"".join(f'<li class="bg-[{GOLD_BAND}] p-6 md:p-8 flex flex-col gap-3"><span class="font-label-mono text-label-mono text-[{GOLD_LIGHT}]">{i:02d}</span><h3 class="font-headline-sm text-headline-sm text-white">{t}</h3><p class="font-body-md text-white/70">{b}</p></li>' for i, (t, b) in enumerate(PRINCIPLES, 1))}</ol>
</div></section>'''

axiom = section("time", "The founding idea", "Time has its effect on people.",
    "This is not a metaphor. Time is the least examined variable in every system that governs people’s lives: care, work, money, health and justice. People change, situations move on, obligations pile up. A system that ignores this ends up holding people to conditions that no longer exist, or crediting them for conditions that never did.",
    table(["Field", "What time does", "What systems do now", "What they should do"], TIME_ROWS)
    + f'<p class="mt-6 max-w-3xl {LEAD}">The common thread: <strong class="text-ink-dark font-medium">every system treats time as a date stamp, not as something that changes the person.</strong> Mantle treats time as the variable itself.</p>', border=False)

deterrent = section("obligations", "Deterrent obligations", "When a record outlives the reason for it.",
    "A deterrent obligation is any requirement or condition placed on a person that lasts beyond its relevance, or was never relevant, and stands in the way of their progress. They are judgements frozen in time, applied to people who are not.",
    cards(EXAMPLES) + f'<p class="mt-6 max-w-3xl {LEAD}">Part of the duty of care is noticing when an obligation has become a deterrent, and producing the evidence that lets someone release it, replace it, or look at it again.</p>')

engine = section("research", "The research", "A model whose main variable is time.",
    "Mantle’s research builds a temporal model: one that learns how a particular person changes over time, how their situation moves on, and how the obligations on them age. It is not a language model, and it is not a prediction engine.",
    f'''<div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
<div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-3 gap-px bg-border-editorial border border-border-editorial rounded-xl overflow-hidden">
<div class="bg-surface p-6 flex flex-col gap-2"><p class="{EYEBROW}">In</p><p class="font-body-md text-ink-dark">A person’s record over time: what they did, how it was assessed, how it turned out. The field it comes from, and the obligations on them, with when each began.</p></div>
<div class="bg-surface p-6 flex flex-col gap-2"><p class="{EYEBROW}">Model</p><p class="font-body-md text-ink-dark">How each attribute fades or grows for this person, how long each obligation has been relevant, and whether they are improving, steady, declining or diverging.</p></div>
<div class="bg-surface p-6 flex flex-col gap-2"><p class="{EYEBROW}">Out</p><p class="font-body-md text-ink-dark">Whether an obligation is still relevant, stale or a deterrent; the person as they are now; a suggestion to keep, release or review; and how confident it is.</p></div>
</div>
<div class="lg:col-span-5 flex flex-col gap-4">
<p class="{LEAD}"><strong class="text-ink-dark font-medium">The model does not make decisions. It produces signals.</strong> The people and organisations who use it decide what to do with them.</p>
<ul class="flex flex-col gap-2 font-body-md text-ink-muted">{"".join(f'<li class="flex gap-2"><span class="text-[{GOLD}]" aria-hidden="true">—</span>{x}</li>' for x in ["Not a general-purpose AI or language model", "Not a “digital twin”: we don’t simulate people, we understand how time changes them", "Not a forecast of behaviour: it reads the time in the evidence that already exists", "Not a compliance tool, though compliance teams can use it"])}</ul>
</div></div>''')

in_aultrum = section("aultrum", "In Aultrum", "How the foundation shows up in our products.", "",
    cards([
        ("Peak", "Recognition that reflects how a carer is doing now: steady attendance, growing rapport, praise that adds up over time."),
        ("Gateway", "Every enquiry answered and passed to a person, so no one waiting for care is left unheard."),
        ("Pleasant", "Training and checks followed as they age, so an expiry is caught before it puts anyone at risk."),
    ]))

why_now = section("now", "Why now", "Three reasons this matters now.", "",
    cards([
        ("Regulation is looking at time.", "The CQC is moving toward continuous monitoring, and the EU AI Act asks for risk to be reassessed over time. Systems that model time are built to comply."),
        ("AI makes more data, not better judgement.", "Models can write about time but rarely model it. Seeing people as they are now needs a different kind of model."),
        ("The workforce crisis is about time.", "Skills fade faster than training cycles, and tiredness builds faster than rest. Retention is a question of balance over time."),
    ]))

programme = section("programme", "Programme", "What we are testing, and when.",
    "We don’t claim to have solved time. We have found a gap no existing system fills, and we are testing whether this fills it.",
    table(["Phase", "When", "Focus", "Result"], PHASES))

close = f'''<section class="w-full relative overflow-hidden bg-[{GOLD_BAND}] py-20 md:py-28 text-center"><div class="{W} flex flex-col items-center gap-4">
<p class="font-label-mono text-label-mono text-[{GOLD_LIGHT}] uppercase tracking-wider">Mantle</p>
<h2 class="font-display-hero text-headline-lg md:text-display-hero text-white tracking-tight max-w-3xl">The duty of care is ours. AI just helps us see.</h2>
<p class="font-body-lg text-white/70 max-w-xl">Read where Aultrum is going, and what we believe about care.</p>
<div class="flex flex-col sm:flex-row items-center gap-3 mt-4"><a class="inline-flex items-center gap-2 bg-[{GOLD_LIGHT}] text-[{GOLD_BAND}] font-body-sm font-medium px-8 py-3.5 rounded-full hover:bg-white transition-all" href="/vision.html">Our vision</a><a class="inline-flex items-center gap-2 border border-white/30 text-white font-body-sm font-medium px-8 py-3.5 rounded-full hover:bg-white/10 transition-all" href="/statements/">Statements</a></div>
</div></section>'''

main = f'<main class="w-full pt-16 bg-surface"><div class="flex flex-col w-full text-on-surface">{hero}{principles}{axiom}{deterrent}{engine}{in_aultrum}{why_now}{programme}{close}</div></main>'

page_head = re.sub(r"<title>[^<]*</title>", "<title>Mantle · The golden foundation | Aultrum</title>", head)
page_head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Mantle is the foundation beneath everything Aultrum builds: everyone has a duty of care, and AI is a means to deliver it more accurately and with more insight.">', page_head)
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(page_head + header + main + footer + "\n</body>\n</html>\n", encoding="utf-8")
print("wrote", OUT)
