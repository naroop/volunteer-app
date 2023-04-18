/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ["./dist/**/*.{vue,js,ts,jsx,tsx}", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  mode: "jit",
  content: [
    "./src/components/**/*.{html,js,ts,vue}",
    "./src/views/**/*.{html,js,ts,vue}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
