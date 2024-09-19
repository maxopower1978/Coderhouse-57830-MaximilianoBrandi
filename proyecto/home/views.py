# from django.contrib.auth.models import User
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, UpdateView
# from .forms import CustomUserCreationForm, UserProfileForm

def index(request):
    return render(request, "home/index.html")
