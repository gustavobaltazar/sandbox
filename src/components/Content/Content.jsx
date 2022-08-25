import { ArrowDown } from "./ArrowDown";

export const Content = () => {
  return (
    <>
      <div className="py-44">
        <h1 className="px-6 select-none text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-pink-500 via-maincolor0 to-maincolor tracking-wider subpixel-antialiased leading-2 md:capitalize">
          Baltas Bank É o que você Precisa
        </h1> 
        <h1 className="px-6 py-6 select-none text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-pink-500 via-maincolor0 to-maincolor tracking-wider subpixel-antialiased leading-2">
          Confia!
        </h1>
      </div>

      <ArrowDown href="content" />
      <div className="flex bg-contentDark flex-col gap-6" id="content">
        <h1 className="text-maincolor dark:text-maincolor text-5xl ml-8 mr-2 tracking-wider mt-12">Cartão de Crédito</h1>
        <h1 className="ml-20 text-white text-4xl">Gratuito, Prático e moderno</h1>
        <img
          src="/credit-card.png"
          className="h-15 saturate-200 ml-4 my-4 mr-4"
        />
        <h1 className="ml-8 text-3xl text-maincolor dark:text-maincolor underline">Adquira já o seu</h1>
 
      </div>
    </>
  );
};
