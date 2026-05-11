/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./blog/*.html"
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ['"Instrument Serif"', 'serif'],
        ui:      ['"Inter Tight"', 'Inter', 'system-ui', 'sans-serif'],
        mono:    ['"JetBrains Mono"', 'ui-monospace', 'monospace']
      },
      colors: {
        ink:      { 1:'#15110D', 2:'#3A2710', 3:'#4F4840', 4:'#8C8378', 5:'#B6AEA1', 6:'#E5DDD0', 7:'#F6F2EA' },
        cream:    '#FAF8F4',
        ochre:    { DEFAULT:'#C58B43', deep:'#8E5F22', soft:'#F5E8D2', light:'#E0A95C', line:'#E8CFA3' },
        positive: '#2F8F4E',
        negative: '#C44232',
        warning:  '#B08518'
      }
    }
  },
  corePlugins: { preflight: true },
  plugins: []
};
