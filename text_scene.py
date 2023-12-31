from pico2d import *

import server
import random

text_update= [0,0,0,0,0,0,0,0,0,0,0]

class text_scene:
    run = 1
    def __init__(self,round =0):
        self.bgm =load_music('resource/talk.mp3')
        self.click = load_wav('resource/click.wav')
        self.click.set_volume(5)
        self.font = load_font('resource/떡볶이체.ttf',25)
        self.skip = load_image('resource/skip.png')
        self.back_image = []
        self.girl_image = []
        self.text = []
        for i in range (0, 3):
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
        if (round == 1):
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
            self.text.append((0, "주인공", "(뭐야...별거없네)", 1))
            self.text.append((0, "주인공", "(기다려라 박아현! 널 내여자로 만들겠어!)", 1))
        if (round == 3):
            self.text.append((0, "", "게임이 끝났다...", 1))
        if (round== 4):
            self.text.append((0, "", "농구가 끝났다...", 1))
            server.bask_goal_score = random.randint(7,14)
            self.text.append((0,"",f"아현이의 점수는 {server.bask_goal_score}점인가...",1))





    def enter(self):
        self.bgm.repeat_play()


    def exit(self):
        server.text_round+=1
        self.bgm.stop()
        self.run =0



    def update(self):
        if (server.text_round ==2 and text_update[2] == 0):
            if (server.bow_goal_score >= server.bow_my_score):
                self.text.append((2, "박아현", "ㅋㅋㅋㅋ내기록도 못넘으면 어떡하노", 0))
                self.text.append((0, "주인공", "끙...어떡하지", 1))
                self.text.append((3, "박아현", "ㄱㅊ 두판 더할거임", 0))
                self.text.append((0, "주인공", "두..두판을 더?!", 1))
                self.text.append((4, "박아현", "볼링말고ㅋㅋㅋ 다음은 에어하키다 따라와라...", 0))
                self.text.append((0, "주인공", "다...다행이다 끝이아니구나!", 1))
                self.text.append((0, "주인공", "(에어하키에서는 반드시 이겨주겠어!)", 1))
            else :
                server.win +=1

                self.text.append((5, "박아현", "이런젠장!! 내가 지다니!!!", 0))
                self.text.append((0, "주인공", "휴...겨우이겼어", 1))
                self.text.append((3, "박아현", "ㄱㅊ 아직끝아님", 0))
                self.text.append((0, "주인공", "뭐...뭐라고!!!", 1))
                self.text.append((7, "박아현", "진정한 상남자는 에어하키를 할때 드러나지 따라와라", 0))
                self.text.append((0, "주인공", "끝이 아니라니...", 1))
                self.text.append((0, "주인공", "(에어하키에서는 반드시 이겨주겠어!)", 1))
            text_update[2] = 1
        if (server.text_round ==3  and text_update[3] == 0):
            if (server.a_you_score >= server.a_my_score):
                self.text.append((8, "박아현", "개못한다 진짜...", 0))
                self.text.append((0, "주인공", "(흑흑...왜이렇게 어렵지?)", 1))
                self.text.append((7, "박아현", "좀 실망인데...", 0))
                self.text.append((0, "주인공", "아직 안끝났어...!", 1))
                self.text.append((4, "박아현", "옴멈머? 맞앙ㅋ 이제 농구만 하면된다능ㅋ", 0))
                self.text.append((0, "주인공", "이제 마지막 승부야...", 1))
                self.text.append((0, "주인공", "반드시 이길거야!", 1))
            else :
                server.win +=1

                self.text.append((6, "박아현", "ㅋㅋㅋㅋ아니 어케 이겼노ㅋㅋ 핵씀?", 0))
                self.text.append((0, "주인공", "어케알았지?", 1))
                self.text.append((3, "박아현", "후...이제 마지막 승부만이 남았어", 0))
                self.text.append((0, "주인공", "그래...이번엔 뭐야?", 1))
                self.text.append((8, "박아현", "농구.", 0))
                self.text.append((0, "주인공", "윽,,,농구? 내가 할수있을까...", 1))
                self.text.append((0, "주인공", "아냐, 할수있을까가 아니지. 반드시 이길거야!", 1))
            text_update[3] = 1
        if (server.text_round == 4  and text_update[4] == 0):
            if (server.bask_goal_score >= server.bask_my_score):
                self.text.append((3, "박아현", "헤헷~ 제가 이겻네여?", 0))
                self.text.append((0, "주인공", "젠장...나도 잘했다고 생각했는데!", 1))
            else :
                server.win+=1
                self.text.append((6, "박아현", "엄멍 ㅠㅠ 제가 졌네여 ㅠㅠ", 0))
                self.text.append((0, "주인공", "휴!!", 1))
            self.text.append((7, "박아현",f"그럼 총{server.win}:{3-server.win}...", 0))
            if (server.win>=2):
                self.text.append((0, "주인공", "내...내가 이겼다!!!", 1))
                self.text.append((0, "박아현", "....", 0))
                self.text.append((0, "주인공", "아현아 무슨 생각으로 이런 내기를 한건진 모르겠지만...", 1))
                self.text.append((0, "주인공", "지금 나 제대로 고백할게!", 1))
                self.text.append((0, "주인공", "나 너 진짜 많이 좋아해...너가 어떤말을 하더라도 너무 귀여워!", 1))
                self.text.append((0, "주인공", "나랑 사귀자... 진짜 잘해줄게!", 1))
                self.text.append((4, "박아현", "흥...바보", 0))
                self.text.append((2, "박아현", "내가 더 좋아하거든...", 0))
                self.text.append((0, "주인공", "에엣?! (두근)", 1))
                self.text.append((2, "박아현", "스포츠게임을 하자한것도... 너와 더 오래있고싶어서 그런거였어", 0))
                self.text.append((2, "박아현", "사랑해 인공아! 나! 너 여자친구가 될래!", 0))
                self.text.append((0, "주인공", "아이시떼루 아현쨩!", 1))
                self.text.append((0, "", "해피엔딩~ 즐겨주셔서 감사합니다 이제나가세요 ㅅㄱ",1))

            else :
                self.text.append((0, "주인공", "치욕스럽다... 완전히 졌어", 1))
                self.text.append((0, "박아현", "....", 0))
                self.text.append((0, "주인공", "아현아 정말 스포츠게임이 중요했어...?", 1))
                self.text.append((0, "주인공", "나는 안되는거야...?", 1))
                self.text.append((0, "주인공", "나 너 진짜 많이 좋아한단말야...", 1))
                self.text.append((0, "주인공", "스포츠게임은 나중에 더연습할게...그러니까..제발..응?", 1))
                self.text.append((8, "박아현", "응안돼", 0))
                self.text.append((8, "박아현", "뭔 나도 못이기냐 실망이노", 0))
                self.text.append((0, "주인공", "흑흑...", 1))
                self.text.append((8, "박아현", "우리 걍 좋은 친구로 지내자 ㅅㄱ", 0))
                self.text.append((0, "주인공", "제기랄...제기랄!!!", 1))
                self.text.append((0, "", "배드엔딩~ 즐겨주셔서 감사합니다 이제나가세요 ㅅㄱ", 1))

            text_update[4] = 1

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
            self.skip.draw(710, 530)


    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == 1:
                self.click.play()
                if (event.x>=660 and event.x<=800 and (600-event.y)>=495 and (600-event.y)<=585):self.run= 0
                else:
                    self.text.pop(0)
                    if len(self.text) ==0 :
                        self.run = 0

    def running(self): return self.run


    def pause(self): pass

    def resume(self): pass
