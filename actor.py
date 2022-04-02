from movement import Velocity, Position
from sdl2.ext import Entity
from renderer import Sprites


class Actor(Entity):
    def __init__(self, world, sprites, vmax):
        self.position = Position()
        self.sprites = Sprites(sprites)
        self.velocity = Velocity(vmax=vmax)
