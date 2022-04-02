import sys
from sdl2 import ext

ext.init()

window = ext.Window("Hello", (640, 800))
window.show()

input()