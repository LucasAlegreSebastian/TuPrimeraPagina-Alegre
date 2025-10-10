# Create your models here.
from django.db import models
from cuentas.models import Usuario
from pokedex.models import Pokemon


class Combate(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name="combates_iniciados")
    pokemon_usuario = models.ForeignKey(
        Pokemon, related_name="pokemon_usuario", on_delete=models.CASCADE
    )

    usuario_enemigo = models.ForeignKey(
        Usuario, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name="combates_recibidos" 
    )

    pokemon_enemigo = models.ForeignKey(
        Pokemon, related_name="pokemon_enemigo", on_delete=models.CASCADE
    )
    resultado = models.CharField(max_length=10)  # victoria,derrota
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        oponente_str = self.usuario_enemigo.username if self.usuario_enemigo else self.pokemon_enemigo.nombre
        return f"{self.usuario.username} vs {oponente_str} ({self.resultado})"
