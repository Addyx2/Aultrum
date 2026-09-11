# 03 · Compliance — lens on package health

> **Lens:** Is the package operating within its legal and regulatory obligations, with records that could survive an audit?

---

## Definition

Compliance observes whether the legal duties attached to this package — staffing, registration, safety, records, and reporting — are met and provable. It is the lens that answers: *if inspected today, would this package pass?*

---

## Legal framework(s)

> *[Placeholder — insert exact regulators, statutes, and duties.]*

Sketch of the basis:
- Care Quality Commission (CQC) regulated activity duties: staffing, training, safeguarding, notification, records.
- Data protection duties (UK GDPR / Data Protection Act) for the personal and special-category data the package holds.
- Duty of candour and safeguarding reporting obligations.
- Health and safety duties for staff and receivers.

---

## Psychological framework(s)

> *[Placeholder — insert the human factors referenced.]*

Sketch of the basis:
- Psychological safety of staff: a compliant environment is one where staff can report without fear — compliance failures hide where psychological safety is absent.
- Risk perception and normalization: "it has always been done this way" — normalization of deviance as a driver of drift.
- Trust calibration: receivers and families trust the agency, and that trust is a function of what the agency visibly does about obligations.

---

## Yardsticks (observables)

| # | Yardstick | Observable | Level |
|---|-----------|-----------|-------|
| E1 | Registration currency | CQC/registration status valid & current | L1 |
| E2 | Record completeness | Required records present, current, complete | L2 |
| E3 | Safeguarding reporting | Notifications sent within required windows | L2 |
| E4 | Training compliance | Statutory training current across team | L2 |
| E5 | DBS/right-to-work status | Screening valid and verified | L1 |
| E6 | Audit survivability | Sample records would pass a mock inspection | L3 |

---

## Mathematical grading model

> Working model — refine with the research base.

```
Compliance qualifier = base − Σ (violations × severity × duration)

  severity  = statutory weight of the unmet obligation
  duration  = how long the obligation has been unmet (time-aware)
  detection = whether it is self-found vs. found by inspection (self-found is lighter)
  audit risk = probability the gap is exposed in an inspection
```

Compliance decays with **time of unmet obligation** — an old gap is heavier than a fresh one. This is the temporal dimension of the lens.

---

## Persona Intelligence inputs

- Regulatory events, notifications, inspection correspondence.
- Record gaps and the time they remained open.
- Internal audits and self-assessments vs. external findings.
- The engine learns: *which gaps actually precede enforcement, audit failure, or harm* — weighting static rules with observed consequence.

---

## Example readout

```
COMPLIANCE // package: jordan-adeyemi
- registration: current (no flags)
- record completeness: 94% — 2 of 5 stars missing medication logs
- safeguarding: 1 notification within window, on time
- training compliance: 88% (carer A statutory training overdue)
- DBS/right-to-work: all verified
- audit risk: MEDIUM — medication log gap open 9 days
- compliance score: 0.83/1.00 → RECOMMEND: close medication log gap within 72h
```