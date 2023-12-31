from pico2d import *
from math import radians,cos,sin,atan2,degrees,sqrt
import server
time = 0

shut = 0
def calculate_angle(x1, y1, x2, y2):

    x2 -= x1
    y2 -= y1

    angle_rad = atan2(y2, x2)

    if angle_rad < 0:
        angle_rad += 2 * 3.141592653589793


    angle_deg = degrees(angle_rad)

    return angle_deg

class goal:
    def __init__(self):
        self.sprite = [load_image('resource/goaldae.png'),load_image('resource/ring.png')]
        self.x = 400
        self.dir = 1
    def update(self):
        global time
        time_speed = time
        if (time > 3):time_speed = 3
        self.x += (1+time/10.0)*self.dir*server.frame_time
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
        self.speed = 0
        self.frame = 0

    def update(self):
        if (self.speed != 0):
            self.frame = (self.frame +server.frame_time*15)%6
            if (self.z > 80):
                self.x += cos(radians(self.dir)) * server.frame_time*200*4
                self.y += sin(radians(self.dir)) * server.frame_time*200*4
                self.z -= self.speed*4 *server.frame_time*20
            else:
                global shut
                self.y -= server.frame_time*200 * 10
                if (self.y < 0) : self.x =400; self.y = 100; self.z = 200;self.speed = 0;self.dir = 90;shut = 0

    def draw(self):
        self.sprite.clip_composite_draw(100*int(self.frame),0,100,100,radians(self.dir-90),'0',self.x ,self.y ,self.z,self.z)


class basket_ball_scene:
    animation =0
    run = 1
    def __init__(self):
        self.back = load_image('resource/basketball_background.png')
        self.bgm = load_music('resource/battle.mp3')
        self.wavs = [load_wav('resource/shoot.wav'),load_wav('resource/goal.mp3')]
        self.wavs[0].set_volume(20)
        self.font = load_font('resource/떡볶이체.ttf', 25)

        self.goal_dae = goal()
        self.balls= [ball()]

        self.start = None
        pass


    def enter(self):
        self.start= get_time()
        self.bgm.repeat_play()
        pass

    def exit(self):
        pass


    def update(self):
        global time
        global shut
        time += 1
        self.goal_dae.update()
        for b in self.balls:
            b.update()
        if (self.balls[0].z<=80 and self.balls[0].x>self.goal_dae.x-50 and self.balls[0].x<self.goal_dae.x+50 and self.balls[0].y<600-194 and self.balls[0].y > 600-205 and  shut ==0): shut = 1;server.bask_my_score += 1 ; self.wavs[1].play()

        pass

    def draw(self):

        self.back.draw(400,300)

        self.goal_dae.draw()
        if (self.balls[0].z>80):self.goal_dae.ring_draw()
        for b in self.balls:
            b.draw()
        if (self.balls[0].z <= 80): self.goal_dae.ring_draw()

        self.font.draw(70, 560, f"time : {int(60 - (get_time() - self.start))}", (0, 0, 0))
        self.font.draw(70, 520, f"score : {server.bask_my_score}", (0, 0, 0))
        pass


    def handle_events(self):
        sx ,sy =0,0
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_UP:
                server.bask_my_score = 99
                self.run = 0
            if event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
                server.bask_my_score = 0
                self.run = 0
            if event.type == SDL_MOUSEBUTTONDOWN and event.button ==1 :
                sx = event.x
                sy = 600-event.y
                pass
            if event.type == SDL_MOUSEMOTION:
                pass
            if event.type == SDL_MOUSEBUTTONUP and event.button ==1:
                self.wavs[0].play()
                self.balls[0].dir = 2* calculate_angle(sx,sy,event.x,600-event.y)
                self.balls[0].speed = 3
                pass
        if (60-(get_time()-self.start) <= 0):
            self.run = 0


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

