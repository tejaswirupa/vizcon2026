import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Temperature", page_icon="🌡️", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a1a; }
    .main { background-color: #0a0a1a; }
    [data-testid="stSidebar"] { background-color: #0d0d2b; }
    .chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; }
    .page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0; }
    .page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:1.5rem; }
    .insight-box { background:linear-gradient(135deg,#3a1a1a,#5e2d2d); border-left:4px solid #e74c3c; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
    .fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; text-align:center; }
    .fact-num { font-size:2rem; font-weight:900; color:#e74c3c; }
    .fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">Chapter 06</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🌡️ The Bill is Already Here</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Climate change is not a future problem. The temperature is already rising — and our daily choices are a major driver.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""<div class="fact-card"><div class="fact-num">+2.45°C</div>
        <div class="fact-label">France and Germany already at +2.45°C</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="fact-card"><div class="fact-num">1.5°C</div>
        <div class="fact-label">Paris Agreement limit already being breached</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="fact-card"><div class="fact-num">+0.57°C</div>
        <div class="fact-label">India — lowest rise yet most vulnerable</div></div>""", unsafe_allow_html=True)

st.markdown("""<div class="insight-box">
    <div style="color:#e74c3c; font-weight:700; margin-bottom:0.5rem">🔥 The Cruel Irony</div>
    <div style="color:#f5a0a0; font-size:1rem; line-height:1.6">
        The countries warming fastest are wealthy nations most insulated from consequences.
        Meanwhile India, warming slowest, faces the most devastating climate impacts.
        <strong style="color:#ffffff">Those who caused it least suffer the most.</strong>
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-TemperatureWake-up/TemperatureWake-up?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)
st.markdown("---")
st.markdown("""<div style="color:#718096; font-size:0.85rem; text-align:center">
    Source: Agrofood CO2 Emissions Dataset
</div>""", unsafe_allow_html=True)
