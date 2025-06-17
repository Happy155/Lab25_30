from django.shortcuts import get_object_or_404, redirect, render

from .forms import IssueForm
from .models import Issue


def report_issue_form(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("issue_list")
    else:
        form = IssueForm()
    return render(request, "report_issue.html", {"form": form})


def issue_list(request):
    issues = Issue.objects.all().order_by("-submitted_at")
    return render(request, "issue_list.html", {"issues": issues})


def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    return render(request, "issue_detail.html", {"issue": issue})
