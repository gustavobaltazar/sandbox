import React from 'react'
import ReactDOM from 'react-dom/client'
import { App } from './App'
import './index.css'
import { DarkMode } from './components/DarkmodeControl/Darkmode'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <DarkMode>
      <App />
    </DarkMode>

  </React.StrictMode>
)
