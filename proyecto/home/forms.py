from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')   

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'  

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')  
