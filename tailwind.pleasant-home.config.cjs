// Tailwind build for aultrum.co.uk/pleasant/: the homepage's design in Pleasant purple.
//   npm run build:pleasant-home-css
const config = require("./tailwind.home.config.cjs");
const purple = {
  "ink-primary": "#6d28d9",
  "primary": "#4c1d95",
  "primary-container": "#5b21b6",
  "ink-secondary": "#4c3d7a",
  "surface-tint": "#7c3aed",
};
module.exports = {
  ...config,
  content: ["./public/pleasant/index.html"],
  theme: { ...config.theme, extend: { ...config.theme.extend, colors: { ...config.theme.extend.colors, ...purple } } },
};
