import { ArrowDown } from "./ArrowDown";

export const Content = () => {
  return (
    <>
      <div className="py-56">
        <h1 className="px-6 select-none text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-pink-500 via-maincolor0 to-maincolor tracking-wider subpixel-antialiased leading-2">
          Baltas Bank É o que você Precisa
        </h1>
        <h1 className="px-6 py-10 select-none text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-pink-500 via-maincolor0 to-maincolor tracking-wider subpixel-antialiased leading-2">
          Confia!
        </h1>
      </div>

      <ArrowDown href="content" />
      <div className="flex items-center py-96" id="content">
        <h1 className="text-escure dark:text-white text-xl px-5">ola ola </h1>
      </div>


      <div className="text-pink-500 text-2xl ml-2">
        <h1>oi maite</h1>
      </div>
    </>
  );
};
