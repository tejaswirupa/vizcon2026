import streamlit as st

st.set_page_config(
    page_title="Same 24 Hours. Very Different Planets.",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .main { background-color: #0a0a1a; }
    .stApp { background-color: #0a0a1a; }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        color: #ffffff;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        color: #a0aec0;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    .stat-box {
        background: linear-gradient(135deg, #1a1a3e, #2d2d5e);
        border: 1px solid #4a4a8a;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.5rem;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 900;
        color: #e74c3c;
    }
    .stat-label {
        font-size: 0.85rem;
        color: #a0aec0;
        margin-top: 0.3rem;
    }
    .chapter-card {
        background: linear-gradient(135deg, #1a1a3e, #2d2d5e);
        border: 1px solid #4a4a8a;
        border-radius: 12px;
        padding: 1.2rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    .chapter-card:hover {
        border-color: #e74c3c;
        transform: translateX(5px);
    }
    .chapter-number {
        font-size: 0.8rem;
        color: #e74c3c;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .chapter-title {
        font-size: 1.1rem;
        color: #ffffff;
        font-weight: 600;
        margin-top: 0.3rem;
    }
    .divider {
        height: 2px;
        background: linear-gradient(90deg, #e74c3c, #3498db, #2ecc71);
        margin: 2rem 0;
        border-radius: 2px;
    }
    .insight-box {
        background: linear-gradient(135deg, #1a3a2a, #2d5a3e);
        border-left: 4px solid #2ecc71;
        border-radius: 8px;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
    }
    .insight-text {
        color: #a0d9b4;
        font-size: 1rem;
        line-height: 1.6;
    }
    [data-testid="stSidebar"] {
        background-color: #0d0d2b;
        border-right: 1px solid #2d2d5e;
    }
    .sidebar-title {
        color: #ffffff;
        font-weight: 700;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('''<div style="text-align:center; padding: 1rem 0;">
        <div style="font-size:2.5rem">🌍</div>
        <div style="color:#ffffff; font-weight:700; font-size:1rem; margin-top:0.5rem">
            Same 24 Hours
        </div>
        <div style="color:#a0aec0; font-size:0.8rem">Very Different Planets</div>
    </div>''', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('''<div style="color:#a0aec0; font-size:0.8rem; padding:0.5rem">
        Navigate the story using the pages below. Each chapter reveals a new layer 
        of how daily life shapes our planet.
    </div>''', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('''<div style="color:#a0aec0; font-size:0.75rem; padding:0.5rem">
        📊 Data Sources<br>
        • Global Lifestyle Survey<br>
        • World Happiness Report 2024<br>
        • Global Ecological Footprint 2023<br>
        • SDG Index 2000-2022<br>
        • Agrofood CO2 Emissions<br>
        • OECD Meat Consumption
    </div>''', unsafe_allow_html=True)

# ── Hero Section ──────────────────────────────────────────────────────────
st.markdown('''
<div style="padding: 3rem 0 2rem 0;">
    <div class="hero-title">Same 24 Hours.<br>Very Different Planets.</div>
    <div class="hero-subtitle">
        8 billion people wake up every day and make thousands of tiny choices.<br>
        Most of us never think twice. But these invisible daily habits, 
        multiplied by billions,<br>are either healing or harming our world.
    </div>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Key Stats ─────────────────────────────────────────────────────────────
st.markdown('<div style="color:#ffffff; font-size:1.2rem; font-weight:600; margin-bottom:1rem">The Numbers That Should Shock You</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('''<div class="stat-box">
        <div class="stat-number">4.9x</div>
        <div class="stat-label">Earths needed if everyone<br>lived like Canada</div>
    </div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="stat-box">
        <div class="stat-number">0.69</div>
        <div class="stat-label">Earths needed if everyone<br>lived like India</div>
    </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="stat-box">
        <div class="stat-number">9/10</div>
        <div class="stat-label">Countries living beyond<br>planetary limits</div>
    </div>''', unsafe_allow_html=True)
with col4:
    st.markdown('''<div class="stat-box">
        <div class="stat-number">+2.45°C</div>
        <div class="stat-label">Temperature rise already<br>in France & Germany</div>
    </div>''', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Story Chapters ────────────────────────────────────────────────────────
st.markdown('<div style="color:#ffffff; font-size:1.2rem; font-weight:600; margin-bottom:1rem">📖 The Story — 8 Chapters</div>', unsafe_allow_html=True)

chapters = [
    ("01", "🕐", "How the World Spends Its Day", "We all have 24 hours — but we spend them very differently"),
    ("02", "🌍", "How Many Earths Does Your Country Need?", "The hidden planetary cost of where you were born"),
    ("03", "🌾", "The Hidden Cost on Your Plate", "Food systems are quietly destroying the planet"),
    ("04", "🎯", "Where the World Is Failing", "The SDG scorecard that should scare us all"),
    ("05", "🌱", "What Are We Actually Doing About It?", "The uncomfortable gap between impact and action"),
    ("06", "🌡️", "The Bill is Already Here", "Temperature is rising — and we caused it"),
    ("07", "📈", "Are We Getting Better or Worse?", "Happiness trends across 18 years of data"),
    ("08", "😊", "The Happiness Paradox", "The most surprising finding — happiness vs sustainability"),
]

col1, col2 = st.columns(2)
for i, (num, emoji, title, desc) in enumerate(chapters):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f'''<div class="chapter-card">
            <div class="chapter-number">Chapter {num}</div>
            <div class="chapter-title">{emoji} {title}</div>
            <div style="color:#718096; font-size:0.85rem; margin-top:0.3rem">{desc}</div>
        </div>''', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Key Insight ───────────────────────────────────────────────────────────
st.markdown('''<div class="insight-box">
    <div style="color:#2ecc71; font-weight:700; margin-bottom:0.5rem">💡 The Central Finding</div>
    <div class="insight-text">
        The only country living within planetary limits is India — with 0.69 Earths required. 
        But India also has the lowest happiness score of all 10 countries studied. 
        Every other nation is overshooting. The question this project asks: 
        <strong style="color:#ffffff">Can the world be happy AND sustainable? 
        Or are we forced to choose?</strong>
    </div>
</div>''', unsafe_allow_html=True)

st.markdown('''<div style="color:#718096; font-size:0.8rem; text-align:center; margin-top:2rem">
    Built for VizCon 2026 · Data: Global Lifestyle Survey, World Happiness Report, 
    Global Ecological Footprint, SDG Index, Agrofood CO2, OECD · 
    Powered by Streamlit + Tableau + Python
</div>''', unsafe_allow_html=True)
