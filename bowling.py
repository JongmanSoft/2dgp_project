from pico2d import *
from math import sin,cos,radians
import server

turn = 0
def break_test(x1,y1,size,x2,y2,w,h):
    # 첫 번째 객체의 경계를 계산
    x1_min = x1 - size / 2
    x1_max = x1 + size / 2
    y1_min = y1 - size / 2
    y1_max = y1 + size / 2

    # 두 번째 객체의 경계를 계산
    x2_min = x2 - w / 2
    x2_max = x2 + w / 2
    y2_min = y2 - h / 2
    y2_max = y2 + h / 2

    # 충돌 여부를 확인
    if (x1_max >= x2_min and x1_min <= x2_max) and (y1_max >= y2_min and y1_min <= y2_max):
        return True
    else:
        return False

class my_ball:
    global turn
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
        if (n != 0 and n<3): add = 60
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
    global turn
    animation =0
    run = 1
    state = 0
    score = [[0, 0] for _ in range(10)]

    add = 1
    def __init__(self):
        self.font = load_font('resource/떡볶이체.ttf', 25)
        self.board = load_image('resource/score_borad.png')
        self.bgm = load_music('resource/battle.mp3')
        self.bgm.set_volume(32)
        self.wavss = [load_wav(('resource/fall.wav')), load_wav('resource/rolling.wav')]
        self.wavss[0].set_volume(64);self.wavss[1].set_volume(64)
        self.back = load_image('resource/bowling_back.png')
        self.pin = load_image('resource/pin.png')
        self.arrow = load_image('resource/ball_dir.png')
        self.balls = [my_ball()]
        self.Pin = pins()
        pass


    def enter(self):
        self.bgm.repeat_play()
        pass

    def exit(self):
        self.bgm.stop()
        pass


    def update(self):
        global turn


        if (self.state==0):
            self.balls[0].dir += 10* self.add
            if (self.balls[0].dir > 150): self.add = -1
            if (self.balls[0].dir < 30 ): self.add =  1


        for ball in self.balls:
            global turn
            ball.update()
            if (ball.y > 320):
                ball.x = 400;ball.y = 100;self.state = 0;ball.speed =0;ball.frame=0
                turn_score = 0
                if (turn % 2 == 0):
                    for p in self.Pin.data:
                        if (p.frame == 2):
                            p.frame =3
                            turn_score += 1
                        if (p.frame == 1): p.frame = 0
                else :
                    for p in self.Pin.data:
                        if (p.frame == 2):
                            p.frame =0
                            turn_score += 1
                        else: p.frame = 0
                self.score[turn//2][turn%2] = turn_score
                turn += 1


        for p in self.Pin.data:
            if (break_test(self.balls[0].x,self.balls[0].y,self.balls[0].size,p.x,p.y,p.w,p.h)):
                if (p.frame<2):p.frame +=1 ;self.wavss[0].play()

        if (turn ==20):
            sum = 0
            for j in range(0, 10):
                sum += self.score[j][0] + self.score[j][1]
            server.bow_my_score =sum
            self.run = 0

        pass

    def draw(self):
        self.back.draw(400,300)
        self.Pin.draw()
        for ball in self.balls:
            ball.draw()
        if (self.state == 0):self.arrow.clip_composite_draw(0,0,100,290,radians(self.balls[0].dir-90),'h',400,75,100,290)
        self.board.draw(400,540)
        for i in range(0,10):
            if (i>turn//2):break
            for j in range (0,2):
                self.font.draw(10+40*((2*i)+j), 540,str(self.score[i][j]), (255,255,255))

        for i in range (0,10):
            if (i> turn//2):break
            sum = 0
            for j in range(0,i+1):
                sum += self.score[j][0]+ self.score[j][1]
            self.font.draw(20 + 80* i, 500, str(sum), (255, 255, 255))

        pass


    def handle_events(self):

        events = get_events()
        for event in events:
            if event.type ==SDL_KEYDOWN and event.key == SDLK_UP:
                server.bow_my_score = 100
                self.run = 0
            if event.type ==SDL_KEYDOWN and event.key == SDLK_DOWN:
                server.bow_my_score = 0
                self.run = 0
            if event.type == SDL_MOUSEMOTION:
                pass
            if event.type == SDL_MOUSEBUTTONDOWN and event.button ==1:
                self.wavss[1].play()
                self.state = 1
                self.balls[0].speed = 8

                pass


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

