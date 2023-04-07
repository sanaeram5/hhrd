from django.shortcuts import render
from django.views import View

# Create your views here.
class Index(View):
    def get(self,request, *args, **kwargs):
        return render(request,'website/index.html')

class Education(View):
    def get(self,request, *args, **kwargs):
        return render(request,'website/education.html')

class Safety(View):
    def get(self,request, *args, **kwargs):
        return render(request,'website/safety.html')

class Elderly(View):
    def get(self,request, *args, **kwargs):
        return render(request,'website/elderly.html')

class Mental(View):
    def get(self,request, *args, **kwargs):
        return render(request,'website/mental.html')

class Health(View):
    def get(self,request, *args, **kwargs):
        return render(request,'website/health.html')