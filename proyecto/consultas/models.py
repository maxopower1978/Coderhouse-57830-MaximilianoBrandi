from django.db import models
from derechos.models import Derecho
from clientes.models import Cliente
from nosotros.models import Nosotros

class Consulta(models.Model):
    # Generador de modelo de consulta

    class Estado(models.TextChoices):
        # Estado de la consulta
        PENDIENTE = "PENDIENTE", "Pendiente"
        RESPONDIDA = "RESPONDIDA", "Respondida"

    cuil = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    derecho = models.ForeignKey(Derecho, on_delete=models.DO_NOTHING)
    abogado = models.ForeignKey(Nosotros, on_delete=models.DO_NOTHING)
    consulta = models.TextField(max_length=200)
    fecha_consulta = models.DateField(auto_now=True)
    estado_consulta = models.CharField(
        max_length=10, choices=Estado.choices, default=Estado.PENDIENTE
    )
    fecha_respuesta = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return f"Nro CUIL: {self.cuil}, Derecho: {self.derecho}, Consulta: {self.consulta}, Estado: {self.estado_consulta}, Fecha de consulta: {self.fecha_consulta}"
