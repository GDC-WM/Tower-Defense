from Entity import Entity, ActiveEntity

from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QImage, QCursor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer

class World():

    def __init__(self, engine):
        self.engine = engine
        self.entity_list = []
        self.screen = Entity()
        self.screen.x = 0
        self.screen.y = 0
        self.screen.width = self.engine.screen_width
        self.screen.height = self.engine.screen_height
        self.tracked_entity = None

        # View offset for the camera to facilitate scrolling
        # These are added to the x and y value of each entity when rendered

        # default white background
        self.background = QImage(self.screen.width, self.screen.height, QImage.Format_RGB32)
        self.background.fill(QColor(255,255,255))

    def drawScreen(self, qp):
        """Draws all entities to the screen.\n
        qp -- a QPainter.
        """
        qp.drawImage(QPoint(0,0), self.background)

        for e in self.entity_list:
            if e.image is not None and e.isInRange(self.screen, 0):
                qp.drawImage(QPoint(int(e.x * self.engine.scale),
                                    int(e.y * self.engine.scale)),
                                    e.getImage(self.engine.scale))

    def runEntities(self):
        """Calls the physics() and run() methods."""
        for e in self.entity_list:
            if isinstance(e, ActiveEntity):
                e.physics()
                e.run()

        if self.tracked_entity is not None:
            self.screen.x = (self.tracked_entity.x + self.tracked_entity.width
                             / 2 - self.screen.width / 2)
            self.screen.y = (self.tracked_entity.y + self.tracked_entity.height
                             / 2 - self.screen.height / 2)

    def run(self):
        """User implementation of run method."""
        pass

    def addEntity(self, entity, x, y):
        """Add the designated entity to the entity list.\n
        x -- x-coordinate of the entity\n
        y -- y-coordinate of the entity
        """
        if not isinstance(entity, Entity):
            raise TypeError("Only accepts objects of type Entity")
        entity.x = x
        entity.y = y
        entity.world = self
        self.entity_list.append(entity)

    def removeEntity(self, entity):
        """Remove the designated entity from the entity list."""
        self.entity_list.remove(entity)

    def autoFocus(self, entity):
        """Keeps the given entity on the screen"""
        self.tracked_entity = entity

    def manualFocus(self):
        """Ends autoFocus"""
        self.tracked_entity = None

    def mouseX(self):
        """Get mouse X position"""
        return QCursor.pos().x()

    def mouseY(self):
        """Get mouse Y position"""
        return QCursor.pos().y()

    def isKeyPressed(self, key):
        """Check if a key is pressed\n
        key -- An integer key ID. Use Engine.key(keyName) to convert to key ID.
        """
        return (key in self.engine.pressed_keys)

    def mousePressed(self, key=0x00000001 ):
        return (key in self.engine.mouse_keys)

    def mouseReleased(self, key=0x00000001 ):
        return (key in self.engine.mouse_released)
