from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(label= "Password", widget=forms.PasswordInput, min_length=4)
    password2 = forms.CharField(label= "Confirm Password", widget=forms.PasswordInput, min_length=4)
    
