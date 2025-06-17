document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar-container");
  const descriptionPanel = document.getElementById("description-panel");

  if (sidebar && descriptionPanel) {
    const images = sidebar.querySelectorAll("img");
    let imagesLoaded = 0;

    if (images.length > 0) {
      images.forEach((img) => {
        if (img.complete) {
          imagesLoaded++;
        } else {
          img.addEventListener("load", () => {
            imagesLoaded++;
            if (imagesLoaded === images.length) {
              descriptionPanel.style.height = `${sidebar.offsetHeight}px`;
            }
          });
        }
      });

      if (imagesLoaded === images.length) {
        descriptionPanel.style.height = `${sidebar.offsetHeight}px`;
      }
    } else {
      descriptionPanel.style.height = `${sidebar.offsetHeight}px`;
    }
  }
});
