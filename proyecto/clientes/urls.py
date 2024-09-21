from django.urls import path,include
from django.conf import settings
from . import views
from .views import ClienteList, ClienteCreate, ClienteDetail, ClienteDelete,  ClienteUpdate
# from .views import Register, Profile
# from django.conf.urls.static import static
# from django.contrib.auth.views import LoginView, LogoutView

app_name = "clientes"

urlpatterns = [
    path('clientes/index/', views.index, name='index'),
    # path('register/', Register.as_view(), name='register'),
    # path('profile/', Profile.as_view(), name='profile'),
    # path('login/', LoginView.as_view(template_name='clientes/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='clientes/logout.html'), name='logout'),
    path('clientes/list/', ClienteList.as_view(), name='cliente_list'),
    path('clientes/create/', ClienteCreate.as_view(), name='cliente_create'),
    path('clientes/detail/<int:pk>', ClienteDetail.as_view(), name='cliente_detail'),
    path('clientes/update/<int:pk>', ClienteUpdate.as_view(), name='cliente_update'),
    path('clientes/delete/<int:pk>', ClienteDelete.as_view(), name='cliente_delete'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)