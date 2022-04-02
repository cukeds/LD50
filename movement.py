from sdl2.ext import Applicator


class MovementSystem(Applicator):
    def __init__(self):
        super(MovementSystem, self).__init__()
        self.componenttypes = Position, Velocity

    def process(self, world, component_sets):
        for position, velocity in component_sets:
            position.x += velocity.vx
            position.y += velocity.vy


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0


class Velocity:
    def __init__(self, vmax):
        self.vx = 0
        self.vy = 0
        self.vmax = vmax

    def __repr__(self):
        return f"({self.vx}, {self.vy})"
