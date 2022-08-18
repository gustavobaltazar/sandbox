import { ArrowDown } from "./ArrowDown"

export const Content = () => {
    return (
        <>
            <div className="flex items-center py-64">
                <h1 className="animate-pulse select-none text-escure dark:text-white text-xl px-5">Baltas Bank é o que você precisa, confia!</h1>
            </div>
            
            <ArrowDown href="content"/>            
            <div className="flex items-center py-96" id="content">
                <h1 className="text-escure dark:text-white text-xl px-5">ola ola </h1>
            </div>
        </>
    )
}
