from GameEngine.Engine.World import World
from GameEngine.Engine.Image import Image
from Button import Button

class MainMenu(World):
    
    def __init__(self, engine):
        super().__init__(engine)
        print("MainMenu")
        self.start_button = Button()
        self.start_button.setImage(Image("StartButton.png"))
        self.addEntity(self.start_button, 1920 / 2 - self.start_button.width / 2, 1080 * 2 / 3)