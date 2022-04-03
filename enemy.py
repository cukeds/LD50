from actor import Actor
from AI import AI

class Enemy(Actor):
    def __init__(self, world, sprites, ai_cat):
        super(Enemy, self).__init__(world, sprites, vmax=1)
        self.ai = AI(ai_cat)
        self.sprites.current = sprites[4]

