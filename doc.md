# Project Documentation

## File Descriptions

- `actions.py`: Defines various action classes representing player and entity actions such as movement, attacking, picking up items, and using items. Uses components like Actor, Item, and Engine.

- `color.py`: Contains color definitions used throughout the project.

- `components/ai.py`: Implements AI behavior for entities, including base AI, hostile enemy AI, and confused enemy AI.

- `components/base_component.py`: Base class for components that provides access to the game map and engine.

- `components/consumable.py`: Defines consumable item components that can be activated for effects like healing or damage.

- `components/equipment.py`: Manages equipment worn by entities, including weapons and armor, and their bonuses.

- `components/equippable.py`: Defines equippable item components such as weapons and armor types.

- `components/fighter.py`: Contains the Fighter component managing combat-related stats like health, power, and defense.

- `components/inventory.py`: Implements the inventory component for holding items.

- `components/level.py`: Manages leveling mechanics, experience points, and level-up benefits.

- `engine.py`: Core game engine managing the game state, rendering, and enemy turns.

- `entity.py`: Defines the base Entity class and subclasses for Actor and Item, representing all game objects.

- `entity_factories.py`: Contains factory functions to create various game entities.

- `equipment_types.py`: Defines equipment type enumerations used by equippable components.

- `exceptions.py`: Defines custom exceptions used in the game.

- `game_map.py`: Manages the game map, including tiles, entities on the map, and rendering.

- `input_handlers.py`: Handles user input and event processing, including different event handlers for game states.

- `main.py`: Entry point of the game, includes main game loop and save functionality.

- `message_log.py`: Manages the message log system for displaying game messages.

- `procgen.py`: Procedural generation functions for dungeon creation and entity placement.

- `render_functions.py`: Contains functions for rendering UI elements like bars and names.

- `render_order.py`: Defines rendering order enumeration for entities.

- `setup_game.py`: Functions to start a new game or load a saved game, and main menu handling.

- `tile_types.py`: Defines tile types and helper functions for tile creation.


## Project Structure Visualization

```
main.py - Entry point, game loop, save/load
engine.py - Game engine core
setup_game.py - Game setup and main menu

input_handlers.py - User input and event handling
message_log.py - Game message system
render_functions.py - UI rendering helpers
render_order.py - Entity render order

entity.py - Base entity classes (Actor, Item)
entity_factories.py - Entity creation

components/
  ai.py - AI behaviors
  base_component.py - Base component class
  consumable.py - Consumable item components
  equipment.py - Equipment management
  equippable.py - Equippable item components
  fighter.py - Combat stats component
  inventory.py - Inventory component
  level.py - Leveling system

game_map.py - Map and tile management
procgen.py - Dungeon procedural generation

actions.py - Player and entity actions
color.py - Color definitions
exceptions.py - Custom exceptions
equipment_types.py - Equipment type enums

```
