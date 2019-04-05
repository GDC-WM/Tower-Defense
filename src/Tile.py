from GameEngine import Engine.Entity.Entity

class Tile(Entity):

    def __init__(self):
        """Class for tiles.
        """
        super().__init__()
        self.open = False       #Can a defense be placed here?
    
    @staticmethod
    def getTyleType(color):
        pass #set of if statements for returning which it is

class Path(Tile):

    def __init__(self):
        """Class for Path Tiles.
        """
        super().__init__()