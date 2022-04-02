import actor
import controller

class Player(actor.Actor):
    def __init__(self, world, sprite, pos_x, pos_y):
        super().__init__(pos_x, pos_y, sprite)
        self.controller = controller.Controller()