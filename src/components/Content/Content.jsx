import { ArrowDown } from "./ArrowDown"

export const Content = () => {
    return (
        <>
            <div className="flex justify-center items-center py-64 text-center">
                <h1 className="select-none text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-pink-500 via-maincolor0 to-maincolor tracking-wider subpixel-antialiased leading-2">Baltas Bank é o que você precisa confia!</h1>
            </div>

            <ArrowDown href="content" />
            <div className="flex items-center py-96" id="content">
                <h1 className="text-escure dark:text-white text-xl px-5">ola ola </h1>
            </div>
        </>
    )
}
