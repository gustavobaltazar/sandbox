export const Inputs = (props, onChange = "") => {
    return (
        <div className="flex flex-col w-84 md:w-96">
            <span className="dark:text-black flex">{props.username}</span>
            <input className="input-style bg-escurinho border-none dark:bg-white focus:outline-none focus:shadow-outline" type={props.type} placeholder={props.placeholder} value={props.value} onChange={props.onChange}/>
        </div>
    )
}