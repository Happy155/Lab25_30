document.addEventListener("DOMContentLoaded", () => {
  const mobileMenuButton = document.getElementById("mobile-menu-button");
  const mobileMenu = document.getElementById("mobile-menu");
  const iconMenu = document.getElementById("icon-menu");
  const iconClose = document.getElementById("icon-close");

  mobileMenuButton?.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = !mobileMenu.classList.contains("hidden");
    mobileMenu.classList.toggle("hidden");
    iconMenu.classList.toggle("hidden", !isOpen);
    iconClose.classList.toggle("hidden", isOpen);
    mobileMenuButton.setAttribute("aria-expanded", String(!isOpen));
  });

  document.addEventListener("click", (e) => {
    if (!mobileMenu.classList.contains("hidden")) {
      if (
        !mobileMenu.contains(e.target) &&
        !mobileMenuButton.contains(e.target)
      ) {
        mobileMenu.classList.add("hidden");
        iconMenu.classList.remove("hidden");
        iconClose.classList.add("hidden");
        mobileMenuButton.setAttribute("aria-expanded", "false");
      }
    }
  });

  const button = document.getElementById("user-menu-button");
  const menu = document.getElementById("user-menu");
  const arrow = document.getElementById("user-menu-arrow");

  if (button) {
    button.addEventListener("click", (e) => {
      e.stopPropagation();
      menu.classList.toggle("hidden");
      const expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
      arrow.classList.toggle("rotate-180", !expanded);
    });

    document.addEventListener("click", () => {
      if (!menu.classList.contains("hidden")) {
        menu.classList.add("hidden");
        button.setAttribute("aria-expanded", "false");
        arrow.classList.remove("rotate-180");
      }
    });
  }
});
