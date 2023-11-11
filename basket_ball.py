from pico2d import *

time = 0
class goal:
    def __init__(self):
        self.sprite = [load_image('resource/goaldae.png'),load_image('resource/ring.png')]
        self.x = 400
        self.dir = 1
    def update(self):
        global time
        self.x += (1+time/10.0)*self.dir
        if (self.x>650):self.dir = -1
        if (self.x <150):self.dir = 1



class basket_ball_scene:
    animation =0
    run = 1
    def __init__(self):
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

