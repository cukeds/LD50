import sdl2.ext as ext
from sdl2.ext import SoftwareSpriteRenderSystem, Applicator

from movement import Position


class Renderer(SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(Renderer, self).__init__(window)

    def render(self, components, x=None, y=None):
        # x and y are offsets to render sprites relative to
        ext.fill(self.surface, ext.Color(0, 0, 0))
        super(Renderer, self).render(components, x, y)


class RendererSystem(Applicator):
    def __init__(self, window):
        super(RendererSystem, self).__init__()
        self.renderer = Renderer(window)
        self.my_components = []
        self.componenttypes = Position, Sprites

    def process(self, world, component_sets):
        to_render = []
        for position, sprites in component_sets:
            sprite = sprites.current
            sprite.x = position.x
            sprite.y = position.y

            to_render.append(sprite)

        self.renderer.render(to_render)


class Sprites:
    def __init__(self, sprites, index=0):
        self.current = sprites[index]
        self.sprites = sprites
