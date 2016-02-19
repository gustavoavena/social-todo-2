from django import forms
MAX_LENGTH = 50

class CreateTaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=MAX_LENGTH, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="Description", max_length=MAX_LENGTH, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    collaborator1 = forms.CharField(max_length=MAX_LENGTH, required=False, widget=forms.TextInput(attrs={'placeholder': 'Collaborator 1'}))
    collaborator2 = forms.CharField(max_length=MAX_LENGTH, required=False, widget=forms.TextInput(attrs={'placeholder': 'Collaborator 2'}))
    collaborator3 = forms.CharField(max_length=MAX_LENGTH, required=False, widget=forms.TextInput(attrs={'placeholder': 'Collaborator 3'}))
    
