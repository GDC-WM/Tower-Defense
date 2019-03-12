import sys
import time

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, QPoint, QRect, Qt, QThread
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QScreen
from PyQt5.QtWidgets import QApplication, QWidget

from World import World

class Engine(QWidget):

    class RunThread(QThread):
        def __init__(self, engine):
            QtCore.QThread.__init__(self) 
            self.engine = engine
            self.running = True
        
        def run(self):
            while self.running:
                start_time = time.time()
                
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
        
        self.run_thread = self.RunThread(self)
        self.run_thread.start()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        if self.active_world is not None:
            self.active_world.drawScreen(qp)
        
        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Engine()
    ex.active_world = World(ex)
    sys.exit(app.exec_())
