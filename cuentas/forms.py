from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from pokedex.models import Pokemon


class EditProfileForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ("email", "first_name", "last_name", "password")
        labels = {
            "email": "Correo Electrónico",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField()
    pokemon_favorito = forms.ModelChoiceField(
        queryset=Pokemon.objects.all(), required=False
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        label="Fecha de nacimiento",
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
