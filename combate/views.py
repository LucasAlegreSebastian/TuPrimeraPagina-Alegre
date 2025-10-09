# combate/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pokedex.models import Pokemon
from .models import Combate
from .utils import calcular_resultado


@login_required
def seleccionar_mi_pokemon(request):
    """
    Paso 1: El usuario elige con qué Pokémon va a luchar.
    El favorito viene pre-seleccionado por defecto.
    """
    usuario = request.user
    pokemones = Pokemon.objects.all()

    if request.method == "POST":
        pokemon_usuario_id = request.POST.get("pokemon_id")
        # Pasamos el ID del pokémon elegido a la siguiente vista
        return redirect(
            "combate:elegir_oponente", pokemon_usuario_id=pokemon_usuario_id
        )

    return render(
        request,
        "combate/seleccionar_mi_pokemon.html",
        {
            "pokemones": pokemones,
            # Pasamos el ID del favorito para marcarlo en la plantilla
            "pokemon_favorito_id": (
                usuario.pokemon_favorito.id if usuario.pokemon_favorito else None
            ),
        },
    )


@login_required
def elegir_oponente(request, pokemon_usuario_id):
    """
    Paso 2: El usuario elige al oponente.
    Muestra el Pokémon que eligió en el paso anterior.
    """
    pokemon_usuario = Pokemon.objects.get(id=pokemon_usuario_id)

    # Excluimos el pokémon del usuario de la lista de posibles oponentes
    pokemones_oponentes = Pokemon.objects.exclude(id=pokemon_usuario_id)

    if request.method == "POST":
        pokemon_oponente_id = request.POST.get("oponente_id")
        return redirect(
            "combate:iniciar",
            pokemon_usuario_id=pokemon_usuario_id,
            pokemon_oponente_id=pokemon_oponente_id,
        )

    return render(
        request,
        "combate/elegir_oponente.html",
        {
            "pokemon_usuario": pokemon_usuario,
            "pokemones_oponentes": pokemones_oponentes,
        },
    )


@login_required
def iniciar_combate(request, pokemon_usuario_id, pokemon_oponente_id):
    """
    Paso 3: Se realiza el combate y se muestra el resultado.
    """
    usuario = request.user
    pokemon_usuario = Pokemon.objects.get(id=pokemon_usuario_id)

    if pokemon_oponente_id == "random":
        pokemon_enemigo = (
            Pokemon.objects.exclude(id=pokemon_usuario_id).order_by("?").first()
        )
    else:
        pokemon_enemigo = Pokemon.objects.get(id=pokemon_oponente_id)

    if not pokemon_enemigo:
        return render(
            request,
            "combate/error.html",
            {"mensaje": "No se pudo encontrar un oponente."},
        )

    resultado = calcular_resultado(pokemon_usuario, pokemon_enemigo)

    Combate.objects.create(
        usuario=usuario,
        pokemon_usuario=pokemon_usuario,
        pokemon_enemigo=pokemon_enemigo,
        resultado=resultado,
    )

    # Actualizamos las estadísticas del usuario
    usuario.registrar_resultado(resultado)

    return render(
        request,
        "combate/batalla.html",
        {
            "pokemon_usuario": pokemon_usuario,
            "pokemon_enemigo": pokemon_enemigo,
            "resultado": resultado,
        },
    )
