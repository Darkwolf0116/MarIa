import { Bot, Heart } from 'lucide-react'

export default function Footer() {
  return (
    <footer className="relative py-16 overflow-hidden border-t border-violet-500/10">
      <div className="absolute inset-0 bg-[#0a0612]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-3 gap-12 items-center">
          {/* Logo & Info */}
          <div className="text-center lg:text-left">
            <img
              src="/assets/logo-men.png"
              alt="Ministerio de Educación Nacional"
              className="h-14 w-auto mx-auto lg:mx-0 mb-4"
            />
            <p className="text-sm text-slate-500">
              Ministerio de Educación Nacional
              <br />
              República de Colombia
            </p>
          </div>

          {/* MarIA Branding */}
          <div className="text-center">
            <div className="inline-flex items-center gap-3 mb-4">
              <Bot className="w-8 h-8 text-violet-400" />
              <span className="text-3xl font-extrabold">
                <span className="text-white">Mar</span>
                <span className="text-fuchsia-400">IA</span>
              </span>
            </div>
            <p className="text-sm text-slate-500 mb-4">
              Transformando la gestión pública a través de la Inteligencia Artificial
            </p>
            <div className="flex items-center justify-center gap-2 text-xs text-slate-600">
              <span>Política de Gobierno Digital</span>
              <span>|</span>
              <span>IA LAB MEN</span>
            </div>
          </div>

          {/* Quick Links */}
          <div className="text-center lg:text-right">
            <h4 className="text-sm font-semibold text-slate-400 mb-4">Enlaces del evento</h4>
            <nav className="space-y-2">
              {[
                { href: '#proposito', label: 'Propósito IA LAB' },
                { href: '#maria', label: 'Conoce a MarIA' },
                { href: '#feria', label: 'La Arquitectura de la Feria' },
                { href: '#circuito', label: 'Circuito de Aprendizaje' },
                { href: '#estaciones', label: 'Las 6 Estaciones' },
                { href: '#talleres', label: 'Talleres de Co-creación' },
              ].map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="block text-sm text-slate-500 hover:text-violet-400 transition-colors"
                >
                  {link.label}
                </a>
              ))}
            </nav>
          </div>
        </div>

        {/* Divider */}
        <div className="my-10 h-px bg-gradient-to-r from-transparent via-violet-500/20 to-transparent" />

        {/* Bottom */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-xs text-slate-600 flex items-center gap-1">
            Hecho con <Heart className="w-3 h-3 text-rose-500" /> por el Ministerio de Educación Nacional
          </p>
          <p className="text-xs text-slate-600">
            Feria Digital: El Parche de MarIA | 2025
          </p>
        </div>
      </div>
    </footer>
  )
}
