import actor
import controller


class Player(actor.Actor):
    def __init__(self, world, sprite):
        super(Player, self).__init__(world, sprite, vmax=2)
        self.controller = controller.Controller()

    def update(self):
        if self.controller.right:
            self.velocity.vx += 1
        elif self.controller.left:
            self.velocity.vx -= 1

        if self.controller.up:
            self.velocity.vy -= 1
        elif self.controller.down:
            self.velocity.vy += 1

        self.velocity.vx = min(self.velocity.vmax, max(-self.velocity.vmax, self.velocity.vx))
        self.velocity.vy = min(self.velocity.vmax, max(-self.velocity.vmax, self.velocity.vy))
