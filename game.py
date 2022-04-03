import sdl2 as sdl
import sdl2.ext as ext
from sdl2.ext import Resources, Window, SpriteFactory
from world import World
from config import *
from enemy import Enemy
from controller import ControllerV2


class Game:
    def __init__(self, title, size=None, resources=None):
        self._setup(title, size or (WIDTH, HEIGHT), resources or "res")

    def _setup(self, title, size, resources):
        self.RES = Resources(__file__, resources)
        ext.init()

        self.window = Window(title, size)

        self.sprite_factory = SpriteFactory(ext.SOFTWARE)
        self._load_sprites()

        self.world = World(self.window)

        self.player = self.world.create_player(self.sprites["player"])

    def _load_sprites(self):
        self.sprites = {}
        sprite_names = ["player_down.png", "player_left.png", "player_up.png", "player_right.png", "test_proj.png"]
        sprites = []
        for sprite in sprite_names:
            sprites.append(self.sprite_factory.from_image(self.RES.get_path(sprite)))

        self.sprites["player"] = sprites
        self.sprites["enemy"] = sprites.copy()

    def run(self):
        running = True
        self.window.show()
        Enemy(self.world, self.sprites["enemy"], AGG, 300, 300)
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
