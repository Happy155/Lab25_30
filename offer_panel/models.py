from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Course(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="courses"
    )
    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    duration_hours = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
