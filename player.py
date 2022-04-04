from actor import Actor
from controller import Controller
from config import *


class Player(Actor):

    def __init__(self, world, sprites, controller=None):
        super(Player, self).__init__(world, sprites, vmax=2)
        self.controller = controller or Controller()

    def update(self):
        self.velocity.vx = 0
        self.velocity.vy = 0
        index = DOWN
        if self.controller.right:
            self.velocity.vx = self.velocity.vmax
            index = RIGHT
        elif self.controller.left:
            self.velocity.vx -= self.velocity.vmax
            index = LEFT
        if self.controller.up:
            self.velocity.vy = -self.velocity.vmax
            index = UP
        elif self.controller.down:
            self.velocity.vy = self.velocity.vmax
            index = DOWN
        self.sprites.current = self.sprites.sprites[index]

    def execute(self, x, y):
        self.velocity.vx = x * self.velocity.vmax
        self.velocity.vy = y * self.velocity.vmax

        index = 0
        if y == -1:
            index = self.UP
        elif y == 1:
            index = self.DOWN
        elif x == 1:
            index = self.RIGHT
        elif x == -1:
            index = self.LEFT

        self.sprites.current = self.sprites.sprites[index]
