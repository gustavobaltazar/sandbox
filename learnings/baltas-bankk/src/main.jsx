import React from 'react'
import ReactDOM from 'react-dom/client'
import { App } from './App'
import './index.css'
import { DarkMode } from './components/DarkmodeControl/Darkmode'
import { LoginPage } from './components/LoginPage/LoginPage'
import { RegisterPage } from './components/RegisterPage/RegisterPage'
import { ProfilePage } from './components/ProfilePage/ProfilePage'
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/LoginPage" element={<DarkMode> <LoginPage /> </DarkMode>} />
      <Route path="/RegisterPage" element={<DarkMode> <RegisterPage /> </DarkMode>} />
      <Route path="/ProfilePage" element={<DarkMode> <ProfilePage/> </DarkMode>}/>
    </Routes>
  </BrowserRouter>
)

