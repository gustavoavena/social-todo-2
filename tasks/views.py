from django.shortcuts import render
from django.http import HttpResponse

from . import forms
# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You're at the tasks index.")
	# return render(request, 'index.html', {"title": "hasuaus", "message": "testing variables"})
	
def say_whatsup(request):
	return HttpResponse("Hello, WHAT IS UP?")


def create(request):
	if request.method != 'POST':
		return HttpResponse('Request Error')
	else: 
		form = users.forms.CreateTaskForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			#create new task.
		else:
			return HttpResponse('Invalid Form.')
	
		return HttpResponse('Processing.')


def complete(request):
	return HttpResponse("COMPLETE TASK")


def remove(request):
	return HttpResponse("REMOVE TASK")





#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
