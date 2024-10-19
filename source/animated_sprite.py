from pygame.surface import Surface
from source.window_manager import WindowManager
from source.resource_loader import ResourceLoader
import pygame
class AnimatedSprite:
    
    def __init__(self, width, height):
        self.surface = Surface((width, height))
        # example format {"misty_sleep":["misty_sleep1","misty_sleep2","misty_sleep3"]}
        self.animation_tracks = {}
        self.animation = ""
        self.pointer = 0
        pass
    
    def update(self):
        # update animation states
        
        # TODO update pointer with looping
        
        
        pass
    
    def render(self):
        # update surface with image
        self.surface.fill(WindowManager.TRANSPARENT)
        track = self.animation_tracks[self.animation]
        img = ResourceLoader.resources[track[self.pointer]]
        w_scale,h_scale = (self.surface.get_width(), self.surface.get_height())
        w_scale /= img.get_width()
        h_scale /= img.get_height()
        bigger_scale = max(w_scale,h_scale)
        img = pygame.transform.scale_by(img, bigger_scale)
        self.surface.blit(img, (0,0))
        pass