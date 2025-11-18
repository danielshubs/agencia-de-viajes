from django.shortcuts import render, get_object_or_404 , redirect
from . import models
from .models import Viaje , Cliente , Destino , Reserva
from django.contrib import messages
from .models import Viaje, Destino


# Create your views here.
def index(request):
    lista_destinos = Destino.objects.all()[:3]
    return render(request, 'index.html', {'destinos': lista_destinos})

def detalle_viaje(request, viaje_id):
    viaje = get_object_or_404(Viaje, pk=viaje_id)
    return render(request, 'viaje_details.html', {'viaje': viaje})


def detalle_destino(request, destinoID):
    destino = get_object_or_404(models.Destino, destinoID=destinoID)
    viajes_asociados = models.Viaje.objects.filter(destino=destino)
    return render(request, 'destino.html', {'destino': destino, 'viajes': viajes_asociados})

def destinos(request):
    lista_destinos = models.Destino.objects.all()
    return render(request, 'destinos.html', {'destinos': lista_destinos})

def reservar(request, nombre_destino: str = None):
    lista_destinos = models.Destino.objects.all()

    if nombre_destino:
        return render(request, 'reservar.html', {'destino': nombre_destino})
    else:
        return render(request, 'reservar.html', {'destinos': lista_destinos})

def login(request):
    return render(request, 'login.html')

def login_enter(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        user = Cliente.objects.filter(email=mail, password=password).first()
        if user:
            return redirect('index')
        messages.error(request, "Usuario o contraseña incorrectos.")
        return login(request)


