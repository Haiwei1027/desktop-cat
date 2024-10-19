import pygame
from source.entity import Entity
from source.resource_loader import ResourceLoader
from source.animated_sprite import AnimatedSprite
from source.vector import *

class Misty(Entity):
    
    def __init__(self, position=(0,0)):
        animated_sprite = AnimatedSprite(256,256)
        animated_sprite.animation_tracks["sat"] = ["misty_sat"]
        animated_sprite.animation = "sat"
        super().__init__("Misty", animated_sprite,position=position)
        self.action = "sit"
        pass
    
    def misty_sat():
        cat_image = ResourceLoader.resources["i.png"].convert_alpha()
        cat_image = pygame.transform.scale_by(cat_image, 0.4)
        return cat_image

    def misty_sleep():
        cat_image = pygame.image.load("photos/Picture7.png").convert_alpha()
        cat_image = pygame.transform.scale_by(cat_image, 0.05)
        return cat_image

    def misty_move():
        cat_image = pygame.image.load("photos/h.png").convert_alpha()
        cat_image = pygame.transform.scale_by(cat_image, 0.4)
        return cat_image
    
    def update(self):
        super().update()
        self.position = addi(self.position, (0,1))
        pass
    