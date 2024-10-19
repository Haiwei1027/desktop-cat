import os
import pygame

class ResourceLoader:
    resources = {}
    
    def __init__(self):
        
        pass
    
    def load_images(path):
        for filename in os.listdir(path):
            if filename.endswith(".png"):
                image_path = os.path.join(path, filename)
                image_name = os.path.splitext(filename)[0]
                ResourceLoader.resources[image_name] = pygame.image.load(image_path)
                pass
            pass
        pass