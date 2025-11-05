from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    viajes = models.Viaje.objects.all()
    context = {
        'empresas': viajes,
    }
    return render(request, 'index.html' , context)
