from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import forms
from . import models
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
		# print(request.POST)
		form = forms.CreateTaskForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			print(formData)
			#I'm still missing collaborators.
			newTask = models.Task(owner=request.user, title=formData['title'], description=formData['description'])
			newTask.save()
			print('Task saved: ', newTask)
			#create new task.
		else:
			print(form.errors.as_data())
			return HttpResponse('Invalid Form.')
	
		return redirect('/user/dashboard')


def complete(request):
	return HttpResponse("COMPLETE TASK")


def remove(request):
	return HttpResponse("REMOVE TASK")





#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
