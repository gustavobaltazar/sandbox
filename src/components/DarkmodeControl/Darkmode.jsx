import { useState, useContext, createContext, useEffect } from 'react'
const themeContext = createContext()

export const DarkMode = ({ children }) => {
    const [theme, setTheme] = useState(localStorage.getItem("theme") !== "dark" ? "light" : "dark")

    useEffect(() => {
        const root = window.document.documentElement
        const removeOldTheme = theme === "dark" ? "light" : "dark"
          
        root.classList.remove(removeOldTheme)
        root.classList.add(theme)
        localStorage.setItem("theme", theme)
    }, [theme])
    return (
        <themeContext.Provider value={{ theme, setTheme }}>
            {children}
        </themeContext.Provider>
    )
}

export function useTheme() {
    return useContext(themeContext)
}