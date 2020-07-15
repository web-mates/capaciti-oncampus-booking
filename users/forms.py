from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django.db import models



class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1', 
            'password2', 
            ]

class EditUserForm(UserChangeForm):
    model = User
    fields = (
        'username', 
        'first_name',
        'last_name',
        'email',
    )
    