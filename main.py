from pico2d import *
import title
import text_scene
import air_hockey_scene
import bowling
import basket_ball
import game_framework
import server
import time
open_canvas(800, 600)
current_scene = 0
scene = [title.Title(), text_scene.text_scene(0),text_scene.text_scene(1),bowling.bowling_scene(),text_scene.text_scene(2), air_hockey_scene.air_hockey_scene(),text_scene.text_scene(3),basket_ball.basket_ball_scene(),text_scene.text_scene(4)]
#scene = [ bowling.bowling_scene()]
T = text_scene.text_scene()
game_roop =1
scene[0].enter()

while game_roop:
    clear_canvas()
    scene[current_scene].draw()
    scene[current_scene].handle_events()
    scene[current_scene].update()
    server.frame_time= time.time() - server.current_time
    server.current_time += server.frame_time
    update_canvas()
    if (scene[current_scene].running() == 0):
        if (current_scene == 8):
            game_roop =0
        scene[current_scene].exit()
        current_scene += 1
        scene[current_scene].enter()

close_canvas()