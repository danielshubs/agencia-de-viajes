from django.shortcuts import render, get_object_or_404
from . import models
from .models import Viaje


# Create your views here.
def index(request):

    lista_viajes = models.Viaje.objects.select_related('destino').all()

    context = {
        'lista_viajes': lista_viajes,
    }
    return render(request, 'index.html' , context)

def detalle_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje, pk=viaje_id)
    return render(request, 'viaje_details.html', {'viaje': viaje})


    return render(request, 'index.html', {'destinos': lista_destinos})

def destinos(request, nombre_destino: str = None):
    if nombre_destino:
        return render(request, 'destino.html', {'destino': nombre_destino})
    else:
        return render(request, 'destinos.html', {'destinos': lista_destinos})

def reservar(request, nombre_destino: str = None):
    if nombre_destino:
        return render(request, 'reservar.html', {'destino': nombre_destino})
    else:
        return render(request, 'reservar.html', {'destinos': lista_destinos})