from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Consulta
from .forms import ConsultaForm, CreateForm

@login_required
def index(request):
    return render (request, 'consultas/consulta_index.html')

# listado
class ConsultaList(LoginRequiredMixin, ListView):
    model = Consulta

# create
class ConsultaCreate(LoginRequiredMixin, CreateView):
    model = Consulta
    form_class = CreateForm
    success_url = reverse_lazy('consultas:consulta_list')

# Detail
class ConsultaDetail(LoginRequiredMixin, DetailView):
    model = Consulta
    template_name = 'consultas/consulta_detail.html'
    context_object_name = 'consulta'

    # Solo mostrar ciertos campos en el contexto de la vista
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Limitar los campos mostrados
        consulta = self.get_object()
        context['cuil'] = consulta.cuil
        context['derecho'] = consulta.derecho
        context['abogado'] = consulta.abogado
        return context

# # Update
class ConsultaUpdate(LoginRequiredMixin, UpdateView):
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy('consultas:consulta_list')

# # Delete
class ConsultaDelete(LoginRequiredMixin, DeleteView):
    model = Consulta
    success_url = reverse_lazy('consultas:consulta_list') 