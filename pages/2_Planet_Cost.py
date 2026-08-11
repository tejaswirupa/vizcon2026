import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Planet Cost", page_icon="🌍", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a1a; }
    .main { background-color: #0a0a1a; }
    [data-testid="stSidebar"] { background-color: #0d0d2b; }
    .chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; 
                   text-transform:uppercase; letter-spacing:3px; }
    .page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0; }
    .page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:1.5rem; }
    .insight-box { background:linear-gradient(135deg,#3a1a1a,#5e2d2d); 
                   border-left:4px solid #e74c3c; border-radius:8px; 
                   padding:1.2rem 1.5rem; margin:1rem 0; }
    .fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); 
                 border:1px solid #4a4a8a; border-radius:12px; 
                 padding:1.2rem; text-align:center; }
    .fact-num { font-size:2rem; font-weight:900; color:#e74c3c; }
    .fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">Chapter 02</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🌍 How Many Earths Does Your Country Need?</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">If everyone on Earth lived like your country, how many planets would we need? The answer is alarming.</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">4.9x</div>
        <div class="fact-label">🇨🇦 Canada<br>Most planets needed</div>
    </div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">0.69x</div>
        <div class="fact-label">🇮🇳 India<br>Only sustainable country</div>
    </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">9/10</div>
        <div class="fact-label">Countries overshooting<br>planetary limits</div>
    </div>''', unsafe_allow_html=True)
with col4:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">1.69x</div>
        <div class="fact-label">🇧🇷 Brazil<br>The sweet spot country</div>
    </div>''', unsafe_allow_html=True)

st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)
st.markdown('''<div class="insight-box">
    <div style="color:#e74c3c; font-weight:700; margin-bottom:0.5rem">🔴 Wake-Up Call</div>
    <div style="color:#f5a0a0; font-size:1rem; line-height:1.6">
        We only have ONE planet. But if everyone lived like Canadians, 
        we would need <strong style="color:#ffffff">5 Earths</strong>. 
        Like Australians? <strong style="color:#ffffff">4 Earths</strong>. 
        The map below shows the true planetary cost of how we live — 
        darker red means deeper in ecological debt.
    </div>
</div>''', unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-PlanetCost/PlanetCost?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)

st.markdown("---")
st.markdown('''<div style="color:#718096; font-size:0.85rem; text-align:center">
    Source: Global Ecological Footprint 2023 · 
    <a href="https://public.tableau.com/views/VizCon2026-PlanetCost/PlanetCost" 
    style="color:#3498db">View in Tableau ↗</a>
</div>''', unsafe_allow_html=True)

col1, col2 = st.columns([4,1])
with col2:
    if st.button("Next Chapter →", type="primary"):
        st.switch_page("pages/3_🌾_Food_Emissions.py")
