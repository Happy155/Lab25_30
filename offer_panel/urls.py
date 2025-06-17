from django.urls import path

from . import views

urlpatterns = [
    path("", views.main_panel, name="main_panel"),
    path("categ-lst", views.category_list, name="category_list"),
    path("course-lst", views.course_list, name="course_list"),
    path("categ-add", views.add_category, name="add_category"),
    path("course-add", views.add_course, name="add_course"),
    path("categ-edit/<int:category_id>/", views.edit_category, name="edit_category"),
    path(
        "categ-delete/<int:category_id>/", views.delete_category, name="delete_category"
    ),
    path("course-edit/<int:course_id>/", views.edit_course, name="edit_course"),
    path("course-delete/<int:course_id>/", views.delete_course, name="delete_course"),
]
