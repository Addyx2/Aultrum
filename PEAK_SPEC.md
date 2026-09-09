# Flowstate Peak — Caregiver Recognition & Rewards Engine

## 1. Product Summary

**Peak** is Flowstate's recognition and rewards engine for social care workers. Agencies give carers a points account: points are earned for working shifts, on-time arrivals, client praise, training, and longevity — then cashed out as real money or spent on benefits and financial perks.

**Peak is intentionally light.** It replaces Honor inside Flowstate and deliberately **excludes the HR-heavy core** — no CVs, no references, no compliance paperwork. It is a loyalty/rewards engine, not an HR system. That exclusion is the moat: it removes the compliance surface, the data burden, and the build cost.

**Positioning:** The fastest-to-ship product in the Flowstate ecosystem. Retail-grade incentives logic, Stripe-grade payments rails, and a perks marketplace. Agencies deploy it in days to lift carer retention, attendance, and morale.

**Honor relationship:** Honor becomes a standalone Aultrum product (carer-facing, alongside Flowstate at the company level). Honor **integrates Peak as its incentive feature** — when a carer uses Honor, Peak powers the earn-and-redeem experience.

**Naming:** Peak = the phase where a carer is recognised, rewarded, and at their best.

---

## 2. Why This Product Wins

1. **No compliance constraint** — no health data, no CQC surface, no DCB0129. Retail loyalty logic + payments rails.
2. **Easy build** — a points ledger and a Stripe Issuing integration. Weeks, not months.
3. **Retention economics** — UK social care turnover is ~30%+. A £20–50/month rewards spend per retained carer pays for itself many times over (recruitment costs £2,000–5,000+ per carer).
4. **Fast demo** — agencies *see* the value instantly. Peak is the wedge that opens Flowstate and Gateway conversations.
5. **Cross-sell path** — Peak proves Flowstate, then Gateway handles the calls.

---

## 3. Position in the Ecosystem

```
Aultrum (company)
│
├── Flowstate (agency platform)
│   ├── Gateway    — contact centre (launch product)
│   ├── Peak       — recognition & rewards (this spec) ★
│   ├── Metrics    — dashboards (coming soon)
│   └── Compliance — CQC-ready docs (coming soon)
│
└── Honor (standalone carer product)
    └── integrates Peak as its incentive feature
```

**Peak = the incentive feature wherever it lives.** Inside Flowstate it's a tier. Inside Honor it's the reward engine backing the carer experience.

---

## 4. Mechanics

### 4.1 Earning Points

| Rule | Points | Source |
|------|--------|--------|
| Shift worked | Per-shift base | Rota/Gateway feed |
| On-time arrival | Bonus | Clock-in signal |
| Client praise | Bonus | Client feedback/NPS mention |
| Training completed | Bonus | Training record |
| Monthly perfect attendance | Streak bonus | Attendance calc |
| Longevity (anniversary) | Milestone | Tenure calc |
| Peer nomination | Community bonus | Manager/peer input |

- Agencies configure rule weights per-orbit in the no-code admin.
- Points are **non-expiring** (configurable to expire after 12 months of inactivity).

### 4.2 Cashing Out (Stripe Issuing)

- Points convert to a **virtual/prepaid Stare card** on the carer's phone (tap to pay).
- Value conversion is agency-defined (e.g. 100 points = £1).
- Instant issuance, no signed card in the post.
- Programmable card controls: spend categories, merchant blocks, per-card limits.

### 4.3 Benefits Marketplace (Hybrid Funding)

| Contributor | Provides |
|-------------|----------|
| **Agency** | Funds the cashable value (points → £) |
| **Aultrum** | Negotiates and supplies perks catalog (retail discounts, memberships, financial wellbeing perks) |

- Agency funds the cashable core; Aultrum layers the perks catalog on top at volume.
- Perks are headline items in the marketplace; cash-out is the fallback.

### 4.4 Financial Perks

- Salary advance hooks (funded certifications, shift advances) via downstream partners.
- Vouchers for CPD/training credits.

---

## 5. Architecture

### 5.1 Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| App | Web + mobile-first (Honor integration point) | Carer points portal |
| API | Fastify (same as Gateway) | Ledger + rules API |
| Ledger | PostgreSQL (double-entry) | Points, conversions, cash-outs |
| Issuing | Stripe Issuing | Virtual card issuance & spend |
| Marketplace | Catalog service + partner APIs | Perks assets, redemptions |
| Admin | No-code configuration | Rule weights, value, caps |
| Auth | Clerk / Auth0 | Agency & carer identity |

### 5.2 Data Model (Core)

```
agencies
  id, name, points_value_pence, perks_enabled

carers
  id, agency_id, active, joined_at

points_ledger
  id, carer_id, delta, balance_after, type (earn|redeem|cashout), rule, ref, created_at

incentives_rules
  id, agency_id, rule_key, points, enabled

redemptions
  id, carer_id, points, pence, kind (perk|card_deposit|advance), state, stripe_ref

perks
  id, sku, title, cost_pence, partner, redemption_url
```

The ledger is **double-entry**: every points movement writes a credit and debit row, so the balance can always be reconciled against Stripe settlements.

---

## 6. Unit Economics

### 6.1 Cost Per Carer-Month (facility)

| Component | Cost |
|-----------|------|
| Stripe Issuing issuance | £0.00–0.20 |
| Card load (only when cashed) | £0.50 per load est. |
| Points ledger + infra (amortised) | £0.10 |
| Perks catalog COGS (Aultrum volume deals) | ~0–5% of perk value |
| **Cost to run** | **~£0.20–1.00/carer/mo** |

### 6.2 Pricing Model (SaaS tiers)

| Tier | Carens incl. | Price | Per extra carer |
|------|--------------|-------|-----------------|
| Starter | 10 | £49/mo | £2 |
| Growth | 50 | £149/mo | £1.50 |
| Scale | 500 | £499/mo | £1 |

**Margin:** Platform fees are mostly gross profit; agency funds the *points value* itself (a pass-through cost to the agency, not Aultrum). Aultrum earns on SaaS + perks margins.

### 6.3 Retention Math (Agency Pitch)

- Median cost to replace a carer: £2,000–£5,000 (recr., training, gaps).
- Peak spend per carer: ~£20/mo agency (funded points) + £1–2 SaaS.
- If Peak holds just **1 in 20 carers per year** who would otherwise leave: £2,000+ saved vs ~£300 spent.

---

## 7. Compliance & Data

**Intentionally outside the clinical/compliance surface:**

| Dimension | Peak position |
|-----------|---------------|
| CQC | Not applicable — no care documentation, no clinical risk |
| DCB0129 | Not applicable — no patient-safety decision making |
| Health data | None stored — points are activity/completion records |
| GDPR | Standard — carer PII only (name, email, bank/card details via Stripe) |
| Payments | PCI via Stripe Issuing (outsourced compliance) |

This is the build-fastest wedge: **no regulator in the loop**.

---

## 8. No-Code Admin

- **Rules engine:** configure point values per rule, enable/disable, set caps.
- **Points value:** define £ per 100 points.
- **Catalog:** toggle perks in/out, add partner redemptions, set per-perk cost.
- **Card controls:** spend limits, merchant categories, freeze a card.
- **Analytics:** points issued, redemption rate, retention lift, cost per carer.

---

## 9. Two-Week Build Plan

| Day | Task |
|-----|------|
| 1–2 | Ledger schema (double-entry) + Fastify API skeleton |
| 3 | Agency admin: rules config + points value |
| 4–5 | Carer points portal: balance, earn history, redeem UI |
| 6 | Stripe Issuing: card issuance + load-from-points flow |
| 7 | Perks catalog stub: first 20 perks, redemption links |
| 8 | Honor integration seam: exposed incentive APIs |
| 9 | Auth + invite flow (agency → carer) |
| 10 | Demo build: seeded agency, rules, cards live in test mode |

### Phase 2 (Weeks 3–6)

- Real perks partner agreements (volume catalogue).
- Salary-advance partner integration.
- Attendance/clock-in data connectors (rota systems).
- Full reporting + retention cohort dashboard.

---

## 10. Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Fraud (points farming) | Medium | Per-carer earn caps, anomaly rules, ledger reconciliation |
| Agency doesn't fund points | High | Emphasise single-annual-budget funding; starter tier constrains value |
| Low engagement | Medium | Streak bonuses, client-praise moments, tenure milestones |
| Stripe Issuing availability (UK) | Medium | Evaluate Payoneer/commercial card fallback |
| Partner perks underdeliver | Low | Cash-out is always the fallback; perks are enhancement |

---

## 11. Success Metrics (First 90 Days)

| Metric | Target |
|--------|--------|
| Pilot agencies | 3–5 |
| Active carers | 150+ |
| Monthly engagement (points viewed/earned) | >70% of active carers |
| Points redemption rate | >40% |
| Card activation rate | >60% |
| Retention lift vs baseline | measurable cohort delta |

---

## 12. Naming & Brand

- **Peak** — a carer's best phase; the reward moment; the height of recognition.
- Tagline candidates:
  - "Reward the ones who care."
  - "Recognition that pays."
  - "The incentive standard for social care."
- Colour system: sky blue primary, cloud white/grey support (matches Aultrum rebrand).

---

## 13. File Map

```
flowstatebeta/peak/index.html   — landing/pitch page (public/flowstatebeta/peak/)
PEAK_SPEC.md                    — this document
components/footer.html          — footer already references Products: Peak
```

**Next build step:** launch page at `/flowstatebeta/peak/` (or `/flowstatebeta/peak.html`) + ecosystem grid card on the Flowstate beta landing page.