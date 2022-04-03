from sdl2.ext import Entity
from movement import Velocity, Position
from renderer import Sprites

class Projectile(Entity):
    def __init__(self, world, sprites, x, y, vx, vy):
        self.velocity = Velocity(10, vx, vy)
        self.position = Position(x, y)
        self.sprites = Sprites(sprites)
        self.sprites.current = self.sprites.sprites[4]