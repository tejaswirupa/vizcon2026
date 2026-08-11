import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happiness Trend", page_icon="📈", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a1a; }
    .main { background-color: #0a0a1a; }
    [data-testid="stSidebar"] { background-color: #0d0d2b; }
    .chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; }
    .page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0; }
    .page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:1.5rem; }
    .insight-box { background:linear-gradient(135deg,#1a2a3a,#2d3d5e); border-left:4px solid #3498db; 
                   border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
    .fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; 
                 border-radius:12px; padding:1.2rem; text-align:center; }
    .fact-num { font-size:2rem; font-weight:900; color:#3498db; }
    .fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">Chapter 07</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">📈 Are We Getting Better or Worse?</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">18 years of happiness data across 10 countries. As we consume more and warm the planet faster — are we at least getting happier?</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">7.03</div>
        <div class="fact-label">🇦🇺 Australia 2023<br>Highest happiness score</div>
    </div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">4.68</div>
        <div class="fact-label">🇮🇳 India 2023<br>Lowest happiness score</div>
    </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">📉 2020</div>
        <div class="fact-label">COVID dip visible<br>in almost every country</div>
    </div>''', unsafe_allow_html=True)

st.markdown('<div style="height:1.5rem"></div>', unsafe_allow_html=True)
st.markdown('''<div class="insight-box">
    <div style="color:#3498db; font-weight:700; margin-bottom:0.5rem">📊 18 Years of Data</div>
    <div style="color:#a0d4f5; font-size:1rem; line-height:1.6">
        Despite economic growth, technological advances, and rising consumption, 
        happiness scores have remained <strong style="color:#ffffff">remarkably flat</strong> 
        across most nations since 2005. We are consuming more, emitting more, 
        and using more of the planet — but we are not getting significantly happier. 
        This raises the most important question: <strong style="color:#ffffff">what are we 
        destroying the planet for?</strong>
    </div>
</div>''', unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-HappinessTrend/HappinessTrend?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)

st.markdown("---")
st.markdown('''<div style="color:#718096; font-size:0.85rem; text-align:center">
    Source: World Happiness Report 2024 (2005-2023) · 
    <a href="https://public.tableau.com/views/VizCon2026-HappinessTrend/HappinessTrend" style="color:#3498db">View in Tableau ↗</a>
</div>''', unsafe_allow_html=True)
col1, col2 = st.columns([4,1])
with col2:
    if st.button("Final Chapter →", type="primary"):
        st.switch_page("pages/8_😊_Happiness_Paradox.py")
