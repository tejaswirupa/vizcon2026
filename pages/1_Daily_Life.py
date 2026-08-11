import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="How the World Spends Its Day", page_icon="🕐", layout="wide")

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
.info-box { background:linear-gradient(135deg,#1a2a3a,#2d3d5e); border-left:4px solid #3498db; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; text-align:center; }
.fact-num { font-size:2rem; font-weight:900; color:#3498db; }
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

st.markdown('<div class="chapter-tag">Chapter 01 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">🕐 How the World Spends Its Day</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">We all have exactly 24 hours. Yet the way we fill them — and the planetary cost of those choices — differs dramatically across the globe.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="page-context">
    What does a typical day look like for someone in India versus Canada? In Japan versus Brazil?
    Across 10,000 survey respondents spanning 10 countries, this chapter examines the building blocks
    of daily life — how much we sleep, how often we exercise, how long we stare at screens,
    how far we commute, and how many times we board a plane each year.<br><br>
    The first surprise: <strong style="color:#ffffff;">our routines are eerily similar</strong>.
    Sleep hours, exercise frequency, and screen time are nearly identical across wildly different
    cultures and income levels. The second surprise: despite nearly identical routines, the
    <strong style="color:#ffffff;">carbon cost of those routines varies significantly</strong>
    between countries — driven by energy sources, transport infrastructure, and consumption habits
    that are largely invisible in day-to-day life.<br><br>
    This chapter sets the stage for the rest of the story: if we all live roughly the same way,
    why do some countries need 5 Earths while others need less than 1?
</div>""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="fact-card"><div class="fact-num">7.0 hrs</div>
    <div class="fact-label">Average sleep — nearly identical across all 10 countries</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="fact-card"><div class="fact-num">6.5 hrs</div>
    <div class="fact-label">Daily screen time — we are all glued to our devices</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="fact-card"><div class="fact-num">3 days</div>
    <div class="fact-label">Exercise frequency per week — remarkably consistent globally</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="fact-card"><div class="fact-num">30 min</div>
    <div class="fact-label">Average commute — varies most between countries</div></div>""", unsafe_allow_html=True)

st.markdown('<div style="height:0.5rem"></div>', unsafe_allow_html=True)
st.markdown("""<div class="info-box">
    <div style="color:#3498db; font-weight:700; margin-bottom:0.5rem;">Key Insight — The Sameness Surprise</div>
    <div style="color:#a0c4d8; font-size:1rem; line-height:1.8;">
        Despite oceans, cultures, and income gaps separating them, people in Australia, India, Japan,
        Brazil, and the USA sleep the same amount, exercise at the same frequency, and spend the same
        hours on screens each day. Our daily routines are nearly identical.
        The real difference lies not in <em>how</em> we live —
        but in the invisible <strong style="color:#ffffff;">planetary cost</strong> of how we live.
        This is what makes the sustainability crisis so hard to solve: it is not a lifestyle problem.
        It is a systemic and structural one.
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-Same24Hours/Same24Hours?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=650, scrolling=True
)
st.markdown("---")
st.markdown("""<div class="source-bar">Source: Global Mental Health & Lifestyle Survey — 10,000 respondents, 10 countries ·
    <a href="https://public.tableau.com/views/VizCon2026-Same24Hours/Same24Hours" target="_blank" style="color:#3498db;">Open in Tableau ↗</a>
</div>""", unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.75rem; text-align:center; margin-top:1.5rem;">
    Built by Tejaswi Neelapu for VizCon 2026 ·
    <a href="https://www.linkedin.com/in/tejaswirupa/" style="color:#3498db;">LinkedIn</a> ·
    <a href="https://github.com/tejaswirupa" style="color:#3498db;">GitHub</a>
</div>""", unsafe_allow_html=True)
