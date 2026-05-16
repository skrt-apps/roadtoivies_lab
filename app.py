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
        padding-top: 2rem;
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
# 2. THE CORE STRATEGIC DICTIONARY (HIGH-AUTHORITY COPY)
# ==========================================
STRATEGIC_BINS = {
    "bin_1": {
        "tier": "The Elite Execution Phase (Score 90–100)",
        "bullets": [
            "Academic foundations and institutional rigor are flawless; your profile has successfully cleared the initial quantitative thresholds of ultra-selective committees.",
            "Your specialized academic or extracurricular 'spike' is authentic and verified externally, placing your application file within the top 1% of the global applicant pool.",
            "Critical Vulnerability: High operational risk of appearing structurally over-engineered or lacking an organic, authentic human narrative pulse."
        ],
        "roadmap": "Prioritize narrative decoupling. Intentionally strip out over-polished, formulaic buzzwords from your personal statement. Execute a hyper-aggressive Early Decision (ED) framework targeting the specific institution whose immediate departmental needs align precisely with your vertical spike."
    },
    "bin_2": {
        "tier": "The Spike Validation Phase (Score 75–89)",
        "bullets": [
            "Exceptionally strong internal testing baselines and GPA metrics, but your achievement markers are currently distributed too broadly across disparate areas.",
            "You possess high capability metrics (e.g., strong debate involvements, foundational coding, musical proficiency) but lack a singular, defining intellectual apex hook.",
            "Institutional risk: Admissions committees will categorize you as a 'well-rounded' applicant, a classification that carries severe rejection risk at Tier 1 universities."
        ],
        "roadmap": "Halt the accumulation of minor, low-impact extracurricular involvements. Dedicate the next 90 days exclusively to executing one monolithic independent project that validates your core discipline (e.g., compiling a distinct qualitative research thesis or publishing a specialized dataset)."
    },
    "bin_3": {
        "tier": "The Metric Stabilization Phase (Score 60–74)",
        "bullets": [
            "The profile exhibits distinct flashes of qualitative impact or unique background context, but the overall file is being systematically dragged down by a raw metric limitation.",
            "A historical drop in GPA trajectory or an uncompetitive testing baseline means institutional selectors will hesitate at the academic gate before reviewing your qualitative narrative."
        ],
        "roadmap": "Execute an immediate 6-week diagnostic testing sprint to raise your standardized testing baseline, or systematically shift your application strategy to focus on institutions where your qualitative narrative can dominate the file review process."
    },
    "bin_4": {
        "tier": "The Foundation Re-Centering Phase (Score 45–59)",
        "bullets": [
            "The application file currently presents as a loose collection of baseline institutional requirements rather than a deliberate, focused, and intentional academic trajectory.",
            "Extracurricular activities are largely passive or administrative (e.g., standard club memberships without documented leadership outcomes or measurable operational execution)."
        ],
        "roadmap": "Immediately define your core interdisciplinary domain. Every essay draft, independent reading program, and supplemental response must firmly anchor back to this single thematic center to establish baseline application coherence."
    },
    "bin_5": {
        "tier": "The Structural Reconstruction Phase (Score 30–44)",
        "bullets": [
            "Fundamental structural misalignment exists between your current profile metrics and the baseline operational expectations of selective national research universities.",
            "Significant extracurricular blank spaces are compounded by acute foundational academic vulnerabilities."
        ],
        "roadmap": "Realign your immediate list strategy to include institutions that heavily weight qualitative turnaround narratives, or actively look into established community college-to-university guaranteed transfer pathways."
    },
    "bin_6": {
        "tier": "The Operational Pivot Phase (Score <30)",
        "bullets": [
            "Your profile displays a critical absence of foundational validation metrics across both academic and extracurricular dimensions."
        ],
        "roadmap": "Shift operational focus completely away from elite admissions ranking matrices. Immediate priority must be placed on establishing fundamental academic stability and utilizing structured bridge programs."
    }
}

# ==========================================
# 3. UNIFIED MONOLITHIC USER INTERFACE
# ==========================================
st.title("Admissions Competitiveness & Strategy Lab")
st.markdown("---")

st.subheader("How to Use This Diagnostic Tool")
st.info(
    "Enter your quantitative baselines, institutional context, and extracurricular metrics below. "
    "The system will synthesize these factors to evaluate how your achievement profile impacts the competitiveness of your future application, "
    "providing an authoritative diagnostic tier and a continuous optimization roadmap."
)

with st.form("master_profile_form"):
    st.subheader("Phase 1: Input Profile Matrix")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Academic & Institutional Foundations**")
        gpa = st.slider("Internal Academic Performance (Scaled/Normalized GPA out of 100)", 50, 100, 85)
        sat_act = st.slider("Standardized Testing Percentile (SAT/ACT Equivalent)", 50, 100, 90)
        school_tier = st.selectbox(
            "High School Institutional Context",
            ["Tier 1: Established International Feeder School", 
             "Tier 2: Competitive Regional/National Board School", 
             "Tier 3: Non-Traditional / Local Infrastructure School"]
        )
        target_tier = st.selectbox(
            "Target University Selective Threshold",
            ["Tier 1 Ultra-Selective (Ivy League / Top 5)",
             "Tier 2 Highly Selective (Top 15 - 30)",
             "Tier 3 Competitive Targets (Top 31 - 60)"]
        )

    with col2:
        st.markdown("**Extracurricular & Specialized Spike Validation**")
        ec_breadth = st.slider("Extracurricular Activity Depth & Leadership Scale", 1, 10, 6)
        spike_validation = st.slider("Specialized Vertical Spike Validation (External/Research Hooks)", 1, 10, 5)
        
        st.markdown("**Target Optimization & Client Profile Survey**")
        intended_major = st.text_input("Intended Academic Major / Discipline (e.g., Quantitative Economics, CS)")
        financial_factor = st.radio("Are financial aid/cost considerations a deciding factor in your list strategy?", ["No", "Yes"])

    submit_button = st.form_submit_button(label="Generate Profile Assessment & Strategic Roadmap")

# ==========================================
# 4. MATH SYNTHESIS ENGINE & DYNAMIC ROUTER
# ==========================================
if submit_button:
    st.markdown("---")
    st.subheader("Phase 2: Clinical Diagnostic Output")
    
    # Mathematical integration of user selections
    school_multiplier = 10 if "Tier 1" in school_tier else (5 if "Tier 2" in school_tier else 0)
    raw_score = (gpa * 0.4) + (sat_act * 0.3) + (ec_breadth * 1.5) + (spike_validation * 1.5) + school_multiplier
    final_score = min(100.0, max(0.0, raw_score))
    
    # Router logic matching final indices to strategic arrays
    if final_score >= 90:
        content = STRATEGIC_BINS["bin_1"]
    elif final_score >= 75:
        content = STRATEGIC_BINS["bin_2"]
    elif final_score >= 60:
        content = STRATEGIC_BINS["bin_3"]
    elif final_score >= 45:
        content = STRATEGIC_BINS["bin_4"]
    elif final_score >= 30:
        content = STRATEGIC_BINS["bin_5"]
    else:
        content = STRATEGIC_BINS["bin_6"]
        
    threshold_map = {
        "Tier 1 Ultra-Selective": 90,
        "Tier 2 Highly Selective": 75,
        "Tier 3 Competitive Targets": 60
    }
    selected_target_clean = target_tier.split(" (")[0]
    target_threshold = threshold_map.get(selected_target_clean, 75)
    variance = final_score - target_threshold

    st.markdown(f"### Current Diagnostic Status: **{content['tier']}**")
    
    st.markdown(f"""
        <div class="metric-box">
            <h4 style='margin:0; color:#ff4b4b;'>Synthesized Profile Competitiveness Index: {final_score:.1f} / 100</h4>
            <p style='margin:5px 0 0 0; font-size:0.9rem; color:#fafafa;'>Target Match Variance for {selected_target_clean}: <b>{variance:+.1f} points</b></p>
        </div>
    """, unsafe_content_html=True)
    
    st.markdown("#### Strategic Profile Evaluation")
    for bullet in content["bullets"]:
        st.markdown(f"* {bullet}")
        
    st.markdown("#### Tactical Action Plan & Optimization Roadmap")
    st.success(content["roadmap"])
    
    st.markdown("#### Target Match Optimization Note")
    if variance < 0:
        st.warning(
            f"Your current calculated profile index sits below the historical median threshold for {selected_target_clean}. "
            f"To optimize this action plan and bridge this {abs(variance):.1f}-point deficit, you must execute the "
            "recommended roadmap steps with immediate, maximum intensity over the coming academic cycle."
        )
    else:
        st.info(
            f"Your profile mathematically aligns with or outpaces the baseline selective requirements for {selected_target_clean}. "
            "Your operational priority must shift from metric accumulation to minimizing risk of yield-protection "
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
