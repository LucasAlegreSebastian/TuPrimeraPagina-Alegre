from django.urls import path
from . import views

app_name = "pokedex"
urlpatterns = [
    path("pokedex/Lista_pokemon", views.poke_list, name="list_pokemon"),
    path("pokedex/Crear_Pokemon", views.poke_crear, name="crear_pokemon"),
    path("pokedex/Lista_Entrenadores", views.entrenador_list, name="list_entrenador"),
    path("pokedex/Crear_Entrenador", views.entrenador_crear, name="crear_entrenador"),
]
