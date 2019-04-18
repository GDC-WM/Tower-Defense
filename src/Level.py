import cv2

from GameEngine.Engine.World import World
from Tile import *

class Level(World):

    def __init__(self, engine, level):
        """Class for each level. Reads in a file for the layout.
        level -- A string level name
        """ 
        super().__init__(engine)
        self.tiles = []
        
        """R is for the backgrounds (water, grass, etc.)
        G is for obstacles on the tile or roads
        B is for status effects
        """
        level_img = cv2.imread("levels/" + level + ".png")
        for i in range(level_img.shape[0]):
            for j in range(level_img.shape[1]):
                if level_img[i,j][1]:
                    pass
                else:
                    row.append(Tile.getTyleType(j))