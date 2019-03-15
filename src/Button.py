from GameEngine import Engine.Entity.Entity

class Button(Entity):

    def __init__(self, text):
        """
        text -- a string to display on the button.
        """
        super().__init__()
        self.image = "replace this with an image"
        self.text = text
