import { Navbar } from './components/Navbar/Navbar'
import { Content } from './components/Content/Content'

export const App = () => {
  return (
    <div className="bg-darkmode h-screen">
      <Navbar />
      <Content />
    </div>
  )
}


