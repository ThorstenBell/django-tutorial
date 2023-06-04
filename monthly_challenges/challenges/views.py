from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def monthly_challenges(request, month):
    match month:
        case "january":
            challenge_text = "Read a book"
        case "february":
            challenge_text = "Workout 6 times a week"
        case other:
            return HttpResponseNotFound("No challenge found!")

    return HttpResponse(challenge_text)
