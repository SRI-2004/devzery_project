# authorisation/forms.py
from django import forms
from .models import AuthorizationUser

class SignupForm(forms.ModelForm):
    class Meta:
        model = AuthorizationUser
        fields = ['name', 'age', 'profession', 'location', 'phone_number', 'email_id', 'username', 'password','is_admin']
        widgets = {'password': forms.PasswordInput}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
