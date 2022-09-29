from Tiles.Tile import Tile

class Food_Tile(Tile):
    def __init__(self, x, y, isActive):
        self.isActive = isActive
        Tile.__init__(self, x, y)

    def __str__(self):
        return "(Food: {0}, {1}, isActive: {2})".format(self.x, self.y, self.isActive)
    
    def set_active(self, isActive):
        self.isActive = isActive
    
    def get_active(self):
        return self.isActive
    
    
    