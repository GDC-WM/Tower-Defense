import cv2

from GameEngine.Engine.World import World
from Tile import *

class Level(World):

    def __init__(self, engine, level):
        """Class for each level. Reads in a file for the layout.
        level -- The integer level number
        """
        super().__init__(engine)
        self.tiles = []
        
        level_img = cv2.imread("levels/" + str(level) + ".png")
        for i in level_img:
            row = []
            for j in i:
                row.append(Tile.getTyleType(j))
