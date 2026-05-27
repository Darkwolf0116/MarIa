import { Lightbulb, Zap, Shield, CheckCircle } from 'lucide-react'

export default function Proposito() {
  const pilares = [
    {
      icon: Lightbulb,
      title: 'Innovación',
      subtitle: 'Casos de uso prácticos en el sector educativo',
      description: 'Implementamos soluciones reales de IA que transforman procesos educativos y administrativos.',
      color: 'from-amber-500 to-yellow-400',
      bgColor: 'bg-amber-500/10',
      borderColor: 'border-amber-500/20',
    },
    {
      icon: Zap,
      title: 'Eficiencia',
      subtitle: 'Optimización de la operatividad ministerial',
      description: 'Reducimos tiempos de gestión y mejoramos la productividad de los funcionarios públicos.',
      color: 'from-violet-500 to-purple-400',
      bgColor: 'bg-violet-500/10',
      borderColor: 'border-violet-500/20',
    },
    {
      icon: Shield,
      title: 'Transformación',
      subtitle: 'Apropiación tecnológica y seguridad de la información',
      description: 'Capacitamos en el uso ético de la IA promoviendo transparencia y protección de datos.',
      color: 'from-blue-500 to-cyan-400',
      bgColor: 'bg-blue-500/10',
      borderColor: 'border-blue-500/20',
    },
  ]

  return (
    <section id="proposito" className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#140d25] to-[#0f0a1a]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16 lg:mb-20">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-violet-500/10 border border-violet-500/30 rounded-full text-sm font-medium text-violet-300 mb-4">
            IA LAB MEN
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            El propósito fundacional del{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-violet-400 to-blue-400">
              IA LAB MEN
            </span>
          </h2>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            Tres pilares que guían nuestra estrategia de transformación digital
          </p>
        </div>

        {/* Pillars Grid */}
        <div className="grid md:grid-cols-3 gap-6 lg:gap-8 mb-16">
          {pilares.map((pilar, index) => (
            <div
              key={pilar.title}
              className={`group relative p-8 rounded-2xl border ${pilar.borderColor} ${pilar.bgColor} backdrop-blur-sm hover:scale-[1.02] transition-all duration-500`}
              style={{ animationDelay: `${index * 0.15}s` }}
            >
              <div className={`inline-flex p-4 rounded-xl bg-gradient-to-br ${pilar.color} mb-6 shadow-lg`}>
                <pilar.icon className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-2xl font-bold text-white mb-2">{pilar.title}</h3>
              <p className="text-sm font-medium text-slate-400 mb-4">{pilar.subtitle}</p>
              <p className="text-slate-400 leading-relaxed">{pilar.description}</p>
            </div>
          ))}
        </div>

        {/* Base Ética */}
        <div className="relative p-8 lg:p-10 rounded-3xl bg-gradient-to-r from-violet-900/30 via-blue-900/20 to-violet-900/30 border border-violet-500/20 backdrop-blur-sm">
          <div className="absolute -top-px left-8 right-8 h-px bg-gradient-to-r from-transparent via-violet-500/50 to-transparent" />

          <div className="flex flex-col lg:flex-row items-start lg:items-center gap-6">
            <div className="flex items-center gap-4">
              <div className="p-4 bg-gradient-to-br from-violet-600 to-blue-600 rounded-xl shadow-lg">
                <CheckCircle className="w-8 h-8 text-white" />
              </div>
              <div>
                <h3 className="text-2xl font-bold text-white">Base Ética</h3>
                <p className="text-violet-300 font-medium">Ley, Moral, Cultura</p>
              </div>
            </div>
            <div className="lg:flex-1 lg:pl-8 lg:border-l border-violet-500/20">
              <p className="text-slate-300 leading-relaxed">
                Reflexión sobre el uso ético de la Inteligencia Artificial, promoviendo{' '}
                <span className="text-violet-400 font-semibold">transparencia</span>,{' '}
                <span className="text-blue-400 font-semibold">responsabilidad</span> y{' '}
                <span className="text-fuchsia-400 font-semibold">protección de la información</span>.
                Pasar de la teoría a la práctica en la gestión pública.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
