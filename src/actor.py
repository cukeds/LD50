from movement import Velocity
from sdl2.ext import Entity


class Actor(Entity):
    def __init__(self, world, sprite, vmax):
        self.sprite = sprite
        self.velocity = Velocity(vmax=vmax)
