from django.shortcuts import get_object_or_404, render
from offer_panel.models import Category


def category_list(request):
    categories = Category.objects.filter(is_published=True).order_by("order")
    for cat in categories:
        cat.published_courses_count = cat.courses.filter(is_published=True).count()
    return render(request, "category_list.html", {"categories": categories})


def course_list_by_category(request, category):
    try:
        category_obj = Category.objects.get(name=category, is_published=True)
    except Category.DoesNotExist:
        return render(
            request,
            "course_list_by_category.html",
            {"category": None, "courses": []},
        )
    courses = category_obj.courses.filter(is_published=True).order_by("order")
    return render(
        request,
        "course_list_by_category.html",
        {"category": category_obj, "courses": courses},
    )


def course_detail(request, category, course_id):
    category_obj = get_object_or_404(Category, name=category, is_published=True)
    course = get_object_or_404(category_obj.courses, id=course_id, is_published=True)
    return render(
        request,
        "course_detail.html",
        {"category": category_obj, "course": course},
    )
