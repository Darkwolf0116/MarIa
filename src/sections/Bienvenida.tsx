import { Mic, Monitor, Navigation, Camera } from 'lucide-react'

export default function Bienvenida() {
  const features = [
    {
      icon: Mic,
      title: 'Interacción por Voz',
      description: 'Mensajes hablados dinámicos para guiar y entretener a los asistentes durante su recorrido.',
      color: 'from-violet-500 to-purple-500',
    },
    {
      icon: Monitor,
      title: 'Proyección Multimedia',
      description: 'Pantalla táctil integrada con animaciones de la marca para una experiencia inmersiva.',
      color: 'from-blue-500 to-cyan-500',
    },
    {
      icon: Navigation,
      title: 'Navegación Autónoma',
      description: 'Recorridos programados interactuando con los asistentes de forma autónoma y segura.',
      color: 'from-fuchsia-500 to-pink-500',
    },
    {
      icon: Camera,
      title: 'Fotocabina Interactiva',
      description: 'Captura de momentos clave del evento guiados por voz para recordar la experiencia.',
      color: 'from-amber-500 to-yellow-500',
    },
  ]

  return (
    <section className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#0d0818] to-[#0f0a1a]" />

      {/* Decorative */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-violet-600/5 rounded-full blur-[150px]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-violet-500/10 border border-violet-500/30 rounded-full text-sm font-medium text-violet-300 mb-4">
            Punto de Contacto 0
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            La Experiencia de{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-violet-400 to-blue-400">
              Bienvenida
            </span>
          </h2>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            Un robot físico te acompañará desde el primer momento
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Robot Image */}
          <div className="relative flex justify-center order-2 lg:order-1">
            <div className="relative group">
              <div className="absolute inset-0 bg-gradient-to-br from-blue-500/20 via-violet-500/20 to-cyan-500/20 rounded-full blur-3xl scale-125 group-hover:scale-150 transition-transform duration-700" />
              <img
                src="/assets/robot-maria.png"
                alt="Robot MarIA de Bienvenida"
                className="relative w-64 sm:w-80 lg:w-96 h-auto object-contain drop-shadow-2xl"
              />
            </div>
          </div>

          {/* Features */}
          <div className="space-y-5 order-1 lg:order-2">
            {features.map((feature, index) => (
              <div
                key={feature.title}
                className="group flex items-start gap-5 p-5 bg-white/5 border border-white/10 rounded-2xl hover:border-violet-500/30 hover:bg-violet-500/5 transition-all duration-500"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className={`flex-shrink-0 p-3 rounded-xl bg-gradient-to-br ${feature.color} shadow-lg`}>
                  <feature.icon className="w-6 h-6 text-white" />
                </div>
                <div>
                  <h3 className="text-lg font-bold text-white mb-1.5 group-hover:text-violet-300 transition-colors">
                    {feature.title}
                  </h3>
                  <p className="text-sm text-slate-400 leading-relaxed">
                    {feature.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  )
}
