# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', LoginView.as_view(template_name='home/login.html'), name='login'),
    # path('logout', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
#     path('register', views.Register.as_view(), name='register'),
#     path('profile', views.Profile.as_view(), name='profile'),
]