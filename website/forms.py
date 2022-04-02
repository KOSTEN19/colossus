"""Import line"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from user.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)
       # fields = "__all__"
        #fields = ('balance')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
        #fields = ('balance')        
       # fields = "__all__"