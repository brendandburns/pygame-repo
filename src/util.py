from pgzrun import *

class Background:
    def __init__(self, image, width, height):
        self.image = Actor(image)
        self.image.width = width
        self.image.height = height
        self.image.pos = width/2, height/2


    def draw(self):
        self.image.draw()