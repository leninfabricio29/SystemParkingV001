from django.db import models
from django.utils.timezone import  datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.



class EspacioEstacionamiento (models.Model):
    codigoIdentificativo = models.CharField(max_length=10, blank=True)
    estadoEstacionamiento = models.BooleanField(default=True)
    def __str__(self):
        return self.codigoIdentificativo

class Automovil (models.Model):
    placa = models.CharField(max_length=10, blank=True)
    marca = models.CharField(max_length=15, blank=True)
    modelo = models.CharField(max_length=20, blank=True)



    def __str__(self):
        return self.placa

class Cliente (models.Model):
    nombre = models.CharField(max_length=20, blank=True)
    apellido = models.CharField(max_length=25, blank=True)
    cedula = models.CharField(max_length=10, blank=True)
    direccion = models.CharField(max_length=50, blank=True)


    auto = models.ForeignKey(Automovil, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nombre

class Tarifa (models.Model):
    nombreTarifa = models.CharField(max_length=30, blank=True)
    precioTarifa = models.DecimalField(decimal_places=2, max_digits=5, blank=True)
    descripcionTarifa = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.nombreTarifa


class AutoEspacio (models.Model):
    auto = models.ForeignKey(Automovil, on_delete=models.CASCADE, blank=True, null=True)
    espacio = models.ForeignKey(EspacioEstacionamiento, on_delete=models.CASCADE, blank=True, null=True)
    tarifa = models.ForeignKey(Tarifa,  on_delete=models.CASCADE, blank=True, null=True)
    horaIngreso = models.DateField(datetime.now(), blank=True, null=True)

    def __str__(self):
        return self.auto.placa




