from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'}))

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }))

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'repeat password'
    }))

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": "Name"
    }))

    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control',
        "placeholder": "Surname"
    }))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'first_name', 'last_name']
