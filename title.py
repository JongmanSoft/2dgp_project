from pico2d import *


class Title:
    animation =0
    run = 1
    def __init__(self):
        self.bgm = load_music('resource/title_bgm.mp3')
        self.click = load_music('resource/home.wav')
        self.title_art = [load_image('resource/title_art.png'),400,300]
        self.title_polygon = [load_image('resource/title_polygon.png'),600,300]
        self.title_name = [load_image('resource/title_name.png'),500,200]
        self.title_sub = [load_image('resource/title_sub.png'),500,100]

    def enter(self):

        self.bgm.repeat_play()

    def exit(self):
        self.bgm.stop()
        self.run = 0


    def update(self):
        if self.animation > 0:
            if self.animation > 40:
                self.exit()
            else :
                self.title_polygon[1] += 10
                self.title_name[1] += 20
                self.title_sub[1] += 20
                self.animation += 1

    def draw(self):
        self.title_art[0].draw(self.title_art[1], self.title_art[2])
        self.title_polygon[0].draw(self.title_polygon[1], self.title_polygon[2],400,800)
        self.title_name[0].draw(self.title_name[1], self.title_name[2])
        self.title_sub[0].draw(self.title_sub[1], self.title_sub[2])

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == 1:
                self.animation = 1
                self.click.play()

    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass


