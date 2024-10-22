import pygame
from source.entity import Entity
from source.resource_loader import ResourceLoader
from source.animated_sprite import AnimatedSprite
from source.vector import *
from source.window_manager import WindowManager
from source.input_manager import InputManager
from source.sound_manager import SoundManager
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
        
        InputManager.on_mouse_press_event.append(self.on_click)
        
        pass
    
    def update(self):
        super().update()
        if self.action == "sleep":
            self.animated_sprite.animation = "sleep"
            #make misty randomly have a sit
            SoundManager.play_sound("snore")
            if random.randint(0, 500) == 9:
                self.action = "sat"
                SoundManager.stop_sound("snore")

        elif self.action == "move":
            self.animated_sprite.animation = "move"
            #self.position = addi(self.position, (random.randint(-10,10),random.randint(-10,10)))
            
            w_width,w_height = WindowManager.getScreenSize()
            self.confine((0,0,w_width,w_height))
            #make misty randomly have a sit
            if random.randint(0, 200) == 9:
                self.action = "sat"

        elif self.action == "sat":
            self.animated_sprite.animation = "sat"
            #ResourceLoader.resources["pur"].play()
            #make misty randomly have a move
            if random.randint(0, 100) == 9:
                self.action = "move"
                #ResourceLoader.resources["pur"].play()
            #make misty randomly have a sleep
            if random.randint(0, 100) == 9:
                self.action = "sleep"
                #ResourceLoader.resources["pur"].play()

        elif self.action == "awake":
            self.animated_sprite.animation = "awake"
            #ResourceLoader.resources["little_meow"].play()
            #make misty randomly have a move
            if random.randint(0, 200) == 9:
                self.action = "move"
                #ResourceLoader.resources["little_meow"].stop()
            #make misty randomly have a sleep
            if random.randint(0, 200) == 9:
                self.action = "sleep"
                #ResourceLoader.resources["little_meow"].stop()
                #make misty randomly have a sit
            if random.randint(0, 200) == 9:
                self.action = "sat"
                #ResourceLoader.resources["little_meow"].stop()

        else:
            raise Exception(f"Unknown misty action {self.action}")
        pass
    
    def on_click(self,pos,button):
        if self.contains(pos):
            print("why u click misty")
            if self.action == "sleep":
                self.action = "awake"
                SoundManager.stop_sound("snore")
            pass
        pass
    
    pass
    