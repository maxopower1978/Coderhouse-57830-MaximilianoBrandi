from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'email', 'mensaje']  # Ajusta los campos de tu modelo
