# 06 · Satisfaction — lens on package health

> **Lens:** Does the receiver — and the family/key persons — experience the care as good, respectful, and responsive to them as a person?

---

## Definition

Satisfaction observes the experienced quality of care from the receiver's side of the relationship. It is the human-facing verification of the other lenses: Competence may be provable, and Compliance may be passable, but Satisfaction is how it *feels* to the person being cared for.

---

## Legal framework(s)

> *[Placeholder — insert exact references.]*

Sketch of the basis:
- Person-centred care duties — the receiver's view is a regulatory consideration, not an optional extra.
- Complaint/feedback handling duties — channels must exist and be acted upon.
- Dignity and respect obligations transcending clinical measures.

---

## Psychological framework(s)

> *[Placeholder — insert experience/expectation literature referenced.]*

Sketch of the basis:
- Perceived quality diverges from clinical quality — experience is shaped by expectations, control, and dignity.
- Voice and agency: receivers who feel heard report higher satisfaction and better outcomes.
- Family trust is the practical decision-maker — satisfaction of receivers and key persons drives retention of the client relationship.

---

## Yardsticks (observables)

| # | Yardstick | Observable | Level |
|---|-----------|-----------|-------|
| S1 | Response rate | % of receivers/families giving feedback | L1 |
| S2 | Sentiment level | Current satisfaction score (NPS-like or adapted) | L2 |
| S3 | Sentiment trend | Slope of satisfaction over time | L2 |
| S4 | Voice access | Receiver can raise concerns + is heard (channel use) | L2 |
| S5 | Complaint handling | Open complaints resolved within standard | L2 |
| S6 | Experienced quality | Receiver-rated quality of care (not inputs) | L3 |

---

## Mathematical grading model

> Working model — refine with the research base.

```
Satisfaction qualifier = f(response, level, trend) + voice_credit

  level   = current satisfaction score across the package
  trend   = slope over rolling window (increasing > flat > declining)
  response = validity weight: low response → low confidence
  voice   = proportion of raised concerns resolved+ communicated back
```

The qualifier prefers **trend evidence** over a single score — a 7 that is climbing may outrank an 8 that is falling.

---

## Persona Intelligence inputs

- Receiver/family satisfaction replies (time-stamped).
- Praise, complaint, and concern events.
- Retention of the client relationship (did the family stay or leave?).
- The engine learns: *which experiences at which thresholds actually predict family retention* — weighting the judged experience by its real consequence.

---

## Example readout

```
SATISFACTION // package: jordan-adeyemi
- response rate: 82% (confident sample)
- sentiment level: 4.3 / 5
- sentiment trend: +0.4 over 90 days (climbing)
- voice access: 3 concerns raised, 3 resolved, communicated
- complaint handling: 0 open beyond standard
- experienced quality: 4.2 / 5 (receiver-rated)
- satisfaction score: 0.81/1.00 → HEALTHY and improving
```