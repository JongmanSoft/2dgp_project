from pico2d import *


class text_scene:
    def __init__(self):
        self.font = load_font('resource/떡볶이체.ttf',25)

        self.back_image = []
        self.girl_image = []
        self.text = []
        for i in range (0, 2):
            file_name = "back" + str(i) + ".png"
            self.back_image.append(load_image("resource/"+file_name))
        for i in range (0,8):
            file_name = "a" + str(i) + ".png"
            self.girl_image.append(load_image("resource/"+file_name))
        self.window = load_image("resource/"+"text_window.png")
        self.text.append((0,"박아현","여기가 대사"))
        self.text.append((1, "박아현", "두번째 대사"))


    def enter(self):
        pass

    def exit(self):
        pass


    def update(self):

        pass

    def draw(self):
        self.back_image[0].draw(400,300,800,600)
        self.girl_image[self.text[0][0]].draw(400,300)
        self.window.draw(400,100,760,160)
        self.font.draw(70,140,self.text[0][1],(182,23,76))
        self.font.draw(70, 100, self.text[0][2], (0, 23, 76))


    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == 1:
                self.text.pop(0)



    def pause(self): pass

    def resume(self): pass
