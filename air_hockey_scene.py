from pico2d import *


class puck:
    def __init__(self):
        self.sprite = load_image('resource/puck.png')
        self.x = 400
        self.y = 300
        self.xdir = 0
        self.ydir = 0
        self.speed = 0

    def draw(self):
        self.sprite.draw(self.x, self.y)

    def update(self):
        self.x = self.x + (self.xdir//100)
        self.y = self.y + (self.ydir//100)
        if (self.x > 600):self.xdir = -abs(self.xdir)
        if (self.x < 200): self.xdir = abs(self.xdir)
        if (self.y > 540 ):self.ydir = -abs(self.ydir)
        if (self.y < 60): self.ydir = abs(self.ydir)



class my_handle:
    def __init__(self):
        self.sprite = load_image('resource/my_handle.png')
        self.x = 400
        self.y = 100
        self.dir = 0
        self.speed = 0
        self.sx = 0
        self.sy = 0
        self.time = get_time()
    def draw(self):
        self.sprite.draw(self.x, self.y)
    def update(self):
        if self.time+2 < get_time():
            self.time = get_time()
            self.sx = self.x
            self.sy = self.y
        pass

class you_handle:
    def __init__(self):
        self.sprite = load_image('resource/you_handle.png')
        self.x = 400
        self.y = 500
        self.dir = 0
        self.speed = 0

    def update(self):
        pass

    def draw(self):
        self.sprite.draw(self.x, self.y)

class air_hockey_scene:
    animation =0
    run = 1
    click = 0
    def __init__(self):
        self.bgm = load_music('resource/battle.mp3')
        self.back =[load_image('resource/draw_back.png') ,load_image('resource/win_back.png'),load_image('resource/lose_back.png')]
        self.objects = [puck(), my_handle(), you_handle()]


    def enter(self):
        self.bgm.repeat_play()

    def exit(self):
        self.bgm.stop()
        self.run = 0


    def update(self):
        if (self.objects[1].x > self.objects[0].x-25 and self.objects[1].x < self.objects[0].x +25):
            if (self.objects[1].y > self.objects[0].y - 25 and self.objects[1].y < self.objects[0].y + 25):
                self.objects[0].xdir = self.objects[1].x -self.objects[1].sx
                self.objects[0].ydir = self.objects[1].y - self.objects[1].sy

        for o in self.objects:
            o.update()
        pass

    def draw(self):
        self.back[0].draw(400,300)
        for o in self.objects:
            o.draw()


    def handle_events(self):

        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button ==1 :

                self.click = 1
            if event.type == SDL_MOUSEMOTION and self.click == 1:
                self.objects[1].x = event.x
                if (event.x < 190): self.objects[1].x = 190
                if (event.x> 610):self.objects[1].x = 610
                self.objects[1].y = 600-event.y
                if (event.y < 300):self.objects[1].y = 300
                if (event.y > 550):self.objects[1].y = 50
            if event.type == SDL_MOUSEBUTTONUP and event.button ==1:
                self.click = 0


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

