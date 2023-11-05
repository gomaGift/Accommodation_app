from django import forms
from django.contrib.auth.models import models
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CustomLoginForm(forms.Form):
    id_number = forms.CharField(max_length=100, label='Identity number')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-class'}))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id_num', 'province', 'password1', 'password2']

    