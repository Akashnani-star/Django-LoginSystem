from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.forms.widgets import PasswordInput,TextInput

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'myform-input','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'myform-input','placeholder':'Password'}))


class CustomCreateForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'myform-input','placeholder': 'Username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'myform-input','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'myform-input','placeholder':'Confirm Password'}))

# widgets in forms

