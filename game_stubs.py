"""
Stub file for The Farmer Was Replaced.

This file exists ONLY so VS Code / Pylance stops showing errors for the
game's built-in functions and constants (they don't exist in real Python,
so the game injects them at runtime when your script is copy-pasted in).

How to use:
1. Drop this file in the same folder as your farming scripts.
2. Add a `.vscode/settings.json` (or pyrightconfig.json) next to it with:
    {
        "python.analysis.extraPaths": ["."],
        "python.analysis.typeCheckingMode": "off"
    }
3. Do NOT paste this file's contents into the game - it's only for the
   editor. The game already provides these at runtime.
"""

from typing import Any, Optional

# ---- Directions ----
North: Any
South: Any
East: Any
West: Any


# ---- Enums (exact members vary by game version/unlocks - add as needed) ----
class Entities:
    Grass: Any
    Bush: Any
    Tree: Any
    Carrot: Any
    Pumpkin: Any
    Sunflower: Any
    Cactus: Any
    Dinosaur: Any
    Weed: Any


class Grounds:
    Grassland: Any
    Soil: Any
    Water: Any


class Items:
    Wood: Any
    Hay: Any
    Carrot_Seed: Any
    Pumpkin_Seed: Any
    Fertilizer: Any
    Water_Tank: Any
    Egg: Any


class Unlocks:
    Carrots: Any
    Trees: Any
    Multi_Trade: Any
    # ...add more unlock names as you unlock them, for autocomplete


# ---- Movement / position ----
def move(direction: Any) -> bool: ...
def get_pos_x() -> int: ...
def get_pos_y() -> int: ...
def get_world_size() -> int: ...
def do_a_flip() -> None: ...


# ---- Farming actions ----
def till() -> None: ...
def plant(entity: Any) -> bool: ...
def harvest() -> bool: ...
def can_harvest() -> bool: ...
def swap(direction: Any) -> None: ...
def get_entity_type() -> Any: ...
def get_ground_type() -> Any: ...
def get_water() -> float: ...
def get_companion() -> Optional[list]: ...
def measure(direction: Any = None) -> Any: ...


# ---- Items / trading / unlocks ----
def use_item(item: Any, n: int = 1) -> bool: ...
def num_items(item: Any) -> int: ...
def get_cost(thing: Any) -> Optional[dict]: ...
def unlock(unlock_target: Any) -> bool: ...
def num_unlocked(thing: Any) -> int: ...
def trade(item: Any, n: int = 1) -> Any: ...


# ---- Debug / utility ----
def print(*args: Any) -> None: ...  # game's print, overrides builtin's meaning in-game
def quick_print(*args: Any) -> None: ...
def clear() -> None: ...
def get_tick_count() -> int: ...
def get_time() -> float: ...
def set_execution_speed(speed: float) -> None: ...
def set_farm_size(size: int) -> None: ...
def timed_reset() -> None: ...


# ---- Multi-drone ----
def spawn_drone(function: Any, *args: Any) -> Optional[int]: ...
