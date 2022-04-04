from sdl2.ext import Entity
from movement import Position
from renderer import Sprites


class Portal(Entity):
    def __init__(self, world, sprites, x, y):
        self.position = Position(x, y)
        self.sprite = Sprites(sprites)
