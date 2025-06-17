from django.db import models


class Issue(models.Model):
    MODULE_CHOICES = [
        ("offer_panel", "Oferta panel"),
        ("offer_public", "Oferta publiczna"),
        ("register", "Rejestracja"),
        ("issues", "Problemy"),
    ]

    submitted_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    module = models.CharField(max_length=50, choices=MODULE_CHOICES)
    attachment = models.ImageField(
        upload_to="issue_attachments/", blank=True, null=True
    )

    def __str__(self):
        return f"Issue #{self.id} - {self.subject} by {self.author}"
