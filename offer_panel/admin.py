from django.contrib import admin

from .models import Category, Course


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_published", "order")
    list_filter = ("is_published",)
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "price",
        "duration_hours",
        "is_published",
        "order",
    )
    list_filter = ("is_published", "category")
    search_fields = ("title", "description", "number")
