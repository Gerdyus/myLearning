from django.urls import path
from . import views


urlpatterns = [
    path("<int:keyword>",views.genericReponseInt),
    path("<str:keyword>",views.genericResponse)
]