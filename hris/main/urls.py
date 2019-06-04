from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', logout_user, name="logout")
]