import streamlit as st

st.set_page_config(
    page_title="Same 24 Hours. Very Different Planets.",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

<style>
.hero-title { font-size:3.8rem; font-weight:900; color:#ffffff; line-height:1.05; margin-bottom:0.5rem; }
.hero-sub { font-size:1.25rem; color:#a0aec0; margin-bottom:0.3rem; font-weight:300; line-height:1.7; }
.stat-box { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.5rem; text-align:center; }
.stat-number { font-size:2.4rem; font-weight:900; color:#e74c3c; }
.stat-label { font-size:0.82rem; color:#a0aec0; margin-top:0.3rem; line-height:1.4; }
.chapter-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.2rem; margin:0.4rem 0; }
.chapter-number { color:#e74c3c; font-size:0.78rem; font-weight:700; text-transform:uppercase; letter-spacing:2px; }
.chapter-title { font-size:1rem; color:#ffffff; font-weight:600; margin-top:0.2rem; }
.chapter-desc { font-size:0.82rem; color:#718096; margin-top:0.2rem; line-height:1.4; }
.about-card { background:linear-gradient(135deg,#1a1a3e,#2d2d5e); border:1px solid #4a4a8a; border-radius:12px; padding:1.5rem; text-align:center; }
.social-btn { display:inline-block; padding:0.5rem 1.2rem; border-radius:8px; font-weight:700; font-size:0.9rem; text-decoration:none; margin:0.3rem; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""<div style="text-align:center; padding:1rem 0;">
        <div style="font-size:2.8rem">🌍</div>
        <div style="color:#ffffff; font-weight:900; font-size:1.1rem; margin-top:0.5rem">Same 24 Hours</div>
        <div style="color:#a0aec0; font-size:0.85rem; margin-top:0.2rem">Very Different Planets</div>
        <div style="color:#718096; font-size:0.75rem; margin-top:0.2rem">VizCon 2026</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""<div style="color:#a0aec0; font-size:0.82rem; padding:0.5rem; line-height:1.6;">
        <strong style="color:#ffffff">About this project</strong><br>
        An 8-chapter data story exploring how daily life across 10 countries connects
        to sustainability, happiness, and planetary health.<br><br>
        <strong style="color:#ffffff">Navigate</strong> using the pages above
        or scroll down to explore the full story arc.
    </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""<div style="color:#a0aec0; font-size:0.78rem; padding:0.5rem; line-height:1.7;">
        <strong style="color:#ffffff">Data Sources</strong><br>
        Global Lifestyle Survey<br>
        World Happiness Report 2024<br>
        Global Ecological Footprint 2023<br>
        SDG Index 2000–2022<br>
        Agrofood CO2 Emissions<br>
        OECD Meat Consumption<br>
        Sustainable Energy Dataset<br><br>
        <strong style="color:#ffffff">Built with</strong><br>
        Python · Tableau Public<br>
        Streamlit · Orcha AI
    </div>""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────
st.markdown("""<div style="padding:2.5rem 0 1.5rem 0;">
    <div style="color:#e74c3c; font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:3px; margin-bottom:0.5rem">VizCon 2026 · Data Storytelling</div>
    <div class="hero-title">Same 24 Hours.<br>Very Different Planets.</div>
    <div class="hero-sub">
        8 billion people wake up every day and make thousands of tiny choices —<br>
        what to eat, how to travel, how much energy to use.<br>
        Most of us never think twice. But these invisible daily habits,<br>
        multiplied by billions, are either healing or harming our world.
    </div>
</div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Shock Stats ───────────────────────────────────────────────────────────
st.markdown('<div style="color:#ffffff; font-size:1.2rem; font-weight:700; margin-bottom:1rem">The Numbers That Should Shock You</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""<div class="stat-box"><div class="stat-number">4.9x</div>
    <div class="stat-label">Earths needed if everyone<br>lived like Canada</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="stat-box"><div class="stat-number" style="color:#2ecc71">0.69x</div>
    <div class="stat-label">Earths needed if everyone<br>lived like India</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="stat-box"><div class="stat-number">9/10</div>
    <div class="stat-label">Countries living beyond<br>planetary limits</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="stat-box"><div class="stat-number" style="color:#f39c12">+2.45°C</div>
    <div class="stat-label">Temperature rise already<br>in France & Germany</div></div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Project Context ───────────────────────────────────────────────────────
st.markdown('<div style="color:#ffffff; font-size:1.2rem; font-weight:700; margin-bottom:0.8rem">What This Project Is About</div>', unsafe_allow_html=True)
st.markdown("""<div class="page-context">
    This project was built for <strong style="color:#ffffff">VizCon 2026</strong> under the theme
    <em>"How the World Lives, Thrives, and Connects"</em>. It takes the lens of
    <strong style="color:#ffffff">daily life and sustainability</strong> — exploring whether the way we live
    each day is compatible with a planet that can sustain us.<br><br>
    Using <strong style="color:#ffffff">9 datasets</strong> merged into a single long-format analytical file
    covering <strong style="color:#ffffff">10 countries, 47 metrics, and 30+ years of data</strong>,
    this story follows a deliberate arc: from the mundane (how we sleep, eat, commute)
    to the profound (what those choices cost the planet and whether they even make us happier).<br><br>
    The central question: <strong style="color:#e74c3c">Can the world be happy AND sustainable —
    or are we forced to choose?</strong>
</div>""", unsafe_allow_html=True)

# ── Story Chapters ────────────────────────────────────────────────────────
st.markdown('<div style="color:#ffffff; font-size:1.2rem; font-weight:700; margin-bottom:0.8rem">The 8-Chapter Story</div>', unsafe_allow_html=True)
chapters = [
    ("01", "🕐", "How the World Spends Its Day", "Daily routines across 10 countries — sleep, exercise, screen time, commute. Surprisingly similar."),
    ("02", "🌍", "How Many Earths Does Your Country Need?", "A world map of ecological footprints. Most countries are deep in planetary debt."),
    ("03", "🌾", "The Hidden Cost on Your Plate", "Food production and consumption emissions broken down by country. The plate has a price."),
    ("04", "🎯", "Where the World Is Failing", "The UN SDG scorecard for 10 countries. Wealthy nations fail on climate and consumption."),
    ("05", "🌱", "What Are We Actually Doing About It?", "Plant-based diets, EV ownership, recycling rates. The gap between impact and action."),
    ("06", "🌡️", "The Bill is Already Here", "Temperature change 1990–2020. The Paris Agreement limit is already being breached."),
    ("07", "📈", "Are We Getting Better or Worse?", "18 years of happiness trends. Consumption rises. Happiness stays flat."),
    ("08", "😊", "The Happiness Paradox", "The hero chart: happiness vs earths required. The most surprising finding of the project."),
]
col1, col2 = st.columns(2)
for i, (num, emoji, title, desc) in enumerate(chapters):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""<div class="chapter-card">
            <div class="chapter-number">Chapter {num}</div>
            <div class="chapter-title">{emoji} {title}</div>
            <div class="chapter-desc">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Central Finding ───────────────────────────────────────────────────────
st.markdown("""<div class="insight-box">
    <div style="color:#2ecc71; font-weight:700; font-size:1rem; margin-bottom:0.5rem">The Central Finding</div>
    <div style="color:#a0d9b4; font-size:1rem; line-height:1.8;">
        The only country living within planetary limits is <strong style="color:#ffffff">India — 0.69 Earths</strong>.
        But India also has the <strong style="color:#ffffff">lowest happiness score (4.68/10)</strong> of all countries studied.
        Meanwhile <strong style="color:#ffffff">Canada needs 4.9 Earths</strong> yet sits comfortably in the "Happy" tier.
        <strong style="color:#ffffff">Brazil emerges as the sweet spot</strong> — decent happiness (6.55) with a relatively
        low footprint (1.69 Earths). The data suggests a third path exists —
        but the world has to want it.
    </div>
</div>""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── About Me ──────────────────────────────────────────────────────────────
st.markdown('<div style="color:#ffffff; font-size:1.2rem; font-weight:700; margin-bottom:0.8rem">About the Author</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""<div class="about-card">
        <div style="font-size:2.5rem; margin-bottom:0.5rem">👩💻</div>
        <div style="color:#ffffff; font-weight:900; font-size:1.3rem">Tejaswi Neelapu</div>
        <div style="color:#a0aec0; font-size:0.9rem; margin:0.3rem 0 1rem 0">
            Business Analyst · WFM Strategy & Business Dev<br>
            Amazon · Seattle, WA
        </div>
        <div style="margin-top:1rem;">
            <a href="https://www.linkedin.com/in/tejaswirupa/" target="_blank"
               style="display:inline-block; padding:0.5rem 1.5rem; background:#0077b5;
               border-radius:8px; color:#ffffff; font-weight:700; font-size:0.9rem;
               text-decoration:none; margin:0.3rem;">
               🔗 LinkedIn
            </a>
            <a href="https://github.com/tejaswirupa" target="_blank"
               style="display:inline-block; padding:0.5rem 1.5rem; background:#24292e;
               border-radius:8px; color:#ffffff; font-weight:700; font-size:0.9rem;
               text-decoration:none; margin:0.3rem; border:1px solid #4a4a8a;">
               💻 GitHub
            </a>
        </div>
        <div style="color:#718096; font-size:0.8rem; margin-top:1rem; line-height:1.6;">
            Built for VizCon 2026 · Powered by Python, Tableau, Streamlit & Orcha AI
        </div>
    </div>""", unsafe_allow_html=True)

st.markdown("""<div style="color:#718096; font-size:0.78rem; text-align:center; margin-top:2rem; line-height:1.8;">
    Data Sources: Global Lifestyle Survey · World Happiness Report 2024 ·
    Global Ecological Footprint 2023 · SDG Index 2000–2022 ·
    Agrofood CO2 Emissions · OECD Meat Consumption · Sustainable Energy Dataset<br>
    All datasets sourced from Kaggle · Full citations at
    <a href="https://github.com/tejaswirupa/vizcon2026" style="color:#3498db">
    github.com/tejaswirupa/vizcon2026</a>
</div>""", unsafe_allow_html=True)
