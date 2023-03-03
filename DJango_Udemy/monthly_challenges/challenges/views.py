from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
# Create your views here.

month_dictionary = {
    "january":"Jan",
    "february":"Feb",
    "march":"Mar",
    "april":"Apr",
    "may":"May",
    "june":"Jun",
    "july":"Jul",
    "august":"Aug",
    "september":"Sep",
    "october":"Oct",
    "november":"Nov",
    "december":"Dec",
}

def genericResponse(request, keyword):
    try:
        returnText = month_dictionary[keyword]
    except:
        return HttpResponseNotFound("Unknown parameter keyword.")
    return HttpResponse(returnText)


def genericReponseInt(request, keyword):
    if(keyword>12):
        return HttpResponseNotFound("Invalid month")
    try:
        dict_keys = list(month_dictionary.keys())
        returnText = dict_keys[keyword-1]
    except:
        return HttpResponseNotFound("Unknown parameter keyword.")
    return HttpResponseRedirect("/challenges/"+returnText)
