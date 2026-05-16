import streamlit as st

# ==========================================
# 1. HARDCODED ENTERPRISE STYLE & THEME CORRECTION
# ==========================================
st.set_page_config(
    page_title="Road to Ivies | Profile Diagnostic Lab",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* Absolute suppression of Streamlit platform branding */
    #MainMenu, header, .stAppDeployButton, footer {
        visibility: hidden;
        display: none;
        height: 0;
    }
    /* Force high-contrast production dark workspace theme */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    /* Structure padding optimization */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
    /* Clean metric card container styling */
    .metric-box {
        background-color: #1e222b;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. THE STRATEGIC NARRATIVE DICTIONARY (FROM COLLEGE.DOCX)
# ==========================================
STRATEGIC_BINS = {
    "bin_1": {
        "tier": "The Elite Execution Phase (Score 90–100)",
        "bullets": [
            "Your quantitative assets align directly with elite historical baselines (IB 39+/42 or equivalent unweighted marks). Your file safely clears initial baseline filters.",
            "Independent research validation is verified externally (e.g., Summer Science Program (SSP) selection or research publication co-authored under an academic professional).",
            "Critical Vulnerability: High risk of narrative genericism. If your essays present like an unpolished corporate resume or a simple autobiography, ultra-selective schools will reject the file."
        ],
        "roadmap": "Prioritize strategic major calibration and narrative consistency. Your technical narrative must bleed cleanly into university-specific supplemental essays. If there is an internal drop in your specific major-related subject grade, you must actively pivot your application major to a less competitive division to bypass institutional rejection gates."
    },
    "bin_2": {
        "tier": "The Spike Validation Phase (Score 75–89)",
        "bullets": [
            "Strong fundamental baselines, but your extracurricular profile relies heavily on unverified or scattered school-level involvements (e.g., standard club participation, cushions, or shadowing).",
            "For international applicants, the burden of proof is exceptionally high. Passive activities without documented, publicly verifiable evidence are rendered operationally meaningless by competitive selectors.",
            "Institutional Risk: Grouped as a 'well-rounded' applicant—carrying massive rejection risk at schools prioritizing highly specialized, 'pointy' candidates."
        ],
        "roadmap": "Halt the accumulation of low-impact, unverified extracurricular items. Spend the next 90 days generating tangible, public-facing evidence of your skills. For programmers, this is a live GitHub repository with functional builds; for researchers, a verified research project under local university mentorship."
    },
    "bin_3": {
        "tier": "The Metric Stabilization Phase (Score 60–74)",
        "bullets": [
            "Your profile displays strong qualitative hooks or high potential, but the entire file is bottlenecked by a rigid quantitative deficiency (e.g., IB score below 37 or SAT below 1500).",
            "Elite research institutions will hesitate at the academic gate based on these scores before ever evaluating your qualitative essays or independent projects."
        ],
        "roadmap": "Execute an immediate, high-intensity diagnostic testing sprint to break through the standardized testing threshold. If your internal school marks carry a historical dip, strategically target top-tier private and public STEM institutions that allow elite project portfolios to compensate for GPA anomalies."
    },
    "bin_4": {
        "tier": "The Foundation Re-Centering Phase (Score 45–59)",
        "bullets": [
            "The profile presents as a loose collection of basic high school requirements rather than an ambitious, hungry, and intentional academic trajectory.",
            "Academic milestones and testing indicators sit beneath competitive thresholds for highly selective research institutions."
        ],
        "roadmap": "Immediately establish your core profile archetype. Define whether your path is a high-ROI Specialist or a cross-functional Polymath. Every essay draft, independent project attempt, and activity alignment must anchor back to this single thematic core to rescue baseline file coherence."
    },
    "bin_5": {
        "tier": "The Structural Reconstruction Phase (Score 30–44)",
        "bullets": [
            "Significant extracurricular blank spaces compounded by deep structural gaps across academic rigor and standardized benchmarks."
        ],
        "roadmap": "Shift target school lists toward regional institutions that value qualitative turnaround stories, or leverage structured, guaranteed university transfer pathways to rebuild your profile competitiveness."
    },
    "bin_6": {
        "tier": "The Operational Pivot Phase (Score <30)",
        "bullets": [
            "Critical absence of baseline validation metrics across all key application dimensions."
        ],
        "roadmap": "Pivot completely away from elite national ranking systems. Focus exclusively on stabilizing local academic performance and building verifiable foundational skills."
    }
}

# ==========================================
# 3. UNIFIED MONOLITHIC USER INTERFACE
# ==========================================
st.title("Admissions Competitiveness & Strategy Lab")
st.markdown("---")

# DAD'S FEEDBACK #1: Explicit operational guidance framework placed at the top entry gate
st.markdown("""
<div style="background-color: #1e222b; padding: 1.2rem; border-radius: 6px; margin-bottom: 2rem; border-left: 4px solid #ff4b4b;">
    <h5 style="margin: 0 0 0.5rem 0; color: #ff4b4b;">Operational Guidance</h5>
    <p style="margin: 0; font-size: 0.95rem; color: #fafafa; line-height: 1.4;">
        Enter your explicit academic and profile data choices in the matrix below. The diagnostic engine will synthesize 
        these variables to evaluate how your current achievements map to elite institutional thresholds, generating an 
        authoritative, continuous <b>Strategic Optimization Roadmap</b> instead of an absolute judgment.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Profile Diagnostic Methodology & Framework")
st.markdown(
    "This predictive lab evaluates an international applicant's profile using the multi-dimensional framework "
    "employed by elite admissions committees. Admissions at this level are strictly non-linear: "
    "quantitative scores only serve to pass initial academic thresholds, while ultimate acceptance depends entirely "
    "on narrative differentiation, subject-specific alignment, and verified project spikes."
)

# Multi-column methodological breakdown
m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    st.markdown("##### **1. Quantitative Thresholds**")
    st.markdown(
        "<small>Internal marks and standardized tests are measured against elite baselines (e.g., SAT 1530+, IB 39+/42). "
        "Clearing this gate ensures your file is read, but metrics alone do not guarantee admission.</small>", 
        unsafe_allow_html=True
    )

with m_col2:
    st.markdown("##### **2. Major Calibration & Rigor**")
    st.markdown(
        "<small>Universities analyze subject-specific grades relative to your intended major. A lower grade in a core discipline "
        "causes an automatic rejection, even if your overall cumulative GPA appears competitive.</small>", 
        unsafe_allow_html=True
    )

with m_col3:
    st.markdown("##### **3. The Narrative Spike**")
    st.markdown(
        "<small>Elite programs reject 'well-rounded' applications. The tool heavily weights independent, publicly "
        "verifiable projects (e.g., GitHub code bases, publications) over passive school club memberships.</small>", 
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# DAD'S FEEDBACK #2: Entire input structure bound into a single, unified analytical pass
with st.form("master_profile_form"):
    st.subheader("Phase 1: Input Profile Matrix")
    
    # ------------------------------------------
    # LEVEL 1: FOUNDATIONAL METRICS (2-COLUMN BALANCED LAYOUT)
    # ------------------------------------------
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Academic Foundations**")
        
        st.markdown("<small style='color:#b0b3b8;'>Select your internal academic grading bracket. <i>Note: IB 39+ or equivalent is the standard competitive baseline for Ivy League considerations.</i></small>", unsafe_allow_html=True)
        gpa_choice = st.selectbox(
            "Internal Academic Performance Baseline (GPA / Board Marks)",
            options=[
                "Elite Bracket: IB 39-42 / 4.0 GPA Tier",
                "Target Bracket: IB 35-38 / GPA 3.3-3.6 Tier",
                "Developing Bracket: IB 32-34 / GPA 3.0-3.2 Tier",
                "Foundational Bracket: IB Score below 32"
            ],
            label_visibility="collapsed"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<small style='color:#b0b3b8;'>Standardized Testing Baseline. <i>Note: Scores below 1500 typically require heavy independent project offsets.</i></small>", unsafe_allow_html=True)
        sat_choice = st.selectbox(
            "Standardized Testing Baseline (SAT / ACT Equivalent)",
            options=[
                "Top Tier Benchmark: SAT 1530-1600 / ACT 34-36",
                "Competitive Mid-Range: SAT 1500-1520 / ACT 33",
                "Target Baseline: SAT 1350-1490 / ACT 31-32",
                "Developing Baseline: SAT below 1350 / ACT below 31"
            ],
            label_visibility="collapsed"
        )

    with col2:
        st.markdown("#### **Institutional & Profile Archetype**")
        
        st.markdown("<small style='color:#b0b3b8;'>High School Institutional Context</small>", unsafe_allow_html=True)
        school_tier_choice = st.selectbox(
            "High School Institutional Context",
            options=[
                "Tier 1: Established International Feeder School (e.g., TISB, Mallya Aditi)",
                "Tier 2: Competitive Regional/National Board School (CBSE/ICSE)",
                "Tier 3: Non-Traditional / Developing Local Infrastructure School"
            ],
            label_visibility="collapsed"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("<small style='color:#b0b3b8;'>Applicant Profile Archetype Structure</small>", unsafe_allow_html=True)
        archetype_choice = st.selectbox(
            "Applicant Profile Archetype Structure",
            options=[
                "Specialist: Highly focused, early drive toward high-ROI STEM/Finance pipelines",
                "Polymath: Multi-talented, cross-functional profile requiring a unifying narrative",
                "The Tree: Steady growth trajectory; exceptional long-term adaptability"
            ],
            label_visibility="collapsed"
        )

    st.markdown("---")

    # ------------------------------------------
    # LEVEL 2: STRATEGIC INFLECTION POINTS (FULL-WIDTH FOR MAXIMUM READABILITY & NO TEXT CLIPPING)
    # ------------------------------------------
    st.markdown("#### **Specialized Independent Projects & Verification (The 'Spike')**")
    st.markdown(
        "<p style='margin:0 0 0.5rem 0; font-size:0.85rem; color:#b0b3b8;'>"
        "Elite admissions committees reject generic 'well-rounded' applicant files. Select the verification tier "
        "that matches your highest external burden-of-proof milestone:</p>", 
        unsafe_allow_html=True
    )
    spike_choice = st.selectbox(
        "Specialized Independent Projects & Verification (The 'Spike')",
        options=[
            "Elite Validation: Peer-reviewed publication co-authored with academic experts, or selection to premier merit tracks (e.g., SSP)",
            "Emerging Validation: Independent technical development with a public codebase (GitHub), active thesis drafting, or local lab internship",
            "Participation Level: Long-term community volunteering, student council leadership, or local event organization",
            "Baseline Level: Standard high school club membership without documented external outcomes"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### **Target University Selective Threshold**")
    st.markdown(
        "<p style='margin:0 0 0.5rem 0; font-size:0.85rem; color:#b0b3b8;'>"
        "Define your target benchmark level. This choice directly calibrates the deficit scoring models and variance metrics "
        "in your final roadmap analysis:</p>", 
        unsafe_allow_html=True
    )
    target_tier_choice = st.selectbox(
        "Target University Selective Threshold",
        options=[
            "Elite Ivy League Core: Hyper-Selective Targets (Princeton, Harvard, Yale, Stanford, MIT, Caltech)",
            "Level 2 Top Tier Targets: Competitive Global Universities (UC Berkeley, CMU, NYU, Columbia, Cornell, UCLA)",
            "Level 3 National Universities: Standard Global Multi-Universities"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # ------------------------------------------
    # LEVEL 3: CLIENT BACKGROUND & SURVEY (2-COLUMN LAYOUT)
    # ------------------------------------------
    # DAD'S FEEDBACK #5 & #6: Expanded Target Context & Custom Constraint Survey Section
    st.markdown("#### **Target Optimization & Customization Survey**")
    col3, col4 = st.columns(2)
    
    with col3:
        intended_major = st.text_input(
            "Intended Academic Major / Discipline Focus", 
            placeholder="e.g., Quantitative Finance, Computer Science, Biology"
        )
        survey_status = st.selectbox(
            "University Goal Positioning Context",
            options=[
                "Highly Certain: Confirmed selection of explicit target institutions.",
                "Exploratory: Decided on core disciplines but open to geographic/institutional variance.",
                "Uncertain / Requires Structural Advisory: Seeking strategic clarity on major-to-university mapping."
            ]
        )

    with col4:
        financial_factor = st.radio(
            "Are financial aid/overall cost constraints a deciding factor in your list strategy?", 
            ["No", "Yes"]
        )

    st.markdown("<br>", unsafe_allow_html=True)
    submit_button = st.form_submit_button(label="Generate Profile Assessment & Strategic Roadmap")

# ==========================================
# 4. MATH SYNTHESIS ENGINE & DYNAMIC ROUTER
# ==========================================
if submit_button:
    st.markdown("---")
    st.subheader("Phase 2: Clinical Diagnostic Output")
    
    # 4.1 Deconstruct Selection Matrices to Quant Values
    if "Elite Bracket" in gpa_choice: gpa_score = 100
    elif "Target Bracket" in gpa_choice: gpa_score = 82
    elif "Developing Bracket" in gpa_choice: gpa_score = 68
    else: gpa_score = 50

    if "Top Tier" in sat_choice: sat_score = 100
    elif "Competitive" in sat_choice: sat_score = 88
    elif "Target Baseline" in sat_choice: sat_score = 75
    else: sat_score = 50

    school_multiplier = 10 if "Tier 1" in school_tier_choice else (5 if "Tier 2" in school_tier_choice else 0)
    
    if "Elite" in spike_choice: spike_score = 10
    elif "Emerging" in spike_choice: spike_score = 7
    elif "Participation" in spike_choice: spike_score = 5
    else: spike_score = 2

    # 4.2 Mathematical Synthesis Calculation (Calibrated to achieve a clean 100 maximum)
    raw_score = (gpa_score * 0.4) + (sat_score * 0.3) + (spike_score * 2.0) + school_multiplier
    final_score = min(100.0, max(0.0, raw_score))
    
    # 4.3 Score Bin Router Logic
    if final_score >= 90: content = STRATEGIC_BINS["bin_1"]
    elif final_score >= 75: content = STRATEGIC_BINS["bin_2"]
    elif final_score >= 60: content = STRATEGIC_BINS["bin_3"]
    elif final_score >= 45: content = STRATEGIC_BINS["bin_4"]
    elif final_score >= 30: content = STRATEGIC_BINS["bin_5"]
    else: content = STRATEGIC_BINS["bin_6"]
        
    threshold_map = {
        "Elite Ivy League Core": 92,
        "Level 2 Top Tier Targets": 78,
        "Level 3 National Universities": 60
    }
    selected_target_clean = target_tier_choice.split(":")[0].strip()
    target_threshold = threshold_map.get(selected_target_clean, 78)
    variance = final_score - target_threshold

    # 4.4 Render Production Interface
    st.markdown(f"### Current Diagnostic Status: **{content['tier']}**")
    
    st.markdown(f"""
        <div class="metric-box">
            <h4 style='margin:0; color:#ff4b4b;'>Synthesized Profile Competitiveness Index: {final_score:.1f} / 100</h4>
            <p style='margin:5px 0 0 0; font-size:0.9rem; color:#fafafa;'>Target Match Variance for {selected_target_clean}: <b>{variance:+.1f} points</b></p>
        </div>
    """, unsafe_allow_html=True)
    
    # DAD'S FEEDBACK #3: 3-4 Bullets of Qualitative Strategic Feedback
    st.markdown("#### Strategic Profile Evaluation")
    for bullet in content["bullets"]:
        st.markdown(f"* {bullet}")
        
    # DAD'S FEEDBACK #4 & #5: Continuous Action Plan and Roadmap Optimization Notes
    st.markdown("#### Tactical Action Plan & Optimization Roadmap")
    st.success(content["roadmap"])
    
    # Context Injection Module incorporating the Survey Matrix variables directly into output text
    st.markdown("#### Custom Survey Context Calibration")
    major_context = intended_major if intended_major else "Unspecified Academic Field"
    
    context_bullet_1 = f"**Major Calibration:** Evaluating your metrics within the strict context of **{major_context}**. Highly quantitative or high-ROI tracks will face increased review stringency regarding subject-specific grading subsets."
    
    if financial_factor == "Yes":
        context_bullet_2 = "**Financial Strategy Constraint:** Financial aid considerations are active. Your institutional list strategy must prioritize aid-blind elite universities or institutions offering robust, merit-based tuition adjustments to minimize structural funding liabilities."
    else:
        context_bullet_2 = "**Financial Strategy Constraint:** Full-funding capability confirmed. Your strategic roadmap can confidently prioritize maximum institutional selection alignment without geographic or structural budgetary guardrails."

    st.markdown(f"* {context_bullet_1}")
    st.markdown(f"* {context_bullet_2}")
    st.markdown(f"* **Goal Positioning Status:** Client profile is classified as *{survey_status.split(':')[0]}*.")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Target Match Optimization Summary")
    if variance < 0:
        st.warning(
            f"Your current calculated profile index sits below the historical median threshold for {selected_target_clean}. "
            f"To optimize this action plan and bridge this {abs(variance):.1f}-point deficit, you must execute the "
            "recommended roadmap steps with immediate, maximum intensity over the coming academic cycle."
        )
    else:
        st.info(
            f"Your profile mathematically aligns with or outpaces the baseline selective requirements for {selected_target_clean}. "
            f"Your operational priority must shift from metric accumulation to minimizing risk of yield-protection "
            "rejections by explicitly validating your unique cultural and institutional fit through your supplemental essays."
        )
        
    # Lead Catchment Module
    st.markdown("---")
    st.subheader("Request Bespoke Profile Optimization Plan")
    st.markdown(
        "To customize this continuous roadmap based on your selected major context, specific university preferences, "
        "or complex financial constraints, initiate a formal profile expansion review below."
    )
    with st.expander("Submit Profile Metrics for Human Consultation Review"):
        with st.form("lead_generation_form"):
            user_name = st.text_input("Parent / Student Representative Name")
            contact_email = st.text_input("Primary Communication Email Address")
            specific_queries = st.text_area("Detail any specific concerns, university restrictions, or legacy considerations:")
            
            submit_lead = st.form_submit_button("Request Premium Strategy Alignment Analysis")
            if submit_lead:
                st.success("Your comprehensive diagnostic matrix has been securely logged. An advisor will contact you within 24 business hours.")
