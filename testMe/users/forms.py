from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'Enter Email'}))
    first_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")