from sdl2.ext import Applicator
from movement import Position
from renderer import Sprites


def _overlap(area1, area2):
    left, top, right, bottom = area1
    bleft, btop, bright, bbottom = area2

    return (bleft <= right and bright >= left and
            btop <= bottom and bbottom >= top)


class CollisionSystem(Applicator):
    def __init__(self):
        super(CollisionSystem, self).__init__()
        self.componenttypes = Position, Sprites, Collider

    def process(self, world, componentsets):
        components = [comp for comp in componentsets]
        for pos, sprites, collider in components:
            for pos2, sprites2, collider2 in components:
                if collider is collider2:
                    continue
                s = sprites.current
                s2 = sprites2.current

                area1 = (pos.x, pos.y, pos.x + s.size[0], pos.y + s.size[1])
                area2 = (pos2.x, pos2.y, pos2.x + s2.size[0], pos2.y + s2.size[1])
                overlap = _overlap(area1, area2)
                if not overlap:
                    continue
                collider.on_collision(collider2)


class Collider:
    def __init__(self, on_collision):
        self.on_collision = on_collision


def print_collider(other):
    print(f"I collided against {other}")


def pass_collider(other):
    pass
