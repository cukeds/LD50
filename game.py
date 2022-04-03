import sdl2 as sdl
import sdl2.ext as ext
from sdl2.ext import Resources, Window, SpriteFactory
from world import World
from config import *
from enemy import Enemy
from controller import ControllerV2
import os


class Game:
    def __init__(self, title, size=None, resources=None):
        self._setup(title, size or (WIDTH, HEIGHT), resources or "res")

    def _setup(self, title, size, resources):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.res = os.path.join(dir_path, resources)

        ext.init()

        self.window = Window(title, size)

        self.sprite_factory = SpriteFactory(ext.SOFTWARE)
        self._load_sprites()

        self.world = World(self.window)

        self.player = self.world.create_player(self.sprites["player"])

    def _load_sprites(self):
        self.sprites = {
            "player": [],
            "enemies": {
                "fruity": [],
                "boss": [],
                "blueberry": [],
                "crab": []
            },
            "backgrounds": [],
            "objects": []
        }
        for sprite_name in os.listdir(self.res):
            sprite = self.sprite_factory.from_image(os.path.join(self.res, sprite_name))
            s = str(sprite_name)
            if "player" in s:
                self.sprites['player'].append(sprite)
            elif "bg" in s:
                self.sprites["backgrounds"].append(sprite)
            elif "portal" in s:
                self.sprites["objects"].append(sprite)
            else:
                for k in self.sprites["enemies"].keys():
                    if k in s:
                        self.sprites["enemies"][k].append(sprite)
                        self.sprites["enemies"]["boss"].append(sprite)

    def run(self):
        running = True
        self.window.show()
        Enemy(self.world, self.sprites["enemies"]["boss"], AGG, 300, 300)
        # controller = ControllerV2(self.player)
        while running:
            self.window.refresh()

            events = ext.get_events()
            for event in events:
                if event.type == sdl.SDL_QUIT:
                    running = False
                if event.type == sdl.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl.SDLK_c and event.key.keysym.mod & sdl.KMOD_CTRL:
                        running = False
                        break
                    self.player.controller.handle_keydown(event.key)
                if event.type == sdl.SDL_KEYUP:
                    self.player.controller.handle_keyup(event.key)

            self.player.update()

            self.world.update()
