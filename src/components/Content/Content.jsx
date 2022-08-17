export const Content = () => {
    return (
        <>
            <div className="bg-white inline-block rounded-lg p-12">
                <h1 className="text-black text-2xl">Make your login</h1>
                <div className="flex flex-col w-48 gap-6">
                    <input className="rounded text-black bg-slate-200"  type="text" placeholder="Enter your username" />
                    <input className="rounded text-black bg-slate-200"  type="password" placeholder="Enter your password" />
                </div>
            </div>
        </>
    )
}