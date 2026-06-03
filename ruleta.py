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
.stApp {
    background: linear-gradient(135deg, #0f0a1a, #1a0a2e, #0f0a1a);
    color: white;
}
h1, h2, h3 { text-align: center; }
.stButton button {
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
.stButton button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 0 50px rgba(245,158,11,0.7) !important;
}
.ganador-card {
    text-align: center;
    padding: 2rem;
    background: rgba(255,255,255,0.03);
    border: 2px solid rgba(34,211,238,0.3);
    border-radius: 1.5rem;
    margin-top: 1.5rem;
}
</style>
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
st.title("🎰 Ruleta de Sorteo")
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
