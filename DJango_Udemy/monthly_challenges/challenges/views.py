from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

month_dictionary = {
    "january": "Jan Challenge",
    "february": "Feb  Challenge",
    "march": "Mar  Challenge",
    "april": "Apr  Challenge",
    "may": "May  Challenge",
    "june": "Jun  Challenge",
    "july": "Jul  Challenge",
    "august": "Aug  Challenge",
    "september": "Sep  Challenge",
    "october": "Oct  Challenge",
    "november": "Nov  Challenge",
    "december": None,
}


def index(request):
    http_response = ""
    dict_keys = list(month_dictionary.keys())
    dict_vals = list(month_dictionary.values())
    for month in dict_keys:
        root_url = reverse("month-challenge", args=[month])
        http_response += f"<li><a href = \" {root_url} \"> {month.capitalize()} </a></li>"

    return render(request, "challenges/index.html",{
        "listMonths":dict_keys,
    })


def genericResponse(request, keyword):
    try:
        returnText = month_dictionary[keyword]
        return render(request, "challenges/challenges.html", {
            "text":keyword,
            "challenge": month_dictionary[keyword]
        })
        # reverseCode = reverse("month-challenge", args = [keyword])
        return_html = render_to_string("challenges/challenges.html")
        return HttpResponse(return_html)
    except:
        raise Http404()#Looks for a 404.html file in the root project templates
        tempdata = render_to_string("404.html")
        return HttpResponseNotFound(tempdata)


def genericReponseInt(request, keyword):
    if (keyword > 12):
        return HttpResponseNotFound("Invalid month")
    try:
        dict_keys = list(month_dictionary.keys())
        returnText = dict_keys[keyword-1]
        # Pretty great - will make /challenge/month (from returnText)
        redirect_path = reverse("month-challenge", args=[returnText])
    except:
        return HttpResponseNotFound("Unknown parameter keyword.")
    return HttpResponseRedirect(redirect_path)
