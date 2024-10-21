import pygame
import time

from source.window_manager import WindowManager
from source.vector import *
from source.resource_loader import ResourceLoader
from source.misty import Misty

from source.input_manager import InputManager


class PetApp:

    def __init__(self):
        # setup the app and the window
        pygame.init()
        self.screen = pygame.display.set_mode(WindowManager.getScreenSize(), pygame.NOFRAME | pygame.SRCALPHA)
        self.window_manager = WindowManager()
        self.input_manager = InputManager()
        self.running = True
        self.tick = 0
        self.fps = 30
        self.entities = []
        self.window_manager.makeWindowTransparent()
        
        # load all .png from resources/photos
        ResourceLoader.load_images("resources/photos")
        
        # instance misty and add to entity list
        misty = Misty(position=divi(self.window_manager.display_size,2))
        self.entities.append(misty)
        pass
    
    def update(self):
        # update window and entities
        if self.tick % 10 == 0:
            self.window_manager.putAppOnTop()
            pass
            
        for entity in self.entities:
            entity.update()
            pass
        
        # 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                pass
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
        self.input_manager.stop()
        self.running = False
        pass