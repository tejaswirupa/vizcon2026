import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Are We Getting Better or Worse?", page_icon="📈", layout="wide")

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


st.markdown('<div class="chapter-tag">Chapter 07 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">📈 Are We Getting Better or Worse?</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">18 years of happiness data. Consumption keeps rising. Emissions keep rising. But are we actually getting any happier?</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="page-context">The World Happiness Report has tracked happiness scores across countries since 2005,
using the Cantril Ladder — a 0 to 10 scale where respondents rate their lives.
This chapter plots happiness trends for all 10 countries from 2005 to 2023,
revealing what nearly two decades of rising consumption, rising emissions, and
rising inequality has done to human wellbeing.<br><br>
The answer is sobering: <strong style="color:#ffffff">almost nothing</strong>.
Happiness scores have remained remarkably flat across most nations despite significant
economic growth and rising consumption. The brief dip visible around
<strong style="color:#ffffff">2020 captures the COVID-19 effect</strong> — a stark reminder
that happiness is fragile and deeply tied to social connection, not material consumption.<br><br>
India has remained consistently at the bottom of the happiness rankings — a reflection of
persistent poverty and inequality, not a failure of culture or values.</div>""", unsafe_allow_html=True)

col_list = st.columns(4)
col_list[0].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#3498db">7.03</div>
    <div class="fact-label">Australia 2023 — highest happiness score</div>
</div>""", unsafe_allow_html=True)
col_list[1].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#3498db">4.68</div>
    <div class="fact-label">India 2023 — lowest happiness score</div>
</div>""", unsafe_allow_html=True)
col_list[2].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#3498db">Flat 📊</div>
    <div class="fact-label">Most countries: barely changed since 2005</div>
</div>""", unsafe_allow_html=True)
col_list[3].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#3498db">📉 2020</div>
    <div class="fact-label">COVID-19 dip visible in nearly every country</div>
</div>""", unsafe_allow_html=True)

st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)

st.markdown("""<div class="info-box">
    <div style="color:#3498db; font-weight:700; margin-bottom:0.5rem">Key Insight</div>
    <div style="color:#e0e0e0; font-size:1rem; line-height:1.8"><strong style="color:#ffffff">We are consuming more, emitting more, and living no happier.</strong>
Since 2005, global consumption has risen dramatically. Carbon emissions have grown.
Ecological footprints have deepened. Yet happiness scores have barely moved.
This raises the most uncomfortable question of the entire project:
<strong style="color:#ffffff">if rising consumption does not make us happier,
what exactly are we destroying the planet for?</strong>
The data suggests we may have confused comfort with joy, and accumulation with fulfilment.</div>
</div>""", unsafe_allow_html=True)



st.markdown("---")
components.iframe("https://public.tableau.com/views/VizCon2026-HappinessTrend/HappinessTrend?:embed=yes&:showVizHome=no&:toolbar=yes", height=650, scrolling=True)
st.markdown("---")
st.markdown("""<div class="source-bar">Source: World Happiness Report 2024 — Gallup World Poll 2005–2023 · 
    <a href="https://public.tableau.com/views/VizCon2026-HappinessTrend/HappinessTrend" target="_blank" style="color:#3498db">Open in Tableau ↗</a></div>""",
    unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.75rem; text-align:center; margin-top:1.5rem;">
    Built by Tejaswi Neelapu for VizCon 2026 ·
    <a href="https://www.linkedin.com/in/tejaswirupa/" style="color:#3498db">LinkedIn</a> ·
    <a href="https://github.com/tejaswirupa" style="color:#3498db">GitHub</a>
</div>""", unsafe_allow_html=True)
