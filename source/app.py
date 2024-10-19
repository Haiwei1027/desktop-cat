import pygame
import time

from source.window_manager import WindowManager
from source.vector import *
from source.resource_loader import ResourceLoader
from source.misty import Misty

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
        
        # load all .png from resources/photos
        ResourceLoader.load_images("resources/photos")
        
        # instance misty and add to entity list
        misty = Misty(position=divi(self.window_manager.display_size,2))
        self.entities.append(misty)
        pass
    
    def handle_events(self):
        # handle input events
        # refer to https://www.pygame.org/docs/ref/event.html
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                print(f"pressed {key}")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                button = event.button
                print(f"pressed {button} at {pos}")
                for entity in self.entities:
                    if entity.contains(pos):
                        entity.click()
                
            pass
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
        
        while self.running:
            start_time = time.process_time()
            
            self.handle_events()
            self.update()
            self.render()
            
            # maintains a consistent frame rate
            frame_duration = time.process_time() - start_time
            if frame_duration < 1/self.fps:
                time.sleep(1/self.fps-frame_duration)
            self.tick += 1
            pass
        pass
    
    def quit(self):
        # stop the app
        pygame.quit()
        self.running = False
        pass