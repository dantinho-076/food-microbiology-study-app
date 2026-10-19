"""
Food Microbiology (FHM-20306) Master Web Application - Version 4 (Formatted Scientific Notation)
Includes a * 10^q notation inputs and displays for Quantitative Microbiology Calculator.
"""

import streamlit as st
import math

st.set_page_config(
    page_title="Food Microbiology Master Suite (FHM-20306)",
    page_icon="🧫",
    layout="wide"
)

st.title("🧫 Food Microbiology (FHM-20306) Master Study Suite")
st.caption("Complete Unified Exam Preparation Tool: Pathogens, Math, Spoilage, Fermentation, Hygiene & Sampling")

# Sidebar navigation
st.sidebar.header("Navigation")
menu = st.sidebar.radio(
    "Select Module:",
    [
        "🌲 Outbreak Decision Tree",
        "📝 Complete Exam Practice Bank",
        "🧮 Quantitative Math Calculator",
        "🥩 Spoilage & Associations",
        "🧀 Fermentation & Succession",
        "🧼 Hygiene, Biofilms & HACCP",
        "📊 Sampling & Criteria"
    ]
)

# Helper function to format float to a * 10^q string
def format_sci_10q(val):
    if val <= 0:
        return "0"
    exp = int(math.floor(math.log10(val)))
    coeff = val / (10 ** exp)
    if abs(coeff - round(coeff, 2)) < 1e-4:
        coeff = round(coeff, 2)
    if coeff == 1.0:
        return f"10^{exp}"
    return f"{coeff:.2f} × 10^{exp}"

# ---------------------------------------------------------
# MODULE 1: OUTBREAK DECISION TREE
# ---------------------------------------------------------
if menu == "🌲 Outbreak Decision Tree":
    st.header("🌲 Outbreak Decision Tree Diagnoser")
    st.markdown("Trace outbreak symptoms and food parameters to their causative pathogen.")

    col1, col2 = st.columns(2)
    
    with col1:
        symptom = st.selectbox(
            "Primary Symptom:",
            ["Vomiting & Nausea predominant", "Diarrhea & Abdominal Cramps predominant"]
        )
    
    if symptom == "Vomiting & Nausea predominant":
        with col2:
            onset = st.selectbox("Onset Time:", ["Rapid (< 6 hours)", "Slow / Neurotoxin (12-36 hours)"])
        
        if onset == "Rapid (< 6 hours)":
            food = st.radio("Food Vehicle / Risk Factor:", [
                "Rich creamy foods, cooked ham, manual handling",
                "Fried rice, starchy foods, room temp storage"
            ])
            if "manual" in food:
                st.success("### 🦠 Staphylococcus aureus")
                st.markdown("""
                * **Mechanism:** Pre-formed heat-stable enterotoxin (intoxication).
                * **Onset:** 1 - 6 hours (rapid).
                * **Fever:** None.
                * **Key Exam Note:** Associated with human handlers, low $a_w$ foods, and cooked ham with minimal competing flora.
                """)
            else:
                st.success("### 🦠 Bacillus cereus (Emetic Type)")
                st.markdown("""
                * **Mechanism:** Pre-formed heat-stable cereulide toxin (intoxication).
                * **Onset:** 0.5 - 6 hours.
                * **Fever:** None.
                * **Key Exam Note:** Spores survive cooking; toxin forms in boiled/fried rice left at room temperature.
                """)
        else:
            st.error("### 🦠 Clostridium botulinum")
            st.markdown("""
            * **Mechanism:** Pre-formed neurotoxin (intoxication).
            * **Symptoms:** Flaccid paralysis, double vision, respiratory failure.
            * **Key Exam Note:** Anaerobic sporeformer; controlled by 12D cook ($D_{121} = 0.2$ min) or pH < 4.5.
            """)

    else: # Diarrhea
        with col2:
            fever = st.selectbox("Fever & Mechanism:", ["No Fever (Toxico-infection)", "Fever Present (Invasive Infection)"])
        
        if fever == "No Fever (Toxico-infection)":
            vehicle = st.radio("Outbreak Scenario:", [
                "Large pots of meat, gravy, or stew cooled slowly (8-16h onset)",
                "Vanilla sauce or pudding cooled at room temp (8-16h onset)"
            ])
            if "meat" in vehicle:
                st.warning("### 🦠 Clostridium perfringens")
                st.markdown("""
                * **Mechanism:** Toxico-infection (enterotoxin released in intestine during sporulation).
                * **Onset:** 8 - 16 hours.
                * **Key Exam Note:** Anaerobic sporeformer multiplying in center of large batch-cooked meat.
                """)
            else:
                st.warning("### 🦠 Bacillus cereus (Diarrhoeal Type)")
                st.markdown("""
                * **Mechanism:** Toxico-infection (heat-labile enterotoxin produced in intestine).
                * **Onset:** 8 - 16 hours.
                * **Key Exam Note:** Spores survive boiling of desserts/sauces; germinate during slow cooling.
                """)
        else:
            pathogen_sel = st.radio("Invasive Pathogen Profile:", [
                "Salmonella spp. (Poultry, eggs, raw milk; 12-36h onset, invasive diarrhea & fever)",
                "Campylobacter jejuni (Raw chicken, unpasteurized milk; microaerophilic, bloody diarrhea)",
                "STEC / E. coli O157 (Undercooked ground beef; bloody diarrhea & risk of HUS)",
                "Listeria monocytogenes (RTE foods, soft cheese; psychrotrophic, severe mortality in vulnerable groups)"
            ])
            if "Salmonella" in pathogen_sel:
                st.info("""### 🦠 Salmonella spp.
* **Infection:** Ingested cells invade intestinal epithelial cells causing inflammation, diarrhea, and fever.""")
            elif "Campylobacter" in pathogen_sel:
                st.info("""### 🦠 Campylobacter jejuni
* **Infection:** High infection potential, microaerophilic growth (3-5% $O_2$), associated with raw poultry.""")
            elif "STEC" in pathogen_sel:
                st.info("""### 🦠 Shiga toxin-producing E. coli (STEC / O157)
* **Infection:** Low infectious dose, produces Shiga toxin causing hemorrhagic colitis and Hemolytic Uremic Syndrome (HUS).""")
            else:
                st.info("""### 🦠 Listeria monocytogenes
* **Infection:** Psychrotrophic (grows down to 0°C), intracellular pathogen, high mortality in pregnant women, elderly, and immunocompromised.""")

# ---------------------------------------------------------
# MODULE 2: COMPLETE EXAM PRACTICE BANK
# ---------------------------------------------------------
elif menu == "📝 Complete Exam Practice Bank":
    st.header("📝 Complete Exam Practice Question Bank")
    st.markdown("Test yourself on 15 core questions compiled directly from FHM-20306 Test Exams and Lecture Exercises.")

    questions = [
        {
            "q": "1. Vacuum packed, cooled fresh meat spoils mainly due to which group of microorganisms?",
            "opts": ["1) Pseudomonas and Moraxella", "2) Lactobacillus and Leuconostoc", "3) Osmophilic yeasts"],
            "ans": "2) Lactobacillus and Leuconostoc",
            "exp": "Vacuum packaging excludes oxygen, inhibiting strict aerobes like Pseudomonas. Lactic Acid Bacteria (Lactobacillus, Leuconostoc) become the dominant spoilage association."
        },
        {
            "q": "2. The D-value (decimal reduction time) depends on:",
            "opts": ["1) The temperature and the specific micro-organism", "2) The heating time and temperature", "3) The heating time and pH"],
            "ans": "1) The temperature and the specific micro-organism",
            "exp": "D-value is a characteristic property of a specific microorganism at a specific temperature (and substrate conditions)."
        },
        {
            "q": "3. What is the primary advantage of UHT (Ultra High Temperature) treatment compared to traditional canning sterilization?",
            "opts": ["1) Enzymes are completely inactivated", "2) Sensory and nutritional quality remains higher", "3) Complete destruction of all thermophilic bacterial spores"],
            "ans": "2) Sensory and nutritional quality remains higher",
            "exp": "Because high temperatures accelerate microbial inactivation faster than chemical quality degradation (z-value for spores ~10°C vs z-value for vitamins ~30°C), short high-temp processing preserves quality."
        },
        {
            "q": "4. What is the definition of a 'spoilage-association'?",
            "opts": ["1) The specific spoilage flora that develops on a specific product under specific conditions", "2) The sum of intrinsic, extrinsic, and implicit factors", "3) The chemical reactions occurring during rotting"],
            "ans": "1) The specific spoilage flora that develops on a specific product under specific conditions",
            "exp": "A spoilage association is the predominant group of micro-organisms that outcompetes others under the product's specific intrinsic and extrinsic conditions."
        },
        {
            "q": "5. Most non-sporeforming vegetative foodborne pathogens can be safely inactivated by:",
            "opts": ["1) Freezing for 1 week at -20°C", "2) Packaging in a modified atmosphere (65% CO2, 25% N2)", "3) Heating the product to a center temperature of 70°C"],
            "ans": "3) Heating the product to a center temperature of 70°C",
            "exp": "Pasteurization / cooking to a core temperature of 70°C for 2 minutes achieves a 6-log reduction for vegetative pathogens like Salmonella and Listeria."
        },
        {
            "q": "6. At what order of magnitude of microbial cell count does noticeable organoleptic spoilage occur in fresh foods?",
            "opts": ["1) > 10^7 CFU/g (10,000,000 CFU/g)", "2) > 10^3 CFU/g", "3) > 10^11 CFU/g"],
            "ans": "1) > 10^7 CFU/g (10,000,000 CFU/g)",
            "exp": "Spoilage manifestations (off-odors, slime, discoloration) become detectable when bacterial populations exceed ~10^7 to 10^8 CFU/g."
        },
        {
            "q": "7. You go out for dinner and experience rapid vomiting during the night (within 4 hours). This points to a:",
            "opts": ["1) Foodborne infection", "2) Foodborne intoxication", "3) Toxico-infection"],
            "ans": "2) Foodborne intoxication",
            "exp": "Vomiting within a short incubation time (<6h) is characteristic of pre-formed toxins ingested with food (e.g. S. aureus or B. cereus emetic toxin)."
        },
        {
            "q": "8. Which pathogen has a significantly higher disease burden and mortality rate per individual case?",
            "opts": ["1) Staphylococcus aureus", "2) Listeria monocytogenes"],
            "ans": "2) Listeria monocytogenes",
            "exp": "While S. aureus causes self-limiting gastroenteritis, Listeria monocytogenes causes invasive listeriosis (septicemia, meningitis, miscarriages) with a mortality rate of 20-30%."
        },
        {
            "q": "9. Comparing cooked ham vs. fermented salami, which product forms a higher risk for Staphylococcus aureus growth and toxin formation?",
            "opts": ["1) Cooked ham", "2) Fermented salami"],
            "ans": "1) Cooked ham",
            "exp": "Cooked ham has low competing flora (killed during cooking) and high aw. S. aureus is a poor competitor, so post-process contamination on cooked ham allows it to multiply freely if temperature abused."
        },
        {
            "q": "10. In a hospital outbreak, chocolate pudding and vanilla sauce were boiled, cooled slowly at room temp in large jars, and served 24h later. Patients suffered diarrhea and nausea 10 hours later. What was the causative pathogen?",
            "opts": ["1) Staphylococcus aureus", "2) Bacillus cereus (diarrhoeal type)", "3) Salmonella Enteritidis"],
            "ans": "2) Bacillus cereus (diarrhoeal type)",
            "exp": "B. cereus spores survived boiling, germinated during slow room-temp cooling in vanilla sauce, and caused toxico-infection in the gut with an 8-16h incubation period."
        },
        {
            "q": "11. Moulds of which genus are primarily linked to the production of carcinogenic aflatoxins?",
            "opts": ["1) Penicillium", "2) Aspergillus", "3) Rhizopus"],
            "ans": "2) Aspergillus",
            "exp": "Aspergillus flavus and Aspergillus parasiticus produce aflatoxins in nuts, maize, and dried fruits."
        },
        {
            "q": "12. What is the correct chronological succession of lactic acid bacteria during natural sauerkraut fermentation?",
            "opts": [
                "1) Leuconostoc mesenteroides -> Lactobacillus plantarum -> Lactobacillus brevis",
                "2) Lactobacillus plantarum -> Leuconostoc mesenteroides -> yeast",
                "3) Pseudomonas -> Lactobacillus -> Bacillus"
            ],
            "ans": "1) Leuconostoc mesenteroides -> Lactobacillus plantarum -> Lactobacillus brevis",
            "exp": "Leuconostoc mesenteroides initiates fermentation rapidly (heterofermentative). As acid accumulates, homofermentative Lactobacillus plantarum takes over, followed by tolerant Lactobacillus brevis."
        },
        {
            "q": "13. What are the two main roles of salt addition in vegetable fermentations (e.g. sauerkraut, pickles)?",
            "opts": [
                "1) Extracts cell sap/nutrients via osmosis AND inhibits unwanted spoilage/pathogenic micro-organisms",
                "2) Kills all bacterial spores AND sterilizes the vegetable surface",
                "3) Increases water activity AND accelerates aerobic respiration"
            ],
            "ans": "1) Extracts cell sap/nutrients via osmosis AND inhibits unwanted spoilage/pathogenic micro-organisms",
            "exp": "Salt draws out fermentable sugars and moisture via osmotic pressure while selecting for salt-tolerant lactic acid bacteria over Gram-negative spoilage bacteria."
        },
        {
            "q": "14. Sous-vide products are vacuum packed, mildly heated (90°C, 10 min), and stored refrigerated. Which hurdle specifically prevents the growth of surviving psychrotrophic sporeformers like non-proteolytic C. botulinum?",
            "opts": ["1) The vacuum packaging", "2) The 90°C heating step", "3) Strict cooled storage (< 3°C)"],
            "ans": "3) Strict cooled storage (< 3°C)",
            "exp": "Non-proteolytic C. botulinum spores survive 90°C for 10 min and can grow under anaerobic vacuum conditions down to 3.3°C. Storing strictly below 3°C prevents their growth."
        },
        {
            "q": "15. What selective chromogenic agar medium is standard for detecting Listeria monocytogenes in sampling plans?",
            "opts": ["1) ALOA (Agar Listeria according to Ottaviani and Agosti)", "2) VRBG agar", "3) PCA (Plate Count Agar)"],
            "ans": "1) ALOA (Agar Listeria according to Ottaviani and Agosti)",
            "exp": "ALOA uses selective agents and chromogenic substrates to differentiate pathogenic L. monocytogenes (blue colonies with opaque halos) from other Listeria species."
        }
    ]

    for idx, item in enumerate(questions):
        st.subheader(item["q"])
        user_ans = st.radio(f"Select answer for Q{idx+1}:", item["opts"], key=f"q_{idx}")
        if st.button(f"Check Answer {idx+1}", key=f"btn_{idx}"):
            if user_ans == item["ans"]:
                st.success(f"✅ Correct! {item['exp']}")
            else:
                st.error(f"""❌ Incorrect. Correct answer: **{item['ans']}**

*Explanation:* {item['exp']}""")
        st.divider()

# ---------------------------------------------------------
# MODULE 3: QUANTITATIVE MATH CALCULATOR (a * 10^q FORMAT)
# ---------------------------------------------------------
elif menu == "🧮 Quantitative Math Calculator":
    st.header("🧮 Quantitative Microbiology Calculator")
    st.caption("Inputs and outputs use standard base-10 exponential format (a × 10^q) for clear readability.")
    
    tab1, tab2 = st.tabs(["🔥 Thermal Inactivation (D & z values)", "🧫 Enumeration & Log Reduction"])
    
    with tab1:
        st.subheader("Thermal Process Time Calculator")
        st.markdown("Calculate process time ($t = D \\cdot \\log_{10}(N_0/N_t)$) using $a \\times 10^q$ inputs.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### **Initial Contamination ($N_0$)**")
            c1_1, c1_2 = st.columns([2, 2])
            with c1_1:
                n0_a = st.number_input("Coefficient (a)", value=1.0, step=0.1, key="n0_a")
            with c1_2:
                n0_q = st.number_input("Exponent (q in 10^q)", value=6, step=1, key="n0_q")
            N0 = n0_a * (10 ** n0_q)
            st.info(f"**Value N0:** {n0_a:.2f} × 10^{n0_q} = **{N0:,.0f} CFU/g**")

            st.markdown("---")
            st.markdown("#### **Target Contamination ($N_t$)**")
            c2_1, c2_2 = st.columns([2, 2])
            with c2_1:
                nt_a = st.number_input("Coefficient (a)", value=1.0, step=0.1, key="nt_a")
            with c2_2:
                nt_q = st.number_input("Exponent (q in 10^q)", value=0, step=1, key="nt_q")
            Nt = nt_a * (10 ** nt_q)
            st.info(f"**Value Nt:** {nt_a:.2f} × 10^{nt_q} = **{Nt:,.2f} CFU/g**")

            st.markdown("---")
            D_val = st.number_input("D-value at processing temperature (minutes):", value=0.2, step=0.1, key="d_val")

        with col2:
            st.markdown("#### **Calculated Thermal Results**")
            if N0 > 0 and Nt > 0 and D_val > 0:
                log_red = math.log10(N0 / Nt)
                process_time = D_val * log_red
                
                st.metric("Log Reductions Required:", f"{log_red:.2f} decimal reductions")
                st.metric("Required Heating Time (t):", f"{process_time:.2f} minutes")
                
                st.markdown("**Calculation Breakdown:**")
                st.write(f"- N0 = {n0_a:.2f} × 10^{n0_q}")
                st.write(f"- Nt = {nt_a:.2f} × 10^{nt_q}")
                st.write(f"- Log reductions = log10(N0/Nt) = {log_red:.2f}")
                st.write(f"- Required Time = {D_val} × {log_red:.2f} = **{process_time:.2f} minutes**")

                if D_val == 0.2 and log_red >= 12:
                    st.success("✅ Meets or exceeds the 12D 'Botulinum Cook' standard (D121 = 0.2 min) for canning!")

    with tab2:
        st.subheader("Colony Enumeration (CFU/g)")
        st.markdown("Calculate microbial density (CFU/g = Colonies / (Volume × Dilution)) with 10^q dilution factor.")
        
        c1, c2 = st.columns(2)
        with c1:
            colonies = st.number_input("Colonies counted on plate:", value=45, step=1, key="colonies")
            vol = st.number_input("Plating Volume (mL):", value=0.1, step=0.01, key="vol")
            
            st.markdown("#### **Dilution Factor ($10^q$)**")
            dil_q = st.number_input("Dilution exponent q (e.g. -3 for 10^-3 or 1:1000):", value=-3, step=1, key="dil_q")
            dilution = 10 ** dil_q
            st.info(f"**Dilution Factor:** 10^{dil_q} (= {dilution:g})")

        with c2:
            st.markdown("#### **Enumeration Results**")
            if vol > 0 and dilution > 0:
                cfu_g = colonies / (vol * dilution)
                log_cfu = math.log10(cfu_g)
                
                st.metric("Microbial Density (CFU/g):", f"{format_sci_10q(cfu_g)} CFU/g")
                st.metric("Log Concentration:", f"{log_cfu:.2f} log10 CFU/g")
                
                st.markdown("**Calculation Formula:**")
                st.write(f"CFU/g = {colonies} / ({vol} mL × 10^{dil_q}) = **{format_sci_10q(cfu_g)} CFU/g**")

# ---------------------------------------------------------
# MODULE 4: SPOILAGE & ASSOCIATIONS
# ---------------------------------------------------------
elif menu == "🥩 Spoilage & Associations":
    st.header("🥩 Food Spoilage & Microbial Associations")
    st.write("Spoilage organisms are selected by intrinsic (pH, $a_w$, redox) and extrinsic (temperature, gas atmosphere) parameters.")
    
    spoiler = st.selectbox("Select Spoilage Association Matrix:", [
        "Aerobic Cold Storage Meat (Pseudomonas)",
        "Vacuum-Packed Cold Meat (Lactic Acid Bacteria)",
        "High-Sugar / High-Salt Foods (Osmophilic Yeasts & Molds)",
        "Plant / Vegetable Soft Rot (Pectobacterium / Erwinia)"
    ])
    
    if "Pseudomonas" in spoiler:
        st.info("""### 🥩 Pseudomonas spp.
* **Characteristics:** Gram-negative, obligate aerobe, psychrotrophic.
* **Mechanism:** Outcompetes others in aerobic cold storage. Breaks down glucose and amino acids, producing slime and off-odors (ammonia, esters, sulfides) when populations exceed $> 10^7$ CFU/cm².""")
    elif "Vacuum" in spoiler:
        st.info("""### 🥓 Lactic Acid Bacteria (Lactobacillus, Leuconostoc)
* **Characteristics:** Microaerophilic / facultative anaerobes, psychrotrophic, acid-tolerant.
* **Mechanism:** Selected by exclusion of $O_2$ in vacuum packs. Outcompetes *Pseudomonas*; causes souring, milky exudate, and off-flavors.""")
    elif "High-Sugar" in spoiler:
        st.info("""### 🍯 Osmophilic Yeasts (e.g. Zygosaccharomyces rouxii)
* **Characteristics:** Osmotolerant, grows down to $a_w \\approx 0.62 - 0.80$.
* **Mechanism:** Spoils honey, syrups, jams, and dried fruits by fermenting sugars into alcohol and $CO_2$.""")
    else:
        st.info("""### 🥦 Pectolytic Bacteria (Pectobacterium carotovorum)
* **Characteristics:** Gram-negative, facultative anaerobe.
* **Mechanism:** Secretes pectinases that degrade plant cell walls (middle lamella), leading to bacterial soft rot in vegetables.""")

# ---------------------------------------------------------
# MODULE 5: FERMENTATION & SUCCESSION
# ---------------------------------------------------------
elif menu == "🧀 Fermentation & Succession":
    st.header("🧀 Fermentation & Microbial Succession")
    
    st.subheader("🥬 Sauerkraut Fermentation: 3-Stage Microbial Succession")
    st.markdown("""
    1. **Stage 1: *Leuconostoc mesenteroides***
       * **Role:** Heterofermentative lactic acid bacterium; rapidly initiates fermentation.
       * **Products:** Lactic acid, acetic acid, ethanol, and $CO_2$.
       * **Effect:** Replaces trapped air with $CO_2$ (preventing mold) and lowers pH quickly.
    2. **Stage 2: *Lactobacillus plantarum***
       * **Role:** Homofermentative lactic acid bacterium.
       * **Products:** Exclusively lactic acid.
       * **Effect:** Drives pH down to ~3.5–3.8, inhibiting most competing organisms.
    3. **Stage 3: *Lactobacillus brevis***
       * **Role:** Highly acid-tolerant heterofermentative bacterium.
       * **Effect:** Completes the acid production and final characteristic flavor development.
    """)
    
    st.subheader("🧂 3 Key Roles of Salt in Vegetable Fermentations:")
    st.markdown("""
    * **1. Osmotic Extraction:** Draws out moisture and fermentable sugars from plant tissues to form brine.
    * **2. Microbial Selection:** Inhibits Gram-negative spoilage organisms and pathogens while selecting for salt-tolerant Lactic Acid Bacteria (LAB).
    * **3. Texture Maintenance:** Keeps plant cell walls crisp by inhibiting plant tissue-softening enzymes.
    """)

# ---------------------------------------------------------
# MODULE 6: HYGIENE, BIOFILMS & HACCP
# ---------------------------------------------------------
elif menu == "🧼 Hygiene, Biofilms & HACCP":
    st.header("🧼 Hygiene, Biofilms & Food Safety Management")
    
    st.warning("""⚠️ **GOLDEN RULE: Cleaning MUST always precede disinfection!**

Organic soils (fats, proteins, starch) neutralize chemical disinfectants (e.g. chlorine) and physically shield bacteria inside biofilms.""")
    
    st.subheader("🧬 Biofilm Formation Stages:")
    st.markdown("""
    1. **Reversible Attachment:** Planktonic bacterial cells adhere to surfaces via van der Waals forces.
    2. **Irreversible Attachment:** Production of Extracellular Polymeric Substances (EPS) matrix.
    3. **Maturation:** Microcolony development with nutrient channels.
    4. **Dispersal:** Planktonic cells detach to colonize new processing equipment.
    """)
    
    st.subheader("🛡️ Food Safety Management Hierarchy:")
    st.markdown("""
    * **GHP / GMP (Prerequisite Programs):** Basic environmental and operational hygiene (sanitation, pest control, personal hygiene).
    * **OPRP (Operational Prerequisite Program):** Control measure identified by hazard analysis as essential to control specific hazards (e.g., glass control, raw/cooked segregation).
    * **HACCP / CCP (Critical Control Point):** Step at which control can be applied to **prevent, eliminate, or reduce a hazard to acceptable levels** with measurable critical limits (e.g., core pasteurization temp of 72°C for 15s).
    """)

# ---------------------------------------------------------
# MODULE 7: SAMPLING & CRITERIA
# ---------------------------------------------------------
elif menu == "📊 Sampling & Criteria":
    st.header("📊 Sampling Plans & ICMSF Microbiological Criteria")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔴 2-Class Sampling Plan (n, c, m)")
        st.markdown("""
        * **Application:** Used for **severe hazards / pathogens** (e.g., *Salmonella* in 25g, *E. coli O157*).
        * **Parameters:**
          * **n:** Number of sample units tested.
          * **c:** Maximum allowable defective sample units.
          * **m:** Microbiological limit ($m=0$ for severe pathogens; presence = rejection).
        * **Result:** Sample is either **Acceptable** ($\le m$) or **Defective / Rejected** ($> m$).
        """)
        
    with col2:
        st.subheader("🟡 3-Class Sampling Plan (n, c, m, M)")
        st.markdown("""
        * **Application:** Used for **hygiene indicators or spoilage organisms** (e.g., Enterobacteriaceae, total count).
        * **Parameters:**
          * **m:** Target microbiological limit (good quality).
          * **M:** Upper maximum limit (unacceptable hazard threshold).
          * **c:** Number of samples allowed between $m$ and $M$.
        * **Evaluation:**
          * **Acceptable:** All samples $\le m$.
          * **Marginally Acceptable:** Up to $c$ samples between $m$ and $M$.
          * **Rejected:** Any sample $> M$ OR more than $c$ samples $> m$.
        """)

st.sidebar.markdown("---")
st.sidebar.caption("Grounded in Wageningen University FHM-20306 Course Materials")
