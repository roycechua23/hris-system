from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):

    def get(self, request, *args, **kwargs):
        return render(request,template_name="main/login.html",context={})

    def post(self, request, *args, **kwargs):
        pass