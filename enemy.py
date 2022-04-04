from actor import Actor
from AI import AI
from projectile import Projectile

CD = 25


class Enemy(Actor):
    def __init__(self, world, sprites, ai_cat, x=0, y=0, attack=None):
        super(Enemy, self).__init__(world, sprites, 1, x, y)
        self.ai = AI(ai_cat, attack or Shoot)


class Action:
    def __init__(self):
        pass

    def execute(self, world, *args):
        raise NotImplementedError()

    def update(self, world):
        raise NotImplementedError()


class Shoot(Action):
    def __init__(self):
        super(Shoot, self).__init__()
        self.projectiles = []
        self.gameticks = 0

    def execute(self, world, *args):
        if self.gameticks > CD:
            self.projectiles.append(Projectile(world, *args))
            self.gameticks = 0

    def update(self, world):
        self.gameticks += 1
        for p in self.projectiles:
            p.life.lifespan -= 1
            if p.life.lifespan <= 0:
                p.delete()
                self.projectiles.remove(p)


class Explode(Action):
    def __init__(self):
        super(Explode, self).__init__()

    def execute(self, world, *args):
        pass

    def update(self, world):
        pass
