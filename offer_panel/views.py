from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, CourseForm
from .models import Category, Course


@login_required(login_url="/members/login")
def main_panel(request):
    return render(request, "main_panel.html")


@login_required(login_url="/members/login")
def category_list(request):
    categories = Category.objects.all().order_by("order")
    return render(request, "category_list_panel.html", {"categories": categories})


@login_required(login_url="/members/login")
def course_list(request):
    courses = Course.objects.all().order_by("order")
    return render(request, "course_list.html", {"courses": courses})


@login_required(login_url="/members/login")
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    return render(request, "add_category.html", {"form": form})


@login_required(login_url="/members/login")
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "add_course.html", {"form": form})


@login_required(login_url="/members/login")
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Zaktualizowano kategorię.", extra_tags="message_success"
            )
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "edit_category.html", {"form": form, "category": category})


@login_required(login_url="/members/login")
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        category.delete()
        messages.success(request, "Usunięto kategorię.", extra_tags="message_success")
        return redirect("category_list")
    return redirect("edit_category", category_id=category_id)


@login_required(login_url="/members/login")
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Zaktualizowano szkolenie.", extra_tags="message_success"
            )
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "edit_course.html", {"form": form, "course": course})


@login_required(login_url="/members/login")
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Usunięto szkolenie.", extra_tags="message_success")
        return redirect("course_list")
    return redirect("edit_course", course_id=course_id)
