// Tailwind build for the Pleasant product pages (public/pleasant). The pages
// are static files in public/, so their CSS is compiled ahead of time:
//   npm run build:pleasant-css
module.exports = {
  content: ["./public/pleasant/**/*.html", "./public/pleasant/assets/*.js"],
  theme: {
    extend: {
      colors: {
        ink: "#0b0f14",
        brand: {
          50: "#eef9f7", 100: "#d5f0eb", 200: "#ade1d8", 300: "#7ccbc0", 400: "#4aafa3",
          500: "#2f938a", 600: "#237670", 700: "#1f5f5b", 800: "#1d4d4a", 900: "#1b403e", 950: "#0d2c2b",
        },
      },
      fontFamily: {
        sans: ["DM Sans", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["Space Grotesk", "DM Sans", "ui-sans-serif", "system-ui", "sans-serif"],
        serif: ["Instrument Serif", "Georgia", "serif"],
      },
      boxShadow: {
        frame: "0 1px 0 rgba(255,255,255,.6) inset, 0 30px 80px -20px rgba(13,44,43,.35), 0 12px 24px -12px rgba(13,44,43,.25)",
        pill: "0 8px 30px -10px rgba(11,15,20,.25), 0 1px 0 rgba(255,255,255,.8) inset",
      },
    },
  },
};
