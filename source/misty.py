import pygame
from source.entity import Entity

class Misty(Entity):
    
    def __init__(self):
        self.action = "sit"
        pass
    
    def misty_sat():
        cat_image = pygame.image.load("photos/i.png").convert_alpha()
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