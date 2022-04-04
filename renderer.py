from sdl2.ext import Applicator, Window, fill, Color
from sdl2.ext.common import SDLError
from sdl2 import video, rect, surface

from movement import Position


class Renderer(Applicator):
    def __init__(self, window):
        super(Renderer, self).__init__()
        if isinstance(window, Window):
            self.window = window
        else:
            raise TypeError("unsupported window type")
        self.target = window
        sfc = video.SDL_GetWindowSurface(self.window.window)
        if not sfc:
            raise SDLError()
        self.surface = sfc.contents
        self.componenttypes = Position, Sprites
        self.clear_color = Color(200, 30, 230)
        self.background = None

    def process(self, world, components):
        fill(self.surface, self.clear_color)
        r = rect.SDL_Rect(0, 0, 0, 0)

        w, h = self.window.size
        r.w = w
        r.h = h
        surface.SDL_BlitSurface(self.background.surface, None, self.surface, r)

        sorted_components = sorted(components, key=lambda component: component[1].current.depth)

        for position, sprites in sorted_components:
            sprite = sprites.current
            r.x = position.x
            r.y = position.y
            surface.SDL_BlitSurface(sprite.surface, None, self.surface, r)
        video.SDL_UpdateWindowSurface(self.window.window)


class Sprites:
    def __init__(self, sprites, index=0):
        self.current = sprites[index]
        self.sprites = sprites



    def copy(self):
        return [s.subsprite((0, 0, s.size[0], s.size[1])) for s in self.sprites]
