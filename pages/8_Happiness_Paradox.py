import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="The Happiness Paradox", page_icon="😊", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0a0a1a; }
    .main { background-color: #0a0a1a; }
    [data-testid="stSidebar"] { background-color: #0d0d2b; }
    .chapter-tag { color:#f39c12; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; }
    .page-title { font-size:2.8rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0; }
    .page-subtitle { font-size:1.2rem; color:#a0aec0; margin-bottom:1.5rem; }
    .hero-insight { background:linear-gradient(135deg,#2a1a3a,#3d2d5e); 
                    border:2px solid #f39c12; border-radius:12px; 
                    padding:2rem; margin:1.5rem 0; text-align:center; }
    .hero-text { font-size:1.4rem; color:#ffffff; font-weight:600; line-height:1.6; }
    .fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; 
                 border-radius:12px; padding:1.2rem; text-align:center; }
    .fact-num { font-size:2rem; font-weight:900; color:#f39c12; }
    .fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; }
    .conclusion-box { background:linear-gradient(135deg,#1a2a1a,#2d3d2d); 
                      border:1px solid #2ecc71; border-radius:12px; 
                      padding:2rem; margin:1.5rem 0; }
    .final-cta { background:linear-gradient(135deg,#3a1a1a,#5e2d2d); 
                 border:2px solid #e74c3c; border-radius:12px; 
                 padding:1.5rem; margin:1rem 0; text-align:center; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">⭐ Final Chapter — The Big Reveal</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">😊 The Happiness Paradox</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">After 7 chapters of data, we arrive at the most important question of our time.</div>', unsafe_allow_html=True)

st.markdown('''<div class="hero-insight">
    <div class="hero-text">
        "The happiest countries need up to 5 Earths to sustain their lifestyle.<br>
        The only sustainable country has the lowest happiness score.<br><br>
        <span style="color:#f39c12">Can we be happy AND sustainable?<br>
        Or are we forced to choose?</span>"
    </div>
</div>''', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">🇦🇺 7.0</div>
        <div class="fact-label">Happiness Score<br>3.83 Earths needed</div>
    </div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">🇧🇷 6.6</div>
        <div class="fact-label">Happiness Score<br>1.69 Earths — Sweet Spot!</div>
    </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">🇨🇦 6.8</div>
        <div class="fact-label">Happiness Score<br>4.91 Earths needed 🔴</div>
    </div>''', unsafe_allow_html=True)
with col4:
    st.markdown('''<div class="fact-card">
        <div class="fact-num">🇮🇳 4.7</div>
        <div class="fact-label">Happiness Score<br>0.69 Earths — Sustainable</div>
    </div>''', unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-TheHappinessParadox/TheHappinessParadox?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=700, scrolling=True
)

st.markdown("---")

st.markdown('''<div class="conclusion-box">
    <div style="color:#2ecc71; font-weight:700; font-size:1.1rem; margin-bottom:1rem">
        🌱 The Answer: Brazil Points the Way
    </div>
    <div style="color:#a0d9b4; font-size:1rem; line-height:1.8">
        Brazil sits closest to the intersection of happiness and sustainability — 
        decent happiness (6.55) with a relatively low footprint (1.69 Earths). 
        It's not perfect, but it suggests a third path exists.<br><br>
        <strong style="color:#ffffff">The world doesn't have to choose between 
        happiness and sustainability. But it requires rethinking what happiness 
        actually means — less consumption, more connection. 
        Less flying, more living.</strong>
    </div>
</div>''', unsafe_allow_html=True)

st.markdown('''<div class="final-cta">
    <div style="color:#e74c3c; font-weight:700; font-size:1.1rem; margin-bottom:0.5rem">
        ⚡ The Call to Action
    </div>
    <div style="color:#f5a0a0; font-size:1rem; line-height:1.6">
        Every day you make thousands of choices. What you eat. How you commute. 
        What you buy. Where you travel. <strong style="color:#ffffff">
        The data shows those choices add up to either 0.69 Earths or 4.9 Earths. 
        The gap between those two numbers is your daily life.</strong>
    </div>
</div>''', unsafe_allow_html=True)

st.markdown('''<div style="color:#718096; font-size:0.85rem; text-align:center; margin-top:2rem">
    Source: Global Ecological Footprint 2023 + World Happiness Report 2024 · 
    <a href="https://public.tableau.com/views/VizCon2026-TheHappinessParadox/TheHappinessParadox" 
    style="color:#3498db">View in Tableau ↗</a><br><br>
    Built for VizCon 2026 · 
    Data: Global Lifestyle Survey, World Happiness Report, Global Ecological Footprint, 
    SDG Index, Agrofood CO2, OECD Meat Consumption · 
    Powered by Streamlit + Tableau + Python + Orcha AI
</div>''', unsafe_allow_html=True)

if st.button("← Back to Beginning", type="secondary"):
    st.switch_page("app.py")
