from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from . import forms
from . import models
from django.contrib.auth.models import User
# Create your views here.


@login_required #this decorator makes sure that only logged in users can access the "view" or function below.
def create(request): #creates tasks by fetching the form in the POST request and adding it to the database.
	if request.method != 'POST':
		return HttpResponse('Request Error')
	else: 
		# print(request.POST)
		form = forms.CreateTaskForm(request.POST) #fetches the form from the request and creates a CreateTaskForm object.
		if form.is_valid(): #checks if the form is valid. By calling this command, it also modifies the attribute cleaned_data by putting the information there as a dictionary.
			formData = form.cleaned_data
			newTask = models.Task(owner=request.user, title=formData['title'], description=formData['description'], isComplete=False) #creates Task object.
			newTask.save() #saves it before adding collaborators. It needs to be saved before adding ManyToMany object relations (in this case collaborators).

			collaborators = [formData['collaborator1'], formData['collaborator2'], formData['collaborator3']] #creates list with collaborators emails (usernames)

			for c in collaborators:
				u = User.objects.filter(username=c) #try to get an user with this username.
				if u:
					newTask.collaborators.add(u[0]) #if there is a user with this username, add it to the task as a collaborator.
			newTask.save()

			print('Task saved: ' + newTask.title + '\n\n') #for debugging.

		else:
			# print(form.errors.as_data()) #for debugging.
			return HttpResponse('Invalid Form.')
	
		return redirect('/user/dashboard') #redirects back to the user's dashboard.

@login_required
def complete(request): #toggles task as complete or incomplete, by changing this boolean attribute to the opposite of what it is.
	if 'id' in request.GET.keys(): #if there is a task id in the GET request query string, store it in the variable id.
		id = request.GET['id']
	else: #else, there is an error finding the task in the database.
		return redirect('/user/dashboard/?errors=Id+Not+Found.') 

	taskToToggle = models.Task.objects.filter(id=id)[0] #gets task from the database
	taskToToggle.isComplete = not taskToToggle.isComplete #changes the isComplete attribute.
	taskToToggle.save()

	return redirect('/user/dashboard')

@login_required
def remove(request):
	if 'id' in request.GET.keys(): #same as the complete function.
		id = request.GET['id']
	else:
		return redirect('/user/dashboard/?errors=Id+Not+Found.')

	try:
		taskToToggle = models.Task.objects.filter(id=id)[0]
	except:
		return redirect('/user/dashboard/?errors=Task+Not+Found.') 
	taskToToggle.delete() #deletes the task from the db.

	return redirect('/user/dashboard')



