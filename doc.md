# Project Documentation

## File Descriptions

- `actions.py`: Defines game actions such as movement, attacking, item usage, and interaction with the environment. Uses entities, engine, and components like inventory and equipment.
- `color.py`: Contains color definitions used throughout the game.
- `components/ai.py`: Implements AI behaviors for enemies, including pathfinding and different AI states. Depends on actions and entities.
- `components/base_component.py`: Base class for components linked to entities, providing access to game map and engine.
- `components/consumable.py`: Defines consumable item components with various effects like healing, damage, and confusion. Uses actions and entities.
- `components/equipment.py`: Manages equipment worn by actors, calculating bonuses and handling equip/unequip logic.
- `components/equippable.py`: Defines equippable item components with power and defense bonuses.
- `components/fighter.py`: Manages combat-related stats and behavior for actors, including health, damage, and death.
- `components/inventory.py`: Handles item storage for actors, including adding and dropping items.
- `components/level.py`: Manages experience points, leveling up, and attribute increases for actors.
- `engine.py`: Core game engine managing game state, rendering, enemy turns, and saving/loading.
- `entity.py`: Defines base classes for game entities including actors and items, managing position and components.
- `entity_factories.py`: Contains factory functions to create game entities.
- `equipment_types.py`: Defines equipment type enumeration (weapon, armor).
- `exceptions.py`: Custom exceptions for game logic control.
- `game_map.py`: Represents the game map with tiles, entities, visibility, and map-related queries.
- `input_handlers.py`: Handles user input, event processing, and UI screens.
- `main.py`: Entry point for the game, initializes and runs the main game loop.
- `message_log.py`: Manages in-game message logging and rendering.
- `procgen.py`: Procedural generation of dungeon maps, rooms, tunnels, and entity placement.
- `render_functions.py`: Rendering helper functions for UI elements and entity names.
- `render_order.py`: Defines rendering priority for entities.
- `setup_game.py`: Game setup functions including new game initialization and main menu.
- `tile_types.py`: Defines tile properties such as walkability and transparency.

## Project Structure Visualization

```
project_root/
├── actions.py               # Game actions and interactions
├── color.py                 # Color definitions
├── components/             # Game components
│   ├── ai.py               # Enemy AI behaviors
│   ├── base_component.py   # Base component class
│   ├── consumable.py       # Consumable item effects
│   ├── equipment.py        # Equipment management
│   ├── equippable.py       # Equippable item definitions
│   ├── fighter.py          # Combat stats and logic
│   ├── inventory.py        # Item inventory management
│   └── level.py            # Experience and leveling
├── engine.py               # Core game engine
├── entity.py               # Base entity classes
├── entity_factories.py     # Entity creation functions
├── equipment_types.py      # Equipment type enums
├── exceptions.py          # Custom exceptions
├── game_map.py            # Map and tile management
├── input_handlers.py      # Input and event handling
├── main.py                # Game entry point
├── message_log.py         # Message logging
├── procgen.py             # Dungeon generation
├── render_functions.py    # Rendering utilities
├── render_order.py        # Rendering priorities
├── setup_game.py          # Game setup and menus
└── tile_types.py          # Tile definitions
```

This documentation provides a brief overview of each file's purpose and their relationships within the project.