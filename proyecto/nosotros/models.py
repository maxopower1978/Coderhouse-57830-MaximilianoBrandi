from django.db import models

class Nosotros(models.Model):
    # Generador del modelo de clase profesional
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(null = True, blank = True)
    matricula = models.TextField(max_length=30)
    celular = models.IntegerField()
    disponible = models.BooleanField(default= True)
    
    class Meta:
        # Meta definición para clase Nosotros
        verbose_name = 'Nosotro'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return f"{self.nombre}, {self.descripcion}, {self.celular}"
    
from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"
