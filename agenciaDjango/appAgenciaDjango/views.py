from django.shortcuts import render

# Ejemplo de lista de destinos turísticos
lista_destinos = ['París', 'Nueva York', 'Tokio', 'Londres', 'Roma']

# Create your views here.
def index(request):
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