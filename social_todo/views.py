from django.shortcuts import render, redirect
from django.http import HttpResponse

import users.forms as forms
# Create your views here.


#this is the index controller. It will render the log in and register page as well as redirect to the user's
#dashboard if there is a logged in user.
def index(request):
	if request.user.is_authenticated():
		return redirect('/user/dashboard')
	RegisterForm = forms.RegisterForm()
	LoginForm = forms.LoginForm()
	if 'errors' in request.GET.keys():
		errors = request.GET['errors']
		print(errors)
		
	else:
		errors = None
		# print('No errors.')
	return render(request, 'index.html', {"title": "cpsc 113", "message": "Starting page!", 'RegisterForm' : RegisterForm, 'LoginForm': LoginForm, 'errors': errors})
    




