from django.shortcuts import render, redirect
from django.views import View

from .models import HR
from employee.models import Employee

from datetime import datetime 
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
class Index(View):

    def get(self, request, *args, **kwargs):
        if "user_info" in request.session:
            return redirect("employee/")
        else:
            return render(request,template_name="main/login.html",context={})

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username==HR.objects.filter(username=username)[0].username:
            print("user exists")
            verified_user = HR.objects.filter(username=username)[0]
            if check_password(password,verified_user.password):
                print("password is correct")
                HR.objects.filter(username=username).update(date_lastlogin=datetime.now(),is_loggedin=True)
                request.session["user_info"]={"username":username}
                return redirect('employee/')
            # If existing user's input password was wrong
            else:
                print("wrong password")
                return redirect('/')
        # Outer condition: If user doesn't exist
        else:
            print("user doesn't exist")
            return redirect('/')

class SignUp(View):

    def get(self, request, *args, **kwargs):
        return render(request,template_name="main/registration.html",context={})

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == HR.objects.filter(username=username)[0].username:
            print("Account already exists")
            return redirect('/')
        else:
            hashed_pass = make_password(password)
            HR.objects.create(username=username,password=hashed_pass)
            return redirect('/')

def logout_user(request):
    user = HR.objects.filter(username=request.session["user_info"]["username"]).update(is_loggedin=False)
    del request.session["user_info"]
    return redirect("/")
