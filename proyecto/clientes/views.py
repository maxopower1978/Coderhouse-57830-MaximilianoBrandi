# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, UpdateView
# from .forms import CustomUserCreationForm, UserProfileForm

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cliente
from .forms import ClienteForm, ClienteCreateForm #, LoginForm

# @login_required
def index(request):
   return render (request, 'clientes/index.html')

# class Register(CreateView):
#     form_class = ClienteForm
#     template_name = 'clientes/register.html'
#     success_url = reverse_lazy('home:index')

# class Profile(LoginRequiredMixin, UpdateView):
#     model = Cliente
#     form_class = ClienteForm
#     template_name = 'clientes/profile.html'
#     success_url = reverse_lazy('clientes:index')

#     def get_object(self):
#         # Devuelve el usuario actual, si no, Django va a esperar un pk en la URL
#         return self.request.user

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cuil = form.cleaned_data['cuil']
#             password = form.cleaned_data['password1']
#             user = authenticate(request, username=cuil, password=password1)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home:index')  # Redirige a la página principal
#             else:
#                 form.add_error(None, 'Credenciales incorrectas')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# listado
class ClienteList(ListView):
    model = Cliente

# create
class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteCreateForm
    success_url = reverse_lazy('clientes:cliente_list')

# Detail
class ClienteDetail(DetailView):
    model = Cliente

# # Update
class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_list')

# Delete
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list')