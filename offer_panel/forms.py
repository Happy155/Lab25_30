from django import forms

from .models import Category, Course


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "order", "is_published"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "order": forms.NumberInput(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "category",
            "title",
            "description",
            "number",
            "duration_hours",
            "price",
            "order",
            "is_published",
        ]
        widgets = {
            "category": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "number": forms.TextInput(attrs={"class": "form-control"}),
            "duration_hours": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "order": forms.NumberInput(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
