from pico2d import *

class Title:
    def __init__(self):
        bgm = load_music('resource/title_bgm.mp3')
        title_art = [load_image('resource/title_art.png'),400,300]
        title_polygon = [load_image('resource/title_polygon.png'),400,300]
        title_name =  [load_image('resource/title_name.png'),200,200]
        title_sub =  [load_image('resource/title_sub.png'),200,100]
    def render(self):


