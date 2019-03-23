import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QPoint, QRect, Qt, QThread
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QScreen, QKeyEvent
from PyQt5.QtWidgets import QApplication, QWidget

from World import World

class EngineInit():

    def __init__(self):
        pass

    def startWorld(self, ex):
        return World(ex)


class Engine(QWidget):

    class RunThread(QThread):
        def __init__(self, engine):
            QtCore.QThread.__init__(self) 
            self.engine = engine
            self.running = True
        
        def run(self):
            while self.running:
                start_time = time.time()

                while len(self.engine.mouse_released) != 0:
                    self.engine.mouse_released.pop()

                while len(self.engine.mouse_up_instant) != 0:
                    key = self.engine.mouse_up_instant.pop()
                    self.engine.mouse_keys.discard(key)
                    self.engine.mouse_released.add(key)

                if self.engine.active_world is not None:
                    self.engine.active_world.runEntities()
                    self.engine.active_world.run()
                
                if(1/60 - (time.time() - start_time)) > 0:
                    time.sleep(1/60 - (time.time() - start_time))
                self.engine.update()

    def __init__(self):
        super().__init__()

        self.screen_width = QScreen.size(QApplication.primaryScreen()).width()
        self.screen_height = QScreen.size(QApplication.primaryScreen()).height()
        self.setFixedSize(self.screen_width, self.screen_height)
        #set scale based on relation to 1080p
        self.scale = self.screen_width/1080
        self.showFullScreen()

        self.active_world = None
        self.pressed_keys = set()
        self.mouse_keys = set()
        self.mouse_released = set()
        self.mouse_up_instant = set()
        
        self.run_thread = self.RunThread(self)
        self.run_thread.start()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        if self.active_world is not None:
            self.active_world.drawScreen(qp)
        
        qp.end()

    def keyPressEvent(self, event):
        self.pressed_keys.add(event.key())

    def keyReleaseEvent(self, event):
        self.pressed_keys.discard(event.key())

    def mousePressEvent(self, event):
        self.mouse_keys.add(event.button())

    def mouseReleaseEvent(self, event):
        self.mouse_up_instant.add(event.button())


    @staticmethod
    def start(main):
        app = QApplication(sys.argv)
        ex = Engine()
        ex.active_world = main.startWorld(ex)
        sys.exit(app.exec_())

    @staticmethod
    def key(keyName):
        if len(keyName) == 1:
            return ord(keyName.upper())
        elif keyName == "left":
            return 0x01000012
        elif keyName == "up":
            return 0x01000013
        elif keyName == "right":
            return 0x01000014
        elif keyName == "down":
            return 0x01000013
        elif keyName == "shift":
            return 0x01000020
        elif keyName == "ctrl":
            return 0x01000021
        elif keyName == "alt":
            return 0x01000023
        elif keyName == "return":
            return 0x01000004
        elif keyName == "esc":
            return 0x01000000
        elif keyName == "tab":
            return 0x01000001
        elif keyName == "backspace":
            return 0x01000003

    @staticmethod
    def mouseKey(keyName):
        if keyName == "left":
            return 0x00000001
        if keyName == "right":
            return 0x00000002
        if keyName == "middle":
            return 0x00000004

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Engine()
    ex.active_world = World(ex)
    sys.exit(app.exec_())
