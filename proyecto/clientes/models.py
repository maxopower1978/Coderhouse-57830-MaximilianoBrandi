from django.db import models

class Cliente(models.Model):
    # Modelo alta de clientes
    
    class Estado(models.TextChoices):
        # Estado civil
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
    direccion = models.TextField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=30)
    fecha_nacimiento = models.DateTimeField()
    estado_consulta = models.CharField(max_length=20, choices=Estado.choices)
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return (
            f"{self.apellido}, {self.nombre} ({self.dni}) - Telefono: {self.telefono}"
        )
