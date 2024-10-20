
#* this is new file for me, it will be for creating forms to be used in the app
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUserModel

#* Starting with the form for creating a new custom user
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = ('username', 'email' ,'age',)
        
        
#* Now to the form for changing a custom user
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email' ,'age',)