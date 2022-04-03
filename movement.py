from sdl2.ext import Applicator


class MovementSystem(Applicator):
    def __init__(self):
        super(MovementSystem, self).__init__()
        self.componenttypes = Position, Velocity

    def process(self, world, component_sets):
        for position, velocity in component_sets:
            velocity.vx = min(velocity.vmax, max(-velocity.vmax, velocity.vx))
            velocity.vy = min(velocity.vmax, max(-velocity.vmax, velocity.vy))

            position.x += velocity.vx
            position.y += velocity.vy


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Velocity:
    def __init__(self, vmax):
        self.vx = 0
        self.vy = 0
        self.vmax = vmax

    def __repr__(self):
        return f"({self.vx}, {self.vy})"
