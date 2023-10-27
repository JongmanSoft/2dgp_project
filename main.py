from pico2d import *
import title
open_canvas(800, 600)
current_scene = 0
scene = [title.Title()]
T = title.Title()

T.enter()
while True:
    clear_canvas()
    T.draw()
    T.update()
    T.handle_events()
    delay(0.05)
    update_canvas()
