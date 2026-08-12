# Planning Agent — Poora Flow, Node by Node (Hinglish)

Ye document sirf ek kaam karta hai: **jab trader kuch type karta hai, tab andar exactly kya
hota hai** — kaun si node chalti hai, kya karti hai, kya likhti hai, aur agla kaun chalta
hai. A to Z. Kisi bhi node ka naam yahan search karke uska poora kaam samajh sakte ho.

Code ke saath match karta hai: `app/agent/graph.py` (wiring), `app/agent/gates.py`
(routers), `app/agent/nodes/*.py` (nodes).

---

## 1. Sabse pehle: bada picture

Agent teen alag-alag dimaag ka combination hai, aur **teeno ka kaam alag hai**:

| Layer | Kaam | Kahan |
|---|---|---|
| **LLM (model)** | Sirf 2 kaam — message ko *classify* karna, aur brief se fields *extract* karna. Words choose karta hai. **Koi number khud se nahi bana sakta.** | `app/agent/llm.py`, `voice.py` |
| **Tools / MCP** | VOW ke real data ka access — deals, rate card, audiences, forecast. Har number yahan se aata hai. | `app/tools/mcp/` |
| **Registry** | Do cheezein: (a) **grounded data** — "ye value asli hai ya nahi", (b) **phrasebook** — agent ke saare user-facing words YAML me | `app/knowledge/registry/` |
| **Graph (code)** | Decide karta hai ki kaunsa tool chalega, kaunsi node chalegi, kab rukna hai. Arithmetic aur merging bhi code karta hai. | `app/agent/graph.py`, `gates.py` |

**Golden rule:** model kabhi figure nahi banata. Model sirf batata hai ki trader ne kya
kaha. Number sirf VOW se aata hai. Words registry se aate hain.

---

## 2. Ek turn ka lifecycle (top level)

```
Trader type karta hai
        ↓
POST /api/v1/sessions/{id}/chat        ← app/api/sessions.py
        ↓
Checkpointer se purani state load       ← app/agent/checkpointer.py
        ↓
LangGraph graph.ainvoke(state)          ← poora graph TOP se chalta hai, har turn
        ↓
Nodes chalti hain (neeche detail me)
        ↓
Reply(s) + acknowledgement opener       ← app/agent/acknowledge.py
        ↓
State checkpoint ho jaati hai + JSON response
```

**Sabse important baat:** graph **har turn poora top se chalta hai**. Iska matlab:

- Purani state yaad rehti hai (`extract_fields` merge karta hai, overwrite nahi).
- Har node ko dobara chance milta hai — isliye jo node kuch nahi kehna chahti, use
  chup rehna padta hai. Wo kaam `gates.say()` karta hai (same message dobara nahi bolega).
- Validation dobara compute hoti hai, store nahi hoti. Trader ne galti sudhaari → error
  khud hi gayab ho jaata hai, kisi ne "clear" nahi kiya.

---

## 3. Graph ka poora map

```
START
  ↓
classify_intent  ← Node 0: "ye message kya hai?"
  ├── BRIEF ─────────────→ extract_fields
  ├── SELECTION (audience) → apply_audience
  ├── SELECTION (deal) ───→ apply_deal
  ├── go-ahead ──────────→ select_inventory  /  suggest_audiences
  ├── QUESTION ──────────→ answer_question → END
  ├── NOT_GOOD_ENOUGH ───→ offer_repair → END
  ├── START_OVER ────────→ start_over → END
  ├── NO_ANSWER_YET ─────→ park_question → END
  ├── GEOGRAPHY_INSTEAD ─→ resolve_locations
  └── kuch aur ──────────→ reply → END

extract_fields ──→ validate_basics ──→ validate_slots ──→ suggest_basics ──→ confirm_basics
                        │                    │                  │                  │
                     (blocker)            (blocker)           (ask)             (go-ahead?)
                        ↓                    ↓                  ↓                  ↓
                       ask                  ask                ask         select_inventory
                                                                                   ↓
                                                                        (deal choice — TURN END)
                                                                                   ↓
                                                        apply_deal ──→ suggest_audiences
                                                                                   ↓
                                                                    (audience choice — TURN END)
                                                                                   ↓
                                                      apply_audience ──→ predict_reach
                                                                                   ↓
                                                                          deliver_plan → END
```

**Teen jagah turn deliberately rukta hai** (agent apna question puchhta hai, aur trader ka
jawab wait karta hai):

1. Step 1 complete hone ke baad → "inventory dekhein?"
2. Inventory dikhane ke baad → "kaunsa deal?"
3. Audience options dikhane ke baad → "kaunsi audience?"

Ye teeno jaan-boojh kar hain. Pehle agent khud decide kar leta tha — reviewer ne wahi
reject kiya tha ("agent apna sawaal khud answer kar raha hai").

---

## 4. Node by node — poori detail

### Node 0 — `classify_intent`
**File:** `app/agent/nodes/classify_intent.py`

**Kaam:** Kuch bhi karne se pehle decide karna — *ye message plan ka kya karta hai?*

Ye node pehle nahi thi. Isse pehle har message brief samajha jaata tha, isliye "hello"
likhne par bhi agent khaali slots ki list de deta tha.

**Kya karta hai:**
- Message ko ek **closed list** me se ek label deta hai (khula sawaal nahi puchta):
  `GREETING`, `PLEASANTRY`, `CAPABILITY`, `BRIEF`, `QUESTION`, `SELECTION`, `HELD`,
  `GEOGRAPHY_INSTEAD`, `NOT_GOOD_ENOUGH`, `START_OVER`, `NO_ANSWER_YET`, `OUT_OF_SCOPE`,
  `UNCLEAR`, `EMPTY`
- `SELECTION` hone par ye bhi batata hai kya choose hua: `NARROW` / `BALANCED` / `WIDE` /
  `NONE` (NONE = "audience nahi chahiye" — ye bhi valid jawab hai)
- Pehle **rules** try karta hai (regex), phir LLM. Rules pehle isliye ki "yes", "wider",
  "show me the rate card" jaise chhote jawab deterministic rehne chahiye.
- `awaiting_choice` dekhta hai — matlab "abhi kaunsa sawaal table par hai". Isse "use
  Prime Video" ko naya brief samajhne ki galti nahi hoti, wo ek *jawab* hai.

**Likhta hai:** `intent`, `selection`
**Aage:** `route_by_intent` — 11 possible destinations (upar map me).

---

### Node 1 — `extract_fields`
**File:** `app/agent/nodes/extract_fields.py` — sabse bada node

**Kaam:** Brief samajhna, aur **jo pehle se pata hai wo bhoolna nahi.**

**Do behaviour jo parsing se bhi zyada important hain:**

1. **Accumulate karta hai.** Trader thoda-thoda karke brief deta hai ("50,000" akela
   message me aa sakta hai). Ye node purani state me *merge* karta hai. Agar overwrite
   karta, to budget ka jawab dene par market gayab ho jaati aur conversation kabhi
   complete na hoti.
2. **Confirm karta hai.** Extract karne ke baad ek line ka card wapas bolta hai:
   `CTV_GB_2026-08 · GB · £50,000 · Aug 1-31 · 30s · Awareness`
   Ye trust mechanism hai — jo infer hua wo dikhna chahiye, warna trader correct nahi
   kar sakta. **Card sirf tab bhejta hai jab Step 1 poora ho jaaye aur kuch actually
   badla ho.**

**Kya-kya nikalta hai:** market, flight dates, durations, budget / impression target,
currency, channels (Prime Video etc.), product, goal, audience profile (agar brief me hi
BALANCED bol diya), strategy name.

**Kuch important chhoti baatein (har ek ek bug se aayi hai):**
- `"amazon"` akela channel **nahi** hai. "we sell on Amazon" = product kahan bikta hai,
  ad kahan chalega wo nahi. Channel ka naam Prime Video hai.
- 45s / 40s bhi extract hota hai, chhupaya nahi jaata. Platform 10/15/20/30 bechta hai —
  to 45 ko `unsupported_durations` me rakh kar trader ko bolte hain. **Kabhi round nahi
  karte.** Pehle 45 chup-chaap 30 ban jaata tha — plan badal jaata tha aur kisi ko pata
  nahi chalta tha.
- `"£10,000"` se 10-second creative nahi banega (ye asli bug tha).
- Aadha flight (`sirf start date`) bhi sambhaal ke rakha jaata hai — `flight_start` /
  `flight_end` raw slots. Warna agla turn wahi date dobara puchta tha.
- Currency sirf tab set hoti hai jab symbol/code bola gaya ho. Market se guess karke
  overwrite karna band — "back to the UK" bolne par USD budget chup-chaap GBP ban jaata tha.

**Likhta hai:** saari basics + `strategy_name`, `goal`, `kpi`, `awaiting`, `extraction_method`
**Aage:** `route_after_basics` → `validate_basics` (ya `end` agar message ne kuch badla hi nahi)

---

### Node 1b — `validate_basics` (KNW-02, Vishal ka)
**File:** `app/agent/nodes/validate_basics.py`

**Kaam:** Trader ne jo bola, wo **VOW me actually exist karta hai ya nahi** — live data ke
against check karna.

Ye "complete hai kya" nahi puchta, ye puchta hai **"possible hai kya"**. Do alag sawaal hain,
aur doosra pehle kabhi puchha hi nahi jaata tha.

**Kya check karta hai (grounded registry snapshot se):**
- Market VOW bechta hai? (CN maanga to → "main CN plan nahi kar sakta, ye 4 markets hain")
- Duration platform bechta hai? Us market ke rate card par hai?
- Currency valid hai? Goal/KPI pair valid hai?
- Deal ID asli hai? (invented ID → refuse, aur asli list offer)

**Khaas baat:** jis rule ka input trader ne diya hi nahi, wo rule skip karta hai. Isliye
adhoora brief bhi is node se guzar sakta hai — jo aaya hai wo *usi turn* check ho jaata hai.

**Likhta hai:** `validation_errors` (structured), `validation_checks` (UI panel ke liye — pass
bhi include)
**Aage:** `route_after_grounding` → koi blocker mila to `ask`, warna `validate_slots`

---

### Node 1b (doosra) — `validate_slots`
**File:** `app/agent/nodes/validate_slots.py`

**Kaam:** Wo checks jinka jawab snapshot ke paas nahi hai.

Dono validators ek doosre ka superset nahi hain, isliye dono chalte hain, series me:
- `validate_basics` → "VOW ye bechta hai kya?"
- `validate_slots` → "flight past me hai kya? impression target ko divide karne ke liye
  price hai kya? strategy name unique hai?"

**Likhta hai:** `slot_problems`
**Aage:** `route_after_validation` → blocker ho to `ask`, problem ho to `end`, sab theek to
`suggest_basics`

---

### Node 1c — `suggest_basics`
**File:** `app/agent/nodes/suggest_basics.py`

**Kaam:** Sawaal puchhne se **pehle** ye batana ki behtar kya hoga.

Example: "GB me 15s bhi available hai aur 30s se sasta hai" — ye baat *pehle* aani chahiye,
sawaal ke baad nahi. Sawaal ke neeche advice likhne se lagta hai agent apni hi baat ke upar
bol raha hai.

**Aage:** `ask` / `confirm_basics` / `end`

---

### Node 1d — `confirm_basics`
**File:** `app/agent/nodes/confirm_basics.py`

**Kaam:** Step 1 khatam. **Turn bhi khatam.**

Step 1 complete ho jaana Step 2 shuru karne ki permission nahi hai. Agent puchta hai
"inventory nikaalun?" aur rukta hai. Trader "haan" bolega tabhi aage.

**Aage:** `select_inventory` (go-ahead mila) ya `end`

---

### Node 2 — `select_inventory`
**File:** `app/agent/nodes/select_inventory.py`

**Kaam:** CTV deals match karna, aur phir samajhna ki **har deal actually kya hai.**

**Ye node simple kyun nahi hai:** deal payload me `channel`, `inventory_tier`, `provider`,
`publisher` — in me se **kuch bhi nahi hota** (staging ke saare 369 deals par verify kiya).
Channel sirf free-text `name` ke andar hota hai. Matlab tier ek aisi cheez se nikalta hai jo
khud ek string se nikli hai — isliye dono derivations ke saath **confidence** likhi jaati hai.
Parse kiya hua channel jo API ke channel jaisa dikhe, wo hallucination hi hai.

**Kya karta hai:**
1. `GET /deals/` — market + format ke liye deals (M1 = PREFERRED deals only)
2. `GET /rates/ctv/{market}/` — rate card (kaunsi duration us market me price hoti hai)
3. Ek extra read: market me **total** kitne deals hain — taaki reply keh sake
   "GB me total 9 GB CTV deals hain, tumhaare 30s ke liye 3 relevant hain" — "found one"
   se ye bilkul alag baat hai
4. Har deal ka channel parse → tier classify → CPM, currency, deal type, genre, ad lengths
5. Numbered rows banata hai, 4 facts per row, aur end me **sawaal**:
   "Prime Video ke saath aage badhein, ya GB ka wider inventory dikhaun?"

**Sabse important:** ye node deal **offer** karta hai, **select nahi karta**. `selected_deals`
khaali rehta hai. `deal_options` me options jaate hain aur `awaiting_choice = "deal"`.
Trader ke pick karne par `apply_deal` plan me likhta hai.

**Aage:** `route_after_inventory` → almost always `end` (turn khatam, sawaal screen par hai).
Sirf curated-inventory case me `ask`.

---

### `apply_deal`
**File:** `app/agent/nodes/apply_deal.py`

**Kaam:** Trader ne jo deal pick kiya, use plan me likhna. **Yahi wo node hai jo inventory
plan me daalti hai.**

Samajhta hai: channel ka naam ("Prime Video"), ordinal ("first one", "option 2"), ya sirf
"haan" (lekin sirf tab jab ek hi option offer hua tha — warna "haan" ka matlab clear nahi).

**Likhta hai:** `selected_deals`, `inventory_tier`
**Aage:** END (turn khatam — deal set ho gaya aur agla sawaal usi message me hai)

---

### Node 3 — `suggest_audiences`
**File:** `app/agent/nodes/suggest_audiences.py`

**Kaam:** Teen audience options dikhana, aur phir **ruk jaana.**

VOW ke ~3,400 segments koi haath se nahi dekhta, isliye server suggest karta hai aur agent
exactly teen shapes dikhata hai: NARROW / BALANCED / WIDE.

**Jo number matter karta hai wo effective CPM hai** = deal CPM + audience VCPM fee. Sirf deal
price dikhana galat hai, kaam ki cheez combined figure hai. Ye arithmetic registry me hoti
hai (`Decimal` me, float me nahi — `18.22 + 3.50` binary float me `21.72` nahi hota).

**Fee ke baare me do baatein (review ne correct ki thi):**
- Fee **first-party data** use karne se lagti hai, profile se nahi. Narrow/Balanced/Wide me
  reach aur precision ka farak hai, **price ka nahi**.
- Ek provider ke andar compound nahi hoti; providers ke across stack hoti hai.

**Ye node choose nahi karta.** Pehle khud BALANCED set kar deta tha — matlab "pick one and
I'll forecast" ek jhoota waada tha. Ab `awaiting_choice = "audience"` set hota hai aur turn
rukta hai. Chautha jawab bhi valid hai: teeno mana karke broad chalana.

**Aage:** `route_after_audiences` → `end` (wait), `apply_audience` (choice pehle hi aa gayi),
`ask` (kuch aur outstanding), `predict_reach`

---

### `apply_audience`
**File:** `app/agent/nodes/apply_audience.py`

**Kaam:** Trader ki chuni hui audience plan me likhna — ya jo unhone mana ki hai wo record karna.

**Likhta hai:** `chosen_audience`
**Aage:** `predict_reach` (settle ho gaya) ya `end`

---

### Node 4 — `predict_reach`
**File:** `app/agent/nodes/predict_reach.py`

**Kaam:** Reach forecast, aur **jab forecast possible nahi hai to saaf-saaf mana karna.**

**Honesty rule:** reach forecast **sirf Amazon-owned inventory** par milta hai. Third-party
par nahi. Aise case me agent kehta hai "main reach forecast nahi kar sakta", aur uske badle
impressions batata hai — saath me ye line: "ye impressions hain, unique log nahi."

Ek payload jo kehta hai "reach unavailable" aur phir reach number bhi bhejta hai — wahi
fabricated-reach failure hai jise ye node rokta hai.

**Repair loop ka seam:** reach available hai par bahut kam (viability floor se neeche) →
warning record hoti hai. Trader "ye reach kam lag rahi hai" bolega to `offer_repair` chalega.

**Likhta hai:** `forecast`, `validation_errors`
**Aage:** `deliver_plan`

---

### Node 5 — `deliver_plan`
**File:** `app/agent/nodes/deliver_plan.py`

**Kaam:** Poora plan **ek message me**, aur collecting conversation ka end.

Isse pehle har node bolte-bolte kaam karta hai. Wo plan banate waqt kaam ka hai, record ke
taur par bekaar — trader ko "to humne kya decide kiya?" ke liye 4 turn scroll karna padta hai.
Ye node ek baar sab consolidate karke bolta hai aur `current_stage = "delivered"` set karta
hai (UI ko yahi signal chahiye).

**Ye present karta hai, commit nahi.** VOW me kuch mutate nahi hota. Isliye yahan `interrupt()`
approval gate nahi hai — jo action exist hi nahi karta uske aage gate lagana natak hai.

Jo warnings pehle boli gayi thi, wo summary me **dobara** aati hain. Ek consolidated plan jo
"10-second GB rate card par nahi hai" chhupa de, wahi to approve ho jaata hai kisi aise
insaan se jisne wo baat 4 turn pehle miss kar di thi.

**Aage:** END

---

### `ask_for_missing` — "ask" node
**File:** `app/agent/nodes/ask_for_missing.py`

**Kaam:** Rukna aur **ek** sawaal puchhna.

Jab bhi koi stage `awaiting` me kuch likhta hai, ya validation blocker hota hai, yahan aata hai.

**Do tarah ke sawaal, ek node (`gates.next_question` decide karta hai):**
1. **Conflict pehle** — trader ne jo value di wo VOW accept nahi karta. Ye correction hai,
   request nahi: "CN market me VOW CTV nahi bechta, ye 4 hain" — "market kaunsa hai?" nahi
   (wo unhone bata diya hai). Invalid value baaki sab ko block karti rehti hai, isliye pehle.
2. **Gap** — jo field missing hai. Ek baar me ek, `gates.BASICS` ke order me:
   market → dates → spend → durations.

**"Ek baar me ek" ka matlab wizard nahi hai.** Wizard wo hota hai jo ek screen par sirf ek
field *accept* karta hai. Ye ek puchta hai aur **jo bhi aaye sab le leta hai** — trader "UK,
£8k, September" bolega to teeno absorb honge aur do sawaal skip ho jaayenge.

**Dates + money ek saath puchhe jaate hain** (`PAIRED_ASKS`) — kyunki dono facts trader ke
paas already hain aur insaan ek hi saans me puchta hai.

Har reply me jo bhi mila hai wo naam le kar wapas bolta hai + agla sawaal. Aur ek guard:
**reply me "?" hona chahiye** — model kabhi values bol kar ruk jaata tha ("Lovely, trainers,
GB") aur conversation ka koi raasta nahi bachta tha.

**Aage:** END

---

### `answer_question`
**File:** `app/agent/nodes/answer_question.py`

**Kaam:** Sawaal ka jawab **live data se** dena, plan ko chhue bina.

"GB me kitne deals hain?", "sabse sasta kaunsa hai?", "rate card dikhao" — ye plan change
nahi karte, isliye ye node kuch nahi likhta. Number tool call se aata hai, hardcode nahi.

**Aage:** END

---

### `reply_from_registry`
**File:** `app/agent/nodes/reply_from_registry.py`

**Kaam:** Registry se ek phrase bolna, aur bas.

Greeting, pleasantry, capability question, out-of-scope, unclear, empty — sab ke liye YAML me
phrase hai. **Plan me kuch nahi likhta**, isliye "hi" bolne se plan corrupt nahi hota.

**Aage:** END

---

### `resolve_locations` (Step 5)
**File:** `app/agent/nodes/resolve_locations.py`

**Kaam:** Plan ko country se chhoti jagah par le jaana — "sirf London", postcodes, radius.

Ambiguous postcode ya unconfirmed radius = sawaal. Resolve hui location = ek change jo trader
ko dikhna chahiye **re-forecast se pehle**.

**Aage:** `predict_reach` ya `end`

---

### `offer_repair` (Step 6 repair loop)
**File:** `app/agent/nodes/offer_repair.py`

**Kaam:** Trader kehta hai "ye reach kam lag rahi hai" → ek lever offer karo aur ruko.

Pehle ye message `BRIEF` samajha jaata tha, koi field nahi milti thi, aur agent bolta tha
"isse plan me kuch nahi badla" — us insaan ko, jisne abhi bataya ki plan theek nahi hai.

Ek lever offer karta hai (audience wider karna) aur rukta hai. Trader ki "haan" `SELECTION`
ban kar aati hai, `apply_audience` apply karta hai, aur wahan se `predict_reach` ka edge
re-forecast kar deta hai.

**Aage:** END

---

### `park_question`
**File:** `app/agent/nodes/park_question.py`

**Kaam:** "Pata nahi abhi", "tum decide karo" — trader ko na jaanne ka haq hai.

Ye na refusal hai na answer — ye aage badhne ki permission hai. Pehle ye `UNCLEAR` ban jaata
tha, matlab jo insaan bilkul clear tha usse kaha jaata tha ki wo clear nahi tha. Field
outstanding rehti hai (jhooth nahi bolte), par turn aage badh jaata hai.

**Aage:** END

---

### `start_over`
**File:** `app/agent/nodes/start_over.py`

**Kaam:** Plan phenk dena — jaan-boojh kar, jab trader kahe.

Iski apni intent hai kyunki **koi doosra path ye nahi kar sakta**: baaki sab purani state me
merge karte hain, jo correction ke liye bilkul sahi hai aur reset ke liye bilkul galat.
"scrap that, let's start again" ka jawab pehle "isse plan me kuch nahi badla" hota tha — aur
sach me kuch nahi badalta tha, to agla brief purane plan ka product, channel aur currency
inherit kar leta tha.

Kya clear hota hai aur kya rehta hai — `_CLEARED` / `_KEPT` me likha hai (advertiser ki
currency aur exchange rates rakhe jaate hain, wo `GET /user` se aaye hain, plan se nahi).

**Aage:** END

---

## 5. Routers (gates) — kaun kahan bhejta hai

Router LangGraph me **state padh sakta hai, likh nahi sakta.** Node `awaiting` set karti hai;
router sirf decide karta hai agla kaun.

| Router | Kahan se | Decision |
|---|---|---|
| `route_by_intent` | classify_intent | intent ke hisaab se 11 destinations |
| `route_after_basics` | extract_fields | `validate_basics`, ya `end` agar kuch badla hi nahi |
| `route_after_grounding` | validate_basics | blocker → `ask`, warna `validate_slots` |
| `route_after_validation` | validate_slots | blocker → `ask`, problem → `end`, warna `suggest_basics` |
| `route_after_suggestions` | suggest_basics | `ask` / `confirm_basics` / `end` |
| `route_after_basics_confirmed` | confirm_basics | go-ahead → `select_inventory`, warna `end` |
| `route_after_inventory` | select_inventory | blocker → `ask`, curation → `ask`, warna `end` |
| `route_after_audiences` | suggest_audiences | blocker → `ask`, choice pending → `end`, choice aa gayi → `apply_audience` |
| `route_after_audience_choice` | apply_audience | `predict_reach` ya `end` |
| `route_after_locations` | resolve_locations | `predict_reach` ya `end` |

**Do rule jo har router par lagte hain:**

1. **Blocker pehle.** Agar kisi ne validation blocker record kiya hai jo abhi kisi ne bola
   nahi, to `ask` par jaana hai. Warna turn khatam ho jaayega aur trader ko wajah pata hi
   nahi chalegi. Bina boli hui validation failure, repeat sawaal se zyada buri hai.
2. **Jo sawaal node ne khud puch liya, uske liye `ask` par nahi jaate.** Inventory dead-end
   aur audience options — dono apna behtar sawaal already puch chuke hain; `ask` sirf ek
   dhundhla duplicate add karta.

---

## 6. Support files — jo nodes use karte hain

| File | Kaam |
|---|---|
| `state.py` | `PlanningAgentState` — poora plan + `awaiting`, `awaiting_choice`, `validation_errors`, `validation_checks`, `last_said` |
| `gates.py` | Kya outstanding hai (`missing_basics`), kya already answer ho chuka (`already_chose_*`), routers, `say()`, `record()` |
| `stages.py` | Har outstanding sawaal ka **contract** — kya puch raha hai, kaunse jawab accept karta hai, kaunsa jawab kahan bhejta hai. Classifier prompt aur router **dono** yahi padhte hain, isliye wo aapas me drift nahi kar sakte |
| `acknowledge.py` | Turn ke pehle reply par ek rotating opener ("Perfect.", "Got it.", "Nice one."). Rotate hota hai — teen turn ek jaisa khulna template jaisa lagta hai |
| `voice.py` | Model se words lena, par **figure guard** ke saath: jo number notes me nahi hai wo reply me aaya to composed version bhej dete hain |
| `presentation.py` | Layout — bullets, options block, sentence joining |
| `formatting.py` | `money()`, `spend()`, `count()`, `approx()` — **poore codebase me money ka ek hi formatter**. Card me "£15,000" aur read-back me "15,000.00 GBP" — ek hi figure do tarah se likha gaya tha, isliye ye rule test se enforce hota hai |
| `knowledge/registry/` | Grounded data (kya asli hai) + phrasebook (kya bolna hai). Trader ko dikhne wala koi bhi text Python me nahi hai |
| `core/logging.py` | Step-wise terminal logger — kaun si node chali, kaunsi file, kya trigger hua |

---

## 7. Do poore examples

### Example A — complete brief, ek message me

**Trader:** "CTV campaign in the UK for October 2026, £50,000, 30 second creatives"

```
classify_intent    → BRIEF
extract_fields     → market GB, flight Oct 1-31, budget £50,000, duration 30s
                     card bolta hai: CTV_GB_2026-10 · GB · £50,000 · Oct 1-31 · 30s · Awareness
validate_basics    → GB bikta hai ✓  30s bikta hai ✓  GB rate card par 30s hai ✓  → validate_slots
validate_slots     → flight future me hai ✓  budget valid ✓  → suggest_basics
suggest_basics     → "15s bhi available hai aur sasta hai" (agar relevant ho)
confirm_basics     → "Inventory nikaalun GB ke liye, rate card ke saath?"  ← TURN KHATAM
```

**Trader:** "haan"

```
classify_intent    → go-ahead → select_inventory
select_inventory   → 9 deals total, 30s ke liye 3 relevant, numbered rows + CPM
                     "Prime Video ke saath aage badhein, ya wider inventory dekhein?"  ← TURN KHATAM
```

**Trader:** "Prime Video"

```
classify_intent    → SELECTION (deal), awaiting_choice = "deal"
apply_deal         → selected_deals = [Prime Video 30s], inventory_tier = AMAZON_OWNED  ← TURN KHATAM
```

**Trader:** "audiences dikhao"

```
classify_intent    → go-ahead → suggest_audiences
suggest_audiences  → NARROW / BALANCED (recommended) / WIDE, effective CPM ke saath
                     "Kaunsi chahiye? Ya skip karke broad chalayein — koi data fee nahi"  ← TURN KHATAM
```

**Trader:** "balanced"

```
classify_intent    → SELECTION = BALANCED
apply_audience     → chosen_audience set
predict_reach      → VOW se forecast: impressions, unique reach, frequency
deliver_plan       → poora plan ek message me → END
```

### Example B — aadha brief (demo ke liye yahi behtar hai)

**Trader:** "We're launching a new running shoe line, want to run something on Prime Video in the UK"

```
classify_intent    → BRIEF
extract_fields     → product "running shoe line", channel Prime Video, market GB
                     dates, budget, duration — teen missing
                     card nahi bhejta (Step 1 adhoora hai)
validate_basics    → GB ✓ (baaki rules ka input nahi aaya — skip)
validate_slots     → kuch galat nahi
suggest_basics     → kuch kehne layak nahi abhi
ask                → "Running shoes — nice. Kab chalana hai (start aur end date),
                      aur budget kitna soch rahe ho?"                        ← TURN KHATAM
```

Dhyaan do: **Prime Video dobara nahi puchha jaata.** Trader ne bata diya hai. Ye wahi bug
tha jise `gates.already_chose_inventory()` fix karta hai — sawaal ye nahi ki "ye choice hai
kya", sawaal ye hai ki **"ye choice abhi khuli hai kya"**.

**Trader:** "October 1 to 31, £15,000"

```
extract_fields     → dates + budget merge, sirf duration missing
ask                → "Perfect — Oct 1-31, £15k. Creative length kya hai — 10, 15, 20 ya 30 seconds?"
```

**Trader:** "30 seconds"

```
extract_fields     → duration set, Step 1 poora → card bhejta hai
...                → wahi flow jaisa Example A me "haan" ke baad
```

---

## 8. Poore system par lagne wale rules

Ye rules har node par lagte hain. Naya node likhte waqt inhe follow karna hai:

1. **Teen tarah ke action, aur category confuse karna hi asli bug hai:**
   - **FETCH** — padho, kabhi puchho mat (deals, rate card, account currency)
   - **FILL** — default lagao, par *mark* karo ("Awareness (default)")
   - **CHOOSE** — trader ka decision. Recommend karo, apply kabhi nahi
2. **Jo sawaal conversation me already answer ho chuka, uska gate nahi khulna chahiye.**
   Test ye nahi ki "ye choice hai kya" — test ye hai ki **"ye choice abhi khuli hai kya"**.
3. **Bina bola hua filter, trader ki taraf se liya gaya decision hai.** 9 me se 3 deals
   dikhaye to bolna padega ki 9 the.
4. **Agent wo action promise nahi kar sakta jo wo le nahi sakta.** Jhoota action = jhoota
   number, ek level upar.
5. **Fallback jo maan leta hai ki trader raazi hai, wo bina consent action le raha hai.**
6. **Model number introduce nahi kar sakta.** Number VOW se, words registry se, arithmetic
   aur merging code se.
7. **Ek turn me ek sawaal**, par jawab me jo bhi aaye sab absorb karo.
8. **Har node ka apna ek kaam.** Do nodes ko merge karne se replies apni hi baat ke upar
   bolne lagti hain — rejection ke neeche advice, ya puche gaye sawaal ke neeche price table.

---

## 9. Terminal logger kaise padhein

Structured logger har turn ko step-wise dikhata hai:

```
USER  "30 seconds"
 ├─ step 1  classify_intent      classify_intent.py   → BRIEF
 ├─ step 2  extract_fields       extract_fields.py    → durations=[30]
 ├─ step 3  validate_basics      validate_basics.py   → 5 checks, 0 blockers
 ├─ step 4  validate_slots       validate_slots.py    → ok
 ├─ step 5  suggest_basics       suggest_basics.py    → nothing to add
 ├─ step 6  confirm_basics       confirm_basics.py    → asks for go-ahead
 └─ SAID   "Perfect. Here's what I've got: ..."
```

Har line batati hai: kaunsi node chali, kaunsi file me hai, aur usne kya decide kiya. Jab
response galat aaye, isse pata chalta hai **kis step par** galat hua.
