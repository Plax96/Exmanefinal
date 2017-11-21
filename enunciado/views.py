from django.shortcuts import render
from .models import *
from .forms import *

def listar(request):
    grados=Gestion_grado.objects.all().values()
    return render(request,'grado/listar.html',{'grado':grados})

def crear(request):
    grados=Gestion_grado.objects.all().values()
    return render(request,'grado/listar.html',{'grado':grado})

def asignar(request):
    grados=Gestion_grado.objects.all().values()
    return render(request,'grado/listar.html',{'grado':grado})
# Create your views here.
