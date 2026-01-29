# Project Documentation

## File Descriptions

- `actions.py`: Defines game actions such as movement, attacking, item usage, and interactions. Uses entities, components, and engine.
- `color.py`: (Not explored, likely color definitions for rendering.)
- `components/ai.py`: AI behaviors for actors including hostile and confused states. Depends on actions and entities.
- `components/base_component.py`: Base class for components linked to entities, providing access to game map and engine.
- `components/consumable.py`: Defines consumable item behaviors like healing, fireball, confusion, and lightning damage. Uses actions and components.
- `components/equipment.py`: Manages equipped items on actors, calculating bonuses and toggling equipment.
- `components/equippable.py`: Defines equippable item components with power and defense bonuses.
- `components/fighter.py`: Handles combat stats and mechanics for actors including health, damage, and death.
- `components/inventory.py`: Manages actor's inventory, item capacity, and dropping items.
- `components/level.py`: Manages experience, leveling up, and attribute increases for actors.
- `engine.py`: Core game engine managing game state, rendering, enemy turns, and saving.
- `entity.py`: Base entity class for all game objects, including actors and items, with positioning and spawning.
- `entity_factories.py`: (Not explored, likely factory functions for creating entities.)
- `equipment_types.py`: Enum defining equipment categories (weapon, armor).
- `exceptions.py`: Custom exceptions for game logic like impossible actions and quit without saving.
- `game_map.py`: Represents the game map with tiles, entities, visibility, and map generation.
- `input_handlers.py`: Handles user input events, game state transitions, and UI interactions.
- `main.py`: Entry point for the game, initializes and runs the main game loop.
- `message_log.py`: Manages in-game messages, stacking repeated messages, and rendering logs.
- `procgen.py`: Procedural generation of dungeon maps, rooms, tunnels, and entity placement.
- `render_functions.py`: Rendering helpers for UI elements like health bars and entity names.
- `render_order.py`: Enum defining rendering priority of entities.
- `setup_game.py`: Functions to start a new game, load saved games, and main menu handling.
- `tile_types.py`: Defines tile properties like walkability and transparency.

## Project Structure Visualization

```
main.py           - Game entry point and main loop
setup_game.py     - Game initialization and main menu
engine.py         - Core game engine managing state and rendering

actions.py        - Game actions (move, attack, use item)
input_handlers.py - User input and event handling
message_log.py    - In-game message management
render_functions.py - UI rendering helpers
render_order.py   - Entity rendering priority

entity.py         - Base game entities (actors, items)
components/       - Game components:
  ai.py           - AI behaviors
  base_component.py - Base component class
  consumable.py   - Consumable item effects
  equipment.py    - Equipment management
  equippable.py   - Equippable item definitions
  fighter.py      - Combat stats and mechanics
  inventory.py    - Inventory management
  level.py        - Experience and leveling

game_map.py      - Map representation and visibility
procgen.py       - Dungeon generation
exceptions.py    - Custom game exceptions
color.py         - Color definitions
entity_factories.py - Entity creation helpers
equipment_types.py - Equipment type enums
tile_types.py    - Tile properties
```

This documentation provides a concise overview of each file's purpose and their relationships within the project.