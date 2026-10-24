// Mobile menu, scroll reveals and the pricing billing toggle for the product pages.
document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.getElementById("menu-button");
  const menu = document.getElementById("mobile-menu");
  if (menuButton && menu) {
    menuButton.addEventListener("click", () => {
      const open = menu.classList.toggle("hidden") === false;
      menuButton.setAttribute("aria-expanded", String(open));
    });
  }

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add("is-visible"); observer.unobserve(e.target); }
      }),
      { threshold: 0, rootMargin: "0px 0px -40px 0px" },
    );
    document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
  } else {
    document.querySelectorAll(".reveal").forEach((el) => el.classList.add("is-visible"));
  }

  // Pricing: switch every price between monthly and annual (17% off).
  const toggles = document.querySelectorAll("[data-billing]");
  const setBilling = (mode) => {
    toggles.forEach((b) => {
      const active = b.dataset.billing === mode;
      b.setAttribute("aria-pressed", String(active));
      b.classList.toggle("bg-ink", active);
      b.classList.toggle("text-white", active);
    });
    document.querySelectorAll("[data-monthly]").forEach((el) => {
      const monthly = Number(el.dataset.monthly);
      const value = mode === "annual" ? Math.round(monthly * 0.83) : monthly;
      el.textContent = "£" + value.toLocaleString("en-GB");
    });
    document.querySelectorAll("[data-billing-note]").forEach((el) => {
      el.textContent = mode === "annual" ? "per month, billed annually" : "per month";
    });
  };
  toggles.forEach((b) => b.addEventListener("click", () => setBilling(b.dataset.billing)));
});
