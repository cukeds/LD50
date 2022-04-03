from sdl2.ext import Applicator, Window, fill, Color
from sdl2.ext.common import SDLError
from sdl2 import video, rect, surface

from movement import Position


class Renderer(Applicator):
    def __init__(self, window):
        super(Renderer, self).__init__()
        if isinstance(window, Window):
            self.window = window.window
        elif isinstance(window, video.SDL_Window):
            self.window = window
        else:
            raise TypeError("unsupported window type")
        self.target = window
        sfc = video.SDL_GetWindowSurface(self.window)
        if not sfc:
            raise SDLError()
        self.surface = sfc.contents
        self.componenttypes = Position, Sprites
        self.clear_color = Color(0, 0, 0)

    def process(self, world, components):
        fill(self.surface, self.clear_color)
        r = rect.SDL_Rect(0, 0, 0, 0)

        sorted_components = sorted(components, key=lambda component: component[1].current.depth)

        for position, sprites in sorted_components:
            sprite = sprites.current
            r.x = position.x
            r.y = position.y
            surface.SDL_BlitSurface(sprite.surface, None, self.surface, r)
        video.SDL_UpdateWindowSurface(self.window)


class Sprites:
    def __init__(self, sprites, index=0):
        self.current = sprites[index]
        self.sprites = sprites

    def copy(self):
        return [s.subsprite((0, 0, s.size[0], s.size[1])) for s in self.sprites]
