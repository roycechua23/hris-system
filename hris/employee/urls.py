from django.urls import path
from .views import *

app_name = "employee"

urlpatterns = [
    path("",Dashboard.as_view(),name="dashboard"),
]