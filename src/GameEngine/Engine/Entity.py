import math
from Image import Image

class Entity():
    """General code for things that appear in the world.
    """
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.image = None
        self.world = None

        self.text = None    #this should remain none unless you want the object to be rendered as text.

        self.animated = False
        self.animationDelay = None
        self.animationCounter = 0

    def isNeighbor(self, entity):
        """Checks if this entity is in contact with another.
        entity -- type Entity
        """
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")

        return (self.x <= entity.x + entity.width and
                self.x + self.width >= entity.x and
                self.y <= entity.y + entity.height and
                self.y + self.height >= entity.y)

    def isInRange(self, entity, rng):
        """Checks the bounds of the given entity against its own.\n
        entity -- type Entity\n
        rng -- integer distance between the centers of the entities
        """
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")

        return math.sqrt(((self.x + self.width / 2) - (entity.x + entity.width / 2))**2 +
                         ((self.y + self.height / 2) - (entity.y + entity.height / 2))**2) <= rng

    def getNeighbors(self, *args):
        """Get entities in the current world that are in contact with this entity. Option to specify a certain type of entity to look for and a range at which to look for them.\n
        entity_type -- A subclass of entity\n
        rng -- integer distance between the centers of the entities
        """
        rng = None
        entity_type = None
        neighbors = set()

        for arg in args:
            if isinstance(arg, int):
                rng = arg
            elif issubclass(arg, Entity):
                entity_type = arg
            else:
                raise TypeError("Only accepts integers or a subclass of Entity")

        if entity_type:
            if rng:
                for e in self.world.entity_list():
                    if isinstance(e, entity_type) and self.isInRange(e, rng):
                        neighbors.add(e)
            else:
                for e in self.world.entity_list():
                    if isinstance(e, entity_type) and self.isNeighbor(e):
                        neighbors.add(e)
        else:
            if rng:
                for e in self.world.entity_list():
                    if self.isInRange(e, rng):
                        neighbors.add(e)
            else:
                for e in self.world.entity_list():
                    if self.isNeighbor(e):
                        neighbors.add(e)
        
        neighbors.discard(self)  #"Thou shalt love thy neighbor, not thyself" -God

        return neighbors

    def setImage(self, image, width=0, height=0):
        """Sets the image\n
        image -- Type Image\n
        width -- A positive integer for width. Default is zero where it will be ignored.
        height -- A positive integer for height. Default is zero where it will be ignored.
        """
        if not isinstance(image, Image):
            raise TypeError("Only accepts objects of type Image")

        self.image = image
        if height > 0 and width > 0:
            self.image.setSize(height, width)

        self.width = image.getWidth()
        self.height = image.getHeight()

    def getImage(self, scale):
        """Returns the image associated with the entity.\n
        scale -- A double representation of the scaling factor
        """
        return self.image.getScaled(scale) if self.image else None

    def animationLoop(self):
        """unknown
        """
        if self.animationCounter == self.animationDelay:
            self.image.nextImage()
            self.animationCounter = 0
        self.animationCounter += 1

class ActiveEntity(Entity):
    """A type of entity that allows for movement within the world.
    """
    def __init__(self):
        super().__init__()
        self.physical = False
        self.mass = 0
        self.x_speed = 0
        self.y_speed = 0
    
    def physics(self):
        """Applies the appropriate affects of game physics to the entity
        """
        if self.physical:
            pass

        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def run(self):
        """User implementation of run method.
        """
        pass
    
    def push(self, vector):
        """Adds a momentum vector to the entity\n
        vector -- magnitude and direction (radians) in a tuple
        """
        self.x_speed = (self.mass * self.x_speed + vector[0] * math.cos(vector[1])) / self.mass
        self.y_speed = (self.mass * self.y_speed + vector[0] * math.sin(vector[1])) / self.mass
