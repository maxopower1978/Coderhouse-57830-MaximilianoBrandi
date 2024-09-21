from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
        }

class ClienteCreateForm(forms.ModelForm):
   class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'style': 'width: 150px; margin: 0 auto;'  # Ajusta el tamaño y centra
            }),
        }

# class LoginForm(forms.Form):
#     cuil = forms.CharField(max_length=15, label='Número de CUIL')
#     password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
