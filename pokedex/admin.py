from django.contrib import admin

# Register your models here.
from .models import Pokemon, Entrenador, Gimnasio, Pokebola

admin.site.register(Pokemon)
admin.site.register(Entrenador)
admin.site.register(Gimnasio)
admin.site.register(Pokebola)
