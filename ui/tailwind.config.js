/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ["./dist/**/*.{vue,js,ts,jsx,tsx}", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  mode: "jit",
  content: ["./src/components/**/*.{html,js,ts,vue}", "./src/views/**/*.{html,js,ts,vue}"],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        ducks: {
          primary: "#f47a38",
          secondary: "#7C909A",
          accent: "#b9975b",
          neutral: "#23282E",
          "base-100": "#303030",
          info: "#0091D5",
          success: "#6BB187",
          warning: "#DBAE59",
          error: "#AC3E31",
        },
      },
    ],
  },
};
