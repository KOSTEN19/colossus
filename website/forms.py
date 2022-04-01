from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'fadeI',
                ' placeholder': 'login'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'fadeIn third', ' placeholder': 'password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'fadeIn fourth', ' placeholder': 'password again'}))


class LoginUserForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'fadeI',
                ' placeholder': 'login'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'fadeIn third', ' placeholder': 'password'}))
