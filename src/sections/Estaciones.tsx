import { Brain, Globe, Coffee, Bot, BookOpen, Mountain, ArrowRight, Users, Clock } from 'lucide-react'
import { useState } from 'react'

export default function Estaciones() {
  const [activeStation, setActiveStation] = useState(0)

  const estaciones = [
    {
      number: '1',
      title: 'Impacto de la IA en la sociedad',
      shortTitle: 'Impacto IA',
      aliado: 'XERTICA',
      icon: Brain,
      objetivo: 'Casos de uso tangibles y de alto impacto público.',
      foco: 'Presentar desde una perspectiva macro la Inteligencia Artificial mediante casos de uso reales y de alto impacto en el sector público.',
      quote: 'Aquí expandimos la mente. Mostramos cómo la IA está resolviendo problemas reales antes de enfocarnos en las herramientas.',
      color: 'from-amber-500 to-yellow-400',
      bgColor: 'bg-amber-500/5',
      borderColor: 'border-amber-500/20',
      textColor: 'text-amber-400',
    },
    {
      number: '2',
      title: '¡Ok Google! Innovación sin Límites',
      shortTitle: 'Ecosistema Google',
      aliado: 'GOOGLE',
      icon: Globe,
      objetivo: 'Presentación ágil de la suite Google AI.',
      foco: 'Una inmersión didáctica y ágil en la suite de herramientas y tecnologías de IA generativa de Google.',
      quote: 'Ecosistema transversal: Promoción activa de Google Skills.',
      color: 'from-blue-500 to-cyan-400',
      bgColor: 'bg-blue-500/5',
      borderColor: 'border-blue-500/20',
      textColor: 'text-blue-400',
    },
    {
      number: '3',
      title: 'Copilot y un cafecito',
      shortTitle: 'Copilot Microsoft',
      aliado: 'MICROSOFT',
      icon: Coffee,
      objetivo: 'Integración de IA en la productividad y agenda diaria.',
      foco: 'Descubrir cómo usar Microsoft AI para la organización de tareas, agendas, y generación de correos en el día a día. Tu copiloto del futuro.',
      quote: 'La meta es que el funcionario recupere tiempo valioso para tareas verdaderamente estratégicas.',
      color: 'from-emerald-500 to-teal-400',
      bgColor: 'bg-emerald-500/5',
      borderColor: 'border-emerald-500/20',
      textColor: 'text-emerald-400',
    },
    {
      number: '4',
      title: 'Crea e interactúa con agentes',
      shortTitle: 'Creador de Agentes',
      aliado: 'XERTICA',
      icon: Bot,
      objetivo: 'Soluciones "no-code" y asistentes autónomos.',
      foco: 'Explicar de forma sencilla cómo estructurar agentes inteligentes autónomos útiles para la gestión pública institucional.',
      quote: 'Desmitificamos la programación. La tecnología se adapta al funcionario, no al revés.',
      color: 'from-violet-500 to-purple-400',
      bgColor: 'bg-violet-500/5',
      borderColor: 'border-violet-500/20',
      textColor: 'text-violet-400',
    },
    {
      number: '5',
      title: 'Tu biblioteca con superpoderes',
      shortTitle: 'NotebookLM',
      aliado: 'XERTICA / GOOGLE',
      icon: BookOpen,
      objetivo: 'Análisis y síntesis de información compleja.',
      foco: 'Dominar NotebookLM. Cómo subir múltiples documentos complejos, normdejos, normativas o contratos, y pedirle a la IA que los cruce, analice y resuma.',
      quote: 'Ideal para equipos que procesan altos volúmenes de documentos técnicos y legales.',
      color: 'from-fuchsia-500 to-pink-400',
      bgColor: 'bg-fuchsia-500/5',
      borderColor: 'border-fuchsia-500/20',
      textColor: 'text-fuchsia-400',
    },
    {
      number: '6',
      title: 'La Estrategia de IA del MEN',
      shortTitle: 'Estrategia MEN',
      aliado: 'OTSI',
      icon: Mountain,
      objetivo: 'Aplicativos propietarios: Convalidaciones y Gratuidad.',
      foco: 'El Cerebro Estratégico: Presentación oficial de MarIA como el motor de eficiencia del MEN.',
      quote: 'No solo adoptamos herramientas externas; creamos nuestro propio ecosistema para transformar el Estado.',
      color: 'from-rose-500 to-red-400',
      bgColor: 'bg-rose-500/5',
      borderColor: 'border-rose-500/20',
      textColor: 'text-rose-400',
      apps: [
        { name: 'MarIA Convalidaciones', desc: 'Optimización de trámites de reconocimiento de títulos, reduciendo tiempos y mejorando el servicio al ciudadano.' },
        { name: 'MarIA Gratuidad', desc: 'Transparencia y precisión analítica en la asignación de subsidios de educación superior.' },
      ],
    },
  ]

  const active = estaciones[activeStation]

  return (
    <section id="estaciones" className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#0e0718] to-[#0f0a1a]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-fuchsia-500/10 border border-fuchsia-500/30 rounded-full text-sm font-medium text-fuchsia-300 mb-4">
            Matriz Diagnóstica del Ecosistema
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            Las{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-violet-400 via-fuchsia-400 to-rose-400">
              6 Estaciones
            </span>
          </h2>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            Cada estación es una experiencia de 15 minutos diseñada para transformar tu perspectiva sobre la IA
          </p>
        </div>

        {/* Station Selector */}
        <div className="flex flex-wrap justify-center gap-3 mb-12">
          {estaciones.map((est, index) => (
            <button
              key={est.number}
              onClick={() => setActiveStation(index)}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-sm font-semibold transition-all duration-300 ${
                activeStation === index
                  ? `${est.bgColor} ${est.borderColor} border text-white shadow-lg`
                  : 'bg-white/5 border border-white/10 text-slate-400 hover:bg-white/10 hover:text-white'
              }`}
            >
              <span className={`w-6 h-6 rounded-full bg-gradient-to-br ${est.color} flex items-center justify-center text-xs text-white font-bold`}>
                {est.number}
              </span>
              <span className="hidden sm:inline">{est.shortTitle}</span>
            </button>
          ))}
        </div>

        {/* Active Station Detail */}
        <div className={`p-8 lg:p-10 rounded-3xl border ${active.borderColor} ${active.bgColor} backdrop-blur-sm transition-all duration-500`}>
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Main Info */}
            <div className="lg:col-span-2 space-y-6">
              <div className="flex items-start gap-4">
                <div className={`p-4 rounded-2xl bg-gradient-to-br ${active.color} shadow-lg`}>
                  <active.icon className="w-8 h-8 text-white" />
                </div>
                <div>
                  <div className="flex items-center gap-3 mb-2">
                    <span className={`text-sm font-bold ${active.textColor}`}>Estación #{active.number}</span>
                    <span className="px-2 py-0.5 bg-white/10 rounded text-xs text-slate-400">15 minutos</span>
                  </div>
                  <h3 className="text-2xl lg:text-3xl font-bold text-white">{active.title}</h3>
                </div>
              </div>

              <div className="flex flex-wrap gap-4">
                <div className="flex items-center gap-2 px-4 py-2 bg-white/5 rounded-xl">
                  <Users className="w-4 h-4 text-slate-400" />
                  <span className="text-sm text-slate-300">A cargo de: <strong className="text-white">{active.aliado}</strong></span>
                </div>
                <div className="flex items-center gap-2 px-4 py-2 bg-white/5 rounded-xl">
                  <Clock className="w-4 h-4 text-slate-400" />
                  <span className="text-sm text-slate-300">Duración: <strong className="text-white">15 Minutos</strong></span>
                </div>
              </div>

              <div className="p-5 bg-white/5 rounded-2xl border border-white/10">
                <h4 className="text-sm font-semibold text-slate-300 mb-2 flex items-center gap-2">
                  <ArrowRight className="w-4 h-4" />
                  Objetivo Principal
                </h4>
                <p className="text-white font-medium">{active.objetivo}</p>
              </div>

              <div>
                <h4 className="text-sm font-semibold text-slate-300 mb-2">Foco Estratégico</h4>
                <p className="text-slate-400 leading-relaxed">{active.foco}</p>
              </div>

              {/* Quote */}
              <div className={`p-5 rounded-2xl border-l-4 ${active.borderColor} bg-white/5`}>
                <p className={`text-sm italic ${active.textColor}`}>"{active.quote}"</p>
              </div>
            </div>

            {/* Side Info */}
            <div className="space-y-6">
              {active.apps && (
                <div className="space-y-4">
                  <h4 className="text-lg font-bold text-white">Aplicativos MarIA</h4>
                  {active.apps.map((app) => (
                    <div key={app.name} className="p-4 bg-gradient-to-br from-violet-900/20 to-blue-900/20 border border-violet-500/20 rounded-xl">
                      <h5 className="font-bold text-violet-300 mb-2">{app.name}</h5>
                      <p className="text-sm text-slate-400">{app.desc}</p>
                    </div>
                  ))}
                </div>
              )}

              {!active.apps && (
                <div className="p-6 bg-gradient-to-br from-violet-900/10 to-blue-900/10 border border-violet-500/10 rounded-2xl">
                  <img
                    src="/assets/maria-avatar.png"
                    alt="MarIA"
                    className="w-32 h-32 mx-auto object-contain opacity-60"
                  />
                  <p className="text-center text-sm text-slate-500 mt-4">
                    Selecciona otra estación para ver más detalles
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
