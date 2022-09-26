import { Inputs } from "./Inputs"
import { useState } from "react";
export const CardRegister = () => {
    const [email, setEmail] = useState("");
    const [message, setMessage] = useState("");

    const emailValidation = () => {
        const regEx = /[a-zA-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,8}(.[a-z{2,8}])?/g
        if (regEx.test(email)) {
            setMessage("Email válido")
        } else if (!regEx.test(email) && email != "") {
            setMessage("Email inválido")
        } else {
            setMessage("")
        }
    }

    const handleOnChange = (e) => {
        setEmail(e.target.value)
    }

    return (
        <div>
            <div className="text-center h-screen flex justify-center items-center">
                <div className="bg-escurinho p-24 md:p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                    <h1 className="text-white text-2xl dark:text-black mb-8">Crie sua conta</h1>
                    <div className="flex flex-col w-48 gap-6 justify-center items-center">

                        <Inputs username="Usuário" type="text" placeholder="Usuário" />
                        <Inputs username="Email" type="email" placeholder="Email" value={email} onChange={handleOnChange} />
                        <Inputs username="Senha" type="password" placeholder="Senha" />

                        <div className="flex gap-8">

                            <button href="#" onClick={emailValidation} className="w-32 h-10 text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center py-2">Register</button>
                            <a className="text-maincolor" href="/LoginPage">Já possuo uma conta!</a>
                        
                        </div>
                        <div className="text-maincolor text-3xl">{message}</div>
                    </div>
                </div>
            </div>
        </div>
    )
}