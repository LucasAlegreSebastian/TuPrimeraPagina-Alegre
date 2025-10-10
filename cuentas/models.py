from django.contrib.auth.models import AbstractUser
from django.db import models
from pokedex.models import Pokemon


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    pokemon_favorito = models.ForeignKey(
        Pokemon, on_delete=models.SET_NULL, null=True, blank=True
    )
    fecha_nacimiento = models.DateField(blank=True, null=True)

    # Contadores de combates
    combates_jugados = models.PositiveIntegerField(default=0)
    combates_ganados = models.PositiveIntegerField(default=0)
    combates_perdidos = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f"Nombre usuario: {self.username} - Nombre y apellido: {self.first_name} {self.last_name}"

    def registrar_resultado(self, resultado):
        """
        Para guardar informacion de los combates (Victoria,Derrota,Empate)
        """
        self.combates_jugados += 1
        if resultado == "Victoria":
            self.combates_ganados += 1
        elif resultado == "Derrota":
            self.combates_perdidos += 1
        self.save()


class Avatar(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"
