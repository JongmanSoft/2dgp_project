from pico2d import *
import server

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
        self.x = self.x + (self.xdir//10)
        self.y = self.y + (self.ydir//10)
        if (self.x > 600):self.x = 600;self.xdir = -abs(self.xdir)
        if (self.x < 200):self.x = 200; self.xdir = abs(self.xdir)
        if (self.y > 540 ):self.y = 540;self.ydir = -abs(self.ydir)
        if (self.y < 60): self.y =60; self.ydir = abs(self.ydir)

        if (self.x >= 335 and self.x<=455 and self.y>520): self.x = 400; self.y = 300; server.a_my_score +=1
        if (self.x >= 335 and self.x <= 455 and self.y < 80): self.x = 400; self.y = 300; server.a_you_score += 1



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
        self.sx = 400
        self.sy = 500
        self.cx = 0
        self.cy = 0
        self.dir = 0
        self.speed = 0
        self.t = 0
        self.attack = 0


    def update(self):
        if (self.x > 600):self.x = 600
        if (self.x < 200): self.x = 200
        if (self.y > 540 ):self.y = 540
        if (self.y < 300): self.y = 300
        pass
    def move(self,px,py):

        if (self.attack == 0):
            self.t+= 0.1
            self.x = (1-self.t)*self.sx + self.t*px
            self.y = (1 - self.t) * self.sy + self.t * py
            if (self.t >= 1 or (px -25 < self.x and px +25 > self.x and py -25 <self.y and py+25>self.y)): self.cx = self.x ; self.cy = self.y ;self.t = 0; self.attack =1
        if (self.attack == 1):
            self.t += 0.1
            self.x = (1 - self.t) * self.cx + self.t * 400
            self.y = (1 - self.t) * self.cy + self.t * 500
            if (self.t >= 1): self.t = 0; self.attack = 0
            pass

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
        self.font = load_font('resource/떡볶이체.ttf', 50)
        self.font = load_font('resource/떡볶이체.ttf', 54)


    def enter(self):
        self.bgm.repeat_play()

    def exit(self):
        self.bgm.stop()
        self.run = 0


    def update(self):
        if (self.objects[0].y>300 and self.objects[0].y<450 ):self.objects[2].move(self.objects[0].x ,self.objects[0].y)
        else: self.objects[2].attack=0

        if (self.objects[1].x >= self.objects[0].x-30 and self.objects[1].x <= self.objects[0].x +30 ):
            if (self.objects[1].y >= self.objects[0].y -30 and self.objects[1].y <= self.objects[0].y + 30):
                dis =[self.objects[0].x - self.objects[1].x,self.objects[0].y - self.objects[1].y]
                self.objects[0].x += dis[0]
                self.objects[0].y += dis[1]
                self.objects[0].xdir = self.objects[1].x -self.objects[1].sx
                self.objects[0].ydir = self.objects[1].y - self.objects[1].sy
        if (self.objects[2].x >= self.objects[0].x-30 and self.objects[2].x <= self.objects[0].x +30):
            if (self.objects[2].y >= self.objects[0].y -30 and self.objects[2].y <= self.objects[0].y +30):

                dis =[self.objects[0].x - self.objects[2].x,self.objects[0].y - self.objects[2].y]
                print(f"{dis}")
                self.objects[0].x += dis[0]
                self.objects[0].y += dis[1]
                self.objects[0].xdir = (self.objects[2].x - self.objects[2].sx)*2
                self.objects[0].ydir = (self.objects[2].y - self.objects[2].sy)*2



        for o in self.objects:
            o.update()

        if (server.a_you_score >= 10 or server.a_my_score<= 10):
            self.run = 0
        pass

    def draw(self):

        if (server.a_my_score == server.a_you_score):self.back[0].draw(400,300)
        elif(server.a_my_score > server.a_you_score):self.back[1].draw(400,300)
        else :self.back[2].draw(400, 300)
        for o in self.objects:
            o.draw()
        self.font.draw(102, 302, str(server.a_you_score), (255, 255, 255))
        self.font.draw(98, 302, str(server.a_you_score), (255, 255, 255))
        self.font.draw(102, 298, str(server.a_you_score), (255, 255, 255))
        self.font.draw(98, 298, str(server.a_you_score), (255,255,255))
        self.font.draw(100, 300, str(server.a_you_score), (233, 16, 81))
        self.font.draw(702, 298, str(server.a_my_score), (255, 255, 255))
        self.font.draw(698, 298, str(server.a_my_score), (255, 255, 255))
        self.font.draw(702, 302, str(server.a_my_score), (255, 255, 255))
        self.font.draw(698, 302, str(server.a_my_score), (255, 255, 255))
        self.font.draw(700, 300, str(server.a_my_score), (26, 111, 168))


    def handle_events(self):

        events = get_events()
        for event in events:

            if event.type == SDL_MOUSEMOTION:
                self.objects[1].x = event.x
                if (event.x < 190): self.objects[1].x = 190
                if (event.x> 610):self.objects[1].x = 610
                self.objects[1].y = 600-event.y
                if (event.y < 300):self.objects[1].y = 300
                if (event.y > 550):self.objects[1].y = 50
            if event.type == SDL_MOUSEBUTTONUP and event.button == 1:
                self.click = 0
            if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                self.run = 0
            if event.type ==SDL_KEYDOWN and event.key == SDLK_UP:
                server.a_my_score = 10 ; server.a_you_score = 0
                self.run = 0
            if event.type ==SDL_KEYDOWN and event.key == SDLK_DOWN:
                server.a_my_score = 0 ; server.a_you_score = 10
                self.run = 0


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

