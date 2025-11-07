from django.shortcuts import render, get_object_or_404
from . import models
from .models import Viaje


# Create your views here.
def index(request):

    return render(request, 'index.html')

def detalle_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje, pk=viaje_id)
    return render(request, 'viaje_details.html', {'viaje': viaje})


def destinos(request):
        lista_destinos = models.Destino.objects.all()
        return render(request, 'destino.html', {'destino': lista_destinos})

def reservar(request, nombre_destino: str = None):
    lista_destinos = models.Destino.objects.all()

    if nombre_destino:
        return render(request, 'reservar.html', {'destino': nombre_destino})
    else:
        return render(request, 'reservar.html', {'destinos': lista_destinos})