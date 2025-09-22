from django.contrib import admin

# Register your models here.
from .models import Pokemon, Entrenador, Gimnasio, Pokebola

# admin.site.register(Pokemon)
# admin.site.register(Entrenador)
# admin.site.register(Gimnasio)
# admin.site.register(Pokebola)


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ["numero", "nombre", "tipo", "debilidad", "habilidad"]
    list_filter = ["tipo", "debilidad"]
    ordering = ["numero"]


@admin.register(Entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "region"]


@admin.register(Gimnasio)
class GimnasioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "ciudad", "lider"]


@admin.register(Pokebola)
class PokebolaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
