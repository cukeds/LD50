import sdl2.ext as ext
from renderer import Renderer


class World(ext.World):
    def __init__(self, window, renderer=None):
        super(World, self).__init__()
        self.renderer = renderer or Renderer(window)
        self.add_system(self.renderer)
