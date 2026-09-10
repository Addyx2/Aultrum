# Flowstate — Product & Technical Architecture Brief

> Version: 1.0 · Sep 2026
> Status: Pre-build · Awaiting UI/UX design
> Author: Aultrum / Mantorium Research

---

## 1. Product overview

**Flowstate** is the authenticated product application for Aultrum's social care platform. It is where coordinators manage their care operations, and where carers interact with their rewards and recognition.

- **URL:** `flowstate.aultrum.co.uk`
- **Access:** Authenticated (login required)
- **Marketing site:** `aultrumpro.vercel.app` (separate, public, Vite)

Flowstate has two structural layers:

1. **Platform** — the horizontal foundation (Directory, Package, Integrations, Account)
2. **Products** — vertical modules built on the platform. **Peak** is the first product. Gateway is excluded from production.

---

## 2. Navigation architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│  Flowstate          Directory    Package    Integrations    Account   │
│  (logo/top-left)    ─────────────────────────────────────────────── │
│                     Platform (horizontal menu)                       │
└─────────────────────────────────────────────────────────────────────┘
│                                                                     │
│  Peak                                                               │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  Cashable Points │ Microrecognition │ Giftcard │ Early Rota  │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

- **Flowstate** = brand name, top-left header, always visible
- **Platform** = horizontal menu bar below the header (Directory, Package, Integrations, Account)
- **Peak** = first vertical product, accessed from the dashboard or a products menu. Its own sub-navigation: Cashable Points | Microrecognition | Giftcard | Early Rota

---

## 3. Data model

### 3.1 People (Directory)

Unified people table. One table, four roles, filter tabs in the UI.

| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| name | TEXT | Full name |
| email | TEXT | Unique |
| phone | TEXT | Optional |
| role | ENUM | `carer` \| `care_receiver` \| `coordinator` \| `key_person` |
| metadata | JSONB | Role-specific attributes (see below) |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

**Role-specific metadata:**

| Role | Metadata fields |
|------|----------------|
| carer | skills: string[], training_expiry: date, certifications: string[], shift_preference: string |
| care_receiver | care_needs: string[], emergency_notes: string, package_id: UUID (FK) |
| coordinator | organisation: string, packages: UUID[] (FK), permissions: string[] |
| key_person | relationship: string (e.g. "daughter", "son", "spouse"), person_id: UUID (FK → care_receiver) |

**Directory UI:** Filter tabs — All | Carers | Care Receivers | Coordinators | Key Persons

### 3.2 Packages (Care Teams)

A Package is a group of people in the Directory working together to care for a care receiver.

| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| name | TEXT | e.g. "Mrs. Adeyemi's Care Team" |
| receiver_id | UUID | FK → people (role = care_receiver) |
| coordinator_id | UUID | FK → people (role = coordinator) |
| status | ENUM | `active` \| `paused` \| `archived` |
| peak_channels | JSONB | Which Peak receivables are enabled: `{ cashable: true, recognition: true, giftcard: false, earlyrota: true }` |
| created_at | TIMESTAMP | |
| updated_at | TIMESTAMP | |

**Package Members:**

| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| package_id | UUID | FK → packages |
| person_id | UUID | FK → people |
| role_in_package | ENUM | `primary_carer` \| `secondary_carer` \| `key_person` |
| joined_at | TIMESTAMP | |

### 3.3 Integrations

Third-party connections. Coordinators choose which to enable per Package or per Account.

| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| scope | ENUM | `account` \| `package` |
| scope_id | UUID | FK → accounts or packages |
| provider | TEXT | e.g. "stripe", "tango_card", "rota_system" |
| config | JSONB | Encrypted provider credentials + settings |
| status | ENUM | `active` \| `inactive` \| `error` |
| created_at | TIMESTAMP | |

### 3.4 Accounts

Organisation layer. Billing, settings, access control.

| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| name | TEXT | Organisation name |
| owner_id | UUID | FK → people (role = coordinator) |
| settings | JSONB | Org-level settings |
| created_at | TIMESTAMP | |

### 3.5 Users (Auth)

Separate from People. Authentication credentials.

| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| person_id | UUID | FK → people (links auth to a person in the Directory) |
| email | TEXT | Unique, used for login |
| password_hash | TEXT | bcrypt hashed |
| created_at | TIMESTAMP | |
| last_login_at | TIMESTAMP | |

### 3.6 Peak — Ledger (existing)

Double-entry points ledger. Preserved from current scaffold.

| Table | Key fields |
|-------|-----------|
| accounts | id, kind (asset/liability), scope, name |
| entries | id, ts, account_id, delta, memo, ref_kind, ref_id |
| checkpoints | scope, balance_key, balance_value |

### 3.7 Peak — Recognition (Microrecognition)

Internal badge/streak system. No external API.

| Table | Key fields |
|-------|-----------|
| badges | id, name, icon, description, criteria (JSONB) |
| carer_badges | carer_id (FK → people), badge_id (FK → badges), awarded_at |
| streaks | carer_id, streak_type (e.g. "perfect_attendance"), current_count, best_count, last_event_at |
| praise | id, carer_id, from_person_id, package_id, message, created_at |

**Badge examples:**
- "14-day perfect attendance" — streak_type: perfect_attendance, threshold: 14
- "100 shifts" — streak_type: total_shifts, threshold: 100
- "Client hero" — manually awarded by coordinator
- "First praise" — automatically awarded on first client praise

### 3.8 Peak — Cashable (Stripe Issuing)

| Table | Key fields |
|-------|-----------|
| cards | id, carer_id (FK → people), stripe_card_id, status (active/frozen/closed), last_four |
| card_loads | id, card_id (FK → cards), points_redeemed, amount_loaded_gbp, stripe_transfer_id, created_at |

### 3.9 Peak — Giftcard (Tango Card)

| Table | Key fields |
|-------|-----------|
| giftcard_orders | id, carer_id (FK → people), provider (tango_card), reward_link_id, points_redeemed, status (pending/delivered/failed), created_at |

### 3.10 Peak — Early Rota

| Table | Key fields |
|-------|-----------|
| rota_access | id, carer_id (FK → people), package_id (FK → packages), priority_window_hours (e.g. 24), enabled_at, expires_at |

---

## 4. Technical architecture

### 4.1 Two repos

| Repo | Tech | Deploy | URL |
|------|------|--------|-----|
| `Addyx2/Aultrum` | Vite | Vercel | `aultrumpro.vercel.app` |
| `Addyx2/flowstate` | Next.js (App Router) | Vercel | `flowstate.aultrum.co.uk` |
| Peak repo (existing, renamed to `flowstate-api`) | Fastify | Railway | API endpoint |

### 4.2 Fastify API (backend)

```
POST   /auth/register          ← create account (email + password)
POST   /auth/login             ← returns JWT
GET    /auth/me                ← current user

GET    /platform/directory     ← list people (filterable by role)
POST   /platform/directory     ← add person
GET    /platform/directory/:id ← person detail
PUT    /platform/directory/:id ← update person
DELETE /platform/directory/:id ← remove person

GET    /platform/packages              ← list packages for account
POST   /platform/packages              ← create package
GET    /platform/packages/:id          ← package detail (includes members)
POST   /platform/packages/:id/members  ← add member to package
DELETE /platform/packages/:id/members/:person_id ← remove member

GET    /platform/integrations          ← list integrations
POST   /platform/integrations          ← connect integration
PUT    /platform/integrations/:id      ← update integration config
DELETE /platform/integrations/:id      ← disconnect

GET    /platform/account               ← account detail + settings
PUT    /platform/account               ← update settings

GET    /peak/ledger/balances           ← points balances (scoped to account/package)
POST   /peak/ledger/entries            ← post double-entry

GET    /peak/cashable/cards            ← list carer's cards
POST   /peak/cashable/cards            ← issue card
POST   /peak/cashable/cards/:id/load   ← fund card from points

GET    /peak/recognition/badges        ← list badges
GET    /peak/recognition/badges/:carer_id ← carer's badges
POST   /peak/recognition/badges/:carer_id/award ← award badge
GET    /peak/recognition/streaks/:carer_id ← carer's streaks
POST   /peak/recognition/praise        ← give praise

GET    /peak/giftcard/orders           ← list giftcard orders
POST   /peak/giftcard/orders           ← issue giftcard

GET    /peak/earlyrota/access          ← list priority access
POST   /peak/earlyrota/access          ← grant priority access
```

### 4.3 Next.js frontend

- **App Router** (Next.js 14+)
- **Styling:** Tailwind CSS (Obsidian Precision design system — same as Flowstate beta)
- **Auth:** JWT stored in httpOnly cookie, middleware checks auth on all routes except /login and /register
- **State:** React Server Components where possible, client components for interactive elements
- **API calls:** Server-side fetching from Fastify API (no CORS issues — same origin via Vercel rewrite or server-side proxy)

### 4.4 Auth flow

1. User visits `flowstate.aultrum.co.uk`
2. Redirected to `/login` if not authenticated
3. Email + password → POST `/auth/login` → JWT in httpOnly cookie
4. JWT contains `person_id` + `account_id` + `role`
5. All subsequent API calls include JWT → middleware validates → routes to correct account scope

### 4.5 Deployment

| Service | Platform | Config |
|---------|----------|--------|
| Next.js frontend | Vercel | `flowstate.aultrum.co.uk` subdomain, env vars for API URL |
| Fastify API | Railway | PostgreSQL addon, env vars for DB + JWT secret + Stripe/Tango keys |
| Database | Railway PostgreSQL | Production. SQLite for local dev. |
| DNS | Vercel or Cloudflare | CNAME `flowstate.aultrum.co.uk` → Vercel |

---

## 5. UI/UX requirements

### 5.1 Pages to design

**Auth:**
- `/login` — email + password form, "Create account" link
- `/register` — name + email + password + confirm password form

**Dashboard:**
- `/` — overview: packages, recent activity, quick stats

**Platform (horizontal menu):**
- `/directory` — people list with filter tabs (All | Carers | Care Receivers | Coordinators | Key Persons)
- `/directory/:id` — person detail page (shows role-specific metadata)
- `/package` — packages list
- `/package/:id` — package detail (members, Peak channel toggles, activity)
- `/integrations` — available integrations, connected status, connect/disconnect
- `/account` — account settings, billing, team

**Peak (vertical product):**
- `/peak` — Peak overview: total points issued, active cards, badges awarded, engagement rate
- `/peak/cashable` — card management: issue card, view card, load card, transaction history
- `/peak/recognition` — badge gallery, streaks dashboard, praise feed
- `/peak/giftcard` — giftcard catalog, order history, issue giftcard
- `/peak/earlyrota` — priority access management, per-package settings

### 5.2 Design system

- **Brand:** Flowstate (top-left), not Aultrum
- **Design language:** Obsidian Precision (same as Flowstate beta marketing site)
- **Typography:** JetBrains Mono (headers), system sans-serif (body)
- **Colours:** `#070708` background, `#4a9eff` accent blue, `#f0f2f5` cloud white, `#c8ccd2` cloud grey
- **Components:** glass panels, rounded corners, subtle borders, dark mode primary
- **Mobile:** responsive, mobile-first for carer-facing pages

### 5.3 Key UI patterns

**Directory filter tabs:**
```
[ All ]  [ Carers ]  [ Care Receivers ]  [ Coordinators ]  [ Key Persons ]
```
Each tab shows a filtered table of the unified people list. Click a row → person detail.

**Package detail — Peak channel toggles:**
```
Peak Receivables
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cashable Points    [● Enabled]    [Stripe connected]
Microrecognition   [● Enabled]    [Internal]
Giftcard           [○ Disabled]   [Tango Card — Connect]
Early Rota         [● Enabled]   [Rota system — Connect]
```

**Recognition dashboard:**
```
Badges awarded this month: 47
Active streaks: 23 carers
Praise messages: 12
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recent badges:
  Sarah A. — 14-day perfect attendance ✓
  James K. — Client hero (awarded by coordinator)
  Maria L. — 100 shifts ✓
```

---

## 6. Build sequence

| Phase | What | Est. time |
|-------|------|-----------|
| **P0** | Design (UI/UX for all pages) | Your design session |
| **P1** | Backend restructure (Fastify API) | 2–3 days |
| **P2** | Auth (register, login, JWT) | 1 day |
| **P3** | Platform base (Directory, Package, Integrations, Account) | 2–3 days |
| **P4** | Peak channels (recognition, cashable, giftcard stub, earlyrota stub) | 2–3 days |
| **P5** | Frontend (Next.js) | 3–5 days |
| **P6** | Integration + deploy (Railway + Vercel) | 1 day |

**P0 (your design) feeds into P1–P6 (my build).**

---

## 7. Open questions for the designer

1. **Dashboard layout** — what's the primary information a coordinator sees on login? Package summaries? Recent activity? Points balances?
2. **Directory table** — what columns are visible by default for each role filter? What's the sort order?
3. **Peak channel cards** — how are the four receivables presented on the Peak overview? Cards? List? Dashboard widgets?
4. **Mobile layout** — does the horizontal Platform menu collapse into a hamburger on mobile? How does the Peak sub-nav work on small screens?
5. **Badge design** — are badges visual icons (SVG)? Text-only? Do they have tiers (bronze/silver/gold)?
6. **Empty states** — what does the Directory look like with zero people? What does Peak look like with no points issued?
7. **Onboarding flow** — after registration, does the coordinator immediately see the Dashboard, or is there a setup wizard (create first package, add first carer)?

---

## 8. Constraints

- Gateway is excluded from production. It exists in code but is not built, deployed, or surfaced in the UI.
- The marketing site (`aultrumpro.vercel.app`) is separate and unchanged.
- Peak's ledger (double-entry) is preserved as-is from the current scaffold.
- The Mantorium research programme is background context. It does not appear in the Flowstate UI.
- Design system must match the Flowstate beta marketing site (Obsidian Precision, dark mode).