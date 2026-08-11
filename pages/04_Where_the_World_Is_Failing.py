import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Where the World Is Failing", page_icon="🎯", layout="wide")

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


st.markdown('<div class="chapter-tag">Chapter 04 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🎯 Where the World Is Failing</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">The United Nations set 17 Sustainable Development Goals. This is the global scorecard — and it should alarm every wealthy nation.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="page-context">The SDG Index scores countries on all 17 UN Sustainable Development Goals on a scale of 0–100.
A score of 100 means a country has fully achieved that goal. This chapter focuses on the four goals
most directly linked to daily life and sustainability:<br><br>
<strong style="color:#ffffff">Goal 12</strong> — Responsible Consumption and Production<br>
<strong style="color:#ffffff">Goal 13</strong> — Climate Action<br>
<strong style="color:#ffffff">Goal 15</strong> — Life on Land<br>
<strong style="color:#ffffff">Goal 7</strong> — Affordable and Clean Energy<br><br>
The heatmap below reveals a deeply uncomfortable pattern:
<strong style="color:#e74c3c">the richer the country, the worse it scores on climate and consumption goals</strong>.
Germany leads overall with 83.4 but scores only 55.4 on Responsible Consumption.
Australia scores a devastating <strong style="color:#e74c3c">16.9/100 on Climate Action</strong>.</div>""", unsafe_allow_html=True)

col_list = st.columns(4)
col_list[0].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#9b59b6">83.4</div>
    <div class="fact-label">Germany — highest SDG overall score</div>
</div>""", unsafe_allow_html=True)
col_list[1].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#9b59b6">63.4</div>
    <div class="fact-label">India — lowest SDG overall score</div>
</div>""", unsafe_allow_html=True)
col_list[2].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#9b59b6">16.9 🔴</div>
    <div class="fact-label">Australia — worst Climate Action (Goal 13)</div>
</div>""", unsafe_allow_html=True)
col_list[3].markdown("""<div class="fact-card">
    <div class="fact-num" style="color:#9b59b6">94.8 ✅</div>
    <div class="fact-label">India — best Responsible Consumption (Goal 12)</div>
</div>""", unsafe_allow_html=True)

st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)

st.markdown("""<div class="purple-box">
    <div style="color:#9b59b6; font-weight:700; margin-bottom:0.5rem">Key Insight</div>
    <div style="color:#e0e0e0; font-size:1rem; line-height:1.8"><strong style="color:#ffffff">Wealth enables destruction — and the data proves it.</strong>
The countries most capable of transitioning to sustainable consumption are the ones least willing to do so.
India — the poorest nation in this study — scores 94.3 on Climate Action and 94.8 on Responsible Consumption.
Not because of environmental policy, but because low income = low consumption = low emissions.
<strong style="color:#ffffff">Sustainability by necessity is not sustainability by choice.</strong>
The wealthy world needs to choose it.</div>
</div>""", unsafe_allow_html=True)



st.markdown("---")
components.iframe("https://public.tableau.com/views/VizCon2026-SDGGaps/SDGGaps?:embed=yes&:showVizHome=no&:toolbar=yes", height=650, scrolling=True)
st.markdown("---")
st.markdown("""<div class="source-bar">Source: Sustainable Development Report — SDG Index 2000–2022 · 
    <a href="https://public.tableau.com/views/VizCon2026-SDGGaps/SDGGaps" target="_blank" style="color:#3498db">Open in Tableau ↗</a></div>""",
    unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.75rem; text-align:center; margin-top:1.5rem;">
    Built by Tejaswi Neelapu for VizCon 2026 ·
    <a href="https://www.linkedin.com/in/tejaswirupa/" style="color:#3498db">LinkedIn</a> ·
    <a href="https://github.com/tejaswirupa" style="color:#3498db">GitHub</a>
</div>""", unsafe_allow_html=True)
