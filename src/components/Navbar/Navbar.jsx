import { Links } from "./Links"
import { useTheme } from "../DarkmodeControl/Darkmode"
import { MdDarkMode } from 'react-icons/md'
import { BsFillSunFill } from 'react-icons/bs'
import { useState } from 'react';

export const Navbar = () => {
    const { theme, setTheme } = useTheme()
    console.log(theme)
    const [open, setOpen] = useState(false)
    return (
        <>
            <div className="md:flex md:justify-between md:py-4 my-4 ml-4 md:mr-8">
            <img src="/logo-bank.png" className="h-14 hover:animate-spin saturate-200 shrink-0 ml-4 my-4" />
                <div onClick={() => setOpen(!open)} className="text-3xl text-maincolor absolute right-8 top-6 cursor-pointer md:hidden">
                    <ion-icon className="" name={open ? 'close' : 'menu'}></ion-icon>
                </div>
                <div className={`md:flex md:flex-row md:gap-4 md:-items-center md:pb-0 pb-4 bg-escure md:text-black md:bg-transparent text-white absolute text-2xl py-4 dark:bg-white
                md:dark:bg-transparent md:dark:text-white dark:text-escure md:static left-0 w-full md:w-auto md:pl-0 pl-4 flex flex-col text-center items-center gap-3 transition-all duration-[500ms] ease-in ${open ? 'top-20' : 'top-[-490px]'} `}>
                    {theme === "light" ? (<MdDarkMode size={30} className="cursor-pointer text-white dark:text-white md:text-escure" onClick={() => setTheme("dark")} />) :
                        (<BsFillSunFill size={30} className="cursor-pointer text-white dark:text-escure md:dark:text-white" onClick={() => setTheme("light")} />)}

                    <Links linkName="Home" />
                    <Links linkName="Contact" />
                    <Links linkName="About" />
                    <Links linkName="Wallet" />
                    <a href="/LoginPage" className="text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center px-4 py-2">Login</a>
                </div>
            </div>
        </>
    )
}
