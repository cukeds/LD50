import sdl2 as sdl
import sdl2.ext as ext

from world import World
from player import Player

RESOURCES = ext.Resources(__file__, "res")

ext.init()
window = ext.Window("Test", size=(800, 600))

factory = ext.SpriteFactory(ext.SOFTWARE)
spriterenderer = factory.create_sprite_render_system(window)


def run():
    window.show()
    running = True

    sprite = factory.from_image(RESOURCES.get_path("player.png"))
    spriterenderer.render(sprite)

    world = World(window)

    player = Player(world, sprite)

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

        player.update()
        world.process()


if __name__ == "__main__":
    run()
