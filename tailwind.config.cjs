/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [  
  "./index.html",
  "./src/**/*.{vue,js,ts,jsx,tsx}",
],
  darkMode: "class",
  
  theme: {
    textFillColor: theme => theme('borderColor'),
    textStrokeColor: theme => theme('borderColor'),
    textStrokeWidth: theme => theme('borderWidth'),
    paintOrder: {
      'fsm': { paintOrder: 'fill stroke markers' },
      'fms': { paintOrder: 'fill markers stroke' },
      'sfm': { paintOrder: 'stroke fill markers' },
      'smf': { paintOrder: 'stroke markers fill' },
      'mfs': { paintOrder: 'markers fill stroke' },
      'msf': { paintOrder: 'markers stroke fill' },
    },
    extend: {
      transitionDuration: {
        '0': '0ms',
        '2000': '2000ms',
      }, 
      colors: {
        escure: "#1d1929",
        maincolor: "#8257E5",
        escurinho: "#323238",
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
  plugins: [require('tailwindcss-text-fill-stroke'),],
  
}

