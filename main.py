from pico2d import *
import title
import text_scene
open_canvas(800, 600)
current_scene = 0
scene = [title.Title(), text_scene.text_scene()]
T = text_scene.text_scene()

scene[0].enter()
while True:
    clear_canvas()
    scene[current_scene].draw()
    scene[current_scene].update()
    scene[current_scene].handle_events()
    delay(0.05)
    if (scene[current_scene].running() == 0):
        current_scene += 1
        scene[current_scene].enter()
    update_canvas()
