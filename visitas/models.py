
from django.db import models
from django.shortcuts import render

class Jardinero(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    cliente_nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    tipo_servicio = models.CharField(max_length=100)
    disponibilidad = models.CharField(max_length=100)
    metros_cuadrados = models.FloatField()
    jardinero = models.ForeignKey(Jardinero, on_delete=models.SET_NULL, null=True, blank=True)
    confirmado = models.BooleanField(default=False)
    hora_confirmada = models.DateTimeField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.cliente_nombre} - {self.direccion}"



