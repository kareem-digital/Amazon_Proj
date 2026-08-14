# Planning Agent Ka Code Flow

**VOW Platform · PLN-01 / VA-191**

Har node kis liye hai, ek turn me kya-kya chalta hai, `classify_intent` se `understand` tak
kya badla aur kyun, aur registry me kya add hua. Poora flow — taaki kisi ko bhi samjhaya
ja sake.

---

## Contents

| | |
|---|---|
| 01 | [Ek turn me kya hota hai](#01--ek-turn-me-kya-hota-hai) |
| 02 | [classify_intent vs understand](#02--classify_intent-vs-understand) |
| 03 | [Saare nodes ka purpose](#03--saare-nodes-ka-purpose) |
| 04 | [Routers — graph decide kaise karta hai](#04--routers--graph-decide-kaise-karta-hai) |
| 05 | [stages.py — sunne ki layer](#05--stagespy--sunne-ki-layer) |
| 06 | [Registry aur validate.py](#06--registry-aur-validatepy) |
| 07 | [Data kahan se aata hai](#07--data-kahan-se-aata-hai) |
| 08 | [Kya hata, kya juda](#08--kya-hata-kya-juda) |

---

## 01 · Ek turn me kya hota hai

User UI se message bhejta hai → `POST /api/v1/sessions/chat` → `app/api/sessions.py`.
Wahan se LangGraph ka state machine chalta hai. State `session_id` ke against checkpoint hoti
hai, isliye agla message pichhle plan ko yaad rakhta hai.

```
START
  │
  ├─> extract_fields              ← entry node, hamesha yahi pehla
  │     │   understand.read_message()   ← EK model call: intent + slots dono
  │     │   _merge()                    ← naya value purane plan me merge
  │     ▼
  │   route_after_message               ← ye turn ka EK HI fork hai
  │
  ├─ BRIEF ──────> validate_basics > validate_slots > suggest_basics
  │                      │                                  │
  │                      └─ galat value? ──> ask            ▼
  │                                                   confirm_basics ─> END
  │
  ├─ SELECTION ──> select_inventory / apply_deal / apply_audience
  │                suggest_audiences / resolve_locations / create_strategy
  │
  ├─ QUESTION ───> answer_question ─> END
  ├─ GREETING ───> reply (registry phrasebook) ─> END
  ├─ NO_ANSWER ──> park_question ─> END
  ├─ START_OVER ─> start_over ─> END
  └─ NOT_GOOD_ENOUGH ─> offer_repair ─> END

Har node ke baad ek router hota hai. Router decide karta hai:
turn yahin khatam ho, ya agla node chale.
```

Do baatein jo poore graph par lagti hain.

**Pehli — model kabhi decide nahi karta ki kaunsa tool call hoga.** Wo graph ka kaam hai. Model
sirf do cheezein karta hai: message ko label deta hai, aur us me se values nikalta hai.

**Dusri — reply ke shabd registry se aate hain** jahan possible ho, model se nahi.

Turn khatam kab hota hai — jab kisi node ne `awaiting` ya `awaiting_choice` set kar diya,
matlab ab user ka jawab chahiye. Ye do fields hi poore flow ka "abhi kya pooch rahe hain" hain.

---

## 02 · classify_intent vs understand

Ye sabse bada architectural change hai, isliye detail me.

### Pehle kya tha

Do alag nodes the, aur dono model ko call karte the — **ek hi message par, do baar**:

| Node | Sawal jo poochta tha |
|---|---|
| `classify_intent` | Ye message plan ke saath **karta kya hai?** — BRIEF hai, SELECTION hai, QUESTION hai, greeting hai? |
| `extract_fields` | Ye message **carry kya karta hai?** — market, budget, dates, duration, KPI? |

### Issue — jo maine measure kiya

`logs.json` ki ek real session me: classify ne **1602 ms** liye, extract ne **1707 ms** — back
to back, dono ne ~1924 input tokens bheje. Turn total **4713 ms**, jisme **99.6% sirf model
latency thi**. Baaki har node 4 ms ya usse kam.

Matlab problem node count nahi thi — **call count thi.** Ek message ke liye do round trips,
do prompts, lagbhag same context.

### Merge karna aasan kyun nahi tha

Dono prompts ki **context requirement ulti thi**, aur dono sahi the. Yahi wo hissa hai jo
change karne se pehle samajhna zaroori hai:

- **classify ko context chahiye tha.** "30 seconds" akela aaye to BRIEF hai. Lekin agar agent
  ne abhi poocha tha "creative length kya hai?" to wahi shabd ek ANSWER hai. Message akela ye
  decide nahi kar sakta.

- **extract ko context nahi chahiye tha.** Ise ek baar known values de kar merge karne ko kaha
  gaya tha. Ye fresh brief aur addition me farq nahi kar paaya, to dono ko union kar diya —
  France ka brief pehle tha, phir user ne likha "£10,000 in the US for September", aur wapas
  aaya `Markets: FR, US`. Prompt me "ignore the context" likhne se fix nahi hua. Context
  *hatane* se hua.

### Resolution

"Context" actually **do alag cheezein** thi:

- **Kya poocha gaya tha** — ek label, jaise "the budget", "audience", "deal". Ye safe hai, aur
  classification ko yahi chahiye.
- **Kya pehle se pata hai** — actual values. Yahi extraction ko contaminate kar raha tha.

### Ab kya hai — `understand.read_message()`

Ek structured-output call jo dono jawab ek saath deti hai: intent, selection, aur har slot jo
message ne set kiya.

Prompt me **sirf** ye jaata hai — kaunsa sawal khula hai (label), aur ek boolean ki plan exist
karta hai ya nahi. **Ek bhi slot value prompt me nahi jaati.** Model wo value copy hi nahi kar
sakta jo usne dekhi hi nahi, aur purani values aage le jaana `extract_fields._merge` me
deterministic rehta hai.

### Baaki kya-kya isme aaya

- **Rules pehle chalte hain, model baad me.** `classify_by_rules` greeting, blank message, bare
  "yes", stage-specific answers — ye sab bina model ke decide karta hai. Agar rules ne decide
  kar liya *aur* wo intent plan ko likh nahi sakta, to model call hoti hi nahi. Us path par ek
  turn **64 ms** me khatam hua, 4713 ms ke against.

- **Off-track guarantee code me hai, prompt me nahi.** `WRITES_TO_PLAN` me sirf chaar intents
  hain. Greeting, pleasantry, capability question, weather, unclear — ye sab `understood = None`
  ke saath aage jaate hain, model ne kuch bhi return kiya ho. "hi" se state write tak koi rasta
  hi nahi hai.

- **Model off-topic message ko label karta hai, answer nahi karta.** Reply registry phrasebook
  se aati hai — matlab agent weather report de hi nahi sakta, uske paas uske shabd hi nahi hain.

- **Patterns model ke neeche floor hain.** Model jo slot khali chhod de, wo patterns bhar dete
  hain. "United Kingdom" akela message model khali laut aya tha — patterns use pehchante hain,
  isliye ab dono chalte hain aur model har tie jeetta hai.

- **Model na ho ya fail ho jaye** to patterns chalte hain aur message BRIEF maana jaata hai. Ek
  asli brief ko refuse karna, ek greeting ko over-parse karne se zyada bura hai.

### To `classify_intent.py` file abhi bhi kyun hai?

Kyunki node aur module do alag cheezein hain.

**Node hata diya gaya hai** — wo dead pada tha, graph me register hi nahi tha, phir bhi apna
poora system prompt aur apni structured-output call leke baitha tha. **382 lines nikali** (node,
`_classify_with_llm`, `_system_prompt`, `IntentDecision`).

Lekin usi file me jo zinda hai wo `understand` use karta hai: `classify_by_rules`,
`looks_like_a_brief`, `looks_like_a_question`, `PHRASE_FOR_INTENT`, `IntentLabel` /
`SelectionLabel`. Isliye file rahi. File ka naam stale hai — rename alag change hai.

> **Isko rakhne ka asli cost.** Dead copy **drift kar chuki thi.** Uske andar `offered` list
> sirf `deal_options` padh rahi thi. Jo fix maine kiya tha — ki jo channel already plan me hai
> use dobara "discover" na maana jaye — wo `understand.py` me gaya, fossil me nahi. Do copies
> ek din disagree karti hi hain.

---

## 03 · Saare nodes ka purpose

Graph me **19 nodes** register hain (`app/agent/graph.py`). Flow chart ke step ke hisaab se
grouped:

### Step 1 — brief samajhna aur ground karna

**`extract_fields`** — *Node 1, entry point*
Har turn ka pehla node. `understand.read_message()` call karta hai, phir jo mila use plan me
merge karta hai. Merge additive hai ya replacing — ye ek readable rule decide karta hai, model
nahi. Aur agar market ya duration badla to uske neeche ki har cheez (deals, tier, audiences,
forecast) invalidate ho jaati hai, kyunki purane length ke liye match ki gayi inventory naye
length par jhooth hai.

**`validate_basics`** — *Node 1b, Vishal ka grounded check*
Jo extract hua wo **VOW actually bechta hai ya nahi** — live registry snapshot ke against.
Market, currency, duration, goal/KPI, aur jo channel user ne naam liya. Ye KNW-02 ka code hai.

**`validate_slots`** — *Node 1b, hamara check*
Zero-hallucination ka doosra hissa: **user ne value di isliye wo verified nahi ho jaati.** Past
dates, aisi duration jo platform bechta hi nahi, budget jo credit se zyada hai. Snapshot ke paas
jinka data nahi, wo yahan check hote hain.

**`suggest_basics`** — *Step 1b*
Validation batati hai kya **galat** hai. Ye batata hai kya **behtar** hoga — aur har suggestion
kisi fetch kiye hue number se padhi jaati hai. "30 seconds is popular for CTV" invented hai,
chahe sach ho, isliye wo yahan nahi bolti.

**`confirm_basics`** — *Step 1 ka ant*
Plan card print karta hai aur **turn khatam kar deta hai.** Pehle graph ek hi turn me Step 1, 2
aur 4 chala deta tha — user ek brief type karta tha aur wapas confirmation + inventory + teen
audience options ek saath aa jaate the. Teen steps, pehle wale par haan kehne se pehle.

**`ask`** — *ask_for_missing*
Jab bhi kisi node ne `awaiting` me kuch daala, ye node wahan divert hota hai. **Ek baar me ek hi
cheez poochta hai** — aur jo cheezein natural taur par saath jaati hain unhe pair karta hai
(budget aur dates).

### Step 2 & 3 — inventory aur budget split

**`select_inventory`** — *Node 2*
**Deals fetch karta hai aur teen tiers me baantta hai** — ye poore flow ka primary fork hai,
kyunki tier decide karta hai reach forecast possible hai ya nahi. Rate card bhi padhta hai,
taaki wo channels bhi dikh sakein jinki price hai par deal nahi. **Offer karta hai, select nahi
karta.**

**`apply_deal`** — *+ Step 3 andar hi*
User ne jo deal choose ki, wo plan me likhta hai. Naam se, ya position se ("the first one"), ya
"both". **Step 3 ka budget split yahin rehta hai** — split tabhi banta hai jab do se zyada deal
ho, isliye wo Step 2 ka substep hai, apna step nahi. Accept / adjust / skip — teeno ke apne
jawab hain.

### Step 4 — audience

**`suggest_audiences`** — *Node 3*
Server se suggestion mangwata hai aur **teen shapes** dikhata hai — narrow, balanced, wide — har
ek ki pool size aur effective CPM ke saath. Phir **ruk jaata hai.** Pehle ye khud BALANCED set
kar deta tha aur aage badh jaata tha, matlab agent apna hi sawal khud answer kar raha tha.

**`apply_audience`**
User ka jawab apply karta hai. **Teen outcomes**: ek profile choose hui, teeno decline hui (ye
valid plan hai, koi failure nahi — aur isme data fee nahi lagti), ya jawab ambiguous tha to
dobara pooch lo. Default set karna yahan sabse bada bug hota.

### Step 5 & 6 — targeting, forecast, repair

**`resolve_locations`** — *Step 5*
Plan ko country se chhoti jagah par le jaata hai. **Chaar shapes**: place name, postcode, radius
(address + distance), aur exclusion. Radius ek nayi location *mint* karta hai platform par,
isliye create karne se pehle confirm poochta hai. "No extra targeting" bhi isi node me record
hota hai — kyunki wo ek jawab hai, absence nahi.

**`predict_reach`** — *Node 4*
Reach forecast — aur jahan possible nahi wahan **saaf mana karta hai.** Forecast sirf Amazon
inventory par milta hai; Netflix/Disney+ ke liye impressions de sakte hain
(budget ÷ CPM × 1000) par reach nahi, aur wo bolna padta hai. Reach ki **do ceilings** hain —
impressions ÷ frequency, aur audience size × location share — jo bind karti hai wahi
`limited_by` me jaati hai.

**`offer_repair`** — *Step 6 ka loop*
User bole ki forecast kaafi nahi hai, to ye lever offer karta hai — wider audience, zyada
budget, broader location — real numbers ke saath, umeed ke saath nahi.

### Step 7 & 8 — plan, approval, creation

**`deliver_plan`** — *Node 5*
Poora plan ek jagah — campaign, market, location, flight, creative, budget, goal, inventory,
audience, forecast, aur reach curve. Baaki sab nodes kaam karte-karte bolte hain; ye ek baar
consolidated bolta hai, taaki user ko chaar turns scroll na karne pade. Aur yahin approval ka
sawal aata hai.

**`create_strategy`** — *Step 8*
**Poore graph ka pehla node jo VOW me kuch likhta hai.** Isi wajah se Step 7 ka approval gate
iske theek saamne hai aur yahan kuch bhi auto-retry nahi hota. Draft nahi banata — client ka
apna instruction hai ki draft sirf wizard ke liye hai. Pehle audience set create karta hai, phir
strategy, phir locations set karta hai.

### Kabhi bhi chal sakte hain

**`answer_question`**
Sawal ka jawab **live data se**. Rule do hisso me: numbers, counts, lists, prices — hamesha tool
call se; definitions aur explanations — registry se. Isliye "28 deals" jaisa constant kabhi
hardcode nahi ho sakta. ~30 question types handle hote hain.

**`park_question`**
"Pata nahi" ek valid jawab hai. Pehle iska reply tha "Sorry, samajh nahi aaya" — jo un logon ko
mil raha tha jinhone bilkul saaf jawab diya tha. **Park karna skip karna nahi hai:** field abhi
bhi required hai, bas ab wo blocker nahi hai, aur agent ek recommendation offer kar sakta hai.

**`start_over`**
Baaki poora graph **merge** karta hai — ek brief kai messages me aata hai. Ye ek jagah hai jahan
merge galat hai. "scrap that, start again" ka jawab "that didn't change anything" tha, jo
technically sach tha aur uska matlab tha purana plan chup-chaap zinda hai.

**`reply`** — *reply_from_registry*
Sirf ek registry phrase lookup karta hai aur wahi return karta hai. Kuch compose nahi karta,
kuch format nahi karta. Isi wajah se guarantee testable hai: greeting, refusal aur capability
answer ke shabd ek file me hain jinke owner content log hain, Python me nahi.

---

## 04 · Routers — graph decide kaise karta hai

Har node ke baad ek router function hota hai (`app/agent/gates.py`). Router state padhta hai aur
ek string return karta hai — agla node ka naam ya `END`. **Model kabhi router nahi hota.**

| Router | Kya decide karta hai |
|---|---|
| `route_after_message` | **Turn ka ek hi fork.** Pehle do routers the — ek extraction se pehle, ek baad me — kyunki do nodes message padhte the. Ab ek node padhta hai, to ek fork sab decide karta hai. |
| `route_after_basics` | Unconditional — validation branch nahi hai, agla step hai. "Complete" aur "possible" alag cheezein hain. |
| `route_after_grounding` | Grounded check ne kuch reject kiya to `ask`, warna doosra validator. |
| `route_after_validation` | Teen raste, jo jitna jaldi rokta hai us order me. **Galat value, missing value se pehle poochi jaati hai.** |
| `route_after_suggestions` | Suggestion dono taraf useful hai, isliye router khud decide nahi karta ki wo blocker hai ya nahi. |
| `route_after_basics_confirmed` | Turn khatam, inventory ke sawal par. |
| `route_after_inventory` | Hamesha turn khatam — **Step 2 ek step hai, staging post nahi.** |
| `route_after_deal_choice` | Deal pehle aa gayi aur brief adhoora hai to baaki brief maango — warna audience ka sawal. |
| `route_after_audiences` | Options screen par aa gaye, turn khatam. Sawal us message me already poocha ja chuka hai. |
| `route_after_audience_choice` | Choice settle ho gayi to forecast. Decline bhi settle hai. |
| `route_after_forecast` | Plan deliver karo — **jab tak Step 5 ka sawal khula na ho.** Ye pehle unconditional edge thi, isi wajah se reply chaar block lamba ho jaata tha. |
| `route_after_locations` | Plan me pehle se forecast tha to dobara forecast karo, warna turn khatam. |

> **Ek rule jo baar-baar bacha.** Sawal ye nahi hai ki *"kya ye ek choice hai"* — sawal ye hai
> ki ***"kya ye choice abhi bhi khuli hai"***. User ne brief me hi Prime Video bol diya to
> "inventory dhoondhun?" poochna, ek answered sawal dobara poochna hai.

---

## 05 · stages.py — sunne ki layer

Ek problem jo poore flow me repeat hoti thi: **same shabd, alag jagah, alag matlab.**

"show me the rate card" kahin bhi ek reasonable question hai — par deal step par wo *is* rate
card ki baat hai, definition ki nahi. "wide" tab selection hai jab teen options screen par hain,
warna brief ka hissa hai.

`app/agent/stages.py` me har khule sawal ke liye ek `Stage` hai, aur har stage teen cheezein
declare karta hai:

- **`asks`** — situation ka description, jo classifier ke prompt me verbatim jaata hai.
  Instruction ki tarah nahi, situation ki tarah likha gaya.
- **`phrases`** — wo phrasings jinka is stage par ek hi matlab hai, bina model ke. **Order matter
  karta hai** — "keep it broad" me audience shabd nahi hai par "no audience" me hai, aur zyada
  specific reading ko jeetna chahiye.
- **`accepts`** — kaunsa reading kaunse node par jaayega.

Abhi ke stages: `basics`, `deal`, `budget_split`, `inventory`, `audience`, `targeting`,
`unavailable_inventory`, `approval`, `product_location`, `location`.

> **Kyun ye alag file hai.** Classifier aur router **dono** yahi contract padhte hain. Agar stage
> kehta hai ki wo "widen" sunta hai, to test file check karti hai ki "widen" ke liye ek handler
> bhi ho. Warna wahi bug banta hai jo teen alag jagah bana: agent ek shabd offer karta hai jise
> wo khud nahi samajhta. **Jo darwaza agent kholta hai, uske peeche kamra hona chahiye.**

---

## 06 · Registry aur validate.py

Registry (`app/knowledge/registry/`) Vishal ka lane hai — KNW-02. Ye har turn par ek **grounded
snapshot** banata hai: markets, currencies, durations, deals, rate cards, audience profiles,
targeting types. Agent ka koi bhi claim isi snapshot se ground hota hai.

### Do validators, do alag sawal

- **`SnapshotValidator`** — payload ki shape check karta hai. Ek missing *required* field
  breaking hai (raise), ek extra field additive hai (log). Yahi additive-vs-breaking ka farq hai
  bina compatibility engine ke.
- **`StepwiseCTVValidator`** — **19 rules**, flow chart ke step ke hisaab se. Market, currency,
  durations, goal/KPI, flight dates, product categories, deal selection, curation requirements,
  split method, audience choice, matching mode, targeting, forecast shape,
  plan-ready-for-approval.

### Maine isme kya add kiya

#### `validate_requested_channels()` — naya rule

User jo channel maange, wo platform carry karta hai ya nahi — **plan bharne se pehle, baad me
nahi.** Pehle "run something on Zee TV in the UK" ka jawab tha *"Perfect. United Kingdom, Zee TV.
Dates kya hain?"* — matlab user ne budget, dates, duration sab ek aise channel ke liye diya jo
khareeda hi nahi ja sakta, aur pata do turn baad chala.

Do sources padhta hai, kyunki dono alag sawal ka jawab dete hain:

- **deals** — abhi buyable inventory
- **rate card** — price hai, deal nahi. GB me Netflix yahan hai, aur use unavailable kehna galat
  hota.

Wording bhi deliberate hai: *"not on this platform"*, kabhi *"not in the UK"* nahi. Zee TV
Britain me chalta hai; VOW use nahi bechta. Doosri baat kehna duniya ke baare me ek galat claim
hai.

Aur **snapshot load na ho to ye chup rehta hai.** Dono khali hone ka matlab fetch fail hua, ye
nahi ki VOW kuch bechta hi nahi — 403 ke bharose kisi ka channel unavailable bol dena ulti taraf
ki wahi galti hai.

#### `validate_target_markets()` — bug fix

`market_name(row)` tabhi call hota hai jab row ek 2-letter code ho. Warna user ke apne shabd
wapas jaate hain. Pehle ye non-code value ko bhi normalize karne ki koshish karta tha aur message
me galat naam chala jaata tha.

#### `registry/targeting.py` + `data/targeting_types.json` — naya, config-driven

Client ka apna instruction hai: *"this targeting list frequently changes so it should be easy to
add new targeting types"* aur *"must be config-driven, not hard-coded"*. To paanch types JSON me
hain, har ek declare karta hai ki uski values kaunsa tool deta hai aur kaise padhni hain.

**Boundary jaan-boojh kar do-tarfa hai.** Agent kya *offer* kar sakta hai — wo config se badal
sakta hai. Kya *submit* kar sakta hai — wo nahi, kyunki VOW ke schema me paanch named fields hain
aur value tabhi bheji ja sakti hai jab uske liye field ho. Naya type config se offerable ban
jaata hai, aur submittable tab banta hai jab VOW me field aaye. Iske alawa kuch bhi pretending
hota.

> **Verify kaise kiya ki registry sach me chal rahi hai.** Runtime par fixture badal kar. Deal ka
> CPM 28.88 se 77.77 kiya aur reply ke numbers badle. `reach_share` 0.14 se 0.90 kiya aur
> forecast badla. Agar kahin static hota to reply hilti hi nahi. Har turn par
> `GroundedRegistrySnapshot` banta hai, 9 MCP tools call hote hain, aur integrity check 0 errors
> deta hai.

---

## 07 · Data kahan se aata hai

Rule simple hai aur poore codebase par lagta hai: **koi bhi number static nahi hai.** Agar reply
me koi figure hai, wo ya tool call se aaya hai ya registry se.

- **MCP tools** (`app/tools/mcp/`) — VOW ke endpoints ka wrapper. `LIST_DEALS`, `CTV_RATE_CARD`,
  `SUGGEST_AUDIENCES`, `REACH_FORECAST`, `CREATE_AUDIENCE_SET`, `CREATE_STRATEGY`,
  `SET_STRATEGY_LOCATIONS`, `STRATEGY_CHOICES`, aur baaki.

- **Mock client** (`mock.py`) — local dev ke liye. Deals staging se field-for-field copy kiye
  gaye hain. Forecast ka arithmetic real hai — do ceilings, area-based radius share, addressable
  audience — isliye mock par jo behaviour dikhta hai wo real server par bhi wahi rahega.

- **Registry snapshot** — har turn par banta hai, grounded claims ke liye.

- **Phrasebook** (`answers.yaml`, `phrases.yaml`) — definitions aur fixed replies. Schema
  **figure allow hi nahi karta** ek answer me: "there are 6 markets" likhte hi wo us din jhooth
  ban jaata hai jab server alag number de.

---

## 08 · Kya hata, kya juda

### Hataya gaya dead code

- **`classify_intent` node** — 382 lines. Graph me register hi nahi tha, aur classifier ki poori
  doosri copy leke baitha tha.
- **`extract_fields._system_prompt` + `_extract_with_llm`** — 78 lines. Purane two-call path ka
  doosra aadha hissa.
- **`select_inventory` ke 4 renderers** — `_deal_line`, `_tier_name`, `_tier_capability`,
  `_tier_label`. Jab inventory list rows me convert hui, ye orphan ho gaye the.
- **`mock_data.deals_for`** — `mock._DEALS_BY_MARKET` ne replace kar diya tha, aur ab uske saath
  *contradict* bhi kar raha tha.
- **`scripts/` folder** — 6 throwaway probe files, kabhi commit nahi hui thi, kisi ne reference
  nahi ki thi.

### Deliberately rakha gaya

- **`tools/auth.py::SessionTokenAuth`** — call nahi hota, par ye placeholder hai real VOW auth ke
  liye. Client ka jawab pending hai (Open Questions A1). Ye pending work hai, dead code nahi.

### Recent fixes

- **Radius targeting kaam hi nahi karta tha.** Agent khud example deta tha
  "within 3km of Manchester city centre" aur wahi line wapas type karne par "samajh nahi aaya"
  milta tha. City aur postcode ek pattern se pahunchte the jise verb chahiye ("target London");
  radius me verb hota hi nahi.
- **Definitions cold refuse ho rahi thi.** "what is a CPM?" ka jawab `answers.yaml` me hamesha se
  tha; label fail ho raha tha. Ab platform ke apne nouns wala sawal rule se QUESTION hai, model
  call ke bina.
- **Ek channel chaar lines ban jaata tha.** Widened list me Prime Video ki chaar rows hain;
  "Prime Video and Tubi" paanch lines aur paanch-tarfa split de raha tha. Ab ek channel = ek
  deal, wo jo plan ki creative length leta ho.
- **Named-but-unbuyable channel chup-chaap drop ho jaata tha.** "Prime Video and Netflix" me
  Netflix bina ek shabd ke gayab, aur plan card dono naam dikhata tha.
- **CPM ka jawab forecast se contradict karta tha** — £28.88 bola jab forecast £30.51 keh raha
  tha. Ab dono figures aur unka farq bolta hai.

---

Test cases ke liye alag document hai — 72 cases, step ke hisaab se, sab live server par run
karke likhe gaye. Ye document code ka *kyun* hai; wo document *kya type karna hai* hai.
