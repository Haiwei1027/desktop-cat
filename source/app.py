import pygame
import time

from source.window_manager import WindowManager
from source.vector import *

class PetApp:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WindowManager.getScreenSize(), pygame.NOFRAME | pygame.SRCALPHA)
        self.window_manager = WindowManager()
        self.running = True
        self.tick = 0
        self.fps = 30
        self.window_manager.makeWindowTransparent()
        pass
    
    def handle_events(self, event):
        # refer to https://www.pygame.org/docs/ref/event.html
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                button = event.button
            pass
        pass
    
    def mainloop(self):
        while self.running:
            start_time = time.process_time()
            self.screen.fill(self.window_manager.transparent)
            
            pygame.display.flip()
            if self.tick % 10 == 0:
                self.window_manager.putAppOnTop()
            frame_duration = time.process_time() - start_time
            if frame_duration < 1/self.fps:
                time.sleep(1/self.fps-frame_duration)
            self.tick += 1
            pass
        pass
    
    def quit(self):
        pygame.quit()
        self.running = False
        pass