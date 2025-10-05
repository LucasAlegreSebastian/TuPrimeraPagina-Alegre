from django.urls import path
from . import views

app_name = "pokedex"
urlpatterns = [
    path("Lista_pokemon", views.poke_list, name="list_pokemon"),
    path("Crear_Pokemon", views.poke_crear, name="crear_pokemon"),
    path("Lista_Entrenadores", views.entrenador_list, name="list_entrenador"),
    path("Crear_Entrenador", views.entrenador_crear, name="crear_entrenador"),
    path("Lista_Gimnasios", views.gimnasios_list, name="list_gimnasios"),
    path("Crear_Gimnasios", views.gimnasio_crear, name="crear_gimnasios"),
    path("Lista_Pokebolas", views.pokebolas_list, name="list_pokebolas"),
    path("Crear_Pokebolas", views.pokebola_crear, name="crear_pokebolas"),
]
