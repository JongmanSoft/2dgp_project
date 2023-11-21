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
        self.size = (200-(self.y/2))/2
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


class pin:
    def __init__(self,n):
        if (n==0):self.size = 4
        elif (n<3): self.size =3
        elif (n<6): self.size =2
        else : self.size = 1
        add = 0
        if (n ==0): add = 30
        if (n != 0and n<3): add = 60
        if (n >2 and n < 6): add = 50

        self.x =add+ 280+self.size*50 + (n - (7-self.size)) *40
        self.y = (4-self.size)*20 + 250
        self.frame = 0
        self.w = ((self.size+5)*6)/2
        self.h = ((self.size+5)*13)/2
class pins:
    def __init__(self):
        self.sprite = load_image('resource/pin.png')
        self.data = [pin(i)for i in range(10)]

    def draw(self):
        for p in range(9,-1,-1):
            self.sprite.clip_composite_draw(self.data[p].frame*30,0,30,65,0,'h',self.data[p].x,self.data[p].y,(self.data[p].size+5)*6,(self.data[p].size+5)*13)


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
        self.Pin = pins()
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
        self.Pin.draw()
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

