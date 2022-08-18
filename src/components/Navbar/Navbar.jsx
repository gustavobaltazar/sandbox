import { Links } from "./Links"
import { useTheme } from "../DarkmodeControl/Darkmode"
import { MdDarkMode } from 'react-icons/md'
import { BsFillLightbulbFill } from 'react-icons/bs'

export const Navbar = () => {
    const { theme, setTheme } = useTheme()
    console.log(theme)
    return (
        <>
            <div className="flex justify-between py-4">
                <img src="/logo-bank.png" className="h-14 hover:animate-spin saturate-200 shrink-0" />
                <div className="flex items-center gap-6">
                    <div className="flex justify-self-end">
                        {theme === "light" ? (<MdDarkMode size={30} className="cursor-pointer text-escure" onClick={() => setTheme("dark")} />) :
                            (<BsFillLightbulbFill size={30} className="cursor-pointer text-white" onClick={() => setTheme("light")} />)}
                    </div>
                    <Links linkName="Home" />
                    <Links linkName="Contact" />
                    <Links linkName="About" />
                    <Links linkName="Wallet" />
                    <a href="#" className="w-20 h-10 text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center py-2">Login</a>
                </div>
            </div>
        </>
    )
}
