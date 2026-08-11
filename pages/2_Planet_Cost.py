import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="How Many Earths Does Your Country Need?", page_icon="🌍", layout="wide")

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background-color: #0a0a1a; }
.main { background-color: #0a0a1a; }
[data-testid="stSidebar"] { background-color: #0d0d2b; border-right: 1px solid #2d2d5e; }
section[data-testid="stSidebar"] * { color: #ffffff !important; font-weight: 700 !important; }
[data-testid="stSidebarNav"] a { color: #ffffff !important; font-weight: 700 !important; }
.chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; }
.page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0 0.3rem 0; }
.page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:0.5rem; line-height:1.6; }
.page-context { font-size:1rem; color:#cbd5e0; margin-bottom:1.5rem; line-height:1.8; background:linear-gradient(135deg,#0d0d2b,#1a1a3e); border-radius:10px; padding:1.2rem 1.5rem; border:1px solid #2d2d5e; }
.warning-box { background:linear-gradient(135deg,#3a1a1a,#5e2d2d); border-left:4px solid #e74c3c; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; text-align:center; }
.fact-num { font-size:2rem; font-weight:900; color:#e74c3c; }
.fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; line-height:1.4; }
.divider { height:2px; background:linear-gradient(90deg,#e74c3c,#3498db,#2ecc71); margin:1.5rem 0; border-radius:2px; }
.source-bar { color:#718096; font-size:0.82rem; text-align:center; margin-top:1rem; padding:0.8rem; background:#0d0d2b; border-radius:8px; }
h1, h2, h3, h4 { color: #ffffff !important; }
p { color: #cbd5e0; }
</style>""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""<div style="text-align:center; padding:0.8rem 0;">
        <div style="font-size:2.2rem">🌍</div>
        <div style="color:#ffffff; font-weight:900; font-size:1rem; margin-top:0.4rem;">Same 24 Hours</div>
        <div style="color:#a0aec0; font-size:0.78rem;">Very Different Planets</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""<div style="color:#a0aec0; font-size:0.78rem; line-height:1.6; padding:0.3rem;">
        An 8-chapter data story on daily life, sustainability, and happiness across 10 countries.<br><br>
        <strong style="color:#ffffff;">10 countries · 47 metrics · 30+ years</strong>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""<div style="font-size:0.75rem; line-height:1.7; padding:0.3rem; color:#a0aec0;">
        <strong style="color:#ffffff;">Author</strong><br>
        Tejaswi Neelapu<br>Business Analyst · Amazon<br><br>
        <a href="https://www.linkedin.com/in/tejaswirupa/" target="_blank" style="color:#3498db; text-decoration:none;">🔗 LinkedIn</a><br>
        <a href="https://github.com/tejaswirupa" target="_blank" style="color:#3498db; text-decoration:none;">💻 GitHub</a>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="chapter-tag">Chapter 02 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🌍 How Many Earths Does Your Country Need?</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">If everyone on Earth lived like your country does today, how many planets would we need? The answer should stop you in your tracks.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="page-context">
    The Ecological Footprint measures how much of Earth's regenerative capacity a country consumes —
    expressed as "Earths required." A score of 1.0 means living within planetary limits.
    Anything above 1.0 means we are borrowing against the future.<br><br>
    Of the 10 countries in this study,
    <strong style="color:#ffffff;">only one — India — lives within planetary limits</strong>
    at just 0.69 Earths. Every other country is in ecological debt.
    Canada tops the chart at 4.9 Earths, meaning if all 8 billion humans lived like Canadians,
    we would need nearly <strong style="color:#ffffff;">5 planets</strong> to sustain us.<br><br>
    The chart below tells a story of stark inequality — not just in wealth, but in
    <strong style="color:#e74c3c;">planetary consumption</strong>. The world's most comfortable
    nations are also its most ecologically destructive. This is not a coincidence.
    High consumption is what comfort looks like in 2024 — and comfort has a planetary price tag
    that future generations will be forced to pay.
</div>""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="fact-card"><div class="fact-num">4.9x 🇨🇦</div>
    <div class="fact-label">Earths needed if everyone lived like Canada</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="fact-card"><div class="fact-num">3.8x 🇦🇺</div>
    <div class="fact-label">Earths needed if everyone lived like Australia</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="fact-card"><div class="fact-num" style="color:#f39c12;">1.69x 🇧🇷</div>
    <div class="fact-label">Brazil — closest to sustainable prosperity</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="fact-card"><div class="fact-num" style="color:#2ecc71;">0.69x 🇮🇳</div>
    <div class="fact-label">India — the only truly sustainable country</div></div>""", unsafe_allow_html=True)

st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
st.markdown("""<div class="warning-box">
    <div style="color:#e74c3c; font-weight:700; margin-bottom:0.5rem;">Key Insight — We Have One Planet. But We Live as if We Have Five.</div>
    <div style="color:#f5a0a0; font-size:1rem; line-height:1.8;">
        The ecological footprint data reveals a brutal truth: the world's wealthiest, most comfortable
        nations are also the ones most deeply in ecological debt. Canada, Australia, and the USA
        collectively need between 3.8 and 4.9 Earths each — meaning their lifestyle is only possible
        by consuming planetary resources faster than they can regenerate.
        This debt is not abstract. It is being paid right now in the form of biodiversity collapse,
        ocean acidification, aquifer depletion, and accelerating climate change.
        <strong style="color:#ffffff;">The bill is being sent to future generations — and they did not order this meal.</strong>
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-PlanetCost/PlanetCost?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)
st.markdown("---")
st.markdown("""<div class="source-bar">Source: Global Ecological Footprint Network 2023 — 182 countries ·
    <a href="https://public.tableau.com/views/VizCon2026-PlanetCost/PlanetCost" target="_blank" style="color:#3498db;">Open in Tableau ↗</a>
</div>""", unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.75rem; text-align:center; margin-top:1.5rem;">
    Built by Tejaswi Neelapu for VizCon 2026 ·
    <a href="https://www.linkedin.com/in/tejaswirupa/" style="color:#3498db;">LinkedIn</a> ·
    <a href="https://github.com/tejaswirupa" style="color:#3498db;">GitHub</a>
</div>""", unsafe_allow_html=True)
