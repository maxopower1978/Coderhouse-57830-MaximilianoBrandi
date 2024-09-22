from django.urls import path
from . import views
from .views import ConsultaList, ConsultaCreate, ConsultaDelete, ConsultaDetail, ConsultaUpdate

app_name = "consultas"

urlpatterns = [
    path('consultas/', views.index, name='consulta_index'),
    path('consultas/list/', ConsultaList.as_view(), name='consulta_list'),
    path('consultas/create/', ConsultaCreate.as_view(), name='consulta_create'),
    path('consultas/detail/<int:pk>', ConsultaDetail.as_view(), name='consulta_detail'),
    path('consultas/update/<int:pk>', ConsultaUpdate.as_view(), name='consulta_update'),
    path('consultas/delete/<int:pk>', ConsultaDelete.as_view(), name='consulta_delete'),
] 