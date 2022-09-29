
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(Generic: {0}, {1})".format(self.x, self.y)
    
    def set_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def get_position(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    