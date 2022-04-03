from sdl2 import SDL_Delay
import sdl2.ext as ext
from renderer import RendererSystem
from movement import MovementSystem
from AI import AISystem
from player import Player


class World(ext.World):
    def __init__(self, window, renderer=None, movement_system=None, ai_system=None):
        super(World, self).__init__()
        self.player = None

        self.renderer = renderer or RendererSystem(window)
        self.movement_system = movement_system or MovementSystem()
        self.ai_system = ai_system or AISystem()

        self.add_system(self.renderer)
        self.add_system(self.movement_system)
        self.add_system(self.ai_system)

    def update(self):
        SDL_Delay(10)
        self.player.update()
        self.process()

    def create_player(self, sprites):
        self.player = Player(self, sprites)
        self.ai_system.player = self.player
        return self.player
