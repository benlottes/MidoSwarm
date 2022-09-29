from Tiles.Agent_Tile import Agent_Tile
from Tiles.Food_Tile import Food_Tile
from Tiles.Water_Tile import Water_Tile
from Tiles.Tile import Tile
import random

class Map:
    def __init__(self, map_size, num_food, num_water, num_agents):
        self.map_size = map_size
        self.num_food = num_food
        self.num_water = num_water
        self.num_agents = num_agents
        self.map = [[None]*map_size for i in range(map_size)]
        self.build_map()
    
    def print(self):
        for i in range(self.map_size):
            for j in range(self.map_size):
                print( i, ",", j, ": ", self.map[i][j])

    def build_map(self):
        for i in range(self.num_food):
            self.add_food()
        for i in range(self.num_water):
            self.add_water()
        for i in range(self.num_agents):
            self.add_agent()
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
    
    def add_agent(self):
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
    


