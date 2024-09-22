from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)