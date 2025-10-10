# combate/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pokedex.models import Pokemon
from .models import Combate
from .utils import calcular_resultado
from cuentas.models import Usuario
import random


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
    # Lista de usuarios registrados
    usuarios_oponentes = Usuario.objects.exclude(id=request.user.id)
    usuarios_oponentes = usuarios_oponentes.filter(is_superuser=False)

    if request.method == "POST":

        oponente_tipo = request.POST.get("oponente_tipo")
        oponente_id = request.POST.get("oponente_id")

        if oponente_tipo == "usuario":
            oponente_id = f"user_{oponente_id}"
        else:
            oponente_id = oponente_id

        return redirect(
            "combate:iniciar",
            pokemon_usuario_id=pokemon_usuario_id,
            pokemon_oponente_id=oponente_id,
        )

    return render(
        request,
        "combate/elegir_oponente.html",
        {
            "pokemon_usuario": pokemon_usuario,
            "pokemones_oponentes": pokemones_oponentes,
            "usuarios_oponentes": usuarios_oponentes,
        },
    )


@login_required
def iniciar_combate(request, pokemon_usuario_id, pokemon_oponente_id):
    """
    INICIO: Prepara el combate, calcula el enemigo y guarda el estado inicial en la sesión.
    """
    usuario = request.user
    pokemon_usuario = Pokemon.objects.get(id=pokemon_usuario_id)

    usuario_enemigo = None
    if pokemon_oponente_id == "random":
        pokemon_enemigo = (
            Pokemon.objects.exclude(id=pokemon_usuario_id).order_by("?").first()
        )
    elif pokemon_oponente_id.startswith("user_"):
        usuario_enemigo_id = pokemon_oponente_id.split("_")[1]
        try:
            usuario_enemigo = Usuario.objects.get(id=usuario_enemigo_id)
            pokemon_enemigo = usuario_enemigo.pokemon_favorito
        except (Usuario.DoesNotExist, Pokemon.DoesNotExist):
            return redirect("combate:seleccionar_mi_pokemon")
    else:
        pokemon_enemigo = Pokemon.objects.get(id=pokemon_oponente_id)

    # Combate
    request.session["combate_actual"] = {
        "usuario_id": usuario.id,
        "pokemon_usuario_id": pokemon_usuario.id,
        "pokemon_enemigo_id": pokemon_enemigo.id,
        "hp_usuario": 100,
        "hp_enemigo": 100,
        "turno_actual": 0,
        "max_turnos": 3,
        "log_turnos": [],
        "usuario_enemigo_id": usuario_enemigo.id if usuario_enemigo else None,
    }

    return redirect("combate:turno")


def historial_combates_general(request):
    """
    Vista que muestra todos los combates registrados en la página.
    """
    combates = Combate.objects.all().order_by("-fecha")

    return render(
        request,
        "combate/historial_general.html",
        {
            "combates": combates,
            "titulo": "Historial de Todos los Combates",
        },
    )


@login_required
def historial_combates_usuario(request):
    """
    Vista que muestra solo los combates en los que participó el usuario logueado.
    """
    usuario_actual = request.user

    combates = Combate.objects.filter(usuario=usuario_actual).order_by("-fecha")

    return render(
        request,
        "combate/historial_usuario.html",
        {
            "combates": combates,
            "titulo": f"Mis Combates ({usuario_actual.username})",
        },
    )


@login_required
def manejar_turno(request):
    """
    Procesa un turno de combate o finaliza la batalla.
    """

    estado = request.session.get("combate_actual")
    if not estado:
        return redirect("combate:seleccionar_mi_pokemon")

    pokemon_usuario = Pokemon.objects.get(id=estado["pokemon_usuario_id"])
    pokemon_enemigo = Pokemon.objects.get(id=estado["pokemon_enemigo_id"])

    if request.method == "POST" and estado["turno_actual"] < estado["max_turnos"]:

        estado["turno_actual"] += 1

        MIN_DANO = 20
        MAX_DANO = 40

        dano_u = random.randint(MIN_DANO, MAX_DANO)
        estado["hp_enemigo"] -= dano_u

        log_turno = f"{pokemon_usuario.nombre} ataca. Daño: {dano_u}."

        if estado["hp_enemigo"] <= 0:
            resultado = "Victoria"
        else:
            dano_e = random.randint(MIN_DANO, MAX_DANO)
            estado["hp_usuario"] -= dano_e

            log_turno += f" | {pokemon_enemigo.nombre} ataca. Daño: {dano_e}."

            if estado["hp_usuario"] <= 0:
                resultado = "Derrota"
            else:
                resultado = None

        estado["log_turnos"].append(log_turno)

        request.session["combate_actual"] = estado
        request.session.modified = True

        if resultado or estado["turno_actual"] == estado["max_turnos"]:
            return redirect("combate:finalizar_combate")

    return render(
        request,
        "combate/batalla_turno.html",
        {
            "pokemon_usuario": pokemon_usuario,
            "pokemon_enemigo": pokemon_enemigo,
            "estado": estado,
        },
    )


@login_required
def finalizar_combate(request):
    estado = request.session.pop("combate_actual", None)

    if not estado:
        return redirect("combate:seleccionar_mi_pokemon")

    pokemon_usuario = Pokemon.objects.get(id=estado["pokemon_usuario_id"])
    pokemon_enemigo = Pokemon.objects.get(id=estado["pokemon_enemigo_id"])

    hp_final_usuario = max(0, estado["hp_usuario"])
    hp_final_enemigo = max(0, estado["hp_enemigo"])

    if hp_final_usuario > hp_final_enemigo:
        resultado = "Victoria"
    elif hp_final_enemigo > hp_final_usuario:
        resultado = "Derrota"
    else:
        resultado = "Empate"

    usuario = request.user
    usuario.registrar_resultado(resultado)

    usuario_enemigo = None
    if estado["usuario_enemigo_id"]:
        try:
            usuario_enemigo = Usuario.objects.get(id=estado["usuario_enemigo_id"])
        except Usuario.DoesNotExist:
            pass 

    Combate.objects.create(
        usuario=usuario,
        usuario_enemigo=usuario_enemigo,
        pokemon_usuario=pokemon_usuario,
        pokemon_enemigo=pokemon_enemigo,
        resultado=resultado,
    )

    if usuario_enemigo:
        if resultado == "Victoria":
            resultado_enemigo = "Derrota"
        elif resultado == "Derrota":
            resultado_enemigo = "Victoria"
        else:
            resultado_enemigo = "Empate"

        Combate.objects.create(
            usuario=usuario_enemigo,
            usuario_enemigo=usuario, 
            pokemon_usuario=pokemon_enemigo,
            pokemon_enemigo=pokemon_usuario,
            resultado=resultado_enemigo,
        )
        usuario_enemigo.registrar_resultado(resultado_enemigo)
    
    return render(
        request,
        "combate/batalla_final.html",
        {
            "pokemon_usuario": pokemon_usuario,
            "pokemon_enemigo": pokemon_enemigo,
            "resultado": resultado,
            "log_turnos": estado["log_turnos"],
            "hp_final_usuario": hp_final_usuario,
            "hp_final_enemigo": hp_final_enemigo,
        },
    )