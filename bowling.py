from pico2d import *
from math import sin,cos,radians

class my_ball:
    def __init__(self):
        self.sprite = load_image('resource/my_ball.png')
        self.x = 400
        self.y = 100
        self.dir = 90
        self.frame = 0
        self.speed = 0
    def draw(self):
        self.sprite.clip_composite_draw(self.frame*50,0,50,50,0, 'h',self.x,self.y,200-(self.y/2),200-(self.y/2))
    def update(self):
        if not(self.speed == 0):
            self.frame += 1
            self.frame = self.frame%6
            if (self.x>self.y and self.x< 800-self.y):self.x += cos(radians(self.dir))*self.speed
            elif (self.x >400):self.x -= self.y/300 * self.speed
            else : self.x +=self.y/300 * self.speed

            self.y += sin(radians(self.dir))*self.speed

        pass

class pins:
    def __init__(self):
        self.sprite = load_image('resource/pin.png')


class bowling_scene:
    animation =0
    run = 1
    state = 0
    add = 1

    def __init__(self):
        self.back = load_image('resource/bowling_back.png')
        self.pin = load_image('resource/pin.png')
        self.arrow = load_image('resource/ball_dir.png')
        self.balls = [my_ball()]
        pass


    def enter(self):
        pass

    def exit(self):
        pass


    def update(self):
        if (self.state==0):
            self.balls[0].dir += 10* self.add
            if (self.balls[0].dir > 150): self.add = -1
            if (self.balls[0].dir < 30 ): self.add =  1


        for ball in self.balls:
            ball.update()
            if (ball.y > 320): ball.x = 400;ball.y = 100;self.state = 0;ball.speed =0;ball.frame=0
        pass

    def draw(self):
        self.back.draw(400,300)
        for ball in self.balls:
            ball.draw()
        if (self.state == 0):self.arrow.clip_composite_draw(0,0,100,290,radians(self.balls[0].dir-90),'h',400,75,100,290)
        pass


    def handle_events(self):

        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEMOTION:
                pass
            if event.type == SDL_MOUSEBUTTONDOWN and event.button ==1:
                self.state = 1
                self.balls[0].speed = 5

                pass


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

