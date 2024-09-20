from django.urls import path,include
from . import views
from .views import ClienteList, ClienteCreate, ClienteDelete, ClienteDetail, ClienteUpdate
from django.conf import settings
from django.conf.urls.static import static

app_name = "clientes"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('clientes/list/', ClienteList.as_view(), name='cliente_list'),
    path('clientes/create/', ClienteCreate.as_view(), name='cliente_create'),
    path('clientes/detail/<int:pk>', ClienteDetail.as_view(), name='cliente_detail'),
    path('clientes/update/<int:pk>', ClienteUpdate.as_view(), name='cliente_update'),
    path('clientes/delete/<int:pk>', ClienteDelete.as_view(), name='cliente_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)