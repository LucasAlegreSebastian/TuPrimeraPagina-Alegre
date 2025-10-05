from django.contrib.auth.models import AbstractUser
from django.db import models
from pokedex.models import Pokemon


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    pokemon_favorito = models.ForeignKey(
        Pokemon, on_delete=models.SET_NULL, null=True, blank=True
    )
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Nombre usuario : {self.username} - Nombre y apellido: {self.first_name} {self.last_name}"
