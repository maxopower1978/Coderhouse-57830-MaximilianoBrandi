from django.urls import path
from . import views
# from .views import nosotros_list

app_name = "nosotros"

urlpatterns = [
    path('index/', views.index, name='index'),
 ]
