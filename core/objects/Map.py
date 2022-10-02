"""

"""

import random
from typing import Any

from core.objects.Tiles.Agent_Tile import Agent_Tile
from core.objects.Tiles.Food_Tile import Food_Tile
from core.objects.Tiles.Water_Tile import Water_Tile
from core.objects.Tiles.Tile import Tile

from ..visitors import Visitor
from .object import SimObject
from .colony import Colony


class Map(SimObject):
    def __init__(self, map_size, num_food, num_water, num_colonies, agents_per_colony):
        self.map_size = map_size
        self.num_food = num_food
        self.num_water = num_water
        self.num_colonies = num_colonies
        self.agents = [Colony(agents_per_colony) for _ in range(num_colonies)]
        self.map = [[None]*map_size for i in range(map_size)]
        self.build_map()

    def accept(self, visitor: Visitor, *args, **kwargs) -> Any:
        return visitor.visit_map(self, *args, **kwargs)
    
    def print(self):
        for i in range(self.map_size):
            for j in range(self.map_size):
                print( i, ",", j, ": ", self.map[i][j])

    def build_map(self):
        for i in range(self.num_food):
            self.add_food()
        for i in range(self.num_water):
            self.add_water()
        for i in range(self.num_colonies):
            self.add_colony()
        for i in range(self.map_size):
            for j in range(self.map_size):
                if self.map[i][j] == None:
                    self.map[i][j] = Tile(i, j)

    def add_food(self):
        x = random.randint(0, self.map_size-1)
        y = random.randint(0, self.map_size-1)
        while self.map[x][y] != None:
            x = random.randint(0, self.map_size-1)
            y = random.randint(0, self.map_size-1)
        self.map[x][y] = Food_Tile(x, y, True)
    
    def add_water(self):
        x = random.randint(0, self.map_size-1)
        y = random.randint(0, self.map_size-1)
        while self.map[x][y] != None:
            x = random.randint(0, self.map_size-1)
            y = random.randint(0, self.map_size-1)
        self.map[x][y] = Water_Tile(x, y, True)
    
    def add_colony(self):
        x = random.randint(0, self.map_size-1)
        y = random.randint(0, self.map_size-1)
        while self.map[x][y] != None:
            x = random.randint(0, self.map_size-1)
            y = random.randint(0, self.map_size-1)
        self.map[x][y] = Agent_Tile(x, y, True, 8, 8, 1)
    
    def get_tile(self, x, y):
        return self.map[x][y]
    
    def set_tile(self, x, y, tile):
        self.map[x][y] = tile
