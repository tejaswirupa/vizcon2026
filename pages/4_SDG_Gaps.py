import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SDG Gaps", page_icon="🎯", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a1a; }
    .main { background-color: #0a0a1a; }
    [data-testid="stSidebar"] { background-color: #0d0d2b; }
    .chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; }
    .page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0; }
    .page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:1.5rem; }
    .insight-box { background:linear-gradient(135deg,#1a1a3a,#2d2d5a); border-left:4px solid #9b59b6; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
    .fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; text-align:center; }
    .fact-num { font-size:2rem; font-weight:900; color:#9b59b6; }
    .fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">Chapter 04</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🎯 Where the World Is Failing</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">The UN Sustainable Development Goals are a global report card. Here is how our 10 countries score.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class="fact-card"><div class="fact-num">83.4</div>
        <div class="fact-label">🇩🇪 Germany — highest SDG overall score</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="fact-card"><div class="fact-num">63.4</div>
        <div class="fact-label">🇮🇳 India — lowest SDG overall score</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="fact-card"><div class="fact-num">16.9</div>
        <div class="fact-label">🇦🇺 Australia — worst Climate Action score</div></div>""", unsafe_allow_html=True)

st.markdown("""<div class="insight-box">
    <div style="color:#9b59b6; font-weight:700; margin-bottom:0.5rem">📋 The Scorecard Nobody Wants to See</div>
    <div style="color:#d7a0f5; font-size:1rem; line-height:1.6">
        The richer the country, the worse it scores on Climate Action and Responsible Consumption.
        <strong style="color:#ffffff">Australia scores just 16.9/100 on Climate Action.</strong>
        Meanwhile India scores 94.3. The pattern is clear: wealth enables destruction.
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-SDGGaps/SDGGaps?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)
st.markdown("---")
st.markdown("""<div style="color:#718096; font-size:0.85rem; text-align:center">
    Source: SDG Index 2000-2022
</div>""", unsafe_allow_html=True)
