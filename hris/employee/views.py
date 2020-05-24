from django.shortcuts import render, redirect
from django.views import View

from main.models import HR
from .models import Employee
from datetime import datetime

# Create your views here.
class Dashboard(View):
    def get(self, request, *args, **kwargs):
        if "user_info" in request.session:
            username = request.session["user_info"]["username"]
            request.session["user_info"]["current_page"] = "home"
            try:
                if len(Employee.objects.all()) > 0:
                    employees = Employee.objects.all()
                    return render(request,template_name="employee/employee.html",context={"employees":employees})
                else:
                    return render(request,template_name="employee/employee.html",context={})
            except IndexError:
                return render(request,template_name="employee/employee.html",context={})
        else:
            return redirect("/")

    def post(self, request, *args, **kwargs):
        pass

class CreateEmployee(View):

    def get(self, request, *args, **kwargs):
        if "user_info" in request.session:
            return render(request,template_name="employee/create_employee.html",context={})
        else:
            return redirect("/")
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get("first_name")
        date_of_birth = request.POST.get("date_of_birth")
        position = request.POST.get("position")
        salary = request.POST.get("salary")
        sss = request.POST.get("sss")
        middle_name = request.POST.get("middle_name")
        address = request.POST.get("address")
        department = request.POST.get("department")
        date_hired = request.POST.get("date_hired")
        pag_ibig = request.POST.get("pag_ibig")
        philhealth = request.POST.get("philhealth")
        last_name = request.POST.get("last_name")
        city = request.POST.get("city")
        supervisor = request.POST.get("supervisor")
        tin = request.POST.get("tin")
        status = request.POST.get("status")
        age = datetime.now().year - datetime.strptime(date_of_birth, '%Y-%m-%d').year
        status = True if request.POST.get("salary") =="Active" else False

        record, created = Employee.objects.get_or_create(
            first_name = first_name,
            middle_name = middle_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            age = age,
            address = address,
            city = city,
            position = position,
            department = department,
            supervisor =  supervisor,
            salary = salary,
            date_hired = date_hired,
            tin = tin,
            philhealth = philhealth,
            sss = sss,
            pag_ibig = pag_ibig,
            status = status
        )
        if created == False:
            # Display message to indicate existing account
            return redirect("/")
        return redirect("/")
        
# class CreateEmployee(View):

#     def get(self, request, *args, **kwargs):
#         pass
#     def post(self, request, *args, **kwargs):
#         pass