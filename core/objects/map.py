"""

"""

from typing import Any
from random import randint

from ..visitors import Visitor
from .object import SimObject
from .colony import Colony
from .agent import Agent
from .food import Food

import settings


class Map(SimObject):
    def __init__(self, map_size: tuple[int, int], num_food: int, num_water: int, num_colonies, agents_per_colony):
        self.map_size = map_size
        self.num_food = num_food
        self.num_water = num_water
        self.num_colonies = num_colonies

        self.colonies: list[Colony] = []
        self.agents: list[Agent] = []
        self.food: list[Food] = []
        self.water: list[Any] = []

        self.occupied = set()

        self.tiles = {(i, j): [] for i in range(map_size[0]) for j in range(map_size[1])}

        for _ in range(num_food):
            f = Food((randint(0, settings.MAP_SIZE[0] - 1), randint(0, settings.MAP_SIZE[1] - 1)))
            self.tiles[f.pos].append(f)
            self.food.append(f)
            self.occupied.add(f.pos)

        for _ in range(num_colonies):
            c = Colony(agents_per_colony)
            for a in c.agents:
                self.tiles[a.pos].append(a)
                self.agents.append(a)
                self.occupied.add(a.pos)
            self.colonies.append(c)

        
    def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
        return visitor.visit_map(self, *args, **kwargs)