export const ArrowDown = (props) => {
    return (
        <div className="flex justify-center items-center mt-2">
            <a href={"#" + props.href}><img src="/arrow-down.svg" className="h-14 animate-bounce bg-escure dark: bg-gradient-to-br from-pink-500 via-maincolor0 to-maincolor rounded-full select-none" /></a>
        </div>
    )
}