import random

def calcular_resultado(pokemon_usuario, pokemon_enemigo):
    """
    Simula un combate de 3 turnos con 100 HP, daño aleatorio.
    Devuelve el resultado del combate ("Victoria","Derrota").
    """
    
    hp_usuario = 100
    hp_enemigo = 100
    max_turnos = 3
    
    MIN_DANO = 20
    MAX_DANO = 40
    
    for turno in range(1, max_turnos + 1):
        
        dano_usuario = random.randint(MIN_DANO, MAX_DANO)
        hp_enemigo -= dano_usuario
        
        if hp_enemigo <= 0:
            return "Victoria"
        
        dano_enemigo = random.randint(MIN_DANO, MAX_DANO)
        hp_usuario -= dano_enemigo

        if hp_usuario <= 0:
            return "Derrota"

    if hp_usuario > hp_enemigo:
        return "Victoria"
    elif hp_enemigo > hp_usuario:
        return "Derrota"
    