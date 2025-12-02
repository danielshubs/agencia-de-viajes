from django.db import models
from django.contrib.auth.models import AbstractUser


class Cliente(AbstractUser):
    clienteID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    # Usasamos el email como username para la autenticacion
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'username']

    def __str__(self):
        return self.nombre


class Destino(models.Model):
    destinoID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    pais = models.CharField(max_length=100)
    moneda = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Viaje(models.Model):
    viajeID = models.AutoField(primary_key=True)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()
    plazas_disponibles = models.IntegerField()
    plazas_totales = models.IntegerField()

    def __str__(self):
        return f"{self.viajeID} - {self.destino.nombre}"

    # Todo : Crear funcion para calcular el numero de plazas totales del viaje en base al numero de reservas


class Reserva(models.Model):
    clienteID = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    viajeID = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    fecha_reserva = models.DateField(auto_now_add=True)
    seguro_viaje = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva {self.viajeID} - {self.clienteID.nombre}"
