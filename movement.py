from sdl2.ext import Applicator, Sprite


class MovementSystem(Applicator):
    def __init__(self):
        super(MovementSystem, self).__init__()
        self.componenttypes = Velocity, Sprite

    def process(self, world, component_sets):
        for velocity, sprite in component_sets:
            sprite.x += velocity.vx
            sprite.y += velocity.vy


class Velocity:
    def __init__(self):
        self.vx = 0
        self.vy = 0
