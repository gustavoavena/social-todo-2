from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
   	# return render(request, 'index.html', {"title": "hasuaus", "message": "testing variables"})
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")


def create(request):
    return HttpResponse("CREATE TASK")


def complete(request):
    return HttpResponse("COMPLETE TASK")


def remove(request):
    return HttpResponse("REMOVE TASK")





#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
