from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    # email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput())

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={'class': 'pass form-control w-100 shadow border-0', 'type': 'password', 'placeholder': ''}
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={'class': 'pass form-control w-100 shadow border-0', 'type': 'password', 'placeholder': ''}
        ),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            }),
            'email': EmailInput(attrs={
                'class': "form-control w-100 shadow border-0",
                'placeholder': ''
            })
        }
