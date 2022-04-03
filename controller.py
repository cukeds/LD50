class Controller:
    W = 119
    A = 97
    S = 115
    D = 100

    def __init__(self, up=W, down=S, left=A, right=D):
        self._up_key = up
        self._down_key = down
        self._left_key = left
        self._right_key = right

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def handle_keyup(self, event):
        if event.keysym.sym == self._left_key:
            self.left = False
        elif event.keysym.sym == self._right_key:
            self.right = False

        if event.keysym.sym == self._up_key:
            self.up = False
        elif event.keysym.sym == self._down_key:
            self.down = False

    def handle_keydown(self, event):
        if event.keysym.sym == self._left_key:
            self.left = True
        elif event.keysym.sym == self._right_key:
            self.right = True

        if event.keysym.sym == self._up_key:
            self.up = True
        elif event.keysym.sym == self._down_key:
            self.down = True


class ControllerV2:
    W = 119
    A = 97
    S = 115
    D = 100

    def __init__(self, entity, up=W, down=S, left=A, right=D):
        self.entity = entity
        self._up_key = up
        self._down_key = down
        self._left_key = left
        self._right_key = right

        self.x = 0
        self.y = 0

        if 'execute' not in entity.__dir__():
            raise Exception("'Entity' object must have an 'execute' method that takes X and Y (direction of movement "
                            "with modulus 1) as arguments.")

    def handle_keyup(self, event):
        if event.keysym.sym == self._left_key:
            self.x = 0
        if event.keysym.sym == self._right_key:
            self.x = 0

        if event.keysym.sym == self._up_key:
            self.y = 0
        elif event.keysym.sym == self._down_key:
            self.y = 0

    def handle_keydown(self, event):
        if event.keysym.sym == self._left_key:
            self.x = -1
        elif event.keysym.sym == self._right_key:
            self.x = 1

        if event.keysym.sym == self._up_key:
            self.y = -1
        elif event.keysym.sym == self._down_key:
            self.y = 1

    def update(self):
        self.entity.execute(self.x, self.y)

