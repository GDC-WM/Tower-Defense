from GameEngine.Engine.Entity import Entity

class Button(Entity):

    def __init__(self):
        """Create a button
        """
        super().__init__()
        self.clicked_image = self.image
    
    def isDown(self):
        pass

    def run():
        if(self.world):
            pass