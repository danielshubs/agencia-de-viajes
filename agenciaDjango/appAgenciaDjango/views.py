from django.shortcuts import render, get_object_or_404 , redirect
from . import models
from .models import Viaje , Cliente , Destino , Reserva
from django.contrib import messages
from .models import Viaje, Destino
from django.db.models import Min, Max
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    lista_destinos = Destino.objects.all()[:3]
    return render(request, 'index.html', {'destinos': lista_destinos})



def detalle_destino(request, destinoID):
    destino = get_object_or_404(models.Destino, destinoID=destinoID)
    viajes_asociados = models.Viaje.objects.filter(destino=destino)
    return render(request, 'destino.html', {'destino': destino, 'viajes': viajes_asociados})

def destinos(request):
    lista_destinos = models.Destino.objects.annotate(
        precio_min=Min('viaje__precio'),
        precio_max=Max('viaje__precio')
    )
    lista_viajes = models.Viaje.objects.all()
    return render(request, 'destinos.html', {'destinos': lista_destinos, 'viajes': lista_viajes})

def reservar(request, nombre_destino: str = None):
    lista_destinos = models.Destino.objects.all()

    if nombre_destino:
        return render(request, 'reservar.html', {'destino': nombre_destino})
    else:
        return render(request, 'reservar.html', {'destinos': lista_destinos})

def login_rend(request):
    return render(request, 'login.html')

def login_enter(request):
    if request.method == 'POST':
        mail = request.POST.get('email')
        password = request.POST.get('password')


        # Usamos authetificate para comprobar desde django que el usuario existe , para ello hay que indicar qye
        # nuestra clase sera AUTH_USER_MODEL = 'miapp.Cliente' la que utilizara django para la autenticacion al hacer
        # esto podremos utilizar instancia user desde cualqueir parte de django junto con sus atributos y metodos
        user = authenticate(request, username=mail, password=password)

        if user:
            print("user autenticado")
            login(request, user)
            return redirect('index')
        print("user no autenticado")
        messages.error(request, "Usuario o contraseña incorrectos.")
        return login_rend(request)

def viajes_general(request):
    lista_viajes = Viaje.objects.all()
    return render(request, 'viajes.html', {'viajes': lista_viajes})

def viajes(request , destino_nombre: str):
    destino = Destino.objects.get(nombre=destino_nombre)
    lista_viajes = Viaje.objects.filter(destino=destino.destinoID)
    return render(request, 'viajes.html', {'viajes': lista_viajes})

def viajes_max(request, destino_nombre, precio_maximo):
    destino = Destino.objects.get(nombre=destino_nombre)
    lista_viajes = Viaje.objects.filter(destino=destino.destinoID, precio__lte=precio_maximo)
    return render(request, 'viajes.html', {'viajes': lista_viajes})

def formulario_reserva(request, viaje_id):
    viaje = Viaje.objects.get(viajeID=viaje_id)
    return render(request, 'reservar.html', {
        'viaje': viaje
    })

def confirmar_reserva(request, viaje_id):
    if request.method == 'POST':
        viaje = Viaje.objects.get(viajeID=viaje_id)

        # Crear o obtener cliente

        # Django intenta buscar un objeto Cliente donde el campo email coincida con el valor
        # proporcionado (request.POST.get('email')).Si no encuentra un objeto con ese email,
        # crea uno nuevo utilizando el valor de email y los valores proporcionados en el diccionario defaults.
        cliente, created = Cliente.objects.get_or_create(
            email=request.POST.get('email'),
            defaults={
                'nombre': request.POST.get('nombre'),
                'apellido': request.POST.get('apellido'),
                'telefono': request.POST.get('telefono')
            }
        )

        # Crear la reserva
        reserva = Reserva.objects.create(
            clienteID=cliente,
            viajeID=viaje,
            seguro_viaje='seguro_viaje' in request.POST,
        )

        # Aquí procesarías el pago con los datos de tarjeta
        cc_numero = request.POST.get('cc_numero')
        cc_expiracion = request.POST.get('cc_expiracion')
        cc_cvv = request.POST.get('cc_cvv')

        return render(request, 'reserva_exitosa.html', {'reserva': reserva , 'id': hash(reserva)})

    return redirect('formulario_reserva', viaje_id=viaje_id)

def mis_reservas(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cliente = request.user
    cliente = Cliente.objects.get(email=cliente.email)
    reservas = Reserva.objects.filter(clienteID=cliente.clienteID)

    return render(request, 'mis_reservas.html', {'reservas': reservas})


