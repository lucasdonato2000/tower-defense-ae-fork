# Fork para Algoritmos Evolutivos (FING, UdelaR)

Fork de [mDermek94/BP-tower-defense](https://github.com/mDermek94/BP-tower-defense) (licencia MIT, (c) 2026 Maximilian Dermek)
hecho para un trabajo del curso Algoritmos Evolutivos. El juego y el entorno originales se conservan: con tablero de 10 x 10 y
3 torres el entorno da exactamente los mismos resultados que el original (verificado con 100 individuos aleatorios contra el
paquete `dermek-bp-tower-defense-env` 0.1.5).

## Cambios respecto al original
- **Tablero de tamano parametrizable** (`size.py`): variable de entorno `TD_TILE_COUNT` (por defecto 10). La casilla mide siempre
  70 px, asi que un tablero mayor solo agranda la pantalla logica y no altera el equilibrio entre alcance y velocidad.
- **Torres definidas por tabla** (`specs.py`): `TD_TOWERS` elige cuantas (3 = original, 5 = con las nuevas). Torre 3: largo alcance
  (4.5 casillas, cadencia 800, poder 2, costo 12/8/4). Torre 4: dano en area (radio 1.5 casillas, cadencia 1000, poder 1,
  costo 8/6/0). Un impacto con area elimina a todos los enemigos de tipo <= poder dentro del radio.
- **Generador de mapas sin ventana**: `map_maker.generate_map(seed, difficulty)` (antes solo corria dentro del bucle de pygame).
- **Mapa y oleadas por archivo** (`paths.py`): `TD_BOARD_FILE` y `TD_WAVE_FILE`.
- Archivos modificados: `bullet.py`, `config.py`, `environment.py`, `game_logic.py`, `map_maker.py`, `tower.py`, `wave_maker.py`;
  nuevos: `size.py`, `paths.py`, `specs.py`. `main.py` y `test.py` no se tocaron.

## Uso del entorno con otro tamano
La configuracion se lee al importar los modulos, por lo que es una por proceso y debe definirse antes del `import`.
```python
import os
os.environ["TD_TILE_COUNT"] = "20"
os.environ["TD_TOWERS"] = "5"
os.environ["TD_BOARD_FILE"] = "board.txt"
os.environ["TD_WAVE_FILE"] = "waves.txt"
from environment import TowerDefenseEnv
env = TowerDefenseEnv(render_mode="dictionary")
obs, _ = env.reset(seed=0)
env.step([2, 0, 0, 0])   # [accion, subtipo, x, y]: 0 = torre, 1 = fabrica, 2 = iniciar oleada
```
Para generar un mapa y oleadas sin ventana (con `TD_TILE_COUNT` definido):
```python
import random, map_maker, wave_maker
board, home, spawn, _ = map_maker.generate_map(seed=1, difficulty=10)
map_maker.save_board(board, home, spawn, path="board.txt")
random.seed(1)
game = wave_maker.generate_game(10, 20)
open("waves.txt", "w").write("\n".join(",".join(f"{n}x{t}" for n, t in w["groups"]) for w in game))
```

---

# Tower defense game and Gymnasium environment

This repository contains the source code for my bachelor's thesis project, which is a deterministic tower defense game and Gymnasium environment focused on long-term planning.

The project is split into two main Python packages:

1. `dermek-bp-tower-defense-env`
    A Gymnasium-compatible reinforcement learning environment with shared game logic, procedural map generation, procedural wave generation, default data files and command-line tools.

2. `dermek-bp-tower-defense`
    A playable tower defense game application build on top of the environment package.

The goal of the project is to provide a game environment where decisions have delayed consequences, the agent or player must manage limited resources, build towers and factories, and prepare for future enemy waves.

---

## Repository structure

```text
BP-TOWER-DEFENSE
├──assets
│    └──Sprites
│         ├──Factories          - Factory sprites
│         └──Towers             - Tower sprites
├──data
│    ├──board_test_random.txt   - Current saved board file
│    └──wave_test_random.txt    - Current saved wave file
├──bullet.py                    - Bullet class definition
├──config.py                    - Config file with default values
├──enemy.py                     - Enemy class definition
├──environment.py               - Gymnasium environment
├──factory.py                   - Factory class definition
├──game_logic.py                - Shared game logic functions for the main game loop
├──main.py                      - Main file with user functionality and agent demo
├──map_maker.py                 - Procedural map generator
├──test.py                      - Showcase of how the environment can run on its own
├──tower.py                     - Tower class definition
└──wave_maker.py                - Procedural wave generator
```

## Packages
### Environment package
Package name:
```text
install dermek-bp-tower-defense-env
```

Import name:
```python
import dermek_bp_tower_defense_env
```

This package contains the reinforcement learning environment and the core systems used by the game, as well as the map and wave generators.

It includes:
- Gymnasium environment registration
- dictionary-based observation space
- `MultiDiscrete` action space
- deterministic game logic
- procedural map generator
- procedural wave generator
- default map and wave data
- Pygame rendering mode
- command-line tools for generating maps and waves

The environment can be created directly through Gymnasium like this:
```python
import gymnasium as gym
import dermek_bp_tower_defense_env

env = gym.make("DermekBPTowerDefense-v0", render_mode="dictionary")
```
The import of `dermek_bp_tower_defense_env` registers the environment with Gymnasium.

#### Command-line tools:
Map generator command:
```bash
tower-defense-map-maker --difficulty 10 --seed 42
```
Command arguments:
- `-h`: print available arguments with descrptions
- `--seed`: choose a seed for randomness, if not included, chooses a random seed
- `--difficulty`: choose a difficulty value, required argument, gets clamped to <1;20>

Wave generator command:
```bash
tower-defense-wave-maker --difficulty 10 --num-waves 20 --seed 42
```
Command arguments:
- `-h`: print available arguments with descrptions
- `--seed`: choose a seed for randomness, if not included, chooses a random seed
- `--difficulty`: choose a difficulty value, required argument
- `--num-waves`: choose the number of waves to generate, required argument

Render modes:
- `human`: uses pygame to render a window and show the full game process
- `dictionary`: runs without any visual input and is thus much faster than the other rendermode, intended for reinforcement learning

### Game package
Package name:
```text
dermek-bp-tower-defense
```
This package depends on the environment package. It contains the main playable application, as well as a simple demonstration of the environment using `action_space.sample()`.

Commands:

To run the game in a human-playable mode:
```bash
tower-defense
```
To run the environment demonstration:
 ```bash
 tower-defense --gymnasium --seed 42
 ```
 Command arguments:
 - `-h`: print available arguments with descrptions
- `--gymnasium`: optional argument, runs the environment demonstration 
 - `--seed`: optional argument controlling the action space sampling seed

### PyPI installation
Install the playable game package:
```bash
pip install dermek-bp-tower-defense
```
This also installs the environment package as a dependency.

Alternatively, install only the environment package:
```bash
pip install dermek-bp-tower-defense-env
```

Use the environment package if you are interested mainly in reinforcement learning experiments.

#### Using a virtual environment is recommended when installing either package.

### Running the code from the repository
Clone the repository and simply run the files using python. Example:
```bash
python main.py
```

Runnable files include:
- `main.py`: accepts `--gymnasium` and `--seed`, containts the main playable game and environment demonstration
- `map_maker.py`: accepts `--difficulty` and `--seed`, runs the map generator
- `wave_maker.py`: accepts `--difficulty`, `--num-waves` and `--seed`, runs the wave generator

### Basic Gymnasium usage
When using the installed packages:
```python
import gymnasium as gym
import dermek_bp_tower_defense_env

env = gym.make("DermekBPTowerDefense-v0", render_mode="dictionary")

obs, info = env.reset(seed=42)

terminated = False
truncated = False

while not (terminated or truncated):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)

env.close()
```

## Game overview
The project implements a deterministic single-player tower defense game.

The game is played on a grid-based map. Some tiles form the enemy path, while other tiles can be used to place buildings.

The player or agent can build:
- towers, which attack enemies
- factories, which produce resources

The game contains:
- three tower types
- three enemy types
- three resource types
- two factory types
- procedural maps
- procedural enemy waves

The main planning challenge is deciding how to use the limited resources and limited building space. The player or agent must choose between immediate defense and long-term resource production.

## Long-term planning focus
Planning is encouraged through:
- delayed consequences of building decisions
- limited resources
- limited buildable space
- irreversible building placement
- factories that provide delayed benefits
- future enemy waves that require preparation

## Reproducibility
The project supports reproducibility through seed values.

Seeds can be used for:
- map generation
- wave generation
- random action sampling

To perform a full repeatable experiment:
- run the wave generator with a set `--difficulty`, a set `--num-waves`, and a set `--seed`
- run the map generator with a set `--difficulty` and a set `--seed`, then generate a map and save it using the user keys
- run the game in either a human mode with the generated map and wave structure, or run the game using `--gymnasium` and a set `--seed` value for a reproducible agent

To save an experiment configuration, keep track of all the `--seed` and `--difficulty` values for each file, including `--num-waves` for the wave generator. Note that the map file and the wave file are always overwritten with the last generated instance and the current only way to save maps or waves is to remember the argument parameters.

## Author
Maximilián Dermek

Bachelor thesis project at the Faculty of Informatics and Information Technologies, Slovak University of Technology in Bratislava.