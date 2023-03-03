from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def viewFuncJan(request):
    return HttpResponse("It works! - Jan")


def viewFuncFeb(request):
    return HttpResponse("It works! - Feb")


def viewFuncMar(request):
    return HttpResponse("It works! - Mar")


def genericResponse(request,keyword):
    returnText = "" + keyword +": "
    if(keyword == "january"): # Will never get here because january exists specifically in a previous path
        returnText = returnText + " sent from genericResponse."
    if(keyword == "october"):
        returnText = returnText + " sent from genericResponse."
    else:
        return HttpResponseNotFound("Unknown keyword.")
    return HttpResponse(returnText)