from gymnasium.envs.registration import register, registry

ENV_ID = "TDFork-v0"

if ENV_ID not in registry:
    register(
        id=ENV_ID,
        entry_point="tdenv.environment:TowerDefenseEnv"
    )

__all__ = ["TowerDefenseEnv"]


def __getattr__(name):
    # import perezoso: el entorno carga un mapa al importarse y los generadores
    # de instancias (map_maker, wave_maker) deben poder usarse antes de que exista uno
    if name == "TowerDefenseEnv":
        from .environment import TowerDefenseEnv
        return TowerDefenseEnv
    raise AttributeError(name)
