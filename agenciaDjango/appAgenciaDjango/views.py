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
