from sdl2.ext import Applicator
from movement import Position, Velocity
from config import AGG, PAS
from calculations import *


# player es Player()
class AISystem(Applicator):
    def __init__(self):
        super(AISystem, self).__init__()
        self.componenttypes = AI, Position, Velocity
        self.player = None

    def process(self, world, component_sets):
        for ai, position, velocity in component_sets:
            if ai.category == AGG:
                if distance(position.x, position.y, self.player.position.x, self.player.position.y) > 50:
                    dirx = 1 if position.x < self.player.position.x else -1
                    diry = 1 if position.y < self.player.position.y else -1

                    velocity.vx = 3 * dirx
                    velocity.vy = 3 * diry
                else:
                    velocity.vx = 0
                    velocity.vy = 0




class AI:
    def __init__(self, category):
        self.category = category