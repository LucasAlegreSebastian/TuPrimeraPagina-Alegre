# combate/urls.py

from django.urls import path
from . import views

app_name = "combate"

urlpatterns = [
    path("", views.seleccionar_mi_pokemon, name="seleccionar_mi_pokemon"),
    path(
        "elegir-oponente/<int:pokemon_usuario_id>/",
        views.elegir_oponente,
        name="elegir_oponente",
    ),
    path(
        "iniciar/<int:pokemon_usuario_id>/<str:pokemon_oponente_id>/",
        views.iniciar_combate,
        name="iniciar",
    ),
    path("historial/", views.historial_combates_general, name="historial_general"),
    path("mi-historial/", views.historial_combates_usuario, name="historial_usuario"),
    path(
        "iniciar/<int:pokemon_usuario_id>/<str:pokemon_oponente_id>/",
        views.iniciar_combate,
        name="iniciar",
    ),
    path("turno/", views.manejar_turno, name="turno"),
    path("final/", views.finalizar_combate, name="finalizar_combate"),
]
