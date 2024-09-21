from django.urls import path
from . import views

app_name = "nosotros"

urlpatterns = [
    path('nosotros/', views.index, name='nosotros'),
    path('about_me/', views.aboutme, name='about_me'),
    path('contacto', views.contacto, name='contacto'),
 ]
