import actor
import controller
from sdl2.ext import Entity
from movement import Velocity


class Player(Entity):
    def __init__(self, world, sprite, pos_x, pos_y):
        #super(Player, self).__init__(world, pos_x, pos_y, sprite)
        self.x = pos_x
        self.y = pos_y
        self.sprite = sprite
        self.velocity = Velocity(1)
        self.controller = controller.Controller()

    def update(self):
        if self.controller.right:
            self.velocity.vx += 1
        elif self.controller.left:
            self.velocity.vx -= 1

        if self.controller.up:
            self.velocity.vy += 1
        elif self.controller.down:
            self.velocity.vy -= 1

        print(self.vmax)
