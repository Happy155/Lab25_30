from django.shortcuts import render
from issues.models import Issue
from offer_panel.models import Category, Course
from register.models import Registration
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .serializers import (
    CategorySerializer,
    CourseSerializer,
    IssueSerializer,
    RegistrationSerializer,
)


@api_view(["GET"])
def category_list_api(request):
    """
    Endpoint API zwracający wszystkie kategorie
    """
    categories = Category.objects.all().order_by("order")
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def course_list_api(request):
    """
    Endpoint API zwracający wszystkie szkolenia
    """
    courses = Course.objects.all().order_by("order")
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def registration_list_api(request):
    """
    Endpoint API zwracający wszystkie rejestracje na szkolenia
    """
    registrations = Registration.objects.all().order_by("-registered_at")
    serializer = RegistrationSerializer(registrations, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def registration_detail_api(request, pk):
    """
    Endpoint API zwracający konkretną rejestrację na szkolenie na podstawie ID
    """
    try:
        registration = Registration.objects.get(pk=pk)
        serializer = RegistrationSerializer(registration)
        return Response(serializer.data)
    except Registration.DoesNotExist:
        return Response(
            {"error": "Rejestracja nie została znaleziona"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["GET"])
def issue_list_api(request):
    """
    Endpoint API zwracający wszystkie zgłoszone problemy
    """
    issues = Issue.objects.all().order_by("-submitted_at")
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def registration_create_api(request):
    """
    Endpoint API tworzący nową rejestrację na szkolenie
    """
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        if not request.data.get("gdpr_consent", False):
            return Response(
                {"error": "Musisz wyrazić zgodę na RODO, aby się zarejestrować"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        registration = serializer.save(gdpr_consent=True)

        return Response(
            {
                "message": "Rejestracja zakończona pomyślnie",
                "registration": RegistrationSerializer(registration).data,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def issue_create_api(request):
    """
    Endpoint API tworzący nowe zgłoszenie problemu
    """
    serializer = IssueSerializer(data=request.data)

    if serializer.is_valid():
        issue = serializer.save()

        return Response(
            {
                "message": "Zgłoszenie zostało przesłane pomyślnie.",
                "issue": IssueSerializer(issue).data,
            },
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def api_documentation(request):
    api_endpoints = [
        {
            "name": "Lista kategorii",
            "url": "/api/categories/",
            "method": "GET",
            "description": "Zwraca wszystkie kategorie",
        },
        {
            "name": "Lista szkoleń",
            "url": "/api/courses/",
            "method": "GET",
            "description": "Zwraca wszystkie szkolenia",
        },
        {
            "name": "Lista rejestracji",
            "url": "/api/registers/",
            "method": "GET",
            "description": "Zwraca wszystkie rejestracje na szkolenia",
        },
        {
            "name": "Szczegóły rejestracji",
            "url": "/api/register/<id>/",
            "method": "GET",
            "description": "Zwraca szczegóły konkretnej rejestracji",
        },
        {
            "name": "Utwórz rejestrację",
            "url": "/api/register/",
            "method": "POST",
            "description": "Tworzy nową rejestrację na szkolenie",
        },
        {
            "name": "Lista zgłoszonych problemów",
            "url": "/api/problems/",
            "method": "GET",
            "description": "Zwraca wszystkie zgłoszone problemy",
        },
        {
            "name": "Zgłoś problem",
            "url": "/api/problem-report/",
            "method": "POST",
            "description": "Tworzy nowe zgłoszenie problemu",
        },
    ]

    return render(request, "api_documentation.html", {"api_endpoints": api_endpoints})
