/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [  
  "./index.html",
  "./src/**/*.{vue,js,ts,jsx,tsx}",
],
  darkMode: "class",
  
  theme: {
    extend: {
      transitionDuration: {
        '0': '0ms',
        '2000': '2000ms',
      }, 
      colors: {
        escure: "#1d1929",
        maincolor: "#8257E5",
        escurinho: "#323238",
        contentDark : "#121214",
        textColor: "#c4c4cc",
      },
      backgroundSize: {
        'size-200': '200% 200%',
      },
      backgroundPosition: {
        'pos-0': '0% 0%',
        'pos-100': '100% 100%',
      },
    },
  },
  plugins: [require('tailwind-scrollbar'),],
  
}

