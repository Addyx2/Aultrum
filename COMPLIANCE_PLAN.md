# Aultrum Compliance Plan — Roles & Roll-Out for Gateway

> Version: 1.0 · Sep 2026 · Owner: Flowstate (Aultrum)
> Applies to: Flowstate Platform, Peak, **Gateway**, Tender (when live)
> Sequencing: aligned to `ROADMAP.md` — Gateway launch **Dec 2026**, compliance land-grab during P5.

---

## 1. Objective

Put every compliance role, owner, evidence artefact, and timing in one place so compliance can be **set rolling now** and be launch-ready for Gateway in December — without burning runway early.

Two distinct sets of roles are covered:

1. **Company roles** — the named individuals/accountabilities Aultrum must have (or contract) to operate lawfully and to sell to care providers.
2. **Product roles (RBAC)** — the roles *inside* Flowstate/Gateway that control who can see, do, and approve compliance-relevant activity.

---

## 2. What Aultrum is — and is not

This matters because it defines which roles Aultrum *owns* and which belong to **clients**.

| Question | Answer | Implication |
|----------|--------|-------------|
| Is Aultrum a CQC-registered care provider? | No | Aultrum has no CQC `Responsible Individual`; client agencies do. Aultrum must *support* client CQC compliance, not carry it. |
| Does Aultrum process NHS/social-care data? | Yes, for Gateway (calls, enquiries, assessments) | DSPT applies for NHS data access; UK GDPR processing rules apply regardless. |
| Does Gateway make clinical safety-critical decisions? | No clinical practice, but AI-assisted interaction | DCB0129 risk management applies proportionately; a Clinical Safety Officer role is required. |
| Does Aultrum hold payment/financial data? | Via Stripe only (Peak) | PCI scope outsourced to Stripe — no in-house PCI roles. |

**Net:** Aultrum owns **5 mandatory roles** (below); everything else is contract + supporting evidence.

---

## 3. Company Roles (Aultrum's accountability)

| # | Role | Regulation / Basis | Core responsibilities | Evidence artefact | When in place |
|---|------|--------------------|-----------------------|-------------------|---------------|
| R1 | **Data Protection Officer (DPO)** | UK GDPR Art. 37; ICO registration | Oversee GDPR, DSARs, breach handling (72h), processor agreements, retention | ICO registration number; DPIA register; breach log | **Now** (can be contracted part-time) |
| R2 | **Clinical Safety Officer (CSO)** | DCB0129 / DCB0160 | Own the safety case for Gateway's AI pipelines; hazard log; sign-off before launch | Safety case file + hazard log | **By Nov 2026** (contract or qualified individual) |
| R3 | **Senior Information Risk Owner (SIRO)** | NHS DSP Toolkit | Own organisational risk to information; approve DSPT self-assessment | Named person; DSPT submission | **By Nov 2026** |
| R4 | **Security / IG Lead (CISO-ish)** | DSPT, UK GDPR Art. 32 | Controls, encryption, IR plan, staff training, supply-chain security | Risk register; incident response plan; training records | **Oct 2026** |
| R5 | **AI / Model Risk Owner** | GATEWAY_SPEC §5; responsible AI | Own guardrails (no medical advice, 999/111), model eval, prompt versioning, hallucination controls | AI risk register; model change log | **Nov 2026** (can fold into CSO) |

### Optional / project-stage roles (record when triggered)

| Role | Regulation | Trigger |
|------|-----------|---------|
| Caldicott Guardian | NHS data governance | Only if Aultrum becomes an NHS processor holding identifiable patient data via Tender — not needed for Gateway v1 |
| CQC Responsible Individual | HSCA 2008 | Only if Aultrum ever registers as a provider (not planned) |
| Ofcom Communications lead | PECR / Ofcom | Owns outbound-call consent + number porting rules for Gateway's Telephony ability |
| Supplier / Data Processor reviewer | UK GDPR Art. 28 | Every vendor onboarding (Twilio, Deepgram, AI providers, Stripe, Tango) |

> **Rule:** For pre-seed stage, R1 can be a contracted DPO service and R2–R4 can be one named founder + one advisor. What matters is that **each regulation has a named accountable human** — not a job title, an addressable person.

---

## 4. Product Roles (RBAC inside Flowstate / Gateway)

These extend the roles already defined in `FLOWSTATE_PRODUCT_BRIEF.md` (§3.1 Directory roles) with a compliance view.

| Product role | Scope | Can see | Can do | Default for |
|--------------|-------|---------|--------|-------------|
| Platform Admin | Account-level | Everything incl. audit logs | Manage team, integrations, billing | Agency owner |
| Coordinator | Package-level | Package people, records, Peak channels | Create packages, add members, toggle channels | Care coordinator |
| **Compliance Auditor** *(new)* | Read-only, account-wide | Audit trails, call logs/recordings, inspection reports, compliance score | Export evidence, run reports; **no edits, no deletes** | Internal/external auditor, DPO |
| **IG / Compliance Manager** *(new)* | Account-wide | All compliance data + settings | Approve redactions, set retention, manage consent, run mock inspections | Designated staff |
| Gateway Monitor (Personnel) | Account | Live calls, transcripts, escalation queue | Steal the call, take over, escalate | Agency contact-centre lead |
| Carer | Own profile + Peak | Own badges, points, card, rota access | Redeem, toggle, view own recognition | Care worker |
| Care Receiver / Key Person | Own profile only | Own record, not staff data | Submit feedback/praise | Receiver / family |

### Mandatory RBAC rules (build into gateway/flowstate-api)

1. **Audit roles are read-only by construction** — cannot be mutated by any UI or API route.
2. **Consent & retention** toggles sit behind `IG / Compliance Manager` only.
3. **Call recording access** requires `Compliance Auditor` or above; recordings stored 8 years (CQC), surfaced only in the compliance surface.
4. **ZDR (zero-day retention) mode** — one toggle that prevents any persistence of a call (see GATEWAY_SPEC §6.4); restricted to `IG / Compliance Manager`.
5. Every compliance-relevant action is itself **audited** (who did what, when) — validator of R1.

---

## 5. Ownership Grid — "who answers on the day of inspection / ICO / DCB review"

| Question a regulator asks | Owning role | Document to hand over |
|---------------------------|-------------|------------------------|
| Who owns data protection? | R1 DPO | DPIA, RoPA, ICO registration, breach log |
| How do we know Gateway is safe? | R2 CSO | Safety case, hazard log, test evidence |
| Who owns information risk? | R3 SIRO | DSPT submission, named person |
| How do you keep data secure? | R4 Security/IG | IR plan, encryption spec, training records |
| How do you stop the AI doing harm? | R5 Model Risk | AI risk register, guardrail tests, prompt history |
| Who sees what in the product? | Product RBAC (§4) | Role matrix + enforced in code |

---

## 6. Roll-Out Timeline ("set rolling")

| Window | Actions | Owner |
|--------|---------|-------|
| **Sep 2026 — now** | ICO registration (data protection fee); appoint DPO (contract ok); draft Records of Processing + DPIA skeleton; start AI risk register | Founder + DPO |
| **Oct 2026** | Name SIRO + Security lead; security baseline (MFA, encryption at rest/in transit, IR plan); vendor Art. 28 reviews (Twilio, Deepgram, LLM provider, Stripe, Fish/TTS) | Security lead |
| **Nov 2026 (P4/P5)** | Appoint/contract **Clinical Safety Officer**; complete Gateway safety case + hazard log; design consent script + recording retention; DSPT self-assessment drafted; RBAC implemented (Compliance Auditor + IG roles in code) | CSO + SIRO |
| **Dec 2026 (P6 gate)** | DPIA signed off; DCB safety case approved; DSPT submitted; CQC evidence pack + audit trail verified; **GO / NO-GO demands all five roles named + artefacts complete** | Founder + all |
| **Q1 2027** | Annual review cycle; compliance lens (Layer 03) live in qualifier engine; post-launch surveillance (post-market plan) | IG lead + CSO |

> **Gate tie-in:** ROADMAP P6 GO/NO-GO adds one line — *"Compliance gate: R1–R5 named, DPIA + safety case + DSPT + audit trail verified."*

---

## 7. Artefact Register (single source of truth)

| Artefact | Format | Owner | Location |
|----------|--------|-------|----------|
| ICO registration | ICO portal | DPO | ICO |
| Records of Processing (RoPA) | Sheet | DPO | Notion/IG folder |
| DPIA (Gateway) | Doc | DPO + Founder | `docs/` or Notion |
| DCB safety case + hazard log | Doc | CSO | `docs/` |
| AI risk register | Sheet | Model Risk/CSO | Notion |
| Incident response plan | Doc | Security | Notion |
| DSPT self-assessment | NHS portal | SIRO | NHS DSPT |
| Training records | Sheet | Security | Notion |
| Vendor Art. 28 register | Sheet | DPO | Notion |
| CQC evidence pack (rolled from product audit trails) | Exportable | Product (audit IIFE) | Flowstate |

---

## 8. Decisions needed from you

1. **DPO** — use a contracted DPO service (≈£500–1k/yr, fast) or keep internal for now? Recommendation: **contract** now, revisit at seed.
2. **CSO** — contract a qualified clinical-safety consultant for a fixed-scope safety case (recommended for Nov) rather than hire.
3. **RBAC ownership** — does the IG / Compliance Manager sit client-side (agency staff) as a standard account role, or is it vendor-only for now? Recommendation: expose to agencies — it's a selling point.
4. **Where artefacts live** — the existing `knowledge-base/` Notion kit, or a repo `docs/compliance/` folder? Recommend repo `docs/` so they version with the code.

---

## 9. What "done" looks like before Gateway ships

- [ ] ICO registration active
- [ ] DPO, SIRO, Security lead, CSO, AI Risk owner **named** (people, not titles)
- [ ] DPIA signed, Rest of RoPA drafted
- [ ] Safety case + hazard log exist and are versioned
- [ ] DSPT self-assessment draft completed
- [ ] RBAC enforced in code (incl. read-only auditor)
- [ ] Consent + 8-year recording retention wired
- [ ] No-crossed-wires with client-side CQC: the client owns the provider inspection; Aultrum owns the software evidence it hands over