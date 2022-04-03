from actor import Actor
from controller import Controller


class Player(Actor):
    PDOWN = 0
    PLEFT = 1
    PUP = 2
    PRIGHT = 3

    def __init__(self, world, sprites, controller=None):
        super(Player, self).__init__(world, sprites, vmax=1)
        self.controller = controller or Controller()

    def update(self):
        self.velocity.vx = 0
        self.velocity.vy = 0
        if self.controller.right:
            self.velocity.vx = 1
        elif self.controller.left:
            self.velocity.vx -= 1

        if self.controller.up:
            self.velocity.vy = -1
        elif self.controller.down:
            self.velocity.vy = 1

    def execute(self, x, y):
        self.velocity.vx = x
        self.velocity.vy = y

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
