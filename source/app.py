import pygame
import time

from source.window_manager import WindowManager
from source.vector import *
from source.resource_loader import ResourceLoader
from source.misty import Misty

from pynput import mouse, keyboard
from threading import Thread, Condition

stop_mouse_condition = Condition()
stop_keyboard_condition = Condition()


def mouse_listener_thread(app):
    with mouse.Listener(on_move=app.on_mouse_move, on_click=app.on_mouse_click) as listener:
        with stop_mouse_condition:
            stop_mouse_condition.wait()
        listener.stop()
    pass

def keyboard_listener_thread(app):
    with keyboard.Listener(on_press=app.on_key_press, on_release=app.on_key_release) as listener:
        with stop_keyboard_condition:
            stop_keyboard_condition.wait()
        listener.stop()
    pass

class PetApp:

    def __init__(self):
        # setup the app and the window
        pygame.init()
        self.screen = pygame.display.set_mode(WindowManager.getScreenSize(), pygame.NOFRAME | pygame.SRCALPHA)
        self.window_manager = WindowManager()
        self.running = True
        self.tick = 0
        self.fps = 30
        self.entities = []
        self.window_manager.makeWindowTransparent()
        
        Thread(target=mouse_listener_thread,args=(self,)).start()
        Thread(target=keyboard_listener_thread,args=(self,)).start()
        
        # load all .png from resources/photos
        ResourceLoader.load_images("resources/photos")
        
        # instance misty and add to entity list
        misty = Misty(position=divi(self.window_manager.display_size,2))
        self.entities.append(misty)
        pass
    def on_mouse_move(self, x,y):
        print(f"{x} {y}")
        pass
    
    def on_mouse_click(self,x,y,button,press_or_release):
        print(f"{x} {y} {button} {press_or_release}")
        pass
    
    def on_key_release(self, keycode):
        print(f"released {keycode}")
        pass
    
    def on_key_press(self, keycode):
        print(f"pressed {keycode}")
        pass
    
    def handle_events(self):
        # handle input events
        # refer to https://www.pygame.org/docs/ref/event.html
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
        pass
    
    def update(self):
        # update window and entities
        if self.tick % 10 == 0:
            self.window_manager.putAppOnTop()
            pass
            
        for entity in self.entities:
            entity.update()
            pass
        pass
    
    def render(self):
        # make background transparent
        self.screen.fill(WindowManager.TRANSPARENT)
        
        # draw all entities
        for entity in self.entities:
            entity.render(self.screen)
            pass
        
        # update the screen
        pygame.display.flip()
        pass
    
    def mainloop(self):
        try:
            while self.running:
                start_time = time.process_time()
                
                self.handle_events()
                self.update()
                self.render()

                # pygame.event.set_grab(True) # Keeps the cursor within the pygame window
                
                # maintains a consistent frame rate
                frame_duration = time.process_time() - start_time
                if frame_duration < 1/self.fps:
                    time.sleep(1/self.fps-frame_duration)
                self.tick += 1
                pass
        except KeyboardInterrupt as e:
            self.quit()
            pass
        pass
    
    def quit(self):
        # stop the app
        pygame.quit()
        with stop_keyboard_condition:
            stop_keyboard_condition.notify()
        with stop_mouse_condition:
            stop_mouse_condition.notify()
        self.running = False
        pass