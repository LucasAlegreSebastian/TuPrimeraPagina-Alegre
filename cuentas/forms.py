from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .models import Usuario
from pokedex.models import Pokemon


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "pokemon_favorito",
            "fecha_nacimiento",
        )
        labels = {
            "username": "Nombre de usuario",
            "email": "Correo Electrónico",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "pokemon_favorito": "Pokémon favorito",
            "fecha_nacimiento": "Fecha de nacimiento",
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
