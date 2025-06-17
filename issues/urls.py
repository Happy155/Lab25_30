from django.urls import path

from . import views

urlpatterns = [
    path("", views.issue_list, name="issue_list"),
    path("report", views.report_issue_form, name="report_issue_form"),
    path("<int:issue_id>/", views.issue_detail, name="issue_detail"),
]
