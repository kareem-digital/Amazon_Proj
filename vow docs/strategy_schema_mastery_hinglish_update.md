# Strategy Schema Document + 28 Comments — Poori Mastery (Hinglish)

**Ye document kis liye:** Confluence par `Strategy Schema documentation v2.0` hai. Us par David Moss ne **28 comments** kiye. Ye document do cheezein deta hai:

1. **Poora technical foundation** — CTV, Programmatic Guaranteed, Preferred Deals, Private Auctions, aur har technical shabd, real examples ke saath
2. **28 comments ki poori mastery** — David ne kya kaha, kyun kaha, maqsad kya tha, maine kya samjha, mai unse kya puch sakta hoon, wo mujhse kya puch sakte hain

**Kaise use karein:** Team me koi puche *"David ke is comment ka matlab kya hai, tumne kya samjha?"* — Part C me us comment ka number dhundo, `Maine kya samjha` bolo, `Real example` se explain karo. Koi technical shabd puche — Part A me hai.

---

## Contents

| Part | Kya hai |
|---|---|
| **A** | Technical foundation — ecosystem, CTV vs non-CTV, **auction**, **teen deal types (hotel analogy)**, **floor vs fixed**, **bid**, **CPM ka ganit**, 1P/2P/3P data, reach, endemic, baaki sab terms |
| **B** | Strategy Schema document ki structure — kya hai, kyun bana, 13 steps |
| **C** | **28 comments** — ek-ek, poora breakdown |
| **D** | 7 bade themes jo 28 comments me baar-baar aate hain |
| **E** | Viva prep — 35 sawaal jo team puch sakti hai, jawab ke saath |
| **F** | Jo sawaal humein team/client se puchne hain |

---
---

# PART A — Technical Foundation

## Part A ka naksha — isi order me padho

Ye sections ek **chain** hain. Har agla pichle par khada hai. Order se padho:

| § | Kya | Kyun isi jagah |
|---|---|---|
| **A1** | Advertising ka ecosystem | Har shabd isi chain me kahin baithta hai |
| **A2** | CTV kya hai, non-CTV kya hai | Poora product CTV ke liye hai |
| **A3** | "Programmatic" ka matlab | Deal types isi ke andar aate hain |
| **A4** | 🔴 **Auction kya hai** | **Teen deal types ka farak "auction hota hai ya nahi" ka farak hai** |
| **A5** | 🔴 **Teen deal types** (hotel analogy) | Schema ka §2.3, aur Comment 1 + 18 ka base |
| **A6** | 🔴 **Floor vs Fixed** | Ye do shabd hi poora confusion hain |
| **A7** | 🔴 **Bid** — kya, kaun, kahan | Comment 12 samajhne ke liye zaroori |
| **A8** | **CPM ka ganit** | Har forecast aur estimate isi par khada hai |
| **A9** | 1P/2P/3P data aur fees | Comment 2 + 19 ka base |
| **A10** | Reach, Frequency, Impressions | Comment 8 + 10 ka base |
| **A11** | Endemic vs Non-Endemic | Comment 16 + 17 ka base |
| **A12** | Baaki sab technical shabd | Reference ke liye — order matter nahi karta |

**Agar sirf teen deal types samajhne aaye ho:** A4 → A5 → A6 → A7 padho. Chaar sections, aur poora clear ho jaayega.

---

## A1. Advertising ka poora ecosystem — pehle ye samjho

Har technical shabd isi chain me kahin baithta hai. Ye chain samajh gaye to baaki sab apne aap clear ho jaayega.

```
  ADVERTISER          "Mujhe apna product bechna hai"
  (BrightPath — education website)
        │
        │  brief deta hai: "£10,000, UK, September, awareness"
        ↓
  AGENCY / TRADER     "Mai plan banaunga aur ad kharidunga"
  (VOW ka user — jise hum "trader" kehte hain)
        │
        │  VOW Platform par strategy banata hai
        ↓
  VOW PLATFORM        DSP reseller — Amazon DSP ka authorised partner
        │
        │  Amazon DSP par campaign publish karta hai
        ↓
  DSP                 Demand Side Platform — Amazon DSP
  (khareedne ka side)  "Mai advertiser ke paise se inventory khareedunga"
        │
        │  bid request / deal
        ↓
  SSP / EXCHANGE      Supply Side Platform — Freewheel, Pubmatic, Magnite
  (bechne ka side)     "Mai publisher ki khaali jagah bechunga"
        │
        ↓
  PUBLISHER           Prime Video, Netflix, Disney+, ITVX, Channel 4
  (jiske paas jagah hai)
        │
        ↓
  VIEWER              Ghar par TV dekh raha banda
```

**Do sides yaad rakho:**
- **Demand side** = khareedar ka side (advertiser, agency, DSP) — *"mujhe ad dikhana hai"*
- **Supply side** = bechne wala side (publisher, SSP) — *"mere paas khaali ad slot hai"*

**DSP aur SSP ek marketplace ke do end hain.** Beech me auction hota hai.

**Real example:**
```
Aap Prime Video par "The Boys" dekh rahe ho.
Episode ke beech me ad break aata hai.

Us ek second me:
  Prime Video (publisher) → "mere paas ek slot hai, ek 32-saal ka UK ka banda dekh raha hai"
  → SSP ko batata hai
  → SSP 50 DSPs ko bid request bhejta hai
  → Amazon DSP bolta hai "mai £22 CPM dunga, mera BrightPath ka ad chalao"
  → Doosra DSP bolta hai "mai £19 dunga"
  → Amazon DSP jeet gaya
  → aapko BrightPath ka ad dikhta hai

Ye poora khel 100 milliseconds me hua.
```

**VOW kahan hai:** VOW ka apna DSP nahi hai. VOW **Amazon DSP ka reseller** hai. Yaani VOW ke traders Amazon DSP use karte hain, par VOW ke interface se. Isi liye har cheez me "Amazon" aata hai — audiences, deals, creative approval, sab Amazon ke through.

---

## A2. CTV kya hai — aur non-CTV kya hai

### CTV = Connected TV

**Definition:** Aisa TV jo **internet se juda** hua hai, aur uspar ad **programmatically** (automatically, real-time) khareedi jaa sakti hai.

**CTV device kaunse hain:**
```
Smart TV              Samsung, LG, Sony — jisme WiFi built-in hai
Streaming stick       Amazon Fire TV Stick, Roku, Chromecast
Gaming console        PlayStation, Xbox (jab uspar Netflix chalate ho)
Set-top box           Apple TV, Sky Glass
```

**CTV par ad kaisa hota hai:**
```
✓ Video ad, 10 se 60 second
✓ NON-SKIPPABLE — skip button nahi hota
✓ Full screen, TV ki screen par
✓ Show ke pehle (pre-roll), beech me (mid-roll), ya baad me (post-roll)
✗ Click NAHI ho sakta — remote se click nahi hota!
```

### Non-CTV kya hai

| Kism | Kya hai | Device | Click? |
|---|---|---|---|
| **Display** | Banner image / static ad | Phone, laptop, tablet | ✅ Haan |
| **Online Video (OLV)** | Video ad website/app par | Phone, laptop, tablet | ✅ Haan |
| **Linear TV** | Purana normal TV ad | Cable/antenna wala TV | ❌ Nahi |
| **Audio** | Spotify, podcast ad | Kuch bhi | ✅ Kabhi |

### CTV vs OLV — ye confusion sabse zyada hoti hai

Dono **video** hain. Farak **kahan chal raha hai** ka hai:

```
CTV  →  video ad TV KI SCREEN par chal raha hai
OLV  →  video ad PHONE/LAPTOP par chal raha hai
```

Aur ek **bahut zaroori twist:**

🔴 **Prime Video CTV bhi hai aur OLV bhi.** Kyunki Prime Video TV par bhi chalti hai aur phone par bhi. Same content, alag device.

Isi liye VOW me do alag fields hain:
```
formats      = ["streaming_tv"]      ← content ki kism (streaming video)
device_types = ["Connected TV"]      ← screen jispar chalega
```

**`streaming_tv` format ka matlab TV screen NAHI hai.** Matlab hai "streaming content". Wo phone par bhi ho sakta hai. **Ye Comment 22 ka poora point hai** — dhyaan se yaad rakho.

### CTV vs Linear TV — VOW ka pitch yahi hai

| | Linear TV (purana) | CTV (naya) |
|---|---|---|
| Kaise kharidte ho | Phone karke, hafte pehle | Programmatically, seconds me |
| Kisko dikhega | "8 baje news dekhne wale" — sabko | "32 saal, UK, healthy food me interest" — specific |
| Kitna minimum | £50,000+ | £1,000 se bhi |
| Measurement | Panel survey (~2,000 ghar ka sample) | Har impression track hoti hai |
| Badal sakte ho? | Nahi, ad chhap gaya | Haan, live badal sakte ho |
| Frequency control | Nahi | Haan — "hafte me max 3 baar" |

### CTV ki teen mahatvapoorn limitations (schema me ye baar-baar aayengi)

**1. Click nahi ho sakta**
```
TV remote se ad par click nahi kar sakte.
→ Isliye click_through_url OPTIONAL hai (Comment 25)
→ Isliye CTR jaisi metric CTV me kaam nahi karti
→ Call to action: QR code, "search for BrightPath", ya bas brand yaad rehna
```

**2. Funnel ke neeche track karna mushkil**
```
Awareness  ← CTV yahan kaam karta hai
Consideration
Conversion  ← CTV se yahan tak jodna bahut mushkil

David ka apna quote: "CTV is typically used as an Awareness goal
as it's hard to track anything further down the funnel"
→ Isliye goal FIXED = Awareness (Comment 6 ka hissa)
```

**3. Mehnga hai**
```
Display CPM     £2 – £5
OLV CPM         £8 – £15
CTV CPM         £18 – £40      ← 5 se 10 guna mehnga

Kyun? TV screen par full-screen non-skippable ad ki value zyada hai,
aur premium content (Prime Video, Netflix) ki supply limited hai.
```

---

## A3. "Programmatic" ka matlab kya hai

**Programmatic = automatically, software se, real-time me ad khareedna** — insaan ke phone karke deal karne ke bajaye.

**Purana tareeka (direct / IO-based):**
```
1. Trader Prime Video ko email karta hai
2. Prime Video rate card bhejta hai
3. Negotiation — 2 din
4. IO (Insertion Order) sign hota hai — ek contract
5. Manually campaign set hoti hai
Total: 1-2 hafte
```

**Programmatic:**
```
1. Trader DSP me campaign banata hai
2. Ad slot khaali hone par milliseconds me auction
3. Live
Total: minutes
```

Par **"programmatic" ka matlab "hamesha open auction" nahi hai.** Programmatic ke andar 4 kism ke sauda hote hain — aur wahi agla section hai.

---

## A4. Auction kya hai — sabse pehle ye

Teen deal types samajhne se pehle **auction** samajhna zaroori hai. Kyunki teeno ka farak asal me "auction hota hai ya nahi, aur kaisa hota hai" ka farak hai.

### Ek line me

**Auction = jab ek cheez ki supply kam ho aur khareedar zyada hon, to daam khareedar tay karte hain — bolke.**

### Sabzi mandi ki nilaami

```
Ek tokri aam hai. Ek hi tokri.
Teen khareedar khade hain.

Bolne wala:  "500 se shuru!"
Khareedar A: "500"
Khareedar B: "600"
Khareedar C: "700"
Khareedar A: "750"
Khareedar B: "chhod diya"
Khareedar C: "chhod diya"

→ Khareedar A jeeta, Rs 750 me tokri mili.
```

### Auction ke chaar hisse

| Hissa | Matlab |
|---|---|
| **Ek cheez** | Sirf ek tokri hai — dono ko nahi mil sakti |
| **Kai khareedar** | Competition hai |
| **Bid** | Har khareedar apna daam bolta hai |
| **Sabse zyada jeetta hai** | Baaki khaali haath |

### 🔴 Aur ek paanchwa hissa jo sabse zaroori hai — RESERVE PRICE

```
Bolne wala: "Is tokri ka minimum Rs 500 hai.
             Rs 500 se kam koi bid manzoor nahi.
             Koi Rs 500 na de to mai tokri nahi bechunga."
             
Rs 500  =  RESERVE PRICE  =  FLOOR PRICE  =  "farsh"
```

**Floor ka matlab yaad rakho: neeche jaa nahi sakte, upar jaana padta hai.**

Yahi teeno deal types samajhne ki chaabi hai.

### Ad ki duniya me auction kaise hota hai

Ek baat samajhni hai: **ad slot bhi "ek tokri aam" jaisa hai — aur wo SADH JAATA HAI.**

```
Aap Prime Video par "The Boys" dekh rahe ho.
Ad break aaya. Ek slot khaali hai. Aap ek hi banda ho.

Ye slot ABHI bikna hai. Iske do second baad iski value = ZERO.
Prime Video ise fridge me nahi rakh sakta.
```

Isliye Prime Video ise auction me daal deta hai — **aur poora auction 100 millisecond me hota hai:**

```
Aapne "The Boys" par play dabaya
        |
        v  (0 ms)
Prime Video: "Mere paas ek slot hai. Dekhne wala:
              32 saal, UK, male, Prime member,
              pehle education ke videos dekhe hain"
        |
        v  (10 ms)
SSP 50 DSPs ko ye info bhejta hai: "koi lega?"
        |
        v  (40 ms)
Amazon DSP:  "£24 dunga — mera BrightPath ka ad chalao"
Trade Desk:  "£19 dunga"
DV360:       "£22 dunga"
        |
        v  (80 ms)
Amazon DSP JEET GAYA (£24 sabse zyada)
        |
        v  (100 ms)
Aapko BrightPath ka ad dikha
```

**Aapko pata bhi nahi chala. Par ek auction ho gaya.**

**Ek din me aisa BILLION baar hota hai.** Isi liye ye "programmatic" hai — insaan itni tezi se nahi kar sakta, software karta hai.

---

## A5. 🔴 Teen Deal Types — hotel ke kamron se samjho

Ab teeno. Aur main ek analogy use karunga jo **ad slot se bilkul milta hai.**

### Analogy: HOTEL KE KAMRE

Ek hotel hai. **Aaj raat ke 100 kamre hain.**

**Ye ad slot jaisa hi hai** — kyunki:
- Supply fix hai (100 kamre, na kam na zyada)
- **Aaj raat khaali gaya to value ZERO** (kal nahi bech sakte)
- Isliye hotel ko bechna hi hai, kisi tareeke se

Hotel ke paas **chaar** tareeke hain kamre bechne ke.

---

### Tareeka 1 — OPEN AUCTION (khuli nilaami)

```
Hotel ka board bahar: "Kamre available — jo zyada de, uska"

Koi bhi aa sakta hai. Koi bhi bid kar sakta hai.

Raat 11 baje 3 kamre bache hain, 5 log khade hain
   -> daam badh gaya
Raat 11 baje 40 kamre bache hain, 2 log khade hain
   -> daam gir gaya
```

**Ad me:** ye **open exchange** hai. Premium publishers (Prime Video, Netflix) **ye use nahi karte** — kyunki isme control nahi hota ki kaun ad chala raha hai. Ek luxury brand ke saath satta app ka ad chal jaaye to brand naraz.

🔴 **Isliye VOW ke schema me ye nahi hai.** Bas samajhne ke liye batayi — kyunki baaki teen isse compare karke hi samajh aate hain.

---

### 🔵 Tareeka 2 — PRIVATE AUCTION

```
Hotel manager 8 travel agents ko phone karta hai:

"Sirf aap 8 log bid kar sakte ho. Aur ek shart —
 minimum Rs 4,000 per kamra. Usse kam mai nahi bechunga.
 Baaki tum aapas me compete karo."

Aaj raat:
   Agent A: Rs 4,200
   Agent B: Rs 4,500      <- JEET GAYA, Rs 4,500 diya
   Agent C: Rs 4,000
   Agent D: Rs 4,100
```

**Do baatein dhyaan se:**

**Ek — Rs 4,000 MINIMUM hai, FINAL nahi.** Agent B ne Rs 4,500 diya kyunki competition tha. Sirf ek agent hota to shayad Rs 4,000 me mil jaata.

**Do — jeetne ki GUARANTEE nahi hai.**
```
Agent A ne Rs 4,200 bid kiya. Wo HAAR gaya.
Usko ek bhi kamra nahi mila.
Uske paise bache -- par uska kaam nahi hua.
```

#### Ad me PRIVATE AUCTION

```
Netflix bolta hai:
  "Meri UK Streaming TV inventory ka FLOOR £22.96 hai.
   Mai 8 DSPs ko invite kar raha hoon.
   £22.96 se upar bid karo. Jo zyada dega, use slot."

Slot khaali hua:
   Amazon DSP  £24.00   <- jeeta
   Trade Desk  £23.50   <- haara
   DV360       £22.96   <- haara
```

| Sawaal | Jawab |
|---|---|
| Daam pakka? | Nahi — £22.96 se shuru, upar kuch bhi |
| **Bid karna padta hai?** | ✅ **HAAN — yahi ek jagah hai jahan bid matter karta hai** |
| Kitne slots milenge? | Pata nahi — jitne jeetoge |
| Poora budget kharch hoga? | Pata nahi — jeete to hoga |
| Pause kar sakte ho? | ✅ Haan, kabhi bhi |

**🔴 Iska sabse bada RISK — under-delivery:**

```
Aapne £10,000 daala, floor £22.96, aap £24 bid kar rahe ho.

Us mahine Christmas aa gayi. Sab brands ad chala rahe hain.
Sab £32 bid kar rahe hain.

Aap £24 bid kar rahe ho -> aap HAR JAGAH HAAR rahe ho.

Mahine ke aakhir me:
   Kharch hua: £2,100
   Bacha:      £7,900
   Client:     "Mera campaign chala hi nahi!"
```

**Isliye is deal type me "kitni reach milegi" ka andaza lagana mushkil hai.** Pata nahi kitni baar jeetoge.

---

### 🟢 Tareeka 3 — PREFERRED DEAL

```
Hotel manager apne SABSE PURANE agent ko bulata hai:

"Tumhare liye Rs 5,000 per kamra FIX. Auction nahi.

 Aur ek faayda -- jab bhi mere paas kamra khaali hoga,
 mai PEHLE tumhe phone karunga.
 
 Tum 'haan' bolo -> Rs 5,000 me tumhara.
 Tum 'na' bolo   -> mai auction me daal dunga.
 
 Aur haan -- tum par koi majboori nahi. Ek kamra lo ya
 pachas, ya ek bhi na lo. Mai kuch nahi kahunga."
```

**Teen baatein:**

**Ek — daam PAKKA hai.** Rs 5,000. Christmas ho ya normal din, Rs 5,000. Bid karne ki zaroorat hi nahi.

**Do — PEHLA HAQ hai.** Manager pehle aapko puchega, phir doosron ko. Isko **"first look"** ya **"right of first refusal"** kehte hain.

**Teen — par GUARANTEE nahi hai.**
```
Kya ho sakta hai:
   Manager ne pehle se 90 kamre kisi PG contract me de diye hain.
   Ab sirf 10 bache. Aapko wo 10 hi milenge, chahe 50 chahiye the.
   
   Daam pakka tha. Kitne milenge, wo pakka nahi tha.
```

#### Ad me PREFERRED DEAL

```
Prime Video bolta hai:
  "Tumhare liye £15.26 CPM fix. Koi auction nahi.
   Slot khaali hone par PEHLE tumse puchunga."

Slot khaali hua:
   -> Prime Video -> Amazon DSP: "chahiye? £15.26"
   -> Aapka campaign chal raha hai, budget hai -> "haan"
   -> Slot mila, £15.26 diya. AUCTION HUA HI NAHI.
   
   Agar aapka budget khatam -> "na"
   -> Prime Video wo slot auction me daal deta hai
```

| Sawaal | Jawab |
|---|---|
| Daam pakka? | ✅ **HAAN** — £15.26, hamesha |
| Bid karna padta hai? | ❌ **Nahi** — daam already tay hai |
| Kitne slots milenge? | ⚠️ Pata nahi — priority hai, guarantee nahi |
| Poora budget kharch hoga? | ⚠️ Pata nahi |
| Pause kar sakte ho? | ✅ Haan |

---

### 🔴 Tareeka 4 — PROGRAMMATIC GUARANTEED (PG)

```
Hotel manager aur ek badi company ka CONTRACT:

"1 September ki raat, 50 kamre, Rs 5,000 per kamra.
 Total Rs 2,50,000.
 
 Mai 50 kamre PAKKA dunga -- chahe hotel me aag lag jaaye,
 mai kahin se 50 kamre nikaalunga.
 
 Tum Rs 2,50,000 PAKKA doge -- chahe tumhare mehmaan aayein
 ya na aayein. Chahe conference cancel ho jaaye.
 Chahe tum sirf 10 kamre use karo.
 
 Ye contract hai. Sign karo."
```

🔴 **Ye auction NAHI hai.** Koi bidding nahi, koi competition nahi. Ye ek **contract** hai.

**Do taraf ka wada hai:**
```
Hotel ka wada:    50 kamre PAKKA milenge
Company ka wada:  Rs 2,50,000 PAKKA denge
```

**Aur yahi khatra hai:**
```
25 August ko conference cancel ho gaya.
Company: "hamein kamre nahi chahiye"
Manager: "Contract hai. Rs 2,50,000 doge."

-> Paise gaye. Kamre bhi bekaar.
```

#### Ad me PROGRAMMATIC GUARANTEED

```
Prime Video aur VOW ka contract:
  "1-30 September, 300,000 impressions, £20 CPM.
   Total £6,000.
   
   Mai 300,000 impressions PAKKA dunga.
   Tum £6,000 PAKKA doge."

Slot khaali hua:
   -> SEEDHA aapka ad chala. Koi auction nahi. Koi bid nahi.
   -> Kyunki contract hai.
   
15 September ko aap campaign band karna chahte ho:
   -> 🔴 NAHI KAR SAKTE. £6,000 owed hai.
```

| Sawaal | Jawab |
|---|---|
| Daam pakka? | ✅ Haan |
| Bid karna padta hai? | ❌ Nahi — auction hi nahi hota |
| Kitne slots milenge? | ✅ **PAKKA — guaranteed** |
| Poora budget kharch hoga? | 🔴 **HAAN — chahe use karo ya na** |
| Pause kar sakte ho? | 🔴 **NAHI** |

---

### Teeno ek saath — hotel ki bhasha me

| | 🔵 Private Auction | 🟢 Preferred | 🔴 Prog. Guaranteed |
|---|---|---|---|
| **Hotel me** | 8 agents bulaye, min Rs 4,000, compete karo | Purane agent ko Rs 5,000 fix, pehla haq, majboori nahi | Contract: 50 kamre, Rs 2.5 lakh, dono bandhe |
| **Daam** | Rs 4,000 se **shuru** | Rs 5,000 **pakka** | Rs 5,000 **pakka** |
| **Auction?** | ✅ Haan (band) | ❌ Nahi | ❌ Nahi |
| **Bid?** | ✅ **Haan** | ❌ Nahi | ❌ Nahi |
| **Kamre pakka?** | ❌ Nahi | ⚠️ Priority, pakka nahi | ✅ **Pakka** |
| **Paise phanse?** | ❌ Nahi | ❌ Nahi | 🔴 **Haan** |
| **Cancel?** | ✅ Haan | ✅ Haan | 🔴 **Nahi** |

### Ad ki bhasha me — poora technical comparison

| | **Private Auction** | **Preferred Deal** | **Programmatic Guaranteed** |
|---|---|---|---|
| **Doosra naam** | PMP, PA | First Look, PD | PG, Guaranteed |
| **VOW ka `deal_type`** | `PRIVATE_AUCTION` | `PREFERRED` | `PROGRAMMATIC_GUARANTEED` |
| **VOW ka `deal_price_type`** | `FLOOR_RATE` | `FIXED_CPM` | `FIXED_CPM` |
| **Auction hota hai?** | ✅ Haan (band) | ❌ Nahi | ❌ Nahi |
| **Bid karna padta hai?** | ✅ **HAAN** | ❌ Nahi | ❌ Nahi |
| **Volume guarantee** | ❌ | ❌ | ✅ **HAAN** |
| **Poora budget owed?** | ❌ | ❌ | 🔴 **HAAN** |
| **Pause?** | ✅ | ✅ | 🔴 **NAHI** |
| **Priority** | Sabse kam (open se upar) | Beech | Sabse zyada |
| **Daam ka andaza** | ❌ Mushkil | ✅ Pakka | ✅ Pakka |
| **Volume ka andaza** | ❌ Mushkil | ⚠️ Thoda | ✅ Pakka |
| **Flexibility** | ✅ Poori | ✅ Poori | 🔴 Zero |
| **VOW me kitni** | 🔴 **Lagbhag saari** | Kuch (Prime Video) | Ek bhi nahi mili |

---

### Ek hi scenario me teeno ka farak

**Situation:** BrightPath ka £10,000 ka campaign, September.

#### 🔵 Private Auction chuna

```
Netflix deal, floor £22.96. Aapne base bid £24 rakha.

Normal mahina:
   Aapne 60% auctions jeete
   Kharch: £6,000
   Impressions: 250,000
   
Christmas ka mahina (sab bid badha rahe hain):
   Aapne 20% auctions jeete
   Kharch: £2,000            <- 🔴 UNDER-DELIVERY
   Impressions: 83,000
   Bacha: £8,000
   
Fix kar sakte ho?
   ✅ HAAN -- base bid £24 se £30 karo
              -> zyada jeetoge -> zyada impressions
```

#### 🟢 Preferred Deal chuna

```
Prime Video deal, £15.26 fixed.

Prime Video par supply achhi hai:
   Kharch: £10,000
   Impressions: 655,000     <- poora budget chala
   
Prime Video par PG contracts bhare hue hain:
   Kharch: £4,000           <- ⚠️ slots hi nahi mile
   Impressions: 262,000
   
Fix kar sakte ho?
   ❌ Bid nahi badha sakte (daam fix hai)
   ✅ Doosri inventory add kar sakte ho
```

#### 🔴 Programmatic Guaranteed chuna

```
Prime Video PG, £20 CPM, 500,000 impressions guaranteed.

Kharch: £10,000            <- PAKKA
Impressions: 500,000       <- PAKKA
   
5 September ko pata chala ki creative me galti hai:
   Aap: "band karo!"
   -> 🔴 NAHI HO SAKTA. £10,000 owed hai.
   -> Galat creative POORE MAHINE chalega
   
Fix kar sakte ho?
   🔴 KUCH NAHI. Sab pehle se tay hai.
```

---

### 🔴 "Kya choose karenge to kya hoga"

| Situation | Kya choose karo | Kyun |
|---|---|---|
| Awareness, £10,000, "zyada log tak pahunchao" | **Private Auction** | Reach chahiye, exact volume nahi. Flexible rehna hai |
| "September 15 ko product launch hai, us din pakka chalna chahiye" | **Programmatic Guaranteed** | Ek din ka mauka, miss nahi kar sakte |
| "Prime Video par chalao, budget flexible" | **Preferred Deal** | Premium chahiye, daam pakka chahiye, par commit nahi |
| Pehli baar test kar rahe hain | **Private Auction** | Ghalti hui to pause kar sakte hain |
| Client ne "500,000 impressions" ka wada kiya | **Programmatic Guaranteed** | Sirf ye guarantee de sakta hai |
| Budget chhota hai (£2,000) | **Private Auction** | PG ka minimum bada hota hai |

### Har choice ka asar — teen jagah

**1. Repair loop par asar** (jab reach kam aaye)
```
Private Auction  ->  BID BADHA SAKTE HO  ✅  (ek extra lever)
Preferred        ->  bid ka koi kaam nahi ❌
PG               ->  kuch nahi kar sakte, volume already fix hai ❌
```
🔴 **Ye Comment 12 ka open question hai.** David ne kaha *"CTV me bid apply nahi hota"* — jo Preferred aur PG ke liye sach hai. Par Private Auction ke liye **galat** hai. Aur VOW ki lagbhag saari deals Private Auction hain.

**2. Forecast par asar**
```
Private Auction  ->  impressions ka andaza mushkil (jeet hi na paye)
Preferred        ->  behtar andaza (daam pakka hai)
PG               ->  pakka pata hai (volume guaranteed)
```

**3. Trader ko kya batana hai**
```
Private Auction  ->  "£22.96 floor hai, actual isse zyada ho sakta hai"
Preferred        ->  "£15.26 pakka"
PG               ->  "£6,000 committed, pause nahi ho sakta"  <- MUST BOLNA HAI
```

### Ek line me yaad rakhne ka tareeka

```
🔵 PRIVATE AUCTION   =  "Mandi me line lag ke boli lagao"
                        Sasta mil sakta hai, par mil hi jaaye -- pakka nahi
                        Bid ka kaam HAI

🟢 PREFERRED DEAL    =  "Dukaandar tumhe pehle phone karta hai, daam fix"
                        Daam pakka, par stock pakka nahi
                        Bid ka kaam NAHI

🔴 PROG. GUARANTEED  =  "Advance me poora order book kar diya, paise diye"
                        Sab pakka -- par paise wapas nahi
                        Bid ka kaam NAHI
```

---

## A6. 🔴 FLOOR vs FIXED — ye do shabd hi poora confusion hain

### Sabse simple farak

```
FIXED  =  "Daam YE hai"          ->  ek NUMBER
FLOOR  =  "Daam YAHAN SE shuru"  ->  ek SHURUAAT
```

### Rozmarra ka example

**FIXED — Big Bazaar me saaman:**
```
Packet par likha hai: Rs 250
Aap counter par jaate ho.
Aap Rs 250 dete ho.
Bas. Khatam.

Aap Rs 300 nahi de sakte (kaun dega?).
Aap Rs 200 nahi de sakte (nahi milega).
Sirf Rs 250. Ek number.
```

**FLOOR — property ki nilaami:**
```
Sarkari notice: "Plot ki RESERVE PRICE Rs 50 lakh hai.
                 Rs 50 lakh se KAM koi bid manzoor nahi."

Nilaami hui:
   Bidder A: Rs 52 lakh
   Bidder B: Rs 58 lakh    <- jeeta
   Bidder C: Rs 50 lakh

-> Plot Rs 58 lakh me bika, Rs 50 lakh me nahi.

Rs 50 lakh ne SIRF ITNA BATAYA ki neeche nahi jaa sakte.
Kitne me bikega -- wo NILAAMI ne tay kiya.
```

### 🔴 Sabse zaroori baat

```
FIXED:  jo number DIKHA, wahi PAY karoge         <- pakka
FLOOR:  jo number DIKHA, usse UPAR jaana padega  <- kitna upar? PATA NAHI
```

| | FIXED | FLOOR |
|---|---|---|
| Number ka matlab | Ye pay karoge | Isse zyada pay karoge |
| Planning kar sakte ho? | ✅ Haan, pakka | ❌ Mushkil |
| Kitna pay karoge? | Pata hai | Auction ke baad pata chalega |
| Compete karna padta hai? | ❌ Nahi | ✅ Haan |

### Ek hi deal, do duniya me

Maan lo ek Netflix deal hai, number **£22.96**.

**Agar `FIXED_CPM` hoti:**
```
"£22.96 CPM. Bas."

Aapko slot mila   ->  £22.96 pay kiya
Doosra slot mila  ->  £22.96 pay kiya
Christmas ka mahina, sab bid badha rahe hain  ->  £22.96 pay kiya
                                                   ^ FARAK NAHI PADTA
                                                 
£10,000 me kitne impressions?
   10,000 / 22.96 x 1000 = 435,540
   -> aur ye number PAKKA hai
```

**Aur `FLOOR_RATE` hai (asal me yahi hai):**
```
"£22.96 se upar bid karo. Compete karo."

Normal din, aapne £24 bid kiya, jeete   ->  £24.00 pay kiya
Christmas, sab £32 bid kar rahe          ->  aap HAARE, £0 pay kiya
Aapne bid £30 kiya, jeete                ->  £30.00 pay kiya

£10,000 me kitne impressions?
   -> PATA NAHI!
   -> depend karta hai ki kitni baar jeete aur kitne me jeete
```

🔴 **Yahi wajah hai ki floor deals me "reach ka andaza" lagana mushkil hai.**

### VOW par kya dikhta hai

Platform ke Step 3 (Deals) me do columns hain:

```
| Name                                | Deal type       | CPM    | CPM type |
| 3PS_Freewheel_UK_STV_Paramount_My 5 | Private Auction | £22.96 | Floor    |
| 3PS_Netflix_Always On_Auto Int...   | Private Auction | £38.12 | Floor    |
| Prime Video | Preferred Deal | ...  | Preferred Deal  | £15.26 | Fixed    |
                                        ^                          ^
                                   deal_type              deal_price_type
```

Aur API me:
```json
{
  "deal_price_type": "FLOOR_RATE",     <- ya "FIXED_CPM"
  "deal_price_amount": "22.96",
  "deal_price_currency": "GBP"
}
```

**Ek shabd me:**
```
"Floor"  ->  £22.96 se UPAR jao   ->  bid CHAHIYE
"Fixed"  ->  £15.26 hi hai        ->  bid ki zaroorat NAHI
```

---

## A7. 🔴 BID — exactly kya hai, kaun set karta hai, kahan

### Pehle sabse badi ghalatfehmi door karo

**Ghalatfehmi:** *"Bid har impression ke liye set hoti hai"*

🔴 **GALAT.** Trader har impression ke liye bid set nahi karta — wo **naamumkin** hai:

```
Ek mahine me aapke campaign par 50 CRORE bid requests aa sakti hain.
Trader har ek ke liye number nahi daal sakta.
```

**Jo asal me hota hai:**

```
Trader EK BAAR ek "BASE BID" set karta hai
        |
        v
DSP (Amazon DSP) us base bid ko STARTING POINT maanta hai
        |
        v
Phir DSP HAR AUCTION me KHUD decide karta hai kitna bid karna hai
```

### Base bid asal me kya hai

**Base bid = "aap 1,000 impressions ke liye zyada se zyada kitna dene ko taiyaar ho"**

Ye ek **rate** hai, ek **instruction** hai — ek payment nahi.

```
Base bid £25 ka matlab:

  ❌ Nahi: "har 1,000 impressions ke £25 dunga"
  ✅ Haan: "1,000 impressions ke liye £25 TAK jaa sakta hoon,
            usse zyada nahi"
```

Aur DSP uske andar rehte hue **smart** decisions leta hai:

```
DSP soch raha hai:

Auction 1:  32-saal ka banda, education videos dekhta hai
            "ye BrightPath ke liye PERFECT hai"
            -> £24 bid karta hoon (base ke qareeb)

Auction 2:  70-saal ka banda, gardening videos dekhta hai
            "ye education courses nahi khareedega"
            -> £14 bid karta hoon (base se kam)

Auction 3:  22-saal ka student, exam prep search kiya
            "ye BEST hai"
            -> £25 bid karta hoon (poora base)

Auction 4:  floor £30 hai
            -> bid HI NAHI karta (base £25 se zyada hai floor)
```

🔴 **To base bid ek CEILING hai, ek fixed price nahi.**

### Kahan set hota hai — actual platform

Maine platform par verify kiya. Step 2 me:

```
Budget & Bid                    [ Primary ] [ Market ]

| Market            | Budget     | Base bid |
| 🇬🇧 United Kingdom | £10,000    |    25    |   <- trader yahan type karta hai
```

**Per market ek number.** Bas.

**Payload me kaise jaata hai:**
```json
"markets_info": [{
    "market": "GB",
    "base_supply_bid": "25",     <- trader ka ek number
    "budget": 10000,
    "currency": "GBP"
}]
```

**Aur creation ke baad Planner me kya banta hai:**
```
                     Market      Streaming TV     Prime Video
Bid                              EUR 27.27        EUR 27.27
                                   ^                ^
              EK bid gaya, DO bane -- per format, aur alag-alag editable
              (£25 GBP -> EUR 27.27, rate 1.0909)
```

### 🔴 Bid aur Budget — do bilkul alag cheezein

| | **Budget** | **Base bid** |
|---|---|---|
| Kya hai | **Total** kitna kharch karna hai | **Rate** — 1,000 impressions ka max |
| Example | £10,000 | £25 |
| Unit | Poore campaign ka total | Per 1,000 impressions |
| Khatam hota hai? | ✅ Haan — £10,000 khatam, campaign ruk gaya | ❌ Nahi — ye ek rate hai |
| Analogy | "Petrol ke liye Rs 5,000 hain" | "Rs 100/litre se zyada nahi dunga" |

**Petrol ka analogy poora:**
```
Budget    = Rs 5,000        "itna kharch kar sakta hoon"
Base bid  = Rs 100/litre    "isse mehnga petrol nahi lunga"

Pump par Rs 95/litre   ->  bharwa liya
Pump par Rs 105/litre  ->  aage nikal gaya (limit se zyada)

Rs 5,000 khatam -> gaadi ruk gayi
```

### Bid ka kaam kab hai, kab nahi

```
FLOOR_RATE deal  ->  🔴 BID KA KAAM HAI
                     Aapko floor se upar jaana hai, aur compete karna hai
                     Bid kam   -> haar jaaoge -> impressions kam
                     Bid zyada -> jeetoge     -> impressions zyada

FIXED_CPM deal   ->  ✅ BID KA KAAM NAHI
                     Daam £15.26 hai. Bas. Auction hi nahi hota.
                     Bid £20 rakho ya £50 -- £15.26 hi lagega
```

### Teen situations jo bid se hoti hain

**Situation 1 — Bid floor se KAM:**
```
Netflix floor:  £22.96
Aapka bid:      £20.00

-> Aapki bid VALID HI NAHI hai
-> Aap kabhi kisi auction me shaamil nahi honge
-> Impressions: ZERO
-> Kharch: £0

🔴 Campaign chala hi nahi. Aur trader ko pata bhi nahi chalega
   ki wajah bid thi.
```

**Situation 2 — Bid floor ke barabar / thoda upar:**
```
Netflix floor:  £22.96
Aapka bid:      £23.00

-> Valid hai, par bahut kamzor
-> Jab competition kam ho tab jeetoge
-> Christmas me bilkul nahi jeetoge
-> Impressions: kam aur unpredictable

⚠️ Under-delivery ka risk
```

**Situation 3 — Bid floor se achha upar:**
```
Netflix floor:  £22.96
Aapka bid:      £30.00

-> Zyadatar auctions jeetoge
-> Par har impression mehngi
-> £10,000 jaldi khatam hoga
-> Impressions: zyada win rate, par per-impression mehngi

⚠️ Budget jaldi khatam hone ka risk
```

🔴 **Isliye bid set karna ek trade-off hai** — kam rakho to campaign nahi chalega, zyada rakho to budget jaldi khatam.

### Ek chhoti baat — jo pay karte ho wo bid se kam ho sakta hai

Aaj ke zamane me zyadatar auctions **first-price** hain — jeetne wala apni bid pay karta hai. Par kuch jagah **second-price** hoti hai:

```
Second-price auction:
   Aap:      £30 bid
   Doosra:   £24 bid
   
   -> Aap jeete, par aap £24.01 pay karte ho -- £30 NAHI!
   -> Doosre se bas thoda zyada
```

Bas itna yaad rakho: **bid = maximum**, **actual spend = usse kam ya barabar** — kabhi zyada nahi.

---

## A8. CPM ka poora ganit

### Pehle: CPM kya hai aur 1,000 kyun

**CPM = Cost Per Mille.** *Mille* Latin me "hazaar".

**= 1,000 impressions ka daam.**

**1,000 par kyun?**
```
Ek impression ka daam:  £0.02296
Padhna:                 mushkil, decimals bahut
Compare karna:          £0.02296 vs £0.01526? confusing

1,000 impressions ka daam:  £22.96
Padhna:                     aasan
Compare karna:              £22.96 vs £15.26? turant saaf
```

**CPM ek convention hai, koi jaadu nahi.**

### Do formula — bas ye do

```
              budget
impressions = --------  x 1000
               CPM


              spend
CPM         = -----------  x 1000
              impressions
```

**Pehla** — "mere paise me kitne impressions milenge?" (planning ke waqt)
**Doosra** — "mujhe kitne me mile?" (report ke waqt — isko **eCPM** kehte hain)

### Formula ka reverse-engineer — 1000 kahan se aaya

```
Agar 1,000 impressions ka daam £22.96 hai
to 1 impression ka daam = 22.96 / 1000 = £0.02296

£10,000 me kitne impressions?
   = 10,000 / 0.02296
   = 435,540

Aur shortcut:
   = 10,000 / 22.96 x 1000
   = 435,540           <- wahi jawab
```

**Bas CPM ko 1000 se divide karke per-impression daam nikalna hai. `x 1000` wahi kaam karta hai.**

### 🔴 Poora worked example — actual verified numbers

Ye maine platform par khud dekha. Test strategy `VMA2026368`.

**Step 1 — Trader kya daalta hai**
```
Budget:    £10,000
Base bid:  £25
Market:    GB
Formats:   Streaming TV + Prime Video
Dates:     1-30 September 2026
```

**Step 2 — Currency convert hoti hai**
```
Trader ne market currency (GBP) me daala.
Strategy ki primary currency EUR hai.

£10,000 x 1.0909  =  EUR 10,909.09
£25     x 1.0909  =  EUR 27.27
```

**Step 3 — Deals chuni**
```
Deal A:  £24.79 CPM
Deal B:  £34.80 CPM
```

**Step 4 — Forecast chalta hai**

Yahan **twist** aata hai. Forecast ne deals ke CPM use **nahi** kiye:

```json
"supplies": [
  { "supply": "DSP_STREAMING_TV",
    "est_spend": 4931.71,  "avg_cpm": "7.60",
    "est_impressions": 647856,  "est_reach": 132713 },
    
  { "supply": "DSP_PRIME_VIDEO",
    "est_spend": 5068.29,  "avg_cpm": "23.98",
    "est_impressions": 212860,  "est_reach": 71120 }
],
"total_impressions": 860716,
"total_reach": 233803
```

**Step 5 — Ganit verify karo**

Streaming TV:
```
impressions = 4,931.71 / 7.60 x 1000 = 648,909
API ne diya: 647,856      (farak ~1,000, rounding)
✅ Formula sahi hai
```

Prime Video:
```
impressions = 5,068.29 / 23.98 x 1000 = 211,355
API ne diya: 212,860
✅ Formula sahi hai
```

Spend jodo:
```
4,931.71 + 5,068.29 = £10,000.00   ✅ poora budget
```

Impressions jodo:
```
647,856 + 212,860 = 860,716        ✅ API ka total bilkul yahi
```

Reach jodo:
```
132,713 + 71,120 = 203,833
API ka total_reach = 233,803

🔴 API ka number ZYADA hai, sum se!
   -> REACH ADD NAHI HOTI. API ka number use karo.
```

Frequency nikalo (API deta hi nahi):
```
frequency = 860,716 / 233,803 = 3.68
```

eCPM:
```
eCPM = 10,000 / 860,716 x 1000 = £11.62

Interesting: deals £24.79 aur £34.80 thi.
Blended eCPM sirf £11.62 aaya.
```

### 🔴 Teen CPM ka trap

| CPM ki kism | Value | Kahan se |
|---|---|---|
| **Deal ka CPM** | £24.79, £34.80 | Trader ne deals chuni |
| **Supply ka avg CPM** | £7.60, £23.98 | Forecast API ne diya |
| **eCPM** | £11.62 | Total spend / total impressions |

**Teeno alag hain. Aur teeno "CPM" hi kehlate hain.**

```
Koi puche "CPM kitna hai?"
-> Pehle puchna padega: "KAUNSA CPM?"
```

**Kyun alag hain:** deal CPM us specific deal ka daam hai. Supply avg CPM us poore supply pool ka blended average hai — jisme aapki chuni gayi deals ke alawa **aur bhi** inventory hai. eCPM asal me jo hua wo hai.

### CPM ki saat kism — poori list

| Naam | Matlab | Kahan milta hai |
|---|---|---|
| **Rate-card CPM** | Publisher ka list price | Rate card, curation se pehle |
| **Fixed CPM** | Pakka daam | Preferred, PG deals |
| **Floor CPM** | Minimum, iske upar bid | Private Auction |
| **Base bid** | Aap kitna bid karenge (max) | Trader daalta hai |
| **Effective CPM** | Deal CPM **+** audience fee | Agent calculate karta hai |
| **eCPM** | Jo asal me kharch hua | Reporting me, baad me |
| **Supply avg CPM** | Forecast ka blended average | Forecast API |

### 🔴 Effective CPM — Agent ke liye sabse zaroori

*(Audience fee ke poore rules §A9 me hain — kab lagti hai, compound kyun nahi hoti, providers kaise stack hote hain.)*

```
Effective CPM = Deal CPM + Audience data fee (VCPM)

Netflix deal          £22.96 CPM
Amazon audience fee  + £1.63 VCPM
-----------------------------------
Effective CPM         £24.59

Impressions:
   Deal CPM se:       10,000 / 22.96 x 1000 = 435,540
   Effective CPM se:  10,000 / 24.59 x 1000 = 406,669
   
   Farak: 28,871 impressions (7% kam!)
```

🔴 **Agar agent sirf deal CPM se calculate karega to wo trader ko 7% zyada impressions batayega — aur wo jhooth hoga.**

Isi liye schema §2.4 me likha hai: *"the agent should surface the effective CPM (deal + audience fee), not just the deal price."*

### Do numeric traps jo agent me guard chahiye

**Trap 1 — Division by zero:**
```
Maine platform par ek deal dekhi: VowMade_Fifa 2026_ZA
   deal_price_amount: "0.00"

impressions = 10,000 / 0 x 1000
            = 🔴 CRASH

-> Agent me guard chahiye: CPM = 0 ho to skip karo ya flag karo
```

**Trap 2 — Currency mismatch:**
```
Budget:  EUR 10,909.09  (EUR me)
Deal:    £22.96         (GBP me)

Galat hisaab:
   10,909.09 / 22.96 x 1000 = 475,178 impressions

Sahi hisaab (ek currency me lao):
   EUR 10,909.09 = £10,000
   10,000 / 22.96 x 1000 = 435,540 impressions

🔴 Farak: 39,638 impressions -- 9% ka jhoot!
```

Aur maine dekha ki platform par **UK deals USD me bhi hain** (`$1.64`, `$56.13`). To ye trap asli hai.

### Teeno hisson ka nateeja — ek jagah

```
FLOOR vs FIXED
   Fixed  =  ye number pay karoge          ->  bid ki zaroorat nahi
   Floor  =  is number se UPAR jaana hai   ->  bid CHAHIYE
   
BID
   Ek RATE hai, per 1,000 impressions ka MAXIMUM
   Trader EK BAAR set karta hai, per market
   DSP har auction me uske andar rehte hue KHUD decide karta hai
   Bid != Budget.  Bid = rate ka ceiling.  Budget = total paise.
   Bid < floor  ->  campaign chalega hi nahi
   
CPM
   impressions = budget / CPM x 1000
   Effective CPM = deal CPM + audience fee    <- YE use karo
   Teen alag CPM hote hain -- hamesha pucho kaunsa
   Reach add nahi hoti. Impressions add hoti hain.
   Guards: CPM = 0, aur currency mismatch
```

---
## A9. 1P, 2P, 3P Data — aur fees

Ye samajhna Comment 2 aur Comment 19 ke liye zaroori hai.

### Teen kism ka data

| Naam | Poora naam | Kiska data | Example |
|---|---|---|---|
| **1P** | First-party | **Aapka khud ka** | BrightPath ki website par jo aaye |
| **2P** | Second-party | Partner ka, seedha share kiya | Kisi ne apna data aapko diya |
| **3P** | Third-party | Kisi aur ne ikattha kiya, bech raha hai | Experian, Nielsen |

### 🔴 Par advertising me "1P" aur "3P" ek aur matlab me bhi use hote hain

Ye confusion ka bada source hai:

| Context | "1P" | "3P" |
|---|---|---|
| **Data ke baare me** | Amazon ka apna data | Experian jaisi company ka data |
| **Inventory ke baare me** | Amazon ki apni inventory | Netflix, Disney+, Hulu |

Deal names me `3PS_Netflix_...` dikhta hai — wahan **3PS = 3rd Party Supply**, yaani inventory ki baat ho rahi hai, data ki nahi.

**To jab bhi "3P" sune, puchna: "3P inventory ya 3P data?"**

### Amazon ka data kyun khaas hai

```
Amazon jaanta hai:
  ✓ Aapne kya kharida (asli purchase data — koi doosra nahi jaanta)
  ✓ Aapne kya search kiya
  ✓ Aapne kaunsa product page dekha
  ✓ Aapke ghar me kaun-kaun hai (delivery address, Prime sharing)
  ✓ Aapki income ka andaza (kya kharidte ho)
  ✓ Aap Prime Video par kya dekhte ho

Isi liye Amazon audiences premium hain — aur unki FEE hai.
```

### 🔴 Audience fee ke teen rules (Comment 2 ka core)

David ne teen rules diye:

**Rule 1 — Fee kab lagti hai:** Jab **1P data** use karo — chahe Amazon ka ho ya kisi third-party ka apna first-party data (jaise Experian ka Lifestyle data). Profile (Narrow/Balanced/Wide) se koi lena-dena nahi.

**Rule 2 — Compound nahi hoti:** Ek provider se 1 segment lo ya 30, **ek hi fixed CPM** lagta hai.
```
Amazon se 1 segment  → £1.63 VCPM
Amazon se 30 segment → £1.63 VCPM     ← wahi!
```

**Rule 3 — Cross-provider stack hoti hai:** Do alag providers use kiye to **dono ki fee** lagegi.
```
Amazon se segment + Experian se segment
→ £1.63 (Amazon) + £2.00 (Experian) = £3.63 total VCPM
```

**Real example:**
```
Case 1: Koi audience nahi
        £22.96 CPM → 435,540 impressions
        
Case 2: Amazon se 25 segments
        £22.96 + £1.63 = £24.59 → 406,669 impressions
        (Fee ek baar lagi, 25 baar nahi)
        
Case 3: Amazon se 20 + Experian se 5
        £22.96 + £1.63 + £2.00 = £26.59 → 376,081 impressions
        (Dono providers ki fee)
        
Case 2 se Case 3 me sirf 5 segments jode, par 30,588 impressions kam!
```

🔴 **Isliye agent ko `audience_data_sources` track karna padta hai** (`AMAZON_1P` / `THIRD_PARTY` / `NONE`) — **kaun-kaun provider use ho raha hai**, kitne segments nahi.

### VCPM kya hai

**VCPM = Viewable CPM.** Yahan iska matlab hai **audience data ki fee, per 1,000 impressions.**

Deal CPM inventory ka daam hai. VCPM data ka daam hai. Dono jodte hain.

**VOW me actual values (staging par dekha):**
```
standard_display_fee: "0.59"    ← Display ke liye
video_fee:            "1.63"    ← Video/CTV ke liye
fee_currency:         "GBP"
```

Aur kaunsi audience free hai — **category se pata chalta hai:**
```
🟢 FREE  →  Demographic (age, gender, income)  ·  Device
🔴 PAID  →  In-market  ·  Lifestyle  ·  Interest  ·  Custom-built  →  £1.63
```

---

## A10. Reach, Frequency, Impressions — ka poora ganit

Ye teen alag cheezein hain. Confuse karna aam ghalti hai.

```
IMPRESSIONS  =  ad kitni BAAR dikha           (total count)
REACH        =  kitne UNIQUE LOGON ne dekha   (log ki ginti)
FREQUENCY    =  ek banda kitni baar dekha     (average)

        impressions
FREQ =  ───────────
           reach
```

**Real example:**
```
Aapka ad 300,000 baar dikha (impressions)
100,000 alag-alag logon ne dekha (reach)
→ frequency = 300,000 ÷ 100,000 = 3

Yaani average har banda 3 baar dekha.
```

### 🔴 Frequency ka window — "per week"

VOW platform par likha hai: *"The number of times an ad is shown to one user **per week**."*

To `kpi_target_value = 3` ka matlab **hafte me 3 baar**, poore campaign me 3 baar nahi. Ye bahut bada farak hai — 4 hafte ka campaign me total 12 exposures.

### 🔴 Frequency target forecast BADAL DETA HAI (Comment 10 ka core)

```
impressions budget aur CPM se FIX hain — ye badal nahi sakte.
To frequency target set karne ka matlab hai reach target set karna:

   impressions = budget ÷ effective CPM × 1000
   reach       = impressions ÷ target frequency

Example:
   £10,000 ÷ £33.33 CPM × 1000 = 300,000 impressions   (fix)
   
   Target frequency 3  →  reach chahiye  100,000 log
   Target frequency 5  →  reach chahiye   60,000 log
   Target frequency 2  →  reach chahiye  150,000 log
```

**Aur repair loop isi par chalta hai:**
```
Target frequency = 3, matlab 100,000 log chahiye.
Forecast aaya: reach 60,000, frequency 5.

Diagnosis: audience BAHUT TIGHT hai.
Wahi 300,000 impressions kam logon par gir rahi hain — har banda 5 baar dekh raha hai.
Wo irritating hai (ad fatigue) aur paise waste ho rahe hain.

Fix: audience widen karo → zyada log → frequency 3 par aayegi.
```

🔴 **Target ke bina agent ke paas compare karne ke liye kuch nahi hai.** Forecast "frequency 5" aaya — accha hai ya bura? Pata nahi. Target 3 pata hone se hi bura hai.

### 🔴 Reach jodi nahi jaa sakti (bahut zaroori)

```
Prime Video par reach   132,713
Netflix par reach        71,120
                        ────────
Jod?                    203,833   ← ❌ GALAT!

Kyun? Wahi banda dono par dekh sakta hai. Double count ho jaayega.
Isko "deduplication" kehte hain — aur cross-platform deduplication
maujood nahi hai.

Maine staging par verify kiya:
   API ka total_reach = 233,803
   Sum of supplies    = 203,833
   → API ka number ZYADA hai, sum se
```

**Rule: reach kabhi khud add na karo. API jo `total_reach` de, wahi use karo.**

Par **impressions add ho sakti hain** — kyunki wo events hain, log nahi:
```
647,856 + 212,860 = 860,716  ✅  API ka total bilkul yahi
```

**Ek exception:** Alag-alag **market** ki reach add ho sakti hai — kyunki UK ka banda US me nahi dekhega. Schema me Comment 8 me yahi likha hai.

---

## A11. Endemic vs Non-Endemic (On/Off Amazon)

| | **Endemic** (On Amazon) | **Non-Endemic** (Off Amazon) |
|---|---|---|
| Matlab | Advertiser **Amazon par bechta hai** | Apni website par bechta hai |
| Example | Samsung TV Amazon par | BrightPath education courses |
| VOW ka field | `SOLD_ON_AMAZON` | `NOT_SOLD_ON_AMAZON` |
| Tracking kaise | **ASIN** se | **Ad Tag** se |
| ASIN required? | ✅ Haan | ❌ Nahi (optional) |
| Kya track hota hai | DPV, Add-to-cart, Purchase, ROAS | Page view, Checkout, Application |

**ASIN kya hai:** *Amazon Standard Identification Number* — Amazon par har product ka unique ID, jaise `B08N5WRWNW`. Ye bata deta hai *"ye mera product hai, iski sales dekho"*.

**Ad Tag kya hai:** Ek JavaScript snippet jo advertiser apni website par lagata hai. Jab koi banda ad dekh kar site par aaye, tag Amazon ko batata hai *"conversion hua"*.

🔴 **Ad tag pehle install hona chahiye.** Tag campaign se pehle lagana padega — kyunki tag sirf **lagne ke baad** ka data record karta hai. Pehle ka nahi.

### 🔴 Halo Sales — ek dilchasp cheez

Non-endemic advertiser bhi ASINs de sakta hai. Kyun?

```
BrightPath education courses apni website par bechta hai — Amazon par nahi.
Par Amazon par education books bikti hain.

BrightPath CTV ad chalata hai → log education ke baare me sochte hain
→ kuch log Amazon par jaakar education books kharidte hain

Ye "halo sales" hai — indirect asar.
BrightPath category ke ASINs jod kar ye asar dekh sakta hai.
```

Isi liye VOW platform Off Amazon par bhi ASIN field dikhata hai — **par required nahi karta.** Maine test kiya: Off Amazon par zero ASINs se bhi next step par jaa sakte hain. On Amazon par invalid ASIN rok deta hai.

---

## A12. Baaki sab technical shabd

### Attribution Window

**14-day post-view aur post-click** (schema §2.2).

```
Matlab: Aapne ad dekha 1 September ko.
        Aap 12 September ko product kharidte ho.
        → Wo sale is ad ko CREDIT milti hai (14 din ke andar hai)
        
        Aap 20 September ko kharidte ho.
        → Credit nahi milti (14 din se zyada)
```

**Post-view** = dekha, click nahi kiya. **Post-click** = click kiya. CTV me sirf post-view relevant hai (click hi nahi hota).

### ROS / RON

| Term | Poora naam | Matlab |
|---|---|---|
| **ROS** | Run of Service | Publisher ke poore service par kahin bhi — Prime Video par koi bhi show |
| **RON** | Run of Network | Poore network par kahin bhi — aur bhi khula |

**ROS sasta hota hai** kyunki aap choose nahi kar rahe. **Genre-specific mehnga** hota hai.

```
Maine staging par dekha (schema me bhi likha hai):
   Prime Video ROS      $18.22 CPM
   Prime Video Action   $22.07 CPM
   
Farak $3.85 — kyunki Action dekhne wale specific audience hain.
```

Isi ko schema **"genre upsell"** kehta hai — agent brief padh kar suggest kare *"aapke brief me sports ki baat hai, Action genre £4 zyada me behtar match hoga"*.

### Instream position

```
PRE-ROLL   →  show shuru hone se pehle    (sabse mehnga — sabse zyada dekha jaata hai)
MID-ROLL   →  show ke beech me            (accha — log wapas aate hain)
POST-ROLL  →  show khatam hone ke baad    (sasta — log chale jaate hain)
```

### Frequency Cap

**"Ek bande ko max kitni baar dikhao"** ki limit.

```
Frequency cap = 3 per week
→ ek banda hafte me 3 baar se zyada nahi dekhega

Kyun zaroori: 
  Cap ke bina, chhoti audience par bada budget → ek banda 20 baar dekhega
  → wo naraz ho jaayega ("ad fatigue")
  → brand ko nuksan, paise waste
```

🔴 Ye **advertiser-level setting** hai (Comment 13) — kyunki ye brand ki policy hai, campaign ka faisla nahi.

### Brand Safety / Content Exclusions

```
BrightPath education advertiser hai.
Wo nahi chahta ki uska ad:
  ✗ violent content ke saath chale
  ✗ adult content ke saath chale
  ✗ news of tragedy ke saath chale

Ye "content category exclusions" hain — brand safety.
```

Ye bhi advertiser-level policy hai.

### Curation

```
Kuch inventory ka deal PEHLE SE bana hua hota hai (pre-curated) —
turant use kar sakte ho.

Kuch ka nahi. Disney+ ke liye:
  1. Trader bolta hai "Disney+ chahiye"
  2. VOW Disney+ se baat karta hai
  3. IO (Insertion Order) sign hota hai
  4. Deal banta hai
  5. Ab use kar sakte ho
  
Ye "curation" hai. Isme din/hafte lagte hain.
```

Isliye schema me **teen tiers** hain (§2.3): Amazon-owned (turant), 3P pre-curated (turant), 3P needs-curation (baad me).

### Bid Request Volume

**Kitni inventory available hai** — supply ka size.

```
Deal object me:
  "bid_request_volume": 1457882193    ← 1.46 billion requests
  
Matlab: is deal par 1.46 billion baar "koi ad chahiye?" ka sawaal aaya.
Bada number = badi supply = zyada chance ki aapko slot milega.
```

🔴 Maine dekha ki third-party deals me ye `1` hai — placeholder, asli data nahi. Ye **data quality issue** hai.

### DSP-related terms

| Term | Matlab |
|---|---|
| **IO** | Insertion Order — ad khareedne ka legal contract |
| **Flight dates** | Campaign kab se kab tak chalega |
| **Pacing** | Budget ko flight me barabar phailana (ek din me khatam na ho) |
| **Under-delivery** | Poora budget kharch nahi hua — plan fail |
| **Ad fatigue** | Ek banda bahut baar dekh chuka, ab irritate ho raha hai |
| **Dayparting** | Din ke specific waqt par chalana (VOW me abhi nahi hai) |
| **Deduplication** | Ek banda do jagah gina gaya — usko ek ginna |

### Metrics — poori list

| Metric | Poora naam | Formula | CTV me relevant? |
|---|---|---|---|
| **CTR** | Click-through rate | clicks ÷ impressions | ❌ (click nahi hota) |
| **VCR** | Video completion rate | completions ÷ impressions | ✅ Bahut |
| **VR** | View rate / viewability | viewable ÷ impressions | ✅ |
| **DPVR** | Detail page view rate | DPVs ÷ impressions | Sirf endemic |
| **CPA** | Cost per acquisition | spend ÷ conversions | Conversion goal me |
| **ROAS** | Return on ad spend | revenue ÷ spend | Conversion goal me |
| **ACOS** | Advertising cost of sale | spend ÷ revenue (ROAS ka ulta) | Conversion goal me |
| **eCPM** | Effective CPM | spend ÷ impressions × 1000 | ✅ |
| **CPVC** | Cost per video completion | spend ÷ completions | ✅ CTV me kaam ka |

🔴 **CTV me sirf ye kaam ke hain:** reach, frequency, impressions, VCR, VR, eCPM, CPVC. Baaki click ya conversion par depend karte hain — aur wo CTV me kamzor hain. **Isi liye goal FIXED = Awareness hai.**

---
---

# PART B — Strategy Schema Document ki Structure

Comments samajhne se pehle **document ka naksha** pata hona chahiye. Kyunki David ke comments document ke specific jagah par baithe hain, aur *"kahan"* ka jawab dena padta hai.

## B1. Ye document kya hai aur kyun bana

**Kya hai:** VOW ke Strategy Module ko **agentic** banane ka blueprint. Yaani wo 6-step wizard jise trader manually bharta hai — usko AI agent chat se bhar de.

**Version history:**
```
v1.1.0   →  Pehla draft. 6-step UI wizard ka seedha copy.
             Display + OLV + CTV — sab kuch cover karta tha.
             
v2.0     →  CTV-first kar diya. Order badal diya (wizard ka nahi, agent ka flow).
             13 steps banaye. Client feedback (v5 flow) shamil kiya.
             ← YAHI Confluence par hai, ISI par David ne 28 comments kiye
             
v3.0     →  28 comments address kiye. Structure v2.0 jaisa hi rakha
             (kyunki comments apni jagah anchored rehne chahiye).
             ← Ye maine banaya
```

**Status:** *"For client verification"* — yaani ye final nahi hai, client ko verify karna hai. Isi liye David ne comment kiye.

## B2. Document ke 6 bade hisse

```
1. Core Principles          3 principles — agent kaise behave karega
2. Business Logic           §2.1 to §2.4 — domain rules
3. The Agentic Flow         13 steps — ye document ka 70% hai
4. API Catalogue            kaunsa endpoint kahan
5. Pydantic Schemas         actual code models
6. LangGraph State Machine  nodes aur edges
```

## B3. Section 1 — Teen Core Principles (UNCHANGED)

| Principle | Matlab | Kyun zaroori |
|---|---|---|
| **Zero-Hallucination Policy** | Agent **kabhi** parameters, metrics, targeting, ya deal IDs invent nahi karega. Sirf wo values use karega jo VOW database ya API se verified hain | Advertising me galat number = galat paise kharch |
| **Self-Filling Form Paradigm** | Agent ek **stateful slot-filling engine** hai (LangGraph par). Chat ya brief se input aata hai, Pydantic slots me bharta hai | Form khud bharta hai, trader se nahi puchta |
| **API-Driven Tool Execution** | Har step ka ek official VOW API endpoint hai | Agent apne se kuch nahi karta, platform ke through karta hai |

🔴 **Zero-Hallucination principle Comment 18 me directly use hota hai:** agar deal ki targeting sirf deal ke NAAM me hai (structured field me nahi), to agent ko string parse karna padega — jo is principle ke khilaf hai.

## B4. Section 2 — Business Logic ke 4 hisse

| § | Kya hai | Kis comment ka target |
|---|---|---|
| **2.1** | Product Attribution & Selling Locations — On/Off Amazon | (indirect: Comment 16, 17) |
| **2.2** | Attribution Window — 14-day post-view aur post-click | — |
| **2.3** | **Deal Types + 3 Inventory Tiers** | 🔴 **Comment 1** |
| **2.4** | **Audience Set Profiles + fees** | 🔴 **Comment 2, 4** |

### §2.3 ki table — jo Comment 1 ka target hai

```
| Tier                   | Examples          | Deals              | Reach forecast | Audiences        |
| Amazon owned           | Prime Video       | Pre-curated        | Available      | Amazon audiences |
| 3P pre-curated         | Netflix, Hulu     | Pre-curated        | Not available  | ??? ← comment    |
| 3P needs curation      | Disney+, others   | Rate-card only     | Not available  | ??? ← comment    |
```

**Teen tiers ka matlab:**
```
Amazon owned          → Prime Video. Deal ready hai. Reach forecast MILTA hai.
3P pre-curated        → Netflix, Hulu. Deal ready hai. Reach forecast NAHI milta.
3P needs curation     → Disney+. Deal READY BHI NAHI hai — VOW banayega, IO ke baad.
```

🔴 **Ye "primary fork" hai** — poora downstream branching isi par depend karta hai.

### §2.4 ki table — jo Comment 2 aur 4 ka target hai

```
| Profile   | Was (v1.1.0)                | Now                                          |
| 1         | Narrow (High Precision)     | Narrow — highly targeted, risk of underdelivery |
| 2         | Balanced (Recommended)      | Balanced — optimal blend, usual recommendation   |
| 3         | Broad (Maximum Scale)       | Wide — broad reach, less precision              |
```

**"Broad" ko "Wide" karne ki wajah:** client ki vocabulary "Wide" hai.

## B5. Section 3 — The Agentic Flow (13 Steps)

**Sabse zaroori baat:** v2.0 ne poora order badal diya. v1.1.0 UI wizard ka order tha. v2.0 **agent ke natural flow** ka order hai.

```
| v1.1.0 (UI wizard)     | v2.0 (agentic)                    |
|------------------------|-----------------------------------|
| Strategy details       | 1.  Basics (+ durations)          |
| Goal, KPI & bid        |     (Basics me merge)             |
| Deals                  | 2.  CTV inventory (3-tier fork)   |
| —                      | 3.  Budget split          NEW     |  ← Comment 3
| Audiences              | 4.  Audiences (optional)          |  ← Comment 4, 19, 20
| —                      | 5.  Targeting             NEW     |  ← Comment 5, 21, 22
| (forecast sub-step)    | 6.  Predict reach                 |
| —                      | 7.  Plan approval         NEW     |  ← Comment 23
| (create at end)        | 8.  Create real strategy          |  ← Comment 24
| Creatives              | 9.  Upload video creative         |  ← Comment 25
| —                      | 10. Creative approval     NEW     |  ← Comment 26
| (ASINs in step 1)      | 11. Tracking setup       MOVED    |  ← Comment 27, 28
| —                      | 12. Credit check          NEW     |
| Summary → create       | 13. Activate              NEW     |  ← Comment 27
```

### Har step ek line me

| # | Step | Kya hota hai |
|---|---|---|
| 1 | **Basics** | Name, dates, market, currency, durations, goal, KPI, budget, caps, format, categories |
| 2 | **CTV Inventory** | Channel choose, deals match, 3-tier fork, curation capture |
| 3 | **Budget Split** | Budget ko inventories aur durations me baantna |
| 4 | **Audiences** | 3 profiles suggest, ek chuno ya sab decline karo |
| 5 | **Targeting** | Location, instream position, device, exclusions |
| 6 | **Predict Reach** | Forecast + honesty rule + repair loop |
| 7 | **Finalise Plan** | DRAFT → FINALISED |
| 8 | **Create Strategy** | `POST /api/simple-strategies/` |
| 9 | **Upload Creative** | Video upload + duration check |
| 10 | **Creative Approval** | Per channel PENDING → APPROVED/REJECTED |
| 11 | **Tracking Setup** | ASINs + ad tag + conversions |
| 12 | **Credit Check** | Balance ≥ budget? |
| 13 | **Activate** | 🔴 **Join node** — sab prerequisites check, phir launch |

### 🔴 Steps 1–8 ordered hain, 9–12 parallel hain

```
Step 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8       (ORDERED — ek doosre par depend)
                                    │
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
              Step 9,10        Step 11         Step 12    (PARALLEL — koi order nahi)
              Creatives        Tracking        Credit
                    └───────────────┼───────────────┘
                                    ↓
                              Step 13 Activate       (JOIN NODE — sab check karta hai)
```

**Kyun 1-8 ordered:** inventory CPM decide karti hai → CPM impressions decide karti hai → forecast ko targeting chahiye. **Chain hai.**

**Kyun 9-12 parallel:** creative agency se aata hai (late aata hai), ad tag advertiser ke developers lagate hain (din lagte hain), credit finance ka matter hai. **Koi doosre par depend nahi.** — Ye **Comment 27** hai.

### Do "Table" jo har step me hoti hain

Har step ki structure ek jaisi hai:

```
### Step N: Naam
CHANGED/NEW/UNCHANGED — kya hua

**What was in v1.1.0:**
    ← purana content, HISTORICAL, isko chhua nahi jaata

**What it is now:**
    | Field | Type | Requirement | Source | Change from v1.1.0 |
    ← YAHAN changes hote hain

**API calls at this step:** ...
```

🔴 **Ye baat Wajahat ke saath issue ban gayi thi.** Wo *"What was in v1.1.0"* block compare kar rahe the — jo jaan-boojh kar untouched hai. Changes *"What it is now"* table me hain.

## B6. 🔴 Requirement aur Source — do alag columns (Comment 6 ka core)

v2.0 me sirf `Requirement` column tha. v3.0 me **Source** column joda gaya. Ye **poore document ka sabse bada structural change** hai.

```
Requirement  =  "Plan ko value CHAHIYE ya nahi?"
Source       =  "Wo value KAHAN SE aayegi?"

Ye do bilkul alag sawaal hain!
```

**Purani ghalti:**
```
| Strategy name | String | Required |
→ padhne wala samjhta hai: trader se PUCHNA padega
→ Galat! Naam agent GENERATE kar sakta hai
```

**Naya tareeka:**
```
| Strategy name | String | Optional | GENERATED |
→ Plan ko naam chahiye (hoga hi), par trader se nahi puchenge
```

### Source ki 9 values

| Source | Matlab | Example |
|---|---|---|
| **ASKED** | Agent seedha trader se puchega | KPI target value |
| **INFERRED** | Brief se padha; brief me na ho to puchega | Flight dates, market, budget |
| **DERIVED** | Doosre field se calculate | Currency (market se) |
| **GENERATED** | System banata hai | Strategy name |
| **ADVERTISER** | Advertiser ki settings se | Frequency cap, device type |
| **FIXED** | CTV ke liye constant | Format = streaming_tv, Goal = Awareness |
| **API** | API response se bharta hai | Rate card, inventory sources |
| **MATCHED** | Agent plan se khud nikalta hai | Selected deals |
| **LATER** | Is step me nahi | (ASINs pehle the) |

### 🔴 Nateeja — trader se sirf 3 cheezein puchi jaati hain

```
ASKED / INFERRED se aane wali cheezein:
   ✓ Market
   ✓ Budget
   ✓ Dates
   
Aur wo bhi brief me likhi ho to nahi puchenge!
   
Baaki SAB:  GENERATED, DERIVED, ADVERTISER, FIXED, API, MATCHED
```

**Ye Comment 6 ka poora point hai:** *"The trader should end up being asked for very little."*

## B7. Section 4, 5, 6 — chhote hisse

**§4 API Catalogue** — table of endpoints. Comment 24 me ye poora staging Swagger ke against re-check hua, **14 rows add/correct hue.**

**§5 Pydantic Schemas** — actual code:
```python
FormatEnum, CurrencyEnum, GoalEnum, KpiEnum, ApprovalStatusEnum,
PlanStatusEnum,                 # ← Comment 23 se NEW
AdvertiserSetting,              # ← Comment 13 se NEW
ActivationPrerequisitesSchema,  # ← Comment 27 se NEW
SelectedDealSchema, MarketBudgetBidSchema, CurationRequirementsSchema,
BudgetSplitSchema, StrategyPlanSchema
```

**§6 LangGraph State Machine** — nodes aur edges ka diagram. Comment 18 me ek node ka naam badla (`select_inventory` → `match_inventory_deals`), Comment 23 me ek `interrupt()` hata, Comment 27 me join node aaya.

---
---

# PART C — 28 Comments, Ek-Ek

## Kaise padhein

Har comment ka format:

```
Kahan            →  document me kis section/text par
David ne likha   →  actual comment (jitna maloom hai)
Pehle kya tha    →  document me us waqt kya likha tha
David kya keh rahe hain  →  seedha matlab
Maqsad           →  kyun kaha — asli wajah
Maine kya samjha →  🔴 YE BOLNA HAI jab koi puche
Real example     →  samajhane ke liye
Kya change kiya  →  v3.0 me kya hua
Mai puch sakta hoon      →  agar samajh na aaye
Wo mujhse puch sakte hain →  Q → A ready
```

## Comments ka naksha — ek nazar me

| # | Kahan | Ek line me |
|---|---|---|
| 1 | §2.3 Deal Types | 3P targeting Amazon **ya** SSP se — deal ke hisab se, tier ke hisab se nahi |
| 2 | §2.4 Audience Profiles | Fee profile se nahi, **data provider** se aati hai — aur compound nahi hoti |
| 3 | §3 Flow / Step 3 | Budget split **optional** hai |
| 4 | §3 Flow / Step 4 | Audiences **optional** hain, mandatory nahi |
| 5 | §3 Flow / Step 5 | Audiences targeting ka hissa hain; targeting **pre-filled** aati hai |
| 6 | Step 1 poori table | CTV ke liye **simplify karo**, baaki **imply karo** |
| 7 | Step 1 Strategy name | Naam **generate** karo, pucho nahi |
| 8 | Step 1 Target markets | Multi-market support hai? Har market ke liye dobara puchna padega? |
| 9 | Step 1 Primary currency | Currency **market se derive** hoti hai |
| 10 | Step 1 KPI | Frequency KPI ke saath **target value** chahiye (1–5) |
| 11 | Step 1 Market budgets | "Table" data type nahi hai — widget hai |
| 12 | Step 1 Base bids | CTV me **bid apply nahi hota** |
| 13 | Step 1 Frequency cap | **Advertiser par default** hota hai |
| 14 | Step 1 Formats | Format **hamesha `streaming_tv`** hai |
| 15 | Step 1 Product categories | **Advertiser par default** hai, ya brief se imply karo |
| 16 | Step 1 Selling location | **Chhod do** yahan se |
| 17 | Step 1 Product ASINs | **Baad me** aate hain |
| 18 | Step 2 Selected deals | Deals **match** hoti hain, **select** nahi |
| 19 | Step 4 constraints | Amazon audiences **3P inventory par bhi** chalti hain |
| 20 | Step 4 open question | `bundles.narrow/balanced/broad` **support nahi hai** |
| 21 | Step 5 Location | **Market ke country se default** hota hai |
| 22 | Step 5 Device type | Kuch advertisers **sirf CTV** chahte hain — advertiser level par set |
| 23 | Step 7 Plan Approval | Simplify kar diya — bas **status change**, manager approval nahi |
| 24 | Step 8 endpoint | `api/strategies` nahi, **`simple-strategies`** hoga |
| 25 | Step 9 Click-through URL | Streaming TV ke liye **optional** |
| 26 | Step 10 approval rows | **Per channel ek status** — Netflix/Disney hardcode na karo, Paramount/Channel 4 bhi ho sakta hai |
| 27 | Step 11 heading | Creatives se **pehle bhi** ho sakta hai — **koi order zaroori nahi** |
| 28 | Step 11 "Confirm with client" | Strategy **creation ke baad update** ho sakti hai |

---

## COMMENT 1 — 3P inventory par targeting kahan se aati hai

**Kahan:** §2.3 Deal Types, inventory tiers ki table, Audiences column me `"Their own targeting (adds CPM)"` par

**David ne kaha:** Third-party inventory par targeting **do jagah se** aa sakti hai — Amazon DSP se, **ya** inventory source (SSP) se. Amazon ka option **limited in functionality** ho sakta hai — kuch cases me sirf **device targeting** hi milti hai. Kaunse options milenge ye **deal-specific** hai.

**Pehle kya tha:**
```
| 3P pre-curated | Netflix, Hulu | ... | Their own targeting (adds CPM) |
```
Yaani document keh raha tha: *"3P inventory par SIRF unki apni targeting use ho sakti hai, aur wo CPM badha degi."*

**David kya keh rahe hain:** *"Sirf" galat hai. Choice hai — Amazon DSP ki targeting bhi 3P inventory par chal sakti hai. Aur wo choice tier se tay nahi hoti, deal se hoti hai.*

**Maqsad:** Document ne teen tiers ko **capability boxes** ki tarah treat kiya — jaise tier decide karta ho ki targeting kahan se aayegi. Asal me tier ye batata hai ki **deal exist karti hai ya nahi** aur **reach forecast milta hai ya nahi**. Targeting ek **alag dimension** hai jo per-deal decide hoti hai. David is galat mapping ko theek kar rahe hain.

**🔴 Maine kya samjha (ye bolna hai):**

> "Document keh raha tha ki Netflix ya Disney par targeting sirf unki apni SSP se aayegi. David ne bataya ki ye galat hai — Amazon DSP ki audiences bhi 3P inventory par lag sakti hain. To ye ek **choice** hai, do options me se.
>
> Par ek catch hai — Amazon ka option 3P par **limited** ho sakta hai. Kuch cases me sirf device targeting milti hai, poori audience targeting nahi.
>
> Aur sabse zaroori: kaunse options available hain ye **deal choose hone ke BAAD** pata chalta hai, planning ke waqt nahi. Isliye agent planning me ye promise nahi kar sakta.
>
> To tier ki table me Audiences column ab tiers ko alag nahi karta. Tier se jo **asal me** farak padta hai wo do cheezein hain: reach forecast milta hai ya nahi, aur deal exist karti hai ya nahi."

**Real example:**
```
Trader: "Netflix par chalao, aur healthy-food waali audience target karo"

Case A — Amazon audience Netflix par chal jaati hai:
   Netflix deal CPM        £22.96
   Amazon audience fee    + £1.63
   Effective CPM           £24.59
   → targeting_source = AMAZON_DSP

Case B — Netflix par Amazon audience limited hai (sirf device):
   Option 1: Netflix ki apni targeting use karo
             £22.96 + Netflix ka targeting fee (£3?) = £25.96
             → targeting_source = INVENTORY_SOURCE
   Option 2: Amazon audience use karo, par sirf device-level milega
             → poori healthy-food targeting nahi milegi

Aur ye pata KAB chalta hai? Deal match hone ke BAAD.
Isliye agent pehle keh nahi sakta.
```

**Kya change kiya (v3.0):**
- Audiences column dono 3P rows me update — *"Choice per deal — Amazon audiences (may be limited, e.g. device only) or targeting at the inventory source / SSP (adds CPM)"*
- Naya field: `targeting_source` = `AMAZON_DSP` / `INVENTORY_SOURCE`
- Note added ki Audiences column ab tiers ko separate nahi karta

**Mai unse puch sakta hoon:**
1. Kya Amazon audiences **aur** inventory source ki targeting **ek hi deal** par saath chal sakti hain, ya ek hi choose karna padta hai?
2. Amazon ki targeting 3P par kitni limited hoti hai practically? Kahan line khinchti hai — sirf device, ya demographic bhi milta hai? (Ye decide karega ki agent kya recommend kare)
3. Deal match hone ke baad ye capability **API se readable** hai, ya sirf VOW team ko manually pata hota hai?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Agar ye deal-specific hai to agent planning me kya bataye?"* | Agent planning me targeting **promise nahi karega**. Wo bolega *"Netflix par audience targeting available ho sakti hai, deal confirm hone par pakka bataunga."* Honesty rule ka hissa hai. |
| *"CPM par kya asar padega?"* | Dono raaston ka CPM alag hai. Amazon route me Amazon ki VCPM fee lagegi (£1.63). SSP route me unka apna targeting fee. Agent ko dono ka effective CPM dikhana chahiye. |
| *"Ye Comment 19 se kaise juda hai?"* | Bilkul ek hi baat hai, do jagah likhi hui. Comment 1 §2.3 table par hai, Comment 19 Step 4 ke constraints list par. Dono me "only" galat tha. |
| *"`targeting_source` kaun set karega?"* | Agent, deal match hone ke baad. Ye `DERIVED` source hai — plan pehle se nahi jaanta. |

---

## COMMENT 2 — Audience fee profile se nahi, data provider se aati hai

**Kahan:** §2.4 Audience Set Profiles, ke neeche jo NEW note tha — `"added fee consequence"` par

**David ne kaha:** *"There is not necessarily a fee consequence"* — aur jo fee hai wo **profile se driven nahi** hai. Teen rules diye:
1. **Fee kab lagti hai** — jab 1P data use ho, chahe Amazon ka ya kisi third-party ka first-party audience (Lifestyle, Interest)
2. **Compound nahi hoti** — ek provider se kitne bhi segments lo, ek fixed CPM
3. **Cross-provider stack hoti hai** — do providers use kiye to dono ki fee

**Pehle kya tha:**
```
NEW note: the audience fee (VCPM) stacks on top of the deal CPM,
so the agent should surface the effective CPM... The fee is set by
which data is used — not by how many segments are selected...
```
Document ye implication chhod raha tha ki **profile choose karna hi fee ka faisla hai** — jaise Narrow sasta ho, Wide mehnga.

**David kya keh rahe hain:** *Profile aur fee ka koi rishta nahi. Narrow, Balanced, Wide teeno me fee same hai — ya zero. Fee ka faisla data se hota hai, breadth se nahi.*

**Maqsad:** Ye ek **cost model** ki galti theek kar rahe hain — aur ye galti agent ke behaviour ko badal deti. Agar agent samjhe ki *"Wide mehnga hai"* to wo trader ko galat trade-off dikhayega. Asli trade-off **reach vs precision** hai, **cost** nahi.

**🔴 Maine kya samjha (ye bolna hai):**

> "Document ye samajh raha tha ki teen profiles ke teen daam hain — Narrow sasta, Wide mehnga. David ne bataya ki aisa nahi hai.
>
> Fee **data** se aati hai, breadth se nahi. Teen rules hain:
>
> Pehla — fee tab lagti hai jab aap 1P data use karo. Amazon ka data 1P hai. Experian jaisi company ka Lifestyle data bhi unka 1P hai. Sirf demographic (age, gender) free hai.
>
> Doosra — fee compound nahi hoti. Amazon se ek segment lo ya tees, ek hi £1.63 lagega. Ye important hai kyunki agent ko ye nahi sochna ki 'zyada segments = zyada mehnga'.
>
> Teesra — par **providers** stack hote hain. Amazon se bhi lo aur Experian se bhi, to dono ki fee — £1.63 + £2.00 = £3.63.
>
> To Narrow/Balanced/Wide me farak **reach aur precision** ka hai, **paise ka nahi**. Aur agent ko `audience_data_sources` track karna padega — kaunse provider use ho rahe hain, kitne segments nahi."

**Real example:**
```
Ek hi campaign, £10,000, deal CPM £22.96

Option A — Koi audience nahi (run of service)
   Effective CPM £22.96
   Impressions   435,540
   Fee           £0
   
Option B — Narrow: Amazon se 5 segments
   Effective CPM £24.59
   Impressions   406,669
   Fee           £1.63
   
Option C — Wide: Amazon se 30 segments
   Effective CPM £24.59      ← OPTION B KE BARABAR!
   Impressions   406,669
   Fee           £1.63       ← 6 guna segments, wahi fee
   
Option D — Amazon se 20 + Experian se 5
   Effective CPM £26.59
   Impressions   376,081
   Fee           £3.63       ← DONO providers ki

Dekho: B aur C ka daam bilkul same hai. Sirf reach alag hai.
Par D 5 extra segments par £2 zyada — kyunki naya PROVIDER aaya.
```

**Kya change kiya (v3.0):**
- Teen rules likhe gaye
- Naya field: `audience_data_sources` = `AMAZON_1P` / `THIRD_PARTY` / `NONE`
- Line add ki: *"Narrow, Balanced and Wide therefore differ in reach and precision, not in cost"*
- Fee value **API se** padhne ka rule — `GET /api/contextual-targeting/fees` (model `Fee`)
- Rule 3 detect karne ka tareeka — `POST /api/audiences/{market}/overlapping-audiences/` overlap batata hai

**Mai unse puch sakta hoon:**
1. Fee values hamesha `GET /api/contextual-targeting/fees` se padhein? Comment ke reply me £2.00 VCPM ka figure aaya tha — agar hardcode karein to stale ho jaayega
2. Kya sirf **Amazon** aur **third-party** do buckets hain, ya har third-party provider ka apna alag rate hai?
3. Ek segment jo **dono** providers me hai — kya dono ki fee lagegi ya ek?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"To profile choose karne ka faayda kya hai agar daam same hai?"* | Reach aur precision ka trade-off. Narrow me kam log par zyada intent — underdelivery ka risk. Wide me zyada log par kam precision. Daam nahi, **outcome** alag hai. |
| *"Agent trader ko kya dikhayega?"* | Teen options, har ek ka **effective CPM aur estimated impressions**. Do options ka CPM same hoga (same provider), reach alag. Trader ko ye saaf dikhna chahiye ki wo paise nahi, precision trade kar raha hai. |
| *"Free audience bhi hoti hai?"* | Haan. Maine staging par verify kiya — sirf **Demographic** aur **Device** category wali sets ka `video_fee = 0.00`. In-market, Lifestyle, Interest, Custom-built par £1.63. |
| *"Overlap ka pata kaise chalega?"* | `POST /api/audiences/{market}/overlapping-audiences/` endpoint hai. Isse double-fee case detect ho sakta hai, guess nahi karna padega. |

---

## COMMENT 3 — Budget split optional hai

**Kahan:** §3 Flow comparison table, `"Budget split NEW"` row par. (UI placement ka point ek alag comment se aaya)

**David ne kaha:** Budget split **optional** hai, required nahi. Aur ye standalone step nahi hona chahiye — Step 2 (CTV Inventory) ke andar ek substep hona chahiye.

**Pehle kya tha:**
```
| — | Budget split NEW |
```
Flow me ek poora naya step, jaise ye zaroori ho.

**David kya keh rahe hain:** *Split optional hai. Aur ye apna step deserve nahi karta — inventory ke andar hi dikha do.*

**Maqsad:** Do cheezein. Ek — trader par ek majboori kam karna. Do — flow ko chhota rakhna. Agar ek deal hi match hui to split karne ke liye kuch hi nahi hai — us case me ek poora step khaali dikhega.

**🔴 Maine kya samjha (ye bolna hai):**

> "Split ko optional hona chahiye, par ye **preferred** hai — aur wajah CPM hai.
>
> Har inventory aur har duration ka apna CPM hota hai. Prime Video £24, Netflix £22. 15-second £18, 30-second £24. Agar split kar diya to har hisse ka apna CPM lagta hai aur impressions ka number **accurate** aata hai.
>
> Agar split nahi kiya to agent ko **blended average** nikalna padega — aur wo approximate hai. Us case me agent ko **saaf bolna** chahiye ki ye estimate hai, exact nahi.
>
> UI ke hisab se: ye Step 2 ke andar substep hai, tab dikhega jab **ek se zyada** deal match ho. Ek deal me split karne ke liye kuch nahi hai.
>
> Behaviour: agent **khud ek split propose karega** by default, aur trader accept, adjust ya skip kar sakta hai."

**Real example:**
```
£10,000 budget, do inventory match hui:
   Prime Video   £24 CPM
   Netflix       £22 CPM

SPLIT KE SAATH (£5,000 each):
   Prime:   5000 ÷ 24 × 1000 = 208,333 impressions
   Netflix: 5000 ÷ 22 × 1000 = 227,273 impressions
   Total                     = 435,606 impressions   ← accurate

SPLIT KE BINA (blended average £23):
   10000 ÷ 23 × 1000 = 434,783 impressions   ← approximate

Farak sirf 823 impressions — chhota lag raha hai.

PAR agar CPM zyada alag ho:
   Prime Video   £40 CPM
   Netflix       £15 CPM
   
   Split ke saath: 125,000 + 333,333 = 458,333
   Blended (£27.5): 363,636
   
   Farak 94,697 impressions — 26% ka farak!
   
Isi liye split "preferred" hai.
```

**Split ke do methods (document me hain):**
```
EVEN_BY_BUDGET      →  same paise har inventory par
                       Prime £5,000, Netflix £5,000
                       Result: impressions UNEVEN (mehnga CPM = kam impressions)

EVEN_BY_IMPRESSIONS →  same impressions har inventory se
                       Result: paise UNEVEN (mehnga CPM = zyada spend)
```
Agent ko **batana padta hai** kaunsa method use kiya aur kyun. Document ka example: *"I've split evenly by impressions, which weights spend toward the 30s at its higher CPM."*

**Kya change kiya (v3.0):**
- Flow comparison me row *"Budget split NEW (optional)"* ho gayi
- Note add hua ki UI me ye Step 2 ka substep hai, tab dikhega jab >1 deal match ho
- Step numbering **jaan-boojh kar nahi badla** — comments apni jagah anchored rehne chahiye

**Mai unse puch sakta hoon:**
1. Kaunsa split method default hona chahiye — `EVEN_BY_BUDGET` ya `EVEN_BY_IMPRESSIONS`?
2. Kya agent ko brief se split infer karna chahiye? Jaise *"mostly Prime Video"* ka matlab 70/30?
3. Split ke bina blended estimate dikhaana kitna acceptable hai — ya split ko practically mandatory maan lein jab CPM me bada farak ho?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Optional hai to agent kya karega?"* | Agent ek split **propose karega** — chup nahi rahega. Trader accept, adjust ya skip kar sakta hai. Optional ka matlab trader ki majboori nahi, agent ki chuppi nahi. |
| *"Split skip kiya to kya nuksan?"* | Agent ko blended CPM se estimate dena padega, aur wo **bolna padega** ki ye approximate hai. CPM me bada farak ho to estimate 20-25% tak galat ho sakta hai. |
| *"Ye kahan store hota hai?"* | Koi API nahi — ye agent-side logic hai. Result `market_budgets` field me jaata hai strategy creation ke waqt. |
| *"Maine platform par kya dekha?"* | 🔴 Platform khud **auto 50/50 split** karta hai per format, creation ke baad. Maine verify kiya: £10,909.09 → £5,454.55 + £5,454.55. Aur Planner me editable hai. To ye kaam creation ke **baad** bhi ho sakta hai. |

---

## COMMENT 4 — Audiences optional hain, mandatory nahi

**Kahan:** §3 Flow comparison me `"mandatory"` shabd par (aur asar §2.4 aur Step 4 par bhi)

**David ne kaha:** Audiences **optional** hain. v1.1.0 me optional thi, v2.0 ne galti se mandatory kar diya — wo revert karo.

**Pehle kya tha:** v2.0 ne audiences ko mandatory promote kar diya tha — jaise har plan me audience honi hi chahiye.

**David kya keh rahe hain:** *Wapas optional karo. Trader teeno options decline kar sakta hai aur bina audience ke chala sakta hai.*

**Maqsad:** Ek asli use case bachana. Bina audience ke campaign chalana **valid strategy** hai — usko "run of service" kehte hain. Broad awareness ke liye ye theek hai, aur **sasta bhi** hai (koi data fee nahi).

**🔴 Maine kya samjha (ye bolna hai):**

> "Audiences optional hain. Agent hamesha teen options **suggest karega** — ye nahi badla. Par trader teeno **decline** kar sakta hai aur bina audience ke chala sakta hai.
>
> Us case ko 'run of service baseline' kehte hain — poori inventory par chalega, koi audience filter nahi. Aur kyunki koi 1P data use nahi hua, **koi data fee bhi nahi lagegi**. To ye asal me sasta option hai.
>
> Par iska ek bada asar hai jo document me note karna zaroori tha: **repair loop ka ek lever chala jaata hai.**
>
> Jab reach kam aati hai to agent ke paas kuch levers hote hain — audience widen karo, targeting relax karo, inventory badhao, bid badhao. Agar audience hi nahi chuni, to 'audience widen karo' lever **maujood hi nahi hai**. Aur Comment 12 ke hisab se CTV me bid lever bhi nahi hai.
>
> To agent ko **saaf bolna** chahiye jab uske paas relax karne ke liye kuch na bache — ye pretend nahi karna chahiye ki fix available hai."

**Real example:**
```
Trader: "£10,000, UK, awareness. Zyada se zyada log tak pahunchao."
Agent:  "Teen audience options hain:
           1. Narrow — 45,000 reach, high intent
           2. Balanced — 120,000 reach
           3. Wide — 280,000 reach
         Ya bina audience ke chala sakte hain — poori inventory,
         aur £1.63 ki data fee nahi lagegi, to 7% zyada impressions."
         
Trader: "Bina audience ke chalao. Broad awareness chahiye."
Agent:  "Theek hai. Run of service — koi audience filter nahi, koi data fee nahi.
         Ek baat bata dun: agar reach kam aayi to mai audience widen
         nahi kar sakta (audience hi nahi hai) aur CTV me bid bhi
         nahi badha sakta. Sirf targeting relax kar sakta hoon ya
         inventory badha sakta hoon."
```

**Kya change kiya (v3.0):**
- Flow comparison me *"Audiences (optional, suggestion-driven)"*
- Step 4 table me `Audience options` requirement **Optional** wapas
- Naya row: `Chosen option` — *"Trader picks one of the three, or declines them all and runs with no audience"*
- Repair loop ka consequence likha gaya

**Mai unse puch sakta hoon:**
1. Agar trader teeno decline kar de, to agent ko phir bhi 3 options dikhane chahiye ya sirf ek baar mention karke aage badh jaana chahiye?
2. Run-of-service default hona chahiye kuch cases me? Jaise broad awareness brief me?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Bina audience ke campaign ka matlab kya?"* | Poori matched inventory par chalega, koi audience filter nahi. Isko run-of-service kehte hain. Broad awareness ke liye valid hai. |
| *"Iska cost par kya asar?"* | Sasta. Koi 1P data use nahi hua → koi VCPM fee nahi → effective CPM = deal CPM → **zyada impressions** same budget me. |
| *"Repair loop par kya asar?"* | 🔴 Ek lever kam. Audience widen nahi kar sakte. Bache: targeting relax karo, inventory badhao, budget badhao, flight lamba karo. Aur agent ko bolna chahiye jab kuch na bache. |
| *"Documented kahan hai?"* | §2.4 me, aur Step 4 ke review note me. Reference: *"a run-of-service baseline, which also means no 1P data and therefore no data fee (see §2.4)."* |

---

## COMMENT 5 — Audiences targeting ka hissa hain, aur targeting pre-filled aati hai

**Kahan:** §3 Flow comparison me `"Targeting NEW"` row par

**David ne kaha:** Audiences targeting ka **ek kism** hai, alag stage nahi. Aur inventory tay hone ke baad trader ko **default targeting already lagi hui** dikhti hai — country targeting aur Connected TV device — phir wo refine karta hai ya accept kar leta hai.

**Pehle kya tha:** Step 4 (Audiences) aur Step 5 (Targeting) do alag steps the — jaise do alag kaam hain.

**David kya keh rahe hain:** *Ye do steps ek hain. Aur targeting khaali form nahi hai — bhari hui aati hai.*

**Maqsad:** Trader ka experience theek karna. Do alag steps ka matlab hai trader ko do baar rokna. Aur khaali form ka matlab hai trader ko sochna padega — jabki 90% cases me default hi theek hota hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Do baatein hain.
>
> Pehli — audience targeting ka ek kism hai. Country targeting bhi targeting hai, device targeting bhi targeting hai, audience segments bhi targeting hai. To Step 4 aur Step 5 ek hi step hain.
>
> Doosri, aur zyada zaroori — **targeting khaali nahi aati, bhari hui aati hai.** Inventory tay hone ke baad trader ko ek baseline already applied dikhta hai: market ka country, aur Connected TV device. Uske baad uske paas teen raaste hain — aur ye teeno **alternatives hain, sequence nahi:**
>
> - audience segments define karo
> - ya geography narrow karo — David ka example tha ek trader jo postcodes chahta hai, audiences nahi
> - ya baseline jaisa hai waise accept kar lo
>
> **Geography audience targeting ki jagah le sakti hai.** Ye bada point hai. 'London ke postcodes me chalao' bhi ek targeting strategy hai — audience segments ki zaroorat nahi.
>
> Practical nateeja: is step me **koi field khaali nahi** hoti, aur trader se blank targeting form kabhi bharwaya nahi jaata."

**Real example:**
```
Inventory tay ho gayi. Agent bolta hai:

"Targeting default lagi hui hai:
   Location:  United Kingdom
   Device:    Connected TV
   
 Aap chahein to:
   → audience segments jod dein (healthy food, parents…)
   → ya geography narrow karein (London, ya specific postcodes)
   → ya isi tarah rehne dein"

Trader A: "SW1, SW3, SW7 postcodes me chalao"
          → koi audience nahi, sirf geography. VALID.
          
Trader B: "healthy food waali audience"
          → audience segments. VALID.
          
Trader C: "theek hai, aise hi chalao"
          → baseline. VALID.

Teeno alag raaste hain. Koi bhi ek kaafi hai.
```

**Kya change kiya (v3.0):**
- Note add ki Steps 4 aur 5 flow me **ek step** hain (numbering nahi badli — comments anchored rehne ke liye)
- Step 5 table me **Source aur Default columns** add hue (Comment 21 se juda)
- Teen alternatives likhe gaye

**Mai unse puch sakta hoon:**
1. Baseline targeting agent khud banaye ya `POST /api/strategies/{id}/targeting/auto-rec/` use kare? Wo endpoint maujood hai aur lagta hai wahi kaam karta hai
2. Trader ne targeting narrow ki — agent turant re-forecast kare aur reach ka farak dikhaye, ya forecast step tak wait kare?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"To Step 4 aur 5 merge ho gaye?"* | Flow ki logic me haan. Document me numbering **jaan-boojh kar** waisi hai taaki comments apni jagah rahein. Ye presentation ka faisla hai, logic ka change hai. |
| *"Baseline me kya hota hai?"* | Location = market ka country, Device = Connected TV (advertiser ki setting se). Baaki fields optional hain aur khaali reh sakti hain. |
| *"Geography audience ki jagah le sakti hai?"* | Haan, aur ye David ka apna example tha. Postcode targeting ek poori strategy hai. Aur ye sasti bhi hai — koi data fee nahi. |
| *"Postcode targeting VOW me hai?"* | ✅ Haan. Maine staging Swagger me verify kiya: `POST /api/strategies/postcode-validation/{market}/`. To ye example buildable hai. |
| *"Platform par ye kahan hai?"* | 🔴 Ek problem hai — wizard me targeting step **nahi** hai. Saare targeting endpoints `/api/strategies/{id}/targeting/…` hain, yaani strategy ID chahiye. To targeting creation ke **baad** hoti hai, Locations section me. |

---

## COMMENT 6 — CTV ke liye simplify karo, baaki imply karo

**Kahan:** Step 1, dono v1.1.0 field lists par (jo Step 1 + Step 2 ke fields the)

**David ne kaha:** Is list ka bahut hissa **general strategy flow** se aaya hai, CTV flow se nahi. Do kaam karo — jo CTV me apply nahi hota **kaat do**, aur baaki **imply karo** (trader se pucho nahi).

**Pehle kya tha:** Step 1 me 13 fields, zyadatar **Required** — jaise trader ko poora form bharna padega. Multi-format choice, click-based KPIs (CTR, CPC, CPA, CPDPV), per-market base bid, sab.

**David kya keh rahe hain:** *Trader se bahut kam puchna chahiye. Baaki sab generate, derive, ya advertiser se lo.*

**Maqsad:** Ye **poore document ka sabse bada comment** hai. Baaki 27 me se lagbhag 10 isi ka detail hain. David ka asli point ye hai: **document ne UI wizard ko chat me copy kar diya tha.** Agent ka faayda ye nahi hai ki wo form ko chat me badal de — faayda ye hai ki **form bharne ki zaroorat hi na rahe.**

**🔴 Maine kya samjha (ye bolna hai):**

> "Ye do alag instructions hain ek comment me.
>
> **Pehla — kaato.** Multi-format choice, click-based KPIs, per-market base bid — ye teeno isliye the ki original flow Display aur non-CTV video bhi cover karta tha. CTV me format ek constant hai, daam deal se aata hai, aur click hi nahi hota. To in choices me **decide karne ke liye kuch nahi hai.**
>
> **Doosra — baaki imply karo.** Trader se practically sirf teen cheezein puchi jaani chahiye — market, budget, dates. Aur wo bhi brief me likhi ho to nahi puchenge.
>
> Isko implement karne ke liye maine table me ek **Source column** add kiya. Kyunki purani table me ek confusion tha: 'Required' ka matlab log samajh rahe the 'trader se puchna padega'. Wo galat hai. **Ye do alag sawaal hain:**
>
> - *Requirement* — plan ko value chahiye ya nahi?
> - *Source* — wo value kahan se aayegi?
>
> Ek field **required** ho sakti hai aur phir bhi trader se kabhi na puchi jaaye. Strategy name required hai — plan me naam hoga hi — par agent generate karega.
>
> Ye ek nazariye ka badlaav hai: **ye form nahi hai. Ye ek conversation hai jisme agent zyadatar cheezein khud pata kar leta hai.**"

**Real example:**
```
PURANA SOCH (form wala):
Agent: "Strategy ka naam?"
Agent: "Kaunsa market?"
Agent: "Currency?"
Agent: "Format? (Display/OLV/STV/Prime Video)"
Agent: "Goal? (Awareness/Consideration/Conversion)"
Agent: "KPI? (Reach/Frequency/CTR/CPC/CPA/CPDPV)"
Agent: "Product category?"
Agent: "Budget?"
Agent: "Base bid?"
Agent: "Frequency cap?"
Agent: "Dates?"
→ 11 sawaal. Trader sochta hai "isse to mai khud form bhar leta"

NAYA SOCH (agentic):
Trader: "BrightPath ke liye UK me £10,000 ka CTV campaign, September"

Agent andar hi andar:
   name         = GENERATED  → "Education_GB_Awareness_Sep2026"
   market       = INFERRED   → GB (brief me tha)
   currency     = DERIVED    → GBP (GB se)
   format       = FIXED      → ["streaming_tv"]
   goal         = FIXED      → AWARENESS (CTV hamesha)
   KPI          = INFERRED   → REACH
   category     = ADVERTISER → Education (BrightPath ki setting se)
   budget       = INFERRED   → 10000 (brief me tha)
   base bid     = DERIVED    → deal ke CPM se
   freq cap     = ADVERTISER → 3 (BrightPath ki setting se)
   dates        = INFERRED   → 2026-09-01 to 2026-09-30
   durations    = INFERRED   → puchna padega, brief me nahi tha

Agent: "Ek sawaal — creative kitne second ka hoga? 15 ya 30?"
→ EK sawaal. Baaki 10 khud pata kar liya.
```

**Kya change kiya (v3.0):**
- **Source column add hua** — 9 values ke legend ke saath
- Har row ki source set ki: 1 ASKED, 4 INFERRED, 2 DERIVED, 1 GENERATED, 3 ADVERTISER, 2 FIXED
- Cut kiya: 3 non-CTV formats, 4 non-awareness KPIs, base bid ka sawaal
- 2 rows poori hata di (Selling location, Product ASINs) — Comments 16, 17
- 3 open questions add hue

**Mai unse puch sakta hoon:**
1. Is table me kuch aisa bacha hai jo aap chahte ho trader se **seedha puchein**? Abhi list market, budget, dates par simat gayi hai
2. `Budget cap` maine ADVERTISER maan liya (frequency cap ki tarah). Ye advertiser par hota hai ya campaign par?
3. Jab agent kuch **infer** kare — kya wo dikha kar confirm karaye, ya sirf jo doubtful hai wahi puche? Pehla safe hai, doosra chhota

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Source column kyun add kiya, Requirement kaafi nahi tha?"* | Kyunki dono ek nahi hain. Requirement batata hai plan ko value chahiye ya nahi. Source batata hai wo kahan se aayegi. Purani table me 'Required' padh kar log samajh rahe the 'trader se puchna hai' — aur yahi galti poore document me thi. |
| *"Total kitne sawaal bachte hain?"* | Practically teen — market, budget, dates. Aur brief me likhe hon to zero. Ek conditional — KPI target value, sirf jab frequency KPI ho. |
| *"Trader ko pata chalega ki agent ne kya assume kiya?"* | Ye ek open question hai. Do options — sab dikhao (safe, lamba) ya sirf doubtful dikhao (chhota, risky). Maine question raise kiya hai, decide nahi kiya. |
| *"Baaki comments isse kaise jude hain?"* | Ye umbrella comment hai. Comments 7, 9, 10, 11, 12, 13, 14, 15, 16, 17 sab isi table ki individual rows par hain. David ne pehle poori list par point banaya, phir row-by-row confirm kiya. |

---

## COMMENT 7 — Strategy name generate karo, pucho nahi

**Kahan:** Step 1, `Strategy name` ke saamne `"Required"` par

**David ne kaha:** Naam auto-generated hona chahiye.

**Pehle kya tha:**
```
| Strategy name | String | Required |
```

**David kya keh rahe hain:** *Ye sawaal puchne ki zaroorat nahi. Agent naam bana sakta hai.*

**Maqsad:** Ek bekaar sawaal hatana. Naam me **koi planning decision nahi** hai — wo bas ek label hai jisse strategy baad me dhundhi jaaye. Us par sawaal kharch karna waste hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Naam ek label hai, faisla nahi. Isse plan me kuch nahi badalta — na budget, na inventory, na reach. Sirf list me dhundhne ke liye hai. To agent brief se bana lega.
>
> Convention: `{Category}_{Market}_{Goal}_{MonthYear}` — jaise `Education_GB_Awareness_Sep2026`.
>
> Uniqueness ka check waise hi rahega — `GET /api/strategies/check_strategy_name_uniqueness/`. Agar naam already hai to agent `_v2` laga kar dobara check karega, rukega nahi.
>
> Aur ek zaroori nukta: requirement **Optional** ho gaya aur source **GENERATED**. Ye do alag baatein hain — plan me naam hamesha hoga, par trader se kabhi maanga nahi jaayega, aur wo baad me rename kar sakta hai.
>
> 'Auto-generated' requirement level nahi hai. Wo **Source** column me jaata hai. Yahi Comment 6 ka Source column ka poora point hai."

**Real example:**
```
Brief: "BrightPath education courses ke liye UK me £10,000 ka
        CTV awareness campaign, September 2026"

Agent naam banata hai:
   Category  = Education   (advertiser ki setting se)
   Market    = GB          (brief se)
   Goal      = Awareness   (CTV me fixed)
   MonthYear = Sep2026     (flight dates se)
   
   → "Education_GB_Awareness_Sep2026"

Check karta hai: GET .../check_strategy_name_uniqueness/?name=Education_GB_Awareness_Sep2026
   → {"is_unique": false}    ← already exist karta hai!
   
   → "Education_GB_Awareness_Sep2026_v2"
   → {"is_unique": true}     ← chal gaya

Trader se ek bhi sawaal nahi. Agar usko naam pasand nahi to rename kar sakta hai.
```

**Kya change kiya (v3.0):**
- Requirement: Required → **Optional**
- Source: **GENERATED**
- Convention likhi gayi
- Collision handling likha gaya (`_v2` suffix, re-check)

**Mai unse puch sakta hoon:**
1. Traders ka koi **naming convention** already hai? Agar wo alag shape me naam dhundhte hain to hamara naam unki list scan karna mushkil kar dega. Better hai unki aadat se match karein
2. `{Category}` product category se aata hai, jo advertiser ki setting ya brief se aata hai. Agar dono na ho to uski jagah kya — advertiser ka naam, ya category ke bina chhota convention?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Naam Required tha to ab Optional kaise?"* | Requirement aur Source alag hain. Plan me naam hoga hi — wo guarantee hai. Par trader se **maanga** nahi jaayega. Optional ka matlab "trader ko dena zaroori nahi", "plan me nahi hoga" nahi. |
| *"Duplicate naam aaya to?"* | `_v2` suffix laga kar dobara check. Loop me chalega jab tak unique na mile. Trader ko rok kar puchna nahi. |
| *"Trader naam badal sakta hai?"* | Haan, kabhi bhi. Isi liye ye Optional hai — generated naam ek starting point hai, final nahi. |
| *"Convention kahan se aaya?"* | Maine propose kiya hai. Ye **open question** hai — traders ki apni aadat pata karni chahiye pehle. |

---

## COMMENT 8 — Multi-market: support hai? Aur har market ke liye dobara puchna padega?

**Kahan:** Step 1, `Target markets` ke saamne `"Multi-select"` par

**David ne poocha:** Kya multi-market support hai? Aur agar hai, to iska matlab har market ke liye choices dobara puchni padengi?

**Pehle kya tha:**
```
| Target markets | Multi-select | Required |
```
Document ne bas "Multi-select" likh diya tha — na ye kaha ki M1 me kitne markets, na ye kaha ki multi-market flow par kya asar padega.

**David kya keh rahe hain:** *Ye do sawaal hain. Scope kya hai, aur uska flow par kya asar?*

**Maqsad:** Ek design gap pakadna. Multi-market poore flow ko badal deta hai — budget per market, currency per market, deals per market, forecast per market. Document ne ye socha hi nahi tha. David chah rahe hain ki ye decide ho.

**🔴 Maine kya samjha (ye bolna hai):**

> "Do sawaal the, dono ke jawab hain.
>
> **Scope:** Recommendation hai **M1 me ek market per strategy** — par field ko **list hi rakhna** hai. Isse baad me multi-market add karna rebuild nahi banega, sirf ek extension. Agar brief me kai markets hain to agent **saaf bolega** aur ek se shuru karne ka proposal dega — chupke se ek uthaa nahi lega.
>
> **Doosra sawaal — kuch bhi do baar nahi puchna chahiye.** Maine list banayi ki kya per-market varies karta hai aur kya ek baar puchta hai:
>
> Per market: budget, currency, matched deals (aur isliye CPM), available locations, available product categories, reach forecast.
>
> Ek baar: flight dates, goal, KPI, creative durations, audience choice, creatives aur unki approval, tracking, credit check.
>
> **Do cheezein aasani se miss ho jaati hain:** locations aur product-categories dono endpoints **market se keyed** hain — yaani wo lists market ke hisab se alag hoti hain, chahe trader ka iraada same ho.
>
> Aur ek zaroori technical baat: **reach markets ke across add ho sakti hai**, kyunki audiences overlap nahi karti — UK ka banda US me nahi dekhega. Par **ek hi market ke andar providers ke across add nahi ho sakti**, kyunki wahi banda Prime Video aur Netflix dono par dekh sakta hai aur deduplication nahi hoti."

**Real example:**
```
Brief: "UK aur Germany me £20,000 ka campaign"

M1 me agent:
"Brief me do markets hain — UK aur Germany. Abhi ek strategy ek market
 support karti hai. UK se shuru karun £10,000 par, aur Germany ke liye
 alag strategy banaun? Ya poora £20,000 UK par?"

Agar multi-market hota, to per market:
   UK:  budget £10,000, currency GBP, apni deals, apna forecast
   DE:  budget €11,500, currency EUR, apni deals, apna forecast
   
   Aur locations list alag:
      GET /api/strategies/locations/GB/  →  London, Manchester, …
      GET /api/strategies/locations/DE/  →  Berlin, Munich, …
      
   Product categories bhi alag:
      GET /api/contextual-targeting/GB/product-categories/
      GET /api/contextual-targeting/DE/product-categories/
      → Education category dono me ho, ye guarantee nahi!

Par ek baar puchenge: dates, goal, KPI, durations, creatives.

Reach:
   UK reach 150,000 + DE reach 180,000 = 330,000   ✅ ADD HO SAKTI HAI
   (koi banda dono me nahi hai)
   
   Par UK ke andar:
   Prime 132,713 + Netflix 71,120 = 203,833        ❌ ADD NAHI HO SAKTI
   (wahi banda dono par dekh sakta hai)
```

**Kya change kiya (v3.0):**
- Recommendation likhi: **ek market per strategy M1 me**, field list hi rahe
- Poori table banayi: per-market vs campaign-level
- Reach summing ka rule likha (markets ke across haan, providers ke across nahi)
- 3 open questions

**Mai unse puch sakta hoon:**
1. M1 ke liye ek market acceptable hai, ya pehle release me multi-market chahiye? Isse budget split, currency rule aur per-market deal matching sab affect hote hain
2. `primary_currency` abhi ek field hai. Multi-market me — plan ka total advertiser ki primary currency me dikhayein aur har market ka spend uski apni currency me, ya poora plan ek currency me?
3. Brief me kai markets hain aur M1 ek support karta hai — agent puche ki kis se shuru karein, ya pehle wale se shuru kare aur bata de?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Field list kyun rakhi jab ek hi market hai?"* | Taaki multi-market baad me add karna schema migration na bane. Ek market wala plan ek-element list bhejega. Code same rahega. |
| *"Reach add ho sakti hai ya nahi?"* | Markets ke across **haan** — audiences overlap nahi karti. Ek market ke andar providers ke across **nahi** — deduplication nahi hoti. Maine ye staging par verify kiya: API ka `total_reach` sum se **zyada** aaya. |
| *"Kya-kya per market varies karta hai?"* | Chhah: budget, currency, matched deals/CPM, available locations, available product categories, reach forecast. |
| *"Platform par kitne markets hain?"* | 🔴 Sirf **do** — UK aur US. Maine filter dekha. To Germany ka example theoretical hai. |

---

## COMMENT 9 — Currency market se derive hoti hai

**Kahan:** Step 1, `Primary currency` ke saamne `"Required"` par

**David ne kaha:** Currency market se derive honi chahiye, puchni nahi.

**Pehle kya tha:**
```
| Primary currency | Dropdown | Required |
```

**David kya keh rahe hain:** *Market pata hai to currency bhi pata hai. Dropdown hatao.*

**Maqsad:** Ek aur bekaar sawaal hatana — Comment 6 ka hi ek instance. GB chuna to GBP hi hoga. Trader ko dropdown dikhana time waste hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Single-market strategy me currency koi faisla nahi hai — wo market ke saath aa jaati hai. `GB → GBP`, `US → USD`, `DE` ya `FR → EUR`.
>
> To dropdown hat gaya. Requirement **Optional** ho gaya, source **DERIVED**. Plan me currency hamesha hogi, par trader se kabhi puchi nahi jaayegi — aur wo override kar sakta hai.
>
> Ye bilkul strategy name jaisa case hai: 'auto-derived' requirement level nahi hai, wo Source me jaata hai. Requirement aur Source alag rakhna — yahi Source column add karne ka poora maqsad hai.
>
> Multi-market ke liye proposal hai: campaign ka total advertiser ki primary currency me dikhao, aur har market ka spend us market ki currency me. Par wo Comment 8 ke neeche question ke roop me hai, yahan settle nahi kiya."

**🔴 Ek zaroori baat — platform par reality different hai:**

> "Maine staging par check kiya aur ek problem mili. `Primary currency` field **`€ - EUR` pehle se bhari hui** aati hai — market chunne se **pehle**. Aur `United Kingdom` chunne ke baad bhi **EUR hi rehti hai.**
>
> Yaani platform par currency **market se derive nahi hoti** — wo advertiser ki setting se aati hai.
>
> Aur maine strategy list me ek `NOK` (Norwegian krone) wali strategy dekhi jiska market `US` tha. Agar currency market se derive hoti to ye possible nahi hota.
>
> To David ka comment **agent ke behaviour ke liye sahi hai** (trader se puchna nahi chahiye) par **mechanism galat hai** — source `ADVERTISER` hona chahiye, `DERIVED` nahi. Ye ek correction hai jo main schema me flag kar raha hoon."

**Real example:**
```
David ka proposal:
   markets = ["GB"]  →  primary_currency = "GBP"     (DERIVED)

Platform ki reality (maine dekha):
   Advertiser ki default = EUR
   markets = ["GB"]  →  primary_currency = "EUR"     (ADVERTISER)
                         markets_info[0].currency = "GBP"
                         
   Aur platform conversion karta hai:
      Market view:   £10,000
      Primary view:  €10,909.09
      (rate ~1.0909)

To DO currencies hain, dono asli, dono payload me jaati hain.
```

**Kya change kiya (v3.0):**
- Requirement: Required → **Optional**
- Source: **DERIVED**
- Mapping likhi: GB→GBP, US→USD, DE/FR→EUR
- 2 open questions

**Mai unse puch sakta hoon:**
1. `CurrencyEnum` me sirf EUR, GBP, USD hain. Jis market ki currency in teeno me na ho — enum extend karein ya wo markets scope se bahar?
2. Trader currency override kar sakta hai? Agar kare to plan ka total aur deal CPMs disagree karenge, jab tak kahin rate apply na ho
3. 🔴 **Ye maine khud add kiya:** Platform par currency advertiser ki default se aa rahi hai, market se nahi — maine `NOK`/`US` waali strategy dekhi. To source `ADVERTISER` hona chahiye ya `DERIVED`?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Optional hai to plan me currency hogi ya nahi?"* | Hogi, hamesha. Optional ka matlab trader se nahi maangenge. |
| *"Multi-market me kaunsi currency?"* | Proposal: total advertiser ki primary me, per-market spend uski apni me. Par ye **open question** hai, settle nahi hua. |
| *"Platform par kya dekha?"* | 🔴 EUR pehle se bhari aati hai, GB chunne par bhi EUR rehti hai. Aur `NOK` currency wali US strategy exist karti hai. To mechanism ADVERTISER hai, DERIVED nahi. |
| *"Currency mismatch se kya problem?"* | Budget ek currency me aur CPM doosri me ho to `impressions = budget ÷ CPM × 1000` **galat** aayega. GBP/EUR rate par ~9% ka farak. Poora hisaab ek currency me karna padega aur batana padega kaunsi. |

---

## COMMENT 10 — Frequency KPI ke saath target value chahiye

**Kahan:** Step 1, `KPI` row par

**David ne kaha:** KPI ke saath ek **target value** hona chahiye — range 1 se 5.

**Pehle kya tha:**
```
| KPI | Select | Required |  ← reach ya frequency
```
Sirf KPI ki kism record hoti thi. **Number kahan jaayega, wo jagah hi nahi thi.**

**David kya keh rahe hain:** *Agar trader frequency choose kare, to wo kitni frequency chahta hai — wo number kahan store hoga?*

**Maqsad:** Ek missing field pakadna. "Frequency" KPI bina number ke adhoora hai. "Mujhe frequency chahiye" ka koi matlab nahi — "mujhe frequency 3 chahiye" ka matlab hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Frequency KPI choose karna record ho raha tha, par jo **number** trader chahta hai uske liye jagah hi nahi thi. Naya field `kpi_target_value` — integer, **2 se 5** inclusive. Sirf tab dikhega jab KPI frequency ho, reach me absent.
>
> Comment me '1-5' likha tha. Maine platform check kiya — dropdown **2, 3, 4, 5** deta hai. 1 offer hi nahi hota. Aur 1 na hona **sahi** hai: frequency 1 ka matlab hai har banda ek hi baar dekhega, jo frequency **target** hi nahi hai — wo frequency target ka **na hona** hai.
>
> Aur sabse zaroori baat — **ye sirf label nahi hai, ye forecast badal deta hai.**
>
> Impressions budget aur CPM se pehle se fix hain. To frequency target set karna asal me **reach target** set karna hai:
>
> ```
> impressions = budget ÷ effective CPM × 1000
> reach       = impressions ÷ target frequency
> ```
>
> 300,000 impressions par target 3 ka matlab plan ko **100,000 log** tak pahunchna hai.
>
> Aur repair loop isi par chalta hai: agar forecast frequency 5 batata hai, matlab audience **bahut tight** hai — wahi impressions kam logon par gir rahi hain. **Target ke bina agent ke paas compare karne ke liye kuch nahi hai.**"

**Real example:**
```
Trader: "£10,000, frequency KPI, target 3"

Agent calculate karta hai:
   effective CPM £33.33
   impressions = 10000 ÷ 33.33 × 1000 = 300,000
   reach chahiye = 300,000 ÷ 3 = 100,000 log

Forecast chalata hai. Result: reach 60,000, frequency 5.

Agent ka diagnosis:
   "Target 3 tha, forecast 5 de raha hai. Audience bahut tight hai —
    300,000 impressions sirf 60,000 logon par gir rahi hain, yaani
    har banda 5 baar dekhega. Wo irritating hoga aur paise waste honge.
    
    Audience widen karta hoon — Balanced se Wide karke.
    
    Naya forecast: reach 105,000, frequency 2.86. Target ke paas hai. ✅"

TARGET KE BINA:
   Forecast: frequency 5.
   Agent: "…5 accha hai ya bura? Pata nahi."
   → repair loop trigger hi nahi hoga
```

**Kya change kiya (v3.0):**
- Naya row: `KPI target value` | Number | Conditional | ASKED
- Range **2–5** (comment ke 1–5 se corrected, platform ke against verified)
- Formula likha gaya, repair loop ka connection likha gaya
- 3 open questions

**Mai unse puch sakta hoon:**
1. Target forecast aur repair loop ko feed kare (jaise maine likha), ya sirf reporting ke liye record ho? Dono se agent ka behaviour bilkul alag hoga
2. KPI frequency hai par trader ne target nahi bataya — agent 3 assume kar le (beech ka number), ya khaali chhode aur bina target forecast kare?
3. **Reach** KPI ke liye bhi koi target hota hai, ya sirf frequency me number aata hai?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"1-5 kaha tha, tumne 2-5 kyun kiya?"* | Maine platform ka dropdown check kiya — wo 2, 3, 4, 5 deta hai. Aur 1 hatana logically sahi hai: frequency 1 target nahi, target ka absence hai. |
| *"Frequency ka window kya hai?"* | 🔴 **Per week.** Platform par likha hai: *"The number of times an ad is shown to one user per week."* To target 3 = hafte me 3 baar, poore flight me nahi. 4 hafte me total 12. |
| *"Ye forecast kaise badalta hai?"* | Impressions fix hain (budget ÷ CPM). Frequency target set karna reach target set karna hai. Forecast usse compare hota hai. Isliye ye label nahi, ek constraint hai. |
| *"Platform par ye field kahan hai?"* | Step 2 me, **per format**. Label: *"KPI target value for Prime Video deals format"*. To ek strategy me Streaming TV ka reach target aur Prime Video ka frequency target dono ho sakte hain. |

---

## COMMENT 11 — "Table" data type nahi hai, widget hai

**Kahan:** Step 1, `Market budgets` ke saamne `"Table"` par

**David ne poocha:** Kya ye ek single market budget hai? (Aur implicitly — "Table" yahan kya kar raha hai?)

**Pehle kya tha:**
```
| Market budgets | Table | Required |
| Base bids      | Table | Required |
```

**David kya keh rahe hain:** *Ek market hai to ek budget hai. Table kyun likha hai?*

**Maqsad:** Do baatein. Turant — ek market me ek number hai, table ki zaroorat nahi. Aur gehri baat — **Type column me UI widget likha hua hai.** Type batata hai field me kya hai. Wo kaise draw hoga wo interface ka kaam hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Turant point: ek market hai to ek budget hai, aur ek number ke liye table dikhana ajeeb hai.
>
> Gehri baat — **Type column me widget aa gaya tha.** 'Table' data type nahi hai, wo screen par kaise dikhta hai wo hai. Type batana chahiye field **kya rakhti hai**; kaise draw hogi wo interface decide karta hai.
>
> Ye same galti Base bids me bhi thi — wahan bhi 'Table' likha tha.
>
> Ab dono ek amount per market ke roop me likhe hain. Schema neeche wahi hai: `market_budgets: list[MarketBudgetBidSchema]` — list rehti hai taaki multi-market rebuild na bane — par single-market plan ek number maangta hai. Aur practically wo brief se aata hai, kyunki briefs budget batate hain.
>
> Aur ek honest observation maine add ki: **isi table me baaki rows me bhi widget hi likhe hain** — 'Multi-select', 'Dropdown', 'Radio', 'Textarea', 'Checkbox table'. Sab controls hain, data types nahi. To ye ek isolated typo nahi, poora column confuse hua hai."

**Real example:**
```
GALAT:
| Market budgets | Table    | Required |
| Target markets | Multi-select | Required |
| Product ASINs  | Textarea | Conditional |
| Selected deals | Checkbox table | Required |
→ ye sab UI CONTROLS hain

SAHI:
| Market budgets | Decimal, one per market  | Required |
| Target markets | List of str (ISO codes)  | Required |
| Product ASINs  | List of str              | Conditional |
| Selected deals | List of deal objects     | Required |
→ ye DATA TYPES hain

Kyun matter karta hai: agent ke liye UI widget ka koi matlab nahi hai.
Agent ko pata hona chahiye ki field me kya jaayega — string, list,
decimal — na ki wo screen par kaisa dikhega.
```

**Kya change kiya (v3.0):**
- `Market budgets` Type: `Table` → **`Decimal, one per market`**
- `Base bids` Type: `Table` → **`Decimal, one per market`**
- Note ki schema neeche list hi rahegi
- Open question raise kiya ki baaki rows me bhi widget hain

**Mai unse puch sakta hoon:**
1. Is table me aur bhi rows hain jinke Type me widget likha hai — 'Multi-select', 'Dropdown', 'Radio', 'Textarea', 'Checkbox table'. Poore column me data types rakhein aur controls alag record karein?
2. Budget brief se aata hai. Agar brief me **range** ho — "aath se dus hazaar" — agent upper le, lower le, ya puche?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Schema badal gaya?"* | Nahi. `market_budgets: list[MarketBudgetBidSchema]` waisa hi hai. Sirf **documentation** theek hui — Type column ab data type batata hai. |
| *"List kyun rakhi?"* | Multi-market ke liye. Ek market wala plan ek-element list bhejega. Baad me multi-market add karna migration nahi banega. |
| *"Ye chhoti baat nahi hai?"* | Nahi. Agent ke liye ye maayne rakhta hai — agent widget nahi dekhta, wo data structure dekhta hai. Aur galti poore column me hai, ek row me nahi. |

---

## COMMENT 12 — CTV me base bid apply nahi hota

**Kahan:** Step 1, `Base bids` ke saamne `"Required"` par (aur asar Step 6 ke repair loop par)

**David ne kaha:** CTV me base bids apply nahi hote.

**Pehle kya tha:**
```
| Base bids | Table | Required |
```
Aur repair loop me: *"Also adjust base CPM bid upward"* — yaani reach kam ho to bid badhao.

**David kya keh rahe hain:** *Daam deal ka CPM hai. Trader ke set karne ke liye koi bid nahi hai.*

**Maqsad:** Ek field hatana jo CTV me kaam nahi karti. Fixed-CPM deal me bid ka koi matlab nahi — daam pehle se tay hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Field ke hisab se seedha hai — daam deal ka CPM hai, to bid karne ke liye kuch nahi hai. Field sawaal banna band ho jaati hai, aur effective rate matched deal ke rate card se padha jaata hai, plus audience data fee.
>
> **Par field se zyada zaroori ye hai ki repair loop ka ek lever chala jaata hai.**
>
> v1.1.0 ke loop me reach kam hone par do moves the: audience widen karo, aur bid badhao. Fixed-CPM deals me doosra move **gaya**. Bacha: targeting relax karo aur inventory widen karo. Aur Comment 4 ke hisab se, agar trader ne audience hi nahi chuni to audience lever bhi nahi hai.
>
> Aur inventory widen karne ki apni limit hai jo bolni chahiye: Netflix ya Disney+ jodne se impressions badhengi, par un tiers se **reach forecast nahi aata** — to agent verify nahi kar sakta ki added inventory ne reach ka problem theek kiya. Usko ye **bolna** chahiye, ye imply nahi karna chahiye ki problem solve ho gaya."

**🔴 Ek zaroori objection maine raise kiya:**

> "Par mera ek sawaal hai jo main schema me open question ke roop me likha hai.
>
> **Private Auction deals me FLOOR CPM hota hai, FIXED nahi.** Document ke apne §2.3 me likha hai: *'Floor CPM, competitive'*. Floor ka matlab minimum hai — uske **upar bid karna padta hai**, aur competition hota hai.
>
> To agar Private Auction deals hain, to bid ka **matlab hai**. Us case me agent ke paas bid lever bacha rehta hai, aur jawab 'CTV me base bid apply nahi hota' se **zyada narrow** hoga.
>
> Aur maine platform par verify kiya — **83 deals me se lagbhag saari `PRIVATE_AUCTION` + `FLOOR_RATE` hain.** Netflix ki saari, Freewheel ki saari, aur Prime Video ki bhi kuch.
>
> Aur platform **base bid required karta hai** — maine pure CTV plan (sirf Streaming TV + Prime Video) me base bid khaali chhoda aur `Next` dabaya. Error aaya: *'All fields should be filled.'*
>
> To mera nateeja: David ka comment **Preferred aur Programmatic Guaranteed deals ke liye sahi hai** (dono FIXED_CPM), par **Private Auction ke liye galat hai** — aur VOW par lagbhag saari deals wahi hain."

**Real example:**
```
PREFERRED DEAL (FIXED_CPM):
   Prime Video, £15.26 fixed
   → bid ka koi kaam nahi. £15.26 hi lagega.
   → David sahi hain

PRIVATE AUCTION (FLOOR_RATE):
   Netflix, floor £22.96
   → aapko £22.96 se UPAR bid karna padta hai
   → competition hai
   → agar aap £23 bid karo aur doosra £30 bid kare, aap HAAR gaye
   → to bid MATTER karta hai!
   
   Repair loop:
      Reach kam aayi. Kyun? Kyunki aap auctions haar rahe ho.
      Fix: bid £23 se £28 karo → zyada jeet → zyada impressions → zyada reach
      
   → Ye lever MAUJOOD hai. Document keh raha hai nahi hai.
```

**Kya change kiya (v3.0):**
- `Base bids` Requirement: Required → **—** (asked nahi), Source **DERIVED**
- Note: payload me phir bhi rahega kyunki `MarketBudgetBidSchema.base_bid` required field hai
- Step 6 ka repair loop table corrected: *"No longer applies. CTV deal CPMs are fixed, so there is no bid to raise"*
- 🔴 **Open question raise kiya** Private Auction ke floor CPM ke baare me

**Mai unse puch sakta hoon:**
1. 🔴 **Private auction deals me floor CPM hota hai, fixed nahi** — §2.3 khud kehta hai "Floor CPM, competitive". Wahan bid matter karta hai? Agar haan, to agent ko us deal type par bid lever rakhna chahiye, aur jawab "CTV me base bids apply nahi hote" se narrow hoga
2. `MarketBudgetBidSchema.base_bid` create payload me required field hai. Trader se puchte nahi to kya bhejein — deal ka CPM, null, ya CTV endpoint field hi drop kar deta hai?
3. 🔴 **Platform base bid required karta hai** — maine pure CTV plan par test kiya, `Next` block ho gaya. To agent ko kuch bhejna hi padega. Kya?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Bid nahi to payload me kya jaayega?"* | Ye **open question** hai. Maine teen options rakhe: deal ka CPM, null, ya endpoint drop kar de. Platform par maine dekha ki trader ne `base_supply_bid: "25"` bheja aur wo store hua per format. To kuch bhejna padega. |
| *"Repair loop me kitne levers bache?"* | Do — targeting relax karo, inventory widen karo. Plus budget/flight. Aur agar audience nahi chuni to audience lever bhi nahi (Comment 4). Agent ko bolna chahiye jab kuch na bache. |
| *"Tum David se disagree kar rahe ho?"* | Partially, aur maine wo open question ke roop me likha hai — assertion ke roop me nahi. Preferred aur PG me wo bilkul sahi hain. Private Auction me floor CPM hai aur bid matter karta hai. Aur VOW par lagbhag saari deals Private Auction hain. |
| *"Inventory widen karna kaam karega?"* | Impressions badhengi, par 3P tiers se **reach forecast nahi aata** — to agent verify nahi kar sakta. Usko ye bolna chahiye. |

---

## COMMENT 13 — 🔴 Advertiser-level defaults (naya concept)

**Kahan:** Step 1, `Frequency cap` ke saamne `"Optional"` par

**David ne kaha:** *"we have a default per advertiser"*

**Pehle kya tha:**
```
| Frequency cap | Number | Optional |
```
Jaise trader se puchna padega — ya khaali reh jaayegi.

**David kya keh rahe hain:** *Ye advertiser par set hota hai, har campaign me puchne ki zaroorat nahi.*

**Maqsad:** Ek **naya concept** introduce kar rahe hain jo document me **tha hi nahi**. David ne sirf ek field theek nahi ki — unhone ek poori nayi category batayi.

**🔴 Maine kya samjha (ye bolna hai) — ye 28 me se sabse important comment hai:**

> "Ye ek concept introduce karta hai jo document me nahi tha: **kuch settings advertiser ki hoti hain, campaign ki nahi.**
>
> Wo brief se brief nahi badalti. To unhe har baar puchna mehnat ka waste hai.
>
> Frequency cap pehla hai, par akela nahi. Baad ke comments me pata chala ki **product categories** (Comment 15), **selling location** (Comment 16), aur **device type** (Comment 22) — teeno bhi advertiser par baithe hain. To ye ek pattern hai, ek exception nahi.
>
> **Kahan se aayenge aur kab:** advertiser settings **session ke shuru me** padhi jaayengi, brief parse karne se **pehle** — `GET /api/admin/advertiser/{id}/`, model `AdvertiserAdminRetrieve`. Ye order zaroori hai: pehle defaults form bharenge, phir brief me jo likha hai wo override karega. Ulta karne se defaults brief ko overwrite kar denge.
>
> **Aur ek cheez jo plain default express nahi kar sakta.** Comment 22 me pata chalta hai ki kuch advertisers **sirf Connected TV** chahte hain. Wo default nahi lagta — wo **policy** lagti hai. Yaani trader usko override nahi kar sakta, aur **repair loop usko chupke se relax nahi kar sakta.**
>
> Isliye har setting ko batana padega ki wo **binding** hai ya nahi:
>
> ```python
> class AdvertiserSetting(BaseModel):
>     value: Any
>     is_locked: bool = False      # brand policy — trader override nahi kar sakta
>     reason: Optional[str] = None # locked hone par trader ko dikhega
> ```
>
> **`is_locked` ke bina agent starting point aur rule me farak nahi kar sakta**, aur wo aisi cheez relax karne ki offer karega jise chhune ki ijazat nahi hai."

**Real example:**
```
Session shuru:
   GET /api/admin/advertiser/brightpath-uuid/
   
   → {
       frequency_cap:        {value: 3, is_locked: false},
       product_categories:   {value: ["Education"], is_locked: false},
       device_types:         {value: ["Connected TV"], is_locked: TRUE,
                              reason: "Brand policy — TV screens only"},
       selling_location:     {value: "NOT_SOLD_ON_AMAZON", is_locked: false}
     }

Phir brief parse hota hai:
   "UK me £10,000, September, frequency 4 rakho"
   → frequency_cap override ho gaya 3 se 4 (locked nahi hai) ✅

Ab reach kam aati hai. Repair loop chalti hai:
   Agent: "Reach kam hai. Mai device targeting widen kar sakta hoon…"
          → CHECK: device_types.is_locked = TRUE
          → "…nahi, ye advertiser ki brand policy hai (TV screens only).
             Mai audience widen karta hoon uske bajaye.
             Aur bata deta hoon ki device lever available nahi tha."

is_locked KE BINA:
   Agent: "Mobile bhi add kar deta hoon, reach badh jaayegi!"
   → Brand policy tod di. Client naraz.
```

**Kya change kiya (v3.0):**
- `Frequency cap` Source: **ADVERTISER**
- `Budget cap` naya row add hua, Source ADVERTISER
- `AdvertiserSetting` model add hua `is_locked` ke saath
- Note ki settings **session ke shuru me** load hongi, brief se pehle
- Endpoint correct kiya: `GET /api/admin/advertiser/{id}/` (v1.1.0 me `/api/advertisers/{id}/defaults/` tha — **exist hi nahi karta**)
- 4 open questions

**Mai unse puch sakta hoon:**
1. 🔴 **Advertiser par kitni settings hoti hain — poori list kya hai?** Abhi pata karna better hai, warna har comment me ek nayi field aayegi. Ab tak: frequency cap, product categories, selling location, device type, aur shayad budget cap
2. In me se kaunsi **locked** brand policy hain aur kaunsi overridable default? Isse tay hoga ki repair loop kya badal sakta hai
3. Advertiser record me frequency cap **already hai** ya field add karna padega? Endpoint hai, par usme ye value hai ya nahi API listing se nahi dikhta
4. Advertiser ki koi value set nahi hai to agent kya kare — khaali chhode ya platform-wide default use kare?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"`is_locked` kyun chahiye, value hi kaafi nahi?"* | Kyunki agent ko farak pata hona chahiye ki ye **starting point** hai ya **rule**. Repair loop settings relax karta hai. Locked setting relax karna brand policy todna hai. Bina flag ke agent ko pata nahi chalega. |
| *"Settings kab load hongi?"* | 🔴 Session ke **shuru me, brief parse karne se pehle**. Order zaroori hai — defaults form bharte hain, brief override karta hai. Ulta karne se defaults brief ko overwrite kar denge. |
| *"Endpoint kaunsa?"* | `GET /api/admin/advertiser/{id}/`, model `AdvertiserAdminRetrieve`. v1.1.0 me `/api/advertisers/{id}/defaults/` likha tha — wo **exist hi nahi karta**. Ye Comment 24 ke Swagger check me pakda gaya. |
| *"Ye kaun-kaun se comments se juda hai?"* | Comment 15 (product categories), 16 (selling location), 22 (device type) — teeno advertiser par hain. Aur Comment 22 hi `is_locked` ki wajah hai. Comment 13 concept introduce karta hai, baaki teen instances hain. |
| *"Trader locked setting badal sakta hai?"* | Nahi. Aur agent usko `reason` dikhayega — jaise *"Brand policy: TV screens only"*. Silently ignore nahi karega. |

---

## COMMENT 14 — Format hamesha `streaming_tv` hai; Prime Video ek channel hai

**Kahan:** Step 1, `Formats` ke saamne `"Required"` par

**David ne kaha:** *"is always streaming_tv"*

**Pehle kya tha:**
```
| Formats | List of enum | Required |
```
Aur `FormatEnum` me `PRIME_VIDEO` ek value thi. v1.1.0 me deals ki table ka heading bhi *"Prime Video Deals"* tha.

**David kya keh rahe hain:** *CTV me format ek hi hai. Choice hi nahi hai.*

**Maqsad:** Do galtiyan theek karna. Ek — ek hi possible value hai to choice dikhana bekaar hai. Do — `prime_video` **format nahi hai**, wo **channel** hai. Document ne do levels mix kar diye the.

**🔴 Maine kya samjha (ye bolna hai):**

> "Do baatein.
>
> Pehli — ek hi possible value hai to present karne ke liye koi choice nahi hai. Field ek **constant** ban jaati hai aur trader se puchi jaane wali list se nikal jaati hai.
>
> Doosri, aur zyada zaroori — **row ne do levels mix kar diye the.** `prime_video` format ki tarah listed tha, par Prime Video ek **channel** hai — wo `streaming_tv` ke **andar** baithta hai, Netflix aur Disney+ ke saath.
>
> ```
> Format   = inventory ki KISM        → streaming_tv
> Channel  = KAUN ad dikha raha hai   → Prime Video, Netflix, Disney+
> ```
>
> **Aur document khud apne aap ko contradict kar raha tha.** Step 2 deals fetch karta hai `GET /api/deals/?markets={market}&formats=streaming_tv` — sirf `streaming_tv`. Aur `SelectedDealSchema.provider` ka description hai *'e.g. Prime Video, Netflix, Disney+'* — to Prime Video **ek step baad already sahi jagah** capture ho raha tha.
>
> **Step 2 sahi tha. Step 1 v1.1.0 ki galti carry kar raha tha** — wahan deals ki table ka heading hi 'Prime Video Deals' tha.
>
> `FormatEnum.PRIME_VIDEO` ko maine **delete nahi kiya, annotate kiya** — enum value hatana breaking change hai un sab ke liye jo already bhej rahe hain."

**🔴 Ek zaroori exception maine platform par pakda:**

> "Par mujhe ek jagah mili jahan `prime_video` **matter karta hai** — aur ye David ke comment ke against ek exception hai.
>
> Reach forecast API `formats` array leti hai. Maine test kiya:
>
> ```
> formats: ["streaming_tv", "prime_video"]
> → do supply lines aayi:
>      DSP_STREAMING_TV   est_reach 132,713
>      DSP_PRIME_VIDEO    est_reach  71,120
>      
> Agar sirf ["streaming_tv"] bhejein:
> → DSP_PRIME_VIDEO line AATI HI NAHI
> → 71,120 reach aur 212,860 impressions CHALI JAATI HAIN
> ```
>
> To poora picture ye hai:
>
> | Endpoint | `prime_video` matter karta hai? |
> |---|---|
> | `GET /api/inventory-sources/` | ❌ Nahi — maine test kiya, wahi do Amazon sources aaye |
> | `POST /api/strategies/reach-forecast/` | ✅ **HAAN** — alag supply line deta hai |
>
> To 'format hamesha streaming_tv hai' **model ke liye sahi** hai (Prime Video channel hi hai), par **forecast payload ke liye galat** hai. Agar agent constant `["streaming_tv"]` bheje to wo Prime Video ka reach kho dega."

**Real example:**
```
MODEL me (David sahi hain):
   format  = "streaming_tv"        ← inventory ki kism
   channel = "Prime Video"         ← kaun dikha raha hai
   
   Prime Video Netflix jaisa hi ek channel hai. Dono streaming_tv hain.

FORECAST PAYLOAD me (exception):
   POST /api/strategies/reach-forecast/
   { "formats": ["streaming_tv", "prime_video"], ... }
   
   → API "formats" ko supply-line key ki tarah treat karti hai, na ki
     content type ki tarah. To dono bhejne padte hain.
     
Ye API ka design compromise hai — model theek hai, API confuse hai.
```

**Kya change kiya (v3.0):**
- `Formats` Requirement: `—` (asked nahi), Source **FIXED**
- Value: **always `["streaming_tv"]`**
- `prime_video` format se hataya, channel bataya
- `FormatEnum.PRIME_VIDEO` **annotated, deleted nahi** (breaking change se bachne ke liye)
- Document ka self-contradiction likha gaya (Step 2 sahi tha)
- 2 open questions

**Mai unse puch sakta hoon:**
1. CTV strategy ke liye API asal me kaunse format values accept karti hai — sirf `streaming_tv`? `GET /api/strategies/choices/` aur `FormatsAndKpis` model wahi jagah lagti hai jahan ye define hai — assume karne ke bajaye padhna behtar hai
2. v1.1.0 ka create payload example `"formats": ["prime_video"]` bhejta hai. Usko `["streaming_tv"]` karein, ya endpoint purani value bhi accept karta hai?
3. 🔴 **Forecast API me `prime_video` alag supply line deti hai** — maine verify kiya. Uske liye kya bhejein?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Format aur channel me farak?"* | Format = inventory ki kism (streaming video). Channel = kaun dikha raha hai (Prime Video, Netflix). Prime Video `streaming_tv` ke andar baithta hai, uske barabar nahi. |
| *"Enum value delete kyun nahi ki?"* | Breaking change hai. Jo already `prime_video` bhej raha hai wo toot jaayega. Annotate kar diya — deprecated, use na karo. |
| *"Platform par kitne formats hain?"* | Creation me **chaar**: display, online_video, streaming_tv, prime_video. Filter me **chhah** (Netflix, Disney+ extra). To platform Prime Video ko format hi treat karta hai — model se disagreement hai. |
| *"To David sahi hain ya galat?"* | Model ke liye **sahi** — Prime Video channel hai. Par forecast API ke liye ek exception hai jo maine pakda: `prime_video` bhejna padta hai warna 71,120 reach kho jaata hai. Ye API ka design issue hai. |

---

## COMMENT 15 — Product categories advertiser se ya brief se aayengi

**Kahan:** Step 1, `Product categories` ke saamne `"Required for video"` par

**David ne kaha:** *"we have a default on the advertiser, or maybe could imply from the brief"*

**Pehle kya tha:**
```
| Product categories | List of int | Required for video |
```

**David kya keh rahe hain:** *Advertiser par default hai. Ya brief se imply ho sakta hai. Puchne ki zaroorat nahi.*

**Maqsad:** Comment 13 ka doosra instance. Aur ek chhoti si cheez bhi — *"for video"* qualifier bekaar hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Product category ek campaign se doosre campaign me badalti nahi — BrightPath har brief par education advertiser hai. To har baar puchna advertiser ki **property** ko campaign ka **faisla** samajhna hai.
>
> Resolution order: pehle advertiser ki setting, aur wo na ho to brief se imply karo — 'an education website' itna kaafi hai place karne ke liye.
>
> **`for video` qualifier bhi jaata hai.** Wo v1.1.0 se aaya jahan Display bhi scope me tha. CTV **hamesha** video hai, to condition hamesha true hai — aur aisa lagta hai jaise koi case hai jahan field apply nahi karti. Aisa koi case nahi hai.
>
> **Ek teesra source hai par wo bahut late aata hai.** `POST /api/contextual-targeting/{market}/asin-validation/` har valid ASIN ke saath product category wapas deta hai. Par ASINs tracking step par collect hote hain — is step ke bahut baad. To wo category yahan bhar nahi sakti.
>
> **Par cross-check ke liye kaam ki hai:** agar advertiser Education set hai aur ASINs Electronics wapas karte hain, kuch galat hai aur agent ko bolna chahiye — mismatch ko chupke se jaane nahi dena chahiye."

**Real example:**
```
Case A — Advertiser par set hai:
   GET /api/admin/advertiser/brightpath/
   → product_categories: ["304861615492321169"]  (Education)
   → seedha use kar liya. Koi sawaal nahi.

Case B — Advertiser par nahi hai, brief se imply:
   Brief: "BrightPath online education courses ke liye campaign"
   → agent "education" pakadta hai
   → GET /api/contextual-targeting/GB/product-categories/ se match karta hai
   → Education category mil gayi

Case C — Cross-check (baad me, tracking step par):
   Advertiser setting: Education
   ASIN validation:    B08N5WRWNW → category "Consumer Electronics"
   
   Agent: "Ek mismatch hai — advertiser Education set hai par
           ASINs Consumer Electronics ke hain. Confirm kar lein?"
   → chupke se aage nahi badhta
```

**🔴 Platform par jo dekha:**

> "Maine platform par ye field dekhi. Do-level hierarchy hai:
>
> ```
> Education          ← parent, sirf expand hota hai, CHUN NAHI SAKTE
>     ☐ Language Education
>     ☐ General
>     ☐ Schools, College & Universities
>     ☐ Test Preparation
>     … (9 subcategories)
> ```
>
> Sirf **leaf** chun sakte ho, parent nahi. Multi-select hai.
>
> Aur helper text kehta hai: *'VOW will use this to improve strategy **targetting**'* — to ye **targeting input** hai, reporting label nahi. Ye zaroori hai kyunki isse reach par asar padta hai.
>
> Payload me values long numeric strings hain: `["304861615492321169", "345704700972773738"]` — Amazon ke IDs."

**Kya change kiya (v3.0):**
- Requirement: `Required for video` → **Required** (qualifier hata)
- Source: **ADVERTISER → INFERRED** (resolution order)
- ASIN validation ko cross-check ke roop me likha
- 3 open questions

**Mai unse puch sakta hoon:**
1. 🔴 **Advertiser par jo hai wo product category hai ya industry?** Advertiser endpoints me `GET /api/admin/advertiser/get_industry_and_sub_industry_choices/` hai, jabki product categories **poori alag taxonomy** se aati hain (`GET /api/contextual-targeting/{market}/product-categories/`, models `ProductCategory` aur `ProductSubcategory`). Agar advertiser industry rakhta hai to **mapping chahiye** — aur wo document me kahin nahi hai
2. Advertiser ek category rakhta hai ya kai? Field list hai, to agent ko advertiser record ki shape se match karna chahiye
3. Categories per market fetch hoti hain. Multi-market me — wahi category har market me available maan lein, ya har market check karein?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"'for video' kyun hataya?"* | CTV hamesha video hai. Condition hamesha true hai. Rakhne se lagta hai koi case hai jahan apply nahi karti — nahi hai. |
| *"ASIN se category mil jaati hai, wo use nahi kar sakte?"* | Wo **bahut late** aati hai — ASINs tracking step par collect hote hain, Step 1 ke baad. Par **cross-check** ke liye kaam ki hai. |
| *"Industry aur product category ek nahi hain?"* | 🔴 **Nahi, aur ye mera sabse zaroori sawaal hai.** Do alag taxonomies hain, do alag endpoints. Agar advertiser industry rakhta hai to mapping banani padegi — jo abhi kahin nahi hai. |
| *"Platform par ye required hai?"* | 🔍 Video format chunne par field dikhti hai. Maine required hone ka test nahi kiya. Par helper text saaf kehta hai ki ye targeting improve karta hai — to functionally zaroori hai. |

---

## COMMENT 16 — Selling location is step se hat jaayega

**Kahan:** Step 1, `Selling location` ke saamne `"Required"` par

**David ne kaha:** *"can leave out"*

**Pehle kya tha:**
```
| Selling location | Radio | Required |   ← On Amazon / Off Amazon
```
Aur **ye sawaal Step 11 (Tracking) me bhi tha** — do jagah.

**David kya keh rahe hain:** *Ise Step 1 se nikaal do.*

**Maqsad:** Duplication hatana. Aur field ko sahi jagah rakhna.

**🔴 Maine kya samjha (ye bolna hai):**

> "Row Step 1 ki table se **hata di** gayi.
>
> Wajah: advertiser Amazon par bechta hai ya nahi, ye tay karta hai ki **conversions kaise measure honge** — plan kaise banega, wo nahi. To ye **tracking step** ke saath jaata hai, jahan ASIN aur ad-tag ke sawaal already baithe hain.
>
> Aur tracking step **already** puchta hai *'Sells on Amazon?'* — to ye **wahi sawaal** hai, do jagah pucha ja raha tha.
>
> Aur ye campaign ki nahi, **advertiser ki property** hai — to advertiser ki settings se pre-filled aayegi, aur trader sirf us rare case me badalega jab ek campaign alag ho.
>
> **Aur ye chupke se ek bada open question aadha solve kar deta hai.** Document me do baar flag kiya gaya tha ki `product_location` Step 8 ke `POST /strategies/` payload me **required** hai, par Step 11 me collect ho raha hai — uske **baad**. Wo timing ka problem lagta tha.
>
> Par agar value **advertiser ki settings se** aati hai — jo session ke shuru me load hoti hain — to agent ke paas wo **already hai** jab wo strategy create karta hai. Kuch patch karne ki zaroorat nahi.
>
> Sirf ASINs baad me aate hain — aur wo aadha Comment 17 aur Comment 28 me handle hua."

**Real example:**
```
PURANA (problem):
   Step 1:  "Amazon par bechte hain?" → puch liya
   Step 8:  POST /strategies/ { product_location: "..." } → required hai
   Step 11: "Amazon par bechte hain?" → DOBARA puch liya!
   
   → do baar pucha, aur confusion ki Step 8 me value kahan se aayi

NAYA (solved):
   Session start:  GET /api/admin/advertiser/brightpath/
                   → selling_location: "NOT_SOLD_ON_AMAZON"
                   → agent ke paas already hai
                   
   Step 1:  nahi pucha
   Step 8:  POST /strategies/ { product_location: "NOT_SOLD_ON_AMAZON" }
            → advertiser setting se bhar diya ✅
   Step 11: "Amazon par bechte hain? (advertiser setting: nahi)"
            → confirm kar liya, aur ASINs/ad-tag ka faisla kiya
            
   → ek baar, sahi jagah, aur Step 8 ka payload complete
```

**Kya change kiya (v3.0):**
- **Row poori hata di** Step 1 ki table se
- Note likha ki wo Step 11 me already hai
- Open question ka **aadha RESOLVED** mark kiya
- 2 open questions

**Mai unse puch sakta hoon:**
1. Ek advertiser ke campaigns me **alag-alag selling location** ho sakti hai — kuch Amazon par bhejein, kuch apni site par? Agar haan to ye overridable default rahega, fixed advertiser property nahi
2. Advertiser par selling location set nahi hai aur brief bhi nahi batata — `NOT_SOLD_ON_AMAZON` assume karna safe hai aur ad-tag tracking par bharosa karein, ya agent puche?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Field delete ho gayi?"* | Nahi. Step 11 (Tracking) me hai, jahan hamesha honi chahiye thi. Sirf Step 1 se duplicate hataya. |
| *"Step 8 ke payload me kahan se aayegi?"* | Advertiser ki settings se — jo session ke **shuru me** load hoti hain. To creation ke waqt agent ke paas already hai. |
| *"Ye timing question solve kar deta hai?"* | **Aadha.** `product_location` ka aadha solve ho gaya (advertiser se aata hai). ASINs ka aadha Comment 17 aur 28 me solve hua (empty bhejo, phir PATCH karo). |
| *"On/Off Amazon me farak kya?"* | On Amazon = advertiser Amazon par bechta hai, ASIN se track hoga. Off Amazon = apni site par bechta hai, ad tag se track hoga. Ye **measurement** ka faisla hai, plan ka nahi. |

---

## COMMENT 17 — Product ASINs bhi is step se hat jaayenge

**Kahan:** Step 1, `Product ASINs` ke saamne `"Conditional"` par

**David ne kaha:** *"comes later"*

**Pehle kya tha:**
```
| Product ASINs | Textarea | Conditional |
```
v2.0 ne **already** kaha tha ki ASINs Step 11 par move ho gaye hain — par row Step 1 me **phir bhi listed thi**, ek note ke saath.

**David kya keh rahe hain:** *Ye baad me aate hain.*

**Maqsad:** Ye comment un chaar me se ek hai jo **jo revision ne already kaha tha usko confirm karta hai**. Par ek chhota correction hai: agar baad me aate hain, to yahan listed nahi hone chahiye.

**🔴 Maine kya samjha (ye bolna hai):**

> "Ye wo confirm karta hai jo revision ne already kaha tha — ASINs tracking step par move ho gaye. Correction chhota hai: **agar wo baad me aate hain, to yahan note ke saath listed nahi hone chahiye.** Row hata di.
>
> Sequence ye hai: strategy `product_asins: []` ke saath create karo, phir tracking step par ASINs collect aur validate karo, aur strategy update kar do.
>
> Validation waisi hi hai — `POST /api/contextual-targeting/{market}/asin-validation/`, aur **market se keyed** hai, ek hardcoded market par nahi.
>
> Comment 16 ke saath milkar, ye poora **timing question band kar deta hai** jo document me **do baar** aaya tha — Step 1 par aur Step 11 par."

**Real example:**
```
Step 8 — strategy create:
   POST /api/simple-strategies/
   {
     "name": "Education_GB_Awareness_Sep2026",
     "product_location": "SOLD_ON_AMAZON",   ← advertiser se (Comment 16)
     "product_asins": [],                     ← KHAALI
     ...
   }
   → 201 Created, id: VMA2026368

Step 11 — tracking setup:
   Trader ASINs deta hai: "B08N5WRWNW, B07XYZ1234"
   
   POST /api/contextual-targeting/GB/asin-validation/
   { "asins": ["B08N5WRWNW", "B07XYZ1234"] }
   → B08N5WRWNW  valid,   category: Education
   → B07XYZ1234  INVALID
   
   Agent: "B07XYZ1234 valid nahi hai. Baaki ek attach kar diya."
   
   PATCH /api/strategies/VMA2026368/
   { "product_asins": ["B08N5WRWNW"] }
   → ✅ attach ho gaya
```

**🔴 Platform par jo dekha:**

> "Maine platform par ASIN field test ki:
>
> ```
> On Amazon chuna   →  ASIN required. Invalid ASIN se Next BLOCK ho jaata hai
> Off Amazon chuna  →  ASIN field dikhti hai, par ZERO ASINs se bhi Next chalta hai
> ```
>
> Aur validation **batch me** hoti hai — comma-separated paste karo, `Add` dabao, tab validate hota hai. Type karte waqt nahi.
>
> Aur Off Amazon par ASIN field dikhne ki wajah **halo sales** hai — jo advertiser Amazon par nahi bechta wo bhi apni category ke ASINs jod kar indirect Amazon sales dekh sakta hai."

**Kya change kiya (v3.0):**
- **Row poori hata di** Step 1 se
- Sequence likha gaya (empty create → PATCH later)
- Timing question **RESOLVED** mark kiya
- 1 open question

**Mai unse puch sakta hoon:**
1. ASIN list **ek call me** validate karein tracking step par, ya jaise trader paste karta jaaye waise? Late validate karne ka matlab hai trader 20 ASINs daal de aur phir pata chale ki 3 galat hain

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Create ke waqt ASINs khaali bhejenge?"* | Haan, `product_asins: []`. Phir tracking step par `PATCH /api/strategies/{id}/` se attach karenge. |
| *"PATCH allowed hai?"* | ✅ Haan — Comment 28 me confirm hua, aur maine staging Swagger me verify kiya. Model `StrategyUpdate`. |
| *"Ye Comment 28 se kaise juda hai?"* | Comment 28 wo **mechanism** deta hai jo isko possible banata hai. Agar strategy creation ke baad update na ho sakti, to ASINs pehle collect karne padte. Do comments ek hi change ke do side hain. |
| *"Off Amazon par ASIN kyun?"* | Halo sales. Non-endemic advertiser bhi apni category ke ASINs jod kar Amazon par indirect asar dekh sakta hai. Par **required nahi** — maine test kiya, zero ASINs se bhi aage jaa sakte hain. |

---

## COMMENT 18 — 🔴 Deals match hoti hain, select nahi

**Kahan:** Step 2, `Selected deals` ke saamne `"Checkbox table"` par

**David ne kaha:** Checkbox table nahi hona chahiye.

**Pehle kya tha:**
```
| Selected deals | Checkbox table | Required |
```
Yaani trader ko deals ki list dikhegi aur wo tick karega — bilkul UI wizard jaise.

**David kya keh rahe hain:** *Trader deals table me se pick na kare. Requirements bataye, aur agent deals dhoondhe.*

**Maqsad:** Ye Comment 6 ke baad **sabse structural comment** hai. Ye **poore step ka order ulta kar deta hai.** Aur ye agentic soch ka core hai: agent ka kaam UI ko chat me copy karna nahi, **kaam khud kar dena** hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Ye step ka order ulta kar deta hai. Table gayi; trader requirements batata hai aur agent wo deals dhundta hai jo fit karti hain.
>
> **Trader kya decide karta hai, aur agent kya nikaalta hai:**
>
> Prime Video ko Netflix ke upar chunna ek **asli faisla** hai. `EXT7P75718S8MNR` aur `EXT7P75719Q2LKM` ke beech chunna faisla **nahi** hai — wo plumbing hai.
>
> To trader deta hai: channel, optionally genre ya run-of-service, aur jo targeting chahiye. Agent match karta hai market, duration aur channel par, aur jo fit hota hai wo laata hai. Jis trader ke paas already koi deal hai wo `specific_deal_id` se naam le sakta hai — shortcut rehta hai par sabko use karna nahi padta.
>
> **Kya dikhaya jaayega:** channel, effective CPM, aur estimated impressions. **Deal IDs nahi, raw deal names nahi** — `Prime Video | Preferred Deal | UK - 30 - ROS` jaisa naam kuch nahi batata jo trader kahin aur saaf na dekh sake, aur galti se ek galat padhna chupke se plan badal deta hai.
>
> **🔴 Par do cheezein phir bhi surface karni PADENGI, chahe deal chhupi ho:**
>
> **Ek — Tier capability.** Third-party tiers reach forecast **nahi** dete. Agar sirf CPM dikhaya, to trader ko pata hi nahi chalega ki plan ke ek hisse ka reach figure missing hai. Aur Step 6 ka honesty rule kehta hai ye batana hai.
>
> **Do — Commercial commitment.** Programmatic Guaranteed deal **poora budget owe karti hai aur pause nahi ho sakti** (§2.3). Deal chhupane se ye **chhupna nahi chahiye**. Agent ko saaf bolna chahiye trader ke CPM accept karne se **pehle** — *'ye guaranteed deal hai, to poora £6,000 committed hoga aur pause nahi kar sakenge'* — na ki commitment chupke se nikal jaaye kyunki deal type internal thi.
>
> **Aur ek dilchasp baat: ye pattern document me already tha, ek jagah.** Neeche curation capture me — jahan deals select hi nahi ho sakti (Disney+) aur agent genres, durations, targeting aur budget record karta hai. **Wahi model hai jo describe kiya jaa raha hai.** Bas un tiers par apply nahi kiya gaya tha jahan deals exist karti hain.
>
> Graph node ka naam bhi badal diya — `select_inventory` se `match_inventory_deals` — taaki code wahi kahe jo wo karta hai."

**Real example:**
```
PURANA (checkbox table):
Agent: "Ye 83 deals hain, jo chahiye tick karo:
        ☐ 3PS_Freewheel_UK_STV_Paramount_My 5 — £22.96 Floor
        ☐ 3PS_Netflix_Always On_Auto Intenders_Interest Based_NOT
          Amazon Audience Enabled_STV_UK_Q3 — £38.12 Floor
        ☐ Prime Video | Preferred Deal | Video | UK - 15, 20 – ROS — £15.26 Fixed
        … 80 more"
        
Trader: "…mujhe kya pata kaunsa lena hai?"
→ Agent ne apna kaam trader par daal diya

NAYA (matched):
Trader: "Prime Video par chalao, 30-second creative"

Agent andar hi andar:
   GET /api/deals/?markets=GB&formats=streaming_tv
   → filter: channel = Prime Video, ad_lengths me 30 ho
   → 4 deals match hui
   → sabse sasta chuna: £24.79 CPM

Agent: "Prime Video par £24.79 effective CPM mil raha hai
        (£22.96 deal + £1.83 audience fee).
        £10,000 par ~403,000 impressions.
        Ye ek preferred deal hai — daam pakka, pause kar sakte hain.
        Aage badhun?"

→ Deal ID kahin nahi dikha. Par tier aur commitment saaf bataya.

AGAR PG DEAL HOTI:
Agent: "Prime Video par £22 CPM mil raha hai, ~454,000 impressions.
        🔴 Ek baat zaroori hai: ye GUARANTEED deal hai —
        poora £10,000 committed ho jaayega aur campaign pause
        nahi kar sakenge. Aage badhun?"
```

**Kya change kiya (v3.0):**
- `Selected deals` Type: `Checkbox table` → **`List of deal objects`**, Source **MATCHED**
- Teen naye rows: `Channel` (INFERRED), `ROS or genre` (INFERRED), `Specific deal ID` (ASKED)
- `Inventory tier (per deal)` row (DERIVED)
- Node rename: `select_inventory` → `match_inventory_deals`
- Rule likha: tier capability aur commercial commitment **must surface**
- 4 open questions

**Mai unse puch sakta hoon:**
1. 🔴 **Deal ki built-in targeting structured fields me hai ya sirf naam me?** `GET /api/deals/filter-properties/` (model `AmzDealFilterProperties`) wahi jagah lagti hai, aur agar usme genre, ROS aur targeting hai to matching straightforward hai. Agar wo facts sirf **deal ke naam ke andar** hain, to agent ko string parse karni padegi ye decide karne ke liye ki kya khareedna hai — jo **Zero-Hallucination principle ke khilaf** hai. **Ye ek jawab hai jo tay karega ki ye step build ho sakta hai ya nahi**
2. Jab kai deals match ho — agent kaise chune? Sabse sasta CPM, best genre fit, ya sabse zyada forecastable reach?
3. Jab kuch bhi match na ho — kya kare? Duration widen kare, genre drop kare, ya report karke puche?
4. Programmatic Guaranteed deal **automatically match** honi chahiye, budget commitment ko dekhte hue? Ya sirf jab trader ne maanga ho?

**🔴 Aur maine platform par jo pata kiya (ye sabse zaroori update hai):**

> "Maine 83 deals ka poora data dekha, aur mera pehla sawaal ka jawab mil gaya — **aur wo bura jawab hai.**
>
> **1. `genre` field exist karti hai par bharosemand nahi hai.** `GET /api/deals/filter-properties/` ye deta hai:
> ```
> "genres": ["15, 20, 30", "2026", "2027", "Action", "Comedy", "Drama",
>            "RON", "ROS", "Suspense", "TEST", "Top Trending", "Winter Holiday"]
> ```
> Isme `2026`, `2027` **saal** hain. `TEST` ek test label hai. `15, 20, 30` **ad lengths ki list** hai jo genre ban gayi. Aur Netflix deals me genre naam ke **andar** hai par field `null` hai.
>
> Lagta hai `genre` deal ke naam ka **aakhri token** le leta hai. **To genre par matching build nahi ho sakti.**
>
> **2. `inventory_tier` field DEAL PAR EXIST HI NAHI KARTI.** Poore teen-tier fork ka koi data source nahi hai.
>
> **3. `channel` field bhi exist nahi karti.** Prime Video ya Netflix sirf `name` ke andar hai.
>
> **4. 'Amazon Audience Enabled' deal ke NAAM me hai:**
> ```
> 3PS_Netflix_..._NOT Amazon Audience Enabled_STV_UK_...
> 3PS_Netflix_Always On_Run of Network_Amazon Audience Enabled_STV_UK_...
> ```
> Aur deal object me koi audience-capability field nahi hai. To Comment 1 ka `targeting_source` **reliably set nahi ho sakta**.
>
> To mera nateeja: **David ka comment design ke liye sahi hai, par abhi buildable nahi hai** — kyunki matching ke liye jo structured data chahiye wo maujood nahi hai. Ye **data-quality request** ban jaati hai client ke liye."

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Trader ko deal ID kabhi nahi dikhega?"* | Nahi, default me nahi. Wo `specific_deal_id` se naam le sakta hai agar uske paas already koi deal hai — shortcut hai, majboori nahi. |
| *"To trader ko kya dikhega?"* | Channel, effective CPM, estimated impressions. Plus tier capability (reach forecast milega ya nahi) aur commercial commitment (PG deal hai to). |
| *"PG deal chhupa sakte hain?"* | 🔴 **Nahi.** Deal chhupana theek hai, par **paise ka commitment chhupana galat hai.** Agent ko bolna padega: "poora budget committed hoga, pause nahi ho sakta." Ye document me likha hua hai. |
| *"Ye buildable hai?"* | 🔴 **Abhi nahi.** Maine verify kiya — `genre` polluted hai, `inventory_tier` field exist nahi karti, `channel` field exist nahi karti, aur audience capability sirf deal ke naam me hai. Ye client se **data-quality request** chahti hai. |
| *"Curation capture se kya rishta?"* | Wo **wahi pattern hai** jo David describe kar rahe hain — jahan deal select nahi ho sakti wahan agent requirements record karta hai. Document me pattern already tha, bas un tiers par apply nahi kiya tha jahan deals exist karti hain. |

---

## COMMENT 19 — Amazon audiences 3P inventory par bhi chalti hain

**Kahan:** Step 4, "Constraints for CTV" list ki pehli bullet me `"Netflix/Disney"` par

**David ne kaha:** *"can use amazon audiences too"*

**Pehle kya tha:** Bullet keh raha tha ki Netflix/Disney par **sirf** unki apni targeting use ho sakti hai.

**David kya keh rahe hain:** *"Only" galat hai. Amazon audiences 3P par bhi lag sakti hain.*

**Maqsad:** Yahi galti **doosri baar** theek karna. Comment 1 §2.3 ki table par tha, ye Step 4 ki list par hai. **Ek hi galat baat do jagah likhi hui thi.**

**🔴 Maine kya samjha (ye bolna hai):**

> "'Only' shabd galat tha. Amazon audiences Amazon-owned inventory tak **confined nahi** hain — wo Netflix, Disney+ aur baaki par bhi lag sakti hain. Inventory source ki apni targeting **alternative** hai, **only option** nahi.
>
> Ye **wahi galti hai jo §2.3 ki tier table me thi** — is list me doosri baar. Ab dono jagah likha hai ki ye **per-deal choice** hai.
>
> **Aur ye cost ka ganit badal deta hai, jo wording se zyada matter karta hai.**
>
> Purani assumption thi ki Amazon ki data fee **sirf plan ke Amazon hisse** par lag sakti hai. Agar Amazon audiences 3P hisse par bhi chalti hain, to fee **wahan bhi** lagegi, aur us hisse ka effective CPM badh jaayega.
>
> To trader **teen situations** compare kar raha hai, do nahi:
> 1. Koi audience data nahi
> 2. Amazon data poore plan par
> 3. Amazon data Amazon inventory par, aur SSP ki apni targeting baaki par
>
> **Aur agent 3P par jo nahi kar sakta wo hai result verify karna.** Un tiers se reach forecast nahi aata, to agent audience widen kar sakta hai par dikha nahi sakta ki wo kaam kiya. Usko ye bolna chahiye, unverified change ko fix ki tarah present nahi karna chahiye."

**Real example:**
```
Plan: £10,000 — Prime Video £5,000, Netflix £5,000

SITUATION 1 — Koi audience data nahi:
   Prime:   £5,000 ÷ £24.00 × 1000 = 208,333 imps
   Netflix: £5,000 ÷ £22.96 × 1000 = 217,770 imps
   Total: 426,103 impressions, fee £0

SITUATION 2 — Amazon data POORE plan par:
   Prime:   £5,000 ÷ £25.63 × 1000 = 195,084 imps   (24.00 + 1.63)
   Netflix: £5,000 ÷ £24.59 × 1000 = 203,335 imps   (22.96 + 1.63)
   Total: 398,419 impressions, fee dono par
   → 27,684 impressions kam, par targeting dono par

SITUATION 3 — Amazon data sirf Amazon par, Netflix apni targeting:
   Prime:   £5,000 ÷ £25.63 × 1000 = 195,084 imps
   Netflix: £5,000 ÷ £25.96 × 1000 = 192,604 imps   (22.96 + £3 SSP fee)
   Total: 387,688 impressions
   → sabse kam impressions! SSP ki fee Amazon se mehngi thi

Purana document sirf Situation 1 aur 3 dikha sakta tha.
Situation 2 exist hi nahi karta tha uske liye.
```

**Kya change kiya (v3.0):**
- Constraint bullet rewrite: *"Amazon audiences can be applied to third-party inventory as well as Amazon-owned. The alternative is the inventory source's own targeting — a choice made per deal, not a property of the tier"*
- §2.3 ki Audiences column **tiers ko separate karna band** kar di
- Cost arithmetic ka asar likha
- 3 open questions

**Mai unse puch sakta hoon:**
1. Kya Amazon audiences **aur** inventory source ki targeting **ek hi deal** par chal sakti hain, ya ek hi?
2. Amazon ki targeting 3P par practically kitni limited hai? Tier-table note kehta hai kuch cases me sirf device — line kahan hai ye tay karega ki agent kya recommend kare
3. Is comment ke reply me **£2.00 VCPM** Amazon data fee quote hui thi. Aise figures hamesha `GET /api/contextual-targeting/fees` se padhne chahiye specification me likhne ke bajaye — taaki plan kabhi stale rate quote na kare?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Ye Comment 1 se alag kaise hai?"* | Same baat, doosri jagah. Comment 1 §2.3 ki tier table par tha, Comment 19 Step 4 ke constraints list par. David ne ek hi galti do jagah pakdi. |
| *"Cost par kya asar?"* | Bada. Pehle sochte the Amazon fee sirf Amazon inventory par lagegi. Ab pata chala ki 3P par bhi lagegi. To trader ke paas teen options hain, do nahi — aur teeno ka impressions count alag hai. |
| *"3P par audience widen kar sakte hain?"* | Technically haan. Par **verify nahi kar sakte** — 3P se reach forecast nahi aata. Agent ko bolna chahiye ki change kiya hai par uska asar dikha nahi sakta. |
| *"£2.00 figure kahan se aaya?"* | Comment ke reply me quote hua tha. Maine open question raise kiya ki aise figures hardcode na karein — API se padhein. Aur maine platform par actual value dekhi: `video_fee: "1.63"` GBP. |

---

## COMMENT 20 — `bundles.narrow/balanced/broad` support nahi hai

**Kahan:** Step 4, table ke neeche ka open question, `"bundles.narrow/balanced/broad"` par

**David ne kaha:** *"not currently supported"*

**Pehle kya tha:** v1.1.0 maan kar chal raha tha ki `POST /api/audience-sets/suggest/` endpoint **teen ready-made groups** wapas karta hai — ek object jisme `bundles.narrow`, `bundles.balanced`, `bundles.broad` hain.

**David kya keh rahe hain:** *Aisa kuch nahi hai. Endpoint ye nahi deta.*

**Maqsad:** Ek **galat assumption** pakadna. Document ek API feature par plan bana raha tha jo maujood nahi hai. Isse agent ka kaam badh jaata hai — grouping ka logic **humein likhna padega**.

**🔴 Maine kya samjha (ye bolna hai):**

> "v1.1.0 maan raha tha ki endpoint teen ready-made groups deta hai. Wo nahi deta. Agent ko segments ki **flat list** milti hai unke reach aur relevance ke saath, aur teen profiles **agent khud assemble karta hai**.
>
> **Aur ye badal deta hai ki teen profiles kya HAIN.**
>
> Do pehle ke comments ke saath dekho — fee provider se aati hai profile se nahi (Comment 2), aur profile choose karna optional hai (Comment 4). To Narrow, Balanced, Wide ab **teen price points wala API feature nahi hain**. Wo **ek hi flat list ko teen breadth levels par present karne ka tareeka hain**. Unme reach aur precision ka farak hai. **Daam ka farak nahi hai.**
>
> **Aur grouping ka rule ab likhna padega, kyunki upstream se kuch nahi aata.** Mera proposal:
> - **Cumulative reach** se group karo — kyunki fee ab options ko separate nahi karti, aur reach hi asal me unhe distinguish karta hai
> - Groups ko **nested** rakho — Balanced me Narrow ho, Wide me Balanced ho. Ye teen unrelated sets se zyada samajhne layak hai
> - Segments **reach target** tak add karo, fixed segment count tak nahi — taaki profiles alag-alag size ke briefs me comparable rahein
>
> Aur ek chhoti baat: `broad` vs `WIDE` ka naming mismatch jo v1.1.0 me note kiya gaya tha, **wo apne aap khatam ho gaya** — jab `bundles` object hi nahi hai to disagree karne ke liye koi API field nahi hai. `AudienceProfileEnum.WIDE` chalta rahega."

**Real example:**
```
DOCUMENT KYA MAAN RAHA THA:
POST /api/audience-sets/suggest/
→ {
    "bundles": {
      "narrow":   {"segments": [...], "reach": 45000},
      "balanced": {"segments": [...], "reach": 120000},
      "broad":    {"segments": [...], "reach": 280000}
    }
  }
→ Agent bas dikha deta. Kaam khatam.

ASLIYAT (David ke hisab se):
POST /api/audience-sets/suggest/
→ {"id": "abc-123"}                       ← async! ID milti hai
GET /api/audience-sets/suggest/abc-123/
→ [
    {"amz_id": "...", "name": "Healthy Food",       "reach": 45000, "relevance": 0.92},
    {"amz_id": "...", "name": "Health Conscious",   "reach": 38000, "relevance": 0.88},
    {"amz_id": "...", "name": "Diet and Nutrition", "reach": 52000, "relevance": 0.85},
    … 40 more segments, FLAT LIST
  ]

AB AGENT KO GROUP KARNA PADEGA (mera proposal — nested, cumulative reach):
   NARROW (target 50,000 reach):
      Healthy Food (45,000) + Health Conscious (38,000)
      → cumulative ~60,000 (overlap ke baad)
      
   BALANCED (target 150,000) — Narrow ko INCLUDE karta hai:
      Narrow ke segments + Diet and Nutrition + Gluten Free + Biscuits Snacks
      → cumulative ~155,000
      
   WIDE (target 300,000) — Balanced ko INCLUDE karta hai:
      Balanced ke segments + Females + Age 36-45 + Presence of children
      → cumulative ~310,000
```

**Kya change kiya (v3.0):**
- Open question **RESOLVED** mark kiya
- Grouping rule likha gaya (cumulative reach, nested, reach target)
- Note ki teen profiles ab presentation hain, API feature nahi
- `broad`/`WIDE` mismatch closed
- 5 open questions

**Mai unse puch sakta hoon:**
1. 🔴 **Kya `POST /api/audience-sets/suggest/` ka ek real response sample mil sakta hai?** Ye jaanna ki `bundles` galat hai sirf aadha jawab hai — grouping rule, fee handling aur audience schema sab actual shape par depend karte hain. **Audience ka kaam unblock karne ke liye ye sabse kaam ki cheez hai**
2. Staging me request model ka naam `SuggestAudienceGroupsInput` hai. "Groups" ka matlab ye hai ki **caller** groups ki sankhya maang sakta hai? Agar endpoint ko grouping bata sakte hain, to agent ko apna logic likhne ki zaroorat hi nahi
3. `POST` ek id deta hai aur `GET /api/audience-sets/suggest/{id}/` result padhta hai — to suggestion **asynchronous** lagta hai. Ye kitna time leta hai? Isse tay hoga ki agent conversation me wait kare ya baad me batane ka bole
4. Cumulative reach se group karna sahi basis hai, ya **relevance score** lead kare? Mera proposal reach maan raha hai
5. Comment me likha tha "not **currently** supported". Agar `bundles` baad me aaye, to agent ki grouping **replaceable** honi chahiye, baked-in nahi — abhi se design karein?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"To teen profiles ka matlab kya hai ab?"* | Wo ek flat list ko teen breadth levels par present karne ka tareeka hain. Reach aur precision me farak hai, cost me nahi. |
| *"Grouping kaise karenge?"* | Mera proposal: cumulative reach par, nested (Balanced me Narrow ho), aur reach target tak add karo — fixed segment count tak nahi. **Ye proposal hai, confirmed nahi.** |
| *"Async hai?"* | Lagta hai haan — POST id deta hai, GET result. Timing pata nahi, aur ye **open question** hai. Agar 30 second lagta hai to agent conversation me wait kar sakta hai. Agar 5 minute to nahi. |
| *"Platform par kya dekha?"* | 🔴 Maine ek bahut zaroori cheez dekhi: audience sets me ek **`prompt` field** hai — natural language, jaise *"Mums looking for healthier snacks for their kids school lunch boxes"*. Yaani **suggest feature pehle se hai aur use hota hai**. To agent ka kaam is step par asal me **prompt likhna** hai, segments browse karna nahi. |
| *"Aur kya dekha?"* | `audience_groups` field ek **nested boolean tree** hai (AND/OR), JSON **string** me. Chaar level deep. To "widen" karne ka matlab ya OR me term jodna hai ya AND branch hatana — dono ka reach par bilkul alag asar. |

---

## COMMENT 21 — Location market ke country se default hoti hai

**Kahan:** Step 5, `Location` ke saamne `"Optional"` par

**David ne kaha:** *"defaults to market country"*

**Pehle kya tha:**
```
| Location | List of str | Optional |
```
Jaise field khaali shuru hoti hai.

**David kya keh rahe hain:** *Field khaali nahi hoti. Market ka country pehle se bhara hota hai.*

**Maqsad:** Comment 5 ka hi practical detail — targeting pre-filled aati hai. Aur "Optional" ke matlab ko theek karna.

**🔴 Maine kya samjha (ye bolna hai):**

> "Field khaali shuru nahi hoti. Wo market ke apne country se bhari hoti hai, aur trader wahan se **narrow** karta hai — region, city, ya postcode tak.
>
> To 'Optional' ka matlab **'aapko chhune ki zaroorat nahi'** hai, na ki **'jab tak aap na bharein khaali hai'**. Ye bada farak hai.
>
> **Aur ek cheez jo document ne kabhi nahi kahi: `markets` aur `location` do alag fields hain, chahe dono aksar GB kehte hain.** Isi wajah se wo duplication lagte hain. Par wo **do alag sawaal** ka jawab dete hain:
>
> | | Kya sawaal ka jawab | Kya decide karta hai |
> |---|---|---|
> | `markets` | Kis market me kharid rahe hain? | Kaunsi deals exist karti hain, kaunsa rate card, kaunsi currency, kaunsi category aur location lists |
> | `location` | Ad kahan dikhna chahiye? | Geographic delivery |
>
> Wo same shuru hote hain aur **jaise hi trader narrow kare waise diverge** ho jaate hain: GB inventory khareedna par sirf London me deliver karna = `markets = ["GB"]` with `location = ["London"]`.
>
> **Aur narrow karne se reach ghat jaati hai, aur agent ko ye bolna chahiye.** Country se kuch postcodes tak jaane se addressable audience bahut kam ho sakti hai. Kyunki trader ne narrow karte waqt forecast nahi dekha, agent ko asar **report karna** chahiye — na ki reach shortfall baad me surprise ban kar aaye."

**Real example:**
```
Shuru me:
   markets  = ["GB"]
   location = ["GB"]          ← DEFAULT, khaali nahi
   
Trader: "sirf London me chalao"
   markets  = ["GB"]          ← same — GB inventory hi khareed rahe hain
   location = ["London"]      ← narrow ho gaya
   
Trader: "SW1, SW3, SW7 postcodes"
   markets  = ["GB"]          ← still GB
   location = ["SW1", "SW3", "SW7"]
   
Reach par asar:
   GB poora:     280,000 addressable
   London:        45,000 addressable      (84% kam!)
   3 postcodes:    3,200 addressable      (99% kam!)
   
Agent bolna chahiye:
   "Postcodes tak narrow karne se addressable audience 280,000 se
    3,200 par aa gayi. £10,000 par isse frequency bahut high ho jaayegi —
    har banda 100+ baar dekhega. Ya budget kam karein ya area badhayein?"
```

**Kya change kiya (v3.0):**
- Step 5 ki table me **Source aur Default columns add hue**
- `Location` Default: **"The market's country — `markets = [\"GB\"]` gives `location = [\"GB\"]`"**
- `markets` vs `location` ki table add hui
- Note ki narrow karne se reach ghatti hai aur agent ko bolna chahiye
- 2 open questions

**Mai unse puch sakta hoon:**
1. Content-category exclusions advertiser ki brand-safety settings se default honi chahiye? Maine table me waisa mark kiya hai ye maan kar ki brand safety advertiser-level rule hai, par ye confirm nahi hua
2. Jab trader geography narrow kare — agent turant re-forecast kare aur reach ka farak dikhaye, ya forecast step tak wait kare?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"`markets` aur `location` me farak?"* | `markets` = kahan **khareed** rahe hain (deals, rate card, currency isse aate hain). `location` = ad kahan **dikhna** chahiye (delivery). Same shuru hote hain, narrow karne par diverge. |
| *"Optional hai to khaali reh sakta hai?"* | Nahi. Optional ka matlab "trader ko chhune ki zaroorat nahi" hai. Value hamesha hogi — market ka country. |
| *"Postcode targeting hai VOW me?"* | ✅ Haan. Maine staging Swagger me verify kiya: `POST /api/strategies/postcode-validation/{market}/`. Aur `GET`/`POST /api/strategies/locations/{market}/` country, region, city ke liye. |
| *"Platform par ye kahan hai?"* | 🔴 Wizard me **nahi hai**. Creation ke baad `Locations` section me hai. Endpoint `/api/strategies/{id}/targeting/{market}/locations/` — strategy ID chahiye. To targeting creation ke baad hoti hai. |
| *"Aur kya mila Swagger me?"* | 🔴 `POST /api/strategies/{id}/targeting/auto-rec/` (model `StrategyTargetAutoREC`) — ye **automatically targeting recommend** karta hai. To baseline agent-side banane ki zaroorat hi nahi ho sakti. Ye endpoint pehle check karna chahiye. |

---

## COMMENT 22 — 🔴 Device type advertiser ki setting hai, aur "CTV" ke do matlab hain

**Kahan:** Step 5, `Device type` ke saamne `"Optional"` par

**David ne kaha:** *"Some advertisers only want CTV only - set at advertiser level"*

**Pehle kya tha:**
```
| Device type | List of str | Optional |
```
Aur `Mobile environment` field bhi thi, Optional.

**David kya keh rahe hain:** *Kuch advertisers sirf Connected TV chahte hain, aur wo advertiser level par set hota hai.*

**Maqsad:** Do kaam. Ek — advertiser-level defaults ka teesra instance. Do — aur ye zyada gehra — **document do cheezein blend kar raha tha**: content type aur device type.

**🔴 Maine kya samjha (ye bolna hai) — ye Comment 13 ke baad sabse gehra comment hai:**

> "Field advertiser se bhari aati hai, puchi nahi jaati. Ye **teesri setting** hai jo advertiser par nikli — frequency cap aur product category ke baad.
>
> **Par comment do cheezein alag karta hai jo document blend kar raha tha:**
>
> | | Kya hai | Kahan tay hota hai |
> |---|---|---|
> | `formats = ["streaming_tv"]` | Content ki kism — streaming video | CTV ke liye constant |
> | `device_types = ["Connected TV"]` | Screen jispar ad chalega | Advertiser ki setting |
>
> **Streaming content sirf TV par nahi dekha jaata.** Prime Video phones, tablets aur desktop browsers par chalti hai — aur wo sab **phir bhi `streaming_tv`** hain.
>
> **Aur document isko khud prove karta hai:** isi table me `Mobile environment` field hai — in-app vs mobile web. **Agar delivery sirf TV screens par hoti to wo field ka koi matlab hi nahi hota.** Uska maujood hona hi saboot hai ki aisa nahi hai.
>
> To wo field ab **Conditional** ho gayi: sirf tab apply karti hai jab device types me Mobile ya Tablet ho.
>
> **Connected TV tak restrict karne ke do asar hain jo trader ne choose nahi kiye:**
> 1. Streaming ka bada hissa mobile par hota hai — to **available inventory ghat jaati hai**
> 2. Connected TV inventory mobile se **mehngi** hai — to **CPM badh jaata hai** aur same budget me kam impressions
>
> Kyunki ye advertiser se aa raha hai, brief se nahi, agent ko **dono asar batane** chahiye — na ki plan chupke se chhota aa jaaye.
>
> **Aur yahi jagah hai jahan default aur policy ka farak matter karna shuru karta hai.** 'Only want CTV only' ek **rule** lagta hai, starting point nahi. Device targeting relax karna un levers me se ek hai jo repair loop reach kam hone par use karta hai — aur agar advertiser ne usko rule out kiya hai, to **wo lever available nahi hai**. Agent ko wo cheez widen karne ki offer **nahi karni** chahiye jise chhune ki ijazat nahi hai, aur usko **batana** chahiye ki kaunsa lever use nahi kar paya. **Yahi `is_locked` flag ka maqsad hai** jo Comment 13 me introduce hua."

**Real example:**
```
Format aur device do alag cheezein hain:

   formats = ["streaming_tv"]              ← Prime Video ka content
   
   device_types = ["Connected TV"]          → TV screen par Prime Video
   device_types = ["Connected TV", "Mobile"] → TV + phone par Prime Video
   device_types = ["Mobile"]                → sirf phone par Prime Video
   
   TEENO CASES ME format streaming_tv HI HAI!

Ab locked policy ka asar:

BrightPath ki setting:
   device_types: {value: ["Connected TV"], is_locked: TRUE,
                  reason: "Brand policy — premium TV screens only"}

Agent plan banata hai:
   Available inventory:  CTV only     → 40% kam supply
   CPM:                  £24 (CTV)    → mobile £14 hota
   Impressions:          £10,000 ÷ 24 × 1000 = 416,667
                         (mobile allow hota to 714,286 milte)
   
Agent bolta hai:
   "Advertiser ki policy CTV-only hai. Isse inventory kam hai aur CPM
    zyada — mobile allow hota to same budget me ~70% zyada impressions
    milte. Par ye brand policy hai, mai badal nahi sakta."

Reach kam aati hai. Repair loop:
   Agent: "Levers check kar raha hoon —
           ✗ device widen — LOCKED (brand policy)
           ✓ audience widen — available
           ✓ inventory widen — available
           Audience widen karta hoon."
           
   is_locked KE BINA:
   Agent: "Mobile add kar deta hoon!" → BRAND POLICY TOOT GAYI
```

**Kya change kiya (v3.0):**
- `Device type` Source: **ADVERTISER**, Default: *"The advertiser's own setting — Connected TV only for some brands. May be locked rather than merely defaulted"*
- `Mobile environment` Requirement: Optional → **Conditional**
- Format vs device ki table add hui
- Do asar likhe gaye (inventory shrink, CPM rise)
- `is_locked` ka connection Comment 13 se banaya
- 4 open questions

**Mai unse puch sakta hoon:**
1. 🔴 **Device setting ek default hai jise trader override kar sakta hai, ya ek locked brand policy?** Isse tay hoga ki repair loop usko chhu sakta hai — **aur ye ek jawab hai jo wording ke bajaye agent ka behaviour badalta hai**
2. Isi tarah aur kaunsi advertiser settings lock ho sakti hain? Brand-safety exclusions candidate lagti hain
3. Agar advertiser ki koi device setting hi nahi hai, to fallback kya — Connected TV only, ya sab devices?
4. `Connected TV`, `Mobile`, `Tablet`, `Desktop` — ye poori list hai? Aur ye list kisi endpoint se aati hai ya schema me fixed hai?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"`streaming_tv` format ka matlab TV screen nahi?"* | 🔴 **Nahi.** Matlab hai "streaming content". Prime Video phone par bhi chalti hai aur wo bhi `streaming_tv` hai. Screen `device_types` batata hai. Ye do alag fields hain. |
| *"Iska saboot kya hai?"* | Document khud. Isi table me `Mobile environment` field hai (in-app vs mobile web). Agar delivery sirf TV par hoti to wo field bemaani hoti. Uska hona hi saboot hai. |
| *"CTV-only ka nuksan kya?"* | Do — inventory ghatti hai (streaming ka bada hissa mobile par hai), aur CPM badhta hai (CTV mehngi hai). To same budget me kam impressions. Agent ko dono batane chahiye. |
| *"`is_locked` yahin se aaya?"* | Haan. Comment 13 me maine introduce kiya, par **wajah ye comment hai**. "Only want CTV only" rule lagta hai, default nahi. Bina flag ke agent locked policy relax karne ki offer kar dega. |
| *"Platform par device targeting kahan hai?"* | 🔴 Wizard me **nahi**. Deals ke filter me `Device` hai (Connected TV, Desktop, Mobile, Unknown) — par wo deals filter karta hai, targeting set nahi karta. Asli device targeting creation ke baad hogi. |

---

## COMMENT 23 — Approval ek status change ban gaya

**Kahan:** Step 7 ke heading `"Plan Approval"` par

**David ne kaha:** *"we simplified this so it's just a status changed to finalise the plan - no manager approval required for now"*

**Pehle kya tha:** Step 7 ek poora **approval gate** tha — manager routing, rejection reason, rejection path wapas audience step par, aur LangGraph me `interrupt()`.

**David kya keh rahe hain:** *Ye simplify ho gaya. Bas ek status change hai. Manager approval abhi nahi chahiye.*

**Maqsad:** Scope kam karna. Ek poori approval workflow M1 se nikalna.

**🔴 Maine kya samjha (ye bolna hai):**

> "Step ka naam **Finalise Plan** ho gaya, aur wo ek status par simat gaya — `DRAFT` se `FINALISED`, trader hi conversation me karta hai. `Manager required` aur `Rejection reason` fields gayi, aur audience step par wapas jaane ka rejection path bhi gaya.
>
> **Jo hataya wo ek field se bahut bada hai.** Approval gate ka matlab tha ek doosra insaan: ek notification bhejna, unknown time tak wait karna, ek rejection route, ek threshold rule (kab approval chahiye), aur roles (kaun de sakta hai). **Ye sab M1 se nikal gaya.**
>
> **Aur ye ek jagah bhi hataata hai jahan agent ko rukna padta tha.** Step LangGraph ka `interrupt()` use karta tha — graph rukta tha aur state persist karta tha jab tak koi doosra act na kare, jo ghanton baad ho sakta tha, aur conversation beech me khuli reh jaati thi. **Wo interrupt gaya.**
>
> **Par creative-approval step ka interrupt RAHEGA — aur sahi hai.** Wahan agent Amazon ya publisher ki review par wait kar raha hai, jo **asal me external aur asynchronous** hai. Ye farak saaf rakhna zaroori hai: **platform jo review karta hai uske liye rukna, aur colleague ke liye rukna — ek jaisi cheez nahi hai.**
>
> **Do cheezein maine jaan-boojh kar extensible rakhi**, kyunki comment me likha tha 'for now':
>
> 1. `PlanStatusEnum` apna alag enum hai, `ApprovalStatusEnum` reuse nahi kiya. Plan aur creative ke lifecycle ab **alag** hain — `DRAFT`/`FINALISED` vs `PENDING`/`APPROVED`/`REJECTED` — aur ek enum share karne se ek ko doosre ki values carry karni padengi jo use nahi kar sakta. Baad me `PENDING_APPROVAL` add karna phir **additive** hoga, rework nahi
> 2. Fields rename kiye: `approval_status` → `plan_status`, `approved_by` → `finalised_by`, `approved_at` → `finalised_at` — taaki naam wahi kahe jo hota hai
>
> **Aur approval agar wapas aaya to manager gate ke roop me nahi aayega.** Comment 13 ke advertiser-defaults ke baad, zyada likely shape ye hai: ek **advertiser-level rule** — '£10,000 se upar ke plans ko meri sign-off chahiye' — jo VOW ke andar approval workflow nahi, **advertiser ki policy** hai. `approval_threshold` ke liye advertiser settings me jagah chhodne ki cost zero hai aur rework se bacha lega."

**Real example:**
```
PURANA (approval gate):
Trader: "plan theek hai, approve karo"
Agent:  [interrupt()] → manager ko notification
        → graph RUK GAYA
        → 3 ghante baad manager aata hai
        → manager reject karta hai: "budget zyada hai"
        → graph Step 4 par wapas jaata hai
        → trader dobara audience choose karta hai
        → dobara approval maangta hai
→ complex, aur agent ghanton fansa rehta hai

NAYA (status change):
Trader: "plan theek hai"
Agent:  plan_status: DRAFT → FINALISED
        finalised_by: "kareem@calyxio.ai"
        finalised_at: "2026-08-04T15:30:00Z"
        "Plan finalise ho gaya. Ab strategy create karta hoon."
→ koi ruk nahi, koi doosra insaan nahi

PAR Step 10 ka interrupt RAHEGA:
Agent:  creative Amazon ko bheja
        [interrupt()] → Amazon review kar raha hai
        → ye SAHI hai, kyunki Amazon asal me bahar hai aur time lega
```

**Kya change kiya (v3.0):**
- Step ka naam: `Plan Approval` → **`Finalise Plan`**
- `PlanStatusEnum{DRAFT, FINALISED}` naya enum add hua
- Fields rename: `plan_status`, `finalised_by`, `finalised_at`
- `Manager required`, `Rejection reason` fields **hata di**
- Rejection path hata diya
- `interrupt()` hata diya (Step 10 ka rakha)
- `approval_threshold` advertiser settings me future scope
- 4 open questions

**Mai unse puch sakta hoon:**
1. Finalised plan wapas `DRAFT` ho sakta hai? Isse tay hoga ki agent finalise karne se pehle warn kare ya reversible maane
2. Plan finalise hone ke baad kya badal sakta hai? Budget aur matched deals commercial commitments hain, to wo targeting jaisi category me nahi lagte
3. Advertiser-level approval threshold plan karna chahiye, ya approval abhi poori tarah scope se bahar?
4. Status change **kaunsa endpoint** record karta hai? Staging API me kuch aisa nahi dikha jo plan status ko `POST /api/strategies/{id}/set_status/` se alag treat kare — aur wo activation hai

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Ek field hatane me itna kya hai?"* | Ek field nahi hati. Poora approval workflow gaya — notification, wait, rejection route, threshold rule, roles, aur ek `interrupt()`. Ye implementation ka bada hissa hai. |
| *"Interrupt kyun hataya?"* | Kyunki wahan agent ek **colleague** ka wait kar raha tha. Ab trader khud finalise karta hai, usi conversation me. Koi wait nahi. Par Step 10 ka interrupt **raha** — wahan Amazon ka wait hai, jo asal me external hai. |
| *"Alag enum kyun banaya?"* | Plan aur creative ke lifecycle alag hain. Plan `DRAFT`/`FINALISED` hai. Creative `PENDING`/`APPROVED`/`REJECTED` hai. Share karne se ek ko doosre ki values carry karni padengi. Aur baad me `PENDING_APPROVAL` add karna additive rahega. |
| *"'For now' ka kya socha?"* | Approval wapas aa sakta hai — par manager gate ke roop me nahi. Advertiser-level rule ke roop me: "£10k se upar mera sign-off". Isliye maine `approval_threshold` ke liye jagah chhodi hai. |
| *"Platform par draft kya hai?"* | 🔴 Maine dekha ki `Save as draft` button Step 1 par **disabled** hai, Step 2 par **enable** ho jaata hai. Aur drafts me `budget: null` hota hai. Aur draft rows ka `status: "6_inactive"` hai — to draft alag status nahi, ek boolean hai. |

---

## COMMENT 24 — Creation `simple-strategies` use karega

**Kahan:** Step 8, `"api/strategies"` par

**David ne kaha:** *"probably more likely simple-strategies endpoint"*

**Pehle kya tha:**
```
POST /api/strategies/     ← creation ke liye
```

**David kya keh rahe hain:** *Ye endpoint galat lagta hai. `simple-strategies` hona chahiye.*

**Maqsad:** Ek galat endpoint theek karna. Par isse ek bada sawaal khada hota hai: **agar ek endpoint galat hai to baaki kitne galat hain?**

**🔴 Maine kya samjha (ye bolna hai):**

> "Staging API ke against confirm kiya — `POST /api/simple-strategies/` exist karta hai, request model `SimpleStrategyCreate`. Comment me 'probably' likha tha; ab wo guess nahi hai.
>
> **Par bada point ye tha ki ek galat endpoint akela nahi hota.** Is document ke API calls v1.1.0 se aaye the aur dobara check kabhi nahi hue. To maine **poori list staging Swagger ke against padhi.** Ye mila:
>
> | Document me maana | Asliyat |
> |---|---|
> | `POST /api/strategies/` creation ke liye | `POST /api/simple-strategies/` — CTV variant, POST only |
> | *(koi update endpoint listed nahi)* | `PATCH /api/strategies/{id}/` exist karta hai — model `StrategyUpdate` |
> | `POST /api/rate-cards/match/` deal matching ke liye | 🔴 **EXIST NAHI KARTA.** Matching `GET /api/deals/` + `GET /api/deals/filter-properties/` se hoti hai |
> | `/api/advertisers/{id}/defaults/` advertiser settings ke liye | 🔴 **EXIST NAHI KARTA.** Settings `GET /api/admin/advertiser/{id}/` par hain |
> | Postcode support unknown | `POST /api/strategies/postcode-validation/{market}/` exist karta hai |
> | Fee values unknown | `GET /api/contextual-targeting/fees` exist karta hai |
>
> **Total 14 catalogue rows add ya correct hue.**
>
> Aur ek baat jo saaf likhni padi kyunki warna inconsistent lagti hai: **`simple-strategies` sirf POST support karta hai** — usme koi read ya update nahi hai. To strategy CTV endpoint se **create** hoti hai aur phir general endpoint se **update** hoti hai."

**Real example:**
```
Do endpoints, do kaam:

Create:
   POST /api/simple-strategies/
   { name, flight_dates, markets_info, market_deals, ... }
   → 201 { id: "VMA2026368" }
   
   Par is endpoint par:
      GET    → nahi hai
      PATCH  → nahi hai
      PUT    → nahi hai
      
Update (baad me, ASINs attach karne ke liye):
   PATCH /api/strategies/VMA2026368/
   { product_asins: ["B08N5WRWNW"] }
   → model StrategyUpdate
   
To do alag families use karni padengi. Ye ajeeb lagta hai par
documented hai — warna koi soch lega ki galti hai.
```

**🔴 Ek zaroori discovery maine platform par ki:**

> "Maine platform par actual creation dekhi — aur usne **`POST /api/strategies/`** use kiya, `simple-strategies` **nahi**.
>
> Yaani manual wizard general endpoint use karta hai. `simple-strategies` aur `automated-strategies` dono exist karte hain par **manual flow me use nahi hote**.
>
> To sawaal ye ban jaata hai: agent ko kaunsa use karna chahiye? Teen options hain aur teeno exist karte hain. Aur `automated-strategies` ka naam agent ke liye sabse fit lagta hai."

**Kya change kiya (v3.0):**
- Endpoint: `POST /api/strategies/` → **`POST /api/simple-strategies/`**
- §4 API catalogue me **14 rows add/corrected**, staging Swagger ke against, 4 Aug 2026 ko dated
- Note ki `simple-strategies` POST-only hai
- 2 non-existent endpoints flag kiye
- 3 open questions

**Mai unse puch sakta hoon:**
1. 🔴 **`POST /api/automated-strategies/` kya hai?** Wo API me `simple-strategies` ke saath baithta hai, models `AutomatedStrategyCreate` aur `AutomatedStrategyFormatsAndKpis`. Naam se lagta hai ki wo agent ke liye `simple-strategies` se zyada fit hai. In dono me se kaunsa intended hai?
2. `SimpleStrategyCreate` ki field list mil sakti hai? Is document me jo payload describe hua hai — no base bid, format fixed, advertiser defaults pre-filled — usko **field-by-field match** karna hai, aur endpoint listing se wo nahi dikhta
3. `strategies-sp` ek alag family hai apne draft endpoints ke saath. Confirm ho jaaye ki wo sponsored products hai aur CTV se irrelevant hai to wo band ho jaayega

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Sirf ek endpoint galat tha?"* | Nahi. Maine poori list check ki — **do endpoints exist hi nahi karte** (`rate-cards/match`, `advertisers/{id}/defaults`), do jinke baare me pata nahi tha wo exist karte hain (postcode, fees), aur ek update endpoint jo listed nahi tha wo hai (PATCH). Total 14 corrections. |
| *"Do endpoint families kyun?"* | `simple-strategies` POST-only hai. To create CTV endpoint se, update general endpoint se. Ajeeb lagta hai par aisa hi hai. |
| *"Platform par kaunsa use hota hai?"* | 🔴 **`POST /api/strategies/`** — general wala. `simple-strategies` manual flow me use hi nahi hota. To agent ke liye kaunsa sahi hai, ye open question hai. |
| *"Ye kaise verify kiya?"* | Company ne staging ka Swagger listing diya (`swagger_api.txt`). Maine har endpoint us list ke against padha, 4 August 2026 ko. Corrections dated hain. |

---

## COMMENT 25 — Click-through URL streaming TV par optional hai

**Kahan:** Step 9, `Click-through URL` ke saamne `"Required"` par

**David ne kaha:** *"optional for streaming tv"*

**Pehle kya tha:**
```
| Click-through URL | HttpUrl | Required |
```

**David kya keh rahe hain:** *Streaming TV me ye required nahi hona chahiye.*

**Maqsad:** Ek field ko required hone se rokna jiska CTV me kaam hi nahi hai. Agar required rahe to trader us field par **block** ho jaayega jo uske liye bemaani hai.

**🔴 Maine kya samjha (ye bolna hai):**

> "Remote pakde hue viewer ad par click nahi kar sakta, to landing page maangna trader ko ek aisi field par rok dega jiska television par koi kaam nahi hai. Schema follow karta hai: `click_through_url: Optional[HttpUrl] = None`, aur jab di jaaye tab bhi URL ki tarah validate hogi.
>
> **Wajah likh raha hoon taaki ye wapas na daali jaaye.** CTV par call-to-action doosri shakal leta hai — creative me QR code, bolke ya screen par 'search for BrightPath' ka prompt, ya bas brand recall. **Measurement bhi click par depend nahi karta** — wo tracking step par set hone wale ASINs ya ad tag se aata hai.
>
> **Ek refinement, Comment 22 ke device-type ke baad.** Device types advertiser se aate hain aur unme mobile, tablet ya desktop ho sakta hai — **aur un screens par ad click HO SAKTA hai.**
>
> To 'optional for streaming TV' asal me **do cases** hain:
> - Sirf Connected TV — URL kuch kar hi nahi sakta
> - Mobile ya desktop bhi hai — URL kaam ki cheez hai
>
> Isliye row me maine likha ki us case me **recommended** hai, required nahi — trader block nahi hota par click-through chupke se waste bhi nahi hota."

**Real example:**
```
Case A — sirf Connected TV:
   device_types = ["Connected TV"]
   click_through_url = None
   → theek hai. TV par click hi nahi ho sakta.
   → CTA: QR code creative me, ya "search BrightPath"
   → Measurement: ad tag (site par jo aaye) ya ASINs

Case B — CTV + Mobile:
   device_types = ["Connected TV", "Mobile"]
   click_through_url = "https://brightpath.com/courses"
   → RECOMMENDED. Mobile par click ho sakta hai.
   → Agar URL na do to mobile impressions ka click-through waste
   
Agent ka behaviour:
   Case A me: URL nahi maangta
   Case B me: "Device targeting me mobile bhi hai — landing page URL
               de dein? Mobile par ad clickable hoga."
```

**🔴 Platform par jo verify kiya:**

> "Maine actual creatives dekhe aur David ki baat **confirm** ho gayi:
>
> ```json
> { "type": "Streaming TV Video", "approval_status": "APPROVED", "click_through_url": null }
> { "type": "Streaming TV Video", "approval_status": "APPROVED", "click_through_url": null }
> ```
>
> **Streaming TV creative bina click-through URL ke APPROVED ho sakta hai.** To ye sirf schema ka faisla nahi, platform bhi aise hi kaam karta hai.
>
> Aur ek dilchasp baat — staging me kuch URLs polluted hain. Testers ne address bar ka URL paste kar diya hai:
> ```
> https://staging.vowmade.dev/app/strategies/create/dsp?aid=…&step=1
> ```
> Field kisi bhi URL ko accept karta hai — validate nahi karta ki wo landing page hai ya nahi."

**Kya change kiya (v3.0):**
- Requirement: Required → **Optional**
- Schema: `click_through_url: Optional[HttpUrl] = None`
- Wajah likhi gayi (QR code, search prompt, brand recall)
- Note ki mobile/desktop ho to **recommended**
- 3 open questions

**Mai unse puch sakta hoon:**
1. Jahan device types me mobile ya desktop ho — agent **actively URL maange**, ya optional rakhe aur ek baar mention kar de?
2. 🔴 **Staging API me ek model hai `MarketWithClickthroughUrl`.** Kya click-through URL **per market** hota hai? Multi-market campaign me ye matter karega — German landing page British se alag hai — aur ye document abhi isko ek single value maanta hai
3. CTV creatives me **QR codes** allowed hain, aur uska koi spec hai? Agar wo practical CTA hai to usko yahan naam dena chahiye, traders ko guess karne ke liye chhodne ke bajaye

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"URL nahi to CTA kya hoga?"* | Teen tareeke — creative me QR code, on-screen/spoken prompt ("search for BrightPath"), ya sirf brand recall. Aur measurement click par depend nahi karta, wo ASINs ya ad tag se aata hai. |
| *"Mobile hai to zaroori hai?"* | Required nahi, **recommended**. Mobile par ad clickable hai, to URL na dena mauka waste karna hai. Par trader ko block nahi karenge. |
| *"Validate hoga?"* | Haan, jab diya jaaye tab URL ki tarah validate hoga. Optional ka matlab "de sakte ho ya nahi", "kuch bhi de do" nahi. |
| *"Platform ye confirm karta hai?"* | ✅ Haan. Maine `Streaming TV Video` type ke creatives dekhe jo `APPROVED` hain aur `click_through_url: null` hai. |

---

## COMMENT 26 — Per channel ek status, aur channel list data hai

**Kahan:** Step 10, teen hardcoded approval rows par

**David ne kaha:** *"It's just a single status for each channel not necessary netflix or disney - could be paramount or channel 4"*

**Pehle kya tha:** Teen alag-alag rows, publisher ke naam ke saath hardcoded:
```
| Prime Video approval | Enum | Read-only |
| Netflix approval     | Enum | Read-only |
| Disney+ approval     | Enum | Read-only |
```

**David kya keh rahe hain:** *Ek field jo per channel status rakhe. Aur Netflix/Disney hardcode na karo — Paramount ya Channel 4 bhi ho sakta hai.*

**Maqsad:** Ek **schema design** ki galti theek karna. Publisher ke naam **data** hain, schema ke fields nahi. Aur wo change hote rehte hain.

**🔴 Maine kya samjha (ye bolna hai):**

> "Teen rows ek field ban gaye jo per channel status rakhta hai, aur keys wo channels hain jo plan ne **actually match** kiye:
>
> ```json
> {"Prime Video": "APPROVED", "Netflix": "PENDING", "Channel 4": "PENDING"}
> ```
>
> **Shape tidiness se zyada matter karta hai.** Publisher ke hisab se ek row hone par Paramount+ add karna matlab: schema badlo, migrate karo, backend chhuo, interface chhuo, tests chhuo, aur ek release ship karo — **ek naam add karne ke liye.** Dictionary hone par wo ek **data change** hai aur bas.
>
> **Aur 'Channel 4' ka chunav jaan-boojh kar hai:** wo ek **British broadcaster** hai. To list sirf changeable nahi, **market-specific** bhi hai — UK me ITVX aur Channel 4 hain, US me Hulu aur Peacock. Hardcode karna sirf untidy nahi hota; wo **ek market se aage scale hi nahi karta.**
>
> **Jo fixed rehta hai wo states ka set hai.** `PENDING`, `APPROVED`, `REJECTED` stable hain aur agent ki logic un par depend karti hai, to wo enum rahenge. **Keys data hain, values nahi.** Sab kuch dynamic karna type safety kho dega jo matter karti hai.
>
> **Aur ek baat jo mujhe achhi lagi: document me ye rule EK section pehle already tha.** Targeting step (Step 5) me ek design note hai ki *'This targeting list frequently changes so it should be easy to add new targeting types'* — config-driven hona chahiye, hardcoded nahi. **Channels wahi kism ki list hain.** Rule likh diya gaya tha aur yahan apply nahi kiya gaya.
>
> **Naming:** client ka shabd 'channel' hai. Deal schema isi cheez ko `provider` kehta tha, aur inventory step me ab ek `Channel` field hai — to ek concept ke **teen naam** ho gaye the. `SelectedDealSchema.provider` ko **`channel`** rename kiya, aur wahi field `CurationRequirementsSchema` aur `BudgetSplitSchema.by_inventory` me bhi.
>
> **Ek caveat**, kyunki 'provider' document se gaya nahi hai: wo audience notes me **abhi bhi hai**, jahan uska matlab **data provider** hai — Amazon 1P vs Experian jaisa third party. **Wo channel se alag cheez hai** aur dono ko collapse nahi karna chahiye. **Channel = kaun ad dikha raha hai. Data provider = kiska audience data khareed rahe ho.**"

**Real example:**
```
PURANA (hardcoded):
class CreativeApproval(BaseModel):
    prime_video: ApprovalStatusEnum
    netflix:     ApprovalStatusEnum
    disney:      ApprovalStatusEnum

Paramount+ add karna:
   1. schema me field add karo
   2. database migration likho
   3. backend endpoint update karo
   4. frontend component update karo
   5. tests update karo
   6. release ship karo
→ ek naam add karne ke liye poora release!

Aur UK campaign me? Channel 4 ke liye field hi nahi hai.

NAYA (dictionary):
creative_approval_statuses: dict[str, ApprovalStatusEnum]

UK plan:
   {"Prime Video": "APPROVED", "Channel 4": "PENDING", "ITVX": "PENDING"}
   
US plan:
   {"Prime Video": "APPROVED", "Hulu": "PENDING", "Peacock": "REJECTED"}
   
→ code me kuch nahi badla. Keys plan se aate hain.
→ Paramount+ add karna: bas naya key aa jaayega. Zero code change.

Par VALUES enum hi hain:
   "APPROVED" ✅   "PENDING" ✅   "REJECTED" ✅
   "kind-of-approved" ❌  ← type error, aur ye achha hai
```

**Kya change kiya (v3.0):**
- Teen rows → ek field: `creative_approval_statuses: dict[str, ApprovalStatusEnum]`
- Keys **data**, values **enum**
- `SelectedDealSchema.provider` → **`channel`** rename (aur 2 aur jagah)
- Note ki "provider" audience context me raha (data provider), channel se alag
- Config-driven rule ka reference Step 5 se
- 3 open questions

**Mai unse puch sakta hoon:**
1. Channel list kahan se aani chahiye — `GET /api/admin/advertiser/get_channels_choices/`, ya matched deals se derive? Endpoint exist karta hai; matched deals se derive karne se sirf wo channels milenge jo plan me hain, jo shayad interface ko wahi chahiye
2. Approval status **per channel** hota hai, ya **per creative-and-channel** pair? Ek plan me 15s aur 30s creative ho, to ek approve ho aur doosra na ho — usi channel par — ye possible lagta hai
3. Is document me aur kaunsi lists config-driven honi chahiye? Genres, markets aur device types teeno candidate lagte hain, aur `GET /api/strategies/choices/` shayad kuch already serve karta hai

**🔴 Platform par jo mila (aur ye David ke model se disagree karta hai):**

> "Maine actual creative objects dekhe. Ye mila:
>
> ```json
> { "market": "GB", "approval_status": "APPROVED", "type": "Streaming TV Video" }
> ```
>
> **Creative object me channel ka koi dimension hi nahi hai.** Granularity **creative × market** hai, creative × channel nahi.
>
> To David ka model — per channel ek status — VOW ke current data se **populate nahi ho sakta.** Ye document me `STILL OPEN` ke roop me flag hai, aur wo sahi flag tha."

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Keys data kyun aur values enum kyun?"* | Keys badalte rehte hain (naye publishers, aur market-specific hain) — to wo data honi chahiye. Values fixed hain (PENDING/APPROVED/REJECTED) aur agent ki logic unpar depend karti hai — to wo enum rehni chahiye. Sab dynamic karna type safety kho dega. |
| *"Channel 4 ka example kyun diya?"* | Kyunki wo British hai. Ye dikhata hai ki list sirf changeable nahi, **market-specific** bhi hai. UK me ITVX/Channel 4, US me Hulu/Peacock. Hardcode karna ek market se aage scale nahi karega. |
| *"`provider` se `channel` kyun?"* | Client ka shabd "channel" hai, aur ek concept ke teen naam the. Par **audience context me `provider` raha** — wahan matlab data provider hai (Amazon vs Experian), jo bilkul alag cheez hai. |
| *"Ye buildable hai?"* | 🔴 **Abhi nahi.** Maine verify kiya — creative object me channel dimension hi nahi hai. Granularity creative × market hai. Ye `STILL OPEN` hai document me. |

---

## COMMENT 27 — 🔴 Koi order nahi, aur isliye ek gate chahiye

**Kahan:** Step 11 ke heading `"Tracking Setup"` par

**David ne kaha:** *"could be done before creatives if they are no available yet - no order necessary"*

**Pehle kya tha:** Steps 9, 10, 11, 12 numbered the — jaise ek chain ho: creative → approval → tracking → credit.

**David kya keh rahe hain:** *Tracking creative se pehle bhi ho sakti hai. Koi order zaroori nahi.*

**Maqsad:** Ek galat sequence hatana. Par iska nateeja bahut bada hai — jo David ne shayad ek chhoti allowance samjha, wo asal me **flow ki shape badal deta hai.**

**🔴 Maine kya samjha (ye bolna hai):**

> "Tracking creative aane se pehle set ho sakti hai. Jo ek chhoti allowance lagti hai — **aur nahi hai.**
>
> **Numbering ek chain imply kar rahi thi jo maujood nahi hai.** Agar tracking, creatives aur credit check kisi bhi order me ho sakte hain, to wo steps 9, 10, 11, 12 **nahi hain** — wo **teen branches** hain jo strategy create hone ke baad independently chalti hain aur **activation par milti hain**.
>
> Creation tak ka sequence **asal me ordered** hai: inventory CPM decide karti hai, CPM impressions decide karti hai, forecast ko targeting chahiye. **Chain hai.** Creation ke baad, teeno me se koi doosre ka wait nahi karta.
>
> **Aur ye matches karta hai ki kaam asal me kaise aata hai.** Creatives agency se aate hain aur **aksar late** aate hain. Ad tag advertiser ke apne developers ko install karna padta hai, jisme **din lag sakte hain**. Credit finance ka matter hai. **Order force karne ka matlab hai ek late item sab kuch block kar deta hai**, jabki trader baaki sab khatam kar sakta tha.
>
> **🔴 Order hatane se ek completeness check ZAROORI ho jaata hai.** Kisi cheez ko establish karna padega ki paise kharch hone se pehle sab kuch jagah par hai — aur yahi Step 13 ka **join node** karta hai:
>
> | Prerequisite | Kab hold karta hai |
> |---|---|
> | Creatives uploaded | Plan ki har duration ke liye ek — 15s aur 30s plan ko dono chahiye |
> | Creatives approved | Har matched channel ne `APPROVED` diya |
> | Ad tag registered | Advertiser Amazon par nahi bechta aur tag lag chuka hai |
> | ASINs attached | Advertiser Amazon par bechta hai aur ASINs validate ho gaye |
> | Conversions chosen | Chun liye, ya jaan-boojh kar skip kiye |
> | Credit sufficient | Balance ≥ strategy budget |
>
> **Aur document ne ye already imply kiya tha bina kahe:** creative-approval step me likha hai *'a plan can be fully approved and funded and still not launch until the creative clears.'* **Wo prose me likha hua launch gate hai** — ab wo ek checklist hai.
>
> **Step numbers maine jaan-boojh kar waise hi rakhe** taaki review comments apni jagah anchored rahein. Parallelism yahan aur state machine me record hai, renumbering se nahi.
>
> **🔴 Aur checklist ek unresolved cheez par depend karti hai.** 'Har channel ne approve kiya' sirf tab check ho sakta hai jab wo per-channel statuses **API se readable** hon — jo Comment 26 ka open question hai. Agar wo VOW ke bahar track hote hain, to wo prerequisite **evaluate hi nahi ho sakta**, aur activation ya to indefinitely block hoga ya trader par bharosa karna padega."

**Real example:**
```
PURANA (forced order):
Step 8:  strategy created ✅
Step 9:  creative upload — 🔴 agency ne abhi bheja nahi. RUK GAYE.
Step 10: (block)
Step 11: (block) — jabki ad tag TODAY set ho sakta tha
Step 12: (block) — jabki credit TODAY check ho sakta tha
→ ek late creative ne 3 din waste kar diye

NAYA (parallel branches):
Step 8: strategy created ✅
        │
        ├─→ Branch A: Creatives    🔴 agency ka wait (3 din)
        ├─→ Branch B: Tracking     ✅ AAJ HO GAYA
        └─→ Branch C: Credit       ✅ AAJ HO GAYA
        
Day 3: creative aa gaya, approve hua
        │
        └─→ Step 13 JOIN NODE:
              creative_uploaded  {"15": true, "30": true}  ✅
              creative_approved  {"Prime Video": APPROVED} ✅
              ad_tag_registered  true                      ✅
              asins_attached     null (not applicable)     ✅
              conversions_chosen true                      ✅
              credit_sufficient  true                      ✅
              
              → ready_to_activate = TRUE
              → ACTIVATE
              
→ 3 din bache, aur launch ke waqt sab verified
```

**Code jo add hua:**
```python
class ActivationPrerequisitesSchema(BaseModel):
    """NEW — checked at the join node before any spend."""
    creative_uploaded: dict[str, bool]                 # per duration: {"15": True, "30": False}
    creative_approved: dict[str, ApprovalStatusEnum]   # per channel: {"Prime Video": APPROVED}
    ad_tag_registered: Optional[bool] = None           # None when not applicable
    asins_attached: Optional[bool] = None              # None when not applicable
    conversions_chosen: bool = False                   # True if chosen or deliberately skipped
    credit_sufficient: bool = False
```

**Kya change kiya (v3.0):**
- Note ki Steps 9–12 **parallel branches** hain, ordered steps nahi
- Step 13 ko **join node** banaya
- `ActivationPrerequisitesSchema` add hua 6 prerequisites ke saath
- `ready_to_activate` property
- Step numbers **nahi badle** (comments anchored rehne ke liye)
- Dependency flag ki checklist Comment 26 par depend karti hai
- 4 open questions

**Mai unse puch sakta hoon:**
1. Prerequisite list **poori** hai, ya kuch aur bhi true hona chahiye campaign live hone se pehle?
2. **Credit check** asal me order-free hai? Uska outcome **budget badal sakta hai** — jo argue karta hai ki wo plan finalise hone se pehle chale, creative ke saath-saath nahi
3. Conversions **poori tarah skip** ho sakti hain — bilkul bina conversion tracking activate karna — ya kam se kam ek hamesha chahiye?
4. Koi endpoint hai jo **activation readiness** report kare, ya agent ko individual checks se ye khud assemble karna hai?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"Order hatana chhoti baat nahi?"* | Nahi, **bilkul nahi.** Ye flow ki shape badal deta hai. Chaar sequential steps teen parallel branches + ek join node ban gaye. Aur wo join node ek naya schema aur nayi logic maangta hai. |
| *"Join node kyun chahiye?"* | Kyunki order hatane se koi guarantee nahi bachi ki sab kuch complete hai. Pehle order hi guarantee tha. Ab explicit checklist chahiye — warna adhoora campaign activate ho jaayega aur paise kharch honge. |
| *"Numbering kyun nahi badli?"* | Taaki Confluence par comments apni jagah anchored rahein. Wajahat ne specifically kaha ki structure same rahe. Parallelism note me aur state machine me record hai. |
| *"Checklist evaluate ho sakti hai?"* | 🔴 **Poori nahi.** "Har channel ne approve kiya" ke liye per-channel statuses API se readable hone chahiye — aur maine verify kiya ki creative object me channel dimension hi nahi hai. To wo ek prerequisite abhi check nahi ho sakta. |
| *"Platform par activation kaise hoti hai?"* | 🔴 Maine dekha ki created strategy `Paused` / `Inactive` me land karti hai aur background me Amazon se sync hoti hai. Aur sync **fail ho sakta hai** — list me kai strategies par `failure_reason: "CAMPAIGN_SYNC_ISSUES"` hai. To creation ka matlab Amazon par exist karna nahi hai. |

---

## COMMENT 28 — Strategy creation ke baad update ho sakti hai

**Kahan:** Step 11, `"Confirm with client"` par (jo ek unresolved question ka note tha)

**David ne kaha:** *"no they can be updated on the strategy after creation"*

**Pehle kya tha:** Document me ek open question tha jo do baar aaya (Step 1 par aur Step 11 par): `product_location` aur `asin_numbers` Step 8 ke create payload me required hain, par Step 11 me collect hote hain — creation ke **baad**. Note kehta tha *"Confirm with client"*.

**David kya keh rahe hain:** *Ye problem nahi hai. Strategy creation ke baad update ho sakti hai.*

**Maqsad:** Ek assumption theek karna jisne ek jhoothi problem paida ki thi. Document creation ko **point of no return** maan raha tha.

**🔴 Maine kya samjha (ye bolna hai):**

> "Document creation ko point of no return maan raha tha, isi wajah se ASINs ki timing problem lag rahi thi. **Wo problem nahi hai.** Strategy jo pata hai uske saath create hoti hai, aur baaki baad me attach hota hai `PATCH /api/strategies/{id}/` se — staging API me confirmed, model `StrategyUpdate`.
>
> Ye wo question **band kar deta hai** jo document me **do baar** aaya tha.
>
> **🔴 Aur ye wahi cheez hai jo Comment 27 ko kaam karne deti hai.** Creative, tracking aur credit branches se order hatana **sirf tab** sense banata hai jab wo branches **already exist karti hui strategy me wapas likh sakti hain**. Agar strategy creation par fix ho jaati, to sab kuch pehle collect karna padta aur sequence **tod hi nahi sakte the**.
>
> **To do comments ek hi change ke do side hain:** *no order necessary* wo **behaviour** hai, *updatable after creation* wo **mechanism** hai jo usko permit karta hai.
>
> **🔴 Par kya freely updatable NAHI hona chahiye.** Jawab measurement fields ke baare me tha, aur ise 'kuch bhi badal sakta hai' nahi padhna chahiye. **Kuch fields me paise hain:**
>
> | Safely updatable | Guardrail chahiye |
> |---|---|
> | `product_asins`, `product_location` | `market_budgets` — guaranteed deal already poora budget owe karti hai |
> | Ad tag, conversions | `selected_deals` — deal book ho chuki hai |
> | Creatives | `flight_dates` — booking se bandhi hui hain |
> | Targeting, frequency cap | `markets` — poora plan invalid ho jaayega |
>
> **Is farak ke bina koi ek din us strategy par budget PATCH kar dega jiski Programmatic Guaranteed deal ne wo budget already commit kar rakha hai** — aur plan aur commitment disagree karenge."

**Real example:**
```
Creation:
   POST /api/simple-strategies/
   {
     "product_location": "SOLD_ON_AMAZON",   ← advertiser se (Comment 16)
     "product_asins": [],                     ← khaali
     "market_budgets": [{"market": "GB", "budget": 10000}],
     ...
   }
   → 201 { id: "VMA2026368" }

Baad me — SAFE update:
   PATCH /api/strategies/VMA2026368/
   { "product_asins": ["B08N5WRWNW"] }
   → ✅ theek hai. Measurement field hai, paise se lena-dena nahi.

Baad me — KHATARNAK update:
   PATCH /api/strategies/VMA2026368/
   { "market_budgets": [{"market": "GB", "budget": 5000}] }
   
   → 🔴 Agar us strategy me Programmatic Guaranteed deal hai:
        Deal ne £10,000 pe 500,000 impressions commit kiye
        Aap budget £5,000 kar rahe ho
        → Deal phir bhi £10,000 owe karti hai
        → Plan kehta hai £5,000, commitment kehta hai £10,000
        → Ye disagreement kabhi resolve nahi hoga
        
   → Isliye GUARDRAIL chahiye: budget change karne se pehle check karo
     ki koi PG deal hai ya nahi. Agar hai to warn karo ya rok do.
```

**Kya change kiya (v3.0):**
- Timing ka question **RESOLVED** mark kiya (dono jagah)
- `PATCH /api/strategies/{id}/` API catalogue me add hua
- **Safely updatable vs needs-guardrail** ki table add hui
- Comment 27 se connection banaya (mechanism vs behaviour)
- 4 open questions

**Mai unse puch sakta hoon:**
1. 🔴 **Kaunsi fields creation ke baad updatable honi chahiye aur kaunsi fixed?** Upar ki table ek **proposal** hai, confirmation nahi. Budget aur deals wo hain jo matter karte hain
2. "After creation" ka matlab **after activation** bhi hai? Live campaign ek alag case hai us se jo create ho chuki par launch nahi hui
3. Update kuch **re-run** karta hai — validation, ya reach forecast? Agar PATCH targeting badal de, to jo forecast trader ko dikhaya tha wo ab apply nahi hota, aur agent ko ye **bolna** chahiye
4. `PATCH /api/strategies/{id}/` sahi route hai us strategy ke liye jo `simple-strategies` se bani ho, jabki `simple-strategies` khud POST-only hai?

**Wo mujhse puch sakte hain:**

| Sawaal | Jawab |
|---|---|
| *"To sab kuch badal sakte hain?"* | 🔴 **Nahi.** Measurement fields safe hain (ASINs, ad tag, conversions, targeting). Par budget, deals, flight dates aur markets me **paise** hain. Un par guardrail chahiye. |
| *"Guardrail kyun?"* | Programmatic Guaranteed deal poora budget commit karti hai. Uske baad budget PATCH karna plan aur commitment ko disagree kara dega. |
| *"Ye Comment 27 se kaise juda hai?"* | Ye uska **mechanism** hai. Comment 27 kehta hai order nahi chahiye. Wo sirf tab possible hai jab branches existing strategy me wapas likh sakein. Do comments ek change ke do side hain. |
| *"Platform par PATCH hota hai?"* | ✅ Endpoint Swagger me hai (`StrategyUpdate`). Aur maine platform par dekha ki Planner me budget aur bid **editable** hain creation ke baad — to update practically hota hai. |
| *"Timing question kya tha?"* | `product_location` aur `asin_numbers` Step 8 ke payload me required the par Step 11 me collect ho rahe the. Ab solved: product_location advertiser se aata hai (Comment 16), ASINs empty jaate hain aur PATCH se attach hote hain (Comment 17 + 28). |

---
---

# PART D — Saat Bade Themes

28 comments alag-alag lagte hain, par asal me **saat ideas** baar-baar aate hain. Ye samajh gaye to koi bhi comment explain kar sakte ho — aur ye batane par team ko lagega ki aapne poora document samjha hai, sirf comments nahi.

## Theme 1 — Form nahi, conversation hai

**Kaunse comments:** 6, 7, 9, 13, 14, 15, 16, 17, 18, 21, 22 — **gyarah comments!**

**Idea:** Document ne UI wizard ko chat me copy kar diya tha. David har jagah wahi baat kah rahe hain — **trader se ye pucho hi mat.**

```
Poocho     →  market, budget, dates  (aur wo bhi brief me na ho to)
Generate   →  strategy name
Derive     →  currency
Advertiser →  frequency cap, product category, selling location, device type
Fixed      →  format, goal
Match      →  deals
Default    →  location
```

**Agent ka faayda form ko chat me badalna nahi hai. Faayda form ki zaroorat khatm karna hai.**

## Theme 2 — Requirement aur Source do alag cheezein hain

**Kaunse comments:** 6, 7, 9, 21

**Idea:** Ek field **required** ho sakti hai aur phir bhi trader se **kabhi na puchi jaaye**.

```
Requirement  =  plan ko value chahiye?
Source       =  wo value kahan se aayegi?
```

Aur `Optional` ke bhi do matlab hain:
```
Optional + GENERATED  →  "value hogi, par tumse nahi maangenge"
Optional + DERIVED    →  "value hogi, calculate ho jaayegi"
Optional (Location)   →  "chhune ki zaroorat nahi, default bhara hua hai"
```

Ye **kabhi** ka matlab "khaali reh jaayega" nahi hai.

## Theme 3 — Advertiser-level settings (naya concept)

**Kaunse comments:** 13 (introduce), 15, 16, 22 (instances)

**Idea:** Kuch settings advertiser ki hoti hain, campaign ki nahi. Wo brief se brief nahi badalti.

```
Ab tak mile:  frequency cap, product categories, selling location,
              device type, (aur shayad budget cap)
              
Kab load:     session ke SHURU me, brief parse karne se PEHLE
Endpoint:     GET /api/admin/advertiser/{id}/
```

**Aur sabse zaroori — `is_locked`:**
```python
class AdvertiserSetting(BaseModel):
    value: Any
    is_locked: bool = False      # brand policy — override nahi ho sakti
    reason: Optional[str] = None
```

Bina iske agent **starting point** aur **rule** me farak nahi kar sakta, aur locked policy relax karne ki offer kar dega.

## Theme 4 — Ek jaisi galti ek jagah kabhi nahi hoti

**Kaunse comments:** 1 & 19 (same galti), 16 & 17 & 28 (same timing question), 24 (ek endpoint galat → 14 corrections)

**Idea:** Jab bhi ek galti mile, poori document me dhundo.

```
Comment 1  §2.3 me "only"          →  Comment 19 Step 4 me wahi "only"
Comment 16 Step 1 me duplicate     →  Comment 17 + 28 ne poora question solve kiya
Comment 24 ek endpoint galat       →  14 rows corrected, 2 endpoints exist hi nahi karte
Comment 11 ek "Table"              →  poore column me widgets hain
Comment 26 hardcoded channels      →  Step 5 me wahi rule pehle se likha tha
```

**Yahi cheez batane par team ko lagega ki aap document samajhte ho.**

## Theme 5 — Design ke faisle se zyada uska ASAR matter karta hai

**Kaunse comments:** 4, 12, 22, 27

**Idea:** Har comment ek field badalta hai. Par **asli baat** wo hai jo us change se aage hoti hai.

```
Comment 4  audiences optional     →  🔴 repair loop ka ek lever gaya
Comment 12 bid nahi hota          →  🔴 repair loop ka doosra lever gaya
Comment 22 CTV-only policy        →  🔴 inventory ghatti hai, CPM badhta hai,
                                       aur repair loop ka teesra lever locked
Comment 27 order nahi             →  🔴 join node + checklist ZAROORI ho gaya
```

**Repair loop ka poora hisaab:**
```
v1.1.0 ke levers:      audience widen  +  bid raise
Comment 12 ke baad:    audience widen  (bid gaya)
Comment 4 ke baad:     kuch nahi bacha, agar audience na chuni ho
Comment 22 ke baad:    device bhi locked ho sakta hai

Bacha: targeting relax, inventory widen, budget/flight badlo

Aur inventory widen karne ki limit: 3P se reach forecast NAHI aata,
to agent verify nahi kar sakta ki fix kaam kiya.

→ Isliye agent ko BOLNA chahiye jab kuch na bache.
```

## Theme 6 — Honesty rule

**Kaunse comments:** 3, 4, 8, 12, 18, 19, 21

**Idea:** Agent ko **saaf bolna** chahiye jab wo kuch verify nahi kar sakta, ya jab uske paas lever na bache.

```
Comment 3  split na kiya      →  "ye blended estimate hai, exact nahi"
Comment 4  audience na chuni  →  "audience widen nahi kar sakta"
Comment 8  multi-market brief →  "brief me do markets hain, ek se shuru karun?"
Comment 12 3P inventory jodi  →  "reach verify nahi kar sakta"
Comment 18 PG deal            →  "poora budget committed, pause nahi hoga"
Comment 19 3P par audience    →  "widen kiya par asar dikha nahi sakta"
Comment 21 geography narrow   →  "reach 280,000 se 3,200 par aa gayi"
```

**Zero-Hallucination principle ka practical roop yahi hai** — invent na karna sirf aadha hai; **jo nahi jaante wo bolna** doosra aadha hai.

## Theme 7 — Schema me data aur code alag rakhо

**Kaunse comments:** 26 (channels), 11 (types), 14 (enum annotate not delete), 23 (alag enum)

**Idea:** Jo cheez badalti rehti hai wo **data** honi chahiye. Jo fixed hai wo **code**.

```
Channels        badalte hain, market-specific hain  →  dict ke KEYS (data)
Approval states fixed hain, logic depend karti hai  →  ENUM (code)

Genres, markets, device types                        →  candidates for config
Targeting types                                      →  Step 5 me rule already likha tha
```

**Aur backward compatibility:**
```
Comment 14  FormatEnum.PRIME_VIDEO  →  ANNOTATE kiya, DELETE nahi
                                        (delete = breaking change)
Comment 23  PlanStatusEnum          →  ALAG enum banaya
                                        (share karne se rework hota)
```

---
---

# PART E — Viva Prep: 35 Sawaal Jo Team Puch Sakti Hai

Ye woh sawaal hain jo koi bhi — Wajahat, Vishal, Basil, ya David khud — puch sakta hai. Har ek ka jawab **do-teen line me**, taaki turant bol sako.

## E1. Foundation ke sawaal (1–10)

**1. "CTV kya hai?"**
> Connected TV — internet se juda TV jispar programmatically ad khareedi jaa sakti hai. Smart TV, Fire Stick, Roku, gaming console. Ad video hota hai, non-skippable, full screen, aur **click nahi ho sakta** — remote se click nahi hota.

**2. "CTV aur Online Video me farak?"**
> Dono video hain. Farak **screen** ka hai — CTV TV par, OLV phone/laptop par. Aur ek twist: **Prime Video dono hai**, kyunki wo TV par bhi chalti hai aur phone par bhi. Isi liye VOW me do alag fields hain — `formats` content batata hai, `device_types` screen batata hai.

**3. "Teen deal types kya hain aur kya farak hai?"**
> **Private Auction** — floor CPM, band auction, bid karna padta hai, koi commitment nahi, pause kar sakte ho.
> **Preferred Deal** — fixed CPM, pehla haq, bid nahi, koi commitment nahi, pause kar sakte ho.
> **Programmatic Guaranteed** — fixed CPM + guaranteed volume, **poora budget owed**, **pause nahi ho sakta**.
> Ek line me: Private Auction sabse flexible, PG sabse committed.

**4. "PG kab choose karenge?"**
> Jab ek **event** miss nahi kar sakte — product launch day, World Cup final, Black Friday. Ya jab client ne exact impressions ka wada kiya ho. Baaki sab cases me Private Auction ya Preferred better hai, kyunki paise phanste nahi.

**5. "VOW par kaunsi deals hain?"**
> 🔴 Maine 83 deals dekhi — **lagbhag saari `PRIVATE_AUCTION` + `FLOOR_RATE`** hain. Netflix ki saari, Freewheel ki saari, aur Prime Video ki bhi kuch. Prime Video me kuch `PREFERRED` + `FIXED_CPM` hain. **Ek bhi PG deal nahi mili**, jabki filter me option hai.

**6. "CPM kya hai?"**
> Cost Per Mille — 1,000 impressions ka daam. `impressions = budget ÷ CPM × 1000`. 1,000 par kyunki ek impression ka daam £0.022 jaisa hota hai, padhna mushkil.

**7. "Effective CPM kya hai aur kyun zaroori hai?"**
> Deal CPM + audience data fee. Agar agent sirf deal CPM se impressions calculate kare to £1.63 ki fee miss ho jaayegi aur wo **7% zyada impressions** batayega — jo galat hoga. Isliye schema kehta hai effective CPM surface karo.

**8. "Reach, frequency, impressions me farak?"**
> Impressions = ad kitni **baar** dikha. Reach = kitne **unique log** ne dekha. Frequency = impressions ÷ reach. Aur VOW me frequency **per week** hai — target 3 ka matlab hafte me 3 baar.

**9. "Reach add kar sakte hain?"**
> **Markets ke across haan** — UK ka banda US me nahi dekhega. **Providers ke across nahi** — wahi banda Prime Video aur Netflix dono par dekh sakta hai, aur cross-platform deduplication nahi hoti. Maine verify kiya: API ka `total_reach` = 233,803 par sum = 203,833. To API ka **zyada** hai.

**10. "Audience fee kaise kaam karti hai?"**
> Teen rules. **Ek** — fee tab lagti hai jab 1P data use ho (Amazon ka ya third-party ka apna). **Do** — compound nahi hoti; ek provider se 1 segment lo ya 30, ek hi £1.63. **Teen** — providers stack hote hain; Amazon + Experian = dono ki fee.

## E2. Document ke sawaal (11–18)

**11. "Ye document kya hai?"**
> VOW ke Strategy Module ko agentic banane ka blueprint. v1.1.0 UI wizard ka copy tha. v2.0 CTV-first hua aur 13 steps banaye. **v2.0 par David ne 28 comments kiye**, aur v3.0 unko address karta hai — structure v2.0 jaisa rakh kar, taaki comments apni jagah anchored rahein.

**12. "13 steps kaunse hain?"**
> 1 Basics, 2 CTV Inventory, 3 Budget Split, 4 Audiences, 5 Targeting, 6 Predict Reach, 7 Finalise Plan, 8 Create Strategy, 9 Upload Creative, 10 Creative Approval, 11 Tracking Setup, 12 Credit Check, 13 Activate.

**13. "Steps me koi order hai?"**
> **1–8 ordered hain** — inventory CPM decide karti hai, CPM impressions, forecast ko targeting chahiye. **Chain hai.** **9–12 parallel branches hain** — creatives, tracking, credit koi doosre ka wait nahi karta. **13 join node hai** jo sab check karta hai. Ye Comment 27 se aaya.

**14. "Teen core principles?"**
> **Zero-Hallucination** — agent kabhi values invent nahi karta, sirf API/DB se verified. **Self-Filling Form** — agent stateful slot-filling engine hai LangGraph par. **API-Driven** — har step ka ek official endpoint hai.

**15. "Source column kyun add kiya?"**
> Kyunki `Requirement` aur `Source` do alag sawaal hain. Requirement = plan ko value chahiye? Source = kahan se aayegi? Purani table me 'Required' padh kar log samajh rahe the 'trader se puchna hai' — **aur yahi galti poore document me thi.** Ye Comment 6 ka core hai.

**16. "Trader se total kitne sawaal puche jaayenge?"**
> Practically **teen** — market, budget, dates. Aur wo bhi brief me likhe hon to zero. Plus ek conditional — KPI target value, sirf jab frequency KPI ho.

**17. "Advertiser-level settings kya hain?"**
> Comment 13 se aaya naya concept. Kuch settings advertiser ki hoti hain, campaign ki nahi — brief se brief nahi badalti. Ab tak: frequency cap, product categories, selling location, device type. Session ke **shuru me** load hoti hain, brief parse karne se **pehle**.

**18. "`is_locked` kyun chahiye?"**
> Kyunki agent ko farak pata hona chahiye ki setting **starting point** hai ya **rule**. Repair loop settings relax karta hai. Locked setting relax karna brand policy todna hai. Comment 22 se aaya — "only want CTV only" rule lagta hai, default nahi.

## E3. Comments ke sawaal (19–30)

**19. "Sabse bada comment kaunsa hai?"**
> **Comment 6** — CTV ke liye simplify karo, baaki imply karo. 28 me se lagbhag 10 uske detail hain. Aur usne poore document me Source column add karaya.

**20. "Sabse gehra comment kaunsa hai?"**
> **Comment 13** — advertiser-level defaults. Kyunki wo ek concept introduce karta hai jo document me **tha hi nahi**, aur teen aur comments (15, 16, 22) uske instances nikle.

**21. "Kaunsa comment sabse zyada structural change laaya?"**
> **Comment 18** (deals matched not selected) aur **Comment 27** (no order). 18 ne ek step ka order ulta kar diya. 27 ne chaar sequential steps ko teen parallel branches + join node bana diya.

**22. "Comment 1 aur 19 ek hi baat hai?"**
> Haan — ek galti do jagah likhi thi. Comment 1 §2.3 ki tier table par, Comment 19 Step 4 ke constraints par. Dono me "only" galat tha. Amazon audiences 3P inventory par bhi chalti hain.

**23. "Comment 27 aur 28 ka rishta?"**
> Ek hi change ke do side. **27 behaviour hai** — koi order zaroori nahi. **28 mechanism hai** — strategy creation ke baad update ho sakti hai. Order hatana sirf tab possible hai jab branches existing strategy me wapas likh sakein.

**24. "Kitne open questions the aur kitne band hue?"**
> **Chaar band hue:** ASIN aur product-location ki timing (do baar aaya tha), audience suggest ka response shape, aur postcode support. **Do khule hain:** created strategy kaunse status me land karti hai, aur per-channel creative approval API se readable hai ya nahi. Plus **22 naye question blocks** add kiye jo team ko answer karne hain.

**25. "Repair loop me kitne levers bache?"**
> v1.1.0 me do the — audience widen, bid raise. **Comment 12** ne bid lever hata diya (CTV me fixed CPM). **Comment 4** ne bataya ki agar audience na chuni ho to wo lever bhi nahi. **Comment 22** ne bataya ki device lever locked ho sakta hai. **Bacha:** targeting relax, inventory widen, budget/flight badlo. Aur inventory widen karne se reach **verify nahi hoti** (3P forecast nahi deta).

**26. "Approval kyun hataya?"**
> Comment 23. Manager approval M1 se nikal gaya. Par jo hataya wo ek field se bada tha — notification, unknown wait, rejection route, threshold rule, roles, aur ek LangGraph `interrupt()`. **Step 10 ka interrupt raha** kyunki wahan Amazon ka wait hai, jo asal me external hai.

**27. "Channels dictionary kyun banaye?"**
> Comment 26. Publisher ke naam **data** hain, schema fields nahi. Hardcode karne se Paramount+ add karna poora release maangega. Aur "Channel 4" ka example dikhata hai ki list **market-specific** bhi hai — UK me ITVX/Channel 4, US me Hulu/Peacock. **Keys data hain, values enum.**

**28. "`provider` se `channel` kyun rename kiya?"**
> Client ka shabd "channel" hai, aur ek concept ke teen naam ho gaye the. **Par audience context me `provider` raha** — wahan matlab **data provider** hai (Amazon vs Experian). Channel = kaun ad dikha raha hai. Data provider = kiska data khareed rahe ho. Do alag cheezein.

**29. "Endpoint check me kya mila?"**
> Comment 24. David ne ek endpoint galat bataya, to maine **poori list** staging Swagger ke against padhi. **Do endpoints exist hi nahi karte** — `rate-cards/match` aur `advertisers/{id}/defaults`. Do jinke baare me pata nahi tha wo hain — postcode validation aur fees. Ek update endpoint jo listed nahi tha wo hai — PATCH. **Total 14 corrections.**

**30. "`bundles` ka kya hua?"**
> Comment 20. Document maan raha tha ki suggest endpoint teen ready-made groups deta hai. Nahi deta — **flat list** deta hai. To grouping ka logic **humein** likhna padega. Aur isse teen profiles ka matlab badal gaya — wo API feature nahi, ek flat list ko teen breadth levels par present karne ka tareeka hain.

## E4. Platform reality ke sawaal (31–35)

Ye woh sawaal hain jahan **maine platform par verify kiya** aur schema se disagreement mila. Ye batane par team ko lagega ki aapne sirf document nahi padha, **product bhi dekha**.

**31. "Kya schema ki koi baat platform par galat nikli?"**
> 🔴 Haan, kai. Sabse zaroori:

| Schema kehta hai | Platform par reality |
|---|---|
| Targeting Step 5 hai, creation se pehle | 🔴 Saare targeting endpoints ko **strategy ID chahiye** — creation ke **baad** hoti hai |
| Budget split agent ka kaam hai | 🔴 Platform **khud 50/50 split** karta hai per format, aur Planner me editable hai |
| Currency market se derive hoti hai | 🔴 **Advertiser default se** aati hai. Maine `NOK` currency wali `US` market strategy dekhi |
| `formats = ["streaming_tv"]` constant safe hai | 🔴 Forecast me `prime_video` **alag supply line** deta hai — 71,120 reach kho jaata |
| Forecast audiences/targeting par depend karta hai | 🔴 Forecast sirf **char inputs** leta hai: dates, formats, goal, market_budgets |
| Deal me `inventory_tier` aur `channel` hai | 🔴 **Dono field exist hi nahi karti** |
| Creative approval per channel | 🔴 Granularity **creative × market** hai |
| Ek flight date range | 🔴 Platform **kai flight ranges** support karta hai |

**32. "Repair loop platform par exist karta hai?"**
> 🔴 **Nahi.** Audience-aware forecast endpoints **exist karte hain** (`POST /api/audience-sets/reach-forecast/`, `POST /api/strategies/{id}/audiences/reach-forecast/`) — par **product me koi unhe call hi nahi karta.** Jo ek forecast chalta hai wo Summary par hai, aur wo audiences nahi leta. To repair loop ek **nayi capability** hai, VOW ka description nahi.

**33. "Deal matching buildable hai?"**
> 🔴 **Abhi nahi.** `genre` field polluted hai — usme `2026`, `TEST`, `15, 20, 30` values hain, aur Netflix ke genres `null` hain. `inventory_tier` field **exist nahi karti**. `channel` field **exist nahi karti**. "Amazon Audience Enabled" sirf **deal ke naam** me hai. To ye **client se data-quality request** maangta hai.

**34. "Client se kya maangna hai?"**
> Teen data-quality requests:
> 1. `genre` field properly populate karo — abhi usme saal aur ad lengths hain
> 2. "Amazon Audience Enabled" ko ek **boolean field** banao, deal ke naam me na rakho
> 3. `inventory_tier` ka koi **source** do — teen-tier fork ka data source nahi hai

**35. "Agent ke liye kaunsa create endpoint use karenge?"**
> 🔴 **Ye open question hai.** Teen exist karte hain — `strategies`, `simple-strategies`, `automated-strategies`. David ne `simple-strategies` kaha. Par maine dekha ki **manual wizard `POST /api/strategies/` use karta hai**, `simple-strategies` nahi. Aur `automated-strategies` ka naam agent ke liye sabse fit lagta hai. Ye poochna hai.

---
---

# PART F — Jo Sawaal Humein Puchne Hain

Ye poori list hai, priority ke hisab se. Har ek ke saath likha hai **kyun** zaroori hai — kyunki "kyun" bina sawaal poochna time waste karta hai.

## F1. 🔴 BLOCKING — inke bina kaam aage nahi badh sakta

| # | Sawaal | Kyun blocking hai |
|---|---|---|
| 1 | **Deal ki built-in targeting structured fields me hai ya sirf deal ke naam me?** | Agar sirf naam me hai to agent ko string parse karni padegi — **Zero-Hallucination principle ke khilaf**. Ye ek jawab tay karega ki Step 2 build ho sakta hai ya nahi. **Aur maine verify kiya ki abhi structured nahi hai** |
| 2 | **`POST /api/audience-sets/suggest/` ka ek real response sample mil sakta hai?** | Grouping rule, fee handling aur poora audience schema iski shape par depend karte hain. Audience ka kaam unblock karne ke liye sabse kaam ki cheez |
| 3 | **Agent ke liye kaunsa create endpoint — `strategies`, `simple-strategies`, ya `automated-strategies`?** | Teeno exist karte hain. Payload teeno ka alag ho sakta hai. Aur `is_automated` field pehle se hai jo teesre par ishaara karta hai |
| 4 | **`SimpleStrategyCreate` ki poori field list?** | Jo payload document me describe hua hai usko **field-by-field match** karna hai. Endpoint listing se wo nahi dikhta |
| 5 | **Advertiser par kitni settings hoti hain — poori list?** | Abhi pata karne se section ek baar banega, warna har comment me ek nayi field aayegi. Ab tak: frequency cap, product categories, selling location, device type, budget cap |
| 6 | **In me se kaunsi LOCKED brand policies hain?** | Isse tay hoga ki repair loop kya badal sakta hai. **Ye ek jawab hai jo wording ke bajaye agent ka behaviour badalta hai** |

## F2. 🟠 DATA QUALITY — client se request

| # | Request | Kyun |
|---|---|---|
| 7 | **`genre` field properly populate karo** | Abhi usme `2026`, `2027`, `TEST`, `15, 20, 30` values hain, aur Netflix deals ke genres `null` hain jabki naam me genre likha hai. **Genre par matching build nahi ho sakti** |
| 8 | **"Amazon Audience Enabled" ko boolean field banao** | Abhi wo sirf deal ke **naam** me hai. Comment 1 ka `targeting_source` reliably set nahi ho sakta |
| 9 | **`inventory_tier` ka source do** | Deal par ye field **exist hi nahi karti**. Teen-tier fork ka koi data source nahi |
| 10 | **Third-party deals ka metadata kyun khaali hai?** | Netflix deals me `devices: []`, `environments: []`, `media_types: []`, aur location volume `1`. Amazon deals me poora data hai. **3P par matching aur volume check possible nahi** |
| 11 | **Ek deal `$0.00` CPM par hai** (`VowMade_Fifa 2026_ZA`) | `budget ÷ CPM` division by zero. Data error hai ya intentional? |

## F3. 🟡 DESIGN — decide karna hai

| # | Sawaal | Kyun |
|---|---|---|
| 12 | M1 me **ek market per strategy** acceptable hai? | Isse budget split, currency rule, per-market deal matching sab affect hote hain |
| 13 | Multi-market me currency — total advertiser ki primary me aur per-market spend uski apni me? | Ya poora plan ek currency me? |
| 14 | KPI target value forecast aur repair loop ko feed kare, ya sirf reporting ke liye? | Dono se agent ka behaviour bilkul alag hoga |
| 15 | Frequency KPI hai par target nahi diya — agent 3 assume kare ya khaali chhode? | Target ke bina repair loop trigger nahi hoga |
| 16 | **Reach** KPI ke liye bhi koi target hota hai? | Ya sirf frequency me number aata hai |
| 17 | Kaunsa budget split method default — `EVEN_BY_BUDGET` ya `EVEN_BY_IMPRESSIONS`? | Agent ko ek default chunna padega |
| 18 | Kai deals match hui to agent kaise chune — sasta CPM, genre fit, ya zyada reach? | Matching logic ka core |
| 19 | Kuch match na hua to kya kare — duration widen, genre drop, ya puche? | Failure path |
| 20 | PG deal **automatically match** honi chahiye? | Budget commitment ko dekhte hue |
| 21 | Kaunsi fields creation ke baad updatable, kaunsi fixed? | Budget aur deals me paise hain. Guardrail chahiye |
| 22 | "After creation" ka matlab "after activation" bhi hai? | Live campaign alag case hai |
| 23 | Grouping cumulative reach par ya relevance score par? | Audience profiles ka basis |
| 24 | `SuggestAudienceGroupsInput` — "groups" ka matlab caller groups maang sakta hai? | Agar haan to agent ka grouping logic hi nahi chahiye |
| 25 | Content-category exclusions advertiser ki brand-safety settings se default hon? | Maine assume kiya hai, confirm nahi hua |
| 26 | Trader ko dikhaya jaaye ki agent ne kya infer kiya, ya sirf doubtful cheezein? | Pehla safe hai, doosra chhota |

## F4. 🟢 CLARIFICATION — jaanna achha hoga

| # | Sawaal |
|---|---|
| 27 | Private auction me **floor CPM** hai — wahan bid matter karta hai? Agar haan to Comment 12 ka jawab narrow hoga |
| 28 | `MarketBudgetBidSchema.base_bid` required hai. Kya bhejein — deal CPM, null, ya endpoint drop kar deta hai? |
| 29 | Advertiser par jo hai wo **product category** hai ya **industry**? Do alag taxonomies hain, mapping chahiye hogi |
| 30 | Ek advertiser ke campaigns me alag-alag selling location ho sakti hai? |
| 31 | `CurrencyEnum` me sirf EUR/GBP/USD hain — baaki markets ka kya? |
| 32 | Trader currency override kar sakta hai? |
| 33 | Traders ka koi **naming convention** already hai strategies ke liye? |
| 34 | Amazon audiences aur SSP targeting **ek hi deal** par saath chal sakti hain? |
| 35 | Amazon ki targeting 3P par kitni limited hai — sirf device, ya demographic bhi? |
| 36 | Suggest endpoint async hai — kitna time leta hai? |
| 37 | Finalised plan wapas `DRAFT` ho sakta hai? |
| 38 | Plan status change **kaunsa endpoint** record karta hai? |
| 39 | Advertiser-level **approval threshold** plan karna chahiye? |
| 40 | Channel list kahan se — `get_channels_choices/` ya matched deals se derive? |
| 41 | Approval **per channel** hai ya **per creative-and-channel** pair? |
| 42 | Click-through URL **per market** hota hai? (`MarketWithClickthroughUrl` model hai) |
| 43 | CTV creatives me **QR codes** allowed hain? Koi spec hai? |
| 44 | Prerequisite list poori hai, ya kuch aur bhi chahiye activation se pehle? |
| 45 | **Credit check** asal me order-free hai? Uska outcome budget badal sakta hai |
| 46 | Conversions poori tarah **skip** ho sakti hain? |
| 47 | Koi endpoint hai jo **activation readiness** report kare? |
| 48 | ASIN list **ek call me** validate karein ya paste karte waqt? |
| 49 | `strategies-sp` sponsored products hai aur CTV se irrelevant? |
| 50 | Multiple flight ranges M1 me chahiye? Platform support karta hai |
| 51 | `enable_brand_safety_targeting` default **OFF** hai — ON hona chahiye? Trader ko pata bhi nahi chalta |
| 52 | Amazon sync fail hua ya nahi — kaise pata karein? Webhook hai ya poll karna padega? |

---
---

# QUICK REVISION CARD

**Print karke rakh lo. Ek page me sab.**

## 28 comments — ek line me har ek

```
 1  3P targeting Amazon YA SSP se — per deal choice, tier se nahi
 2  Audience fee provider se, profile se nahi. Compound nahi hoti. Providers stack hote hain
 3  Budget split OPTIONAL. Preferred kyunki CPM alag hote hain
 4  Audiences OPTIONAL. Decline kar sakte hain — run of service, koi fee nahi
 5  Audiences targeting ka hissa. Targeting PRE-FILLED aati hai. Geography audience ki jagah le sakti hai
 6  🔴 CTV ke liye kaato, baaki IMPLY karo. Trader se sirf market/budget/dates
 7  Naam GENERATE karo. {Category}_{Market}_{Goal}_{MonthYear}
 8  M1 me EK market. Field list rahe. Reach markets ke across add hoti hai, providers ke across nahi
 9  Currency market se DERIVE. (Par platform par advertiser se aati hai!)
10  Frequency KPI ke saath TARGET VALUE 2-5. Ye forecast BADAL deta hai
11  "Table" widget hai, data type nahi. Poore column me widgets hain
12  CTV me bid nahi. 🔴 Repair loop ka lever gaya. (Par Private Auction me floor hai!)
13  🔴 ADVERTISER-LEVEL SETTINGS — naya concept. is_locked chahiye
14  Format hamesha streaming_tv. Prime Video CHANNEL hai. (Par forecast me matter karta hai!)
15  Product categories advertiser se ya brief se. "for video" hata do
16  Selling location Step 1 se HATAO — tracking me already hai
17  ASINs baad me aate hain. Empty create karo, PATCH karo
18  🔴 Deals MATCH hoti hain, select nahi. Par tier capability aur PG commitment BOLNA hai
19  Amazon audiences 3P par bhi chalti hain. Cost ka ganit badal jaata hai
20  bundles.narrow/balanced/broad EXIST NAHI KARTA. Flat list milti hai, grouping hamari
21  Location market ke country se DEFAULT. markets ≠ location. Narrow karne se reach ghatti hai
22  🔴 Device advertiser ki setting. streaming_tv ka matlab TV screen NAHI
23  Approval ek STATUS CHANGE. Manager gaya, interrupt gaya. Step 10 ka interrupt raha
24  simple-strategies use karo. 🔴 14 endpoint corrections. 2 endpoints exist nahi karte
25  Click-through URL OPTIONAL — TV par click nahi hota. Mobile ho to recommended
26  Per channel EK status. Keys DATA, values ENUM. provider → channel rename
27  🔴 KOI ORDER NAHI — 3 parallel branches. Isliye JOIN NODE + CHECKLIST chahiye
28  Strategy creation ke BAAD update ho sakti hai. Par budget/deals par guardrail
```

## 7 themes

```
1  Form nahi, conversation hai            → 11 comments
2  Requirement ≠ Source                   → 4 comments
3  Advertiser-level settings (naya)       → 4 comments
4  Ek galti kabhi akeli nahi hoti         → 5 comments
5  Faisle se zyada uska ASAR matter karta → 4 comments
6  Honesty rule                            → 7 comments
7  Data aur code alag rakho                → 4 comments
```

## 3 deal types

```
PRIVATE AUCTION   floor CPM   bid ✅   commitment ❌   pause ✅   ← VOW pe lagbhag saari
PREFERRED DEAL    fixed CPM   bid ❌   commitment ❌   pause ✅   ← Prime Video pe kuch
PROG. GUARANTEED  fixed CPM   bid ❌   commitment 🔴   pause 🔴   ← ek bhi nahi mili
```

Hotel ke kamron se:
```
PRIVATE AUCTION   "8 agents bulaye, min Rs 4,000, aapas me compete karo"
                  → sasta mil sakta hai, par mile hi — pakka nahi

PREFERRED DEAL    "Purane agent ko Rs 5,000 fix, pehla haq, majboori nahi"
                  → daam pakka, par kitne kamre milenge pakka nahi

PROG. GUARANTEED  "Contract: 50 kamre, Rs 2.5 lakh, dono bandhe"
                  → sab pakka, par paise wapas nahi
```

## Floor vs Fixed vs Bid

```
FIXED  =  jo number DIKHA, wahi PAY karoge        → bid ki zaroorat NAHI
FLOOR  =  jo number DIKHA, usse UPAR jaana hai    → bid CHAHIYE

BID    =  per 1,000 impressions ka MAXIMUM rate
          Trader EK BAAR set karta hai, per market
          DSP har auction me uske ANDAR rehte hue KHUD decide karta hai
          Bid ≠ Budget  (bid = rate ka ceiling, budget = total paise)
          Bid < floor → campaign chalega hi NAHI
```

## Formulas

```
impressions    = budget ÷ effective CPM × 1000
frequency      = impressions ÷ reach                    (PER WEEK!)
reach needed   = impressions ÷ target frequency
effective CPM  = deal CPM + audience VCPM fee
eCPM           = spend ÷ impressions × 1000
```

## 5 numbers yaad rakho

```
28   comments
13   steps (1-8 ordered, 9-12 parallel, 13 join)
 3   sawaal trader se (market, budget, dates)
 4   open questions band hue, 2 khule, 22 naye
14   endpoint corrections
```

---

**Ye document `strategy_schema_documentation_v3.md` ke 28 review notes se bana hai, aur platform par 4 August 2026 ko ki gayi verification se cross-checked hai (`vow_manual_flow_analysis.md` — 177 findings).**

**Jahan schema aur platform disagree karte hain, wo 🔴 se mark hai. Wo disagreements sirf documentation nahi hain — wo implementation se pehle resolve karne wale items hain.**
