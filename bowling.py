from pico2d import *



class bowling_scene:
    animation =0
    run = 1
    def __init__(self):
        self.back = load_image('resource/bowling_back.png')

        pass


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
            if event.type == SDL_MOUSEBUTTONDOWN and event.button ==1 :
                pass
            if event.type == SDL_MOUSEMOTION:
                pass
            if event.type == SDL_MOUSEBUTTONUP and event.button ==1:
                pass


    def running(self):
        return self.run

    def pause(self): pass

    def resume(self): pass

