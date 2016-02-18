from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
import users.forms
# import users.models


def register(request):
	if request.method != 'POST':
		return HttpResponse('Access Error')
	else:
		# print(request.POST)
		form = users.forms.RegisterForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			newUser = User.objects.create_user(username=formData['email'], password=formData['password'], first_name=formData['fl_name'])
		else:
			return HttpResponse('Invalid Form.')
	
		return HttpResponse('Processing.')


def login_user(request):
	if request.method != 'POST':
		return HttpResponse('Access Error')
	else:
		form = users.forms.LoginForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			user = authenticate(username=formData['email'], password=formData['password'])
			if user is not None:
				print('Valid user!!')
				login(request, user)
				# return redirect('/user/dashboard')
				return redirect('/')
			else:
				print('The username and password were incorrect.')
				return redirect('/')
			
		else:
			return HttpResponse('Invalid Form.')
	

	return HttpResponse("USER LOGIN")


def logout_user(request):
	print('User logged out!')
	logout(request)
	return redirect('/')
	# return HttpResponse("USER LOGOUT")


def dashboard(request):
	if request.user.is_authenticated():
		return render(request, 'dashboard.html')
	else:
		return HttpResponse("You are not authorized to be here.")


#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
