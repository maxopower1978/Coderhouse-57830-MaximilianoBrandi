from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        # Incluir los campos necesarios: CUIL, Derecho, Abogado y Consulta
        fields = ['cuil', 'derecho', 'abogado', 'consulta', 'fecha_respuesta']
        # Widgets personalizados
        widgets = {
            'cuil': forms.Select(attrs={'class': 'form-control'}),
            'derecho': forms.Select(attrs={'class': 'form-control'}),
            'abogado': forms.Select(attrs={'class': 'form-control'}),
            'consulta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Área de texto para consulta
            'fecha_respuesta': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',  # Para que se muestre un selector de fecha
            }),
        }

class CreateForm(forms.ModelForm):
    class Meta:
        model = Consulta
        # Incluir los campos necesarios: CUIL, Derecho, Abogado y Consulta
        fields = ['cuil', 'derecho', 'abogado', 'consulta',]
        # Widgets personalizados
        widgets = {
            'cuil': forms.Select(attrs={'class': 'form-control'}),
            'derecho': forms.Select(attrs={'class': 'form-control'}),
            'abogado': forms.Select(attrs={'class': 'form-control'}),
            'consulta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Área de texto para consulta
             }