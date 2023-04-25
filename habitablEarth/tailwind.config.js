/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
    "./src/**/**/*.{html,ts}",
  ],
  theme: {
    extend: {
      colors: {
        'prime': '#ff8080',
        'bg': '#d6dcdc',
      },
    }
  },
  plugins: [],
}

