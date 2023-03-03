from django.urls import path
from . import views


urlpatterns = [
    path("january",views.viewFuncJan),
    path("february",views.viewFuncFeb),
    path("march",views.viewFuncMar),
    path("<keyword>",views.genericResponse)
]