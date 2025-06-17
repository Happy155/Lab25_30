function dismissToast(toast) {
  if (toast) {
    toast.style.opacity = "0";
    setTimeout(() => {
      toast.style.display = "none";
    }, 300);
  }
}

document
  .querySelectorAll("#toast-success, #toast-danger, #toast-warning")
  .forEach((toast) => {
    setTimeout(() => {
      toast.style.opacity = "1";
    }, 100);
    setTimeout(() => {
      dismissToast(toast);
    }, 5000);
  });

document.querySelectorAll("[data-dismiss-target]").forEach((button) => {
  button.addEventListener("click", () => {
    const targetId = button.getAttribute("data-dismiss-target");
    const target = document.querySelector(targetId);
    dismissToast(target);
  });
});
