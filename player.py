import actor
import controller


class Player(actor.Actor):
    def __init__(self, world, sprite, pos_x, pos_y):
        super().__init__(world, pos_x, pos_y, sprite)
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