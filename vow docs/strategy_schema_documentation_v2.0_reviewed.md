# Strategy Schema documentation v2.0

## VOW Platform — Strategy Schema (Revised v2.0)
### Aligned to the confirmed CTV-first agentic flow (v5)

**Original version:** 1.1.0 by Kareem
**This revision:** 2.0.0 — reordered, scoped to CTV, and extended with client-confirmed corrections
**Review status:** ✅ **Review complete — all 28 comments addressed** *(see Review Status below)*
**Status:** For client verification

---

## 🔵 Review Status

David Moss reviewed v2.0 and raised **28 comments**. **All 28 are incorporated**, each answered inline as a **📋 Review Note** placed directly under the section it applies to.

| # | Section | Comment | Outcome |
|---|---|---|---|
| 1 | §2.3 Inventory tiers | *"For 3P there's often a choice whether to use Amazon's targeting…"* | 🔄 Corrected — targeting is a **choice**, and it is **deal-bound** |
| 2 | §2.4 Audience profiles | *"there's not necessarily a fee consequence…"* | 🔄 Corrected — fee depends on **data source**, not profile; no compounding |
| 3 | Step 3 Budget split | *"is optional but to give an accurate CPM is preferred"* | 🔄 **Optional**, not Required |
| 4 | Step 4 Audiences | *"optional again"* | 🔄 **Optional**, not mandatory |
| 5 | Step 5 Targeting | *"I would treat audiences as part of targeting…"* | 🔄 **Steps 4 + 5 merge**; default-then-refine |
| 6 | Step 1 field list | *"a lot of this is for a non CTV strategy — can simplify and imply answers"* | 🔄 Step 1 rebuilt; **Source** column added |
| 7 | Step 1 Strategy name | *"could be auto generated from brief"* | 🔄 Source = **Generated** |
| 8 | Step 1 Target markets | *"Are we going to support multi market?…"* | ⚠ **Scope decision required** |
| 9 | Step 1 Primary currency | *"just use market currency if single market"* | 🔄 Source = **Derived** |
| 10 | Step 1 KPI | *"if frequency then you can have kpi target too of 1-5"* | ➕ **Missing field added** |
| 11 | Step 1 Market budgets | *"single market budget?"* | 🔄 Type column split; single figure in M1 |
| 12 | Step 1 Base bids | *"not required for CTV as defined by CPM of deals"* | ❌ **Removed** — and repair loop rewritten |
| 13 | Step 1 Frequency cap | *"we have a default per advertiser"* | ➕ **Advertiser defaults added** (new concept) |
| 14 | Step 1 Formats | *"is always streaming_tv"* | 🔄 Constant, not a choice |
| 15 | Step 1 Product categories | *"we have a default on the advertiser, or imply from the brief"* | 🔄 Source = **Advertiser → brief → API** |
| 16 | Step 1 Selling location | *"can leave out"* | ❌ **Removed** from Step 1 |
| 17 | Step 1 Product ASINs | *"comes later"* | ❌ Removed from Step 1 — ✅ **resolves Open Question 1** |
| 18 | Step 2 Selected deals | *"remove the technical need to select deals from a table"* | 🔄 **Agent matches deals**; only CPM surfaced |
| 19 | Targeting constraints | *"can use amazon audiences too"* | 🔄 Amazon audiences **do apply to 3P** — corrects Note 1 |
| 20 | Targeting open question | *"not currently supported"* | ✅ **Resolves Open Question 2** — profiles are agent-built |
| 21 | Targeting Location | *"defaults to market country"* | 🔄 Source = **Derived** |
| 22 | Targeting Device type | *"Some advertisers only want CTV only — set at advertiser level"* | 🔄 Source = **Advertiser** · corrects Note 21 · **format ≠ device** |
| 23 | Plan Approval (step) | *"we simplified this so it's just a status changed… no manager approval required for now"* | 🔵 **Design change, not a correction** — step becomes **Finalise Plan**; `interrupt()` no longer needed here |
| 24 | Create step → API call | *"probably more likely simple-strategies endpoint"* | ⚠ **Hint to verify** — points at a whole **CTV endpoint family** |
| 25 | Creative → Click-through URL | *"optional for streaming tv"* | ✅ **Closes a gap this revision flagged** — Required → Optional |
| 26 | Platform approval → status table | *"just a single status for each channel… could be paramount or channel 4"* | ✅ **Confirms the proposed `dict` fix** · channel list is **open** · settles the naming question |
| 27 | Tracking Setup (step) | *"could be done before creatives if they are no available yet — no order necessary"* | 🔴🔴 **The tail of the flow becomes parallel branches**, not a chain |
| 28 | Tracking Setup → the ⚠ open question | *"no they can be updated on the strategy after creation"* | ✅ **Resolves the most-repeated open question** — and confirms the capability Note 27 depends on |

### What the review changed, in summary

Three themes account for almost all 18 comments:

1. **The document over-constrained.** Several fields were marked Required or Mandatory that are actually optional — and in two cases the schema was already correct while the field table was not.
2. **The document asked where it should infer.** Most Step 1 fields can be inferred from the brief, derived from another field, taken from advertiser defaults, generated, or are simply constant for CTV. After the review, **no Step 1 field is both asked and required.**
3. **Three steps had the wrong interaction model.** Step 1 is a summary to confirm, not a form to fill. Step 2 matches deals rather than presenting a table. Steps 4 and 5 are one step with a sensible default.

Three genuine gaps were also found: **advertiser-level defaults** did not exist anywhere in the document, the **repair loop** depended on levers that do not work for CTV, and **several API examples in §4.2 were assumptions rather than verified contracts** — one of which is now confirmed wrong.

**One comment is not a correction at all.** Comment 23 reports that the team has **simplified plan approval** since v2.0 was written — the document was not wrong, it had gone out of date. That distinction is worth keeping visible: this document describes decisions that are still moving, so sections should be read as *"last confirmed"* rather than *"final."*

### Corrections to this revision itself

Three conclusions in earlier review notes turned out to be wrong, and are corrected in place rather than quietly amended:

| Where | What was wrong | Corrected by |
|---|---|---|
| **Review Note 1** — the explanation for why Amazon's targeting is limited on 3P inventory | It asserted that 3P publishers pass no viewer identity, so Amazon *cannot* apply audience segments. **Over-claimed** — Amazon audiences do work on 3P inventory | **Note 19** |
| **Review Note 21** — the targeting default table | It listed **Device type** as `🔒 FIXED — CTV module`, assuming a CTV module implies Connected TV delivery. It is an **advertiser-level value** that varies by advertiser | **Note 22** |
| **Review Note 17** — the *evidence*, not the conclusion | It cited `"product_asins": []` in §4.2's create payload as proof that creating without ASINs works. That example is for `POST /api/strategies/`; the CTV path likely uses a different endpoint, so the evidence does not carry. **The conclusion still stands** — it came from David's comments | **Note 24** |
| **Open Question 1** — the recommended resolution | This revision leaned toward keeping ASINs in Step 1 (Option B). David answered the other way | **Notes 16 and 17** |

### Two things this revision flagged that David has now confirmed

| Where | What was flagged | Confirmed by |
|---|---|---|
| **Upload Creative** | *"Click-through URL is Required, unexplained… either Amazon DSP mandates it even for CTV, **or it should be Optional for CTV**"* | **Note 25** — optional |
| **Platform Creative Approval** | The schema held one approval status where the step needed several; a **dictionary keyed by channel** was proposed | **Note 26** — one status per channel |
| **Upload Creative** | *"Multiple durations, partial upload is not covered"* | **Note 27** — closed by the per-duration `creative_uploaded` map |

### And the ⚠ markers did their job

v2.0 carried **five** ⚠ open questions. David commented directly on **two** of them — the `bundles` response shape (Note 20) and the ASIN timing conflict (Note 28) — and **both were blocking.** Had either been assumed rather than flagged, the audience module would have been built against a response shape that does not exist, and the ASIN handling would have gone in the wrong direction.

| # | v2.0 open question | Status |
|---|---|---|
| 1 | ASIN and `product_location` timing | ✅ **Resolved** — Notes 16, 17, 28 |
| 2 | Suggest endpoint response shape | ✅ **Resolved** — Note 20 |
| 3 | What status does a created strategy land in? | ⬜ Open *(Note 28 helps: "created" means mutable and not spending)* |
| 4 | Do channel creative review statuses surface in VOW's API? | ⬜ Open |
| 5 | What is the simplified CTV forecast endpoint called? | ⬜ Open — Note 24 widened it |

---

## How to read this document

Every section carries a change marker relative to v1.1.0:

| Marker | Meaning |
|---|---|
| ✅ **UNCHANGED** | Kept exactly as Kareem wrote it |
| 🔄 **CHANGED** | The concept existed but is modified (original shown for comparison) |
| ➕ **NEW** | Did not exist in v1.1.0, added from client feedback |
| ❌ **REMOVED** | Existed in v1.1.0 but dropped for CTV scope (kept as future scope) |

Review notes carry their own marker:

| Marker | Meaning |
|---|---|
| 📋 **REVIEW NOTE** | A correction or clarification arising from David's review, with the reasoning and the resulting schema/flow change |
| ⚠ **OPEN QUESTION** | Still unresolved — needs a decision from David or the client |
| ✅ **RESOLVED** | An open question that the review has now answered |

The document follows the confirmed agentic flow order, not the existing wizard order.

---

# 1. Core Principles

✅ **UNCHANGED** — all three kept exactly as written.

1. **Zero-Hallucination Policy** — The agent NEVER invents strategy parameters, metrics, targeting criteria, or deal IDs. It only populates values verified against the VOW database and REST APIs.
2. **Self-Filling Form Paradigm** — The agent operates as a stateful slot-filling engine backed by LangGraph. Inputs via chat or uploaded briefs are parsed into registered Pydantic slot schemas.
3. **API-Driven Tool Execution** — Every step maps to official VOW API endpoints.

> ### 📋 REVIEW NOTE — Principle 2 is the standard the rest of the document is measured against
>
> Several of David's comments (#5, #6, #7, #9, #13, #15, #18) reduce to the same observation: **the document did not follow its own second principle.** A "form that fills itself in" cannot present fourteen required fields and a deal table for the trader to work through.
>
> The corrections in this revision — the `Source` column in every field matrix, default-then-refine targeting, and agent-side deal matching — are what Principle 2 looks like when applied consistently. The principle itself needed no change; the steps did.

---

# 2. Business Logic

## 2.1 Product Attribution & Selling Locations

✅ **UNCHANGED**

- **On Amazon (`ON_AMAZON`) [Endemic]:** ASINs required. Enables DPV, ATC, Purchase, ROAS tracking.
- **Off Amazon (`NOT_SOLD_ON_AMAZON`) [Non-Endemic]:** ASINs optional (monitors halo sales). Ad tag conversions required for site event tracking.

> ### 📋 REVIEW NOTE — Selling location is an advertiser attribute, collected at Step 11
>
> Per David's comment on Step 1, the selling-location question **leaves Step 1** — see the Step 1 review notes. The business logic above is unchanged; only where the value comes from has changed.
>
> Whether an advertiser sells on Amazon is largely a **property of the advertiser, not of the campaign** — it does not vary campaign to campaign. It should therefore come from the advertiser record as a default (overridable), with confirmation happening at Step 11 alongside ASINs and the ad-tag check.

## 2.2 Attribution Window

✅ **UNCHANGED** — 14-day post-view and post-click.

> ### ⚠ OPEN QUESTION — Is the attribution window configurable?
>
> The document states 14 days as the default but has no field for it. If a trader or advertiser can change it, an `attribution_window_days` field is needed; if it is fixed for M1, the document should say so explicitly. **To confirm.**

## 2.3 Deal Types

🔄 **CHANGED** — deal types unchanged, but inventory tiers added.

### Original deal types (kept)

| Type | Price | Commitment | Can pause? |
|---|---|---|---|
| **Programmatic Guaranteed (PG)** | Fixed CPM, guaranteed volume | **Full budget owed** | ❌ No |
| **Preferred Deals** | Fixed CPM | None | ✅ Yes |
| **Private Auctions** | Floor CPM, competitive | None | ✅ Yes |

### ➕ NEW — Three inventory tiers (the primary fork in the CTV flow)

Every deal now carries an inventory tier. This classification drives most of the downstream branching — whether reach can be forecast, whether Amazon audiences apply, and whether the deal is selectable now.

| Tier | Examples | Deals | Reach forecast | Audiences / Targeting |
|---|---|---|---|---|
| **Amazon owned** | Prime Video | Pre-curated, selectable now | ✅ Available | Amazon audiences |
| **3P pre-curated** | Netflix, Hulu, others | Pre-curated, selectable now | ❌ Not available | **Amazon audiences** *(may be limited)* **or SSP-side** — a choice. See Notes 1 and 19 |
| **3P needs curation** | Disney+, others | Rate-card CPM only; VOW curates the deal after the IO is signed | ❌ Not available | Same choice — specified at curation. See Notes 1 and 19 |

> **What actually differentiates the tiers.** After Review Note 19, the Audiences column is **no longer a differentiator** — Amazon audiences apply across all three tiers. The two real differences are:
>
> | | Reach forecast | Deal availability |
> |---|---|---|
> | **Amazon owned** | ✅ Available | Selectable now |
> | **3P pre-curated** | ❌ Not available | Selectable now |
> | **3P needs curation** | ❌ Not available | Must be curated after the IO is signed |

**Why this matters:** a plan spanning Prime + Netflix + Disney has three portions, each with different capabilities. The agent must handle them differently — and be honest about what it can and cannot forecast.

> ### 📋 REVIEW NOTE 1 — Targeting for 3P inventory is a choice, and it is bound to the deal
>
> **David's comment:** *"For 3P there's often a choice whether to use Amazon's targeting (may be limited in functionality i.e. only device) or to apply the targeting at the inventory source / SSP. Which is then specific to the deal that is chosen or curated."*
>
> The table previously read *"Their own targeting (adds CPM)"* for both 3P tiers. That was **incomplete** — it presented one option where there are two, and it is the trader's choice.
>
> | | **Option A — Amazon's targeting** | **Option B — Inventory source / SSP targeting** |
> |---|---|---|
> | Applied at | Amazon DSP side | The publisher's own SSP |
> | Capability | ⚠ **May be limited** by deal/provider | Fuller, publisher-specific |
> | Includes Amazon audiences? | ✅ **Yes** *(see Note 19)* | — |
> | Cost | **Amazon 1P data fee applies** *(see Note 19)* | **Adds CPM** |
> | When chosen | Can be applied in the Targeting step | 🔴 **Bound to the deal** — determined at deal selection (3P pre-curated) or specified during curation (3P needs curation) |
>
> > **⚠ CORRECTION to this note, from Review Note 19.** An earlier version of this note explained the limitation by asserting that 3P publishers pass no viewer identity, so Amazon *cannot* apply audience segments — only device-level targeting. **That over-claimed.** David's wording was *"may be limited"*, and Note 19 confirms **Amazon audiences do work on 3P inventory.** The constraint is a matter of degree, set by the deal and provider, not a technical barrier. The specific mechanism is Amazon's and is not documented here.
>
> **Flow consequence.** For the 3P portion, targeting is **not** a free-standing Targeting-step decision — it is coupled to inventory selection. Either the chosen deal already carries its targeting, or the targeting preference must be captured as part of the curation request. The Targeting step's fields therefore apply in full only to the **Amazon-owned portion**.
>
> **Agent behaviour required.** When 3P inventory is selected, the agent must surface the choice with its trade-off — e.g. *"For the Netflix portion you can either use Amazon's targeting (device-level only) or Netflix's own targeting, which is richer but adds to the CPM. Which do you prefer?"*
>
> **Schema additions:**
> ```python
> class TargetingSourceEnum(str, Enum):
>     """➕ NEW — where targeting is applied (per review)"""
>     AMAZON_DSP = "AMAZON_DSP"              # limited on 3P (e.g. device only)
>     INVENTORY_SOURCE = "INVENTORY_SOURCE"  # SSP-side; deal-bound; adds CPM
>
> # SelectedDealSchema
> targeting_source: Optional[TargetingSourceEnum] = Field(
>     None, description="Where targeting is applied for this deal")
> source_targeting_cpm_uplift: Optional[str] = Field(
>     None, description="Added CPM if SSP targeting is used")
> built_in_targeting: Optional[dict] = Field(
>     None, description="Targeting already baked into a 3P deal, if exposed")
> ```
>
> **Also corrected in:** the Targeting step constraints, where the same absolute phrasing appeared.
>
> #### ⚠ OPEN QUESTIONS arising
> 1. **How limited is Amazon's targeting on 3P, exactly?** Note 19 confirms audiences work; what does *"may be limited"* exclude, and does it vary by provider?
> 2. Can Amazon audiences **and** SSP targeting apply to the same 3P deal, or is it one or the other?
> 3. **🔴 Is a 3P deal's built-in targeting exposed in structured deal metadata?** *This has become **blocking** — see Review Note 18. If the agent is matching deals against stated requirements, it must be able to read each deal's targeting programmatically.*

> ### 📋 REVIEW NOTE — Deal commitment must be surfaced even when deal identity is hidden
>
> The "Can pause?" column above carries real financial consequence: a **PG deal commits the full budget and cannot be paused.** Review Note 18 establishes that deal identity is no longer surfaced to the trader. Those two facts together create a risk — the agent could select a PG deal and the trader would commit spend without knowing.
>
> **Rule:** the agent hides deal *identity* but must always surface the **commitment consequence**. See Review Note 18 for the wording.

## 2.4 Audience Set Profiles

🔄 **CHANGED** — renamed "Broad" to "Wide" per client vocabulary.

| Profile | Was (v1.1.0) | Now |
|---|---|---|
| 1 | Narrow (High Precision) | **Narrow** — highly targeted, elevated intent, **risk of underdelivery** |
| 2 | Balanced (Recommended) | **Balanced** — optimal blend, the usual recommendation |
| 3 | Broad (Maximum Scale) | **Wide** — broad demographic/interest reach, less precision |

➕ **NEW** — the audience fee (VCPM) stacks on top of the deal CPM. The agent should surface the **effective CPM** (deal + audience fee), not just the deal price.

➕ **NEW** — audiences are **optional** and suggestion-driven. The agent always suggests three options using VOW's existing pgvector + OpenAI feature (`POST /audience-sets/suggest/`). Nobody browses the ~3,400 segments manually.

❌ **REMOVED** for CTV: product audiences (not applicable per client). AMC audiences are conditional — available only when the advertiser has prior campaign data (retargeting tactic).

> ### 📋 REVIEW NOTE 2 — The audience fee model was wrong: fee follows the data source, not the profile
>
> **David's comments:**
> > *"there's not necessarily a fee consequence. Fee is determined by which audiences are used not how many. If it's Amazon's or a 3P first party data like Lifestyle or Interest then there's a fee for using it. This is regardless of profile."*
> >
> > *"Note here that it doesn't compound the more audiences you use. There is just 1 fixed CPM applied when 1P data is used for Amazon or Third party audience. But if the user matches a segment in both you would pay both fees."*
>
> v2.0 previously stated *"added fee consequence"*, marked Narrow as carrying a *"higher audience fee"* and Wide a *"lower fee"*, and described a narrow audience as *"both smaller and more expensive per impression."* **All of that was incorrect.** It asserted a correlation between profile breadth and cost that does not exist.
>
> | | **What v2.0 said (wrong)** | **How it actually works** |
> |---|---|---|
> | What drives the fee | Profile breadth (Narrow / Balanced / Wide) | **The data source** of the segments used |
> | More segments | More fee (compounding) | ❌ **No compounding** — one fixed CPM per data source |
> | Narrow vs Wide | Narrow more expensive | **Identical**, if both use the same data source |
>
> **The rule, precisely:**
> - Using **Amazon's own (1P) audience data** → **one fixed CPM** applies, regardless of how many Amazon segments are in the bundle
> - Using **third-party audience data** (e.g. Lifestyle, Interest segments) → **one fixed CPM** applies for that source
> - If a given user **matches a segment in both** sources → **both fees** are charged for that impression
> - This is **regardless of profile**
>
> **What remains correct:** the fee still **stacks on top of the deal CPM**, and Narrow still carries a genuine **risk of underdelivery** — but for reach reasons, not cost reasons.
>
> #### Consequence for effective CPM — it becomes a range
>
> For a **single-source** bundle, effective CPM is a single figure:
> ```
> Deal CPM £28.88 + Amazon data fee £1.85 = £30.73
> ```
> For a **mixed-source** bundle it is a **range**, because it depends on which source each impression's user matched in:
> ```
> Matched Amazon only  → £28.88 + £1.85         = £30.73
> Matched 3P only      → £28.88 + £2.10         = £30.98
> Matched both         → £28.88 + £1.85 + £2.10 = £32.83
>
> → Effective CPM: £30.73 – £32.83
> ```
> The agent must therefore present effective CPM as a **range or a blended estimate for mixed-source bundles**, and state that it is an estimate. A single exact figure is not available in that case.
>
> **Consequence for the agent's recommendation.** The reason for recommending Balanced changes. It is not cheaper than Narrow — with the same data source it costs exactly the same. It is recommended because it delivers materially more reach at no additional data cost.
>
> **Schema changes:**
> ```python
> class AudienceDataSourceEnum(str, Enum):
>     """➕ NEW — the fee is charged per data source, not per segment"""
>     AMAZON_1P = "AMAZON_1P"
>     THIRD_PARTY = "THIRD_PARTY"
>     NONE = "NONE"                # e.g. basic demographic — no data fee
>
> class SelectedAudienceSetSchema(BaseModel):
>     audience_set_id: str
>     name: str
>     data_source: AudienceDataSourceEnum    # ➕ NEW — drives the fee
>     profile: AudienceProfileEnum
>     estimated_reach: Optional[int] = None
>     # vcpm_fee REMOVED from segment level — the fee is per source
>
> class AudienceFeeSchema(BaseModel):
>     """➕ NEW — fees resolved per data source, not per segment"""
>     amazon_1p_fee: Optional[str] = None
>     third_party_fee: Optional[str] = None
>     is_mixed_source: bool = False
>     effective_cpm_min: str        # one source matched
>     effective_cpm_max: str        # matched in both
>     effective_cpm_note: str       # e.g. "range because bundle is mixed-source"
> ```
>
> #### ⚠ OPEN QUESTIONS arising
> 1. **The `suggest` endpoint returns a per-segment `vcpm`** (`1.85`, `1.63`, `1.20`). If the fee is one fixed CPM per data source, are those values each segment's respective source rate — or does the agent need to collapse them to a per-source fee itself? *The effective-CPM calculation cannot be implemented until this is settled.*
> 2. Is there any audience type that carries **no** data fee (e.g. basic demographic)? If so the agent can offer a zero-fee option.
> 3. What are the **actual figures** for the Amazon 1P fee and the third-party fee — fixed, or dependent on audience type?
> 4. In a mixed-source bundle, what is the typical **match-in-both ratio**? Without it, only a range can be given, not a blended estimate.

> ### 📋 REVIEW NOTE — What the three profiles actually are, after the review
>
> Three separate comments have changed the nature of Narrow / Balanced / Wide. Taken together the description in this section needs rewriting, not just adjusting:
>
> | | v2.0 said | After review |
> |---|---|---|
> | **Cost** | Narrow costs more, Wide less | **Identical** on the same data source — Note 2 |
> | **Requirement** | One must be chosen | **Optional** — Note 4 |
> | **Origin** | Returned by the `suggest` API as `bundles.narrow/balanced/broad` | **Constructed by the agent** — the API does not support that shape (Note 20) |
> | **Applies to** | Amazon-owned inventory only | **All tiers** — Amazon audiences work on 3P too (Note 19) |
>
> So the profiles are an **agent-side presentation device**, built from a flat API response, that differ on **reach and precision only**, are **opt-in**, and apply across all inventory tiers.
>
> **One inconsistency this clears up:** `AudienceProfileEnum` uses `WIDE` while §4.2's example returned `bundles.broad`. Since Note 20 establishes there is no `bundles` object, the mismatch disappears — `WIDE` stands, and the agent's own grouping uses it.

---

# 3. The Agentic Flow — Step by Step

🔄 **CHANGED** — entirely reordered. The original followed the 6-step UI wizard. This follows the client-confirmed CTV-first agentic flow (v5).

## Comparison: old order vs new order

| Old (v1.1.0 wizard) | New (v2.0 agentic, confirmed) | Review outcome |
|---|---|---|
| 1. Strategy details | **1. Basics** (+ durations) | 🔄 Rebuilt — see Review Notes 6–17 |
| 2. Goal, KPI & bid | *(goal/KPI/bid folded into Basics)* | 🔄 KPI target value added (Note 10); base bid removed (Note 12) |
| 3. Deals | **2. CTV inventory** (three-tier fork) | 🔄 Deals now **matched by the agent** — see Review Note 18 |
| — | **3. Budget split** ➕ NEW | 🔄 **Optional**, not Required — see Review Note 3 |
| 4. Audiences | **4. Audiences** (~~mandatory~~ **optional**, suggestion-driven) | 🔄 **Optional** — see Review Note 4 |
| — | **5. Targeting** ➕ NEW | 🔄 **Merges with Step 4** — see Review Note 5 |
| *(forecast was a sub-step)* | **6. Predict reach** (Amazon only; repair loop) | 🔄 Repair loop rewritten — see Review Note 12 |
| — | **7. Plan approval** ➕ NEW | ✅ Unchanged by review |
| *(create was at the end)* | **8. Create the real strategy** | 🔄 `product_asins: []` at create — see Review Note 17 |
| 5. Creatives | **9. Upload video creative** (+ duration check) | ✅ Unchanged by review *(comments 19–28 pending)* |
| — | **10. Platform creative approval** ➕ NEW | ✅ Unchanged by review |
| *(ASINs were in step 1)* | **11. Tracking setup** (ASINs + ad tag) 🔄 MOVED | 🔄 Selling location also moves here — see Review Notes 16–17 |
| — | **12. Credit check** ➕ NEW | ✅ Unchanged by review |
| 6. Summary → create | **13. Activate** ➕ NEW | ✅ Unchanged by review |

> ### 📋 REVIEW NOTE — After the review, the flow is 12 steps, not 13
>
> Review Note 5 merges Audiences and Targeting into a single step. The confirmed sequence becomes:
>
> ```
>  1. Basics                  (summary to confirm, not a form)
>  2. CTV inventory           (agent matches deals; only CPM surfaced)
>  3. Targeting               (default applied → refine or accept;
>                              audiences are one targeting type)
>  4. Budget split            (optional; preferred for an accurate CPM)
>  5. Predict reach           (Amazon only; rewritten repair loop)
>  6. ⏸ Plan approval
>  7. Create the real strategy
>  8. Upload video creative   (+ duration check)
>  9. Platform creative approval
> 10. Tracking setup          (selling location + ASINs + ad tag)
> 11. Credit check
> 12. 💰 Activate
> ```
>
> ⚠ **Step order to confirm.** Targeting is shown **before** Budget split. David's wording — *"once inventory decided / inferred then you are shown the default targeting"* — implies targeting comes straight after inventory. There is also a logical reason: the audience data fee is set during targeting, and that fee is an input to the accurate CPM the budget split is meant to produce. **To confirm with David.**

> ### 🔴 REVIEW NOTE — After Note 27, the tail of the flow is not a chain
>
> The list above still reads as a linear sequence. **It is not, after the create step.** Review Note 27 establishes that creative, tracking and credit are **independent** and converge at activation:
>
> ```
> SEQUENTIAL — each step genuinely requires the previous
>   1. Basics                  (a summary to confirm — Note 6)
>   2. CTV Inventory           (the agent matches deals — Note 18)
>   3. Targeting               (default → refine or accept; audiences included — Note 5)
>   4. Budget Split            (optional — Note 3)
>   5. Predict Reach           (honesty rule; rewritten repair loop)
>   6. Finalise Plan           (a status change — Note 23)
>   7. Create Strategy         (⚠ simple-strategies endpoint — Note 24)
>
> ─────── 🔀 PARALLEL — any order, concurrently — Note 27 ───────
>
>   A: 📹 Upload creative ──→ Platform approval (per channel — Note 26)
>        🔁 rejected → re-upload                    (branch-local)
>        🔁 duration mismatch → ⬆ back to Finalise   (cross-branch)
>        ⏸ interrupt() — the only genuine one in M1  (Note 23)
>
>   B: 📊 Tracking setup
>        • Ad tag check + install   ← 🔴 no dependency; can start first
>        • ASIN collect + PATCH     ← after Create
>        • Conversion events        ← after the tag
>
>   C: 💳 Credit check
>        🔁 insufficient → top-up                    (branch-local)
>
> ─────── 🔗 JOIN — waits for all branches ───────
>
>   💰 ACTIVATE                (the single spend action)
>      ⚠ The agent states anything still incomplete — e.g. a duration
>        whose creative has not been uploaded will not deliver
> ```
>
> **Why this matters for the build:** the graph has a different shape. Three branches means three independent progress states, a join condition at activation, and an agent that reports *what is outstanding* rather than *what is next.*

---

# Step 1: Basics

🔄 **CHANGED** — merged original Steps 1 and 2 (strategy details + goal/KPI/bid), added durations, scoped to CTV.

## What was in v1.1.0 (Step 1 + Step 2)

- Strategy name, flight dates, target markets, primary currency, formats (all four), product categories, selling location, ASINs
- Goal (three choices), KPI (six choices), ad tag conversions, market budgets, base bids

## What it was in v2.0 before review

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Strategy name | String | Required | ✅ Unchanged. Validated via `GET /api/strategies/check_strategy_name_uniqueness/` |
| Flight dates | Date range | Required | ✅ Unchanged. `lower ≥ today`, `upper > lower` |
| Target markets | Multi-select | Required | ✅ Unchanged. ISO country codes (GB, US, DE) |
| Primary currency | Dropdown | Required | ✅ Unchanged. EUR, GBP, USD |
| Creative durations | Multi-select | Required | ➕ NEW. Values 10, 15, 20, 30 (seconds). Determines which deals are available and what CPM applies |
| Goal | Fixed | Required | 🔄 CHANGED. For CTV, always Awareness |
| KPI | Select | Required | 🔄 CHANGED. For CTV, reach or frequency only |
| Market budgets | Table | Required | ✅ Unchanged. Per-market budget, must be > 0 |
| Base bids | Table | Required | ✅ Unchanged. Per-market base CPM bid |
| Frequency cap | Number | Optional | ➕ NEW. Client confirmed optional |
| Budget cap | Number | Optional | ➕ NEW. Client confirmed optional |
| Formats | Fixed | Required | 🔄 CHANGED. For M1, streaming_tv and prime_video only |
| Product categories | Multi-select | Required for video | ✅ Unchanged. Fetched via `GET /api/contextual-targeting/{market}/product-categories/` |
| Selling location | Radio | Required | ✅ Unchanged. `ON_AMAZON` or `NOT_SOLD_ON_AMAZON` |
| Product ASINs | Textarea | Conditional | 🔄 MOVED. Validation and collection now at Step 11 |

**API calls at this step:** `GET /api/strategies/check_strategy_name_uniqueness/`, `GET /api/contextual-targeting/{market}/product-categories/`

❌ **REMOVED from this step:** ad tag conversions (moved to Step 11), the three non-CTV format options (Display, Online Video — future scope), the four non-awareness KPIs (CTR, CPC, CPA, CPDPV — future scope).

---

## 📋 REVIEW NOTES — Step 1 (twelve comments)

Twelve of David's eighteen comments land on this single table. Taken together they change what Step 1 *is*: not a form the trader fills in, but **a summary the agent presents for confirmation.**

### The structural fix: every field matrix needs a `Source` column

The matrices record **whether** a value is required but never **where it comes from**. "Required" has been read as "the trader must type it" — those are two different things. **A value can be required and supplied by the agent.**

All field matrices in this document now carry a **Source** column:

| Source | Meaning | Example |
|---|---|---|
| 💬 **ASKED** | The trader must supply it | KPI target value, when the KPI is frequency |
| 🧠 **INFERRED** | Parsed from the brief text | *"UK"* → `markets: ["GB"]` |
| ⚙️ **DERIVED** | Computed from another field | `markets: ["GB"]` → `primary_currency: "GBP"` |
| 🏢 **ADVERTISER** | From the advertiser's defaults or record | Frequency cap, product categories |
| 🤖 **GENERATED** | Produced by the agent | Strategy name |
| 🔒 **FIXED** | Constant for CTV | `goal = AWARENESS`, `formats = ["streaming_tv"]` |
| 🔌 **API** | Returned by an API call | `product_category` from ASIN validation |
| ⏭️ **LATER** | Collected at a later step — not listed here at all | Selling location, ASINs |

The `Type` column is also split. It currently mixes four different things — real data types (String, Number, Date range), UI widgets (Dropdown, Radio, **Table**, Toggle, Checkbox table), sources (Fixed, Derived, Question, Check) and domain terms ("3 profiles", "Allocation (%)"). **UI widgets are removed entirely: this document is the data contract, not the UI specification.** Widget choices belong in the UI spec.

### The revised Step 1

| Field | Data type | Requirement | Source | Note |
|---|---|---|---|---|
| **Strategy name** | `str` | Required | 🤖 **GENERATED** (editable) | 7 |
| **Flight dates** | `{lower, upper, bounds}` | Required | 🧠 INFERRED from brief | 6 |
| **Target markets** | `list[str]` *(M1: length 1)* | Required | 🧠 INFERRED from brief | 8 |
| **Primary currency** | `CurrencyEnum` | Required | ⚙️ **DERIVED** from market · 🏢 or advertiser default | 9 |
| **Creative durations** | `list[DurationEnum]` | Required | 🧠 INFERRED from brief | 6 |
| **Goal** | `GoalEnum` | Required | 🔒 **FIXED** = `AWARENESS` | 6 |
| **KPI** | `KPIEnum` | Required | ⚙️ **DERIVED** from goal (default `reach`) | 6 |
| ➕ **KPI target value** | `int` (1–5) | **Conditional** — required if KPI = frequency | 💬 ASKED | **10** |
| **Market budgets** | `list[{market, budget}]` *(M1: length 1)* | Required | 🧠 INFERRED from brief | 11 |
| **Product categories** | `list[int]` | Required | 🏢 **ADVERTISER** → 🧠 brief → 🔌 ASIN API | 15 |
| **Frequency cap** | `int` | Optional | 🏢 **ADVERTISER** default | 13 |
| **Budget cap** | `str` | Optional | 🏢 ADVERTISER default · 💬 or asked | 13 |

**Removed from Step 1 (five fields):**

| Field | Where it goes | Note |
|---|---|---|
| **Formats** | 🔒 System constant — `["streaming_tv"]` | 14 |
| **Base bids** | ❌ Not applicable to CTV (fixed-CPM deals) | 12 |
| **Selling location** | ⏭️ Step 11 · 🏢 advertiser default | 16 |
| **Product ASINs** | ⏭️ Step 11 | 17 |
| *Ad tag conversions* | ⏭️ Step 11 *(already moved in v2.0)* | — |

> **The result:** twelve fields instead of fourteen, and **no field is both asked and required.** The only asked field is a conditional one. That is what Principle 2 looks like in practice — and the previous matrix did not express it.

### What Step 1 now looks like in conversation

```
Trader:
"BrightPath — UK, August, £10,000, Prime Video awareness campaign,
 education website, 30-second creative."

Agent (infers everything, asks nothing):
┌────────────────────┬──────────────────────────────────────────────┐
│ Strategy name      │ BrightPath_Awareness_GB_Aug2026   (generated)│
│ Market             │ United Kingdom (GB)                          │
│ Currency           │ GBP — derived from market                    │
│ Flight             │ 1–30 Aug 2026                                │
│ Budget             │ £10,000                                      │
│ Duration           │ 30 seconds                                   │
│ Goal               │ Awareness — fixed for CTV                    │
│ KPI                │ Reach — default for Awareness                │
│ Product category   │ Education — from advertiser record           │
│ Frequency cap      │ 3 per week — advertiser default              │
└────────────────────┴──────────────────────────────────────────────┘

"That's what I've taken from your brief. Tell me if anything's wrong,
 otherwise I'll move on to inventory."
```

---

### 📋 REVIEW NOTE 6 — The field list needs reviewing for CTV, and answers implied

**David's comment:** *"should review as a lot of this is for a non CTV strategy - can simplify for CTV and imply answers"*

Two distinct problems.

**First, some fields are genuinely non-CTV** and should not be presented as choices at all:

| Field | Problem | Correction |
|---|---|---|
| `formats` (all four) | Display and online_video are out of scope; in a CTV module the format is known | 🔒 **FIXED** — see Note 14 |
| `goal` (three choices) | CTV is always Awareness (client-confirmed) | 🔒 **FIXED** to `AWARENESS` |
| `kpi` (six choices) | Four of the six are click-based and impossible on CTV | ⚙️ Scoped to `reach` / `frequency`, defaulted from goal |

**Second, the `Source` column** — covered above. Applied to Step 1 it produces the revised table above.

**A further consequence — base bids.** `Base bids` was Required. It can be derived from the CTV rate card, and Step 6's repair loop already assumes the agent knows the right value (*"increase from £15 to £30 for Prime Video"*). **David's separate comment goes further and removes the field entirely — see Note 12.**

---

### 📋 REVIEW NOTE 7 — Strategy name is generated, not asked

**David's comment:** *"could be auto generated from brief"*

`Strategy name` remains **Required** — a strategy cannot exist without one — but its **Source is GENERATED**. The agent composes it from the brief:

```
advertiser + goal + market + month + year
→ "BrightPath_Awareness_GB_Aug2026"
```

The uniqueness check runs automatically (`GET /api/strategies/check_strategy_name_uniqueness/`), and on collision the agent appends a suffix and **tells the trader** — consistent with the existing duplicate-name protocol in §7.2 (*"append suffix… and prompt user"*). The trader can override the generated name at any point.

**Why generated rather than asked:** the name is a retrieval label, not a planning decision. Traders do not care about it while planning, and agent-generated names are consistently formatted, which makes later search reliable.

**⚠ To confirm:** is there an existing naming convention the generated name should follow?

---

### 📋 REVIEW NOTE 8 — Multi-market support: a scope decision is required

**David's comment:** *"Are we going to support multi market? what impact to the flow will it have - repeating choices for each market?"*

`Target markets` is multi-select, and §7.1 explicitly adds *"UK and France → `markets: ["GB", "FR"]"`* as a ➕ NEW parsing rule — so v2.0 brought multi-market into scope. **The flow consequences were not worked through.** They are substantial.

| Already per-market | 🔴 Would need to repeat per market |
|---|---|
| `market_budgets` · `base_bids` | Deals · Audiences · Rate card · Locations · Product categories · ASIN validation · Forecast · Creatives (language) · Creative approval |

**Two concrete gaps this exposes:**

1. **Every market-scoped API takes a single market**, not a list:
   `GET /api/deals/?markets={market}` · `POST /audience-sets/suggest/` with `{"market": "GB"}` · `GET /api/rates/ctv/{market}/` · `GET /api/strategies/locations/{market}/` · `GET|POST /api/contextual-targeting/{market}/…`
   Multi-market therefore means **N calls per step**, and N result sets to hold and present. The document never states this.

2. **`BudgetSplitSchema` has no `by_market`.** It has `by_inventory` and `by_duration` only. Multi-market makes the split **three-dimensional** — market × inventory × duration. Two markets, two inventories and two durations is eight lines.

**One clarification worth recording either way:** unlike the cross-platform case, **reach can be summed across markets** — a GB viewer and an FR viewer are different people, so there is no deduplication problem. This is the opposite of the Prime + Netflix case in Step 6, and both should be stated explicitly.

**Recommendation (for decision):** keep `markets: list[str]` in the schema so nothing has to migrate later, but **constrain M1 to a single market in the flow**. If a brief names more than one, the agent says so plainly and offers to plan the first market, with the others as separate strategies. This matches the single-market shape of every relevant API and keeps M1 deliverable.

> **⚠ OPEN QUESTION — Is multi-market in scope for M1, or M2?** This affects effort materially and should be decided before build, not discovered during it.

---

### 📋 REVIEW NOTE 9 — Primary currency is derived, not asked

**David's comment:** *"just use market currency if single market"*

`Primary currency` was typed **Dropdown / Required**, implying the trader selects it. **For a single market it is derived from that market** — `GB → GBP`, `US → USD`, `DE|FR → EUR`. The term "primary" only has meaning when more than one currency is in play.

**This already contradicted §7.1**, which lists `UK → markets: ["GB"], primary_currency: "GBP"` as an original ✅ parsing rule. The parsing section derives it; the field matrix asked for it. The matrix was wrong.

**Corrected:** Requirement stays **Required**; Source becomes **DERIVED from market**.

**Multi-market rule (previously undefined):** in order of preference — (1) the advertiser account's default currency, (2) the currency of the largest-budget market, (3) ask. In all cases the agent shows it as an assumption: *"Reporting in GBP — the advertiser's account currency. Change it?"*

> Note 13 confirms that advertiser-level defaults exist, so option (1) now rests on something concrete rather than an assumption.

---

### 📋 REVIEW NOTE 10 — A missing field: KPI target value

**David's comment:** *"if frequency then you can have kpi target too of 1-5"*

The matrix recorded `KPI` as the metric (`reach` or `frequency`) but had **no field for the target value.** Per David, **when KPI is `frequency`, a numeric target of 1–5 applies.**

**Two pieces of internal evidence that this field was always needed:**

1. The schema field is named **`kpi_target_type`** — "type" implies a companion "value" that does not exist.
2. **The repair loop references a target the schema cannot hold.** §6.2 says *"Check if reach > 0 and **frequency within targets**"*, and §7.1 triggers repair on *"`estimated_unique_reach == 0` **or insufficient frequency**"*. Neither was implementable — there was nothing to compare against.

**Frequency target and frequency cap are different things**, and the document previously had only the latter:

| | **Frequency target (1–5)** | **Frequency cap** |
|---|---|---|
| What it is | An **optimisation goal** — the average to aim for | A **hard limit** — never exceed |
| DSP behaviour | Paces delivery toward the average | Blocks the (n+1)th impression |
| In one word | **Aim** | **Ceiling** |

**Why only frequency has a numeric target:** frequency is **controllable** — the DSP can pace delivery to hit an average. Reach is an **outcome** — it falls out of budget, audience, inventory and CPM. You read reach; you set frequency.

**Schema addition:**
```python
# FullStrategySchema
kpi_target_value: Optional[int] = Field(
    None, ge=1, le=5,
    description="Target average frequency. Required when kpi_target_type == frequency")
```

**Validation rules to add:**
- Required when `kpi_target_type == "frequency"`; must be 1–5
- **`frequency_cap` must exceed `kpi_target_value`** — a target of 4 under a cap of 3 is mathematically unreachable. This matters because the cap has an advertiser-level default (Note 13), so the conflict can arise without the trader doing anything.

**Consequence:** with this field in place, the repair loop's frequency check becomes implementable for the first time.

> **⚠ OPEN QUESTION —** §7.1 should also define what *"insufficient frequency"* means numerically. How far below target triggers repair?

---

### 📋 REVIEW NOTE 11 — Market budgets shape, and a structural problem with the Type column

**David's comment:** *"single market budget?"*

**On the immediate question:** if M1 is single-market (Note 8), the trader deals with **one budget figure**, not a table.

| | Schema (unchanged, M2-ready) | What the trader sees in M1 |
|---|---|---|
| Budget | `list[{market, budget}]`, length 1 | *"Budget: £10,000"* — a single figure |

**Data model shape and presentation shape are different things**, and this document should specify the former.

**Which exposes the structural problem the highlight points at:** "Table" is a **UI widget**, not a data type. See *"The `Type` column is also split"* above — this is the concrete case that motivated it. Note 18 shows why it matters: because a UI widget sat in the data contract, the document accidentally specified an interaction model that turned out to be wrong.

---

### 📋 REVIEW NOTE 12 — Base bids are not applicable to CTV, and the repair loop depended on them

**David's comment:** *"not required for CTV as defined by CPM of deals"*

`Base bids` was marked **Required**. It is **not required for CTV, because the CPM is defined by the deal.**

**The document's own §2.3 already said this:**

| Deal type | Price | Is a base bid meaningful? |
|---|---|---|
| Programmatic Guaranteed | **Fixed CPM** | ❌ No — the price is set |
| Preferred Deals | **Fixed CPM** | ❌ No — the price is set |
| Private Auctions | Floor CPM, **competitive** | 🟡 Possibly — bidding occurs |

A base bid is a maximum you are willing to pay in an **auction**. Pre-curated Preferred and PG deals have no auction, so the field has nothing to act on. Every deal example in this document is Preferred. **Base bid is an open-auction / Display concept carried over from v1.1.0** — the same class of leftover as `formats (all four)`.

**Corrected:** `base_bid` → **not applicable for CTV**, or Conditional (Private Auction only). `MarketBudgetBidSchema.base_bid` becomes `Optional[str] = None`.

#### 🔴 The significant consequence — the repair loop loses a lever

§7.1 Action 2 reads *"Adjust base CPM bid up to market recommended floor (e.g. increase from £15 to £30 for Prime Video)."* **On a fixed-CPM deal this does nothing.** Combined with audiences becoming optional (Note 4), the loop can be left with **no levers at all**:

```
No audience selected + Preferred (fixed CPM) deal + low reach
  Action 1: widen the audience  → nothing to widen
  Action 2: raise the bid       → CPM is fixed
  Action 3: re-forecast         → same result
  → the repair loop has nothing to do
```

**The repair loop is therefore rewritten with a real, ordered lever list:**

| # | Lever | Applies when |
|---|---|---|
| 1 | **Relax other targeting** — device, location, content exclusions | Always — *the primary lever now that audiences are optional* |
| 2 | **Extend the audience** — add segments within the chosen profile | An audience is applied |
| 3 | **Switch matching mode** Exact → Similar | An audience is applied |
| 4 | **Add inventory** — more deals / more providers | Always |
| 5 | **Extend flight dates** | Always |
| 6 | **Increase budget** | Requires the trader |
| 7 | **State the limit honestly** — *"this deal's inventory cannot deliver more reach than X"* | When nothing above helps — Zero-Hallucination |

This rewrite applies in both §7.1 and Step 6, and it **materially affects the graph** — the number and shape of repair edges changes.

> **⚠ OPEN QUESTIONS —**
> 1. Are **Private Auction** deals in scope for CTV M1? Every example here is Preferred. If they are, `base_bid` stays as a conditional field rather than being dropped.
> 2. When no lever remains, what exactly should the agent do — stop and report, or offer to change the plan?

---

### 📋 REVIEW NOTE 13 — Advertiser-level defaults are a missing concept

**David's comment:** *"we have a default per advertiser"*

`Frequency cap` was marked **Optional**, implying it is empty unless the trader fills it. **There is a default per advertiser** — the field arrives pre-filled and the trader overrides it.

"Optional" is technically correct (the trader need not supply it) but practically misleading (it is never empty). Requirement = **Optional**, Source = **🏢 ADVERTISER default**.

#### 🔴 The larger finding: advertiser-level defaults do not exist anywhere in this document

`advertiser_id` appears as a UUID and nothing more. There is:

- ❌ no `AdvertiserDefaultsSchema`
- ❌ no endpoint in §4 to fetch advertiser settings
- ❌ no `advertiser_defaults` in `PlanningAgentState`
- ❌ no mention of "advertiser settings" anywhere in the document

**Additions required:**
```python
class AdvertiserDefaultsSchema(BaseModel):
    """➕ NEW — defaults held per advertiser, loaded at session start"""
    frequency_cap: Optional[int] = None                    # confirmed
    product_categories: list[int] = Field(default_factory=list)   # confirmed (Note 15)
    product_location: Optional[ProductLocationEnum] = None        # likely (Note 16)
    primary_currency: Optional[CurrencyEnum] = None               # likely (Note 9)
    budget_cap: Optional[str] = None
    content_category_exclusions: list[str] = Field(default_factory=list)
    approval_threshold: Optional[str] = None                      # possibly (Step 7)
```
Plus an endpoint in §4 (`GET /api/advertisers/{id}/defaults/` or the real equivalent), and `advertiser_defaults: Optional[dict]` in the planning state, **loaded before field extraction**.

**This was confirmed twice** — frequency cap here, and product categories in Note 15 — which makes it a firm requirement rather than a suggestion. It may also answer Step 7's open question about the manager-approval threshold being *"possibly budget-threshold-based"*.

> **⚠ OPEN QUESTIONS —**
> 1. Beyond frequency cap and product categories, which values have advertiser-level defaults? Currency? Budget cap? Content exclusions? Approval threshold?
> 2. What is the real endpoint for fetching them?
> 3. Is the frequency cap default weekly, daily or lifetime? *(The Pydantic comment says weekly; the field table does not say.)*

---

### 📋 REVIEW NOTE 14 — Format is always `streaming_tv`; Prime Video is a provider

**David's comment:** *"is always streaming_tv"*

The matrix listed `formats` as *"streaming_tv and prime_video only"*. It is **always `streaming_tv`** — a single value.

**The reason is a level error:** `prime_video` is not a format. It is a **provider** (supply source) *within* streaming TV.

| Level | Values | Where it is decided |
|---|---|---|
| **Format** | `streaming_tv` | Step 1 — constant for a CTV module |
| **Provider** | Prime Video · Netflix · Hulu · Disney+ | **Step 2** (inventory) |

**This is already modelled correctly elsewhere in the document** — `SelectedDealSchema.provider` carries *"e.g. Prime Video, Netflix, Disney+"*. Listing Prime Video again as a format duplicated it at the wrong level.

**And Step 2's own API example agrees:** `GET /api/deals/?markets={market}&formats=streaming_tv` — `streaming_tv` only. Step 1 and Step 2 contradicted each other, and Step 2 was right.

**Corrected:** `formats` becomes a **system constant** (`["streaming_tv"]`) rather than a field with choices. `FormatEnum.PRIME_VIDEO` is annotated as *"not a format — see `SelectedDealSchema.provider`"*.

> **⚠ To confirm:** v1.1.0's create payload used `"formats": ["prime_video"]`, so the Amazon DSP API may historically accept it. Which values does the real endpoint take?

---

### 📋 REVIEW NOTE 15 — Product categories come from the advertiser, not the trader

**David's comment:** *"we have a default on the advertiser, or maybe could imply from the brief"*

`Product categories` was marked *"Required for video"*, implying the trader selects it per campaign. **There is a default on the advertiser, and it can also be implied from the brief.**

**This is the second confirmation of advertiser-level defaults** (Note 13), which is what makes the missing `AdvertiserDefaultsSchema` a firm requirement.

**Why product category belongs to the advertiser:** it does not vary by campaign. BrightPath is always Education; Nike is always Apparel. Asking for it on every strategy is conceptually wrong — it is an attribute of the advertiser, not of the plan.

**Resolution order (fallback chain):**

| Priority | Source | Example |
|---|---|---|
| 1 | 🏢 **Advertiser default** | BrightPath → Education |
| 2 | 🧠 **Inferred from brief** | *"education website"* → Education |
| 3 | 🔌 **ASIN validation response** | the response already returns `"product_category": "Electronics"` |
| 4 | 💬 Ask the trader | last resort only |

**Source 3 already exists in this document and has never been used** — §4.2's ASIN validation example returns `product_category` per ASIN. It should be wired to auto-fill this field.

**Also:** *"Required for video"* is a v1.1.0 artefact. CTV is always video (Note 14), so the qualifier is redundant — it is simply **Required**.

---

### 📋 REVIEW NOTE 16 — Selling location leaves Step 1

**David's comment:** *"can leave out"*

Two reasons support it:

1. **It is a tracking question, not a planning question.** v2.0 already moved ASIN collection and ad-tag conversions to Step 11; selling location belongs with them.
2. **It is largely an advertiser attribute, not a campaign one.** Whether a brand sells on Amazon does not change per campaign. This makes it the third field — after Frequency cap and Product categories — that is really an advertiser-level value.

**Corrected:** the row is removed from Step 1. `product_location` is added to `AdvertiserDefaultsSchema` as the default (overridable per campaign), with confirmation at Step 11 where the *"Sells on Amazon?"* question already sits.

> **⚠ To confirm:** is `product_location` held on the advertiser record, or should it simply be asked at Step 11?

---

### 📋 REVIEW NOTE 17 — Product ASINs leave Step 1 — ✅ this resolves Open Question 1

**David's comment:** *"comes later"* — confirming v2.0's move to Step 11. The row therefore does not appear in the Step 1 matrix at all.

#### ✅ RESOLVED — Open Question 1 (raised twice, at Step 1 and again at Step 11)

> *"`product_location` and `asin_numbers` are fields in the `POST /strategies/` payload called at Step 8. If ASINs are collected at Step 11, they'd need to be patched afterwards. Alternatively, the ASIN question stays early…"*

**The answer is Option A — collect later and patch.** *(v2.0 had leaned toward Option B, keeping ASINs early. This review settles it the other way.)*

**And the document already demonstrates that Option A works.** §4.2's create payload example sends:
```json
"product_location": "NOT_SOLD_ON_AMAZON",
"product_asins": [],          ← empty array
```
So `POST /api/strategies/` accepts an empty ASIN list. The sequence becomes:

| Step | What happens |
|---|---|
| **Create strategy** | `POST /api/strategies/` with `product_asins: []`; `product_location` taken from the advertiser record |
| **Tracking setup** | Collect and validate ASINs, then `PATCH /api/strategies/{id}/` to attach them, plus the ad-tag check and conversions |

> **🔴 One gap this exposes: `PATCH /api/strategies/{id}/` is not in the §4 API catalogue.** It needs adding, since the resolution depends on it.
>
> **⚠ To confirm:** does that endpoint exist, and is `product_location` optional in the create payload?

---

# Step 2: CTV Inventory (the tier fork)

🔄 **CHANGED** — was Step 3 "Deals" in v1.1.0. Now comes before audiences, and introduces the three-tier fork.

## What was in v1.1.0

A flat deals table filtered by market and format, with checkbox selection.

## What it was in v2.0 before review

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Selected deals | Checkbox table | Required | ✅ Core concept unchanged. Fetched via `GET /api/deals/?markets={market}&formats=streaming_tv` |
| Inventory tier (per deal) | Enum | Derived | ➕ NEW. Each deal classified as `AMAZON_OWNED`, `THIRD_PARTY_PRECURATED`, or `THIRD_PARTY_NEEDS_CURATION` |
| CTV rate card | Reference | Read | ➕ NEW. `GET /api/rates/ctv/{market}/` — channels, durations, CPMs |
| Curation: genres | Multi-select | Required for curation tier | ➕ NEW |
| Curation: durations | Multi-select | Required for curation tier | ➕ NEW |
| Curation: targeting prefs | Text | Optional | ➕ NEW |
| Curation: budget | Number | Required for curation tier | ➕ NEW |
| Curation: flight dates | Date range | Required for curation tier | ➕ NEW |

➕ **NEW — Genre upsell logic.** The client asked: *"based on the brief we can suggest whether a specific available genre would be a better match at a slightly higher CPM."* Example: Prime Video ROS at $18.22 vs Action at $22.07 — the agent should recommend when the brief implies a genre match.

➕ **NEW — Curation capture (for 3P-needs-curation tier).** When deals can't be selected yet (Disney+ etc.), the agent captures what VOW needs to curate later: genres, durations, targeting preferences, budget, flight dates.

**API calls at this step:** `GET /api/deals/`, `GET /api/deals/filter-properties/`, `GET /api/rates/ctv/{market}/`

---

## 📋 REVIEW NOTE 18 — Deals are matched by the agent, not selected by the trader

**David's comment:**
> *"In majority of cases we want to pick the deals based on the requirements of the brief which we can do if we know the market, duration and channel. Optional ROS / genre and the different targeting types mentioned later. They may provide a deal id if they have 1 in mind but we want to remove the technical need to select deals from a table. We don't surface the underlying deal choices to the user - only the CPM"*

`Selected deals` was typed **"Checkbox table"** — an interaction the trader should not have to perform.

### The flow inverts

Previously the trader picked a deal and inherited whatever it carried. Instead, **the trader states requirements and the agent finds the deal that satisfies them.**

| | **Was (v1.1.0 model, retained in v2.0)** | **Now** |
|---|---|---|
| Trader does | Browses a deal table, reads deal names, ticks checkboxes | States requirements: channel, genre/ROS, targeting |
| Agent does | Renders the table | **Matches deals** from market + duration + channel |
| Trader sees | Deal names, deal IDs, deal types, CPMs | **Provider, CPM, impressions, tier capability** |
| Escape hatch | — | Trader **may supply a deal ID** if they have one in mind |

### The division of labour

| Trader — strategic | Agent — technical |
|---|---|
| Which platforms (Prime / Netflix / Disney+) | Which deal ID |
| ROS or a specific genre | Which deal within that genre |
| Targeting requirements | Which deal supports that targeting |
| Budget | Deal type, inventory tier derivation |

### This document already contained the correct pattern — it was not generalised

The **Tier 3 (3P-needs-curation)** treatment captures *"genres, durations, targeting preferences, budget, flight dates"* rather than presenting deals, because Disney+ deals do not exist yet. **That is exactly the model described here.** Tiers 1 and 2 kept the v1.1.0 checkbox table instead of adopting it. The curation-capture model should have applied to all three tiers.

### What is surfaced vs internal

| ✅ Surfaced to the trader | ❌ Internal only |
|---|---|
| Provider / channel | Deal name |
| CPM | Deal ID |
| Estimated impressions | The full deals list |
| Genre (if a specific one applies) | `ad_lengths` and other internals |
| **Tier capability** — whether reach is forecastable | Deal type *(but see the exception below)* |

> **⚠ One necessary exception to "only the CPM".** Deal *type* must not be silently hidden. A **Programmatic Guaranteed** deal commits the full budget and cannot be paused (§2.3). If the agent selects one without saying so, the trader commits spend without knowing.
>
> The agent hides the deal identity but surfaces the **commitment**:
>
> *"Prime Video, £31.50 CPM, 190,476 impressions. Note: this is guaranteed inventory — the full £6,000 is committed and cannot be paused. A Preferred deal is available at £33.20 if you'd rather keep the option to pause."*

### Genre upsell survives unchanged

The ➕ NEW genre-upsell logic presents **content type and CPM only** — no deal identity:

*"Two options: Prime Video with no content restriction at £18.22 CPM → 439,000 impressions, or Prime Video Sports content at £22.07 → 362,000 impressions. Your product is for gym-goers, so I'd recommend Sports — 77,000 fewer impressions but each one more relevant."*

It already conforms to this model.

### 🔴 A dependency this creates

For the agent to match deals against stated targeting requirements, it must be able to **read each deal's built-in targeting from structured metadata**. If that targeting exists only inside the deal *name* (`"Netflix | UK - 30 - Drama - A18-34"`), the agent would have to parse strings — fragile, and contrary to the Zero-Hallucination principle.

**This turns Review Note 1's third open question from a display concern into a blocking prerequisite for this step.**

### The revised Step 2

| Field | Data type | Requirement | Source |
|---|---|---|---|
| ➕ **Channel / provider** | `list[str]` | Required | 🧠 INFERRED from brief · 💬 asked — **this is the strategic choice** |
| ➕ **ROS or genre preference** | `Optional[str]` | Optional | 🧠 INFERRED from brief |
| ➕ **Targeting requirements** | `dict` | Optional | ⏭️ From the Targeting step |
| 🔄 **Selected deals** *(not surfaced)* | `list[SelectedDealSchema]` | Required | 🤖 **AUTO-MATCHED** from market + duration + channel |
| ➕ **Specific deal ID** *(escape hatch)* | `Optional[str]` | Optional | 💬 ASKED — only if the trader has one in mind |
| ✅ **Inventory tier** (per deal) | `InventoryTierEnum` | Derived | 🔌 API |
| ✅ **CTV rate card** | reference | Read | 🔌 API |
| ✅ **Curation fields** (×5) | `CurationRequirementsSchema` | Required if Tier 3 | 💬 ASKED · 🧠 INFERRED |

**Removed:** *"Checkbox table"* — a UI widget, not a data type — and the deal browsing/selection interaction itself.

### Schema changes

```python
class SelectedDealSchema(BaseModel):
    """🔄 CHANGED — deals are auto-matched, not trader-selected"""
    deal_id: str
    name: str                            # internal only — not surfaced
    cpm: str                             # ✅ surfaced
    inventory_tier: InventoryTierEnum    # ✅ surfaced (drives capability)
    provider: str                        # ✅ surfaced
    genre: Optional[str]                 # ✅ surfaced if specific
    ad_lengths: list[str]                # internal only
    deal_type: str                       # internal — but commitment is surfaced

    # ➕ NEW
    selection_method: str = Field("AUTO_MATCHED",
        description="AUTO_MATCHED | TRADER_SPECIFIED")
    matched_on: Optional[dict] = Field(None,
        description="Criteria used: market, duration, channel, genre, targeting")
    is_surfaced_to_trader: bool = Field(False,
        description="Deal identity is internal; only CPM is surfaced")


class DealMatchCriteriaSchema(BaseModel):
    """➕ NEW — what the agent matches deals against"""
    market: str
    duration: DurationEnum
    channel: str                                      # provider
    ros_or_genre: Optional[str] = None
    targeting_requirements: Optional[dict] = None
    trader_specified_deal_id: Optional[str] = None    # escape hatch
```

### Knock-on changes

- The state-machine node `select_inventory` becomes **`match_inventory`**
- `GET /api/deals/filter-properties/` changes purpose — it no longer populates filter dropdowns for a table; it tells the agent which genres and lengths are available to match against
- The adaptive canvas artifact for this step changes — a CPM summary, not a deals table

> **⚠ OPEN QUESTIONS arising**
> 1. 🔴 **Is a deal's built-in targeting exposed in structured metadata?** *Blocking — auto-matching cannot work without it.*
> 2. Should the agent ever auto-select a **PG deal**, or should PG always require explicit trader consent?
> 3. **Naming:** David says *"channel"*, the rate card endpoint says *"channels"*, and `SelectedDealSchema` says **`provider`** — all for the same thing. Meanwhile `ChannelTypeEnum` uses "channel" for `dsp`/`sponsored`. One term should be chosen.
> 4. If **several deals match**, how should the agent choose — cheapest? most relevant? best forecast?
> 5. If **no deal matches**, what should the agent do?

---

# Step 3: Targeting *(merged — was Steps 4 and 5)*

🔄 **CHANGED** — Review Note 5 merges the former Step 4 (Audiences) and Step 5 (Targeting) into one step, positioned directly after inventory.

## What was in v1.1.0

- Step 4: browse/search audience sets, checkbox selection, Similar/Exact toggle
- *(No targeting step existed)*

## What it was in v2.0 before review

**Step 4 — Audiences**

| Field | Type | Requirement | Change |
|---|---|---|---|
| Audience options | 3 profiles | Required | 🔄 CHANGED from optional to mandatory. Agent always generates narrow / balanced / wide |
| Chosen option | Select one | Required | ➕ NEW. Trader picks one of the three |
| Matching mode | Toggle | Required | ✅ Unchanged. Similar vs Exact |
| Effective CPM (per option) | Display | Read-only | ➕ NEW. Deal CPM + audience VCPM fee |

**Step 5 — Targeting** *(all optional)*: Location, Instream position, Content-category exclusions, Device type, Mobile environment.

**Critical design note from the client:** *"This targeting list frequently changes so it should be easy to add new targeting types."* — the implementation must be **config-driven, not hard-coded.**

**Not supported by VOW today (future scope):** genre exclusions, day-parting, language.

**Constraints for CTV (as stated in v2.0):**
- ~~Amazon audiences only apply to Amazon-owned inventory. For Netflix/Disney, their own targeting applies~~ → **corrected by Review Note 19**
- ❌ Product audiences not applicable to CTV (removed)
- AMC audiences are conditional — only when the advertiser has prior campaign data
- Nobody browses — the agent uses `POST /api/audience-sets/suggest/` exclusively
- The audience set does not need to be created before forecasting — it's created later at strategy creation via a simplified CTV endpoint

---

## 📋 REVIEW NOTE 19 — Amazon audiences do apply to 3P inventory

**David's comment:** *"can use amazon audiences too"*

The constraint read: *"Amazon audiences **only apply to Amazon-owned inventory**. For Netflix/Disney, their own targeting applies."* **That is wrong.**

This is the **same absolute statement corrected in Review Note 1**, in its second location — Note 1 flagged that it appeared here too, and David has now commented on it directly.

### It also corrects part of Note 1

Note 1 explained the limitation by asserting that 3P publishers do not pass viewer identity, so Amazon *cannot* apply audience segments — only device-level targeting. **That explanation over-claimed.** David's original wording was *"may be limited"*, not "is limited", and this comment confirms **Amazon audiences do work on 3P inventory.** The constraint is a matter of degree set by the deal and provider, not a technical barrier.

### Corrected picture for 3P inventory

| | **Amazon audiences** | **SSP / publisher targeting** |
|---|---|---|
| Available on 3P | ✅ **Yes** | ✅ Yes |
| Capability | ⚠ *May be* limited by deal/provider | Fuller, publisher-specific |
| Cost | **Amazon 1P data fee applies** | Adds CPM |
| When chosen | At this step | 🔴 Bound to the deal (Note 1) |

### Consequence 1 — the tier table's Audiences column stops being a differentiator

If Amazon audiences apply across all tiers, what actually distinguishes them is **whether reach can be forecast** and **whether the deal is selectable now**. The §2.3 table has been updated accordingly.

### Consequence 2 — the effective-CPM model widens

Note 2 established that the fee follows the **data source**. Since Amazon audiences can be applied to the 3P portion, **the Amazon 1P data fee can apply there too** — which neither the document nor Note 2's example allowed for. The agent now has **three** configurations to compare, not two:

```
Prime £6,000 @ £28.88 · Netflix £4,000 @ £32.00 · Amazon 1P fee £1.85
Netflix SSP targeting uplift £2.50 (illustrative)

1. No audience anywhere
   Prime   £28.88 → 207,756      Netflix £32.00 → 125,000
   Total 332,756 · data fee £0
   → cheapest and highest reach (see Note 4)

2. Amazon audiences on both portions          ← newly possible
   Prime   £30.73 → 195,249      Netflix £33.85 → 118,168
   Total 313,417 · fee charged on both
   → ⚠ capability on Netflix may be limited

3. Amazon audiences on Prime, SSP targeting on Netflix
   Prime   £30.73 → 195,249      Netflix £34.50 → 115,942
   Total 311,191 · two different upliftsated
```

### Consequence 3 — a nuance for the repair loop

The audience can now be widened on the 3P portion as well — but the effect **cannot be verified**, since 3P still reports no reach. The lever list itself (Note 12) is unchanged, but the agent must say so rather than imply improvement:

*"I've widened the Netflix audience too, but I can't confirm the effect — Netflix doesn't report reach."*

### Schema addition

```python
# SelectedAudienceSetSchema
applies_to_providers: list[str] = Field(default_factory=list,
    description="Which inventory portions this audience is applied to")
```

> **⚠ OPEN QUESTIONS arising**
> 1. Can Amazon audiences **and** SSP targeting both apply to the same 3P deal, or is it one or the other?
> 2. Does the same hold for **AMC audiences** — the constraint above describes them as conditional?
> 3. How limited is Amazon's targeting on 3P exactly, and does it vary by provider?

---

## 📋 REVIEW NOTE 20 — ✅ RESOLVED: the `bundles` response shape does not exist

**David's comment on the open question below:** *"not currently supported"*

v2.0 raised this itself: *"the suggest endpoint's response shape. v1.1.0 assumed it returns `bundles.narrow/balanced/broad`. The real endpoint may return a flat list that we group ourselves. Confirm against the real API."*

**The assumption carried from v1.1.0 was wrong. The API does not return pre-grouped bundles.**

> This is what flagging rather than assuming was for. Had the shape been taken as fact, the schema would have been built around `bundles`, code written against it, and the mismatch found at integration — with the audience module needing a rewrite.

### The significant consequence: the three profiles are an agent-side construct

Narrow / Balanced / Wide are **built by the agent** from whatever the endpoint returns. They are a presentation device, and **the grouping logic is our responsibility** — the document never covered it because the API was assumed to handle it.

### Bundle construction (agent-side) — three decisions

| Decision | Options | Recommendation |
|---|---|---|
| **Grouping basis** | Relevance score · cumulative reach · data source | **Cumulative reach** — after Note 2, reach is the only real differentiator between profiles |
| **Nested or independent** | `balanced ⊇ narrow ⊇ …`, or separate sets | **Nested**, as v2.0's example showed — easier to explain: *"Balanced includes Narrow plus one more"* |
| **Segments per profile** | Fixed 1 / 2 / 3 · or as many as needed to reach a target | **Reach target** — segment sizes vary by brief, so a fixed count gives inconsistent results |

**Illustrative:** given a flat list ordered by relevance, the agent accumulates segments until each profile's reach target is met — roughly ~500K for Narrow, ~1.5M for Balanced, ~5M for Wide, scaled to the market.

### Schema addition

```python
class AudienceBundleConstructionSchema(BaseModel):
    """➕ NEW — how the agent builds the three profiles from a flat API response"""
    grouping_basis: str = Field("cumulative_reach",
        description="cumulative_reach | relevance_score | data_source")
    is_nested: bool = True
    reach_targets: dict[str, int] = Field(default_factory=dict)
    # {"NARROW": 500_000, "BALANCED": 1_500_000, "WIDE": 5_000_000}
```

### Corrections required

- Mark the open question below **resolved**
- **§4.2's `bundles` example is incorrect** and must be removed or clearly marked as such
- Change the `Audience options` source to **🤖 GENERATED (agent-side grouping)**
- The `bundles.broad` vs `WIDE` inconsistency noted in §2.4 no longer applies

> ### 🔴 ⚠ NEW BLOCKING QUESTION — what does the endpoint actually return?
>
> This closes one question and opens a more urgent one. Knowing the `bundles` shape is wrong does not tell us the right shape, and **three things are blocked until we have it**: the grouping logic (group on which field?), the effective-CPM calculation (Note 2's question about the per-segment `vcpm`), and finalising the schema.
>
> **The ask is a single real response sample from `POST /api/audience-sets/suggest/`.** That one artefact answers this and Note 2's question together.
>
> Also worth knowing: *"not **currently** supported"* suggests bundles may be added later. If so, the agent-side grouping is a workaround that can move server-side, and should be written so it can be swapped out.

~~⚠ **Open question:** the suggest endpoint's response shape. v1.1.0 assumed it returns `bundles.narrow/balanced/broad`. The real endpoint may return a flat list that we group ourselves. Confirm against the real API.~~ → **✅ RESOLVED above.**

---

## 📋 REVIEW NOTE 4 — Audiences are optional, not mandatory

**David's comment:** *"optional again"*

v2.0 changed audiences from optional (v1.1.0) to **mandatory**. **That change was wrong** — audiences are **optional**. v1.1.0 was correct on this point.

**"Suggestion-driven" stays correct** — nobody browses ~3,400 segments, so the agent suggests. But **suggesting is not the same as requiring.** Those two ideas were conflated.

### Why "no audience" is a legitimate — often preferable — option

| | With an Amazon audience | With no audience |
|---|---|---|
| Reach | Capped at the segment size | **Maximum** — the full available deal inventory |
| Data fee | £1.85 (per Note 2) | **£0.00** — no audience data used |
| Effective CPM | £30.73 | **£28.88** — the deal CPM, nothing added |
| Impressions on £10,000 | 325,415 | **346,260** |

For an **Awareness-only** module — which this is — maximum reach at lowest cost is frequently the right answer. Making audiences mandatory removed the cheapest, highest-reach option from the flow.

**Corrected:** Audience options → **Optional**. Chosen option → **Optional**. The constraint *"At least one audience set must be selected"* is removed. §8's summary entry *"audiences mandatory"* is removed.

**What is retained:** the pgvector suggestion engine and the Narrow / Balanced / Wide options remain — they become **opt-in** rather than a gate. A trader who chooses an audience now does so deliberately.

> Note: `audience_options` in §5 was **already optional** (`Field(default_factory=list)`). Only the prose and the field table said mandatory. The schema was right.

---

## 📋 REVIEW NOTE 5 — Audiences are part of targeting; default-then-refine

**David's comment:**
> *"I would treat audiences as part of targeting. So once inventory decided / inferred then you are shown the default targeting applied / suggested like country targeting and Connected TV (CTV) device only and then you could refine this, define the audience segments or accept it as sufficient. Example: the user wants to use only postcodes instead of audiences for targeting"*

Three changes follow.

### 1. Audiences merge into Targeting

Both answer the same question — **who sees this ad.** Splitting them into two steps confused the trader and duplicated the interaction. Audience segments become **one targeting type** alongside location, device, content exclusions and the rest.

This also satisfies the client's earlier requirement that targeting be **config-driven and easy to extend** — with audiences inside the same registry, one mechanism covers all of it.

### 2. A default is applied automatically, then refined

Once inventory is decided or inferred, the agent **shows a default that is already applied**, derived from what is already known:

| Default applied | Derived from |
|---|---|
| Country targeting | `markets` (Step 1) |
| Connected TV device only | CTV format (Step 1) |
| No audience | nothing selected — the deal's full inventory |

The trader then either **refines** it (add audience segments, add postcodes, add exclusions…) or **accepts it as sufficient** and moves on.

**This follows this document's own Principle 2 better than the previous design did.** The old Step 5 presented five empty fields; this pre-fills what is already known.

### 3. Audience and location targeting are alternatives, not a sequence

Per David's example, a trader may want *"only postcodes instead of audiences"* — a complete and valid targeting strategy on its own. The previous mandatory-audience design made that impossible.

### What this looks like in conversation

```
Agent: "Inventory is set. Here's the targeting I've applied:

        ✓ Country    United Kingdom (GB)
        ✓ Device     Connected TV only
        ✓ Audience   None — the deal's full inventory

        Effective CPM £28.88 (the deal CPM — no audience data fee)
        Estimated impressions 346,260

        Your KPI is reach, and this setup gives maximum reach at the
        lowest cost. You can refine it if you want:
          • Audience segments — I'll suggest three options
            (adds a data fee and reduces reach)
          • Locations or postcodes
          • Content exclusions
          • Instream position, mobile environment

        Or just say it's fine and I'll move to the forecast."
```

### Flow consequences

- **Steps 4 and 5 collapse into one** — 13 steps becomes 12
- **The repair loop becomes conditional** — if no audience is applied, *"widen the audience"* has nothing to widen. The agent must relax other targeting instead, or state that reach is bound by the inventory. *(See Note 12 for the rewritten lever list.)*
- **The `TargetingSchema` must genuinely be config-driven.** Its docstring says *"config-driven, extensible"* but the model hard-codes five fields — which does not satisfy the client's requirement:

```python
# Was — hard-coded despite the docstring
class TargetingSchema(BaseModel):
    """➕ NEW — CTV targeting options (config-driven, extensible)"""
    locations: list[str] = Field(default_factory=list)
    instream_positions: list[str] = Field(default_factory=list)
    content_category_exclusions: list[str] = Field(default_factory=list)
    device_types: list[str] = Field(default_factory=list)
    mobile_environments: list[str] = Field(default_factory=list)

# Now — keys validated against a targeting-type registry at runtime
class TargetingSchema(BaseModel):
    """Config-driven targeting. Audience segments are one targeting type.
       Keys are validated against the targeting-type registry, not hard-coded."""
    selections: dict[str, list[str]] = Field(default_factory=dict)
    # {"locations": ["SW1","SW3"], "device_types": ["Connected TV"],
    #  "audience_segments": ["aud_101","aud_102"]}
    defaults_applied: list[str] = Field(default_factory=list)
    accepted_as_default: bool = False
```

Adding a new targeting type then becomes a **configuration change, not a code change** — which is what the client asked for.

> **⚠ OPEN QUESTIONS arising**
> 1. Should Targeting sit **before** Budget split? David's wording suggests it comes straight after inventory, and it is also logically necessary — the audience data fee is an input to the accurate CPM the split is meant to produce.
> 2. Does `GET /api/strategies/locations/{market}/` support **postcodes**, or only cities and regions? The postcode example depends on it.
> 3. If no audience is applied, which targeting should the repair loop relax first?

---

## 📋 REVIEW NOTE 21 — Location defaults to the market country

**David's comment:** *"defaults to market country"*

`Location` is marked **Optional**, implying it is empty unless the trader fills it. It **defaults to the market country.** Requirement stays Optional; **Source becomes ⚙️ DERIVED from `markets`.**

This is the field-level confirmation of Note 5's default-then-refine model, where David described the default as *"country targeting and Connected TV (CTV) device only."* It is also the **fifth field** whose Requirement was right and whose Source was missing.

### A distinction the document has never stated

`markets` and `location` can both hold `"GB"` but do different jobs:

| | `markets` (Basics) | `location` (Targeting) |
|---|---|---|
| What it is | **Buying scope** — whose inventory, deals, rate card, audiences and currency | **Delivery filter** — where the ad may be shown |
| Default relationship | — | Defaults to the same country |
| Can they diverge? | — | ✅ Yes — buy GB inventory, deliver only to London |

Without this stated, the two read as duplication.

### Location is a hierarchy, and the default sits at the top

```
Country    GB                     ← 🟢 default, derived from markets
Region     England, Scotland
City       London, Manchester
Postcode   SW1, SW3, W1, W8       ← David's example in Note 5
```

Narrowing reduces available inventory, so the agent should state the effect when the trader refines downward.

### The Targeting step's complete default set

Notes 4, 5, 19, 20 and 21 together define what is applied before the trader touches anything:

| Targeting type | Default applied | Requirement | Source |
|---|---|---|---|
| **Location** | ✅ Market country (GB) | Optional | ⚙️ **DERIVED** from `markets` — Note 21 |
| **Device type** | ✅ The advertiser's setting *(often Connected TV only)* | Optional | 🏢 **ADVERTISER** — Note 22 · fallback Connected TV only · ⚠ **may be locked** |
| **Audience segments** | ✅ None | Optional | 🤖 Agent suggests three options on request — Notes 4, 20. *Applies to 3P too — Note 19* |
| **Content exclusions** | 🟡 Advertiser brand-safety rules? | Optional | 🏢 **ADVERTISER** default — *to confirm; more likely after Note 22* |
| **Instream position** | ❌ None | Optional | 💬 ASKED |
| **Mobile environment** | ❌ None | **Conditional** — only if `Mobile` ∈ device types | 💬 ASKED — Note 22 |
| ➕ **Targeting source** (3P only) | 🟡 Amazon audiences? | Optional | 💬 ASKED — Notes 1, 19 |

**Two defaults apply automatically; nothing is asked-and-required.** The trader accepts or refines — **except where an advertiser setting is locked** (see Note 22).

```python
# TargetingSchema
defaults_applied: list[str] = Field(default_factory=list)
# ["location:market_country", "device_types:connected_tv"]
```

> **⚠ To confirm:** (a) does `GET /api/strategies/locations/{market}/` support **postcodes**, or only cities and regions? *(Raised in Note 5, still open — David's own example depends on it.)* (b) Should **content exclusions** default from the advertiser's brand-safety rules, the way frequency cap does?

---

## 📋 REVIEW NOTE 22 — Device type comes from the advertiser, and may be a policy rather than a default

**David's comment:** *"Some advertisers only want CTV only - set at advertiser level"*

`Device type` is marked **Optional**, implying it is empty unless the trader fills it. It comes from the **advertiser record**, and for some advertisers it restricts delivery to Connected TV only.

### This is the third confirmation of advertiser-level defaults

| Note | Field | David's wording |
|---|---|---|
| 13 | Frequency cap | *"we have a default per advertiser"* |
| 15 | Product categories | *"we have a default on the advertiser"* |
| **22** | **Device type** | *"set at advertiser level"* |

Three explicit confirmations make `AdvertiserDefaultsSchema` a firm requirement, not a suggestion. The document still contains no advertiser-settings schema, endpoint, state field or even a mention.

### ⚠ CORRECTION to Review Note 21

Note 21's default table listed **Device type** as **🔒 FIXED — CTV module**, on the assumption that a CTV module implies Connected TV delivery. **That was wrong.** David's *"**some** advertisers"* means it varies by advertiser — so the source is **🏢 ADVERTISER**, not a constant. The distinction matters: a fixed value cannot be changed; an advertiser value can be, subject to policy.

### 🔴 The underlying conceptual fix: "CTV" as a format is not "CTV" as a device

The document has conflated two different things:

| | **Format** | **Device** |
|---|---|---|
| Value | `streaming_tv` | `Connected TV` |
| What it means | The **content type** — streaming video inventory | The **screen** the ad is delivered to |
| Decided at | Step 1 — always `streaming_tv` (Note 14) | Here — varies by advertiser (this note) |

Streaming TV inventory can be delivered to a **Connected TV, a phone, a tablet or a desktop browser** — the Prime Video and Netflix apps run on all of them. So `formats = ["streaming_tv"]` does **not** imply Connected TV delivery, and the device filter is neither redundant nor derivable from the format.

**The document already proves this to itself:** this step includes a **`Mobile environment`** field (in-app vs mobile web). That field would be meaningless if delivery were restricted to Connected TV by definition. Its existence establishes that mobile delivery is possible — the format-vs-device distinction was simply never written down.

### Why an advertiser would restrict to Connected TV

| Reason | |
|---|---|
| **Brand positioning** | A premium brand wants the big screen, not a phone |
| **Creative quality** | A 4K TV asset looks poor on a small screen |
| **Attention and viewability** | CTV completion rates are materially higher; mobile video is often muted or skipped |
| **Measurement consistency** | Mixing devices complicates reporting |
| **Client contract** | The media plan sold to the client says CTV |

### Consequences

**Reach and CPM — and the trader did not choose this.** A large share of Prime Video viewing is on mobile, so restricting to Connected TV materially reduces available inventory (lower reach), while Connected TV inventory is typically **more expensive** (higher CPM, fewer impressions). The agent should surface both effects rather than applying the setting silently.

**🔴 The repair loop's primary lever may be locked.** Note 12's rewritten lever list puts *"relax other targeting — device, location, content exclusions"* **first**, precisely because audiences became optional and the bid lever turned out not to work on fixed-CPM deals. **If device type is an advertiser policy, the agent cannot relax it.** The worst case is now:

```
No audience selected            (Note 4)   → levers 2 and 3 unavailable
Preferred fixed-CPM deal        (Note 12)  → the bid lever does nothing
Advertiser policy: CTV only     (Note 22)  → 🔒 the primary lever is locked

Remaining: location, content exclusions, add inventory,
           extend flight dates, increase budget
```

The lever list needs a **"can this be locked?"** column — see the revised list in Step 5.

### 🔴 A new distinction the schema needs: default vs constraint

Advertiser-level values are not all the same kind of thing:

| | 🏢 **Advertiser default** | 🔒 **Advertiser constraint** |
|---|---|---|
| Pre-filled | ✅ | ✅ |
| Trader can override | ✅ Yes | ❌ No — it is brand policy |
| Repair loop can relax it | ✅ Yes | ❌ No |
| Example | Frequency cap (Note 13) | Device policy — *"CTV only"* |

```python
class AdvertiserSetting(BaseModel):
    """➕ NEW — an advertiser-level value plus whether it can be overridden"""
    value: Any
    is_locked: bool = Field(False,
        description="True = brand policy; the trader cannot override and "
                    "the repair loop cannot relax it")
    reason: Optional[str] = Field(None,
        description="Shown to the trader when locked, e.g. 'brand policy: CTV only'")
```

Every field in `AdvertiserDefaultsSchema` is wrapped in this. **The agent must know which values it is allowed to touch — and must tell the trader when it is not.**

### What this looks like in conversation

```
Agent: "Inventory is set. Here's the targeting applied:

        ✓  Country    United Kingdom (GB)     — derived from market
        🔒 Device     Connected TV only       — BrightPath brand policy
        ✓  Audience   None

        Effective CPM £28.88 · Estimated impressions 346,260

        Note on the device setting: BrightPath's account restricts delivery
        to Connected TV, so the ad won't run on phones or tablets. That
        reduces available inventory and pushes the CPM up slightly, but
        keeps the brand on the big screen.

        This is an account-level policy — I can't change it for this
        campaign. It would need changing in the advertiser settings.

        Anything else to refine, or shall I move on?"
```

And during repair:

```
Agent: "Reach came back low at 68,000. I tried:
          ✅ Widened location to all of the UK (was London only)
          ✅ Removed two content exclusions
          🔒 Could not relax device — 'Connected TV only' is an
             advertiser policy, so it's outside what I can change

        Reach is now 94,000. To go further you'd need to increase the
        budget, add inventory, or have the device policy relaxed in the
        account settings."
```

### A dependency the document does not state

**`Mobile environment` is conditional on `Device type`.** If `Mobile` is not among the selected device types, in-app vs mobile web is meaningless. Its requirement is **Conditional**, not Optional — corrected in the default table above.

> **⚠ OPEN QUESTIONS arising**
> 1. 🔴 **Is the advertiser device setting a default (overridable) or a constraint (locked)?** This determines whether the repair loop can touch it.
> 2. Should **content exclusions** also come from the advertiser? Brand-safety rules normally sit at brand level, and this comment makes that more likely.
> 3. What is the fallback when an advertiser has no device setting — Connected TV only, or all devices?
> 4. Which other advertiser settings can be **locked** rather than merely defaulted?

---

# Step 4: Budget Split

➕ **ENTIRELY NEW** — did not exist in v1.1.0. Added per client requirement: *"We will need to support the suggested budget split across inventories or creative durations."*

The agent proposes how the total budget is divided across inventories (Prime / Netflix / Disney) and across creative durations (15s / 30s). This is genuinely hard — different durations have different CPMs, and there is no reach data for Netflix/Disney to optimise against.

**Split method options:**
- `EVEN_BY_BUDGET` — same £ per inventory/duration; uneven impressions (higher CPM = fewer impressions)
- `EVEN_BY_IMPRESSIONS` — same impression count; uneven £ (higher CPM = more spend)
- `CUSTOM` — the trader specifies percentages

The agent must state which it chose and why, so the trader can adjust. Example: *"I've split evenly by impressions, which weights spend toward the 30s at its higher CPM."*

**No API call** — this is agent-side logic. The resulting budgets feed into the `market_budgets` field at strategy creation.

## 📋 REVIEW NOTE 3 — Budget split is optional

**David's comment:** *"is optional but to give an accurate CPM is preferred"*

The field matrix marked the splits as *"Required when multiple inventories/durations selected"*. **Both are optional.** They are **preferred**, because without a split an accurate CPM cannot be given.

### Why the split drives CPM accuracy

With four lines at £20.00, £24.00, £31.50 and £32.00, the blended CPM depends entirely on how the money is distributed:

```
With a split:
  Prime 15s    £2,340 ÷ £20.00 × 1000 = 117,000 impressions
  Prime 30s    £3,660 ÷ £31.50 × 1000 = 116,190 impressions
  Netflix 30s  £4,000 ÷ £32.00 × 1000 = 125,000 impressions
  → 358,190 impressions — accurate, because each line's CPM is known

Without a split:
  → Allocation happens at runtime on the DSP side
  → The effective CPM cannot be stated in advance
  → Only a range (£20–£32) or a blended estimate is possible
```

**Corrected:** both split fields → **Optional**.

> Note: `budget_split: Optional[BudgetSplitSchema] = None` in §5 was **already optional**. Only this table said Required. The schema was right.

**Agent behaviour:** propose the split as before, state the method and why (unchanged), **and offer to skip it** — while stating the consequence: *"Without a split I can't give you an accurate CPM; the forecast will be an estimate only."*

> **⚠ OPEN QUESTIONS —**
> 1. Without a split, how does Amazon DSP allocate — by any stated rule, or purely auction-driven?
> 2. If multi-market is in scope, `BudgetSplitSchema` needs a **`by_market`** dimension (see Note 8).

---

# Step 5: Predict Reach

🔄 **CHANGED** — was embedded in the original flow. Now a first-class step with the tier-based honesty rule.

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Reach curve | Chart | Read-only **(Amazon only)** | 🔄 CHANGED. Only available for Amazon-owned inventory. For 3P, state honestly that reach is unavailable |
| Estimated impressions | Number | Read-only | ✅ Unchanged |
| Estimated unique reach | Number | Read-only **(Amazon only)** | 🔄 CHANGED. Not available for Netflix/Disney |
| Average frequency | Number | Read-only **(Amazon only)** | 🔄 CHANGED. Not available for Netflix/Disney |
| Indicative CPM | Number | Read-only | ✅ Unchanged |

➕ **NEW — the honesty rule for 3P inventory.** For Netflix/Disney, the agent shows rate-card CPM and derived impressions (budget ÷ CPM × 1,000). It explicitly states that reach is unavailable and why. **Never invent a reach number.**

➕ **NEW — consequences:**
- The repair loop applies only to the Amazon portion
- Total reach cannot be summed across providers (no cross-platform deduplication)

**API calls at this step:** `POST /api/audience-sets/reach-forecast/` (or the simplified CTV endpoint, name TBC)

## 📋 REVIEW NOTE — The repair loop is rewritten (from Notes 4, 5 and 12)

The repair loop as written had three actions, **two of which no longer hold:**

| Original action | Status after review |
|---|---|
| 1. Switch/extend the audience bundle | ⚠ **Conditional** — audiences are optional (Note 4), so there may be no audience to widen |
| 2. Adjust base CPM bid upward (£15 → £30) | ❌ **Invalid for CTV** — the CPM is fixed by the deal (Note 12) |
| 3. Re-run the forecast | 🟡 Not an action — a re-check |

In the worst case — no audience selected, Preferred (fixed-CPM) deal — the loop had **nothing to do.**

### The rewritten, ordered lever list

| # | Lever | Applies when | Can it be locked? |
|---|---|---|---|
| 1 | **Relax other targeting** — location, content exclusions, device | Always — *the primary lever now* | 🔒 **Yes** — device and content exclusions may be advertiser policy (Note 22) |
| 2 | **Extend the audience** — add segments within the chosen profile | An audience is applied | No |
| 3 | **Switch matching mode** Exact → Similar | An audience is applied | No |
| 4 | **Add inventory** — more deals / providers | Always | 🟡 Possibly — an advertiser may restrict providers |
| 5 | **Extend flight dates** | Always | No |
| 6 | **Increase budget** | Requires the trader | No |
| 7 | **State the limit honestly** — *"this deal's inventory cannot deliver more reach than X"* | When nothing above helps | — |

> **🔒 The "can it be locked?" column matters.** Note 22 establishes that some targeting values are advertiser **policy**, not defaults — the agent cannot relax them. In the worst case (no audience, a fixed-CPM Preferred deal, and a locked device policy) the primary lever is unavailable and only levers 4–7 remain. When that happens the agent must **say which lever it could not use and why**, rather than reporting a weaker result without explanation.

**This changes the graph** — the number and shape of repair edges is different from what §6 currently shows, and some edges are now conditional on advertiser policy.

**Also implementable for the first time:** the frequency check. §6.2's *"frequency within targets"* and §7.1's *"insufficient frequency"* now have a field to compare against — `kpi_target_value` (Note 10).

> **⚠ OPEN QUESTION —** how far below target counts as *"insufficient frequency"*?

## 📋 REVIEW NOTE — Reach can be summed across markets, but not across platforms

Two superficially similar cases with opposite answers, and both should be stated explicitly:

| | Can reach be summed? | Why |
|---|---|---|
| **Across platforms** (Prime + Netflix) | ❌ **No** | The same person may view on both — no cross-platform deduplication exists |
| **Across markets** (GB + FR) | ✅ **Yes** | A GB viewer and an FR viewer are different people — no deduplication problem |

*(Raised by Note 8.)*

---

# Step 6: Finalise Plan

*(was "Plan Approval" — see Review Note 23)*

➕ **ENTIRELY NEW** — did not exist in v1.1.0.
🔄 **SIMPLIFIED** since v2.0 was written — manager approval deferred.

The trader reviews the plan and **marks it finalised.** Nothing is spent yet; spend begins only at activation.

| Field | Data type | Requirement | Source |
|---|---|---|---|
| **Plan status** | `PlanStatusEnum` — `DRAFT` → `FINALISED` | Required | 💬 ASKED — the trader confirms |
| **Finalised by** | `str` (user) | Set on finalise | 🔌 Session — the trader |
| **Finalised at** | timestamp | Set on finalise | 🔌 System |

**Removed (for now):** `Manager required` · `Rejection reason` · the `PENDING`/`APPROVED`/`REJECTED` states.

**Implementation:** a normal conversational turn — **no `interrupt()` needed** (see Review Note 23). Session state persists via the checkpointer regardless. The node is kept distinct so manager routing can be reinstated later without restructuring the graph.

**No API call** — agent-internal. `finalised_by` and `finalised_at` are recorded in state.

---

## 📋 REVIEW NOTE 23 — Plan approval simplified to a status change; manager routing deferred

**David's comment:** *"we simplified this so it's just a status changed to finalise the plan - no manager approval required for now"*

> 🔵 **This is not a correction — it is a design change made after v2.0 was written.** The approval workflow previously described here reflects what the client had confirmed at the time; the team has since simplified it. The document was not wrong; it had gone out of date.

### What the step becomes

| | **Was** | **Now** |
|---|---|---|
| Step name | Plan Approval | **Finalise Plan** |
| Who acts | Trader submits, optionally a **manager** approves | **The trader**, self-service |
| States | `PENDING` → `APPROVED` \| `REJECTED` | `DRAFT` → `FINALISED` |
| `Manager required` | Configurable, possibly budget-threshold-based | ❌ **Removed for now** |
| `Rejection reason` | Required on reject | ❌ **Removed** — there is no rejection |
| Implementation | LangGraph `interrupt()` — graph stops, awaits an external signal | **A normal conversational turn** |
| On rejection | Return to the Targeting step | ❌ **Edge removed** |

### 🔴 `interrupt()` is no longer needed at this step

`interrupt()` exists to **stop the graph and wait for a signal from outside the conversation.** That was justified when a **manager** — a different person, working from a dashboard — had to approve. With the trader finalising their own plan **from within the conversation**, the signal is just the next message.

**A distinction worth keeping clear**, because the two are often conflated:

| | What it does | When it applies |
|---|---|---|
| **Checkpointer** | Persists session state so a trader can leave and return | **Always** — independent of this change |
| **`interrupt()`** | Stops the graph pending an **external, asynchronous** signal | Only where a genuine external gate exists |

A trader returning two days later to finalise is handled by the **checkpointer**, not by `interrupt()`.

**Consequently, the only genuine `interrupt()` in M1 is platform creative approval (Step 8).** Amazon, Netflix and Disney review independently, on their own timelines, outside the conversation. That is what an interrupt is for. `interrupt()` has not left the design — it has moved to where it belongs.

### Recommendation: remove the mechanism, keep the seam

David's *"for now"* implies manager approval returns later.

| | Effort now | Effort when manager approval returns |
|---|---|---|
| Remove the step entirely | Least | Rebuild the node and its edges — a **structural** change |
| **Keep a distinct node, simplify its mechanism** | Slightly more | Add `interrupt()` and routing to an existing node — a **routing** change |

The second is recommended. Keeping `finalise_plan` as its own node **is** the seam that manager approval slots into later. The enum carries the same intent:

```python
class PlanStatusEnum(str, Enum):
    """➕ NEW — simplified for M1; manager approval deferred"""
    DRAFT = "DRAFT"
    FINALISED = "FINALISED"
    # PENDING_APPROVAL = "PENDING_APPROVAL"   # future — manager routing
    # APPROVED = "APPROVED"                   # future
    # REJECTED = "REJECTED"                   # future
```

`ApprovalStatusEnum` is **retained** — platform creative approval still needs it, since that is a genuine three-way approval.

### ⚠ A control has been deliberately given up, and should be recorded as such

This step previously carried: *"The budget is locked at this moment — nothing launches that a person hasn't approved."*

| | Old model | New model |
|---|---|---|
| Who plans | Trader | Trader |
| Who approves | **A manager** — a second person | **The same trader** |
| Independent check | ✅ Yes | ❌ No |

**The spend gate itself remains** — activation still requires an explicit trader action, so nothing launches accidentally. What has gone is **separation of duties**: the second pair of eyes.

For M1 this is a reasonable trade — small team, contained budgets. It is recorded here so that nobody later assumes a control exists that does not. When budgets grow, *"who approved this £50,000?"* will have the answer *"the person who built it,"* and the manager routing will need reinstating.

### Two loops survive, one disappears

| Loop | Status |
|---|---|
| **Duration mismatch → re-confirm the plan** (Step 7) | ✅ **Survives** — the economics genuinely changed, so the trader must confirm again. *"Re-approval"* becomes *"re-confirmation"* |
| **Budget reduced at credit check → re-confirm** (Step 10) | ✅ **Survives**, same treatment |
| **Plan rejected → return to Targeting** | ❌ **Removed** — there is no rejection. A trader who is not satisfied simply keeps refining and does not finalise |

### ✅ This closes an open question

*"Is the manager-approval threshold per advertiser, global, or per role?"* — **moot for M1**, since there is no manager approval. It returns if the routing does.

### What the step looks like now

```
Agent: "Here's the plan:

        BrightPath_Awareness_GB_Aug2026
        £10,000 · 1–30 Aug 2026 · United Kingdom

        Prime Video   £6,000  →  195,249 impressions · 118,000 reach
        Netflix       £4,000  →  125,000 impressions · reach unavailable

        Total impressions 320,249. Reach can't be summed across
        providers — no cross-platform deduplication.

        Finalise this plan? Nothing has been spent yet — spend only
        begins at activation."

Trader: "Yes, finalise it"

Agent: "✅ Plan finalised — Kareem, 30 Jul 09:35. Creating the strategy."
```

> **⚠ To confirm**
> 1. Are `finalised_by` / `finalised_at` needed for audit, or can they be dropped along with the approval workflow?
> 2. Can a trader **un-finalise** a plan and keep editing? *(Affects whether the loop edges are one-way.)*
> 3. When is manager approval expected back — M2? *(Determines how much scaffolding to leave in place.)*

> ### ⚠ OPEN QUESTION — Where is the audit trail stored?
>
> Less critical now that there is no external approver, but `finalised_by` and `finalised_at` are still worth recording. State persists in the LangGraph checkpointer; whether a durable audit record is needed in the VOW database is unresolved, and **no endpoint exists for it.**

---

# Step 7: Create the Real Strategy

🔄 **CHANGED** — was "Summary & Create" (Step 6) in v1.1.0. Key change: create the **real** strategy, not a draft.

| Field | Change |
|---|---|
| Endpoint | 🔄 `POST /api/strategies/` — **not** `/strategies/draft/`. Client: *"don't need to create draft strategy; draft is just for the wizard creation"* |
| Audience set | ➕ Created at this step via the simplified CTV endpoint (not before forecasting) |
| All slots | All filled slots from earlier steps are assembled into the creation payload |

**API calls at this step:** ⚠ `POST /api/simple-strategies/` *(name to confirm — see Review Note 24)*, audience-set creation via CTV endpoint

## 📋 REVIEW NOTE 24 — The create endpoint is probably `simple-strategies`, and this points at a wider gap

**David's comment:** *"probably more likely simple-strategies endpoint"* (edited)

Noting the hedge — *"probably more likely"*, and the comment was edited — this is a **hint to verify**, not a confirmed correction. It is recorded as an unresolved item rather than applied as fact.

### The document already contained half of this signal

The Targeting step states that the audience set is *"created later at strategy creation via a **simplified CTV endpoint**"*, and this step says *"audience-set creation via **CTV endpoint**"*. So the document already assumed a **CTV-specific endpoint for audiences** — while using the **full wizard-era endpoint for the strategy itself.** That is internally inconsistent, and David's comment suggests both have simplified variants.

### Why a simplified endpoint would exist — and why it matters here

`POST /api/strategies/` was built for the six-step wizard covering all four formats. **The review has progressively removed most of what that payload expects:**

| Removed by | What went |
|---|---|
| Note 6 | `goal` and `kpi` as multi-choice — now fixed and derived |
| Note 12 | `base_bid` — not applicable to CTV |
| Note 14 | `formats` as a four-way choice — always `streaming_tv` |
| Note 16 | `product_location` — moves to the advertiser record |
| Note 17 | `product_asins` — collected later |
| Note 23 | The approval workflow |
| Note 25 | `click_through_url` — now optional |

**The payload has been shrinking with every comment — and an endpoint apparently already exists built for exactly that reduced shape.**

### ⚠ This weakens the evidence in Review Note 17

Note 17 resolved the ASIN-timing open question and cited §4.2's create payload — `"product_asins": []` — as proof that creating without ASINs works. **That example is for `POST /api/strategies/`.** If the CTV path uses `simple-strategies`, the example does not apply.

**The conclusion still stands** — it came from David's own comments — but the supporting evidence needs re-verifying against the correct endpoint. The answer is right; the justification was for the wrong endpoint.

### 🔴 This escalates the API-verification problem

Previously the concern was that §4.2's **response shapes** were assumptions. It now extends to **endpoint names**:

| Endpoint | Status |
|---|---|
| `POST /audience-sets/suggest/` | ❌ Response shape confirmed wrong (Note 20) |
| `POST /api/strategies/` | ⚠ **The endpoint itself may be wrong** (this note) |
| Audience-set creation | ⚠ *"simplified CTV endpoint, name TBC"* — never named |
| `PATCH /api/strategies/{id}/` | ❌ Not in the catalogue at all (Note 17) |
| Reach forecast | ⚠ Two listed plus a third "TBC" — which applies when is unstated |
| The nine v2.0 endpoints | ❌ No specifications |

**§4 should be treated as a set of assumptions, not a contract.**

> ### ⚠ THE QUESTION TO ASK IS BIGGER THAN ONE ENDPOINT
>
> **Is there a CTV-specific endpoint family in VOW, and what is in it?** One answer resolves six of the items above. Also to confirm: is it `/api/simple-strategies/` or `/api/strategies/simple/`, and what payload does it accept?

> ### 📋 REVIEW NOTE — The payload changes, per Notes 12, 14 and 17
>
> | Field | Was | Now |
> |---|---|---|
> | `formats` | `["prime_video"]` | **`["streaming_tv"]`** — a constant (Note 14) |
> | `base_bid` | Required per market | **Omitted / `null`** — not applicable to CTV (Note 12) |
> | `product_asins` | Collected at Step 1 | **`[]`** at create; patched at Tracking setup (Note 17) |
> | `product_location` | Collected at Step 1 | **From the advertiser record** (Note 16) |
> | `kpi_target_value` | *(did not exist)* | ➕ **Included when KPI = frequency** (Note 10) |
>
> **A new endpoint is required:** `PATCH /api/strategies/{id}/`, to attach ASINs at the Tracking step. It is not in §4.

> ### ⚠ OPEN QUESTION — What status does the created strategy land in?
>
> Unresolved from v2.0, and the document contradicts itself: `FullStrategySchema` sets `status: str = Field("created")` while §4.2's response example returns `"status": "draft"`.
>
> Two different things are being conflated — the **draft endpoint** (removed, per client) and the **draft status** (a field value, which the client did not comment on).
>
> **Recommendation:** `created` after this step, `active` after `set_status`. That keeps "created but not spending" and "active and spending" clearly distinct. **To confirm**, and the §4.2 example should be corrected either way.

---

# Step 8: Upload Video Creative

🔄 **CHANGED** — was Step 5 "Creatives" in v1.1.0. Simplified to video only, moved to after plan approval, and duration check added.

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Video file | Upload (direct or URL) | Required | 🔄 CHANGED. For CTV, always video. No display creatives, no pre-approved selection, no responsive e-commerce |
| Click-through URL | URL | **Optional** | 🔄 **CHANGED — optional for streaming TV** (see Review Note 25) |
| Duration | Derived from file | Checked | ➕ NEW. Must match one of the durations in the approved plan |

➕ **NEW — Duration match check.** If the uploaded video is 30s but the approved plan specified 15s deals, the economics change (different CPM → different impressions for the same budget). This triggers **re-approval** (return to Plan approval with the amended plan).

**Upload path:** `POST /api/assets/amz_assets/gen_upload_urls/` → `POST /api/assets/amz_assets/register/`

❌ **REMOVED for CTV:** browse existing assets (`GET /api/assets/`), pre-approved creatives (`GET /api/creatives/`), responsive e-commerce (`POST /api/creatives/recs/`), third-party tags (`POST /api/creatives/third-party/`). These are valid for Display but not for CTV scope.

## 📋 REVIEW NOTE 25 — ✅ Click-through URL is optional for streaming TV

**David's comment:** *"optional for streaming tv"*

**This closes a gap this revision had flagged as unresolved:**

> *"Click-through URL is Required, unexplained. CTV has no click. The field is ✅ UNCHANGED from v1.1.0 where Display was in scope. Either Amazon DSP mandates it even for CTV (in which case say so), **or it should be Optional for CTV**."*

**The second reading was correct.**

### Why

There is no click on a television — no cursor, no tap. A click-through URL has no mechanism to act on for the great majority of CTV delivery. It may still matter in narrow cases (interactive overlays, QR codes, reporting consistency) but it cannot be required.

**This is another v1.1.0 leftover**, in the same class as `base_bid` (Note 12), the four-way `formats` choice (Note 14) and *"Required for video"* (Note 15): fields that made sense when Display was in scope and do not now.

### Requirement is conditional on format

| Format | Click-through URL |
|---|---|
| `streaming_tv` | **Optional** |
| `display` | Required — *but out of scope* |

Since the format is always `streaming_tv` (Note 14), it is **effectively always optional in M1**.

### Agent behaviour: do not ask, but accept

Consistent with Notes 6, 7, 9, 13 and 21 — do not ask for something that is not needed. The agent should not prompt for a click-through URL; if the trader volunteers one, it is accepted.

### Schema change

```python
# SelectedCreativeSchema
click_through_url: Optional[HttpUrl] = Field(
    None, description="Optional for streaming TV — no click mechanism on CTV")
```

The `"click_through_url"` value in §4.2's create payload example remains valid as an example, but the field itself is optional.

> ### ⚠ TWO ITEMS STILL FLAGGED HERE
>
> One of the three items previously flagged at this step is now resolved (above). Two remain:
>
> 1. **The API catalogue contradicts this step.** `GET /api/assets/` and `GET /api/creatives/` are marked ✅ Unchanged in §4 but ❌ REMOVED here. §4 needs correcting.
> 2. **Multiple durations, partial upload is not covered.** If the plan has both 15s and 30s budget and only the 30s creative is uploaded, the 15s portion cannot deliver. The document does not say what the agent should do.

---

# Step 9: Platform Creative Approval

➕ **ENTIRELY NEW** — did not exist in v1.1.0.

| Field | Data type | Requirement | Source |
|---|---|---|---|
| **Approval status per channel** | `dict[str, ApprovalStatusEnum]` | Read-only | ⚙️ **DERIVED** — keys come from the channels in the plan (see Review Note 26) |

Values per channel: `PENDING` → `APPROVED` or `REJECTED`

Every video must pass each channel's content and technical review before it can run. **Each channel reviews its own inventory independently.** A plan can be fully finalised and funded and still not launch until the creative clears.

**On rejection:** the agent reports the reason and asks for a replacement (return to Upload video creative).

## 📋 REVIEW NOTE 26 — One status per channel, and the channel list is open

**David's comment:** *"It's just a single status for each channel not necessary netflix or disney - could be paramount or channel 4"*

Two things — one confirmed, one corrected.

### ✅ Confirmed: one status per channel

This validates the fix this revision had already proposed at this step. `FullStrategySchema.creative_approval_status` was a single value while the table specified three; the proposed replacement was a **dictionary keyed by channel**. David's *"a single status for each channel"* is exactly that.

### 🔄 Corrected: the channel list is not Amazon / Netflix / Disney

The table hard-coded three channels. **The real list is open** — Paramount+, Channel 4, ITVX, Sky, Hulu and others.

**The document was inconsistent with itself here:** §2.3's tier table says *"Netflix, Hulu, **others**"*, while this step named exactly three. The tier table was right.

### The keys are derived, not declared

```python
creative_approval_statuses: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
# keys derived from selected_deals[].channel
# {"Prime Video": "APPROVED", "Netflix": "PENDING"}
```

A dictionary satisfies both requirements at once — independent per-channel statuses **and** an open channel list. An enum could do neither.

It also **removes the *"(if Netflix inventory)"* qualifiers**: the dictionary contains only the channels actually in the plan, so the condition is expressed by the data rather than by a note. And it supports **partial delivery** — the Prime Video portion can run while Netflix is still pending.

### 🔴 The config-driven requirement is broader than targeting

The Targeting step records the client's requirement: *"This targeting list frequently changes so it should be easy to add new targeting types"* — config-driven, not hard-coded. **This comment applies the same principle to channels.**

That suggests it was never a rule about targeting specifically, but a **general principle**. Other places this document declares a closed list that may not be:

| List | Status |
|---|---|
| Targeting types | ✅ Confirmed open — client |
| **Channels** | ✅ **Confirmed open — this note** |
| Audience data sources | 🟡 Amazon 1P, third-party… and others? |
| Deal types | 🟡 PG, Preferred, Private Auction… and others? |
| Inventory tiers | 🟡 Three — could there be more? |
| Creative durations | 🟡 10 / 15 / 20 / 30 — and others? |
| Currencies | 🟡 EUR / GBP / USD — as markets expand? |

**A pass over the document is needed to find every fixed list that should be open.**

### ✅ This settles the naming question

The conflict raised in Note 18 — *"channel"* vs *"channels"* vs `provider` — resolves in favour of **"channel"**:

| Term | Where it appears |
|---|---|
| **"channel"** | David, three times — *"market, duration and channel"* (Note 18), *"a single status for each channel"* (here) |
| **"channels"** | The rate-card endpoint's own response |
| `provider` | **Only in this document's schema** |

**`SelectedDealSchema.provider` should be renamed to `channel`** throughout, and `ChannelTypeEnum` — which uses "channel" for `dsp`/`sponsored` — renamed to avoid the collision.

> ### ⚠ OPEN QUESTION — Do Netflix/Disney review statuses surface in VOW's API?
>
> Unresolved from v2.0, and it determines the whole design of this step. If they do, the agent can poll and progress automatically. If they are tracked externally, a manual-entry route or webhook is needed and the agent must hold an "awaiting external confirmation" state — **which would expand M1's scope.** To confirm.

---

# Step 10: Tracking Setup

🔄 **MOVED** — ASIN validation was in Step 1 and ad-tag conversions were in Step 2. Both now sit here.

⚠ **This step is not gated on the creative.** It can be done before, after, or alongside creative upload — see Review Note 27.

| Field | Type | Requirement | Change from v1.1.0 |
|---|---|---|---|
| Sells on Amazon? | Question | Asked here | 🔄 MOVED from Step 1 |
| Product ASINs | Textarea | Required if endemic | ✅ Validation unchanged: `POST /api/contextual-targeting/{market}/asin-validation/` |
| Sells on own website? | Question | Asked here | ➕ NEW explicit question |
| Ad tag registered? | Check | Required if yes | ➕ NEW. If not, show setup instructions — the tag must be installed **before** the campaign runs (tracking only records activity after it goes live) |
| Ad tag conversions | Multi-select | Required if ad tag exists | 🔄 MOVED from Step 2. Events: Page view, Add to cart, Checkout, Application. Via `GET /api/conversions/definitions/` |

**API calls at this step:** `POST /api/contextual-targeting/{market}/asin-validation/`, `GET /api/conversions/definitions/`

> ### ✅ REVIEW NOTE — Open Question 1 is resolved here (Notes 16 and 17)
>
> The open question raised twice in v2.0 — ASINs being needed in the create payload but collected at this step — **is now settled: collect later and patch.**
>
> | Step | What happens |
> |---|---|
> | **Create strategy** | `POST /api/strategies/` with `product_asins: []`; `product_location` from the advertiser record |
> | **Here** | Confirm selling location (defaulted from the advertiser), collect and validate ASINs, then **`PATCH /api/strategies/{id}/`** to attach them, plus the ad-tag check and conversions |
>
> **Selling location also moves here** (Note 16), defaulted from the advertiser record rather than asked at Step 1.
>
> 🔴 **`PATCH /api/strategies/{id}/` must be added to §4** — the resolution depends on it, and it is not currently listed.
>
> Two things worth keeping in view:
> - The **ASIN validation response returns `product_category`**, which should auto-fill Step 1's product category (Note 15). One call, two fields.
> - The **ad-tag warning is irreversible** — data before the tag is installed is permanently lost. This is the single most consequential operational warning in the flow and should stay prominent.

---

## 📋 REVIEW NOTE 27 — The tail of the flow is unordered; tracking is not gated on creatives

**David's comment:** *"could be done before creatives if they are no available yet - no order necessary"*

This step's introduction previously stated that ASIN validation and ad-tag conversions *"now sit here, **after creative approval**."* **That ordering is not necessary** — and putting it last is actively harmful.

### The document placed the longest-lead-time task last

| Task | Typical duration | Depends on |
|---|---|---|
| Plan (Basics → Predict reach) | Minutes | The agent |
| Finalise and create | Seconds | One trader action |
| Creative upload | **Days** | The agency producing the video |
| Platform approval | **24–48 hours** | The channels — external |
| 🔴 **Ad tag installation** | **Days to weeks** | The **advertiser's development team** |
| Credit top-up | Minutes to hours | Finance |

**The ad tag is the longest task in the flow, depends on a third team, and its consequence of being late is irreversible** — this step's own warning says *"tracking only records activity after it goes live."* Data before installation is permanently lost.

Placing it last maximises the chance it is rushed or skipped. **This comment is not only about flexibility; it reduces a real risk.**

### The flow model changes: a chain becomes a set of prerequisites

```
❌ As written — a linear chain, each step gating the next
   Create → Creative → Platform approval → Tracking → Credit → Activate

   If the creative is delayed, tracking is blocked — despite having
   no relationship to it.

✅ Corrected — three independent branches joining at activation
   Create ──┬──→ Creative upload ──→ Platform approval ──┐
            ├──→ Tracking setup ─────────────────────────┤──→ 💰 Activate
            └──→ Credit check ──────────────────────────┘
```

**The real dependencies, traced:**

| Dependency | Genuine? |
|---|---|
| Basics → Inventory → Targeting → Budget split → Predict reach → Finalise → Create | ✅ Each genuinely requires the previous |
| Create → ASIN patch | ✅ Needs the strategy ID (Note 17) |
| Creative upload → Platform approval | ✅ Nothing to review until uploaded |
| Create → Credit check | ❌ Credit is entirely independent |
| **Tracking ↔ Creative** | ❌ **No relationship whatsoever** |
| Everything → Activate | ✅ Activation is a **join** |

### Tracking setup itself splits into three, with different dependencies

| Sub-task | Depends on | Earliest possible |
|---|---|---|
| **Ad tag installation** | Nothing — the tag lives on the advertiser's own site | 🔴 **Immediately** |
| ASIN collection and `PATCH` | The strategy must exist | After Create |
| Conversion event selection | The ad tag must exist | After the tag |

**⚠ A suggestion going beyond David's comment:** since ad-tag installation has *no* dependency and the longest lead time, the **check** for whether a tag exists could run at the very start of the session — alongside loading advertiser defaults (Note 13). If an advertiser has no tag and needs one, that is a multi-day dependency the trader should learn on day one, not at the end. *This is an extension of the lead-time logic, not something David stated — to confirm.*

### 🔴 `current_stage` cannot express this

`PlanningAgentState.current_stage: str` drives the adaptive canvas. **Once three branches are in flight, there is no single stage** — the creative may be awaiting platform approval while tracking awaits a tag and credit is already settled. One string cannot represent that.

```python
# Was
current_stage: str

# Needs
current_focus: str                        # what the trader is working on now
activation_prerequisites: dict            # what remains outstanding
```

```python
class ActivationPrerequisitesSchema(BaseModel):
    """➕ NEW — these run independently; activation joins them"""
    creative_uploaded: dict[str, bool] = Field(default_factory=dict)
    # per duration: {"30": True, "15": False}
    creative_approved: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
    # per channel — Note 26
    ad_tag_registered: Optional[bool] = None
    asins_attached: bool = False
    conversions_selected: bool = False
    tracking_skipped: bool = False        # explicitly declined by the trader
    credit_sufficient: Optional[bool] = None

    @property
    def outstanding(self) -> list[str]: ...
    @property
    def ready_to_activate(self) -> bool: ...
```

**A side benefit:** making `creative_uploaded` a per-duration map also **closes the gap flagged at the Upload Creative step** — *"multiple durations, partial upload is not covered."* One change, two problems.

### Loops become branch-local, with one exception

| Loop | Scope |
|---|---|
| Creative rejected → re-upload | **Within the creative branch** — other branches unaffected |
| Credit insufficient → top-up | **Within the credit branch** |
| **Duration mismatch → re-confirm the plan** | 🔴 **Cross-branch** — it returns upstream of all three, because the plan's economics changed |

Previously a rejection anywhere stalled the whole chain. Now only its own branch stalls.

### Agent behaviour: report what is outstanding, not what is next

```
Agent: "✅ Strategy VMA2026412 created.

        Three things remain before activation. They're independent —
        any order:

        📹 CREATIVE   30s ⬜ not uploaded · 15s ⬜ not uploaded
                      Platform approval follows upload — 24–48 hours
        📊 TRACKING   Ad tag ⬜ not registered · ASINs ⬜ not collected
        💳 CREDIT     £7,500 available, £10,000 needed

        I'd start with the ad tag. It's your development team's work,
        it takes the longest, and if it's installed after the campaign
        starts, the data before that point is lost permanently.

        It can run in parallel while you wait for the creative.

        Which would you like to work on?"
```

The lead-time recommendation matters: it is the agent contributing judgement rather than sequencing steps.

### Flow structure across three comments

| | Steps | Structure | Loops | Interrupts |
|---|---|---|---|---|
| v2.0 as written | 13 | Rigid chain | 5 | 2 |
| After Notes 5, 23, 27 | **~7 sequential + 3 parallel** | **Head + branches + join** | 4 *(two branch-local, one cross-branch)* | **1** — platform approval only |

> **⚠ To confirm**
> 1. Can the **ad-tag check** run at the very start of the session, given it has no dependency? *(A suggestion, not something David stated.)*
> 2. Does creative upload need the strategy ID, or could it also precede Create?
> 3. Can a trader **explicitly skip** tracking and run without conversion measurement? *(The `tracking_skipped` flag assumes yes.)*

---

## 📋 REVIEW NOTE 28 — ✅ RESOLVED: `product_location` and ASINs can be updated after creation

**David's comment on this document's own open question:** *"no they can be updated on the strategy after creation"*

This answers the question v2.0 raised **twice** — at Step 1 and repeated here — the most-frequently-repeated ⚠ marker in the document. **The answer is: collect later and update.**

### The full history of this one question

| Stage | What happened |
|---|---|
| v2.0 | Raised the question twice, with two options and *"Confirm with client"* |
| This revision, initially | Leaned toward **keeping ASINs early**. **Wrong** |
| Notes 16, 17 | *"Can leave out"* and *"comes later"* — the later option **implied**; cited `product_asins: []` as supporting evidence |
| Note 24 | Showed that evidence was for `POST /api/strategies/`, which may be the wrong endpoint — **the justification weakened** |
| **Note 28** | **Direct, explicit confirmation.** The weakened evidence is no longer needed — the answer is stated by the client |

### 🔴 The larger point: the strategy is mutable after creation

David's wording is general — *"they can be **updated on the strategy after creation**."* This is not a rule about ASINs; it is a **capability of the strategy record.**

**And this is the mechanism that makes Review Note 27 possible.** Note 27 established that creative, tracking and credit are independent branches converging at activation — but that only works if the strategy does not have to be complete at creation. **This comment confirms it does not.**

The two notes are complementary: **27 describes the architecture, 28 confirms the capability it rests on.**

### The resulting pattern: create minimal, attach later

```
Finalise  →  Create (minimal)  →  attach in parallel  →  Activate
```

| Required at creation | Attached after creation |
|---|---|
| Name · flight dates · market · currency · durations | `product_asins` — Notes 17, 28 |
| Goal · KPI · budget | `product_location` — Notes 16, 28 *(or from the advertiser record)* |
| Selected deals (channels) | `ad_tag_conversions` — Note 28 |
| Targeting, as applied | `selected_creatives` and their approval statuses |

**The strategy is therefore a mutable record until activation, not a frozen artefact.** That also completes the *"costless plan"* principle: after creation the record exists and can still be changed, and no spend has occurred. **Activation is both the spend action and the point at which the plan settles.**

This also supports the recommendation in Note 23's open question about status: `created` means *"the record exists, is still mutable, and is not spending."*

### ⚠ What is confirmed, and what is not

| | Status |
|---|---|
| Post-creation update **capability** | ✅ **Confirmed** |
| The **endpoint** for it | ⚠ **Still unnamed** — `PATCH`, `PUT`, or a dedicated route? |

Given Note 24, the update endpoint may also have a CTV-specific variant. **This is therefore not a new question — it is one more item in the CTV endpoint family question.**

> **⚠ To confirm**
> 1. What is the update endpoint — `PATCH`, `PUT`, or something dedicated? *(Folded into the CTV endpoint family question.)*
> 2. Can **budget** also be updated after creation? If so, Note 23's re-confirmation loop applies to it.

---

# Step 11: Credit Check

➕ **ENTIRELY NEW** — did not exist in v1.1.0.

Credit is checked **only at activation**, not during planning. Everything before this point is a **costless plan**.

| Field | Type | Requirement |
|---|---|---|
| Account balance | Number | Read-only |
| Strategy budget | Number | Read-only |
| Sufficient | Boolean | Derived (balance ≥ budget) |

**If insufficient:** prompt a top-up via `POST /api/credits/` or `POST /api/credits/stripe/`.

**API call:** `GET /api/credits/summary/`

> ### 📋 REVIEW NOTE — Reducing the budget here re-triggers approval
>
> If credit is insufficient, one option is to reduce the budget. That changes the forecast, which means the plan the manager approved no longer matches what will run — **so it must return to Plan approval.** The agent should say so when offering the option, not after.
>
> ⚠ The response shape for `GET /api/credits/summary/` is not specified in §4.2. To add.

---

# Step 12: Activate

➕ **ENTIRELY NEW** — did not exist in v1.1.0 (was implicit in "create strategy").

**The single spend action in the entire flow. Everything before this was free.**

**API call:** `POST /api/strategies/{id}/set_status/`

After activation, VOW's outbound sync creates the Campaigns and Ad Groups on Amazon DSP.

> ### 📋 REVIEW NOTE — This step's separation from "create" is a strength worth keeping explicit
>
> Splitting *create* (a free database record) from *activate* (the only spend action) is one of v2.0's better decisions, and none of the review comments touch it. It is what makes Steps 1–11 a costless plan the trader can iterate on freely.
>
> One addition worth making: the agent should state at activation **what is still incomplete** — e.g. a duration whose creative has not been uploaded and approved (see Step 8's flagged items), since that portion will not deliver.

---

# 4. API Catalogue

🔄 **CHANGED** — original catalogue kept, with additions and removals marked.

## ✅ Unchanged from v1.1.0

| Operation | Method | Endpoint |
|---|---|---|
| Check name uniqueness | `GET` | `/api/strategies/check_strategy_name_uniqueness/` |
| ASIN validation | `POST` | `/api/contextual-targeting/{market}/asin-validation/` |
| Product categories | `GET` | `/api/contextual-targeting/{market}/product-categories/` |
| Conversion definitions | `GET` | `/api/conversions/definitions/` |
| List deals | `GET` | `/api/deals/` |
| Deal filter properties | `GET` | `/api/deals/filter-properties/` |
| List audience sets | `GET` | `/api/audience-sets/` |
| Suggest audiences | `POST` | `/api/audience-sets/suggest/` |
| Audience reach forecast | `POST` | `/api/audience-sets/reach-forecast/` |
| Strategy reach forecast | `POST` | `/api/strategies/reach-forecast/` |
| List assets | `GET` | `/api/assets/` |
| List creatives | `GET` | `/api/creatives/` |
| Create strategy | `POST` | `/api/strategies/` |
| Read strategy | `GET` | `/api/strategies/{id}/` |

## ➕ New in v2.0

| Operation | Method | Endpoint |
|---|---|---|
| CTV rate card | `GET` | `/api/rates/ctv/{market}/` |
| Inventory sources | `GET` | `/api/inventory-sources/` |
| Activate strategy | `POST` | `/api/strategies/{id}/set_status/` |
| Credit summary | `GET` | `/api/credits/summary/` |
| Upload URLs | `POST` | `/api/assets/amz_assets/gen_upload_urls/` |
| Register asset | `POST` | `/api/assets/amz_assets/register/` |
| Locations | `GET` | `/api/strategies/locations/{market}/` |

## ❌ Removed

| Operation | Method | Endpoint | Reason |
|---|---|---|---|
| Draft create | `POST` | `/api/strategies/draft/` | Client: *"draft is just for the wizard"* |

---

## 📋 REVIEW NOTE — The catalogue needs reconciling with the steps

The review surfaced several inconsistencies between this catalogue and the step sections.

### Endpoints to add

| Endpoint | Why | From |
|---|---|---|
| 🔴 **`POST /api/simple-strategies/`** *(name to confirm)* | The CTV create endpoint — `POST /api/strategies/` is probably the wrong one | Note 24 |
| 🔴 **`PATCH /api/strategies/{id}/`** | The ASIN resolution depends on it — attaching ASINs after create | Note 17 |
| 🔴 **`GET /api/advertisers/{id}/defaults/`** *(or the real equivalent)* | Advertiser defaults do not exist anywhere in the document | Note 13 |
| **Simplified CTV audience-set creation** | Referenced at the Create step but never named or listed | v2.0 gap |
| **`POST /api/credits/`, `POST /api/credits/stripe/`** | Referenced at Credit check but not in the table | v2.0 gap |
| **`POST /api/contextual-targeting/{market}/products/`** | Referenced at the Targeting step but not in the table | v2.0 gap |

### Endpoints marked ✅ Unchanged that the steps say are removed

| Endpoint | Catalogue says | Step says |
|---|---|---|
| `GET /api/assets/` | ✅ Unchanged | ❌ REMOVED for CTV (Step 8) |
| `GET /api/creatives/` | ✅ Unchanged | ❌ REMOVED for CTV (Step 8) |
| `GET /api/audience-sets/` | ✅ Unchanged | *"Nobody browses"* (Targeting step) |

**All three should be marked ❌ removed from CTV scope**, with a note that they remain valid for Display.

### Other issues

- **`GET /api/inventory-sources/`** is listed as ➕ NEW but never referenced in any step. It is likely the source of the derived `inventory_tier` — this should be stated (Note 18 depends on tier derivation being explained).
- **Two reach-forecast endpoints exist** (`/audience-sets/reach-forecast/` and `/strategies/reach-forecast/`), plus a third *"simplified CTV endpoint, name TBC"*. Which applies when is not stated.
- **The nine v2.0 endpoints have no request/response specifications.** v1.1.0 gave full contracts for five endpoints; the new ones have names only. As a contract document, this is incomplete — Wajahat and Vishal cannot build against a name.
- **`GET /api/deals/filter-properties/` changes purpose** (Note 18) — no longer populating filter dropdowns for a table, but telling the agent which genres and lengths are available to match against.

---

## 🔴 REVIEW NOTE — §4.2's examples are assumptions, not verified contracts

This is the most consequential finding about this section, and it emerged from Note 20.

**The `POST /api/audience-sets/suggest/` example in §4.2 is confirmed wrong.** It shows a `bundles.narrow/balanced/broad` structure that the endpoint does not support. That example was written in v1.1.0 as an assumption and carried into v2.0 unverified.

**The same doubt applies elsewhere in §4.2:**

| Example | Status | Raised by |
|---|---|---|
| `POST /audience-sets/suggest/` → `bundles.narrow/balanced/broad` | ❌ **INCORRECT** — confirmed not supported | Note 20 |
| 🔴 `POST /api/strategies/` — **the endpoint itself** | ⚠ **PROBABLY WRONG** — the CTV path likely uses `simple-strategies` | **Note 24** |
| The suggest response's **per-segment `vcpm`** | ⚠ **QUESTIONABLE** — if the fee is per data source, what do per-segment values represent? | Note 2 |
| A 3P deal's **built-in targeting** in the deals response | ⚠ **UNKNOWN** — may not be exposed at all, and Note 18 depends on it | Notes 1, 18 |
| `POST /strategies/` accepting `product_asins: []` | ⚠ **INFERRED, and for the wrong endpoint** — see Note 24 | Notes 17, 24 |
| The **nine v2.0 endpoints** | ❌ **NO SPECIFICATION AT ALL** | §4 |

> **🔴 Note 24 escalated this problem.** It was previously about response *shapes*. It now extends to **endpoint names** — the document has assumed wizard-era endpoints throughout, while a CTV-specific family appears to exist. The document itself half-knew this: the audience set is created *"via a simplified CTV endpoint"* while the strategy uses the full one.
>
> **The single most useful ask is therefore: what is in the CTV endpoint family?** One answer resolves six items in this section.

**For a document that four people will code from, this matters more than any single wording fix.** An incorrect API example is worse than a missing one — it looks authoritative.

### Correction: mark every example with its verification status

| Marker | Meaning |
|---|---|
| ✅ **VERIFIED** | Checked against the real API |
| ⚠ **ASSUMED** | Plausible but not yet verified — do not build against it |
| ❌ **INCORRECT** | Confirmed to differ from the real API |

Applied now, only the endpoints v1.1.0 was built against can carry ✅; the rest are ⚠ or ❌ until confirmed. That is an uncomfortable table to publish, but it is the accurate one — and it tells Wajahat and Vishal exactly which contracts they can rely on.

> **🔴 The single most useful thing to unblock this:** real response samples for `POST /api/audience-sets/suggest/`, `GET /api/deals/`, and the nine new endpoints. One sample each converts ⚠ to ✅ and removes the largest source of build risk in this document.

---

# 5. Pydantic Data Models

🔄 **CHANGED** — original models kept where valid, extended and restructured.

## 📋 REVIEW NOTE — Consolidated schema changes from the review

Rather than repeating the full model listing, this is the complete set of schema changes the eighteen comments require. Each links to the note that explains it.

### New enums

```python
class TargetingSourceEnum(str, Enum):
    """➕ NEW (Note 1) — where targeting is applied for 3P inventory"""
    AMAZON_DSP = "AMAZON_DSP"              # limited on 3P (e.g. device only)
    INVENTORY_SOURCE = "INVENTORY_SOURCE"  # SSP-side; deal-bound; adds CPM

class AudienceDataSourceEnum(str, Enum):
    """➕ NEW (Note 2) — the fee is charged per data source, not per segment"""
    AMAZON_1P = "AMAZON_1P"
    THIRD_PARTY = "THIRD_PARTY"
    NONE = "NONE"                          # e.g. basic demographic — no fee
```

### New schemas

```python
class PlanStatusEnum(str, Enum):
    """➕ NEW (Note 23) — simplified for M1; manager approval deferred.
       ApprovalStatusEnum is retained separately for platform creative approval."""
    DRAFT = "DRAFT"
    FINALISED = "FINALISED"
    # PENDING_APPROVAL = "PENDING_APPROVAL"   # future — manager routing
    # APPROVED = "APPROVED"                   # future
    # REJECTED = "REJECTED"                   # future

class ActivationPrerequisitesSchema(BaseModel):
    """➕ NEW (Note 27) — the post-create branches run independently;
       activation is a join that waits for all of them."""
    creative_uploaded: dict[str, bool] = Field(default_factory=dict)
    # per duration: {"30": True, "15": False} — also closes the partial-upload gap
    creative_approved: dict[str, ApprovalStatusEnum] = Field(default_factory=dict)
    # per channel — Note 26
    ad_tag_registered: Optional[bool] = None
    asins_attached: bool = False
    conversions_selected: bool = False
    tracking_skipped: bool = False        # explicitly declined by the trader
    credit_sufficient: Optional[bool] = None

    @property
    def outstanding(self) -> list[str]: ...
    @property
    def ready_to_activate(self) -> bool: ...

class AdvertiserSetting(BaseModel):
    """➕ NEW (Note 22) — an advertiser value plus whether it can be overridden.
       Not all advertiser settings are defaults: some are brand policy."""
    value: Any
    is_locked: bool = Field(False,
        description="True = brand policy; the trader cannot override and "
                    "the repair loop cannot relax it")
    reason: Optional[str] = Field(None,
        description="Shown to the trader when locked, e.g. 'brand policy: CTV only'")

class AdvertiserDefaultsSchema(BaseModel):
    """➕ NEW (Notes 13, 15, 22) — loaded at session start, before field extraction.
       Every value is an AdvertiserSetting so the agent knows what it may change."""
    frequency_cap: Optional[AdvertiserSetting] = None            # ✅ confirmed — Note 13
    product_categories: Optional[AdvertiserSetting] = None       # ✅ confirmed — Note 15
    device_types: Optional[AdvertiserSetting] = None             # ✅ confirmed — Note 22
    product_location: Optional[AdvertiserSetting] = None         # 🟡 likely — Note 16
    primary_currency: Optional[AdvertiserSetting] = None         # 🟡 likely — Note 9
    content_category_exclusions: Optional[AdvertiserSetting] = None   # 🟡 likely — Note 22
    budget_cap: Optional[AdvertiserSetting] = None
    approval_threshold: Optional[AdvertiserSetting] = None       # 🟡 possibly — Step 6

class AudienceFeeSchema(BaseModel):
    """➕ NEW (Note 2) — fees per data source; effective CPM is a range if mixed"""
    amazon_1p_fee: Optional[str] = None
    third_party_fee: Optional[str] = None
    is_mixed_source: bool = False
    effective_cpm_min: str
    effective_cpm_max: str
    effective_cpm_note: str

class DealMatchCriteriaSchema(BaseModel):
    """➕ NEW (Note 18) — what the agent matches deals against"""
    market: str
    duration: DurationEnum
    channel: str                                      # provider
    ros_or_genre: Optional[str] = None
    targeting_requirements: Optional[dict] = None
    trader_specified_deal_id: Optional[str] = None    # escape hatch

class AudienceBundleConstructionSchema(BaseModel):
    """➕ NEW (Note 20) — how the agent builds the three profiles
       from a flat API response. The API does not group them."""
    grouping_basis: str = Field("cumulative_reach",
        description="cumulative_reach | relevance_score | data_source")
    is_nested: bool = True
    reach_targets: dict[str, int] = Field(default_factory=dict)
    # {"NARROW": 500_000, "BALANCED": 1_500_000, "WIDE": 5_000_000}
```

### Changed schemas

| Schema | Change | Note |
|---|---|---|
| `SelectedDealSchema` | ➕ `targeting_source`, `source_targeting_cpm_uplift`, `built_in_targeting` | 1 |
| `SelectedDealSchema` | ➕ `selection_method`, `matched_on`, `is_surfaced_to_trader` | 18 |
| `SelectedDealSchema` | 🔄 `deal_type` should be an enum, not `str` | quality |
| `SelectedAudienceSetSchema` | ❌ Remove `vcpm_fee` (fee is per source) · ➕ `data_source` | 2 |
| `SelectedAudienceSetSchema` | ➕ `applies_to_providers: list[str]` — which portions the audience covers | 19 |
| `AudienceFeeSchema` | 🔄 Must allow the Amazon 1P fee on **3P portions** too | 19 |
| `TargetingSchema` | ➕ `defaults_applied: list[str]` — records which defaults were auto-applied | 21 |
| `TargetingSchema` | ➕ `locked_settings: list[str]` — which values the agent may not change | 22 |
| `TargetingSchema` | 🔄 `mobile_environment` becomes **Conditional** on `Mobile ∈ device_types` | 22 |
| `AdvertiserDefaultsSchema` | 🔄 Every field wrapped in **`AdvertiserSetting`** (`value` + `is_locked` + `reason`) | 22 |
| `FullStrategySchema` | ❌ Remove `manager_required`, `rejection_reason` · 🔄 `approval_status` → `plan_status` · `approved_by/at` → `finalised_by/at` | 23 |
| `PlanningAgentState` | 🔄 Same renames — `plan_status`, `finalised_by`, `finalised_at` | 23 |
| `ApprovalStatusEnum` | ✅ **Retained** — platform creative approval still needs a three-way status | 23 |
| `SelectedCreativeSchema` | 🔄 `click_through_url: HttpUrl = Field(...)` → **`Optional[HttpUrl] = None`** | 25 |
| `FullStrategySchema` | 🔄 `creative_approval_status` → **`creative_approval_statuses: dict[str, ApprovalStatusEnum]`**, keys derived from the plan's channels | 26 |
| `SelectedDealSchema` | 🔄 **Rename `provider` → `channel`** throughout | 26 |
| `ChannelTypeEnum` | 🔄 **Rename** — it uses "channel" for `dsp`/`sponsored`, which now collides | 26 |
| `PlanningAgentState` | 🔴 `current_stage: str` → **`current_focus: str` + `activation_prerequisites: dict`** — one string cannot express three parallel branches | 27 |
| **`ActivationPrerequisitesSchema`** | ➕ **New** — per-branch completion; also closes the partial-upload gap | 27 |
| `MarketBudgetBidSchema` | 🔄 `base_bid: str = Field(...)` → `Optional[str] = None` | 12 |
| `TargetingSchema` | 🔄 Replace five hard-coded fields with a config-driven `selections: dict[str, list[str]]`; audience segments become one targeting type | 5 |
| `FullStrategySchema` | ➕ `kpi_target_value: Optional[int] = Field(None, ge=1, le=5)` | 10 |
| `FullStrategySchema` | 🔄 `formats` becomes a constant `["streaming_tv"]` | 14 |
| `FullStrategySchema` | 🔄 `creative_approval_status` → `creative_approval_statuses: dict[str, ApprovalStatusEnum]` | Step 9 |
| `FormatEnum` | 🔄 Annotate `PRIME_VIDEO` as *"not a format — see `SelectedDealSchema.provider`"* | 14 |
| `BudgetSplitSchema` | ➕ `by_market` if multi-market is in scope | 8 |

### Schema quality issues found during review

These were not raised by David but surfaced while working through his comments, and affect the same models.

| Issue | Where | Why it matters |
|---|---|---|
| **Untyped `list[dict]`** | `BudgetSplitSchema.by_inventory` / `.by_duration`, `ForecastResultSchema.reach_curve`, `TrackingSetupSchema.validated_asins` | Pydantic validates nothing inside a bare `dict` — wrong keys pass silently, which defeats the purpose of the model. Nested models should replace them. |
| **`matching_mode: str`** | `FullStrategySchema` | `Similar` / `Exact` are two fixed values — a typo like `"exact"` or `"Similiar"` would validate. Should be an enum. |
| **`deal_type: str`** | `SelectedDealSchema` | `inventory_tier` is an enum but `deal_type` is a string, despite having three fixed values. Inconsistent. |
| **`DateRangeSchema.lower/upper` as `str`** | `DateRangeSchema` | Pydantic will not validate the date format — `lower="hello"` passes. `datetime.date` would catch it. |
| **`durations` vs `duration_seconds` type mismatch** | `DurationEnum` (`"30"`) vs `SelectedCreativeSchema.duration_seconds` (`30`) | The duration match check has to convert between them; one representation would be safer. |
| **Enum comments do not enforce** | `GoalEnum`, `KPIEnum`, `FormatEnum` | `# future scope` is a comment, so `goal="CONVERSION"` still validates. A runtime validator (or a separate CTV enum) would make the scope real. |
| **`is_available` has no reason field** | `ForecastResultSchema` | The honesty rule needs to explain *why* reach is unavailable; an `unavailable_reason` field would let the UI show it. |

---

# 6. State Machine

🔄 **CHANGED** — needs complete rebuild. The original was a linear pipe. The confirmed flow has branches, loops, and interrupts.

## The confirmed state machine, revised after review

```
 1  START
 2   → load_advertiser_defaults              ➕ NEW (Note 13)
 3   → extract_fields                        (slot-filling from brief)
 4   → confirm_extraction                    ➕ NEW (§7.3's own requirement)
 5   → match_inventory                       🔄 RENAMED from select_inventory (Note 18)
 6      → [if 3P needs curation] capture_curation_requirements
 7   → propose_targeting                     🔄 MERGED from suggest_audiences
 8      → [default applied: country + CTV device + no audience]
 9      → refine_targeting                   (optional — audience is one type)
10   → propose_budget_split                  🔄 now optional (Note 3)
11   → predict_reach
12      → [if Amazon] real forecast + reach curve
13      → [if 3P] CPM + derived impressions only (honest)
14      → [if insufficient] REPAIR: ordered levers → re-predict (loop)
15   → present_plan                          (on the strategy card)
16   → ⏸ PLAN APPROVAL                       (interrupt — optionally a manager)
17      → [if rejected] return to propose_targeting
18   → create_strategy                       (POST /strategies/, product_asins: [])
19   → upload_creative                       (video, gen_upload_urls + register)
20      → [if duration mismatch] amend plan → RE-APPROVE (loop back)
21   → platform_creative_approval            (Amazon / Netflix / Disney, independent)
22      → [if rejected] return to upload_creative
23   → tracking_setup                        (selling location + ASINs + ad tag)
24      → PATCH /strategies/{id}/            ➕ NEW (Note 17)
25   → credit_check
26      → [if insufficient] top-up, or reduce budget → RE-APPROVE
27   → activate                              (the single spend action)
28   → DONE
```

**Q&A side path:** at any point, the trader can ask a pricing/availability question (*"what's the CPM for Netflix 30s?"*). The agent answers from the rate card and resumes.

> ### 📋 REVIEW NOTE — Four structural changes to the graph
>
> | # | Change | From |
> |---|---|---|
> | 1 | ➕ **`load_advertiser_defaults`** at the start — defaults must be loaded before extraction, since several fields resolve from them | Note 13 |
> | 2 | 🔄 **`select_inventory` → `match_inventory`** — the node no longer presents choices, it matches | Note 18 |
> | 3 | 🔄 **`suggest_audiences` + `apply_targeting` → `propose_targeting` + `refine_targeting`** — one step with a default | Note 5 |
> | 4 | 🔴 **The repair loop's edges change** — two of its three actions no longer hold; the rewritten lever list (Step 5's review note) has seven, several conditional | Notes 4, 5, 12 |
>
> **Change 4 is the one that affects the build most.** The graph currently branches on "widen audience" and "raise bid"; neither is reliably available. The new levers are conditional on whether an audience is applied and on the deal type.
>
> ### ➕ `confirm_extraction` was missing from the graph
>
> §7.3 calls the *"Did I understand correctly?"* confirmation **"the single most important trust mechanism in the product"** — but no node existed for it. It is added at line 4, and should carry a short interrupt so the flow does not proceed on a misreading.
>
> ### Node naming
>
> Most nodes follow `verb_noun` (`extract_fields`, `predict_reach`, `create_strategy`). Two do not — `tracking_setup` and `credit_check` should be `setup_tracking` and `check_credit`. Minor, but this is a contract document that four people will code from.
>
> ### `current_stage` has no defined values
>
> `PlanningAgentState.current_stage: str` drives the adaptive canvas but its allowed values are never listed. Basil cannot build against an undefined string. A `StageEnum` should be added.

## Planning state — additions from the review

```python
class PlanningAgentState(TypedDict):
    # … existing fields …

    # ➕ NEW from the review
    advertiser_defaults: Optional[dict]        # Note 13 — loaded first
    kpi_target_value: Optional[int]            # Note 10
    deal_match_criteria: Optional[dict]        # Note 18
    targeting_defaults_applied: list[str]      # Note 5
    targeting_accepted_as_default: bool        # Note 5
    creative_approval_statuses: dict           # Step 9 — was a single value
```

> **A note on typing.** Every state field is a bare `dict` or `list[dict]`, even though §5 defines twelve well-formed Pydantic models. That is the standard LangGraph pattern and fine for performance, but it means no validation happens in the state.
>
> **Recommended approach — parse at the boundary:** each node reads the dict, converts it to the Pydantic model (validating there), does its work, and returns `.model_dump()`. This keeps LangGraph's pattern while catching malformed data at the point it enters a node rather than at the DSP.

---

# 7. Brief Parsing & Edge Cases

## 7.1 Entity Normalisation

✅ **UNCHANGED** — the original examples are correct. Additions:

| Input | Extraction | Status |
|---|---|---|
| `August 2026` | `flight_dates: {lower: "2026-08-01", upper: "2026-08-31"}` | ✅ Original |
| `UK` | `markets: ["GB"]`, `primary_currency: "GBP"` | ✅ Original |
| `£10,000` | `market_budgets: [{market: "GB", budget: "10000.00"}]` | ✅ Original |
| `education website` | `product_location: "NOT_SOLD_ON_AMAZON"` | ✅ Original |
| `30 seconds` | `durations: ["30"]` | ➕ NEW |
| `UK and France` | `markets: ["GB", "FR"]` | ➕ NEW — ⚠ *see Note 8: multi-market scope* |
| `sports drink` | Consider genre-specific deals (Sports) | ➕ NEW |
| `Prime and Netflix` | Multiple inventory tiers | ➕ NEW |

> ### 📋 REVIEW NOTE — This section was already right, and the field matrices were not
>
> Note 9 turns on a contradiction inside this document: **§7.1 already derives currency from market** (`UK → GBP`), while Step 1's matrix asked the trader to pick it from a dropdown. The parsing rules were correct; the field table was not.
>
> That pattern held across the review — **the field matrices were the weakest part of the document**, out of step with the schema (§5), the parsing rules (§7.1), the business logic (§2) and in two cases with the step's own prose. The `Source` column exists to close that gap: it makes explicit what §7.1 was already doing implicitly.
>
> **⚠ Also unresolved in this section:** what `"UK and France, £10,000"` means — £10,000 total, or per market? And if today is mid-August, does *"August"* mean the remainder of this August or next year's? Neither edge case is covered.

## 7.2 Validation Failure Protocols

✅ **UNCHANGED** — duplicate name, invalid ASIN, past dates protocols all correct.

1. **Duplicate name** — if `check_strategy_name_uniqueness` returns `false`, append a suffix (e.g. `Name_v2`) **and prompt the user**
2. **Invalid ASIN** — highlight the exact ASIN and request correction
3. **Past dates** — if `flight_dates.lower < today`, auto-adjust to tomorrow and inform the user

> ### 📋 REVIEW NOTE — These three are consistent, and the set is incomplete
>
> The three protocols encode a sound rule: **where the trader has a genuine choice, ask; where the value is impossible, fix it and say so.** A duplicate name is suggested; a past date is corrected. That distinction should be stated explicitly, because it is the principle the agent should apply to every failure.
>
> Note 7 makes protocol 1 more important, not less — if the agent generates the name, the collision path runs automatically, and *"and prompt user"* is what keeps the trader informed.
>
> **The set is incomplete.** No protocol covers: zero or negative budget · `upper < lower` · an invalid market code · no deals matching the criteria (**newly possible under Note 18**) · the suggest endpoint returning nothing · an API timeout or 500 · `POST /strategies/` returning 400 · a frequency target that exceeds the cap (**newly possible under Notes 10 and 13**).
>
> A complete failure-protocol table is needed — the graph's error edges depend on it.

## 7.3 Repair Loop

🔄 **CHANGED** — see the rewritten lever list in Step 5's review note. Only the Amazon portion is repairable, and two of the three original actions no longer hold.

## 7.4 "Did I understand correctly?" confirmation

➕ **NEW** — after extracting fields from a brief, the agent immediately shows what it understood so the trader can correct before proceeding. **This is the single most important trust mechanism in the product.**

> ### 📋 REVIEW NOTE — This mechanism is now doing more work than before
>
> Under the revised Step 1, **twelve fields are inferred, derived, generated or defaulted, and none are asked.** That makes this confirmation the *only* place the trader sees what the agent concluded — so it carries the full weight of the interaction rather than being a courtesy.
>
> It should show three things distinctly:
> 1. **What was understood** — the values
> 2. **What was assumed, and from where** — *"GBP, derived from market"*, *"frequency cap 3, from the advertiser default"*
> 3. **What is still unknown** — anything genuinely asked
>
> A node for this has been added to the state machine (line 4), which the previous version omitted.

---

# 8. Summary of All Changes

## v1.1.0 → v2.0

| Category | Count | Items |
|---|---|---|
| ✅ **Unchanged** | ~15 | Core principles, product attribution, deal types, date validation, name uniqueness, currency, most API endpoints, brief parsing examples |
| 🔄 **Changed** | ~12 | Step order, goal scoped to Awareness, KPI scoped to reach/frequency, deals enriched with tier, audiences renamed Wide, forecast with availability flag, state restructured, creative simplified to video |
| ➕ **New** | ~15 | Durations, inventory tiers, budget split, targeting, plan approval, creative duration check, platform creative approval, tracking setup (moved), credit check, activation, curation capture, effective CPM, adaptive-canvas fields |
| ❌ **Removed** | ~5 | Draft endpoint, product audiences, non-CTV formats (scoped out), non-awareness KPIs (scoped out) |

> **Note:** the original summary listed *"canary-check"* under Removed. That item does not appear anywhere else in this document, and is not present in v1.1.0 either. It has been removed from the summary. If a canary-style staged rollout was discussed with the client, it should be documented properly as future scope rather than listed as a removal.

## v2.0 → v2.0 reviewed (this revision)

| Category | Count | Items |
|---|---|---|
| 🔄 **Corrected** | 10 | 3P targeting is a choice · audience fee model · budget split optional · audiences optional · audiences merge into targeting · Step 1 rebuilt with a Source column · strategy name generated · currency derived · formats constant · product categories from advertiser |
| ➕ **Added** | 4 | `kpi_target_value` · advertiser defaults (schema, endpoint, state) · deal-match criteria · `PATCH /strategies/{id}/` |
| ❌ **Removed** | 3 | Base bids (not applicable to CTV) · selling location from Step 1 · product ASINs from Step 1 |
| 🔄 **Restructured** | 3 | Steps 4 + 5 merged (13 → 12 steps) · repair loop rewritten · deal selection becomes deal matching |
| ✅ **Resolved** | 1 | Open Question 1 — ASIN timing |

---

# 9. Consolidated Action List

Everything the eighteen comments require, in one place.

## Schema

| # | Change | Note |
|---|---|---|
| 1 | ➕ `TargetingSourceEnum`; `SelectedDealSchema.targeting_source`, `.source_targeting_cpm_uplift`, `.built_in_targeting` | 1 |
| 2 | ➕ `AudienceDataSourceEnum`, `AudienceFeeSchema`; ❌ remove `SelectedAudienceSetSchema.vcpm_fee`; ➕ `.data_source` | 2 |
| 3 | ➕ `kpi_target_value: Optional[int] = Field(None, ge=1, le=5)` + two validation rules | 10 |
| 4 | 🔄 `MarketBudgetBidSchema.base_bid` → `Optional[str] = None` | 12 |
| 5 | ➕ `AdvertiserDefaultsSchema`; ➕ `PlanningAgentState.advertiser_defaults` | 13, 15, 16 |
| 6 | 🔄 `formats` → constant `["streaming_tv"]`; annotate `FormatEnum.PRIME_VIDEO` | 14 |
| 7 | 🔄 `TargetingSchema` → config-driven `selections: dict[str, list[str]]`, audiences included | 5 |
| 8 | ➕ `DealMatchCriteriaSchema`; ➕ `SelectedDealSchema.selection_method`, `.matched_on`, `.is_surfaced_to_trader` | 18 |
| 9 | 🔄 `creative_approval_status` → `creative_approval_statuses: dict[str, ApprovalStatusEnum]` | Step 9 |
| 10 | ➕ `BudgetSplitSchema.by_market` — if multi-market is in scope | 8 |
| 11 | ➕ `AudienceBundleConstructionSchema`; `applies_to_providers`; `defaults_applied` | 19, 20, 21 |
| 12 | 🔄 `AudienceFeeSchema` must allow the Amazon 1P fee on 3P portions | 19 |
| 13 | 🔴 ➕ **`AdvertiserSetting`** wrapper (`value` + `is_locked` + `reason`); wrap every advertiser default in it; add `device_types` | 22 |
| 14 | ➕ `TargetingSchema.locked_settings`; make `mobile_environment` conditional | 22 |
| 15 | 🔵 ➕ **`PlanStatusEnum`** (`DRAFT`/`FINALISED`); remove `manager_required` and `rejection_reason`; rename `approved_by/at` → `finalised_by/at`; **retain `ApprovalStatusEnum`** for platform approval | 23 |
| 16 | 🔄 `click_through_url` → `Optional[HttpUrl] = None` | 25 |
| 17 | 🔴 `creative_approval_status` → `creative_approval_statuses: dict[str, ApprovalStatusEnum]`, keys derived | 26 |
| 18 | 🔴 Rename `provider` → **`channel`**; rename `ChannelTypeEnum` to avoid the collision | 26 |
| 19 | ⚠ Audit which enums should be **open lists** rather than fixed (data sources · deal types · tiers · durations · currencies) | 26 |
| 20 | 🔴🔴 ➕ **`ActivationPrerequisitesSchema`**; split `current_stage` into `current_focus` + `activation_prerequisites` | 27 |
| 21 | 🔄 Replace untyped `list[dict]` with nested models throughout | quality |
| 22 | 🔄 `matching_mode`, `deal_type` → enums *(`current_stage` is being replaced — see 20)* | quality |

## Document

| # | Change | Note |
|---|---|---|
| 1 | 🔴 Add a **`Source`** column to every field matrix; **remove UI widgets** from `Type` | 6, 7, 9, 11, 13 |
| 2 | 🔴 Replace the **Step 1 matrix** with the revised twelve-field version | 6–17 |
| 3 | 🔴 Replace the **Step 2 matrix**; add *"Deal matching, not deal selection"* and *"What is surfaced vs internal"* | 18 |
| 4 | 🔴 **Merge Steps 4 and 5**; add *"Default targeting"* and *"Accept or refine"*; renumber to 12 steps | 5 |
| 5 | 🔴 **Rewrite the repair loop** in both Step 5 and §7.3, with the ordered lever list | 4, 5, 12 |
| 6 | 🔴 Add a **"Advertiser defaults"** section — what they are, when loaded, how overridden | 13 |
| 7 | Correct §2.4 — remove the fee/profile correlation; add the per-source model and the CPM range | 2 |
| 8 | Correct the §2.3 tier table — targeting is a choice, and it is deal-bound | 1 |
| 9 | Add a **"Multi-market handling"** section, or scope it out of M1 explicitly | 8 |
| 10 | Add a **Format vs Provider** note; correct the v1.1.0 payload example | 14 |
| 11 | Mark **Open Question 1 resolved** in both places it appears | 16, 17 |
| 12 | Reconcile the **API catalogue** with the steps; add the five missing endpoints; add request/response specs for the nine v2.0 endpoints | §4 |
| 13 | Add a complete **failure-protocol table** | §7.2 |
| 14 | Add a note that this document is the **data contract, not the UI spec** | 11, 18 |
| 15 | 🔴 Remove the *"Amazon audiences only apply to Amazon-owned"* constraint; correct the tier table's Audiences column and the Note 1 explanation | 19 |
| 16 | 🔴 Add the **three effective-CPM scenarios** (3P can also carry the Amazon 1P fee) | 19 |
| 17 | 🔴 Mark §4.2's `bundles` example **❌ INCORRECT**; add a **"Bundle construction (agent-side)"** section | 20 |
| 18 | 🔴🔴 Add a **verification marker (VERIFIED / ASSUMED / INCORRECT)** to every §4.2 example | 20 |
| 19 | Add the **`markets` vs `location`** distinction and the location hierarchy | 21 |
| 20 | Add the **Targeting step's complete default table** | 4, 5, 19, 20, 21 |
| 21 | Rewrite §2.4's description of the three profiles — agent-built, equal-cost, optional, all tiers | 2, 4, 19, 20 |
| 22 | 🔴🔴 Add a **"CTV as a format vs CTV as a device"** note; correct Note 21's device row | 22 |
| 23 | 🔴 Add the **default vs constraint** distinction to the advertiser-defaults section | 22 |
| 24 | 🔴 Add a **"can it be locked?"** column to the repair-loop lever list | 22 |
| 25 | Make `Mobile environment` **Conditional** on device type | 22 |
| 26 | Note the **reach and CPM effect** of a CTV-only device restriction | 22 |
| 27 | 🔵 Rename the step to **Finalise Plan**; strip the approval workflow; remove the rejection edge | 23 |
| 28 | 🔵 Record that **separation of duties is deliberately deferred**, not overlooked | 23 |
| 29 | 🔵 Note that the **only genuine `interrupt()` in M1 is platform creative approval** | 23 |
| 30 | 🔵 Reword *"re-approval"* → *"re-confirmation"* at the duration-mismatch and credit-check loops | 23 |
| 31 | Add a *"last confirmed"* marker per section — decisions are still moving | 23 |
| 32 | 🔴 Add a **"CTV endpoint family"** section to §4; mark `POST /api/strategies/` as ⚠ ASSUMED | 24 |
| 33 | ⚠ Correct Note 17's evidence — the payload example was for the wrong endpoint | 24 |
| 34 | Reconcile §4 with the Targeting step — audiences got a CTV endpoint, the strategy did not | 24 |
| 35 | ✅ Mark the click-through URL item **resolved** at the Creative step | 25 |
| 36 | 🔴 Replace the three hard-coded channel rows with one derived per-channel row | 26 |
| 37 | 🔴 Reconcile §2.3 (*"Netflix, Hulu, others"*) with the platform-approval step | 26 |
| 38 | 🔴 Add a note that the **config-driven principle applies beyond targeting** | 26 |
| 39 | ✅ Rename `provider` → `channel` document-wide | 26 |
| 40 | 🔴🔴 Restructure §3 — **sequential head + parallel tail + join at Activate** | 27 |
| 41 | 🔴 Remove *"after creative approval"* from the Tracking step; add *"no order necessary"* | 27 |
| 42 | 🔴 Add an **"Activation prerequisites"** section — three branches and the join condition | 27 |
| 43 | 🔴 Add a **"Lead times"** note — the ad tag is the long pole and should start first | 27 |
| 44 | 🔴 Split Tracking setup into its three sub-tasks with their own dependencies | 27 |
| 45 | 🔴 Redraw the §6 state machine with **parallel branches and a join node** | 27 |
| 46 | Mark loops as **branch-local** or **cross-branch** | 27 |
| 47 | ✅ Mark **both instances** of the ASIN-timing open question **resolved** | 28 |
| 48 | 🔴 Add a note: **the strategy is mutable after creation** — a general capability, not an ASIN rule | 28 |
| 49 | Trim the Create payload to the minimal set; add a **"create minimal, attach later"** section | 28 |
| 50 | 🎉 Record in §8 that **2 of 5 ⚠ markers were answered** — the practice worked | 20, 28 |

## Agent behaviour

| # | Change | Note |
|---|---|---|
| 1 | Offer the 3P targeting-source choice with its trade-off | 1 |
| 2 | Present effective CPM as a **range** for mixed-source bundles, and say it is an estimate | 2 |
| 3 | Recommend Balanced on **reach**, not cost | 2 |
| 4 | Offer to **skip** the budget split, stating the accuracy consequence | 3 |
| 5 | Present **"no audience"** as a valid, often-preferable option for Awareness | 4 |
| 6 | Apply **default targeting**, then invite refine-or-accept | 5 |
| 7 | Present Step 1 as a **summary to confirm**, not questions to answer | 6 |
| 8 | **Generate** the strategy name; handle collisions automatically and say so | 7 |
| 9 | Ask for the frequency target (1–5) with guidance; **flag target-vs-cap conflicts** | 10, 13 |
| 10 | **Match** deals; surface provider, CPM, impressions, tier capability — plus the **PG commitment warning** | 18, 12 |
| 11 | Load and display **advertiser defaults**, with override offered | 13 |
| 12 | On the rewritten repair loop, state honestly when no lever remains | 12 |
| 13 | Compare **three** audience configurations, not two — 3P can carry Amazon audiences | 19 |
| 14 | When widening the audience on a 3P portion, **say the effect cannot be verified** | 19 |
| 15 | **Build the three profiles** from the flat API response — grouping is agent-side | 20 |
| 16 | State the reach effect when the trader narrows location below country level | 21 |
| 17 | 🔴 Show **locked** settings with a 🔒 marker and the reason; never silently apply them | 22 |
| 18 | 🔴 In the repair loop, **say which lever could not be used and why** | 22 |
| 19 | Surface the reach and CPM cost of a CTV-only restriction the trader did not choose | 22 |
| 20 | 🔵 Present plan finalisation as an **ordinary confirmation turn**, not a gate with a wait | 23 |
| 21 | **Do not ask for a click-through URL** — accept one if the trader volunteers it | 25 |
| 22 | 🔴 Report approval status **per channel present in the plan**, not against a fixed list | 26 |
| 23 | 🔴🔴 After Create, report **what is outstanding** rather than *"now do X"* — three branches, any order | 27 |
| 24 | 🔴 **Recommend starting with the ad tag** — it is the long pole and the risk is irreversible | 27 |
| 25 | At activation, **state anything still incomplete** (e.g. a duration with no approved creative) | 27 |

---

# 10. Open Questions

## ✅ Resolved by this review

| # | Question | Answer | Via |
|---|---|---|---|
| 1 | ASIN and `product_location` are needed in the create payload but collected at Tracking setup | **Collect later and patch.** `product_asins: []` at create; `product_location` from the advertiser record; `PATCH /api/strategies/{id}/` at Tracking setup | Notes 16, 17 |
| 2 | Does the `suggest` endpoint return `bundles.narrow/balanced/broad`? | **No — not currently supported.** The three profiles are built agent-side from a flat response | Note 20 |
| 3 | Is the manager-approval threshold per advertiser, global, or per role? | **Moot for M1** — manager approval is deferred, so there is no threshold to configure | Note 23 |
| 4 | Is the click-through URL required for CTV, or should it be optional? | **Optional for streaming TV** — there is no click mechanism on a television | Note 25 |
| 5 | *"channel"* vs *"channels"* vs `provider` — which term? | **"channel"** — David uses it consistently, the rate card returns *"channels"*, and `provider` appears only in this document | Note 26 |
| 6 | Must `product_location` and ASINs be collected before the strategy is created? | **No** — they can be updated on the strategy after creation. *This also confirms the capability the parallel-branch structure depends on* | **Note 28** |

## ⚠ Still open — for David / the client

Grouped by what they block.

### Blocking the build

| # | Question | Blocks | Note |
|---|---|---|---|
| 1 | 🔴🔴 **What does `POST /api/audience-sets/suggest/` actually return?** Knowing `bundles` is wrong does not tell us the right shape. **One real response sample is the single most useful thing you can send** | Bundle-construction logic · the effective-CPM calculation · finalising the audience schema | 20, 2 |
| 2 | 🔴 **Is a 3P deal's built-in targeting exposed in structured metadata?** If it exists only in the deal name, the agent would have to parse strings to make buying decisions | **Agent-side deal matching** — the core of Step 2 | 1, 18 |
| 3 | 🔴 **Is multi-market in scope for M1 or M2?** | Step ordering, budget split dimensions, N-call handling, effort estimate | 8 |
| 4 | Which values have **advertiser-level defaults**, and what is the endpoint? | Loading defaults before extraction | 13, 15, 16 |
| 5 | Does `PATCH /api/strategies/{id}/` exist? | The resolution of Open Question 1 | 17 |
| 6 | 🔴🔴 **Is there a CTV-specific endpoint family, and what is in it?** *(`simple-strategies`, the unnamed audience-set endpoint, and possibly others)* | The Create step · and it resolves six items in §4 at once | **Note 24** |
| 7 | Can we get **response samples for the nine v2.0 endpoints**? | Every step that calls them — currently they are names with no contract | §4 |

### Affecting behaviour or figures

| # | Question | Note |
|---|---|---|
| 7 | Can Amazon audiences **and** SSP targeting both apply to the same 3P deal, or is it one or the other? | 1, 19 |
| 8 | How limited is Amazon's targeting on 3P exactly, and does it vary by provider? | 1, 19 |
| 9 | Do **AMC audiences** also apply to 3P inventory, as Amazon audiences do? | 19 |
| 10 | What are the actual Amazon 1P and third-party fee figures? Fixed, or by audience type? | 2 |
| 11 | Is there an audience type with **no** data fee? | 2 |
| 12 | In a mixed-source bundle, what is the typical match-in-both ratio? | 2 |
| 13 | Should bundle grouping be on cumulative reach, relevance score, or something else? | 20 |
| 14 | Will `bundles` support be added later? *("not **currently** supported" suggests it may)* | 20 |
| 15 | Are **Private Auction** deals in scope for CTV M1? *If so, `base_bid` stays conditional rather than removed* | 12 |
| 16 | Should the agent ever auto-select a **PG deal**? | 18, 12 |
| 17 | If several deals match, how should the agent choose? If none match, what should it do? | 18 |
| 18 | Is the frequency cap default weekly, daily or lifetime? | 13, 10 |
| 19 | What counts as *"insufficient frequency"* — how far below target? | 10 |
| 20 | Does `GET /api/strategies/locations/{market}/` support **postcodes**? | 5, 21 |
| 21 | Should **content exclusions** default from the advertiser's brand-safety rules? | 21, 13, 22 |
| 22 | 🔴 **Is the advertiser device setting a default (overridable) or a constraint (locked)?** *Determines whether the repair loop may touch it* | 22 |
| 23 | Which other advertiser settings can be **locked** rather than merely defaulted? | 22 |
| 24 | What is the fallback when an advertiser has no device setting — Connected TV only, or all devices? | 22 |
| 25 | Are `finalised_by` / `finalised_at` needed for audit, or can they be dropped with the approval workflow? | 23 |
| 26 | Can a trader **un-finalise** a plan and keep editing? *(Affects whether loop edges are one-way)* | 23 |
| 27 | When is manager approval expected back — M2? *(Determines how much scaffolding to leave)* | 23 |
| 28 | Is it `/api/simple-strategies/` or `/api/strategies/simple/`, and what payload does it accept? | 24 |
| 29 | Where do the approval-status channel keys come from — deal metadata, or a separate lookup? | 26 |
| 30 | 🔴 **Which other fixed lists in this document should be open?** *(audience data sources · deal types · inventory tiers · durations · currencies)* | 26 |
| 31 | Can the **ad-tag check** run at the very start of the session, given it has no dependency? | 27 |
| 32 | Does creative upload need the strategy ID, or could it also precede Create? | 27 |
| 33 | Can a trader **explicitly skip** tracking and run without conversion measurement? | 27 |
| 34 | Can **budget** also be updated after creation? *(If so, Note 23's re-confirmation loop applies)* | 28 |
| 35 | Is the attribution window configurable? | §2.2 |

### Naming and consistency

| # | Question | Note |
|---|---|---|
| 32 | What status does a created strategy land in — `created` or `draft`? *(The schema and the API example disagree)* | Create step |

*(The *"channel" vs `provider`* naming question is resolved — see the Resolved table above.)*

*(The earlier question about whether the endpoint returns `broad` or `wide` is resolved — Note 20 establishes there is no `bundles` object, so `WIDE` stands.)*

### Carried forward from v2.0, still open

| # | Question | Note |
|---|---|---|
| 33 | Do channel creative review statuses surface in VOW's API, or are they tracked externally? *If external, M1 scope expands* | Platform approval |
| 34 | What is the simplified CTV audience-set creation endpoint called? *(Now part of the wider endpoint-family question — Note 24)* | Create step |
| 35 | Which reach-forecast endpoint applies when — there are two, plus a third TBC | Predict reach |
| 36 | Where is the finalisation audit record stored, if one is needed? No endpoint exists | Note 23 |

*(The question about the manager-approval threshold is now moot — see the Resolved table above.)*

---

# 11. Review Status — Complete

**All 28 comments are incorporated.** What follows is what the review left open, and where the document is still weakest — not because a comment addressed it, but because none did.

## Where the comments landed

| Section | Comments | Read |
|---|---|---|
| §2.3 Inventory tiers | 1 | |
| §2.4 Audience profiles | 1 | |
| §3 Flow comparison | 3 | |
| **Step 1 field matrix** | **12** | 🔴 **43% of the review** — the weakest part of the document |
| Step 2 Inventory | 1 | |
| Targeting (Steps 4–5) | 4 | |
| Finalise Plan | 1 | |
| Create | 1 | |
| Upload creative | 1 | |
| Platform approval | 1 | |
| Tracking setup | 2 | |
| **Credit check · Activate** | **0** | ⚠ **Untouched** — either they were fine, or they were not reached |

**Worth asking:** did the credit-check and activation steps read as correct, or were they simply not reached? They are the only two with no comment, and their response shapes are still unspecified.

## Still weak, and no comment covered it

| Area | Issue |
|---|---|
| **§4 API catalogue** | Endpoint **names** are now in question, not just response shapes (Note 24). Nine endpoints have no contract at all |
| **§5 model quality** | Untyped `list[dict]` in four places; `matching_mode` and `deal_type` should be enums; `DateRangeSchema` dates are strings |
| **§6 state machine** | Needs redrawing entirely — branches with a join, conditional repair edges, `interrupt()` only at platform approval |
| **§7.2 failure protocols** | Three protocols cover a fraction of the real failure cases |
| **Fixed lists** | Audience data sources, deal types, inventory tiers, durations, currencies — all declared closed; Note 26 suggests at least some are open |
| **Level conflation** | Four instances found (data type/widget, format/provider, buying scope/delivery, format/device). A consistent blind spot — likely more |
| 🔵 **Currency of the document** | Comment 23 showed the design had moved since v2.0 was written. Other sections may also be out of date rather than wrong — worth asking, not assuming |

## What to do with this revision

| # | Action |
|---|---|
| **1** | Publish this document, so Wajahat, Vishal and Basil can work from §9 and §12 |
| **2** | Reply to the 28 comments — the reasoning behind each note is in the note itself |
| **3** | Send the **three blocking questions** (§10) as their own short message, separate from the long list. One answer to the CTV-endpoint-family question resolves seven items |
| **4** | Get the **multi-market scope decision** (§10) — it changes step order, budget-split dimensions, call volume and the estimate |

---

# 12. What the Team Should Take From This

Aimed at the three people building against this document.

## Wajahat — state and graph

| What changed | Where |
|---|---|
| **The graph gains a node at the start** — `load_advertiser_defaults`, before extraction | §6, Note 13 |
| **A node was missing** — `confirm_extraction`, which §7.4 calls the most important trust mechanism | §6, §7.4 |
| **`select_inventory` becomes `match_inventory`** — it matches rather than presents | §6, Note 18 |
| **Two nodes merge** — `suggest_audiences` + `apply_targeting` → `propose_targeting` + `refine_targeting` | §6, Note 5 |
| 🔴 **The repair loop's edges are different** — two of the three original actions do not hold for CTV; the replacement has seven levers, several conditional | Step 5, Note 12 |
| 🔴 **Some repair levers can be locked by advertiser policy** — the branch must check `is_locked` before relaxing a targeting value | Note 22 |
| 🔵 **`interrupt()` moves out of plan finalisation** — the only genuine interrupt in M1 is platform creative approval. Plan finalisation is an ordinary turn | Note 23 |
| 🔵 **One loop edge is removed** — plan rejection → Targeting no longer exists | Note 23 |
| 🔵 **Keep `finalise_plan` as a distinct node** — it is the seam manager approval slots back into | Note 23 |
| 🔴🔴 **The post-create tail is three parallel branches with a join at activation** — not a chain. Three independent progress states, and a join condition | Note 27 |
| 🔴 **`current_stage` is replaced** by `current_focus` + an `activation_prerequisites` map — one string cannot express three branches | Note 27 |
| **Loops are branch-local**, except duration mismatch which returns upstream of all three | Note 27 |
| **Six new state fields** | §6 |
| **13 steps become 12** | §3 |

## Vishal — registry

| What changed | Where |
|---|---|
| 🔴 **Every field matrix gains a `Source` column** — eight source types, including advertiser defaults | Step 1 review notes |
| 🔴 **`Type` splits** into data type and source; UI widgets leave the document entirely | Note 11 |
| 🔴 **`TargetingSchema` becomes config-driven** — a targeting-type registry, with audiences as one type | Note 5 |
| 🔴 **Config-driven applies beyond targeting** — the channel list is open too, and other "fixed" lists need auditing | Note 26 |
| 🔄 **`provider` is renamed `channel`** throughout; `ChannelTypeEnum` also renamed | Note 26 |
| **`AdvertiserDefaultsSchema` is new** and did not exist anywhere — confirmed three times | Notes 13, 15, 22 |
| 🔴 **Advertiser values are not all overridable** — each is an `AdvertiserSetting` with `is_locked` and `reason` | Note 22 |
| **`AudienceBundleConstructionSchema` is new** — the three profiles are built here, not by the API | Note 20 |
| **Twelve schema changes in total** | §9 |

## Basil — adaptive canvas

| What changed | Where |
|---|---|
| **Step 1 renders a summary to confirm**, not a form to fill | Note 6 |
| **Step 2 renders a CPM summary**, not a deals table — deal identity is never surfaced | Note 18 |
| **The Targeting step renders applied defaults** with a refine-or-accept action | Notes 5, 21 |
| **Effective CPM may be a range**, not a single figure | Note 2 |
| **Creative approval is one status per channel**, keyed by the channels in the plan — not a fixed set of three | Note 26 |
| 🔒 **Locked settings need a distinct visual state** — pre-filled but not editable, with a reason shown | Note 22 |
| 🔵 **Plan finalisation is a confirmation, not an approval queue** — no pending state, no external approver view | Note 23 |
| 🔴🔴 **After Create, the canvas is a checklist, not a stage** — three independent branches with their own progress. `current_stage` is being replaced | Note 27 |
| ⚠ **`current_focus` needs defined values** — the replacement for `current_stage` still needs an enum before this can be built against | §6, Note 27 |

## Everyone — what is not safe to build on yet

| | Why |
|---|---|
| 🔴 **`POST /api/audience-sets/suggest/`** | The documented response shape is confirmed wrong; the real one is unknown |
| 🔴 **Deal metadata for targeting** | Agent-side deal matching depends on it and it may not be exposed |
| 🔴 **The create endpoint itself** | `POST /api/strategies/` is probably wrong — a CTV endpoint family appears to exist (Note 24) |
| 🔴 **The nine v2.0 endpoints** | Names only, no contracts |
| ⚠ **Multi-market** | Scope undecided; affects step order, budget split and call volume |

**Everything in §9 is safe to start on.** Everything in §10's blocking list is not.

---

---

# ✅ Document status — review complete

**All 28 review comments are incorporated.**

| | |
|---|---|
| ✅ Open questions **resolved** | **4** — ASIN timing · `bundles` response shape · click-through URL · the `channel` naming conflict |
| ✅ Open questions **moot by de-scoping** | **1** — the manager-approval threshold |
| ⚠ Conclusions in earlier notes **corrected in place** | **4** — recorded at the top of this document rather than quietly amended |
| 🎉 Gaps this revision flagged that the review **closed** | **3** — click-through URL · per-channel approval status · partial creative upload |
| 🎉 v2.0 ⚠ markers David **answered directly** | **2 of 5** — and both were blocking |
| 🔴 **Blocking questions remaining** | **3** — see §10 |

**Not every comment was a correction.** One (23) reports a design change made after v2.0 was written — the document was out of date, not wrong. Another (24) is a hint to verify rather than a confirmed fix, and is recorded as unresolved.

## The four changes that matter most for the build

**1. The flow is no longer a chain.** Notes 5, 23, 27 and 28 together take it from 13 rigid steps to roughly **seven sequential steps followed by three parallel branches joining at activation**. The graph has a different shape, `current_stage` is replaced by `current_focus` plus a prerequisites map, and the agent reports what is *outstanding* rather than what is *next*.

**2. The agent infers where it used to ask.** Step 1 goes from fourteen required fields to **none that are both asked and required**. Deals are matched rather than selected. Targeting arrives pre-populated. This is what Principle 2 looks like applied consistently — the principle needed no change, the steps did.

**3. Two whole concepts were missing.** **Advertiser-level defaults** (confirmed three times) had no schema, no endpoint and no state field. And the **config-driven requirement** turned out to be a general principle, not a rule about targeting — it applies to channels too, and probably to other lists still declared closed.

**4. §4 is the largest outstanding risk.** The endpoint **names**, not only the response shapes, are now in question. **A single answer — what is in the CTV endpoint family — resolves seven items.**

---

*Sections 9–12 are review artefacts. Once the blocking questions in §10 are answered, they should be folded into the main body and removed.*






