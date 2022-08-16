import { Navbar } from './components/Navbar/Navbar'
import { Content } from './components/Content/Content'
import { DarkMode } from './components/DarkmodeControl/Darkmode'

export const App = () => {
  return (
    <DarkMode>
      <div className="bg-darkmode h-screen">  
        <Navbar />
        <Content />
      </div>
    </DarkMode>
  )
}


