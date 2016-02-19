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


#I used Django's built-in authentication modules. They are simple and work great.

#this function is responsible for registering users. It gets a register form from the POST request, handles the data, saves the users to the db and logs the user in.
def register(request):
	if request.method != 'POST':
		print('Wrong request method for registering.') #for debugging.
		return HttpResponse('Request Error')
	else:
		form = users.forms.RegisterForm(request.POST) #creates a RegisterForm object from the form in the POST request. All of the form classes I use are derived from Django's Form class.
		print('New user registering. Fetching form data...')
		if form.is_valid(): #checks if the form is valid and sets the cleaned_data attribute with the form data in a dictionary format.
			formData = form.cleaned_data
			if formData['password'] != formData['password_confirmation']: #checks if password and password confirmation match.
				return redirect('/', {'errors': 'Password and password confirmation dont match.'})
			try: #tries to create a new user (user object) and save it to the db. It saves the new object automatically and returns an error if something goes wrong.
				newUser = User.objects.create_user(username=formData['email'], password=formData['password'], first_name=formData['fl_name'])
			except Exception, e: #if there is an error, I check it to see if it matches any error that should be informed to the testing script (like invalid email or duplicate email).
				if regex.search(r'.*unique.*', str(e)):
					errors = '?errors=Account+with+this+email+already+exists!'
				else:
					print('error creating user:')
					print(e) #for debugging
					errors = ''
				return redirect('/' + errors)
			user = authenticate(username=formData['email'], password=formData['password']) #before using the login function to log a user in, 
			#the authenticate function needs to be called to set some attributes in the user object and allow it to be logged in.
			login(request, user)
			print('New user registered! User: ' + user.username + '. Logging user in...') #for debugging
			return redirect('/user/dashboard')
		else:
			# print(form.errors.as_data()) #for debugging.
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
		form = users.forms.LoginForm(request.POST) #same as the other functions that process forms.
		if form.is_valid():
			formData = form.cleaned_data
			user = authenticate(username=formData['email'], password=formData['password'])
			if user is not None: #if there is an user in the db and the password matches, logs the user in.
				print('Valid user!!')
				login(request, user)
				return redirect('/user/dashboard')
				# return redirect('/')
			else: #since authenticate return None if it fails, you can't tell why it failed (no user with this username or wrong password). So if it fails, I try to get a user object from the db
			# to find out if it failed because there is no user registered with this email or if the password was wrong. I need to tell these two apart because of the testing scripts.
				try:
					existingUser = User.objects.get(username=formData['email'])

				except Exception, e:
					return redirect('/?errors=Invalid+email+address')
				return redirect('/?errors=Invalid+password')
			
		else:
			if 'email' in form.errors.as_data().keys():
				errors = '?errors=Invalid+email+address'
			else:
				errors = '?errors=Invalid+Form.'
			return redirect('/' + errors)

	return HttpResponse("USER LOGIN")


def logout_user(request): #logs out the user by calling django's logout function.
	# print('User logged out!')
	logout(request)
	return redirect('/')
	# return HttpResponse("USER LOGOUT")


@login_required
def dashboard(request): #This renders the user's dashboard (page with all of his tasks and where he can create new ones).
	if 'errors' in request.GET.keys():
		errors = request.GET['errors']
	else:
		errors = None
	userTasks = list(request.user.owned_tasks.all()) + list(request.user.tasks.all()) #fetches all of the user's tasks (owned by him or assigned to him by another user) and adds them all to a list.
	return render(request, 'dashboard.html', {'errors':errors, 'CreateTaskForm' : tasks.forms.CreateTaskForm(), 'currentUser': request.user, 'userTasks': userTasks}) #renders the dashboard.


#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
