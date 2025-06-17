from django.core.validators import RegexValidator
from django.db import models
from offer_panel.models import Course


class Registration(models.Model):
    STATUS_CHOICES = [
        ("pending", "Oczekujące"),
        ("confirmed", "Potwierdzone"),
        ("cancelled", "Anulowane"),
    ]

    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Numer telefonu musi być w formacie: '+999999999'. Od 9 do 15 cyfr.",
    )

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="registrations"
    )
    gdpr_consent = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    registered_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, validators=[phone_regex])
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} – {self.course.title}"
