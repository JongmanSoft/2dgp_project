from pico2d import *
import title
import text_scene
import air_hockey_scene
import bowling
import basket_ball
open_canvas(800, 600)
current_scene = 0
scene = [title.Title(), text_scene.text_scene(), air_hockey_scene.air_hockey_scene()]
T = text_scene.text_scene()

scene[0].enter()
while True:
    clear_canvas()
    scene[current_scene].draw()
    scene[current_scene].handle_events()
    scene[current_scene].update()
    delay(0.05)
    update_canvas()
    if (scene[current_scene].running() == 0):
        current_scene += 1
        scene[current_scene].enter()

