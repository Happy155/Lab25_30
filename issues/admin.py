from django.contrib import admin

from .models import Issue


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "author", "module", "submitted_at")
    list_filter = ("module", "submitted_at")
    search_fields = ("subject", "description", "author")
    date_hierarchy = "submitted_at"
    readonly_fields = ("submitted_at",)
