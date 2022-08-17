import { Links } from "./Links"
import { useTheme } from "../DarkmodeControl/Darkmode"
import { MdDarkMode } from 'react-icons/md'
import { BsFillLightbulbFill } from 'react-icons/bs'

export const Navbar = () => {
    const { theme, setTheme } = useTheme()
        console.log(theme)
    return (
        <>
            <div className="flex justify-between px-10 py-4">
                <img src="/logo-bank.png" className="h-14" />
                <div className="flex items-center gap-5">
                    {theme === "light" ? (<MdDarkMode size={30} className="cursor-pointer" onClick={() => setTheme("dark")}/>) : 
                    (<BsFillLightbulbFill size={30} className="cursor-pointer text-white" onClick={() => setTheme("light")}/>)}
                    
                    <Links linkName="Home" />
                    <Links linkName="Contact" />
                    <Links linkName="About" />
                    <Links linkName="Wallet" />
                    <button className="w-20 h-10 text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100">Assinar</button>
                </div>
            </div>
        </>
    )
}
