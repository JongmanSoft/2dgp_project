from pico2d import *
from math import radians,cos,sin
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
    def draw(self):
        self.sprite[0].draw(self.x,300)
    def ring_draw(self):
        self.sprite[1].draw(self.x,300)

class ball:
    def __init__(self):
        self.sprite = load_image('resource/basketball.png')
        self.x = 400
        self.y = 100
        self.z = 200
        self.dir = 90
        self.speed = 1
        self.frame = 0
    def update(self):
        if (self.speed != 0):
            self.frame += 1
            self.frame = self.frame%6
            if (self.z > 80):
                self.x += cos(self.dir) * self.speed * 15
                self.y += sin(self.dir) * self.speed * 15
                self.z -= self.speed*4
            else:
                self.y -= sin(self.dir) * self.speed * 10

    def draw(self):
        self.sprite.clip_composite_draw(100*self.frame,0,100,100,radians(self.dir-90),'0',self.x ,self.y ,self.z,self.z)


class basket_ball_scene:
    animation =0
    run = 1
    def __init__(self):
        self.back = load_image('resource/basketball_background.png')
        self.goal_dae = goal()
        self.balls= [ball()]
        pass


    def enter(self):
        pass

    def exit(self):
        pass


    def update(self):
        global time
        time += 1
        self.goal_dae.update()
        for b in self.balls:
            b.update()
        pass

    def draw(self):
        self.back.draw(400,300)
        self.goal_dae.draw()
        if (self.balls[0].z>80):self.goal_dae.ring_draw()
        for b in self.balls:
            b.draw()
        if (self.balls[0].z <= 80): self.goal_dae.ring_draw()
        pass


    def handle_events(self):

        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button ==1 :
                print(self.balls[0].z)
                pass
            if event.type == SDL_MOUSEMOTION:
                pass
            if event.type == SDL_MOUSEBUTTONUP and event.button ==1:
                pass


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

