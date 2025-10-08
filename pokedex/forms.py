from django import forms
from .models import Pokemon, Entrenador, Gimnasio, Pokebola

POKEMON_TIPOS = [
    ("Planta 🌱", "Planta 🌱"),
    ("Fuego 🔥", "Fuego 🔥"),
    ("Agua 💧", "Agua 💧"),
    ("Eléctrico ⚡", "Eléctrico ⚡"),
    ("Hielo ❄️", "Hielo ❄️"),
    ("Lucha 🥊", "Lucha 🥊"),
    ("Veneno ☠️", "Veneno ☠️"),
    ("Tierra 🌍", "Tierra 🌍"),
    ("Volador 🕊️", "Volador 🕊️"),
    ("Psíquico 🧠", "Psíquico 🧠"),
    ("Bicho 🐛", "Bicho 🐛"),
    ("Roca 🪨", "Roca 🪨"),
    ("Fantasma 👻", "Fantasma 👻"),
    ("Dragón 🐉", "Dragón 🐉"),
    ("Siniestro 🌑", "Siniestro 🌑"),
    ("Acero ⚙️", "Acero ⚙️"),
    ("Hada ✨", "Hada ✨"),
]


class PokemonForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=POKEMON_TIPOS, label="Tipo")

    class Meta:
        model = Pokemon
        fields = [
            "numero",
            "nombre",
            "tipo",
            "ataque1",
            "ataque2",
            "debilidad",
            "imagen_frente",
            "imagen_espalda",
        ]


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
