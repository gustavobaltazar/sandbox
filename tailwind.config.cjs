/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [  
  "./index.html",
  "./src/**/*.{vue,js,ts,jsx,tsx}",
],
  darkMode: 'class',
  theme: {
    extend: {
      transitionDuration: {
        '0': '0ms',
        '2000': '2000ms',
      }, 
      colors: {
        darkmode: "#18181B",
        maincolor: "#8257E5"
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
  plugins: [],
}
