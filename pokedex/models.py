from django.db import models


# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField(unique=True)
    tipo = models.CharField(max_length=30)
    debilidad = models.CharField(max_length=30)

    ataque1 = models.CharField(max_length=50)
    ataque2 = models.CharField(max_length=50)

    imagen_frente = models.ImageField(upload_to="pokemones/", blank=True, null=True)
    imagen_espalda = models.ImageField(upload_to="pokemones/", blank=True, null=True)

    def __str__(self):
        return f"{self.numero} - {self.nombre}"


class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="entrenadores/", blank=True, null=True)

    def __str__(self):
        return f"Entrenador {self.nombre} de la Región : {self.region}"


class Gimnasio(models.Model):
    
    ciudad = models.CharField(max_length=100)
    lider = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="gimnasios/", blank=True, null=True)

    def __str__(self):
        return f"El gimnasio {self.nombre} es de la ciudad {self.ciudad} y el Lider es : {self.lider}"


class Pokebola(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="pokebolas/", blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - Descripción: {self.descripcion}"
