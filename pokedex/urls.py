from django.urls import path
from . import views
from .views import PokemonCreateView, PokemonDetailView, PokemonUpdateView

app_name = "pokedex"
urlpatterns = [
    path("Lista_pokemon", views.poke_list, name="list_pokemon"),
    path("Crear_Pokemon", PokemonCreateView.as_view(), name="crear_pokemon"),
    path("<int:pk>/", PokemonDetailView.as_view(), name="detalle_pokemon"),
    path(
        "<int:pk>/pokemon_editar/", PokemonUpdateView.as_view(), name="editar_pokemon"
    ),
    path("Lista_Entrenadores", views.entrenador_list, name="list_entrenador"),
    path("Crear_Entrenador", views.entrenador_crear, name="crear_entrenador"),
    path("Lista_Gimnasios", views.gimnasios_list, name="list_gimnasios"),
    path("Crear_Gimnasios", views.gimnasio_crear, name="crear_gimnasios"),
    path("Lista_Pokebolas", views.pokebolas_list, name="list_pokebolas"),
    path("Crear_Pokebolas", views.pokebola_crear, name="crear_pokebolas"),
]
