from GameEngine import Engine.Entity.ActiveEntity

class Enemy(ActiveEntity):
    
    def __init__(self):
        super.__init__()
        self.health = 100
        self.width = 50
        self.height = 50
        self.speed = 5
        self.direction = None

    def move():
        if len(self.getNeighborsTyped(Tile)) == 1:
            self.direction = self.getNeighborsTyped[0]
        
        if self.direction == north:
            

    def run():
        self.move()

class Brute(Enemy):

    def __init__(self, level):
        self.__START_HEALTH = 100
        self.__INCREMENT = 1.1
        super.__init__(self.__START_HEALTH * self.__INCREMENT ** level, 5, 30, 30)
