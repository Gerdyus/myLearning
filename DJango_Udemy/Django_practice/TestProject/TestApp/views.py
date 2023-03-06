from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def mainView(request):
    reverseCode = reverse("ReverseTag", args = []) + "RedirectedString"
    redirectString = "<li><a href = \"{reverseCode}\">Redirect Me</a></li>"
    return HttpResponse(redirectString)

def adminFunc(request):
    return HttpResponse("")


def catchAllString(request, keyword):
    reverseCode = reverse("ReverseTag", args = [keyword]) # args was forgotten and keyword was needed in it
    return HttpResponse(keyword + " "+ reverseCode)
