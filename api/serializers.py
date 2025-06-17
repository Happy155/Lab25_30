from issues.models import Issue
from offer_panel.models import Category, Course
from register.models import Registration
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "order", "is_published"]


class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "number",
            "duration_hours",
            "price",
            "order",
            "is_published",
            "category",
            "category_name",
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    course_title = serializers.ReadOnlyField(source="course.title")

    class Meta:
        model = Registration
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "course",
            "course_title",
            "status",
            "registered_at",
            "gdpr_consent",
        ]
        read_only_fields = ["registered_at", "status"]


class IssueSerializer(serializers.ModelSerializer):
    module_display = serializers.CharField(source="get_module_display", read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "submitted_at",
            "author",
            "subject",
            "description",
            "module",
            "module_display",
            "attachment",
        ]
        read_only_fields = ["submitted_at"]
