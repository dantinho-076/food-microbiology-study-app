import streamlit as st
import math

st.set_page_config(
    page_title="Food Microbiology Master Suite",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.1rem; color: #4B5563; margin-bottom: 1.5rem; }
    .card { background-color: #F3F4F6; padding: 1.2rem; border-radius: 10px; border-left: 5px solid #2563EB; margin-bottom: 1rem; }
    .card-success { background-color: #ECFDF5; padding: 1.2rem; border-radius: 10px; border-left: 5px solid #10B981; margin-bottom: 1rem; }
    .card-warning { background-color: #FFFBEB; padding: 1.2rem; border-radius: 10px; border-left: 5px solid #F59E0B; margin-bottom: 1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🔬 Food Microbiology (FHM-20306) Master Study Suite</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Interactive Outbreak Diagnoser, Thermal Math Calculator, Spoilage, Fermentation & HACCP Review</div>', unsafe_allow_html=True)

# Tabs Navigation
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🌲 Outbreak Decision Tree", 
    "🧮 Thermal & CFU Math", 
    "🥩 Food Spoilage", 
    "🧀 Fermentation", 
    "🧼 Biofilms & HACCP", 
    "📊 Sampling Plans",
    "📝 Practice Drills"
])

# TAB 1: DECISION TREE
with tab1:
    st.header("🌲 Outbreak Diagnostic Decision Tree")
    st.write("Walk through step-by-step clinical and epidemiological questions to diagnose the causative pathogen.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        symptom = st.radio("Step 1: Primary Clinical Symptom", ["Vomiting & Nausea predominant", "Abdominal Cramps & Diarrhea predominant"])
        
        if symptom == "Vomiting & Nausea predominant":
            onset = st.radio("Step 2: Onset / Incubation Time", ["Rapid Onset (0.5 to 6 hours)", "Slower Onset (12 to 48 hours)"])
            if onset == "Rapid Onset (0.5 to 6 hours)":
                food = st.radio("Step 3: Food Vehicle", ["Fried rice or starchy dish left at room temp", "Cured ham, cream pastries, manual handling"])
            else:
                food = "Canned low-acid foods, vacuum RTE, cured meats"
        else:
            onset = st.radio("Step 2: Onset / Incubation Time", ["Medium Onset (8 to 24 hours)", "Slower Onset (2 to 5 days)", "Very Slow Onset (Days to Months)"])
            if onset == "Medium Onset (8 to 24 hours)":
                fever = st.radio("Step 3: Is FEVER present?", ["NO FEVER", "YES FEVER"])
                if fever == "NO FEVER":
                    food = st.radio("Step 4: Preparation & Food Matrix", ["Large pots of cooked meat/stew/gravy held warm", "Vanilla sauce, pudding, vegetables cooled slowly"])
                else:
                    food = "Poultry, raw eggs, undercooked meat, raw sprouts"
            elif onset == "Slower Onset (2 to 5 days)":
                food = st.radio("Step 3: Stool Character & Food Matrix", ["Severe cramps + Bloody diarrhea (Poultry/Raw milk)", "Bloody diarrhea + HUS risk (Undercooked beef/Sprouts)"])
            else:
                food = "RTE refrigerated foods with long shelf-life (soft cheese, deli meat, smoked fish)"

    with col2:
        st.subheader("📋 Diagnosis & Pathogen Profile")
        if symptom == "Vomiting & Nausea predominant":
            if onset == "Rapid Onset (0.5 to 6 hours)":
                if "Fried rice" in food:
                    st.markdown("""
                    <div class="card-warning">
                        <h3>🦠 Bacillus cereus (Emetic Type)</h3>
                        <p><b>Mechanism:</b> Intoxication (Pre-formed cereulide toxin in food)</p>
                        <p><b>Incubation:</b> 0.5 – 6 hours</p>
                        <p><b>Classic Food:</b> Fried rice, boiled starchy foods left at room temp</p>
                        <p><b>Prevention:</b> Rapid cooling (<5°C) or hot holding (>60°C)</p>
                        <hr>
                        <small><b>Exam Note:</b> Cereulide toxin is extremely heat-stable! Reheating rice does NOT destroy the toxin.</small>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="card-warning">
                        <h3>🦠 Staphylococcus aureus</h3>
                        <p><b>Mechanism:</b> Intoxication (Pre-formed enterotoxin in food)</p>
                        <p><b>Incubation:</b> 1 – 6 hours</p>
                        <p><b>Classic Food:</b> Cooked ham, cured meats, cream pastries, salty foods handled manually</p>
                        <p><b>Prevention:</b> Personal hygiene, handwashing, rapid cooling</p>
                        <hr>
                        <small><b>Exam Note:</b> Tolerates low water activity (a_w down to 0.85). Toxin is heat-stable.</small>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="card">
                    <h3>🦠 Clostridium botulinum</h3>
                    <p><b>Mechanism:</b> Intoxication (Pre-formed neurotoxin / Botulism)</p>
                    <p><b>Incubation:</b> 12 – 48 hours</p>
                    <p><b>Classic Food:</b> Low-acid canned foods, vacuum-packed RTE meals, garlic in oil</p>
                    <p><b>Prevention:</b> 12D "Botulinum cook" (121°C for 3 min) for low-acid cans; nitrites</p>
                    <hr>
                    <small><b>Exam Note:</b> Obligate anaerobe. Neurotoxin causes double vision, flaccid paralysis.</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            if onset == "Medium Onset (8 to 24 hours)":
                if fever == "NO FEVER":
                    if "Large pots" in food:
                        st.markdown("""
                        <div class="card">
                            <h3>🦠 Clostridium perfringens</h3>
                            <p><b>Mechanism:</b> Toxico-infection (Enterotoxin released in gut during sporulation)</p>
                            <p><b>Incubation:</b> 8 – 16 hours</p>
                            <p><b>Classic Food:</b> Large pots of stew, boiled meats, gravies kept warm</p>
                            <p><b>Prevention:</b> Rapid cooling of large volumes; reheat to >70°C</p>
                            <hr>
                            <small><b>Exam Note:</b> Anaerobic center of large pots allows growth. Severe gas & cramps, NO fever.</small>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="card">
                            <h3>🦠 Bacillus cereus (Diarrhoeal Type)</h3>
                            <p><b>Mechanism:</b> Toxico-infection (Enterotoxin produced in small intestine)</p>
                            <p><b>Incubation:</b> 8 – 16 hours</p>
                            <p><b>Classic Food:</b> Vanilla sauce, puddings, soups, cooked vegetables</p>
                            <p><b>Prevention:</b> Rapid cooling (<5°C) after cooking</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="card-success">
                        <h3>🦠 Salmonella spp.</h3>
                        <p><b>Mechanism:</b> Infection (Invasion of intestinal mucosa)</p>
                        <p><b>Incubation:</b> 12 – 36 hours</p>
                        <p><b>Classic Food:</b> Poultry, raw eggs, undercooked meat, raw sprouts</p>
                        <p><b>Prevention:</b> Cooking (>70°C), avoid cross-contamination</p>
                        <hr>
                        <small><b>Exam Note:</b> Classic gastroenteritis with fever, watery diarrhea, and belly pain.</small>
                    </div>
                    """, unsafe_allow_html=True)
            elif onset == "Slower Onset (2 to 5 days)":
                if "Poultry" in food:
                    st.markdown("""
                    <div class="card-success">
                        <h3>🦠 Campylobacter jejuni</h3>
                        <p><b>Mechanism:</b> Infection (Invasive mucosal colonization)</p>
                        <p><b>Incubation:</b> 2 – 5 days</p>
                        <p><b>Classic Food:</b> Undercooked poultry, raw milk, unchlorinated water</p>
                        <p><b>Prevention:</b> Thorough poultry cooking, avoid cross-contamination</p>
                        <hr>
                        <small><b>Exam Note:</b> Microaerophilic. Leading cause of bacterial diarrhea; severe pain + bloody stool.</small>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="card-success">
                        <h3>🦠 STEC / E. coli O157</h3>
                        <p><b>Mechanism:</b> Infection (Shiga toxin production in gut)</p>
                        <p><b>Incubation:</b> 1 – 8 days (avg 3-4 days)</p>
                        <p><b>Classic Food:</b> Undercooked ground beef ('hamburger disease'), raw sprouts, leafy greens</p>
                        <p><b>Prevention:</b> Cook ground beef thoroughly (>71°C), wash produce</p>
                        <hr>
                        <small><b>Exam Note:</b> Shiga toxin causes kidney failure (HUS - Haemolytic Uremic Syndrome) in children/YOPI.</small>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="card">
                    <h3>🦠 Listeria monocytogenes</h3>
                    <p><b>Mechanism:</b> Invasive Infection (Intracellular pathogen)</p>
                    <p><b>Incubation:</b> Few days up to 3 months</p>
                    <p><b>Classic Food:</b> RTE refrigerated foods (soft cheeses, deli meats, smoked fish)</p>
                    <p><b>Prevention:</b> Hygiene in factories, strict temperature control</p>
                    <hr>
                    <small><b>Exam Note:</b> Psychrotrophic (grows at fridge temp >0°C). High mortality in pregnant women / YOPI.</small>
                </div>
                """, unsafe_allow_html=True)

# TAB 2: THERMAL MATH
with tab2:
    st.header("🧮 Quantitative Microbiology Calculator")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("🔥 Thermal Process Time Calculator")
        N0 = st.number_input("Initial Contamination N₀ (CFU/g)", value=1e6, format="%.2e")
        Nt = st.number_input("Target Contamination Nₜ (CFU/g)", value=1.0, format="%.2e")
        D_val = st.number_input("D-value at target temp (minutes)", value=1.5, step=0.1)
        
        if N0 > 0 and Nt > 0 and D_val > 0:
            log_red = math.log10(N0 / Nt)
            time_req = log_red * D_val
            st.success(f"**Decimal Log Reductions required:** {log_red:.2f} decimal reductions")
            st.info(f"**Required Processing Time:** {time_req:.2f} minutes")
            
            if log_red >= 12:
                st.caption("✅ Meets or exceeds the 12D 'Botulinum Cook' standard for low-acid canned foods!")

    with col_b:
        st.subheader("🧫 Colony Enumeration & CFU/g Calculator")
        colonies = st.number_input("Colonies Counted on Plate", value=45, step=1)
        vol_ml = st.number_input("Plating Volume (mL)", value=0.1, step=0.01)
        dilution = st.number_input("Dilution Factor of Plate (e.g., 1e-4)", value=1e-4, format="%.1e")
        
        if vol_ml > 0 and dilution > 0:
            cfu_g = colonies / (vol_ml * dilution)
            log_cfu = math.log10(cfu_g) if cfu_g > 0 else 0
            st.success(f"**Calculated CFU/g:** {cfu_g:.2e} CFU/g")
            st.info(f"**Log10 CFU/g:** {log_cfu:.2f} log10 CFU/g")

# TAB 3: SPOILAGE
with tab3:
    st.header("🥩 Food Spoilage & Microbial Associations")
    st.write("Spoilage organisms are selected by intrinsic (pH, a_w, redox) and extrinsic (temp, gas) factors.")
    
    spoiler = st.selectbox("Select Spoilage Association:", [
        "Aerobic Cold Storage Meat (Pseudomonas)",
        "Vacuum-Packed Cold Meat (Lactic Acid Bacteria)",
        "High-Sugar / High-Salt Foods (Osmophilic Yeasts & Molds)",
        "Plant / Vegetable Soft Rot (Erwinia / Pectobacterium)"
    ])
    
    if "Pseudomonas" in spoiler:
        st.info("**Pseudomonas spp.:** Gram-negative, obligate aerobe, psychrotrophic. Produces slime, off-odors (ammonia, esters) on fresh meat stored aerobically at fridge temp.")
    elif "Vacuum" in spoiler:
        st.info("**Lactic Acid LAB (e.g. Lactobacillus, Leuconostoc):** Facultative anaerobes, psychrotrophic. Selected by lack of O₂. Causes souring, gas production, or milky exudate.")
    elif "High-Sugar" in spoiler:
        st.info("**Osmophilic Yeasts (e.g. Zygosaccharomyces rouxii):** Tolerates low water activity (a_w < 0.80). Spoils honey, jams, syrups, and dried fruit.")
    else:
        st.info("**Pectolytic Bacteria (e.g. Pectobacterium carotovorum):** Produces pectinases that break down plant cell walls, leading to bacterial soft rot in vegetables.")

# TAB 4: FERMENTATION
with tab4:
    st.header("🧀 Fermentation & Starter Cultures")
    st.subheader("Microbial Succession in Sauerkraut Fermentation")
    st.markdown("""
    1. **Phase 1: *Leuconostoc mesenteroides*** (Heterofermentative, produces CO₂, lactic acid, acetic acid, ethanol; lowers pH rapidly).
    2. **Phase 2: *Lactobacillus plantarum*** (Homofermentative, lowers pH further down to ~3.5).
    3. **Phase 3: *Lactobacillus brevis*** (Final acid tolerance, completes flavor profile).
    """)
    st.subheader("3 Key Roles of Salt in Fermentation:")
    st.markdown("""
    - **1. Selective Pressure:** Inhibits spoilage bacteria and pathogens while favoring Lactic Acid Bacteria (LAB).
    - **2. Moisture Extraction:** Draws out water and fermentable sugars from plant tissues via osmosis.
    - **3. Texture Maintenance:** Keeps plant cell walls crisp by inhibiting tissue-softening enzymes.
    """)

# TAB 5: HYGIENE & HACCP
with tab5:
    st.header("🧼 Hygiene, Biofilms & HACCP Systems")
    st.subheader("Cleaning vs. Disinfection Rule")
    st.warning("⚠️ **ALWAYS CLEAN BEFORE DISINFECTING!** Organic soil (proteins, fats) inactivates chemical disinfectants and protects bacteria trapped inside biofilms.")
    
    st.subheader("Quality System Hierarchy")
    st.markdown("""
    - **GHP / GMP (Prerequisite Programs):** Basic hygiene, sanitation, pest control, personal cleanliness.
    - **OPRP (Operational Prerequisite Program):** Specific control measure to reduce a hazard (e.g., glass control, raw/cooked separation).
    - **HACCP (Hazard Analysis Critical Control Point):** System identifying specific **Critical Control Points (CCPs)** with measurable critical limits (e.g., pasteurization temp/time).
    """)

# TAB 6: SAMPLING PLANS
with tab6:
    st.header("📊 Sampling Plans (ICMSF Criteria)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2-Class Sampling Plan (n, c, m)")
        st.markdown("""
        - Used for **severe hazards** (e.g., *Salmonella* in 25g).
        - **n:** Number of sample units tested.
        - **c:** Maximum allowable defective units.
        - **m:** Microbiological limit (m=0 for pathogens; presence = rejection).
        """)
    with col2:
        st.subheader("3-Class Sampling Plan (n, c, m, M)")
        st.markdown("""
        - Used for **hygiene indicators** or **spoilage** (e.g., *E. coli*, Enterobacteriaceae).
        - **m:** Satisfactory upper limit.
        - **M:** Unacceptable upper limit.
        - **Acceptable:** All ≤ m.
        - **Marginally acceptable:** Up to *c* samples between *m* and *M*.
        - **Rejected:** Any sample > *M* OR more than *c* samples > *m*.
        """)

# TAB 7: PRACTICE DRILLS
with tab7:
    st.header("📝 Interactive Practice Drills")
    q1 = st.radio("Q1: A customer develops sudden severe vomiting 2 hours after eating fried rice. Reheating the rice prior to serving did not prevent illness. Why?", [
        "Reheating activated spore germination.",
        "Bacillus cereus emetic toxin (cereulide) is heat-stable and not destroyed by reheating.",
        "Staphylococcus aureus produced enterotoxin during reheating.",
        "Salmonella multiplied rapidly during heating."
    ])
    if st.button("Check Q1"):
        if "heat-stable" in q1:
            st.success("Correct! Cereulide is a pre-formed heat-stable cyclic peptide toxin that survives normal cooking temperatures.")
        else:
            st.error("Incorrect. The emetic toxin (cereulide) formed in starchy foods is extremely heat-stable!")

    q2 = st.radio("Q2: Why must food-contact surfaces be thoroughly cleaned BEFORE applying a chemical disinfectant?", [
        "Cleaning lowers the temperature of the surface.",
        "Organic soil inactivates disinfectants and protects bacteria inside biofilms.",
        "Disinfectants only work on dry surfaces.",
        "Cleaning changes the pH of bacteria."
    ])
    if st.button("Check Q2"):
        if "Organic soil" in q2:
            st.success("Correct! Organic matter reacts with disinfectants (e.g. chlorine) and physically shields microbes inside biofilms.")
        else:
            st.error("Incorrect. Organic soil neutralizes chemical disinfectants and protects biofilm bacteria.")
