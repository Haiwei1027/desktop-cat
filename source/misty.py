import pygame
from source.entity import Entity
from source.resource_loader import ResourceLoader
from source.animated_sprite import AnimatedSprite
from source.vector import *
from source.window_manager import WindowManager
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
            if random.randint(0, 300) == 9:
                self.action = "sat"

        elif self.action == "move":
            self.animated_sprite.animation = "move"
            self.position = addi(self.position, (random.randint(-10,10),random.randint(-10,10)))

            w_width,w_height = WindowManager.getScreenSize()
            top_x,top_y = self.position
            size_x, size_y = self.animated_sprite.size
            bottom_x,bottom_y = addi(self.position, self.animated_sprite.size)
            if top_x < 0:
                self.position = setX(self.position, 0)
            elif bottom_x > w_width:
                self.position = setX(self.position, w_width - size_x)
            if top_y < 0:
                self.position = setY(self.position, 0)
            elif bottom_y > w_height:
                self.position = setY(self.position, w_height - size_y)
            #make misty randomly have a sit
            if random.randint(0, 1000) == 9:
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
            if random.randint(0, 100) == 9:
                self.action = "move"
            #make misty randomly have a sleep
            if random.randint(0, 100) == 9:
                self.action = "sleep"
                #make misty randomly have a sit
            if random.randint(0, 100) == 9:
                self.action = "sat"

        else:
            raise Exception(f"Unknown misty action {self.action}")
        pass

    def click(self):
        if self.action == "sleep":
            self.action = "awake" 
        pass
    pass
    