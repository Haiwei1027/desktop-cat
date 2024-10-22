import os
import pygame

class ResourceLoader:
    resources = {}
    
    def load_images(path):
        # load all .png in folder path to resources dictionary
        for filename in os.listdir(path):
            if filename.endswith(".png"):
                image_path = os.path.join(path, filename)
                image_name = os.path.splitext(filename)[0]
                ResourceLoader.resources[image_name] = pygame.image.load(image_path).convert_alpha()
                pass
            pass
        pass
    
    def load_sounds(path):
        for filename in os.listdir(path):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                sound_path = os.path.join(path, filename)
                sound_name = os.path.splitext(filename)[0]
                print(sound_name)
                ResourceLoader.resources[sound_name] = pygame.mixer.Sound(sound_path)
                pass
            pass
        pass
    
    pass