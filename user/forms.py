from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, EmailInput

class CustomUserForm(UserCreationForm):

    class Meta:

        model = CustomUser
        fields = ['email', 'nickname', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.EmailField(widget=EmailInput(), required=True)
    password = forms.CharField(widget=PasswordInput(), required=True)