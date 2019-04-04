from Entity import Entity, ActiveEntity

from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QImage, QCursor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint, QTimer

class World():

    def __init__(self, engine):
        self.engine = engine
        self.entities = set()
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
        qp -- a QPainter
        """
        qp.drawImage(QPoint(0,0), self.background)

        for e in self.entities:
            if e.isNeighbor(self.screen):
                if e.image:        
                    qp.drawImage(QPoint(int(e.x * self.engine.scale),
                                        int(e.y * self.engine.scale)),
                                        e.getImage(self.engine.scale))
                elif e.text:
                    qp.drawText(QPoint(int(e.x * self.engine.scale),
                                       int(e.y * self.engine.scale)), e.text)

    def runEntities(self):
        """Calls the physics() and run() methods.
        """
        for e in self.entities:
            if isinstance(e, ActiveEntity):
                e.physics()
                e.run()

        if self.tracked_entity:
            self.screen.x = (self.tracked_entity.x + self.tracked_entity.width
                             / 2 - self.screen.width / 2)
            self.screen.y = (self.tracked_entity.y + self.tracked_entity.height
                             / 2 - self.screen.height / 2)

    def run(self):
        """User implementation of run method.
        """
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
        self.entities.add(entity)

    def removeEntity(self, entity):
        """Remove the designated entity from the entity list.\n
        entity -- type Entity
        """
        self.entities.remove(entity)

    def autoFocus(self, entity):
        """Keeps the given entity on the screen.\n
        entity -- type Entity
        """
        self.tracked_entity = entity

    def manualFocus(self):
        """Ends autoFocus.
        """
        self.tracked_entity = None

    def mouseX(self):
        """Get mouse X position.
        """
        return QCursor.pos().x() / self.engine.scale

    def mouseY(self):
        """Get mouse Y position.
        """
        return QCursor.pos().y() / self.engine.scale

    def isKeyPressed(self, key):
        """Check if a key is pressed.\n
        key -- An integer key ID. Use Engine.key(keyName) to convert to key ID
        """
        return (key in self.engine.pressed_keys)

    def mousePressed(self, key=0x00000001):
        """unknown
        """
        return (key in self.engine.mouse_keys)

    def mouseReleased(self, key=0x00000001):
        """unknown
        """
        return (key in self.engine.mouse_released)

    def mouseOver(self, entity):
        """Is the mouse over the entity?
        """
        return (self.mouseX() <= entity.x + entity.width and
                self.mouseX() >= entity.x and
                self.mouseY() <= entity.y + entity.height and
                self.mouseY() >= entity.y)
