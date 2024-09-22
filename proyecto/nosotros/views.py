from django.shortcuts import render, redirect
from .models import Nosotros
from .forms import ContactForm

def index(request):
    consulta = request.GET.get('q')
    if consulta:
        query = Nosotros.objects.filter(nombre__icontains=consulta)
    else:
        query = Nosotros.objects.all()
    return render(request,'nosotros/index.html', {"object_list": query})

def aboutme(request):
    return render(request,'nosotros/about_me.html')

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Lógica para procesar el formulario
            form.save()
            return redirect('home:index')
    else:
        form = ContactForm()
    
    return render(request, 'nosotros/contacto.html', {'form': form})