# 04 · Shift Readiness — lens on package health

> **Lens:** Is each carer fit to deliver today — rested, prepared, and reliable — and is the package ready for the shifts ahead?

---

## Definition

Shift Readiness observes the momentary and near-term fitness of the care team: a carer who has run too many shifts is not ready for the next three, even though they are technically qualified. It is the lens that answers: *can this package cover its immediate future safely?*

---

## Legal framework(s)

> *[Placeholder — insert exact references.]*

Sketch of the basis:
- Working-time limits and rest requirements (UK Working Time Regulations).
- Employer duty of care and safety for staff and receivers.
- Staffing sufficiency obligations — a package's shift plan must be sustainably coverable.

---

## Psychological framework(s)

> *[Placeholder — insert exhaustion/fatigue literature referenced.]*

Sketch of the basis:
- Fatigue accumulation: consecutive shifts without recovery degrade performance, judgement, and empathy.
- Cognitive load under sleep debt — errors rise silently before they are noticed.
- Motivation and withdrawal: overworked carers disengage and leave — fatigue is the leading predictor of unwelcome turnover.

---

## Yardsticks (observables)

| # | Yardstick | Observable | Level |
|---|-----------|-----------|-------|
| R1 | Rest adequacy | Rest hours between consecutive shifts | L1 |
| R2 | Shift load | Shifts in current window vs. safe ceiling | L2 |
| R3 | Fatigue proxy | Consecutive-day streak, cumulative weekly load | L2 |
| R4 | Preparedness | Equipment/info ready before shift (checklist) | L1 |
| R5 | Reliability | Punctuality + last-minute call-off history | L2 |
| R6 | Coverage certainty | Likelihood all near-term shifts are reliably covered | L3 |

---

## Mathematical grading model

> Working model — refine with the research base.

```
Shift Readiness qualifier = f(rest, load) − fatigue_penalty + reliability_credit

  safe ceiling   = max shifts in rolling window (calibrated by persona intelligence)
  rest gap       = hours below recommended rest between shifts
  fatigue signal = carer running at/above ceiling for N consecutive weeks
  reliability    = long-window punctuality + low call-off rate (a stability credit)
```

The core output is **forecast readiness** — readiness for the *next K shifts*, not just today. This is what lets the qualifier say: *"carer is not ready for the next 3 shifts — rotate."*

---

## Persona Intelligence inputs

- Rota and clock-in/clock-out event streams (time-stamped).
- Call-off, substitution, and late-arrival history.
- Performance/incident data correlated with fatigue windows.
- The engine learns: *this carer's safe ceiling, rest tolerance, and true reliability* — replacing population norms with the individual's observed limits.

---

## Example readout

```
SHIFT READINESS // package: jordan-adeyemi
- rest adequacy: carer B 6h between shifts (below floor)
- shift load: carer B 6 of 7 days, at ceiling for 3rd week
- fatigue proxy: consecutive-day streak 9
- preparedness: 100% checklist completion
- reliability: 4 call-offs in 90 days, 1 late
- coverage certainty: MEDIUM
- readiness forecast: carer B NOT READY for next 3 shifts → RECOMMEND: rotate to C, D
```