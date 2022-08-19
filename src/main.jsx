import React from 'react'
import ReactDOM from 'react-dom/client'
import { App } from './App'
import './index.css'
import { DarkMode } from './components/DarkmodeControl/Darkmode'
import { LoginPage } from './components/LoginPage/LoginPage'

ReactDOM.createRoot(document.getElementById('root')).render(

    <DarkMode>
      <App />
    </DarkMode>
)

