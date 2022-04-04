from sdl2.ext import Applicator
from sdl2 import SDL_GetTicks
from movement import Position, Velocity
from renderer import Sprites
from config import *
from calculations import *
from projectile import Projectile

# 100 TICKS == 33 UNIDADES A 1 U/T
# player es Player()


def get_dir(pos_1, pos_2):
    if pos_1.x < pos_2.x:
        dirx = 1
    elif pos_1.x > pos_2.x:
        dirx = -1
    else:
        dirx = 0

    if pos_1.y < pos_2.y:
        diry = 1
    elif pos_1.y > pos_2.y:
        diry = -1
    else:
        diry = 0

    return dirx, diry


def move_towards(velocity, dirx, diry):
    velocity.vx = 1 * dirx
    velocity.vy = 1 * diry


class AISystem(Applicator):
    def __init__(self):
        super(AISystem, self).__init__()
        self.componenttypes = AI, Position, Velocity, Sprites
        self.player = None
        self.tick = SDL_GetTicks()
        self.proj = None

    def process(self, world, component_sets):
        for ai, position, velocity, sprites in component_sets:
            ai.attack.update(world)
            dirx, diry = get_dir(position, self.player.position)
            if ai.category == AGG:
                if distance(position.x, position.y, self.player.position.x, self.player.position.y) > 100:
                    velocity.vx = 1 * dirx
                    velocity.vy = 1 * diry
                else:
                    velocity.vx = 0
                    velocity.vy = 0

                    ai.attack.execute(world, sprites.copy(), position.x, position.y, dirx*3, diry*3, 20)


            # Handles Sprites on Entities with AI

            if abs(velocity.vx) < abs(velocity.vy):
                if velocity.vy >= 0:
                    sprites.current = sprites.sprites[DOWN]
                else:
                    sprites.current = sprites.sprites[UP]
            else :
                if velocity.vx >= 0:
                    sprites.current = sprites.sprites[RIGHT]
                else:
                    sprites.current = sprites.sprites[LEFT]


class AI:
    def __init__(self, category, attack):
        self.category = category
        self.attack = attack()