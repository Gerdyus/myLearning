from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name = "month-challenge"),
    path("<int:keyword>", views.genericReponseInt),
    path("<str:keyword>", views.genericResponse, name = "month-challenge")
]
