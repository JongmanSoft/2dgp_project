from pico2d import *


class text_scene:
    def __init__(self):
        self.back_image = []
        self.girl_image = []
        self.text = []
        for i in range (0, 2):
            file_name = "back" + str(i)
            self.back_image.append(load_image(file_name))
        for i in range (0,8):
            file_name = "a" + str(i)
            self.girl_image.append(load_image(file_name))




    def enter(self):
        pass

    def exit(self):
        pass


    def update(self):

        pass

    def draw(self):
        pass

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_MOUSEBUTTONDOWN and event.button == 1:
                pass



    def pause(self): pass

    def resume(self): pass
