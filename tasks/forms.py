from django import forms
MAX_LENGTH = 50


#This is the create task form.
class CreateTaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="Description", max_length=5000, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    collaborator1 = forms.CharField(max_length=MAX_LE2NGTH, required=False, widget=forms.TextInput(attrs={'placeholder': 'Collaborator 1'}))
    collaborator2 = forms.CharField(max_length=MAX_LENGTH, required=False, widget=forms.TextInput(attrs={'placeholder': 'Collaborator 2'}))
    collaborator3 = forms.CharField(max_length=MAX_LENGTH, required=False, widget=forms.TextInput(attrs={'placeholder': 'Collaborator 3'}))
    
