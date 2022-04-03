import sdl2.ext as ext
from sdl2.ext import SoftwareSpriteRenderSystem, Applicator, Window
from sdl2 import rect, video, surface

from movement import Position


class RendererSystem(Applicator):
    def __init__(self, window):
        super(RendererSystem, self).__init__()
        self.componenttypes = Position, Sprites

        if isinstance(window, Window):
            self.window = window.window
        elif isinstance(window, video.SDL_Window):
            self.window = window
        else:
            raise TypeError("unsupported window type")
        self.target = window
        sfc = video.SDL_GetWindowSurface(self.window)
        if not sfc:
            raise AssertionError("SDL error when creating renderer")
        self.surface = sfc.contents
        self.clear_color = ext.Color(0, 0, 0)

    def process(self, world, component_sets):
        ext.fill(self.surface, self.clear_color)

        r = rect.SDL_Rect(0, 0, 0, 0)
        for position, sprites in component_sets:
            sprite = sprites.current
            r.x = position.x
            r.y = position.y
            surface.SDL_BlitSurface(sprite.surface, None, self.surface, r)

        video.SDL_UpdateWindowSurface(self.window)


class Sprites:
    def __init__(self, sprites, index=0):
        self.current = sprites[index]
        self.sprites = sprites
