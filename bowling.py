from pico2d import *

class my_ball:
    def __init__(self):
        self.sprite = load_image('resource/my_ball.png')
        self.x = 400
        self.y = 100
        self.dir = 0
        self.frame = 0
        self.speed = 1
    def draw(self):
        self.sprite.clip_composite_draw(self.frame*100,0,100,100,self.dir,0,self.x,self.y,200-(self.y/10),200-(self.y/10))
    def update(self):
        if not(self.speed == 0):
            self.frame += 1
            self.frame = self.frame%6
        pass


class bowling_scene:
    animation =0
    run = 1
    def __init__(self):
        self.back = load_image('resource/bowling_back.png')
        self.balls = [my_ball()]
        pass


    def enter(self):
        pass

    def exit(self):
        pass


    def update(self):

        pass

    def draw(self):
        pass


    def handle_events(self):

        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button ==1 :
                pass
            if event.type == SDL_MOUSEMOTION:
                pass
            if event.type == SDL_MOUSEBUTTONUP and event.button ==1:
                pass


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

