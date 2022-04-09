from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserModel

class CreateUserForm(UserCreationForm):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Username..."}))
	email = forms.CharField(required=True, widget=forms.EmailInput(attrs={"placeholder": "enter your e-mail"}))
	password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "password"}))
	password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "confirm your password"}))
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']