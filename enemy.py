from actor import Actor
from AI import AI


class Enemy(Actor):
    def __init__(self, world, sprites, ai_cat, x=0, y=0):
        super(Enemy, self).__init__(world, sprites, 1, x, y)
        self.ai = AI(ai_cat)
