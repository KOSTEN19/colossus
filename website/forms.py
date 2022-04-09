"""Import line."""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """CLass line"""
    class Meta:
        """Class line"""
        model = CustomUser
        fields = ('username',)
        #fields = "__all__"
        #fields = ('balance')


class CustomUserChangeForm(UserChangeForm):
    """Class line"""
    class Meta:
        """Class line"""
        model = CustomUser
        fields = '__all__'
        #fields = ('balance')
        #fields = "__all__"
