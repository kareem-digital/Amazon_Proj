# Strategy Schema Registry v4.0

**VOW Platform — CTV Planning Agent**

| | |
|---|---|
| **Version** | 4.0 |
| **Supersedes** | 1.1.0, 2.0.0, 3.0 |
| **Status** | For client sign-off. Implementation-ready except where marked **Open**. |
| **Scope** | Connected TV (`streaming_tv`) only. Display and online video are future scope. |
| **Verified against** | `staging.vowmade.dev` — 4 August 2026. Test strategy `VMA2026368`. |
| **Purpose** | Single reference for building the planning agent. Replaces all earlier revisions. |

---

## 0. How to read this document

### 0.1 Why this version exists

Version 2.0 was reviewed and received 28 comments. Version 3.0 answered each of them **in place**, deliberately preserving v2.0's section order so that every comment stayed anchored next to the text it was made on. That made v3.0 easy to review but not easy to build from.

Separately, a full walkthrough of the live Strategy module was carried out — all nine screens, every field, and all seventeen API calls with their payloads and responses. That produced 177 recorded findings, and a number of them contradict positions held in both v2.0 and v3.0.

This version does three things:

1. Carries forward everything in v2.0 that is correct
2. Applies all 28 review resolutions from v3.0
3. Corrects the document against what the platform actually does, and adds the material that was missing entirely

It is organised for implementation rather than for review anchoring. **Section 1 is a full traceability index** so that any earlier comment can still be traced to where it now lives.

### 0.2 Evidence markers

Every non-obvious claim carries one of these:

| Marker | Meaning |
|---|---|
| **Verified** | Seen in an API request or response on staging |
| **Observed** | Seen on screen; not confirmed in the API |
| **Inferred** | Reasoned from evidence; not confirmed |
| **Open** | Needs a client answer before it can be built |

Anything unmarked is either a design decision recorded here or a statement carried unchanged from v2.0.

### 0.3 How to review this document

- **Section 1** shows what changed and why. Start here if you reviewed v2.0.
- **Section 11** lists every open decision, ranked. These are the questions that need answers; six of them block implementation.
- **Section 12** lists four data quality issues that cannot be resolved on our side.

Comments are welcome anywhere. Where a position is contested, the evidence for it is stated inline so the disagreement can be settled on facts rather than on reading.

---

## 1. What changed and where

### 1.1 The 28 review comments — resolution index

Every comment on v2.0, what it asked, and where the answer now lives.

| # | Comment anchor | Resolution | Now in |
|---|---|---|---|
| 1 | "Their own targeting (adds CPM)" | Third-party targeting can come from Amazon DSP **or** the inventory source. It is a per-deal choice, not a property of the tier. Recorded as `targeting_source`. | §4.4, §4.5 |
| 2 | "added fee consequence" | Fee is driven by the data provider, not the profile. Does not compound within a provider; does stack across providers. | §4.5.4 |
| 3 | "Budget split NEW" | Optional. Now placed **after** creation, because the platform allocates budget itself and exposes it for editing. | §5.11 |
| 4 | "mandatory" (audiences) | Audiences are optional. Declining all three is a valid plan and incurs no data fee. | §5.6 |
| 5 | "Targeting NEW" | Audiences are one kind of targeting. Targeting arrives pre-filled. Geography can substitute for audiences entirely. Partially constrained by the API — see note. | §5.6, §5.10 |
| 6 | The two v1.1.0 field lists | **Source** column introduced. Requirement and Source are separate questions. The trader is asked for three things. | §5.3 |
| 7 | "Required" (Strategy name) | Generated from the brief. Requirement Optional, Source GENERATED. | §5.4 |
| 8 | "Multi-select" (Target markets) | One market per strategy in M1, field held as a list. Per-market versus campaign-level split documented. | §3.2, §5.4 |
| 9 | "Required" (Primary currency) | Not asked. **Correction:** it comes from the advertiser, not derived from the market. | §4.6, §5.4 |
| 10 | "KPI" | `kpi_target_value` added, 2–5 inclusive. **Correction:** held per format, not per strategy. | §5.4 |
| 11 | "Table" (Market budgets) | Type column now holds data types throughout. Widgets removed from the whole column. | §5.4, §6 |
| 12 | "Required" (Base bids) | Not asked. **Contested:** floor-rate deals do require a bid, and almost all VOW inventory is floor-rate. See open decision. | §4.3, §5.4, §11 |
| 13 | "Optional" (Frequency cap) | Advertiser-level settings introduced as a concept, with `is_locked` for brand policies. | §3.5 |
| 14 | "Required" (Formats) | Format is a constant. Prime Video is a channel. **Correction:** the forecast endpoint treats `prime_video` as a separate supply line. | §4.7, §5.7 |
| 15 | "Required for video" (Product categories) | From the advertiser, else implied from the brief. "for video" qualifier dropped. | §5.4 |
| 16 | "Required" (Selling location) | Removed from basics; belongs with tracking. Comes from the advertiser. | §5.14 |
| 17 | "Conditional" (Product ASINs) | Removed from basics. Sent empty at creation, attached later. | §5.14 |
| 18 | "Checkbox table" (Selected deals) | Deals are matched, not selected. Only channel and CPM surface — plus tier capability and commercial commitment. **Blocked:** the matching inputs are not available as fields. | §5.5, §11, §12 |
| 19 | "Netflix/Disney" | Same correction as comment 1, second occurrence. | §4.5.3 |
| 20 | "bundles.narrow/balanced/broad" | Does not exist. The agent groups a flat list itself. **New finding:** the suggest flow is already in production use via a `prompt` field. | §4.5.3, §5.6 |
| 21 | "Optional" (Location) | Defaults to the market's country. `markets` and `location` distinguished. | §5.10 |
| 22 | "Optional" (Device type) | From the advertiser, possibly locked. Format and device type separated — `streaming_tv` does not mean a television screen. | §3.5, §4.7, §5.10 |
| 23 | "Plan Approval" heading | Reduced to a status change. `PlanStatusEnum` added. Manager routing, rejection and the interrupt removed. | §5.8 |
| 24 | "api/strategies" | **Contested:** `simple-strategies` exists but the product uses `POST /api/strategies/`. Three candidates. Fourteen catalogue corrections applied. | §7, §11 |
| 25 | "Required" (Click-through URL) | Optional. Confirmed on the platform — approved Streaming TV creatives exist with a null URL. | §5.12 |
| 26 | Three approval rows | One status per channel, keyed by data. **Blocked:** creative approval granularity on the platform is creative × market, with no channel dimension. | §5.13, §11 |
| 27 | "Tracking Setup" heading | No order between the post-creation branches. Activation becomes a join node with an explicit prerequisite checklist. | §5.1, §5.16 |
| 28 | "Confirm with client" | A strategy can be updated after creation. Guardrails added for fields that carry money. | §5.17 |

**Closed by this version:** all four questions v2.0 left open — ASIN and product-location timing (raised twice), the suggest response shape, and postcode support.

**Still open from v2.0:** two — what status a created strategy lands in (now answered: `Paused` / `Inactive`, **Verified**), and whether per-channel creative approval is readable (now answered: it is not, **Verified**). Both are recorded as consequences rather than as unknowns.

### 1.2 Corrections from platform verification

These are positions held in v2.0 and v3.0 that the live platform contradicts. Each is the reason a section in this version differs from earlier revisions.

| Held in v2.0 / v3.0 | What the platform does | Evidence | Now in |
|---|---|---|---|
| Targeting is step 5, before creation | Every targeting endpoint is nested under a strategy id, so targeting cannot precede creation. The wizard has no targeting step; it appears under Locations afterwards. | **Verified** | §5.1, §5.10 |
| Budget split is the agent's job, before creation | The platform splits the market budget evenly per format at creation and exposes it for editing in the Planner. | **Verified** — one submitted budget of £10,000 became two allocations of EUR 5,454.55 | §5.11 |
| Currency is derived from the market | Currency is an advertiser default. It is pre-filled as EUR before a market is chosen and does not change when a market is selected. | **Verified** — a strategy exists with `primary_currency: "NOK"` and `markets: ["US"]` | §4.6 |
| `formats = ["streaming_tv"]` as a constant is safe | The forecast endpoint returns a separate `DSP_PRIME_VIDEO` supply line. Omitting `prime_video` loses that line. | **Verified** — 71,120 reach and 212,860 impressions absent without it | §4.7, §5.7 |
| The forecast depends on audiences and targeting | The forecast payload contains four inputs only: flight dates, formats, goal, market budgets. | **Verified** | §5.7 |
| The repair loop widens the audience and re-forecasts | Audience-aware forecast endpoints exist but nothing in the product calls them. The one forecast the product runs takes no audience input. | **Verified** | §5.7, §11 |
| A deal carries `inventory_tier` and `channel` | Neither field exists on a deal. Both would require parsing the deal name. | **Verified** | §5.5, §12 |
| Creative approval is per channel | A creative carries `market` and `approval_status` with no channel dimension. | **Verified** | §5.13 |
| Audiences are campaign-level | Audiences are nested per market inside `markets_info[].audience_targeting[]`. | **Verified** | §3.2 |
| One flight date range per strategy | The platform supports multiple flight ranges, each with its own per-market, per-format budget. | **Verified** — dedicated CRUD endpoints exist | §3.1, §5.11 |
| KPI is one value per strategy | KPI and its target value are held per format. | **Verified** — `formats_and_kpis[]` | §5.4 |
| `kpi_target_value` range is 1–5 | The control offers 2, 3, 4, 5. | **Observed** | §5.4 |

### 1.3 What is new in this version

Material that was absent from every earlier revision.

| Added | Why it was needed |
|---|---|
| **§3 Domain model** — the full hierarchy, per-market versus campaign-level, identifiers, and the status model | No revision stated how a strategy is actually structured. Several design errors trace back to this gap. |
| **§4.6 Currency model** | Four currency contexts can coexist in one plan. Getting this wrong produces a 9% error in every impression estimate. |
| **§4.7 Taxonomies** | Five overlapping classifications exist for what looks like one concept, and "channel" carries six different meanings across the UI and API. |
| **§4.8 Numeric rules and guards** | Reach cannot be summed; one deal has a zero CPM; currencies mix within a plan. All three break naive arithmetic. |
| **§5.11 Budget and bid allocation** | The platform's allocation model — per flight range, per market, per format — was not documented. |
| **§5.18 Sync and failure handling** | Creation does not mean the campaign exists on Amazon. Sync is asynchronous and can fail. |
| **§8 Platform contract reference** | The verified request and response shapes for all seventeen endpoints, so the payloads do not have to be reverse-engineered during implementation. |
| **§6 Consolidated slot registry** | A single table of every field with its type, requirement, source and endpoint. |

---

## 2. Core principles

Carried forward from v1.1.0 unchanged. All three remain in force.

**Zero-Hallucination Policy.** The agent never invents strategy parameters, metrics, targeting criteria, or deal identifiers. It populates only values verified against the VOW database and REST APIs.

**Self-Filling Form Paradigm.** The agent operates as a stateful slot-filling engine backed by LangGraph. Input arriving by chat or as an uploaded brief is parsed into registered Pydantic slot schemas.

**API-Driven Tool Execution.** Every step maps to an official VOW API endpoint. Where no endpoint exists, that is stated rather than assumed.

### 2.1 A fourth principle, added

**Stated Uncertainty.** Where the agent cannot verify an outcome, it says so rather than presenting an unverified change as a fix. Three cases arise repeatedly in this document:

- Third-party inventory returns no reach forecast, so widening it cannot be shown to have worked
- Floor-rate pricing means the final cost is not known at planning time
- Where an advertiser policy is locked, the agent must name the lever it could not use rather than silently omitting it

Zero-Hallucination covers not inventing. This covers not implying.

---

## 3. Domain model

### 3.1 The hierarchy

**Verified** against the create payload and the post-creation screens.

```
Advertiser                        UUID, e.g. 353eea43-bc42-456f-ba4f-3d3e20ea6bc8
|                                 Scopes everything. Held in the session, not passed as a parameter.
|
+-- Strategy                      id, e.g. VMA2026368  (VMA + year + sequence)
    |                             The primary object of this module.
    |
    +-- Flight ranges[]           Multiple ranges are supported, each with its own budget
    |   +-- Market
    |       +-- Format -> budget
    |
    +-- markets_info[]            Per market: bid, budget, currency, audience targeting
    +-- market_deals[]            Per market: matched deals
    +-- assets[]                  Campaign-level
    +-- Targeting                 Written after creation, per market
    |
    +-- Campaigns[]               Created on Amazon DSP by the background sync
        +-- Ad groups[]           Amazon DSP's own structure
```

Two facts that shape most of this document:

1. **Market is the organising unit of the payload.** Budget, bid, currency, audiences and deals are all per-market. Everything else is campaign-level.
2. **Flight ranges are a list, not a value.** The full budget granularity is `strategy -> flight range -> market -> format`.

### 3.2 Per-market versus campaign-level

**Verified** against the create payload.

| Per market | Campaign-level |
|---|---|
| Budget allocated to that market | Flight dates (per flight range) |
| Currency of that market's spend | Goal |
| Base bid | KPI and KPI target value (per format) |
| Matched deals, and therefore the CPM | Creative durations |
| **Audience targeting** | Assets and creatives |
| Available locations — endpoint is keyed by market | Product categories |
| Available product categories — endpoint is keyed by market | Conversion types |
| Reach forecast | Selected inventory sources |
| Conversion definitions (each carries a market flag) | Tracking (ad tag), credit check |

**Correction from v2.0:** audiences were treated as campaign-level. They are nested inside `markets_info[].audience_targeting[]` and an audience set carries a single `market` value, not a list. Audiences are therefore not shared across markets.

Two entries are easy to miss: the locations and product-category endpoints are both keyed by market, so those lists differ even when the trader's intent does not.

### 3.3 Identifiers

**Verified.**

| Object | Identifier | Notes |
|---|---|---|
| Advertiser | UUID | Session-scoped |
| Strategy | `VMA2026368` | This **is** the `id` field. There is no separate UUID. |
| Deal | `external_deal_id` | At least seven distinct formats in use — see §4.3.4 |
| Audience set | UUID | |
| Audience segment | `amz_id` | Amazon's identifier |
| Asset | UUID | |
| Creative | UUID **and** `amz_id` | Two identifiers on one object |
| Product category | Long numeric string, e.g. `304861615492321169` | Amazon identifier, not an integer in practice |

**Note for implementation:** `product_categories` was typed as `list[int]` in earlier revisions. The values are long numeric strings and should be held as strings.

### 3.4 Status model

**Verified.** A strategy carries **two status fields and five booleans**. They are not interchangeable.

**`status` — lifecycle**

Eight values are exposed in the UI filter. Two exact API strings are confirmed.

```
Delivering        Ready to deliver
Out of budget     Inactive
Ended             Archived
Not running       Draft
```

Confirmed API values: `"3_ended"`, `"6_inactive"`. The numbering suggests the ordering below, **Inferred** from the filter order:

```
1_delivering  2_out_of_budget  3_ended  4_not_running  5_ready_to_deliver  6_inactive
```

**Open:** the exact strings for the remaining four.

**`delivery_activation_status`** — separate field, e.g. `"INACTIVE"`. Whether the strategy is delivering, as distinct from where it sits in its lifecycle.

**Five booleans**

| Field | Meaning |
|---|---|
| `is_draft` | Deliberately saved as a draft |
| `is_syncing` | Background sync to Amazon in progress |
| `is_archived` | Hidden from the default list |
| `is_readonly` | Cannot be edited |
| `is_automated` | Present in the API already. **Open:** is this the agent marker? |

**Important consequence:** `Archived` and `Draft` are **not** `status` values — they are booleans. A draft row carries `status: "6_inactive"`. Code that reads only `status` will classify a draft as inactive.

**`is_readonly` is state-derived**, not a property. Ended strategies return `true`; drafts return `false`. Mutability follows the strategy's state.

**`failure_reason`** — e.g. `"CAMPAIGN_SYNC_ISSUES"`. Populated when the Amazon sync fails. See §5.18.

### 3.5 Advertiser-level settings

**New concept**, introduced by the review comment on the frequency cap and extended by three later comments.

Some settings belong to the advertiser rather than to the campaign. They do not change from one brief to the next, so asking for them each time treats a property of the advertiser as a decision about the campaign.

**Settings identified so far**

| Setting | Confirmed by | Locked? |
|---|---|---|
| Frequency cap | Review comment | **Open** |
| Product categories | Review comment | **Open** |
| Selling location | Review comment | **Open** |
| Device type | Review comment | **Open** — the comment reads as a policy |
| Budget cap | **Inferred** — assumed to behave like the frequency cap | **Open** |
| Primary currency | **Verified** on the platform — pre-filled independently of the market | No |
| Brand-safety exclusions | **Inferred** | **Open** |

**Open decision D6:** the full list, and which entries are locked. This is the single answer that most changes agent behaviour, because it determines what the repair loop is permitted to relax.

**When they are loaded**

At the start of the session, **before the brief is parsed**.

```
GET /api/admin/advertiser/{id}/          model AdvertiserAdminRetrieve
```

The order matters: defaults fill the plan, and anything the brief states overrides them. Reversing it would let defaults overwrite the brief.

**Note:** v1.1.0 specified `/api/advertisers/{id}/defaults/`. That endpoint does not exist.

**Why a plain default is not enough**

The review comment on device type noted that some advertisers permit Connected TV only. That reads as a policy rather than a starting point — something the trader should not override, and that the repair loop must not quietly relax when reach falls short.

```python
class AdvertiserSetting(BaseModel):
    """A setting held on the advertiser rather than the campaign."""
    value: Any
    is_locked: bool = False           # a brand policy the trader cannot override
    reason: Optional[str] = None      # shown to the trader when locked
```

Without `is_locked`, the agent cannot distinguish a starting point from a rule, and will offer to relax something it is not allowed to touch.

**Open:** what should the agent do when an advertiser has no value set — leave the field empty, or fall back to a platform default?

---

## 4. Business logic

### 4.1 Product attribution and selling locations

Carried forward from v1.1.0, with the timing corrected.

**On Amazon — `SOLD_ON_AMAZON` (endemic).** ASINs required. Enables detail page view, add-to-cart, purchase and ROAS tracking.

**Off Amazon — `NOT_SOLD_ON_AMAZON` (non-endemic).** ASINs optional, and used to monitor halo sales. Ad tag conversions required for site event tracking.

**Verified on the platform:**

- On Amazon: an invalid ASIN blocks progress
- Off Amazon: the ASIN field is shown but zero ASINs is accepted
- Validation is batched — the trader pastes a comma-separated list and validation runs on submit, not as they type

**Where it is collected:** the tracking step, not basics. The value itself comes from the advertiser's settings, so the agent already holds it at creation.

### 4.2 Attribution window

Unchanged: 14-day post-view and post-click.

For CTV only post-view is meaningful, since the ad cannot be clicked.

### 4.3 Deal types and price types

#### 4.3.1 The three deal types

| Type | Price type | Bid applies | Volume guaranteed | Full budget owed | Can pause |
|---|---|---|---|---|---|
| `PREFERRED` | `FIXED_CPM` | No | No | No | Yes |
| `PRIVATE_AUCTION` | `FLOOR_RATE` | **Yes** | No | No | Yes |
| `PROGRAMMATIC_GUARANTEED` | `FIXED_CPM` | No | **Yes** | **Yes** | **No** |

#### 4.3.2 Floor rate versus fixed CPM

This distinction drives several decisions in this document and is worth stating plainly.

```
FIXED_CPM    the figure shown is the figure paid
FLOOR_RATE   the figure shown is a minimum that must be exceeded;
             the figure paid is determined by the auction and is
             not known at planning time
```

A floor of £22.96 and a fixed price of £15.26 look identical on screen and mean opposite things. See open decision D3 on how this should be surfaced.

#### 4.3.3 What is actually on the platform

**Verified** — 83 deals available for a GB Streaming TV plan.

| Observation | Consequence |
|---|---|
| Almost all deals are `PRIVATE_AUCTION` with `FLOOR_RATE` — all Netflix, all Freewheel, and some Prime Video | The bid lever exists on almost all inventory. See D3. |
| Some Prime Video deals are `PREFERRED` with `FIXED_CPM` (£15.26, £24.79) | Fixed pricing is the minority case, not the norm |
| No `PROGRAMMATIC_GUARANTEED` deal was found, although the filter offers it | **Open:** does PG inventory ever appear? |
| The platform blocks progress when base bid is empty, on a pure CTV plan | The agent must supply a bid. See D3. |
| One deal is priced at `0.00` (`VowMade_Fifa 2026_ZA`) | Division-by-zero guard required. See §4.8. |
| GB deals are priced in USD as well as GBP | Currency normalisation required. See §4.6. |
| `ZA` deals appear in a GB-filtered list | The agent must filter on `locations[].country_code` itself |

#### 4.3.4 Deal identifier formats

**Verified** — at least seven shapes in use:

```
VIA-159-00100                            structured, sequential
a0f440c9-0159-40bf-aab5-b1108b10614a     UUID
EXT245WE18EEMKX                          Amazon external deal id
apsb8dd1c90                              lowercase alphanumeric
2653736                                  numeric
PM-RDDS-8837                             prefixed alphanumeric
Disney-FAST-SFV-IOA-AZ-2026              descriptive slug
```

The agent cannot validate the **format** of a `specific_deal_id`. It can only attempt a lookup and report whether the deal was found.

#### 4.3.5 Deal metadata completeness

**Verified.** Metadata quality differs sharply between Amazon-owned and third-party deals.

| Field | Prime Video (Preferred) | Netflix (Private Auction) |
|---|---|---|
| `genre` | `"ROS"` | `null` |
| `devices` | 3 entries with volumes | `[]` |
| `environments` | `APP` at 100% | `[]` |
| `media_types` | `VIDEO_STV` at 100% | `[]` |
| `locations[].bid_request_volume` | 1,457,882,193 | 1 |

A location volume of `1` is a placeholder rather than a measurement.

**Consequence:** matching on genre, device or environment works on Amazon inventory and does not work on third-party inventory. Deliverability cannot be assessed from volume on third-party deals. See §12.

### 4.4 Inventory tiers

Three tiers were introduced in v2.0 as the primary fork in the CTV flow.

| Tier | Examples | Deal availability | Reach forecast |
|---|---|---|---|
| Amazon owned | Prime Video, Twitch | Pre-curated, selectable now | Available |
| Third-party pre-curated | Netflix, Hulu, others | Pre-curated, selectable now | Not available |
| Third-party needs curation | Disney+, others | Rate-card CPM only; the deal is curated after the insertion order is signed | Not available |

**Correction from v2.0.** The tier table originally implied that targeting source follows from the tier. It does not. Targeting on third-party inventory can come from **either** Amazon DSP **or** the inventory source, and which options exist is specific to the deal that is chosen or curated — so it is known only after matching, not at planning time.

What genuinely differs by tier is two things: whether a reach forecast comes back, and whether the deal exists yet.

Recorded on the plan as:

```python
targeting_source: TargetingSourceEnum    # AMAZON_DSP | INVENTORY_SOURCE
```

**Open decision D8:** can both run on the same deal? If so this field must be a list, and the combination rule (intersection or union) needs stating, because the two have opposite effects on reach.

**Blocked.** No `inventory_tier` field exists on a deal (**Verified**). The three-tier fork has no data source. See §12.

**Also relevant:** the inventory-sources endpoint returns `Twitch` alongside `Amazon Streaming TV` for a GB Streaming TV awareness plan (**Verified**). Amazon-owned CTV inventory is not only Prime Video, and Twitch carries a materially different audience.

### 4.5 Audience model

#### 4.5.1 Structure

**Verified.** Fifteen audience sets are available for the test advertiser — not the ~3,400 figure quoted in v1.1.0, which refers to individual **segments** held inside sets.

```
Audience set                    UUID, name, market (single value), goal
|
+-- prompt                      natural language, e.g. "Mums looking for
|                               healthier snacks for their kids school lunch boxes"
+-- audience_groups             nested boolean tree, held as a JSON STRING
+-- audience_count              e.g. 23
+-- strategy_count              reuse count; one set is used by 56 strategies
+-- standard_display_fee        e.g. "0.59"
+-- video_fee                   e.g. "1.63"
+-- fee_currency                e.g. "GBP"
```

**Two implementation notes:**

- `audience_groups` is a **JSON string, not an object**. It requires two parse passes.
- `standard_display_fee` can be an **empty string**, not null. Naive numeric parsing will fail.

#### 4.5.2 The boolean tree

**Verified.** `audience_groups` holds a nested tree of groups, each with an `AND` or `OR` operator, up to four levels deep. The structure of the `Healthy snacks` set:

```
AND
+-- OR    Presence of children, Presence of Children aged 5-11, 1 child
+-- AND
    +-- OR    Females
    +-- AND
        +-- OR    Age 36-40, Age 36-45 (High Reach)
        +-- OR    Healthy Food, Healthy Lifestyle, Health Conscious,
                  Gluten Free, Diet and Nutrition, Biscuits Snacks, ... (17 total)
```

Read: households with young children **and** female **and** aged 36–45 **and** interested in healthy food.

**Consequence for the repair loop.** "Widening the audience" is not one operation. It is either adding a term to an `OR` or removing an `AND` branch, and the two have very different effects on reach. The agent needs to state which it did.

#### 4.5.3 The suggest flow

**Correction from v1.1.0.** There is no `bundles.narrow/balanced/broad` object. The endpoint returns a flat list of segments with reach and relevance, and the grouping into three profiles is ours to do.

**New finding, Verified.** The `prompt` field on audience sets is populated with natural language on sets created through the suggest flow. Examples found on staging:

```
"Mums looking for healthier snacks for their kids school lunch boxes"
"find me audiences who are most likely to buy car accessories for luxury cars"
```

**This changes what the agent's job is at this step.** It writes a prompt; it does not browse segments or assemble boolean groups. Existing prompts are also usable as reference material for how to phrase one, and reusable where an existing set matches.

**Grouping rule — proposed, pending a response sample.** Group by cumulative reach, keep the groups nested (Balanced contains Narrow, Wide contains Balanced), and add segments until each group meets a reach target rather than a fixed segment count, so the profiles stay comparable across briefs of different sizes.

**Open decision D2:** a real request and response from the suggest endpoint. The grouping rule, the fee handling and the audience schema all depend on the actual shape, and this is the single most useful thing to unblock the audience work.

#### 4.5.4 Profiles

| Profile | Description |
|---|---|
| Narrow | Highly targeted, elevated intent, risk of underdelivery |
| Balanced | Optimal blend; the usual recommendation |
| Wide | Broad demographic and interest reach, less precision |

Renamed from "Broad" to "Wide" per client vocabulary. With the `bundles` object gone there is no API field to disagree with, so `AudienceProfileEnum.WIDE` stands.

**The three profiles differ in reach and precision, not in cost.** This follows from the fee rules below. They are a way of presenting one flat list at three levels of breadth, not an API feature with three price points.

#### 4.5.5 Fee rules

Three rules, from the review comment:

1. **What triggers a fee** — using first-party data, whether Amazon's own or a third party's own first-party audience such as Lifestyle or Interest. This holds regardless of profile.
2. **No compounding** — one fixed CPM applies when first-party data is used, however many segments are selected from that provider.
3. **Cross-provider stacking** — where a segment is matched in both Amazon and a third-party provider, both fees are paid.

Recorded as:

```python
audience_data_sources: list[AudienceDataSourceEnum]    # AMAZON_1P | THIRD_PARTY | NONE
```

Keyed on providers in play, not on segment count.

**Which categories carry a fee — Verified.** Six audience categories exist. Fee follows the category:

```
Free    Demographic, Device
Paid    In-market, Lifestyle, Interest, Custom-built    -> 1.63 video fee (GBP)
```

Sets containing only Demographic or only Device segments return `video_fee: "0.00"`. Sets containing any of the paid categories return `1.63`, whether they hold 1 segment or 32 — confirming rule 2.

**Two exceptions found**, both with zero segments, so **Inferred** to be data errors rather than counter-examples.

**Fee values must be read, not written into the specification.**

```
GET /api/contextual-targeting/fees                model Fee
POST /api/audiences/{market}/overlapping-audiences/    detects the rule-3 case
```

Staging values are `1.63` video and `0.59` standard display, both GBP. A figure of £2.00 quoted during review would already be stale.

#### 4.5.6 Constraints for CTV

- Amazon audiences can be applied to third-party inventory as well as Amazon-owned. The inventory source's own targeting is the alternative, not the only option.
- Product audiences are not applicable to CTV.
- AMC audiences are conditional — available only where the advertiser has prior campaign data.
- The agent uses the suggest endpoint exclusively. Nobody browses segments.
- The audience set does not need to exist before forecasting — **and in fact the forecast takes no audience input at all** (**Verified**, §5.7).
- The audience list is **not** filtered by goal (**Verified** — a `CONVERSION` set was returned for an Awareness strategy). The agent must filter if filtering is wanted.

#### 4.5.7 Match type

`Similar` / `Exact` toggle, `Exact` by default. Sent as `audience_targeting_match_type: "EXACT"`.

**Open:** what other values does `audience_type` take? Only `AUDIENCE_SET` was observed.

### 4.6 Currency model

**New section.** Four currency contexts can coexist in one plan.

| Context | Field | Example |
|---|---|---|
| Strategy currency | `primary_currency` | `EUR` |
| Market currency | `markets_info[].currency` | `GBP` |
| Deal currency | `deal_price_currency` | `GBP` **and** `USD` in the same list |
| Metrics display | `metrics.display_currency` | `USD` |

**Correction from v2.0.** Currency is **not** derived from the market. It is an advertiser default.

**Verified:**
- The field is pre-filled as `EUR` before any market is selected
- Selecting `United Kingdom` does not change it
- A strategy exists with `primary_currency: "NOK"` and `markets: ["US"]`

Source is therefore `ADVERTISER`, not `DERIVED`. The trader can override it.

**Conversion is real and applied by the platform.** **Verified:**

```
Market view      £10,000        base bid £25
Primary view     EUR 10,909.09  base bid EUR 27.27
Rate             ~1.0909 GBP -> EUR
```

Both figures are genuine and both are sent — the market currency in `markets_info[]`, the strategy currency as `primary_currency`.

**Implementation rule.** All arithmetic must be performed in one currency, and the agent must state which. Mixing a budget in one currency with a CPM in another produces a ~9% error at this rate:

```
Wrong    10,909.09 / 22.96 x 1000 = 475,178 impressions
Right    10,000.00 / 22.96 x 1000 = 435,540 impressions
Error    39,638 impressions
```

**Open:** `CurrencyEnum` holds only EUR, GBP and USD. `NOK` exists in production data. The enum needs extending or those advertisers are out of scope.

### 4.7 Taxonomies

**New section.** Five overlapping classifications exist for what appears to be one concept. This is the largest single source of confusion in the earlier revisions.

| Taxonomy | Values | Where it applies |
|---|---|---|
| `formats` | `display`, `online_video`, `streaming_tv`, `prime_video` (plus `netflix`, `disney+` in the list filter only) | Strategy, deals query, forecast |
| `target_types` / `creative_type` | `DISPLAY`, `VIDEO`, `STREAMING_TV`, `MOBILE` | Assets |
| `media_types` | `VIDEO_STV`, `VIDEO_OLV` | Deals |
| Creative `type` | `Video`, `Streaming TV Video` | Creatives |
| `supply` | `DSP_STREAMING_TV`, `DSP_PRIME_VIDEO` | Forecast response |

#### 4.7.1 Format versus channel

The review comment established that format is always `streaming_tv` and that Prime Video is a channel, not a format.

```
Format    the kind of inventory          streaming_tv
Channel   who is showing the ad          Prime Video, Netflix, Disney+, Channel 4
```

`FormatEnum.PRIME_VIDEO` is retained but annotated as deprecated rather than removed, since deleting an enum value is a breaking change for anything already sending it.

**Correction, Verified.** The forecast endpoint treats `formats` as a set of **supply-line keys**, not as a content type. Sending `["streaming_tv", "prime_video"]` returns two supply lines; sending `["streaming_tv"]` alone omits `DSP_PRIME_VIDEO` and loses 71,120 reach and 212,860 impressions.

| Endpoint | Does `prime_video` matter |
|---|---|
| `GET /api/inventory-sources/` | No — the same two Amazon sources are returned either way (**Verified**) |
| `POST /api/strategies/reach-forecast/` | **Yes** — a separate supply line (**Verified**) |
| `GET /api/deals/` | Passed as a filter; effect untested |

**Implementation rule:** the model holds `streaming_tv` and a channel. The **forecast payload** must send both `streaming_tv` and `prime_video` where Prime Video inventory is in the plan.

#### 4.7.2 Format versus device type

The review comment on device type separated two things earlier revisions had blended.

| | What it is | Where it is decided |
|---|---|---|
| `formats = ["streaming_tv"]` | The kind of content — streaming video | A constant for CTV |
| `device_types = ["Connected TV"]` | The screen the ad plays on | The advertiser's setting |

Streaming content is not watched only on television sets. Prime Video runs on phones, tablets and desktop browsers, all of which remain `streaming_tv`. The document proves this itself: the `Mobile environment` field distinguishing in-app from mobile web would be meaningless if delivery were confined to television screens.

**`streaming_tv` does not mean a television screen.**

#### 4.7.3 The word "channel"

Six distinct meanings across the UI and API:

| Term | Where | Values |
|---|---|---|
| "Channel type" | Strategy overview | On Amazon / Off Amazon |
| "Channels" column | Strategy list | On Amazon / Off Amazon |
| "Location" filter | Strategy list | On Amazon / Off Amazon |
| `product_location` | Strategy record | `SOLD_ON_AMAZON` / `NOT_SOLD_ON_AMAZON` |
| `channel_type` | Strategy record | `dsp` / `sponsored` |
| "Strategy type" | Strategy overview | DSP |

**The UI labels are inverted relative to the API.** What the UI calls "Channel type" is the API's `product_location`. What the API calls `channel_type` appears in the UI as "Strategy type".

And separately, following the review comment on creative approval, `SelectedDealSchema.provider` has been renamed to `channel` — with one caveat. "Provider" survives in the audience context, where it means a **data** provider (Amazon first-party versus a third party such as Experian). Channel is who shows the ad; data provider is whose audience data is being paid for. The two must not be collapsed.

**Recommendation for the implementation:** use the API's names in code and reserve the UI's labels for display. Record the mapping once.

### 4.8 Numeric rules and guards

**New section.** Four rules that naive arithmetic gets wrong.

#### 4.8.1 Reach cannot be summed across supply lines

**Verified:**

```
DSP_STREAMING_TV  est_reach  132,713
DSP_PRIME_VIDEO   est_reach   71,120
Sum                          203,833
API total_reach              233,803        <- higher than the sum
```

There is no cross-platform deduplication, and the API's own total is not the sum. **Always report the API's `total_reach`. Never derive it.**

**Impressions do sum**, and match exactly:

```
647,856 + 212,860 = 860,716  =  API total_impressions
```

**Across markets** reach can be added, since the audiences do not overlap.

#### 4.8.2 Frequency must be derived

The forecast does not return frequency.

```
frequency = total_impressions / total_reach
          = 860,716 / 233,803
          = 3.68
```

**The window is per week**, not per flight (**Observed** — the platform's own label). A target of 3 means three exposures per person per week.

#### 4.8.3 Effective CPM, not deal CPM

```
effective_cpm = deal_cpm + audience_data_fee
```

```
Deal CPM only        10,000 / 22.96 x 1000 = 435,540 impressions
Effective CPM        10,000 / 24.59 x 1000 = 406,669 impressions
Difference                                    28,871  (7%)
```

Quoting impressions from the deal CPM overstates the plan by the size of the fee.

#### 4.8.4 Guards required

| Guard | Why |
|---|---|
| `deal_price_amount == 0` | One deal is priced at `0.00`. Division by zero. |
| Currency equality before arithmetic | GBP and USD deals appear in the same list; the plan may be in EUR |
| `standard_display_fee == ""` | Empty string, not null |
| `ad_lengths` deduplication | `filter-properties` returns 16 entries with 7 distinct values |
| `locations[].country_code` filter | `ZA` deals appear in a GB-filtered list |
| Rate values as strings | All money and rate fields are strings, e.g. `"3.64"`, `"0.00000"` |

#### 4.8.5 Metrics that cannot be trusted

**Observed:** `VCR` of 128.45% appears in staging data. A completion rate above 100% is not meaningful. The agent should report platform metrics rather than recompute or reason from them.

---

## 5. The agentic flow

### 5.1 Flow order, and why it differs from v2.0

v2.0 reordered v1.1.0's wizard sequence into an agent-first flow. That reordering was right in intent, but two of its steps cannot be executed in the position given, and the platform walkthrough established why.

**Two hard constraints, both Verified.**

**Constraint 1 — targeting cannot precede creation.** Every targeting endpoint is nested under a strategy identifier:

```
GET/POST   /api/strategies/{id}/targeting/
POST       /api/strategies/{id}/targeting/auto-rec/
GET/POST   /api/strategies/{id}/targeting/{market}/locations/
GET/POST   /api/strategies/{id}/targeting/{market}/product-categories/
GET/POST   /api/strategies/{id}/targeting/{market}/products/
```

Each requires a strategy that already exists. The wizard has no targeting step; targeting appears under **Locations** on the strategy overview after creation.

**Constraint 2 — budget allocation happens at and after creation.** The trader submits one budget per market. The platform splits it evenly across formats at creation and exposes both budget and bid for editing in the **Planner**. **Verified:** one submitted market budget of £10,000 became two allocations of EUR 5,454.55.

**The corrected order**

```
PHASE A  -  PLAN                    nothing is persisted; all agent-side state
  1  Basics
  2  CTV inventory (deals matched)
  3  Audiences
  4  Reach forecast
  5  Finalise plan

PHASE B  -  CREATE                  one POST
  6  Create the strategy

PHASE C  -  ATTACH                  parallel branches, no order between them
  7  Targeting
  8  Budget and bid allocation
  9  Creative upload
 10  Creative approval
 11  Tracking setup
 12  Credit check

PHASE D  -  ACTIVATE                join node
 13  Activate
```

**Phase A is ordered and cannot be rearranged.** Inventory determines the CPM; the CPM determines the impressions; the forecast needs the budget and the formats. It is a genuine chain.

**Phase C has no internal order.** This follows the review comment on the tracking step. Creatives arrive from an agency and are often late; an ad tag has to be installed by the advertiser's own developers, which can take days; credit is a finance matter. Forcing an order means one late item blocks everything.

**Mapping from v2.0**

| v2.0 | v4.0 | Change |
|---|---|---|
| 1 Basics | 1 Basics | Unchanged in position |
| 2 CTV inventory | 2 CTV inventory | Unchanged in position |
| 3 Budget split | **8** Budget and bid allocation | Moved to Phase C — the platform allocates |
| 4 Audiences | 3 Audiences | Moved earlier; still optional |
| 5 Targeting | **7** Targeting | Moved to Phase C — API constraint |
| 6 Predict reach | 4 Reach forecast | Moved earlier |
| 7 Plan approval | 5 Finalise plan | Renamed; reduced to a status change |
| 8 Create | 6 Create the strategy | |
| 9 Upload creative | 9 Upload creative | Now explicitly parallel |
| 10 Creative approval | 10 Creative approval | Now explicitly parallel |
| 11 Tracking setup | 11 Tracking setup | Now explicitly parallel |
| 12 Credit check | 12 Credit check | Now explicitly parallel |
| 13 Activate | 13 Activate | Now a join node with a checklist |

**A note on the review comment about audiences being part of targeting.** That comment is right about the trader's experience, and this version keeps it: the trader deals with one subject, not two. But the API splits it. Audience **selection** goes into the create payload as `markets_info[].audience_targeting[]`, whereas geographic and device targeting can only be written after creation. So steps 3 and 7 are one subject presented once, executed in two places. The conversation should not expose that seam.

**Open decision D1** covers whether this split is acceptable or whether the intent was different.

### 5.2 What the trader is asked

The review comment on the basics field list asked for two things: cut what does not apply to CTV, and imply the rest. The result:

**Asked outright — three things, and only when the brief does not state them**

```
Market        Budget        Flight dates
```

**Asked conditionally — one**

```
KPI target value       only when the KPI is frequency
```

**Everything else** is generated, derived, taken from the advertiser's settings, fixed for CTV, read from an API, or matched by the agent.

**Open:** where the agent infers a value, should it show what it inferred and let the trader correct it, or surface only the ones it is unsure about? The first is safer; the second is shorter.

### 5.3 The Source column

Earlier revisions had only a Requirement column, and "Required" was widely read as "the trader must be asked". Those are two separate statements. A field can be required by the plan and never put to the trader as a question.

```
Requirement   does the plan need a value?
Source        where does that value come from?
```

| Source | Meaning |
|---|---|
| `ASKED` | The agent asks the trader outright |
| `INFERRED` | Read from the brief; asked only when the brief does not say |
| `DERIVED` | Calculated from another field |
| `GENERATED` | Composed by the system |
| `ADVERTISER` | Pre-filled from the advertiser's settings — `GET /api/admin/advertiser/{id}/` |
| `FIXED` | A system constant for CTV |
| `API` | Pre-populated from an API response |
| `MATCHED` | Worked out by the agent from what the plan already knows |
| `PLATFORM` | Set by the platform, not by the agent (**new in v4.0**) |

`PLATFORM` is added because two values previously attributed to the agent are in fact set server-side: the per-format budget allocation, and the two brand-safety flags.

---

### 5.4 Step 1 — Basics

Merges v1.1.0's Steps 1 and 2 (strategy details plus goal, KPI and bid), adds creative durations, and is scoped to CTV.

| Field | Type | Requirement | Source | Notes |
|---|---|---|---|---|
| Strategy name | `str` | Optional | `GENERATED` | Composed from the brief; the trader can rename. Uniqueness checked via `GET /api/strategies/check_strategy_name_uniqueness/` |
| Flight dates | Date range | Required | `INFERRED` | `lower >= today`, `upper > lower`. Held as a list of ranges — see §5.11 |
| Target markets | `list[str]` | Required | `INFERRED` | ISO country codes. One market per strategy in M1; field remains a list. **Verified:** only `GB` and `US` exist on the platform |
| Primary currency | `str` | Optional | `ADVERTISER` | **Corrected from `DERIVED`.** An advertiser default, not derived from the market. See §4.6 |
| Creative durations | `list[int]` | Required | `INFERRED` | Values 10, 15, 20, 30, 40, 45, 60 (**Verified** from `filter-properties`, seven distinct values, not four). Determines deal availability and CPM |
| Goal | `GoalEnum` | Required | `FIXED` | Always `AWARENESS` for CTV. Client rationale: CTV is hard to track further down the funnel. **Verified:** the platform pre-selects Awareness, and the inventory-sources call sends `goal=AWARENESS` before the trader has chosen one |
| KPI — **per format** | `KpiEnum` | Required | `INFERRED` | `REACH` or `FREQUENCY`. **Corrected:** held per format, not per strategy. Sent as `formats_and_kpis[]` |
| KPI target value — **per format** | `int` | Conditional | `ASKED` | 2–5 inclusive. Applies only where the KPI is frequency. **Observed:** the control offers 2, 3, 4, 5 — corrected from the 1–5 stated in review. A frequency of 1 is the absence of a frequency target, not a value for one |
| Market budgets | `Decimal`, one per market | Required | `INFERRED` | Must be `> 0`. Stored as `market_budgets: list[MarketBudgetBidSchema]` |
| Base bid | `Decimal`, one per market | **Required** | `ASKED` or `DERIVED` | **Contested — see D3.** Review concluded this does not apply to CTV. **Verified:** the platform blocks progress when it is empty, on a pure CTV plan, and almost all inventory is floor-rate |
| Frequency cap | `int` | Optional | `ADVERTISER` | Per week. May be locked — see §3.5 |
| Budget cap | `Decimal` | Optional | `ADVERTISER` | **Inferred** to behave like the frequency cap. **Open** |
| Formats | `list[FormatEnum]` | — | `FIXED` | `["streaming_tv"]` in the model. **The forecast payload must also send `prime_video`** where Prime Video inventory is in the plan — see §4.7.1 |
| Product categories | `list[str]` | Required | `ADVERTISER` then `INFERRED` | "for video" qualifier dropped — CTV is always video. Two-level hierarchy; **only leaf subcategories are selectable** (**Observed**). Values are long numeric strings. Valid values from `GET /api/contextual-targeting/{market}/product-categories/` |
| Conversion types | `list[str]` | Optional | `ASKED` | Four events: `PAGE_VIEW`, `ADD_TO_CART`, `CHECKOUT`, `APPLICATION`. Each carries a market flag. Collected here or at tracking — see §5.14 |
| Selected inventory sources | `list[InventorySource]` | Optional | `API` | Pre-filled from `GET /api/inventory-sources/`. **Verified:** returns `Amazon Streaming TV` and `Twitch` for a GB CTV awareness plan. Presented as removable, not as a question |

**Removed from this step:** selling location and product ASINs, both moved to tracking (§5.14); the three non-CTV format options; the four non-awareness KPIs (CTR, CPC, CPA, CPDPV).

**Strategy name convention**

```
{Category}_{Market}_{Goal}_{MonthYear}        e.g. Education_GB_Awareness_Sep2026
```

On a uniqueness collision the agent appends `_v2` and re-checks rather than stopping to ask.

**Open:** do traders already use a naming convention? Generating names in a different shape would make their own lists harder to scan. And if the category is not known when the name is composed, what stands in its place?

**Product category cross-check**

`POST /api/contextual-targeting/{market}/asin-validation/` returns a product category alongside each valid ASIN. ASINs are collected at tracking, well after this step, so that category cannot populate this field — but it is worth using as a cross-check. If the advertiser is set to Education and the ASINs return Electronics, the agent should say so rather than let the mismatch through.

**Open decision D6:** is the advertiser-level value a product **category** or an **industry**? The advertiser endpoints expose `get_industry_and_sub_industry_choices/`, while product categories come from an entirely different taxonomy. If the advertiser holds an industry, a mapping is required and does not currently exist anywhere.

**Pre-flight feasibility checks**

**Verified.** Four calls fire when formats are selected. They establish whether there is anything workable in the market before the trader invests effort.

```
GET /api/audience-sets/check_market_has_audience_set/?markets=GB
    -> [{"market":"GB","exists":true}]

GET /api/creatives/recs/check_market/?markets=GB
    -> [{"market":"GB","exists":true}]

GET /api/assets/check_market_has_assets/?markets=GB
       &target_types=DISPLAY,VIDEO,STREAMING_TV,MOBILE&dsp_approved=true
    -> [{"market":"GB","creative_type":"DISPLAY","exists":true}, ...]

GET /api/inventory-sources/?strategy_formats=streaming_tv&markets=GB&goal=AWARENESS
    -> [{"name":"Amazon Streaming TV","type":"AMAZON","formats":["streaming_tv"]},
        {"name":"Twitch","type":"AMAZON","formats":["streaming_tv"]}]
```

All four accept comma-separated markets and return an array, so a multi-market plan needs one call each rather than one per market.

Note that `dsp_approved=true` is part of the assets check — an asset existing is not sufficient; it must be approved by the DSP.

**API calls at this step**

```
GET /api/admin/advertiser/{id}/                              (session start)
GET /api/strategies/check_strategy_name_uniqueness/?name=
GET /api/contextual-targeting/{market}/product-categories/
GET /api/audience-sets/check_market_has_audience_set/?markets=
GET /api/creatives/recs/check_market/?markets=
GET /api/assets/check_market_has_assets/?markets=&target_types=&dsp_approved=true
GET /api/inventory-sources/?strategy_formats=&markets=&goal=
GET /api/conversions/definitions/                            (off-Amazon advertisers)
```

---

### 5.5 Step 2 — CTV inventory

Was v1.1.0's Step 3 "Deals", presented as a checkbox table. The review comment reversed the direction of the step: the trader states requirements and the agent finds the deals that fit.

| Field | Type | Requirement | Source | Notes |
|---|---|---|---|---|
| Channel | `list[str]` | Optional | `INFERRED` | Which providers to run on. **This is the strategic choice**; the deal underneath it is not. **Blocked** — no `channel` field exists on a deal |
| ROS or genre | `str` | Optional | `INFERRED` | Run-of-service or a named genre, used to narrow the match. **Blocked** — the `genre` field is unusable, see §12 |
| Selected deals | `list[SelectedDealSchema]` | Required | `MATCHED` | Matched on market, duration and channel, plus optional genre and the targeting requirements. Candidates from `GET /api/deals/` |
| Specific deal id | `str` | Optional | `ASKED` | Escape hatch for a trader with a particular deal in mind. Format cannot be validated — see §4.3.4 |
| Inventory tier — per deal | `InventoryTierEnum` | Required | `DERIVED` | **Blocked** — no source exists, see §12 |
| Targeting source — per deal | `TargetingSourceEnum` | Optional | `MATCHED` | Known only after matching. **Blocked** — capability is encoded in the deal name |
| CTV rate card | Reference | Read | `API` | `GET /api/rates/ctv/{market}/` |

**What the trader decides, and what the agent works out**

Choosing Prime Video over Netflix is a real decision. Choosing between `EXT7P75718S8MNR` and `EXT7P75719Q2LKM` is not. The trader supplies the channel, optionally a genre or run-of-service, and the targeting they want; the agent matches and returns what fits.

**What is surfaced**

Channel, effective CPM, and estimated impressions. Not deal identifiers, not raw deal names.

**Two things must surface even though the deal does not.** Both were established in review and both remain in force.

**Tier capability.** Third-party tiers return no reach forecast. If only the CPM is shown, the trader has no way to know that the reach figure is missing for part of the plan.

**Commercial commitment.** A Programmatic Guaranteed deal owes the full budget and cannot be paused. Hiding the deal must not hide that. The agent states it before the trader accepts the CPM:

> "This is a guaranteed deal, so the full £6,000 is committed and cannot be paused."

**A third, added in v4.0 — price certainty.** A floor rate and a fixed price look identical as a number and mean opposite things. Almost all VOW inventory is floor-rate, so the default case is the uncertain one. See D3.

**Graph node** renamed from `select_inventory` to `match_inventory_deals`.

#### 5.5.1 What the deals endpoint actually provides

**Verified.** 83 deals for a GB Streaming TV plan.

```
GET /api/deals/?search=&page_size=25&ordering=&page=1
    &markets=GB,ZZ
    &formats=streaming_tv,prime_video,UNKNOWN
    &deal_type=&ad_lengths=&genre=&sources=&devices=&publisher=
```

**Note the padded catch-all values.** `ZZ` is an unknown market and `UNKNOWN` an absent format. They include deals whose metadata is incomplete. **The agent should replicate this**, or deals with missing metadata will be silently excluded.

**A deal object — Verified, twelve fields**

```json
{
  "external_deal_id": "VIA-159-00100",
  "name": "3PS_Freewheel_UK_STV_Paramount_My 5",
  "deal_price_type": "FLOOR_RATE",
  "deal_price_amount": "22.96",
  "deal_price_currency": "GBP",
  "deal_type": "PRIVATE_AUCTION",
  "media_types":  [{"media_type": "VIDEO_STV", "bid_request_volume": 22156624.0,
                    "bid_request_volume_rate": 0.840}, ...],
  "devices":      [{"device_type": "CONNECTED_TV", "device_name": "SMART_TV",
                    "bid_request_volume": 14738262.0, "bid_request_volume_rate": 0.559}, ...],
  "environments": [{"environment_type": "APP", "bid_request_volume": 24890285.0,
                    "bid_request_volume_rate": 0.944}, ...],
  "locations":    [{"country_code": "GB", "bid_request_volume": 16049990.0,
                    "bid_request_volume_rate": 0.609}],
  "genre": null,
  "ad_lengths": []
}
```

**What can and cannot be matched on**

| Matching input | Available | Notes |
|---|---|---|
| Market | Yes | `locations[].country_code` |
| Duration | Partly | `ad_lengths` present, but empty on third-party deals |
| Channel | **No** | Only inside `name` |
| Inventory tier | **No** | Field does not exist |
| Genre | **No** | Field exists but is unusable — see §12 |
| Amazon-audience capability | **No** | Encoded in the deal name |
| Device | Partly | Populated on Amazon deals, empty on third-party |
| Volume | Partly | Real on Amazon deals, placeholder `1` on some third-party |

**Open decision D4** is the consequence: two of the three stated matching inputs are not available as fields. This is the one answer that determines whether this step can be built as specified.

#### 5.5.2 Filter properties

```
GET /api/deals/filter-properties/?formats=streaming_tv,prime_video,...
```

**Verified response:**

```json
{
  "genres": ["15, 20, 30","2026","2027","Action","Comedy","Drama",
             "RON","ROS","Suspense","TEST","Top Trending","Winter Holiday"],
  "ad_lengths": ["10","10","15","20","30","15","15","20","15","20","30","20","30","40","45","60"],
  "exchanges": ["DRAX Web Video","Freewheel Video","Pubmatic Web Video","Netflix Web Video",
                "Magnite Streaming Web Video","Prime Video ads","Microsoft Monetize",
                "Amazon Publisher Direct"],
  "devices": ["MOBILE","UNKNOWN","CONNECTED_TV","DESKTOP"]
}
```

Two implementation notes: `ad_lengths` is not distinct (16 entries, 7 distinct values), and `genres` contains years, a test label and an ad-length list. See §12.

#### 5.5.3 Channels and exchanges are different things

The deals screen names nine channels: Amazon Prime Video, Disney+, Multilocal, Discovery+, Paramount+, Hulu, Netflix, Pubmatic, Passion+.

These are not the same kind of thing:

```
Streaming services   Prime Video, Netflix, Disney+, Hulu, Paramount+, Discovery+, Passion+
Supply platforms     Pubmatic, Multilocal, and in the data also Freewheel, Magnite
```

"This deal is on Netflix" is useful to a trader. "This deal is on Freewheel" names the pipe, not the content. Where the agent surfaces a channel it should surface the streaming service, not the exchange.

#### 5.5.4 Curation capture

For the third-party-needs-curation tier, where deals cannot be selected yet. The agent records what VOW needs in order to curate later.

| Field | Type | Requirement |
|---|---|---|
| Curation genres | `list[str]` | Required for this tier |
| Curation durations | `list[int]` | Required for this tier |
| Curation targeting preferences | `str` | Optional |
| Curation budget | `Decimal` | Required for this tier |
| Curation flight dates | Date range | Required for this tier |

This pattern — record the requirement rather than select the deal — is exactly what the review comment asked for across all tiers. It was already present here and simply not applied where deals do exist.

#### 5.5.5 Genre upsell

Client requirement, carried forward: "based on the brief we can suggest whether a specific available genre would be a better match at a slightly higher CPM."

```
Prime Video ROS      $18.22 CPM
Prime Video Action   $22.07 CPM
```

**Dependent on D4.** With the genre field in its current state, this cannot be built.

**Open:** when several deals match, how should the agent choose — cheapest CPM, largest volume, or best genre fit? This is a commercial judgement rather than a technical one, and it needs a stated rule because it applies to every plan.

**Open:** when nothing matches, should the agent widen the duration, drop the genre, or report back and ask?

**Open:** should a Programmatic Guaranteed deal ever be matched automatically, given the budget commitment, or only when the trader has asked for one?

**API calls at this step**

```
GET /api/deals/
GET /api/deals/filter-properties/
GET /api/rates/ctv/{market}/
```

---

### 5.6 Step 3 — Audiences

Optional, suggestion-driven. The review comment reverted v2.0's promotion of this step to mandatory.

| Field | Type | Requirement | Source | Notes |
|---|---|---|---|---|
| Audience prompt | `str` | Optional | `GENERATED` | **New in v4.0.** Natural language, composed from the brief. **Verified** to be how the platform's own suggest flow works |
| Audience options | 3 profiles | Optional | `API` | Agent always generates narrow, balanced and wide from the returned flat list |
| Chosen option | `AudienceProfileEnum` | Optional | `ASKED` | The trader picks one, or declines all three |
| Match type | `MatchTypeEnum` | Conditional | `ASKED` | `SIMILAR` or `EXACT`; `EXACT` by default. Applies only where an audience is chosen |
| Audience data sources | `list[AudienceDataSourceEnum]` | Required | `DERIVED` | Which providers are in play. Drives the fee — see §4.5.5 |
| Effective CPM per option | `Decimal` | Read-only | `DERIVED` | Deal CPM plus audience fee, shown per option |

**Declining all three is a valid plan.** It is a run-of-service baseline, and because no first-party data is used it incurs no data fee — so it is the cheapest option, not a degraded one.

**Consequence for the repair loop.** Widening the audience is one of the levers used when reach falls short. Where no audience has been chosen that lever does not exist, and the agent should say plainly when it has nothing left to relax rather than implying a fix is available.

**Audiences are one kind of targeting.** Per the review comment, the trader is not presented with "audiences" and "targeting" as two subjects. Geography can substitute for audience targeting entirely — a trader who wants postcodes rather than segments has made a complete targeting decision. Note that geography carries no data fee, so substituting it is also cheaper.

**What is sent at creation**

```json
"markets_info": [{
  "market": "GB",
  "audience_targeting": [
    {"audience_set_id": "26f2cbb3-d815-4148-b935-1407a91b60c4",
     "audience_type": "AUDIENCE_SET"}
  ]
}]
```

Per market, not campaign-level.

**API calls at this step**

```
GET  /api/audience-sets/                            list existing sets
POST /api/audience-sets/suggest/                    -> returns an id
GET  /api/audience-sets/suggest/{id}/               read the result
GET  /api/contextual-targeting/fees                 read the fee, never assume it
POST /api/audiences/{market}/overlapping-audiences/ detect cross-provider overlap
```

**Open decision D2** — a real request and response from the suggest endpoint. Also: does `SuggestAudienceGroupsInput` mean the caller can request a number of groups? If the endpoint can group, the agent may not need its own logic. And how long does the asynchronous call take, since that decides whether the agent waits in the conversation.

---

### 5.7 Step 4 — Reach forecast

Was embedded in v1.1.0's flow. A first-class step, with a stated honesty rule.

#### 5.7.1 What the endpoint actually takes

**Verified.** This is materially narrower than every earlier revision assumed.

```
POST /api/strategies/reach-forecast/
```

```json
{
  "flight_dates": {"lower": "2026-09-01", "upper": "2026-09-30"},
  "formats": ["streaming_tv", "prime_video"],
  "goal": "AWARENESS",
  "market_budgets": [{"market": "GB", "budget": 10000,
                      "base_bid": "25", "currency": "GBP"}]
}
```

**Four inputs. No deals, no audiences, no targeting.**

**Note the field name.** This endpoint calls the bid `base_bid`; the create endpoint calls it `base_supply_bid`. The same value, two names.

#### 5.7.2 What it returns

**Verified.**

```json
{
  "total_reach": 233803,
  "total_impressions": 860716,
  "market_reach": [{
    "market": "GB", "reach": 233803, "budget": "10000.00",
    "currency": "GBP", "impressions": 860716,
    "supplies": [
      {"supply": "DSP_STREAMING_TV",
       "est_spend": 4931.712321976001, "est_reach": 132713, "max_reach": 285186,
       "est_impressions": 647856, "max_impressions": 6759074,
       "avg_cpm": "7.60", "max_cpm": "14.98"},
      {"supply": "DSP_PRIME_VIDEO",
       "est_spend": 5068.2876889, "est_reach": 71120, "max_reach": 950000,
       "est_impressions": 212860, "max_impressions": 52757286,
       "avg_cpm": "23.98", "max_cpm": "23.98"}
    ]
  }]
}
```

**Five things this response establishes**

**1. Supplies are keyed by format.** `prime_video` must be sent or its supply line is absent — see §4.7.1.

**2. Budget is split by the endpoint**, and not evenly: 4,931.71 and 5,068.29 against a £10,000 budget. This is an optimisation, and it differs from the even split the platform stores at creation (§5.11).

**3. `est_` and `max_` pairs give the deliverability ceiling.** This is what the repair loop actually needs. When reach falls short, the first question is not "should I widen the audience" but "is more reach available at all". Where `est_reach` already equals `max_reach`, no lever will help.

**4. The forecast CPMs are not the deal CPMs.** The selected deals were £24.79 and £34.80; the forecast returned £7.60 and £23.98. The response is internally consistent, so this is a different concept rather than an error — a blended supply average against a specific deal price. See §4.5 of the traceability note in D3.

**5. Impressions sum; reach does not.** See §4.8.1.

#### 5.7.3 Fields presented to the trader

| Field | Availability |
|---|---|
| Estimated impressions | All tiers |
| Indicative CPM | All tiers |
| Estimated unique reach | Amazon-owned only |
| Average frequency | Amazon-owned only, derived |
| Reach curve | Amazon-owned only |
| Maximum available reach | Amazon-owned only |

#### 5.7.4 The honesty rule for third-party inventory

For Netflix, Disney+ and other third-party tiers the agent shows the rate-card CPM and derived impressions, states explicitly that reach is unavailable and why, and never invents a reach figure.

Consequences, both carried from review:

- The repair loop applies only to the Amazon portion
- Total reach cannot be summed across providers, since there is no cross-platform deduplication

#### 5.7.5 The repair loop

| v1.1.0 | v4.0 |
|---|---|
| If `estimated_unique_reach == 0`, switch from Narrow to Balanced or Broad | If reach is insufficient, extend the audience — which may mean adding segments within the chosen profile rather than switching profiles |
| Also adjust the base CPM bid upward | **Contested.** Removed in review on the grounds that CTV CPMs are fixed. Almost all VOW inventory is floor-rate, where a bid does apply. See D3 |
| Re-run the forecast | Unchanged |

**Levers available, and what removes each**

| Lever | Removed when |
|---|---|
| Widen the audience | No audience was chosen (§5.6) |
| Raise the bid | Deal is fixed-CPM. **Present on floor-rate deals — see D3** |
| Relax the device targeting | The advertiser setting is locked (§3.5) |
| Relax the geography | Trader chose geography deliberately as their targeting |
| Widen the inventory | Available, but third-party tiers return no forecast, so the effect cannot be verified |
| Increase the budget or extend the flight | Commercial decision, not the agent's to make |

Where the agent has nothing left to relax it must say so, and name the levers it could not use.

#### 5.7.6 The repair loop does not exist in the product

**Verified, and material.** Two audience-aware forecast endpoints exist:

```
POST /api/audience-sets/reach-forecast/
POST /api/strategies/{id}/audiences/reach-forecast/
```

**Nothing in the product calls either of them.** The one forecast the product runs is on the summary screen and takes no audience input. The Planner, after creation, is a budget and bid editor with no forecast at all.

So the repair loop as specified is a **new capability**, not a description of existing behaviour. That is a legitimate thing to build, but it should be a decision rather than an assumption.

**Open decision D7:** build the audience-aware repair loop in M1, or match the product's single pre-creation forecast for the first release?

**API calls at this step**

```
POST /api/strategies/reach-forecast/                        (the product's forecast)
POST /api/audience-sets/reach-forecast/                     (exists; unused by the product)
POST /api/strategies/{id}/audiences/reach-forecast/         (exists; unused; post-creation)
```

---

### 5.8 Step 5 — Finalise plan

Reduced from an approval gate to a status change, per review.

| Field | Type | Requirement | Source |
|---|---|---|---|
| Plan status | `PlanStatusEnum` | Required | `ASKED` |
| Finalised by | `str` | Set on finalisation | `DERIVED` |
| Finalised at | `datetime` | Set on finalisation | `GENERATED` |

```
DRAFT -> FINALISED
```

**What this removes.** An approval gate meant a second person: a notification, a wait of unknown length, a rejection route, a threshold rule deciding when approval was needed, and roles saying who could give it. All of that leaves M1.

**It also removes a place where the graph had to stop.** The step used a LangGraph `interrupt()`, halting and persisting state until someone else acted. That interrupt is gone.

**The interrupt at creative approval stays**, and correctly so — there the agent waits on Amazon's or a publisher's review, which is genuinely external and asynchronous. Pausing for a review the platform performs is not the same as pausing for a colleague.

**Kept deliberately extensible**, because the review comment said "for now":

- `PlanStatusEnum` is its own enum rather than a reuse of `ApprovalStatusEnum`. The plan and the creative have different lifecycles, and sharing one enum would force each to carry values the other cannot use. Adding `PENDING_APPROVAL` later is then additive.
- Fields renamed from `approval_status`, `approved_by`, `approved_at` to `plan_status`, `finalised_by`, `finalised_at`.

**Where approval may return is not as a manager gate** but as an advertiser-level rule — "plans over £10,000 need my sign-off". Leaving room for `approval_threshold` on the advertiser settings costs nothing now.

**No API call.** This is agent-internal and logged in the audit trail.

**Open:** which endpoint records the status change, if any should? Nothing in the API covers a plan status as distinct from `POST /api/strategies/{id}/set_status/`, which is activation.

**Open:** can a finalised plan return to `DRAFT`, and what can still change after finalisation? Budget and matched deals are commercial commitments and are not obviously in the same category as, say, targeting.

**Draft mechanics — Verified**

The platform's own draft is a separate concept from the plan status above. `Save as draft` is disabled on step 1 and enabled from step 2, so a draft is created deliberately rather than automatically. Drafts carry `budget: null` and `status: "6_inactive"`, and the payload includes `current_step` — **Inferred** to be how a draft resumes.

---

### 5.9 Step 6 — Create the strategy

One POST. Everything gathered in Phase A is assembled into the payload.

#### 5.9.1 Which endpoint

**Contested.** Three candidates exist and all three are real.

| Endpoint | Status |
|---|---|
| `POST /api/strategies/` | **Verified** — this is what the product's own wizard uses |
| `POST /api/simple-strategies/` | Exists, model `SimpleStrategyCreate`, **POST only** — no read or update. Identified in review as the likely CTV variant |
| `POST /api/automated-strategies/` | Exists, models `AutomatedStrategyCreate` and `AutomatedStrategyFormatsAndKpis` |

The third is worth attention: strategies already carry an `is_automated` boolean, and the name suggests it may be closer to what an agent needs than the other two.

**Open decision D5** — which endpoint, and the full field list for whichever it is. The payload described below is what the product sends to `POST /api/strategies/` and is **Verified**; if a different endpoint is chosen the payload needs re-verifying against it.

Note that `simple-strategies` supports POST only, so a strategy created through it would have to be read and updated through the general endpoint. That is worth stating because it reads as inconsistent otherwise.

`strategies-sp` is a separate family with its own draft endpoints. **Open:** confirming it is sponsored products and irrelevant to CTV would close it off.

#### 5.9.2 The verified payload

**Verified** against the live creation of `VMA2026368`.

```json
{
  "name": "CTV Test GB Sep2026 KA",
  "flight_dates": {"lower": "2026-09-01", "upper": "2026-09-30"},
  "goal": "AWARENESS",
  "primary_currency": "EUR",
  "product_location": "NOT_SOLD_ON_AMAZON",
  "current_step": 5,

  "formats_and_kpis": [
    {"format": "streaming_tv", "kpi": "REACH"},
    {"format": "prime_video",  "kpi": "FREQUENCY", "kpi_target_value": 3}
  ],

  "markets_info": [{
    "market": "GB",
    "base_supply_bid": "25",
    "budget": 10000,
    "currency": "GBP",
    "audience_targeting": [
      {"audience_set_id": "26f2cbb3-d815-4148-b935-1407a91b60c4",
       "audience_type": "AUDIENCE_SET"}
    ]
  }],

  "market_deals": [{
    "market": "GB",
    "deals": [ /* complete deal objects, not identifiers */ ]
  }],

  "selected_inventory_sources": [
    {"name": "Amazon Streaming TV", "type": "AMAZON"},
    {"name": "Twitch", "type": "AMAZON"}
  ],

  "video_product_categories": ["304861615492321169", "345704700972773738"],
  "product_categories": [],
  "audience_targeting_match_type": "EXACT",
  "conversion_types": ["PAGE_VIEW", "CHECKOUT"],
  "product_asins": [],

  "assets": [{"id": "d246bc9a-3bfc-4696-928a-eebfc5cc5aef", "name": "VOWtestVid1"}],
  "pre_approved_creatives": [],
  "rec_creatives": [],
  "third_party_creatives": []
}
```

**Seven implementation notes**

1. **Complete deal objects are sent back, not identifiers.** The agent cannot discard the deals list after matching.
2. **The bid field is named differently here** than on the forecast endpoint: `base_supply_bid` versus `base_bid`.
3. **`formats_and_kpis` carries the KPI and its target value per format**, as a list of pairs.
4. **Two category fields exist** — `product_categories` for display and `video_product_categories` for video. CTV populates the second and sends the first empty.
5. **All four creative arrays must be present**, three of them empty.
6. **`product_asins` is sent empty** and attached later — see §5.14.
7. **`current_step` is part of the payload.** **Inferred** to drive draft resumption.

#### 5.9.3 The response

**Verified.** `201 Created`, and a **subset** of what was sent.

```json
{
  "id": "VMA2026368",
  "name": "CTV Test GB Sep2026 KA",
  "goal": "AWARENESS",
  "primary_currency": "EUR",
  "flight_dates": {"lower": "2026-09-01", "upper": "2026-09-30", "timezone": "UTC"},
  "product_categories": [],
  "video_product_categories": ["304861615492321169", "345704700972773738"],
  "enable_fraud_invalid_traffic_targeting": false,
  "enable_brand_safety_targeting": false,
  "audience_targeting_match_type": "EXACT",
  "conversion_types": ["PAGE_VIEW", "CHECKOUT"],
  "selected_inventory_sources": [...],
  "is_archived": false,
  "is_readonly": false
}
```

`markets_info`, `market_deals`, `assets` and `formats_and_kpis` are **not** returned. A read-back is required to confirm them.

**Two fields appear in the response that were not in the request:**

```json
"enable_fraud_invalid_traffic_targeting": false,
"enable_brand_safety_targeting": false
```

**Both are server-set and both default to off.** Neither appears anywhere in the wizard, so a trader has no way to know brand-safety targeting is disabled.

**Open:** should the agent set `enable_brand_safety_targeting` to true by default, or surface it as a choice? Leaving it off silently seems wrong for a brand-sensitive advertiser, and this is exactly the kind of thing an advertiser-level policy would govern.

#### 5.9.4 What happens after the 201

**Verified.** The created strategy lands in `Paused` / `Inactive` and synchronises to Amazon DSP in the background.

```
Modal:  "Your strategy has been created! VOW will publish and synchronise
         your strategy with Amazon in the background."

Overview:  Status  Paused
           Syncing (spinner)
           Inactive
```

**This answers a question v2.0 left open** — a created strategy does land in a paused, inactive state, so activation via `set_status` remains a separate step.

**And it establishes something the schema did not say: creation does not mean the campaign exists on Amazon.** See §5.18.

**API calls at this step**

```
POST /api/strategies/                              (or one of the two alternatives)
GET  /api/strategies/{id}/                          read-back
GET  /api/reports/performance-metrics/?strategy_id= 
```

---

## Phase C — Attach

Steps 7 to 12 run in parallel. None waits on another. Each writes back to a strategy that already exists.

### 5.10 Step 7 — Targeting

**Moved from v2.0's step 5.** The reason is §5.1's first constraint: every targeting endpoint requires a strategy identifier.

| Field | Type | Requirement | Source | Default |
|---|---|---|---|---|
| Location | `list[str]` | Optional | `DERIVED` | **The market's country.** `markets = ["GB"]` gives `location = ["GB"]` |
| Instream position | `InstreamPositionEnum` | Optional | `ASKED` | None |
| Content-category exclusions | `list[str]` | Optional | `ADVERTISER` | The advertiser's brand-safety exclusions, where it has any. **Open** |
| Device type | `list[str]` | Optional | `ADVERTISER` | The advertiser's setting. **May be locked** — see §3.5 |
| Mobile environment | `MobileEnvEnum` | Conditional | `ASKED` | None. Applies only where Mobile or Tablet is among the device types |

**No field in this step starts empty.** The trader is never asked to fill a blank targeting form. Per review: the trader is shown a default baseline already applied — country targeting and Connected TV device — and then either refines it or accepts it as sufficient.

**Three ways to proceed, and they are alternatives rather than a sequence:**

- define audience segments (which happened at step 3)
- narrow the geography instead — down to a region, a city, or postcodes
- accept the baseline as it stands

**`markets` and `location` are different fields**, even though both usually say GB:

| | Question it answers | What it decides |
|---|---|---|
| `markets` | Which market are we buying in? | Which deals exist, which rate card, which currency, which category and location lists |
| `location` | Where should the ad be allowed to show? | Geographic delivery |

They start the same and diverge as soon as the trader narrows. Buying GB inventory but delivering only in London is `markets = ["GB"]` with `location = ["London"]`.

**Narrowing costs reach, and the agent should report it.** Moving from a country to a handful of postcodes can cut the addressable audience sharply. Since the trader did not see a forecast when they narrowed, the agent should state the effect rather than let the shortfall appear later as a surprise.

**Format and device type are different things.** See §4.7.2. Restricting to Connected TV has two effects the trader did not choose: available inventory shrinks, because a large share of streaming viewing happens on mobile; and Connected TV inventory is priced above mobile, so the CPM rises and the same budget buys fewer impressions. Since this comes from the advertiser rather than the brief, the agent should surface both effects.

**Config-driven, not hard-coded.** Client requirement, carried forward: "This targeting list frequently changes so it should be easy to add new targeting types." Adding a targeting type should be a configuration change, not a code change.

**Not supported today** (future scope): genre exclusions, day-parting, language.

**Postcode support — Verified.** `POST /api/strategies/postcode-validation/{market}/` exists, so the postcode example from review is buildable. This closes a question v2.0 left open.

**An endpoint that may replace this logic entirely.** `POST /api/strategies/{id}/targeting/auto-rec/` (model `StrategyTargetAutoREC`) recommends targeting automatically. The default baseline described above may not need to be assembled agent-side at all.

**Open:** what does `auto-rec` return, and should the agent use it rather than building a baseline?

**Open:** are `Connected TV`, `Mobile`, `Tablet` and `Desktop` the full set of device types, and does that list come from an endpoint?

**API calls at this step**

```
GET/POST /api/strategies/{id}/targeting/
POST     /api/strategies/{id}/targeting/auto-rec/
GET/POST /api/strategies/{id}/targeting/{market}/locations/
GET/POST /api/strategies/{id}/targeting/{market}/product-categories/
GET/POST /api/strategies/{id}/targeting/{market}/products/
POST     /api/strategies/postcode-validation/{market}/
GET      /api/strategies/locations/{market}/
POST     /api/contextual-targeting/{market}/products/
```

---

### 5.11 Step 8 — Budget and bid allocation

**Moved from v2.0's step 3, and substantially rewritten.** v2.0 treated the budget split as agent-side logic performed before creation. The platform performs it itself, at creation, and exposes the result for editing.

#### 5.11.1 What the platform does

**Verified.** One market budget was submitted; two allocations were stored.

```
Submitted     markets_info[0].budget = 10000       (GBP)
                                                    -> EUR 10,909.09

Stored        Market total       EUR 10,909.09
              Streaming TV       EUR  5,454.55
              Prime Video        EUR  5,454.55      exactly even

Bid           Submitted  base_supply_bid = "25"    (GBP)
              Stored     Streaming TV  EUR 27.27
                         Prime Video   EUR 27.27    per format, separately editable
```

**Three numbers, three different concepts.** This is worth stating clearly because earlier revisions conflated them:

| Number | Value in the test plan | What it is |
|---|---|---|
| Forecast `est_spend` | 4,931.71 / 5,068.29 | A prediction of where spend will land, optimised |
| Platform allocation | 5,454.55 / 5,454.55 | The stored cap per format, split evenly |
| Agent's proposed split | Whatever the agent computes | A recommendation |

#### 5.11.2 Multiple flight ranges

**Verified.** A strategy supports several flight ranges, each with its own budget, and dedicated endpoints exist:

```
GET/POST    /api/strategies/{id}/flight-ranges/
PUT/PATCH   /api/strategies/{id}/flight-ranges/{id}/
PUT/PATCH   /api/strategies/{id}/flight-ranges/budget/{id}/
DELETE      /api/strategies/{id}/flight-ranges/{id}/
```

The full budget granularity is therefore:

```
strategy -> flight range -> market -> format -> budget
```

Earlier revisions modelled a single flight date range. **Open:** are multiple flight ranges needed in M1, or is one enough for the first release?

#### 5.11.3 What the agent contributes

Given that the platform allocates evenly and allows editing, the agent's role here is narrower than v2.0 assumed.

| Field | Type | Requirement | Source |
|---|---|---|---|
| Split by format | Allocation | Optional | `MATCHED` |
| Split by duration | Allocation | Optional | `MATCHED` |
| Split method | `SplitMethodEnum` | Required where a split is proposed | `GENERATED` |
| Per-format allocation | `Decimal` | — | `PLATFORM` |

**Split methods**

```
EVEN_BY_BUDGET        equal spend per format or duration; impressions differ,
                      because a higher CPM buys fewer
EVEN_BY_IMPRESSIONS   equal impressions; spend differs, because a higher CPM
                      requires more
```

The agent must state which it chose and why, so the trader can adjust:

> "I have split evenly by impressions, which weights spend toward the 30-second creative at its higher CPM."

**Why a split matters at all.** Each format and each duration carries a different CPM, so a real split produces an accurate impression estimate. Without one the agent must present a blended estimate and should say so. The size of the error depends on how far the CPMs diverge:

```
CPMs close     Prime £24, Netflix £22
               Split      208,333 + 227,273 = 435,606
               Blended £23                  = 434,783
               Error 823 impressions, immaterial

CPMs far       Prime £40, Netflix £15
               Split      125,000 + 333,333 = 458,333
               Blended £27.50               = 363,636
               Error 94,697 impressions, 26 per cent
```

**Recommendation:** the agent proposes a split only where the CPMs diverge enough to matter, and otherwise accepts the platform's even allocation and explains it. **Open decision D9** covers whether this is the intended division of labour.

**Also on this screen — Verified.** `Duplicate strategy` exists (`POST /api/strategies/duplicate/`), which explains the `(1)` and `(2)` suffixed names in the strategy list.

---

### 5.12 Step 9 — Upload video creative

Was v1.1.0's step 5, simplified to video only, with a duration check added.

| Field | Type | Requirement | Source | Notes |
|---|---|---|---|---|
| Video file | Upload | Required | `ASKED` | Always video for CTV. No display creatives, no responsive e-commerce |
| Click-through URL | `Optional[HttpUrl]` | Optional | `ASKED` | Nothing on a television screen can be clicked. **Recommended** where device types include mobile, tablet or desktop |
| Duration | `Decimal` | Checked | `API` | **Verified** to be a structured field on the asset — `"30.00"`, `"20.00"`, `"10.00"`. No derivation needed |

**Click-through URL — Verified on the platform.** Approved Streaming TV creatives exist with `click_through_url: null`, confirming the review comment. The call to action on CTV takes other forms — a QR code in the creative, an on-screen or spoken prompt, or brand recall — and measurement comes from the ASINs or the ad tag rather than from a click.

**A refinement.** Device types come from the advertiser and may include mobile, tablet or desktop, where the ad *can* be clicked. So "optional for streaming TV" is two cases: with Connected TV alone there is nothing a URL could do, while with mobile or desktop in the mix a URL is worth having.

**Open:** the API has a model named `MarketWithClickthroughUrl`. Is the URL held **per market**? For a multi-market campaign that matters, and this document currently treats it as a single value.

**Open:** are QR codes permitted in CTV creatives, and is there a specification for them? If that is the practical call to action it is worth naming here.

#### 5.12.1 Asset and creative are two different objects

**New in v4.0 — Verified.** Earlier revisions treated these as one thing. They are two levels.

| | **Asset** — `/api/assets/` | **Creative** — `/api/creatives/` |
|---|---|---|
| What it is | The video file | The file registered on Amazon, for one market, with a click-through URL |
| Identifier | `id` | `id` **and** `amz_id` |
| Carries | dimensions, `duration`, file size, url, language, `markets` (a list), past metrics | `type`, `market` (single), `approval_status`, `click_through_url` |
| Approval | filtered by `dsp_approved` | its own `approval_status` field |

**One asset produced 25 creatives** in the test data — all approved, all `market: GB`, differing only in `type` and `click_through_url`.

```
GET /api/creatives/?approval_status=APPROVED&markets=GB&asset={id}&no_pagination=true
```

Note `no_pagination=true`, which returns the complete set in one call.

**Creative `type` takes two values — Verified:** `"Video"` and `"Streaming TV Video"`. The same asset can be registered as both. **A CTV plan needs `Streaming TV Video`.**

**The agent's deterministic filter:**

```
type == "Streaming TV Video"  and  market matches  and  approval_status == "APPROVED"
```

**Duration matching is free**, because `duration` is structured:

```
deal.ad_lengths   ["15", "20"]
asset.duration    30.00, 20.00, 20.00, 10.00
                  -> only the two 20-second assets match that deal
```

**Assets carry past metrics — Verified.** `impressions`, `ctr`, `ecpm` and others. The agent can therefore say "this creative has run before and delivered a 57.8% CTR" rather than treating every asset as new.

**Note:** the same video appeared twice in the test data at different resolutions — same name, same URL, different `id`. The agent should group these rather than presenting them as two options.

**Duration match check.** If the uploaded video is 30 seconds but the plan specified 15-second deals, the economics change — a different CPM means different impressions for the same budget. This returns to step 5 with the amended plan.

**Removed for CTV:** browsing existing assets as the primary path, pre-approved creative selection, responsive e-commerce creatives, third-party tags. All valid for display, none for CTV.

**Upload path**

```
POST /api/assets/amz_assets/gen_upload_urls/     obtain upload URLs
POST /api/assets/amz_assets/register/            register the asset on Amazon
```

---

### 5.13 Step 10 — Creative approval

Every video must pass the platform's content and technical review before it can run. Each platform reviews its own inventory independently. A plan can be fully approved and funded and still not launch until the creative clears.

| Field | Type | Requirement | Source |
|---|---|---|---|
| Creative approval statuses | `dict[str, ApprovalStatusEnum]` | Read-only | `API` |

Per review, the three hard-coded publisher rows become one field holding a status per channel, keyed by the channels the plan actually matched:

```json
{"Prime Video": "APPROVED", "Netflix": "PENDING", "Channel 4": "PENDING"}
```

**Keys are data; values are an enum.** Publisher names change and are market-specific — the UK has ITVX and Channel 4, the US has Hulu and Peacock — so a row per publisher would not scale past one market, and adding one would require a schema change, a migration and a release to add a name. The set of states (`PENDING`, `APPROVED`, `REJECTED`) is stable and the agent's logic depends on it, so that stays typed.

**This is the same rule the targeting step already carries** — that a frequently changing list must be config-driven. It was written down and not applied here.

**Blocked — Verified.** A creative object carries `market` and `approval_status` with **no channel dimension at all**:

```json
{"market": "GB", "approval_status": "APPROVED", "type": "Streaming TV Video"}
```

The granularity on the platform is creative × **market**, not creative × channel. The dictionary above cannot be populated from current data.

**This blocks more than this step.** The activation checklist at §5.16 includes "approved by every channel". If per-channel statuses are not readable, that prerequisite cannot be evaluated, and activation either blocks indefinitely or has to trust the trader.

**Open decision D10.**

**On rejection:** the agent reports the reason and asks for a replacement, returning to step 9.

**Interrupt.** This step retains a LangGraph `interrupt()`. The wait here is on an external reviewer and is genuinely asynchronous, unlike the plan-approval wait that was removed at §5.8.

**Open:** where should the channel list come from — `GET /api/admin/advertiser/get_channels_choices/`, or derived from the matched deals? The endpoint exists; deriving from matched deals gives only the channels in play.

**Open:** is the status held per channel, or per creative-and-channel pair? A plan with a 15-second and a 30-second creative could have one approved and the other not on the same channel.

---

### 5.14 Step 11 — Tracking setup

ASIN validation was in v1.1.0's step 1 and ad-tag conversions in its step 2. Both now sit here.

| Field | Type | Requirement | Source | Notes |
|---|---|---|---|---|
| Sells on Amazon | `ProductLocationEnum` | Required | `ADVERTISER` | Moved from basics. Comes from the advertiser, so the agent already holds it at creation |
| Product ASINs | `list[str]` | Required if endemic | `ASKED` | Sent empty at creation, attached here |
| Sells on own website | `bool` | Asked here | `ASKED` | |
| Ad tag registered | `bool` | Required if selling off Amazon | `API` | If not registered, the agent shows setup instructions. **The tag must be installed before the campaign runs** — tracking only records activity after it goes live |
| Ad tag conversions | `list[str]` | Required if an ad tag exists | `ASKED` | Four events, each carrying a market flag |

**How the timing question resolves.** v2.0 flagged twice that `product_location` is required by the create payload yet was being collected after creation. Both halves are now closed:

- `product_location` comes from the advertiser's settings, loaded at session start, so the agent holds it at creation — nothing needs patching
- `product_asins` is sent as `[]` at creation and attached here through `PATCH /api/strategies/{id}/`

**Verified on the platform:** an invalid ASIN blocks progress on an On-Amazon plan; an Off-Amazon plan accepts zero ASINs. Off-Amazon advertisers may still supply ASINs to monitor halo sales.

**Open:** should the ASIN list be validated in one call here, or as the trader pastes them? Validating late means a trader can enter twenty ASINs and only then learn that three are wrong.

**Open:** can conversions be skipped entirely — activating with no conversion tracking — or is at least one always required?

**API calls at this step**

```
POST /api/contextual-targeting/{market}/asin-validation/
GET  /api/conversions/definitions/
PATCH /api/strategies/{id}/
```

---

### 5.15 Step 12 — Credit check

Credit is checked only at activation, not during planning. Everything before this point is a costless plan.

| Field | Type | Requirement | Source |
|---|---|---|---|
| Account balance | `Decimal` | Read-only | `API` |
| Strategy budget | `Decimal` | Read-only | `DERIVED` |
| Sufficient | `bool` | Derived | `DERIVED` |

```
GET /api/credits/summary/?advertiser={uuid}
```

**Verified:** the same figure appears in the platform header — "Credit available EUR 999,889.82".

If insufficient, the agent prompts a top-up via `POST /api/credits/` or `POST /api/credits/stripe/`.

**Open:** is the credit check genuinely order-free? Its outcome can change the budget, which would argue for running it before the plan is finalised rather than alongside the creative work.

---

## Phase D — Activate

### 5.16 Step 13 — Activate

The single spend action in the entire flow. Everything before this was free.

**A join node, not just a step.** Because the Phase C branches run in any order, this is where completeness is checked. Removing the order made an explicit checklist necessary — previously the order itself was the guarantee.

| Prerequisite | Holds when |
|---|---|
| Creatives uploaded | One per duration in the plan — a plan with 15-second and 30-second inventory needs both |
| Creatives approved | Every matched channel has returned `APPROVED`. **Blocked — see §5.13** |
| Targeting written | The baseline is applied, or the trader's refinement is saved |
| Budget allocated | Per format, and accepted or edited |
| Ad tag registered | The advertiser does not sell on Amazon and a tag is in place |
| ASINs attached | The advertiser does sell on Amazon and the ASINs validated |
| Conversions chosen | Selected, or explicitly skipped |
| Credit sufficient | Balance is at least the strategy budget |

```python
class ActivationPrerequisitesSchema(BaseModel):
    """Checked at the join node before any spend."""
    creative_uploaded: dict[str, bool]                  # per duration: {"15": True, "30": False}
    creative_approved: dict[str, ApprovalStatusEnum]     # per channel: {"Prime Video": APPROVED}
    targeting_written: bool = False
    budget_allocated: bool = False
    ad_tag_registered: Optional[bool] = None             # None when not applicable
    asins_attached: Optional[bool] = None                # None when not applicable
    conversions_chosen: bool = False                     # True if chosen or deliberately skipped
    credit_sufficient: bool = False

    @property
    def ready_to_activate(self) -> bool:
        return (
            all(self.creative_uploaded.values())
            and all(s == ApprovalStatusEnum.APPROVED for s in self.creative_approved.values())
            and self.targeting_written
            and self.budget_allocated
            and (self.ad_tag_registered is not False)
            and (self.asins_attached is not False)
            and self.conversions_chosen
            and self.credit_sufficient
        )

    def blocking_reasons(self) -> list[str]:
        """Every unmet prerequisite, so the agent can report all of them at once
        rather than one per attempt."""
        ...
```

Two prerequisites are new in v4.0 — `targeting_written` and `budget_allocated` — because both moved into Phase C.

**The document already implied this checklist without stating it.** The creative-approval step notes that "a plan can be fully approved and funded and still not launch until the creative clears". That is a launch gate described in prose.

```
POST /api/strategies/{id}/set_status/
```

**Open:** is the prerequisite list complete? And is there an endpoint that reports activation readiness, or is the agent expected to assemble it from the individual checks?

---

### 5.17 Post-creation update rules

**New section.** Per review, a strategy can be updated after creation:

```
PATCH /api/strategies/{id}/          model StrategyUpdate
```

This is what makes Phase C's parallelism possible. Removing the order between the creative, tracking and targeting branches only works if those branches can write back to a strategy that already exists. The two are one change seen from two sides: *no order necessary* is the behaviour, *updatable after creation* is the mechanism.

**But not everything should be freely updatable.** The review answer concerned the measurement fields and should not be read as "anything may change". Some fields carry money.

| Safely updatable | Needs a guardrail | Why |
|---|---|---|
| `product_asins` | `market_budgets` | A guaranteed deal already owes the full budget |
| `product_location` | `market_deals` | The deal is booked |
| Ad tag, `conversion_types` | `flight_dates` | Tied to the booking |
| Creatives, assets | `markets` | Invalidates the whole plan |
| Targeting, frequency cap | | |

Without that distinction, someone will patch a budget on a strategy whose Programmatic Guaranteed deal has already committed it, and the plan and the commitment will disagree.

**Open decision D11:** which fields are updatable and which fixed? The table is a proposal.

**Open:** does "after creation" extend to "after activation"? A live campaign is a different case from one created but not yet launched.

**Open:** does an update re-run anything — validation, or the reach forecast? If a patch changes the targeting, the forecast the trader was shown no longer applies, and the agent should say so.

**Open:** is `PATCH /api/strategies/{id}/` the right route for a strategy created through `simple-strategies`, given that `simple-strategies` is POST only?

---

### 5.18 Sync and failure handling

**New section.** Nothing in any earlier revision covered what happens after creation on the Amazon side.

**Creation does not mean the campaign exists on Amazon.** **Verified:**

- The created strategy shows `is_syncing: true` and a spinner
- Synchronisation to Amazon DSP runs in the background
- **It can fail.** Several strategies in the list carry `failure_reason: "CAMPAIGN_SYNC_ISSUES"` with an amber indicator

**What the agent must handle**

| Situation | Behaviour |
|---|---|
| `is_syncing: true` | Report that the strategy is publishing, and do not present it as live |
| `failure_reason` populated | Report the failure and its reason. Do not report success |
| Sync completes | Campaigns appear under the strategy; activation can proceed |

**Open:** how is sync completion or failure detected — is there a webhook, or must the agent poll `GET /api/strategies/{id}/`? This decides whether the agent can tell the trader when the campaign is genuinely live.

**Amazon-side structure.** After a successful sync the strategy holds Campaigns, each holding Ad Groups. These are Amazon DSP's own objects. Nothing in the planning flow creates them directly.

---

## 6. Consolidated slot registry

Every field in the plan, in one table. This is the registry the implementation builds against; §5 gives the reasoning.

**Legend for Requirement:** `R` required, `O` optional, `C` conditional, `—` present in the payload but never asked.

| Step | Field | Type | Req | Source | Endpoint or constant |
|---|---|---|---|---|---|
| 1 | `name` | `str` | O | `GENERATED` | `check_strategy_name_uniqueness/` |
| 1 | `flight_dates` | `list[DateRange]` | R | `INFERRED` | — |
| 1 | `markets` | `list[str]` | R | `INFERRED` | `GB`, `US` only |
| 1 | `primary_currency` | `CurrencyEnum` | O | `ADVERTISER` | `admin/advertiser/{id}/` |
| 1 | `creative_durations` | `list[int]` | R | `INFERRED` | 10,15,20,30,40,45,60 |
| 1 | `goal` | `GoalEnum` | R | `FIXED` | `AWARENESS` |
| 1 | `formats_and_kpis[].format` | `FormatEnum` | — | `FIXED` | `streaming_tv` |
| 1 | `formats_and_kpis[].kpi` | `KpiEnum` | R | `INFERRED` | `REACH` or `FREQUENCY` |
| 1 | `formats_and_kpis[].kpi_target_value` | `int` | C | `ASKED` | 2–5, frequency only |
| 1 | `markets_info[].budget` | `Decimal` | R | `INFERRED` | `> 0` |
| 1 | `markets_info[].currency` | `CurrencyEnum` | R | `DERIVED` | from market |
| 1 | `markets_info[].base_supply_bid` | `Decimal` | R | `ASKED` / `DERIVED` | **contested, D3** |
| 1 | `frequency_cap` | `int` | O | `ADVERTISER` | per week |
| 1 | `budget_cap` | `Decimal` | O | `ADVERTISER` | **open** |
| 1 | `video_product_categories` | `list[str]` | R | `ADVERTISER` / `INFERRED` | `contextual-targeting/{market}/product-categories/` |
| 1 | `product_categories` | `list[str]` | — | `FIXED` | `[]` for CTV |
| 1 | `conversion_types` | `list[str]` | O | `ASKED` | `conversions/definitions/` |
| 1 | `selected_inventory_sources` | `list[InventorySource]` | O | `API` | `inventory-sources/` |
| 2 | `channel` | `list[str]` | O | `INFERRED` | **blocked, D4** |
| 2 | `ros_or_genre` | `str` | O | `INFERRED` | **blocked, D4** |
| 2 | `market_deals[].deals` | `list[SelectedDealSchema]` | R | `MATCHED` | `deals/` |
| 2 | `specific_deal_id` | `str` | O | `ASKED` | lookup only, no format validation |
| 2 | `inventory_tier` (per deal) | `InventoryTierEnum` | R | `DERIVED` | **blocked, D4** |
| 2 | `targeting_source` (per deal) | `TargetingSourceEnum` | O | `MATCHED` | **blocked, D8** |
| 2 | `curation_requirements` | `CurationRequirementsSchema` | C | `ASKED` | needs-curation tier only |
| 3 | `audience_prompt` | `str` | O | `GENERATED` | `audience-sets/suggest/` |
| 3 | `markets_info[].audience_targeting` | `list[AudienceTargeting]` | O | `ASKED` | per market |
| 3 | `audience_targeting_match_type` | `MatchTypeEnum` | C | `ASKED` | `EXACT` default |
| 3 | `audience_data_sources` | `list[AudienceDataSourceEnum]` | R | `DERIVED` | drives the fee |
| 4 | `forecast` | `ReachForecastSchema` | — | `API` | `strategies/reach-forecast/` |
| 5 | `plan_status` | `PlanStatusEnum` | R | `ASKED` | `DRAFT` → `FINALISED` |
| 5 | `finalised_by` | `str` | — | `DERIVED` | |
| 5 | `finalised_at` | `datetime` | — | `GENERATED` | |
| 6 | `product_location` | `ProductLocationEnum` | R | `ADVERTISER` | required at creation |
| 6 | `product_asins` | `list[str]` | — | `FIXED` | `[]` at creation |
| 6 | `current_step` | `int` | R | `GENERATED` | draft resumption |
| 6 | `enable_brand_safety_targeting` | `bool` | — | `PLATFORM` | defaults false, **open** |
| 6 | `enable_fraud_invalid_traffic_targeting` | `bool` | — | `PLATFORM` | defaults false |
| 7 | `location` | `list[str]` | O | `DERIVED` | defaults to market country |
| 7 | `instream_position` | `InstreamPositionEnum` | O | `ASKED` | |
| 7 | `content_category_exclusions` | `list[str]` | O | `ADVERTISER` | **open** |
| 7 | `device_types` | `list[str]` | O | `ADVERTISER` | may be locked |
| 7 | `mobile_environment` | `MobileEnvEnum` | C | `ASKED` | mobile or tablet only |
| 8 | per-format budget | `Decimal` | — | `PLATFORM` | even split at creation |
| 8 | per-format bid | `Decimal` | — | `PLATFORM` | from `base_supply_bid` |
| 8 | `split_method` | `SplitMethodEnum` | C | `GENERATED` | where a split is proposed |
| 9 | `assets` | `list[AssetRef]` | R | `ASKED` | `assets/` |
| 9 | `click_through_url` | `Optional[HttpUrl]` | O | `ASKED` | **open:** per market? |
| 9 | asset `duration` | `Decimal` | — | `API` | structured, not derived |
| 10 | `creative_approval_statuses` | `dict[str, ApprovalStatusEnum]` | — | `API` | **blocked, D10** |
| 11 | ad tag registered | `bool` | C | `API` | off-Amazon only |
| 12 | credit sufficient | `bool` | — | `DERIVED` | `credits/summary/` |
| 13 | `activation_prerequisites` | `ActivationPrerequisitesSchema` | R | `DERIVED` | join node |

**Fields sent empty but required by the payload:** `product_categories`, `product_asins`, `pre_approved_creatives`, `rec_creatives`, `third_party_creatives`.

---

## 7. API catalogue

Checked against the staging OpenAPI listing, 4 August 2026. **Verified** means the call was observed in the product with its payload and response.

### 7.1 Corrections to earlier revisions

| Assumed in v1.1.0 / v2.0 | Reality |
|---|---|
| `POST /api/rate-cards/match/` for deal matching | **Does not exist.** Matching uses `GET /api/deals/` with `GET /api/deals/filter-properties/` |
| `GET /api/advertisers/{id}/defaults/` for advertiser settings | **Does not exist.** Settings are at `GET /api/admin/advertiser/{id}/` |
| `POST /api/strategies/draft/` | Not used. Draft is a boolean on the strategy, not a separate endpoint |
| No update endpoint listed | `PATCH /api/strategies/{id}/` exists — model `StrategyUpdate` |
| Postcode support unknown | `POST /api/strategies/postcode-validation/{market}/` exists |
| Fee values unknown | `GET /api/contextual-targeting/fees` exists |
| Audience reach forecast assumed to be the plan's forecast | Two audience-aware forecast endpoints exist; the plan's forecast is `POST /api/strategies/reach-forecast/` |

### 7.2 The seventeen calls the product makes

| # | Endpoint | Method | When | Status |
|---|---|---|---|---|
| 1 | `/api/credits/summary/?advertiser=` | GET | List load, credit check | **Verified** |
| 2 | `/api/reports/user-preferences/` | GET | List load | **Verified** |
| 3 | `/api/strategies/?{11 params}` | GET | List load | **Verified** |
| 4 | `/api/audience-sets/check_market_has_audience_set/?markets=` | GET | Step 1 | **Verified** |
| 5 | `/api/creatives/recs/check_market/?markets=` | GET | Step 1 | **Verified** |
| 6 | `/api/assets/check_market_has_assets/?markets=&target_types=&dsp_approved=` | GET | Step 1 | **Verified** |
| 7 | `/api/inventory-sources/?strategy_formats=&markets=&goal=` | GET | Step 1 | **Verified** |
| 8 | `/api/conversions/definitions/` | GET | Step 1, off-Amazon | **Verified** |
| 9 | `/api/strategies/check_strategy_name_uniqueness/?name=` | GET | Step 1 to 2 | **Verified** |
| 10 | `/api/deals/?{11 params}` | GET | Step 2 | **Verified** |
| 11 | `/api/deals/filter-properties/?formats=` | GET | Step 2 | **Verified** |
| 12 | `/api/audience-sets/?search=&page_size=` | GET | Step 3 | **Verified** |
| 13 | `/api/assets/?search=&target_types=&dsp_approved=` | GET | Step 9 | **Verified** |
| 14 | `/api/creatives/?approval_status=&markets=&asset=&no_pagination=true` | GET | Step 9 | **Verified** |
| 15 | `/api/strategies/reach-forecast/` | POST | Step 4 | **Verified** |
| 16 | `/api/strategies/` | POST | Step 6 | **Verified** — returns 201 |
| 17 | `/api/strategies/{id}/` | GET | After creation | **Verified** |

**Common to all:** `Server: gunicorn`, `Vary: Accept, Cookie, origin`, session-cookie authentication.

**Note on scoping:** the strategy list call carries no `advertiser` parameter, unlike the credits call. `Vary: Cookie` indicates the advertiser is held in the session. The `aid` in the browser URL is front-end state only.

### 7.3 Endpoints the agent needs that the product does not call

| Endpoint | Purpose | Status |
|---|---|---|
| `GET /api/admin/advertiser/{id}/` | Advertiser settings | Exists |
| `POST /api/audience-sets/suggest/` | Audience suggestion | Exists. **D2** — response shape needed |
| `GET /api/audience-sets/suggest/{id}/` | Read the suggestion | Exists |
| `GET /api/contextual-targeting/fees` | Fee values | Exists |
| `POST /api/audiences/{market}/overlapping-audiences/` | Cross-provider overlap | Exists |
| `GET /api/contextual-targeting/{market}/product-categories/` | Category taxonomy | Exists |
| `POST /api/contextual-targeting/{market}/asin-validation/` | ASIN validation | Exists |
| `GET /api/rates/ctv/{market}/` | CTV rate card | Exists |
| `POST /api/strategies/postcode-validation/{market}/` | Postcode validation | Exists |
| `GET /api/strategies/locations/{market}/` | Location taxonomy | Exists |
| `POST /api/strategies/{id}/targeting/auto-rec/` | Recommended targeting | Exists. **Open** — what does it return |
| `GET/POST /api/strategies/{id}/targeting/{market}/locations/` | Write targeting | Exists |
| `GET/POST /api/strategies/{id}/flight-ranges/` | Flight range CRUD | Exists |
| `PATCH /api/strategies/{id}/` | Post-creation update | Exists |
| `POST /api/strategies/{id}/set_status/` | Activation | Exists |
| `POST /api/strategies/duplicate/` | Duplicate a strategy | Exists |
| `POST /api/assets/amz_assets/gen_upload_urls/` | Creative upload | Exists |
| `POST /api/assets/amz_assets/register/` | Register on Amazon | Exists |
| `POST /api/credits/` , `POST /api/credits/stripe/` | Top-up | Exists |
| `GET /api/strategies/choices/` | Enumerations | Exists. **Open** — may replace several hard-coded lists |
| `POST /api/simple-strategies/` | CTV creation variant | Exists, POST only. **D5** |
| `POST /api/automated-strategies/` | Automated creation | Exists. **D5** |

---

## 8. Platform read model

**New section.** The shape of a strategy as the API returns it. Needed for status checks, reporting and any read-back after creation.

### 8.1 The list query

```
GET /api/strategies/
    ?metrics_date_range=&markets=&formats=&product_locations=&goal=&search=
    &page=1&page_size=20&ordering=name&include_archived=false&currency_type=primary
```

Standard DRF pagination: `count`, `next`, `previous`, `results`.

Note that `goal` is accepted as a filter parameter although it is not exposed in the UI, and that `product_locations` is what the UI labels "Channels" or "Location".

### 8.2 The strategy object

**Verified** — twenty fields.

```json
{
  "id": "VMA2025107",
  "name": "...",
  "channel_type": "dsp",
  "goal": "AWARENESS",
  "budget_at_risk": "0.00",
  "primary_currency": "EUR",
  "flight_dates": {"lower": "2025-02-28", "upper": "2025-02-28", "timezone": "UTC"},
  "product_location": "NOT_SOLD_ON_AMAZON",
  "delivery_activation_status": "INACTIVE",
  "formats": ["display", "online_video", "streaming_tv"],
  "markets": ["US"],
  "metrics": { /* 29 fields, see below */ },
  "status": "3_ended",
  "budget": "3.64",
  "is_draft": false,
  "is_syncing": true,
  "failure_reason": "CAMPAIGN_SYNC_ISSUES",
  "is_archived": false,
  "is_readonly": true,
  "is_automated": false
}
```

**`budget_at_risk`** — **Open.** The field exists and appears as a column. Its definition is not documented. **Inferred** to mean budget committed but unlikely to deliver.

### 8.3 The metrics object

**Verified** — 29 fields in four groups.

| Group | Fields |
|---|---|
| Counts | `impressions`, `click_throughs`, `viewable_impressions`, `purchases`, `off_amazon_purchases`, `off_amazon_conversions` |
| Rates | `vr`, `ctr`, `vcr`, `dpvr`, `acos`, `off_amazon_cvr` |
| Returns | `roas`, `c_roas`, `t_roas`, `off_amazon_roas` |
| Money | `sales`, `total_cost`, `total_sales`, `product_sales`, `off_amazon_product_sales` |
| Unit costs | `ecpm`, `ecpc`, `cpvc`, `cpdpv`, `off_amazon_cpa`, `off_amazon_purchases_cpa` |
| Context | `display_currency` |

**All money and rate values are strings**, not numbers — `"3.64"`, `"0.00000"`. Rates carry five decimal places.

**Three attribution families** are reported separately and should not be conflated:

```
Off-Amazon      the advertiser's own site, via the ad tag
On-Amazon       Amazon, via the ASINs
Total           the two combined
```

**Which metrics are meaningful for CTV**

```
Meaningful     reach, frequency, impressions, vcr, vr, ecpm, cpvc
Not meaningful ctr, ecpc, and anything click-derived — the ad cannot be clicked
Conditional    dpvr and the sales metrics — only where ASINs or an ad tag exist
```

This is the underlying reason the goal is fixed to Awareness.

---

## 9. Pydantic schemas

```python
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Optional
from pydantic import BaseModel, Field, HttpUrl, model_validator


# ---------------------------------------------------------------- enumerations

class FormatEnum(str, Enum):
    STREAMING_TV = "streaming_tv"
    PRIME_VIDEO = "prime_video"    # a channel, not a format; retained because
                                   # removing an enum value is a breaking change.
                                   # Required in the forecast payload - see 4.7.1
    DISPLAY = "display"            # out of scope for CTV
    ONLINE_VIDEO = "online_video"  # out of scope for CTV


class CurrencyEnum(str, Enum):
    EUR = "EUR"
    GBP = "GBP"
    USD = "USD"
    # NOK exists in production data - see 4.6. Open decision.


class GoalEnum(str, Enum):
    AWARENESS = "AWARENESS"
    CONSIDERATION = "CONSIDERATION"    # out of scope for CTV
    CONVERSION = "CONVERSION"          # out of scope for CTV


class KpiEnum(str, Enum):
    REACH = "REACH"
    FREQUENCY = "FREQUENCY"


class ProductLocationEnum(str, Enum):
    SOLD_ON_AMAZON = "SOLD_ON_AMAZON"
    NOT_SOLD_ON_AMAZON = "NOT_SOLD_ON_AMAZON"


class DealTypeEnum(str, Enum):
    PREFERRED = "PREFERRED"
    PRIVATE_AUCTION = "PRIVATE_AUCTION"
    PROGRAMMATIC_GUARANTEED = "PROGRAMMATIC_GUARANTEED"


class DealPriceTypeEnum(str, Enum):
    FIXED_CPM = "FIXED_CPM"
    FLOOR_RATE = "FLOOR_RATE"


class InventoryTierEnum(str, Enum):
    AMAZON_OWNED = "AMAZON_OWNED"
    THIRD_PARTY_PRECURATED = "THIRD_PARTY_PRECURATED"
    THIRD_PARTY_NEEDS_CURATION = "THIRD_PARTY_NEEDS_CURATION"


class TargetingSourceEnum(str, Enum):
    AMAZON_DSP = "AMAZON_DSP"
    INVENTORY_SOURCE = "INVENTORY_SOURCE"


class AudienceProfileEnum(str, Enum):
    NARROW = "NARROW"
    BALANCED = "BALANCED"
    WIDE = "WIDE"


class AudienceDataSourceEnum(str, Enum):
    AMAZON_1P = "AMAZON_1P"
    THIRD_PARTY = "THIRD_PARTY"
    NONE = "NONE"


class MatchTypeEnum(str, Enum):
    SIMILAR = "SIMILAR"
    EXACT = "EXACT"


class SplitMethodEnum(str, Enum):
    EVEN_BY_BUDGET = "EVEN_BY_BUDGET"
    EVEN_BY_IMPRESSIONS = "EVEN_BY_IMPRESSIONS"


class PlanStatusEnum(str, Enum):
    """Deliberately separate from ApprovalStatusEnum. The plan and the creative
    have different lifecycles; adding PENDING_APPROVAL later stays additive."""
    DRAFT = "DRAFT"
    FINALISED = "FINALISED"


class ApprovalStatusEnum(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


# ------------------------------------------------------- advertiser settings

class AdvertiserSetting(BaseModel):
    """A setting held on the advertiser rather than the campaign.

    is_locked distinguishes a starting point from a brand policy. Without it the
    repair loop cannot tell what it is allowed to relax.
    """
    value: Any
    is_locked: bool = False
    reason: Optional[str] = None


class AdvertiserDefaults(BaseModel):
    """Loaded at session start, BEFORE the brief is parsed, so that anything the
    brief states overrides these rather than the other way round."""
    primary_currency: Optional[AdvertiserSetting] = None
    frequency_cap: Optional[AdvertiserSetting] = None
    budget_cap: Optional[AdvertiserSetting] = None
    product_categories: Optional[AdvertiserSetting] = None
    selling_location: Optional[AdvertiserSetting] = None
    device_types: Optional[AdvertiserSetting] = None
    content_category_exclusions: Optional[AdvertiserSetting] = None
    approval_threshold: Optional[AdvertiserSetting] = None   # future scope


# ------------------------------------------------------------------ the plan

class DateRangeSchema(BaseModel):
    lower: date
    upper: date
    timezone: str = "UTC"

    @model_validator(mode="after")
    def _check_order(self):
        if self.upper <= self.lower:
            raise ValueError("upper must be later than lower")
        return self


class FormatKpiSchema(BaseModel):
    """KPI is held per format, not per strategy - corrected in v4.0."""
    format: FormatEnum
    kpi: KpiEnum
    kpi_target_value: Optional[int] = Field(default=None, ge=2, le=5)

    @model_validator(mode="after")
    def _target_only_for_frequency(self):
        if self.kpi is KpiEnum.REACH and self.kpi_target_value is not None:
            raise ValueError("kpi_target_value applies only to a frequency KPI")
        return self


class AudienceTargetingSchema(BaseModel):
    audience_set_id: str
    audience_type: str = "AUDIENCE_SET"


class MarketInfoSchema(BaseModel):
    """Market is the organising unit of the payload. Budget, bid, currency and
    audiences are all per market."""
    market: str
    budget: Decimal = Field(gt=0)
    currency: CurrencyEnum
    base_supply_bid: Decimal          # named base_bid on the forecast endpoint
    audience_targeting: list[AudienceTargetingSchema] = Field(default_factory=list)


class VolumeEntry(BaseModel):
    bid_request_volume: float
    bid_request_volume_rate: float


class SelectedDealSchema(BaseModel):
    """The complete deal object is sent back at creation, not just an identifier."""
    external_deal_id: str
    name: str
    deal_type: DealTypeEnum
    deal_price_type: DealPriceTypeEnum
    deal_price_amount: Decimal
    deal_price_currency: CurrencyEnum

    media_types: list[dict] = Field(default_factory=list)
    devices: list[dict] = Field(default_factory=list)
    environments: list[dict] = Field(default_factory=list)
    locations: list[dict] = Field(default_factory=list)
    genre: Optional[str] = None          # unusable in practice - see section 12
    ad_lengths: list[str] = Field(default_factory=list)

    # Derived by the agent, not returned by the API
    channel: Optional[str] = None                       # renamed from provider
    inventory_tier: Optional[InventoryTierEnum] = None  # no source exists - D4
    targeting_source: Optional[TargetingSourceEnum] = None

    @property
    def bid_applies(self) -> bool:
        """A floor rate must be exceeded; a fixed price is paid as shown."""
        return self.deal_price_type is DealPriceTypeEnum.FLOOR_RATE

    @property
    def commits_full_budget(self) -> bool:
        """A guaranteed deal owes the full budget and cannot be paused. This must
        be surfaced to the trader even though the deal itself is not."""
        return self.deal_type is DealTypeEnum.PROGRAMMATIC_GUARANTEED

    @property
    def returns_reach_forecast(self) -> bool:
        return self.inventory_tier is InventoryTierEnum.AMAZON_OWNED


class MarketDealsSchema(BaseModel):
    market: str
    deals: list[SelectedDealSchema]


class CurationRequirementsSchema(BaseModel):
    """For the needs-curation tier, where a deal does not exist yet."""
    channel: str                       # renamed from provider
    genres: list[str]
    durations: list[int]
    targeting_preferences: Optional[str] = None
    budget: Decimal
    flight_dates: DateRangeSchema


class BudgetSplitSchema(BaseModel):
    by_format: dict[str, Decimal] = Field(default_factory=dict)
    by_duration: dict[str, Decimal] = Field(default_factory=dict)
    method: SplitMethodEnum
    rationale: str          # the agent must state which method it chose and why


class SupplyForecastSchema(BaseModel):
    """est_ and max_ pairs give the deliverability ceiling. Where est_reach already
    equals max_reach, no lever will improve it."""
    supply: str                        # DSP_STREAMING_TV | DSP_PRIME_VIDEO
    est_spend: float
    est_reach: int
    max_reach: int
    est_impressions: int
    max_impressions: int
    avg_cpm: Decimal
    max_cpm: Decimal


class MarketReachSchema(BaseModel):
    market: str
    reach: int
    impressions: int
    budget: Decimal
    currency: CurrencyEnum
    supplies: list[SupplyForecastSchema]


class ReachForecastSchema(BaseModel):
    total_reach: int
    total_impressions: int
    market_reach: list[MarketReachSchema]

    @property
    def average_frequency(self) -> float:
        """Not returned by the API. The window is per week."""
        return self.total_impressions / self.total_reach if self.total_reach else 0.0

    # Never sum est_reach across supplies. The API total is higher than the sum
    # because there is no cross-platform deduplication - see 4.8.1.


class TargetingSchema(BaseModel):
    """Written after creation. No field starts empty."""
    location: list[str]                       # defaults to the market's country
    instream_position: Optional[str] = None
    content_category_exclusions: list[str] = Field(default_factory=list)
    device_types: list[str] = Field(default_factory=list)
    mobile_environment: Optional[str] = None  # only where mobile or tablet applies


class ActivationPrerequisitesSchema(BaseModel):
    """Checked at the join node before any spend. See section 5.16."""
    creative_uploaded: dict[str, bool] = Field(default_factory=dict)
    creative_approved: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
    targeting_written: bool = False
    budget_allocated: bool = False
    ad_tag_registered: Optional[bool] = None
    asins_attached: Optional[bool] = None
    conversions_chosen: bool = False
    credit_sufficient: bool = False


class StrategyPlanSchema(BaseModel):
    """The agent's complete plan state. Phase A fills this; phase B creates from
    it; phase C attaches the rest."""

    # Basics
    name: Optional[str] = None                        # GENERATED
    flight_dates: list[DateRangeSchema]               # a list - multiple ranges
    markets: list[str]                                # one per strategy in M1
    primary_currency: CurrencyEnum                    # from the advertiser
    creative_durations: list[int]
    goal: GoalEnum = GoalEnum.AWARENESS               # fixed for CTV
    formats: list[FormatEnum] = [FormatEnum.STREAMING_TV]
    formats_and_kpis: list[FormatKpiSchema]
    frequency_cap: Optional[int] = None
    budget_cap: Optional[Decimal] = None
    video_product_categories: list[str] = Field(default_factory=list)
    product_categories: list[str] = Field(default_factory=list)   # empty for CTV
    conversion_types: list[str] = Field(default_factory=list)
    selected_inventory_sources: list[dict] = Field(default_factory=list)

    # Per market
    markets_info: list[MarketInfoSchema]
    market_deals: list[MarketDealsSchema] = Field(default_factory=list)

    # Inventory
    channel: list[str] = Field(default_factory=list)
    ros_or_genre: Optional[str] = None
    specific_deal_id: Optional[str] = None
    curation_requirements: Optional[CurationRequirementsSchema] = None

    # Audiences
    audience_prompt: Optional[str] = None
    audience_profile: Optional[AudienceProfileEnum] = None
    audience_targeting_match_type: MatchTypeEnum = MatchTypeEnum.EXACT
    audience_data_sources: list[AudienceDataSourceEnum] = Field(default_factory=list)

    # Forecast
    forecast: Optional[ReachForecastSchema] = None

    # Plan lifecycle
    plan_status: PlanStatusEnum = PlanStatusEnum.DRAFT
    finalised_by: Optional[str] = None
    finalised_at: Optional[datetime] = None

    # Creation and after
    strategy_id: Optional[str] = None                 # VMA... once created
    product_location: ProductLocationEnum
    product_asins: list[str] = Field(default_factory=list)   # empty at creation
    current_step: int = 0
    targeting: Optional[TargetingSchema] = None
    budget_split: Optional[BudgetSplitSchema] = None
    assets: list[dict] = Field(default_factory=list)
    click_through_url: Optional[HttpUrl] = None
    creative_approval_statuses: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
    activation_prerequisites: Optional[ActivationPrerequisitesSchema] = None

    # Required by the payload, always empty for CTV
    pre_approved_creatives: list[dict] = Field(default_factory=list)
    rec_creatives: list[dict] = Field(default_factory=list)
    third_party_creatives: list[dict] = Field(default_factory=list)

    @property
    def effective_cpm_inputs_valid(self) -> bool:
        """Guard: one deal on the platform is priced at 0.00, and deal currencies
        can differ from the plan's currency - see 4.8.4."""
        for md in self.market_deals:
            for d in md.deals:
                if d.deal_price_amount == 0:
                    return False
        return True
```

---

## 10. LangGraph state machine

```
                          load_advertiser_defaults
                                     |
                                     v
                              parse_brief
                                     |
                                     v
  +------------------------- PHASE A - PLAN ---------------------------+
  |                                                                   |
  |   collect_basics                                                  |
  |        |                                                          |
  |        v                                                          |
  |   match_inventory_deals          (renamed from select_inventory)   |
  |        |                                                          |
  |        v                                                          |
  |   suggest_audiences  <---------------+                            |
  |        |                             |                            |
  |        v                             | repair loop                |
  |   forecast_reach ---- shortfall -----+ (levers per 5.7.5)         |
  |        |                                                          |
  |        | reach acceptable, or no levers remain                    |
  |        v                                                          |
  |   finalise_plan          DRAFT -> FINALISED, no interrupt          |
  +-------------------------------|-----------------------------------+
                                  v
                          create_strategy                  one POST
                                  |
  +------------------------- PHASE C - ATTACH ------------------------+
  |            (parallel branches, no order between them)             |
  |                                                                   |
  |   write_targeting      allocate_budget      upload_creative       |
  |         |                    |                    |               |
  |         |                    |                    v               |
  |         |                    |            await_approval          |
  |         |                    |            [interrupt] external    |
  |         |                    |                    |               |
  |   setup_tracking       check_credit                |               |
  |         |                    |                    |               |
  +---------|--------------------|--------------------|---------------+
            |                    |                    |
            +--------------------+--------------------+
                                 v
                        check_prerequisites             JOIN NODE
                                 |
                    +------------+------------+
                    | ready               not ready
                    v                        v
                activate              report_blockers
                    |                        |
                    v                        v
              monitor_sync              (back to the
              (5.18)                     blocking branch)
```

### 10.1 Node notes

| Node | Note |
|---|---|
| `load_advertiser_defaults` | Runs **before** `parse_brief` so the brief overrides the defaults |
| `match_inventory_deals` | Renamed per review, so the node name says what it does |
| `forecast_reach` | The product's forecast takes four inputs only. The audience-aware endpoints exist but are unused — **D7** |
| `finalise_plan` | The `interrupt()` was removed here |
| `await_approval` | Retains its `interrupt()` — the wait is genuinely external |
| `check_prerequisites` | The join node. Reports **every** unmet prerequisite at once, not one per attempt |
| `monitor_sync` | New in v4.0. Creation does not mean the campaign exists on Amazon |

### 10.2 Repair loop guards

The loop must terminate and must not offer what it cannot do.

```python
def available_levers(plan: StrategyPlanSchema,
                     defaults: AdvertiserDefaults) -> list[str]:
    levers = []
    if plan.audience_profile is not None:
        levers.append("widen_audience")
    if any(d.bid_applies for md in plan.market_deals for d in md.deals):
        levers.append("raise_bid")                       # floor-rate deals - D3
    if not (defaults.device_types and defaults.device_types.is_locked):
        levers.append("relax_device_targeting")
    if plan.targeting and len(plan.targeting.location) > 1:
        levers.append("widen_geography")
    levers.append("widen_inventory")     # always available, but unverifiable on 3P
    return levers
```

Three rules:

1. **Cap the iterations.** Two or three attempts, then report.
2. **Check `max_reach` before acting.** Where `est_reach == max_reach` no lever will help, and the agent should say the inventory is exhausted rather than trying.
3. **Name the levers it could not use.** A locked advertiser policy or an absent audience is information the trader needs, not something to omit silently.

---

## 11. Open decisions

Ranked. The first six block implementation.

### Blocking

| # | Decision | Why it blocks | Owner |
|---|---|---|---|
| **D1** | **Targeting timing.** Every targeting endpoint requires a strategy id, so targeting cannot precede the forecast as v2.0 specified. Should the agent hold targeting in its own state, forecast, create, then write it? Or does targeting genuinely belong after creation? | Determines the graph order and whether steps 3 and 7 can be presented as one subject | Client |
| **D2** | **A real request and response from `POST /api/audience-sets/suggest/`.** Knowing that `bundles` does not exist is only half the answer; the grouping rule, the fee handling and the audience schema all depend on the actual shape. Also: does `SuggestAudienceGroupsInput` mean the caller can request groups, and how long does the async call take? | Nothing in step 3 can be built without it | Client |
| **D3** | **Does the bid apply on floor-rate deals?** §2.3 describes private auctions as "Floor CPM, competitive". Almost all 83 deals on staging are `PRIVATE_AUCTION` with `FLOOR_RATE`, and the platform blocks progress when base bid is empty on a pure CTV plan. If the bid applies, the repair loop keeps a lever the current specification removes. And what should be sent for `base_supply_bid` if the trader is never asked? | Changes agent behaviour, and the create payload requires a value | Client |
| **D4** | **Are the deal matching inputs available as fields?** There is no `channel` and no `inventory_tier` on a deal; `genre` exists but returns years, a test label and an ad-length list; Amazon-audience capability is encoded in the deal name. Is there a source we have missed, or can these be added? | Step 2 cannot be built as specified. This is the single largest blocker | Client |
| **D5** | **Which create endpoint, and its field list?** Three exist: `strategies` (what the product uses), `simple-strategies` (POST only, identified in review), `automated-strategies` (name suggests agent use; strategies already carry `is_automated`). | The entire create payload depends on the answer | Client |
| **D6** | **Advertiser settings: the full list, and which are locked.** Five identified so far. Locked versus default determines what the repair loop may relax. Also: is the advertiser-level value a product category or an industry? The two are separate taxonomies with no mapping between them. | Determines repair-loop behaviour and the basics resolution order | Client |

### Behaviour-changing

| # | Decision | Why it matters |
|---|---|---|
| **D7** | **Build the audience-aware repair loop in M1?** The endpoints exist but nothing in the product calls them, and the product's forecast takes no audience input. The repair loop is therefore a new capability rather than existing behaviour. | Scope. A significant piece of work either way |
| **D8** | **Can Amazon audiences and the inventory source's targeting run on the same deal?** If both, `targeting_source` must be a list, and the combination rule needs stating — intersection and union have opposite effects on reach. Also, how limited is Amazon's targeting on third-party inventory in practice? | Field design, cost model, and what the agent recommends |
| **D9** | **Who owns the budget split?** The platform allocates evenly per format at creation and allows editing. Three numbers exist — the forecast's estimate, the platform's allocation, and any agent proposal. Which does the trader see, and which does the agent set? | Whether step 8 is agent logic or explanation |
| **D10** | **Where do per-channel creative approval statuses live?** A creative carries `market` and `approval_status` with no channel dimension. If these are tracked outside VOW, the activation prerequisite cannot be evaluated. Is the status per channel, or per creative-and-channel pair? | Whether the activation gate can be built |
| **D11** | **Which fields are updatable after creation, and which fixed?** The proposal at §5.17 separates measurement fields from those that carry money. Budget and deals are the ones that matter, because a guaranteed deal has already committed the budget. Does "after creation" extend to "after activation"? | Prevents a plan and a commitment disagreeing |
| **D12** | **What does the KPI target value do?** Either it drives the forecast check — impressions are fixed by budget and CPM, so a frequency target implies a reach target — or it is recorded for reporting only. The two lead to very different agent behaviour. And if the KPI is frequency with no stated target, should the agent assume one? | Whether the repair loop has a trigger at all |

### Scope and smaller decisions

| # | Decision |
|---|---|
| D13 | One market per strategy in M1, or is multi-market needed in the first release? |
| D14 | Are multiple flight ranges needed in M1? The platform supports them |
| D15 | When several deals match, how should the agent choose — cheapest CPM, largest volume, or best genre fit? |
| D16 | When nothing matches, should the agent widen the duration, drop the genre, or ask? |
| D17 | Should a Programmatic Guaranteed deal ever be matched automatically, given the commitment? Does PG inventory appear at all — none was found on staging |
| D18 | Should `enable_brand_safety_targeting` default to true? It is currently false and invisible to the trader |
| D19 | Should the agent show every inferred value for correction, or only the uncertain ones? |
| D20 | What does `POST /api/strategies/{id}/targeting/auto-rec/` return? It may replace the baseline logic entirely |
| D21 | Is the click-through URL held per market? The model `MarketWithClickthroughUrl` suggests it may be |
| D22 | Are QR codes permitted in CTV creatives, and is there a specification? |
| D23 | How is sync completion or failure detected — webhook, or polling? |
| D24 | Should the ASIN list be validated in one call, or as the trader pastes? |
| D25 | Can conversions be skipped entirely, or is at least one always required? |
| D26 | Is the credit check genuinely order-free? Its outcome can change the budget |
| D27 | Can a finalised plan return to `DRAFT`? What can change after finalisation? |
| D28 | Should an advertiser-level approval threshold be planned for? |
| D29 | Where should the channel list come from — `get_channels_choices/`, or derived from matched deals? |
| D30 | `CurrencyEnum` holds EUR, GBP and USD. `NOK` exists in production data. Extend, or scope out? |
| D31 | Can the trader override the derived market currency? Doing so makes the plan total and the deal CPMs disagree unless a rate is applied |
| D32 | Do traders use an existing strategy naming convention? |
| D33 | Is `is_automated` the agent marker, or does it mean something else? |
| D34 | What is `budget_at_risk`? The field and column exist; the definition does not |
| D35 | Is `strategies-sp` sponsored products and irrelevant to CTV? |
| D36 | Does `GET /api/strategies/choices/` serve the enumerations currently hard-coded here? |
| D37 | What are the exact `status` strings for the four values not yet observed? |
| D38 | What other values does `audience_type` take beyond `AUDIENCE_SET`? |
| D39 | Is `no_pagination=true` available on `/api/deals/`? 83 deals in one call would be simpler |
| D40 | Is the activation prerequisite list complete? |

---

## 12. Data quality requests

Four issues that cannot be resolved on our side. Each blocks or degrades a specific capability.

### 12.1 The `genre` field is unusable

**Verified.** `GET /api/deals/filter-properties/` returns:

```json
"genres": ["15, 20, 30", "2026", "2027", "Action", "Comedy", "Drama",
           "RON", "ROS", "Suspense", "TEST", "Top Trending", "Winter Holiday"]
```

| Value | What it actually is |
|---|---|
| `Action`, `Comedy`, `Drama`, `Suspense` | Genuine genres |
| `Top Trending`, `Winter Holiday` | Content categories — workable |
| `RON`, `ROS` | Placement types, not genres |
| `2026`, `2027` | Years |
| `TEST` | A test label |
| `15, 20, 30` | An ad-length list |

And the Netflix deals carry their genre **in the name** while the field is `null`:

```
3PS_Netflix_Always On_Primetime Entertainment_...     genre: null
3PS_Netflix_Always On_Sports & Action_...             genre: null
```

**Inferred:** the field takes the last token of the deal name. Where a name ends on a genre it is correct; where it ends on a year it is wrong; where the genre sits mid-name it is empty.

**Request:** populate `genre` from a controlled vocabulary. **Blocks:** genre matching and the genre upsell feature.

### 12.2 Amazon-audience capability is encoded in the deal name

**Verified.**

```
3PS_Netflix_..._NOT Amazon Audience Enabled_STV_UK_...      (five deals)
3PS_Netflix_Always On_Run of Network_Amazon Audience Enabled_STV_UK_...  (one deal)
```

The deal object carries no audience-capability field.

**Request:** expose this as a boolean. **Blocks:** setting `targeting_source` reliably, which the review comment on the tier table introduced.

### 12.3 No source exists for `inventory_tier`

**Verified.** No `inventory_tier` field on a deal, and no `channel` field either. The three-tier fork is the primary branch of the CTV flow and has no data source.

**Request:** a source for tier and channel. **Blocks:** the entire tier fork — reach-forecast availability, curation capture, and what the agent tells the trader about capability.

### 12.4 Third-party deal metadata is largely absent

**Verified.**

| Field | Prime Video | Netflix |
|---|---|---|
| `devices` | 3 entries with volumes | `[]` |
| `environments` | `APP` 100% | `[]` |
| `media_types` | `VIDEO_STV` 100% | `[]` |
| `locations[].bid_request_volume` | 1,457,882,193 | 1 |
| `ad_lengths` | populated | `[]` |

A location volume of `1` is a placeholder.

**Request:** clarification — is this a data gap, or is the metadata genuinely unavailable upstream from third-party exchanges? **Degrades:** duration matching, device matching and deliverability assessment on all third-party inventory, which is the majority of the available deals.

### 12.5 Smaller items

| Item | Detail |
|---|---|
| One deal priced at zero | `VowMade_Fifa 2026_ZA` has `deal_price_amount: "0.00"`. Data error, or intentional? |
| `ad_lengths` not distinct | `filter-properties` returns 16 entries with 7 distinct values |
| Empty-string fees | `standard_display_fee` returns `""` rather than null on some sets |
| Two audience sets break the fee pattern | Both have zero segments; **Inferred** to be data errors |
| `VCR` above 100% | 128.45% observed. Not meaningful |
| `ZA` deals in a GB-filtered list | The agent filters on `locations[].country_code`; confirming this is expected would help |
| Click-through URLs contain application URLs | Testers have pasted `staging.vowmade.dev/app/...` addresses. The field does not validate |
| Duplicate assets | The same video appears twice at different resolutions with the same name and URL |

---

## 13. Out of scope

Recorded so that the boundary is explicit and so that nothing here is mistaken for an omission.

### 13.1 Out of scope for CTV

| Item | Reason |
|---|---|
| Display and online video formats | This agent is CTV-first. Both remain valid in the platform |
| Consideration and Conversion goals | CTV is used for awareness; tracking further down the funnel is unreliable |
| CTR, CPC, CPA and CPDPV as KPIs | Click-derived, and CTV ads cannot be clicked |
| Product audiences | Not applicable to CTV |
| Responsive e-commerce creatives | Display only |
| Third-party creative tags | Display only |
| Pre-approved creative selection | Display only |

### 13.2 Not supported by the platform today

| Item | Note |
|---|---|
| Genre exclusions | Future scope |
| Day-parting | Future scope |
| Language targeting | Future scope |
| Cross-platform reach deduplication | Does not exist. This is why reach cannot be summed |
| Reach forecast on third-party inventory | Does not exist. This is the basis of the honesty rule |

### 13.3 Deferred by decision

| Item | Where it would return |
|---|---|
| Manager approval workflow | As an advertiser-level threshold rather than a gate — see §5.8 |
| Multi-market strategies | Field is already a list, so this is additive — **D13** |
| Multiple flight ranges | Platform supports it — **D14** |
| AMC audiences | Conditional on the advertiser having prior campaign data |

---

## 14. Change log

| Version | Change |
|---|---|
| 1.1.0 | Initial schema. Followed the six-step UI wizard. Covered display, online video and CTV |
| 2.0.0 | Reordered to a CTV-first agent flow. Thirteen steps. Client feedback incorporated |
| 3.0 | All 28 review comments answered in place. v2.0's structure and step numbering preserved so that comments stayed anchored |
| **4.0** | Reorganised for implementation. Flow order corrected against the platform. Domain model, currency model, taxonomies, numeric rules, budget allocation, sync handling and the platform read model added. Twelve positions corrected against verified behaviour. Forty open decisions and four data quality requests recorded |

---

**End of Strategy Schema Registry v4.0**

*Verified against `staging.vowmade.dev` on 4 August 2026. Where a position is contested, the evidence is stated inline so that the disagreement can be settled on facts. Comments are welcome on any section; §11 lists the questions that need answers before implementation can proceed.*
