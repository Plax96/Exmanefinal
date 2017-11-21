from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from .forms import *

def listar(request):
    grados=Materia.objects.all().values()
    return render(request,'grado/listar.html',{'grado':grados})

def crear(request):
    if request.method == "POST":
        grado = GradoForm(request.POST)
        if grado.is_valid():
            grado = grado.save(commit = False)
            grado.save()
            return redirect('asignar', iden=grado.id)
    else:
        grado = GradoForm()
    return render(request, 'grado/crear.html', {'form':grado})

def materia(request):
    if request.method == "POST":
        grado = MateriaForm(request.POST)
        if grado.is_valid():
            grado = grado.save(commit = False)
            grado.save()
            return redirect('asignar', iden=grado.id)
    else:
        grado = GradoForm()
    return render(request, 'grado/materia.html', {'form':grado})
