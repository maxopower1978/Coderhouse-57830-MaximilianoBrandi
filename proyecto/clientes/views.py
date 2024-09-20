from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
   return render (request, 'clientes/index.html')

# listado
class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

# create
class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_list')

# Detail
class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente

# Update
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_list')

# Delete
class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list') 