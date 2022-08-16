import { useState, useContext, createContext, useEffect } from 'react'
const themeContext = createContext()

export const DarkMode = ({ children }) => {
    const [isDarkMode, setIsDarkMode] = useState(localStorage.getItem("isDarkMode") !== "dark" ? "light" : "dark")

    useEffect(() => {
        const root = window.document.documentElement

        console.log("funfo")

        const removeOldTheme = isDarkMode === "dark" ? "light": "dark"
        root.classList.remove(removeOldTheme)
        root.classList.add(isDarkMode)
        localStorage.setItem("theme", isDarkMode)
    },[isDarkMode])
    return (
        <>
            <themeContext.Provider value={{isDarkMode, setIsDarkMode}}>
                { children }
            </themeContext.Provider>
        </>
    )
}

export function useTheme() {
    return useContext(themeContext)
}