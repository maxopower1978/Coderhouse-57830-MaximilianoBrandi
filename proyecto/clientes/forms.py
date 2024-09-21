from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
    
class LoginForm(forms.Form):
    cuil = forms.CharField(max_length=15, label='Número de CUIL')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
