import sdl2.ext as ext
from renderer import Renderer
from movement import MovementSystem


class World(ext.World):
    def __init__(self, window, renderer=None, movement_system=None):
        super(World, self).__init__()
        self.renderer = renderer or Renderer(window)
        self.movement_system = movement_system or MovementSystem()

        self.add_system(self.renderer)
        self.add_system(self.movement_system)
