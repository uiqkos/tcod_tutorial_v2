from __future__ import annotations

from typing import Iterator, Tuple, TYPE_CHECKING

import numpy as np

import tile_types

if TYPE_CHECKING:
    from entity import Entity
    from tcod import Console
    from engine import Engine


class GameMap:
    def __init__(
        self,
        engine: Engine,
        width: int,
        height: int,
        entities: set[Entity] = None,
    ):
        self.engine = engine
        self.width, self.height = width, height

        self.entities = entities if entities is not None else set()

        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")
        self.explored = np.full((width, height), fill_value=False, order="F")

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.
        """
        # Draw all tiles in the game map
        for x in range(self.width):
            for y in range(self.height):
                visible = self.visible[x, y]
                wall = not self.tiles[x, y]["walkable"]

                if visible:
                    console.tiles_rgb[x, y] = self.tiles[x, y]["light"]
                    self.explored[x, y] = True
                elif self.explored[x, y]:
                    console.tiles_rgb[x, y] = self.tiles[x, y]["dark"]
                else:
                    console.tiles_rgb[x, y] = tile_types.SHROUD

        # Draw all entities in the game map
        entities_sorted = sorted(self.entities, key=lambda x: x.render_order.value)
        for entity in entities_sorted:
            if self.in_bounds(entity.x, entity.y) and self.visible[entity.x, entity.y]:
                console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)