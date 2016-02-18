from django import forms

class RegisterForm(forms.Form):
    fl_name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label="Email", max_length=30, widget=forms.EmailInput())
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label="Passoword Confirmation", max_length=30, widget=forms.PasswordInput())

class LoginForm(forms.Form):
	email = forms.EmailField(label="Email", max_length=30)
	password = forms.CharField(label="password", max_length=30, widget=forms.PasswordInput())