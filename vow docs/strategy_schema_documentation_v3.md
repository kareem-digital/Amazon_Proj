# VOW Platform — Strategy Schema v3

Aligned to the confirmed CTV-first agentic flow (v5)

Original version: 1.1.0. Previous revision: 2.0.0. This revision: 3.0 — reordered, scoped to CTV, and extended with client-confirmed corrections Status: For client verification

**How to read this document.** Every section is marked:

- UNCHANGED — kept exactly as written in v1.1.0
- CHANGED — the concept existed but is modified (original shown for comparison)
- NEW — did not exist in v1.1.0, added from client feedback
- REMOVED — existed in v1.1.0 but dropped for CTV scope (kept as future scope)

The document follows the confirmed agentic flow order, not the existing wizard order.

---

## What changed in v3.0, and where

Every change made in this revision comes from a review comment on v2.0. The structure, section order and step numbering of v2.0 are unchanged deliberately, so that each comment still sits next to the text it was made on. Only the affected row, cell or paragraph has been edited, with a note beneath it.

**Sections with no comments on them are identical to v2.0.** In particular, each step's *"What was in v1.1.0"* block is historical and has not been touched — the changes are in the *"What it is now"* table that follows it.

| # | Section | Row or text changed | What changed |
|---|---|---|---|
| 1 | 2.3 Deal Types | Audiences column, both 3P rows | Third-party targeting can come from Amazon DSP **or** the inventory source — it is a choice per deal, not fixed by the tier |
| 2 | 2.4 Audience Profiles | Narrow and Wide rows; the fee note | Fee depends on the data provider, not on the profile, and does not compound. Profiles differ in reach and precision, not cost |
| 3 | 3 Flow comparison | Budget split row | Marked optional |
| 4 | 3 Flow comparison, 2.4, Step 4 | "mandatory" | Audiences are optional, not mandatory |
| 5 | 3 Flow comparison, Step 5 | Targeting row | Audiences are part of targeting; targeting arrives pre-filled with defaults |
| 6 | Step 1 | Whole field table | **Source column added.** "Required" and "asked" are separate things — most fields are now inferred, derived or taken from the advertiser |
| 7 | Step 1 | Strategy name | Requirement Required → Optional; generated from the brief |
| 8 | Step 1 | Target markets | One market per strategy in M1; per-market versus campaign-level fields documented |
| 9 | Step 1 | Primary currency | Required → Optional; taken from the market rather than asked |
| 10 | Step 1 | KPI | **New row added:** KPI target value, 1–5, when the KPI is frequency |
| 11 | Step 1 | Market budgets, Base bids | Type column corrected — "Table" was a UI widget, not a data type |
| 12 | Step 1, Step 6 | Base bids; repair-loop table | Base bids do not apply to CTV. The repair loop loses its bid lever |
| 13 | Step 1 | Frequency cap | **New concept:** advertiser-level defaults, loaded at session start |
| 14 | Step 1, §5 | Formats; `FormatEnum` | Format is always `streaming_tv`. Prime Video is a channel, not a format |
| 15 | Step 1 | Product categories | "Required for video" dropped; taken from the advertiser or implied from the brief |
| 16 | Step 1 | Selling location | **Row removed** — belongs with tracking |
| 17 | Step 1 | Product ASINs | **Row removed** — collected at tracking. Closes the timing question raised twice in v2.0 |
| 18 | Step 2, §6 | Selected deals; state machine | Deals are **matched, not selected**. The checkbox table goes; only channel and CPM are surfaced. Three new rows added |
| 19 | Step 4 | Constraints list, first bullet | Amazon audiences apply to third-party inventory too |
| 20 | Step 4 | The open question below the table | `bundles.narrow/balanced/broad` does not exist. The agent groups a flat list itself |
| 21 | Step 5 | Location row | **Source and Default columns added.** Location defaults to the market's country |
| 22 | Step 5 | Device type, Mobile environment | Device type comes from the advertiser and may be a locked policy. Mobile environment becomes conditional |
| 23 | Step 7, §5, §6 | Whole step; `PlanStatusEnum` | Approval becomes a status change. Manager routing, rejection and the interrupt are removed |
| 24 | Step 8, §4 | Endpoint; API catalogue | Creation uses `simple-strategies`. **Fourteen catalogue rows added or corrected** against the staging API |
| 25 | Step 9, §5 | Click-through URL | Required → Optional — nothing on a television screen is clickable |
| 26 | Step 10, §5 | Three approval rows | Replaced by one status per channel, keyed by data. `provider` renamed to `channel` |
| 27 | Step 11, Step 13, §6 | Whole step; activation | No order between creatives, tracking and credit. **Activation prerequisite checklist added** |
| 28 | Step 11 | "Confirm with client" | A strategy can be updated after creation. Closes the timing question |

**Four questions raised in v2.0 are now answered** and marked `RESOLVED` in place: the ASIN and product-location timing (twice), the audience suggest response shape, and postcode support.

**Two remain open** and are marked `STILL OPEN`: what status a created strategy lands in, and whether per-channel creative approval statuses are readable through the API.

**Twenty-two blocks of questions** are marked `OPEN QUESTIONS` under the relevant notes, for the team to answer before the schema is locked.

---

## 1. Core Principles

UNCHANGED — all three kept exactly as written.

**Zero-Hallucination Policy:** The agent NEVER invents strategy parameters, metrics, targeting criteria, or deal IDs. It only populates values verified against the VOW database and REST APIs.

**Self-Filling Form Paradigm:** The agent operates as a stateful slot-filling engine backed by LangGraph. Inputs via chat or uploaded briefs are parsed into registered Pydantic slot schemas.

**API-Driven Tool Execution:** Every step maps to official VOW API endpoints.

---

## 2. Business Logic

### 2.1 Product Attribution & Selling Locations

UNCHANGED

**On Amazon (ON_AMAZON) [Endemic]:** ASINs required. Enables DPV, ATC, Purchase, ROAS tracking.

**Off Amazon (NOT_SOLD_ON_AMAZON) [Non-Endemic]:** ASINs optional (monitors halo sales). Ad tag conversions required for site event tracking.

### 2.2 Attribution Window

UNCHANGED — 14-day post-view and post-click.

### 2.3 Deal Types

CHANGED — deal types unchanged, but inventory tiers added.

Original deal types (kept):

| Type | Price | Commitment | Can pause? |
|---|---|---|---|
| Programmatic Guaranteed (PG) | Fixed CPM, guaranteed volume | Full budget owed | No |
| Preferred Deals | Fixed CPM | None | Yes |
| Private Auctions | Floor CPM, competitive | None | Yes |

**NEW — Three inventory tiers** (the primary fork in the CTV flow):

Every deal now carries an inventory tier. This classification drives most of the downstream branching — whether reach can be forecast, where the targeting comes from, and whether the deal is selectable now.

| Tier | Examples | Deals | Reach forecast | Audiences |
|---|---|---|---|---|
| Amazon owned | Prime Video | Pre-curated, selectable now | Available | Amazon audiences |
| 3P pre-curated | Netflix, Hulu, others | Pre-curated, selectable now | Not available | Choice per deal — Amazon audiences (may be limited, e.g. device only) or targeting at the inventory source / SSP (adds CPM) |
| 3P needs curation | Disney+, others | Rate-card CPM only; VOW curates the deal after the IO is signed | Not available | Choice, decided at curation — Amazon audiences (may be limited) or targeting at the inventory source / SSP (adds CPM) |

> **REVIEW NOTE — 3P targeting source** (review comment on *"Their own targeting (adds CPM)"*): Targeting on third-party inventory can come from either side: Amazon DSP, or the inventory source / SSP. Amazon's option may be limited in functionality — device only, in some cases. Which options exist is specific to the deal that is chosen or curated, so it is known only after the deal is matched, not at planning time. Recorded on the plan as `targeting_source` (`AMAZON_DSP` / `INVENTORY_SOURCE`). Note that the Audiences column no longer separates the tiers: Amazon audiences can apply to third-party inventory too, so what actually differs by tier is the reach forecast and whether the deal exists yet.

**Why this matters:** a plan spanning Prime + Netflix + Disney has three portions, each with different capabilities. The agent must handle them differently — and be honest about what it can and cannot forecast.

### 2.4 Audience Set Profiles

CHANGED — renamed "Broad" to "Wide" per client vocabulary; fee rules corrected.

| Profile | Was (v1.1.0) | Now |
|---|---|---|
| 1 | Narrow (High Precision) | Narrow — highly targeted, elevated intent, risk of underdelivery |
| 2 | Balanced (Recommended) | Balanced — optimal blend, the usual recommendation |
| 3 | Broad (Maximum Scale) | Wide — broad demographic/interest reach, less precision |

NEW note: the audience fee (VCPM) stacks on top of the deal CPM, so the agent should surface the effective CPM (deal + audience fee), not just the deal price. The fee is set by which data is used — not by how many segments are selected, and not by which profile.

> **REVIEW NOTE — audience data fees** (review comment on *"added fee consequence"*): There is not necessarily a fee consequence, and any fee is not driven by the profile. Three rules apply:
>
> 1. **What triggers a fee** — using 1P data, whether Amazon's own or a third-party first-party audience such as Lifestyle or Interest. This holds regardless of profile.
> 2. **No compounding** — one fixed CPM applies when 1P data is used, however many segments are selected from that provider.
> 3. **Cross-provider stacking** — if the user matches a segment in both Amazon and a third-party provider, both fees are paid.
>
> Narrow, Balanced and Wide therefore differ in reach and precision, not in cost. Recorded on the plan as `audience_data_sources` (`AMAZON_1P` / `THIRD_PARTY` / `NONE`), so the effective CPM is built from the providers in play rather than from the segment count.
>
> **Where the fee values come from** (staging Swagger, checked 4 Aug 2026): `GET /api/contextual-targeting/fees` (model `Fee`) returns them, so the agent reads the fee rather than assuming a figure — which matters, because the effective CPM it quotes drives the impression estimate the trader sees.
>
> Rule 3 above — paying both fees where a segment is matched in both providers — has an endpoint too: `POST /api/audiences/{market}/overlapping-audiences/` reports audience overlap, so the double-fee case can be detected rather than guessed at.

NEW: audiences are optional and suggestion-driven. The agent always suggests three options using VOW's existing pgvector + OpenAI feature (`POST /audience-sets/suggest/`), and the trader may decline them all. Nobody browses the ~3,400 segments manually.

REMOVED for CTV: product audiences (not applicable per client). AMC audiences are conditional — available only when the advertiser has prior campaign data (retargeting tactic).

---

## 3. The Agentic Flow — Step by Step

CHANGED — entirely reordered. The original followed the 6-step UI wizard. This follows the client-confirmed CTV-first agentic flow (v5).

**Comparison: old order vs new order**

| Old (v1.1.0 wizard) | New (v2.0 agentic, confirmed) |
|---|---|
| Strategy details | Basics (+ durations) |
| Goal, KPI & bid | (goal/KPI/bid folded into Basics) |
| Deals | CTV inventory (three-tier fork) |
| — | Budget split NEW (optional) |
| Audiences | Audiences (optional, suggestion-driven) |
| — | Targeting NEW (audiences form part of this step) |
| (forecast was a sub-step) | Predict reach (Amazon only; repair loop) |
| — | Plan approval NEW |
| (create was at the end) | Create the real strategy |
| Creatives | Upload video creative (+ duration check) |
| — | 10. Platform creative approval NEW |
| (ASINs were in step 1) | 11. Tracking setup (ASINs + ad tag) MOVED |
| — | 12. Credit check NEW |
| Summary → create | 13. Activate NEW |

### Step 1: Basics

CHANGED — merged original Steps 1 and 2 (strategy details + goal/KPI/bid), added durations, scoped to CTV.

**What was in v1.1.0 (Step 1 + Step 2):**

Strategy name, flight dates, target markets, primary currency, formats (all four), product categories, selling location, ASINs

Goal (three choices), KPI (six choices), ad tag conversions, market budgets, base bids

**What it is now:**

NEW — a **Source** column. "Required" says whether the plan needs a value; **Source** says where that value comes from. The two are not the same, and conflating them is what made this step look like a form the trader has to fill in. Source values:

| Source | Meaning |
|---|---|
| ASKED | The agent asks the trader outright |
| INFERRED | Read from the brief; asked only when the brief does not say |
| DERIVED | Calculated from another field |
| GENERATED | Composed by the system |
| ADVERTISER | Pre-filled from the advertiser's own settings — read from `GET /api/admin/advertiser/{id}/` (model `AdvertiserAdminRetrieve`) |
| FIXED | A system constant for CTV |
| API | Pre-populated from an API response |
| MATCHED | The agent works it out from what the plan already knows |
| LATER | Not collected in this step |

| Field | Type | Requirement | Source | Change from v1.1.0 |
|---|---|---|---|---|
| Strategy name | String | Optional | GENERATED | CHANGED. Composed from the brief rather than asked for; the trader can rename it. Uniqueness still validated via `GET /api/strategies/check_strategy_name_uniqueness/` |
| Flight dates | Date range | Required | INFERRED | Unchanged. lower ≥ today, upper > lower |
| Target markets | Multi-select | Required | INFERRED | CHANGED. ISO country codes (GB, US, DE). Held as a list, but one market per strategy in M1 — see review note |
| Primary currency | Dropdown | Optional | DERIVED | CHANGED. Derived from the market rather than asked — GB → GBP, US → USD, DE/FR → EUR. Values EUR, GBP, USD |
| Creative durations | Multi-select | Required | INFERRED | NEW. Values: 10, 15, 20, 30 (seconds). Determines which deals are available and what CPM applies |
| Goal | Fixed | Required | FIXED | CHANGED. For CTV, always Awareness. Client: "CTV is typically used as an Awareness goal as it's hard to track anything further down the funnel" |
| KPI | Select | Required | INFERRED | CHANGED. For CTV, reach or frequency only. Was six choices; others scoped out. Stored as `kpi_target_type` |
| KPI target value | Number | Conditional | ASKED | NEW. `kpi_target_value`, an integer from **2 to 5** inclusive. Applies only when the KPI is frequency; absent when the KPI is reach. A frequency of 1 is not offered — one exposure per person is the absence of a frequency target rather than a value for one |
| Market budgets | Decimal, one per market | Required | INFERRED | CHANGED. Type was recorded as "Table", which is how it renders rather than what it holds. Stored as `market_budgets: list[MarketBudgetBidSchema]`; with one market that is a single amount. Must be > 0 |
| Base bids | Decimal, one per market | — | DERIVED | CHANGED. Not asked for CTV — the price is the deal's CPM. Still present in the payload because `MarketBudgetBidSchema.base_bid` is a required field; see review note |
| Frequency cap | Number | Optional | ADVERTISER | CHANGED. Pre-filled from the advertiser's own setting rather than asked; the trader can override it for a single campaign |
| Budget cap | Number | Optional | ADVERTISER | NEW. Was absent; client confirmed optional |
| Formats | List of enum | — | FIXED | CHANGED. Always `["streaming_tv"]`, a system constant, so nothing is asked. `prime_video` dropped — it is a provider, not a format. Display and online_video remain out of scope |
| Product categories | List of int | Required | ADVERTISER → INFERRED | CHANGED. "for video" dropped — CTV is always video, so the condition was always true. Taken from the advertiser's settings, else implied from the brief. Valid values from `GET /api/contextual-targeting/{market}/product-categories/` |

> **REVIEW NOTE — simplify for CTV and imply the answers** (review comment on the two v1.1.0 field lists above): Much of this list came from the general strategy flow rather than a CTV one. Two things follow.
>
> **Cut what does not apply to CTV.** The multi-format choice, the click-based KPIs and the per-market base bid all exist because the original flow covered Display and non-CTV video. For CTV the format is a constant and the price comes from the deal, so those choices have nothing to decide.
>
> **Imply the rest.** The trader should end up being asked for very little — in practice the market, the budget and the dates, and even those are read from the brief when the brief states them. Everything else is generated, derived, taken from the advertiser's settings, or fixed. Hence the Source column above: a field can be required by the plan and still never be put to the trader as a question.
>
> **OPEN QUESTIONS:**
>
> - Is there anything left in this table you would still want the trader **asked outright**, rather than implied? The list is currently down to market, budget and dates.
> - `Budget cap` is marked ADVERTISER here on the assumption it behaves like the frequency cap. Is a budget cap held per advertiser, or is it per campaign?
> - When the agent infers a value, should it show what it inferred and let the trader correct it, or only surface the ones it is unsure about? The first is safer; the second is shorter.
>
> Individual rows in this table are confirmed by later comments in this same review — currency, KPI, frequency cap, formats, product categories, selling location and ASINs each have their own note further down.

> **REVIEW NOTE — strategy name is generated, not asked** (review comment on *"Required"* against Strategy name): The name carries no planning decision — it is a label for finding the strategy again later — so the agent composes it from the brief instead of spending a question on it.
>
> Convention: `{Category}_{Market}_{Goal}_{MonthYear}`, for example `Education_GB_Awareness_Sep2026`. Uniqueness is still checked against `GET /api/strategies/check_strategy_name_uniqueness/`; on a collision the agent appends a version suffix (`_v2`) and re-checks rather than stopping to ask.
>
> The requirement becomes **Optional** and the source **GENERATED**. Those are two separate statements: the plan will always end up with a name, but the trader is never required to supply one, and can rename it afterwards. "Auto-generated" is not a requirement level — it belongs in the Source column.
>
> **OPEN QUESTIONS:**
>
> - Do traders already use a naming convention for finding strategies later? Generating names in a different shape would make their own lists harder to scan, so it is better to match an existing habit than to invent one.
> - `{Category}` comes from the product category, which is itself taken from the advertiser's settings or implied from the brief. If neither is known when the name is composed, what should stand in its place — the advertiser name, or a shorter convention without the category?

> **REVIEW NOTE — multi-market scope and its effect on the flow** (review comment on *"Multi-select"* against Target markets, asking whether multi-market is supported and whether it means repeating choices per market): Recommendation is **one market per strategy in M1**, with the field kept as a list so that adding multi-market later is not a rebuild. If a brief names several markets the agent says so plainly and proposes starting with one rather than silently picking.
>
> On the second half of the question — nothing should be asked twice. Most of the flow is decided once for the campaign; only a few things genuinely vary by market:
>
> | Varies per market | Asked once for the campaign |
> |---|---|
> | Budget allocated to that market | Flight dates |
> | Currency of that market's spend | Goal and KPI |
> | Deals matched, and therefore the CPM | Creative durations |
> | Available locations — `GET /api/strategies/locations/{market}/` | Audience choice |
> | Available product categories — `GET /api/contextual-targeting/{market}/product-categories/` | Creatives and their approval |
> | Reach forecast for that market | Tracking (ASINs, ad tag), credit check |
>
> Two of those are easy to miss: the locations and product-category endpoints are both keyed by market, so those lists differ even when the trader's intent does not. Reach can be added together across markets, since the audiences do not overlap — unlike across providers within one market, where there is no deduplication.
>
> **OPEN QUESTIONS:**
>
> - Is one market per strategy acceptable for M1, or is multi-market needed in the first release? It affects the budget split, the currency rule and per-market deal matching.
> - `primary_currency` is currently a single field. For a multi-market campaign, should the plan total be shown in the advertiser's primary currency with each market's spend in its own, or should the whole plan sit in one currency?
> - When a brief names several markets and M1 supports one, should the agent ask which market to start with, or start with the first named and say so?

> **REVIEW NOTE — currency comes from the market** (review comment on *"Required"* against Primary currency): For a single-market strategy the currency is not a decision — it follows from the market. `GB → GBP`, `US → USD`, `DE` or `FR → EUR`. The dropdown goes, and the requirement becomes **Optional** with source **DERIVED**: the plan always has a currency, but the trader is never asked for one and can still override it.
>
> As with the strategy name, "auto-derived" is not a requirement level. Whether the plan needs a value and where the value comes from are two separate columns, and keeping them separate is the whole point of adding Source.
>
> For multi-market, the proposal is to show the campaign total in the advertiser's primary currency and each market's spend in that market's own currency — flagged as a question under the Target markets note above rather than settled here.
>
> **OPEN QUESTIONS:**
>
> - `CurrencyEnum` holds only EUR, GBP and USD. What should happen for a market whose currency is outside that list — is the enum extended, or are those markets simply out of scope?
> - Should a trader be able to override the derived currency at all, or is the market's currency binding? Overriding it would make the plan total and the deal CPMs disagree unless a rate is applied somewhere.

> **REVIEW NOTE — a frequency KPI can carry a target value** (review comment on *"KPI"*): Choosing frequency as the KPI was recorded without anywhere to put the number the trader is aiming for. A new field `kpi_target_value` holds it — an integer from **2 to 5 inclusive** — shown only when the KPI is frequency and absent when it is reach. The comment said "1-5"; the platform's own control offers 2, 3, 4 and 5, and omitting 1 is right — a frequency of one exposure per person is not a frequency target.
>
> **This is not a label; it changes the forecast.** The impressions are already fixed by budget and CPM, so a frequency target implies the reach the plan has to hit:
>
> ```
> impressions = budget ÷ effective CPM × 1000
> reach = impressions ÷ target frequency
> ```
>
> A target of 3 on 300,000 impressions means the plan needs to reach 100,000 people. If the forecast comes back at a frequency of 5, the audience is too narrow — the same impressions are landing on too few people — and that is what the repair loop should act on. Without the target the agent has nothing to compare the forecast against.
>
> **OPEN QUESTIONS:**
>
> - Should the target feed the forecast and the repair loop as described, or is it recorded for reporting only? The two lead to different agent behaviour.
> - When the KPI is frequency and the trader does not state a target, should the agent assume one — 3 is the obvious middle — or leave it empty and forecast without a target to check against?
> - Is there an equivalent target for a **reach** KPI, or does only frequency carry a number?

> **REVIEW NOTE — "Table" is a widget, not a data type** (review comment on *"Table"* against Market budgets, asking whether it is a single market budget): With one market there is one budget, and a table is a strange way to present a single number. The deeper point is that the Type column had a UI widget in it. Type should say what the field holds; how it is drawn belongs to the interface.
>
> The same correction applies to Base bids, which also read "Table". Both are now stated as an amount per market, with the schema unchanged underneath: `market_budgets: list[MarketBudgetBidSchema]` stays a list so multi-market needs no rebuild, while a single-market plan asks for one number — in practice read from the brief, since briefs state the budget.
>
> **OPEN QUESTIONS:**
>
> - Are there other rows in this table where the Type column still names a widget rather than a type? "Multi-select", "Dropdown", "Radio", "Textarea" and "Checkbox table" all describe controls. Worth agreeing whether this column should hold data types throughout, with the controls recorded separately for the interface.
> - The budget is read from the brief where the brief states one. If a brief gives a range — "eight to ten thousand" — should the agent take the upper figure, the lower, or ask?

> **REVIEW NOTE — base bids do not apply to CTV** (review comment on *"Required"* against Base bids): The price is the deal's CPM, so there is no bid for the trader to set. The field stops being a question and the effective rate is read from the matched deal's rate card, plus any audience data fee.
>
> **This costs the repair loop a lever, which matters more than the field does.** The v1.1.0 loop had two moves when reach fell short: widen the audience, and raise the bid. With fixed-CPM deals the second one is gone. What remains is relaxing the targeting and widening the inventory — and per the audiences note above, even the audience lever may be absent when the trader has chosen no audience. The repair-loop row in Step 6 has been corrected accordingly.
>
> Widening the inventory has its own limit worth stating: adding Netflix or Disney+ raises impressions, but those tiers return no reach forecast, so the agent cannot verify that the added inventory fixed the reach shortfall. It should say so rather than imply the problem is solved.
>
> **OPEN QUESTIONS:**
>
> - **Private auction deals carry a floor CPM, not a fixed one** — §2.3 describes them as "Floor CPM, competitive". Does a bid still matter there? If it does, the agent keeps a bid lever on that deal type and the answer is narrower than "base bids do not apply to CTV".
> - `MarketBudgetBidSchema.base_bid` is a required field on the create payload. If the trader is never asked for it, what should be sent — the deal's CPM, a null, or does the CTV create endpoint drop the field entirely?

> **REVIEW NOTE — advertiser-level defaults** (review comment on *"Optional"* against Frequency cap: *"we have a default per advertiser"*): This introduces a concept the document did not have. Some settings belong to the advertiser, not to the campaign — they do not change from one brief to the next, so asking for them every time is wasted effort. The frequency cap is the first of several: product categories, selling location and device type all turn out to sit here too, each confirmed in a later comment.
>
> **Where they come from and when.** Advertiser settings are read at the start of the session, before the brief is parsed — `GET /api/admin/advertiser/{id}/`, model `AdvertiserAdminRetrieve`. Loading them first and parsing the brief second gives the right precedence: the defaults fill the form, and anything the brief states overrides them.
>
> **One thing a plain default cannot express.** A later comment notes that some advertisers permit Connected TV only. That reads less like a default and more like a policy — something the trader should not be able to override, and that the repair loop must not quietly relax when reach falls short. So each setting needs to carry whether it is binding, not just its value:
>
> ```python
> class AdvertiserSetting(BaseModel):
> value: Any
> is_locked: bool = False # a brand policy the trader cannot override
> reason: Optional[str] = None # shown to the trader when locked
> ```
>
> Without `is_locked` the agent cannot tell the difference between a starting point and a rule, and will offer to relax something it is not allowed to touch.
>
> **OPEN QUESTIONS:**
>
> - **What is the full list of settings held per advertiser?** Knowing it now means building the section once instead of adding a field each time one surfaces. So far: frequency cap, product categories, selling location, device type — and possibly budget cap.
> - Which of them are **locked** brand policies rather than overridable defaults? That decides what the repair loop is allowed to change.
> - Does the advertiser record already hold a frequency cap, or does that field need adding? The endpoint exists; whether it carries this value is not visible from the API listing alone.
> - When an advertiser has no value set for one of these, what should the agent do — leave it empty, or fall back to a platform-wide default?

> **REVIEW NOTE — the format is always `streaming_tv`; Prime Video is a provider** (review comment on *"Required"* against Formats: *"is always streaming_tv"*): With one possible value there is no choice to present, so the field becomes a constant and leaves the list of things the trader is asked.
>
> The row also mixed up two levels. `prime_video` was listed as a format, but Prime Video is a **provider** — it sits inside `streaming_tv` alongside Netflix, Disney+ and others. Format is the kind of inventory; provider is who is showing the ad.
>
> **The document already contradicted itself on this.** Step 2 fetches deals with `GET /api/deals/?markets={market}&formats=streaming_tv` — `streaming_tv` only. And `SelectedDealSchema.provider` is described as *"e.g. Prime Video, Netflix, Disney+"*, so Prime Video was already captured correctly one step later. Step 2 was right; Step 1 was carrying a v1.1.0 mistake, where the deals table was even headed "Prime Video Deals". `FormatEnum.PRIME_VIDEO` has been annotated rather than deleted, since removing an enum value is a breaking change for anything already sending it.
>
> **OPEN QUESTIONS:**
>
> - Which format values does the API actually accept for a CTV strategy — `streaming_tv` only? `GET /api/strategies/choices/` and the `FormatsAndKpis` model look like the place this is defined, so it is worth reading rather than assuming.
> - The v1.1.0 create payload example sends `"formats": ["prime_video"]`. Should that be corrected to `["streaming_tv"]` in the API examples further down, or does the endpoint still accept the old value?

> **REVIEW NOTE — product categories come from the advertiser or the brief** (review comment on *"Required for video"*: *"we have a default on the advertiser, or maybe could imply from the brief"*): A product category does not change from one campaign to the next — BrightPath is an education advertiser on every brief — so asking for it each time treats a property of the advertiser as if it were a decision about the campaign.
>
> Resolution order: the advertiser's own setting first, and where that is absent, what the brief implies — "an education website" is enough to place it.
>
> The **"for video"** qualifier goes too. It arrived from v1.1.0, where Display was also in scope. CTV is always video, so the condition is always true and reads as if there were a case where the field did not apply.
>
> **A third source exists but arrives too late to fill this field.** `POST /api/contextual-targeting/{market}/asin-validation/` returns a product category alongside each valid ASIN. Since ASINs are collected at the tracking step, well after this one, that category cannot populate Step 1 — but it is worth using as a **cross-check**: if the advertiser is set to Education and the ASINs come back as Electronics, something is wrong and the agent should say so rather than let the mismatch through.
>
> **OPEN QUESTIONS:**
>
> - **Is the advertiser-level value actually a product category, or an industry?** The advertiser endpoints expose `GET /api/admin/advertiser/get_industry_and_sub_industry_choices/`, while product categories come from a different taxonomy entirely (`GET /api/contextual-targeting/{market}/product-categories/`, models `ProductCategory` and `ProductSubcategory`). If the advertiser holds an industry, a mapping between the two is needed and is not currently anywhere in this document.
> - Does an advertiser carry one category or several? The field is a list, so the agent should match whatever shape the advertiser record uses.
> - Product categories are fetched per market. For a multi-market campaign, can the same category be assumed available in every market, or must each be checked?

> **REVIEW NOTE — selling location leaves this step** (review comment on *"Required"* against Selling location: *"can leave out"*): The row has been removed from the table above. Whether the advertiser sells on Amazon decides **how conversions are measured**, not how the plan is built — so it belongs with the tracking step, where the ASIN and ad-tag questions already sit. The tracking step asks *"Sells on Amazon?"* already; this is the same question, and it was being asked in two places.
>
> It is also an advertiser-level property rather than a campaign one, so it arrives pre-filled from the advertiser's settings and the trader only changes it in the rare case a campaign differs.
>
> **This quietly resolves half of the open question flagged twice in this document.** The concern was that `product_location` is required by the `POST /strategies/` payload at Step 8, yet was being collected at Step 11 afterwards. If the value comes from the advertiser's settings — loaded at the start of the session — then the agent already holds it when it creates the strategy, and nothing needs patching. Only the ASINs still arrive later; that half is dealt with in the notes on the ASIN row and on post-creation updates.
>
> **OPEN QUESTIONS:**
>
> - Can one advertiser have campaigns with different selling locations — some driving to Amazon, some to their own site? If so this stays an overridable default rather than a fixed advertiser property.
> - If an advertiser has no selling location set and the brief does not say, is it safe to assume `NOT_SOLD_ON_AMAZON` and rely on ad-tag tracking, or should the agent ask?

> **REVIEW NOTE — product ASINs leave this step too** (review comment on *"Conditional"* against Product ASINs: *"comes later"*): This one confirms what the revision already said — ASINs moved to the tracking step. The correction is smaller: if they come later, they should not still be listed here with a note attached. The row has been removed.
>
> The sequence is: create the strategy with `product_asins: []`, then collect and validate the ASINs at the tracking step and update the strategy. Validation is unchanged — `POST /api/contextual-targeting/{market}/asin-validation/`, keyed by market rather than hard-coded to a single one.
>
> With the selling-location note above, this closes the timing question that appeared twice in this document.
>
> **OPEN QUESTION:**
>
> - Should the ASIN list be validated in one call at the tracking step, or as the trader pastes them in? Validating late means a trader can enter twenty ASINs and only then learn that three are wrong.

**API calls at this step:** `GET /api/strategies/check_strategy_name_uniqueness/`, `GET /api/contextual-targeting/{market}/product-categories/`

REMOVED from this step: ad tag conversions (moved to Step 11), the three non-CTV format options (Display, Online Video — future scope), the four non-awareness KPIs (CTR, CPC, CPA, CPDPV — future scope)

> **RESOLVED — was: open question on `product_location` and `asin_numbers` timing.** Both were listed in this step while also being collected at the tracking step, after the strategy is created. The answer is to collect them late and let the strategy be updated afterwards:
>
> - `product_location` arrives from the advertiser's settings, so the agent already holds it when it creates the strategy — nothing to patch.
> - `asin_numbers` is sent as an empty list at creation and filled in at the tracking step via `PATCH /api/strategies/{id}/` (model `StrategyUpdate`, confirmed present in the staging API).
>
> The second half of this question is repeated further down at the tracking step and is closed there too.

### Step 2: CTV Inventory (the tier fork)

CHANGED — was Step 3 "Deals" in v1.1.0. Now comes before audiences, and introduces the three-tier fork.

**What was in v1.1.0:**

A flat deals table filtered by market and format, with checkbox selection

**What it is now:**

| Field | Type | Requirement | Source | Change from v1.1.0 |
|---|---|---|---|---|
| Channel | List of str | Optional | INFERRED | NEW. Which providers to run on — Prime Video, Netflix, Disney+. This is the strategic choice; the deal underneath it is not |
| ROS or genre | String | Optional | INFERRED | NEW. Run-of-service, or a named genre, used to narrow the match |
| Selected deals | List of deal objects | Required | MATCHED | CHANGED. No longer picked from a table. Matched from the market, duration and channel, with optional ROS or genre and the targeting requirements. Candidates from `GET /api/deals/?markets={market}&formats=streaming_tv` |
| Specific deal ID | String | Optional | ASKED | NEW. `specific_deal_id` — an escape hatch for a trader who already has a particular deal in mind |
| Inventory tier (per deal) | Enum | Derived | DERIVED | NEW. Each deal classified as AMAZON_OWNED, THIRD_PARTY_PRECURATED, or THIRD_PARTY_NEEDS_CURATION |
| CTV rate card | Reference | Read | API | NEW. `GET /api/rates/ctv/{market}/` — channels, durations, CPMs |

**NEW — Genre upsell logic:** The client asked: "based on the brief we can suggest whether a specific available genre would be a better match at a slightly higher CPM." Example: Prime Video ROS at $18.22 vs Action at $22.07 — the agent should recommend when the brief implies a genre match.

**NEW — Curation capture** (for 3P-needs-curation tier): When deals can't be selected yet (Disney+ etc.), the agent captures what VOW needs to curate later: genres, durations, targeting preferences, budget, flight dates.

| Field | Type | Requirement |
|---|---|---|
| Curation: genres | Multi-select | Required for curation tier |
| Curation: durations | Multi-select | Required for curation tier |
| Curation: targeting prefs | Text | Optional |
| Curation: budget | Number | Required for curation tier |
| Curation: flight dates | Date range | Required for curation tier |

**API calls at this step:** `GET /api/deals/`, `GET /api/deals/filter-properties/`, `GET /api/rates/ctv/{market}/`

> **REVIEW NOTE — deals are matched, not selected** (review comment on *"Checkbox table"* against Selected deals): This reverses the order of the step. The table went; the trader states requirements and the agent finds the deals that fit them.
>
> **What the trader decides, and what the agent works out.** Choosing Prime Video over Netflix is a real decision. Choosing between `EXT7P75718S8MNR` and `EXT7P75719Q2LKM` is not — it is plumbing. So the trader supplies the channel, optionally a genre or run-of-service, and the targeting they want; the agent matches on market, duration and channel and returns what fits. A trader who already has a deal in mind can name it through `specific_deal_id`, which keeps the shortcut without making everyone use it.
>
> **What is surfaced.** The channel, the effective CPM and the estimated impressions. Not deal IDs, not raw deal names — a name like *"Prime Video | Preferred Deal | UK - 30 - ROS"* carries nothing the trader cannot see more plainly elsewhere, and mis-reading one silently changes the plan.
>
> **Two things must still surface, even though the deal does not.**
>
> - **Tier capability.** Third-party tiers return no reach forecast. If only the CPM is shown, the trader has no way to know that the reach figure is missing for part of the plan — and Step 6's honesty rule requires telling them.
> - **Commercial commitment.** A Programmatic Guaranteed deal owes the full budget and cannot be paused (§2.3). Hiding the deal must not hide that. The agent should say it plainly before the trader accepts the CPM — *"this is a guaranteed deal, so the full £6,000 is committed and cannot be paused"* — rather than let a commitment pass unnoticed because the deal type was internal.
>
> This pattern was already in the revision, in one place: the curation capture below, where deals cannot be selected yet and the agent records genres, durations, targeting and budget instead. That is exactly the model being described. It simply was not applied to the tiers where deals do exist.
>
> The graph node has been renamed from `select_inventory` to `match_inventory_deals` so the code says what it does.
>
> **OPEN QUESTIONS:**
>
> - **Is a deal's built-in targeting available as structured fields, or only in its name?** `GET /api/deals/filter-properties/` (model `AmzDealFilterProperties`) looks like the place this lives, and if it holds genre, ROS and targeting then matching is straightforward. If those facts exist only inside the deal name, the agent would have to parse a string to decide what to buy, which the Zero-Hallucination principle rules out. This is the one answer that decides whether this step can be built as described.
> - When several deals match, how should the agent choose — cheapest CPM, best genre fit, or largest forecastable reach?
> - When nothing matches, what should happen? Widen the duration, drop the genre, or report back and ask?
> - Should a Programmatic Guaranteed deal ever be matched automatically, given the budget commitment, or only when the trader has asked for one?

### Step 3: Budget Split

ENTIRELY NEW — did not exist in v1.1.0. Added per client requirement.

> "We will need to support the suggested budget split across inventories or creative durations."

The agent proposes how the total budget is divided across inventories (Prime / Netflix / Disney) and across creative durations (15s / 30s). This is genuinely hard — different durations have different CPMs, and there's no reach data for Netflix/Disney to optimise against.

| Field | Type | Requirement |
|---|---|---|
| Split by inventory | Allocation (%) | Optional — preferred when more than one inventory is selected |
| Split by duration | Allocation (%) | Optional — preferred when more than one duration is selected |
| Split method | Enum | Agent states its assumption |

**Split method options:**

- **EVEN_BY_BUDGET** — same £ per inventory/duration; uneven impressions (higher CPM = fewer impressions)
- **EVEN_BY_IMPRESSIONS** — same impression count; uneven £ (higher CPM = more spend)

The agent must state which it chose and why, so the trader can adjust. Example: "I've split evenly by impressions, which weights spend toward the 30s at its higher CPM."

No API call — this is agent-side logic. The resulting budgets feed into the `market_budgets` field at strategy creation.

> **REVIEW NOTE — budget split is optional** (review comment on *"Budget split NEW"*; UI placement from a separate comment): The split is optional, not required. It is preferred because each inventory and each duration carries a different CPM, so a real split produces an accurate CPM; without one the agent must present a blended estimate and should say so plainly. The agent proposes a split by default and the trader can accept, adjust or skip it.
>
> **UI placement:** rather than a standalone step, the split is surfaced as a substep inside Step 2 (CTV Inventory), appearing only when more than one inventory deal is matched — with a single deal there is nothing to split. The step numbering here is left unchanged so the review comments stay anchored; the substep is a presentation decision, not a change to the flow's logic.

### Step 4: Audiences

CHANGED — was Step 4 in v1.1.0 and optional. Still optional, now suggestion-driven, and positioned after the budget split.

**What was in v1.1.0:**

Browse/search audience sets, checkbox selection, Similar/Exact toggle

**What it is now:**

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Audience options | 3 profiles | Optional | Requirement unchanged — still optional. Agent always generates narrow / balanced / wide |
| Chosen option | Select one | Optional | NEW. Trader picks one of the three, or declines them all and runs with no audience |
| Matching mode | Toggle | Conditional | Unchanged. Similar vs Exact — applies only when an audience is chosen |
| Effective CPM (per option) | Display | Read-only | NEW. Deal CPM + audience VCPM fee, shown per option so the trader sees the real cost |

**Constraints for CTV:**

- Amazon audiences can be applied to third-party inventory as well as Amazon-owned. The alternative is the inventory source's own targeting — a choice made per deal, not a property of the tier
- Product audiences not applicable to CTV (removed)
- AMC audiences are conditional — only when the advertiser has prior campaign data
- Nobody browses — the agent uses `POST /api/audience-sets/suggest/` exclusively
- The audience set does not need to be created before forecasting — it's created later at strategy creation via a simplified CTV endpoint

> **REVIEW NOTE — audiences are optional** (review comment on *"mandatory"* in the flow comparison above): Audiences were optional in v1.1.0 and remain optional. This revision had promoted them to mandatory; that is reverted. The agent still suggests three options every time, but the trader can decline all of them and run with no audience — a run-of-service baseline, which also means no 1P data and therefore no data fee (see §2.4).
>
> **Consequence for the repair loop:** widening the audience is one of the levers the agent uses when reach falls short. When no audience has been chosen that lever does not exist, so the agent has to work with budget, flight duration and the other targeting instead — and should say plainly when it has nothing left to relax rather than implying a fix is available.

> **REVIEW NOTE — Amazon audiences reach third-party inventory too** (review comment on *"Netflix/Disney"* in the constraints above: *"can use amazon audiences too"*): The word "only" was wrong. Amazon audiences are not confined to Amazon-owned inventory — they can be attached to Netflix, Disney+ and the rest. The inventory source's own targeting is the alternative, not the only option.
>
> This is the same mistake as the one on the tier table in §2.3, appearing a second time in this list. Both now describe a choice made per deal.
>
> **It changes the cost arithmetic, which matters more than the wording.** The earlier assumption was that an Amazon data fee could only apply to the Amazon portion of a plan. If Amazon audiences run on the third-party portion as well, the fee applies there too, and the effective CPM for that portion rises accordingly. The trader is comparing three situations rather than two: no audience data at all, Amazon data across the whole plan, or Amazon data on Amazon inventory with the source's own targeting elsewhere.
>
> **What the agent still cannot do on third-party inventory is verify the result.** Those tiers return no reach forecast, so the agent can widen an audience there but cannot show that it worked. It should say so rather than present an unverified change as a fix.
>
> The Audiences column in the §2.3 tier table therefore stops separating the tiers. What genuinely differs by tier is whether a reach forecast comes back and whether the deal exists yet.
>
> **OPEN QUESTIONS:**
>
> - Can Amazon audiences and the inventory source's own targeting both run on the **same** deal, or is it one or the other?
> - How limited is Amazon's targeting on third-party inventory in practice? The tier-table note says it may be device-only in some cases; knowing where the line falls decides whether the agent should recommend it or the source's own targeting.
> - The reply on this comment quoted a £2.00 VCPM Amazon data fee. Should figures like that be read from `GET /api/contextual-targeting/fees` in every case rather than written into the specification, so the plan never quotes a stale rate?

**API calls at this step:** `POST /api/audience-sets/suggest/` → `GET /api/audience-sets/suggest/{id}/`

> **RESOLVED — was: open question on the suggest endpoint's response shape.** There is no `bundles.narrow/balanced/broad` object; the endpoint returns a flat list of segments and the grouping is ours to do.
>
> **REVIEW NOTE — the three profiles are built by the agent, not returned by the API** (review comment on *"bundles.narrow/balanced/broad"*: *"not currently supported"*): v1.1.0 assumed the endpoint handed back three ready-made groups. It does not. The agent receives a flat list of segments with their reach and relevance, and assembles the three profiles itself.
>
> **This changes what the three profiles are.** Taken with the two earlier notes — the fee depends on the data provider rather than the profile, and choosing a profile is optional — Narrow, Balanced and Wide are no longer an API feature with three price points. They are a way of presenting the same flat list at three levels of breadth. They differ in reach and precision. They do not differ in cost.
>
> **The grouping rule now has to be written down, because nothing upstream provides it.** Proposal: group by **cumulative reach**, since the fee no longer separates the options and reach is what actually distinguishes them; keep the groups **nested**, so Balanced contains Narrow and Wide contains Balanced, which is easier to reason about than three unrelated sets; and add segments until each group meets a reach target rather than a fixed segment count, so the profiles stay comparable across briefs of different sizes.
>
> The `broad` versus `WIDE` naming mismatch noted in v1.1.0 disappears with the `bundles` object — there is no API field to disagree with, and `AudienceProfileEnum.WIDE` stands.
>
> **OPEN QUESTIONS:**
>
> - **Could we have a real response sample from `POST /api/audience-sets/suggest/`?** Knowing that `bundles` is wrong is only half the answer; the grouping rule, the fee handling and the audience schema all depend on the actual shape. This is the single most useful thing to unblock the audience work.
> - The request model in the staging API is named `SuggestAudienceGroupsInput`. Does "groups" mean the **caller** asks for a number of groups? If the endpoint can be told how to group, the agent may not need its own logic at all.
> - `POST` returns an id and `GET /api/audience-sets/suggest/{id}/` reads the result, so suggestion looks asynchronous. How long does it usually take? It decides whether the agent waits in the conversation or tells the trader it will come back.
> - Is grouping by cumulative reach the right basis, or should relevance score lead? The proposal above assumes reach.
> - the comment said "not **currently** supported". If `bundles` arrives later, the agent's grouping should be replaceable rather than baked in — is it worth designing for that now?

### Step 5: Targeting

ENTIRELY NEW — did not exist in v1.1.0.

| Field | Type | Requirement | Source | Default |
|---|---|---|---|---|
| Location | List of str | Optional | DERIVED | The market's country — `markets = ["GB"]` gives `location = ["GB"]` |
| Instream position | Enum | Optional | ASKED | None |
| Content-category exclusions | List of str | Optional | ADVERTISER | The advertiser's brand-safety exclusions, where it has any |
| Device type | List of str | Optional | ADVERTISER | The advertiser's own setting — Connected TV only for some brands. May be locked rather than merely defaulted; see note |
| Mobile environment | Enum | Conditional | ASKED | None — applies only when Mobile or Tablet is among the device types |

**Critical design note from the client:** "This targeting list frequently changes so it should be easy to add new targeting types." — the implementation must be config-driven, not hard-coded. Adding a new targeting type should be a configuration change, not a code change.

Not supported by VOW today (future scope): genre exclusions, day-parting, language.

> **REVIEW NOTE — audiences are part of targeting, and targeting arrives pre-filled** (review comment on *"Targeting NEW"*): Audiences are one kind of targeting, not a separate stage. Once the inventory is decided or inferred, the trader is shown a default targeting baseline already applied — country targeting and Connected TV device only — and then either refines it or accepts it as sufficient.
>
> Three ways to proceed from the baseline, and they are alternatives rather than a sequence:
>
> - define audience segments;
> - narrow the geography instead — the example given is a trader who wants postcodes rather than audiences;
> - accept the baseline as it stands.
>
> The practical consequence is that no field in this step starts empty, and the trader is never asked to fill a blank targeting form. Geography can substitute for audience targeting entirely.
>
> Steps 4 and 5 are therefore a single step in the flow. The numbering here is left unchanged so the review comments stay anchored; the merge is how the step is presented, not a change to what it collects.

**API calls at this step:** `POST /api/contextual-targeting/{market}/products/`, `GET /api/strategies/locations/{market}/`

> **RESOLVED against the API** (staging Swagger, checked 4 Aug 2026): postcode targeting is supported — `POST /api/strategies/postcode-validation/{market}/` validates postcodes for a market, alongside `GET` and `POST /api/strategies/locations/{market}/` for country, region and city. the postcode example is therefore buildable.
>
> The same check turned up `POST /api/strategies/{id}/targeting/auto-rec/` (model `StrategyTargetAutoREC`), which recommends targeting automatically. The default baseline described above may not need to be assembled agent-side at all — this endpoint looks like it already does it. Worth confirming what it returns before writing that logic ourselves.

> **REVIEW NOTE — location defaults to the market's country** (review comment on *"Optional"* against Location: *"defaults to market country"*): The field does not start empty. It is filled with the market's own country, and the trader narrows it from there — to a region, a city, or a postcode. Optional therefore means "you need not touch it", not "it is blank until you do".
>
> **`markets` and `location` are not the same field, even though both usually say GB.** The document has never said so, which makes them look like duplication. They answer different questions:
>
> | | Question it answers | What it decides |
> |---|---|---|
> | `markets` | Which market are we buying in? | Which deals exist, which rate card applies, which currency, which category and location lists |
> | `location` | Where should the ad be allowed to show? | Geographic delivery |
>
> They start the same and diverge as soon as the trader narrows: buying GB inventory but delivering only in London is `markets = ["GB"]` with `location = ["London"]`.
>
> **Narrowing costs reach, and the agent should say so.** Moving from country to a handful of postcodes can cut the addressable audience sharply. Since the trader did not see a forecast when they narrowed, the agent should report the effect rather than let the reach shortfall appear later as a surprise.
>
> Device type is also defaulted rather than asked, but from the advertiser rather than the market — that is the subject of the next comment.
>
> **OPEN QUESTIONS:**
>
> - Should content-category exclusions default from the advertiser's brand-safety settings? They are marked that way above on the assumption that brand safety is an advertiser-level rule rather than a per-campaign choice, but that has not been confirmed.
> - When a trader narrows the geography, should the agent re-forecast immediately and show the reach change, or wait until the forecast step?

> **REVIEW NOTE — device type is an advertiser setting, and "CTV" means two different things** (review comment on *"Optional"* against Device type: *"Some advertisers only want CTV only - set at advertiser level"*): The field arrives filled from the advertiser rather than asked. This is the third setting to turn out to live on the advertiser, after the frequency cap and the product category.
>
> **The comment also separates two things this document had been blending.**
>
> | | What it is | Where it is decided |
> |---|---|---|
> | `formats = ["streaming_tv"]` | The kind of content — streaming video | A constant for CTV |
> | `device_types = ["Connected TV"]` | The screen the ad plays on | The advertiser's setting |
>
> Streaming content is not watched only on television sets. Prime Video runs on phones, tablets and desktop browsers, all of which are still `streaming_tv`. **The document proves this itself:** the `Mobile environment` field in this same table — in-app versus mobile web — would be meaningless if delivery were confined to television screens. Its existence is the evidence that it is not.
>
> That field has accordingly become **Conditional**: it only applies when Mobile or Tablet is among the device types, and is meaningless otherwise.
>
> **Restricting to Connected TV has two effects the trader did not choose.** A large share of streaming viewing happens on mobile, so the available inventory shrinks; and Connected TV inventory is priced above mobile, so the CPM rises and the same budget buys fewer impressions. Since this comes from the advertiser rather than the brief, the agent should surface both effects rather than let the plan simply come back smaller than expected.
>
> **This is where the difference between a default and a policy starts to matter.** "Only want CTV only" reads like a rule, not a starting point. Relaxing the device targeting is one of the levers the repair loop reaches for when reach falls short — and if the advertiser has ruled it out, that lever is not available. The agent must not offer to widen something it is not allowed to touch, and should say which lever it could not use. This is what the `is_locked` flag on `AdvertiserSetting` is for, introduced in the frequency-cap note above.
>
> **OPEN QUESTIONS:**
>
> - Is the device setting a **default the trader can override**, or a **locked brand policy**? This decides whether the repair loop may touch it, and it is the one answer that changes agent behaviour rather than wording.
> - Which other advertiser settings can be locked in the same way? Brand-safety exclusions look like candidates.
> - If an advertiser has no device setting at all, what should the fallback be — Connected TV only, or all devices?
> - Are `Connected TV`, `Mobile`, `Tablet` and `Desktop` the full set of device types, and does that list come from an endpoint rather than being fixed in the schema?

### Step 6: Predict Reach

CHANGED — was embedded in the original flow. Now a first-class step with the tier-based honesty rule.

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Reach curve | Chart | Read-only (Amazon only) | CHANGED. Only available for Amazon-owned inventory. For 3P, state honestly that reach is unavailable |
| Estimated impressions | Number | Read-only | Unchanged |
| Estimated unique reach | Number | Read-only (Amazon only) | CHANGED. Not available for Netflix/Disney |
| Average frequency | Number | Read-only (Amazon only) | CHANGED. Not available for Netflix/Disney |
| Indicative CPM | Number | Read-only | Unchanged |

**NEW — the honesty rule for 3P inventory:** For Netflix/Disney, the agent shows: rate-card CPM and derived impressions (budget ÷ CPM × 1,000). It explicitly states that reach is unavailable and why. Never invent a reach number.

**NEW — consequences:**

- The repair loop (too narrow → widen → re-forecast) applies only to the Amazon portion
- Total reach cannot be summed across providers (no cross-platform deduplication)

**Repair loop** (v1.1.0 §7.1 — concept correct, mechanism updated):

| Was (v1.1.0) | Now |
|---|---|
| If `estimated_unique_reach == 0`, switch from Narrow to Balanced/Broad | If reach is insufficient, extend the audience (not necessarily switch profiles — could add segments within the chosen profile) |
| Also adjust base CPM bid upward | No longer applies. CTV deal CPMs are fixed, so there is no bid to raise. Replaced by relaxing the targeting and widening the inventory |
| Re-run forecast | Unchanged |

**API calls at this step:** `POST /api/audience-sets/reach-forecast/` (or the simplified CTV endpoint, name TBC)

### Step 7: Finalise Plan

ENTIRELY NEW — did not exist in v1.1.0.

The plan is finalised by the trader within the conversation. Nothing is routed to a manager for now.

| Field | Type | Requirement | Source |
|---|---|---|---|
| Plan status | Enum | Required | ASKED |
| Finalised by | String (user) | Set on finalisation | DERIVED |
| Finalised at | Timestamp | Set on finalisation | GENERATED |

Values: DRAFT → FINALISED

**Implementation:** a status change, not a gate. The graph does not stop and wait for a second person — the trader finalises the plan in the same conversation and the flow continues.

No API call — this is agent-internal. The change is logged in the audit trail.

> **REVIEW NOTE — approval became a status change** (review comment on the *"Plan Approval"* heading: *"we simplified this so it's just a status changed to finalise the plan - no manager approval required for now"*): The step is renamed **Finalise Plan** and reduced to one status moving from `DRAFT` to `FINALISED`, done by the trader in the conversation. The `Manager required` and `Rejection reason` fields are gone, as is the rejection path back to the audience step.
>
> **What this removes is larger than one field.** An approval gate meant a second person: a notification to send, a wait of unknown length, a rejection route, a threshold rule deciding when approval was needed, and roles saying who could give it. All of that leaves M1.
>
> **It also removes a place where the agent had to stop.** The step used a LangGraph `interrupt()` — the graph halted and persisted state until someone else acted, which could be hours later, with the conversation left open in between. That interrupt goes. The one at the creative-approval step stays, and correctly so: there the agent is waiting on Amazon's or a publisher's review, which genuinely is external and asynchronous. The distinction is worth keeping clear — pausing for a review the platform performs is not the same as pausing for a colleague.
>
> **Two things kept deliberately extensible**, because the comment said "for now":
>
> - `PlanStatusEnum` is its own enum rather than reusing `ApprovalStatusEnum`. The plan and the creative now have different lifecycles — `DRAFT`/`FINALISED` against `PENDING`/`APPROVED`/`REJECTED` — and sharing one enum would force one to carry values the other cannot use. Adding `PENDING_APPROVAL` later is then additive rather than a rework.
> - The `approval_status`, `approved_by` and `approved_at` fields have been renamed to `plan_status`, `finalised_by` and `finalised_at`, so the names describe what actually happens.
>
> **Where approval may return is not as a manager gate.** After the advertiser-defaults note above, the more likely shape is an advertiser-level rule — "plans over £10,000 need my sign-off" — which is an advertiser policy rather than an approval workflow inside VOW. Leaving room for `approval_threshold` on the advertiser settings costs nothing now and avoids a rework if it appears.
>
> **OPEN QUESTIONS:**
>
> - Can a finalised plan return to `DRAFT`? It decides whether the agent should warn before finalising or treat it as reversible.
> - What can still change after a plan is finalised? The budget and the matched deals are commercial commitments, so they are not obviously in the same category as, say, the targeting.
> - Is an advertiser-level approval threshold something to plan for, or is approval out of scope entirely for now?
> - Which endpoint records the status change? Nothing in the staging API obviously covers a plan status as distinct from `POST /api/strategies/{id}/set_status/`, which is activation.

### Step 8: Create the Real Strategy

CHANGED — was "Summary & Create" (Step 6) in v1.1.0. Key change: create the real strategy, not a draft.

**What was in v1.1.0:**

Summary view → `POST /api/strategies/` or `POST /api/strategies/draft/` → returns `status: "draft"`

**What it is now:**

| Field | Change |
|---|---|
| Endpoint | `POST /api/strategies/` — not `/strategies/draft/`. Client: "don't need to create draft strategy; draft is just for the wizard creation" |
| Audience set | Created at this step via the simplified CTV endpoint (not before forecasting) |
| All slots | All filled slots from Steps 1–7 are assembled into the creation payload |

**API calls at this step:** `POST /api/simple-strategies/`, audience-set creation via CTV endpoint

> **STILL OPEN:** what status does the created strategy land in? If it is `draft` by default, activation via `set_status` remains a separate step. This is a different question from the plan status settled at Step 7 — the plan being `FINALISED` says nothing about what state the created strategy sits in.

> **REVIEW NOTE — creation uses `simple-strategies`** (review comment on *"api/strategies"*: *"probably more likely simple-strategies endpoint"*): Confirmed against the staging API — `POST /api/simple-strategies/` exists, with request model `SimpleStrategyCreate`. The comment said "probably"; it is no longer a guess.
>
> **The wider point was that one wrong endpoint is rarely alone.** The API calls in this document came across from v1.1.0 and were never re-checked, so the whole list was read against the staging Swagger. What that found:
>
> | Assumed here | Reality |
> |---|---|
> | `POST /api/strategies/` for creation | `POST /api/simple-strategies/` — the CTV variant, POST only |
> | *(no update endpoint listed)* | `PATCH /api/strategies/{id}/` exists — model `StrategyUpdate` |
> | `POST /api/rate-cards/match/` for deal matching | **Does not exist.** Matching uses `GET /api/deals/` with `GET /api/deals/filter-properties/` |
> | `/api/advertisers/{id}/defaults/` for advertiser settings | **Does not exist.** Settings are at `GET /api/admin/advertiser/{id}/` |
> | Postcode support unknown | `POST /api/strategies/postcode-validation/{market}/` exists |
> | Fee values unknown | `GET /api/contextual-targeting/fees` exists |
>
> Note that `simple-strategies` supports **POST only** — there is no read or update on it. So a strategy is created through the CTV endpoint and then updated through the general one, which is worth stating plainly since it looks inconsistent otherwise.
>
> Endpoints found that this document does not mention at all have been added to the catalogue in §4.
>
> **OPEN QUESTIONS:**
>
> - **What is `POST /api/automated-strategies/`?** It sits alongside `simple-strategies` in the API, with models `AutomatedStrategyCreate` and `AutomatedStrategyFormatsAndKpis`. The name suggests it may be closer to what an agent needs than `simple-strategies` is. Which of the two is intended here?
> - Could we have the field list for `SimpleStrategyCreate`? The payload described in this document — no base bid, format fixed, advertiser defaults pre-filled — needs to match it field for field, and the endpoint listing alone does not show that.
> - `strategies-sp` is a separate family with its own draft endpoints. Confirming that is sponsored products and irrelevant to CTV would close it off.

### Step 9: Upload Video Creative

CHANGED — was Step 5 "Creatives" in v1.1.0. Simplified to video only, moved to after plan approval, and duration check added.

**What was in v1.1.0:**

Browse assets and pre-approved creatives, select from table, add click-through URL

**What it is now:**

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Video file | Upload (direct or URL) | Required | CHANGED. For CTV, always video. No display creatives, no pre-approved selection, no responsive e-commerce |
| Click-through URL | HttpUrl | Optional | CHANGED. Nothing on a television screen can be clicked, so the field stops being required. Still validated as a URL when one is given. Recommended where the device types include mobile, tablet or desktop |
| Duration | Derived from file | Checked | NEW. Must match one of the durations in the approved plan |

**NEW — Duration match check:** If the uploaded video is 30s but the approved plan specified 15s deals, the economics change (different CPM → different impressions for the same budget). This triggers re-approval (return to Step 7 with the amended plan).

**Upload path:** `POST /api/assets/amz_assets/gen_upload_urls/` (get upload URLs) → `POST /api/assets/amz_assets/register/` (register the asset on Amazon)

REMOVED for CTV: browse existing assets (`GET /api/assets/`), pre-approved creatives (`GET /api/creatives/`), responsive e-commerce (`POST /api/creatives/recs/`), third-party tags (`POST /api/creatives/third-party/`). These are valid for Display but not for CTV scope.

> **REVIEW NOTE — the click-through URL is optional on streaming TV** (review comment on *"Required"* against Click-through URL: *"optional for streaming tv"*): A viewer holding a remote cannot click an ad, so requiring a landing page would block a trader on a field that has nothing to do on a television. The schema follows: `click_through_url: Optional[HttpUrl] = None`, still validated as a URL when one is supplied.
>
> **Recording why, so it does not get put back.** The call to action on CTV takes other forms — a QR code in the creative, a spoken or on-screen prompt to search for the brand, or simply brand recall. Measurement does not depend on the click either: it comes from the ASINs or the ad tag set up at the tracking step.
>
> **One refinement, following the device-type comment above.** Device types come from the advertiser and may include mobile, tablet or desktop — and on those screens the ad *can* be clicked. So "optional for streaming TV" is really two cases: with Connected TV alone there is nothing a URL could do, while with mobile or desktop in the mix a URL is worth having. The row above recommends it in that case rather than requiring it, which keeps the trader unblocked without quietly wasting the click-through.
>
> **OPEN QUESTIONS:**
>
> - Where the device types include mobile or desktop, should the agent actively ask for a URL, or leave it optional throughout and mention it once?
> - The staging API has a model named `MarketWithClickthroughUrl`. Is the click-through URL held **per market**? For a multi-market campaign that would matter — a German landing page is not the same as a British one — and this document currently treats it as a single value.
> - Are QR codes permitted in CTV creatives, and is there a spec for them? If that is the practical call to action, it is worth naming here rather than leaving traders to guess.

### Step 10: Platform Creative Approval

ENTIRELY NEW — did not exist in v1.1.0.

| Field | Type | Requirement | Source |
|---|---|---|---|
| Creative approval statuses | `dict[str, ApprovalStatusEnum]` | Read-only | API |

CHANGED — one entry per channel, keyed by the channels actually matched, replacing the three hard-coded rows. For example:

```json
{"Prime Video": "APPROVED", "Netflix": "PENDING", "Channel 4": "PENDING"}
```

Values per channel: PENDING → APPROVED or REJECTED

Every video must pass the platform's content and technical review before it can run. Each platform reviews its own inventory independently. A plan can be fully approved and funded and still not launch until the creative clears.

**On rejection:** the agent reports the reason and asks for a replacement (return to Step 9).

> **STILL OPEN, and it blocks more than this step:** do the per-channel review statuses surface inside VOW's API, or are they tracked externally? Nothing in the staging Swagger obviously carries a per-channel creative approval status. If these statuses are not readable, the dictionary above cannot be populated and the activation checklist cannot verify that every channel has approved — the agent can only check what it can read.

> **REVIEW NOTE — one status per channel, and the channel list is data** (review comment on the three hard-coded approval rows: *"It's just a single status for each channel not necessary netflix or disney - could be paramount or channel 4"*): The three rows become one field holding a status per channel, keyed by the channels the plan actually matched.
>
> **Why the shape matters more than the tidiness.** With a row per publisher, adding Paramount+ means changing the schema, migrating, touching the backend, the interface and the tests, and shipping a release — to add a name. As a dictionary it is a data change and nothing else. the choice of "Channel 4" is a deliberate one: it is a British broadcaster, so the list is market-specific as well as changeable — UK has ITVX and Channel 4, the US has Hulu and Peacock. Hard-coding would not merely be untidy; it would not scale past one market.
>
> **What stays fixed is the set of states.** `PENDING`, `APPROVED` and `REJECTED` are stable and the agent's logic depends on them, so those remain an enum. It is the **keys** that are data, not the values. Making everything dynamic would lose the type safety that matters.
>
> **The document already contained this rule, one section earlier.** The targeting step carries a design note that the targeting list changes often and so must be config-driven rather than hard-coded. Channels are the same kind of list. The rule was written down and then not applied here.
>
> **Naming.** The client's word is "channel". The deal schema called the same thing `provider`, and the inventory step now has a `Channel` field, which left three names for one concept. `SelectedDealSchema.provider` has been renamed to `channel`, along with the same field on `CurationRequirementsSchema` and inside `BudgetSplitSchema.by_inventory`.
>
> One caveat, since "provider" has not disappeared from this document: it still appears in the audience notes, where it means a **data** provider — Amazon 1P against a third party such as Experian. That is a different thing from a channel, and the two should not be collapsed. Channel is who shows the ad; data provider is whose audience data is being paid for.
>
> **OPEN QUESTIONS:**
>
> - Where should the channel list come from — `GET /api/admin/advertiser/get_channels_choices/`, or derived from the deals that were matched? The endpoint exists; deriving from matched deals gives only the channels in play, which may be what the interface actually needs.
> - Is the approval status held **per channel**, or per creative-and-channel pair? A plan with a 15s and a 30s creative could plausibly have one approved and the other not on the same channel.
> - Which other lists in this document should be config-driven rather than fixed in the schema? Genres, markets and device types all look like candidates, and `GET /api/strategies/choices/` may already serve some of them.

### Step 11: Tracking Setup

MOVED — ASIN validation was in Step 1 (strategy details) and ad-tag conversions were in Step 2 (goal/KPI). Both now sit here, after creative approval and before tracking is attached.

**What was in v1.1.0:**

ASINs collected in Step 1 and validated via `POST /api/contextual-targeting/{market}/asin-validation/`

Ad tag conversions selected in Step 2 via `GET /api/conversions/definitions/`

**What it is now:**

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Sells on Amazon? | Question | Asked here | MOVED from Step 1 |
| Product ASINs | Textarea | Required if endemic | Validation unchanged: `POST /api/contextual-targeting/{market}/asin-validation/` |
| Sells on own website? | Question | Asked here | NEW explicit question |
| Ad tag registered? | Check | Required if yes | NEW. Check whether an ad tag is already registered. If not, show setup instructions — the tag must be installed before the campaign runs (tracking only records activity after it goes live) |
| Ad tag conversions | Multi-select | Required if ad tag exists | MOVED from Step 2. Events: Page view, Add to cart, Checkout, Application. Via `GET /api/conversions/definitions/` |

**API calls at this step:** `POST /api/contextual-targeting/{market}/asin-validation/`, `GET /api/conversions/definitions/`

> **RESOLVED — was: the repeat of the Step 1 timing question, ending "Confirm with client".** `product_location` comes from the advertiser's settings, so the agent holds it at creation; the ASINs are sent empty and attached here through `PATCH /api/strategies/{id}/`. See the note on the ASIN row at Step 1.

> **REVIEW NOTE — a strategy can be updated after it is created** (review comment on *"Confirm with client"*: *"no they can be updated on the strategy after creation"*): The document treated creation as a point of no return, which is why the timing of the ASINs looked like a problem. It is not one. The strategy is created with what is known, and the rest is attached afterwards through `PATCH /api/strategies/{id}/` — confirmed present in the staging API, model `StrategyUpdate`.
>
> This closes the question that appeared twice in this document, at Step 1 and again here.
>
> **It is also what makes the previous comment work.** Removing the order from the creative, tracking and credit branches only makes sense if those branches can write back to a strategy that already exists. Had the strategy been fixed at creation, everything would have had to be collected beforehand and the sequence could not have been broken. So the two comments are one change seen from two sides: *no order necessary* is the behaviour, *updatable after creation* is the mechanism that permits it.
>
> **What should not be freely updatable.** The answer was about the measurement fields, and it should not be read as "anything may change". Some fields carry money:
>
> | Safely updatable | Needs a guardrail |
> |---|---|
> | `product_asins`, `product_location` | `market_budgets` — a guaranteed deal already owes the full budget |
> | Ad tag, conversions | `selected_deals` — the deal is booked |
> | Creatives | `flight_dates` — tied to the booking |
> | Targeting, frequency cap | `markets` — invalidates the whole plan |
>
> Without that distinction someone will PATCH a budget on a strategy whose Programmatic Guaranteed deal has already committed it, and the plan and the commitment will disagree.
>
> **OPEN QUESTIONS:**
>
> - **Which fields should be updatable after creation, and which fixed?** The table above is a proposal, not a confirmation. Budget and deals are the ones that matter.
> - Does "after creation" extend to **after activation**? A live campaign is a different case from one that has been created but not yet launched.
> - Does an update re-run anything — validation, or the reach forecast? If a PATCH changes the targeting, the forecast the trader was shown is no longer the forecast that applies, and the agent should say so.
> - Is `PATCH /api/strategies/{id}/` the right route for a strategy created through `simple-strategies`, given that `simple-strategies` itself is POST-only?

> **REVIEW NOTE — no order, and therefore a gate** (review comment on the *"Tracking Setup"* heading: *"could be done before creatives if they are no available yet - no order necessary"*): Tracking can be set up before the creative arrives. Which sounds like a small allowance, and is not.
>
> **The numbering implied a chain that does not exist.** If tracking, creatives and the credit check can happen in any order, they are not steps 9, 10, 11 and 12 — they are three branches that run independently after the strategy is created and meet at activation. The sequence up to creation is genuinely ordered: the inventory decides the CPM, the CPM decides the impressions, the forecast needs the targeting. After creation, none of the three waits on another.
>
> **This matches how the work actually arrives.** Creatives come from an agency and are often late. An ad tag has to be installed by the advertiser's own developers, which can take days. Credit is a finance matter. Forcing an order means one late item blocks everything, when the trader could have finished the rest.
>
> **Removing the order makes a completeness check necessary.** Something has to establish that everything is in place before money is spent, which is what the join node at Step 13 now does — see the prerequisite table and `ready_to_activate` there. The document already implied this without stating it: the creative-approval step notes that *"a plan can be fully approved and funded and still not launch until the creative clears."* That is a launch gate described in prose; it is now a checklist.
>
> **Step numbers are left as they are** so the review comments stay anchored. The parallelism is recorded here and in the state machine rather than by renumbering the document.
>
> **The checklist depends on something still unresolved.** "Approved by every channel" can only be checked if those per-channel statuses are readable through the API — the open question raised at the creative-approval step. If they are tracked outside VOW, that prerequisite cannot be evaluated and activation would either block indefinitely or have to trust the trader.
>
> **OPEN QUESTIONS:**
>
> - Is the prerequisite list complete, or is there something else that must be true before a campaign can go live?
> - Is the **credit check** genuinely order-free? Its outcome can change the budget, which would argue for running it before the plan is finalised rather than alongside the creative work.
> - Can conversions be **skipped** entirely — activating with no conversion tracking at all — or is at least one always required?
> - Is there an endpoint that reports activation readiness, or is the agent expected to assemble this from the individual checks?

### Step 12: Credit Check

ENTIRELY NEW — did not exist in v1.1.0.

Credit is checked only at activation, not during planning. Everything before this point is a costless plan.

| Field | Type | Requirement |
|---|---|---|
| Account balance | Number | Read-only |
| Strategy budget | Number | Read-only |
| Sufficient | Boolean | Derived (balance ≥ budget) |

If insufficient: prompt a top-up via `POST /api/credits/` or `POST /api/credits/stripe/`.

**API call:** `GET /api/credits/summary/`

### Step 13: Activate

ENTIRELY NEW — did not exist in v1.1.0 (was implicit in "create strategy").

The single spend action in the entire flow. Everything before this was free.

NEW — **a join node, not just a step.** Because the creative, tracking and credit branches run in any order, this is where completeness is checked. Nothing launches until every prerequisite holds:

| Prerequisite | Holds when |
|---|---|
| Creatives uploaded | One per duration in the plan — a 15s and a 30s plan needs both |
| Creatives approved | Every matched channel has returned `APPROVED` |
| Ad tag registered | The advertiser does not sell on Amazon and a tag is in place |
| ASINs attached | The advertiser does sell on Amazon and the ASINs validated |
| Conversions chosen | Selected, or explicitly skipped |
| Credit sufficient | Balance ≥ strategy budget |

```python
class ActivationPrerequisitesSchema(BaseModel):
    """NEW — checked at the join node before any spend."""
    creative_uploaded: dict[str, bool] # per duration: {"15": True, "30": False}
    creative_approved: dict[str, ApprovalStatusEnum] # per channel: {"Prime Video": APPROVED}
    ad_tag_registered: Optional[bool] = None # None when not applicable
    asins_attached: Optional[bool] = None # None when not applicable
    conversions_chosen: bool = False # True if chosen or deliberately skipped
    credit_sufficient: bool = False

    @property
    def ready_to_activate(self) -> bool:
        return (
            bool(self.creative_uploaded) and all(self.creative_uploaded.values())
            and bool(self.creative_approved)
            and all(s == ApprovalStatusEnum.APPROVED for s in self.creative_approved.values())
            and (self.ad_tag_registered is not False)
            and (self.asins_attached is not False)
            and self.conversions_chosen
            and self.credit_sufficient
        )
```

The agent should be able to answer "what is still outstanding?" at any point from this, rather than only discovering the gap at activation.

**API call:** `POST /api/strategies/{id}/set_status/`

After activation, VOW's outbound sync creates the Campaigns and Ad Groups on Amazon DSP.

---

## 4. API Catalogue

CHANGED — original catalogue kept, with additions and removals marked. Checked against the staging Swagger (`https://staging.vowmade.dev/api/openapi`) on 4 August 2026; rows marked *"NEW to this document"* exist in the API but were missing here.

| Operation | Method | Endpoint | Status |
|---|---|---|---|
| Check name uniqueness | GET | `/api/strategies/check_strategy_name_uniqueness/` | Unchanged |
| ASIN validation | POST | `/api/contextual-targeting/{market}/asin-validation/` | Unchanged |
| Product categories | GET | `/api/contextual-targeting/{market}/product-categories/` | Unchanged |
| Conversion definitions | GET | `/api/conversions/definitions/` | Unchanged |
| List deals | GET | `/api/deals/` | Unchanged |
| Deal filter properties | GET | `/api/deals/filter-properties/` | Unchanged |
| List audience sets | GET | `/api/audience-sets/` | Unchanged |
| Suggest audiences | POST | `/api/audience-sets/suggest/` | Unchanged |
| Audience reach forecast | POST | `/api/audience-sets/reach-forecast/` | Unchanged |
| Strategy reach forecast | POST | `/api/strategies/reach-forecast/` | Unchanged |
| List assets | GET | `/api/assets/` | Unchanged |
| List creatives | GET | `/api/creatives/` | Unchanged |
| Create strategy (general) | POST | `/api/strategies/` | Unchanged — not the CTV route |
| **Create strategy (CTV)** | POST | `/api/simple-strategies/` | **This is the one Step 8 uses.** POST only; model `SimpleStrategyCreate` |
| Update strategy after creation | PATCH | `/api/strategies/{id}/` | NEW to this document. Model `StrategyUpdate`. How ASINs are attached at the tracking step |
| Read strategy | GET | `/api/strategies/{id}/` | Unchanged |
| Advertiser settings | GET | `/api/admin/advertiser/{id}/` | NEW to this document. Model `AdvertiserAdminRetrieve`. Source of the advertiser defaults |
| Audience data fees | GET | `/api/contextual-targeting/fees` | NEW to this document. Model `Fee`. So the agent reads fee rates rather than assuming them |
| Postcode validation | POST | `/api/strategies/postcode-validation/{market}/` | NEW to this document. Confirms postcode-level geo targeting is available |
| Targeting recommendation | POST | `/api/strategies/{id}/targeting/auto-rec/` | NEW to this document. Model `StrategyTargetAutoREC`. May already produce the default baseline |
| Audience overlap | POST | `/api/audiences/{market}/overlapping-audiences/` | NEW to this document. Detects the cross-provider case where both data fees apply |
| Channel choices | GET | `/api/admin/advertiser/get_channels_choices/` | NEW to this document. Where the channel list comes from rather than hard-coding it |
| Strategy choices | GET | `/api/strategies/choices/` | NEW to this document. Model `StrategyChoiceList`. Config-driven lists including formats and KPIs |
| Brand lookup by domain | GET | `/api/brand/get_brand_by_domain/` | NEW to this document. Could resolve the brand from a website named in the brief |
| Ad tag events | GET | `/api/ad-tags/{market}/ad-tag-events/` | NEW to this document. Used at the tracking step |
| Set creative durations | POST | `/api/strategies/{id}/creatives/set_durations/` | NEW to this document. Supports the duration match check |
| Automated strategy create | POST | `/api/automated-strategies/` | Exists in the API; purpose unclear. See the question at Step 8 |
| ~~Deal matching~~ | ~~POST~~ | ~~`/api/rate-cards/match/`~~ | **Does not exist.** Matching uses `/api/deals/` with `/api/deals/filter-properties/` |
| CTV rate card | GET | `/api/rates/ctv/{market}/` | NEW |
| Inventory sources | GET | `/api/inventory-sources/` | NEW |
| Activate strategy | POST | `/api/strategies/{id}/set_status/` | NEW |
| Credit summary | GET | `/api/credits/summary/` | NEW |
| Upload URLs | POST | `/api/assets/amz_assets/gen_upload_urls/` | NEW |
| Register asset | POST | `/api/assets/amz_assets/register/` | NEW |
| Locations | GET | `/api/strategies/locations/{market}/` | NEW |
| Draft create | POST | `/api/strategies/draft/` | REMOVED — client: "draft is just for the wizard" |

---

## 5. Pydantic Data Models

CHANGED — original models kept where valid, extended and restructured.

```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


# ==========================================
# ENUMS
# ==========================================

class ChannelTypeEnum(str, Enum):
    """UNCHANGED"""
    DSP = "dsp"
    SPONSORED = "sponsored"

class GoalEnum(str, Enum):
    """CHANGED — kept all values, but for CTV M1 only AWARENESS is used"""
    AWARENESS = "AWARENESS"
    CONSIDERATION = "CONSIDERATION" # future scope
    CONVERSION = "CONVERSION" # future scope

class KPIEnum(str, Enum):
    """CHANGED — kept all values, but for CTV M1 only reach and frequency"""
    REACH = "reach"
    FREQUENCY = "frequency"
    CTR = "ctr" # future scope
    CPC = "cpc" # future scope
    CPA = "cpa" # future scope
    CPDPV = "cpdpv" # future scope

class ProductLocationEnum(str, Enum):
    """UNCHANGED"""
    ON_AMAZON = "ON_AMAZON"
    NOT_SOLD_ON_AMAZON = "NOT_SOLD_ON_AMAZON"

class FormatEnum(str, Enum):
    """CHANGED — for CTV the format is always streaming_tv"""
    DISPLAY = "display" # future scope
    ONLINE_VIDEO = "online_video" # future scope
    STREAMING_TV = "streaming_tv" # the only value used for CTV
    PRIME_VIDEO = "prime_video" # not a format — a provider; see SelectedDealSchema.provider

class CurrencyEnum(str, Enum):
    """UNCHANGED"""
    EUR = "EUR"
    GBP = "GBP"
    USD = "USD"

# NEW ENUMS

class DurationEnum(str, Enum):
    """NEW — creative durations for CTV"""
    TEN = "10"
    FIFTEEN = "15"
    TWENTY = "20"
    THIRTY = "30"

class InventoryTierEnum(str, Enum):
    """NEW — the three inventory tiers driving the flow's primary fork"""
    AMAZON_OWNED = "AMAZON_OWNED"
    THIRD_PARTY_PRECURATED = "THIRD_PARTY_PRECURATED"
    THIRD_PARTY_NEEDS_CURATION = "THIRD_PARTY_NEEDS_CURATION"

class ApprovalStatusEnum(str, Enum):
    """NEW — creative approval only; the plan uses PlanStatusEnum"""
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class PlanStatusEnum(str, Enum):
    """NEW — the plan is finalised by the trader, not approved by a manager.
    Kept extensible: the review said "no manager approval required for now"."""
    DRAFT = "DRAFT"
    FINALISED = "FINALISED"

class BudgetSplitMethodEnum(str, Enum):
    """NEW — how the budget is divided"""
    EVEN_BY_BUDGET = "EVEN_BY_BUDGET"
    EVEN_BY_IMPRESSIONS = "EVEN_BY_IMPRESSIONS"
    CUSTOM = "CUSTOM"

class AudienceProfileEnum(str, Enum):
    """NEW — the three audience options"""
    NARROW = "NARROW"
    BALANCED = "BALANCED"
    WIDE = "WIDE"


# ==========================================
# COMPONENT SCHEMAS
# ==========================================

class DateRangeSchema(BaseModel):
    """UNCHANGED"""
    lower: str = Field(..., description="ISO date YYYY-MM-DD")
    upper: str = Field(..., description="ISO date YYYY-MM-DD")
    bounds: str = Field("[)", description="Interval boundary notation")

class MarketBudgetBidSchema(BaseModel):
    """UNCHANGED"""
    market: str = Field(..., description="ISO country code")
    budget: str = Field(..., description="Total budget decimal string")
    base_bid: str = Field(..., description="Base CPM bid decimal string")

class SelectedDealSchema(BaseModel):
    """CHANGED — added inventory_tier, genre, ad_lengths, channel"""
    deal_id: str = Field(..., description="External deal ID e.g. EXT7P75718S8MNR")
    name: str = Field(..., description="Deal name")
    cpm: str = Field(..., description="Fixed or floor CPM price")
    inventory_tier: InventoryTierEnum = Field(..., description="Which tier this deal belongs to") # NEW
    channel: str = Field(..., description="e.g. Prime Video, Netflix, Disney+, Paramount+, Channel 4") # was `provider` — "channel" is the client's word
    genre: Optional[str] = Field(None, description="Genre if genre-specific deal") # NEW
    ad_lengths: list[str] = Field(default_factory=list, description="Supported durations") # NEW
    deal_type: str = Field(..., description="PG, Preferred, or Private Auction") # NEW

class SelectedAudienceSetSchema(BaseModel):
    """CHANGED — added profile and effective_cpm"""
    audience_set_id: str = Field(..., description="Audience set UUID")
    name: str = Field(..., description="Audience set name")
    vcpm_fee: str = Field(..., description="VCPM fee decimal")
    profile: AudienceProfileEnum = Field(..., description="Narrow, Balanced, or Wide") # NEW
    effective_cpm: Optional[str] = Field(None, description="Deal CPM + audience VCPM") # NEW
    estimated_reach: Optional[int] = Field(None, description="If Amazon inventory") # NEW

class SelectedCreativeSchema(BaseModel):
    """CHANGED — added duration_seconds for the match check"""
    asset_id: str = Field(..., description="Registered asset ID")
    click_through_url: Optional[HttpUrl] = Field(
        None, description="Landing page URL — optional for CTV; nothing on a TV screen is clickable"
    ) # CHANGED from required
    duration_seconds: int = Field(..., description="Video length in seconds") # NEW
    upload_method: str = Field("direct", description="direct or url") # NEW

# NEW SCHEMAS

class BudgetSplitSchema(BaseModel):
    """NEW — how budget is divided across inventories and durations"""
    method: BudgetSplitMethodEnum = Field(..., description="Even by budget, even by impressions, or custom")
    by_inventory: list[dict] = Field(..., description="[{channel, budget, impressions_estimate}]")
    by_duration: list[dict] = Field(..., description="[{duration, budget, cpm, impressions_estimate}]")

class CurationRequirementsSchema(BaseModel):
    """NEW — captured for 3P-needs-curation inventory (e.g. Disney+)"""
    channel: str = Field(..., description="e.g. Disney+") # was `provider`
    genres: list[str] = Field(default_factory=list)
    durations: list[str] = Field(default_factory=list)
    targeting_preferences: Optional[str] = None
    budget: str = Field(..., description="Allocated budget for this channel")
    flight_dates: DateRangeSchema = Field(...)

class TargetingSchema(BaseModel):
    """NEW — CTV targeting options (config-driven, extensible)"""
    locations: list[str] = Field(default_factory=list)
    instream_positions: list[str] = Field(default_factory=list)
    content_category_exclusions: list[str] = Field(default_factory=list)
    device_types: list[str] = Field(default_factory=list)
    mobile_environments: list[str] = Field(default_factory=list)

class ForecastResultSchema(BaseModel):
    """CHANGED — added availability flag for the honesty rule"""
    is_available: bool = Field(..., description="False for Netflix/Disney — no reach data") # NEW
    estimated_impressions: Optional[int] = None
    estimated_unique_reach: Optional[int] = Field(None, description="Only for Amazon inventory")
    average_frequency: Optional[float] = Field(None, description="Only for Amazon inventory")
    indicative_cpm: Optional[str] = None
    reach_curve: Optional[list[dict]] = Field(None, description="[{budget, reach}] — Amazon only")

class TrackingSetupSchema(BaseModel):
    """NEW — tracking prerequisites collected at Step 11"""
    sells_on_amazon: bool = Field(...)
    validated_asins: list[dict] = Field(default_factory=list, description="[{asin, title, brand}]")
    sells_on_own_site: bool = Field(...)
    ad_tag_registered: Optional[bool] = None
    ad_tag_conversions: list[str] = Field(default_factory=list, description="Selected conversion events")


# ==========================================
# FULL STRATEGY SCHEMA
# ==========================================

class FullStrategySchema(BaseModel):
    """CHANGED — restructured from wizard steps to semantic grouping"""

    # --- Identity ---
    id: Optional[str] = Field(None, description="System-assigned strategy ID")
    advertiser_id: str = Field(..., description="Parent advertiser UUID")
    channel_type: ChannelTypeEnum = ChannelTypeEnum.DSP

    # --- Basics (Step 1) ---
    name: str = Field(..., description="Unique strategy name")
    flight_dates: DateRangeSchema = Field(...)
    markets: list[str] = Field(..., description="ISO country codes")
    primary_currency: CurrencyEnum = Field(CurrencyEnum.GBP)
    durations: list[DurationEnum] = Field(..., description="Creative durations") # NEW
    formats: list[FormatEnum] = Field(...)
    goal: GoalEnum = Field(GoalEnum.AWARENESS, description="Fixed for CTV") # CHANGED default
    kpi_target_type: KPIEnum = Field(...)
    product_categories: list[int] = Field(default_factory=list)
    product_location: ProductLocationEnum = Field(...)
    market_budgets: list[MarketBudgetBidSchema] = Field(...)
    frequency_cap: Optional[int] = Field(None, description="Optional weekly cap") # NEW
    budget_cap: Optional[str] = Field(None, description="Optional budget cap") # NEW

    # --- Inventory (Step 2) ---
    selected_deals: list[SelectedDealSchema] = Field(...) # CHANGED — enriched schema
    curation_requirements: list[CurationRequirementsSchema] = Field(default_factory=list) # NEW

    # --- Budget Split (Step 3) ---
    budget_split: Optional[BudgetSplitSchema] = None # NEW

    # --- Audiences (Step 4) ---
    audience_options: list[SelectedAudienceSetSchema] = Field(default_factory=list) # CHANGED — now carries all three
    chosen_audience_profile: Optional[AudienceProfileEnum] = None # NEW
    matching_mode: str = Field("Exact", description="Similar or Exact") # UNCHANGED

    # --- Targeting (Step 5) ---
    targeting: Optional[TargetingSchema] = None # NEW

    # --- Forecast (Step 6) ---
    forecast: Optional[ForecastResultSchema] = None # CHANGED — enriched with availability

    # --- Finalisation (Step 7) ---
    plan_status: Optional[PlanStatusEnum] = None # was approval_status
    finalised_by: Optional[str] = None # was approved_by
    finalised_at: Optional[str] = None # was approved_at

    # --- Creative (Step 9) ---
    selected_creatives: list[SelectedCreativeSchema] = Field(default_factory=list) # CHANGED — enriched
    creative_duration_match: Optional[bool] = None # NEW
    creative_approval_statuses: dict[str, ApprovalStatusEnum] = Field(
        default_factory=dict,
        description="One entry per matched channel — keys are data, not schema",
    ) # was a single creative_approval_status

    # --- Tracking (Step 11) ---
    tracking: Optional[TrackingSetupSchema] = None # NEW
    product_asins: list[str] = Field(default_factory=list) # MOVED from Step 1

    # --- Activation (Steps 12-13) ---
    credit_sufficient: Optional[bool] = None # NEW
    status: str = Field("created", description="Strategy status") # CHANGED from "draft"
    is_syncing: bool = Field(False)


# ==========================================
# LANGGRAPH PLANNING STATE
# ==========================================

# CHANGED — restructured from wizard-step-based to semantic field names

# WAS (v1.1.0):
# class PlanningAgentState(TypedDict):
# messages: List[Dict[str, Any]]
# advertiser_id: str
# current_step: int # 0 to 5
# strategy_id: Optional[str]
# step1_details: Optional[Dict[str, Any]]
# step2_goal_kpi_bid: Optional[Dict[str, Any]]
# step3_deals: Optional[Dict[str, Any]]
# step4_audiences: Optional[Dict[str, Any]]
# step5_creatives: Optional[Dict[str, Any]]
# forecast_results: Optional[Dict[str, Any]]
# validation_errors: List[str]
# is_complete: bool

# NOW:
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class PlanningAgentState(TypedDict):
    """State carried through the LangGraph planning flow.

    Named semantically, not by wizard step — the state describes
    the plan, not the UI that collected it.
    """
    # --- Conversation ---
    messages: Annotated[list, add_messages]

    # --- Session context ---
    advertiser_id: str
    session_id: str
    current_stage: str # NEW — for the adaptive canvas
    current_artifact_id: Optional[str] # NEW — for the adaptive canvas

    # --- Basics ---
    strategy_name: Optional[str]
    flight_dates: Optional[dict]
    markets: list[str]
    durations: list[str] # NEW
    primary_currency: str
    goal: str # fixed: AWARENESS for CTV
    kpi: str # reach or frequency
    market_budgets: list[dict]
    product_location: Optional[str]
    frequency_cap: Optional[int] # NEW
    budget_cap: Optional[str] # NEW

    # --- Inventory ---
    inventory_tier: Optional[str] # NEW — which tier fork we're on
    selected_deals: list[dict]
    curation_requirements: list[dict] # NEW

    # --- Budget split ---
    budget_split: Optional[dict] # NEW

    # --- Audiences ---
    audience_options: list[dict] # the three profiles
    chosen_audience: Optional[dict] # which one the trader picked

    # --- Targeting ---
    targeting: Optional[dict] # NEW

    # --- Forecast ---
    forecast: Optional[dict] # reach/impressions/CPM (with availability flag)

    # --- Finalisation ---
    plan_status: Optional[str] # DRAFT/FINALISED — was approval_status
    finalised_by: Optional[str] # was approved_by
    finalised_at: Optional[str] # was approved_at

    # --- Creative ---
    creative_id: Optional[str]
    creative_duration_match: Optional[bool] # NEW
    creative_approval_status: Optional[str] # NEW

    # --- Tracking ---
    tracking_setup: Optional[dict] # NEW
    product_asins: list[str] # MOVED

    # --- Activation ---
    credit_sufficient: Optional[bool] # NEW
    strategy_id: Optional[str]
    strategy_status: Optional[str]

    # --- Errors ---
    validation_errors: list[str]
```

---

## 6. State Machine

CHANGED — needs complete rebuild. The original was a linear pipe. The confirmed flow has branches, loops, and interrupts.

The confirmed state machine (v5):

```
START
  → extract_fields (slot-filling from brief)
  → match_inventory_deals (CTV, three-tier fork — matched, not selected)
    → [if 3P needs curation] capture_curation_requirements
  → propose_budget_split (across inventories + durations)
  → suggest_audiences (3 options via pgvector; optional — may be declined)
  → apply_targeting (optional, configurable)
  → predict_reach
    → [if Amazon] real forecast + reach curve
    → [if 3P] CPM + derived impressions only (honest)
    → [if too narrow] REPAIR: extend audience → re-predict (loop)
  → present_plan (on the strategy card)
  → finalise_plan (status DRAFT → FINALISED — no interrupt, no manager)
  → create_strategy (POST /simple-strategies/ — the real one, not draft)

  ── from here the three branches run in any order, none waits on another ──

  ├── BRANCH A upload_creative (video, gen_upload_urls + register)
  │ → [if duration mismatch] amend plan → re-finalise (loop back)
  │ platform_creative_approval (per matched channel)
  │ → interrupt — waiting on the platform's review, not on a colleague
  │ → [if rejected] return to upload_creative
  │
  ├── BRANCH B tracking_setup (ASINs + ad tag check)
  │ → PATCH /strategies/{id}/ to attach the ASINs
  │
  └── BRANCH C credit_check (GET /credits/summary/)
                 → [if insufficient] prompt top-up (loop)

  → activate — join node. Checks ready_to_activate across all three
                  branches, then POST /strategies/{id}/set_status/
                  (the single spend action)
  → DONE
```

**Q&A side path:** at any point, the trader can ask a pricing/availability question ("what's the CPM for Netflix 30s?"). The agent answers from the rate card and resumes.

---

## 7. Brief Parsing & Edge Cases

### 7.1 Entity Normalisation

UNCHANGED — the original examples are correct. Additions:

| Input | Extraction | Status |
|---|---|---|
| August 2026 | `flight_dates: {lower: "2026-08-01", upper: "2026-08-31"}` | Original |
| UK | `markets: ["GB"], primary_currency: "GBP"` | Original |
| £10,000 | `market_budgets: [{market: "GB", budget: "10000.00"}]` | Original |
| education website | `product_location: "NOT_SOLD_ON_AMAZON"` | Original |
| 30 seconds | `durations: ["30"]` | NEW |
| UK and France | `markets: ["GB", "FR"]` | NEW |
| sports drink | Consider genre-specific deals (Sports) | NEW |
| Prime and Netflix | Multiple inventory tiers | NEW |

### 7.2 Validation Failure Protocols

UNCHANGED — duplicate name, invalid ASIN, past dates protocols all correct.

### 7.3 Repair Loop

CHANGED — concept correct, mechanism updated (see Step 6 above). Only applies to Amazon-owned inventory.

**NEW — "Did I understand correctly?" confirmation.** After extracting fields from a brief, the agent immediately shows what it understood so the trader can correct before proceeding. This is the single most important trust mechanism in the product.

---

## 8. Summary of all changes

| Category | Count | Items |
|---|---|---|
| Unchanged | ~15 | Core principles, product attribution, deal types, date validation, name uniqueness, currency, most API endpoints, brief parsing examples |
| Changed | ~12 | Step order, goal scoped to Awareness, KPI scoped to reach/frequency, deals enriched with tier, audiences suggestion-driven + renamed Wide, forecast with availability flag, state restructured, creative simplified to video |
| New | ~15 | Durations, inventory tiers, budget split, targeting, plan approval, creative duration check, platform creative approval, tracking setup (moved), credit check, activation, curation capture, effective CPM, adaptive-canvas fields |
| Removed | ~5 | Draft endpoint, product audiences, non-CTV formats (scoped out), non-awareness KPIs (scoped out), canary-check |

---

This document is for client verification. Once confirmed, it becomes the shared contract that the agent, registry and interface teams build against.
