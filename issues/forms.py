from django import forms

from .models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ["author", "subject", "description", "module", "attachment"]
        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "module": forms.Select(attrs={"class": "form-control"}),
            "attachment": forms.FileInput(attrs={"class": "form-control"}),
        }
        labels = {
            "author": "Autor",
            "subject": "Temat",
            "description": "Opis",
            "module": "Moduł",
            "attachment": "Załącznik",
        }
