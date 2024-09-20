from django.contrib import admin
from . import models

@admin.register(models.Nosotros)
class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion','disponible',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
    list_filter = ('disponible','nombre')