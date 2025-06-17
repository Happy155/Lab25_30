from django.contrib import messages
from django.shortcuts import redirect, render
from offer_panel.models import Course

from .forms import RegistrationForm


def registration_form(request):
    course_id = request.GET.get("course_id")
    initial = {}
    if course_id:
        try:
            course = Course.objects.get(id=course_id)
            initial["course"] = course
        except Course.DoesNotExist:
            pass
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        form.fields["course"].queryset = Course.objects.filter(is_published=True)
        if not request.POST.get("gdpr_consent"):
            messages.warning(
                request, "Musisz wyrazić zgodę na przetwarzanie danych osobowych."
            )
        if form.is_valid() and request.POST.get("gdpr_consent"):
            form.save()
            messages.success(
                request,
                "Zarejestrowano na szkolenie pomyślnie.",
                extra_tags="message_success",
            )
            return redirect("/")
    else:
        form = RegistrationForm(initial=initial)
        form.fields["course"].queryset = Course.objects.filter(is_published=True)
    return render(request, "registration_form.html", {"form": form})
