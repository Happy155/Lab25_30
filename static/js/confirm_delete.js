function confirmDelete(
  message = "Czy na pewno chcesz usunąć ten element? Ta operacja jest nieodwracalna."
) {
  if (confirm(message)) {
    const form = document.getElementById("delete-form");
    if (form) form.submit();
  }
}
