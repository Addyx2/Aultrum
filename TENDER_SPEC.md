# Tender — Discharge-to-Assess Matching & Collaboration

> **Status:** Standing spec · Sep 2026 · Awaiting build signal
> **Name:** Tender (discharge to care — the tender handover of a receiver to a provider)
> **Positioning line:** *The discharge to the right provider, matched on the capability to care.*

---

## 1. What Tender is

Tender is the NHS-facing product that discharges care receivers from hospital to care providers **safely, fast, and matched to capability**.

It is the collaboration layer between:
- **Clinicians** (who decide discharge and need a capable, available destination)
- **Social care coordinators** (who plan and broker the care package)
- **Providers** (who will actually deliver — and whose capability is measured)

**It is NOT a clinical system.** No clinical practice happens inside Tender. Clinical decisions, medication reconciliation, diagnosis, and treatment remain entirely in the clinician's domain. Tender enables the **flow around clinical care** — refer, match, appoint, record handover, and hand the receiver into a provider's Flowstate package.

---

## 2. Scope — the hard line

### What Tender does do

| Area | What it does |
|------|--------------|
| **Referral & discharge request** | Clinician submits a receiver for discharge with a needs profile + discharge date |
| **Matching** | Matches receiver to provider on capability, availability, continuity, and prior outcomes (qualifier engine) |
| **Appointment** | Coordinates joint visits, assessment slots, and handover meetings across health and social care |
| **Record** | Social-care-domain record: referral, assessment outcomes, care plan handover, progress — with full audit trail |
| **Collaboration** | Tasks, messages, and statuses between clinician, coordinator, and provider |
| **Package handover** | On placement, the receiver becomes a package inside the provider's Flowstate, lenses attached |

### What Tender does NOT do

| Area | Why it's excluded |
|------|-------------------|
| Medication reconciliation | Clinical practice — stays with clinician |
| Diagnosis / treatment decisions | Clinical practice — stays with clinician |
| Clinical documentation of patient care | Out of scope — record is the social-care domain |
| Point-of-care clinical safety decisions | Avoids clinical-safety (DCB0129) classification — Tender does not drive or record care decisions |

This line is deliberate: it keeps Tender a **collaboration and matching product**, not a clinical system — simpler compliance, clearer procurement, and it complements rather than competes with NHS EPR systems.

---

## 3. Users

| User | Role in Tender | What they see |
|------|----------------|---------------|
| **Clinician** (hospital / discharge team) | Refers the receiver; sets discharge constraints | Referral form, provider match view, appointment status, handover record |
| **Social care coordinator** (LA / ICB) | Brokers the placement | All referrals, matching, appointments, provider network health |
| **Provider coordinator** (Flowstate) | Accepts and commits capacity | Matching offers, capability profile, accepts → package opens |
| **Receiver & key persons** (through the care relationship) | Informed, consenting | Timeline, handover summary, who will care for them |

---

## 4. Core flows

### 4.1 Refer → Match → Appoint → Record → Package

```
CLINICIAN (Tender)
  └─ submits referral: needs profile + discharge window + constraints
        │
        ▼
ENGINE (shared qualifier engine)
  └─ matches provider network on:
       Competence  — capability vs. receiver needs (coverage ratio)
       Readiness   — available, non-fatigued capacity for the window
       Rapport     — prior outcomes + continuity with this receiver type
       Compliance  — registration + audit standing
        │
        ▼
PROVIDER (Flowstate)
  └─ receives match offer → accepts capacity → commits a slot
        │
        ▼
APPOINTMENT (Tender)
  └─ joint assessment / handover meeting coordinated across health & social care
        │
        ▼
RECORD (Tender)
  └─ assessment outcome + care plan handover recorded (social-care domain)
        │
        ▼
PACKAGE (Flowstate)
  └─ receiver becomes a package; lenses attach; care begins
```

### 4.2 Appointment collaboration

- Joint visit booking between clinical and social care teams.
- Slot coordination across provider availability windows.
- Handover meeting scheduling with digest records.
- No clinical decisions taken in Tender — the appointment is a *collaboration event*, documented in the social-care record.

### 4.3 Record collaboration

- Referral record (source: clinician, structured).
- Assessment outcomes and agreed care plan (social care domain).
- Progress and handover notes visible to provider + coordinator.
- Change log + consent/audit trail.
- Clinicians' clinical notes are never stored or authored here.

---

## 5. Where the engine fits

Tender is the **second product surface** on the Persona Intelligence engine — the first being Flowstate.

```
Persona Intelligence engine (qualifiers, yardsticks, persona learning)
   ├── Flowstate   → agency operations: Peak, Coordination, Billing, Contracts
   └── Tender      → discharge matching + clinician↔social-care collaboration
```

One engine, two surfaces. The matching intelligence is identical in both: *"which capability, matched to a receiver's needs, delivers quality consistently?"* — in Flowstate it matches carers to a receiver in a package; in Tender it matches a provider to a receiver at discharge.

---

## 6. Commercial & go-to-market

### The market-maker move

Tender is where Aultrum stops being a tool vendor and becomes a **market-maker**: the matching layer between hospital supply and provider capacity. Its market power rises with the provider network on Flowstate — every live package makes Tender's match better and faster.

### Entry route (partner-led)

1. **Partner with CQC-registered homecare providers** (Tender carries the matching engine; the partner carries delivery compliance).
2. **SBRI Healthcare / innovation frameworks** for the first NHS money (no turnover threshold).
3. **G-Cloud / NHS SBS / HealthTrust Europe** to appear in commissioning without a giant tender win.
4. **Pilot with one ICB** — one live discharge route ("hospital→provider via Tender") is the reference every future trust wants.

### Unit economics

| Side | Revenue model |
|------|---------------|
| NHS / ICB / LA | Licenced placement fee per matched discharge (per-placement) or annual collaboration licence |
| Providers (Flowstate) | Standard platform licence + placement value |
| Both | The network data (outcomes, capability, continuity) is the compounding asset |

### Compliance checklist (no clinical practice)

- [ ] DSPT (Data Security and Protection Toolkit) — mandatory for NHS data
- [ ] UK GDPR — social-care-domain data handling, lawful bases, minimum dataset
- [ ] ISO 27001 / Cyber Essentials Plus on the route to production
- [ ] No DCB0129 claim needed (no clinical-safety decision-making in product) — document the line
- [ ] Data sharing framework agreement aligned to the ICB's arrangements
- [ ] Audit trail + consent records on all referrals and handovers

---

## 7. Relationship to the roadmap

| Phase | Date | Focus |
|-------|------|-------|
| **Peak launch** | Sep–Nov 2026 | Live providers → the matching network Tender needs |
| **Gateway launch** | Dec 2026 | Access layer; discharge calls become referrals in Tender |
| **Tender build** | 2027 (flag) | First product surface on the engine for the NHS |

Tender does not move the December plan — but it gives the December plan its long-tail story: one NHS contract on Tender lifts Aultrum from agency platform to care market-maker.

---

## 8. Success criteria (when Tender is live)

- Average discharge-to-placement days reduced vs. local baseline for matched routes.
- Provider match rate: % of referrals successfully matched on first offer.
- Appointment no-show / re-coordination rate below local baseline.
- One ICB reference deployment: named trust, named provider network, sustainable route.
- Audit-clean records: 100% of handovers with consent + audit trail.