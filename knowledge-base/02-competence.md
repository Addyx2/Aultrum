# 02 · Competence — lens on package health

> **Lens:** Is the skill of the care team current, verified, and matched to the receiver's needs?

---

## Definition

Competence observes whether the knowledge and skill required to care for this receiver is present, current, and proven — not assumed. A competent package can demonstrate its ability; an incompetent package can only claim it.

---

## Legal framework(s)

> *[Placeholder — insert the exact statutes, regulations, and duties you reference.]*

Sketch of the basis:
- Obligation that care staff be appropriately trained and competent for the care they deliver (CQC regulation on staffing and training).
- Records of training and verification must be maintainable and auditable.
- Skill decay is a legal-relevant fact: a credential ages, and the right to be relied upon ages with it.

---

## Psychological framework(s)

> *[Placeholder — insert the exact psychological theories/theories of skill you reference.]*

Sketch of the basis:
- Skill retention and decay over time (memory/learning literature) — competence is a decaying function without practice and renewal.
- Confidence vs. competence calibration — perception of ability does not equal measured ability.
- Expertise develops through deliberate practice, not time served.

---

## Yardsticks (observables)

| # | Yardstick | Observable | Level |
|---|-----------|-----------|-------|
| C1 | Training currency | Each required training record within validity window | L1 |
| C2 | Certification status | Valid certs held vs. required certs for the package | L2 |
| C3 | Skill-match | Skill list vs. receiver care-need list (coverage ratio) | L2 |
| C4 | Skill decay | Time since last refresh for each current skill | L2 |
| C5 | Verification gap | % of team with unverified/expired credentials | L2 |
| C6 | Application evidence | Documented successful use of a skill in this package | L3 |

---

## Mathematical grading model

> Working model — refine with the research base.

```
Competence qualifier = Σ over the team of: (currency × relevance × verification)

  currency  = f(validity windows, time since refresh)      → decay-weighted
  relevance = skill overlap with the receiver's care needs
  verification = confirmed record exists and is current
  team gap  = important needs with no competent assigned carer
```

Grading is done **at package level** (the team vs. the receiver's needs), then attributed down to individual carer profiles.

---

## Persona Intelligence inputs

- Training completion and renewal events (time-stamped).
- Recorded care tasks vs. declared skills (does practice match claims?).
- Incident/outcome data correlated with skill gaps (which gaps actually matter?).
- The engine learns: *which skill gap, in which context, has real consequence* — refining the grading weights.

---

## Example readout

```
COMPETENCE // package: jordan-adeyemi
- training currency: 87% (carer A is 3 trainings behind → flag)
- certification status: 2 of 3 certs current
- skill-match: 91% (high-need: PEG management covered)
- skill decay: 2 skills > 24 months since refresh
- verification gap: 1 unverified record
- team gap: 0 uncovered high-severity needs
- competence score: 0.78/1.00 → RECOMMEND: schedule carer A training
```