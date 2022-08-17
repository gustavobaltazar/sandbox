import { MdDarkMode } from 'react-icons/md'
import { BsFillLightbulbFill } from 'react-icons/bs'
import { useTheme } from "../DarkmodeControl/Darkmode"
import { Card } from '../Cards/Card'

export const LoginPage = () => {
    const { theme, setTheme } = useTheme()
    return (
        <>
            <img src="/logo-bank.png" className="h-14 fixed m-5" />
            <div className="centralize px-10">
                <div className="absolute right-0 top-6 h-16 w-16">
                    {theme === "light" ? (<MdDarkMode size={30} className="cursor-pointer" onClick={() => setTheme("dark")} />) :
                        (<BsFillLightbulbFill size={30} className="cursor-pointer text-white" onClick={() => setTheme("light")} />)}
                </div>
                <Card />
            </div>
        </>
    )
}