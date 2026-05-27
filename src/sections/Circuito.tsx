import { Brain, Globe, Coffee, Bot, BookOpen, Mountain } from 'lucide-react'

export default function Circuito() {
  const estaciones = [
    {
      number: '1',
      title: 'Impacto IA',
      subtitle: 'Impacto de la IA en la sociedad',
      icon: Brain,
      color: 'from-amber-500 to-yellow-400',
      bgColor: 'bg-amber-500/10',
      borderColor: 'border-amber-500/30',
    },
    {
      number: '2',
      title: 'Ecosistema Google',
      subtitle: '¡Ok Google! Innovación sin Límites',
      icon: Globe,
      color: 'from-blue-500 to-cyan-400',
      bgColor: 'bg-blue-500/10',
      borderColor: 'border-blue-500/30',
    },
    {
      number: '3',
      title: 'Copilot Microsoft',
      subtitle: 'Copilot y un cafecito',
      icon: Coffee,
      color: 'from-emerald-500 to-teal-400',
      bgColor: 'bg-emerald-500/10',
      borderColor: 'border-emerald-500/30',
    },
    {
      number: '4',
      title: 'Creador de Agentes',
      subtitle: 'Crea e interactúa con agentes',
      icon: Bot,
      color: 'from-violet-500 to-purple-400',
      bgColor: 'bg-violet-500/10',
      borderColor: 'border-violet-500/30',
    },
    {
      number: '5',
      title: 'NotebookLM',
      subtitle: 'Tu biblioteca con superpoderes',
      icon: BookOpen,
      color: 'from-fuchsia-500 to-pink-400',
      bgColor: 'bg-fuchsia-500/10',
      borderColor: 'border-fuchsia-500/30',
    },
    {
      number: '6',
      title: 'Estrategia MEN',
      subtitle: 'La Estrategia de IA del MEN (Clímax)',
      icon: Mountain,
      color: 'from-rose-500 to-red-400',
      bgColor: 'bg-rose-500/10',
      borderColor: 'border-rose-500/30',
    },
  ]

  return (
    <section id="circuito" className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#100820] to-[#0f0a1a]" />

      {/* Background Path */}
      <div
        className="absolute inset-0 bg-cover bg-center opacity-10"
        style={{ backgroundImage: 'url(/assets/circuit-path.jpg)' }}
      />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-violet-500/10 border border-violet-500/30 rounded-full text-sm font-medium text-violet-300 mb-4">
            Circuito de Aprendizaje
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            El Circuito de{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-violet-400 via-fuchsia-400 to-blue-400">
              Aprendizaje
            </span>
          </h2>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            6 estaciones de inmersión práctica en IA, 15 minutos cada una
          </p>
        </div>

        {/* Stations Grid */}
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {estaciones.map((estacion, index) => (
            <a
              key={estacion.number}
              href="#estaciones"
              className={`group relative p-6 rounded-2xl border ${estacion.borderColor} ${estacion.bgColor} backdrop-blur-sm hover:scale-[1.03] transition-all duration-500`}
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              {/* Number Badge */}
              <div className={`absolute -top-3 -left-3 w-10 h-10 rounded-full bg-gradient-to-br ${estacion.color} flex items-center justify-center text-white font-bold text-lg shadow-lg`}>
                {estacion.number}
              </div>

              <div className="pt-4">
                <div className={`inline-flex p-3 rounded-xl bg-gradient-to-br ${estacion.color} mb-4 shadow-lg`}>
                  <estacion.icon className="w-6 h-6 text-white" />
                </div>
                <h3 className="text-xl font-bold text-white mb-2 group-hover:text-violet-300 transition-colors">
                  {estacion.title}
                </h3>
                <p className="text-sm text-slate-400">{estacion.subtitle}</p>

                <div className="mt-4 flex items-center gap-2 text-xs text-slate-500">
                  <span className="px-2 py-1 bg-white/5 rounded-md">15 min</span>
                  <span>Rotación activa</span>
                </div>
              </div>
            </a>
          ))}
        </div>

        {/* Talleres Note */}
        <div className="mt-12 flex justify-center">
          <div className="inline-flex items-center gap-3 px-6 py-4 bg-white/5 border border-white/10 rounded-2xl">
            <div className="p-2 bg-blue-500/10 rounded-lg">
              <BookOpen className="w-5 h-5 text-blue-400" />
            </div>
            <div>
              <p className="text-white font-semibold">Talleres de Co-creación</p>
              <p className="text-sm text-slate-400">2 Terminales disponibles durante el circuito</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
