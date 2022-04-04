from sdl2.ext import Entity
from movement import Position
from renderer import Sprites
from collision import Collider, pass_collider


class Portal(Entity):
    def __init__(self, world, sprites, x, y):
        self.position = Position(x, y)
        self.sprite = Sprites(sprites)
        self.collider = Collider(pass_collider)
