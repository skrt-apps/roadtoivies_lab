import streamlit as st

st.set_page_config(
    page_title="Ivy Delta Simulator | RoadToIvies", 
    page_icon="📈", 
    layout="wide"
)

# Custom Dark Professional CSS Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stHeading h1 { color: #ff4b4b; font-family: 'Helvetica Neue', sans-serif; }
    .metric-box { background-color: #1e222b; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    .delta-card { background-color: #161b22; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #ff4b4b; }
    </style>
""", unsafe_allow_html=True)

st.title("📈 The Ivy Delta Simulator")
st.subheader("Hard Filter Diagnostic: Academics & Demographic Pool Risk")
st.markdown("---")

# Two-Column Layout for Input vs Output
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🛠️ Profile Inputs")
    
    # 1. Academic Baseline
    sat_score = st.slider("Target or Current SAT Score", 1000, 1600, 1520, step=10)
    
    rigor = st.selectbox(
        "Course Rigor (APs / IB Higher Levels / Advanced Curricula)",
        ["Maximum Rigor (4-5+ APs, or school-maximum advanced track with 4 HLs)", 
         "Standard/Average Rigor for elite international schools"]
    )
    
    # 2. Demographic & Quota Risk
    demographic_pool = st.radio(
        "Applicant Pool & Major Category",
        ["International Applicant - Bengaluru STEM", 
         "International Applicant - Non-STEM / Humanities", 
         "US Citizen / Domestic Applicant Pool"]
    )
    
    st.markdown("---")
    st.markdown("### 🏆 Institutional Validation")
    # 3. Independent "Spike" Multiplier
    has_elite_summer = st.checkbox(
        "Accepted to an Elite Independent Research or University Feeder Program (e.g., SSP, UPenn M&T Summer, RSI)"
    )

# --- SCORECARD ENGINE (Expert Judgment Scorecard Framework) ---
base_score = 50
academic_points = 0
pool_points = 0
rigor_points = 0
validation_points = 0

# 1. SAT Binning Logic
if sat_score >= 1570:
    academic_points = 40
elif sat_score >= 1530:
    academic_points = 25  # Competitive baseline for T20
else:
    academic_points = -20 # Severe automated filter risk for Indian STEM

# 2. Curriculum Rigor Weights
if "Maximum Rigor" in rigor:
    rigor_points = 15

# 3. Demographic Pool Density Scaling
if demographic_pool == "International Applicant - Bengaluru STEM":
    pool_points = -40  # Maximum pool density penalty
elif demographic_pool == "International Applicant - Non-STEM / Humanities":
    pool_points = -15
else:
    pool_points = 10   # Domestic processing pool advantage

# 4. Institutional Validation Offset
if has_elite_summer:
    validation_points = 45 # The "Spike" asset that neutralizes demographic risk

# Compute Final Matrix Sum
total_score = base_score + academic_points + pool_points + rigor_points + validation_points
final_index = max(1, min(100, total_score))

# --- REAL-TIME DISPLAY ENGINE ---
with col2:
    st.markdown("### 📊 Diagnostic Output")
    
    # Status Determination Thresholds
    if final_index >= 70:
        st.success("🟢 STATUS: SURVIVED FIRST CUT")
        status_text = "The profile metrics successfully surpass the base filters. Your application possesses enough quantitative weight to clear automated screeners and reach a human admissions officer's desk for holistic review."
    elif final_index >= 45:
        st.warning("⚠️ STATUS: HIGH POOL RISK")
        status_text = "The profile is caught in the 'International Filter' danger zone. Due to the extreme density of the Bengaluru/Indian applicant pool, standard academic excellence is neutralized by pure peer volume."
    else:
        st.error("🔴 STATUS: FILTERED OUT")
        status_text = "Critical structural risk. Historical data patterns indicate a high probability of automated rejection or immediate triage before qualitative or essay-based evaluation occurs."

    # Visual Score Display
    st.markdown(f"""
    <div class="metric-box">
        <p style="margin:0; font-size:14px; color:#8b949e;">Filter Clearance Index</p>
        <h1 style="margin:0; font-size:48px; color:#ff4b4b;">{final_index}/100</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write(status_text)
    
    st.markdown("---")
    st.markdown("### 📉 Quantitative Delta Report")
    
    # Dynamic Advisory Generator
    deltas = []
    
    if sat_score < 1570:
        needed = 1570 - sat_score
        deltas.append(f"**Academic Delta:** Your current score leaves you mathematically vulnerable. In the hyper-competitive international pool, you need a +{needed} point delta to consistently bypass automated cutoffs without relying on institutional hooks.")
        
    if "Maximum Rigor" not in rigor:
        deltas.append("**Curriculum Delta:** Your course configuration lacks the maximum structural weight required by elite admissions matrices. You must actively optimize your curriculum with advanced certifications (like APs or maximizing HL points) to match the cohort baseline.")
        
    if demographic_pool == "International Applicant - Bengaluru STEM" and not has_elite_summer:
        deltas.append("**Demographic Delta:** Competing as an unhooked Indian STEM applicant means standard perfection behaves like a zero-point variable. Because your baseline demographics act as a severe penalty multiplier (-40 points), you require immediate independent validation—such as an elite tier-4 research program or a deployable technical project—to shift the needle.")

    if not deltas:
        st.info("✨ Optimal Quantitative Foundation. The academic, rigor, and validation parameters are maxed out. Your core structural risk is cleared—your execution strategy must now focus entirely on positioning and narrative cohesion.")
    else:
        for delta in deltas:
            st.markdown(f'<div class="delta-card">{delta}</div>', unsafe_allow_html=True)
