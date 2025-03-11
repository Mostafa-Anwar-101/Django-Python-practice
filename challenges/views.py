from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "Reflect and Plan"
}


def index(request):
    list_items = ""
    months = list(challenges.keys())
    for month in months:
        month_url = reverse("monthly-challenge", args=[month])
        captialized_month = month.capitalize()
        list_items += f"<li><a href=\"{month_url}\">{captialized_month}</a></li>"

    return HttpResponse(f"<ul>{list_items}</ul>")


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
        return HttpResponseNotFound("This month is not supported")
