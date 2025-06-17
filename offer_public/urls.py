from django.urls import path

from . import views

urlpatterns = [
    path("", views.category_list, name="public_category_list"),
    path(
        "<str:category>/", views.course_list_by_category, name="course_list_by_category"
    ),
    path(
        "<str:category>/course/<int:course_id>/",
        views.course_detail,
        name="course_detail",
    ),
]
