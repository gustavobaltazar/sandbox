import { Links } from "./Links"
import logo from '../../assets/logo-bank.png'

export const Navbar = () => {
    return (
        <>
            <div className="flex justify-between px-10 py-4">
                <img src={logo} className="h-14" />
                <div className="flex items-center gap-5">
                    <Links linkName="Home" />
                    <Links linkName="Contact" />
                    <Links linkName="About" />
                    <Links linkName="Wallet" />
                    <button className="hover:text-2xl rounded-full bg-maincolor text-white">Assinar</button>
                </div>
            </div>
        </>
    )
}