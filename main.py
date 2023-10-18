from pico2d import *
open_canvas(800, 600)
title = load_image('resource/title_art.png')
title_bgm =load_music('resource/title_bgm.mp3')
title_bgm.repeat_play()
while True:
    clear_canvas()
    title.draw(400,300,800,600)
    update_canvas()