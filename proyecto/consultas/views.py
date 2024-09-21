from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Consulta
from .forms import ConsultaForm, CreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render (request, 'consultas/consulta_index.html')

# # listado
# # def nosotros_list(request):
# #     consulta = request.GET.get('q')
# #     if consulta:
# #         query = Nosotros.objects.filter(abogado__icontains=consulta)
# #     else:
# #         query = Nosotros.objects.all()
# #     return render(request,'nosotros/nosotros_list.html', {"object_list": query})

class ConsultaList(ListView):
    model = Consulta

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         consulta = self.request.GET.get('q')
#         if consulta:
#             queryset = Cliente.objects.filter(dni__icontains=consulta)
#         return queryset

# # create
# # def nosotros_create(request):
# #     if request.method == "GET":
# #         form = NosotrosForm()
# #     if request.method == "POST":
# #         form = NosotrosForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('nosotros:nosotros_list')
# #     return render(request, 'nosotros/nosotros_form.html', {'form':form})

class ConsultaCreate(CreateView):
    model = Consulta
    form_class = CreateForm
    success_url = reverse_lazy('consultas:consulta_list')

# # Detail
# # def nosotros_detail(request, pk:int):
# #     query = Nosotros.objects.get(id=pk)
# #     contexto = {'object':query}
# #     return render(request, 'nosotros/nosotros_detail.html', contexto)

class ConsultaDetail(DetailView):
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
# # def nosotros_update(request, pk:int):
# #     query = Nosotros.objects.get(id=pk)
# #     if request.method == "GET":
# #         form = NosotrosForm(instance=query)
        
# #     if request.method == "POST":
# #         form = NosotrosForm(request.POST, instance=query)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('nosotros:nosotros_list')

# #     return render(request, 'nosotros/nosotros_form.html', {'form':form})

class ConsultaUpdate(UpdateView):
    model = Consulta
    form_class = ConsultaForm
    success_url = reverse_lazy('consultas:consulta_list')

# # Delete
# # def nosotros_delete(request, pk:int):
# #     query = Nosotros.objects.get(id=pk)
# #     if request.method == "POST":
# #         query.delete()
# #         return redirect('nosotros:nosotros_list')
# #     return render(request, 'nosotros/nosotros_confirm_delete.html', {'object':query})

class ConsultaDelete(DeleteView):
    model = Consulta
    success_url = reverse_lazy('consultas:consulta_list') 