import pygame
from source.entity import Entity
from source.resource_loader import ResourceLoader
from source.animated_sprite import AnimatedSprite
from source.vector import *
import random

class Misty(Entity):
    
    def __init__(self, position=(0,0)):
        animated_sprite = AnimatedSprite(256,256)
        animated_sprite.animation_tracks["sat"] = ["misty_sat"]
        animated_sprite.animation_tracks["move"] = ["misty_move"]
        animated_sprite.animation_tracks["sleep"] = ["misty_sleep"]
        animated_sprite.animation_tracks["awake"] = ["misty_awake"]
        animated_sprite.animation = "sat"
        super().__init__("Misty", animated_sprite,position=position)
        self.action = "sat"
        pass
    
    def update(self):
        super().update()
        if self.action == "sleep":
            self.animated_sprite.animation = "sleep"
            #make misty randomly have a sit
            if random.randint(0, 1000) == 9:
                self.action = "sat"

        elif self.action == "move":
            self.animated_sprite.animation = "move"
            self.position = addi(self.position, (random.randint(-100,100),random.randint(-100,100)))
            #make misty randomly have a sit
            if random.randint(0, 100) == 9:
                self.action = "sat"
        elif self.action == "sat":
            self.animated_sprite.animation = "sat"
            #make misty randomly have a move
            if random.randint(0, 100) == 9:
                self.action = "move"
            #make misty randomly have a sleep
            if random.randint(0, 100) == 9:
                self.action = "sleep"

        elif self.action == "awake":
            self.animated_sprite.animation = "awake"
            #make misty randomly have a move
            if random.randint(0, 300) == 9:
                self.action = "move"
            #make misty randomly have a sleep
            if random.randint(0, 300) == 9:
                self.action = "sleep"
                #make misty randomly have a sit
            if random.randint(0, 300) == 9:
                self.action = "sat"

        else:
            raise Exception(f"Unknown misty action {self.action}")
        pass
    
    def click(self):
        if self.action == "sleep":
            self.action = "awake" 
        pass
    pass
    