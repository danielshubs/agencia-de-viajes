from django.shortcuts import render, get_object_or_404 , redirect
from . import models
from .models import Viaje , Cliente , Destino , Reserva
from django.contrib import messages
from .models import Viaje, Destino
from django.db.models import Min, Max
from django.contrib.auth import authenticate, login
import datetime
from django.db import IntegrityError
from django.contrib.auth import logout


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
            # login() permite que el usuario permanezca autenticado mientras navega por diferentes
            # páginas de la aplicación. Por lo que podriamos usar request.user en cualquier html o vista
            # para obtener el usuario autenticado actualmente y asi usar su informacion que se halla en la ddbb
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
    print(reservas)
    reservas_updated =[reserva for reserva in reservas if reserva.viajeID.fecha_regreso >=  datetime.date.today()]
    ids = [hash(reserva) for reserva in reservas]

    return render(request, 'mis_reservas.html', {'reservas': zip(reservas_updated, ids) })

def registro_view(request):
    """Vista para mostrar el formulario de registro"""
    return render(request, 'registro.html')

def registro_procesar(request):
    """Procesar el registro de nuevo usuario con modelo actual"""
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Validaciones básicas
        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('registro')

        if len(password) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres')
            return redirect('registro')

        # Verificar si el usuario ya existe
        if Cliente.objects.filter(email=email).exists():
            messages.error(request, 'Este correo ya está registrado')
            return redirect('registro')

        try:
            # Dividir nombre completo
            nombre_partes = nombre_completo.split(' ', 1)
            nombre = nombre_partes[0]
            apellido = nombre_partes[1] if len(nombre_partes) > 1 else ''

            # Crear usuario - IMPORTANTE: el username es obligatorio para AbstractUser
            usuario = Cliente.objects.create_user(
                username=email,  # Obligatorio
                email=email,
                password=password,
                # Campos de AbstractUser
                first_name=nombre,
                last_name=apellido,
                # Campos específicos de tu modelo
                nombre=nombre,
                apellido=apellido,
                telefono=''
            )

            # Autenticar
            auth_user = authenticate(request, username=usuario.email, password=usuario.password)
            if auth_user:
                login(request, auth_user)
                messages.success(request, f'¡Registro exitoso! Bienvenido/a, {nombre}')
                return redirect('index')

        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('registro')

    return redirect('registro')

def logout_view(request):
    """Cerrar sesión"""
    logout(request)  # Ya está importado arriba
    messages.success(request, 'Sesión cerrada correctamente')
    return redirect('index')

