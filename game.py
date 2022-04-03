import sdl2 as sdl
import sdl2.ext as ext
from sdl2.ext import init, Resources, Window, SpriteFactory
from world import World
from config import *
from enemy import Enemy


class Game:
    def __init__(self, title, size=None, resources=None):
        self._setup(title, size or (WIDTH, HEIGHT), resources or "res")
        self.running = True
        self.window.show()

    def _setup(self, title, size, resources):
        self.RES = Resources(__file__, resources)
        init()

        self.sprite_factory = SpriteFactory(ext.SOFTWARE)
        self._load_sprites()

        self.window = Window(title, size)
        self.world = World(self.window)

        self.player = self.world.create_player(self.sprites["player"])

    def _load_sprites(self):
        self.sprites = {}
        sprite_names = ["player_down.png", "player_left.png", "player_up.png", "player_right.png"]
        sprites = []
        for sprite in sprite_names:
            sprites.append(self.sprite_factory.from_image(self.RES.get_path(sprite)))

        self.sprites["player"] = sprites
        self.sprites["enemy"] = sprites.copy()

    def run(self):
        enemy = Enemy(self.world, self.sprites["enemy"], AGG)
        while self.running:
            self.window.refresh()

            events = ext.get_events()
            for event in events:
                if event.type == sdl.SDL_QUIT:
                    self.running = False
                if event.type == sdl.SDL_KEYDOWN:
                    if event.key.keysym.sym == sdl.SDLK_c and event.key.keysym.mod & sdl.KMOD_CTRL:
                        self.running = False
                        break
                    self.player.controller.handle_keydown(event.key)
                if event.type == sdl.SDL_KEYUP:
                    self.player.controller.handle_keyup(event.key)

            if self.player.controller.up:
                self.player.sprites.current = self.sprites["player"][PUP]
            elif self.player.controller.down:
                self.player.sprites.current = self.sprites["player"][PDOWN]
            elif self.player.controller.left:
                self.player.sprites.current = self.sprites["player"][PLEFT]
            elif self.player.controller.right:
                self.player.sprites.current = self.sprites["player"][PRIGHT]
            self.world.update()
