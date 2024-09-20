from django.shortcuts import render
from .models import Derecho

# LISTAR
def index(request):
    consulta = request.GET.get('q')
    if consulta:
        query = Derecho.objects.filter(nombre__icontains=consulta)
    else:
        query = Derecho.objects.all()
    return render(request,'derechos/index.html', {"object_list": query})