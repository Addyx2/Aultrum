# Aultrum Roadmap — Peak First, Gateway by December 2026

> Dated: 9 Sep 2026 · Owner: Flowstate (Aultrum)
> Principle: **build the wedge first, gate the flagship on revenue and data.**

## Why Peak First

1. **Zero compliance surface** — no CQC, no GDPR health data, no DCB0129. Ships in weeks.
2. **Entry wedge** — agencies adopt Peak instantly; Gateway becomes an upsell inside an active account, not a cold pitch.
3. **Fast cash flow** — £49–499/mo SaaS, ~90% gross margin, trivial infra. Funds Gateway's heavier engineering.
4. **Data foundation** — Peak's ledger (rota, attendance, streaks, tenure, praise) builds the **Shift Readiness** and **Rapport** qualifiers the Layers engine needs — data Gateway later consumes.

---

## Commitment

**Gateway launches December 2026.** Peak funds + de-risks the runway to get there.

| Phase | Window | Focus | Exit Criteria |
|-------|--------|-------|---------------|
| **P0 — Peak Core** | Sep 2026 | Ledger (double-entry) + Fastify API + agency admin | Points earn/redeem work in test |
| **P1 — Peak Payments** | Sep–Oct 2026 | Stripe Issuing virtual card, load-from-points | Card issued + funded in test mode |
| **P2 — Qualifier Engine** | Oct 2026 | Layer qualifiers: **Shift Readiness + Rapport** first | Rewards gate on measured care quality |
| **P3 — Peak Pilots** | Oct–Nov 2026 | 3–5 agencies, 150+ carers, perks catalog | 90-day target metrics met (see PEAK_SPEC) |
| **P4 — Gateway Build** | Nov 2026 | Contact centre pipeline (Twilio/Deepgram/LiteLLM/Fish) | End-to-end call flow in staging |
| **P5 — Gateway Compliance** | Nov–Dec 2026 | UK GDPR eu-west-2, audit trails, +44, 999/111 | Compliance checklist complete |
| **P6 — GATEWAY LAUNCH** | **Dec 2026** | Production deploy + first paying clients | GO / NO-GO review |

---

## Sequencing Logic

```
Sep   ▸ Peak core (ledger + rules)
Oct   ▸ Peak payments + Qualifier Engine (Shift Readiness, Rapport)
Oct█Nov ▸ Peak pilots → revenue + retention data
Nov   ▸ Gateway build (funded by Peak revenue + pilot LOIs)
Nov█Dec ▸ Gateway compliance + hardening
Dec   ▸ █ GATEWAY LAUNCH █
```

### Dependencies
- **Peak → Gateway:** Peak proves the client relationship + builds qualifier data. Gateway calls feed the same qualifier pipeline post-launch.
- **Qualifier Engine → Gateway:** the Layers IP (Rapport, Shift Readiness) is the shared moat both products surface.
- **Revenue → compliance:** Gateway's compliance work is funded by Peak cash flow; don't burn runway on regulator work before revenue.

### Risk gates
| Gate | Trigger | Action |
|------|---------|--------|
| Pilot count | <2 agencies by 1 Nov | Extend Peak pilots, delay Gateway build 2 weeks |
| Card rail fail | Stripe Issuing unavailable in UK test | Fallback: Payoneer/commercial card eval in P1 |
| Gateway cost blowout | No pilot revenue by mid-Nov | Ship Gateway as LOI-timed prototype, keep December demo milestone |

---

## Role of Aultrum Layers

Rewards in Peak are **gated by measured care quality**, not attendance alone. That makes incentive spend defensible to agencies:

- **Shift Readiness** — on-time, prepared, consistent → first qualifier live
- **Rapport** — client NPS + praise signals → second qualifier live
- **Competence / Compliance / Satisfaction / Purpose** — later phases

This turns Peak from "points for showing up" into **"rewards prove quality"** — the CQC-aligned story, and the proprietary logic competitors can't copy.

---

## What Success Looks Like

### Peak (Oct—Nov)
- 3–5 pilot agencies, 150+ active carers
- 70%+ monthly engagement, >40% points redemption, >60% card activation
- Measurable retention delta vs baseline

### Gateway (Dec)
- Live +44 numbers, real inbound calls, CRM writes in production
- UK GDPR eu-west-2, audit trails, 999/111 escalation verified
- First paying client going live at/after DEMO

---

## Rule of Thumb Going Forward
**Any new product idea gets sequenced against Peak-first + Gateway-December.** If it doesn't fund, de-risk, or accelerate those two commitments, it waits.