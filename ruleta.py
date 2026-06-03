import streamlit as st
import random
import time
from postgrest import SyncPostgrestClient

st.set_page_config(
    page_title="Ruleta · Sorteo MarIA",
    page_icon="🎰",
    layout="centered",
)

st.markdown("""
<style>
/* ── Base ── */
.stApp {
    background: linear-gradient(135deg, #0f0a1a, #1a0a2e, #0f0a1a) !important;
    color: white;
}
h1, h2, h3 { text-align: center; }

/* ── Floating particles ── */
#particles {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}
#particles::before {
    content: '';
    position: absolute;
    width: 100%; height: 100%;
    animation: particleFloat 30s infinite linear;
    background:
        radial-gradient(3px 3px at 10% 20%, rgba(167,139,250,0.7), transparent),
        radial-gradient(4px 4px at 25% 55%, rgba(34,211,238,0.6), transparent),
        radial-gradient(2px 2px at 40% 10%, rgba(245,158,11,0.6), transparent),
        radial-gradient(3px 3px at 55% 70%, rgba(34,211,238,0.7), transparent),
        radial-gradient(5px 5px at 70% 30%, rgba(167,139,250,0.5), transparent),
        radial-gradient(2px 2px at 85% 85%, rgba(239,68,68,0.6), transparent),
        radial-gradient(4px 4px at 15% 90%, rgba(245,158,11,0.5), transparent),
        radial-gradient(3px 3px at 90% 10%, rgba(34,211,238,0.6), transparent),
        radial-gradient(2px 2px at 50% 40%, rgba(167,139,250,0.6), transparent),
        radial-gradient(3px 3px at 30% 80%, rgba(239,68,68,0.5), transparent),
        radial-gradient(4px 4px at 5% 60%, rgba(34,211,238,0.5), transparent),
        radial-gradient(3px 3px at 75% 15%, rgba(245,158,11,0.5), transparent),
        radial-gradient(2px 2px at 60% 50%, rgba(167,139,250,0.6), transparent),
        radial-gradient(3px 3px at 45% 90%, rgba(239,68,68,0.5), transparent),
        radial-gradient(4px 4px at 20% 40%, rgba(34,211,238,0.6), transparent),
        radial-gradient(2px 2px at 95% 70%, rgba(245,158,11,0.5), transparent),
        radial-gradient(3px 3px at 10% 50%, rgba(167,139,250,0.5), transparent),
        radial-gradient(5px 5px at 80% 80%, rgba(34,211,238,0.5), transparent),
        radial-gradient(2px 2px at 35% 30%, rgba(239,68,68,0.5), transparent),
        radial-gradient(3px 3px at 65% 5%, rgba(245,158,11,0.6), transparent);
}
#particles::after {
    content: '';
    position: absolute;
    width: 100%; height: 100%;
    animation: particleFloat 40s infinite linear reverse;
    background:
        radial-gradient(2px 2px at 5% 45%, rgba(245,158,11,0.6), transparent),
        radial-gradient(4px 4px at 45% 15%, rgba(167,139,250,0.5), transparent),
        radial-gradient(3px 3px at 65% 60%, rgba(34,211,238,0.6), transparent),
        radial-gradient(2px 2px at 80% 5%, rgba(239,68,68,0.5), transparent),
        radial-gradient(3px 3px at 95% 40%, rgba(167,139,250,0.6), transparent),
        radial-gradient(4px 4px at 20% 30%, rgba(245,158,11,0.5), transparent),
        radial-gradient(2px 2px at 60% 90%, rgba(34,211,238,0.6), transparent),
        radial-gradient(3px 3px at 35% 50%, rgba(239,68,68,0.4), transparent),
        radial-gradient(4px 4px at 15% 25%, rgba(245,158,11,0.5), transparent),
        radial-gradient(2px 2px at 50% 75%, rgba(167,139,250,0.5), transparent),
        radial-gradient(3px 3px at 75% 45%, rgba(34,211,238,0.5), transparent),
        radial-gradient(2px 2px at 25% 5%, rgba(239,68,68,0.5), transparent),
        radial-gradient(4px 4px at 88% 55%, rgba(245,158,11,0.5), transparent),
        radial-gradient(3px 3px at 40% 65%, rgba(167,139,250,0.5), transparent),
        radial-gradient(2px 2px at 70% 10%, rgba(34,211,238,0.5), transparent),
        radial-gradient(3px 3px at 10% 85%, rgba(239,68,68,0.4), transparent),
        radial-gradient(4px 4px at 55% 35%, rgba(245,158,11,0.5), transparent),
        radial-gradient(2px 2px at 90% 90%, rgba(167,139,250,0.5), transparent);
}
@keyframes particleFloat {
    0% { transform: translateY(0) rotate(0deg); opacity: 0.4; }
    50% { opacity: 0.9; }
    100% { transform: translateY(-100vh) rotate(360deg); opacity: 0.4; }
}

/* ── Title gradient + glow ── */
.title-wrapper {
    text-align: center;
    margin-bottom: 0.5rem;
}
.title-glow {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #f59e0b, #ef4444, #a78bfa, #22d3ee);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 6s ease infinite;
    filter: drop-shadow(0 0 30px rgba(245,158,11,0.3));
}
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── Shimmer button ── */
.stButton button {
    position: relative !important;
    overflow: hidden !important;
    background: linear-gradient(135deg, #f59e0b, #ef4444) !important;
    border: none !important;
    border-radius: 2rem !important;
    font-size: 1.5rem !important;
    font-weight: 800 !important;
    padding: 1rem 3rem !important;
    color: white !important;
    box-shadow: 0 0 30px rgba(245,158,11,0.4) !important;
    transition: all 0.3s !important;
}
.stButton button::after {
    content: '';
    position: absolute;
    top: 0; left: -100%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
    transform: skewX(-20deg);
    animation: shimmer 3s infinite ease-in-out;
}
@keyframes shimmer {
    0% { left: -100%; }
    100% { left: 150%; }
}
.stButton button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 0 50px rgba(245,158,11,0.7) !important;
}

/* ── Winner card ── */
.ganador-card {
    text-align: center;
    padding: 2rem;
    background: rgba(255,255,255,0.03);
    border: 2px solid rgba(34,211,238,0.3);
    border-radius: 1.5rem;
    margin-top: 1.5rem;
    animation: slideUp 0.6s ease-out, borderPulse 2s ease-in-out infinite 0.6s;
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes borderPulse {
    0%, 100% { border-color: rgba(34,211,238,0.3); box-shadow: 0 0 20px rgba(34,211,238,0.1); }
    50% { border-color: rgba(34,211,238,0.7); box-shadow: 0 0 40px rgba(34,211,238,0.3); }
}
</style>
<div id="particles"></div>
""", unsafe_allow_html=True)


@st.cache_resource
def get_supabase() -> SyncPostgrestClient:
    return SyncPostgrestClient(
        f"{st.secrets['SUPABASE_URL']}/rest/v1",
        headers={
            "apiKey": st.secrets["SUPABASE_KEY"],
            "Authorization": f"Bearer {st.secrets['SUPABASE_KEY']}",
        },
    )


# ── Session state for winner tracking ──
if "ganadores_ids" not in st.session_state:
    st.session_state.ganadores_ids = set()
if "columna_existe" not in st.session_state:
    st.session_state.columna_existe = True
if "ultimo_ganador" not in st.session_state:
    st.session_state.ultimo_ganador = None
if "mostrar_celebracion" not in st.session_state:
    st.session_state.mostrar_celebracion = False


# ── Load participants ──
supabase = get_supabase()
disponibles = []
total_count = 0

if st.session_state.columna_existe:
    try:
        r = supabase.table("opiniones").select("id,nombre,email").not_.is_("ganador", "true").execute()
        disponibles = list(r.data or [])
        r2 = supabase.table("opiniones").select("id", count="exact").execute()
        total_count = r2.count if hasattr(r2, "count") and r2.count else len(r2.data or [])
    except Exception:
        st.session_state.columna_existe = False

if not st.session_state.columna_existe:
    r = supabase.table("opiniones").select("id,nombre,email").execute()
    todos = list(r.data or [])
    total_count = len(todos)
    disponibles = [p for p in todos if p["id"] not in st.session_state.ganadores_ids]


# ── UI ──
st.markdown(
    '<h1 class="title-wrapper"><span class="title-glow">🎰 Ruleta de Sorteo</span></h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="text-align:center;color:#94a3b8;max-width:36rem;margin:0 auto 2rem;">'
    "Seleccionaremos un ganador al azar de los participantes que opinaron</p>",
    unsafe_allow_html=True,
)

contador = st.empty()
if disponibles:
    contador.markdown(
        f"<p style='text-align:center;font-size:1.125rem;color:#a78bfa;'>"
        f"🎯 {len(disponibles)} disponibles / {total_count} total</p>",
        unsafe_allow_html=True,
    )
else:
    contador.markdown(
        "<p style='text-align:center;font-size:1.125rem;color:#ef4444;'>"
        "No hay participantes disponibles</p>",
        unsafe_allow_html=True,
    )

if st.button("🎲 ¡Girar ruleta!", type="primary", use_container_width=True):
    if not disponibles:
        st.warning("No hay participantes disponibles")
    else:
        anim_ph = st.empty()
        pool = list(disponibles)

        for _ in range(12):
            temp = random.choice(pool)
            anim_ph.markdown(
                f"<h2 style='text-align:center;font-size:2.5rem;color:#fbbf24;'>"
                f"🎡 {temp['nombre']}</h2>",
                unsafe_allow_html=True,
            )
            time.sleep(0.1)

        for _ in range(6):
            temp = random.choice(pool)
            anim_ph.markdown(
                f"<h2 style='text-align:center;font-size:3rem;color:#f97316;'>"
                f"🎡 {temp['nombre']}</h2>",
                unsafe_allow_html=True,
            )
            time.sleep(0.2)

        ganador = random.choice(pool)

        # ── Mark winner in Supabase ──
        if st.session_state.columna_existe:
            try:
                supabase.table("opiniones").update({"ganador": True}).eq("id", ganador["id"]).execute()
            except Exception:
                pass

        st.session_state.ganadores_ids.add(ganador["id"])
        st.session_state.ultimo_ganador = ganador
        st.session_state.mostrar_celebracion = True
        st.rerun()

# ── Show winner ──
if st.session_state.ultimo_ganador:
    g = st.session_state.ultimo_ganador
    st.markdown(
        '<div class="ganador-card">'
        f"<h1 style='font-size:3.5rem;color:#22d3ee;text-shadow:0 0 40px rgba(34,211,238,0.6);margin:0;'>"
        f"🎉 {g['nombre']} 🎉</h1>"
        f"<p style='font-size:1.25rem;color:#94a3b8;'>📧 {g['email']}</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    if st.session_state.mostrar_celebracion:
        st.session_state.mostrar_celebracion = False
        st.balloons()
        st.success("¡Tenemos un ganador!")
