from django.shortcuts import render
from django.http import HttpResponse

import users.forms as forms
# Create your views here.

def index(request):
	RegisterForm = forms.RegisterForm()
	LoginForm = forms.LoginForm()
	return render(request, 'index.html', {"title": "cpsc 113", "message": "Starting page!", 'RegisterForm' : RegisterForm, 'LoginForm': LoginForm})
    





#django-admin startapp users
#create a file called urls.py in new subapp
#edit urls.py in social-todo/urls following the model of tasks to route to new subapp
