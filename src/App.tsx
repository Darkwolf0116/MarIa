import Hero from './sections/Hero'
import Proposito from './sections/Proposito'
import Identidad from './sections/Identidad'
import Arquitectura from './sections/Arquitectura'
import Bienvenida from './sections/Bienvenida'
import Circuito from './sections/Circuito'
import Estaciones from './sections/Estaciones'
import Talleres from './sections/Talleres'
import Articulacion from './sections/Articulacion'
import Footer from './sections/Footer'
import Navigation from './sections/Navigation'

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-hero">
      <Navigation />
      <Hero />
      <Proposito />
      <Identidad />
      <Arquitectura />
      <Bienvenida />
      <Circuito />
      <Estaciones />
      <Talleres />
      <Articulacion />
      <Footer />
    </div>
  )
}
