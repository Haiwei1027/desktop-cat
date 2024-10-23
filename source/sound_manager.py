import os
from source.resource_loader import ResourceLoader
import pygame

class SoundManager:
    current_sounds = []

    def play_sound (name):

        if name not in SoundManager.current_sounds:
            SoundManager.current_sounds.append(name)
            ResourceLoader.resources.get(name).play()
            #print(SoundManager.current_sounds)
            pass
        pass

    def stop_sound (name):

        if name in SoundManager.current_sounds:
            SoundManager.current_sounds.remove(name)
            ResourceLoader.resources.get(name).stop()
            #print(SoundManager.current_sounds)
            pass
        pass

    pass

