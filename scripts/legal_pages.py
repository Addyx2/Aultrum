"""Writes the legal pages in the homepage's design: /privacy/, /terms/ and /dpa/.

Header and footer come from index.html. CSS: npm run build:home-css.
Change UPDATED whenever the wording changes.
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
UPDATED = "27 October 2026"
CONTACT = "Wisdom@aultrum.co.uk"
COMPANY = "Aultrum Technologies Ltd"

home = (SITE / "index.html").read_text(encoding="utf-8")
head = home[: home.index("<header")].replace('<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n', '<link rel="icon" href="/brand/icon.svg" type="image/svg+xml">\n')
header = home[home.index("<header") : home.index("</header>") + 9]
footer = home[home.index("<footer") : home.index("</footer>") + 9]

W = "max-w-[1320px] mx-auto px-margin md:px-margin-md lg:px-margin-lg"
EYEBROW = "font-label-mono text-label-mono text-ink-primary uppercase tracking-wider"
MAIL = f'<a class="text-ink-primary hover:underline" href="mailto:{CONTACT}">{CONTACT}</a>'

# Companies that handle personal data for us, and why. Shared by the privacy policy and the DPA.
SUBPROCESSORS = [
    ("Vercel Inc.", "Hosting for the website and apps, and their databases (through Vercel’s storage partners)", "United States and EU"),
    ("Anthropic PBC", "The AI model behind Gateway’s replies and Persona", "United States"),
    ("Twilio Inc.", "Phone calls and text messages for Gateway, including turning speech into text", "United States"),
    ("Resend Inc.", "Sending emails: sign-in links, invites and notifications", "United States"),
    ("Cal.com Inc.", "Booking demos on the website", "United States and EU"),
    ("FormSubmit", "Delivering website forms (contact and merch orders) to our inbox", "United States"),
]


def sub_table():
    rows = "".join(f'<tr class="border-t border-border-editorial align-top"><td class="px-4 py-3 font-medium text-ink-dark">{n}</td><td class="px-4 py-3 text-ink-muted">{w}</td><td class="px-4 py-3 text-ink-muted">{l}</td></tr>' for n, w, l in SUBPROCESSORS)
    return f'<div class="overflow-x-auto rounded-xl border border-border-editorial bg-surface-container-lowest not-prose"><table class="w-full min-w-[640px] font-body-md text-left"><thead class="bg-surface-container-low"><tr><th class="px-4 py-3 font-label-mono text-label-mono uppercase tracking-wider text-ink-muted">Company</th><th class="px-4 py-3 font-label-mono text-label-mono uppercase tracking-wider text-ink-muted">What for</th><th class="px-4 py-3 font-label-mono text-label-mono uppercase tracking-wider text-ink-muted">Where</th></tr></thead><tbody>{rows}</tbody></table></div>'


def ul(items):
    return '<ul class="list-disc pl-5 flex flex-col gap-2">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def sections(parts):
    """parts: list of (heading, html). Numbered, with a contents list."""
    toc = "".join(f'<li><a class="hover:text-ink-primary" href="#s{i}">{h}</a></li>' for i, (h, _) in enumerate(parts, 1))
    body = "".join(f'<section id="s{i}" class="scroll-mt-24 flex flex-col gap-4"><h2 class="font-headline-md text-headline-sm md:text-headline-md text-ink-dark tracking-tight">{i}. {h}</h2>{html}</section>' for i, (h, html) in enumerate(parts, 1))
    return toc, body


def write(slug, title, lead, parts, description):
    toc, body = sections(parts)
    main = f'''<main class="w-full pt-16 bg-surface"><div class="{W} pt-10 pb-16 md:pt-16 md:pb-24 grid grid-cols-1 lg:grid-cols-12 gap-10">
<aside class="lg:col-span-3 lg:sticky lg:top-24 self-start hidden lg:block"><p class="{EYEBROW} mb-3">Contents</p><ol class="flex flex-col gap-2 font-body-sm text-ink-muted list-decimal pl-4">{toc}</ol>
<p class="{EYEBROW} mt-8 mb-3">Legal</p><div class="flex flex-col gap-2 font-body-sm"><a class="text-ink-muted hover:text-ink-primary" href="/privacy/">Privacy policy</a><a class="text-ink-muted hover:text-ink-primary" href="/terms/">Terms of service</a><a class="text-ink-muted hover:text-ink-primary" href="/dpa/">Data processing agreement</a></div></aside>
<article class="lg:col-span-8 lg:col-start-5 min-w-0 flex flex-col gap-10 font-body-lg text-body-lg text-ink-dark [&_a]:break-words">
<header class="flex flex-col gap-3"><p class="{EYEBROW}">Last updated {UPDATED}</p><h1 class="font-display-hero text-headline-lg md:text-display-hero text-ink-primary tracking-tight">{title}</h1><p class="text-on-surface-variant">{lead}</p></header>
{body}
</article></div></main>'''
    h = re.sub(r"<title>[^<]*</title>", f"<title>{title} | Aultrum</title>", head)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{description}">', h)
    out = SITE / "public" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(h + header + main + footer + "\n</body>\n</html>\n", encoding="utf-8")
    print("wrote", out)


P = lambda t: f"<p>{t}</p>"

# ------------------------------------------------------------------ Privacy policy
write("privacy", "Privacy policy",
      f"How {COMPANY} (“Aultrum”, “we”) handles personal data on aultrum.co.uk and in Elements, Pleasant and Aultrum ID.",
      [
          ("Who we are", P(f"{COMPANY} makes software for social care: Elements (Gateway and Peak), Pleasant, and Aultrum ID, the account that signs you in to them. For questions about your data, or to use your rights, email {MAIL}.")),
          ("Two roles", P("We handle personal data in two ways, and the rules differ:") + ul([
              "<strong class=\"font-medium\">As a controller</strong>, for our own purposes: our website, the accounts of people who use our products, sales conversations, and orders.",
              "<strong class=\"font-medium\">As a processor</strong>, for our customers: the care organisations that use Elements or Pleasant decide what data goes in about their staff, clients and callers, and we handle it only on their instructions, under our <a class=\"text-ink-primary hover:underline\" href=\"/dpa/\">data processing agreement</a>. If you are a carer, a client or a caller, the organisation you work with or contacted is responsible for that data. Contact them first; we will help them answer you.",
          ])),
          ("What we collect", ul([
              "<strong class=\"font-medium\">Account details:</strong> your name, work email, organisation, role, and a hashed password (we never store the password itself).",
              "<strong class=\"font-medium\">Sign-in records:</strong> when you signed in, failed attempts, and IP addresses, used to keep accounts secure and to limit repeated attempts.",
              "<strong class=\"font-medium\">What our customers put in:</strong> for example carers’ and contacts’ names and phone numbers, Peak points and rewards, and in Pleasant shifts, timesheets, compliance records, payroll and invoices.",
              "<strong class=\"font-medium\">Gateway conversations:</strong> when someone calls, texts or chats with an organisation that uses Gateway, we keep the phone number or chat visitor code, the conversation as text, and a summary. Phone calls are turned into text; we do not keep audio recordings.",
              "<strong class=\"font-medium\">Website forms:</strong> what you send us when you book a demo, apply or contact us, or order merch (including a delivery address).",
          ])),
          ("Why we use it, and our lawful basis", ul([
              "To provide the products you or your organisation signed up for (contract).",
              "To keep accounts and services secure, prevent abuse and fix faults (legitimate interests).",
              "To reply to enquiries, arrange demos and send orders (legitimate interests, or steps before a contract).",
              "To meet legal obligations, such as keeping financial records (legal obligation).",
          ]) + P("We do not sell personal data, and we do not use it for advertising.")),
          ("How we use AI", P("Gateway and Persona use an AI model provided by Anthropic. The text of a conversation is sent to the model so it can reply. Anthropic does not use data sent through its commercial API to train its models.") + P("AI never makes decisions about people on its own. Gateway answers questions and takes enquiries and messages for a person to follow up; Persona prepares work that a person must approve. We do not carry out solely automated decision-making that has legal or similarly significant effects on anyone.")),
          ("Who we share it with", P("We use these companies to run our services. Each is bound by a contract to protect the data and use it only for us.") + sub_table() + P("We may also share data if the law requires it, or with a buyer if our business is sold, under the same protections.")),
          ("International transfers", P("Some of these companies are based in the United States. When data leaves the UK, we rely on the safeguards UK data protection law requires, such as the UK International Data Transfer Addendum or the UK Extension to the EU–US Data Privacy Framework.")),
          ("How long we keep it", ul([
              "Account and customer data: while the account is open. When a customer closes their account, we delete their data within 30 days, unless they ask us to return it first.",
              "Sign-in records and rate-limit counters: up to 12 months.",
              "Website enquiries and orders: up to 2 years, longer if the law requires (for example, financial records for 6 years).",
          ])),
          ("Security", P("Data is encrypted in transit. Passwords are hashed. Links sent by email expire and work once. Embedded screens and webhooks are signed so they cannot be forged. Access is limited to the people who need it, and important actions are recorded in an audit log.")),
          ("Cookies", P("Our apps use one essential cookie to keep you signed in. The website’s merch page remembers your basket in your browser. We do not use advertising or analytics cookies. Fonts are loaded from Google Fonts, which receives your IP address when a page loads.")),
          ("Your rights", P(f"Under UK data protection law you can ask for a copy of your data, ask us to correct or delete it, object to or restrict how we use it, and ask for it in a portable format. Email {MAIL}; we reply within one month. If you’re unhappy with our answer, you can complain to the Information Commissioner’s Office at <a class=\"text-ink-primary hover:underline\" href=\"https://ico.org.uk\">ico.org.uk</a>.")),
          ("Children", P("Our products are for organisations and their staff. They are not meant for children under 16.")),
          ("Changes", P("We will update this page when our practices change, and tell customers about significant changes by email.")),
      ],
      "How Aultrum handles personal data on its website and in Elements, Pleasant and Aultrum ID.")

# ------------------------------------------------------------------ Terms of service
write("terms", "Terms of service",
      f"The agreement between {COMPANY} (“Aultrum”, “we”) and the organisation that uses Elements, Pleasant or Aultrum ID (“you”).",
      [
          ("Accepting these terms", P("By creating an organisation or using our products, you agree to these terms on behalf of your organisation, and confirm you are allowed to. If you have a signed agreement with us, it takes priority where it differs.")),
          ("Beta", P("Elements is in open beta. Features may change, and we may pause or remove parts of it. We’ll tell you before any change that removes something you rely on. Fees, if any, will be agreed with you in writing before you are charged.")),
          ("Your account", ul([
              "Keep sign-in details secret, and tell us straight away if you think someone else has them.",
              "You are responsible for the people you invite and what they do in your account.",
              "Give us accurate details, and keep your contact email up to date.",
          ])),
          ("Your data", P("You own the data you put into our products. You give us permission to handle it only to provide, secure and support the service, as set out in our <a class=\"text-ink-primary hover:underline\" href=\"/dpa/\">data processing agreement</a>, which forms part of these terms. You are responsible for having a lawful basis to put people’s data in, and for telling them how it is used.")),
          ("What the products are, and aren’t", ul([
              "<strong class=\"font-medium\">Gateway is not an emergency service.</strong> It takes enquiries and messages. If it hears signs of an emergency it tells the caller to ring 999 and flags the conversation, but it can miss them. You must follow up every conversation it hands to you.",
              "<strong class=\"font-medium\">AI can be wrong.</strong> Check what Gateway and Persona say and prepare before relying on it. People in your organisation remain responsible for care decisions.",
              "<strong class=\"font-medium\">Peak rewards are yours to give.</strong> Cash-outs and perks your organisation approves are your obligation to pay or provide, including any tax due.",
              "<strong class=\"font-medium\">Pleasant’s payroll and invoices are tools.</strong> Check every payrun and invoice before you use it. You remain responsible for paying people correctly and for your filings with HMRC.",
          ])),
          ("Acceptable use", P("Don’t use our products to break the law, to send spam or harassing messages, to try to get into accounts or data that aren’t yours, to overload or attack the service, or to copy it. We may suspend an account that does, and will tell you why unless the law stops us.")),
          ("Our responsibilities", P("We will run the service with reasonable skill and care, keep your data secure as described in our privacy policy and data processing agreement, and give you support by email. We don’t promise the service will be uninterrupted or error-free, especially during the beta.")),
          ("Liability", P("Nothing in these terms limits liability for death or personal injury caused by negligence, for fraud, or for anything else the law does not allow to be limited.") + P("Otherwise, neither of us is liable for indirect or consequential loss, or for lost profits, revenue or data that could have been avoided by reasonable precautions. Our total liability in any 12 months is limited to the greater of the fees you paid us in that period and £100.")),
          ("Ending the agreement", P(f"You can stop using our products and close your account at any time by emailing {MAIL}. We may end it with 30 days’ notice, or straight away if you seriously break these terms. When it ends, you can ask us for a copy of your data within 30 days; after that we delete it.")),
          ("Changes to these terms", P("We may update these terms. We’ll tell you by email at least 30 days before a change that affects you takes effect, unless it is required by law sooner.")),
          ("Law", P("These terms are governed by the law of England and Wales, and the courts of England and Wales will deal with any dispute.")),
          ("Contact", P(f"{COMPANY}. Email {MAIL}.")),
      ],
      "The terms for using Aultrum Elements, Pleasant and Aultrum ID.")

# ------------------------------------------------------------------ Data processing agreement
write("dpa", "Data processing agreement",
      f"How {COMPANY} (the “processor”) handles personal data for the organisations that use its products (each a “controller”), as UK GDPR Article 28 requires. It forms part of our <a class=\"text-ink-primary hover:underline\" href=\"/terms/\">terms of service</a>.",
      [
          ("What we process", ul([
              "<strong class=\"font-medium\">Subject matter and purpose:</strong> providing Elements, Pleasant and Aultrum ID to the controller.",
              "<strong class=\"font-medium\">Duration:</strong> while the controller uses our products, and up to 30 days after, to return or delete the data.",
              "<strong class=\"font-medium\">People:</strong> the controller’s staff and carers, its clients and their contacts, and people who call, text or chat with it through Gateway.",
              "<strong class=\"font-medium\">Data:</strong> names, contact details, work records (shifts, timesheets, training and compliance records, pay), Peak points and rewards, and conversation transcripts. Compliance records may include health information or criminal record check results where the controller enters them.",
          ])),
          ("Our obligations", ul([
              "Process the data only on the controller’s documented instructions, which are these terms and the controller’s use of the product, unless the law requires otherwise; we’ll say so if we think an instruction breaks the law.",
              "Make sure everyone who can access the data is bound to keep it confidential.",
              "Keep it secure with appropriate technical and organisational measures (section 3).",
              "Use sub-processors only as set out in section 4.",
              "Help the controller answer people who use their data protection rights, and with security, breach notifications, impact assessments and consultations with the ICO, taking into account what we can reasonably do.",
              "At the end, delete or return the data as the controller chooses, unless the law requires us to keep it.",
              "Give the controller the information needed to show we meet these obligations, and allow reasonable audits on 30 days’ notice, at most once a year unless there has been a breach.",
          ])),
          ("Security measures", ul([
              "Encryption in transit; passwords hashed; secrets kept out of the code.",
              "Access limited by role inside each organisation, and to the staff at Aultrum who need it to run the service.",
              "One-time, expiring links for sign-in emails and invites; signed, expiring links for embedded screens; signed webhooks.",
              "Rate limits on sign-in and public endpoints; account lock-out after repeated failed sign-ins.",
              "An audit log of important actions in each organisation.",
          ])),
          ("Sub-processors", P("The controller authorises us to use these sub-processors. We will give at least 30 days’ notice by email before adding or replacing one, so the controller can object; if we can’t resolve an objection, the controller may end the agreement. Each sub-processor is bound by data protection terms at least as protective as these.") + sub_table()),
          ("International transfers", P("Where data is transferred outside the UK, we rely on the UK International Data Transfer Addendum, the UK Extension to the EU–US Data Privacy Framework, or another safeguard UK law allows.")),
          ("Personal data breaches", P("We will tell the controller without undue delay, and within 48 hours, after becoming aware of a personal data breach affecting their data, with what we know, what we are doing about it, and what they may need to do. We will keep them updated.")),
          ("Contact", P(f"For anything about this agreement, email {MAIL}.")),
      ],
      "The data processing agreement for organisations that use Aultrum Elements, Pleasant and Aultrum ID.")
