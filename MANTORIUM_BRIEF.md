# Brief: Mantorium — The Effect of Time on People

> Mantorium Research · Written Sep 2026
> A research brief laying out the founding thesis, research programme, and model architecture for a company that helps computers understand how time shapes human experience — and how that understanding produces freedom from deterrent obligations.

---

## The founding axiom

**Time has its effect on people.**

This is not a metaphor. It is the single most under-examined variable in every system that governs human decision-making: care, employment, finance, health, housing, justice, education. Time passes. People change. Situations evolve. Events recur. Obligations accumulate. And every system that fails to account for time's effect on people ends up punishing them for conditions that no longer exist — or rewarding them for conditions that never did.

Mantorium exists to change that. Not philosophically. Computationally. We build models that understand time's effect on people — and we make that understanding available to the organisations, products, and platforms that serve them.

---

## What "the effect of time" means

Time does not affect people uniformly. Its effects are domain-specific, measurable, and often irreversible:

| Domain | Time's effect | What the system currently does | What it should do |
|--------|--------------|-------------------------------|-------------------|
| **Care work** | A carer's skill decays without training; rapport accumulates through continuity; burnout accrues over shifts | Treats all carers as interchangeable; measures hours, not quality-diminished-over-time | Track skill drift, bond maturity, burnout risk as time-series signals |
| **Employment** | CVs are a static snapshot; experience degrades in relevance; skills expire | Hire on "years of experience" as a proxy; never model skill half-life | Model competence as a time-decaying curve, not a credential |
| **Finance** | Income volatility is temporal; obligations have time-weight; debt accumulates interest over real time | Snapshot income; miss the pattern; penalise volatility that is structurally normal | Model income as a temporal signal; predict cashflow, not just balance |
| **Health** | Conditions change over time; treatment adherence decays; risk is time-weighted | Static assessments; periodic re-evaluation by appointment | Continuous risk surfaces that age with the person |
| **Justice / Compliance** | Risk profiles change; rehabilitation is a time-process; static checks miss improvement | DBS checks freeze a moment; repeat offenders flagged regardless of trajectory | Model risk as a time-decaying curve with verifiable improvement |

The common structure: **every system treats time as a coordinate, not as a variable that changes the person.** Mantorium treats time as the variable itself.

---

## "Deterrent obligations" — the problem Mantorium solves

A *deterrent obligation* is any constraint, requirement, or condition imposed on a person that persists beyond its relevance — or was never relevant to begin with — and acts as a barrier to action, progress, or freedom.

Examples:

- A care worker whose CV says "5 years experience" but whose training expired 2 years ago → the 5 years is a deterrent credential; the expired training is an overlooked deterrent obligation.
- A person rejected for finance because of a debt that was repaid 3 years ago → the historical record is a deterrent obligation; the current reality is invisible.
- A carer not matched to a client because their "years served" doesn't match the client's profile → the static metric deters; the actual competence (which may be superior) is unmeasured.
- A person denied housing because of a compliance flag that no longer applies → the flag persists; the person changed; the system didn't.

**Deterrent obligations are time-frozen judgements applied to people who are no longer time-frozen.** They are the mechanism by which systems that fail to model time's effect on people end up constraining them.

Mantorium's research goal: build models that recognise when an obligation has become deterrent — and produce the signal that would allow a system to release it, replace it, or re-evaluate it.

---

## The research programme

### What we are building

A **temporal modelling engine** — a model trained to understand how people change over time, how situations evolve, and how obligations age. Not a language model. Not a prediction engine. A model whose primary variable is time and whose output is the effect of time on a specific person in a specific context.

### Core research questions

1. **How do human-relevant attributes (skill, competence, risk, wellbeing, trust) decay or accumulate over time?**
   - Skill decay curves by domain (care, finance, health)
   - Rapport accumulation as a time-series (Aultrum's Rapport Layer)
   - Risk trajectory: does it decay, or does it bifurcate?

2. **How do we detect when an obligation has become deterrent?**
   - The "time of relevance" for a given constraint: when was it true, and is it still?
   - Obligation half-life: how long until a recorded constraint should be automatically re-evaluated?
   - The distinction between "still relevant" and "historically true but currently misleading."

3. **How do we model time's effect on a specific person, not a population?**
   - Individual temporal signatures: each person's pattern of change is unique.
   - Population-level models miss the individual trajectory — they tell you what "most people" do, not what this person did.
   - The model must operate on individual longitudinal data, not cross-sectional snapshots.

4. **How does understanding time's effect produce freedom?**
   - If the model can show that a person's current state differs from their historical state, it produces the evidence needed to release a deterrent obligation.
   - Freedom here is not abstract: it is the concrete ability to act (be hired, be matched, be financed, be cared for) without being constrained by time-frozen data.

### What we are NOT building

- Not a general-purpose AI or language model
- Not a "digital twin" (we are not simulating people; we are understanding how time changes them)
- Not a prediction engine (we are not forecasting behaviour; we are modelling the temporal dimension of existing evidence)
- Not a compliance tool (though compliance systems are a client)

---

## Model architecture — working hypothesis

```
TEMPORAL MODELLING ENGINE (v0)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUTS (per person):
  longitudinal event stream (time-stamped actions, assessments, outcomes)
  domain context (care / finance / employment / health)
  obligation registry (current constraints + their origin timestamp)

CORE MODEL:
  individual decay/accumulation curves per attribute
  time-since-relevance scorer for each obligation
  trajectory clustering (improving / stable / declining / bifurcating)

OUTPUTS:
  obligation_age:  [stale | relevant | deterrent]
  person_state:    [current] — modelled, not snapshot
  freedom_signal:  [constrain | release | flag_for_review]
  confidence:      [low | medium | high] — based on data density
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

The engine does not make decisions. It produces signals. The organisations that use it decide what to do with those signals. Aultrum (social care) uses them to match carers to clients based on time-aware competence rather than static CVs. A finance platform uses them to evaluate current income patterns rather than historical snapshots. A compliance system uses them to assess current risk rather than historical records.

---

## How this connects to the brands

Mantorium is the research company. Its models are the engine. The brands are the applications:

| Brand | Application of Mantorium's temporal modelling |
|-------|----------------------------------------------|
| **Aultrum** (social care) | Carer competence decay curves, rapport accumulation, burnout trajectory, qualification half-life → Peak rewards + Gateway call intelligence + Honor carer profile |
| **Future brand** (finance) | Income temporal modelling, obligation half-life, volatility-as-signal → underwriting, credit access |
| **Future brand** (employment) | Skill decay, experience relevance curves, trajectory matching → hiring, career progression |
| **Future brand** (compliance) | Risk trajectory modelling, obligation re-evaluation, rehabilitation-as-time-process → regulatory decisions |

Each brand consumes Mantorium's temporal signals through a domain-specific lens. The core engine is shared. The outputs are specialised.

---

## Why this matters now

Three convergences make this research urgent:

1. **Regulation is moving toward temporal assessment.** CQC is shifting toward continuous monitoring; the EU AI Act requires risk reassessment over time; GDPR's right to erasure is implicitly a temporal claim. Systems that model time will be compliant-by-design.

2. **AI is producing more data, faster — but models still treat people as snapshots.** LLMs can write about time, but they don't model it. Mantorium's temporal engine is a different class of model: not generative, but relational-to-time.

3. **The workforce crisis is a temporal problem.** Skills decay faster than training cycles. Burnout accrues faster than rest. Retention is not a pay problem — it is a time-balance problem. Systems that model this will outperform systems that don't.

---

## Research programme — phase plan

| Phase | Window | Focus | Deliverable |
|-------|--------|-------|-------------|
| **M0 — Foundations** | Sep–Oct 2026 | Skill decay literature review; obligation half-life taxonomy; individual temporal signature formalisation | Mantorium Thesis Paper (v0) |
| **M1 — Aultrum prototype** | Nov 2026 | Temporal model applied to Aultrum's Peak qualifier data (Shift Readiness + Rapport as time-series) | Proof-of-concept: time-aware carer quality signal |
| **M2 — Second domain** | Q1 2027 | Apply temporal model to a second domain (finance or employment) | Cross-domain model validation |
| **M3 — Model publication** | Q2 2027 | Formal paper: Temporal Modelling of Human Attributes — Architecture and Evidence | Peer-reviewed publication; public model architecture |

---

## Success criteria

- The model produces measurable improvement over snapshot-based systems in at least one domain (Aultrum social care) within 90 days of M1.
- The thesis paper is cited in at least one policy or academic context within 12 months.
- The "deterrent obligation" concept enters the vocabulary of at least one regulatory or commissioning body (CQC, ICS, EU AI Act discourse).
- The core engine is demonstrated across at least two distinct domains by end of M2.

---

## Tone

- This is a research company's founding brief, not a pitch deck.
- The tone is precise, specific, and honest about what is known and what is to be tested.
- Mantorium does not claim to have solved time. It claims to have identified a modelling gap that no existing system addresses — and proposes to fill it.
- The language should make a non-technical reader feel the idea is obvious in retrospect, and a technical reader feel it is well-grounded and testable.