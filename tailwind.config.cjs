/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [  
  "./index.html",
  "./src/**/*.{vue,js,ts,jsx,tsx}",
],
  theme: {
    extend: {
      colors: {
        darkmode: "#18181B",
        maincolor: "#8257E5"
      },
    },
  },
  plugins: [],
}
