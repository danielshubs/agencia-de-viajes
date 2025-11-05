from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Viaje(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    fecha_salida = models.DateField()
    fecha_regreso = models.DateField()

    def __str__(self):
        return f"{self.cliente.nombre} - {self.destino.nombre}"
