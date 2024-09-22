from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, UserProfileForm

def index(request):
    return render(request, 'home/index.html')

class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('home:login')

class Profile(LoginRequiredMixin, UpdateView):
    model = User  # Asegúrate de usar el modelo correcto
    form_class = UserProfileForm
    template_name = 'home/profile.html'
    success_url = reverse_lazy('home:index')

    def get_object(self):
        # Devuelve el perfil del usuario actualmente autenticado
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
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
      
        if profile_form.is_valid():
            profile_form.save()
            new_avatar_url = request.user.userprofile.image.url
            print(f"Nueva URL del avatar: {new_avatar_url}")  # Imprime la URL en la consola
            return JsonResponse({'message': 'Avatar actualizado correctamente.', 'new_avatar_url': new_avatar_url})
        else:
            return JsonResponse({'message': 'Error al actualizar el avatar.'}, status=400)
  
    profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'home/profile.html', {'profile_form': profile_form})
