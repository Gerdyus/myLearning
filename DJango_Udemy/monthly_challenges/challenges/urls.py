from django.urls import path
from . import views


urlpatterns = [
    path("january",views.viewFuncJan),
    path("february",views.viewFuncFeb),
    path("march",views.viewFuncMar),
    path("april",views.viewFuncApr),
    path("may",views.viewFuncMay),
    path("june",views.viewFuncJun),
]