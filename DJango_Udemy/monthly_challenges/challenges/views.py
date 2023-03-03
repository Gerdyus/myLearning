from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

month_dictionary = {
    "january": "Jan",
    "february": "Feb",
    "march": "Mar",
    "april": "Apr",
    "may": "May",
    "june": "Jun",
    "july": "Jul",
    "august": "Aug",
    "september": "Sep",
    "october": "Oct",
    "november": "Nov",
    "december": "Dec",
}

def index(request):
    http_response = ""
    dict_keys = list(month_dictionary.keys())
    for month in dict_keys:
        root_url = reverse("month-challenge",args = [month])
        http_response+= f"<li><a href = \" {root_url} \"> {month.capitalize()} </a></li>"
          
    return HttpResponse(http_response)

def genericResponse(request, keyword):
    try:
        returnText = month_dictionary[keyword]
        return_html = f"<h1>{returnText}</h1>"
    except:
        return HttpResponseNotFound("Unknown parameter keyword.")
    return HttpResponse(return_html)


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
