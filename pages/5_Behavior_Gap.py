import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Behavior Gap", page_icon="🌱", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a1a; }
    .main { background-color: #0a0a1a; }
    [data-testid="stSidebar"] { background-color: #0d0d2b; }
    .chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; }
    .page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0; }
    .page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:1.5rem; }
    .insight-box { background:linear-gradient(135deg,#1a3a2a,#2d5a3d); border-left:4px solid #2ecc71; 
                   border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
    .fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; 
                 border-radius:12px; padding:1.2rem; text-align:center; }
    .fact-num { font-size:2rem; font-weight:900; color:#2ecc71; }
    .fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">Chapter 05</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🌱 What Are We Actually Doing About It?</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">We know the planet is in trouble. So what actions are people actually taking in their daily lives? The answer is sobering.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">~27%</div>
        <div class="fact-label">Average vegetarian/vegan<br>diet across all countries</div>
    </div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">Low</div>
        <div class="fact-label">EV ownership still very low<br>in most countries studied</div>
    </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">Gap 📉</div>
        <div class="fact-label">Big difference between<br>awareness and action</div>
    </div>''', unsafe_allow_html=True)

st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)
st.markdown('''<div class="insight-box">
    <div style="color:#2ecc71; font-weight:700; margin-bottom:0.5rem">🌿 The Action Gap</div>
    <div style="color:#a0d9b4; font-size:1rem; line-height:1.6">
        Despite knowing climate change is real, individual sustainable behaviors remain low. 
        Countries that need to act most — high footprint nations like Canada and Australia — 
        show the lowest rates of plant-based diets and green transport adoption. 
        <strong style="color:#ffffff">Knowledge without action is just guilt.</strong>
    </div>
</div>''', unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-BehaviorGap/BehaviorGap?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)

st.markdown("---")
st.markdown('''<div style="color:#718096; font-size:0.85rem; text-align:center">
    Source: Global Lifestyle Survey Dataset · 
    <a href="https://public.tableau.com/views/VizCon2026-BehaviorGap/BehaviorGap" style="color:#3498db">View in Tableau ↗</a>
</div>''', unsafe_allow_html=True)
col1, col2 = st.columns([4,1])
with col2:
    if st.button("Next Chapter →", type="primary"):
        st.switch_page("pages/6_🌡️_Temperature.py")
