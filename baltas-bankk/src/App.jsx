import { Navbar } from './components/Navbar/Navbar'
import { Content } from './components/Content/Content'
import { DarkMode } from './components/DarkmodeControl/Darkmode'

export const App = () => {
  return (
    <div>
      <DarkMode>
        <Navbar />
        <Content />
      </DarkMode>
    </div>
  )
}


