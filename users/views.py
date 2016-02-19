from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
import users.forms
import tasks.forms
import tasks.models
# import users.models
import re as regex


def register(request):
	if request.method != 'POST':
		return HttpResponse('Request Error')
	else:
		# print(request.POST)
		form = users.forms.RegisterForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			if formData['password'] != formData['password_confirmation']:
				return redirect('/', {'errors': ''})
			try:
				newUser = User.objects.create_user(username=formData['email'], password=formData['password'], first_name=formData['fl_name'])
			except Exception, e:
				# print e
				if regex.search(r'.*UNIQUE.*', str(e)):
					errors = '?errors=Account+with+this+email+already+exists!'
				else:
					errors = ''
				return redirect('/' + errors)
			user = authenticate(username=formData['email'], password=formData['password'])
			login(request, user)
			return redirect('/user/dashboard')
		else:
			# print(form.errors.as_data())
			if 'email' in form.errors.as_data().keys() and regex.search(r'.*Enter a valid email address.*', str(form.errors.as_data()['email'])):
					errors = '?errors=Invalid+email+address'
			else:
				errors = '?errors=Invalid+Form.'
			return redirect('/' + errors)
	
		return HttpResponse('Processing.')


def login_user(request):
	if request.method != 'POST':
		return HttpResponse('Request Error')
	else:
		form = users.forms.LoginForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			user = authenticate(username=formData['email'], password=formData['password'])
			# print(authenticate(username=formData['email'], password=formData['password']))
			# print(form.errors.as_data())
			if user is not None:
				print('Valid user!!')
				login(request, user)
				return redirect('/user/dashboard')
				# return redirect('/')
			else:
				try:
					existingUser = User.objects.get(username=formData['email'])
				except Exception, e:
					return redirect('/?errors=Invalid+email+address')
				# print('The username and password were incorrect.')
				return redirect('/?errors=Invalid+password')
			
		else:
			return HttpResponse('Invalid Form.')
	

	return HttpResponse("USER LOGIN")


def logout_user(request):
	# print('User logged out!')
	logout(request)
	return redirect('/')
	# return HttpResponse("USER LOGOUT")


@login_required
def dashboard(request):
	if request.user.is_authenticated():
		if 'errors' in request.GET.keys():
			errors = request.GET['errors'] 
		else:
			errors = None
			# print(request.user.tasks.all())
		userTasks = list(request.user.owned_tasks.all()) + list(request.user.tasks.all())
		return render(request, 'dashboard.html', {'errors':errors, 'CreateTaskForm' : tasks.forms.CreateTaskForm(), 'currentUser': request.user, 'userTasks': userTasks})
	else:
		return HttpResponse("You are not authorized to be here.")


#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
