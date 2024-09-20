from django.urls import path
from . import views

app_name = "nosotros"

urlpatterns = [
    path('nosotros/', views.index, name='nosotros'),
 ]
