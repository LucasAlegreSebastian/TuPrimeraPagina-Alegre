import random


def calcular_resultado(pokemon_usuario, pokemon_enemigo):
    efectividad = 1.0
    relaciones = {
        "fuego": {"fuerte": "planta", "debil": "agua"},
        "agua": {"fuerte": "fuego", "debil": "planta"},
        "planta": {"fuerte": "agua", "debil": "fuego"},
        "eléctrico": {"fuerte": "agua", "debil": "tierra"},
    }

    tipo_u = pokemon_usuario.tipo.lower()
    tipo_e = pokemon_enemigo.tipo.lower()

    if tipo_u in relaciones:
        if tipo_e == relaciones[tipo_u]["fuerte"]:
            efectividad = 2.0
        elif tipo_e == relaciones[tipo_u]["debil"]:
            efectividad = 0.5

    daño = random.randint(10, 30) * efectividad
    return "Ganaste" if daño >= 20 else "Perdiste"
