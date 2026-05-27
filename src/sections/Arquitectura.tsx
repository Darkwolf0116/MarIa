import { Calendar, Clock, Users, Monitor, Headphones } from 'lucide-react'

export default function Arquitectura() {
  const cards = [
    {
      icon: Calendar,
      title: 'Coordenadas',
      items: [
        'Miércoles 03 de Junio',
        '8 Horas de inmersión',
        'Salas del 1er piso',
        'Capacidad: 5 salas',
      ],
      color: 'from-violet-500 to-purple-500',
      bgColor: 'bg-violet-500/5',
      borderColor: 'border-violet-500/20',
    },
    {
      icon: Users,
      title: 'Metodología',
      items: [
        'Aprendizaje por Estaciones',
        '15 minutos por rotación',
        'Práctico y rápido',
        'Orientado a retos',
      ],
      color: 'from-blue-500 to-cyan-500',
      bgColor: 'bg-blue-500/5',
      borderColor: 'border-blue-500/20',
    },
    {
      icon: Monitor,
      title: 'Ecosistema Transversal',
      items: [
        'Impulso continuo a Google Skills',
        'Durante toda la jornada',
        'Envío de invitaciones:',
        '27 de Mayo',
      ],
      color: 'from-fuchsia-500 to-pink-500',
      bgColor: 'bg-fuchsia-500/5',
      borderColor: 'border-fuchsia-500/20',
    },
    {
      icon: Headphones,
      title: 'Soporte Tecnológico',
      items: [
        'Infraestructura garantizada',
        'Pantallas táctiles, sonido, luces',
        'Por XERTICA',
        'Estaciones #1 y #6',
      ],
      color: 'from-amber-500 to-yellow-500',
      bgColor: 'bg-amber-500/5',
      borderColor: 'border-amber-500/20',
    },
  ]

  return (
    <section id="feria" className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#110b20] to-[#0f0a1a]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-blue-500/10 border border-blue-500/30 rounded-full text-sm font-medium text-blue-300 mb-4">
            Arquitectura del Evento
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            La Arquitectura de la{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-violet-400">
              Feria
            </span>
          </h2>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            Un evento diseñado para la inmersión total en el mundo de la IA
          </p>
        </div>

        {/* Cards Grid */}
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {cards.map((card, index) => (
            <div
              key={card.title}
              className={`group relative p-6 rounded-2xl border ${card.borderColor} ${card.bgColor} backdrop-blur-sm hover:scale-[1.03] transition-all duration-500`}
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <div className={`inline-flex p-3 rounded-xl bg-gradient-to-br ${card.color} mb-5 shadow-lg`}>
                <card.icon className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-xl font-bold text-white mb-4">{card.title}</h3>
              <ul className="space-y-2.5">
                {card.items.map((item, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm text-slate-400">
                    <span className={`w-1.5 h-1.5 rounded-full bg-gradient-to-r ${card.color} mt-2 flex-shrink-0`} />
                    {item}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        {/* Invitation Banner */}
        <div className="mt-12 p-6 lg:p-8 rounded-2xl bg-gradient-to-r from-amber-500/10 via-amber-500/5 to-amber-500/10 border border-amber-500/20">
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 text-center sm:text-left">
            <div className="p-3 bg-amber-500/10 rounded-xl">
              <Clock className="w-8 h-8 text-amber-400" />
            </div>
            <div>
              <p className="text-amber-300 font-semibold text-lg">Envío de invitaciones: 27 de Mayo</p>
              <p className="text-slate-400 text-sm">Prepara tu computadora personal (Bring Your Own Device)</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
