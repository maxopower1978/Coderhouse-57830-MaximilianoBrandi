from django.db import models
from django import forms

class Cliente(models.Model):
    # Modelo alta de clientes
    
    class Estado(models.TextChoices):
        # Estado civil
        SELECCIONE = '', 'Seleccione'
        SOLTERO = "SOLTERO", "soltero"
        CASADO = "CASADO", "casado"
        DIVORCIADO = "DIVORCIADO", "divorciado"
        SEPARADO = "SEPARADO", "separado"
        VIUDO = "VIUDO", "viudo"
        CONCUBINO = "CONCUBINO", "concubino"
        
    cuil = models.IntegerField(unique=True)
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(max_length=30)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estado_civil = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.SELECCIONE,  # Establece "Seleccione" como valor por defecto
    )
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return (
            f"{self.apellido}, {self.nombre} ({self.cuil}) - Telefono: {self.telefono}"
        )
