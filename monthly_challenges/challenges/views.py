from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Read a book",
    "february": "Workout six times a week",
    "march": "Have a cold shower everyday",
    "april": "Have a cold shower everyday",
    "may": "Have a cold shower everyday",
    "june": "Have a cold shower everyday",
    "july": "Have a cold shower everyday",
    "august": "Have a cold shower everyday",
    "september": "Have a cold shower everyday",
    "october": "Have a cold shower everyday",
    "november": "Have a cold shower everyday",
    "december": None,
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


# Create your views here.
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text,
        })
    except:
        raise Http404()


# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month <= 0:
        raise Http404()
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
