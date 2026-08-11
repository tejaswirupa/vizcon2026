import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="The Happiness Paradox", page_icon="😊", layout="wide")

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
.warning-box { background:linear-gradient(135deg,#3a1a1a,#5e2d2d); border-left:4px solid #e74c3c; border-radius:8px; padding:1.2rem 1.5rem; margin:1rem 0; }
.hero-insight { background:linear-gradient(135deg,#2a1a3a,#3d2d5e); border:2px solid #f39c12; border-radius:12px; padding:2rem; margin:1.5rem 0; text-align:center; }
.conclusion-box { background:linear-gradient(135deg,#1a2a1a,#2d3d2d); border:1px solid #2ecc71; border-radius:12px; padding:2rem; margin:1.5rem 0; }
.cta-box { background:linear-gradient(135deg,#3a1a1a,#5e2d2d); border:2px solid #e74c3c; border-radius:12px; padding:1.5rem; margin:1rem 0; text-align:center; }
.about-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.5rem; text-align:center; }
.fact-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; text-align:center; }
.fact-num { font-size:2rem; font-weight:900; }
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

st.markdown('<div class="chapter-tag">Chapter 08 of 8 · The Big Reveal</div>', unsafe_allow_html=True)
st.markdown('<div class="page-title">😊 The Happiness Paradox</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">After 7 chapters of evidence, we arrive at the most important question of our time — and the most surprising answer in the data.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown("""<div class="page-context">
    This final chapter brings everything together in a single scatter plot:
    <strong style="color:#ffffff;">Happiness Score (y-axis) vs Earths Required (x-axis)</strong>
    for all 10 countries.<br><br>
    If sustainability and happiness were compatible, we would expect to see countries clustered
    in the top-left quadrant — high happiness, low footprint. What we actually find is almost
    the opposite: <strong style="color:#e74c3c;">the happiest countries cluster in the top-right</strong>
    — high happiness, high ecological cost. The red dashed line at x=1.0 marks the planetary boundary.
    Every country to the right of that line is borrowing against the future.<br><br>
    India sits alone to the left — the only sustainable country — but also at the bottom of
    the happiness axis. Brazil offers the closest thing to hope: moderate happiness (6.55) with
    a relatively low footprint (1.69 Earths). It is imperfect. But it points toward a
    <strong style="color:#2ecc71;">third path</strong> — one the world has not yet chosen to take.
</div>""", unsafe_allow_html=True)

st.markdown("""<div class="hero-insight">
    <div style="font-size:1.3rem; color:#ffffff; font-weight:600; line-height:1.7;">
        The happiest countries need up to 5 Earths to sustain their lifestyle.<br>
        The only sustainable country has the lowest happiness score.<br><br>
        <span style="color:#f39c12; font-size:1.6rem; font-weight:900;">
        Can we be happy AND sustainable?<br>Or are we forced to choose?</span>
    </div>
</div>""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="fact-card">
        <div class="fact-num" style="color:#f39c12;">🇦🇺 7.0</div>
        <div class="fact-label">Happiness — but needs 3.83 Earths</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="fact-card">
        <div class="fact-num" style="color:#2ecc71;">🇧🇷 6.6</div>
        <div class="fact-label">Happiness — only 1.69 Earths (The Sweet Spot)</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="fact-card">
        <div class="fact-num" style="color:#e74c3c;">🇨🇦 6.8</div>
        <div class="fact-label">Happiness — but needs 4.91 Earths</div>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="fact-card">
        <div class="fact-num" style="color:#3498db;">🇮🇳 4.7</div>
        <div class="fact-label">Happiness — only 0.69 Earths (Most Sustainable)</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")
components.iframe(
    "https://public.tableau.com/views/VizCon2026-TheHappinessParadox/TheHappinessParadox?:embed=yes&:showVizHome=no&:toolbar=yes",
    height=700, scrolling=True
)
st.markdown("---")

st.markdown("""<div class="conclusion-box">
    <div style="color:#2ecc71; font-weight:700; font-size:1.1rem; margin-bottom:0.8rem;">The Answer: Brazil Points the Way</div>
    <div style="color:#a0d9b4; font-size:1rem; line-height:1.8;">
        Brazil sits closest to the intersection of happiness and sustainability —
        decent happiness (6.55) with a relatively low footprint (1.69 Earths).
        It is not perfect. But it proves a third path exists.<br><br>
        The world does not have to choose between happiness and a liveable planet.
        But it requires a fundamental rethinking of what happiness actually means —
        <strong style="color:#ffffff;">less consumption, more connection.
        Less flying, more living. Less accumulation, more meaning.</strong><br><br>
        The data from 10 countries and 18 years of happiness research points to
        the same uncomfortable conclusion: <strong style="color:#ffffff;">we have been
        chasing the wrong things — and the planet has been paying the price.</strong>
    </div>
</div>""", unsafe_allow_html=True)

st.markdown("""<div class="cta-box">
    <div style="color:#e74c3c; font-weight:700; font-size:1.1rem; margin-bottom:0.5rem;">The Call to Action</div>
    <div style="color:#f5a0a0; font-size:1rem; line-height:1.7;">
        Every day you make thousands of choices. What you eat. How you commute. What you buy. Where you fly.
        <strong style="color:#ffffff;">The data shows those choices add up to either 0.69 Earths or 4.9 Earths.
        The gap between those two numbers is your daily life.</strong><br><br>
        The question this project leaves you with is not what governments should do.
        It is what <strong style="color:#ffffff;">you</strong> will do tomorrow morning —
        with your same 24 hours.
    </div>
</div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown('<div style="color:#ffffff; font-size:1.1rem; font-weight:700; margin-bottom:0.8rem; text-align:center;">About the Author</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""<div class="about-card">
        <div style="font-size:2rem; margin-bottom:0.5rem;">👩💻</div>
        <div style="color:#ffffff; font-weight:900; font-size:1.2rem;">Tejaswi Neelapu</div>
        <div style="color:#a0aec0; font-size:0.88rem; margin:0.3rem 0 1rem 0;">
            Business Analyst · WFM Strategy & Business Dev<br>Amazon · Seattle, WA
        </div>
        <a href="https://www.linkedin.com/in/tejaswirupa/" target="_blank"
           style="display:inline-block; padding:0.5rem 1.5rem; background:#0077b5;
           border-radius:8px; color:#ffffff; font-weight:700; font-size:0.9rem;
           text-decoration:none; margin:0.3rem;">🔗 LinkedIn</a>
        <a href="https://github.com/tejaswirupa" target="_blank"
           style="display:inline-block; padding:0.5rem 1.5rem; background:#24292e;
           border-radius:8px; color:#ffffff; font-weight:700; font-size:0.9rem;
           text-decoration:none; margin:0.3rem; border:1px solid #4a4a8a;">💻 GitHub</a>
        <div style="color:#718096; font-size:0.78rem; margin-top:1rem; line-height:1.6;">
            Built for VizCon 2026 · Python + Tableau + Streamlit + Orcha AI
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.75rem; text-align:center; margin-top:1.5rem; line-height:1.8;">
    Data Sources: Global Lifestyle Survey · World Happiness Report 2024 · Global Ecological Footprint 2023 ·
    SDG Index 2000-2022 · Agrofood CO2 Emissions · OECD Meat Consumption ·
    <a href="https://github.com/tejaswirupa/vizcon2026" style="color:#3498db;">Full citations on GitHub</a>
</div>""", unsafe_allow_html=True)
