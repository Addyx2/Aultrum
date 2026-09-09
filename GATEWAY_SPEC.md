# Flowstate Gateway — Engineering & Commercial Blueprint

## 1. Product Summary

**Gateway** is Flowstate's always-on contact centre for social care agencies. It answers inbound calls, qualifies enquiries, books assessments, takes payments, and logs every interaction directly into the client's CRM.

**Positioning:** The first AI-native contact centre built specifically for UK social care. Gateway replaces after-hours gaps, reduces manual inbound handling costs, and creates a single source of truth for every client interaction.

**Launch scope:** CX for enquiry only — qualifies callers, makes services clear, books the assessment into the sales funnel. Gateway does **not** extend to in-house care delivery operations. Coordination is a separate future capability.

---

## 2. Architecture

### 2.1 Call Flow

```
Inbound Call (Twilio/Telnyx)
    │
    ├─► STT (Deepgram Nova-2 / Whisper)
    │       │
    │       ▼
    ├─► LLM (GPT-4o-mini / Llama via LiteLLM)
    │       │
    │       ├─► Intent Classification
    │       │       ├─► Enquiry qualification
    │       │       ├─► Book assessment
    │       │       ├─► Take payment
    │       │       ├─► Log interaction
    │       │       └─► Escalate to Personnel
    │       │
    │       └─► Response Generation
    │               │
    │               ▼
    ├─► TTS (Fish Audio / ElevenLabs)
    │       │
    │       ▼
    └─► Audio Stream → Caller
```

### 2.2 Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Telephony | Twilio / Telnyx | SIP trunking, +44 number provisioning, call routing |
| STT | Deepgram Nova-2 / OpenAI Whisper | Real-time speech-to-text |
| LLM | GPT-4o-mini / Llama 3 (via LiteLLM) | Intent classification, response generation |
| TTS | Fish Audio / ElevenLabs | Natural voice synthesis |
| Routing | LiteLLM / OpenRouter | Model routing, BYOK, failover |
| Storage | PostgreSQL | Call logs, CRM data, audit trails |
| Cache | Redis | Session state, rate limiting |
| Metering | ClickHouse | Usage tracking, billing metrics |
| Billing | Stripe | Subscription management, usage-based billing |

### 2.3 Why Build, Not Buy

| | Custom Pipeline | Off-the-Shelf (Retell/Vapi/OpenAI Realtime) |
|---|---|---|
| Cost per call | $0.15–0.25 | $0.80–2.40 |
| Voice quality | Customizable (Fish Audio) | Limited to vendor voices |
| Data residency | Full control (UK `eu-west-2`) | Vendor-dependent |
| CRM integration | Native, real-time | Webhook-based, delayed |
| Compliance | CQC audit trails, GDPR | Limited audit capabilities |
| Lock-in | None | High |

**5–10× cost advantage** at scale. At 10,000 calls/month, custom saves $5,500–21,500/month vs off-the-shelf.

---

## 3. Features

### 3.1 Live Call

Real-time transcript displayed as the call progresses. Shows speaker labels, timestamps, and intent detection. Personnel can monitor and step in at any time.

### 3.2 Logs

Every call is logged with:
- Full transcript (anonymised for training data)
- Intent classification (enquiry, booking, payment, escalation)
- Sentiment analysis
- Duration, cost, and model usage
- CRM write status (success/failure/retry)

### 3.3 Abilities

Abilities are modular capabilities that Gateway activates during calls:

| Ability | Status | Description |
|---------|--------|-------------|
| **Default** | Always ON | Answer, understand, route |
| **Payments** | Optional | Collect card/deposit during call (PCI-safe) |
| **Book Assessment** | Optional | Book first care assessment into CRM funnel |

### 3.4 Personnel

Human-in-the-loop mechanism within Gateway:

- **Alert** — notify a team member (push/SMS) when Gateway detects a complex enquiry
- **Inform** — log a summary for later review without interrupting the call
- **Take Over** — warm transfer to a live agent when the caller requests a human

Personnel pairs with Abilities: when booking, payment, or a complex case needs a human, Gateway hands to Personnel.

### 3.5 Coming Soon

- **Compliance** — CQC-ready documentation and audit trails
- **Metrics** — Real-time dashboards and conversion tracking
- **Runners** — Field agent coordination

---

## 4. Unit Economics

### 4.1 Per-Call Cost Breakdown (Custom Pipeline)

| Component | Cost per Call |
|-----------|--------------|
| Telephony (Twilio, ~2min avg) | $0.02–0.04 |
| STT (Deepgram Nova-2) | $0.01–0.02 |
| LLM (GPT-4o-mini, ~800 tokens) | $0.001–0.003 |
| TTS (Fish Audio, ~600 chars) | $0.005–0.01 |
| **Total** | **$0.04–0.07** |

### 4.2 Blended Cost (with overhead)

| Component | Cost per Call |
|-----------|--------------|
| Direct costs | $0.04–0.07 |
| Infrastructure (Redis, Postgres, ClickHouse) | $0.01–0.02 |
| Monitoring & logging | $0.005–0.01 |
| Failover/retry overhead | $0.005–0.01 |
| **Blended total** | **$0.06–0.11** |

### 4.3 Pricing Model

| Tier | Calls/month | Price | Per-Call |
|------|------------|-------|----------|
| Starter | Up to 500 | £299/mo | £0.60 |
| Growth | Up to 2,000 | £899/mo | £0.45 |
| Enterprise | Unlimited | £2,499/mo | £0.25 avg |

**Margin at Starter tier:** £0.60 revenue vs £0.08 cost = **87% gross margin**
**Margin at Enterprise tier:** £0.25 revenue vs £0.08 cost = **68% gross margin**

---

## 5. UK Compliance (Non-Negotiable)

### 5.1 CQC (Care Quality Commission)

- Full audit trail of every AI interaction
- Call recordings stored for 8 years (regulatory requirement)
- Ability to demonstrate AI decision-making process
- Human escalation paths documented

### 5.2 UK GDPR

- Data residency: `eu-west-2` (London) — all data stays in UK
- Right to erasure: automated PII redaction on request
- Data minimisation: only collect what's needed for care delivery
- Privacy impact assessment completed before launch

### 5.3 NHS DSP Toolkit

- Data Security and Protection Toolkit compliance
- Annual self-assessment completed
- Staff training records maintained
- Incident reporting procedures in place

### 5.4 DCB0129

- Clinical risk management for AI-assisted decisions
- Risk assessment documented for each AI capability
- Clinical safety officer appointed
- Post-market surveillance plan

### 5.5 Telephony

- +44 number provisioning via Twilio/Telnyx
- 999/111 emergency escalation (hard-coded, never blocked)
- Call recording consent (verbal consent at start of call)
- Ofcom compliance for outbound calling

---

## 6. No-Code Admin

### 6.1 Models

- Select LLM per use case (GPT-4o-mini for CX, Llama for compliance)
- Select TTS voice per persona (Fish Audio custom voices)
- A/B test model performance
- Version control for prompts

### 6.2 Per-Call Limits

- Hard caps: maximum call duration, maximum tokens per call
- Soft caps: warn when approaching limits
- Role-based limits (different limits for different agent types)
- Emergency override for 999/111 calls

### 6.3 Billing

- Live usage meters (ClickHouse)
- Stripe integration for subscription management
- Usage-based billing with overage charges
- Invoice generation and export

### 6.4 Data Privacy

- Zero-day retention (ZDR) mode for sensitive calls
- PII/PHI redaction in transcripts
- UK data residency enforcement
- Consent management dashboard

---

## 7. Two-Week Build Plan

### Week 1: Core Pipeline

| Day | Task |
|-----|------|
| 1–2 | Twilio/Telnyx SIP trunk setup, +44 number provisioning |
| 2–3 | Deepgram Nova-2 STT integration, real-time streaming |
| 3–4 | LiteLLM routing, GPT-4o-mini intent classification |
| 4–5 | Fish Audio TTS integration, voice selection |
| 5 | End-to-end call flow testing |

### Week 2: Features + Compliance

| Day | Task |
|-----|------|
| 6–7 | CRM integration (webhook + REST API) |
| 7–8 | Abilities framework (Default, Payments, Book Assessment) |
| 8–9 | Personnel alerting (push/SMS/warm transfer) |
| 9–10 | Audit trail, call recording, GDPR compliance |
| 10 | Load testing, failover testing, production deployment |

### Post-Launch (Weeks 3–4)

- CQC compliance documentation
- NHS DSP Toolkit self-assessment
- Client onboarding flow
- Monitoring dashboards
- Billing integration (Stripe)

---

## 8. Risk Register

| Risk | Impact | Mitigation |
|------|--------|-----------|
| STT accuracy on accents | High | Deepgram Nova-2 UK English model + fallback to Whisper |
| LLM hallucination on care advice | Critical | Hard guardrails: Gateway never gives medical advice, always escalates |
| 999/111 blocking | Critical | Hard-coded emergency detection, immediate transfer, never logged |
| CRM integration failures | Medium | Retry queue, dead letter handling, manual sync fallback |
| Cost overruns at scale | Medium | Per-call limits, usage alerts, model fallback to cheaper options |
| Data breach | Critical | Encryption at rest + in transit, UK residency, minimal data collection |

---

## 9. Success Metrics (First 90 Days)

| Metric | Target |
|--------|--------|
| Calls handled | 5,000+ |
| Enquiry-to-assessment conversion | >35% |
| Average call duration | <3 minutes |
| CRM write success rate | >99% |
| Uptime | >99.9% |
| Client NPS | >50 |
| Cost per call | <£0.10 |

---

## 10. Future Roadmap

| Phase | Timeline | Capabilities |
|-------|----------|-------------|
| **Phase 1: CX** | Now | Enquiry qualification, assessment booking, payment collection |
| **Phase 2: Coordination** | Q2 2026 | Shift scheduling, carer matching, visit coordination |
| **Phase 3: Compliance** | Q3 2026 | Automated documentation, CQC audit trails, risk scoring |
| **Phase 4: Intelligence** | Q4 2026 | Predictive analytics, demand forecasting, outcome tracking |

**Note:** Coordination (Phase 2) is a separate capability from CX (Phase 1). Gateway's current scope is explicitly CX for enquiry only. Coordination will be built as a distinct module within Flowstate, not as an extension of Gateway's contact centre.
