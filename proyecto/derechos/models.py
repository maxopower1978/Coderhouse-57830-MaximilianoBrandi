from django.db import models

class Derecho(models.Model):
    # Modelo para los derechos de asesoramiento
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre}, {self.descripcion}: {self.disponible}"

    class Meta:
        # Meta definición para el modelo Derecho
        verbose_name = 'Derecho'
        verbose_name_plural = 'Derechos'

