from pico2d import *

import server
import random


class text_scene:
    run = 1
    def __init__(self,round =0):
        self.bgm =load_music('resource/talk.mp3')
        self.click = load_music('resource/click.wav')
        self.font = load_font('resource/떡볶이체.ttf',25)

        self.back_image = []
        self.girl_image = []
        self.text = []
        for i in range (0, 2):
            file_name = "back" + str(i) + ".png"
            self.back_image.append(load_image("resource/"+file_name))
        for i in range (0,9):
            file_name = "a" + str(i) + ".png"
            self.girl_image.append(load_image("resource/"+file_name))
        self.window = load_image("resource/"+"text_window.png")
        if (round ==0):
            self.text.append((0,"주인공","후... 떨리는걸?",1))
            self.text.append((0, "주인공", "오늘은 내가 좋아하는 아현이에게 고백하는날이야.", 1))
            self.text.append((0, "주인공", "앗...아현이다!", 1))
            self.text.append((0,"박아현","인공아 안녕!", 0))
            self.text.append((2, "박아현", "오늘 갑자기 왜부른거야?", 0))
            self.text.append((0, "주인공", "그...그게 사실...", 1))
            self.text.append((8, "박아현", "응?말을해 말을!!", 0))
            self.text.append((0, "주인공", "아현아...사실 내가 널 좋아하는거 같아!", 1))
            self.text.append((0, "주인공", "그러니 나랑 사귀어주지않을래...?", 1))
            self.text.append((7, "박아현", "뭐...뭐라고?", 0))
            self.text.append((0, "주인공", "(나...차인건가?)", 1))
            self.text.append((4, "박아현", "나랑 사귀고싶니?", 0))
            self.text.append((0, "주인공", "응! 당연하지! 너한테 뭐든지 해줄수있어!", 1))
            self.text.append((4, "박아현", "그럼... 나랑 스포츠게임하지않을래?", 0))
            self.text.append((0, "주인공", "뭐라고...?스포츠게임?", 1))
            self.text.append((3, "박아현", "응! 나 스포츠게임 잘하는 남자가 이상형이거든!", 0))
            self.text.append((3, "박아현", "그니까 일단 나한테 볼링부터 이기셈 ㅋㅋ", 0))
            self.text.append((0, "주인공", "아현이의 이상형이 이렇게 독특할 줄이야... ", 1))
            self.text.append((0, "주인공", "하지만 이겨야 사귈수 있겠지? 반드시 이겨주겠어!", 1))
        if (round >= 1):
            self.text.append((0, "주인공", "여자랑 볼링장을 와보다니...", 1))
            self.text.append((8, "박아현", "뭘 멍때리고 있노?",0))
            self.text.append((0, "주인공", "응...? 아현아 넌 돈 안내?", 1))
            self.text.append((8, "박아현", "난 안칠건데?",0))
            self.text.append((0, "주인공", "?", 1))
            self.text.append((4, "박아현", "당연히 너혼자 쳐야지 내 역대최고기록이나 깨",0))
            self.text.append((0, "주인공", "(아...아현이랑 같이 치는걸 기대했는데)", 1))
            self.text.append((0, "주인공", "넌 몇점인데?", 1))
            server.bow_goal_score = random.randint(50,80)
            self.text.append((8, "박아현", f"{server.bow_goal_score}점인데 ㄱㄴ?",0))
            self.text.append((0, "주인공", "뭐야...", 1))


    def enter(self):
        self.bgm.repeat_play()


    def exit(self):
        server.text_round+=1
        self.bgm.stop()
        self.run =0



    def update(self):

        pass

    def draw(self):
        if (len(self.text) != 0):
            if (server.text_round ==0):self.back_image[0].draw(400,300,800,600)
            if (server.text_round == 1): self.back_image[1].draw(400, 300, 800, 600)
            if (server.text_round >= 2): self.back_image[2].draw(400, 300, 800, 600)
            if self.text[0][3] == 0:
                self.girl_image[self.text[0][0]].draw(400,300)
            self.window.draw(400,100,760,160)
            self.font.draw(70,140,self.text[0][1],(182,23,76))
            self.font.draw(70, 100, self.text[0][2], (0, 23, 76))


    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == 1:
                self.text.pop(0)
                if len(self.text) ==0 :
                    self.run = 0

    def running(self): return self.run


    def pause(self): pass

    def resume(self): pass
