from Tiles.Tile import Tile

class Agent_Tile(Tile):
    def __init__(self, x, y, isAlive, hunger, thirst, facing):
        self.isAlive = isAlive
        self.hunger = hunger
        self.thirst = thirst
        self.facing = facing 
        Tile.__init__(self, x, y)


    def __str__(self):
        return "(Food: {0}, {1}, isAlive: {2}, hunger: {3}, thirst: {4}, facing: {5})".format(self.x, self.y, self.isAlive, self.hunger, self.thirst, self.facing)
    
    def kill(self):
        self.isAlive = False
    
    def is_alive(self):
        return self.isAlive
    
    def set_hunger(self, hunger):
        self.hunger = hunger
    
    def get_hunger(self):
        return self.hunger
    
    def set_thirst(self, thirst):
        self.thirst = thirst
    
    def get_thirst(self):
        return self.thirst
    
    def set_facing(self, facing):
        self.facing = facing
    
    def get_facing(self):
        return self.facing
    
    
    