import streamlit as st

st.set_page_config(
    page_title="RoadToIvies | Admissions Lab",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Dark/Professional Accent Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stHeading h1 { color: #ff4b4b; font-family: 'Helvetica Neue', sans-serif; }
    .expert-note { background-color: #1e222b; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 RoadToIvies: The Admissions Lab")
st.subheader("Quantitative Profile Scorecards for HNW STEM Applicants")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Welcome to the Architecture Stage
    Most college counseling relies on subjective opinions and backward-looking essay editing. 
    **The Admissions Lab** uses a judgment-based credit scorecard framework—similar to institutional risk modeling—to decompose your student's profile into completely independent, orthogonal variables.
    
    By stripping out overlapping variance, we isolate the true signals that elite admissions committees use to filter out international applicants.
    
    #### 🛠️ Available Diagnostic Tools (Select in the Sidebar):
    1. **The Ivy Delta Simulator:** Measures hard filters (Academics + Demographic Pool Risk).
    2. **The Activity Impact Grader:** Isolates your subject-level delta (The "Spike" vs. the "All-Rounder").
    """)
    
    st.markdown("""
    <div class="expert-note">
    <strong>Founder's Note:</strong> At schools like UC Berkeley, Stanford, and the Ivies, the 'International Filter' captures 95% of applicants before an essay is ever read. This lab calculates whether you survive the cut.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.metric(label="Calculated Filter Rigor (Bengaluru STEM)", value="98.4%", delta="Top 1.6% Only")
    st.info("💡 Navigate using the sidebar to run a real-time scorecard diagnostic on your current profile metrics.")
