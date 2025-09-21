from django import forms
from .models import Pokemon, Entrenador, Gimnasio, Pokebola


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["numero", "nombre", "tipo", "habilidad", "debilidad"]


class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ["nombre", "region"]


class GimnasioForm(forms.ModelForm):
    class Meta:
        model = Gimnasio
        fields = ["nombre", "ciudad", "lider"]


class PokebolaForm(forms.ModelForm):
    class Meta:
        model = Pokebola
        fields = ["nombre", "descripcion"]
