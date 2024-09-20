from django.urls import path,include
from . import views

app_name = "derechos"

urlpatterns = [
    path('derechos/', views.index, name='derechos'),
]
