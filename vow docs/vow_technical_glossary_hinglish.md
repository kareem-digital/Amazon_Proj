# VOW Platform - Advertising & Technical Terms Glossary (Hinglish Guide for Beginners)

**Document Name:** `vow_technical_glossary_hinglish.md`  
**Purpose:** Beginner-friendly Hinglish dictionary explaining all programmatic advertising & VOW platform technical terms with real-world daily life examples.  
**Target Audience:** New Team Members, QA Testers, Junior Developers, Non-Marketing Engineers.  

---

## 📌 Introduction (Yeh Document Kyun Banaya Gaya Hai?)

VOW Advertising Platform aur Strategy Module me bohot saare **Digital Advertising & Programmatic Terms** (jaise *Amazon DSP, CTV, ASIN, CPM, ROAS, DPV, VCR, ROS*) use hote hain.

Agar aap Advertising domain me naye hain, to ye terms confuse kar sakti hain. Is document me **har single technical term** ko **sabse aasan Hinglish** me, **Real-Life Examples** (jaise Zomato, Swiggy, Smart TV, Aadhaar Card) ke sath samjhaya gaya hai.

---

## 📚 Table of Contents (Kon-Kon Se Words Cover Hue Hain?)

1. [Platform & Channel Terms](#1-platform--channel-terms)
   - Amazon DSP (Demand-Side Platform)
   - CTV (Connected TV) & Streaming TV
   - SSP (Supply-Side Platform)
2. **Attribution & Product Terms**
   - ASIN (Amazon Standard Identification Number)
   - Endemic vs Non-Endemic Advertisers
3. **Pricing & Bidding Metrics**
   - CPM (Cost Per Mille)
   - eCPM / Effective CPM & Blended CPM
   - VCPM Data Fee (Variable Cost Per Mille)
   - Base Bid
4. **Targeting & Delivery Metrics**
   - ROS (Run-of-Service / Run-of-Site)
   - Frequency & Frequency Cap
   - 1P Data vs 3P Data (First-Party vs Third-Party)
5. **Performance & Engagement Metrics**
   - CTR (Click-Through Rate)
   - DPV & DPVR (Detail Page View & Rate)
   - Off-Amazon CPA (Cost Per Acquisition)
   - ROAS (Return on Ad Spend)
   - VCR (Video Completion Rate)
   - VR (Viewability Rate)
6. **Deal Types**
   - PG (Programmatic Guaranteed) vs Preferred Deals

---

## 1. Platform & Channel Terms

### 🔹 1. Amazon DSP (Demand-Side Platform)
- **Simple Definition:** Amazon DSP ek software portal hai jahan advertisers automatically (programmatically) video aur display ads khareedte hain aur target karte hain.
- **Real-Life Example:** Jaise aap Swiggy ya Zomato app se alag-alag restaurants se food order karte hain bina unhe call kiye, waise hi advertiser Amazon DSP software se ek hi jagah baith kar Prime Video, Netflix, Twitch, aur Web Portals par ads buy kar sakta hai.

---

### 🔹 2. CTV (Connected TV) & Streaming TV
- **Simple Definition:** Internet se judi hui Smart TVs (Samsung Smart TV, LG WebOS, Fire TV Stick, Apple TV) jin par streaming apps (Prime Video, Netflix, Disney+, YouTube) chalti hain.
- **Real-Life Example:** Aapke ghar ka Smart TV jo Cable/Dish TV par nahi, balki Home Wi-Fi Internet par chalta hai. Jab aap Prime Video par movie dekhte hain aur beech me 15-second ka ad aata hai, use **CTV Ad** ya **Streaming TV Ad** kehte hain.

---

### 🔹 3. SSP (Supply-Side Platform)
- **Simple Definition:** Publishers (jaise Netflix, Disney+, Channel 4) ka software jiske zariye wo apne TV shows ke beech bachi hui ad spaces ko advertisers ko bechte hain.
- **Real-Life Example:** Jaise MakeMyTrip / Airbnb par hotel owners apne khali rooms list karke sell karte hain, waise hi TV publishers apni ad spaces SSP ke zariye DSP ko sell karte hain.

---

## 2. Attribution & Product Terms

### 🔹 4. ASIN (Amazon Standard Identification Number)
- **Simple Definition:** Amazon Catalog ka 10-character ka unique ID (jaise `B08N5WRWNW`) jo Amazon par bikne wale har single product ko diya jata hai.
- **Real-Life Example:** Jaise Har Insaan ka **Aadhaar Number** ya **Passport Number** Unique hota hai, waise hi Amazon Marketplace par "Sony Wireless Headphones" ya "Nike Shoes" ka ek Unique 10-digit ASIN number hota hai.

---

### 🔹 5. Endemic vs Non-Endemic Advertisers
- **Simple Definition:** 
  - **Endemic Advertiser:** Jo brands apne products Amazon website par direct bechte hain (e.g., Samsung, Anker, Philips).
  - **Non-Endemic Advertiser:** Jo brands Amazon par products nahi bechte, balki apni external website/app par traffic chahte hain (e.g., Oxford University, BMW, Banks, Insurance companies).
- **Real-Life Example:** Amazon par Samsung Mobile ka ad aana = Endemic. Amazon Prime Video par BMW Car ya HDFC Bank Loan ka ad aana = Non-Endemic.

---

## 3. Pricing & Bidding Metrics

### 🔹 6. CPM (Cost Per Mille / Cost Per Thousand Impressions)
- **Simple Definition:** 1,000 Ad Impressions (dikhayi dene wale ads) ki price. Latin language me "Mille" ka matlab 1,000 hota hai.
- **Real-Life Example:** Agar CPM = **£20.00** hai, iska matlab hai ki agar aapka ad **1,000 logon ke TV par dikha**, to aapko total **£20.00** pay karne honge. Agar 10,000 impressions hue to cost £200.00 hogi.

---

### 🔹 7. eCPM (Effective CPM) & Blended CPM
- **Simple Definition:** Campaign me sabhi heterogeneous deals, base bids, aur extra audience data fees (VCPM) ko milakar 1,000 impressions ka final Average Cost.
- **Real-Life Example:** Jaise aapne 1 Pizza £10.00 ka khareeda aur 1 Burger £5.00 ka khareeda (Total £15.00 for 2 items = Average £7.50 per item). Waise hi agar Prime Video Deal £28.88 CPM hai aur Netflix Deal £22.00 CPM hai, to unka combined average rate = **Blended eCPM**.

---

### 🔹 8. VCPM Data Fee (Variable Cost Per Mille Data Fee)
- **Simple Definition:** Campaign me Extra Audience Data (jaise Amazon 1P Lifestyle/Interest segments) use karne par lagne wala extra CPM charge jo Base Deal CPM ke upar judta hai.
- **Real-Life Example:** Movie Ticket = **£10.00** (Base Deal CPM), aur Recliner Seat Upgrade = **£2.00** (VCPM Data Fee). Total Ticket Cost = **£12.00** (Effective CPM).

---

### 🔹 9. Base Bid
- **Simple Definition:** Programmatic auctions (bidding) me 1,000 impressions ke liye advertiser ki maximum bid amount. *(Note: CTV Deals me Base Bid omit kar diya jata hai kyunki pricing fixed rate-card CPM se chalti hai).*

---

## 4. Targeting & Delivery Metrics

### 🔹 10. ROS (Run-of-Service / Run-of-Site)
- **Simple Definition:** Jab aap kisi specific show, genre, ya audience ko restrict kiye bina pooray platform (e.g. Poore Prime Video ya Poore Netflix) par ad chalne dete hain.
- **Real-Life Example:** Jaise TV news channel par din me kisi bhi program ke beech ad chal jana, bina kisi specific show ko chuney.

---

### 🔹 11. Frequency & Frequency Cap
- **Simple Definition:** 
  - **Frequency:** Ek single user / TV household ko campaign duration me kitni baar aapka ad dikha.
  - **Frequency Cap:** Limit set karna (jaise Max 3 Impressions in 24 Hours) taaki user ek hi ad baar-baar dekh kar bore na ho.
- **Real-Life Example:** Ek TV viewer ko 24 ghante me Maximum 3 baar hi same brand ka ad dikhana.

---

### 🔹 12. 1P Data vs 3P Data (First-Party vs Third-Party Data)
- **Simple Definition:** 
  - **Amazon 1P Data:** Amazon ka apna authentic shopping & browsing history data (e.g., "Log jo abhi Laptop search kar rahe hain").
  - **3P Data:** External data provider companies (jaise Experian, LiveRamp) ka data.
- **Real-Life Example:** Amazon khud janta hai ki pichle 3 din me kisne TV search kiya (1P Data). Lekin credit card limit ka data kisi bahar ki agency se milta hai (3P Data).

---

## 5. Performance & Engagement Metrics

### 🔹 13. CTR (Click-Through Rate)
- **Simple Definition:** Ads dekhne wale logon me se kitne % ne ad par **CLICK** kiya.
- **Formula:** $\text{CTR} = \left(\frac{\text{Total Clicks}}{\text{Total Impressions}}\right) \times 100$
- **Real-Life Example:** Agar 1,000 logon ne mobile screen par ad dekha aur 10 logon ne click karke website kholi, to **CTR = 1.0%**.

---

### 🔹 14. DPV & DPVR (Detail Page View & Detail Page View Rate)
- **Simple Definition:** 
  - **DPV (Detail Page View):** TV ya Display Ad dekhne ke baad customer ka Amazon par us product ke Main Purchase Page ko open karna.
  - **DPVR:** Total ad dekhne wale logon me se kitne % ne Amazon Detail Page visit kiya.
- **Real-Life Example:** Aapne Smart TV par Nike shoes ka ad dekha. Shaam ko aapne Amazon app khol kar us Nike shoe ka Detail Page check kiya – system isko **1 DPV** count karega.

---

### 🔹 15. Off-Amazon CPA (Cost Per Acquisition / Cost Per Action)
- **Simple Definition:** Amazon ke bahar kisi brand ki website par **1 Single Customer Action / Lead / Form Fill** haasil karne me aaya cost.
- **Formula:** $\text{CPA} = \frac{\text{Total Ad Spend}}{\text{Total Conversions}}$
- **Real-Life Example:** Ek University (e.g. Oxford) ne £1,000 spend karke website par 10 Admission Forms bharwaye. To **CPA = £100 per Admission Form**.

---

### 🔹 16. ROAS (Return on Ad Spend)
- **Simple Definition:** Ad par spend kiye gaye har £1 / $1 ke badle kitne £ / $ ki product sales hui.
- **Formula:** $\text{ROAS} = \frac{\text{Total Sales Revenue}}{\text{Total Ad Spend}}$
- **Real-Life Example:** Agar aapne ad par **£1,000** spend kiya aur Amazon par **£4,000** ke products bik gaye, to aapka **ROAS = 4.0x** (yani 4 guna return).

---

### 🔹 17. VCR (Video Completion Rate)
- **Simple Definition:** Total video ad start karne walon me se kitne % users ne aapka ad **start se leke end tak poora 100% dekha** (bina skip kiye).
- **Real-Life Example:** Agar 100 logon ke TV par 15-second ad play hua aur 90 logon ne end tak 15 sec dekha, to **VCR = 90%**.

---

### 🔹 18. VR (Viewability Rate)
- **Simple Definition:** Screen par chalne wale ads me se kitne % ads actual me human eye ko dikhayi diye (At least 50% ad pixels for 2 continuous seconds).
- **Real-Life Example:** Webpage scroll karte wqt agar ad screen par aane se pehle hi user ne fast scroll kar diya, to wo Viewable nahi mana jayega. Smart TV ads ki Viewability Rate **95%+** hoti hai.

---

## 6. Programmatic Deal Types

### 🔹 19. Programmatic Guaranteed (PG) vs Preferred Deals
- **Simple Definition:** 
  - **Programmatic Guaranteed (PG):** Reserved inventory room jahan impressions volume aur price dono 100% guaranteed hote hain.
  - **Preferred Deals:** Non-guaranteed volume lekin agreed fixed CPM price.
- **Real-Life Example:** Flight me confirmed seat ticket book kar lena = **PG Deal**. Priority counter ticket lena par seat availability par depend hona = **Preferred Deal**.

---

## 📊 Summary Cheat-Sheet

| Technical Term | Simple Hindi Meaning | Main Use Case |
| :--- | :--- | :--- |
| **Amazon DSP** | Advertising Software Portal | Prime Video, Netflix, Web par ads buy karna |
| **CTV** | Internet Smart TV | TV Screen par video ads run karna |
| **ASIN** | Amazon Product Catalog Unique Code | Amazon products ki tracking & sales monitor karna |
| **CPM** | 1,000 Ad Views ki Cost | Ad campaign ka budget aur pricing calculate karna |
| **eCPM** | Combined Average CPM | Multiple deals aur data fees ka final cost nikalna |
| **DPV / DPVR** | Amazon Product Page Views | Ad dekh kar kitne log product dekhne aaye |
| **ROAS** | Ad Spend Par Profit Return | Total Revenue divided by Total Ad Spend |
| **VCR** | Video Full View % | Kitne logon ne ad start se end tak poora dekha |
| **ROS** | Run-of-Service | Bina show selection ke poore platform par ad chalna |
| **Frequency Cap** | 1 User par Max Ad Limit | User ko ek hi ad baar-baar dikha kar bore na karna |

---

## 📄 Related Project Files
- 📄 **Hinglish Review Guide (28 Comments Breakdown):** [update_schema_registery_hinglish.md](file:///e:/VOW%20Agent/update_schema_registery_hinglish.md)
- 📄 **Main Technical Specification:** [update_strategy_schema_registry.md](file:///e:/VOW%20Agent/update_strategy_schema_registry.md)
- 📄 **Formal Change Audit Registry:** [updated_schema_registry.md](file:///e:/VOW%20Agent/updated_schema_registry.md)
