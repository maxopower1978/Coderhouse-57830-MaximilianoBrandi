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
                'type': 'date',
                'style': 'width: 150px; margin: 0 auto;'  # Ajusta el tamaño y centra
            }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Filtrar el campo 'derecho' para mostrar solo el nombre del derecho deseado
            derecho = Derecho.objects.get(id=1)  # Cambia 1 por el ID del derecho que deseas mostrar
            self.fields['derecho'].queryset = Derecho.objects.filter(id=derecho.id)
            self.fields['derecho'].initial = derecho  # Establecer el valor inicial como el derecho específico


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