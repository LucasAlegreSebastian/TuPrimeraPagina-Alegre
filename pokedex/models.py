from django.db import models


# Create your models here.
class Pokemon(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)
    habilidad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    debilidad = models.CharField(max_length=100)

    def __str__(self):
        return f"#{self.numero} Nombre: {self.nombre} - Habilidad : {self.habilidad} - Tipo: {self.tipo} - Debilidad : {self.debilidad}"


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"Entrenador {self.nombre} de la Región : {self.region}"


class Gimnasio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    nombre_lider = models.CharField(max_length=100)

    def __str__(self):
        return f"El gimnasio {self.nombre} es de la ciudad {self.ciudad} y el Lider es : {self.nombre_lider}"

class Pokebola(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - Descripción: {self.descripcion}"