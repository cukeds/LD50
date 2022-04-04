import sdl2 as sdl
import sdl2.ext as ext
from sdl2.ext import Resources, Window, SpriteFactory
from world import World
from config import *
from enemy import Enemy
from portal import Portal
from controller import ControllerV2
import os
import random


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
                "fruity1": [],
                "fruity2": [],
                "boss": [],
                "blueberry": [],
                "crab": []
            },
            "backgrounds": {},
            "objects": []
        }
        for sprite_name in os.listdir(self.res):
            sprite = self.sprite_factory.from_image(os.path.join(self.res, sprite_name))
            s = str(sprite_name)
            if "player" in s:
                self.sprites['player'].append(sprite)
            elif "bg" in s:
                self.sprites["backgrounds"][s] = sprite
            elif "portal" in s:
                self.sprites["objects"].append(sprite)
            else:
                for k in self.sprites["enemies"].keys():
                    if k in s:
                        self.sprites["enemies"][k].append(sprite)  # Appends sprites!


    def run(self):
        running = True
        self.window.show()
        levels = []
        levels.append(self.level_one)
        levels.append(self.level_two)
        levels.append(self.level_three)
        levels[0]()
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
                    elif event.key.keysym.sym == sdl.SDLK_1:
                        levels[0]()
                    elif event.key.keysym.sym == sdl.SDLK_2:
                        levels[1]()
                    elif event.key.keysym.sym == sdl.SDLK_3:
                        levels[2]()
                    self.player.controller.handle_keydown(event.key)
                if event.type == sdl.SDL_KEYUP:
                    self.player.controller.handle_keyup(event.key)

            self.player.update()
            self.world.update()

    def level_one(self):
        self.world.reset()
        self.world.background = self.sprites["backgrounds"]["river_bridge_bg.png"]

        for i in range(5):
            x = random.choice(range(WIDTH))
            y = random.choice(range(HEIGHT))
            self.world.create_entity(Enemy, self.sprites["enemies"]["crab"], AGG, x, y)

        self.world.create_entity(Portal, self.sprites["objects"], WIDTH//2 - 50, 0)

    def level_two(self):
        self.world.reset()
        self.world.background = self.sprites["backgrounds"]["forest_bg.png"]

        for i in range(5):
            x = random.choice(range(WIDTH))
            y = random.choice(range(HEIGHT))
            enemy = random.choice(["fruity1", "fruity2"])
            self.world.create_entity(Enemy, self.sprites["enemies"][enemy], AGG, x, y)

        self.world.create_entity(Portal, self.sprites["objects"], WIDTH // 2 - 50, HEIGHT - 50)
        self.world.create_entity(Portal, self.sprites["objects"], WIDTH // 2 - 50, 0)

    def level_three(self):
        self.world.reset()
        self.world.background = self.sprites["backgrounds"]["clock_tower_bg1.png"]

        self.world.create_entity(Enemy, self.sprites["enemies"]["boss"], AGG, WIDTH // 2, HEIGHT // 2)

        self.world.create_entity(Portal, self.sprites["objects"], WIDTH//2 - 50, HEIGHT - 50)
