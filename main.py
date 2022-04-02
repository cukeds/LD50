import sys
from sdl2 import ext as sdl

RESOURCES = sdl.Resources(__file__, "res")

sdl.init()

window = sdl.Window("Hello", (640, 800))
window.show()


factory = sdl.SpriteFactory(sdl.SOFTWARE)
sprite = factory.from_image(RESOURCES.get_path("sonic.png"))

spriterenderer = factory.create_sprite_render_system(window)
spriterenderer.render(sprite)
