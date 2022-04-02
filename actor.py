from sdl2.ext import Entity

class Actor():
    def __init__(self, pos_x, pos_y, sprite):
        self.x = pos_x
        self.y = pos_y
        self.sprite = sprite