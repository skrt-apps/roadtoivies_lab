import streamlit as st

st.set_page_config(
    page_title="Activity Impact Grader | RoadToIvies", 
    page_icon="🔥", 
    layout="wide"
)

# Custom Dark Professional CSS Styling (Matching the Suite Identity)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stHeading h1 { color: #ff4b4b; font-family: 'Helvetica Neue', sans-serif; }
    .metric-box { background-color: #1e222b; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    .delta-card { background-color: #161b22; padding: 15px; border-radius: 8px; margin-bottom: 12px; border-left: 4px solid #ff4b4b; }
    </style>
""", unsafe_allow_html=True)

st.title("🔥 The Activity Impact Grader")
st.subheader("Profile Delta: Differentiating 'Spike' Execution from School-Level Volatility")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🛠️ Profile & Extracurricular Inputs")
    
    intended_major = st.selectbox(
        "Intended Major Cluster",
        ["Computer Science / Data Science", "Engineering / Physics", "Economics / Finance", "Pre-Med / Biology", "Humanities / Arts"]
    )
    
    st.markdown("**Select Your Highest-Impact Core Activity (The Primary 'Spike' Candidate):**")
    activity_tier = st.radio(
        "Activity Execution Level",
        [
            "Tier 4 (Sovereign): Elite Independent Validation (e.g., SSP, RSI, First-Author Peer-Reviewed Research, Founder of active revenue-generating entity)",
            "Tier 3 (Elite): University-Specific Feeder Program (e.g., UPenn M&T Summer, Stanford SIMR) or High-Impact Independent Technical Project/Codebase",
            "Tier 2 (Competitive): School Leadership (Student Council Captain, Club President), State/National sports, standard corporate internships",
            "Tier 1 (Generic): Passive Member of School Clubs, Model UN delegate, standard local NGO volunteering"
        ]
    )
    
    narrative_alignment = st.radio(
        "Does your highest-tier activity directly match your Intended Major Cluster?",
        ["Yes, perfect linear alignment (e.g., Economics Major + Independent Market Architecture/Quant Models)", 
         "No, it is a general leadership/humanities activity unrelated to my core STEM/Quant track"]
    )
    
    st.markdown("---")
    st.markdown("### 🏫 The High School Context Filter (Localized Competition)")
    cohort_competition = st.selectbox(
        "How many peers from your immediate graduating class are applying to the same top-tier universities with the same major?",
        ["Solo Applicant (I am the only major contender from my school this cycle)",
         "Moderate Competition (1-2 other competitive peers applying with a similar direction)",
         "Hyper-Saturated Cohort (3+ top-tier peers applying simultaneously from my school)"]
    )

# --- SCORECARD ENGINE ---
base_ec_score = 30
tier_points = 0
alignment_multiplier = 1.0
cohort_penalty = 0

# 1. Activity Tier Weights
if "Tier 4" in activity_tier:
    tier_points = 50
elif "Tier 3" in activity_tier:
    tier_points = 35
elif "Tier 2" in activity_tier:
    tier_points = 15
else:
    tier_points = 5

# 2. Narrative Alignment Coefficient (Multi-collinearity protection)
if "perfect linear alignment" in narrative_alignment:
    alignment_multiplier = 1.2
else:
    alignment_multiplier = 0.7  # Harsh penalty for incoherent profiles

# 3. High School Context Filter Weights (Calibrated to School Profile Quotas)
if "Hyper-Saturated" in cohort_competition:
    cohort_penalty = -25  # The "Zero-Sum Gladiator" school cap penalty
elif "Moderate Competition" in cohort_competition:
    cohort_penalty = -10
else:
    cohort_penalty = 10  # Solo applicant premium

# Compute Final Profile Score
raw_profile_score = (base_ec_score + tier_points) * alignment_multiplier + cohort_penalty
final_profile_score = max(1, min(100, int(raw_profile_score)))

# --- DISPLAY OUTPUT ---
with col2:
    st.markdown("### 📊 Extracurricular Diagnostic Output")
    
    if final_profile_score >= 75:
        st.success("🎯 PROFILE STATUS: HIGH-IMPACT SPIKE")
        ec_status = "Your profile demonstrates systemic, independently verified authority. You have successfully decoupled yourself from standard school-level activities and established a distinct strategic niche."
    elif final_profile_score >= 45:
        st.warning("⚠️ PROFILE STATUS: THE GENERIC ALL-ROUNDER RISK")
        ec_status = "Your profile is highly competitive on paper but lacks an undeniable 'Spike.' You risk being viewed as interchangeable with other high-achieving peers in your local cohort."
    else:
        st.error("🚨 PROFILE STATUS: INCOHERENT / HIGHLY VOLATILE")
        ec_status = "Critical structural vulnerability. The application profile is highly exposed to localized cohort caps or lacks the narrative alignment required to survive the international filter."

    # Visual Score Display
    st.markdown(f"""
    <div class="metric-box">
        <p style="margin:0; font-size:14px; color:#8b949e;">Profile Cohesion Index</p>
        <h1 style="margin:0; font-size:48px; color:#ff4b4b;">{final_profile_score}/100</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write(ec_status)
    
    st.markdown("---")
    st.markdown("### 🔬 Strategic Engineering Advice")
    
    # Dynamic logic feedback
    if "Hyper-Saturated" in cohort_competition:
        st.markdown(f'<div class="delta-card">⚠️ **The High School Cap Alert:** Because you are in a hyper-saturated cohort, standard excellence is a trap. If a peer has an internal university-specific hook or a domestic citizenship advantage, you risk being bottlenecked by institutional quotas. You must pivot your positioning entirely away from what your school peers are executing.</div>', unsafe_allow_html=True)
        
    if alignment_multiplier < 1.0:
        st.markdown(f'<div class="delta-card">⚠️ **Narrative Alignment Gap:** Your highest-value activity does not back up your stated major cluster. Admissions committees at elite levels look for extreme subject-level specialization. A student whose best achievement is unrelated to their major looks fragmented under evaluation.</div>', unsafe_allow_html=True)
        
    if "Tier 1" in activity_tier or "Tier 2" in activity_tier:
        st.markdown(f'<div class="delta-card">💡 **Actionable Task:** To shift this index above 75, school-based leadership is insufficient. You need an immediate external validator: an independent, deployable technical project, a public-facing codebase, or verified academic research outside of your school framework.</div>', unsafe_allow_html=True)

    if final_profile_score >= 75 and "Solo" in cohort_competition:
        st.info("✨ Optimal Extracurricular Standing. You hold a clear runway with zero localized competition and high individual profile leverage. Focus entirely on maintaining this absolute differentiation in your written essays.")
