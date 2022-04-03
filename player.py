from actor import Actor
from controller import Controller
from config import *


class Player(Actor):
    PDOWN = 0
    PLEFT = 1
    PUP = 2
    PRIGHT = 3

    def __init__(self, world, sprites, controller=None):
        super(Player, self).__init__(world, sprites, vmax=2)
        self.controller = controller or Controller()

    def update(self):
        self.velocity.vx = 0
        self.velocity.vy = 0
        index = 0
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
            index = self.PUP
        elif y == 1:
            index = self.PDOWN
        elif x == 1:
            index = self.PRIGHT
        elif x == -1:
            index = self.PLEFT

        self.sprites.current = self.sprites.sprites[index]
