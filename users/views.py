from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def register(request):
    return HttpResponse("REGISTER USER")


def login(request):
    return HttpResponse("USER LOGIN")


def logout(request):
    return HttpResponse("USER LOGOUT")





#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
