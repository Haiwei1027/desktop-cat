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
        animated_sprite.add_track("sat", [("misty_sat",12),("misty_sleep",12)])
        animated_sprite.add_track("move", [("misty_move",24)])
        animated_sprite.add_track("sleep", [("misty_sleep",24)])
        animated_sprite.add_track("awake", [("misty_awake",12)])
        animated_sprite.animation = "sat"
        super().__init__("Misty", animated_sprite,position=position)
        self.action = "sat"
        self.destination = (0,0)
        InputManager.on_mouse_press_event.append(self.on_click)
        self.animated_sprite.on_finish_event.append(self.on_animation_finish)
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
            delta = subi(self.destination, self.position)

            if magi(delta) > 20:
                self.position = addi(self.position, muli(norm(delta),10))
                SoundManager.play_sound("steps")
                w_width,w_height = WindowManager.getScreenSize()
                self.confine((0,0,w_width,w_height))
                #make misty randomly have a sit
                if random.randint(0, 200) == 9:
                    self.action = "sat"
                    SoundManager.stop_sound("steps")
            else:
                self.action = "sat"
                SoundManager.stop_sound("steps")

        elif self.action == "sat":
            self.animated_sprite.animation = "sat"
            SoundManager.play_sound("pur")
            #make misty randomly have a move
            if random.randint(0, 100) == 9:
                self.action = "move"
                self.destination = (random.randrange(0,WindowManager.getScreenSize()[0]), random.randrange(0,WindowManager.getScreenSize()[1]))
                SoundManager.stop_sound("pur")
            #make misty randomly have a sleep
            if random.randint(0, 100) == 9:
                self.action = "sleep"
                SoundManager.stop_sound("pur")

        elif self.action == "awake":
            self.animated_sprite.animation = "awake"
            SoundManager.play_sound("little_meow")
            #make misty randomly have a move
            if random.randint(0, 150) == 9:
                self.action = "move"
                self.destination = (random.randrange(0,WindowManager.getScreenSize()[0]), random.randrange(0,WindowManager.getScreenSize()[1]))
                SoundManager.stop_sound("little_meow")
            #make misty randomly have a sleep
            if random.randint(0, 150) == 9:
                self.action = "sleep"
                SoundManager.stop_sound("little_meow")
                #make misty randomly have a sit
            if random.randint(0, 150) == 9:
                self.action = "sat"
                SoundManager.stop_sound("little_meow")

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
    
    def on_animation_finish(self):
        print("anim finish")
        pass
    
    pass
    