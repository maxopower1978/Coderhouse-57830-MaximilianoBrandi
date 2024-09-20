from django.shortcuts import render, redirect
from .models import Nosotros
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    consulta = request.GET.get('q')
    if consulta:
        query = Nosotros.objects.filter(nombre__icontains=consulta)
    else:
        query = Nosotros.objects.all()
    return render(request,'nosotros/index.html', {"object_list": query})