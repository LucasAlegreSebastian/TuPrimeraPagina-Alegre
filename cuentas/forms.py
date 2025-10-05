from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from pokedex.models import Pokemon


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    pokemon_favorito = forms.ModelChoiceField(
        queryset=Pokemon.objects.all(), required=False
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1940, 2030))
    )

    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "pokemon_favorito",
            "fecha_nacimiento",
            "password1",
            "password2",
        ]
