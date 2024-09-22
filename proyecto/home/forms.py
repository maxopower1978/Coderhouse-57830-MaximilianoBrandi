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
        fields = '__all__'  # Campos del usuario

class UserProfileForm(forms.ModelForm):
    image = forms.ImageField(label='avatar',required=False)
    class Meta:
        model = UserProfile
        fields = ['image']  # Solo el campo del avatar
