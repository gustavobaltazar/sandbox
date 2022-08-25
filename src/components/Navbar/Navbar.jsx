import { Links } from "./Links";
import { useTheme } from "../DarkmodeControl/Darkmode";
import { MdDarkMode } from "react-icons/md";
import { BsFillSunFill } from "react-icons/bs";
import { useState } from "react";

export const Navbar = () => {
  const { theme, setTheme } = useTheme();
  console.log(theme);
  const [open, setOpen] = useState(false);
  return (
    <>
   
      <div className="md:flex md:justify-between my-4 ml-4 md:mr-12 md:items-center md:text-center">
      <img
          src="/baltas-bank-logo.png"
          className="h-56  pt-12 saturate-200 shrink-0"
        />
        <div
          onClick={() => setOpen(!open)}
          className="text-3xl text-maincolor absolute right-10 top-24  cursor-pointer md:hidden"
        >
          <ion-icon name={open ? "close" : "menu"}></ion-icon>
        </div>
        <div
          className={`md:flex md:flex-row md:justify=center md:items-center md:mb-12 md:gap-2 bg-escure md:text-black md:bg-transparent text-white absolute text-2xl py-4 dark:bg-white
                md:dark:bg-transparent md:dark:text-white md:h-0 dark:text-escure md:static left-0 w-screen md:w-auto ease-in ${
                  open
                    ? "top-20 h-screen z-40 flex flex-col justify-center items-center text-center gap-1 transition-all duration-[500ms]"
                    : "top-[-490px] h-0 transition-all duration-[500ms] ease-out duration-[500ms]"
                } `}
        >
          {theme === "light" ? (
            <MdDarkMode
              size={30}
              className="cursor-pointer text-white dark:text-white md:text-escure"
              onClick={() => setTheme("dark")}
            />
          ) : (
            <BsFillSunFill
              size={30}
              className="cursor-pointer text-white dark:text-escure md:dark:text-white"
              onClick={() => setTheme("light")}
            />
          )}
          <div className="flex flex-col justify-center text-center gap-2 w-full md:flex md:flex-row md:gap-2 md:justify-center">
            <div className="border-b-2 w-full md:border-none md:select-none">
              <Links linkName="Home" />
            </div>
            <div className="border-b-2 w-full md:border-none md:select-none">
              <Links linkName="Contact" />
            </div>
            <div className="border-b-2 w-full md:border-none md:select-none">
              <Links linkName="About" />
            </div>
            <div className="border-b-2 w-full md:border-none md:select-none">
              <Links linkName="Wallet" />
            </div>
          </div>

          <a
            href="/LoginPage"
            className="text-white rounded-full transition-all duration-[500ms] bg-gradient-to-tl from-pink-500 via-maincolor to-maincolor bg-size-200 bg-pos-0 hover:bg-pos-100 text-center px-4 py-2 ml-2 md:text-center md:flex md:justify-center md:items-center md:select-none"
          >
            Login
          </a>
        </div>
      </div>
    </>
  );
};
