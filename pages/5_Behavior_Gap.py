import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="What Are We Actually Doing About It?", page_icon="🌱", layout="wide")

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
.insight-box { background:linear-gradient(135deg,#1a3a2a,#2d5a3e); border-left:4px solid #2ecc71; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; text-align:center; }
.fact-num { font-size:2rem; font-weight:900; color:#2ecc71; }
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

st.markdown('<div class="chapter-tag">Chapter 05 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🌱 What Are We Actually Doing About It?</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">We know the planet is in crisis. So what are people actually changing in their daily lives? The answer reveals a troubling gap between knowledge and action.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="page-context">
    This chapter examines three concrete individual sustainability behaviors captured in the
    lifestyle survey: the percentage of people following a plant-based or vegetarian diet,
    the percentage who own an electric vehicle, and the percentage who recycle regularly.<br><br>
    These three behaviors represent different levels of commitment and cost.
    Diet is a daily choice made three times a day — low barrier, high impact.
    Recycling is a habitual behavior — easy to adopt, moderate impact.
    EV ownership requires significant financial investment — high barrier, potentially high impact.
    Together, they paint a picture of where individuals are — and are not — willing to act.<br><br>
    The pattern that emerges is striking:
    <strong style="color:#ffffff;">the countries with the highest ecological footprints
    show the lowest rates of all three sustainable behaviors</strong>.
    Countries living furthest beyond their means are also doing the least to change course
    at the individual level. This is the behavior gap — and it is measurable,
    documented, and deeply uncomfortable.
</div>""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="fact-card"><div class="fact-num">~27%</div>
    <div class="fact-label">Average plant-based or vegan diet across all 10 countries</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="fact-card"><div class="fact-num">~26%</div>
    <div class="fact-label">Average regular recycling rate across countries</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="fact-card"><div class="fact-num" style="color:#e74c3c;">Low</div>
    <div class="fact-label">EV ownership still very low across most countries</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="fact-card"><div class="fact-num" style="color:#f39c12;">Gap 📉</div>
    <div class="fact-label">Biggest behavior gap in highest-footprint countries</div></div>""", unsafe_allow_html=True)

st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
st.markdown("""<div class="insight-box">
    <div style="color:#2ecc71; font-weight:700; margin-bottom:0.5rem;">Key Insight — Awareness Without Action Is Just Guilt</div>
    <div style="color:#a0d9b4; font-size:1rem; line-height:1.8;">
        The behavior gap is real and measurable: countries that cause the most planetary damage are
        also the ones where the fewest people adopt sustainable daily behaviors.
        This is not ignorance — global awareness of climate change is near-universal.
        It is a failure of <em>will</em>, not knowledge.<br><br>
        <strong style="color:#ffffff;">Individual action matters — but it cannot carry the weight alone.</strong>
        The data suggests that systemic change (pricing carbon, subsidizing plant-based food,
        building public transit) creates the conditions for individual action.
        Waiting for individuals to lead without systemic support is a strategy that the data shows is failing.
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-BehaviorGap/BehaviorGap?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)
st.markdown("---")
st.markdown("""<div class="source-bar">Source: Global Mental Health & Lifestyle Survey — 10,000 respondents ·
    <a href="https://public.tableau.com/views/VizCon2026-BehaviorGap/BehaviorGap" target="_blank" style="color:#3498db;">Open in Tableau ↗</a>
</div>""", unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.75rem; text-align:center; margin-top:1.5rem;">
    Built by Tejaswi Neelapu for VizCon 2026 ·
    <a href="https://www.linkedin.com/in/tejaswirupa/" style="color:#3498db;">LinkedIn</a> ·
    <a href="https://github.com/tejaswirupa" style="color:#3498db;">GitHub</a>
</div>""", unsafe_allow_html=True)
