from pygame.surface import Surface
from source.window_manager import WindowManager
from source.resource_loader import ResourceLoader
import pygame
import random

class AnimatedSprite:
    
    def __init__(self, width, height):
        self.surface = Surface((width, height))
        self.size = (width, height)
        # example format {"misty_sleep":["misty_sleep1","misty_sleep2","misty_sleep3"]}
        # sprite should correspond with ResourceLoader's loaded resources
        self.animation_tracks = {}
        # current playing animation
        self.animation = ""
        # current frame in the current animation
        self.pointer = 0
        
        self.on_finish_event = []
        pass
    
    def add_track(self, name, timed_track):
        compiled_track = []
        for keyframe in timed_track:
            img,duration = keyframe
            for i in range(duration):
                compiled_track.append(img)
        self.animation_tracks[name] = compiled_track
        pass
    
    def set_animation(self, new_animation):
        self.animation = new_animation
        self.pointer = 0
        pass
    
    def update(self):
        # update animation states
        
        # TODO update pointer with looping
        self.pointer += 1
        track = self.animation_tracks[self.animation]
        
        if self.pointer >= len(track):
            self.pointer = 0
            try:
                for subscriber in self.on_finish_event:
                    subscriber()
            except Exception as e:
                print(e)
        pass
    
    def render(self):
        # make background transparent
        self.surface.fill(WindowManager.TRANSPARENT)
        # select current sprite
        track = self.animation_tracks[self.animation]
        img = ResourceLoader.resources[track[self.pointer]]
        # scale the sprite to fit in the surface
        w_scale,h_scale = (self.surface.get_width(), self.surface.get_height())
        w_scale /= img.get_width()
        h_scale /= img.get_height()
        bigger_scale = 1-max(1-w_scale,1-h_scale)
        img = pygame.transform.scale_by(img, bigger_scale)

        #img = pygame.transform.rotate(img, random.randint(0,50))

        # update surface with image
        self.surface.blit(img, (0,0))
        pass