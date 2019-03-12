import math

class Entity():
    """General code for things that appear in the world."""

    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.image = None

        self.animated = False
        self.animationDelay = None
        self.animationCounter = 0

    def isTouching(self, entity):
        """Checks if an entity is in contact with another"""
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")
        if (self.x <= entity.x + entity.width and
            self.x + self.width <= entity.x and
            self.y <= self.x + entity.height and
            self.y + self.height <= entity.y):
            return True
        return False

    def isInRange(self, entity, range):
        """Checks the bounds of the given entity against its own."""
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")
        if math.sqrt(((self.x + self.width / 2) - (entity.x + entity.width / 2))**2 +
                     ((self.y + self.height / 2) - (entity.y + entity.height / 2))**2) <= range:
            return True
        return False

    def getImage(self, scale):
        """Returns the image associated with the entity."""
        if self.image == None:
            return None

        return self.image.scaled(scale)

    def animationLoop(self):
        if self.animationCounter == self.animationDelay:
            self.image.nextImage()
            self.animationCounter = 0
        self.animationCounter += 1


class ActiveEntity(Entity):
    """A type of entity that allows for movement within the world."""

    def __init__(self):
        super().__init__()
        self.physical = False
        self.mass = 0
        self.x_speed = 0
        self.y_speed = 0
    
    def physics(self):
        """Applies the appropriate affects of game physics to the entity"""
        if self.physical:
            pass

        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def run(self):
        """User implementation of run method."""
        pass
    
    def push(self, vector):
        """Adds a momentum vector to the entity\n
        vector -- magnitude and direction (radians) in a tuple
        """
        self.x_speed = (self.mass*self.x_speed+vector[0]*math.cos(vector[1]))/self.mass
        self.y_speed = (self.mass*self.y_speed+vector[0]*math.sin(vector[1]))/self.mass
