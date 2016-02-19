from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from . import forms
from . import models
from django.contrib.auth.models import User
# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You're at the tasks index.")
	# return render(request, 'index.html', {"title": "hasuaus", "message": "testing variables"})
	
def say_whatsup(request):
	return HttpResponse("Hello, WHAT IS UP?")


@login_required
def create(request):
	if request.method != 'POST':
		return HttpResponse('Request Error')
	else: 
		# print(request.POST)
		form = forms.CreateTaskForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			# print(formData)
			#I'm still missing collaborators.
			newTask = models.Task(owner=request.user, title=formData['title'], description=formData['description'], isComplete=False)
			newTask.save()
			# collaborators = User.objects.filter(username=formData['collaborator1']).filter(username=formData['collaborator2']).filter(username=formData['collaborator3'])
			collaborators = [formData['collaborator1'], formData['collaborator2'], formData['collaborator3']]
			for c in collaborators:
				u = User.objects.filter(username=c)
				if u:
					newTask.collaborators.add(u[0])
			newTask.save()
			# print('Task saved: ', newTask.title, newTask.description, newTask.collaborators)

			#create new task.
		else:
			print(form.errors.as_data())
			return HttpResponse('Invalid Form.')
	
		return redirect('/user/dashboard')

@login_required
def complete(request):
	if 'id' in request.GET.keys():
		id = request.GET['id']
	else:
		return redirect('/user/dashboard/?errors=Id+Not+Found.')

	taskToToggle = models.Task.objects.filter(id=id)[0]
	taskToToggle.isComplete = not taskToToggle.isComplete
	taskToToggle.save()

	return redirect('/user/dashboard')

@login_required
def remove(request):
	if 'id' in request.GET.keys():
		id = request.GET['id']
	else:
		return redirect('/user/dashboard/?errors=Id+Not+Found.')

	taskToToggle = models.Task.objects.filter(id=id)[0]
	taskToToggle.delete()

	return redirect('/user/dashboard')





#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
