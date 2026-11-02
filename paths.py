"""Rutas de los archivos de instancia (mapa y oleadas). Se pueden redirigir con
TD_BOARD_FILE y TD_WAVE_FILE. Vive aparte de config.py para que los generadores
de mapas y oleadas no necesiten un mapa valido ya cargado para importarse."""
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data")
CURRENT_BOARD_FILE = os.environ.get("TD_BOARD_FILE") or os.path.join(DATA_PATH, "board_test_random.txt")
CURRENT_WAVE_FILE = os.environ.get("TD_WAVE_FILE") or os.path.join(DATA_PATH, "wave_test_random.txt")
