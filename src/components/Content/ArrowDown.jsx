export const ArrowDown = (props) => {
    return (
        <div className="flex justify-center items-center mt-24">
            <a href={"#" + props.href}><img src="/arrow-down.svg" className="h-14 animate-bounce bg-escure dark:bg-white rounded-full" /></a>
        </div>
    )
}