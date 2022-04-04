from sdl2 import SDL_Delay
import sdl2.ext as ext
from renderer import Renderer
from movement import MovementSystem
from AI import AISystem
from player import Player
from enemy import Enemy
from config import *


class World(ext.World):
    def __init__(self, window, renderer=None, movement_system=None, ai_system=None):
        super(World, self).__init__()
        self.player = None

        self.renderer = renderer or Renderer(window)
        self.movement_system = movement_system or MovementSystem()
        self.ai_system = ai_system or AISystem()

        self.add_system(self.ai_system)
        self.add_system(self.movement_system)
        self.add_system(self.renderer)

        self.stuff = []

    @property
    def background(self):
        return self.renderer.background

    @background.setter
    def background(self, bg):
        self.renderer.background = bg

    def update(self):
        SDL_Delay(10)
        # self.player.update()
        self.process()

    def create_player(self, sprites):
        self.player = Player(self, sprites)
        self.ai_system.player = self.player
        return self.player

    def create_entity(self, creator, *args):
        entity = creator(self, *args)
        self.stuff.append(entity)
        return entity

    def reset(self):
        self.player.position.x = WIDTH // 2 - 50
        self.player.position.y = HEIGHT - 120
        for enemy in self.stuff:
            enemy.delete()

        self.stuff = []
