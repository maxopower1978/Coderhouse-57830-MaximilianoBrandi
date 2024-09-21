from django.contrib import admin
from . import models

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('cuil','derecho','consulta','fecha_consulta','estado_consulta')
    search_fields = ('cuil',)
    ordering = ('fecha_consulta',)
    list_filter = ('cuil', 'estado_consulta',)