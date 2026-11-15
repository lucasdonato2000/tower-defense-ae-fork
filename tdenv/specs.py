"""Tabla de torres del fork. Un solo lugar define costos y comportamiento.

cost          = (dinero, recurso 1, recurso 2)
range_tiles   = alcance en casillas (la casilla mide TILE_PX pixeles)
cooldown      = milisegundos entre disparos
bullet_speed  = velocidad de la bala
power         = tipo maximo de enemigo que la bala elimina (enemy.type <= power)
splash_tiles  = radio de dano en area en casillas (0 = golpea un solo enemigo)

Las 3 primeras reproducen exactamente el juego original. Con TD_TOWERS=3 (default)
el fork se comporta igual que el paquete original; TD_TOWERS=5 habilita las nuevas.
Los valores de las torres 3 y 4 son iniciales, para calibrar.
"""
import os

ALL_TOWERS = [
    # 0, 1, 2: originales
    dict(cost=(5, 0, 0),    range_tiles=2.5, cooldown=800,  bullet_speed=3.2, power=0, splash_tiles=0.0),
    dict(cost=(5, 5, 0),    range_tiles=2.5, cooldown=600,  bullet_speed=3.2, power=1, splash_tiles=0.0),
    dict(cost=(10, 10, 10), range_tiles=2.5, cooldown=500,  bullet_speed=3.2, power=2, splash_tiles=0.0),
    # 3: largo alcance (dispara lento, mata hasta tipo 2)
    dict(cost=(12, 8, 4),   range_tiles=4.5, cooldown=800, bullet_speed=3.2, power=2, splash_tiles=0.0),
    # 4: area (mata todo enemigo de tipo <= 1 dentro del radio del impacto)
    dict(cost=(8, 6, 0),    range_tiles=2.5, cooldown=1000, bullet_speed=3.2, power=1, splash_tiles=1.5),
]

N_TOWERS = int(os.environ.get("TD_TOWERS", "3"))
TOWER_SPECS = ALL_TOWERS[:N_TOWERS]

# En el tablero: 0 camino, 1 libre, 2.. torres, luego fabricas (original: torres 2-4, fabricas 5-6)
FACTORY_BOARD_BASE = 2 + len(TOWER_SPECS)
