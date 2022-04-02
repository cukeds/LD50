import sdl2 as sdl
import sdl2.ext as ext
from world import World
from player import Player
from config import *

RESOURCES = ext.Resources(__file__, "res")


ext.init()
def load(factory):
    sprite_names = ["player_down.png", "player_left.png", "player_up.png", "player_right.png"]
    sprites = []
    for sprite in sprite_names:
        sprites.append(factory.from_image(RESOURCES.get_path(sprite)))

    return sprites

def run():
    window = ext.Window("Test", size=(WIDTH, HEIGHT))
    factory = ext.SpriteFactory(ext.SOFTWARE)
    window.show()
    running = True

    sprites = load(factory)

    world = World(window)

    player = Player(world, sprites)

    while running:

        window.refresh()

        events = ext.get_events()
        for event in events:
            if event.type == sdl.SDL_QUIT:
                running = False
            if event.type == sdl.SDL_KEYDOWN:
                player.controller.handle_keydown(event.key)
            if event.type == sdl.SDL_KEYUP:
                player.controller.handle_keyup(event.key)


        if player.controller.up:
            player.sprites.current = sprites[PUP]
        elif player.controller.down:
            player.sprites.current = sprites[PDOWN]
        elif player.controller.left:
            player.sprites.current = sprites[PLEFT]
        elif player.controller.right:
            player.sprites.current = sprites[PRIGHT]
        player.update()
        world.update()


if __name__ == "__main__":
    run()
