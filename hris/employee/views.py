from django.shortcuts import render, redirect
from django.views import View

from main.models import HR
from .models import Employee

# Create your views here.
class Dashboard(View):
    def get(self, request, *args, **kwargs):
        if "user_info" in request.session:
            return render(request,template_name="employee/dashboard.html",context={})
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        pass