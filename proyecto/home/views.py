from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, UserProfileForm, UserUpdateForm
from .models import UserProfile

def index(request):
    return render(request, 'home/index.html')

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('home:login')

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'home/profile.html'
    success_url = reverse_lazy('home:index')

    def get_object(self):
        # Devuelve el usuario actual, si no, Django va a esperar un pk en la URL
        return self.request.user

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:profile')  # Cambia 'profile' a tu URL de redirección
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'home/login.html')

@login_required
def profile_view(request):
    profile_form = UserProfileForm(instance=request.user.userprofile)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        if profile_form.is_valid():
            profile_form.save()
            return JsonResponse({'message': 'Avatar actualizado correctamente.'})

    return render(request, 'home/profile.html', {
        'profile_form': profile_form,
    })
