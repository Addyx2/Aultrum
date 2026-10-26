// Tailwind build for the Canvas product pages (public/canvas). The pages
// are static files in public/, so their CSS is compiled ahead of time:
//   npm run build:canvas-css
module.exports = {
  content: ["./public/canvas/**/*.html", "./public/canvas/assets/*.js"],
  theme: {
    extend: {
      colors: {
        ink: "#0b0f14",
        brand: {
          50: "#f3f2ff", 100: "#e7e5ff", 200: "#d1cdff", 300: "#b0a8ff", 400: "#8b7dfc",
          500: "#6c5cf5", 600: "#5a45e8", 700: "#4b37c9", 800: "#3e2fa3", 900: "#352b81", 950: "#201a4b",
        },
      },
      fontFamily: {
        sans: ["DM Sans", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["Space Grotesk", "DM Sans", "ui-sans-serif", "system-ui", "sans-serif"],
        serif: ["Instrument Serif", "Georgia", "serif"],
      },
      boxShadow: {
        frame: "0 1px 0 rgba(255,255,255,.6) inset, 0 30px 80px -20px rgba(32,26,75,.35), 0 12px 24px -12px rgba(32,26,75,.25)",
        pill: "0 8px 30px -10px rgba(11,15,20,.25), 0 1px 0 rgba(255,255,255,.8) inset",
      },
    },
  },
};
