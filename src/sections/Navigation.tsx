import { useState, useEffect } from 'react'
import { Menu, X, Bot } from 'lucide-react'

export default function Navigation() {
  const [isScrolled, setIsScrolled] = useState(false)
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const navLinks = [
    { href: '#proposito', label: 'Propósito' },
    { href: '#maria', label: 'Conoce a MarIA' },
    { href: '#feria', label: 'La Feria' },
    { href: '#circuito', label: 'Circuito' },
    { href: '#estaciones', label: 'Estaciones' },
    { href: '#talleres', label: 'Talleres' },
  ]

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${
        isScrolled
          ? 'bg-[#0f0a1a]/95 backdrop-blur-xl border-b border-violet-500/20 shadow-lg shadow-violet-500/5'
          : 'bg-transparent'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16 lg:h-20">
          <a href="#" className="flex items-center gap-3 group">
            <img
              src="/assets/logo-men.png"
              alt="Ministerio de Educación Nacional"
              className="h-10 lg:h-12 w-auto object-contain transition-transform group-hover:scale-105"
            />
          </a>

          <div className="hidden lg:flex items-center gap-1">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                className="px-4 py-2 text-sm font-medium text-slate-300 hover:text-white hover:bg-violet-500/10 rounded-lg transition-all duration-300"
              >
                {link.label}
              </a>
            ))}
          </div>

          <div className="flex items-center gap-3">
            <a
              href="#articulacion"
              className="hidden sm:flex items-center gap-2 px-5 py-2.5 bg-gradient-to-r from-violet-600 to-blue-600 hover:from-violet-500 hover:to-blue-500 text-white text-sm font-semibold rounded-full transition-all duration-300 hover:shadow-lg hover:shadow-violet-500/25"
            >
              <Bot className="w-4 h-4" />
              Únete al evento
            </a>

            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="lg:hidden p-2 text-slate-300 hover:text-white hover:bg-violet-500/10 rounded-lg transition-all"
            >
              {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {isMobileMenuOpen && (
        <div className="lg:hidden bg-[#0f0a1a]/98 backdrop-blur-xl border-t border-violet-500/20">
          <div className="px-4 py-4 space-y-1">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                onClick={() => setIsMobileMenuOpen(false)}
                className="block px-4 py-3 text-slate-300 hover:text-white hover:bg-violet-500/10 rounded-lg transition-all font-medium"
              >
                {link.label}
              </a>
            ))}
            <a
              href="#articulacion"
              onClick={() => setIsMobileMenuOpen(false)}
              className="block sm:hidden mt-3 px-4 py-3 bg-gradient-to-r from-violet-600 to-blue-600 text-white text-center font-semibold rounded-lg"
            >
              Únete al evento
            </a>
          </div>
        </div>
      )}
    </nav>
  )
}
