from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.category_list_api, name="category_list_api"),
    path("courses/", views.course_list_api, name="course_list_api"),
    path("registers/", views.registration_list_api, name="registration_list_api"),
    path(
        "register/<int:pk>/",
        views.registration_detail_api,
        name="registration_detail_api",
    ),
    path("register/", views.registration_create_api, name="registration_create_api"),
    path("problems/", views.issue_list_api, name="issue_list_api"),
    path("problem-report/", views.issue_create_api, name="issue_create_api"),
    path("documentation/", views.api_documentation, name="api_documentation"),
]
