from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the starter page!")
   	return render(request, 'index.html', {"title": "cpsc 113", "message": "Starting page!"})
    





#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp