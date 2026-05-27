import { Sparkles, Calendar, MapPin, Clock, ArrowDown } from 'lucide-react'

export default function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden pt-20">
      {/* Background Image */}
      <div
        className="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-30"
        style={{ backgroundImage: 'url(/assets/hero-bg.jpg)' }}
      />

      {/* Gradient Overlays */}
      <div className="absolute inset-0 bg-gradient-to-b from-[#0f0a1a] via-transparent to-[#0f0a1a]" />
      <div className="absolute inset-0 bg-gradient-to-r from-[#0f0a1a] via-transparent to-[#0f0a1a]" />

      {/* Animated Orbs */}
      <div className="absolute top-1/4 left-1/4 w-72 h-72 bg-violet-600/20 rounded-full blur-[100px] animate-pulse" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-blue-600/15 rounded-full blur-[120px] animate-pulse" style={{ animationDelay: '1s' }} />
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-fuchsia-600/10 rounded-full blur-[150px] animate-pulse" style={{ animationDelay: '2s' }} />

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32">
        <div className="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
          {/* Left Content */}
          <div className="text-center lg:text-left space-y-8 animate-slide-up">
            {/* Badge */}
            <div className="inline-flex items-center gap-2 px-4 py-2 bg-violet-500/10 border border-violet-500/30 rounded-full">
              <Sparkles className="w-4 h-4 text-violet-400" />
              <span className="text-sm font-medium text-violet-300">
                Ministerio de Educación Nacional | Política de Gobierno Digital
              </span>
            </div>

            {/* Main Title */}
            <div className="space-y-4">
              <h2 className="text-xl sm:text-2xl font-medium text-blue-300">
                Feria Digital:
              </h2>
              <h1 className="text-5xl sm:text-6xl lg:text-7xl xl:text-8xl font-extrabold leading-[0.95] tracking-tight">
                <span className="text-white">El Parche</span>
                <br />
                <span className="text-white">de </span>
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-fuchsia-400 via-violet-400 to-blue-400">
                  MarIA
                </span>
              </h1>
              <p className="text-lg sm:text-xl text-slate-400 max-w-xl mx-auto lg:mx-0 pt-4 leading-relaxed">
                Transformando la gestión pública a través de la Inteligencia Artificial
              </p>
            </div>

            {/* Event Details */}
            <div className="flex flex-wrap justify-center lg:justify-start gap-4">
              <div className="flex items-center gap-2 px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl">
                <Calendar className="w-5 h-5 text-violet-400" />
                <span className="text-sm font-medium text-slate-300">Miércoles 03 de Junio</span>
              </div>
              <div className="flex items-center gap-2 px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl">
                <Clock className="w-5 h-5 text-blue-400" />
                <span className="text-sm font-medium text-slate-300">8 Horas de inmersión</span>
              </div>
              <div className="flex items-center gap-2 px-4 py-2.5 bg-white/5 border border-white/10 rounded-xl">
                <MapPin className="w-5 h-5 text-fuchsia-400" />
                <span className="text-sm font-medium text-slate-300">Salas del 1er piso (5 salas)</span>
              </div>
            </div>

            {/* CTA */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <a
                href="#circuito"
                className="inline-flex items-center justify-center gap-2 px-8 py-4 bg-gradient-to-r from-violet-600 to-blue-600 hover:from-violet-500 hover:to-blue-500 text-white font-bold rounded-full transition-all duration-300 hover:shadow-xl hover:shadow-violet-500/25 hover:scale-105"
              >
                <Sparkles className="w-5 h-5" />
                Explora el Circuito
              </a>
              <a
                href="#maria"
                className="inline-flex items-center justify-center gap-2 px-8 py-4 bg-white/5 hover:bg-white/10 border border-white/20 text-white font-semibold rounded-full transition-all duration-300 hover:border-violet-400/50"
              >
                Conoce a MarIA
              </a>
            </div>
          </div>

          {/* Right Content - MarIA Avatar */}
          <div className="relative flex justify-center lg:justify-end animate-float">
            <div className="relative">
              {/* Glow Effect */}
              <div className="absolute inset-0 bg-gradient-to-br from-violet-500/30 via-fuchsia-500/20 to-blue-500/30 rounded-full blur-3xl scale-110" />

              {/* Avatar Image */}
              <img
                src="/assets/maria-avatar.png"
                alt="MarIA - Tu guía virtual de IA"
                className="relative w-72 h-72 sm:w-96 sm:h-96 lg:w-[450px] lg:h-[450px] object-contain drop-shadow-2xl"
              />

              {/* Floating Badge */}
              <div className="absolute -bottom-4 left-1/2 -translate-x-1/2 px-6 py-3 bg-gradient-to-r from-violet-600/90 to-blue-600/90 backdrop-blur-xl border border-violet-400/30 rounded-2xl shadow-xl shadow-violet-500/20">
                <span className="text-white font-bold text-sm whitespace-nowrap">
                  🤖 Tu guía virtual de IA
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <a href="#proposito" className="flex flex-col items-center gap-2 text-slate-500 hover:text-violet-400 transition-colors">
          <span className="text-xs font-medium">Descubre más</span>
          <ArrowDown className="w-5 h-5" />
        </a>
      </div>
    </section>
  )
}
