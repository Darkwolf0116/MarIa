import { User, FileText, Palette, Sparkles } from 'lucide-react'

export default function Identidad() {
  const protocolos = [
    'Prohibido deformar, estirar o alterar proporciones.',
    'Respetar estrictamente la paleta institucional y márgenes de resguardo espacial.',
    'Mantener fondos de alto contraste (idealmente blancos o neutros limpios).',
  ]

  const caracteristicas = [
    {
      number: '01',
      title: 'Tipografía',
      description: 'Outfit extrabold. Color: Blanco Puro (#FFFFFF).',
      color: 'text-white',
      bgColor: 'bg-white/10',
    },
    {
      number: '02',
      title: 'Color MarIA',
      description: 'Magenta Brillante (#F500F5). Sin espacio entre palabras.',
      color: 'text-fuchsia-400',
      bgColor: 'bg-fuchsia-500/10',
    },
    {
      number: '03',
      title: 'Arco Dorado',
      description: 'Exclusivo sobre "IA". Grosor máximo 8px. Estructura de luna creciente.',
      color: 'text-amber-400',
      bgColor: 'bg-amber-500/10',
    },
  ]

  return (
    <section id="maria" className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#120822] to-[#0f0a1a]" />

      {/* Decorative */}
      <div className="absolute top-1/3 right-0 w-80 h-80 bg-fuchsia-600/10 rounded-full blur-[120px]" />
      <div className="absolute bottom-1/3 left-0 w-80 h-80 bg-violet-600/10 rounded-full blur-[120px]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-fuchsia-500/10 border border-fuchsia-500/30 rounded-full text-sm font-medium text-fuchsia-300 mb-4">
            Identidad Digital
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            Conoce a tu guía virtual:{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-fuchsia-400 via-violet-400 to-blue-400">
              MarIA
            </span>
          </h2>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
          {/* Left - Avatar */}
          <div className="relative flex justify-center order-2 lg:order-1">
            <div className="relative group">
              <div className="absolute inset-0 bg-gradient-to-br from-violet-500/20 via-fuchsia-500/20 to-blue-500/20 rounded-3xl blur-2xl scale-110 group-hover:scale-125 transition-transform duration-700" />
              <div className="relative p-8 bg-gradient-to-br from-violet-900/20 to-blue-900/20 border border-violet-500/20 rounded-3xl backdrop-blur-sm">
                <img
                  src="/assets/maria-avatar.png"
                  alt="MarIA"
                  className="w-64 h-64 sm:w-80 sm:h-80 object-contain drop-shadow-2xl"
                />
                <div className="absolute bottom-6 left-1/2 -translate-x-1/2 px-6 py-3 bg-gradient-to-r from-fuchsia-600/90 to-violet-600/90 rounded-xl border border-fuchsia-400/30 shadow-lg">
                  <span className="text-white font-bold text-lg">MarIA</span>
                </div>
              </div>
            </div>
          </div>

          {/* Right - Info */}
          <div className="space-y-8 order-1 lg:order-2">
            {/* Description */}
            <div className="p-6 bg-white/5 border border-white/10 rounded-2xl">
              <div className="flex items-start gap-4">
                <div className="p-3 bg-violet-500/10 rounded-xl">
                  <User className="w-6 h-6 text-violet-400" />
                </div>
                <div>
                  <h3 className="text-xl font-bold text-white mb-2">¿Quién es MarIA?</h3>
                  <p className="text-slate-400 leading-relaxed">
                    MarIA es el cerebro estratégico y la cara amigable de nuestra política de IA. 
                    Es una niña de <span className="text-violet-400 font-semibold">8 a 10 años</span>, curiosa, 
                    inteligente y dispuesta a ayudar.
                  </p>
                </div>
              </div>
            </div>

            {/* Identity Elements */}
            <div className="space-y-4">
              <h3 className="text-lg font-bold text-white flex items-center gap-2">
                <Palette className="w-5 h-5 text-fuchsia-400" />
                Elementos de Identidad
              </h3>
              {caracteristicas.map((item) => (
                <div
                  key={item.number}
                  className="flex items-start gap-4 p-4 bg-white/5 border border-white/10 rounded-xl hover:border-violet-500/30 transition-colors"
                >
                  <span className={`inline-flex items-center justify-center w-10 h-10 ${item.bgColor} rounded-lg text-sm font-bold ${item.color}`}>
                    {item.number}
                  </span>
                  <div>
                    <h4 className="font-semibold text-white">{item.title}</h4>
                    <p className="text-sm text-slate-400">{item.description}</p>
                  </div>
                </div>
              ))}
            </div>

            {/* Protocol */}
            <div className="p-6 bg-amber-500/5 border border-amber-500/20 rounded-2xl">
              <h3 className="text-lg font-bold text-white flex items-center gap-2 mb-4">
                <FileText className="w-5 h-5 text-amber-400" />
                Protocolo de Identidad
              </h3>
              <ul className="space-y-3">
                {protocolos.map((protocolo, index) => (
                  <li key={index} className="flex items-start gap-3 text-sm text-slate-400">
                    <Sparkles className="w-4 h-4 text-amber-400 mt-0.5 flex-shrink-0" />
                    {protocolo}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
