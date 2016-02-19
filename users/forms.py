from django import forms
MAX_LENGTH = 50

class RegisterForm(forms.Form):
    fl_name = forms.CharField(label='Name', max_length=MAX_LENGTH, required=True)
    email = forms.EmailField(label="Email", max_length=MAX_LENGTH, widget=forms.EmailInput(), required=True)
    password = forms.CharField(label="Password", max_length=MAX_LENGTH, widget=forms.PasswordInput(), required=True)
    password_confirmation = forms.CharField(label="Passoword Confirmation", max_length=MAX_LENGTH, widget=forms.PasswordInput(), required=True)

class LoginForm(forms.Form):
	email = forms.CharField(label="Email", max_length=MAX_LENGTH, required=True)
	password = forms.CharField(label="password", max_length=MAX_LENGTH, widget=forms.PasswordInput(), required=True)