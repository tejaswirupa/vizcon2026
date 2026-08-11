import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="The Hidden Cost on Your Plate", page_icon="🌾", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background-color: #0a0a1a; }
.main { background-color: #0a0a1a; }
[data-testid="stSidebar"] { background-color: #0d0d2b; border-right: 1px solid #2d2d5e; }
section[data-testid="stSidebar"] * { color: #ffffff !important; font-weight: 700 !important; }
[data-testid="stSidebarNav"] a { color: #ffffff !important; font-weight: 700 !important; border-radius: 8px; padding: 0.4rem 0.8rem; display: block; }
[data-testid="stSidebarNav"] a:hover { background-color: #1a1a3e !important; }
[data-testid="stSidebarNav"] a[aria-selected="true"] { background-color: #e74c3c !important; }
.chapter-tag { color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; margin-bottom:0.3rem; }
.page-title { font-size:2.5rem; font-weight:900; color:#ffffff; line-height:1.2; margin:0.5rem 0 0.3rem 0; }
.page-subtitle { font-size:1.1rem; color:#a0aec0; margin-bottom:0.5rem; line-height:1.6; }
.page-context { font-size:1rem; color:#cbd5e0; margin-bottom:1.5rem; line-height:1.8; background:linear-gradient(135deg,#0d0d2b,#1a1a3e); border-radius:10px; padding:1.2rem 1.5rem; border:1px solid #2d2d5e; }
.insight-box { background:linear-gradient(135deg,#1a3a2a,#2d5a3e); border-left:4px solid #2ecc71; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.warning-box { background:linear-gradient(135deg,#3a1a1a,#5e2d2d); border-left:4px solid #e74c3c; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.info-box { background:linear-gradient(135deg,#1a2a3a,#2d3d5e); border-left:4px solid #3498db; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.purple-box { background:linear-gradient(135deg,#1a1a3a,#2d2d5a); border-left:4px solid #9b59b6; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.gold-box { background:linear-gradient(135deg,#2a1a00,#3d2d00); border-left:4px solid #f39c12; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; text-align:center; }
.fact-num { font-size:2rem; font-weight:900; }
.fact-label { color:#a0aec0; font-size:0.85rem; margin-top:0.3rem; line-height:1.4; }
.divider { height:2px; background:linear-gradient(90deg,#e74c3c,#3498db,#2ecc71); margin:1.5rem 0; border-radius:2px; }
.source-bar { color:#718096; font-size:0.82rem; text-align:center; margin-top:1rem; padding:0.8rem; background:#0d0d2b; border-radius:8px; }
h1, h2, h3, h4 { color: #ffffff !important; }
p { color: #cbd5e0; }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("""<div style="text-align:center; padding:0.8rem 0;">
        <div style="font-size:2.2rem">🌍</div>
        <div style="color:#ffffff; font-weight:900; font-size:1rem; margin-top:0.4rem">Same 24 Hours</div>
        <div style="color:#a0aec0; font-size:0.78rem">Very Different Planets</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""<div style="color:#a0aec0; font-size:0.78rem; line-height:1.6; padding:0.3rem">
        An 8-chapter data story on daily life, sustainability, and happiness across 10 countries.<br><br>
        <strong style="color:#ffffff">10 countries · 47 metrics · 30+ years</strong>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""<div style="font-size:0.75rem; line-height:1.7; padding:0.3rem; color:#a0aec0;">
        <strong style="color:#ffffff">Author</strong><br>
        Tejaswi Neelapu<br>
        Business Analyst · Amazon<br><br>
        <a href="https://www.linkedin.com/in/tejaswirupa/" target="_blank"
           style="color:#3498db; text-decoration:none;">🔗 LinkedIn</a><br>
        <a href="https://github.com/tejaswirupa" target="_blank"
           style="color:#3498db; text-decoration:none;">💻 GitHub</a>
    </div>""", unsafe_allow_html=True)


st.markdown('<div class="chapter-tag">Chapter 03 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🌾 The Hidden Cost on Your Plate</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Every meal you eat has a carbon price tag. Most of us never see the bill — but the planet does, every single day.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="page-context">The global food system — from field to fork — is one of the largest contributors to
greenhouse gas emissions on Earth. This chapter breaks down agrofood emissions by country across six
components: food transport, household consumption, retail, processing, fertilizer manufacturing, and
agricultural waste.<br><br>
The scale is staggering. The USA generated over <strong style="color:#ffffff">1 million kilotons
of CO2-equivalent</strong> from its food system in 2020 alone. Brazil, despite lower per-capita
consumption, tops total emissions due to deforestation-linked cattle farming.
India, despite having the world's largest vegetarian population,
still generates significant emissions through rice cultivation and crop burning.<br><br>
<strong style="color:#ffffff">What we eat</strong> — and how that food is grown, transported, and wasted —
is one of the most powerful levers any individual has for reducing their planetary footprint.</div>""", unsafe_allow_html=True)

col_list = st.columns(4)
col_list[0].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#f39c12">1M kt</div>
    <div class="fact-label">USA total agrofood CO2 emissions in 2020</div>
</div>""", unsafe_allow_html=True)
col_list[1].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#f39c12">🇧🇷 #1</div>
    <div class="fact-label">Brazil — highest total due to deforestation & cattle</div>
</div>""", unsafe_allow_html=True)
col_list[2].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#f39c12">10x gap</div>
    <div class="fact-label">USA food emissions vs India per capita</div>
</div>""", unsafe_allow_html=True)
col_list[3].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#f39c12">30%</div>
    <div class="fact-label">Of global emissions linked to the food system</div>
</div>""", unsafe_allow_html=True)

st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)

st.markdown("""<div class="gold-box">
    <div style="color:#f39c12; font-weight:700; margin-bottom:0.5rem">Key Insight</div>
    <div style="color:#e0e0e0; font-size:1rem; line-height:1.8"><strong style="color:#ffffff">Your plate is political.</strong>
Switching to a plant-based diet is estimated to reduce an individual's food-related carbon footprint
by up to 73%. Yet across our 10 countries, only ~27% of respondents follow a vegetarian or vegan diet.
The countries with the highest food emissions — USA, Canada, Australia — also have the lowest rates
of plant-based eating. <strong style="color:#ffffff">The highest-impact daily choice most people never make.</strong></div>
</div>""", unsafe_allow_html=True)



st.markdown("---")
components.iframe("https://public.tableau.com/views/VizCon2026-FoodEmissions/FoodEmissions?:embed=yes&:showVizHome=no&:toolbar=yes", height=650, scrolling=True)
st.markdown("---")
st.markdown("""<div class="source-bar">Source: Agrofood CO2 Emissions Dataset — FAO data 1990–2020 · 
    <a href="https://public.tableau.com/views/VizCon2026-FoodEmissions/FoodEmissions" target="_blank" style="color:#3498db">Open in Tableau ↗</a></div>""",
    unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.75rem; text-align:center; margin-top:1.5rem;">
    Built by Tejaswi Neelapu for VizCon 2026 ·
    <a href="https://www.linkedin.com/in/tejaswirupa/" style="color:#3498db">LinkedIn</a> ·
    <a href="https://github.com/tejaswirupa" style="color:#3498db">GitHub</a>
</div>""", unsafe_allow_html=True)
