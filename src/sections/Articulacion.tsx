import { Settings, Puzzle, Calendar, MessageCircle } from 'lucide-react'

export default function Articulacion() {
  return (
    <section id="articulacion" className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#120d20] to-[#0f0a1a]" />

      {/* Decorative */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-violet-600/5 rounded-full blur-[150px]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-violet-500/10 border border-violet-500/30 rounded-full text-sm font-medium text-violet-300 mb-4">
            Articulación Institucional
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            Próximos{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-violet-400 to-blue-400">
              Pasos
            </span>
          </h2>
        </div>

        {/* Content Grid */}
        <div className="grid lg:grid-cols-2 gap-8 mb-12">
          {/* Soporte Técnico */}
          <div className="p-8 rounded-3xl bg-gradient-to-br from-violet-900/20 to-blue-900/10 border border-violet-500/20 backdrop-blur-sm">
            <div className="flex items-start gap-4 mb-6">
              <div className="p-4 bg-gradient-to-br from-violet-500 to-purple-500 rounded-2xl shadow-lg">
                <Settings className="w-8 h-8 text-white" />
              </div>
              <div>
                <h3 className="text-2xl font-bold text-white mb-2">Soporte Técnico</h3>
                <p className="text-slate-400">
                  Soporte total de infraestructura y tecnología garantizado por{' '}
                  <span className="text-violet-400 font-semibold">XERTICA</span>
                </p>
              </div>
            </div>
            <div className="p-4 bg-white/5 rounded-xl border border-white/10">
              <p className="text-sm text-slate-400">
                Especial foco en estaciones de impacto{' '}
                <span className="text-violet-400 font-semibold">#1 (Impacto IA)</span> y{' '}
                <span className="text-rose-400 font-semibold">#6 (Estrategia MEN)</span>
              </p>
            </div>
          </div>

          {/* Sinergia MEN */}
          <div className="p-8 rounded-3xl bg-gradient-to-br from-blue-900/20 to-violet-900/10 border border-blue-500/20 backdrop-blur-sm">
            <div className="flex items-start gap-4 mb-6">
              <div className="p-4 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-2xl shadow-lg">
                <Puzzle className="w-8 h-8 text-white" />
              </div>
              <div>
                <h3 className="text-2xl font-bold text-white mb-2">Sinergia MEN</h3>
                <p className="text-slate-400">
                  Operación coordinada entre todas las dependencias
                </p>
              </div>
            </div>
            <div className="flex flex-wrap gap-2">
              {['SG', 'SDO', 'OAC', 'OTSI', 'SRC'].map((sigla) => (
                <span
                  key={sigla}
                  className="px-4 py-2 bg-white/5 border border-white/10 rounded-lg text-sm font-semibold text-blue-300"
                >
                  {sigla}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Launch Banner */}
        <div className="relative p-8 lg:p-10 rounded-3xl bg-gradient-to-r from-amber-500/10 via-amber-500/5 to-amber-500/10 border border-amber-500/20 overflow-hidden">
          <div className="absolute -top-20 -right-20 w-60 h-60 bg-amber-500/10 rounded-full blur-[80px]" />

          <div className="relative grid lg:grid-cols-2 gap-8 items-center">
            <div className="flex items-center gap-6">
              <div className="p-5 bg-gradient-to-br from-amber-500 to-yellow-500 rounded-2xl shadow-lg shadow-amber-500/20">
                <Calendar className="w-10 h-10 text-white" />
              </div>
              <div>
                <h3 className="text-2xl lg:text-3xl font-extrabold text-white mb-2">
                  Lanzamiento de Invitación Oficial
                </h3>
                <p className="text-amber-300 font-semibold text-lg">27 de Mayo</p>
              </div>
            </div>
            <div className="flex items-start gap-4 p-5 bg-white/5 rounded-2xl border border-white/10">
              <MessageCircle className="w-6 h-6 text-violet-400 flex-shrink-0 mt-1" />
              <p className="text-slate-300 italic">
                "El cambio cultural comienza aquí. ¡Con MarIA, tú solo confía!"
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
