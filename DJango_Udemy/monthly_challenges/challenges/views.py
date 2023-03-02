from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def viewFuncJan(request):
    return HttpResponse("It works! - Jan")


def viewFuncFeb(request):
    return HttpResponse("It works! - Feb")


def viewFuncMar(request):
    return HttpResponse("It works! - Mar")


def viewFuncApr(request):
    return HttpResponse("It works! - Apr")


def viewFuncMay(request):
    return HttpResponse("It works! - May")


def viewFuncJun(request):
    return HttpResponse("It works! - Jun")


def viewFuncJul(request):
    return HttpResponse("It works! - Jul")


def viewFuncAug(request):
    return HttpResponse("It works! - Aug")