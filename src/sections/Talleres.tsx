import { Wrench, Code, Laptop, ArrowRight, Clock, Users } from 'lucide-react'

export default function Talleres() {
  const talleres = [
    {
      number: '1',
      title: 'Aprende haciendo: Crea tu propio agente',
      aliado: 'XERTICA',
      icon: Wrench,
      metodologia: '100% interactivo y guiado paso a paso.',
      entregable: 'Un agente digital totalmente funcional, configurado para automatizar una tarea específica de tu oficina.',
      color: 'from-violet-500 to-purple-500',
      bgColor: 'bg-violet-500/5',
      borderColor: 'border-violet-500/20',
      textColor: 'text-violet-400',
    },
    {
      number: '2',
      title: 'AI Studio: Soluciones sin código',
      aliado: 'XERTICA / GOOGLE',
      icon: Code,
      metodologia: 'Demostración estructurada de lógica de asistentes en la plataforma AI Studio.',
      entregable: 'Un prototipo de aplicativo lógico diseñado para resolver necesidades administrativas cotidianas.',
      color: 'from-blue-500 to-cyan-500',
      bgColor: 'bg-blue-500/5',
      borderColor: 'border-blue-500/20',
      textColor: 'text-blue-400',
    },
  ]

  return (
    <section id="talleres" className="relative py-24 lg:py-32 overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-[#100a1c] to-[#0f0a1a]" />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-16">
          <img
            src="/assets/logo-men.png"
            alt="MEN"
            className="h-12 w-auto mx-auto mb-6 opacity-80"
          />
          <span className="inline-block px-4 py-1.5 bg-blue-500/10 border border-blue-500/30 rounded-full text-sm font-medium text-blue-300 mb-4">
            De la Teoría a la Práctica
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-white mb-6">
            Talleres de{' '}
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-violet-400">
              Co-creación
            </span>
          </h2>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            30 minutos de inmersión total. Aprenderemos haciendo.
          </p>
        </div>

        {/* Info Banner */}
        <div className="mb-12 p-6 bg-white/5 border border-white/10 rounded-2xl">
          <div className="grid sm:grid-cols-3 gap-6 text-center">
            <div className="flex flex-col items-center gap-2">
              <Clock className="w-6 h-6 text-violet-400" />
              <span className="text-white font-semibold">Doble Jornada</span>
              <span className="text-sm text-slate-400">Mañana y Tarde</span>
            </div>
            <div className="flex flex-col items-center gap-2">
              <Users className="w-6 h-6 text-blue-400" />
              <span className="text-white font-semibold">30 Minutos</span>
              <span className="text-sm text-slate-400">Inmersión total</span>
            </div>
            <div className="flex flex-col items-center gap-2">
              <Laptop className="w-6 h-6 text-fuchsia-400" />
              <span className="text-white font-semibold">Bring Your Own Device</span>
              <span className="text-sm text-slate-400">Hardware obligatorio</span>
            </div>
          </div>
        </div>

        {/* Talleres Grid */}
        <div className="grid lg:grid-cols-2 gap-8">
          {talleres.map((taller) => (
            <div
              key={taller.number}
              className={`group p-8 rounded-3xl border ${taller.borderColor} ${taller.bgColor} backdrop-blur-sm hover:scale-[1.02] transition-all duration-500`}
            >
              <div className="flex items-start gap-4 mb-6">
                <div className={`p-4 rounded-2xl bg-gradient-to-br ${taller.color} shadow-lg`}>
                  <taller.icon className="w-8 h-8 text-white" />
                </div>
                <div>
                  <span className={`text-sm font-bold ${taller.textColor}`}>Taller #{taller.number}</span>
                  <h3 className="text-xl font-bold text-white mt-1">{taller.title}</h3>
                </div>
              </div>

              <div className="space-y-4">
                <div className="flex items-center gap-2">
                  <span className="text-sm text-slate-400">Aliado:</span>
                  <span className="text-sm font-semibold text-white">{taller.aliado}</span>
                </div>

                <div className="p-4 bg-white/5 rounded-xl border border-white/10">
                  <h4 className="text-sm font-semibold text-slate-300 mb-2 flex items-center gap-2">
                    <ArrowRight className="w-4 h-4" />
                    Metodología
                  </h4>
                  <p className="text-sm text-slate-400">{taller.metodologia}</p>
                </div>

                <div className="p-4 bg-gradient-to-br from-white/5 to-white/[0.02] rounded-xl border border-white/10">
                  <h4 className="text-sm font-semibold text-slate-300 mb-2">Entregable Práctico</h4>
                  <p className="text-sm text-slate-400">{taller.entregable}</p>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* No-Code Concept */}
        <div className="mt-12 p-8 rounded-3xl bg-gradient-to-r from-violet-900/20 via-blue-900/10 to-violet-900/20 border border-violet-500/20">
          <div className="text-center">
            <h3 className="text-2xl font-bold text-white mb-4">
              El Concepto Clave: Soluciones{' '}
              <span className="text-violet-400">'No-Code'</span>
            </h3>
            <p className="text-lg text-slate-400 mb-8">
              Si sabes dar una instrucción clara, sabes crear un agente de IA.
            </p>

            <div className="grid sm:grid-cols-3 gap-6">
              <div className="p-6 bg-white/5 border border-white/10 rounded-2xl">
                <div className="w-12 h-12 mx-auto mb-4 bg-gradient-to-br from-violet-500 to-purple-500 rounded-xl flex items-center justify-center">
                  <span className="text-white font-bold">1</span>
                </div>
                <h4 className="font-bold text-white mb-2">Instrucción Humana</h4>
                <p className="text-sm text-slate-400">El funcionario escribe un reto en lenguaje natural</p>
              </div>
              <div className="p-6 bg-white/5 border border-white/10 rounded-2xl">
                <div className="w-12 h-12 mx-auto mb-4 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-xl flex items-center justify-center">
                  <span className="text-white font-bold">2</span>
                </div>
                <h4 className="font-bold text-white mb-2">El Motor Lógico (AI Studio)</h4>
                <p className="text-sm text-slate-400">La plataforma estructura la solución automáticamente</p>
              </div>
              <div className="p-6 bg-white/5 border border-white/10 rounded-2xl">
                <div className="w-12 h-12 mx-auto mb-4 bg-gradient-to-br from-fuchsia-500 to-pink-500 rounded-xl flex items-center justify-center">
                  <span className="text-white font-bold">3</span>
                </div>
                <h4 className="font-bold text-white mb-2">El Agente Funcional</h4>
                <p className="text-sm text-slate-400">Un aplicativo listo para ejecutar la tarea de forma autónoma</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
