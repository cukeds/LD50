from sdl2.ext import Entity
from movement import Velocity


class Actor(Entity):
    def __init__(self, world, pos_x, pos_y, sprite):
        self.x = pos_x
        self.y = pos_y
        self.sprite = sprite
        self.velocity = Velocity()

