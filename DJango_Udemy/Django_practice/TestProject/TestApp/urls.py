from django.urls import path
from . import views

urlpatterns = [
    path("",views.mainView, name = "ReverseTag"),
    path("admin",views.adminFunc), #Don't put / or \ here
    path("<str:keyword>",views.catchAllString, name = "ReverseTag")
]