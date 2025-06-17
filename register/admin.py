from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "course",
        "email",
        "phone",
        "status",
        "registered_at",
    )
    list_filter = ("status", "registered_at", "course")
    search_fields = ("first_name", "last_name", "email", "phone")
    date_hierarchy = "registered_at"
    readonly_fields = ("registered_at",)
