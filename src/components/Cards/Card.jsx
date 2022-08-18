import { Inputs } from "./Inputs"
export const Card = () => {
    return (
        <div className="text-center h-screen flex justify-center items-center">
            <div className="bg-escurinho p-36 text-center text-white dark:bg-white inline-block rounded-lg">
                <h1 className="text-white text-2xl dark:text-black mb-8">Make your login</h1>
                <div className="flex flex-col w-48 gap-6 justify-center items-center">
                    <Inputs username="Username" type="text" placeholder="Username" />
                    <Inputs username="Password" type="password" placeholder="Password" />
                    <div className="flex gap-8">
                        <a href="#" className="w-32 h-10 text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center py-2">Login</a>
                        <a className="text-maincolor" href="">Don't have account</a>
                    </div>
                </div>
            </div>
        </div>
    )
}