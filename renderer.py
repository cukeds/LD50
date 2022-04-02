import sdl2.ext as ext


class Renderer(ext.SoftwareSpriteRenderSystem):
    def __init__(self, window):
        super(Renderer, self).__init__(window)

    def render(self, components):
        ext.fill(self.surface, ext.Color(0, 0, 0))
        super(Renderer, self).render(components)
