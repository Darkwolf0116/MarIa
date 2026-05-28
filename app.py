import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Feria Digital: El Parche de MarIA",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def img_to_base64(path):
    try:
        data = Path(path).read_bytes()
        ext = Path(path).suffix[1:]
        mime = f"image/{'png' if ext == 'png' else 'jpeg'}"
        return f"data:{mime};base64,{base64.b64encode(data).decode()}"
    except Exception:
        return ""


LOGO = img_to_base64("assets/logo-men.png")
HERO_BG = img_to_base64("assets/hero-bg.jpg")
MARIA_AVATAR = img_to_base64("assets/maria-avatar.png")
ROBOT = img_to_base64("assets/robot-maria.png")
CIRCUIT_BG = img_to_base64("assets/circuit-path.jpg")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
    font-family: 'Outfit', sans-serif;
    background: #0f0a1a;
    color: white;
    overflow-x: hidden;
}

.bg-gradient-hero {
    background: linear-gradient(135deg, #1a0b2e 0%, #2d1b69 30%, #1e3a8a 60%, #0f172a 100%);
}

.bg-gradient-card {
    background: linear-gradient(145deg, rgba(107,33,168,0.15), rgba(37,99,235,0.1));
}

.bg-gradient-section {
    background: linear-gradient(180deg, #0f0a1a, #1a103c, #0f172a);
}

.text-gradient-violet {
    background: linear-gradient(to right, #a78bfa, #c084fc, #e879f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.text-gradient-blue {
    background: linear-gradient(to right, #60a5fa, #22d3ee, #2dd4bf);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.glow-violet {
    box-shadow: 0 0 30px rgba(139,92,246,0.3), 0 0 60px rgba(139,92,246,0.1);
}

.glow-blue {
    box-shadow: 0 0 30px rgba(59,130,246,0.3), 0 0 60px rgba(59,130,246,0.1);
}

@keyframes float {
    0%,100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}

@keyframes pulse-glow {
    0%,100% { box-shadow: 0 0 20px rgba(139,92,246,0.3); }
    50% { box-shadow: 0 0 40px rgba(139,92,246,0.6); }
}

@keyframes slide-up {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes bounce {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.animate-float { animation: float 6s ease-in-out infinite; }
.animate-pulse-glow { animation: pulse-glow 3s ease-in-out infinite; }
.animate-slide-up { animation: slide-up 0.8s ease-out forwards; }
.animate-fade-in { animation: fade-in 1s ease-out forwards; }
.animate-bounce { animation: bounce 1s infinite; }

section { position: relative; overflow: hidden; }

.max-w-7xl {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 1rem;
}

@media (min-width: 640px) {
    .max-w-7xl { padding: 0 1.5rem; }
}

@media (min-width: 1024px) {
    .max-w-7xl { padding: 0 2rem; }
}

/* Ocultar la barra de herramientas nativa de Streamlit */
[data-testid="stToolbar"],
[data-testid="stHeader"],
header[data-testid="stHeader"] {
    display: none !important;
}

/* Eliminar padding superior que deja Streamlit para su barra */
[data-testid="stAppViewContainer"] > section:first-child,
[data-testid="stMain"] {
    padding-top: 0 !important;
}
.stApp > header { display: none !important; }

/* Navegación de estaciones manejada via query params — sin botones Streamlit */

/* Logo MarIA con arco dorado */
.maria-logo {
    display: inline-flex;
    align-items: flex-end;
    position: relative;
    font-family: 'Outfit', sans-serif;
    font-weight: 900;
    line-height: 1;
    letter-spacing: -0.02em;
}
.maria-logo .mar { color: #FFFFFF; }
.maria-logo .ia-wrap {
    position: relative;
    display: inline-block;
}
.maria-logo .ia { color: #F500F5; }
.maria-logo .arco {
    position: absolute;
    top: -0.30em;
    left: 45%;
    transform: translateX(-50%);
    pointer-events: none;
}
</style>"""


def maria_logo_html(size_rem="1em", extra_style=""):
    """
    Genera el logotipo MarIA con arco dorado SVG.
    size_rem: tamaño de fuente (hereda si se pasa 'inherit').
    extra_style: estilos CSS extra para el contenedor.
    """
    # El arco SVG se escala proporcionalmente al tamaño de fuente
    return (
        '<span class="maria-logo" style="font-size:'
        + size_rem
        + ";"
        + extra_style
        + '">'
        '<span class="mar">Mar</span>'
        '<span class="ia-wrap">'
        # SVG arco dorado — viewBox calibrado para cubrirlas letras "IA"
        # Arco circular caligráfico: radio real, grosor 8 en el centro, puntas finas
        '<svg class="arco" xmlns="http://www.w3.org/2000/svg"'
        ' viewBox="-55 -55 110 40" width="1.25em" height="0.46em"'
        ' style="overflow:visible;display:block;">'
        '<path d="'
        "M -43.5,-20.3"
        " A 52,52 0 0,1 43.5,-20.3"
        ' A 44,44 0 0,0 -43.5,-20.3 Z"'
        ' fill="#FFD166"/>'
        "</svg>"
        '<span class="ia">IA</span>'
        "</span>"
        "</span>"
    )


def nav_html():
    logo_markup = (
        f'<img src="{LOGO}" alt="MEN" class="nav-logo" />'
        if LOGO
        else '<span class="nav-logo-fallback">MEN</span>'
    )
    return f"""
    <nav style="position:fixed;top:0;left:0;right:0;z-index:999;background:rgba(15,10,26,0.95);backdrop-filter:blur(20px);border-bottom:1px solid rgba(139,92,246,0.2);transition:all 0.5s;overflow:visible;">
    <style>
    #menu-toggle {{ display: none; }}
    .nav-container {{ max-width: 1280px; margin: 0 auto; padding: 0 2rem; overflow: visible; }}
    .nav-shell {{ display: flex; align-items: center; justify-content: space-between; height: 6.5rem; gap: 1rem; overflow: visible; }}
    .nav-logo-link {{ text-decoration: none; }}
    .nav-logo-wrap {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.2rem 0;
    }}
    .nav-logo {{
        height: 4rem;
        width: auto;
        max-width: 15rem;
        object-fit: contain;
        display: block;
    }}
    .nav-logo-fallback {{
        font-size: 1.35rem;
        font-weight: 800;
        color: #1e3a8a;
        letter-spacing: 0.04em;
    }}
    .nav-link {{
        padding: 0.5rem 1rem;
        font-size: 0.875rem;
        font-weight: 500;
        color: #cbd5e1;
        text-decoration: none;
        border-radius: 0.5rem;
        transition: all 0.3s;
        display: inline-block;
    }}
    .nav-link:hover {{ color: white; background: rgba(139,92,246,0.1); }}
    .cta-btn {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.625rem 1.25rem;
        background: linear-gradient(to right, #7c3aed, #2563eb);
        color: white;
        font-size: 0.875rem;
        font-weight: 600;
        border-radius: 9999px;
        text-decoration: none;
        transition: all 0.3s;
    }}
    .cta-btn:hover {{
        background: linear-gradient(to right, #8b5cf6, #3b82f6);
        box-shadow: 0 10px 15px -3px rgba(139,92,246,0.25);
    }}
    .hamburger-label {{
        display: none; padding: 0.5rem; color: #cbd5e1; cursor: pointer;
        border-radius: 0.5rem; font-size: 1.5rem; user-select: none;
    }}
    .hamburger-label:hover {{ background: rgba(139,92,246,0.1); color: white; }}
    .desktop-links {{ display: flex; align-items: center; gap: 0.25rem; }}
    .mobile-menu {{
        display: none;
        background: rgba(15,10,26,0.98);
        backdrop-filter: blur(20px);
        border-top: 1px solid rgba(139,92,246,0.2);
        padding: 1rem;
    }}
    #menu-toggle:checked ~ .mobile-menu {{ display: block; }}
    @media (max-width: 1023px) {{
        .desktop-links, .desktop-cta {{ display: none !important; }}
        .hamburger-label {{ display: inline-block !important; }}
        .nav-container {{ padding: 0 1rem !important; }}
        .nav-shell {{ height: 5.5rem !important; }}
        .nav-logo-wrap {{ padding: 0.1rem 0; }}
        .nav-logo {{ height: 3.5rem !important; max-width: 11rem !important; }}
    }}
    @media (min-width: 1024px) {{
        .mobile-menu {{ display: none !important; }}
    }}
    </style>
    <div class="nav-container">
        <div class="nav-shell">
            <a href="#" class="nav-logo-link"><span class="nav-logo-wrap">{logo_markup}</span></a>
            <div class="desktop-links">
                <a class="nav-link" href="#proposito">Propósito</a>
                <a class="nav-link" href="#maria">Conoce a MarIA</a>
                <a class="nav-link" href="#feria">La Feria</a>
                <a class="nav-link" href="#circuito">Circuito</a>
                <a class="nav-link" href="#estaciones">Estaciones</a>
                <a class="nav-link" href="#talleres">Talleres</a>
            </div>
            <div style="display:flex;align-items:center;gap:0.75rem;">
                <a class="cta-btn desktop-cta" href="#articulacion">🤖 Únete al evento</a>
                <label class="hamburger-label" for="menu-toggle">☰</label>
            </div>
        </div>
    </div>
    <input type="checkbox" id="menu-toggle" />
    <div class="mobile-menu">
        <div style="display:flex;flex-direction:column;gap:0.25rem;">
            <a class="nav-link" href="#proposito">Propósito</a>
            <a class="nav-link" href="#maria">Conoce a MarIA</a>
            <a class="nav-link" href="#feria">La Feria</a>
            <a class="nav-link" href="#circuito">Circuito</a>
            <a class="nav-link" href="#estaciones">Estaciones</a>
            <a class="nav-link" href="#talleres">Talleres</a>
            <a class="cta-btn" href="#articulacion" style="justify-content:center;margin-top:0.75rem;">🤖 Únete al evento</a>
        </div>
    </div>
    </nav>
    """


def hero_html():
    _maria = maria_logo_html("inherit")
    return f"""
    <section style="min-height:100vh;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;padding-top:5rem;">
        <div style="position:absolute;inset:0;background-image:url('{HERO_BG}');background-size:cover;background-position:center;opacity:0.3;"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,transparent,#0f0a1a);"></div>
        <div style="position:absolute;inset:0;background:linear-gradient(to right,#0f0a1a,transparent,#0f0a1a);"></div>
        <div style="position:absolute;top:25%;left:25%;width:18rem;height:18rem;background:rgba(124,58,237,0.2);border-radius:50%;filter:blur(100px);animation:pulse 3s infinite;"></div>
        <div style="position:absolute;bottom:25%;right:25%;width:24rem;height:24rem;background:rgba(37,99,235,0.15);border-radius:50%;filter:blur(120px);animation:pulse 3s infinite;animation-delay:1s;"></div>
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:500px;height:500px;background:rgba(192,38,211,0.1);border-radius:50%;filter:blur(150px);animation:pulse 3s infinite;animation-delay:2s;"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;padding:5rem 0;">
            <div style="display:grid;grid-template-columns:1fr;gap:3rem;align-items:center;" class="lg-grid-2">
                <div class="animate-slide-up" style="text-align:center;">
                    <div style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.5rem 1rem;background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);border-radius:9999px;margin-bottom:2rem;">
                        <span style="font-size:1rem;">✨</span>
                        <span style="font-size:0.875rem;font-weight:500;color:#c4b5fd;">Ministerio de Educación Nacional | Política de Gobierno Digital</span>
                    </div>
                    <div style="margin-bottom:2rem;">
                        <h2 style="font-size:1.5rem;font-weight:500;color:#93c5fd;margin-bottom:0.5rem;">Feria Digital:</h2>
                        <h1 style="font-size:3rem;font-weight:900;line-height:1.25;letter-spacing:-0.02em;" class="hero-title">
                            <span style="color:white;">El Parche</span><br />
                            <span style="color:white;">de </span>
                            {_maria}
                        </h1>
                        <p style="font-size:1.125rem;color:#94a3b8;max-width:36rem;margin:1rem auto 0;line-height:1.625;">Transformando la gestión pública a través de la Inteligencia Artificial</p>
                    </div>
                    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:1rem;margin-bottom:2rem;">
                        <div style="display:flex;align-items:center;gap:0.5rem;padding:0.625rem 1rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:0.75rem;">
                            <span style="font-size:1.25rem;">📅</span>
                            <span style="font-size:0.875rem;font-weight:500;color:#cbd5e1;">Miércoles 03 de Junio</span>
                        </div>
                        <div style="display:flex;align-items:center;gap:0.5rem;padding:0.625rem 1rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:0.75rem;">
                            <span style="font-size:1.25rem;">⏰</span>
                            <span style="font-size:0.875rem;font-weight:500;color:#cbd5e1;">8 Horas de inmersión</span>
                        </div>
                        <div style="display:flex;align-items:center;gap:0.5rem;padding:0.625rem 1rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:0.75rem;">
                            <span style="font-size:1.25rem;">📍</span>
                            <span style="font-size:0.875rem;font-weight:500;color:#cbd5e1;">Salas del 1er piso (5 salas)</span>
                        </div>
                    </div>
                    <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center;">
                        <a href="#circuito" style="display:inline-flex;align-items:center;gap:0.5rem;padding:1rem 2rem;background:linear-gradient(to right,#7c3aed,#2563eb);color:white;font-weight:700;border-radius:9999px;text-decoration:none;transition:all 0.3s;">✨ Explora el Circuito</a>
                        <a href="#maria" style="display:inline-flex;align-items:center;gap:0.5rem;padding:1rem 2rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.2);color:white;font-weight:600;border-radius:9999px;text-decoration:none;transition:all 0.3s;">Conoce a MarIA</a>
                    </div>
                </div>
                <div class="animate-float" style="display:flex;justify-content:center;">
                    <div style="position:relative;">
                        <div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(139,92,246,0.3),rgba(192,38,211,0.2),rgba(59,130,246,0.3));border-radius:50%;filter:blur(3rem);transform:scale(1.1);"></div>
                        <img src="{MARIA_AVATAR}" alt="MarIA" style="position:relative;width:18rem;object-fit:contain;filter:drop-shadow(0 20px 40px rgba(0,0,0,0.5));" class="hero-avatar" />
                        <div style="position:absolute;bottom:-1rem;left:50%;transform:translateX(-50%);padding:0.75rem 1.5rem;background:linear-gradient(to right,rgba(124,58,237,0.9),rgba(37,99,235,0.9));backdrop-filter:blur(20px);border:1px solid rgba(139,92,246,0.3);border-radius:1rem;box-shadow:0 10px 15px -3px rgba(139,92,246,0.2);white-space:nowrap;">
                            <span style="color:white;font-weight:700;font-size:0.875rem;">🤖 Tu guía virtual de IA</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="animate-bounce" style="position:absolute;bottom:2rem;left:50%;transform:translateX(-50%);">
            <a href="#proposito" style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;color:#64748b;text-decoration:none;transition:color 0.3s;">
                <span style="font-size:0.75rem;font-weight:500;">Descubre más</span>
                <span style="font-size:1.25rem;">⬇</span>
            </a>
        </div>
    </section>
    <style>
    @media (min-width: 1024px) {{
        .lg-grid-2 {{ grid-template-columns: 1fr 1fr !important; }}
        .lg-grid-2 > .text-center {{ text-align: left !important; }}
    }}
    .hero-title {{ font-size: 3rem !important; }}
    @media (min-width: 640px) {{ .hero-title {{ font-size: 3.75rem !important; }} }}
    @media (min-width: 1024px) {{ .hero-title {{ font-size: 4.5rem !important; }} }}
    @media (min-width: 1280px) {{ .hero-title {{ font-size: 6rem !important; }} }}
    .hero-avatar {{ width: 18rem !important; }}
    @media (min-width: 640px) {{ .hero-avatar {{ width: 24rem !important; }} }}
    @media (min-width: 1024px) {{ .hero-avatar {{ width: 28rem !important; }} }}
    </style>
    """


def proposito_html():
    return f"""
    <section id="proposito" style="padding:6rem 0;position:relative;overflow:hidden;">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,#140d25,#0f0a1a);"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="text-align:center;margin-bottom:4rem;">
                <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1.5rem;opacity:0.8;" />
                <span style="display:inline-block;padding:0.375rem 1rem;background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);border-radius:9999px;font-size:0.875rem;font-weight:500;color:#c4b5fd;margin-bottom:1rem;">IA LAB MEN</span>
                <h2 style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;" class="section-title">El propósito fundacional del <span class="text-gradient-violet">IA LAB MEN</span></h2>
                <p style="font-size:1.125rem;color:#94a3b8;max-width:42rem;margin:0 auto;">Tres pilares que guían nuestra estrategia de transformación digital</p>
            </div>
            <div style="display:grid;grid-template-columns:1fr;gap:1.5rem;margin-bottom:4rem;" class="pilar-grid">
                <div style="padding:2rem;border-radius:1rem;border:1px solid rgba(245,158,11,0.2);background:rgba(245,158,11,0.1);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:inline-flex;padding:1rem;border-radius:0.75rem;background:linear-gradient(135deg,#f59e0b,#eab308);margin-bottom:1.5rem;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">💡</div>
                    <h3 style="font-size:1.5rem;font-weight:700;color:white;margin-bottom:0.5rem;">Innovación</h3>
                    <p style="font-size:0.875rem;font-weight:500;color:#94a3b8;margin-bottom:1rem;">Casos de uso prácticos en el sector educativo</p>
                    <p style="color:#94a3b8;line-height:1.625;">Implementamos soluciones reales de IA que transforman procesos educativos y administrativos.</p>
                </div>
                <div style="padding:2rem;border-radius:1rem;border:1px solid rgba(139,92,246,0.2);background:rgba(139,92,246,0.1);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:inline-flex;padding:1rem;border-radius:0.75rem;background:linear-gradient(135deg,#8b5cf6,#a855f7);margin-bottom:1.5rem;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">⚡</div>
                    <h3 style="font-size:1.5rem;font-weight:700;color:white;margin-bottom:0.5rem;">Eficiencia</h3>
                    <p style="font-size:0.875rem;font-weight:500;color:#94a3b8;margin-bottom:1rem;">Optimización de la operatividad ministerial</p>
                    <p style="color:#94a3b8;line-height:1.625;">Reducimos tiempos de gestión y mejoramos la productividad de los funcionarios públicos.</p>
                </div>
                <div style="padding:2rem;border-radius:1rem;border:1px solid rgba(59,130,246,0.2);background:rgba(59,130,246,0.1);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:inline-flex;padding:1rem;border-radius:0.75rem;background:linear-gradient(135deg,#3b82f6,#22d3ee);margin-bottom:1.5rem;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">🛡</div>
                    <h3 style="font-size:1.5rem;font-weight:700;color:white;margin-bottom:0.5rem;">Transformación</h3>
                    <p style="font-size:0.875rem;font-weight:500;color:#94a3b8;margin-bottom:1rem;">Apropiación tecnológica y seguridad de la información</p>
                    <p style="color:#94a3b8;line-height:1.625;">Capacitamos en el uso ético de la IA promoviendo transparencia y protección de datos.</p>
                </div>
            </div>
            <div style="position:relative;padding:2.5rem;border-radius:1.5rem;background:linear-gradient(to right,rgba(139,92,246,0.3),rgba(37,99,235,0.2),rgba(139,92,246,0.3));border:1px solid rgba(139,92,246,0.2);backdrop-filter:blur(4px);">
                <div style="position:absolute;top:0;left:2rem;right:2rem;height:1px;background:linear-gradient(to right,transparent,rgba(139,92,246,0.5),transparent);"></div>
                <div style="display:flex;flex-direction:column;align-items:flex-start;gap:1.5rem;" class="base-etica">
                    <div style="display:flex;align-items:center;gap:1rem;">
                        <div style="padding:1rem;background:linear-gradient(135deg,#7c3aed,#2563eb);border-radius:0.75rem;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">✅</div>
                        <div>
                            <h3 style="font-size:1.5rem;font-weight:700;color:white;">Base Ética</h3>
                            <p style="color:#c4b5fd;font-weight:500;">Ley, Moral, Cultura</p>
                        </div>
                    </div>
                    <div style="border-top:1px solid rgba(139,92,246,0.2);padding-top:1rem;width:100%;">
                        <p style="color:#cbd5e1;line-height:1.625;">Reflexión sobre el uso ético de la Inteligencia Artificial, promoviendo <strong style="color:#a78bfa;">transparencia</strong>, <strong style="color:#60a5fa;">responsabilidad</strong> y <strong style="color:#e879f9;">protección de la información</strong>. Pasar de la teoría a la práctica en la gestión pública.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <style>
    .pilar-grid {{ grid-template-columns: 1fr !important; }}
    @media (min-width: 768px) {{ .pilar-grid {{ grid-template-columns: 1fr 1fr 1fr !important; }} }}
    .base-etica {{ flex-direction: column !important; }}
    @media (min-width: 1024px) {{ .base-etica {{ flex-direction: row !important; align-items: center !important; }} .base-etica > div:last-child {{ border-left: 1px solid rgba(139,92,246,0.2); padding-left: 2rem; }} }}
    .section-title {{ font-size: 1.875rem !important; }}
    @media (min-width: 640px) {{ .section-title {{ font-size: 2.25rem !important; }} }}
    @media (min-width: 1024px) {{ .section-title {{ font-size: 3rem !important; }} }}
    </style>
    """


def identidad_html():
    _maria = maria_logo_html("inherit")
    _maria_sm = maria_logo_html("1.125rem")
    return f"""
    <section id="maria" style="padding:6rem 0;position:relative;overflow:hidden;">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,#120822,#0f0a1a);"></div>
        <div style="position:absolute;top:33%;right:0;width:20rem;height:20rem;background:rgba(192,38,211,0.1);border-radius:50%;filter:blur(120px);"></div>
        <div style="position:absolute;bottom:33%;left:0;width:20rem;height:20rem;background:rgba(139,92,246,0.1);border-radius:50%;filter:blur(120px);"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="text-align:center;margin-bottom:4rem;">
                <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1.5rem;opacity:0.8;" />
                <span style="display:inline-block;padding:0.375rem 1rem;background:rgba(192,38,211,0.1);border:1px solid rgba(192,38,211,0.3);border-radius:9999px;font-size:0.875rem;font-weight:500;color:#f0abfc;margin-bottom:1rem;">Identidad Digital</span>
                <h2 style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;" class="section-title">Conoce a tu guía virtual: {_maria}</h2>
            </div>
            <div style="display:grid;grid-template-columns:1fr;gap:3rem;align-items:center;" class="lg-grid-2">
                <div style="display:flex;justify-content:center;">
                    <div style="position:relative;">
                        <div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(139,92,246,0.2),rgba(192,38,211,0.2),rgba(59,130,246,0.2));border-radius:1.5rem;filter:blur(2rem);transform:scale(1.1);transition:transform 0.7s;"></div>
                        <div style="position:relative;padding:2rem;background:linear-gradient(135deg,rgba(139,92,246,0.2),rgba(37,99,235,0.2));border:1px solid rgba(139,92,246,0.2);border-radius:1.5rem;backdrop-filter:blur(4px);">
                            <img src="{MARIA_AVATAR}" alt="MarIA" style="width:16rem;height:16rem;object-fit:contain;filter:drop-shadow(0 20px 40px rgba(0,0,0,0.5));" class="identidad-avatar" />
                            <div style="position:absolute;bottom:1.5rem;left:50%;transform:translateX(-50%);padding:0.75rem 1.5rem;background:linear-gradient(to right,rgba(192,38,211,0.9),rgba(139,92,246,0.9));border-radius:0.75rem;border:1px solid rgba(192,38,211,0.3);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">
                                <span style="font-weight:700;font-size:1.125rem;">{_maria_sm}</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div style="display:flex;flex-direction:column;gap:2rem;">
                    <div style="padding:1.5rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;">
                        <div style="display:flex;align-items:flex-start;gap:1rem;">
                            <div style="padding:0.75rem;background:rgba(139,92,246,0.1);border-radius:0.75rem;">👤</div>
                            <div>
                                <h3 style="font-size:1.25rem;font-weight:700;color:white;margin-bottom:0.5rem;">¿Quién es {_maria_sm}?</h3>
                                <p style="color:#94a3b8;line-height:1.625;">{_maria_sm} es el cerebro estratégico y la cara amigable de nuestra política de IA que agiliza todo tipo de procesos para el MEN. Es una niña de <strong style="color:#a78bfa;">8 a 10 años</strong>, curiosa, inteligente y dispuesta a ayudar.</p>
                            </div>
                        </div>
                    </div>
                    <div style="display:flex;flex-direction:column;gap:1rem;">
                        <h3 style="font-size:1.125rem;font-weight:700;color:white;display:flex;align-items:center;gap:0.5rem;">⚡ Atributos de {_maria_sm}</h3>
                        <div style="display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:0.75rem;">
                            <span style="display:inline-flex;align-items:center;justify-content:center;width:2.5rem;height:2.5rem;background:rgba(139,92,246,0.1);border-radius:0.5rem;font-size:0.875rem;font-weight:700;color:#a78bfa;">01</span>
                            <div><h4 style="font-weight:600;color:white;">Rapidez de niña genio</h4><p style="font-size:0.875rem;color:#94a3b8;">Con su rapidez de niña genio, MarIA lee y organiza documentos en segundos, reduciendo meses de espera a solo unos días para que los ciudadanos reciban su reconocimiento sin complicaciones.</p></div>
                        </div>
                        <div style="display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:0.75rem;">
                            <span style="display:inline-flex;align-items:center;justify-content:center;width:2.5rem;height:2.5rem;background:rgba(16,185,129,0.1);border-radius:0.5rem;font-size:0.875rem;font-weight:700;color:#34d399;">02</span>
                            <div><h4 style="font-weight:600;color:white;">Honestidad y precisión</h4><p style="font-size:0.875rem;color:#94a3b8;">Como la más honesta de la clase, ella usa su precisión analítica para que los apoyos económicos lleguen de forma justa y sin errores a quienes más lo necesitan.</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <style>
    .identidad-avatar {{ width: 16rem !important; height: 16rem !important; }}
    @media (min-width: 640px) {{ .identidad-avatar {{ width: 20rem !important; height: 20rem !important; }} }}
    </style>
    """


def arquitectura_html():
    return f"""
    <section id="feria" style="padding:6rem 0;position:relative;overflow:hidden;">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,#110b20,#0f0a1a);"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="text-align:center;margin-bottom:4rem;">
                <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1.5rem;opacity:0.8;" />
                <span style="display:inline-block;padding:0.375rem 1rem;background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);border-radius:9999px;font-size:0.875rem;font-weight:500;color:#93c5fd;margin-bottom:1rem;">Arquitectura del Evento</span>
                <h2 style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;" class="section-title">La Arquitectura de la <span class="text-gradient-blue">Feria</span></h2>
                <p style="font-size:1.125rem;color:#94a3b8;max-width:42rem;margin:0 auto;">Un evento diseñado para la inmersión total en el mundo de la IA</p>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;" class="arq-grid">
                <div style="padding:1.5rem;border-radius:1rem;border:1px solid rgba(139,92,246,0.2);background:rgba(139,92,246,0.05);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:inline-flex;padding:0.75rem;border-radius:0.75rem;background:linear-gradient(135deg,#8b5cf6,#a855f7);margin-bottom:1.25rem;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">📅</div>
                    <h3 style="font-size:1.25rem;font-weight:700;color:white;margin-bottom:1rem;">Coordenadas</h3>
                    <ul style="list-style:none;display:flex;flex-direction:column;gap:0.625rem;">
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#8b5cf6,#a855f7);margin-top:0.375rem;flex-shrink:0;"></span> Miércoles 03 de Junio</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#8b5cf6,#a855f7);margin-top:0.375rem;flex-shrink:0;"></span> 8 Horas de inmersión</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#8b5cf6,#a855f7);margin-top:0.375rem;flex-shrink:0;"></span> Salas del 1er piso</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#8b5cf6,#a855f7);margin-top:0.375rem;flex-shrink:0;"></span> Capacidad: 5 salas</li>
                    </ul>
                </div>
                <div style="padding:1.5rem;border-radius:1rem;border:1px solid rgba(59,130,246,0.2);background:rgba(59,130,246,0.05);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:inline-flex;padding:0.75rem;border-radius:0.75rem;background:linear-gradient(135deg,#3b82f6,#22d3ee);margin-bottom:1.25rem;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">👥</div>
                    <h3 style="font-size:1.25rem;font-weight:700;color:white;margin-bottom:1rem;">Metodología</h3>
                    <ul style="list-style:none;display:flex;flex-direction:column;gap:0.625rem;">
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#3b82f6,#22d3ee);margin-top:0.375rem;flex-shrink:0;"></span> Aprendizaje por Estaciones</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#3b82f6,#22d3ee);margin-top:0.375rem;flex-shrink:0;"></span> 15 minutos por rotación</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#3b82f6,#22d3ee);margin-top:0.375rem;flex-shrink:0;"></span> Práctico y rápido</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#3b82f6,#22d3ee);margin-top:0.375rem;flex-shrink:0;"></span> Orientado a retos</li>
                    </ul>
                </div>
                <div style="padding:1.5rem;border-radius:1rem;border:1px solid rgba(192,38,211,0.2);background:rgba(192,38,211,0.05);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:inline-flex;padding:0.75rem;border-radius:0.75rem;background:linear-gradient(135deg,#d946ef,#ec4899);margin-bottom:1.25rem;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">🖥</div>
                    <h3 style="font-size:1.25rem;font-weight:700;color:white;margin-bottom:1rem;">Ecosistema Transversal</h3>
                    <ul style="list-style:none;display:flex;flex-direction:column;gap:0.625rem;">
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#d946ef,#ec4899);margin-top:0.375rem;flex-shrink:0;"></span> Impulso continuo a Google Skills</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#d946ef,#ec4899);margin-top:0.375rem;flex-shrink:0;"></span> Durante toda la jornada</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#d946ef,#ec4899);margin-top:0.375rem;flex-shrink:0;"></span> Envío de invitaciones:</li>
                        <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="width:0.375rem;height:0.375rem;border-radius:50%;background:linear-gradient(to right,#d946ef,#ec4899);margin-top:0.375rem;flex-shrink:0;"></span> 27 de Mayo</li>
                    </ul>
                </div>
            </div>
    </section>
    <style>
    .arq-grid {{ grid-template-columns: 1fr 1fr !important; }}
    @media (min-width: 1024px) {{ .arq-grid {{ grid-template-columns: 1fr 1fr 1fr !important; }} }}
    </style>
    """


def bienvenida_html():
    return f"""
    <section style="padding:6rem 0;position:relative;overflow:hidden;">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,#0d0818,#0f0a1a);"></div>
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:600px;height:600px;background:rgba(139,92,246,0.05);border-radius:50%;filter:blur(150px);"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="text-align:center;margin-bottom:4rem;">
                <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1.5rem;opacity:0.8;" />
                <span style="display:inline-block;padding:0.375rem 1rem;background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);border-radius:9999px;font-size:0.875rem;font-weight:500;color:#c4b5fd;margin-bottom:1rem;">Punto de Contacto 0</span>
                <h2 style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;" class="section-title">La Experiencia de <span class="text-gradient-violet">Bienvenida</span></h2>
                <p style="font-size:1.125rem;color:#94a3b8;max-width:42rem;margin:0 auto;">Un robot físico te acompañará desde el primer momento</p>
            </div>
            <div style="display:grid;grid-template-columns:1fr;gap:3rem;align-items:center;" class="lg-grid-2">
                <div style="display:flex;justify-content:center;">
                    <div style="position:relative;">
                        <div style="position:absolute;inset:0;background:linear-gradient(135deg,rgba(59,130,246,0.2),rgba(139,92,246,0.2),rgba(34,211,238,0.2));border-radius:50%;filter:blur(3rem);transform:scale(1.25);transition:transform 0.7s;"></div>
                        <img src="{ROBOT}" alt="Robot MarIA" style="position:relative;width:16rem;object-fit:contain;filter:drop-shadow(0 20px 40px rgba(0,0,0,0.5));" class="robot-img" />
                    </div>
                </div>
                <div style="display:flex;flex-direction:column;gap:1.25rem;">
                    <div style="display:flex;align-items:flex-start;gap:1.25rem;padding:1.25rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;transition:all 0.5s;">
                        <div style="flex-shrink:0;padding:0.75rem;border-radius:0.75rem;background:linear-gradient(135deg,#8b5cf6,#a855f7);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">🎤</div>
                        <div><h3 style="font-size:1.125rem;font-weight:700;color:white;margin-bottom:0.375rem;">Interacción por Voz</h3><p style="font-size:0.875rem;color:#94a3b8;line-height:1.5;">Mensajes hablados dinámicos para guiar y entretener a los asistentes durante su recorrido.</p></div>
                    </div>
                    <div style="display:flex;align-items:flex-start;gap:1.25rem;padding:1.25rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;transition:all 0.5s;">
                        <div style="flex-shrink:0;padding:0.75rem;border-radius:0.75rem;background:linear-gradient(135deg,#3b82f6,#22d3ee);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">🖥</div>
                        <div><h3 style="font-size:1.125rem;font-weight:700;color:white;margin-bottom:0.375rem;">Proyección Multimedia</h3><p style="font-size:0.875rem;color:#94a3b8;line-height:1.5;">Pantalla táctil integrada con animaciones de la marca para una experiencia inmersiva.</p></div>
                    </div>
                    <div style="display:flex;align-items:flex-start;gap:1.25rem;padding:1.25rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;transition:all 0.5s;">
                        <div style="flex-shrink:0;padding:0.75rem;border-radius:0.75rem;background:linear-gradient(135deg,#d946ef,#ec4899);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">🧭</div>
                        <div><h3 style="font-size:1.125rem;font-weight:700;color:white;margin-bottom:0.375rem;">Navegación Autónoma</h3><p style="font-size:0.875rem;color:#94a3b8;line-height:1.5;">Recorridos programados interactuando con los asistentes de forma autónoma y segura.</p></div>
                    </div>
                    <div style="display:flex;align-items:flex-start;gap:1.25rem;padding:1.25rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;transition:all 0.5s;">
                        <div style="flex-shrink:0;padding:0.75rem;border-radius:0.75rem;background:linear-gradient(135deg,#f59e0b,#eab308);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">📸</div>
                        <div><h3 style="font-size:1.125rem;font-weight:700;color:white;margin-bottom:0.375rem;">Fotocabina Interactiva</h3><p style="font-size:0.875rem;color:#94a3b8;line-height:1.5;">Captura de momentos clave del evento guiados por voz para recordar la experiencia.</p></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <style>
    .robot-img {{ width: 16rem !important; }}
    @media (min-width: 640px) {{ .robot-img {{ width: 20rem !important; }} }}
    @media (min-width: 1024px) {{ .robot-img {{ width: 24rem !important; }} }}
    </style>
    """


def circuito_html():
    stations = [
        {
            "num": "1",
            "title": "Impacto IA",
            "subtitle": "Impacto de la IA en la sociedad",
            "icon": "🧠",
            "start": "#f59e0b",
            "end": "#facc15",
            "bg": "rgba(245,158,11,0.10)",
            "aliado": "xertica",
            "border": "rgba(245,158,11,0.34)",
        },
        {
            "num": "2",
            "title": "Ecosistema Google",
            "subtitle": "¡Ok Google! Innovaci\u00f3n sin L\u00edmites",
            "icon": "🌍",
            "start": "#3b82f6",
            "end": "#22d3ee",
            "bg": "rgba(59,130,246,0.10)",
            "aliado": "google",
            "border": "rgba(59,130,246,0.34)",
        },
        {
            "num": "3",
            "title": "Copilot Microsoft",
            "subtitle": "Copilot y un cafecito",
            "icon": "☕",
            "start": "#10b981",
            "end": "#14b8a6",
            "bg": "rgba(16,185,129,0.10)",
            "aliado": "microsoft",
            "border": "rgba(16,185,129,0.34)",
        },
        {
            "num": "4",
            "title": "Creador de Agentes",
            "subtitle": "Crea e interact\u00faa con agentes",
            "icon": "🤖",
            "start": "#8b5cf6",
            "end": "#a855f7",
            "bg": "rgba(139,92,246,0.10)",
            "aliado": "xertica",
            "border": "rgba(139,92,246,0.34)",
        },
        {
            "num": "5",
            "title": "NotebookLM",
            "subtitle": "Tu biblioteca con superpoderes",
            "icon": "📖",
            "start": "#d946ef",
            "end": "#ec4899",
            "bg": "rgba(217,70,239,0.10)",
            "aliado": "notebooklm",
            "border": "rgba(217,70,239,0.34)",
        },
        {
            "num": "6",
            "title": "Estrategia MEN",
            "subtitle": "La Estrategia de IA del MEN (Cl\u00edmax)",
            "icon": "⛰",
            "start": "#f43f5e",
            "end": "#ef4444",
            "bg": "rgba(244,63,94,0.10)",
            "aliado": "men",
            "border": "rgba(244,63,94,0.34)",
        },
    ]
    # SVG layout: viewBox 0 0 1000 660
    positions = [
        (150, 110),  # 1: Impacto IA
        (500, 110),  # 2: Ecosistema Google
        (850, 110),  # 3: Copilot Microsoft
        (850, 500),  # 4: Creador de Agentes
        (500, 500),  # 5: NotebookLM
        (150, 500),  # 6: Estrategia MEN
    ]
    # gradient defs
    defs_parts = []
    for i, s in enumerate(stations):
        defs_parts.append(
            '<linearGradient id="sg' + str(i) + '" x1="0%" y1="0%" x2="100%" y2="100%">'
            '<stop offset="0%" stop-color="' + s["start"] + '"/>'
            '<stop offset="100%" stop-color="' + s["end"] + '"/>'
            "</linearGradient>"
        )
    defs_parts.append(
        '<linearGradient id="sgm" x1="0%" y1="0%" x2="100%" y2="100%">'
        '<stop offset="0%" stop-color="#7c3aed"/>'
        '<stop offset="100%" stop-color="#2563eb"/>'
        "</linearGradient>"
    )
    defs_parts.append('<clipPath id="mc"><circle cx="500" cy="320" r="50"/></clipPath>')
    defs_parts.append(
        '<filter id="gf"><feGaussianBlur stdDeviation="10" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    )
    defs_html = "".join(defs_parts)

    # track paths
    track = "M 150,110 L 850,110 C 850,200 700,280 500,320 C 600,370 700,420 850,500 L 150,500"
    loop = "M 150,520 C 150,620 500,620 500,520"

    # station groups
    station_parts = []
    for i, s in enumerate(stations):
        cx, cy = positions[i]
        gid = "sg" + str(i)
        bcx = cx + 34
        bcy = cy - 34

        al = s["aliado"]
        if al == "google":
            brand = (
                '<g transform="translate(' + str(cx - 18) + "," + str(cy - 18) + ')">'
                '<svg viewBox="0 0 24 24" width="36" height="36">'
                '<circle cx="12" cy="12" r="11" fill="white"/>'
                '<path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92a5.06 5.06 0 0 1-2.2 3.32v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.1z"/>'
                '<path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>'
                '<path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>'
                '<path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>'
                "</svg></g>"
            )
        elif al == "microsoft":
            brand = (
                '<g transform="translate(' + str(cx - 18) + "," + str(cy - 18) + ')">'
                '<svg viewBox="0 0 24 24" width="36" height="36">'
                '<rect x="2" y="2" width="9.5" height="9.5" fill="#F25022"/>'
                '<rect x="12.5" y="2" width="9.5" height="9.5" fill="#7FBA00"/>'
                '<rect x="2" y="12.5" width="9.5" height="9.5" fill="#00A4EF"/>'
                '<rect x="12.5" y="12.5" width="9.5" height="9.5" fill="#FFB900"/>'
                "</svg></g>"
            )
        elif al == "notebooklm":
            brand = (
                '<g transform="translate(' + str(cx - 18) + "," + str(cy - 18) + ')">'
                '<svg viewBox="0 0 24 24" width="36" height="36">'
                '<rect x="3" y="2" width="18" height="20" rx="2" fill="#4285F4"/>'
                '<rect x="5" y="4" width="14" height="16" rx="1" fill="white"/>'
                '<path d="M16,16 L16,18 L8,18 L8,16 Z M16,12 L16,14 L8,14 L8,12 Z M16,8 L16,10 L8,10 L8,8 Z" fill="#4285F4" opacity="0.3"/>'
                '<path d="M17,6.5 L18,8.5 L20,9 L18,9.5 L17,11.5 L16,9.5 L14,9 L16,8.5 Z" fill="#FACC15"/>'
                "</svg></g>"
            )
        elif al == "men":
            brand = (
                '<g transform="translate(' + str(cx - 16) + "," + str(cy - 18) + ')">'
                '<svg viewBox="0 0 40 44" width="32" height="36">'
                '<path d="M20,2 L36,10 L36,26 C36,36 20,42 20,42 C20,42 4,36 4,26 L4,10 Z" fill="#0A3D7B" stroke="#FFCC00" stroke-width="1.5"/>'
                '<path d="M20,7 L34,14 L34,26 C34,34 20,38 20,38 C20,38 6,34 6,26 L6,14 Z" fill="white"/>'
                '<text x="20" y="25" text-anchor="middle" font-size="11" font-weight="800" fill="#0A3D7B">MEN</text>'
                '<text x="20" y="43" text-anchor="middle" font-size="5" font-weight="700" fill="#0A3D7B">EDUCACI\u00d3N</text>'
                "</svg></g>"
            )
        else:
            brand = (
                '<g transform="translate(' + str(cx - 20) + "," + str(cy - 10) + ')">'
                '<svg viewBox="0 0 40 20" width="40" height="20">'
                '<rect x="0" y="0" width="40" height="20" rx="4" fill="#6C5CE7"/>'
                '<text x="20" y="13" text-anchor="middle" font-size="10" font-weight="800"'
                ' fill="white" font-family="Arial,sans-serif">Xertica</text>'
                "</svg></g>"
            )

        station_parts.append(
            "<g>"
            '<circle cx="'
            + str(cx)
            + '" cy="'
            + str(cy)
            + '" r="45" fill="rgba(255,255,255,0.06)"'
            ' stroke="rgba(255,255,255,0.12)" stroke-width="2"/>'
            '<circle cx="' + str(bcx) + '" cy="' + str(bcy) + '" r="22" fill="white"'
            ' stroke="' + s["start"] + '" stroke-width="2"/>'
            '<text x="' + str(bcx) + '" y="' + str(bcy + 1) + '" text-anchor="middle"'
            ' dominant-baseline="central" font-size="20" font-weight="800" fill="'
            + s["start"]
            + '">'
            + s["num"]
            + "</text>"
            '<text x="' + str(cx) + '" y="' + str(cy + 62) + '" text-anchor="middle"'
            ' font-size="16" font-weight="600" fill="white">'
            + s["title"]
            + "</text>"
            + brand
            + "</g>"
        )
    stations_svg = "".join(station_parts)

    # MarIA central
    maria_svg = (
        '<circle cx="500" cy="320" r="65" fill="rgba(255,255,255,0.08)" filter="url(#gf)"/>'
        '<circle cx="500" cy="320" r="55" fill="rgba(255,255,255,0.10)"/>'
        '<circle cx="500" cy="320" r="55" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="2"/>'
        '<image href="' + MARIA_AVATAR + '" x="450" y="270" width="100" height="100"'
        ' clip-path="url(#mc)" preserveAspectRatio="xMidYMid meet"/>'
        '<text x="500" y="396" text-anchor="middle" font-size="18" font-weight="700" fill="rgba(255,255,255,0.8)">MarIA</text>'
        '<text x="500" y="414" text-anchor="middle" font-size="12" fill="rgba(255,255,255,0.5)">▼ Avanzando</text>'
    )

    # directional arrows
    arrows = (
        '<path d="M294,103 L294,117 L312,110Z" fill="rgba(255,255,255,0.3)"/>'
        '<path d="M694,103 L694,117 L712,110Z" fill="rgba(255,255,255,0.3)"/>'
        '<path d="M734,203 L748,217 L734,217Z" fill="rgba(255,255,255,0.3)"/>'
        '<path d="M694,413 L708,427 L694,427Z" fill="rgba(255,255,255,0.3)"/>'
        '<path d="M306,493 L306,507 L288,500Z" fill="rgba(255,255,255,0.3)"/>'
        '<path d="M706,493 L706,507 L688,500Z" fill="rgba(255,255,255,0.3)"/>'
        '<path d="M319,588 L319,602 L337,595Z" fill="rgba(255,255,255,0.3)"/>'
    )

    svg = (
        '<svg viewBox="0 0 1000 660"'
        ' style="width:100%;max-width:1000px;height:auto;display:block;margin:0 auto;">'
        "<defs>" + defs_html + "</defs>"
        '<path d="' + track + '" fill="none" stroke="rgba(255,255,255,0.06)"'
        ' stroke-width="38" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="' + track + '" fill="none" stroke="rgba(255,255,255,0.15)"'
        ' stroke-width="40" stroke-linecap="round" stroke-linejoin="round" opacity="0.1"/>'
        '<path d="' + track + '" fill="none" stroke="rgba(255,255,255,0.25)"'
        ' stroke-width="1.5" stroke-dasharray="6,6"/>'
        '<path d="' + loop + '" fill="none" stroke="rgba(255,255,255,0.06)"'
        ' stroke-width="38" stroke-linecap="round"/>'
        '<path d="' + loop + '" fill="none" stroke="rgba(255,255,255,0.25)"'
        ' stroke-width="1.5" stroke-dasharray="6,6"/>'
        '<circle cx="500" cy="320" r="5" fill="rgba(255,255,255,0.4)"/>'
        + stations_svg
        + maria_svg
        + arrows
        + "</svg>"
    )

    return f"""
    <section id="circuito" style="padding:6rem 0;position:relative;overflow:hidden;">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,#100820,#0f0a1a);"></div>
        <div style="position:absolute;inset:0;background-image:url('{CIRCUIT_BG}');background-size:cover;background-position:center;opacity:0.1;"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="text-align:center;margin-bottom:4rem;">
                <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1.5rem;opacity:0.8;" />
                <span style="display:inline-block;padding:0.375rem 1rem;background:rgba(139,92,246,0.1);border:1px solid rgba(139,92,246,0.3);border-radius:9999px;font-size:0.875rem;font-weight:500;color:#c4b5fd;margin-bottom:1rem;">Circuito de Aprendizaje</span>
                <h2 style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;" class="section-title">El Circuito de <span style="background:linear-gradient(to right,#a78bfa,#e879f9,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Aprendizaje</span></h2>
                <p style="font-size:1.125rem;color:#94a3b8;max-width:42rem;margin:0 auto;">6 estaciones de inmersión práctica en IA, 15 minutos cada una</p>
            </div>
            {svg}
            <div style="margin-top:3rem;display:flex;justify-content:center;">
                <div style="display:inline-flex;align-items:center;gap:0.75rem;padding:1rem 1.5rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;">
                    <div style="padding:0.5rem;background:rgba(59,130,246,0.1);border-radius:0.5rem;">📖</div>
                    <div>
                        <p style="color:white;font-weight:600;">Talleres de Co-creación</p>
                        <p style="font-size:0.875rem;color:#94a3b8;">2 Terminales disponibles durante el circuito</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """


ESTACIONES_DATA = [
    {
        "number": "1",
        "title": "Impacto de la IA en la sociedad",
        "shortTitle": "Impacto IA",
        "aliado": "XERTICA",
        "icon": "🧠",
        "objetivo": "Casos de uso tangibles y de alto impacto público.",
        "foco": "Presentar desde una perspectiva macro la Inteligencia Artificial mediante casos de uso reales y de alto impacto en el sector público.",
        "quote": "Aquí expandimos la mente. Mostramos cómo la IA está resolviendo problemas reales antes de enfocarnos en las herramientas.",
        "color": "from-amber-500 to-yellow-400",
        "borderColor": "border-amber-500/20",
        "bgColor": "bg-amber-500/5",
        "textColor": "#fbbf24",
    },
    {
        "number": "2",
        "title": "¡Ok Google! Innovación sin Límites",
        "shortTitle": "Ecosistema Google",
        "aliado": "GOOGLE",
        "icon": "🌍",
        "objetivo": "Presentación ágil de la suite Google AI.",
        "foco": "Una inmersión didáctica y ágil en la suite de herramientas y tecnologías de IA generativa de Google.",
        "quote": "Ecosistema transversal: Promoción activa de Google Skills.",
        "color": "from-blue-500 to-cyan-400",
        "borderColor": "border-blue-500/20",
        "bgColor": "bg-blue-500/5",
        "textColor": "#60a5fa",
    },
    {
        "number": "3",
        "title": "Copilot y un cafecito",
        "shortTitle": "Copilot Microsoft",
        "aliado": "MICROSOFT",
        "icon": "☕",
        "objetivo": "Integración de IA en la productividad y agenda diaria.",
        "foco": "Descubrir cómo usar Microsoft AI para la organización de tareas, agendas, y generación de correos en el día a día. Tu copiloto del futuro.",
        "quote": "La meta es que el funcionario recupere tiempo valioso para tareas verdaderamente estratégicas.",
        "color": "from-emerald-500 to-teal-400",
        "borderColor": "border-emerald-500/20",
        "bgColor": "bg-emerald-500/5",
        "textColor": "#34d399",
    },
    {
        "number": "4",
        "title": "Crea e interactúa con agentes",
        "shortTitle": "Creador de Agentes",
        "aliado": "XERTICA",
        "icon": "🤖",
        "objetivo": "Soluciones 'no-code' y asistentes autónomos.",
        "foco": "Explicar de forma sencilla cómo estructurar agentes inteligentes autónomos útiles para la gestión pública institucional.",
        "quote": "Desmitificamos la programación. La tecnología se adapta al funcionario, no al revés.",
        "color": "from-violet-500 to-purple-400",
        "borderColor": "border-violet-500/20",
        "bgColor": "bg-violet-500/5",
        "textColor": "#a78bfa",
    },
    {
        "number": "5",
        "title": "Tu biblioteca con superpoderes",
        "shortTitle": "NotebookLM",
        "aliado": "XERTICA / GOOGLE",
        "icon": "📖",
        "objetivo": "Análisis y síntesis de información compleja.",
        "foco": "Dominar NotebookLM. Cómo subir múltiples documentos complejos, normativas o contratos, y pedirle a la IA que los cruce, analice y resuma.",
        "quote": "Ideal para equipos que procesan altos volúmenes de documentos técnicos y legales.",
        "color": "from-fuchsia-500 to-pink-400",
        "borderColor": "border-fuchsia-500/20",
        "bgColor": "bg-fuchsia-500/5",
        "textColor": "#e879f9",
    },
    {
        "number": "6",
        "title": "La Estrategia de IA del MEN",
        "shortTitle": "Estrategia MEN",
        "aliado": "OTSI",
        "icon": "⛰",
        "objetivo": "El Cerebro Estratégico: Presentación oficial de MarIA como el motor de eficiencia del MEN.",
        "foco": "Presentar la estrategia de IA del MEN, destacando MarIA como el núcleo de innovación y eficiencia para transformar la gestión pública educativa.",
        "quote": "No solo adoptamos herramientas externas; creamos nuestro propio ecosistema para transformar el Estado.",
        "color": "from-rose-500 to-red-400",
        "borderColor": "border-rose-500/20",
        "bgColor": "bg-rose-500/5",
        "textColor": "#fb7185",
        "apps": [
            {
                "name": "MarIA Convalidaciones",
                "desc": "Optimización de trámites de reconocimiento de títulos, reduciendo tiempos y mejorando el servicio al ciudadano.",
            },
            {
                "name": "MarIA Gratuidad",
                "desc": "Transparencia y precisión analítica en la asignación de subsidios de educación superior.",
            },
        ],
    },
]


def estaciones_section_start_html():
    return f"""
    <section id="estaciones" style="padding:6rem 0;position:relative;overflow:hidden;">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,#0e0718,#0f0a1a);"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="text-align:center;margin-bottom:3rem;">
                <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1.5rem;opacity:0.8;" />
                <span style="display:inline-block;padding:0.375rem 1rem;background:rgba(192,38,211,0.1);border:1px solid rgba(192,38,211,0.3);border-radius:9999px;font-size:0.875rem;font-weight:500;color:#f0abfc;margin-bottom:1rem;">Matriz Diagnóstica del Ecosistema</span>
                <h2 style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;" class="section-title">Las <span style="background:linear-gradient(to right,#a78bfa,#e879f9,#fb7185);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">6 Estaciones</span></h2>
                <p style="font-size:1.125rem;color:#94a3b8;max-width:42rem;margin:0 auto;">Cada estación es una experiencia de 15 minutos diseñada para transformar tu perspectiva sobre la IA</p>
            </div>
        </div>
    </section>
    """


def estaciones_nav_cards_html(estaciones, active_idx):
    """Genera pestañitas compactas (tab bar) con data-station-idx para postMessage."""
    color_map = {
        "1": ("#f59e0b", "#facc15"),
        "2": ("#3b82f6", "#22d3ee"),
        "3": ("#10b981", "#14b8a6"),
        "4": ("#8b5cf6", "#a855f7"),
        "5": ("#d946ef", "#ec4899"),
        "6": ("#f43f5e", "#ef4444"),
    }
    parts = []
    for i, est in enumerate(estaciones):
        c_start, c_end = color_map[est["number"]]
        is_active = i == active_idx
        bg = (
            "linear-gradient(135deg," + c_start + "," + c_end + ")"
            if is_active
            else "rgba(255,255,255,0.05)"
        )
        border_col = c_start if is_active else "rgba(255,255,255,0.1)"
        text_color = "white" if is_active else "#94a3b8"
        font_w = "700" if is_active else "500"
        num_bg = "linear-gradient(135deg," + c_start + "," + c_end + ")"
        shadow = "box-shadow:0 4px 15px " + c_start + "55;" if is_active else ""
        tab = (
            '<div data-station-idx="' + str(i) + '" '
            'style="display:inline-flex;align-items:center;gap:0.5rem;padding:0.6rem 1.1rem;'
            "border-radius:9999px;border:1px solid " + border_col + ";"
            "background:"
            + bg
            + ";"
            + shadow
            + 'cursor:pointer;transition:all 0.3s;white-space:nowrap;user-select:none;">'
            '<span style="display:inline-flex;width:1.5rem;height:1.5rem;border-radius:50%;'
            "background:" + num_bg + ";align-items:center;justify-content:center;"
            'font-size:0.7rem;font-weight:700;color:white;flex-shrink:0;">'
            + est["number"]
            + "</span>"
            '<span style="font-size:0.875rem;font-weight:'
            + font_w
            + ";color:"
            + text_color
            + ';">'
            + est["shortTitle"]
            + "</span>"
            "</div>"
        )
        parts.append(tab)
    tabs_html = "".join(parts)
    return (
        '<div id="estaciones-tabbar" style="display:flex;flex-wrap:wrap;gap:0.75rem;justify-content:center;'
        "margin-bottom:2rem;padding:1rem;background:rgba(255,255,255,0.03);"
        'border:1px solid rgba(255,255,255,0.08);border-radius:1rem;">'
        + tabs_html
        + "</div>"
    )


def estaciones_panel_html(active):
    if active.get("apps"):
        app_tpl = (
            '<div style="padding:1rem;background:linear-gradient(135deg,rgba(139,92,246,0.2),'
            'rgba(37,99,235,0.2));border:1px solid rgba(139,92,246,0.2);border-radius:0.75rem;">'
            '<h5 style="font-weight:700;color:#c4b5fd;margin-bottom:0.5rem;">APPNAME</h5>'
            '<p style="font-size:0.875rem;color:#94a3b8;">APPDESC</p></div>'
        )
        app_items = "".join(
            app_tpl.replace("APPNAME", a["name"]).replace("APPDESC", a["desc"])
            for a in active["apps"]
        )
        apps_html = (
            '<div style="display:flex;flex-direction:column;gap:1rem;">'
            '<h4 style="font-size:1.125rem;font-weight:700;color:white;">Aplicativos Mar\u00cdA</h4>'
            + app_items
            + "</div>"
        )
    else:
        apps_html = (
            '<div style="padding:1.5rem;background:linear-gradient(135deg,rgba(139,92,246,0.1),'
            'rgba(37,99,235,0.1));border:1px solid rgba(139,92,246,0.1);border-radius:1rem;">'
            '<img src="'
            + MARIA_AVATAR
            + '" alt="Mar\u00cdA" style="width:8rem;height:8rem;'
            'margin:0 auto;object-fit:contain;opacity:0.6;" />'
            '<p style="text-align:center;font-size:0.875rem;color:#64748b;margin-top:1rem;">'
            "Selecciona otra estaci\u00f3n para ver m\u00e1s detalles</p></div>"
        )

    # Pre-calcular variables para evitar expresiones complejas dentro del f-string
    icon = active["icon"]
    number = active["number"]
    title = active["title"]
    aliado = active["aliado"]
    objetivo = active["objetivo"]
    foco = active["foco"]
    quote = active["quote"]
    text_color = active["textColor"]
    # Convertir clases Tailwind a colores reales para el gradiente del icono
    color_class = active["color"]
    color_from_map = {
        "from-amber-500": "#f59e0b",
        "from-blue-500": "#3b82f6",
        "from-emerald-500": "#10b981",
        "from-violet-500": "#8b5cf6",
        "from-fuchsia-500": "#d946ef",
        "from-rose-500": "#f43f5e",
    }
    color_to_map = {
        "to-yellow-400": "#facc15",
        "to-cyan-400": "#22d3ee",
        "to-teal-400": "#14b8a6",
        "to-purple-400": "#a855f7",
        "to-pink-400": "#ec4899",
        "to-red-400": "#ef4444",
    }
    grad_start = next(
        (v for k, v in color_from_map.items() if k in color_class), "#8b5cf6"
    )
    grad_end = next((v for k, v in color_to_map.items() if k in color_class), "#a855f7")
    icon_gradient = f"linear-gradient(135deg,{grad_start},{grad_end})"

    return f"""
            <div style="padding:2rem 2.5rem;border-radius:1.5rem;border:1px solid rgba(139,92,246,0.2);background:rgba(139,92,246,0.05);backdrop-filter:blur(4px);transition:all 0.5s;">
                <div style="display:grid;grid-template-columns:1fr;gap:2rem;" class="lg-grid-3">
                    <div class="lg-col-2" style="display:flex;flex-direction:column;gap:1.5rem;">
                        <div style="display:flex;align-items:flex-start;gap:1rem;">
                            <div style="padding:1rem;border-radius:1rem;background:{icon_gradient};box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);"><span style="font-size:2rem;">{icon}</span></div>
                            <div>
                                <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.5rem;">
                                    <span style="font-size:0.875rem;font-weight:700;color:{text_color};">Estación #{number}</span>
                                    <span style="padding:0.125rem 0.5rem;background:rgba(255,255,255,0.1);border-radius:0.25rem;font-size:0.75rem;color:#94a3b8;">15 minutos</span>
                                </div>
                                <h3 style="font-size:1.5rem;font-weight:700;color:white;">{title}</h3>
                            </div>
                        </div>
                        <div style="display:flex;flex-wrap:wrap;gap:1rem;">
                            <div style="display:flex;align-items:center;gap:0.5rem;padding:0.5rem 1rem;background:rgba(255,255,255,0.05);border-radius:0.75rem;">
                                <span style="font-size:0.875rem;color:#94a3b8;">A cargo de: <strong style="color:white;">{aliado}</strong></span>
                            </div>
                            <div style="display:flex;align-items:center;gap:0.5rem;padding:0.5rem 1rem;background:rgba(255,255,255,0.05);border-radius:0.75rem;">
                                <span style="font-size:0.875rem;color:#94a3b8;">Duración: <strong style="color:white;">15 Minutos</strong></span>
                            </div>
                        </div>
                        <div style="padding:1.25rem;background:rgba(255,255,255,0.05);border-radius:1rem;border:1px solid rgba(255,255,255,0.1);">
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.5rem;">&#10145; Objetivo Principal</h4>
                            <p style="color:white;font-weight:500;">{objetivo}</p>
                        </div>
                        <div>
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.5rem;">Foco Estrat&#233;gico</h4>
                            <p style="color:#94a3b8;line-height:1.625;">{foco}</p>
                        </div>
                        <div style="padding:1.25rem;border-radius:1rem;border-left:4px solid {text_color};background:rgba(255,255,255,0.05);">
                            <p style="font-size:0.875rem;font-style:italic;color:{text_color};">"{quote}"</p>
                        </div>
                    </div>
                    <div>
                        {apps_html}
                    </div>
                </div>
            </div>
    <style>
    .lg-grid-3 {{ grid-template-columns: 1fr !important; }}
    @media (min-width: 1024px) {{ .lg-grid-3 {{ grid-template-columns: 2fr 1fr !important; }} }}
    </style>
    """


def talleres_html():
    return f"""
    <section id="talleres" style="padding:6rem 0;position:relative;overflow:hidden;">
        <div style="position:absolute;inset:0;background:linear-gradient(to bottom,#0f0a1a,#100a1c,#0f0a1a);"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="text-align:center;margin-bottom:4rem;">
                <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1.5rem;opacity:0.8;" />
                <span style="display:inline-block;padding:0.375rem 1rem;background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);border-radius:9999px;font-size:0.875rem;font-weight:500;color:#93c5fd;margin-bottom:1rem;">De la Teoría a la Práctica</span>
                <h2 style="font-size:2rem;font-weight:900;color:white;margin-bottom:1.5rem;" class="section-title">Talleres de <span class="text-gradient-violet">Co-creación</span></h2>
                <p style="font-size:1.125rem;color:#94a3b8;max-width:42rem;margin:0 auto;">30 minutos de inmersión total. Aprenderemos haciendo.</p>
            </div>
            <div style="margin-bottom:3rem;padding:1.5rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;">
                <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.5rem;text-align:center;">
                    <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;">
                        <span style="font-size:1.5rem;">⏰</span>
                        <span style="color:white;font-weight:600;">Doble Jornada</span>
                        <span style="font-size:0.875rem;color:#94a3b8;">Mañana y Tarde</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;">
                        <span style="font-size:1.5rem;">👥</span>
                        <span style="color:white;font-weight:600;">30 Minutos</span>
                        <span style="font-size:0.875rem;color:#94a3b8;">Inmersión total</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;">
                        <span style="font-size:1.5rem;">💻</span>
                        <span style="color:white;font-weight:600;">Trae tu propio dispositivo</span>
                        <span style="font-size:0.875rem;color:#94a3b8;">Hardware obligatorio</span>
                    </div>
                    <div style="display:flex;flex-direction:column;align-items:center;gap:0.5rem;grid-column:2;">
                        <span style="font-size:1.5rem;">📅</span>
                        <span style="color:white;font-weight:600;">Primeros dos talleres presenciales</span>
                        <span style="font-size:0.875rem;color:#94a3b8;">Salas del primer piso</span>
                    </div>
                </div>
            </div>
            <div style="display:grid;grid-template-columns:1fr;gap:2rem;" class="talleres-grid">
                <div style="padding:2rem;border-radius:1.5rem;border:1px solid rgba(139,92,246,0.2);background:rgba(139,92,246,0.05);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:flex;align-items:flex-start;gap:1rem;margin-bottom:1.5rem;">
                        <div style="padding:1rem;border-radius:1rem;background:linear-gradient(135deg,#8b5cf6,#a855f7);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">🔧</div>
                        <div>
                            <span style="font-size:0.875rem;font-weight:700;color:#a78bfa;">Taller #1</span>
                            <h3 style="font-size:1.25rem;font-weight:700;color:white;margin-top:0.25rem;">Aprende haciendo: Crea tu propio agente</h3>
                        </div>
                    </div>
                    <div style="display:flex;flex-direction:column;gap:1rem;">
                        <div style="display:flex;align-items:center;gap:0.5rem;"><span style="font-size:0.875rem;color:#94a3b8;">Aliado:</span><span style="font-size:0.875rem;font-weight:600;color:white;">XERTICA</span></div>
                        <div style="padding:1rem;background:rgba(255,255,255,0.05);border-radius:0.75rem;border:1px solid rgba(255,255,255,0.1);">
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.5rem;">➡ Metodología</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">100% interactivo y guiado paso a paso.</p>
                        </div>
                        <div style="padding:1rem;background:linear-gradient(135deg,rgba(255,255,255,0.05),rgba(255,255,255,0.02));border-radius:0.75rem;border:1px solid rgba(255,255,255,0.1);">
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.5rem;">Entregable Práctico</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">Un agente digital totalmente funcional, configurado para automatizar una tarea específica de tu oficina.</p>
                        </div>
                    </div>
                </div>
                <div style="padding:2rem;border-radius:1.5rem;border:1px solid rgba(59,130,246,0.2);background:rgba(59,130,246,0.05);backdrop-filter:blur(4px);transition:all 0.5s;">
                    <div style="display:flex;align-items:flex-start;gap:1rem;margin-bottom:1.5rem;">
                        <div style="padding:1rem;border-radius:1rem;background:linear-gradient(135deg,#3b82f6,#22d3ee);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">💻</div>
                        <div>
                            <span style="font-size:0.875rem;font-weight:700;color:#60a5fa;">Taller #2</span>
                            <h3 style="font-size:1.25rem;font-weight:700;color:white;margin-top:0.25rem;">AI Studio: Soluciones sin código</h3>
                        </div>
                    </div>
                    <div style="display:flex;flex-direction:column;gap:1rem;">
                        <div style="display:flex;align-items:center;gap:0.5rem;"><span style="font-size:0.875rem;color:#94a3b8;">Aliado:</span><span style="font-size:0.875rem;font-weight:600;color:white;">XERTICA / GOOGLE</span></div>
                        <div style="padding:1rem;background:rgba(255,255,255,0.05);border-radius:0.75rem;border:1px solid rgba(255,255,255,0.1);">
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.5rem;display:flex;align-items:center;gap:0.5rem;">➡ Metodología</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">Demostración estructurada de lógica de asistentes en la plataforma AI Studio.</p>
                        </div>
                        <div style="padding:1rem;background:linear-gradient(135deg,rgba(255,255,255,0.05),rgba(255,255,255,0.02));border-radius:0.75rem;border:1px solid rgba(255,255,255,0.1);">
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.5rem;">Entregable Práctico</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">Un prototipo de aplicativo lógico diseñado para resolver necesidades administrativas cotidianas.</p>
                        </div>
                    </div>
            </div>
            <!-- Taller 3 fuera del grid, centrado debajo -->
            <div style="display:flex;justify-content:center;margin-top:2rem;">
                <div style="padding:2rem;border-radius:1.5rem;border:1px solid rgba(245,158,11,0.2);background:rgba(245,158,11,0.05);backdrop-filter:blur(4px);transition:all 0.5s;width:100%;max-width:48rem;">
                    <div style="display:flex;align-items:flex-start;gap:1rem;margin-bottom:1.5rem;">
                        <div style="padding:1rem;border-radius:1rem;background:linear-gradient(135deg,#f59e0b,#ef4444);box-shadow:0 10px 15px -3px rgba(0,0,0,0.3);">🤖</div>
                        <div>
                            <span style="font-size:0.875rem;font-weight:700;color:#fbbf24;">Taller #3 · Virtual</span>
                            <h3 style="font-size:1.25rem;font-weight:700;color:white;margin-top:0.25rem;">Cómo pasar de la Automatización Robótica tradicional a Procesos Inteligentes y Autónomos</h3>
                        </div>
                    </div>
                    <div style="display:flex;flex-direction:column;gap:1rem;">
                        <div style="display:flex;flex-wrap:wrap;gap:1.5rem;">
                            <div style="display:flex;align-items:center;gap:0.5rem;"><span style="font-size:0.875rem;color:#94a3b8;">Aliado:</span><span style="font-size:0.875rem;font-weight:600;color:white;">UIPATH</span></div>
                            <div style="display:flex;align-items:center;gap:0.5rem;"><span style="font-size:0.875rem;">📅</span><span style="font-size:0.875rem;color:#94a3b8;">Miércoles 3 de junio de 2026</span></div>
                            <div style="display:flex;align-items:center;gap:0.5rem;"><span style="font-size:0.875rem;">⏰</span><span style="font-size:0.875rem;color:#94a3b8;">10:30 a.m. – 12:00 p.m.</span></div>
                            <div style="display:flex;align-items:center;gap:0.5rem;"><span style="font-size:0.875rem;">🖥</span><span style="font-size:0.875rem;color:#94a3b8;">Formato Virtual</span></div>
                        </div>
                        <div style="padding:1rem;background:rgba(255,255,255,0.05);border-radius:0.75rem;border:1px solid rgba(255,255,255,0.1);">
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.75rem;display:flex;align-items:center;gap:0.5rem;">➡ Contenido de la charla</h4>
                            <ul style="list-style:none;display:flex;flex-direction:column;gap:0.5rem;margin:0;padding:0;">
                                <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="color:#fbbf24;margin-top:0.1rem;">▸</span>Evolución de la RPA hacia la Automatización Agentic (RPA es poner en "piloto automático" las tareas digitales más pesadas).</li>
                                <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="color:#fbbf24;margin-top:0.1rem;">▸</span>Diferencias clave entre automatización tradicional y agentizada.</li>
                                <li style="display:flex;align-items:flex-start;gap:0.5rem;font-size:0.875rem;color:#94a3b8;"><span style="color:#fbbf24;margin-top:0.1rem;">▸</span>Aplicaciones reales, casos de éxito y potencial en el sector educativo colombiano.</li>
                            </ul>
                        </div>
                        <div style="padding:1rem;background:linear-gradient(135deg,rgba(245,158,11,0.1),rgba(239,68,68,0.05));border-radius:0.75rem;border:1px solid rgba(245,158,11,0.15);">
                            <h4 style="font-size:0.875rem;font-weight:600;color:#cbd5e1;margin-bottom:0.5rem;">Impacto esperado</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">Mayor eficiencia operativa, reducción de tiempos, mejor experiencia del ciudadano y optimización del recurso público en el Ministerio.</p>
                        </div>
                        <div style="padding:0.75rem 1rem;background:rgba(255,255,255,0.03);border-radius:0.75rem;border:1px solid rgba(255,255,255,0.08);display:flex;align-items:center;gap:0.75rem;">
                            <span style="font-size:1.25rem;">🎙</span>
                            <div>
                                <span style="font-size:0.75rem;color:#64748b;display:block;">Conferencista</span>
                                <span style="font-size:0.875rem;color:#94a3b8;font-style:italic;">Especialista UIPATH en Automatización Inteligente — RPA y Agentic en sector público y privado <span style="color:#475569;">(nombre por confirmar)</span></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <div style="margin-top:3rem;padding:2rem;border-radius:1.5rem;background:linear-gradient(to right,rgba(139,92,246,0.2),rgba(37,99,235,0.1),rgba(139,92,246,0.2));border:1px solid rgba(139,92,246,0.2);">
                <div style="text-align:center;">
                    <h3 style="font-size:1.5rem;font-weight:700;color:white;margin-bottom:1rem;">El Concepto Clave: Soluciones <span style="color:#a78bfa;">'No-Code'</span></h3>
                    <p style="font-size:1.125rem;color:#94a3b8;margin-bottom:2rem;">Si sabes dar una instrucción clara, sabes crear un agente de IA.</p>
                    <div style="display:grid;grid-template-columns:1fr;gap:1.5rem;" class="nocode-grid">
                        <div style="padding:1.5rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;">
                            <div style="width:3rem;height:3rem;margin:0 auto 1rem;background:linear-gradient(135deg,#8b5cf6,#a855f7);border-radius:0.75rem;display:flex;align-items:center;justify-content:center;"><span style="color:white;font-weight:700;">1</span></div>
                            <h4 style="font-weight:700;color:white;margin-bottom:0.5rem;">Instrucción Humana</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">El funcionario escribe un reto en lenguaje natural</p>
                        </div>
                        <div style="padding:1.5rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;">
                            <div style="width:3rem;height:3rem;margin:0 auto 1rem;background:linear-gradient(135deg,#3b82f6,#22d3ee);border-radius:0.75rem;display:flex;align-items:center;justify-content:center;"><span style="color:white;font-weight:700;">2</span></div>
                            <h4 style="font-weight:700;color:white;margin-bottom:0.5rem;">El Motor Lógico (AI Studio)</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">La plataforma estructura la solución automáticamente</p>
                        </div>
                        <div style="padding:1.5rem;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:1rem;">
                            <div style="width:3rem;height:3rem;margin:0 auto 1rem;background:linear-gradient(135deg,#d946ef,#ec4899);border-radius:0.75rem;display:flex;align-items:center;justify-content:center;"><span style="color:white;font-weight:700;">3</span></div>
                            <h4 style="font-weight:700;color:white;margin-bottom:0.5rem;">El Agente Funcional</h4>
                            <p style="font-size:0.875rem;color:#94a3b8;">Un aplicativo listo para ejecutar la tarea de forma autónoma</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <style>
    .talleres-grid {{ grid-template-columns: 1fr !important; }}
    @media (min-width: 1024px) {{ .talleres-grid {{ grid-template-columns: 1fr 1fr !important; }} }}
    .nocode-grid {{ grid-template-columns: 1fr !important; }}
    @media (min-width: 640px) {{ .nocode-grid {{ grid-template-columns: 1fr 1fr 1fr !important; }} }}
    </style>
    """


def footer_html():
    _maria_footer = maria_logo_html("1.875rem")
    return f"""
    <footer style="position:relative;padding:4rem 0;border-top:1px solid rgba(139,92,246,0.1);">
        <div style="position:absolute;inset:0;background:#0a0612;"></div>
        <div class="max-w-7xl" style="position:relative;z-index:10;">
            <div style="display:grid;grid-template-columns:1fr;gap:3rem;align-items:center;" class="footer-grid">
                <div style="text-align:center;">
                    <img src="{LOGO}" alt="MEN" style="height:4rem;margin:0 auto 1rem;object-fit:contain;" />
                    <p style="font-size:0.875rem;color:#64748b;">Ministerio de Educación Nacional<br />República de Colombia</p>
                </div>
                <div style="text-align:center;">
                    <div style="display:inline-flex;align-items:center;gap:0.75rem;margin-bottom:1rem;">
                        <span style="font-size:2rem;">🤖</span>
                        <span style="font-size:1.875rem;font-weight:900;">{_maria_footer}</span>
                    </div>
                    <p style="font-size:0.875rem;color:#64748b;margin-bottom:1rem;">Transformando la gestión pública a través de la Inteligencia Artificial</p>
                    <div style="display:flex;align-items:center;justify-content:center;gap:0.5rem;font-size:0.75rem;color:#475569;">
                        <span>Política de Gobierno Digital</span>
                        <span>|</span>
                        <span>IA LAB MEN</span>
                    </div>
                </div>
                <div style="text-align:center;">
                    <h4 style="font-size:0.875rem;font-weight:600;color:#94a3b8;margin-bottom:1rem;">Enlaces del evento</h4>
                    <nav style="display:flex;flex-direction:column;gap:0.5rem;">
                        <a href="#proposito" style="font-size:0.875rem;color:#64748b;text-decoration:none;transition:color 0.3s;">Propósito IA LAB</a>
                        <a href="#maria" style="font-size:0.875rem;color:#64748b;text-decoration:none;transition:color 0.3s;">Conoce a MarIA</a>
                        <a href="#feria" style="font-size:0.875rem;color:#64748b;text-decoration:none;transition:color 0.3s;">La Arquitectura de la Feria</a>
                        <a href="#circuito" style="font-size:0.875rem;color:#64748b;text-decoration:none;transition:color 0.3s;">Circuito de Aprendizaje</a>
                        <a href="#estaciones" style="font-size:0.875rem;color:#64748b;text-decoration:none;transition:color 0.3s;">Las 6 Estaciones</a>
                        <a href="#talleres" style="font-size:0.875rem;color:#64748b;text-decoration:none;transition:color 0.3s;">Talleres de Co-creación</a>
                    </nav>
                </div>
            </div>
            <div style="margin:2.5rem 0;height:1px;background:linear-gradient(to right,transparent,rgba(139,92,246,0.2),transparent);"></div>
            <div style="display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:1rem;" class="footer-bottom">
                <p style="font-size:0.75rem;color:#475569;display:flex;align-items:center;gap:0.25rem;">Hecho con <span style="color:#f43f5e;">❤</span> por el Ministerio de Educación Nacional</p>
                <p style="font-size:0.75rem;color:#475569;">Feria Digital: El Parche de MarIA | 2025</p>
            </div>
        </div>
    </footer>
    <style>
    .footer-grid {{ grid-template-columns: 1fr !important; }}
    @media (min-width: 1024px) {{ .footer-grid {{ grid-template-columns: 1fr 1fr 1fr !important; }} .footer-grid > div:first-child {{ text-align: left !important; }} .footer-grid > div:last-child {{ text-align: right !important; }} }}
    .footer-bottom {{ flex-direction: column !important; }}
    @media (min-width: 640px) {{ .footer-bottom {{ flex-direction: row !important; }} }}
    </style>
    """


st.markdown(CSS, unsafe_allow_html=True)

# ── session_state para la estación activa ────────────────────────────────────
if "station" not in st.session_state:
    st.session_state.station = 0
active_idx = st.session_state.station
# ─────────────────────────────────────────────────────────────────────────────

st.markdown(nav_html(), unsafe_allow_html=True)
st.markdown(hero_html(), unsafe_allow_html=True)
st.markdown(proposito_html(), unsafe_allow_html=True)
st.markdown(identidad_html(), unsafe_allow_html=True)
st.markdown(arquitectura_html(), unsafe_allow_html=True)
st.markdown(bienvenida_html(), unsafe_allow_html=True)
st.markdown(circuito_html(), unsafe_allow_html=True)

# ── Sección Estaciones (100 % Python, sin JavaScript) ───────────────────────
# 1. Encabezado HTML de la sección (self-contained)
st.markdown(estaciones_section_start_html(), unsafe_allow_html=True)

# 2. CSS para las pestañas nativas de Streamlit
_TAB_COLORS = [
    ("#f59e0b", "#facc15"),
    ("#3b82f6", "#22d3ee"),
    ("#10b981", "#14b8a6"),
    ("#8b5cf6", "#a855f7"),
    ("#d946ef", "#ec4899"),
    ("#f43f5e", "#ef4444"),
]
_nth_css = "".join(
    "div[data-testid='stHorizontalBlock'] "
    "div[data-testid='column']:nth-child(" + str(_ci + 1) + ") "
    "button[kind='primary']{"
    "background:linear-gradient(135deg," + _cs + "," + _ce + ")!important;"
    "border-color:" + _cs + "!important;"
    "box-shadow:0 4px 15px " + _cs + "55!important;}"
    for _ci, (_cs, _ce) in enumerate(_TAB_COLORS)
)


# 3. Pestañas: botones nativos Streamlit — clic dispara rerun directamente, sin JS
_tab_cols = st.columns(6)
for _i, _est in enumerate(ESTACIONES_DATA):
    with _tab_cols[_i]:
        _lbl = f"{_est['icon']} {_est['number']} {_est['shortTitle']}"
        if st.button(
            _lbl,
            key=f"_stab_{_i}",
            type="primary" if _i == active_idx else "secondary",
            use_container_width=True,
        ):
            st.session_state.station = _i
            st.rerun()

# 4. Panel de detalle (HTML puro, self-contained)
st.markdown(
    "<div style='background:linear-gradient(to bottom,#0e0718,#0f0a1a);"
    "padding:0 0 5rem;'>"
    "<div class='max-w-7xl' style='max-width:1280px;margin:0 auto;padding:0 2rem;'>"
    + estaciones_panel_html(ESTACIONES_DATA[active_idx])
    + "</div></div>",
    unsafe_allow_html=True,
)
# ────────────────────────────────────────────────────────────────────────────

st.markdown(talleres_html(), unsafe_allow_html=True)
st.markdown(footer_html(), unsafe_allow_html=True)
