from pico2d import *
import title
import text_scene
open_canvas(800, 600)
current_scene = 0
scene = [title.Title()]
T = text_scene.text_scene()

T.enter()
while True:
    clear_canvas()
    T.draw()
    T.update()
    T.handle_events()
    delay(0.05)
    update_canvas()
