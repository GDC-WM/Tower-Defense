import sys
from PyQt5.QtGui import QImage, QColor
from PyQt5.QtCore import Qt, QRect, QPoint

class Image():
    
    def __init__(self, filename):
        self.__image = QImage(filename)

    def getImage(self):
        return self.__image

    def setScale(self, xFactor, yFactor):
        self.__image = self.__image.scaled(self.getWidth()*xFactor, self.getHeight()*yFactor)

    def getScaled(self, factor):
        return self.__image.scaled(self.getWidth()*factor, self.getHeight()*factor)

    def getWidth(self):
        return self.__image.size().width()

    def getHeight(self):
        return self.__image.size().height()

class ImageGroup():

    def __init__(self):
        self.__images = []
        self.__image_index = 0

    def addImage(self, image):
        self.__images.append(image)
    
    def getImage(self):
        return self.__images[self.__image_index]

    def setStart(self):
        self.image = self.__images[0]

    def nextImage(self):
        self.__image_index = (self.__image_index + 1) % len(self.__images)
