from pico2d import *
import title
open_canvas(800, 600)

T = title.Title()

T.enter()
while True:
    clear_canvas()
    T.draw()
    update_canvas()