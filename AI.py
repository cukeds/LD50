from sdl2.ext import Applicator
from sdl2 import SDL_GetTicks
from movement import Position, Velocity
from renderer import Sprites
from config import *
from calculations import *
from projectile import Projectile


# player es Player()
class AISystem(Applicator):
    def __init__(self):
        super(AISystem, self).__init__()
        self.componenttypes = AI, Position, Velocity, Sprites
        self.player = None
        self.tick = SDL_GetTicks()
        self.proj = None

    def process(self, world, component_sets):
        for ai, position, velocity, sprites in component_sets:
            if position.x < self.player.position.x:
                dirx = 1
            elif position.x > self.player.position.x:
                dirx = -1
            else:
                dirx = 0

            if position.y < self.player.position.y:
                diry = 1
            elif position.y > self.player.position.y:
                diry = -1
            else:
                diry = 0

            if ai.category == AGG:
                if distance(position.x, position.y, self.player.position.x, self.player.position.y) > 100:
                    velocity.vx = 1 * dirx
                    velocity.vy = 1 * diry
                else:
                    velocity.vx = 0
                    velocity.vy = 0

                    if self.proj is None:
                        self.tick = SDL_GetTicks()
                        self.proj = Projectile(world, sprites.copy(), position.x, position.y, 3*dirx, 3*diry)
                if SDL_GetTicks() >= self.tick + 200 and self.proj is not None:
                    self.proj.delete()
                    self.proj = None


            # Handles Sprites on Entities with AI
            if abs(velocity.vx) > abs(velocity.vy):
                if velocity.vx >= 0:
                    sprites.current = sprites.sprites[RIGHT]
                else:
                    sprites.current = sprites.sprites[LEFT]
            else:
                if velocity.vy >= 0:
                    sprites.current = sprites.sprites[DOWN]
                else:
                    sprites.current = sprites.sprites[UP]



class AI:
    def __init__(self, category):
        self.category = category