from django.contrib import admin
from . import models

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cuil','apellido','nombre','telefono')
    search_fields = ('cuil', 'apellido')
    ordering = ('apellido',)
    list_filter = ('apellido', 'cuil',)