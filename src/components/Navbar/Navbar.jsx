import { Links } from "./Links"
import { useTheme } from "../DarkmodeControl/Darkmode"
import { MdDarkMode } from 'react-icons/md'
import { BsFillLightbulbFill } from 'react-icons/bs'
import { useState } from 'react';

export const Navbar = () => {
    const { theme, setTheme } = useTheme()
    console.log(theme)
    const [open, setOpen] = useState(false)
    return (
        <>
            <div className="md:flex md:justify-between md:py-4 my-4 ml-4">
                <img src="/logo-bank.png" className="h-14 hover:animate-spin saturate-200 shrink-0 ml-4 my-4" />
                <div className="md:flex md:items-center md:gap-6">
                    <div className="flex  md:flex md:justify-self-end">
                        {theme === "light" ? (<MdDarkMode size={30} className="cursor-pointer text-escure" onClick={() => setTheme("dark")} />) :
                            (<BsFillLightbulbFill size={30} className="cursor-pointer text-white" onClick={() => setTheme("light")} />)}
                    </div>


                    <div onClick={() => setOpen(!open)} className="text-3xl absolute right-8 top-6 cursor-pointer md:hidden">
                        <ion-icon name={open ? 'close' : 'menu'}></ion-icon>
                    </div>

                    <Links linkName="Home" />
                    <Links linkName="Contact" />
                    <Links linkName="About" />
                    <Links linkName="Wallet" />

                    <a href="#" className="w-20 h-10 text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center py-2 mr-4">Login</a>
                </div>
            </div>
        </>
    )
}
