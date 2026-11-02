"""Tamano del tablero del fork. Se define una sola vez por proceso con la variable
de entorno TD_TILE_COUNT (default 10 = juego original).

La casilla mide siempre TILE_PX pixeles: velocidades, hitboxes y alcances del juego
estan en pixeles, asi que un tablero mas grande solo agranda la pantalla logica
y conserva el equilibrio del juego original.
"""
import os

TILE_COUNT = int(os.environ.get("TD_TILE_COUNT", "10"))
TILE_PX = 70
LAST = TILE_COUNT - 1          # indice de la ultima fila/columna (borde)
SCREEN_WIDTH = TILE_PX * TILE_COUNT + 300
SCREEN_HEIGHT = max(800, TILE_PX * TILE_COUNT + 40)
