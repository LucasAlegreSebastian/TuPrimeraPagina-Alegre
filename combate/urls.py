# combate/urls.py

from django.urls import path
from . import views

app_name = "combate"

urlpatterns = [
    # Paso 1: El usuario elige SU pokémon. Esta es la nueva URL de inicio.
    path("", views.seleccionar_mi_pokemon, name="seleccionar_mi_pokemon"),
    # Paso 2: Elige al oponente, pasando el ID de su pokémon en la URL.
    path(
        "elegir-oponente/<int:pokemon_usuario_id>/",
        views.elegir_oponente,
        name="elegir_oponente",
    ),
    # Paso 3: Inicia el combate con ambos IDs en la URL.
    path(
        "iniciar/<int:pokemon_usuario_id>/<str:pokemon_oponente_id>/",
        views.iniciar_combate,
        name="iniciar",
    ),
]
