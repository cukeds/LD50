import sys
import sdl2 as sdl
import sdl2.ext as ext

RESOURCES = ext.Resources(__file__, "res")

ext.init()
window = ext.Window("Test", size=(800, 600))

factory = ext.SpriteFactory(ext.SOFTWARE)
spriterenderer = factory.create_sprite_render_system(window)

def run():
    window.show()
    running = True

    sprite = factory.from_image(RESOURCES.get_path("sonic.png"))
    spriterenderer.render(sprite)

    while running:

        window.refresh()

        events = ext.get_events()
        for event in events:
            if event.type == sdl.SDL_QUIT:
                print("Quiting", running)
                running = False


if __name__ == "__main__":
    run()
