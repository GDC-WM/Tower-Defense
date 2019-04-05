from GameEngine import Engine.Entity.ActiveEntity
from Tile import *

class Enemy(ActiveEntity):
    
    def __init__(self):
        super.__init__()
        self.health = 100
        self.width = 50
        self.height = 50
        self.speed = 5
        self.cur_tile = None
        self.next_tile = None

    def checkTile(self):
        if not self.next_tile and len(self.isNeighbor(Path)) == 2:
            self.next_tile = self.isNeighbor(Path) - {self.cur_tile}

    def move(self):
        pass

    def run(self):
        self.checkTile()
        self.move()

class Brute(Enemy):

    def __init__(self, level):
        self.__START_HEALTH = 100
        self.__INCREMENT = 1.1
        super.__init__(self.__START_HEALTH * self.__INCREMENT ** level, 5, 30, 30)
