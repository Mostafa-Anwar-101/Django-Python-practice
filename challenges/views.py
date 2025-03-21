from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

challenges = {
    "january": "Automate a Manual Task",
    "february": "Learn a New DevOps Tool",
    "march": "Improve Observability",
    "april": "Focus on Security",
    "may": "Optimize CI/CD Pipelines",
    "june": "Contribute to Open Source",
    "july": "Focus on Soft Skills",
    "august": "Learn Cloud-Native Technologies",
    "september": "Implement Infrastructure as Code (IaC)",
    "october": "Focus on Work-Life Balance",
    "november": "Disaster Recovery and Backup",
    "december": None
}


def index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    try:
        months = list(challenges.keys())
        redirect_month = months[month-1]
       # return HttpResponse(challenges[redirect_month])
        redirect_url = reverse("monthly-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenges(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
