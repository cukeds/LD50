from movement import Velocity, Position
from sdl2.ext import Entity
from renderer import Sprites
from collision import Collider, print_collider, pass_collider


class Actor(Entity):
    def __init__(self, world, sprites, vmax, x=0, y=0, on_collision=None):
        self.position = Position(x, y)
        self.sprites = Sprites(sprites)
        self.velocity = Velocity(vmax=vmax)
        self.collider = Collider(on_collision or pass_collider)
