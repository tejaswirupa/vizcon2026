import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Food Emissions", page_icon="🌾", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a1a; }
    .main { background-color: #0a0a1a; }
    [data-testid="stSidebar"] { background-color: #0d0d2b; }
    .chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; }
    .page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0; }
    .page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:1.5rem; }
    .insight-box { background:linear-gradient(135deg,#1a3a1a,#2d5a2d); border-left:4px solid #f39c12; 
                   border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
    .fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; 
                 border-radius:12px; padding:1.2rem; text-align:center; }
    .fact-num { font-size:2rem; font-weight:900; color:#f39c12; }
    .fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">Chapter 03</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🌾 The Hidden Cost on Your Plate</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Every meal you eat has a carbon price tag. Most of us never see the bill — but the planet does.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">1M kt</div>
        <div class="fact-label">🇺🇸 USA total agrofood<br>emissions in 2020</div>
    </div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">10x</div>
        <div class="fact-label">USA food emissions vs<br>India per capita</div>
    </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">🇧🇷</div>
        <div class="fact-label">Brazil highest total — driven<br>by deforestation & cattle</div>
    </div>''', unsafe_allow_html=True)

st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)
st.markdown('''<div class="insight-box">
    <div style="color:#f39c12; font-weight:700; margin-bottom:0.5rem">🍽️ Food for Thought</div>
    <div style="color:#fde8a0; font-size:1rem; line-height:1.6">
        The food on your plate travels thousands of miles, gets processed in energy-hungry 
        factories, sits in refrigerated retail stores, and generates massive waste at home. 
        <strong style="color:#ffffff">Changing what you eat is the single highest-impact 
        daily choice you can make for the planet.</strong> Yet most countries are barely trying.
    </div>
</div>''', unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-FoodEmissions/FoodEmissions?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)

st.markdown("---")
st.markdown('''<div style="color:#718096; font-size:0.85rem; text-align:center">
    Source: Agrofood CO2 Emissions Dataset (1990-2020) · 
    <a href="https://public.tableau.com/views/VizCon2026-FoodEmissions/FoodEmissions" style="color:#3498db">View in Tableau ↗</a>
</div>''', unsafe_allow_html=True)
col1, col2 = st.columns([4,1])
with col2:
    if st.button("Next Chapter →", type="primary"):
        st.switch_page("pages/4_🎯_SDG_Gaps.py")
