# Create your models here.
from django.db import models
from cuentas.models import Usuario
from pokedex.models import Pokemon


class Combate(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pokemon_usuario = models.ForeignKey(
        Pokemon, related_name="pokemon_usuario", on_delete=models.CASCADE
    )
    pokemon_enemigo = models.ForeignKey(
        Pokemon, related_name="pokemon_enemigo", on_delete=models.CASCADE
    )
    resultado = models.CharField(max_length=10)  # victoria,derrota,empate
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} vs {self.pokemon_enemigo.nombre} ({self.resultado})"
